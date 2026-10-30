#!/usr/bin/env python3
"""
Runner and Verification Harness for the Top-44 High-Value Skills Upgrade.

Usage:
    # 1. Print current status of all 44 skills across all 9 batches
    python3 scripts/run_top15_upgrade.py status

    # 2. Get task payload/instructions for a specific batch (1-9) or skill slug
    python3 scripts/run_top15_upgrade.py prompt --batch 1
    python3 scripts/run_top15_upgrade.py prompt --slug bad-faith-demand

    # 3. Verify a batch or specific skill against CI & repo standards
    python3 scripts/run_top15_upgrade.py verify --batch 1
    python3 scripts/run_top15_upgrade.py verify --slug bad-faith-demand
    python3 scripts/run_top15_upgrade.py verify --all
"""

import argparse
import glob
import json
import os
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = REPO_ROOT / "skills"

# 44 Target Skills across 9 Batches
BATCHES = {
    1: {
        "domain": "legal",
        "name": "Legal Litigation",
        "slugs": [
            "bad-faith-demand",
            "demand-letter",
            "summary-judgment-brief",
            "coverage-opinion",
            "expert-report-on-damages",
        ],
    },
    2: {
        "domain": "legal",
        "name": "Legal Transactions & M&A",
        "slugs": [
            "hsr-filing",
            "merger-agreement",
            "disclosure-schedules",
            "due-diligence-report",
            "class-action-settlement",
        ],
    },
    3: {
        "domain": "legal",
        "name": "Legal Regulatory & IP",
        "slugs": [
            "stark-law-aks-compliance",
            "fcpa-compliance-policy",
            "aml-compliance-program",
            "patent-infringement-analysis",
        ],
    },
    4: {
        "domain": "med",
        "name": "Med Acute Care",
        "slugs": [
            "managing-sepsis-bundles",
            "managing-acute-stroke",
            "managing-acute-coronary-syndromes",
            "interpreting-fetal-monitoring",
            "assessing-suicide-risk",
        ],
    },
    5: {
        "domain": "med",
        "name": "Med Pharmacotherapy & Clinical",
        "slugs": [
            "managing-chemotherapy-protocols",
            "reconciling-medications",
            "managing-anticoagulation-therapy",
            "managing-drg-optimization",
            "managing-risk-adjustment-coding",
        ],
    },
    6: {
        "domain": "med",
        "name": "Med Compliance & Revenue Cycle",
        "slugs": [
            "conducting-false-claims-analysis",
            "conducting-stark-law-analysis",
            "managing-emtala-compliance",
            "managing-coding-denials",
            "managing-privacy-breach-response",
        ],
    },
    7: {
        "domain": "finance",
        "name": "Finance Tax Planning & Structuring",
        "slugs": [
            "managing-transfer-pricing-compliance",
            "analyzing-international-tax-planning",
            "analyzing-m-and-a-tax-implications",
            "analyzing-corporate-tax-structures",
            "managing-tax-controversy",
        ],
    },
    8: {
        "domain": "finance",
        "name": "Finance Modeling & Valuation",
        "slugs": [
            "building-lbo-models",
            "building-equity-valuation-models",
            "analyzing-earnings-quality",
            "managing-debt-covenant-compliance",
            "writing-investment-committee-memos",
        ],
    },
    9: {
        "domain": "finance",
        "name": "Finance Accounting, Audit & Underwriting",
        "slugs": [
            "managing-estate-and-gift-tax",
            "managing-revenue-recognition",
            "analyzing-loss-reserves",
            "managing-commercial-loan-underwriting",
            "auditing-aml-transactions",
        ],
    },
}

REQUIRED_SECTIONS = [
    r"why this skill exists",
    r"checkpoint a",
    r"step 1",
    r"checkpoint b",
    r"quality audit",
    r"guidelines?",
]

VALID_LEGAL_TAGS = {
    "litigation", "corporate", "transactional", "regulatory",
    "agreement", "pleading", "motion", "brief", "memo",
    "letter", "summary", "analysis", "checklist", "policy",
    "drafting", "summarization", "research", "funds", "edgar",
}

