---
title: YouTrack Docs Index (Hermes-Wiki)
fetched_at: "2026-09-22 08:36 Asia/Taipei"
scope: Workbench issue tracking only (NOT Agent-KB / Knowledge corpus)
vault_target: "G:\\Obsidian\\Hermes-Wiki\\youtrack\\"
---

# YouTrack — Hermes-Wiki Index

Crawl for **EDGAR-OS Workbench** tracker adoption. Knowledge body stays outside YouTrack.

- **Fetched:** 2026-09-22 08:36 Asia/Taipei
- **Sources:**
  - Cloud llms.txt: https://www.jetbrains.com/help/youtrack/cloud/llms.txt
  - Server llms.txt: https://www.jetbrains.com/help/youtrack/server/llms.txt
  - Dev portal llms.txt: https://www.jetbrains.com/help/youtrack/devportal/llms.txt
  - Pricing: https://www.jetbrains.com/youtrack/buy/
- **Crawled bodies:** 80 markdown pages (high-value subset; full TOC linked below / in raw llms)
- **Ops:** [[ops/DEPLOY-PLAN]] · [[ops/SKILL-DRAFT]]

## Free-tier snapshot (verify on buy page before commit)

| Edition | Free limits | Source |
|--------|-------------|--------|
| **YouTrack Cloud Free** | Up to **10** standard users + **3** helpdesk agents; storage **30 GB** (docs also state 3 GB/user; free/trial capped at 30 GB) | https://www.jetbrains.com/help/youtrack/cloud/new-youtrack-cloud-instances.html · https://www.jetbrains.com/help/youtrack/cloud/switching-subscription-plans.html · https://www.jetbrains.com/help/youtrack/cloud/storage-limits.html |
| **YouTrack Cloud Trial** | 14 days · up to 100 users / 50 agents · storage notes: storage-limits says free+trial **30 GB**; license page mentions trial disk **100 GB** — **reconcile in UI at signup** | same + storage-limits / switching-subscription-plans |
| **YouTrack Server Free** | **10** free users (paid agents beyond free pack per buy page SKUs) | https://www.jetbrains.com/youtrack/buy/ · server license docs |

**$0 default:** Prefer Cloud Free for one-person EDGAR-OS. Do **not** purchase commercial plans unless Edgar decides later.

## Authority rules (EDGAR-OS)

1. Scope = **Workbench issue tracking only**. Do **not** migrate Agent-KB / Knowledge corpus into YouTrack.
2. Until YouTrack is live: **GitHub remains Current authority** for Workbench code.
3. **No dual-write** with Linear. Switch tracker → YouTrack (single Current once cutover completes).
4. Linear is not dual Current; do not keep parallel issue truth.

## Layout

```
youtrack/
  00-index.md          ← this file
  cloud/               ← Cloud admin + user topics
  server/              ← install / ops / migration
  api/                 ← REST + MCP + apps + workflows
  ops/DEPLOY-PLAN.md   ← Edgar-facing plan (zh-TW)
  ops/SKILL-DRAFT.md   ← Skill recipe for parent update_state
  raw/                 ← llms.txt + crawl metadata
```

## Crawled pages


### cloud/

