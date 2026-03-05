#!/usr/bin/env python3
"""
Validate enriched SKILL.md files for required structure, line counts,
and absence of generic filler content.

Usage:
    python scripts/validate_enrichment.py                    # all verticals
    python scripts/validate_enrichment.py --vertical med     # one vertical
    python scripts/validate_enrichment.py --only-failures    # only show failures
    python scripts/validate_enrichment.py --stubs            # only show stubs (unenriched)
"""

import argparse
import os
import re
import sys
from pathlib import Path

SKILLS_ROOT = Path(__file__).resolve().parent.parent / "skills"
VERTICALS = ["med", "finance", "capital"]

# --- Thresholds ---
MIN_BODY_LINES = 100  # enriched body (after frontmatter) should be >= 100 lines
MAX_BODY_LINES = 400  # sanity cap
STUB_THRESHOLD = 80  # files with body <= 80 lines are considered stubs

# --- Required sections (case-insensitive match on heading text) ---
REQUIRED_SECTIONS = [
    r"why this skill exists",
    r"checkpoint a",
    r"step 1",
    r"checkpoint b",
    r"quality audit",
    r"guidelines?",
]

# --- Generic filler phrases that indicate the body was NOT enriched ---
FILLER_PHRASES = [
    "Apply relevant frameworks",
    "Process information using appropriate methodology",
    "Analyze results against standards or criteria",
    "Document findings with supporting evidence",
    "Deliver structured output with quality verification",
    "Gather required inputs and define scope",
    "Output should be actionable for domain professionals",
    "Include appropriate disclaimers for compliance-sensitive outputs",
    "Escalate to human review when confidence is low or stakes are high",
    "This skill operates within the",
    "Use consistent terminology throughout the output",
    "Note limitations and scope boundaries in the final output",
    "Flag assumptions explicitly — never present inferred data as confirmed",
    "Always verify source data completeness before beginning",
    "When in doubt about a data point, mark with [VERIFY] rather than guessing",
]


def parse_frontmatter(text: str):
    """Return (frontmatter_dict_keys, body_text) or (None, text) if no frontmatter."""
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    fm_block = parts[1]
    body = parts[2]
    # Extract top-level keys from YAML (simple regex, no yaml dep needed)
    keys = set(re.findall(r"^(\w[\w_-]*):", fm_block, re.MULTILINE))
    return keys, body


def validate_skill(filepath: Path) -> dict:
    """Validate a single SKILL.md. Returns a result dict."""
    result = {
        "path": str(filepath),
        "slug": filepath.parent.name,
        "vertical": filepath.parent.parent.name,
        "is_stub": False,
        "errors": [],
        "warnings": [],
        "body_lines": 0,
        "total_lines": 0,
    }

    text = filepath.read_text(encoding="utf-8")
    result["total_lines"] = len(text.splitlines())

    # --- Frontmatter ---
    fm_keys, body = parse_frontmatter(text)
    if fm_keys is None:
        result["errors"].append("Missing YAML frontmatter (no opening ---)")
        return result

    for required_key in ["name", "description", "tags"]:
        if required_key not in fm_keys:
            result["errors"].append(f"Frontmatter missing key: {required_key}")

    # --- Body analysis ---
    body_lines = [l for l in body.splitlines() if l.strip()]
    result["body_lines"] = len(body_lines)

    if len(body_lines) <= STUB_THRESHOLD:
        result["is_stub"] = True
        return result  # no point validating structure on stubs

    # --- Line count ---
    if len(body_lines) < MIN_BODY_LINES:
        result["errors"].append(
            f"Body too short: {len(body_lines)} non-blank lines (min {MIN_BODY_LINES})"
        )
    if len(body_lines) > MAX_BODY_LINES:
        result["warnings"].append(
            f"Body unusually long: {len(body_lines)} non-blank lines (max {MAX_BODY_LINES})"
        )

    # --- Required sections ---
    body_lower = body.lower()
    for pattern in REQUIRED_SECTIONS:
        # Look for markdown heading with this text
        heading_re = r"^#{1,4}\s+.*" + pattern
        if not re.search(heading_re, body_lower, re.MULTILINE):
            result["errors"].append(f"Missing required section matching: {pattern}")

    # --- Filler detection ---
    filler_found = []
    for phrase in FILLER_PHRASES:
        if phrase.lower() in body_lower:
            filler_found.append(phrase)
    if filler_found:
        result["errors"].append(
            f"Generic filler detected ({len(filler_found)} phrases): "
            + "; ".join(f'"{p}"' for p in filler_found[:3])
            + ("..." if len(filler_found) > 3 else "")
        )

    return result


