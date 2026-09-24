---
title: "Pricing and Free Limits (notes)"
source_url: "https://www.jetbrains.com/youtrack/buy/"
fetched_at: "2026-09-22 08:36 Asia/Taipei"
product: YouTrack
---

# Pricing and Free Limits (notes)

**Constraint for EDGAR-OS:** $0 default — do **not** purchase paid YouTrack plans unless Edgar explicitly approves later.

## Cloud Free (primary recommendation)

From JetBrains Cloud help (fetched 2026-09-22 08:36 Asia/Taipei):

- **Users:** up to **10** standard users on an unlimited free basis
- **Helpdesk agents:** up to **3** free
- **Helpdesk reporters:** unlimited (helpdesk-license.html)
- **Storage:** **30 GB** for free plan and 14-day trial per storage-limits.html; also described as **3 GB per user** covered by the subscription
- **Hostname:** `{site}.youtrack.cloud`
- Register: documented in new-youtrack-cloud-instances.html

Sources:

- https://www.jetbrains.com/help/youtrack/cloud/new-youtrack-cloud-instances.html
- https://www.jetbrains.com/help/youtrack/cloud/switching-subscription-plans.html
- https://www.jetbrains.com/help/youtrack/cloud/storage-limits.html
- https://www.jetbrains.com/help/youtrack/cloud/helpdesk-license.html
- https://www.jetbrains.com/youtrack/buy/

## Cloud Trial (optional evaluation only)

- 14 days, up to 100 users / 50 agents
- No credit card required (per switching-subscription-plans)
- Can revert to Free after trial

## Server Free

Buy page SKUs reference **YouTrack Server** packs with **10 free users** (commercial for additional users/agents). Self-host implies Docker host, backups, upgrades, TLS — cost in **time/ops**, not necessarily license if staying ≤10 users.

Sources:

- https://www.jetbrains.com/youtrack/buy/
- https://www.jetbrains.com/help/youtrack/server/manage-youtrack-server-license.html
- https://www.jetbrains.com/help/youtrack/server/youtrack-docker-installation.html

## EDGAR decision

Prefer **Cloud Free**. Revisit Server only if Cloud free limits or hosting model fail requirements.
