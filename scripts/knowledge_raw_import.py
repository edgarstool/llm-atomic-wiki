#!/usr/bin/env python3
"""Read an authenticated Knowledge RAW document into the private LLM Wiki raw layer.

This does NOT compile atoms/wiki or contact Honcho. Source bytes are verified
against a caller-provided SHA-256 before any private file is created.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import tempfile
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

DEFAULT_URL = 'https://knowledge-mcp.edgars.tools/mcp'
DEFAULT_DEST = Path(__file__).resolve().parents[1] / 'raw' / 'knowledge'
MAX_RESPONSE_BYTES = 30 * 1024 * 1024


def validate_mcp_url(url: str) -> str:
    parsed = urlsplit(url)
    if parsed.username or parsed.password or parsed.fragment or parsed.query:
        raise ValueError('MCP URL must not contain user credentials, query or fragment')
    if not parsed.hostname:
        raise ValueError('MCP URL must contain hostname')
    is_local = parsed.hostname.lower() in {'127.0.0.1', '::1', 'localhost'}
    if parsed.scheme != 'https' and not (is_local and parsed.scheme == 'http'):
        raise ValueError('MCP URL requires HTTPS except loopback')
    if not parsed.path.endswith('/mcp'):
        raise ValueError('MCP URL must point at an MCP endpoint')
    return url


def parse_mcp_read(response: dict, expected_uri: str) -> str:
    if response.get('error'):
        raise ValueError('Knowledge MCP RPC returned an error')
    result = response.get('result') or {}
    if result.get('isError'):
        raise ValueError('Knowledge MCP tool returned an error')
    data = result.get('structuredContent')
    if not isinstance(data, dict):
        messages = result.get('content') or []
        if not messages or messages[0].get('type') != 'text':
            raise ValueError('Knowledge MCP returned no readable document')
        try:
            data = json.loads(messages[0].get('text', ''))
        except (TypeError, ValueError) as exc:
            raise ValueError('Knowledge MCP response was not JSON') from exc
    if not isinstance(data, dict) or data.get('uri') != expected_uri:
        raise ValueError('Knowledge MCP returned unexpected source URI')
    content = data.get('content')
    if not isinstance(content, str):
        raise ValueError('Knowledge MCP returned no text content')
    return content


def read_knowledge(uri: str, mcp_url: str, bearer: str = '') -> str:
    endpoint = validate_mcp_url(mcp_url)
    if not uri.startswith('knowledge://'):
        raise ValueError('Source must be a knowledge:// URI')
    host = urlsplit(endpoint).hostname or ''
    if host.lower() not in {'127.0.0.1', '::1', 'localhost'} and not bearer:
        raise ValueError('A pre-authorized bearer token is required for the public MCP URL')
    rpc = {'jsonrpc': '2.0', 'id': 'wiki-raw-import', 'method': 'tools/call',
           'params': {'name': 'read', 'arguments': {'uri': uri}}}
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    if bearer:
        headers['Authorization'] = 'Bearer ' + bearer
    request = urllib.request.Request(endpoint, data=json.dumps(rpc).encode('utf-8'),
                                     method='POST', headers=headers)
    with urllib.request.urlopen(request, timeout=25) as response:
        raw = response.read(MAX_RESPONSE_BYTES + 1)
    if len(raw) > MAX_RESPONSE_BYTES:
        raise ValueError('Knowledge MCP response exceeded supported size')
    try:
        return parse_mcp_read(json.loads(raw.decode('utf-8')), uri)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError('Knowledge MCP response cannot be decoded') from exc


def materialize_raw(content: str, expected_sha256: str, source_uri: str, destination: Path) -> Path:
    if not isinstance(content, str) or not source_uri.startswith('knowledge://'):
        raise ValueError('Source content and knowledge:// URI are required')
    if not re.fullmatch(r'[0-9a-f]{64}', expected_sha256):
        raise ValueError('Expected SHA-256 must be 64 lowercase hex characters')
    encoded = content.encode('utf-8')
    actual = hashlib.sha256(encoded).hexdigest()
    if actual != expected_sha256:
        raise ValueError('SHA-256 mismatch: refusing to persist unverified raw')
    destination = Path(destination)
    path = destination / (actual + '.md')
    manifest = destination / (actual + '.json')
    if path.exists() or manifest.exists():
        if not path.is_file() or not manifest.is_file() or path.read_bytes() != encoded:
            raise ValueError('Existing raw document or manifest conflicts')
        existing = json.loads(manifest.read_text(encoding='utf-8'))
        if existing.get('source_uri') != source_uri or existing.get('sha256') != actual:
            raise ValueError('Existing verified raw has a different source')
        return path
    destination.mkdir(parents=True, exist_ok=True)
    metadata = {'schema': 'edgar-llm-wiki-raw/v1', 'source_uri': source_uri,
                'sha256': actual, 'bytes': len(encoded),
                'imported_at': datetime.now(timezone.utc).isoformat(),
                'state': 'raw-verified; not compiled'}
    for target, data in [(path, encoded), (manifest, (json.dumps(metadata, ensure_ascii=False, indent=2) + '\n').encode())]:
        fd, name = tempfile.mkstemp(dir=destination, prefix='.raw-', suffix='.tmp')
        try:
            os.fchmod(fd, 0o600)
            with os.fdopen(fd, 'wb') as f:
                f.write(data)
                f.flush()
                os.fsync(f.fileno())
            os.replace(name, target)
        finally:
            if os.path.exists(name):
                os.unlink(name)
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--uri', required=True, help='Exact knowledge:// source URI')
    parser.add_argument('--sha256', required=True, help='Expected original raw SHA-256')
    parser.add_argument('--mcp-url', default=os.environ.get('EDGAR_KNOWLEDGE_MCP_URL', DEFAULT_URL))
    parser.add_argument('--dest', type=Path, default=DEFAULT_DEST)
    args = parser.parse_args()
    bearer = os.environ.get('EDGAR_KNOWLEDGE_BEARER_TOKEN', '')
    data = read_knowledge(args.uri, args.mcp_url, bearer)
    path = materialize_raw(data, args.sha256, args.uri, args.dest)
    print(json.dumps({'state': 'RAW_READBACK_PASS', 'file': str(path), 'sha256': args.sha256,
                      'atoms': 'NOT_RUN', 'wiki': 'NOT_RUN'}))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
