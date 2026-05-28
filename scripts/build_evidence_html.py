#!/usr/bin/env python3
import csv
import html
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCES_CSV = ROOT / "data" / "sources" / "sources.csv"
CROSSWALK_CSV = ROOT / "reports" / "evidence_crosswalk.csv"
DOCS_INDEX = ROOT / "docs" / "index.html"
REPORT_HTML = ROOT / "reports" / "evidence_crosswalk.html"


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def esc(value):
    return html.escape(value or "", quote=True)


def source_tokens(value):
    if not value:
        return []
    cleaned = value.replace(",", ";")
    tokens = []
    for token in cleaned.split(";"):
        token = token.strip()
        if not token:
            continue
        tokens.append(token)
    return tokens


def expand_range(token, sources):
    if "-" not in token:
        return [token]
    left, right = token.split("-", 1)
    prefix = ""
    for i, ch in enumerate(left):
        if ch.isdigit():
            prefix = left[:i]
            left_num = left[i:]
            break
    else:
        return [token]
    if not right.startswith(prefix):
        right_num = right
    else:
        right_num = right[len(prefix):]
    if not (left_num.isdigit() and right_num.isdigit()):
        return [token]
    width = max(len(left_num), len(right_num))
    start, end = int(left_num), int(right_num)
    if start > end or end - start > 50:
        return [token]
    expanded = [f"{prefix}{str(i).zfill(width)}" for i in range(start, end + 1)]
    if any(item not in sources for item in expanded):
        return [token]
    return expanded


def source_badges(value, sources):
    badges = []
    for token in source_tokens(value):
        expanded = expand_range(token, sources)
        if len(expanded) > 1:
            badges.append(
                '<span class="range">'
                + " ".join(source_badges(";".join(expanded), sources))
                + "</span>"
            )
            continue
        sid = expanded[0]
        src = sources.get(sid)
        if src:
            title = f"{src.get('title','')} | {src.get('source_type','')} | {src.get('accessed_date','')}"
            badges.append(
                f'<a class="source-badge" href="#src-{esc(sid)}" '
                f'title="{esc(title)}">{esc(sid)}</a>'
            )
        else:
            badges.append(f'<span class="source-badge missing" title="未在 sources.csv 找到">{esc(sid)}</span>')
    return badges


def source_details(rows):
    cards = []
    for row in rows:
        sid = row["source_id"]
        cards.append(
            f"""
            <article class="source-card" id="src-{esc(sid)}">
              <div class="source-card-head">
                <a class="source-badge" href="{esc(row['url'])}" target="_blank" rel="noopener">{esc(sid)}</a>
                <span>{esc(row['source_type'])}</span>
                <span>{esc(row['confidence'])}</span>
              </div>
              <h3><a href="{esc(row['url'])}" target="_blank" rel="noopener">{esc(row['title'])}</a></h3>
              <dl>
                <div><dt>城市</dt><dd>{esc(row['city'])}</dd></div>
                <div><dt>区域</dt><dd>{esc(row['area'])}</dd></div>
                <div><dt>层级</dt><dd>{esc(row['layer'])}</dd></div>
                <div><dt>维度</dt><dd>{esc(row['dimension'])}</dd></div>
                <div><dt>URL</dt><dd><a href="{esc(row['url'])}" target="_blank" rel="noopener">{esc(row['url'])}</a></dd></div>
                <div><dt>机构/作者</dt><dd>{esc(row['author_or_org'])}</dd></div>
                <div><dt>发布日期</dt><dd>{esc(row['published_date'])}</dd></div>
                <div><dt>访问日期</dt><dd>{esc(row['accessed_date'])}</dd></div>
                <div><dt>备注</dt><dd>{esc(row['notes'])}</dd></div>
              </dl>
            </article>
            """
        )
    return "\n".join(cards)


def crosswalk_rows(rows, sources):
    rendered = []
    for row in rows:
        lisbon_sources = " ".join(source_badges(row["lisbon_source_ids"], sources))
        cm_sources = " ".join(source_badges(row["chiang_mai_source_ids"], sources))
        rendered.append(
            f"""
            <tr>
              <td class="dimension"><strong>{esc(row['dimension'])}</strong><span>{esc(row['sub_dimension'])}</span></td>
              <td>{esc(row['lisbon_evidence'])}<div class="badges">{lisbon_sources}</div></td>
              <td>{esc(row['chiang_mai_evidence'])}<div class="badges">{cm_sources}</div></td>
              <td>{esc(row['evidence_limitations'])}</td>
              <td>{esc(row['next_manual_check'])}</td>
            </tr>
            """
        )
    return "\n".join(rendered)