- [About YouTrack Cloud](cloud/about-youtrack-cloud.md) — `5492` B — https://www.jetbrains.com/help/youtrack/cloud/about-youtrack-cloud.html
- [Access Management](cloud/access-management.md) — `2096` B — https://www.jetbrains.com/help/youtrack/cloud/access-management.html
- [Apps](cloud/admin-apps.md) — `1375` B — https://www.jetbrains.com/help/youtrack/cloud/admin-apps.html
- [Agile Boards](cloud/agile-board.md) — `2828` B — https://www.jetbrains.com/help/youtrack/cloud/agile-board.html
- [Advanced Search](cloud/attribute-based-search.md) — `16114` B — https://www.jetbrains.com/help/youtrack/cloud/attribute-based-search.html
- [Command Reference](cloud/command-reference.md) — `15362` B — https://www.jetbrains.com/help/youtrack/cloud/command-reference.html
- [Update Issues with Commands](cloud/commands.md) — `9031` B — https://www.jetbrains.com/help/youtrack/cloud/commands.html
- [Configure a Project](cloud/configuring-a-project.md) — `12181` B — https://www.jetbrains.com/help/youtrack/cloud/configuring-a-project.html
- [Create and Update Issues](cloud/create-and-edit-issues.md) — `7200` B — https://www.jetbrains.com/help/youtrack/cloud/create-and-edit-issues.html
- [Create an Agile Board](cloud/create-new-board.md) — `6809` B — https://www.jetbrains.com/help/youtrack/cloud/create-new-board.html
- [Create a Project](cloud/create-new-project.md) — `4858` B — https://www.jetbrains.com/help/youtrack/cloud/create-new-project.html
- [Default Workflows](cloud/default-workflows.md) — `2212` B — https://www.jetbrains.com/help/youtrack/cloud/default-workflows.html
- [Get Started with Agile Boards](cloud/getting-started-with-agile-board.md) — `1240` B — https://www.jetbrains.com/help/youtrack/cloud/getting-started-with-agile-board.html
- [Getting Started](cloud/getting-started-with-youtrack.md) — `8258` B — https://www.jetbrains.com/help/youtrack/cloud/getting-started-with-youtrack.html
- [Helpdesk License](cloud/helpdesk-license.md) — `1033` B — https://www.jetbrains.com/help/youtrack/cloud/helpdesk-license.html
- [Import from CSV](cloud/import-from-csv.md) — `24555` B — https://www.jetbrains.com/help/youtrack/cloud/import-from-csv.html
- [Import from GitHub](cloud/import-from-github.md) — `10533` B — https://www.jetbrains.com/help/youtrack/cloud/import-from-github.html
- [Imports](cloud/imports.md) — `1552` B — https://www.jetbrains.com/help/youtrack/cloud/imports.html
- [Integrate with GitHub](cloud/integrate-project-with-github.md) — `20659` B — https://www.jetbrains.com/help/youtrack/cloud/integrate-project-with-github.html
- [Introduction to YouTrack](cloud/introduction-to-youtrack-cloud.md) — `607` B — https://www.jetbrains.com/help/youtrack/cloud/introduction-to-youtrack-cloud.html
- [Issues](cloud/issues.md) — `1666` B — https://www.jetbrains.com/help/youtrack/cloud/issues.html
- [Manage Permanent Tokens](cloud/manage-permanent-token.md) — `5090` B — https://www.jetbrains.com/help/youtrack/cloud/manage-permanent-token.html
- [Manage Project Members and Access](cloud/manage-project-access.md) — `22254` B — https://www.jetbrains.com/help/youtrack/cloud/manage-project-access.html
- [Projects](cloud/managing-projects.md) — `2527` B — https://www.jetbrains.com/help/youtrack/cloud/managing-projects.html
- [Users](cloud/managing-users.md) — `2337` B — https://www.jetbrains.com/help/youtrack/cloud/managing-users.html
- [New Instances](cloud/new-youtrack-cloud-instances.md) — `6919` B — https://www.jetbrains.com/help/youtrack/cloud/new-youtrack-cloud-instances.html
- [Project Admin Quick Start Guide](cloud/projects-quick-start-guide.md) — `3029` B — https://www.jetbrains.com/help/youtrack/cloud/projects-quick-start-guide.html
- [Issue Quick Start Guide](cloud/reporting-an-issue.md) — `4067` B — https://www.jetbrains.com/help/youtrack/cloud/reporting-an-issue.html
- [Search Query Reference](cloud/search-and-command-attributes.md) — `50689` B — https://www.jetbrains.com/help/youtrack/cloud/search-and-command-attributes.html
- [Issue Search](cloud/search-for-issues.md) — `2800` B — https://www.jetbrains.com/help/youtrack/cloud/search-for-issues.html
- [Security](cloud/security.md) — `8743` B — https://www.jetbrains.com/help/youtrack/cloud/security.html
- [Storage Limits](cloud/storage-limits.md) — `1810` B — https://www.jetbrains.com/help/youtrack/cloud/storage-limits.html
- [Managing Your License](cloud/switching-subscription-plans.md) — `7044` B — https://www.jetbrains.com/help/youtrack/cloud/switching-subscription-plans.html
- [System Admin Quick Start Guide](cloud/system-admins-quick-start.md) — `6953` B — https://www.jetbrains.com/help/youtrack/cloud/system-admins-quick-start.html
- [Transition from GitHub Issues](cloud/transition-from-github-issues.md) — `13835` B — https://www.jetbrains.com/help/youtrack/cloud/transition-from-github-issues.html
- [Transitioning to YouTrack from Other Tools](cloud/transition-to-youtrack.md) — `2998` B — https://www.jetbrains.com/help/youtrack/cloud/transition-to-youtrack.html
- [New User Quick Start Guide](cloud/user-quick-start-guide.md) — `1985` B — https://www.jetbrains.com/help/youtrack/cloud/user-quick-start-guide.html
- [Workflow Constructor](cloud/workflow-constructor.md) — `15233` B — https://www.jetbrains.com/help/youtrack/cloud/workflow-constructor.html
- [Workflows](cloud/workflow-guide.md) — `5130` B — https://www.jetbrains.com/help/youtrack/cloud/workflow-guide.html
- [Workflow Tutorial](cloud/workflow-tutorial.md) — `17872` B — https://www.jetbrains.com/help/youtrack/cloud/workflow-tutorial.html
- [Data Center Locations](cloud/youtrack-cloud-data-center-locations.md) — `2132` B — https://www.jetbrains.com/help/youtrack/cloud/youtrack-cloud-data-center-locations.html
- [YouTrack Cloud Database Backups](cloud/youtrack-cloud-database-backups.md) — `3026` B — https://www.jetbrains.com/help/youtrack/cloud/youtrack-cloud-database-backups.html

