---
title: "Cloud vs Server — EDGAR decision notes"
source_url: "https://www.jetbrains.com/help/youtrack/server/youtrack-docker-installation.html"
fetched_at: "2026-09-22 08:36 Asia/Taipei"
product: YouTrack
---

# Cloud vs Server — EDGAR decision notes

Synthesized for EDGAR-OS (not a verbatim JetBrains page). Official install/ops bodies live alongside this file.

## Recommendation

**YouTrack Cloud Free** for one-person EDGAR-OS Workbench tracking.

## Why Cloud

- $0 for ≤10 users / 3 agents / ~30 GB storage (verify in License Details UI)
- No Docker/TLS/backup duty
- Same product surface for issues, boards, workflows, REST, MCP tools, GitHub integration
- Fast cutover

## When Server wins

- Hard requirement for self-hosted data / air-gap
- Willing to run `jetbrains/youtrack` Docker, backups, upgrades (see `youtrack-docker-installation.md`)

## Migration path

Cloud ↔ Server migration guides crawled under this folder (`migrate-from-cloud-to-server.md`, `migrate-from-server-to-cloud.md`). Prefer picking Cloud first; migrate later only if needed.

## Non-goals

- Do not host Knowledge corpus in either edition for EDGAR-OS
- Do not buy commercial seats on day one

Sources touched: Cloud license/storage docs, Server Docker install, https://www.jetbrains.com/youtrack/buy/
