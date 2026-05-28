# 清迈硬约束证据

## 签证 / 合法停留

```yaml
visa:
  stay_model: "保守模型是旅游签证 TR 60 天 + 在泰国境内申请 30 天延期；另有 DTV 可覆盖远程工作和家属但门槛更高。"
  max_stay_days: "TR 模型通常可做到约 90 天，但必须确认每位护照适用性和延期规则。"
  extension_possible: "旅游签延期 30 天需在泰国移民局申请；不能假设自动批准。"
  applies_to_chinese_passport: "必须用 Thai e-Visa/领馆逐人核验；2026 免签政策处于调整期。"
  applies_to_canadian_passport: "可能有免签路径，但 2026 年 5 月 TAT 已提示 60 天免签调整待公告，不能作为三个月计划核心。"
  family_complexity: "若护照不同，免签、旅游签、DTV 家属路径可能不同。"
  remote_work_risk: "旅游签/免签不应作为稳定远程工作合规依据；DTV 官方页面显示 workcation 和 spouse/dependent children 类别，但申请材料需逐领区确认。"
  official_sources: [TH_VISA_01, TH_VISA_02, TH_VISA_03, TH_DTV_01]
  confidence: Medium
  red_flags:
    - "泰国 2026 免签天数存在政策变动信号；不能用旧攻略确定。"
    - "三个月模型依赖延期时，必须留出移民局办理时间和拒绝/材料补充预案。"
  next_verification:
    - "在 Thai e-Visa 官网按每个家庭成员护照、加拿大居住地和计划天数跑一次 eligibility。"
    - "联系泰国温哥华/渥太华领馆确认中国护照加拿大居民的 TR 材料、儿童材料和延期路径。"
```

## 官方安全建议

```yaml
safety:
  canada_advisory_level: "Exercise a high degree of caution"
  us_advisory_summary: "Level 2 - Exercise increased caution; southern provinces and Cambodia border warnings are not Chiang Mai-specific."
  uk_advisory_summary: "FCDO 对部分边境/南部地区有 avoid travel / all but essential travel 警告；非清迈核心风险。"
  region_specific_warnings: "清迈不在主要冲突区域，但加拿大页面明确提示 Bangkok 和 Chiang Mai 等城市空气污染可达有害水平，北部农业燃烧影响空气。"
  relevance_to_city: "安全红线更多来自空气、交通和道路，而非治安。"
  relevance_to_family_with_children: "儿童在高 PM2.5 日应减少户外活动，住房需配空气净化器，行程避开 3-4 月。"
  confidence: High
  red_flags:
    - "如果目标月份覆盖 3 月或 4 月，空气污染可能直接破坏儿童户外生活。"
  sources: [CAN_TH_01, US_TH_01, UK_TH_01, CM_AIR_02]
```

## 气候 / 空气

```yaml
climate_air:
  best_months: ["November", "December", "January"]
  workable_months: ["October", "February"]
  avoid_months: ["March", "April"]
  average_high_temp_by_target_month_f:
    January: 85
    February: 90
    March: 95
    April: 97
    October: 88
    November: 86
  rainy_days_by_target_month:
    January: 0.5
    February: 0.8
    March: 2.2
    April: 7.0
    October: 10.0
    November: 3.4
  humidity_concern: "雨季和热季高；10 月仍有雨季尾巴，4 月极热。"
  air_quality_risk: "高季节性风险；IQAir 和加拿大官方均指向清迈烟季/农业燃烧。"
  child_outdoor_life_impact: "11-1 月较强；2 月开始不确定；3-4 月可能需要全天候室内 fallback。"
  indoor_fallback_importance: "很高，尤其烟季和热季。"
  confidence: High
  red_flags:
    - "3 月、4 月不建议作为一家四口三个月慢旅行核心月份。"
    - "若必须 2-4 月，需空气净化住房、N95/儿童口罩、室内活动预算和撤离到南部/海边预案。"
  sources: [CM_CLIM_01, CM_AIR_01, CM_AIR_02, CM_AIR_03]
```

## 医疗可达性

```yaml
healthcare:
  pediatric_options:
    - name: "Bangkok Hospital Chiang Mai Pediatric Center"
      type: "私立医院儿科中心"
      official_url: "https://www.bangkokhospital.com/en/chiangmai/center-clinic/child-wellness/pediatric-center-bcm/chivawattana-card-bcm"
      24h_emergency: true
      pediatric_service: true
      english_service_evidence: "英文官网面向国际患者；仍需确认具体医生。"
      foreigner_access_evidence: "私立医院系统，外国人可访问概率高。"
      confidence: High
      source_ids: [CM_HEALTH_01, CM_HEALTH_02]
    - name: "Chiangmai Hospital Pediatric Clinic"
      type: "医院儿科门诊"
      official_url: "https://www.chiangmai-hospital.com/en/our-services/outpatient-department/pediatric-clinic"
      pediatric_service: true
      confidence: Medium
      source_ids: [CM_HEALTH_03]
    - name: "Expat-recommended pediatricians"
      type: "社区推荐路径"
      english_service_evidence: "Reddit 讨论称多家医院有英语工作人员和推荐儿科医生。"
      confidence: Low
      source_ids: [CM_HEALTH_04]
  emergency_pathway: "严重症状：1669 或 Bangkok Hospital Chiang Mai emergency；轻中度儿童病：Bangkok Hospital 儿科中心 / Chiangmai Hospital pediatric clinic。"
  routine_child_illness_pathway: "入住后先注册私立医院，保存儿科中心和急诊电话，确认保险/付款。"
  biggest_unknowns:
    - "儿科专科等待时间、保险直付、各候选区域到医院的实际高峰车程。"
  red_flags:
    - "医疗本身不是清迈红线；烟季导致呼吸道问题的概率才是关键风险。"
  confidence: High
```

## 住房基线

事实：清迈有月租公寓、服务式公寓、2BR condo 和酒店式套房样本，价格和供应明显比里斯本友好；Nimman、Old City edge、Riverside、Hang Dong 均有可行样本。[CMH_01-CMH_10]

解释：清迈住房优势不等于低风险。对本家庭更关键的是：是否在烟季有空气净化器、是否靠近可重复儿童活动、是否避开飞机噪音/夜生活/主路、是否有泳池或安全公共区、是否有可靠洗衣。

未知：短租 75-90 晚合同、押金、儿童安全、净化器、实际噪音、蚊虫/霉味、Grab 到医院和儿童场所的高峰车程。

红线：如果目标月覆盖 3-4 月，住房必须具备空气净化和高质量空调，否则不宜依赖清迈。

证据强度：Medium  
来源限制：平台价格动态；未大规模抓取 Airbnb/Booking。  
新鲜度：2026-05-27 访问。  
需要人工核验：发消息确认 90 晚、空气净化器、儿童、泳池、洗衣、噪音和取消政策。
