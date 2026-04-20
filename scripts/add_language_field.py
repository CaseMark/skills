#!/usr/bin/env python3
"""One-shot backfill: add `language: en` to every SKILL.md frontmatter.

Inserts the line immediately after the top-level `name:` line. Skips files
that already have a top-level `language:` key.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent / "skills"
LANGUAGE_LINE = "language: en\n"


def insert_language(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return False
    fm_end = text.find("\n---\n", 4)
    if fm_end < 0:
        return False
    frontmatter = text[4:fm_end]
    if re.search(r"^language:", frontmatter, re.MULTILINE):
        return False
    match = re.search(r"^(name:[^\n]*\n)", frontmatter, re.MULTILINE)
    if not match:
        return False
    insert_at = 4 + match.end()
    new_text = text[:insert_at] + LANGUAGE_LINE + text[insert_at:]
    path.write_text(new_text, encoding="utf-8")
    return True


def main() -> int:
    if not ROOT.is_dir():
        print(f"skills directory not found: {ROOT}", file=sys.stderr)
        return 1
    updated = skipped = 0
    for skill in sorted(ROOT.rglob("SKILL.md")):
        if insert_language(skill):
            updated += 1
        else:
            skipped += 1
    print(f"Updated: {updated}, skipped: {skipped}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
