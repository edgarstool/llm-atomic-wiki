# Hermes project context — Hermes-Wiki

This directory is the **Hermes LLM knowledge vault** for Edgar (EDGAR-OS).

## Read first

1. `SCHEMA.md` — boundaries vs human Obsidian / Agent-KB / Honcho
2. `CLAUDE.md` — formal atom/wiki operations (from llm-atomic-wiki)
3. `METHODOLOGY.md` — six-phase pipeline
4. `index.md` + tail of `log.md`

## Do

- Ingest into `raw/`, extract immutable atoms under `atoms/<branch>/`, compile to `wiki/`
- Keep secrets out
- Stay inside this vault root (`WIKI_PATH`)

## Do not

- Write into `G:\Obsidian\Edgar'sObsidianVault` from wiki jobs
- Treat wiki pages as source of truth (atoms are)
- Dump Agent-KB rules here as a second constitution
