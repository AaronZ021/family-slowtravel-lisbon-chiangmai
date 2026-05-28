"""Build static HTML site from markdown reports for GitHub Pages."""
import os
import shutil
from pathlib import Path
import markdown
import csv
import html

ROOT = Path(__file__).parent
SITE = ROOT / "docs"
SITE.mkdir(exist_ok=True)

CSS = """
:root {
  --bg: #fafaf8;
  --fg: #1a1a1a;
  --muted: #666;
  --accent: #b85450;
  --lisbon: #2563eb;
  --chiangmai: #d97706;
  --border: #e5e3dd;
  --code-bg: #f3f1ec;
  --table-stripe: #f7f5f0;
}
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif; color: var(--fg); background: var(--bg); line-height: 1.65; }
header.top { background: #fff; border-bottom: 1px solid var(--border); padding: 14px 24px; position: sticky; top: 0; z-index: 100; backdrop-filter: blur(8px); background: rgba(255,255,255,0.85); }
header.top .inner { max-width: 1200px; margin: 0 auto; display: flex; align-items: baseline; gap: 24px; flex-wrap: wrap; }
header.top h1 { font-size: 17px; margin: 0; font-weight: 600; }
header.top nav { display: flex; gap: 16px; font-size: 14px; flex-wrap: wrap; }
header.top nav a { color: var(--muted); text-decoration: none; }
header.top nav a:hover { color: var(--accent); }
header.top nav a.active { color: var(--fg); font-weight: 600; }
main { max-width: 1200px; margin: 0 auto; padding: 32px 24px 80px; }
.page-title { font-size: 32px; font-weight: 700; margin: 0 0 8px; letter-spacing: -0.5px; }
.page-sub { color: var(--muted); margin: 0 0 32px; font-size: 15px; }
h1 { font-size: 26px; margin: 40px 0 12px; font-weight: 700; letter-spacing: -0.3px; }
h2 { font-size: 21px; margin: 32px 0 12px; font-weight: 700; padding-bottom: 6px; border-bottom: 1px solid var(--border); }
h3 { font-size: 17px; margin: 24px 0 10px; font-weight: 600; }
h4 { font-size: 15px; margin: 18px 0 8px; font-weight: 600; color: var(--muted); }
p { margin: 10px 0; }
ul, ol { padding-left: 22px; margin: 10px 0; }
li { margin: 4px 0; }
strong { font-weight: 600; }
blockquote { border-left: 3px solid var(--accent); margin: 14px 0; padding: 4px 16px; color: #444; background: var(--code-bg); border-radius: 0 6px 6px 0; }
code { font-family: ui-monospace, "SF Mono", Menlo, Consolas, monospace; background: var(--code-bg); padding: 1px 6px; border-radius: 4px; font-size: 90%; }
pre { background: var(--code-bg); padding: 14px 18px; border-radius: 8px; overflow-x: auto; font-size: 13px; }
hr { border: none; border-top: 1px solid var(--border); margin: 32px 0; }
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }

table { border-collapse: collapse; width: 100%; margin: 16px 0; font-size: 14px; background: #fff; border: 1px solid var(--border); border-radius: 6px; overflow: hidden; }
th, td { padding: 10px 14px; text-align: left; vertical-align: top; border-bottom: 1px solid var(--border); }
th { background: var(--code-bg); font-weight: 600; font-size: 13px; }
tr:last-child td { border-bottom: none; }
tr:nth-child(even) td { background: var(--table-stripe); }

/* color coded source IDs */
.s-lis { color: var(--lisbon); font-weight: 500; }
.s-cmi { color: var(--chiangmai); font-weight: 500; }

/* card grid on index */
.card-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 16px; margin: 24px 0; }
.card { background: #fff; border: 1px solid var(--border); border-radius: 10px; padding: 20px; transition: all 0.2s; }
.card:hover { border-color: var(--accent); transform: translateY(-2px); box-shadow: 0 4px 16px rgba(0,0,0,0.05); }
.card a { color: var(--fg); }
.card a:hover { text-decoration: none; }
.card h3 { margin: 0 0 6px; font-size: 16px; color: var(--accent); }
.card p { margin: 0; color: var(--muted); font-size: 13px; }
.card .tag { font-size: 11px; background: var(--code-bg); padding: 2px 8px; border-radius: 10px; display: inline-block; margin-bottom: 8px; color: var(--muted); }

/* footer */
footer { max-width: 1200px; margin: 40px auto 24px; padding: 0 24px; color: var(--muted); font-size: 13px; }

/* mobile */
@media (max-width: 640px) {
  header.top .inner { flex-direction: column; gap: 8px; align-items: flex-start; }
  .page-title { font-size: 24px; }
  table { font-size: 13px; }
  th, td { padding: 8px 10px; }
}

/* highlight rows where lisbon/chiang_mai obviously differ — handled by inline data attrs */
.callout { background: #fff7ed; border: 1px solid #fed7aa; padding: 12px 18px; border-radius: 8px; margin: 16px 0; }
.callout.warn { background: #fef2f2; border-color: #fecaca; }
.callout.ok { background: #f0fdf4; border-color: #bbf7d0; }

/* v2 indicator chips */
.chip { display: inline-block; padding: 2px 10px; border-radius: 12px; font-size: 12px; font-weight: 600; }
.chip.green { background: #d1fae5; color: #065f46; }
.chip.yellow { background: #fef3c7; color: #78350f; }
.chip.red { background: #fee2e2; color: #991b1b; }
.chip.gray { background: #e5e7eb; color: #4b5563; }
.conf { font-size: 11px; color: var(--muted); margin-left: 4px; }

/* v2 matrix table */
table.v2-matrix { font-size: 13px; }
table.v2-matrix th { font-size: 12px; }
table.v2-matrix td.judge { text-align: center; min-width: 110px; }
table.v2-matrix td.evidence { color: #444; font-size: 12.5px; }
table.v2-matrix th.layer-cell { background: #ede9d8; }

/* layer-header divider row */
tr.layer-header td { background: #ede9d8; font-weight: 700; padding: 14px; font-size: 14px; }

/* distribution bar */
.dist-bar { display: flex; height: 28px; border-radius: 14px; overflow: hidden; margin: 12px 0; font-size: 12px; font-weight: 600; color: white; }
.dist-bar .seg { display: flex; align-items: center; justify-content: center; }
.dist-bar .seg.green { background: #10b981; }
.dist-bar .seg.yellow { background: #f59e0b; }
.dist-bar .seg.red { background: #ef4444; }
"""


