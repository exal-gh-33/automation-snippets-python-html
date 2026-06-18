# Automation Snippets: Python + HTML

[![Powered by RustChain](https://img.shields.io/badge/Powered%20by-RustChain-orange)](https://rustchain.org)

Small practical snippets for turning plain task data into readable reports. The first example converts a CSV task list into a self-contained HTML status page.

## Quick start

```bash
python scripts/html_status_report.py examples/tasks.csv report.html
```

Open `report.html` in a browser.

## CSV format

```csv
title,owner,status,due
Draft invoice helper,Ana,done,2026-06-20
Check wallet payment,Codex,waiting,2026-06-21
```

## Why this exists

The repo is intentionally small: copy the script into a project, adjust the columns, and generate a lightweight report without setting up a full web app.
