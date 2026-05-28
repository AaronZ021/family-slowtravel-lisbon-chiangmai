# 里斯本儿童日常活动生态

## 室外日常释放

| area | repeatable options | age fit | parent friction | sources |
|---|---|---|---|---|
| Campo de Ourique | Jardim da Parada / Teofilo Braga playground, Jardim da Estrela 10-20 分钟范围, Mercado de Campo de Ourique 周边日常 | 2.5 和 4.5 均可 | 部分坡和人行道需核验 | LIS_CHILD_05, LIS_CHILD_08, LIS_COMM_04 |
| Estrela / Lapa | Jardim da Estrela 是强锚点：公园、儿童游乐、草地、咖啡亭/家庭使用信号 | 2.5 和 4.5 均强 | 周边坡度和婴儿车路线需逐街看 | LIS_CHILD_04, LIS_CHILD_08, LIS_COMM_04 |
| Parque das Nacoes | 河滨步道、平坦区域、儿童游乐点、Oceanario 和科学馆周边 | 2.5 和 4.5 均强 | 更现代但本地生活感弱 | LIS_CHILD_07, LIS_CHILD_09 |
| Belem / Restelo | 河滨、文化设施、花园、热带植物园和开放空间 | 4.5 较强，2.5 可行 | 生活服务密度和交通需核验 | LIS_CHILD_05, LIS_CHILD_07 |

## 室内 fallback

- SandCastle：室内 playground + family/work cafe；4 岁以上可 drop-off，4 岁以下需成人陪同。[LIS_CHILD_01]
- Teddy and Friends：室内儿童游乐空间，适合作为雨天或父母恢复时间候选。[LIS_CHILD_06]
- Petit Cabanon：Parque das Nacoes 亲子咖啡/室内游乐概念信号，但需确认当前营业和年龄规则。[LIS_CHILD_03]
- Oceanario family programs：0-5 岁均有家庭项目；可作为天气差时的重复/半重复文化活动，不是普通日常游乐场。[LIS_CHILD_07]
- 商场/图书馆/泳池：本轮未做充分采样，列为下一步核验。

## 结构化活动与社交

- Wooki sensory playgroups 面向婴幼儿至 5 岁，适合两个孩子至少部分参与。[LIS_CHILD_02]
- Lisbon Parents and Kids Meetup 是公开 parent-child social signal。[LIS_CHILD_10, LIS_COMM_01]
- Lisbon for Parents / Pearl Club 显示外国家庭 parent network 存在，但部分信息可能过时。[LIS_COMM_02, LIS_COMM_03]

## 自然 / 开放式体验

日常自然：Jardim da Estrela、Parque das Nacoes 河滨、Belem 河滨。  
周度自然：Monsanto、Cascais/Estoril 海边、Costa da Caparica、Quinta das Conchas 等需下一轮地图核验。  
文化嵌入：Oceanario、博物馆、市场、公共交通、电车/渡轮可嵌入日常，但不应排成景点清单。[LIS_CHILD_07, LIS_MOB_01]

## Repeatability summary

```yaml
repeatability_summary:
  Campo_de_Ourique:
    daily_repeatable_options_count: 3
    weekly_repeatable_options_count: 4
    indoor_fallback_count: 2
    parent_friendly_count: 3
    stroller_or_transport_risk: "Yellow - hills/cobblestones"
    overall_child_daily_life_signal: "Green/Medium if housing is near flat route to park and groceries"
  Estrela_Lapa:
    daily_repeatable_options_count: 2
    weekly_repeatable_options_count: 4
    indoor_fallback_count: 2
    parent_friendly_count: 3
    stroller_or_transport_risk: "Yellow"
    overall_child_daily_life_signal: "Green/Medium near Jardim da Estrela; otherwise slope-sensitive"
  Parque_das_Nacoes:
    daily_repeatable_options_count: 4
    weekly_repeatable_options_count: 4
    indoor_fallback_count: 3
    parent_friendly_count: 4
    stroller_or_transport_risk: "Green"
    overall_child_daily_life_signal: "Green/Medium; strongest low-friction child logistics"
  Belem_Restelo:
    daily_repeatable_options_count: 2
    weekly_repeatable_options_count: 4
    indoor_fallback_count: 1
    parent_friendly_count: 3
    stroller_or_transport_risk: "Yellow"
    overall_child_daily_life_signal: "Yellow/Medium; nature/culture strong but daily services need mapping"
```

证据强度：Medium  
来源限制：未做 Google Maps 照片逐点核验；部分博客/社区来源为低置信。  
新鲜度：2026-05-27 搜集。  
需要人工核验：每个候选区用地图筛出 1km 内超市、药房、公园、厕所、婴儿车路线和 5 个雨天去处。
