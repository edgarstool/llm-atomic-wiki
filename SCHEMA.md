---
title: Hermes Wiki Schema
created: 2026-08-29
updated: 2026-08-29
type: system
owner: hermes
---

# Wiki Schema (EDGAR / Hermes)

## Domain

Hermes Agent 與 EDGAR-OS 的**編譯型知識庫**（compile > RAG）。  
**不是**人類 PARA vault，**不是** Agent-KB 法典，**不是** Honcho 互動記憶。

## Authority map（勿混）

| 層 | 路徑 | 職責 |
|----|------|------|
| 人類藏書樓 | `G:\Obsidian\Edgar'sObsidianVault` | 日記、人生、剪藏、探索 |
| 本 wiki | `G:\Obsidian\Hermes-Wiki` | raw→atoms→wiki 編譯知識 |
| 跨代理法典 | `G:\Agent-KB` | RULES / CORE / 已驗證 SOP |
| 互動記憶 | Honcho `edgar-team` | 人/偏好/session |

## Pattern

本 vault 採用 **[llm-atomic-wiki](https://github.com/cablate/llm-atomic-wiki)**（Karpathy LLM Wiki + atoms 層）：

```text
raw/  →  atoms/<branch>/  →  wiki/  →  index.md + log.md
```

- **Atoms = source of truth**（immutable；錯了新建 atom + archive 舊的）
- **Wiki = derived cache**（可從 atoms 重建；不要手改當真相）
- 正式 agent 操作規格：**先讀 `CLAUDE.md`**，流程見 `METHODOLOGY.md`

Hermes 內建 `llm-wiki` skill 的 `entities/concepts/` 形狀**不在此 vault 使用**。  
若 skill 被載入，以本 `SCHEMA.md` + `CLAUDE.md` 為準。

## Branches

| Branch | 範圍 |
|--------|------|
| `edgar-os` | 地形、canonical 路徑、主機、命名 |
| `hermes` | Agent / Desktop / Gateway / profiles / skills |
| `mcp` | MCP 本體、客戶端、入口 URL |
| `infrastructure` | CF / VPS / tunnel / DNS / runtime roots |
| `agent-ops` | Kanban、Honcho、編排、值班 |
| `product` | 對外產品與 sprint |
| `identity` | 品牌與公開入口（禁止 secrets） |

新 branch：先改本表 + `.gitignore` 說明，再建 `atoms/<name>/`。

## Conventions

- 檔名：小寫、連字號、無空白
- Atom 檔：`YYYY-MM-DD-<slug>.md`（見 `atoms/_template.md`）
- Wiki 檔：`wiki/<branch>-<topic-slug>.md`（見 `wiki/_template.md`）
- 每個動作 append `log.md`
- 編譯後跑：`bash scripts/gen-index.sh`、`bash scripts/lint.sh`
- **禁止**寫 secrets / tokens / private keys
- **禁止**改人類 vault 或 Agent-KB 當 wiki 輸出
- **禁止**修改 `raw/`（immutable sources）

## Ops for Hermes

1. Session 開始：讀 `SCHEMA.md` → `CLAUDE.md` → `index.md` → `log.md` 尾部
2. Ingest：raw 入庫 → 抽 atoms 到正確 branch
3. Compile：atoms 群組成 wiki 頁（先鎖 slug 再平行寫）
4. Query：先 index / atoms，再 wiki
5. Lint：程式層 scripts，再 LLM 語意層

## WIKI_PATH

```text
WIKI_PATH=G:\Obsidian\Hermes-Wiki
```
