#!/usr/bin/env python3
"""
Runner and verification harness for the top-44 skills upgrade.

Usage:
    # Scorecard for all 44 skills across the 9 batches
    python3 scripts/run_top15_upgrade.py status

    # Full author-agent brief for one skill, or every skill in a batch
    python3 scripts/run_top15_upgrade.py prompt --slug bad-faith-demand
    python3 scripts/run_top15_upgrade.py prompt --batch 1

    # Gate checks (exit 1 on any error; --strict also fails on warnings)
    python3 scripts/run_top15_upgrade.py verify --slug bad-faith-demand
    python3 scripts/run_top15_upgrade.py verify --batch 1
    python3 scripts/run_top15_upgrade.py verify --all
    python3 scripts/run_top15_upgrade.py verify --path skills/legal/form-d-exempt-offering-notice

Gates mirror the repo's CI so a local pass means a CI pass:
  - injection patterns are read from .github/workflows/skill-qa.yml
  - filler phrases are read from scripts/validate_enrichment.py
  - frontmatter is parsed with PyYAML, as skill-qa.yml does
  - legal body length is counted the way skill-qa.yml counts it
The playbook (UPGRADE-PLAYBOOK.md) and execution plan (UPGRADE-EXECUTION-PLAN.md)
add the stricter upgrade gates on top.
"""

import argparse
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML is required: pip install pyyaml")

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = REPO_ROOT / "skills"
SKILL_QA_WORKFLOW = REPO_ROOT / ".github" / "workflows" / "skill-qa.yml"
ENRICHMENT_VALIDATOR = REPO_ROOT / "scripts" / "validate_enrichment.py"
PLAN_FILE = REPO_ROOT / "UPGRADE-EXECUTION-PLAN.md"
BASE_REF = "origin/main"

BATCHES = {
    1: {"domain": "legal", "name": "Legal Litigation", "slugs": [
        "bad-faith-demand", "demand-letter", "summary-judgment-brief",
        "coverage-opinion", "expert-report-on-damages"]},
    2: {"domain": "legal", "name": "Legal Transactions & M&A", "slugs": [
        "hsr-filing", "merger-agreement", "disclosure-schedules",
        "due-diligence-report", "class-action-settlement"]},
    3: {"domain": "legal", "name": "Legal Regulatory & IP", "slugs": [
        "stark-law-aks-compliance", "fcpa-compliance-policy",
        "aml-compliance-program", "patent-infringement-analysis"]},
    4: {"domain": "med", "name": "Med Acute Care", "slugs": [
        "managing-sepsis-bundles", "managing-acute-stroke",
        "managing-acute-coronary-syndromes", "interpreting-fetal-monitoring",
        "assessing-suicide-risk"]},
    5: {"domain": "med", "name": "Med Pharmacotherapy & Clinical", "slugs": [
        "managing-chemotherapy-protocols", "reconciling-medications",
        "managing-anticoagulation-therapy", "managing-drg-optimization",
        "managing-risk-adjustment-coding"]},
    6: {"domain": "med", "name": "Med Compliance & Revenue Cycle", "slugs": [
        "conducting-false-claims-analysis", "conducting-stark-law-analysis",
        "managing-emtala-compliance", "managing-coding-denials",
        "managing-privacy-breach-response"]},
    7: {"domain": "finance", "name": "Finance Tax Planning & Structuring", "slugs": [
        "managing-transfer-pricing-compliance", "analyzing-international-tax-planning",
        "analyzing-m-and-a-tax-implications", "analyzing-corporate-tax-structures",
        "managing-tax-controversy"]},
    8: {"domain": "finance", "name": "Finance Modeling & Valuation", "slugs": [
        "building-lbo-models", "building-equity-valuation-models",
        "analyzing-earnings-quality", "managing-debt-covenant-compliance",
        "writing-investment-committee-memos"]},
    9: {"domain": "finance", "name": "Finance Accounting, Audit & Underwriting", "slugs": [
        "managing-estate-and-gift-tax", "managing-revenue-recognition",
        "analyzing-loss-reserves", "managing-commercial-loan-underwriting",
        "auditing-aml-transactions"]},
}