def navlinks(active=""):
    items = [
        ("index.html", "首页"),
        ("v2_matrix.html", "v2 Indicator 矩阵"),
        ("v2_layer2.html", "Layer 2 硬约束"),
        ("v2_layer3a.html", "Layer 3a 经济/物流"),
        ("v2_layer3b.html", "Layer 3b 儿童/出行"),
        ("v2_layer4.html", "Layer 4 社区主题"),
        ("evidence_side_by_side.html", "v1 横向对照"),
        ("evidence_lisbon.html", "v1 里斯本证据"),
        ("evidence_chiang_mai.html", "v1 清迈证据"),
    ]
    out = []
    for href, label in items:
        cls = ' class="active"' if href == active else ""
        out.append(f'      <a href="{href}"{cls}>{label}</a>')
    return "\n".join(out)


def wrap_page(title, body_html, active=""):
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} · 里斯本 vs 清迈 家庭慢旅基地</title>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='80' font-size='80'>🏝️</text></svg>">
<style>{CSS}</style>
</head>
<body>
<header class="top">
  <div class="inner">
    <h1>🏝️ 里斯本 vs 清迈 · 家庭慢旅基地</h1>
    <nav>
{navlinks(active)}
    </nav>
  </div>
</header>
<main>
{body_html}
</main>
<footer>
  调研日期 2026-05-28 · 143 个来源（85 LIS / 58 CMI）· 14 个证据 markdown · <a href="https://github.com/AaronZ021/family-slowtravel-lisbon-chiangmai">GitHub</a>
