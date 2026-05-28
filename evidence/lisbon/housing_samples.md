# 里斯本 — 住房样本（10 个）

> 警告：本研究**未爬取 Airbnb/Booking 搜索页**。样本来源于公开可访问的页面（Blueground 单 listing、Idealista 列表页 + WebSearch 摘要、博客中提到的具体房源）。  
> Idealista / Flatio 搜索结果页的具体房源未单页抓取，仅作为"该区有 T2 furnished 库存"的存在证明 → 标 confidence: low–medium。  
> 价格区间以 2026 年区域中位 €1,600–€2,200/T2 furnished/月作为参考基线 [S-LIS-042]。

## 摘要

- **Campo de Ourique**：Blueground 至少 3 个 2 卧带家具房源（Rua Maria Pia / Rua Silva Carvalho / Rua do Sol ao Rato），均含空调，部分含电梯/洗衣机 [S-LIS-036][S-LIS-037][S-LIS-038]。
- **Parque das Nações**：Idealista 多个 T2 furnished listing（Distrikt、Rua das Urcas、Av. D. João II 53、Expo Central），80m²+，靠 Vasco da Gama / Gare do Oriente [S-LIS-039]。
- **Belém**：Idealista T2 furnished 起价约 €900/月，多数靠 Belém Tower / Jerónimos 步行可达 [S-LIS-040]。
- **Estrela / Lapa**：Idealista T2 furnished 有库存，部分 1F **无电梯**（与有孩家庭兼容性差）[S-LIS-041]。
- 主要负面信号：无电梯 + 楼梯多、冬季湿冷无中央暖气、霉菌、单层玻璃、cobblestone 周边 [S-LIS-046][S-LIS-047][S-LIS-080]。

---

## 评价框架

每个样本评估：价格、卧室数、洗衣机、Wi-Fi、空调/暖气、电梯、距杂货/医疗/儿童活动、负面评论主题、traffic_light、confidence。

---

## Sample 1 — Campo de Ourique · Rua Maria Pia（Blueground）
- ID: lis-1508488P [S-LIS-036]
- 2 卧 / 1 卫；阳台、空调 [S-LIS-036]
- 可入住：2026-10-03（恰好对应 10 月窗口）
- Wi-Fi / 洗衣机：页面未明示
- 价格：未在抓取页面显示（Blueground 通常需联系，参考区域均价 €1,600–€2,200/月）[S-LIS-042]
- 距杂货：步行 Mercado de Campo de Ourique（市场 + 食肆）< 10 分钟 [S-LIS-026][S-LIS-027]
- 距医疗：Lusíadas Lisboa Uber 10-15 分钟 [S-LIS-018]
- 距儿童活动：Jardim Teófilo Braga 步行可达（Campo de Ourique 内带 2–10 岁游乐场）[S-LIS-027]
- 负面：价格未公开 + 可入住时间锁定 10 月 = 排他性强
- traffic_light：**Yellow**；confidence: medium

## Sample 2 — Campo de Ourique · Rua Silva Carvalho（Blueground）
- ID: lis-1288615P [S-LIS-037]
- 2 卧 / 1 卫；**98 m²**；洗衣机、空调 [S-LIS-037]
- 可入住：2026-06-02（适合 10/11 月起租）
- Wi-Fi / 电梯：未明示
- 距杂货 / 医疗 / 儿童活动：同 Sample 1
- 优势：洗衣机已确认（家庭关键设施）+ 较大面积
- traffic_light：**Green**；confidence: medium

## Sample 3 — Campo de Ourique · Rua do Sol ao Rato（Blueground）
- ID: lis-1288597P [S-LIS-038]
- 2 卧 / 1 卫；**90 m²**；1F **有电梯**、阳台、洗衣机、空调 [S-LIS-038]
- 可入住：2026-05-30
- 优势：电梯 + 洗衣机 + 1 楼（最低升降高度，适合幼儿 + 婴儿车）
- 负面：靠近 Largo do Rato，主路噪音可能（待核）
- traffic_light：**Green**；confidence: medium

## Sample 4 — Parque das Nações · Distrikt 大厦（Idealista 搜索描述）
- 房源描述：T2 with 阳台 + 储藏室 + 停车位，位于 Distrikt 综合体 [S-LIS-039]
- 优势：现代高层、平坦人行道、空气好、靠 CUF Descobertas（24h 儿科）< 10 分钟步行
- 负面：Idealista 单 listing 未单页抓取 → 具体价/家具/Wi-Fi 未确认
- traffic_light：**Yellow**；confidence: low

## Sample 5 — Parque das Nações · Rua das Urcas（Idealista 搜索描述）
- 2 卧 furnished；靠 Campus of Justice、Gare do Oriente、Vasco da Gama Shopping [S-LIS-039]
- 优势：Metro 红线 Oriente 步行 5 分钟；商场内有 Continente 超市
- traffic_light：**Yellow**；confidence: low