# Sibling and cross-vertical skills each upgraded skill must route to (plan section 4.5).
OVERLAP_GROUPS = [
    ["legal/stark-law-aks-compliance", "med/conducting-stark-law-analysis",
     "med/conducting-false-claims-analysis"],
    ["legal/aml-compliance-program", "finance/auditing-aml-transactions"],
    ["legal/merger-agreement", "legal/disclosure-schedules", "legal/due-diligence-report",
     "legal/hsr-filing", "finance/analyzing-m-and-a-tax-implications"],
    ["legal/bad-faith-demand", "legal/demand-letter", "legal/coverage-opinion"],
    ["finance/analyzing-corporate-tax-structures", "finance/analyzing-international-tax-planning",
     "finance/managing-transfer-pricing-compliance"],
]

# Documented exceptions to the playbook (plan section 4.3).
EXCEPTIONS = {
    "legal/demand-letter": {
        "max_refs": 6,
        "output_template": "TEMPLATE.md",
        "note": "Light touch: keeps its five references from PR #66 plus primary-sources.md.",
    },
}

BODY_MIN, BODY_MAX = 140, 320          # playbook band, all verticals, CI-style count
LEGAL_CI_MAX = 500                     # skill-qa.yml hard limit
ENRICH_MIN, ENRICH_MAX = 100, 400      # validate_enrichment.py, non-blank lines
REFS_MIN, REFS_MAX = 2, 4
EVALS_MIN, EVALS_MAX = 3, 5
EVAL_KEYS = ["id", "name", "prompt", "expected_output", "files", "expected_behavior", "trap_note"]

# Every upgraded skill carries the full controller anatomy (heading text, lowercase regex).
REQUIRED_HEADINGS = [
    (r"why this skill exists", "## Why This Skill Exists"),
    (r"where mistakes hide", "## Where Mistakes Hide"),
    (r"ground rules", "## Ground Rules"),
    (r"checkpoint a", "## Checkpoint A: Pre-Draft Intake (Mandatory)"),
    (r"step 1\b", "## Step 1: ..."),
    (r"checkpoint b", "## Checkpoint B: Post-Draft Alignment"),
    (r"quality audit", "## Quality Audit"),
    (r"guidelines?", "## Guidelines"),
    (r"troubleshooting", "## Troubleshooting"),
    (r"related skills", "## Related Skills"),
]

VALID_LEGAL_TAGS = {
    "litigation", "corporate", "transactional", "regulatory",
    "agreement", "pleading", "motion", "brief", "memo",
    "letter", "summary", "analysis", "checklist", "policy",
    "drafting", "summarization", "research", "funds", "edgar",
}

BINARY_SUFFIXES = {".pdf", ".docx", ".xlsx", ".pptx", ".png", ".jpg", ".jpeg", ".gif", ".zip"}


# ── Sources of truth shared with CI ──────────────────────────────────────────

def load_ci_injection_patterns():
    """Read INJECTION_PATTERNS from skill-qa.yml so this harness never drifts from CI."""
    text = SKILL_QA_WORKFLOW.read_text(encoding="utf-8")
    block = re.search(r"INJECTION_PATTERNS = \[(.*?)\n\s*\]\n", text, re.S)
    if not block:
        sys.exit(f"Could not find INJECTION_PATTERNS in {SKILL_QA_WORKFLOW}")
    pairs = re.findall(r"\(r'((?:[^'\\]|\\.)*)',\s*'((?:[^'\\]|\\.)*)'\)", block.group(1))
    if len(pairs) < 20:
        sys.exit(f"Parsed only {len(pairs)} injection patterns from {SKILL_QA_WORKFLOW}; parser is stale")
    return [(re.compile(p), d) for p, d in pairs]


