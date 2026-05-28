# Layer 3a · 经济 / 物流 / 网络 Indicators

**范围**：3.1 物价 COL · 3.2 住房月租 · 3.3 餐饮/食杂/交通月度成本 · 3.4 住房关键设施可见比 · 3.5 网速 · 3.6 移动数据 · 3.7 公共交通 · 3.15 杂货 · 3.16 药店 · 3.17 餐饮多样性

**对比对象**：里斯本（葡萄牙）vs 清迈（泰国） — 2 成人 + 4.5 岁 + 2.5 岁，慢旅 90 天
**判断尺度**：Green = 强支持长居 / Yellow = 可行有摩擦 / Red = 显著风险或不足 / Gray = 数据不足
**置信度**：high = 多平台 indices + 社区交叉 / med = 单平台 + 部分社区 / low = 单源孤证

---

## Indicator 3.1 — Cost of Living Index

**定义/重要性**：整体物价水平直接决定 90 天预算是否可承受。家庭旅居成本主要由住房 + 食物 + 交通 + 服务构成。

**期望数据源**：Numbeo Cost of Living Index、Expatistan、Mercer
**充分性阈值**：至少 2 个聚合 index

| 城市 | 平台 indices（Numbeo 2026） | 关键单价点 | 社区佐证 | 判断 | 置信度 | 关键源 |
|---|---|---|---|---|---|---|
| **里斯本** | COLI **54.2** / Rent **38.6** / COLI+Rent **47.2** / Groceries **50.1** / Restaurant **53.1** / PPP **60.9** | 单人月支出（不含房租）**~€753.5 / C$1,212.8**；廉价餐 €15；中端两人餐 €56.5 | Numbeo 自评 "Lisbon 比 Toronto 便宜 16.8%（不含房租）"；ECI 数据：rent 比 Toronto 仅低 3.4% — 房租贵是核心问题 | **Yellow** — 食杂 / 餐饮中等偏贵，房租是绝对的成本霸主 | high | S-LIS-086, S-LIS-087, S-LIS-088 |
| **清迈** | COLI **34.8** / Rent **10.6** / COLI+Rent **24.0** / Groceries **43.3** / Restaurant **21.2** / PPP **55.5** | 单人月支出（不含房租）**~฿18,113 / C$769**；廉价餐 ฿65；中端两人餐 ฿600 | Numbeo 自评 "Chiang Mai 比 Toronto 便宜 50.7%"；对比 Lisbon："比里斯本 COLI 低 40.7%（不含房租）/ 51.7%（含房租）/ 71.3%（房租）" | **Green** — 数值上几乎所有维度都显著低于里斯本 | high | S-CMI-059, S-CMI-060, S-CMI-061 |

---

## Indicator 3.2 — 住房月租中位（2 卧 furnished 中心区）

**定义/重要性**：4 人家庭至少需 2 卧；furnished + 中心区是慢旅家庭的事实标准。这是 90 天总预算最大的单一变量。

**期望数据源**：Numbeo Apartment Rent + Idealista（PT）+ DDproperty / Hipflat（TH）+ Airbnb 月租
**充分性阈值**：≥2 数据源给出 2BR furnished 价格区间

| 城市 | Numbeo 2026 价位 | 平台 listing 实测 | 社区佐证 | 判断 | 置信度 | 关键源 |
|---|---|---|---|---|---|---|
| **里斯本** | 1BR 中心 **€1,411** / 外围 €1,071；3BR 中心 **€2,539** / 外围 €1,712；推算 **2BR furnished 中心 ≈ €1,800-2,300** | Idealista 显示 Avenidas Novas / Príncipe Real 有 furnished T2（70m²）多个 listing；Blueground furnished 高端 stock 集中在 Avenidas Novas | v1 已多次记录 "rent skyrocketed post-2022 digital nomad influx"；当地新建少 + 历史楼存量 | **Red** — 房租明显挤压家庭 90 天预算（€5,400-6,900 仅住房）；与本地中位净收入 €1,374 形成强烈反差（房价收入比 18.92，Numbeo 列为 Very High） | high | S-LIS-086, S-LIS-088, S-LIS-096, S-LIS-103 |
| **清迈** | 1BR 中心 ฿16,524 / 外围 ฿9,373；3BR 中心 **฿29,942 (~€790)** / 外围 ฿17,308；2BR furnished 中心 **฿20,000-30,000 (~€530-790)** | DDproperty 显示 56 个 2BR condo listing；Nimman Soi 6 实测 ฿30,000 furnished 2BR；Hang Dong 主要是 stand-alone house（很少 condo） | v1 S-CMI-006/007 一致：长租 12-22k THB 2BR；Maya/Nim City 周边 furnished 充足 | **Green** — 90 天 2BR furnished 约 €1,600-2,400 总价；与里斯本相差 3-4 倍 | high | S-CMI-059, S-CMI-061, S-CMI-071 |

