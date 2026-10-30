# Top-15 High-Value Skills Upgrade Instruction Playbook
**Repository:** `CaseMark/skills`  
**Scope:** 44 skills across 3 domains (`skills/legal`: 14 skills, skipping `medical-record-chronology`; `skills/med`: 15 skills; `skills/finance`: 15 skills).  
**Gold Standard Reference Bundles:**  
- `skills/legal/medical-record-chronology/` (production-hardened controller + references)
- `skills/legal/form-d-exempt-offering-notice/` (production controller + 7 references + 11 evals)
- `skills/legal/demand-letter/` (controller + references + text exemplars)
- `skills/legal/ind-nonclinical-summary/` (CTD 2.4/2.6 controller + references)

---

## Part 1: Core Architecture & CI Constraints

Every upgraded skill must strictly comply with the repo's authoring standards and CI test suite (`scripts/embed-skills.test.js`, `scripts/validate_enrichment.py`, `.github/workflows/skill-qa.yml`):

1. **Exact Directory & Slug Matching:**
   - Directory name must match `name:` in frontmatter exactly (`^[a-z0-9]+(?:-[a-z0-9]+)*$`).
   - Check `spec/reserved-slugs.json`. Never rename or alias these slugs.
2. **Text-Only Bundles (Critical Gate):**
   - The publisher (`scripts/embed-skills.js`) and Case.dev MCP adapter require UTF-8 text files.
   - **Never** add binary files (`.pdf`, `.docx`, `.xlsx`, `.png`).
   - All exemplars, templates, and schemas must be `.md`, `.json`, or `.xml`.
3. **Reference Depth = 1:**
   - All companion documentation must live directly in `skills/<domain>/<slug>/references/*.md`.
   - Subdirectories within `references/` are forbidden.
   - Reference files must **never** contain relative markdown links `[...](other.md)` to other markdown files (flagged by `skill-qa.yml`).
   - Any reference file exceeding 100 lines must begin with a `## Contents` table of contents.
4. **Line and Budget Bounds:**
   - `skills/legal/`: `SKILL.md` body must be between 140 and 320 lines (hard CI limit: 500 lines).
   - `skills/med/` and `skills/finance/`: `SKILL.md` non-blank body lines must be between 100 and 400 lines (enforced by `scripts/validate_enrichment.py`).
5. **Required Headings (`med` and `finance`):**
   `scripts/validate_enrichment.py` regex-validates heading presence. Every `med` and `finance` skill must include:
   - `## Why This Skill Exists`
   - `## Checkpoint A: Pre-Draft Intake (Mandatory)`
   - `## Step 1: ...` (through Step N)
   - `## Checkpoint B: Post-Draft Alignment`
   - `## Quality Audit`
   - `## Guidelines`
   - `## Troubleshooting` (required by `spec/SKILL-SPEC.md`)
   Zero matches against `FILLER_PHRASES` in `scripts/validate_enrichment.py`.
6. **Frontmatter Specification:**
   - `language: en`
   - `description`: Third-person declarative ("Drafts...", "Evaluates...", "Tracks...", never "I draft" or starting with "Use this to"), maximum 1024 characters, dense with search triggers.
   - For `legal`: `tags` must only use the 19 controlled tags (`litigation`, `corporate`, `transactional`, `regulatory`, `agreement`, `pleading`, `motion`, `brief`, `memo`, `letter`, `summary`, `analysis`, `checklist`, `policy`, `drafting`, `summarization`, `research`, `funds`, `edgar`).
   - For `med` and `finance`: Preserve existing `tags` and `metadata` (`author`, `practice_areas`, `document_types`, `skill_modes`) blocks.
7. **Prompt Injection Guardrails:**
   Zero occurrences of disallowed patterns from `skill-qa.yml` (`you are now`, `ignore previous instructions`, `system:`, `fetch http`, `curl http`, `eval(`, `exec(`).

---

## Part 2: Deliverable Structure Per Skill

Each upgraded skill directory must contain:

```
skills/<domain>/<slug>/
├── SKILL.md                          # Controller file (140-300 lines)
├── references/                       # 2 to 4 modular reference guides (1 level deep)
│   ├── output-template.md            # Deliverable schema + reconciliation table + hand-off table
│   ├── <domain-rules-or-guide>.md    # Deep technical rules, formulas, statutes, criteria
│   └── primary-sources.md            # Authoritative sources checked + [VERIFY] items
└── evals/                            # Behavioral regression suite
    └── evals.json                    # 3-5 adversarial test prompts targeting the trap map
```

### The `SKILL.md` Controller Anatomy
1. **Frontmatter:** Canonical `name`, `language`, `description`, `tags`, and `metadata`.
2. **Title & One-line Purpose Statement:** Plain `# Title` followed by exact objective.
3. **`## Why This Skill Exists` & `### Where Mistakes Hide` (Trap Map):**
   A structured markdown table:
   | Input / Document | What It Is Used For | Where the Error Hides |
   Exposes common failure modes (relying on summaries, conflating clinical criteria, skipping statutory notice, assuming book accounting equals tax rules).