</footer>
</body>
</html>
"""


def colorize_sources(html_text):
    """Wrap source IDs in colored spans."""
    import re
    html_text = re.sub(r'\[S-LIS-(\d+)\]', r'<span class="s-lis">[S-LIS-\1]</span>', html_text)
    html_text = re.sub(r'\[S-CMI-(\d+)\]', r'<span class="s-cmi">[S-CMI-\1]</span>', html_text)
    return html_text


def md_to_html(md_path, title, active):
    with open(md_path) as f:
        md = f.read()
    body = markdown.markdown(
        md,
        extensions=["tables", "fenced_code", "toc"],
        extension_configs={"toc": {"permalink": "¶"}},
    )
    body = colorize_sources(body)
    return wrap_page(title, body, active)


def csv_to_html(csv_path, title, active, intro=""):
    with open(csv_path) as f:
        rows = list(csv.reader(f))
    if not rows:
        return wrap_page(title, "<p>（空）</p>", active)
    headers = rows[0]
    body_html = [f'<h1 class="page-title">{html.escape(title)}</h1>']
    if intro:
        body_html.append(f'<p class="page-sub">{intro}</p>')
    body_html.append("<table>")
    body_html.append("<thead><tr>")
    for h in headers:
        body_html.append(f"<th>{html.escape(h)}</th>")
    body_html.append("</tr></thead><tbody>")
    for row in rows[1:]:
        body_html.append("<tr>")
        for cell in row:
            cell_html = html.escape(cell).replace("\n", "<br>")
            body_html.append(f"<td>{cell_html}</td>")
        body_html.append("</tr>")
    body_html.append("</tbody></table>")
    return wrap_page(title, colorize_sources("\n".join(body_html)), active)


def combined_evidence_page(city, files, title, active):
    """Combine all evidence markdown for one city into a single page."""
    body_parts = [f'<h1 class="page-title">{html.escape(title)}</h1>']
    body_parts.append('<p class="page-sub">本页汇总该城所有 evidence markdown 文件，按维度组织。</p>')
    toc = ['<div class="callout"><strong>本页章节</strong><ul>']
    section_id_pairs = []
    for fname, label in files:
        sid = fname.replace(".md", "").replace("/", "_")
        section_id_pairs.append((sid, label))
        toc.append(f'<li><a href="#{sid}">{label}</a></li>')
    toc.append("</ul></div>")
    body_parts.append("\n".join(toc))

    for fname, label in files:
        sid = fname.replace(".md", "").replace("/", "_")
        md_path = ROOT / "evidence" / city / fname
        if not md_path.exists():
            continue
        with open(md_path) as f:
            md = f.read()
        # demote heading levels by 1 (so file's "# Title" becomes h2)
        md_lines = []
        for ln in md.splitlines():
            if ln.startswith("# "):
                md_lines.append(f'<h2 id="{sid}">{html.escape(ln[2:])}</h2>')
            elif ln.startswith("## "):
                md_lines.append(f"### {ln[3:]}")
            elif ln.startswith("### "):
                md_lines.append(f"#### {ln[4:]}")
            else:
                md_lines.append(ln)
        section_md = "\n".join(md_lines)
        section_html = markdown.markdown(
            section_md,
            extensions=["tables", "fenced_code"],
        )
        body_parts.append(f'<section id="{sid}">{section_html}</section>')
        body_parts.append("<hr>")
    return wrap_page(title, colorize_sources("\n".join(body_parts)), active)


# === Build pages ===

# Index
index_body = """
<h1 class="page-title">里斯本 vs 清迈：家庭 3 个月慢旅基地 · v2 指标体系</h1>
<p class="page-sub">为 2 大人 + 4.5 岁 + 2.5 岁家庭评估两座城市作为约 90 天慢旅基地的可行性。本站基于 v2 方法论：<strong>每个 indicator 用官方/统计/平台指数支撑判断</strong>，社区反馈作为佐证。不输出城市级总评，判断只到 indicator 级。</p>

<div class="callout">
<strong>v2 方法论修正</strong>
<ul>
<li><strong>按 Layer 2 / 3 / 4 分层</strong>：硬约束 / 生活可运营性 / 纯社区主题</li>
<li>每个 <strong>indicator</strong> 必须有官方/平台量化指数（Numbeo / IQAir / EF EPI / Speedtest / JCI / TomTom 等 NomadList 风格），不停在"找到 N 个 X"</li>
<li>社区反馈集成进 indicator 作佐证（≥3 平台 OR ≥5 来源），同时独立成 Layer 4 主题</li>
<li>不输出"哪座城赢"；每个 indicator 给一个判断（Green/Yellow/Red）+ 置信度</li>
</ul>
</div>

<h2>v2 主要交付</h2>
<div class="card-grid">
  <div class="card">
    <a href="v2_matrix.html">
      <span class="tag">核心矩阵</span>
      <h3>v2 Indicator 矩阵</h3>
      <p>37 个 indicators × 2 城 × 判断 + 置信度 + 关键源，按 Layer 分组。</p>
    </a>
  </div>
  <div class="card">
    <a href="v2_layer2.html">
      <span class="tag">Layer 2</span>
      <h3>硬约束</h3>
      <p>17 个 indicators：签证 / 安全 / 气候 / 空气 / 医疗 / 传染病 / 灾害</p>
    </a>
  </div>
  <div class="card">
    <a href="v2_layer3a.html">
      <span class="tag">Layer 3a</span>
      <h3>经济 / 物流 / 网络</h3>
      <p>10 个 indicators：物价 / 房租 / 网速 / 移动数据 / 公交 / 杂货 / 药店 / 餐饮</p>
    </a>
  </div>
  <div class="card">
    <a href="v2_layer3b.html">
      <span class="tag">Layer 3b</span>
      <h3>儿童 / 出行 / 社群</h3>
      <p>10 个 indicators：walkability / 婴儿车 / car seat / 户外 / 室内 / childcare / 英语 / 社群 / 泡沫</p>
    </a>
  </div>
  <div class="card">
    <a href="v2_layer4.html">
      <span class="tag">Layer 4</span>
      <h3>社区主题 + Verbatim</h3>
      <p>撤离信号 / 留下信号 / 季节切换 / 80+ verbatim / 6 条反共识</p>
    </a>
  </div>
