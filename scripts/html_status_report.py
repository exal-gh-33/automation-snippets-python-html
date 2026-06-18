#!/usr/bin/env python3
"""Convert a simple task CSV into a self-contained HTML status report."""

from __future__ import annotations

import csv
import html
import sys
from pathlib import Path

STATUS_COLORS = {
    "done": "#1f7a4d",
    "doing": "#8a5a00",
    "waiting": "#6a4fb3",
    "blocked": "#a83232",
}


def render_cell(value: str) -> str:
    return html.escape(value.strip())


def render_report(rows: list[dict[str, str]]) -> str:
    headers = list(rows[0].keys()) if rows else ["title", "owner", "status", "due"]
    body_rows = []
    for row in rows:
        status = row.get("status", "").strip().lower()
        color = STATUS_COLORS.get(status, "#555")
        cells = []
        for header in headers:
            value = render_cell(row.get(header, ""))
            if header == "status":
                value = f'<span class="pill" style="--pill-color:{color}">{value}</span>'
            cells.append(f"<td>{value}</td>")
        body_rows.append("<tr>" + "".join(cells) + "</tr>")

    header_html = "".join(f"<th>{html.escape(h)}</th>" for h in headers)
    row_html = "".join(body_rows)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Status Report</title>
  <style>
    body {{ font-family: system-ui, sans-serif; margin: 2rem; color: #1f2933; }}
    table {{ border-collapse: collapse; width: min(100%, 980px); }}
    th, td {{ border-bottom: 1px solid #d8dee6; padding: .65rem .8rem; text-align: left; }}
    th {{ background: #f5f7fa; }}
    .pill {{ background: color-mix(in srgb, var(--pill-color) 14%, white); color: var(--pill-color); border: 1px solid var(--pill-color); border-radius: 999px; padding: .15rem .45rem; font-size: .85rem; }}
  </style>
</head>
<body>
  <h1>Status Report</h1>
  <table>
    <thead><tr>{header_html}</tr></thead>
    <tbody>{row_html}</tbody>
  </table>
</body>
</html>
"""


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: html_status_report.py input.csv output.html", file=sys.stderr)
        return 2
    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    with input_path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    output_path.write_text(render_report(rows), encoding="utf-8")
    print(f"Wrote {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
