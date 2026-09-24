---
title: YouTrack 部署計畫（EDGAR-OS Workbench）
lang: zh-Hant
fetched_at_note: 2026-09-22 08:36 Asia/Taipei
scope: Workbench issue tracking only
budget: $0 default (no paid YouTrack purchase)
---

# YouTrack 部署計畫 — EDGAR-OS Workbench

給 Edgar 的決策與執行計畫。產品名稱與 URL 維持英文。

## 0. 決策摘要（先讀）

| 項目 | 建議 |
|------|------|
| **追蹤器** | 切換至 **YouTrack**（取代 Linear 作為 Workbench tracker；**禁止 dual-write**） |
| **範圍** | **僅 Workbench issue tracking**。Agent-KB / Knowledge corpus **不**搬進 YouTrack |
| **程式碼權威** | YouTrack 上線前：**GitHub 仍是 Workbench code 的 Current**。上線後：issues 以 YouTrack 為 Current；code 仍在 GitHub |
| **方案** | **YouTrack Cloud Free（$0）** 為預設。Self-host Server 僅作備選 |
| **付費** | **預設不購買**任何付費 plan。超限再由 Edgar 決定 |

### 為何選 Cloud Free（一人 EDGAR-OS）

- 免維運（無 Docker / TLS / backup 值班）
- Free：最多 **10** standard users + **3** helpdesk agents；儲存約 **30 GB**（見官方 docs）
- REST API、permanent token、GitHub 整合、workflows、**MCP tools** 皆可用
- 與「$0 default」一致

### 何時才考慮 Server

- 需要資料完全自管 / 離線 / 特定 residency，且願意承擔 Docker 升級與備份
- Server 亦有 **10 free users** 級授權敘述（見 buy 頁），但 **時間成本 ≠ $0**

官方參考：

- Cloud Free / 註冊：https://www.jetbrains.com/help/youtrack/cloud/new-youtrack-cloud-instances.html
- License：https://www.jetbrains.com/help/youtrack/cloud/switching-subscription-plans.html
- Storage：https://www.jetbrains.com/help/youtrack/cloud/storage-limits.html
- Buy：https://www.jetbrains.com/youtrack/buy/
- Docker Server：https://www.jetbrains.com/help/youtrack/server/youtrack-docker-installation.html
- REST：https://www.jetbrains.com/help/youtrack/devportal/youtrack-rest-api.html
- MCP：https://www.jetbrains.com/help/youtrack/devportal/ai-tools.html

---

## Phase A — 決策鎖定（Day 0）

1. 確認：**Cloud Free**（或明確改選 Server）。
2. 確認範圍邊界：
   - ✅ Workbench issues / boards / workflows
   - ❌ Knowledge / Agent-KB 正文不進 YouTrack（可用連結指回 Obsidian / Knowledge MCP）
3. 確認 **no dual Current**：
   - Linear：凍結新建 Workbench issues；歷史可唯讀或匯出後封存
   - GitHub Issues：若曾當 Workbench tracker，同樣凍結新建，改連 YouTrack ID
4. 選定 instance 名稱（hostname）：`something.youtrack.cloud`

**Exit：** Edgar 書面/口頭確認 Cloud vs Server + 站名。

---

## Phase B — 開站與最小設定（$0）

1. 到 JetBrains 註冊 Cloud Free（表單見 New Instances 文件）。
2. 確認 email → 選 data center（就近）→ 設 admin 密碼。
3. **立刻**：
   - 禁用不需要的 guest（預設已 banned）
   - Profile → Account Security → 建立 **permanent token**（給 REST / agents；最小權限）
   - 啟用 2FA（建議）
4. 建立專案（建議 short name）：
   - `WB` — Workbench（主專案）
   - 可選：`OPS` — EDGAR-OS 營運雜項（仍非 Knowledge）
5. 欄位建議（保持精簡）：
   - State：Open / In Progress / Blocked / Done / Cancelled
   - Type：Task / Bug / Spike / Chore
   - Priority：P0–P3
   - 自訂：`Repo`（字串或 enum：對應 GitHub repo）、`Forge`（是否 agent 可執行）
