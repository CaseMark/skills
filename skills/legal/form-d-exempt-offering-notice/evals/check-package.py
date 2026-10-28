#!/usr/bin/env python3
"""Structural regression check for the form-d-exempt-offering-notice skill package.

Run with: python3 -I check-package.py  (from any directory)
Exit status 0 when every check passes; 1 otherwise.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(HERE)
REFS = os.path.join(SKILL_DIR, "references")

failures = []


def check(cond, msg):
    if not cond:
        failures.append(msg)


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def contains_all(text, needles, label):
    for n in needles:
        check(n in text, f"{label}: missing required text: {n!r}")


# --- root skill -----------------------------------------------------------
skill_path = os.path.join(SKILL_DIR, "SKILL.md")
skill = read(skill_path)
m = re.match(r"^---\n(.*?)\n---\n(.*)$", skill, re.S)
check(m is not None, "SKILL.md: frontmatter not found")
if m:
    fm, body = m.group(1), m.group(2)
    check(re.search(r"^name: form-d-exempt-offering-notice$", fm, re.M), "SKILL.md: name mismatch")
    desc = re.search(r"description: >\n((?:  .*\n)+)", fm)
    check(desc is not None, "SKILL.md: folded description not found")
    if desc:
        d = " ".join(l.strip() for l in desc.group(1).splitlines())
        check(len(d) <= 1024, f"SKILL.md: description is {len(d)} chars (limit 1024)")
    lines = len(body.strip().split("\n"))
    check(lines <= 500, f"SKILL.md: body is {lines} lines (limit 500)")
    for ref in sorted(set(re.findall(r"references/([a-z0-9-]+\.md)", body))):
        check(os.path.isfile(os.path.join(REFS, ref)), f"SKILL.md names references/{ref} which does not exist")
    contains_all(body, [
        "## Quality-Control Gate Before Responding",
        "## Troubleshooting",
        "source-review completion gate",
        "evidence-to-field worksheet",
        "confirmed match, affirmative no-match, different entity returned, lookup blocked or failed, not checked",
        "unknown fact, an issuer election, not applicable, an unverified external lookup, or a source conflict",
        "Issuer-specific reconciliation",
        "A flag is not a deliverable",
        "Every unresolved item has an owner and a next action",
        "governing contractual event",
        "Every bad actor questionnaire \"Yes\"",
        "## Where mistakes hide",
        "investor reconciliation table",
        "placement agent cross-check matrix",
    ], "SKILL.md")
    for word in ["ignore previous instructions", "you are now", "developer mode"]:
        check(word not in body.lower(), f"SKILL.md: contains injection-scan trigger {word!r}")

# --- references: operative rules live in one place -------------------------
expected_refs = {
    "source-reconciliation.md": [
        "## Source-review completion gate",
        "| Reviewed |", "| Not relevant |", "| Unreadable after attempt |", "| Still needed |",
        "**Must-review categories.**",
        "## Bad actor questionnaire review",
        "**Potentially disqualifying.**", "**Disclosure-only.**", "**Outside the criteria on its face.**", "**Unresolved.**",
        "September 23, 2013",
        "## Client instructions that point at a lower-ranked source",
    ],
    "form-d-items.md": [
        "## Evidence-to-field worksheet",
        "**MISSING is not a status.**",
        "| Unknown fact |", "| Issuer election |", "| Not applicable |", "| Unverified external lookup |", "| Source conflict |",
        "## Item 11. Minimum Investment (decision framework)",
        "1. **Stated minimum.**", "2. **Waiver authority.**", "3. **Non-waivable floor.**", "4. **Accepted below-minimum subscriptions.**",
        "C&DI 130.03",
        "arithmetic check",
        "never a single figure copied from a ledger, closing memo or client email",
    ],
    "fund-structures.md": [
        "## Issuer-specific reconciliation before any program presentation",
        "**Investor reconciliation table.**", "| Ledger amount | Delta |",
        "**Per-issuer schedule.**", "**Program schedule.**", "**Arithmetic check.**", "**Program totals in issuer fields.**",
        "Regulation D only", "All sales",
        "**Required write-up for each conflict.**",
        "never controls over an executed questionnaire",
    ],
    "edgar-access.md": [
        "## Step 1: Look up every external identifier and record the outcome",
        "| Confirmed match |", "| Affirmative no-match |", "| Different entity returned |", "| Lookup blocked or failed |", "| Not checked |",
        "A failed lookup is never reported as \"not found\"",
        "An affirmative no-match is never softened",
        "**Synthetic, training or fictional identifiers.**",
    ],
    "output-template.md": [
        "**Source-review register**",
        "**Identifier lookup register**",
        "## 3. Evidence-to-field worksheet and item-by-item draft",
        "issuer calculation schedules",
        "A hand-off is complete only when the receiving workflow could start without re-reading the matter.",
        "**`blue-sky-filings`.**", "**`bad-actor-disqualification-review`.**",
        "**placement agent cross-check matrix**", "| Introduced by (agent name or Direct) |",
        "A Direct-introduced investor creates no agent registration gap",
        "is High, not Critical",
        "| # | Open item | Depends on (document, lookup, confirmation) | Owner | Next action | Blocks filing? |",
    ],
    "amendments-and-deadlines.md": ["## Date of first sale", "## Amendments: Rule 503(a)(3)"],
    "primary-sources.md": ["Rule 506(d)(2) exceptions", "Rule 506(e)"],
}
for name, needles in expected_refs.items():
    p = os.path.join(REFS, name)
    check(os.path.isfile(p), f"references/{name} is missing")
    if os.path.isfile(p):
        t = read(p)
        contains_all(t, needles, f"references/{name}")
        nested = re.findall(r"\[[^\]]*\]\(((?!http)[^)]*\.md)\)", t)
        check(not nested, f"references/{name}: markdown links to other .md files (nested references): {nested}")
        if len(t.splitlines()) > 100:
            check("## Contents" in t, f"references/{name}: over 100 lines but has no Contents section")

# The detailed Item 11 framework must not be duplicated in fund-structures.md
fs = read(os.path.join(REFS, "fund-structures.md"))
check("1. **Stated minimum.**" not in fs, "fund-structures.md duplicates the Item 11 framework (should cross-reference form-d-items.md)")
# The cross-check matrix layout must live only in output-template.md
for name in ["form-d-items.md", "source-reconciliation.md", "fund-structures.md", "edgar-access.md"]:
    t = read(os.path.join(REFS, name))
    check("| Introduced by (agent name or Direct) |" not in t, f"references/{name} duplicates the cross-check matrix (should cross-reference output-template.md)")
# The five lookup outcomes table must live only in edgar-access.md
for name in ["form-d-items.md", "source-reconciliation.md", "output-template.md", "fund-structures.md"]:
    t = read(os.path.join(REFS, name))
    check("| Confirmed match |" not in t, f"references/{name} duplicates the lookup-outcome table (should cross-reference edgar-access.md)")

# --- evals index ------------------------------------------------------------
ev = json.load(open(os.path.join(HERE, "evals.json"), encoding="utf-8"))
check(ev.get("skill_name") == "form-d-exempt-offering-notice", "evals.json: skill_name mismatch")
ids = set()
for e in ev.get("evals", []):
    check(e["id"] not in ids, f"evals.json: duplicate id {e['id']}")
    ids.add(e["id"])
    for f in e.get("files", []):
        check(os.path.isfile(os.path.join(HERE, f)), f"evals.json test {e['id']}: fixture {f} missing")
    eb = e.get("expected_behavior")
    check(eb and os.path.isfile(os.path.join(HERE, eb)), f"evals.json test {e['id']}: expected file {eb} missing")
    if eb and os.path.isfile(os.path.join(HERE, eb)):
        t = read(os.path.join(HERE, eb))
        check("## Must" in t and "## Must not" in t, f"{eb}: needs '## Must' and '## Must not' sections")
    check(e.get("prompt"), f"evals.json test {e['id']}: empty prompt")
check(len(ids) == 10, f"evals.json: expected 10 tests, found {len(ids)}")
check(os.path.isfile(os.path.join(HERE, "expected", "_common.md")), "expected/_common.md missing")

# --- report -----------------------------------------------------------------
if failures:
    print("FAIL")
    for f in failures:
        print(" -", f)
    sys.exit(1)
print("PASS: form-d-exempt-offering-notice package structure OK")
