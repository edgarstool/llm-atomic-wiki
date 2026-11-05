# Knowledge → LLM Wiki RAW importer

This is a real, dependency-free adapter between an authorized **Edgar's Knowledge MCP** source and the **private, gitignored `raw/` layer** of this repository.

It is not a compiler and does not create atoms, compiled wiki pages, embeddings, or Honcho messages. The existing `scripts/gen-index.sh` and `scripts/lint.sh` operate **after** an agent has compiled vetted atoms into Wiki pages.

## Preconditions

- Use the existing authenticated Knowledge MCP `read` action and an existing `knowledge://...` source URI.
- Obtain the original source's expected 64-character SHA-256 from a separately verified Knowledge write/read receipt, not from the same response being imported.
- Set `EDGAR_KNOWLEDGE_BEARER_TOKEN` in the approved executor's secret environment for the public HTTPS URL. Do **not** put any token in Git, command-line arguments, logs, atom metadata, or the Wiki.
- A localhost HTTP MCP address is accepted only for an authorized loopback execution on the existing Knowledge host. Do not expose `/internal/mcp` on a public interface or bypass its authorization boundary.
- The public ChatGPT Knowledge connector and the user-approved Factory executor must pass their own connection and permissions acceptance before real remote imports.

## Run (authorized executor only)

```bash
python3 scripts/knowledge_raw_import.py \
  --uri 'knowledge://hermes-wiki/incoming/<verified-source>.md' \
  --sha256 '<verified-64-character-sha256>'
```

Optional `--mcp-url` is useful for testing an already-authorized MCP endpoint. With an external hostname, only HTTPS is accepted and a bearer secret is required. `--dest` defaults to `raw/knowledge/`, which is gitignored.

The import checks the **exact response URI** and **SHA-256 before writing**, writes `raw/knowledge/<sha>.md` byte-identically, and creates a private, local `<sha>.json` manifest with the source URI, hash, size, timestamp, and explicit `raw-verified; not compiled` status. Repeat imports of the same source/hash are idempotent. A file collision, changed content or URI mismatch fails closed.

The source may be UTF-8; non-text binary documents need a separate approved conversion path. The Knowledge MCP `read` response must preserve the source's exact newline bytes for hash matching. The importer cannot repair upstream CRLF normalization.

## Verification

```bash
python3 -m unittest discover -s tests -p 'test_knowledge_raw_import.py' -v
```

Acceptance is **not just saving files**:

1. Confirm the official original and its independent Knowledge receipt/hash.
2. Confirm the authenticated external MCP `read` responds with the same URI and content hash.
3. Confirm private `raw/knowledge/<sha>.md` and manifest, repeat idempotency, no token/content in Git.
4. Only then run the existing LLM Wiki workflow **Raw → one-claim Atoms → Wiki → deterministic lint → semantic lint → publish/readback**.
5. Keep original raw unchanged. Claims/atoms include source identifiers; derived Wiki pages must link to their atoms.

Status 2026-11-02: source implementation and isolated tests passed, but real Factory E2B + public authenticated MCP import, full atom extraction/compilation and published Knowledge readback are **NOT VERIFIED**. Do not claim Wiki completion or deploy a new service from this branch. Zero new recurring cost.
