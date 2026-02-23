#!/usr/bin/env python3
"""
batch-rewrite.py — Rewrites legal skills from DB exports to SKILL.md files
Uses Claude Code CLI, OpenCode CLI, or Codex CLI for each skill.

Usage:
  python3 scripts/batch-rewrite.py                          # Process all remaining (claude)
  python3 scripts/batch-rewrite.py --backend opencode       # Use opencode instead
  python3 scripts/batch-rewrite.py --backend codex          # Use codex exec (fastest)
  python3 scripts/batch-rewrite.py --limit 10               # Process first 10 remaining
  python3 scripts/batch-rewrite.py --slug my-skill          # Process a single skill
  python3 scripts/batch-rewrite.py --dry-run                # Show what would be processed
  python3 scripts/batch-rewrite.py --parallel 4             # Run 4 at a time (default: 5)
  python3 scripts/batch-rewrite.py --model sonnet           # Model choice (default varies by backend)
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
EXPORT_DIR = REPO_ROOT / "audit" / "export" / "by-slug"
SKILLS_DIR = REPO_ROOT / "skills" / "legal"
SYSTEM_PROMPT_FILE = REPO_ROOT / "scripts" / "rewrite-skill.md"
LOG_DIR = REPO_ROOT / "audit" / "rewrite-logs"


def get_existing_skills() -> set:
    """Get all existing skill directory names."""
    if not SKILLS_DIR.exists():
        return set()
    return {
        d.name for d in SKILLS_DIR.iterdir()
        if d.is_dir() and d.name not in {".gitkeep", ".DS_Store", "__pycache__"}
    }


def get_remaining_slugs() -> list:
    """Get DB slugs that haven't been processed yet."""
    existing = get_existing_skills()
    remaining = []

    for fpath in sorted(EXPORT_DIR.glob("*.json")):
        slug = fpath.stem

        # Load and skip hub stubs
        with open(fpath) as f:
            data = json.load(f)
        content = data.get("content", "") or ""
        if len(content) < 200:
            continue

        # Skip if already processed (existing dir matches as suffix of db slug)
        already_done = False
        for existing_dir in existing:
            if slug == existing_dir or slug.endswith("-" + existing_dir):
                already_done = True
                break
        if not already_done:
            remaining.append(slug)

    return remaining


def process_skill_claude(slug: str, idx: int, total: int, system_prompt: str, model: str) -> dict:
    """Process a single skill through claude -p."""
    result = {"slug": slug, "idx": idx, "status": "unknown", "new_slug": None, "lines": 0, "error": None}

    json_file = EXPORT_DIR / f"{slug}.json"
    log_file = LOG_DIR / f"{slug}.log"

    if not json_file.exists():
        result["status"] = "skip"
        result["error"] = "no JSON export found"
        return result

    with open(json_file) as f:
        skill_json = f.read()

    prompt = f"Rewrite this skill into a SKILL.md file. Here is the skill JSON:\n\n{skill_json}"

    env = os.environ.copy()
    env.pop("CLAUDECODE", None)

    try:
        proc = subprocess.run(
            [
                "claude", "-p", prompt,
                "--system-prompt", system_prompt,
                "--output-format", "json",
                "--max-turns", "1",
                "--model", model,
            ],
            capture_output=True,
            text=True,
            timeout=180,
            env=env,
        )
    except subprocess.TimeoutExpired:
        result["status"] = "timeout"
        result["error"] = "timed out after 180s"
        with open(log_file, "w") as f:
            f.write(f"TIMEOUT: {slug}\n")
        return result
    except Exception as e:
        result["status"] = "error"
        result["error"] = str(e)
        return result

    with open(log_file, "w") as f:
        f.write(proc.stderr or "")

    if proc.returncode != 0:
        result["status"] = "failed"
        result["error"] = f"exit code {proc.returncode}"
        with open(log_file, "a") as f:
            f.write(f"\nSTDOUT:\n{proc.stdout[:500]}\n")
        return result

    try:
        output = json.loads(proc.stdout)
        text = output.get("result", "")
    except json.JSONDecodeError:
        text = proc.stdout.strip()

    return _validate_and_write(result, text, slug, log_file)