def load_filler_phrases():
    spec = importlib.util.spec_from_file_location("validate_enrichment", ENRICHMENT_VALIDATOR)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return list(mod.FILLER_PHRASES)


INJECTION_PATTERNS = load_ci_injection_patterns()
FILLER_PHRASES = load_filler_phrases()


# ── Helpers ─────────────────────────────────────────────────────────────────

_ROOTS = None


def vertical_root(domain):
    """Checkout holding a vertical's work. A git worktree whose branch ends in
    -<domain> (e.g. claude/keen-edison-d1mcoa-med) wins; otherwise this checkout."""
    global _ROOTS
    if _ROOTS is None:
        _ROOTS = {}
        try:
            out = subprocess.run(["git", "worktree", "list", "--porcelain"], cwd=REPO_ROOT,
                                 capture_output=True, text=True, check=True).stdout
        except (subprocess.CalledProcessError, FileNotFoundError):
            out = ""
        wt = None
        for line in out.splitlines():
            if line.startswith("worktree "):
                wt = Path(line[len("worktree "):])
            elif line.startswith("branch ") and wt is not None:
                for d in ("legal", "med", "finance"):
                    if line.endswith(f"-{d}"):
                        _ROOTS[d] = wt
    return _ROOTS.get(domain, REPO_ROOT)


def find_slug(slug):
    for b_idx, data in BATCHES.items():
        if slug in data["slugs"]:
            return b_idx, data["domain"]
    return None, None


def all_targets():
    return [(b["domain"], s) for b in BATCHES.values() for s in b["slugs"]]


def overlaps_for(domain, slug):
    key = f"{domain}/{slug}"
    related = []
    for group in OVERLAP_GROUPS:
        if key in group:
            related.extend(k for k in group if k != key and k not in related)
    return related


def split_frontmatter(content):
    """Same regex skill-qa.yml uses. Returns (frontmatter_dict, body) or (None, None)."""
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", content, re.S)
    if not m:
        return None, None
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return None, None
    return fm, m.group(2)


def ci_body_lines(body):
    """skill-qa.yml: len(body.strip().split('\\n')) (blank lines count)."""
    return len(body.strip().split("\n"))


def nonblank_body_lines(content):
    """validate_enrichment.py: non-blank lines after text.split('---', 2)."""
    parts = content.split("---", 2)
    body = parts[2] if len(parts) == 3 else content
    return len([l for l in body.splitlines() if l.strip()])


def base_frontmatter(domain, slug):
    """Frontmatter of the skill on the base ref, for preserve-tags/metadata checks."""
    try:
        raw = subprocess.run(
            ["git", "show", f"{BASE_REF}:skills/{domain}/{slug}/SKILL.md"],
            cwd=REPO_ROOT, capture_output=True, text=True, check=True).stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    fm, _ = split_frontmatter(raw)
    return fm


def trap_map_rows(body):
    """Count data rows of the first table under the Where Mistakes Hide heading."""
    m = re.search(r"^#{2,4}\s+where mistakes hide[^\n]*\n(.*?)(?=^#{1,4}\s)", body, re.I | re.M | re.S)
    if not m:
        return 0, 0
    rows = [l for l in m.group(1).splitlines() if l.strip().startswith("|")]
    if len(rows) < 2:
        return 0, 0
    cols = len([c for c in rows[0].strip().strip("|").split("|")])
    data = [r for r in rows[2:] if not re.match(r"^\|\s*:?-{3,}", r.strip())]
    return cols, len(data)


# ── Verification ────────────────────────────────────────────────────────────

