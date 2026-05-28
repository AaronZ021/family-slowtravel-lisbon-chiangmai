"""Parse v2 evidence files and build indicator matrix CSV.

Each layer file uses a slightly different format; we extract per-indicator
judgment + confidence + sources for both cities.
"""
import re
import csv
from pathlib import Path

ROOT = Path(__file__).parent
EVIDENCE = ROOT / "evidence" / "v2"
OUT_CSV = ROOT / "reports" / "v2_indicator_matrix.csv"

LIGHT_MAP_FULL = {"🟩": "Green", "🟧": "Yellow", "🟥": "Red", "Green": "Green", "Yellow": "Yellow", "Red": "Red"}
CONF_MAP = {"high": "high", "med": "medium", "medium": "medium", "low": "low"}


def normalize_light(s):
    """Extract the first Green/Yellow/Red signal from a string."""
    for sym, val in LIGHT_MAP_FULL.items():
        if sym in s:
            return val
    return ""


def normalize_conf(s):
    s_lower = s.lower().strip()
    for k, v in CONF_MAP.items():
        if k in s_lower:
            return v
    return ""


def parse_layer2(text):
    """Layer 2 format: ## 2.1 indicator title; ### 里斯本/清迈; **判断**: emoji + confidence + **依据**: + **关键源**:"""
    rows = []
    indicator_re = re.compile(r"^##\s+(\d+\.\d+)\s+(.+)$", re.MULTILINE)
    city_re = re.compile(r"^###\s+(里斯本|清迈)", re.MULTILINE)
    # confidence is optional — some indicators give multi-month judgment without explicit confidence
    judge_re = re.compile(r"\*\*判断\*\*[：:]\s*(.+?)(?:\n|$)", re.MULTILINE)
    conf_re = re.compile(r"(?:confidence|置信度)[：:\s]*\*?\*?(high|med(?:ium)?|low)", re.IGNORECASE)
    evidence_re = re.compile(r"\*\*依据\*\*[：:]?\s*([^\n]+)")
    source_re = re.compile(r"\*\*关键源\*\*[：:]?\s*([^\n]+)")

    indicators = list(indicator_re.finditer(text))
    for i, m in enumerate(indicators):
        ind_id, ind_name = m.group(1), m.group(2).strip()
        start = m.end()
        end = indicators[i + 1].start() if i + 1 < len(indicators) else len(text)
        block = text[start:end]
        cities = list(city_re.finditer(block))
        data = {"里斯本": {}, "清迈": {}}
        for j, c in enumerate(cities):
            cname = c.group(1)
            cstart = c.end()
            cend = cities[j + 1].start() if j + 1 < len(cities) else len(block)
            cb = block[cstart:cend]
            jm = judge_re.search(cb)
            if jm:
                judgment_text = jm.group(1)
                data[cname]["light"] = normalize_light(judgment_text)
                # try inline confidence first
                cm = conf_re.search(judgment_text)
                if not cm:
                    # search entire city block
                    cm = conf_re.search(cb)
                if cm:
                    data[cname]["conf"] = normalize_conf(cm.group(1))
                else:
                    data[cname]["conf"] = "high"  # default when not stated (climate facts are deterministic)
                # store judgment text as evidence preview
                data[cname]["judgment_preview"] = re.sub(r"\s+", " ", judgment_text)[:300]
            em = evidence_re.search(cb)
            if em:
                data[cname]["evidence"] = re.sub(r"\s+", " ", em.group(1).strip())[:300]
            elif "judgment_preview" in data[cname]:
                data[cname]["evidence"] = data[cname]["judgment_preview"]
            sm = source_re.search(cb)
            if sm:
                data[cname]["sources"] = re.sub(r"\s+", " ", sm.group(1).strip())[:200]
        rows.append({
            "layer": "Layer 2 · 硬约束",
            "indicator_id": ind_id,
            "indicator_name": ind_name,
            "lisbon_light": data["里斯本"].get("light", ""),
            "lisbon_confidence": data["里斯本"].get("conf", ""),
            "lisbon_evidence": data["里斯本"].get("evidence", ""),
            "lisbon_sources": data["里斯本"].get("sources", ""),
            "chiang_mai_light": data["清迈"].get("light", ""),
            "chiang_mai_confidence": data["清迈"].get("conf", ""),
            "chiang_mai_evidence": data["清迈"].get("evidence", ""),
            "chiang_mai_sources": data["清迈"].get("sources", ""),
        })
    return rows