INJECTION_PATTERNS = [
    (r'(?i)you\s+are\s+now\b', 'Role override attempt'),
    (r'(?i)ignore\s+(all\s+)?previous\s+instructions', 'Ignore-previous-instructions attack'),
    (r'(?i)disregard\s+(all\s+)?(your|previous|prior)', 'Disregard-instructions attack'),
    (r'(?i)override\s+(your|the|all)\s+(instructions|rules|guidelines|constraints)', 'Override attempt'),
    (r'(?i)system\s*:\s', 'System message injection'),
    (r'(?i)\[SYSTEM\]', 'System bracket injection'),
    (r'(?i)send\s+(this|the|all|your)\s+(data|info|content|response)\s+to', 'Data exfiltration attempt'),
    (r'(?i)fetch\s+https?://', 'URL fetch injection'),
    (r'(?i)curl\s+https?://', 'curl injection'),
    (r'(?i)eval\s*\(', 'Eval injection'),
    (r'(?i)exec\s*\(', 'Exec injection'),
]


def find_slug_info(slug):
    for b_idx, data in BATCHES.items():
        if slug in data["slugs"]:
            return b_idx, data["domain"]
    return None, None


def inspect_skill(domain, slug):
    path = SKILLS_ROOT / domain / slug
    skill_file = path / "SKILL.md"
    refs_dir = path / "references"
    evals_file = path / "evals" / "evals.json"

    exists = skill_file.is_file()
    lines = 0
    ref_count = 0
    eval_count = 0
    has_trap_map = False
    has_evals = evals_file.is_file()

    if exists:
        content = skill_file.read_text(encoding="utf-8")
        lines = len(content.splitlines())
        has_trap_map = bool(re.search(r"where\s+mistakes\s+hide|trap\s+map", content, re.I))
        if refs_dir.is_dir():
            ref_count = len([f for f in refs_dir.iterdir() if f.is_file() and f.suffix == ".md"])
        if has_evals:
            try:
                eval_data = json.loads(evals_file.read_text(encoding="utf-8"))
                eval_count = len(eval_data.get("evals", []))
            except Exception:
                pass

    is_complete = (
        exists and
        (130 <= lines <= 350) and
        ref_count >= 2 and
        has_trap_map and
        eval_count >= 3
    )

    return {
        "domain": domain,
        "slug": slug,
        "exists": exists,
        "lines": lines,
        "refs": ref_count,
        "evals": eval_count,
        "has_trap_map": has_trap_map,
        "is_complete": is_complete,
    }


