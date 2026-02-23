---
name: medical-billing-analysis
description: Analyzes medical records and billing information for personal injury litigation, extracting treatment details, costs, causation chains, and inconsistencies. Organizes data chronologically, evaluates charge reasonableness, and flags issues for further review. Use when reviewing medical records, billing statements, treatment summaries, damage calculations, or case valuation during discovery and pre-trial phases.
tags:
  - analysis
  - litigation
---

# Medical and Billing Records Analysis

Analyzes medical records and billing data for litigation, producing a structured chronological report covering treatment, costs, causation, and red flags.

## Prerequisites

1. **Medical records** — treatment notes, diagnostic reports, surgical records, discharge summaries, pharmacy records
2. **Billing statements** — itemized bills from all providers, EOBs, insurance payment records
3. **Incident information** — date of incident/onset, mechanism of injury, and any pre-existing condition history
4. **IME or peer review reports** (if available)

## Process

### Step 1: Document Inventory

Scan all uploaded documents and classify each into:

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

### Step 2: Medical Timeline

Build a chronological table:

| Date | Provider/Facility | Visit Type | Diagnoses (ICD) | Procedures (CPT) | Key Findings | Restrictions/Prognosis |
|---|---|---|---|---|---|---|

Flag:
- [ ] Gaps in treatment > 30 days
- [ ] Changes in diagnosis or treatment plan
- [ ] New providers or referrals
- [ ] Causation statements by treating physicians
- [ ] Pre-existing condition references
- [ ] Work/activity restrictions and duration

### Step 3: Billing Analysis

Catalog all charges:

| Date | Provider | CPT/Code | Description | Billed | Insurance Paid | Adjustment | Patient Owed |
|---|---|---|---|---|---|---|---|

Summarize totals by category:

| Category | Total Billed | Total Paid | Outstanding |
|---|---|---|---|
| Emergency services | | | |
| Hospitalization/surgery | | | |
| Diagnostic imaging | | | |
| Physical/occupational therapy | | | |
| Medications | | | |
| Mental health | | | |
| Ongoing/future care | | | |
| **TOTAL** | | | |

### Step 4: Reasonableness Review

For each major charge category, assess:

- [ ] Charges consistent with geographic area and specialty norms
- [ ] No duplicate billing for same service/date
- [ ] All billed services have corresponding medical documentation
- [ ] Treatment consistent with documented diagnoses and injuries
- [ ] No charges for unrelated conditions without clear explanation

### Step 5: Causation Analysis

Trace the chain from incident to treatment:

1. **Direct causation statements** — quote treating physicians verbatim with document/page citations
2. **Pre-existing conditions** — identify any documented history and whether providers distinguished aggravation vs. new injury
3. **Conflicting opinions** — catalog disagreements between treating physicians, IME doctors, or peer reviewers
4. **Treatment necessity** — note any provider statements on whether treatment was reasonable and necessary

### Step 6: Red Flags and Issues

Flag anything requiring attorney attention:

| Issue | Details | Source (doc/page) | Suggested Action |
|---|---|---|---|
| Gap in treatment | e.g., 3-month gap after ER visit | Record X, p. 4 | Obtain explanation from client |
| Billing without documentation | e.g., PT charges with no notes | Bill Y, line 12 | Request supporting records |
| Causation dispute | e.g., IME attributes symptoms to prior condition | IME report, p. 7 | Consider rebuttal expert |
| Excessive charges | e.g., charges above area norms | Bill Z, line 5 | Evaluate with billing expert |

## Output Format

Deliver a single structured report with these sections:

1. **Document Inventory** — what was reviewed
2. **Medical Timeline** — chronological table
3. **Treatment Summary** — narrative overview of injuries, treatment course, and current status
4. **Billing Summary** — totals by category with line-item detail available
5. **Causation Analysis** — supported chain with citations
6. **Issues and Red Flags** — table of flagged items with recommended actions
7. **Expert Needs** — identify where expert testimony may be required (life care planner, billing expert, medical specialist)

## Guidelines

- Cite specific documents and page numbers for every factual finding
- Never opine on ultimate legal conclusions (liability, damages awards)
- Distinguish between what treating physicians documented vs. IME/defense opinions
- Note where records are missing or incomplete rather than assuming
- Flag but do not resolve billing disputes — identify for attorney review
- If future care costs are projected by any provider, extract and itemize separately
- All dollar amounts should be presented consistently (no mixing of rounded and exact figures)
