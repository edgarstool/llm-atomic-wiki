import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import importlib.util

MODULE = Path(__file__).resolve().parents[1] / 'scripts' / 'knowledge_raw_import.py'


def load():
    spec = importlib.util.spec_from_file_location('knowledge_raw_import', MODULE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class KnowledgeRawImportTests(unittest.TestCase):
    def test_expected_sha_prevents_any_unverified_write(self):
        mod = load()
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaisesRegex(ValueError, 'SHA-256 mismatch'):
                mod.materialize_raw('# QMD\n', '0' * 64, 'knowledge://hermes-wiki/incoming/qmd.md', Path(temp))
            self.assertEqual(list(Path(temp).iterdir()), [])

    def test_exact_bytes_manifest_and_repeat_is_idempotent(self):
        mod = load()
        text = '# QMD 官方說明\n\nVerified source.\n'
        expected = hashlib.sha256(text.encode()).hexdigest()
        with tempfile.TemporaryDirectory() as temp:
            path = mod.materialize_raw(text, expected, 'knowledge://hermes-wiki/incoming/qmd.md', Path(temp))
            self.assertEqual(path.read_bytes(), text.encode())
            meta = json.loads(path.with_suffix('.json').read_text())
            self.assertEqual(meta['source_uri'], 'knowledge://hermes-wiki/incoming/qmd.md')
            self.assertEqual(meta['sha256'], expected)
            original_meta = path.with_suffix('.json').read_bytes()
            again = mod.materialize_raw(text, expected, 'knowledge://hermes-wiki/incoming/qmd.md', Path(temp))
            self.assertEqual(again, path)
            self.assertEqual(original_meta, path.with_suffix('.json').read_bytes())
            self.assertEqual(len(list(Path(temp).iterdir())), 2)

    def test_reject_rebind_different_source_to_same_sha(self):
        mod = load()
        text = 'some content'
        expected = hashlib.sha256(text.encode()).hexdigest()
        with tempfile.TemporaryDirectory() as temp:
            mod.materialize_raw(text, expected, 'knowledge://hermes-wiki/a', Path(temp))
            with self.assertRaisesRegex(ValueError, 'different source'):
                mod.materialize_raw(text, expected, 'knowledge://hermes-wiki/b', Path(temp))

    def test_public_http_mcp_fails_closed(self):
        mod = load()
        for url in ['http://knowledge-mcp.edgars.tools/mcp', 'file:///tmp/mcp', 'https://user:pass@example.com/mcp']:
            with self.assertRaises(ValueError):
                mod.validate_mcp_url(url)
        self.assertEqual(mod.validate_mcp_url('http://127.0.0.1:7979/internal/mcp'), 'http://127.0.0.1:7979/internal/mcp')

    def test_mcp_result_accepts_structured_and_legacy_text(self):
        mod = load()
        uri = 'knowledge://hermes-wiki/incoming/qmd.md'
        self.assertEqual(mod.parse_mcp_read({'result': {'structuredContent': {'uri': uri, 'content': 'body'}}}, uri), 'body')
        legacy = {'result': {'content': [{'type': 'text', 'text': json.dumps({'uri': uri, 'content': 'body'})}]}}
        self.assertEqual(mod.parse_mcp_read(legacy, uri), 'body')
        with self.assertRaises(ValueError):
            mod.parse_mcp_read({'result': {'structuredContent': {'uri': 'knowledge://other/no', 'content': 'wrong'}}}, uri)


if __name__ == '__main__':
    unittest.main()