### server/

- [Database Backup](server/back-up-the-database.md) — `6136` B — https://www.jetbrains.com/help/youtrack/server/back-up-the-database.html
- [Installation and Upgrade](server/installation-and-upgrade.md) — `2653` B — https://www.jetbrains.com/help/youtrack/server/installation-and-upgrade.html
- [Introduction to YouTrack Server](server/introduction-to-youtrack-server.md) — `620` B — https://www.jetbrains.com/help/youtrack/server/introduction-to-youtrack-server.html
- [License Details](server/license-details.md) — `3246` B — https://www.jetbrains.com/help/youtrack/server/license-details.html
- [Managing Your YouTrack Server License](server/manage-youtrack-server-license.md) — `5785` B — https://www.jetbrains.com/help/youtrack/server/manage-youtrack-server-license.html
- [Migrate from Cloud to Server](server/migrate-from-cloud-to-server.md) — `6876` B — https://www.jetbrains.com/help/youtrack/server/migrate-from-cloud-to-server.html
- [Migrate from Server to Cloud](server/migrate-from-server-to-cloud.md) — `4115` B — https://www.jetbrains.com/help/youtrack/server/migrate-from-server-to-cloud.html
- [YouTrack to YouTrack Migration](server/migrating-to-youtrack.md) — `1748` B — https://www.jetbrains.com/help/youtrack/server/migrating-to-youtrack.html
- [Restore Docker Installation](server/restore-docker-image-installation.md) — `5007` B — https://www.jetbrains.com/help/youtrack/server/restore-docker-image-installation.html
- [Run Docker as a Service](server/run-docker-container-as-service.md) — `5307` B — https://www.jetbrains.com/help/youtrack/server/run-docker-container-as-service.html
- [Safeguard Your Installation](server/secure-your-installation.md) — `20894` B — https://www.jetbrains.com/help/youtrack/server/secure-your-installation.html
- [Upgrade with Docker](server/upgrade-with-docker-image.md) — `18537` B — https://www.jetbrains.com/help/youtrack/server/upgrade-with-docker-image.html
- [Docker Installation](server/youtrack-docker-installation.md) — `23207` B — https://www.jetbrains.com/help/youtrack/server/youtrack-docker-installation.html
- [About YouTrack Server](server/youtrack-server-faq.md) — `2408` B — https://www.jetbrains.com/help/youtrack/server/youtrack-server-faq.html
- [Supported Environments](server/youtrack-supported-environments.md) — `6323` B — https://www.jetbrains.com/help/youtrack/server/youtrack-supported-environments.html

### api/

