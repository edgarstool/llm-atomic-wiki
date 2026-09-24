---
title: Skill Draft — YouTrack Workbench Ops
status: DRAFT (parent creates via update_state)
name_candidate: youtrack-workbench
lang_body: en (ops recipe); user plan is zh-TW elsewhere
---

# Skill Draft: `youtrack-workbench`

> Parent agent: register later with `update_state`. This file is the reusable body only.

## Name

`youtrack-workbench`（別名可：`yt-wb`）

## When to use

Use this skill when the user or Forge needs to:

- Create / update / search / close **Workbench** issues in **YouTrack**
- Manage agile board cards for Workbench
- Apply YouTrack commands, link GitHub PRs/commits to `WB-*` issues
- Call YouTrack **REST API** or **MCP tools** for issue ops

**Do not use** for:

- Agent-KB / Knowledge corpus authoring or migration into YouTrack
- Dual-writing the same work item to **Linear** (or keeping Linear as Current)
- Purchasing YouTrack paid plans ($0 default)
- Changing GitHub as code authority

## Preconditions

1. YouTrack Cloud instance URL: `https://<site>.youtrack.cloud` (or Server base URL)
2. Secret: permanent token (Bearer) with least privilege for the acting identity
3. Default project short name: `WB` (configurable)
4. Authority: after cutover, YouTrack is **issue Current** for Workbench; GitHub remains **code Current**

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| `action` | yes | `create` \| `update` \| `get` \| `search` \| `command` \| `comment` \| `link-github` |
| `project` | no | default `WB` |
| `issue_id` | for update/get/command | e.g. `WB-12` |
| `summary` / `description` | create | Markdown OK |
| `fields` | no | State, Type, Priority, custom |
| `query` | search | YouTrack search syntax |
| `command` | command | YouTrack command language |
| `dry_run` | no | default false |

## Steps outline

### A. Authenticate

1. Load token from secret store (never print full token).
2. Base API: `https://<site>.youtrack.cloud/api` (Cloud) — see DevPortal URL docs.
3. Header: `Authorization: Bearer <token>` + `Accept: application/json`.
4. Smoke: `GET /api/users/me?fields=id,login,name`.

### B. Create issue

1. `POST /api/issues?fields=idReadable,summary,id`
2. Body includes `project: { id }` or project shortName per API howto; set custom fields with correct `$type`.
3. Return `idReadable` (`WB-n`) to user.
4. Optionally add to agile board / tag `workbench`.

### C. Update / command

1. Prefer YouTrack **commands** for state/assignee/priority: `POST /api/commands`.
2. Or PATCH custom fields per API use-case docs.
3. Always echo before/after State when changing workflow state.

### D. Search

1. `GET /api/issues?query=<urlencoded>&fields=idReadable,summary,customFields(name,value(name))`
2. Prefer saved searches for recurring agent loops.

### E. GitHub link hygiene

1. In issue description/comment, link PR URL.
2. Instruct commits: `WB-n <message>` and enable project GitHub integration so VCS changes attach.
3. Do **not** open a parallel Linear issue.

### F. MCP path (if enabled on instance)

1. Prefer predefined YouTrack MCP tools for read/update when available (`predefined-ai-tools` docs).
2. Fall back to REST if MCP missing or insufficient.
3. Custom MCP tools only via reviewed app package — out of scope for default skill.

## Guardrails (hard)

1. **No dual-write** to Linear / other trackers for the same Workbench item.
2. **No Knowledge body** create/import into YouTrack articles as a KB migration.
3. **No purchases** / license upgrades unless Edgar explicitly orders.
4. **No secrets** in issue text, wiki, or git.
5. Until cutover complete: if YouTrack not live, **do not invent** a second Current — report blocker; GitHub remains code authority.

## Failure handling

| Symptom | Action |
|---------|--------|
| 401/403 | Refresh/rotate permanent token; check scopes |
| 400 on custom fields | Fetch project field bundle; send proper `$type` + value id |
| Rate / 429 | Backoff; batch fewer updates |
| Instance over storage | Stop attaching files; alert Edgar (Free 30 GB) |

## References (Hermes-Wiki)

- `youtrack/00-index.md`
- `youtrack/ops/DEPLOY-PLAN.md`
- `youtrack/api/youtrack-rest-api.md`
- `youtrack/api/authentication-with-permanent-token.md`
- `youtrack/api/api-howto-create-issue.md`
- `youtrack/api/predefined-ai-tools.md`
- `youtrack/cloud/integrate-project-with-github.md`

## Skill registration payload (for parent)

```yaml
name: youtrack-workbench
when_to_use: |
  Workbench issue ops on YouTrack (create/update/search/command).
  Not for Knowledge migration; not for Linear dual-write; $0 license default.
steps_ref: youtrack/ops/SKILL-DRAFT.md
```
