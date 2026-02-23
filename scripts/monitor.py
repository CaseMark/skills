#!/usr/bin/env python3
"""
monitor.py — Live HTML dashboard for batch skill rewriting.
Serves a self-refreshing HTML page showing progress, recent completions, and failures.

Usage:
  python3 scripts/monitor.py           # Start on port 8787
  python3 scripts/monitor.py --port 9000
"""

import argparse
import json
import os
import time
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import io

REPO_ROOT = Path(__file__).resolve().parent.parent
EXPORT_DIR = REPO_ROOT / "audit" / "export" / "by-slug"
SKILLS_DIR = REPO_ROOT / "skills" / "legal"
LOG_DIR = REPO_ROOT / "audit" / "rewrite-logs"


def get_stats():
    """Compute current progress stats."""
    # Count all exported skills (non-hub)
    total_exported = 0
    hub_count = 0
    for fpath in EXPORT_DIR.glob("*.json"):
        with open(fpath) as f:
            data = json.load(f)
        content = data.get("content", "") or ""
        if len(content) < 200:
            hub_count += 1
        else:
            total_exported += 1

    # Count completed skills
    completed = []
    if SKILLS_DIR.exists():
        for d in sorted(SKILLS_DIR.iterdir()):
            if d.is_dir() and d.name not in {".gitkeep", ".DS_Store", "__pycache__"}:
                skill_file = d / "SKILL.md"
                if skill_file.exists():
                    stat = skill_file.stat()
                    lines = skill_file.read_text().count("\n") + 1
                    completed.append({
                        "slug": d.name,
                        "lines": lines,
                        "size": stat.st_size,
                        "mtime": stat.st_mtime,
                    })

    completed.sort(key=lambda x: x["mtime"], reverse=True)

    # Count failures from log dir
    failures = []
    if LOG_DIR.exists():
        for log_file in LOG_DIR.glob("*.log"):
            content = log_file.read_text()
            if "FAILED" in content or "Error" in content or "exit code" in content:
                failures.append({
                    "slug": log_file.stem,
                    "error": content[:200],
                    "mtime": log_file.stat().st_mtime,
                })

    failures.sort(key=lambda x: x["mtime"], reverse=True)

    # Read slug mapping
    mapping_file = LOG_DIR / "_slug-mapping.txt"
    mappings = []
    if mapping_file.exists():
        mappings = [line.strip() for line in mapping_file.read_text().strip().split("\n") if line.strip()]

    pct = (len(completed) / total_exported * 100) if total_exported > 0 else 0

    return {
        "total_exported": total_exported,
        "hub_count": hub_count,
        "completed": len(completed),
        "recent": completed[:50],
        "failures": failures[:20],
        "mappings": mappings[-20:],
        "pct": pct,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }


def build_html(stats):
    """Generate the dashboard HTML."""
    recent_rows = ""
    for s in stats["recent"]:
        ts = datetime.fromtimestamp(s["mtime"]).strftime("%H:%M:%S")
        recent_rows += f"""
        <tr>
          <td><code>{s['slug']}</code></td>
          <td>{s['lines']}</td>
          <td>{s['size']:,}</td>
          <td>{ts}</td>
        </tr>"""

    failure_rows = ""
    for f in stats["failures"]:
        ts = datetime.fromtimestamp(f["mtime"]).strftime("%H:%M:%S")
        err = f["error"][:100].replace("<", "&lt;").replace(">", "&gt;")
        failure_rows += f"""
        <tr class="failure">
          <td><code>{f['slug']}</code></td>
          <td>{err}</td>
          <td>{ts}</td>
        </tr>"""

    remaining = stats["total_exported"] - stats["completed"]
    bar_pct = min(stats["pct"], 100)

    return f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="5">
  <title>CaseMark Skill Rewrite Monitor</title>
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #0a0a0a; color: #e0e0e0; padding: 20px; }}
    h1 {{ color: #fff; margin-bottom: 8px; font-size: 24px; }}
    .subtitle {{ color: #888; margin-bottom: 24px; font-size: 14px; }}
    .stats {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 24px; }}
    .stat-card {{ background: #1a1a1a; border: 1px solid #333; border-radius: 12px; padding: 20px; text-align: center; }}
    .stat-card .number {{ font-size: 36px; font-weight: 700; color: #4ade80; }}
    .stat-card .label {{ font-size: 12px; color: #888; text-transform: uppercase; letter-spacing: 1px; margin-top: 4px; }}
    .stat-card.remaining .number {{ color: #f59e0b; }}
    .stat-card.failed .number {{ color: #ef4444; }}
    .progress-bar {{ background: #1a1a1a; border: 1px solid #333; border-radius: 12px; padding: 16px; margin-bottom: 24px; }}
    .progress-bar .bar-outer {{ background: #222; border-radius: 8px; height: 32px; overflow: hidden; }}
    .progress-bar .bar-inner {{ background: linear-gradient(90deg, #22c55e, #4ade80); height: 100%; border-radius: 8px; transition: width 0.5s ease; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 14px; color: #000; min-width: 60px; }}
    .section {{ background: #1a1a1a; border: 1px solid #333; border-radius: 12px; padding: 20px; margin-bottom: 16px; }}
    .section h2 {{ font-size: 16px; color: #fff; margin-bottom: 12px; }}
    table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
    th {{ text-align: left; padding: 8px 12px; color: #888; border-bottom: 1px solid #333; font-weight: 500; text-transform: uppercase; font-size: 11px; letter-spacing: 1px; }}
    td {{ padding: 6px 12px; border-bottom: 1px solid #1f1f1f; }}
    tr:hover {{ background: #222; }}
    tr.failure td {{ color: #ef4444; }}
    code {{ background: #222; padding: 2px 6px; border-radius: 4px; font-size: 12px; }}
    .pulse {{ animation: pulse 2s infinite; }}
    @keyframes pulse {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0.5; }} }}
    .live {{ display: inline-block; background: #22c55e; width: 8px; height: 8px; border-radius: 50%; margin-right: 8px; }}
  </style>
</head>
<body>
  <h1>⚖️ CaseMark Skill Rewrite Monitor</h1>
  <p class="subtitle"><span class="live pulse"></span>Auto-refreshing every 5s · Last update: {stats['timestamp']}</p>

  <div class="stats">
    <div class="stat-card">
      <div class="number">{stats['completed']}</div>
      <div class="label">Completed</div>
    </div>
    <div class="stat-card remaining">
      <div class="number">{remaining}</div>
      <div class="label">Remaining</div>
    </div>
    <div class="stat-card">
      <div class="number">{stats['total_exported']}</div>
      <div class="label">Total Skills</div>
    </div>
    <div class="stat-card failed">
      <div class="number">{len(stats['failures'])}</div>
      <div class="label">Failures</div>
    </div>
  </div>

  <div class="progress-bar">
    <div class="bar-outer">
      <div class="bar-inner" style="width: {bar_pct}%">{stats['pct']:.1f}%</div>
    </div>
  </div>

  <div class="section">
    <h2>Recent Completions (last 50)</h2>
    <table>
      <thead><tr><th>Skill</th><th>Lines</th><th>Size</th><th>Time</th></tr></thead>
      <tbody>{recent_rows}</tbody>
    </table>
  </div>

  {"<div class='section'><h2>Failures</h2><table><thead><tr><th>Skill</th><th>Error</th><th>Time</th></tr></thead><tbody>" + failure_rows + "</tbody></table></div>" if failure_rows else ""}
</body>
</html>"""


class MonitorHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            stats = get_stats()
            html = build_html(stats)
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))
        elif self.path == "/api/stats":
            stats = get_stats()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(stats, default=str).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass  # Suppress request logs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8787)
    args = parser.parse_args()

    server = HTTPServer(("0.0.0.0", args.port), MonitorHandler)
    print(f"Monitor running at http://localhost:{args.port}")
    print(f"Watching: {SKILLS_DIR}")
    print(f"Press Ctrl+C to stop")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
        server.server_close()


if __name__ == "__main__":
    main()