- [JavaScript Workflow Quick Start](api/Quick-Start-Guide-Workflows-JS.md) — `19588` B — https://www.jetbrains.com/help/youtrack/devportal/Quick-Start-Guide-Workflows-JS.html
- [MCP Tools](api/ai-tools.md) — `3427` B — https://www.jetbrains.com/help/youtrack/devportal/ai-tools.html
- [Fields Syntax](api/api-fields-syntax.md) — `4583` B — https://www.jetbrains.com/help/youtrack/devportal/api-fields-syntax.html
- [Get Started with REST API](api/api-getting-started.md) — `1644` B — https://www.jetbrains.com/help/youtrack/devportal/api-getting-started.html
- [Update Issue Custom Fields](api/api-how-to-update-custom-fields-values.md) — `4066` B — https://www.jetbrains.com/help/youtrack/devportal/api-how-to-update-custom-fields-values.html
- [Create an Issue and Set Custom Fields](api/api-howto-create-issue-with-fields.md) — `6700` B — https://www.jetbrains.com/help/youtrack/devportal/api-howto-create-issue-with-fields.html
- [Create an Issue (API)](api/api-howto-create-issue.md) — `1979` B — https://www.jetbrains.com/help/youtrack/devportal/api-howto-create-issue.html
- [Log in to YouTrack (API)](api/api-log-in-to-youtrack.md) — `1448` B — https://www.jetbrains.com/help/youtrack/devportal/api-log-in-to-youtrack.html
- [Query Syntax](api/api-query-syntax.md) — `4020` B — https://www.jetbrains.com/help/youtrack/devportal/api-query-syntax.html
- [REST API URL and Endpoints](api/api-url-and-endpoints.md) — `4392` B — https://www.jetbrains.com/help/youtrack/devportal/api-url-and-endpoints.html
- [Apply Commands to Issues](api/api-usecase-commands.md) — `4248` B — https://www.jetbrains.com/help/youtrack/devportal/api-usecase-commands.html
- [YouTrack JavaScript Ecosystem](api/apps-documentation.md) — `1917` B — https://www.jetbrains.com/help/youtrack/devportal/apps-documentation.html
- [Apps](api/apps-get-started.md) — `4329` B — https://www.jetbrains.com/help/youtrack/devportal/apps-get-started.html
- [Permanent Token Authorization](api/authentication-with-permanent-token.md) — `3279` B — https://www.jetbrains.com/help/youtrack/devportal/authentication-with-permanent-token.html
- [Custom MCP Tools](api/custom-ai-tools.md) — `7654` B — https://www.jetbrains.com/help/youtrack/devportal/custom-ai-tools.html
- [Predefined MCP Tools](api/predefined-ai-tools.md) — `9981` B — https://www.jetbrains.com/help/youtrack/devportal/predefined-ai-tools.html
- [YouTrack REST API](api/youtrack-rest-api.md) — `3586` B — https://www.jetbrains.com/help/youtrack/devportal/youtrack-rest-api.html
- [Workflows (Dev)](api/youtrack-workflow-reference.md) — `5103` B — https://www.jetbrains.com/help/youtrack/devportal/youtrack-workflow-reference.html


## Full TOC coverage (bodies deferred)

Full topic lists saved under:

- `raw/cloud-llms.txt`
- `raw/server-llms.txt`
- `raw/devportal-llms.txt`

Deferred high-volume sections (link via official docs; bodies not all mirrored): Helpdesk deep-dive, every report widget, every default workflow page, full Hub REST entity catalog, every auth-module page. Re-crawl later if needed.

## Recommended for Edgar (one-person EDGAR-OS)

**YouTrack Cloud Free** — zero host ops, free tier fits solo + a few collaborators, REST + permanent tokens + MCP tools available, GitHub integration documented. Self-host Server only if data-residency / offline / full control outweighs maintenance.

---
*Generated 2026-09-22 08:36 Asia/Taipei*


## Box → Vault copy (executor note)

Sand executor could **not** write `G:\` directly (`machineId` Shell unavailable in this sandbox). Parent should CopyFromBox:

- Box root: `/workspace/edgar-os/artifacts/youtrack/`
- Tarball: `/workspace/edgar-os/artifacts/youtrack-hermes-wiki.tar.gz`
- Destination: `G:\Obsidian\Hermes-Wiki\youtrack\` (machineId `f9f05705-478b-4eaf-9968-5283c50e5d98`, label edgarstool)

Also mirrored for Forge without machine: same box paths.

*Index refreshed 2026-09-22 08:36 Asia/Taipei*