def collect_skills(verticals: list[str]) -> list[Path]:
    """Find all SKILL.md files in the given verticals."""
    paths = []
    for v in verticals:
        vdir = SKILLS_ROOT / v
        if not vdir.is_dir():
            print(f"WARNING: Vertical directory not found: {vdir}", file=sys.stderr)
            continue
        for skill_dir in sorted(vdir.iterdir()):
            skill_file = skill_dir / "SKILL.md"
            if skill_file.is_file():
                paths.append(skill_file)
    return paths


def main():
    parser = argparse.ArgumentParser(description="Validate enriched SKILL.md files")
    parser.add_argument(
        "--vertical",
        "-v",
        choices=VERTICALS,
        nargs="+",
        help="Validate specific vertical(s). Default: all.",
    )
    parser.add_argument(
        "--only-failures",
        "-f",
        action="store_true",
        help="Only show skills with errors.",
    )
    parser.add_argument(
        "--stubs", "-s", action="store_true", help="Only show unenriched stubs."
    )
    parser.add_argument(
        "--summary",
        action="store_true",
        default=True,
        help="Show summary statistics (default: true).",
    )
    args = parser.parse_args()

    verticals = args.vertical or VERTICALS
    skills = collect_skills(verticals)

    if not skills:
        print("No SKILL.md files found.")
        sys.exit(1)

    results = [validate_skill(p) for p in skills]

    # --- Counts ---
    total = len(results)
    stubs = [r for r in results if r["is_stub"]]
    enriched = [r for r in results if not r["is_stub"]]
    passed = [r for r in enriched if not r["errors"]]
    failed = [r for r in enriched if r["errors"]]
    with_warnings = [r for r in enriched if r["warnings"]]

    # --- Output ---
    if args.stubs:
        print(f"\n{'=' * 70}")
        print(f"UNENRICHED STUBS: {len(stubs)} / {total}")
        print(f"{'=' * 70}\n")
        for v in verticals:
            v_stubs = [r for r in stubs if r["vertical"] == v]
            if v_stubs:
                print(f"  {v}/ ({len(v_stubs)} stubs)")
                for r in v_stubs:
                    print(f"    - {r['slug']} ({r['body_lines']} lines)")
        print()
    elif args.only_failures:
        if not failed:
            print("All enriched skills passed validation.")
        else:
            print(f"\n{'=' * 70}")
            print(f"FAILED: {len(failed)} enriched skills")
            print(f"{'=' * 70}\n")
            for r in failed:
                print(f"  FAIL  {r['vertical']}/{r['slug']} ({r['body_lines']} lines)")
                for e in r["errors"]:
                    print(f"        - {e}")
            print()
    else:
        # Full report
        for r in results:
            if r["is_stub"]:
                continue
            status = "PASS" if not r["errors"] else "FAIL"
            print(f"  {status}  {r['vertical']}/{r['slug']} ({r['body_lines']} lines)")
            for e in r["errors"]:
                print(f"        ERROR: {e}")
            for w in r["warnings"]:
                print(f"        WARN:  {w}")

    # --- Summary ---
    print(f"\n{'=' * 70}")
    print("SUMMARY")
    print(f"{'=' * 70}")
    print(f"  Total skills scanned:   {total}")
    print(f"  Unenriched stubs:       {len(stubs)}")
    print(f"  Enriched:               {len(enriched)}")
    print(f"    Passed:               {len(passed)}")
    print(f"    Failed:               {len(failed)}")
    print(f"    With warnings:        {len(with_warnings)}")
    print()

    for v in verticals:
        v_results = [r for r in results if r["vertical"] == v]
        v_stubs = len([r for r in v_results if r["is_stub"]])
        v_enriched = len(v_results) - v_stubs
        v_passed = len([r for r in v_results if not r["is_stub"] and not r["errors"]])
        v_failed = v_enriched - v_passed
        print(
            f"  {v:12s}  total={len(v_results):4d}  stubs={v_stubs:4d}  enriched={v_enriched:4d}  pass={v_passed:4d}  fail={v_failed:4d}"
        )

    print()

    # Exit code: 0 if no failures among enriched, 1 otherwise
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