def build_html(crosswalk, source_rows):
    sources = {row["source_id"]: row for row in source_rows}
    return f"""<!doctype html>
<html lang="zh-Hans">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>里斯本 vs 清迈：家庭慢旅行证据横向对照</title>
  <style>
    :root {{
      --bg: #f7f8f5;
      --panel: #ffffff;
      --text: #20231f;
      --muted: #5f665d;
      --line: #d9ded4;
      --accent: #11615a;
      --accent-soft: #dbece8;
      --warn: #8a4d12;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.55;
    }}
    header {{
      padding: 32px clamp(18px, 4vw, 56px) 22px;
      border-bottom: 1px solid var(--line);
      background: #eef4f0;
    }}
    h1 {{
      margin: 0 0 10px;
      font-size: clamp(26px, 4vw, 42px);
      letter-spacing: 0;
    }}
    header p {{
      margin: 0;
      max-width: 980px;
      color: var(--muted);
      font-size: 16px;
    }}
    main {{
      padding: 24px clamp(14px, 3vw, 42px) 56px;
    }}
    .note {{
      max-width: 1180px;
      background: var(--panel);
      border: 1px solid var(--line);
      border-left: 5px solid var(--accent);
      padding: 14px 16px;
      margin: 0 0 22px;
    }}
    .table-wrap {{
      width: 100%;
      overflow-x: auto;
      border: 1px solid var(--line);
      background: var(--panel);
    }}
    table {{
      border-collapse: collapse;
      min-width: 1260px;
      width: 100%;
    }}
    th, td {{
      border-bottom: 1px solid var(--line);
      border-right: 1px solid var(--line);
      vertical-align: top;
      padding: 12px;
      font-size: 14px;
    }}
    th {{
      position: sticky;
      top: 0;
      background: #e9f0eb;
      text-align: left;
      z-index: 1;
    }}
    td.dimension {{
      width: 180px;
      background: #fbfcfa;
    }}
    td.dimension span {{
      display: block;
      margin-top: 4px;
      color: var(--muted);
      font-size: 13px;
    }}
    .badges {{
      margin-top: 10px;
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }}
    .source-badge {{
      display: inline-flex;
      align-items: center;
      min-height: 26px;
      padding: 3px 8px;
      border-radius: 6px;
      background: var(--accent-soft);
      color: var(--accent);
      text-decoration: none;
      font-weight: 650;
      font-size: 12px;
      white-space: nowrap;
    }}
    .source-badge:hover {{
      outline: 2px solid var(--accent);
      outline-offset: 1px;
    }}
    .source-badge.missing {{
      background: #f5e7d5;
      color: var(--warn);
    }}
    .range {{
      display: inline-flex;
      flex-wrap: wrap;
      gap: 6px;
    }}
    h2 {{
      margin: 34px 0 14px;
      font-size: 24px;
    }}
    .sources {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 14px;
    }}
    .source-card {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 14px;
    }}
    .source-card-head {{
      display: flex;
      gap: 8px;
      align-items: center;
      flex-wrap: wrap;
      color: var(--muted);
      font-size: 12px;
    }}
    .source-card h3 {{
      font-size: 16px;
      margin: 10px 0;
    }}
    .source-card h3 a {{
      color: var(--text);
      text-decoration-color: var(--accent);
    }}
    dl {{
      display: grid;
      gap: 6px;
      margin: 0;
      font-size: 13px;
    }}
    dl div {{
      display: grid;
      grid-template-columns: 82px 1fr;
      gap: 8px;
    }}
    dt {{
      color: var(--muted);
    }}
    dd {{
      margin: 0;
    }}
    footer {{
      padding: 22px clamp(18px, 4vw, 56px);
      color: var(--muted);
      border-top: 1px solid var(--line);
    }}
  </style>
</head>
<body>
  <header>
    <h1>里斯本 vs 清迈：家庭慢旅行证据横向对照</h1>
    <p>本页只展示证据，不给城市推荐、不使用红黄绿判断。每个证据 ID 对应 <code>data/sources/sources.csv</code> 中的一条来源记录；点击 ID 会打开原始来源链接，页面底部有完整来源索引。</p>
  </header>
  <main>
    <section class="note">
      <strong>读法：</strong>同一行横向比较同一生活功能。证据限制和下一步核验用于说明哪些内容还没有被当前资料证明。
    </section>
    <section class="table-wrap" aria-label="证据横向对照表">
      <table>
        <thead>
          <tr>
            <th>维度</th>
            <th>里斯本证据</th>
            <th>清迈证据</th>
            <th>证据限制</th>
            <th>下一步人工核验</th>
          </tr>
        </thead>
        <tbody>
          {crosswalk_rows(crosswalk, sources)}
        </tbody>
      </table>
    </section>
    <h2>来源索引</h2>
    <section class="sources">
      {source_details(source_rows)}
    </section>
  </main>
  <footer>
    Generated from local CSV files. Access dates and source classifications are stored in sources.csv.
  </footer>
</body>
</html>
"""


def main():
    source_rows = read_csv(SOURCES_CSV)
    crosswalk = read_csv(CROSSWALK_CSV)
    html_text = build_html(crosswalk, source_rows)
    DOCS_INDEX.write_text(html_text, encoding="utf-8")
    REPORT_HTML.write_text(html_text, encoding="utf-8")
    print(f"wrote {DOCS_INDEX}")
    print(f"wrote {REPORT_HTML}")


if __name__ == "__main__":
    main()