</div>

<h2>v1 历史交付（保留）</h2>
<div class="card-grid">
  <div class="card">
    <a href="evidence_side_by_side.html">
      <span class="tag">v1 事实对照</span>
      <h3>18 维度横向对照表</h3>
      <p>v1 纯事实左右两栏对照（已被 v2 取代但保留参考）。</p>
    </a>
  </div>
  <div class="card">
    <a href="evidence_lisbon.html">
      <span class="tag" style="color: var(--lisbon)">里斯本</span>
      <h3>里斯本 v1 全部证据</h3>
      <p>7 个证据 markdown 文件汇总</p>
    </a>
  </div>
  <div class="card">
    <a href="evidence_chiang_mai.html">
      <span class="tag" style="color: var(--chiangmai)">清迈</span>
      <h3>清迈 v1 全部证据</h3>
      <p>7 个证据 markdown 文件汇总</p>
    </a>
  </div>
</div>

<h2>v2 数据规模</h2>
<table>
<thead><tr><th>项</th><th>数量</th></tr></thead>
<tbody>
<tr><td>v2 indicators</td><td>37 个（Layer 2: 17 + Layer 3a: 10 + Layer 3b: 10）</td></tr>
<tr><td>v2 新增源</td><td>115 条（LIS +41 / CMI +74）→ 总计 227 条（126 LIS + 101 CMI）</td></tr>
<tr><td>关键平台指数</td><td>Numbeo / IQAir / EF EPI / Speedtest / TomTom / JCI / Cable.co.uk / Schengen 统计</td></tr>
<tr><td>Layer 4 verbatim</td><td>80+ 条 + 6 条反共识</td></tr>
</tbody>
</table>