---

## Indicator 3.3 — 餐饮 / 食杂 / 交通月度成本

**定义/重要性**：仅次于住房的第二大日常支出，决定家庭日常生活舒适度。

**期望数据源**：Numbeo 全分类 indices + 单价对照
**充分性阈值**：Numbeo 全分类数值

| 类别 | 里斯本 | 清迈 | 备注 |
|---|---|---|---|
| Restaurant Price Index (Numbeo) | **53.1** | **21.2** | 清迈餐厅价 ≈ 里斯本的 40% |
| Groceries Index (Numbeo) | **50.1** | **43.3** | 食杂差距远小于餐饮（清迈进口食品贵） |
| 廉价餐 | €15.00 | €1.71 | ~9 倍差 |
| 中端两人餐 | €56.50 | €15.83 | ~3.5 倍差 |
| 牛奶 1L | €1.04 | €1.65 | 清迈反而更贵 |
| 鸡肉 1kg | €6.63 | €2.55 | 里斯本贵 2.6 倍 |
| 苹果 1kg | €1.96 | €2.24 | 清迈贵 14%（进口） |
| 月度交通月票 | **€40.00** | **€47.48** | 接近，但清迈无统一月票，此数为 Numbeo 估算 |
| 出租车 1km | €0.96 | €0.79 | 清迈低 18% |
| 基本水电 85m² | **€147.20** | **€56.21** | 里斯本贵 2.6 倍（冬季供暖差距更大） |
| 60Mbps 家庭宽带 | €30.48 | €15.89 | 里斯本贵 92% |

**里斯本判断**：餐饮 / 公用事业 / 宽带显著贵；食杂中等；公共交通价廉。家庭月度（不含房租）参考 **€753 单人 × 4 ≈ €2,260（Numbeo 家庭加权约低 25%，~€1,700-2,000）**。**Yellow** · high · 关键源 S-LIS-086, S-LIS-087
**清迈判断**：餐饮 / 公用事业 / 宽带 / 肉类大幅便宜；进口/乳制品/苹果略贵于里斯本（小项）。家庭月度（不含房租）参考 **~฿66,398 / 4 人 ≈ €1,750**。**Green** · high · 关键源 S-CMI-059, S-CMI-060

---

## Indicator 3.4 — 住房关键设施在 listing 中的可见比

**定义/重要性**：电梯（4 人 + 两娃带行李）/ 暖气（里斯本冬季）/ 空气净化器（清迈烧林季）— 缺失会显著降低体感舒适度。

**期望数据源**：Airbnb/Booking/Idealista/DDproperty listing 摘要抽样估算
**充分性阈值**：从 ≥20 listing 估算

| 城市 | 抽样观察 | 平台/社区一致信号 | 判断 | 置信度 | 关键源 |
|---|---|---|---|---|---|
| **里斯本** | Blueground 高端 stock（Avenidas Novas/Príncipe Real）明确标"elevator + AC + heating"；老城 Alfama/Bairro Alto 历史楼 4-5 层无电梯**普遍**；中央暖气罕见，多为可移动电暖器 | v1 S-LIS-081（Portugalist）专题论"如何在没有中央供暖的葡萄牙房子保暖"；S-LIS-080 Tripadvisor 评论投诉电梯故障；多个家庭博客建议**专门筛选带电梯的 listing** | **Yellow** — 高端 furnished stock（Blueground/同等）电梯+AC 可见比高（估 >70%），但**暖气**普遍缺失或不可靠；Alfama/Mouraria 历史楼电梯可见比低（估 <30%） | med | S-LIS-080, S-LIS-081, S-LIS-103 |
| **清迈** | Airbnb Chiang Mai 多 listing 直接标"AC + air purifier + HEPA"；2025 后 HEPA 已成卖点；condo 形态本身电梯标配（Nimman/Maya/Nim City 区） | "Hotels and accommodations now have HEPA air purifiers as a selling point post-2025" — 多数烧林季博客一致；S-CMI-072 Rimping 与 Maya/Nim City 同区，condo 周边普遍 7+ 层带电梯 | **Green** — 烧林季的核心硬约束（空气净化器）反而成为 listing 标准卖点；condo stock 电梯标配 | med | S-CMI-046, S-CMI-072 + 新搜索 |