def verify_skill(domain, slug):
    path = SKILLS_ROOT / domain / slug
    skill_file = path / "SKILL.md"
    errors = []
    warnings = []

    if not skill_file.is_file():
        return [f"File not found: {skill_file}"], []

    content = skill_file.read_text(encoding="utf-8")
    parts = content.split("---", 2)
    if len(parts) < 3:
        return ["Malformed YAML frontmatter"], []

    fm_raw = parts[1]
    body = parts[2]
    body_lines = [l for l in body.splitlines() if l.strip()]

    # Slug match
    name_match = re.search(r"^name:\s*([a-z0-9-]+)", fm_raw, re.M)
    if not name_match or name_match.group(1).strip() != slug:
        errors.append(f"Frontmatter name '{name_match.group(1) if name_match else None}' != directory '{slug}'")

    # Description
    desc_match = re.search(r"description:\s*(?:>|\|)?\s*\n?([^\n]+(?:\n\s+[^\n]+)*)", fm_raw)
    if not desc_match:
        errors.append("Missing description in frontmatter")
    else:
        desc = re.sub(r"\s+", " ", desc_match.group(1)).strip()
        if len(desc) > 1024:
            errors.append(f"Description exceeds 1024 chars ({len(desc)})")
        if re.search(r"^(i|you|use this to)\b", desc, re.I):
            warnings.append("Description should be strictly 3rd person (starts with 'I', 'You', or 'Use this to')")

    # Legal Tags check
    if domain == "legal":
        tag_match = re.search(r"tags:\s*\n((?:\s*-\s*[^\n]+\n)+)", fm_raw)
        if tag_match:
            tags = [t.strip("- \t\r") for t in tag_match.group(1).strip().splitlines()]
            invalid = [t for t in tags if t not in VALID_LEGAL_TAGS]
            if invalid:
                errors.append(f"Invalid legal tags: {invalid}")

    # Body Line count limits
    if domain == "legal":
        if len(body_lines) > 500:
            errors.append(f"Legal skill body exceeds 500 lines ({len(body_lines)})")
        elif len(body_lines) < 80:
            errors.append(f"Legal skill body too short ({len(body_lines)} lines)")
    else:
        if len(body_lines) < 100:
            errors.append(f"Body too short: {len(body_lines)} lines (min 100 for {domain})")
        elif len(body_lines) > 400:
            warnings.append(f"Body long: {len(body_lines)} lines (max 400 for {domain})")

    # Required headings for med/finance
    if domain in ("med", "finance"):
        body_lower = body.lower()
        for pattern in REQUIRED_SECTIONS:
            heading_re = r"^#{1,4}\s+.*" + pattern
            if not re.search(heading_re, body_lower, re.MULTILINE):
                errors.append(f"Missing required section heading matching '{pattern}'")

    # Trap map check
    if not re.search(r"where\s+mistakes\s+hide|trap\s+map", body, re.I):
        warnings.append("Missing 'Where Mistakes Hide' or Trap Map table")

    # Reference check
    refs_dir = path / "references"
    if not refs_dir.is_dir() or len(list(refs_dir.glob("*.md"))) < 2:
        warnings.append(f"Fewer than 2 markdown files in references/")
    else:
        for ref in refs_dir.glob("*.md"):
            ref_text = ref.read_text(encoding="utf-8")
            if re.findall(r'\[.*?\]\(((?!http).*?\.md)\)', ref_text):
                errors.append(f"Nested markdown link found in reference: {ref.name}")
            if len(ref_text.splitlines()) > 100 and not re.search(r"^##\s+Contents", ref_text, re.M):
                warnings.append(f"Reference file {ref.name} >100 lines but missing '## Contents' TOC")

    # Evals check
    evals_file = path / "evals" / "evals.json"
    if not evals_file.is_file():
        warnings.append("Missing evals/evals.json")
    else:
        try:
            eval_data = json.loads(evals_file.read_text(encoding="utf-8"))
            if len(eval_data.get("evals", [])) < 3:
                warnings.append("evals/evals.json has fewer than 3 test cases")
        except Exception as e:
            errors.append(f"Invalid evals.json: {e}")

    # Injection check
    for pat, desc in INJECTION_PATTERNS:
        if re.search(pat, content):
            errors.append(f"Prompt injection trigger detected: {desc}")

    # Binary check
    for p in path.glob("**/*"):
        if p.is_file():
            if p.suffix.lower() in [".pdf", ".docx", ".xlsx", ".png", ".jpg"]:
                errors.append(f"Binary file detected in bundle: {p.relative_to(path)}")

    return errors, warnings


def print_status():
    print("=" * 80)
    print("TOP-44 SKILLS UPGRADE STATUS (CaseMark/skills)")
    print("=" * 80)
    total_complete = 0

    for b_idx, data in BATCHES.items():
        domain = data["domain"]
        print(f"\nBatch {b_idx}: {data['name']} ({domain.upper()})")
        print("-" * 80)
        print(f"{'SLUG':38s} {'LINES':6s} {'REFS':5s} {'EVALS':6s} {'TRAPMAP':8s} {'STATUS':8s}")
        print("-" * 80)
        for slug in data["slugs"]:
            st = inspect_skill(domain, slug)
            if st["is_complete"]:
                total_complete += 1
            status_str = "READY" if st["is_complete"] else "NEEDS_WORK"
            print(f"{slug:38s} {st['lines']:6d} {st['refs']:5d} {st['evals']:6d} "
                  f"{'YES' if st['has_trap_map'] else 'NO':8s} {status_str:8s}")

    print("\n" + "=" * 80)
    print(f"OVERALL COMPLETION: {total_complete} / 44 skills fully hardened to gold standard")
    print("=" * 80)