def parse_layer3_table_per_indicator(text, layer_name):
    """Layer 3a format: ## Indicator 3.X — title; per-indicator markdown table with rows for 里斯本 and 清迈.

    Table columns vary but always end with 判断 | 置信度 | 关键源.
    """
    rows = []
    indicator_re = re.compile(r"^##\s+Indicator\s+(\d+\.\d+)\s*[—\-]\s*(.+)$", re.MULTILINE)
    indicators = list(indicator_re.finditer(text))
    city_row_re = re.compile(r"^\|\s*\*\*(里斯本|清迈)\*\*\s*\|(.+?)\|\s*$", re.MULTILINE)

    # alt format: **里斯本判断**: ... **清迈判断**: ... in plain paragraphs
    paragraph_judge_re = re.compile(r"\*\*(里斯本|清迈)判断\*\*\s*[：:]\s*(.+?)(?=\n\n|\n\*\*|\Z)", re.DOTALL)

    for i, m in enumerate(indicators):
        ind_id, ind_name = m.group(1), m.group(2).strip()
        start = m.end()
        end = indicators[i + 1].start() if i + 1 < len(indicators) else len(text)
        block = text[start:end]
        data = {"里斯本": {}, "清迈": {}}
        for cm in city_row_re.finditer(block):
            cname = cm.group(1)
            cells = [c.strip() for c in cm.group(2).split("|")]
            if len(cells) >= 3:
                judgment_cell = cells[-3]
                conf_cell = cells[-2]
                source_cell = cells[-1]
                data[cname]["light"] = normalize_light(judgment_cell)
                data[cname]["conf"] = normalize_conf(conf_cell)
                data[cname]["evidence"] = re.sub(r"\s+", " ", judgment_cell.replace("**", ""))[:300]
                data[cname]["sources"] = re.sub(r"\s+", " ", source_cell)[:200]
        # fallback: paragraph-style judgments
        if not data["里斯本"].get("light") or not data["清迈"].get("light"):
            for pm in paragraph_judge_re.finditer(block):
                cname = pm.group(1)
                if data[cname].get("light"):
                    continue
                judg_text = pm.group(2)
                data[cname]["light"] = normalize_light(judg_text)
                data[cname]["conf"] = normalize_conf(judg_text) or "high"
                data[cname]["evidence"] = re.sub(r"\s+", " ", judg_text.replace("**", "").replace("·", " · "))[:300]
                src_m = re.search(r"S-(?:LIS|CMI)-\d+(?:\s*,\s*S-(?:LIS|CMI)-\d+)*", judg_text)
                if src_m:
                    data[cname]["sources"] = src_m.group(0)
        rows.append({
            "layer": layer_name,
            "indicator_id": ind_id,
            "indicator_name": ind_name,
            "lisbon_light": data["里斯本"].get("light", ""),
            "lisbon_confidence": data["里斯本"].get("conf", ""),
            "lisbon_evidence": data["里斯本"].get("evidence", ""),
            "lisbon_sources": data["里斯本"].get("sources", ""),
            "chiang_mai_light": data["清迈"].get("light", ""),
            "chiang_mai_confidence": data["清迈"].get("conf", ""),
            "chiang_mai_evidence": data["清迈"].get("evidence", ""),
            "chiang_mai_sources": data["清迈"].get("sources", ""),
        })
    return rows


# Build all rows
all_rows = []

