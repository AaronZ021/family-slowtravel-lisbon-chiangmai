# v2 调研重规划 — 按 Layer 分层的 indicator 体系

> 修正点：v1 的每个格子停在"找到 N 个 X"，不足以支撑该格子的判断。v2 改为以 **indicator** 为最小单元，每个 indicator：
> 1. 优先用**官方/统计/平台指数**（参考 NomadList 风格）
> 2. 用**社区反馈作为佐证**强化或反驳官方数据（同一个社区信号可以同时出现在多个 indicator 下）
> 3. 必须给出**该 indicator 的判断 + 置信度**，不输出"城市总评"

## 评估输出格式（每个 indicator 必须有）

```
### Indicator: <名字>
- 定义/为什么对本家庭重要：1-2 句
- 期望数据源：[官方/平台 indices 列表]
- 充分性阈值：什么样的证据组合足以做出可靠判断

| 城市 | 主要统计数据点 | 平台 indices | 社区佐证（≥3 平台 OR ≥5 评论）| 该指标判断 | 置信度 | 关键源 |
|---|---|---|---|---|---|---|
| 里斯本 | ... | ... | ... | Green/Yellow/Red | high/med/low | S-LIS-XXX |
| 清迈 | ... | ... | ... | Green/Yellow/Red | high/med/low | S-CMI-XXX |
```

**不允许的判断依据**：
- ❌ "找到了 N 家医院的页面" → 必须给出 JCI 认证数 / 病床数 / 排名 / 评分
- ❌ "找到了 N 个游乐场列表" → 必须给出每候选区可达数 + 评分 + 距离阈值
- ❌ "加方建议'正常防范'" → 必须给出 Numbeo Crime Index / 警方统计数据 + 比较参考
- ❌ "搜到一篇报告说雨季湿冷" → 必须给出降雨天数统计 + 月均温 + 社区一致投诉次数

**允许的判断依据**：
- ✅ 官方/统计数据点
- ✅ 平台聚合 indices (Numbeo, IQAir, Speedtest Global Index, NomadList)
- ✅ 社区反馈复现信号 (≥3 平台 OR ≥5 独立来源)
- ✅ 多源交叉验证

---

## Layer 2 · 硬约束（Hard Constraints）

### 2.1 签证 — 90 天停留可行性
- **期望数据源**：泰外交部 / 葡外交部 / 加拿大旅行建议 / VFS Global / Royal Thai Embassy / Schengen 申请拒签率
- **充分性阈值**：至少 2 个官方源 + 已知政策动态

### 2.2 签证 — 申请提前期 + 复杂度
- **期望数据源**：官方处理时间标称 + 实际 expat 经验（社区佐证）
- **充分性阈值**：官方标称时间 + ≥3 来源 expat 实际体验

### 2.3 签证 — 拒签率/接受度（针对中国护照 + 加拿大居民）
- **期望数据源**：欧盟申根拒签率年报 / Royal Thai Consulate 数据 / expat 论坛实际拒签案例
- **充分性阈值**：官方拒签率统计 + 社区案例

### 2.4 官方安全建议
- **期望数据源**：加方 / UK FCDO / 美国务院 / Numbeo Safety Index / 警方犯罪统计
- **充分性阈值**：3 个西方政府对应级别 + 至少一个量化指数

### 2.5 犯罪 — 与家庭+幼儿相关的具体威胁
- **期望数据源**：Numbeo Crime Index / 当地警方分区数据 / 社区反馈
- **充分性阈值**：Numbeo crime index 数值 + 类别细分 + ≥5 社区一致信号

### 2.6 空气质量 — PM2.5 年均
- **期望数据源**：IQAir World Air Quality Report / WHO 数据库 / OpenAQ / 当地环境部门
- **充分性阈值**：≥2 年的官方年均数据

### 2.7 空气质量 — PM2.5 月度峰值（目标月份）
- **期望数据源**：IQAir 历史月度 / WAQI 历史 / 学术研究
- **充分性阈值**：每个目标月份至少 1 个官方数据点

### 2.8 气候 — 月均温度（高/低）
- **期望数据源**：World Meteorological Organization / climate-data.org / Meteostat / Weather Spark
- **充分性阈值**：每个目标月份的多年平均高/低温

### 2.9 气候 — 月均降雨 + 雨天数
- **期望数据源**：同上
- **充分性阈值**：每个目标月份的降雨 mm + 雨天数

### 2.10 气候 — 极端天数（高于 35°C / 高于 -3°C / 暴雨等）
- **期望数据源**：气象统计 + 当地新闻报道
- **充分性阈值**：年均极端天数

