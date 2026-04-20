---
name: medical-billing-analysis
language: en
description: >
  Analyzes medical records and billing data for personal injury litigation,
  producing a chronological report with treatment details, costs, causation
  chains, and red flags. Trigger when the user requests medical billing analysis,
  medical records review, treatment timeline, billing reasonableness review,
  causation analysis, damages documentation, PI case valuation, ICD/CPT code
  review, IME rebuttal prep, or needs to organize medical evidence for a demand
  package or mediation statement.
tags:
  - analysis
  - litigation
---

# Medical Billing Analysis

Produces a litigation-ready analysis of medical records and billing data for personal injury cases. Every finding is cited to a specific document and page. Output supports demand packages, mediation statements, and trial preparation.

## Quick Start

1. Gather records and billing from the user (or confirm what's uploaded)
2. Build document inventory and medical timeline
3. Analyze billing, check reasonableness, trace causation
4. Flag red flags, deliver structured report
5. Align with user on gaps and next steps

## Intake (Mandatory)

Ask every time unless user says "use defaults" or "just draft":

1. **Medical records** — treatment notes, diagnostics, surgical records, discharge summaries, pharmacy records
2. **Billing statements** — itemized bills from all providers, EOBs, insurance payment records
3. **Incident information** — date, mechanism of injury, pre-existing condition history
4. **IME or peer review reports** (if available)

**Request if missing:** provider itemized bills (not just totals), EOBs, lien statements (Medicare/Medicaid/ERISA/hospital), pre-incident records if pre-existing conditions at issue, life care plan if available.

**Defaults when user doesn't respond:** analyze all provided records chronologically; flag treatment gaps > 30 days; separate billed vs. paid; identify causation statements. Label defaults clearly.

Flag missing materials explicitly and proceed with what's available.

## Workflow

### 1. Document Inventory

Classify each document:

| Category | Examples |
|---|---|
| Emergency/acute care | ER records, ambulance reports |
| Inpatient | Hospital admissions, surgical notes |
| Outpatient/specialist | Orthopedic, neurological, pain management |
| Diagnostic imaging | X-ray, MRI, CT reports |
| Therapy | PT, OT, chiropractic, psychological |
| Pharmacy | Prescription records, medication logs |
| Billing/financial | Itemized bills, EOBs, lien statements |
| IME/peer review | Defense or insurance medical evaluations |

### 2. Medical Timeline

Build chronological table with: Date, Provider/Facility, Visit Type, Diagnoses (ICD), Procedures (CPT), Key Findings, Restrictions/Prognosis.

Flag: gaps > 30 days, diagnosis changes, new providers/referrals, causation statements by treating physicians, pre-existing condition references, work/activity restrictions.

### 3. Billing Analysis

Catalog charges with: Date, Provider, CPT/Code, Description, Billed, Insurance Paid, Adjustment, Patient Owed.

Summarize totals by category: emergency, hospitalization/surgery, imaging, therapy, medications, mental health, ongoing/future care.

### 4. Reasonableness Review

For each major charge category, verify:
- Charges consistent with geographic/specialty norms
- No duplicate billing for same service/date
- All billed services have corresponding documentation
- Treatment consistent with documented diagnoses
- No unrelated-condition charges without explanation

### 5. Causation Analysis

1. **Direct causation** — quote treating physicians verbatim with doc/page citations
2. **Pre-existing conditions** — documented history; aggravation vs. new injury distinguished
3. **Conflicting opinions** — disagreements between treating, IME, and peer reviewers
4. **Treatment necessity** — provider statements on reasonable and necessary care

### 6. Red Flags

Flag items requiring attorney attention in a table: Issue, Details, Source (doc/page), Suggested Action.

Common flags: treatment gaps, billing without documentation, causation disputes, charges above area norms.

### 7. Final Report

Deliver a single report with these sections:

**Front matter (required):**
- Documents reviewed with date ranges
- Assumptions and limitations
- Open items (requested but not received)

**Body:**
1. Document Inventory
2. Medical Timeline (chronological table)
3. Treatment Summary (narrative: injuries, treatment course, current status)
4. Billing Summary (category totals with line-item detail available)
5. Causation Analysis (supported chain with citations)
6. Issues and Red Flags (table with recommended actions)
7. Expert Needs (life care planner, billing expert, medical specialist)

## Post-Draft Alignment (Mandatory)

After delivering the initial analysis, ask:

1. Additional providers or records not yet received?
2. Client explanations for treatment gaps?
3. Specific causation disputes to analyze deeper?
4. Future care cost projection needed?

If no response, recommend obtaining missing provider records and proceed if authorized.

## Quality Checklist

- [ ] Every finding cites specific document and page
- [ ] Timeline complete and chronological, no unexplained gaps
- [ ] Billing totals reconcile (billed = paid + adjustments + patient owed)
- [ ] Causation statements quoted verbatim with citations
- [ ] Pre-existing conditions distinguished from incident-related injuries
- [ ] Duplicate charges identified and flagged
- [ ] IME/defense opinions cataloged separately from treating physician findings
- [ ] Missing records noted, not assumed
- [ ] Dollar amounts consistent (no mixed rounding)
- [ ] Future care costs itemized separately if projected
- [ ] No opinions on ultimate legal conclusions

## Rules

- Cite document and page for every factual finding
- Never opine on liability or damages awards
- Distinguish treating physician documentation from IME/defense opinions
- Flag but do not resolve billing disputes — identify for attorney review
- Do not invent findings, diagnoses, causation opinions, or citations
- Include scope notice: "Draft analysis requiring attorney review. Figures based on provided documentation and stated assumptions."
