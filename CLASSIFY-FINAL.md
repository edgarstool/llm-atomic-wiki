# CLASSIFY-FINAL — official docs ingest 2026-08-29/31

Rule: SKILL = repeatable ops (CLI/setup/pitfalls). WIKI = concepts/architecture/spec.
Skill files go to `V:\\tools\\skills\\<name>\\SKILL.md` (not Hermes home).

| Product | Verdict | Where |
|---------|---------|--------|
| Logto | **WIKI** now; skill later if we operate Logto Cloud/OSS daily | atoms/identity |
| Descope | **WIKI** + **extend existing** `V:\\tools\\skills\\descope-*` | do not fork new descope root |
| 1Password | **WIKI** + keep existing 1password skill (op/Environments MCP) | no duplicate |
| Hermes Agent | **WIKI** + existing `hermes-dev` / bundled hermes-agent | no new skill |
| OpenClaw | **WIKI**; ops skill only if V:\\tools\\skills lacks one | atoms/hermes |
| Honcho | **WIKI** + **extend** honcho-cli / honcho-integration / honcho-memory | |
| QMD | **WIKI** + **extend** `qmd-local`; official skill is macos/linux | Windows gap is a pitfall |
| Linear | **WIKI** + **extend** `linear` | |
| Factory AI | **WIKI**; **new skill later** at `V:\\tools\\skills\\factory-droid` if we run `droid` daily | not this pass |
| Vercel | **WIKI**; skill later if deploy CLI is a recurring runbook | |
| MCP 2.0 | **WIKI** (spec). Ops stay in existing MCP skills | latest spec 2026-07-28 |
| Inkbox | **WIKI** + **new skill next** `V:\\tools\\skills\\inkbox` (`hermes plugins install` / `hermes inkbox setup`) | identified as inkbox.ai |

This pass: hub pages ingested, not full-site crawl. Subagent batch timed out at 120s (see log).

## 2026-09-21 Descope full-site compile

- Raw: `raw/articles/descope-official/` (1204 pages + 41 stubs) via `scripts/ingest-descope-docs.py`
- Atoms: 15 new under `atoms/identity/2026-09-21-descope-*.md` (plus prior 2026-08-29/31 Descope atoms)
- Wiki: `identity-descope-overview`, `flows`, `sessions`, `auth-methods`, `authorization`, `agentic-hub`, `federation`, `management`; updated `building-applications` + `auth-vendors`
- Out of scope this pass: per-endpoint API Reference atoms; new `descope-*` skill roots (extend existing only)