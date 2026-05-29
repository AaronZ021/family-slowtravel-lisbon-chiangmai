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
.source-badge { display: inline-flex; align-items: center; min-height: 24px; padding: 2px 7px; border-radius: 6px; background: #eef2ff; color: #3730a3; text-decoration: none; font-size: 12px; font-weight: 600; margin: 2px 4px 2px 0; white-space: nowrap; }
.source-badge:hover { outline: 2px solid #818cf8; outline-offset: 1px; text-decoration: none; }
.badges { margin-top: 6px; display: flex; flex-wrap: wrap; gap: 4px; }
.cell-label { margin: 10px 0 4px; font-size: 12px; font-weight: 700; color: var(--muted); }
.cell-block p { margin: 0 0 8px; }
.meta-row { display: flex; flex-wrap: wrap; gap: 8px; margin: 8px 0 10px; }
.meta-pill { display: inline-flex; min-height: 24px; align-items: center; padding: 2px 8px; border-radius: 6px; background: var(--code-bg); border: 1px solid var(--border); color: #333; font-size: 12px; font-weight: 600; }
.evidence-tier { border-left: 4px solid var(--border); padding: 8px 0 2px 10px; margin: 10px 0; }
.official-tier { border-left-color: #2563eb; }
.platform-tier { border-left-color: #65a30d; }
.community-tier { border-left-color: #d97706; }
.source-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 12px; margin-top: 16px; }
.source-card { background: #fff; border: 1px solid var(--border); border-radius: 8px; padding: 12px; font-size: 13px; }
.source-card h3 { margin: 6px 0; font-size: 15px; }
.source-card dl { margin: 0; display: grid; gap: 4px; }
.source-card dl div { display: grid; grid-template-columns: 72px 1fr; gap: 8px; }
.source-card dt { color: var(--muted); }
.source-card dd { margin: 0; overflow-wrap: anywhere; }
"""


def navlinks(active=""):
    items = [
        ("index.html", "首页"),
        ("indicator_evidence_stack.html", "指标证据栈"),
        ("evidence_side_by_side.html", "证据横向对照"),
        ("final_comparison_report.html", "最终对比报告"),
        ("red_flags.html", "红旗清单"),
        ("unknowns_and_next_verifications.html", "未知与下一步"),
        ("comparison_matrix.html", "对比矩阵"),
        ("evidence_lisbon.html", "里斯本证据"),
        ("evidence_chiang_mai.html", "清迈证据"),
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


def read_source_map():
    path = ROOT / "data/sources/sources.csv"
    if not path.exists():
        return {}
    with open(path, newline="", encoding="utf-8") as f:
        return {row["source_id"]: row for row in csv.DictReader(f)}


def expand_source_token(token, sources):
    if "-" not in token:
        return [token]
    import re
    left, right = token.split("-", 1)
    m = re.match(r"^(.*?)(\d+)$", left)
    if not m:
        return [token]
    prefix, start_s = m.groups()
    end_s = right[len(prefix):] if right.startswith(prefix) else right
    if not end_s.isdigit():
        return [token]
    width = max(len(start_s), len(end_s))
    expanded = [f"{prefix}{i:0{width}d}" for i in range(int(start_s), int(end_s) + 1)]
    return expanded if all(sid in sources for sid in expanded) else [token]


def source_badges(source_ids, sources):
    out = []
    for raw in (source_ids or "").replace(",", ";").split(";"):
        token = raw.strip()
        if not token:
            continue
        for sid in expand_source_token(token, sources):
            if sid in sources:
                title = sources[sid].get("title", "")
                out.append(f'<a class="source-badge" href="#src-{html.escape(sid)}" title="{html.escape(title)}">{html.escape(sid)}</a>')
            else:
                out.append(f'<span class="source-badge">{html.escape(sid)}</span>')
    return '<div class="badges">' + " ".join(out) + "</div>" if out else ""


def source_index_cards(source_ids, sources):
    cards = []
    for sid in sorted(source_ids):
        row = sources.get(sid)
        if not row:
            continue
        cards.append(f"""
<article class="source-card" id="src-{html.escape(sid)}">
  <a class="source-badge" href="{html.escape(row['url'])}" target="_blank" rel="noopener">{html.escape(sid)}</a>
  <h3><a href="{html.escape(row['url'])}" target="_blank" rel="noopener">{html.escape(row['title'])}</a></h3>
  <dl>
    <div><dt>类型</dt><dd>{html.escape(row['source_type'])}</dd></div>
    <div><dt>城市</dt><dd>{html.escape(row['city'])}</dd></div>
    <div><dt>维度</dt><dd>{html.escape(row['dimension'])}</dd></div>
    <div><dt>访问</dt><dd>{html.escape(row['accessed_date'])}</dd></div>
    <div><dt>URL</dt><dd><a href="{html.escape(row['url'])}" target="_blank" rel="noopener">{html.escape(row['url'])}</a></dd></div>
  </dl>
</article>
""")
    return '<div class="source-grid">' + "\n".join(cards) + "</div>"


def stack_cell(row, sources, used_ids):
    def badges(col):
        for raw in (row.get(col) or "").replace(",", ";").split(";"):
            token = raw.strip()
            if token:
                used_ids.update(expand_source_token(token, sources))
        return source_badges(row.get(col, ""), sources)

    return f"""
<div class="cell-block">
  <div class="cell-label">当前维度评估</div>
  <p>{html.escape(row['current_dimension_assessment'])}</p>
  <div class="meta-row">
    <span class="meta-pill">证据充分性：{html.escape(row['evidence_sufficiency'])}</span>
    <span class="meta-pill">置信度：{html.escape(row['confidence'])}</span>
  </div>
  <div class="evidence-tier official-tier">
    <div class="cell-label">官方/统计证据</div>
    <p>{html.escape(row['official_stat_evidence'])}</p>
    {badges('official_source_ids')}
  </div>
  <div class="evidence-tier platform-tier">
    <div class="cell-label">平台/地图证据</div>
    <p>{html.escape(row['platform_map_evidence'])}</p>
    {badges('platform_source_ids')}
  </div>
  <div class="evidence-tier community-tier">
    <div class="cell-label">社区反馈 overlay</div>
    <p>{html.escape(row['community_overlay'])}</p>
    {badges('community_source_ids')}
  </div>
  <div class="cell-label">缺口</div>
  <p>{html.escape(row['gaps'])}</p>
  <div class="cell-label">下一步补数</div>
  <p>{html.escape(row['next_data_to_collect'])}</p>
</div>
"""


def indicator_stack_page(csv_path):
    sources = read_source_map()
    with open(csv_path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    by_layer = {}
    for row in rows:
        by_layer.setdefault(row["layer"], {}).setdefault(row["dimension"], {})[row["city"]] = row
    used_ids = set()
    body = [
        '<h1 class="page-title">指标证据栈</h1>',
        '<p class="page-sub">每个小格子先写该城市在该维度的事实含义，再列官方/统计、平台/地图、社区反馈三类证据。证据 ID 是支撑，不替代文字判断。</p>',
        '<div class="callout"><strong>读法</strong>：这里不做城市总评。每行只处理一个维度；每个城市的小格子说明当前证据能支撑什么、哪里不足、下一步补什么。</div>',
    ]
    for layer, dims in by_layer.items():
        body.append(f"<h2>{html.escape(layer)}</h2>")
        body.append("<table><thead><tr><th>维度</th><th>里斯本</th><th>清迈</th></tr></thead><tbody>")
        for dimension, cities in dims.items():
            lis = cities.get("里斯本")
            cmi = cities.get("清迈")
            body.append("<tr>")
            body.append(f"<td><strong>{html.escape(dimension)}</strong></td>")
            body.append(f"<td>{stack_cell(lis, sources, used_ids) if lis else ''}</td>")
            body.append(f"<td>{stack_cell(cmi, sources, used_ids) if cmi else ''}</td>")
            body.append("</tr>")
        body.append("</tbody></table>")
    body.append("<h2>本页来源索引</h2>")
    body.append(source_index_cards(used_ids, sources))
    return wrap_page("指标证据栈", "\n".join(body), "indicator_evidence_stack.html")


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
<h1 class="page-title">里斯本 vs 清迈：家庭 3 个月慢旅基地证据库</h1>
<p class="page-sub">为 2 大人 + 4.5 岁 + 2.5 岁家庭评估两座城市作为约 90 天慢旅基地的可行性。本站列出所有事实证据，每条挂源 ID，判断由读者自行做出。</p>

<div class="callout">
<strong>核心方法论</strong>
<ul>
<li>不按"哪座城赢"评估，按 <strong>生活功能</strong>（住房 / 医疗 / 儿童活动 / 出行 / 物流 / 文化 / 自然 / 社群）逐维度对比</li>
<li>每条事实必须挂 <code>source_id</code>；轶事需 ≥ 5 条独立评论或 ≥ 3 平台才作复现结论</li>
<li>区分 fact / interpretation / unknown / next verification</li>
</ul>
</div>

<h2>主要报告</h2>
<div class="card-grid">
  <div class="card">
    <a href="indicator_evidence_stack.html">
      <span class="tag">新版</span>
      <h3>指标证据栈</h3>
      <p>每个维度按官方/统计、平台/地图、社区反馈 overlay 拆开，并写出证据实际说明的事实。</p>
    </a>
  </div>
  <div class="card">
    <a href="evidence_side_by_side.html">
      <span class="tag">事实对照</span>
      <h3>证据横向对照表</h3>
      <p>18 个维度纯事实左右两栏对照，无判断、无打分。所有事实挂源 ID。</p>
    </a>
  </div>
  <div class="card">
    <a href="final_comparison_report.html">
      <span class="tag">综合报告</span>
      <h3>最终对比报告</h3>
      <p>12 节中文综合报告，含按月份匹配建议与互补组合假设。</p>
    </a>
  </div>
  <div class="card">
    <a href="red_flags.html">
      <span class="tag">风险</span>
      <h3>红旗清单</h3>
      <p>12 项红旗 + 严重度 + 缓解方式（含共享 R0 / 里斯本特有 / 清迈特有）。</p>
    </a>
  </div>
  <div class="card">
    <a href="unknowns_and_next_verifications.html">
      <span class="tag">待核实</span>
      <h3>未知与下一步</h3>
      <p>T-120 / T-90 / T-60 / T-30 / T-7 / 抵达后第 1 周 核实时间表。</p>
    </a>
  </div>
  <div class="card">
    <a href="comparison_matrix.html">
      <span class="tag">矩阵</span>
      <h3>对比矩阵</h3>
      <p>18 维度红黄绿灰 + 置信度 + 关键源 ID。</p>
    </a>
  </div>
</div>

<h2>原始证据（按城市）</h2>
<div class="card-grid">
  <div class="card">
    <a href="evidence_lisbon.html">
      <span class="tag" style="color: var(--lisbon)">里斯本</span>
      <h3>里斯本 7 个证据 markdown</h3>
      <p>硬约束 / 医疗路径 / 住房样本 / 儿童活动 / 出行 / 生活可运营性 / 社区反馈</p>
    </a>
  </div>
  <div class="card">
    <a href="evidence_chiang_mai.html">
      <span class="tag" style="color: var(--chiangmai)">清迈</span>
      <h3>清迈 7 个证据 markdown</h3>
      <p>硬约束 / 医疗路径 / 住房样本 / 儿童活动 / 出行 / 生活可运营性 / 社区反馈</p>
    </a>
  </div>
</div>

<h2>数据规模</h2>
<table>
<thead><tr><th>项</th><th>数量</th></tr></thead>
<tbody>
<tr><td>总源数</td><td>143 条（85 LIS + 58 CMI）</td></tr>
<tr><td>WebSearch 次数</td><td>81 次</td></tr>
<tr><td>WebFetch 次数</td><td>35 次</td></tr>
<tr><td>不可访问源（已降级）</td><td>7 类（Reddit / Airbnb / Flatio / Facebook 等）</td></tr>
<tr><td>Evidence markdown</td><td>14 个（每城 7 个）</td></tr>
<tr><td>报告 markdown</td><td>4 个 + 1 个 CSV 矩阵</td></tr>
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

(SITE / "indicator_evidence_stack.html").write_text(
    indicator_stack_page(ROOT / "reports/indicator_evidence_stack.csv")
)

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
