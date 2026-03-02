# AgentSkills Expansion Plan: Medical & Capital

## Overview

Extending the AgentSkills framework from `agentskills.legal` (874 skills) into two new verticals:
- **`agentskills.med`** — Medical / Healthcare (400 skills, 20 subgroups)
- **`agentskills.capital`** — Capital / Financial Services (400 skills, 20 subgroups)

Each skill encodes a **semi-structured agentic workflow** — not just knowledge, but a repeatable process for moving information from messy inputs to structured outputs. The agent follows the skill like a junior professional follows a senior's playbook.

**Status**: 800 skills generated and committed. PR [#4](https://github.com/CaseMark/skills/pull/4) open on branch `bench/ASL-9-add-med-finance-skills`. Linear ticket: [ASL-9](https://linear.app/casemarkai/issue/ASL-9).

---

## Design Principles (from Claude Best Practices)

1. **Concise** — Claude is smart; only encode what it doesn't know (domain conventions, regulatory constraints, output formats, decision trees)
2. **Progressive disclosure** — SKILL.md is the entry point (<500 lines); detailed reference in sub-files
3. **Gerund naming** — `summarizing-discharge-notes`, not `discharge-note-summarizer`
4. **Third-person descriptions** — "Synthesizes clinical trial data into..." not "I help you..."
5. **Appropriate degrees of freedom** — High freedom for analysis/synthesis, low freedom for compliance-critical outputs
6. **Feedback loops** — Validate -> fix -> repeat for quality-critical workflows
7. **Executable scripts where useful** — Python helpers for parsing, validation, formatting

---

## Taxonomy Design

Skills are grouped by **subgroup** (analogous to legal practice areas). Each subgroup contains 20 skills. Skills answer: "Given [input type], what structured process produces [output type] that a professional would trust?"

### Directory Structure

Flat directory structure matching legal (no subgroup folders):

```
skills/
  skills/
    med/
      triaging-emergency-presentations/SKILL.md
      managing-trauma-assessments/SKILL.md
      ... (400 skill directories)
    capital/
      summarizing-earnings-calls/SKILL.md
      analyzing-financial-ratios/SKILL.md
      ... (400 skill directories)
  scripts/
    taxonomy_med.py          # Medical taxonomy (source of truth)
    taxonomy_capital.py      # Capital taxonomy (source of truth)
    generate_skills.py       # Generates all SKILL.md files from taxonomies
```

Subgroups are a **logical concept** encoded via tags and `practice_areas` metadata — not directory structure.

---

## AgentSkills.med — Medical (400 skills)

### Subgroup Summary

| # | Subgroup | Skills | Focus |
|---|----------|--------|-------|
| 1 | Emergency Medicine | 20 | ED triage, acute assessment, trauma, resuscitation |
| 2 | Hospital Medicine | 20 | Admission, rounding, discharge, inpatient transitions |
| 3 | Primary Care | 20 | Preventive care, chronic disease management, wellness |
| 4 | Surgery | 20 | Perioperative planning, operative reports, post-op management |
| 5 | Radiology | 20 | Imaging interpretation, reporting, RADS classifications |
| 6 | Pathology | 20 | Tissue diagnosis, lab analysis, quality workflows |
| 7 | Pharmacy | 20 | Medication management, interactions, formulary decisions |
| 8 | Oncology | 20 | Cancer staging, treatment protocols, survivorship |
| 9 | Psychiatry | 20 | Mental health assessment, treatment planning, crisis management |
| 10 | Cardiology | 20 | Cardiac diagnostics, interventions, device management |
| 11 | Obstetrics and Gynecology | 20 | Prenatal care, labor management, gynecologic procedures |
| 12 | Pediatrics | 20 | Growth monitoring, developmental assessment, pediatric conditions |
| 13 | Medical Coding and Billing | 20 | ICD/CPT coding, billing compliance, revenue cycle |
| 14 | Clinical Research | 20 | Protocol design, IRB management, data analysis |
| 15 | Nursing | 20 | Care planning, patient assessment, nursing documentation |
| 16 | Healthcare Compliance | 20 | HIPAA, accreditation, quality reporting |
| 17 | Health Informatics | 20 | EHR optimization, data analytics, interoperability |
| 18 | Public Health | 20 | Epidemiology, surveillance, program evaluation |
| 19 | Dental Medicine | 20 | Oral diagnosis, treatment planning, dental procedures |
| 20 | Rehabilitation Medicine | 20 | Functional assessment, therapy planning, disability evaluation |

### Name Collisions Resolved

Two cross-subgroup collisions were fixed during generation:
- `managing-trauma-assessments` — exists in Emergency Medicine (physical trauma); Psychiatry version renamed to `managing-psychological-trauma-assessments`
- `managing-psychiatric-emergencies` — exists in Emergency Medicine; Psychiatry version renamed to `managing-acute-psychiatric-crises`

---

## AgentSkills.capital — Capital (400 skills)

### Subgroup Summary

| # | Subgroup | Skills | Focus |
|---|----------|--------|-------|
| 1 | Equity Research | 20 | Public equity analysis, valuation, coverage initiation |
| 2 | Fixed Income | 20 | Bond analysis, credit assessment, structured products |
| 3 | Investment Banking | 20 | M&A advisory, capital markets, deal execution |
| 4 | Private Equity | 20 | PE/VC evaluation, portfolio monitoring, fund operations |
| 5 | Asset Management | 20 | Portfolio construction, performance attribution, rebalancing |
| 6 | Risk Management | 20 | VaR, stress testing, operational and market risk |
| 7 | Financial Compliance | 20 | AML, KYC, regulatory examination, surveillance |
| 8 | Corporate Finance | 20 | Treasury, capital structure, cash flow forecasting |
| 9 | Accounting | 20 | Financial reporting, audit, revenue recognition |
| 10 | Real Estate Finance | 20 | Property valuation, REIT analysis, mortgage underwriting |
| 11 | Insurance | 20 | Underwriting, actuarial analysis, claims management |
| 12 | Quantitative Finance | 20 | Derivatives pricing, algorithmic strategies, statistical modeling |
| 13 | Financial Technology | 20 | Payment systems, digital banking, blockchain analysis |
| 14 | Tax | 20 | Corporate tax planning, transfer pricing, tax compliance |
| 15 | Wealth Management | 20 | Estate planning, HNW advisory, retirement planning |
| 16 | Fund Operations | 20 | NAV calculation, fund accounting, regulatory reporting |
| 17 | Financial Planning and Analysis | 20 | Budgeting, variance analysis, management reporting |
| 18 | Commercial Banking | 20 | Lending, credit analysis, trade finance |
| 19 | Sustainable Finance | 20 | ESG integration, green bonds, impact measurement |
| 20 | Economic Analysis | 20 | Macro forecasting, policy analysis, economic indicators |

---

## Skill File Format

Each generated SKILL.md follows this structure:

```yaml
---
name: gerund-style-name
description: Third-person description (<1024 chars) with "Use when..." triggers.
tags:
  - workflow-type-tag
  - subgroup-tag
metadata:
  author: casemark
  practice_areas:
    - Subgroup Practice Area
  document_types:
    - Report Type
  skill_modes:
    - Primary Mode
---
# Human Readable Title

One-line summary.

## Workflow
1. **Step** -- action
(5 steps, contextual to workflow verb type)

## Key Rules
(5 universal rules)

## Guidelines
(5 contextual guidelines with domain and practice areas)
```

### Constraints

| Property | Constraint |
|----------|-----------|
| Name | Gerund form, lowercase-hyphenated, max 64 chars |
| Description | Third-person, max 1024 chars, includes "Use when..." triggers |
| Tags | Array, includes workflow type + subgroup identifier |
| Body | Under 500 lines |
| Reference files | One level deep from SKILL.md |

---

## Generation Pipeline

The skills are generated from Python taxonomy definitions:

1. **`scripts/taxonomy_med.py`** — Defines 20 medical subgroups with 20 skills each (names + descriptions)
2. **`scripts/taxonomy_capital.py`** — Defines 20 capital subgroups with 20 skills each (names + descriptions)
3. **`scripts/generate_skills.py`** — Reads both taxonomies, generates SKILL.md files with:
   - Fully unique frontmatter (name, description, tags, metadata) per skill
   - Templated workflow steps based on the skill's gerund verb category (analyzing, drafting, managing, etc.)
   - Domain-contextualized guidelines referencing the skill's subgroup and practice areas

**Regeneration**: Delete `skills/med/` and `skills/capital/`, then run `python3 scripts/generate_skills.py` to regenerate all 800 skills.

---

## Enrichment Tiers (Future Work)

Not all 800 skills need the same body depth. The current state has fully crafted frontmatter but templated bodies. Enrichment tiers:

### Tier 1 — Full enrichment with reference files and scripts (~40 skills)
Highest-value, most complex workflows. Domain-specific workflow steps, output templates, reference files, and Python helper scripts.

**Med examples**: `summarizing-discharge-notes`, `coding-medical-encounters`, `reconciling-medications`, `abstracting-medical-records`, `writing-prior-authorizations`

**Capital examples**: `summarizing-earnings-calls`, `analyzing-financial-ratios`, `auditing-aml-transactions`, `drafting-investment-memos`, `reconciling-accounts`

### Tier 2 — Standard enrichment (~200 skills)
Domain-specific workflow steps and output templates in SKILL.md. No reference files.

### Tier 3 — Current state (~560 skills)
Fully crafted frontmatter with templated bodies. Suitable for agents that primarily need the description/tags to know when to apply the skill.

---

## Scripts Inventory (Future)

Python helper scripts planned for Tier 1 skills:

| Script | Used By | Purpose |
|--------|---------|---------|
| `validate_icd10.py` | `coding-medical-encounters` | Validate ICD-10 code format |
| `parse_lab_ranges.py` | `analyzing-lab-results` | Flag values outside reference ranges |
| `med_interaction_check.py` | `assessing-drug-interactions` | Check known interaction databases |
| `financial_ratio_calc.py` | `analyzing-financial-ratios` | Calculate standard financial ratios |
| `reconciliation_matcher.py` | `reconciling-accounts` | Fuzzy-match transactions across sources |
| `aml_red_flags.py` | `auditing-aml-transactions` | Pattern detection for suspicious activity |
| `covenant_calculator.py` | `managing-covenant-compliance` | Calculate covenant metrics from financials |

---

## Remaining Work

### Immediate
1. **Thurgood re-review** on PR #4 for the 800-skill expansion commit
2. **Merge PR #4** once CI and review pass

### Near-term
3. **Tier 1 enrichment** — Enrich ~40 high-priority skill bodies with domain-specific workflows, output templates, and reference files
4. **Python utility scripts** — Build helper scripts for calculation-heavy Tier 1 skills

### Future
5. **Embedding pipelines** — GitHub Actions workflows (`med-embed.yml`, `capital-embed.yml`) for skill search/retrieval
6. **Website deployment** — Stand up `agentskills.med` and `agentskills.capital` sites
7. **Cross-vertical references** — Link skills that span med+legal or capital+legal (recommendation: cross-reference, don't duplicate)

---

## Open Design Questions

1. **Cross-vertical skills**: Some skills span med+legal (medical malpractice) or capital+legal (securities litigation). **Decision**: Cross-reference via Related Skills metadata. Don't duplicate.

2. **Regulatory jurisdictions**: Medical and financial regulations vary by country. **Decision**: US-first, with hooks for jurisdiction parameters.

3. **Data sensitivity**: Both verticals handle sensitive data. **Decision**: Include PHI/PII handling instructions. Reference `hipaa-compliance` for med, create `financial-data-handling` reference for capital.

4. **Case.dev integration**: **Decision**: Include optional Case.dev vault/agent API integration patterns for Tier 1 skills.

---

## Success Criteria

A skill is "done" when:
1. An agent can follow it to produce output a domain professional would accept as a reasonable first draft
2. The skill correctly identifies when it should NOT proceed (e.g., missing critical info, out of scope)
3. Compliance-sensitive skills include appropriate disclaimers and human-in-the-loop checkpoints
4. The skill passes 3+ evaluation scenarios