4. **Numbered Ground Rules:**
   - *Draft only*: Always requires qualified human review (attorney, clinician, CPA).
   - *Source-review gate*: Never call an item missing without checking inventory and trying extraction. Classify gaps (`unknown fact`, `source conflict`, `unverified external lookup`, `policy election`).
   - *Hierarchy of authority*: Primary executed instruments / raw clinical records / audited figures govern over summaries, transmittal emails, or ledgers. Name conflicts explicitly; never resolve silently.
   - *Citation discipline*: Every material fact, clinical value, or accounting figure must have a source locator or `[UNVERIFIED]`.
5. **`## Checkpoint A: Pre-Draft Intake (Mandatory)`:**
   Numbered checklist of required inputs, documents to request, plus explicit default fallbacks vs. hard-stop conditions.
6. **`## Step 1` to `## Step N` (Workflow):**
   Ordered operational steps instructing the agent when to read companion files in `references/`.
7. **`## Checkpoint B: Post-Draft Alignment`:**
   Sanity audit against scope, limits, and client objectives.
8. **`## Quality Audit` (10–13 Point Gate):**
   Verification checklist before emitting final response.
9. **`## Guidelines` & `## Troubleshooting`:**
   Boundaries, ethical constraints, and handling degraded/unreadable inputs.

---

## Part 3: Target Skill Manifest (44 Skills)

### Batch 1: Legal Litigation (5 skills)
- `bad-faith-demand`
- `demand-letter`
- `summary-judgment-brief`
- `coverage-opinion`
- `expert-report-on-damages`

### Batch 2: Legal Transactions & M&A (5 skills)
- `hsr-filing`
- `merger-agreement`
- `disclosure-schedules`
- `due-diligence-report`
- `class-action-settlement`

### Batch 3: Legal Regulatory & IP (4 skills)
- `stark-law-aks-compliance`
- `fcpa-compliance-policy`
- `aml-compliance-program`
- `patent-infringement-analysis`

### Batch 4: Med Acute Care (5 skills)
- `managing-sepsis-bundles`
- `managing-acute-stroke`
- `managing-acute-coronary-syndromes`
- `interpreting-fetal-monitoring`
- `assessing-suicide-risk`

### Batch 5: Med Pharmacotherapy & Clinical (5 skills)
- `managing-chemotherapy-protocols`
- `reconciling-medications`
- `managing-anticoagulation-therapy`
- `managing-drg-optimization`
- `managing-risk-adjustment-coding`

### Batch 6: Med Compliance & Revenue Cycle (5 skills)
- `conducting-false-claims-analysis`
- `conducting-stark-law-analysis`
- `managing-emtala-compliance`
- `managing-coding-denials`
- `managing-privacy-breach-response`

### Batch 7: Finance Tax Planning & Structuring (5 skills)
- `managing-transfer-pricing-compliance`
- `analyzing-international-tax-planning`
- `analyzing-m-and-a-tax-implications`
- `analyzing-corporate-tax-structures`
- `managing-tax-controversy`

### Batch 8: Finance Modeling & Valuation (5 skills)
- `building-lbo-models`
- `building-equity-valuation-models`
- `analyzing-earnings-quality`
- `managing-debt-covenant-compliance`
- `writing-investment-committee-memos`

### Batch 9: Finance Accounting, Audit & Underwriting (5 skills)
- `managing-estate-and-gift-tax`
- `managing-revenue-recognition`
- `analyzing-loss-reserves`
- `managing-commercial-loan-underwriting`
- `auditing-aml-transactions`

---

## Part 4: Sub-Agent Execution Instructions

When a sub-agent is assigned a specific skill `skills/<domain>/<slug>`:

1. **Inspect current state:** Read `skills/<domain>/<slug>/SKILL.md`. Identify current line count and missing structural elements.
2. **Verify primary domain facts:** Use web search to verify statutory citations, regulations, clinical scoring systems, or accounting standards. Mark anything that varies or is jurisdiction-contingent as `[VERIFY]`.
3. **Draft companion references:**
   - Create `references/output-template.md` (deliverable structure, reconciliation worksheet, hand-off table).
   - Create `references/<technical-rules>.md` (deep rules, formulas, checklists).
   - Create `references/primary-sources.md` (authoritative texts checked + verification items).
4. **Draft the `SKILL.md` controller:**
   - Keep within 140–320 lines.
   - Insert the trap map table under `Why This Skill Exists`.
   - Add all required section headers.
   - Integrate references cleanly without relative cross-links between reference files.
5. **Add regression evaluations:**
   - Create `evals/evals.json` with 3 to 5 adversarial prompts.
6. **Validate locally before yielding:**
   - Ensure no binary files exist in the skill directory.
   - For `med` or `finance`: run `python3 scripts/validate_enrichment.py --vertical <vertical> --only-failures`.
   - Run repo bundle tests: `node --test scripts/embed-skills.test.js scripts/repair-bundles.test.js scripts/skills-catalog.test.js`.