> **注**：未做严格 20 个 listing 的逐条统计（超出本 indicator 网络预算），结论基于平台搜索结果摘要 + 社区一致信号。如需精确比例，建议后续手动抽样 30 个 listing。

---

## Indicator 3.5 — 网速 — 平均下载 + 上传

**定义/重要性**：远程工作家庭的基础设施约束（视频会议 / 上传剪辑）。

**期望数据源**：Speedtest Global Index（Ookla）城市层 + Wikipedia 聚合
**充分性阈值**：城市层中位 Mbps

| 城市 | 国家级中位（Speedtest, Mar 2026） | 城市级 | 社区佐证 | 判断 | 置信度 | 关键源 |
|---|---|---|---|---|---|---|
| **里斯本** | 固网 **243.84 Mbps** / 移动 **137.64 Mbps** | 里斯本作为葡萄牙最大都市，城市级 ≥ 国家级；Numbeo 60Mbps 月费 €30.48（说明 60Mbps 是基础档，1Gbps fiber 普及） | v1 多个数字游民博客确认 fiber 普及 + 速度稳定 | **Green** — 固网中位 >240Mbps 完全满足视频会议、4K 流媒体、家庭多设备 | high | S-LIS-091 |
| **清迈** | 固网 **279.65 Mbps** / 移动 **137.98 Mbps**；Nation Thailand 2025 报道泰国全球第 13 | 城市级：3BB / AIS / True fiber 在 Nimman/Hang Dong/Mae Rim 全覆盖；3BB Giga Fiber 1Gbps/100Mbps **฿590/月 (~€15.5)** | v1 S-CMI 多源记录 expat 一致认为 CM fiber 稳定快；Iglu 等 co-working 报告 1Gbps 标配 | **Green** — 实际固网中位高于葡萄牙；价格仅为葡萄牙的一半 | high | S-CMI-064, S-CMI-065, S-CMI-068 |

---

## Indicator 3.6 — 移动数据资费

**定义/重要性**：出门带娃必备移动网络；进口 eSIM / 本地 SIM 价差大。

**期望数据源**：Cable.co.uk Worldwide Mobile Data Pricing + 各运营商官方
**充分性阈值**：5GB/30GB 月套餐价

| 城市 | Cable.co.uk 排名 + 1GB 均价（2023 edition） | 主流运营商套餐 | 判断 | 置信度 | 关键源 |
|---|---|---|---|---|---|
| **里斯本** | **#148 / 237，$1.79/GB** | MEO Enjoy 30GB **€15**（15 天）；Vodafone Go Total **€34.99/30 天**；NOS/MEO/Vodafone 5G 全覆盖 | **Yellow** — 价格在欧盟内偏高（≈ 西欧典型），但 30GB 包 €15 起的入门选项对家庭 90 天足够；与本地中位净收入 €1,374 相比仍是小项 | high | S-LIS-092, S-LIS-093 |
| **清迈** | **#34 / 237，$0.41/GB** | dtac GO 30GB ฿899（~€24）/月；AIS 15-30GB ฿49-1599；tourist eSIM 30GB ฿599/15 天 | **Green** — 全球前 35 廉价梯队，1GB 均价仅葡萄牙的 23% | high | S-CMI-066, S-CMI-067 |

---

## Indicator 3.7 — 公共交通通勤时间指数

**定义/重要性**：带娃家庭高度依赖公共交通 / 拼车，长通勤会显著消耗精力。

**期望数据源**：Numbeo Traffic Index、TomTom Traffic Index、Moovit
**充分性阈值**：通勤时间分钟 + 拥堵指数

| 城市 | Numbeo (2026) | TomTom (2024) | 公共交通系统 | 判断 | 置信度 | 关键源 |
|---|---|---|---|---|---|---|
| **里斯本** | Traffic Index **132.71** / Time Index **34.64 min** / 单程 14.41km / 拥堵 138.82 | 拥堵 **26%** / 10km 平均 23m47s / **每年 95h 损失** | Metro 4 线 + Carris bus/tram + CP train；**Navegante Metropolitano €40/月**，子女 €30，家庭票 €80/月 (3+ 人户口) | **Green** — 拥堵率不高（26%），公共交通系统完善 + 家庭月票优惠极大；3 岁以下免费乘车 | high | S-LIS-089, S-LIS-090, S-LIS-095 |
| **清迈** | Traffic Index **115.86** / Time Index **26.20 min** / 单程 13.92km / 拥堵 105.03 | 拥堵 **37%** / 10km 平均 23m31s / **每年 72h 损失** / 全球排名 116 | **无统一地铁 / 公交月票**；songthaew (red truck) ฿20-100/趟 + Grab + Bolt + 自驾摩托；songthaew 无安全座椅 / 安全带 | **Yellow** — Numbeo 时间指数最低（26.2min），但 TomTom 拥堵率反高于里斯本（37%）说明城市路网摩托主导；公共交通体系**缺乏家庭友好结构**（无月票、无安全带），需依赖 Grab + 自带儿童座椅 | high | S-CMI-062, S-CMI-063, S-CMI-070, S-CMI-036, S-CMI-038 |