def process_skill_opencode(slug: str, idx: int, total: int, system_prompt: str, model: str) -> dict:
    """Process a single skill through opencode run."""
    result = {"slug": slug, "idx": idx, "status": "unknown", "new_slug": None, "lines": 0, "error": None}

    json_file = EXPORT_DIR / f"{slug}.json"
    log_file = LOG_DIR / f"{slug}.log"

    if not json_file.exists():
        result["status"] = "skip"
        result["error"] = "no JSON export found"
        return result

    with open(json_file) as f:
        skill_json = f.read()

    prompt = f"{system_prompt}\n\n---\n\nRewrite this skill into a SKILL.md file. Here is the skill JSON:\n\n{skill_json}"

    try:
        proc = subprocess.run(
            [
                "opencode", "run",
                "--format", "json",
                "--model", model,
                prompt,
            ],
            capture_output=True,
            text=True,
            timeout=180,
        )
    except subprocess.TimeoutExpired:
        result["status"] = "timeout"
        result["error"] = "timed out after 180s"
        with open(log_file, "w") as f:
            f.write(f"TIMEOUT: {slug}\n")
        return result
    except Exception as e:
        result["status"] = "error"
        result["error"] = str(e)
        return result

    with open(log_file, "w") as f:
        f.write(proc.stderr or "")

    if proc.returncode != 0:
        result["status"] = "failed"
        result["error"] = f"exit code {proc.returncode}"
        with open(log_file, "a") as f:
            f.write(f"\nSTDOUT:\n{proc.stdout[:500]}\n")
        return result

    # opencode --format json outputs newline-delimited JSON events
    text = ""
    for line in proc.stdout.strip().split("\n"):
        if not line.strip():
            continue
        try:
            event = json.loads(line)
            if event.get("type") == "text":
                text = event.get("part", {}).get("text", "")
                break
        except json.JSONDecodeError:
            continue

    if not text:
        text = proc.stdout.strip()

    return _validate_and_write(result, text, slug, log_file)


def process_skill_codex(slug: str, idx: int, total: int, system_prompt: str, model: str) -> dict:
    """Process a single skill through codex exec."""
    result = {"slug": slug, "idx": idx, "status": "unknown", "new_slug": None, "lines": 0, "error": None}

    json_file = EXPORT_DIR / f"{slug}.json"
    log_file = LOG_DIR / f"{slug}.log"

    if not json_file.exists():
        result["status"] = "skip"
        result["error"] = "no JSON export found"
        return result

    with open(json_file) as f:
        skill_json = f.read()

    # codex exec doesn't have --system-prompt, embed in message
    prompt = f"{system_prompt}\n\n---\n\nRewrite this skill into a SKILL.md file. Here is the skill JSON:\n\n{skill_json}"

    # Use -o to write output to a temp file (most reliable way to capture codex output)
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False, prefix=f"codex-{slug}-") as tmp:
        output_path = tmp.name

    try:
        proc = subprocess.run(
            [
                "codex", "exec",
                "-m", model,
                "--sandbox", "read-only",
                "--ephemeral",
                "-o", output_path,
                prompt,
            ],
            capture_output=True,
            text=True,
            timeout=120,
        )
    except subprocess.TimeoutExpired:
        result["status"] = "timeout"
        result["error"] = "timed out after 120s"
        with open(log_file, "w") as f:
            f.write(f"TIMEOUT: {slug}\n")
        try:
            os.unlink(output_path)
        except OSError:
            pass
        return result
    except Exception as e:
        result["status"] = "error"
        result["error"] = str(e)
        try:
            os.unlink(output_path)
        except OSError:
            pass
        return result

    with open(log_file, "w") as f:
        f.write(proc.stderr or "")

    if proc.returncode != 0:
        result["status"] = "failed"
        result["error"] = f"exit code {proc.returncode}"
        with open(log_file, "a") as f:
            f.write(f"\nSTDOUT:\n{(proc.stdout or '')[:500]}\n")
        try:
            os.unlink(output_path)
        except OSError:
            pass
        return result

    # Read the output file
    try:
        text = Path(output_path).read_text()
    except Exception as e:
        result["status"] = "error"
        result["error"] = f"could not read output: {e}"
        return result
    finally:
        try:
            os.unlink(output_path)
        except OSError:
            pass

    return _validate_and_write(result, text, slug, log_file)