### 2.11 医疗 — 三甲级私立医院密度
- **期望数据源**：JCI Accredited Organizations Database / 国家卫生部医院列表 + 病床数
- **充分性阈值**：30 公里内 JCI 认证医院数 + 病床总数

### 2.12 医疗 — 24h 儿科急诊数量 + 距离
- **期望数据源**：医院 ER 服务页面 + Google Maps 地理距离
- **充分性阈值**：每候选区到最近 24h 儿科急诊的距离 + 数量

### 2.13 医疗 — 英语医生密度
- **期望数据源**：医院多语言声明 / expat 推荐医生列表 / Numbeo "English Speaking Doctors" 评级
- **充分性阈值**：医院明示英语 + ≥3 社区推荐

### 2.14 医疗 — 自付门诊价格
- **期望数据源**：医院公开价目表 / expat 实际账单
- **充分性阈值**：≥3 medical 来源给出价格区间

### 2.15 医疗 — 健康保险直付 + 报销复杂度
- **期望数据源**：保险公司公布的直付清单 / 医院国际患者部门页面
- **充分性阈值**：≥2 加拿大常用保险（Manulife/Sun Life/Allianz）的直付清单

### 2.16 传染病基线
- **期望数据源**：WHO Disease Outlook / 当地 CDC / Travel Health Pro
- **充分性阈值**：列出 top 3 传染病 + 年度发病率（如登革热每年 X 例）

### 2.17 自然灾害基线
- **期望数据源**：USGS / 当地地震局 / 国家气象局
- **充分性阈值**：地震/洪水/野火 历史频次 + 当年风险等级

---

## Layer 3 · 生活可运营性（Life Operability）

### 3.1 物价 — Cost of Living Index
- **期望数据源**：Numbeo Cost of Living Index / Mercer / Expatistan
- **充分性阈值**：至少 2 个聚合 index

### 3.2 物价 — 住房月租中位（2 卧 furnished 中心区）
- **期望数据源**：Numbeo Apartment Rent / Idealista / Airbnb 月租 aggregator / 当地房产报告
- **充分性阈值**：≥2 数据源给出 2 卧 furnished 价格区间

### 3.3 物价 — 餐饮 / 食杂 / 交通月度成本
- **期望数据源**：Numbeo 各分类指数
- **充分性阈值**：Numbeo 全分类数值

### 3.4 住房 — 关键设施在 listing 中的可见比
- **期望数据源**：在 Airbnb/Booking/Idealista 搜索结果中标注电梯/暖气/空气净化器的房源占比（手动估算）
- **充分性阈值**：从 ≥20 listing 摘要中估算

### 3.5 网速 — 平均下载 + 上传
- **期望数据源**：Speedtest Global Index 城市层 / Ookla / NPerf
- **充分性阈值**：城市层中位 Mbps

### 3.6 移动数据资费
- **期望数据源**：各运营商官方 + Cable.co.uk Worldwide Mobile Data Pricing
- **充分性阈值**：5GB/30GB 月套餐价

### 3.7 公共交通 — 通勤时间指数
- **期望数据源**：Numbeo Traffic / TomTom Traffic Index / Moovit
- **充分性阈值**：通勤时间分钟 + 拥堵指数

### 3.8 步行可达度 — walkability
- **期望数据源**：Numbeo Quality of Life "Pollution + Climate + Crime" 派生 / Walk Score 类（不全球可用）/ 城市规划 + 社区描述
- **充分性阈值**：每候选区步行可达 (杂货/药店/游乐场/儿科急诊) 数 + 距离 + 社区一致评分

### 3.9 婴儿车摩擦度
- **期望数据源**：政府无障碍声明 + 社区一致投诉 + 街景 spot-check
- **充分性阈值**：≥5 独立社区来源一致 + 候选区典型街景描述

### 3.10 儿童安全座椅在网约车中的可获得性
- **期望数据源**：Uber/Grab/Bolt 官方功能说明 + 当地法律执行强度 + Taxi Bambino 等专门服务
- **充分性阈值**：app 内功能存在性 + ≥3 社区报告

### 3.11 儿童户外活动 — 候选区前 N 个高质量
- **期望数据源**：Google Maps 评分（≥4.4 + 评论 ≥100）+ 家庭博客推荐
- **充分性阈值**：每候选区 ≥3 个 Google Maps 4.4+ 公园/游乐场 + 距离 ≤2km

### 3.12 室内备选数量（雨/烧林季）
- **期望数据源**：Google Maps 搜索 "indoor playground" + 评分 ≥4.3 + 评论数
- **充分性阈值**：城市内 ≥8 个 4.3+ 评分 + 至少 2 个在每候选区可达

### 3.13 结构化儿童活动（短期接纳）
- **期望数据源**：worldschooling hub 官网 + 当地教育机构页面 + 评论
- **充分性阈值**：≥3 机构明示接受短期参与