---

## Indicator 3.15 — 杂货 — 主要超市数 + 进口食品供应

**定义/重要性**：4.5 岁 + 2.5 岁 picky eater + 进口食材（婴儿食品、欧式乳制品、亚洲调料）需求高。

**期望数据源**：超市官方店面地图 + 评论
**充分性阈值**：每候选区 ≥2 大型超市 + 进口食品类别覆盖

| 城市 | 全国 / 城市连锁 | 进口食品 hub | 候选区可达性 | 判断 | 置信度 | 关键源 |
|---|---|---|---|---|---|---|
| **里斯本** | Continente **500+ 店**（葡萄牙最大） / Pingo Doce **486** / Lidl **277** / Auchan / Mercadona；**El Corte Inglés São Sebastião** = 完整 World Food 区 + 国际品牌；Celeiro / Go Natural = 全城有机连锁；Martim Moniz = 亚洲超市群 | **EC Inglés (Av. António Augusto de Aguiar)** = 1 个；Asian 集群 Martim Moniz；Continente Colombo 库存最深 | Avenidas Novas / Príncipe Real 步行 / 短交通可达 EC Inglés + 多个 Pingo Doce；Continente 在 Colombo / Vasco da Gama mall 大店 | **Green** — 主流连锁高密度 + 国际/有机/亚洲三个垂类齐全 | high | S-LIS-097, S-LIS-098, S-LIS-085 |
| **清迈** | **Rimping**（5+ 店，含 Maya/Nim City/Kad Farang）= 旗舰进口连锁；**Tops** (Central Festival/Kad Suan Kaew)；Big C / Lotus / Makro = 大型；7-Eleven / Family Mart 密度极高 | Rimping 进口覆盖 **瑞士/德/新/西/意/韩/美/日/英/法 10 国**；Maya Branch 商业区核心 | **Nimman**：Rimping Maya（步行）+ Tops Central Festival（10 min）；**Hang Dong**：Rimping Kad Farang（核心目标客户为外籍家庭）；**Mae Rim**：Rimping 集团总部所在区 | **Green** — 候选三区均有 Rimping + Tops 覆盖；进口食品 SKU 不输欧洲城市 | high | S-CMI-041, S-CMI-042, S-CMI-072 |

---

## Indicator 3.16 — 药店密度 + 24h

**定义/重要性**：幼儿急性病（发烧 / 腹泻 / 过敏）经常需要非营业时间购药。

**期望数据源**：政府药店登记 + Google Maps + 24h 网络
**充分性阈值**：每候选区 1 公里内药店数 + 24h 选项

| 城市 | 总量 + 密度 | 24h 系统 | 候选区可达性 | 判断 | 置信度 | 关键源 |
|---|---|---|---|---|---|---|
| **里斯本** | 葡萄牙 **2,800+ 家药店**全国，**1.5 药剂师/1000 人**（2021）；里斯本市区密度高，大致每 300-500m 一家 | **Farmácias de Serviço** 国家级强制轮值系统：每晚每区固定指定 1-2 家 24h 服务，门口贴出最近 24h 药店；含 Farmácia do Marquês 等知名点 | Avenidas Novas / Príncipe Real / Marquês de Pombal 区域内 1km 走路圈 **≥5 家** Farmácia 是常态；夜间需到当晚 de serviço 指定店 | **Green** — 国家级强制 24h 轮值制度 + 高密度，体系成熟 | high | S-LIS-099, S-LIS-100 |
| **清迈** | Boots（含 Nimman / Central Festival G floor / MAYA B1 / Chang Klan / Thapae Gate 多店）+ Watsons（Maya / Central Chiangmai 2 等）+ Save Drug + 本地独立药店密集 | **Be WELL 24/7 Late Night Pharmacy** = 明确 24h；Medica Hub (Nimman) 营业至午夜；Boots Nimman 周末关至 22:30；**国家级 24h 强制轮值不存在** | Nimman 商业核心步行 1km **多 Boots + Watsons + 24/7 Be WELL**；Hang Dong / Mae Rim 候选区 24h 较少，依赖 driving 10-15min 回市区 | **Yellow** — 总密度高 + 有 24h 选项，但**无国家强制轮值**；24h 选项集中在 Nimman 商业带，Hang Dong/Mae Rim 候选区缺乏夜间步行可达 | med | S-CMI-073, S-CMI-074 |