## Sample 6 — Parque das Nações · Av. Dom João II 53（Expo Central, Idealista）
- T2、**80 m²**、fully equipped [S-LIS-039]
- 优势：核心广场，靠 Oceanário + Pavilhão do Conhecimento（步行 < 15 分钟）
- traffic_light：**Yellow**；confidence: low

## Sample 7 — Belém · 河景 T2 步行 Belém Tower（Idealista 描述）
- 2 分钟步行到 Tagus 河 + Belém Tower 花园；周边有 cafe / 餐厅 / 超市 / 药店 [S-LIS-040]
- 优势：Belém 主要儿童景点（MAAT、Jerónimos、Pastéis de Belém）步行可达
- 负面：旅游区可能游客密集，部分时段噪音
- traffic_light：**Yellow**；confidence: low

## Sample 8 — Belém · Rua Alexandre Sá Pinto 73（Idealista 描述）
- 2 卧、**65 m²**、整翻新、双层玻璃、近 cozinha furnished [S-LIS-040]
- 优势：**双层玻璃**（冬季隔热关键，缓解里斯本无暖气问题）[S-LIS-046][S-LIS-081]
- 负面：65m² 对 2 大 2 小较紧；具体价未抓
- traffic_light：**Yellow**；confidence: low

## Sample 9 — Belém Loft 翻新 T2 100m²（Idealista 描述）
- 2 卧 loft、100m²、furnished、靠河 [S-LIS-040]
- Idealista 总览：Belém furnished 起价 €900/月（具体房型不定）[S-LIS-040]
- traffic_light：**Yellow**；confidence: low

## Sample 10 — Estrela · ISEG / Santos / Parlamento 附近 T2（Idealista 描述）
- 2 卧 furnished；高天花板（~3.5m）、双层玻璃、装备齐全的厨房 [S-LIS-041]
- 负面：另一同区 listing 明示"1st floor **without elevator**"——对婴儿车与 4.5/2.5 岁孩子是显著摩擦 [S-LIS-041][S-LIS-045]
- traffic_light：**Yellow**（取决于是否选到带电梯）；confidence: low

---

## 跨样本主题

### 常见正面
- 翻新 + 双层玻璃 + 装备齐全的厨房在多个样本出现（Sol ao Rato、Silva Carvalho、Belém Sá Pinto）。
- Parque das Nações 现代化建筑 + 平坦人行道 + 靠 CUF 医疗（持续优势）[S-LIS-028][S-LIS-017]。

### 常见红旗（跨 ≥ 3 样本 / ≥ 3 来源）
- **冬季湿冷 + 无中央暖气 + 霉菌**：>5 来源（expat 论坛、AnchorLess、Atlas Lisboa、Portugalist、We Heart Lisbon）[S-LIS-044][S-LIS-046][S-LIS-047][S-LIS-048][S-LIS-081]。
- **无电梯 + 高楼层 + 婴儿车**：旅游评论 + 博客明示，特别老城区（Estrela 部分 listing 也有）[S-LIS-045][S-LIS-080][S-LIS-041]。
- **Cobblestone + 山坡 + 婴儿车不便**：≥5 个家庭博客一致提到，普遍建议改用 baby carrier [S-LIS-044][S-LIS-045]。
- 电梯故障/狭窄：Tripadvisor 公寓评论 [S-LIS-080]。

### 红黄绿灰 — 按区
| 区 | 住房供应 | 冬季摩擦 | 婴儿车兼容 | 总评 |
|---|---|---|---|---|
| Campo de Ourique | Green | Yellow | Green | **Green**（confidence medium） |
| Parque das Nações | Green | Yellow（新建好一些） | **Green**（最佳） | **Green**（confidence medium） |
| Estrela / Lapa | Yellow | Yellow | Yellow（部分无电梯） | Yellow |
| Belém / Restelo | Yellow | Yellow | Green（平坦河边） | **Green**（confidence low–medium） |
| Alvalade / Areeiro | Yellow（库存待核） | Yellow | Green | Yellow |
| Cascais / Estoril | Yellow（库存待核） | Yellow | Green | Yellow |

---

## 选房 checklist（基于证据综合）
1. **电梯**（电梯故障是评论高频，建议 ≤ 2F 即使有电梯）[S-LIS-080]
2. **双层玻璃 + 暖气来源**（空调反向制热 / 电暖气 / 不依赖燃气）[S-LIS-046][S-LIS-081]
3. **洗衣机** + 厨房齐全
4. **建造年代 ≥ 1980 年**（抗震法规阈值）[S-LIS-024]
5. 步行 ≤ 500m 到超市 + ≤ 800m 到游乐场 + ≤ 15 分钟到 24h 儿科
6. 入住前 1 周向房东确认除湿机可借/在场

---

## 不可访问 / 降级记录
- Airbnb / Booking 搜索结果页：未爬取（按项目约束）。
- Flatio Parque das Nações 当前无 listing → 已记录（无 listing 不等于不可用，但限制了样本数）[来源：WebFetch flatio]。
- Idealista 单房 listing 未抓取（仅依靠 WebSearch 摘要 + 搜索页 URL）→ 标 confidence low–medium。
