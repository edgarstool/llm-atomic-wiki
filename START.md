# START — Hermes-Wiki

獨立編譯型知識庫。**不是**人類 PARA vault。

| | |
|--|--|
| Path | `G:\Obsidian\Hermes-Wiki` |
| Human vault | `G:\Obsidian\Edgar'sObsidianVault` |
| Spec | [[CLAUDE]] |
| Pipeline | [[METHODOLOGY]] |
| Boundaries | [[SCHEMA]] |
| Index | [[index]] |
| Log | [[log]] |

```text
raw/  →  atoms/<branch>/  →  wiki/  →  index + lint
```

Branches: `edgar-os` · `hermes` · `mcp` · `infrastructure` · `agent-ops` · `product` · `identity`

After compile:

```bash
bash scripts/gen-index.sh
bash scripts/lint.sh
```
