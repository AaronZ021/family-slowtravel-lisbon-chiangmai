# 源使用说明

- 每条事实 → `sources.csv` 中必须有 `source_id`
- 引用源 ID 在证据 markdown 中以 `[S-LIS-001]` / `[S-CMI-001]` 形式标注
- 源 ID 命名规则：
  - `S-LIS-NNN` = 里斯本相关源
  - `S-CMI-NNN` = 清迈相关源
  - `S-GEN-NNN` = 一般 / 跨城适用源（如 Schengen 通则）
- 不准伪造源或挂不存在的 URL
- 不可访问时 → `data/logs/inaccessible_sources.csv`
