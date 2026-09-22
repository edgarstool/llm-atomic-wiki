# Agent instructions — Hermes-Wiki

Operate this repo as **llm-atomic-wiki**.

- Spec: `CLAUDE.md`
- Pipeline: `METHODOLOGY.md`
- Local schema / EDGAR boundaries: `SCHEMA.md`
- Navigation: `index.md`
- History: `log.md` (append-only)

Flow: `Ingest → atoms → Compile wiki → gen-index → lint → Query`.

Human vault and Agent-KB are out of scope for writes.