# Layer 2
text = (EVIDENCE / "layer2_hard_constraints.md").read_text()
rows = parse_layer2(text)
print(f"Layer 2: {len(rows)} indicators")
all_rows.extend(rows)

# Layer 3a
text = (EVIDENCE / "layer3a_economics_utilities.md").read_text()
rows = parse_layer3_table_per_indicator(text, "Layer 3a · 经济/物流/网络")
print(f"Layer 3a: {len(rows)} indicators")
all_rows.extend(rows)

# Layer 3b — use 总结表
def parse_layer3b_summary(text):
    """Layer 3b has a 总结表 with: Indicator | 里斯本 | 置信度 | 清迈 | 置信度."""
    rows = []
    m = re.search(r"## 总结表.*?\n\n(\|.*?\|)\n\|[-:|\s]+\|\n((?:\|.*?\|\n)+)", text, re.DOTALL)
    if not m:
        return rows
    body = m.group(2)
    # Map id → name from indicator headers
    ind_name_map = {}
    for hm in re.finditer(r"^##\s+Indicator\s+(\d+\.\d+)\s*[—\-]\s*(.+)$", text, re.MULTILINE):
        ind_name_map[hm.group(1)] = hm.group(2).strip()
    for line in body.strip().split("\n"):
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) >= 5:
            ind_label = cells[0]
            # ind_label like "3.8 Walkability"
            ind_id_match = re.match(r"(\d+\.\d+)", ind_label)
            ind_id = ind_id_match.group(1) if ind_id_match else ""
            ind_name = ind_name_map.get(ind_id, ind_label)
            lis_judge = cells[1]
            lis_conf = cells[2]
            cmi_judge = cells[3]
            cmi_conf = cells[4]
            rows.append({
                "layer": "Layer 3b · 儿童/出行/社群",
                "indicator_id": ind_id,
                "indicator_name": ind_name,
                "lisbon_light": normalize_light(lis_judge),
                "lisbon_confidence": normalize_conf(lis_conf),
                "lisbon_evidence": re.sub(r"\s+", " ", lis_judge)[:300],
                "lisbon_sources": "",  # 3b 总结表无源；可后续补
                "chiang_mai_light": normalize_light(cmi_judge),
                "chiang_mai_confidence": normalize_conf(cmi_conf),
                "chiang_mai_evidence": re.sub(r"\s+", " ", cmi_judge)[:300],
                "chiang_mai_sources": "",
            })
    return rows


text = (EVIDENCE / "layer3b_children_mobility_community.md").read_text()
rows = parse_layer3b_summary(text)
print(f"Layer 3b: {len(rows)} indicators")
all_rows.extend(rows)

# Write CSV
with open(OUT_CSV, "w", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "layer",
            "indicator_id",
            "indicator_name",
            "lisbon_light",
            "lisbon_confidence",
            "lisbon_evidence",
            "lisbon_sources",
            "chiang_mai_light",
            "chiang_mai_confidence",
            "chiang_mai_evidence",
            "chiang_mai_sources",
        ],
    )
    writer.writeheader()
    for r in all_rows:
        writer.writerow(r)

print(f"\n✅ Wrote {OUT_CSV} with {len(all_rows)} indicator rows total")

# Sanity check
missing = [r for r in all_rows if not r["lisbon_light"] or not r["chiang_mai_light"]]
if missing:
    print(f"\n⚠️  {len(missing)} rows missing light:")
    for r in missing:
        print(f"  - {r['indicator_id']} {r['indicator_name']}: LIS={r['lisbon_light']!r} CMI={r['chiang_mai_light']!r}")

# Light distribution
from collections import Counter
lis_counts = Counter(r["lisbon_light"] for r in all_rows if r["lisbon_light"])
cmi_counts = Counter(r["chiang_mai_light"] for r in all_rows if r["chiang_mai_light"])
print(f"\nLight distribution:")
print(f"  Lisbon:    {dict(lis_counts)}")
print(f"  Chiang Mai: {dict(cmi_counts)}")