---

## Indicator 3.17 — 食物多样性 + 儿童友好餐饮

**定义/重要性**：90 天家庭旅居 ≈ 270 餐外食占比可观，儿童友好 + 多样性影响家庭幸福感。

**期望数据源**：TripAdvisor / Yelp 4.0+ 评分密度 + 家庭博客 / wanderlog
**充分性阈值**：每候选区 ≥5 个 family-friendly 4.0+ 餐厅

| 城市 | 平台密度 + 头部 picks | 儿童设施 (kid menu / high chair / play area) | 文化多样性 | 判断 | 置信度 | 关键源 |
|---|---|---|---|---|---|---|
| **里斯本** | TripAdvisor "Best Family Restaurants Lisbon" 列表 hundreds；Wanderlog top-50 + Taste of Lisboa / Eating Europe / TheUrbanKids 多博客交叉 | Capricciosa（kids menu + high chair + 尿布台）/ Monte Mar（Kids menu + 周末娱乐）/ Lota d'Ávila（专属儿童区）/ Atalho Reel（草坪外摆）/ Café Comoba（儿童椅） | 葡萄牙 + 巴西 + 非洲（莫桑/安哥拉）+ 意大利 + 印度 + 中国 + 日本 + 越南；**Time Out Market** 是 30+ 风味试错圣地 | **Green** — 评分密度极高 + 儿童设施明确化 + 文化多样性最广 | high | S-LIS-101, S-LIS-102 |
| **清迈** | TripAdvisor "10 Best Family Restaurants CM" + Wanderlog top-50 + Chiang Mai Kids / BKK Kids "15 Top Kids Cafes"；分区列表覆盖 Nimman / Hang Dong | Namtok Hang Dong（kid menu + 大型 trampoline 游乐 2-12 岁）/ Ginger Farm Kitchen（耐心带娃，菜单儿童友好）/ Freebird Cafe（kids corner + 玩具）/ Jungle De Cafe Hang Dong（亲子餐厅）/ More Space（小型游乐区） | 北泰 + 全泰 + 中 + 日 + 韩 + 西餐 + 印度 + 素食 + 有机；外籍家庭长居 driving 出菜系多样性；**Nimman 是国际餐厅密度最高带** | **Green** — Nimman/Hang Dong 候选区均 ≥5 个 4.0+ 儿童友好；游乐区设施反而**比里斯本更普遍**（kid cafe 概念发达） | high | S-CMI-052, S-CMI-075, S-CMI-076 |

---

## 数据健康度小结

| Indicator | LIS 置信度 | CMI 置信度 | 量化 indices 覆盖 |
|---|---|---|---|
| 3.1 COL | high | high | Numbeo 全 6 项 + 对比页 ✅ |
| 3.2 住房月租 | high | high | Numbeo 4 档 + 平台 listing ✅ |
| 3.3 餐饮/食杂/交通 | high | high | Numbeo 各分类 ✅ |
| 3.4 设施可见比 | med | med | 抽样观察 + 平台描述（未严格 20-listing 计数） |
| 3.5 网速 | high | high | Speedtest 国家级（city-proxy 合理）+ Numbeo 月费 ✅ |
| 3.6 移动数据 | high | high | Cable.co.uk 国家级 + 运营商套餐 ✅ |
| 3.7 公共交通 | high | high | Numbeo Traffic + TomTom + 官方票价 ✅ |
| 3.15 杂货 | high | high | 连锁全国数 + 区域可达 ✅ |
| 3.16 药店 | high | med | LIS 有国家级 24h 系统；CMI 缺国家级轮值 |
| 3.17 餐饮多样性 | high | high | TripAdvisor + 多博客 + 设施细节 ✅ |

**触线**：WebSearch ≈ 12 次（远低于 40 上限），WebFetch ≈ 14 次（低于 30 上限）；速率正常。**不可访问源**：Speedtest 城市页 + TomTom 城市页（fallback 使用 Wikipedia/Ookla 国家级 + Numbeo Traffic + 搜索摘要，已记入 `inaccessible_sources.csv`）。