6. Agile：建一個個人 Kanban board（WIP 可設 3）。
7. 整合：專案設定 → **GitHub** VCS（commit/PR 連 issue；命令寫在 commit message）。

**Exit：** 能手動建一張 WB-1，並用 permanent token 打通 REST `GET /api/users/me`。

---

## Phase C — Agent / Skill 接通（仍 $0）

1. Parent 用 `ops/SKILL-DRAFT.md` 經 `update_state` 註冊 Skill（本檔僅草稿）。
2. Secrets：token 放既有 secret store（勿寫進 git / wiki）。
3. 驗證 MCP（若 instance 支援 YouTrack MCP）：
   - 預設 tools：讀寫 issues（見 DevPortal `predefined-ai-tools`）
   - 或先用 REST + Skill 步驟（較可控）
4. Forge / Workbench agents：**建立 / 更新 / 查詢** issues 只打 YouTrack；**禁止**同時寫 Linear。

**Exit：** 一條 agent 路徑可 create→update→query 成功；Linear 路徑對 Workbench 關閉。

---

## Phase D — 遷移與切換（單一 Current）

1. **不**做 Knowledge 遷移。
2. Workbench 未完成項目：
   - 從 Linear（或 GitHub Issues）**匯出** → CSV / 手動精選 → YouTrack Import（CSV）或 API 批次
   - 官方：https://www.jetbrains.com/help/youtrack/cloud/import-from-csv.html
3. 每張遷移 issue 註記 `legacy:` 原 ID 連結。
4. 切換日（Cutover）：
   - 宣布 YouTrack = Workbench issue Current
   - Linear Workbench 專案：archive / read-only
   - 文件與 Skill 中的 tracker URL 全部改 YouTrack
5. GitHub：PR / commit 開始引用 `WB-n`；code Current 仍是 GitHub。

**Exit：** 新 issues 100% 只出現在 YouTrack；無 dual-write。

---

## Phase E — 營運慣例

1. 一週回顧：board + saved search `State: -Fixed -Done -Cancelled`
2. 儲存空間：附件節制；接近 30 GB 前清附件（storage-limits）
3. Backup：Cloud 由 JetBrains 管；重大里程碑可另做 issue export
4. Workflow：先用 Constructor 做「In Progress 自動 assignee = 變更者」等小規則；避免過度自動化
5. 付費升級：**預設不做**。僅當 users >10 或儲存不足且 Edgar 批准

---

## 風險與阻擋

| 風險 | 緩解 |
|------|------|
| Free 額度誤判 | 以 instance License Details UI 為準；wiki 數字僅筆記 |
| Agent 誤寫 Linear | Skill 明文禁止；關掉 Linear MCP 對 Workbench 的 write |
| Knowledge 被塞進 YouTrack | 專案說明 + Skill 範圍條款 |
| Token 外洩 | permanent token 可撤銷；分環境 token |
| Server 維運過重 | 預設不選 Server |

---

## 驗收清單（Success）

- [ ] `*.youtrack.cloud` 可登入（Free）
- [ ] 專案 `WB` + board 可用
- [ ] REST + token 可用
- [ ] Skill 已註冊（parent）且 agents 只寫 YouTrack
- [ ] Linear Workbench 無新寫入
- [ ] Hermes-Wiki `youtrack/` 有 index + docs + 本計畫
- [ ] **未**購買付費 plan
- [ ] Knowledge 仍在原系統

---

## 附：Cloud vs Server 對照（決策用）

| | Cloud Free | Server（自架） |
|--|------------|----------------|
| 金錢 | $0（≤10 users） | License 可 Free 級，但需主機 |
| 維運 | JetBrains | 你（Docker/升級/備份/TLS） |
| 上線速度 | 分鐘級 | 小時～天 |
| API/MCP | 有 | 有 |
| 適合 | 一人 EDGAR-OS（預設） | 強自管需求 |

**推薦：Cloud Free。**