def _validate_and_write(result: dict, text: str, slug: str, log_file: Path) -> dict:
    """Validate output and write SKILL.md. Shared between backends."""
    # Strip leading/trailing whitespace
    text = text.strip()

    # Strip markdown code fences if present
    if text.startswith("```markdown"):
        text = text[len("```markdown"):].strip()
    if text.startswith("```"):
        text = text[3:].strip()
    if text.endswith("```"):
        text = text[:-3].strip()

    # Validate: must start with ---
    if not text.startswith("---"):
        result["status"] = "invalid"
        result["error"] = "output doesn't start with ---"
        with open(log_file, "a") as f:
            f.write(f"\nOUTPUT:\n{text[:500]}\n")
        return result

    # Extract new slug from frontmatter
    m = re.search(r"^name:\s*(.+)$", text, re.MULTILINE)
    if not m:
        result["status"] = "invalid"
        result["error"] = "could not extract name from frontmatter"
        with open(log_file, "a") as f:
            f.write(f"\nOUTPUT:\n{text[:500]}\n")
        return result

    new_slug = m.group(1).strip()
    result["new_slug"] = new_slug

    # Validate slug format
    if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", new_slug):
        result["status"] = "invalid"
        result["error"] = f"invalid slug format: {new_slug}"
        with open(log_file, "a") as f:
            f.write(f"\nOUTPUT:\n{text[:500]}\n")
        return result

    # Write the skill file
    skill_dir = SKILLS_DIR / new_slug
    skill_dir.mkdir(parents=True, exist_ok=True)
    skill_file = skill_dir / "SKILL.md"
    skill_file.write_text(text + "\n")

    line_count = text.count("\n") + 1
    result["lines"] = line_count
    result["status"] = "ok"

    return result


def main():
    parser = argparse.ArgumentParser(description="Batch rewrite skills using claude -p, opencode run, or codex exec")
    parser.add_argument("--limit", type=int, default=0, help="Max skills to process")
    parser.add_argument("--slug", type=str, default="", help="Process a single slug")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be processed")
    parser.add_argument("--parallel", type=int, default=5, help="Parallel workers (default: 5)")
    parser.add_argument("--backend", type=str, default="claude", choices=["claude", "opencode", "codex"],
                        help="Backend CLI to use (default: claude)")
    parser.add_argument("--model", type=str, default="",
                        help="Model to use (default varies by backend)")
    args = parser.parse_args()

    # Set default model per backend
    if not args.model:
        if args.backend == "claude":
            args.model = "sonnet"
        elif args.backend == "opencode":
            args.model = "openai/gpt-5.2-codex"
        elif args.backend == "codex":
            args.model = "gpt-5.3-codex-spark"

    LOG_DIR.mkdir(parents=True, exist_ok=True)

    # Build slug list
    if args.slug:
        slugs = [args.slug]
    else:
        slugs = get_remaining_slugs()

    if args.limit > 0:
        slugs = slugs[:args.limit]

    total = len(slugs)
    print(f"=== CaseMark Skill Batch Rewrite ===")
    print(f"Backend: {args.backend}")
    print(f"Total skills to process: {total}")
    print(f"Parallel workers: {args.parallel}")
    print(f"Model: {args.model}")
    print()

    if args.dry_run:
        print("DRY RUN — would process:")
        for slug in slugs:
            json_file = EXPORT_DIR / f"{slug}.json"
            with open(json_file) as f:
                data = json.load(f)
            content_len = len(data.get("content", "") or "")
            print(f"  {slug} ({content_len:,} chars)")
        return

    # Read system prompt
    system_prompt = SYSTEM_PROMPT_FILE.read_text()

    # Select processor function
    process_fns = {
        "claude": process_skill_claude,
        "opencode": process_skill_opencode,
        "codex": process_skill_codex,
    }
    process_fn = process_fns[args.backend]

    # Process skills
    ok_count = 0
    fail_count = 0
    slug_mapping = []
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=args.parallel) as executor:
        futures = {}
        for idx, slug in enumerate(slugs, 1):
            future = executor.submit(process_fn, slug, idx, total, system_prompt, args.model)
            futures[future] = slug

        for future in as_completed(futures):
            result = future.result()
            slug = result["slug"]
            idx = result["idx"]

            if result["status"] == "ok":
                ok_count += 1
                slug_mapping.append(f"{slug} → {result['new_slug']}")
                print(f"  [{idx}/{total}] ✓ {slug} → {result['new_slug']} ({result['lines']} lines)")
            else:
                fail_count += 1
                print(f"  [{idx}/{total}] ✗ {slug} — {result['status']}: {result['error']}")

    elapsed = time.time() - start_time

    # Write slug mapping
    mapping_file = LOG_DIR / "_slug-mapping.txt"
    with open(mapping_file, "a") as f:
        for line in slug_mapping:
            f.write(line + "\n")

    # Summary
    print()
    print(f"=== Complete ===")
    print(f"Processed: {total} skills in {elapsed:.0f}s ({elapsed/max(total,1):.1f}s avg)")
    print(f"Successful: {ok_count}")
    print(f"Failed: {fail_count}")
    print(f"Output: {SKILLS_DIR}")
    print(f"Logs: {LOG_DIR}")

    if fail_count > 0:
        print(f"\nFailed skills — check logs in {LOG_DIR}/")
        sys.exit(1)


if __name__ == "__main__":
    main()