def verify_skill(domain, slug, path=None):
    path = Path(path) if path else vertical_root(domain) / "skills" / domain / slug
    key = f"{domain}/{slug}"
    exc = EXCEPTIONS.get(key, {})
    skill_file = path / "SKILL.md"
    errors, warnings = [], []

    if not skill_file.is_file():
        return [f"File not found: {skill_file.relative_to(REPO_ROOT)}"], []

    # Text-only bundle: every file must decode as UTF-8 (embed-skills.js rule).
    text_files = {}
    for p in sorted(path.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(path).as_posix()
        if p.suffix.lower() in BINARY_SUFFIXES:
            errors.append(f"Binary file in bundle: {rel}")
            continue
        try:
            text_files[rel] = p.read_bytes().decode("utf-8")
        except UnicodeDecodeError:
            errors.append(f"Non-UTF-8 file in bundle (would publish as base64): {rel}")

    content = text_files.get("SKILL.md", "")
    fm, body = split_frontmatter(content)
    if fm is None:
        return errors + ["Missing, malformed, or unparseable YAML frontmatter"], warnings

    # Frontmatter
    name = fm.get("name")
    if name != slug:
        errors.append(f"Frontmatter name {name!r} does not match directory {slug!r}")
    if fm.get("language") != "en":
        errors.append(f"Frontmatter language must be 'en' (got {fm.get('language')!r})")
    desc = fm.get("description") or ""
    if not isinstance(desc, str) or not desc.strip():
        errors.append("Missing description")
    else:
        if len(desc) > 1024:
            errors.append(f"Description exceeds 1024 chars ({len(desc)})")
        low = desc.strip().lower()
        if low.startswith("i ") or " i " in low[:50]:
            warnings.append("Description may use first person (CI warning)")
        if low.startswith("you ") or low.startswith("use this"):
            warnings.append("Description may use second person (CI warning)")
    tags = fm.get("tags") or []
    if not isinstance(tags, list) or not tags:
        errors.append("Frontmatter tags missing or not a list")
    elif domain == "legal":
        invalid = [t for t in tags if t not in VALID_LEGAL_TAGS]
        if invalid:
            errors.append(f"Invalid legal tags: {invalid}")
    if domain in ("med", "finance"):
        base = base_frontmatter(domain, slug)
        if base is None:
            warnings.append(f"Could not read {BASE_REF} frontmatter to confirm tags/metadata are preserved")
        else:
            if base.get("tags") != fm.get("tags"):
                errors.append(f"tags changed from {BASE_REF} (must be preserved): {base.get('tags')} -> {fm.get('tags')}")
            if base.get("metadata") != fm.get("metadata"):
                errors.append(f"metadata block changed from {BASE_REF} (must be preserved)")

    # Length
    ci_lines = ci_body_lines(body)
    if domain == "legal" and ci_lines > LEGAL_CI_MAX:
        errors.append(f"Body exceeds CI hard limit of {LEGAL_CI_MAX} lines ({ci_lines})")
    if not BODY_MIN <= ci_lines <= BODY_MAX:
        errors.append(f"Body is {ci_lines} lines; playbook band is {BODY_MIN}-{BODY_MAX}")
    if domain in ("med", "finance"):
        nb = nonblank_body_lines(content)
        if not ENRICH_MIN <= nb <= ENRICH_MAX:
            errors.append(f"Non-blank body is {nb} lines; validate_enrichment.py requires {ENRICH_MIN}-{ENRICH_MAX}")

    # Headings
    body_lower = body.lower()
    for pattern, label in REQUIRED_HEADINGS:
        if not re.search(r"^#{1,4}\s+.*" + pattern, body_lower, re.M):
            errors.append(f"Missing heading: {label}")

    # Trap map table
    cols, rows = trap_map_rows(body)
    if cols and cols != 3:
        errors.append(f"Where Mistakes Hide table has {cols} columns; expected 3")
    if rows < 5:
        errors.append(f"Where Mistakes Hide table has {rows} data rows; expected at least 5")

    # Filler phrases (validate_enrichment.py) across SKILL.md and references
    for rel, text in text_files.items():
        if rel == "SKILL.md" or rel.startswith("references/"):
            found = [p for p in FILLER_PHRASES if p.lower() in text.lower()]
            if found:
                errors.append(f"Filler phrase in {rel}: {found[0]!r}" + (f" (+{len(found)-1} more)" if len(found) > 1 else ""))

    # Injection patterns (skill-qa.yml) across every text file in the bundle
    for rel, text in text_files.items():
        for pat, label in INJECTION_PATTERNS:
            m = pat.search(text)
            if m:
                line = text.count("\n", 0, m.start()) + 1
                errors.append(f"Injection pattern in {rel}:{line}: {label} (matched {m.group(0)!r})")

    # References
    refs_dir = path / "references"
    ref_files = sorted(p.name for p in refs_dir.glob("*.md")) if refs_dir.is_dir() else []
    max_refs = exc.get("max_refs", REFS_MAX)
    if not REFS_MIN <= len(ref_files) <= max_refs:
        errors.append(f"references/ has {len(ref_files)} .md files; expected {REFS_MIN}-{max_refs}")
    if refs_dir.is_dir():
        for p in refs_dir.iterdir():
            if p.is_dir():
                errors.append(f"Subdirectory in references/ (depth must be 1): {p.name}")
            elif p.suffix != ".md":
                errors.append(f"Non-markdown file in references/: {p.name}")
    for required in (exc.get("output_template", "output-template.md"), "primary-sources.md"):
        if required not in ref_files:
            errors.append(f"Missing references/{required}")
    named_in_skill = set(re.findall(r"references/([A-Za-z0-9._-]+\.md)", body))
    for missing in sorted(named_in_skill - set(ref_files)):
        errors.append(f"SKILL.md names references/{missing}, which does not exist")
    for orphan in sorted(set(ref_files) - named_in_skill):
        errors.append(f"references/{orphan} is never named in SKILL.md")
    for name in ref_files:
        text = text_files.get(f"references/{name}", "")
        if re.findall(r"\[[^\]]*?\]\(((?!https?:)[^)]*?\.md)\)", text):
            errors.append(f"Relative markdown link in references/{name} (skill-qa nested-reference rule)")
        if len(text.splitlines()) > 100 and not re.search(r"^##\s+Contents", text, re.M):
            errors.append(f"references/{name} is over 100 lines and has no '## Contents'")

    # Evals
    evals_rel = "evals/evals.json"
    if evals_rel not in text_files:
        errors.append("Missing evals/evals.json")
    else:
        try:
            data = json.loads(text_files[evals_rel])
        except json.JSONDecodeError as e:
            data = None
            errors.append(f"evals/evals.json is not valid JSON: {e}")
        if data is not None:
            if data.get("skill_name") != slug:
                errors.append(f"evals.json skill_name {data.get('skill_name')!r} != {slug!r}")
            evals = data.get("evals") or []
            if not EVALS_MIN <= len(evals) <= EVALS_MAX:
                errors.append(f"evals.json has {len(evals)} evals; expected {EVALS_MIN}-{EVALS_MAX}")
            for i, ev in enumerate(evals, 1):
                missing = [k for k in EVAL_KEYS if k not in ev]
                if missing:
                    errors.append(f"eval #{i} missing keys: {missing}")
                    continue
                if not isinstance(ev["files"], list):
                    errors.append(f"eval #{i} 'files' must be a list")
                else:
                    for f in ev["files"]:
                        if not (path / "evals" / f).is_file():
                            errors.append(f"eval #{i} lists files entry evals/{f}, which does not exist")
                if not (isinstance(ev["trap_note"], str) and ev["trap_note"].strip()):
                    errors.append(f"eval #{i} trap_note must say why a weak skill fails and that the trap is live")
                eb = ev["expected_behavior"]
                if isinstance(eb, str) and eb.endswith(".md") and not (path / "evals" / eb).is_file():
                    errors.append(f"eval #{i} expected_behavior evals/{eb} does not exist")
                elif not (isinstance(eb, str) and eb.strip()) and not (isinstance(eb, list) and eb):
                    errors.append(f"eval #{i} expected_behavior must be a non-empty string or list")

    # Related skills routing
    for rel_key in overlaps_for(domain, slug):
        rel_slug = rel_key.split("/", 1)[1]
        if rel_slug not in body:
            warnings.append(f"Related skill {rel_key} is not named in SKILL.md")

    return errors, warnings


def inspect_skill(domain, slug):
    path = vertical_root(domain) / "skills" / domain / slug
    content = (path / "SKILL.md").read_text(encoding="utf-8") if (path / "SKILL.md").is_file() else ""
    fm, body = split_frontmatter(content) if content else (None, None)
    refs = len(list((path / "references").glob("*.md"))) if (path / "references").is_dir() else 0
    n_evals = 0
    try:
        n_evals = len(json.loads((path / "evals" / "evals.json").read_text(encoding="utf-8")).get("evals", []))
    except (OSError, json.JSONDecodeError):
        pass
    errors, warnings = verify_skill(domain, slug)
    return {
        "lines": ci_body_lines(body) if body is not None else 0,
        "refs": refs,
        "evals": n_evals,
        "trap": trap_map_rows(body)[1] if body else 0,
        "errors": len(errors),
        "warnings": len(warnings),
        "ready": not errors and not warnings,
    }


# ── Commands ────────────────────────────────────────────────────────────────

def cmd_status():
    print("=" * 92)
    print("TOP-44 SKILLS UPGRADE STATUS (CaseMark/skills)")
    print(f"READY = verify passes with zero errors and zero warnings. Body band {BODY_MIN}-{BODY_MAX} lines.")
    print("Checkouts: " + ", ".join(f"{d}={vertical_root(d)}" for d in ("legal", "med", "finance")))
    print("=" * 92)
    total = 0
    for b_idx, data in BATCHES.items():
        print(f"\nBatch {b_idx}: {data['name']} ({data['domain'].upper()})")
        print(f"{'SLUG':38s} {'BODY':>5s} {'REFS':>5s} {'EVALS':>6s} {'TRAPS':>6s} {'ERR':>4s} {'WARN':>5s}  STATUS")
        print("-" * 92)
        for slug in data["slugs"]:
            st = inspect_skill(data["domain"], slug)
            total += st["ready"]
            print(f"{slug:38s} {st['lines']:5d} {st['refs']:5d} {st['evals']:6d} {st['trap']:6d} "
                  f"{st['errors']:4d} {st['warnings']:5d}  {'READY' if st['ready'] else 'NEEDS_WORK'}")
    print("\n" + "=" * 92)
    print(f"OVERALL: {total} / {len(all_targets())} skills READY")
    print("=" * 92)


def load_brief_template():
    text = PLAN_FILE.read_text(encoding="utf-8")
    m = re.search(r"^## Appendix A[^\n]*\n.*?```\n(.*?)```", text, re.S | re.M)
    if not m:
        sys.exit(f"Could not find the Appendix A brief in {PLAN_FILE.name}")
    return m.group(1)


def render_brief(domain, slug):
    b_idx, _ = find_slug(slug)
    st = inspect_skill(domain, slug)
    if domain == "legal":
        tag_rule = "tags drawn only from the 19 controlled legal tags (see UPGRADE-PLAYBOOK.md Part 1, item 6)"
        enrich_cmd = "(legal: no enrichment validator)"
    else:
        tag_rule = "preserve the existing tags and metadata blocks exactly; the harness compares them to origin/main"
        enrich_cmd = f"cd {vertical_root(domain)} && python3 scripts/validate_enrichment.py --vertical {domain} --only-failures"
    exc = EXCEPTIONS.get(f"{domain}/{slug}")
    exception = f"Exception for this skill: {exc['note']}" if exc else "No exceptions apply to this skill."
    related = ", ".join(overlaps_for(domain, slug)) or "none listed; name any sibling you find"
    repo = str(vertical_root(domain))
    subs = {
        "{repo}": repo, "{domain}": domain, "{slug}": slug, "{n}": str(b_idx),
        "{batch_name}": BATCHES[b_idx]["name"], "{lines}": str(st["lines"]),
        "{refs}": str(st["refs"]), "{evals}": str(st["evals"]),
        "{trap}": "yes" if st["trap"] else "no", "{tag_rule}": tag_rule,
        "{enrichment_cmd}": enrich_cmd, "{related}": related, "{exception}": exception,
    }
    out = load_brief_template()
    for k, v in subs.items():
        out = out.replace(k, v)
    return out


def cmd_prompt(batch_idx=None, slug=None):
    if slug:
        b_idx, domain = find_slug(slug)
        if not b_idx:
            sys.exit(f"Error: slug '{slug}' is not one of the 44 targets.")
        print(render_brief(domain, slug))
    elif batch_idx:
        b = BATCHES[batch_idx]
        for i, s in enumerate(b["slugs"]):
            if i:
                print("\n" + "=" * 80 + "\n")
            print(render_brief(b["domain"], s))
    else:
        sys.exit("prompt needs --slug or --batch")


def cmd_verify(batch_idx=None, slug=None, verify_all=False, path=None, strict=False):
    if path:
        p = Path(path).resolve()
        targets = [(p.parent.name, p.name, p)]
    elif slug:
        b_idx, domain = find_slug(slug)
        if not domain:
            sys.exit(f"Error: slug '{slug}' is not one of the 44 targets (use --path for others).")
        targets = [(domain, slug, None)]
    elif batch_idx:
        b = BATCHES[batch_idx]
        targets = [(b["domain"], s, None) for s in b["slugs"]]
    elif verify_all:
        targets = [(d, s, None) for d, s in all_targets()]
    else:
        sys.exit("verify needs --slug, --batch, --all, or --path")

    failed = 0
    print("=" * 80 + "\nVERIFICATION RUN\n" + "=" * 80)
    for domain, s, p in targets:
        errors, warnings = verify_skill(domain, s, p)
        bad = bool(errors) or (strict and bool(warnings))
        failed += bad
        print(f"\n[{'FAIL' if bad else 'PASS'}] {domain}/{s}")
        for e in errors:
            print(f"    ERROR: {e}")
        for w in warnings:
            print(f"    WARN:  {w}")
    print("\n" + "=" * 80)
    if failed:
        print(f"FAILED: {failed} / {len(targets)} target(s) did not pass.")
        sys.exit(1)
    print(f"SUCCESS: all {len(targets)} target(s) passed.")


def main():
    parser = argparse.ArgumentParser(description="Top-44 skills upgrade runner")
    sub = parser.add_subparsers(dest="command")
    sub.add_parser("status", help="Scorecard for all 44 skills")
    p = sub.add_parser("prompt", help="Print the author-agent brief")
    p.add_argument("--batch", type=int, choices=range(1, 10))
    p.add_argument("--slug")
    v = sub.add_parser("verify", help="Run the gates")
    v.add_argument("--batch", type=int, choices=range(1, 10))
    v.add_argument("--slug")
    v.add_argument("--all", action="store_true")
    v.add_argument("--path", help="Verify any skill directory, e.g. a gold-standard bundle")
    v.add_argument("--strict", action="store_true", help="Treat warnings as failures")
    args = parser.parse_args()

    if args.command == "status":
        cmd_status()
    elif args.command == "prompt":
        cmd_prompt(args.batch, args.slug)
    elif args.command == "verify":
        cmd_verify(args.batch, args.slug, args.all, args.path, args.strict)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