def generate_prompt(batch_idx=None, slug=None):
    playbook_path = REPO_ROOT / "UPGRADE-PLAYBOOK.md"
    playbook = playbook_path.read_text(encoding="utf-8") if playbook_path.is_file() else "Read UPGRADE-PLAYBOOK.md"

    if slug:
        b_idx, domain = find_slug_info(slug)
        if not b_idx:
            print(f"Error: Slug '{slug}' not in the 44 target list.")
            sys.exit(1)
        print(f"### Sub-Agent Task Brief: Upgrade `{domain}/{slug}`\n")
        print(f"Domain: {domain}")
        print(f"Batch: {b_idx} ({BATCHES[b_idx]['name']})")
        print(f"Playbook: Read UPGRADE-PLAYBOOK.md in repository root.")
        print(f"Goal: Harden `skills/{domain}/{slug}` with controller, references, and evals.")
        return

    if batch_idx:
        if batch_idx not in BATCHES:
            print(f"Error: Invalid batch number {batch_idx}. Choose 1-9.")
            sys.exit(1)
        b = BATCHES[batch_idx]
        print(f"### Sub-Agent Task Brief: Batch {batch_idx} ({b['name']})\n")
        print(f"Domain: {b['domain']}")
        print(f"Target Slugs: {', '.join(b['slugs'])}\n")
        print("Execute the upgrade protocol defined in UPGRADE-PLAYBOOK.md for each of the slugs listed above.")
        print(f"Run verification after completion: python3 scripts/run_top15_upgrade.py verify --batch {batch_idx}")


def run_verify(batch_idx=None, slug=None, verify_all=False):
    targets = []
    if slug:
        b_idx, domain = find_slug_info(slug)
        if not domain:
            print(f"Error: slug '{slug}' not found.")
            sys.exit(1)
        targets.append((domain, slug))
    elif batch_idx:
        b = BATCHES.get(batch_idx)
        if not b:
            print(f"Error: invalid batch {batch_idx}")
            sys.exit(1)
        for s in b["slugs"]:
            targets.append((b["domain"], s))
    elif verify_all:
        for b in BATCHES.values():
            for s in b["slugs"]:
                targets.append((b["domain"], s))

    failed = 0
    print("\n" + "=" * 80)
    print("VERIFICATION RUN")
    print("=" * 80)

    for domain, s in targets:
        errors, warnings = verify_skill(domain, s)
        status = "PASS" if not errors else "FAIL"
        if errors:
            failed += 1
        print(f"\n[{status}] {domain}/{s}")
        for e in errors:
            print(f"    ERROR: {e}")
        for w in warnings:
            print(f"    WARN:  {w}")

    print("\n" + "=" * 80)
    if failed == 0:
        print(f"SUCCESS: All {len(targets)} verified target(s) passed structural gates.")
        sys.exit(0)
    else:
        print(f"FAILED: {failed} / {len(targets)} target(s) have blocking errors.")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Top-44 Skills Upgrade Runner")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("status", help="Show current state of all 44 skills")

    p_prompt = subparsers.add_parser("prompt", help="Generate task instructions")
    p_prompt.add_argument("--batch", type=int, choices=range(1, 10), help="Batch number 1-9")
    p_prompt.add_argument("--slug", type=str, help="Specific skill slug")

    p_verify = subparsers.add_parser("verify", help="Verify skills against gates")
    p_verify.add_argument("--batch", type=int, choices=range(1, 10), help="Verify batch 1-9")
    p_verify.add_argument("--slug", type=str, help="Verify specific skill slug")
    p_verify.add_argument("--all", action="store_true", help="Verify all 44 skills")

    args = parser.parse_args()

    if args.command == "status":
        print_status()
    elif args.command == "prompt":
        generate_prompt(args.batch, args.slug)
    elif args.command == "verify":
        run_verify(args.batch, args.slug, args.all)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