<h2>家庭背景</h2>
<ul>
<li>2 大人 + 4.5 岁孩子 + 2.5 岁孩子</li>
<li>持有人：中国护照，加拿大居民（配偶/孩子护照情况 to_verify）</li>
<li>目标停留：约 90 天</li>
<li>目标月份候选：1、2、3、4、10、11 月</li>
<li>风险容忍：低到中；Childcare 可选不必需；不必需远程工作</li>
</ul>
"""

(SITE / "index.html").write_text(wrap_page("首页", index_body, "index.html"))

# Reports
report_pages = [
    ("reports/evidence_side_by_side.md", "evidence_side_by_side.html", "证据横向对照表"),
    ("reports/final_comparison_report.md", "final_comparison_report.html", "最终对比报告"),
    ("reports/red_flags.md", "red_flags.html", "红旗清单"),
    ("reports/unknowns_and_next_verifications.md", "unknowns_and_next_verifications.html", "未知与下一步核实"),
]
for md, out, title in report_pages:
    (SITE / out).write_text(md_to_html(ROOT / md, title, out))

# Comparison matrix CSV → HTML
(SITE / "comparison_matrix.html").write_text(
    csv_to_html(
        ROOT / "reports/comparison_matrix.csv",
        "对比矩阵",
        "comparison_matrix.html",
        intro="18 个维度红黄绿灰 + 置信度 + 关键源 ID。Status 仅作快速比较，详细事实见证据横向对照表。",
    )
)

# Evidence pages (combined per city)
lisbon_files = [
    ("hard_constraints.md", "硬约束（签证 / 安全 / 气候空气 / 医疗基线 / 住房基线）"),
    ("healthcare_pathway.md", "医疗路径（儿科 / 急诊 / 英文医疗）"),
    ("housing_samples.md", "住房样本（10 个）"),
    ("child_activity_ecosystem.md", "儿童活动生态"),
    ("mobility.md", "移动性"),
    ("life_operability.md", "生活可运营性"),
    ("community_feedback.md", "社区反馈"),
]
(SITE / "evidence_lisbon.html").write_text(
    combined_evidence_page("lisbon", lisbon_files, "里斯本 · 全部证据", "evidence_lisbon.html")
)
(SITE / "evidence_chiang_mai.html").write_text(
    combined_evidence_page("chiang_mai", lisbon_files, "清迈 · 全部证据", "evidence_chiang_mai.html")
)

# === v2 pages ===

def chip_html(light, conf=""):
    if not light:
        return '<span class="chip gray">—</span>'
    cls = light.lower()
    conf_html = f'<span class="conf">{html.escape(conf)}</span>' if conf else ""
    return f'<span class="chip {cls}">{html.escape(light)}</span>{conf_html}'


def v2_matrix_page():
    """Combined v2 indicator matrix table."""
    rows = list(csv.DictReader(open(ROOT / "reports/v2_indicator_matrix.csv")))
    body = ['<h1 class="page-title">v2 Indicator 矩阵</h1>']
    body.append('<p class="page-sub">37 个 indicators × 2 城；每行一个 indicator。判断与置信度基于官方/平台指数 + 社区佐证。判断只到 indicator 级，不输出城市总评。</p>')

    # Distribution bars
    from collections import Counter
    lis_c = Counter(r["lisbon_light"] for r in rows if r["lisbon_light"])
    cmi_c = Counter(r["chiang_mai_light"] for r in rows if r["chiang_mai_light"])
    total = len(rows)
    def bar(c):
        parts = []
        for k in ["Green", "Yellow", "Red"]:
            n = c.get(k, 0)
            if n:
                pct = n / total * 100
                parts.append(f'<div class="seg {k.lower()}" style="width:{pct}%">{k} {n}</div>')
        return f'<div class="dist-bar">{"".join(parts)}</div>'

    body.append(f'<h3>里斯本（{total} indicators）</h3>{bar(lis_c)}')
    body.append(f'<h3>清迈（{total} indicators）</h3>{bar(cmi_c)}')

    # Group by layer
    body.append('<table class="v2-matrix"><thead><tr>')
    body.append('<th>ID</th><th>Indicator</th><th>里斯本</th><th>里斯本 依据</th><th>清迈</th><th>清迈 依据</th>')
    body.append('</tr></thead><tbody>')

    current_layer = None
    for r in rows:
        if r["layer"] != current_layer:
            current_layer = r["layer"]
            body.append(f'<tr class="layer-header"><td colspan="6">{html.escape(current_layer)}</td></tr>')
        body.append("<tr>")
        body.append(f'<td><strong>{html.escape(r["indicator_id"])}</strong></td>')
        body.append(f'<td>{html.escape(r["indicator_name"])}</td>')
        body.append(f'<td class="judge">{chip_html(r["lisbon_light"], r["lisbon_confidence"])}</td>')
        body.append(f'<td class="evidence">{colorize_sources(html.escape(r["lisbon_evidence"]))}<br><small>{colorize_sources(html.escape(r["lisbon_sources"]))}</small></td>')
        body.append(f'<td class="judge">{chip_html(r["chiang_mai_light"], r["chiang_mai_confidence"])}</td>')
        body.append(f'<td class="evidence">{colorize_sources(html.escape(r["chiang_mai_evidence"]))}<br><small>{colorize_sources(html.escape(r["chiang_mai_sources"]))}</small></td>')
        body.append("</tr>")
    body.append("</tbody></table>")
    return wrap_page("v2 Indicator 矩阵", "\n".join(body), "v2_matrix.html")


(SITE / "v2_matrix.html").write_text(v2_matrix_page())

# Individual v2 layer pages (just render the markdown evidence)
v2_layer_pages = [
    ("evidence/v2/layer2_hard_constraints.md", "v2_layer2.html", "Layer 2 · 硬约束"),
    ("evidence/v2/layer3a_economics_utilities.md", "v2_layer3a.html", "Layer 3a · 经济 / 物流 / 网络"),
    ("evidence/v2/layer3b_children_mobility_community.md", "v2_layer3b.html", "Layer 3b · 儿童 / 出行 / 社群"),
    ("evidence/v2/layer4_community_themes.md", "v2_layer4.html", "Layer 4 · 社区主题 + Verbatim"),
]
for md, out, title in v2_layer_pages:
    (SITE / out).write_text(md_to_html(ROOT / md, title, out))

# 404 for SPA niceness
(SITE / "404.html").write_text(
    wrap_page(
        "404",
        '<h1 class="page-title">404</h1><p>页面不存在 · <a href="index.html">回首页</a></p>',
        "",
    )
)

# .nojekyll so GitHub Pages serves files literally
(SITE / ".nojekyll").write_text("")

print(f"✅ Built {len(list(SITE.glob('*.html')))} HTML pages in {SITE}")
for f in sorted(SITE.glob("*.html")):
    print(f"  - {f.name} ({f.stat().st_size // 1024} KB)")