### 3.14 Childcare/Nanny — 平台 + 价格 + 信任机制
- **期望数据源**：Babysits / Sitly / 本地 nanny agency / Numbeo Childcare Index
- **充分性阈值**：Numbeo monthly preschool 价格 + ≥2 平台覆盖

### 3.15 杂货 — 主要超市数 + 进口食品供应
- **期望数据源**：超市官方店面定位地图 + 评论
- **充分性阈值**：每候选区 ≥2 大型超市 + 进口食品类别覆盖

### 3.16 药店密度 + 24h
- **期望数据源**：政府药店登记 / Google Maps 密度
- **充分性阈值**：每候选区 1 公里内药店数 + 24h 选项

### 3.17 食物多样性 + 儿童友好餐饮
- **期望数据源**：Yelp/TripAdvisor 餐厅 4.0+ 评分密度 / 家庭博客
- **充分性阈值**：每候选区 ≥5 个 family-friendly 4.0+ 餐厅

### 3.18 英语普及度
- **期望数据源**：EF English Proficiency Index / 当地国家整体 + 城市说明 / 社区报告
- **充分性阈值**：EF EPI 国家分 + 城市层级实践描述

### 3.19 expat / worldschooling 社群活跃度
- **期望数据源**：FB 群组成员数 / Meetup 群组活跃度 / Reddit subreddit subscribers + 周活
- **充分性阈值**：≥3 群组指标 + 一致表述

### 3.20 本地化 vs 旅游/数字游民泡沫
- **期望数据源**：游客 / 居民比 / Airbnb 短租房比例 / 社区描述
- **充分性阈值**：≥3 数据来源 + 候选区描述

---

## Layer 4 · 社区/感受信号（独立主题）

> 这一层不与具体 indicator 一一对应，而是收集**主题级别**的强信号——情感、共识、撤离/留下信号、文化偏好等，作为整体氛围的描述。

### 4.1 撤离信号（"What would make families leave?"）
- 收集每城反复出现的"不能/不该长住"主题
- 阈值：≥3 平台 ≥5 独立信号

### 4.2 留下信号（"What makes families stay multi-season?"）
- 反复出现的"喜欢/想再来"主题
- 阈值同上

### 4.3 季节切换信号（"What month is the killer?"）
- 反复出现的"X 月不要来 / X 月最佳"信号
- 阈值同上

### 4.4 大主题 verbatim 引用
- 每个主题选 3-5 条最具代表性的 verbatim 原文（含来源、平台、日期）
- 用于增强报告的真实感和读者判断

### 4.5 反共识（少数派）
- 与主流意见相反的 verbatim
- 至少 2 条以提示读者主流意见的局限性

---

## 数据采集分工（4 个并行 agent）

| Agent | 范围 | 输出文件 |
|---|---|---|
| **A1: Layer 2** | 2.1-2.17 所有 hard constraint indicators | `evidence/v2/layer2_hard_constraints.md` |
| **A2: Layer 3a** | 3.1-3.7 + 3.15-3.17（物价/网络/物流/餐饮） | `evidence/v2/layer3a_economics_utilities.md` |
| **A3: Layer 3b** | 3.8-3.14 + 3.18-3.20（儿童/出行/社群/泡沫） | `evidence/v2/layer3b_children_mobility_community.md` |
| **A4: Layer 4** | 4.1-4.5 主题级 verbatim | `evidence/v2/layer4_community_themes.md` |

每个 agent 必须：
- 沿用 v1 已收集的 143 条源（不要重复抓取），优先**补充**官方/统计/平台 indices
- 新源继续在 `data/sources/sources.csv` 追加（id 接续，目前到 S-LIS-085 / S-CMI-058）
- WebSearch 每城 ≤ 40 次，WebFetch 每城 ≤ 30 次
- 输出 **per-indicator 判断 + 置信度**，不输出城市总评

## 不在 v2 范围的事

- 不重做 v1 已经做得不错的 evidence/lisbon、evidence/chiang_mai 原始抓取
- 不删除 v1 任何文件（v2 是增量）
- 不输出"哪城更好"的最终结论

## 最终交付

1. `evidence/v2/layer2_hard_constraints.md`
2. `evidence/v2/layer3a_economics_utilities.md`
3. `evidence/v2/layer3b_children_mobility_community.md`
4. `evidence/v2/layer4_community_themes.md`
5. `reports/v2_indicator_matrix.csv` — 每行一个 indicator × 城市 × 判断 + 置信度 + 关键源
6. `reports/v2_layer_views/` — 按 Layer 分页的 HTML 视图
7. 更新 GitHub Pages 站点：新增 Layer 2/3/4 三个主导航
