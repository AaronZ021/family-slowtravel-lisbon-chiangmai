# 里斯本硬约束证据

## 签证 / 合法停留

```yaml
visa:
  stay_model: "中国护照通常需要葡萄牙/申根短期签证；加拿大护照等免签护照仍受申根 90/180 天规则约束。"
  max_stay_days: "最多 90 天，按整个申根区任意 180 天累计，而非葡萄牙单国。"
  extension_possible: "短期申根签证通常不应计划延期；超过 90 天需要国家签证或其他合法路径。"
  applies_to_chinese_passport: "需要按葡萄牙短期申根签证路径核验和申请。"
  applies_to_canadian_passport: "通常免签短停，但仍受 90/180 天限制。"
  family_complexity: "若家庭成员护照不同，规则、材料、允许停留方式可能不同；必须逐人核验。"
  remote_work_risk: "短期申根签证/免签以旅游、商务、探亲等短停为主；若实际从葡萄牙持续远程工作，应向领馆或移民律师确认。"
  official_sources: [LIS_VISA_01, EU_VISA_01]
  confidence: High
  red_flags:
    - "三个月行程如果精确排满 90 天，航班延误或计算错误会触发超期风险。"
    - "申根天数是区域累计；不能用离开葡萄牙去西班牙等方式重置。"
  next_verification:
    - "用官方申根计算器输入家庭每位成员过去 180 天旅行史。"
    - "按每位护照确认 VFS/领馆材料、预约周期、签证有效期和多次入境。"
```

## 官方安全建议

```yaml
safety:
  canada_advisory_level: "Take normal security precautions"
  us_advisory_summary: "Level 1 - Exercise normal precautions"
  uk_advisory_summary: "未在本轮完整采样；需补 UK FCDO Portugal 页面。"
  region_specific_warnings: "加拿大提示里斯本、波尔图等大城市扒窃、抢包、公共交通和旅游区盗窃；15、25、28 路电车需特别注意。"
  relevance_to_city: "主要是财物和旅游区风险，不是儿童生活红线。"
  relevance_to_family_with_children: "需要住房门窗安全、少带现金、避开拥挤电车和夜间低照明区域。"
  confidence: High
  red_flags:
    - "短租公寓和车辆盗窃/入室风险需作为住房筛选项。"
  sources: [CAN_PT_01, US_PT_01]
```

## 气候 / 空气

```yaml
climate_air:
  best_months: ["March", "April", "October"]
  workable_months: ["January", "February", "November"]
  avoid_months: []
  average_high_temp_by_target_month_f:
    January: 58
    February: 60
    March: 65
    April: 67
    October: 72
    November: 64
  rainy_days_by_target_month:
    January: 7.3
    February: 5.8
    March: 5.3
    April: 6.1
    October: 7.4
    November: 8.4
  humidity_concern: "低到中；冬季湿冷和住房保温/除湿比高温更重要。"
  air_quality_risk: "相对低；城市有 PM2.5/PM10/NO2/O3 等监测网络。"
  child_outdoor_life_impact: "大多数目标月份适合户外日常；11 月和冬季雨天需要室内 fallback。"
  indoor_fallback_importance: "中。"
  confidence: Medium
  red_flags:
    - "冬季雨天和老房保温/潮湿可能影响日常舒适度。"
  sources: [LIS_CLIM_01, LIS_AIR_01, LIS_AIR_02]
```

## 医疗可达性

```yaml
healthcare:
  pediatric_options:
    - name: "Hospital Dona Estefania"
      type: "公立儿童/儿科参考医院"
      official_url: "https://www.ulssjose.min-saude.pt/hospital-dona-estefania/"
      24h_emergency: "需电话确认；社区和二级资料反复指向儿科急诊。"
      pediatric_service: true
      english_service_evidence: "未在官方页确认；公立医院英语不应默认。"
      foreigner_access_evidence: "公立急诊可作为严重情况路径；费用/保险需确认。"
      confidence: Medium
      source_ids: [LIS_HEALTH_01]
    - name: "Hospital CUF Descobertas"
      type: "私立综合医院"
      official_url: "https://www.cuf.pt/hospitais-e-clinicas/hospital-cuf-descobertas-lisboa"
      pediatric_service: true
      english_service_evidence: "未逐医生确认；私立系统对外国人较友好但需核验。"
      confidence: Medium
      source_ids: [LIS_HEALTH_02]
    - name: "Hospital da Luz Lisboa"
      type: "私立医院/24h urgent care"
      official_url: "https://www.hospitaldaluz.pt/lisboa/en/services/urgent-care-24-hours"
      24h_emergency: true
      pediatric_service: "需确认儿科急诊时段和排班。"
      confidence: Medium
      source_ids: [LIS_HEALTH_03]
    - name: "UMC Lisbon Pediatrics"
      type: "私立门诊"
      english_service_evidence: "页面显示可提供 medical coordinator/translation assistance。"
      confidence: Medium
      source_ids: [LIS_HEALTH_04]
  emergency_pathway: "严重症状或夜间急症：112 或 Hospital Dona Estefania / 私立医院急诊；轻中度发热、皮疹、肠胃炎：私立儿科门诊或 CUF/Luz urgent care。"
  routine_child_illness_pathway: "提前建立 1-2 个私立儿科门诊账号，确认英文医生、保险直付和周末时段。"
  biggest_unknowns:
    - "每家医院儿科急诊是否 24h、英文医生是否稳定、等待时间和保险直付。"
  red_flags:
    - "路径存在但不能假设无摩擦；公立儿科高峰等待可能长。"
  confidence: Medium
```

## 住房基线

事实：Flatio、服务式公寓和 Vrbo 样本显示 2 居、厨房、洗衣和 30 天以上中租供应存在，但价格跨度大，核心区成本明显高于清迈。[LISH_01-LISH_10]

解释：里斯本住房不是“找不到”，而是“三个月、适合幼儿、少坡、安静、有洗衣/厨房、电梯或低楼层”的筛选会显著缩小供应。短租公寓安全、押金、噪音、飞行路径、楼梯和潮湿需要逐套核验。

未知：Airbnb/Booking 实时 75-90 晚总价、本地短租法规、冬季供暖/除湿、电梯、窗户安全、儿童床具。

红线：如果预算无法覆盖约 2500-4000 EUR/月的保守中高质量 2BR 区间，里斯本会变成住房风险而不是生活风险。

证据强度：Medium  
来源限制：平台价格动态，未大规模抓取。  
新鲜度：平台搜索结果和页面为 2026-05-27 访问。  
需要人工核验：对 10 个候选 listing 发消息确认 90 晚、儿童、洗衣、供暖、楼层、电梯、噪音和取消政策。
