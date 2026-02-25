---
name: medical-billing-analysis
description: >
  Analyzes medical records and billing information for personal injury litigation,
  producing a structured chronological report covering treatment details, costs,
  causation chains, and red flags. Use this skill when the user mentions medical
  billing analysis, medical records review, treatment timeline, billing
  reasonableness review, causation analysis, damages documentation, PI case
  valuation, discovery medical records, or pre-trial medical summary. Also trigger
  when the user asks about treatment gaps, duplicate billing, ICD/CPT code review,
  IME rebuttal preparation, or needs to organize medical evidence for a demand
  package or mediation statement.
tags:
  - analysis
  - litigation
---

# Medical and Billing Records Analysis

## Why This Skill Exists

Medical records and billing data are the evidentiary backbone of every personal injury case, but they arrive as hundreds of pages of unstructured clinical notes, EOBs, and billing codes. Without systematic analysis, treatment gaps go unnoticed until deposition, duplicate charges inflate specials that get attacked at trial, causation statements are buried in progress notes, and defense IME opinions go unanswered. The difference between a well-organized medical summary and a pile of records often determines whether a case settles at full value or gets discounted.

This skill produces a litigation-ready analysis that attorneys can use for demand packages, mediation statements, and trial preparation — every finding cited to a specific document and page.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft." Gather:

1. **Medical records** — treatment notes, diagnostic reports, surgical records, discharge summaries, pharmacy records
2. **Billing statements** — itemized bills from all providers, EOBs, insurance payment records
3. **Incident information** — date of incident/onset, mechanism of injury, any pre-existing condition history
4. **IME or peer review reports** (if available)

**If the user doesn't respond**, apply and clearly label these defaults: analyze all provided records chronologically; flag treatment gaps > 30 days; separate billed vs. paid amounts; identify causation statements.

### Documents to Request

If not yet provided, request:
- All provider itemized bills (not just totals)
- EOBs or insurance payment summaries
- Lien statements (Medicare, Medicaid, ERISA, hospital)
- Pre-incident medical records if pre-existing conditions are at issue
- Life care plan or future care recommendations (if available)

If materials are missing, flag them explicitly and proceed with what's available.

---

## Step 1: Build Document Inventory

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

---

## Step 2: Construct Medical Timeline

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

---

## Step 3: Analyze Billing Data

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

---

## Step 4: Conduct Reasonableness Review

For each major charge category, assess:

- [ ] Charges consistent with geographic area and specialty norms
- [ ] No duplicate billing for same service/date
- [ ] All billed services have corresponding medical documentation
- [ ] Treatment consistent with documented diagnoses and injuries
- [ ] No charges for unrelated conditions without clear explanation

---

## Step 5: Perform Causation Analysis

Trace the chain from incident to treatment:

1. **Direct causation statements** — quote treating physicians verbatim with document/page citations
2. **Pre-existing conditions** — identify documented history and whether providers distinguished aggravation vs. new injury
3. **Conflicting opinions** — catalog disagreements between treating physicians, IME doctors, or peer reviewers
4. **Treatment necessity** — note provider statements on whether treatment was reasonable and necessary

---

## Step 6: Compile Red Flags and Issues

Flag anything requiring attorney attention:

| Issue | Details | Source (doc/page) | Suggested Action |
|---|---|---|---|
| Gap in treatment | e.g., 3-month gap after ER visit | Record X, p. 4 | Obtain explanation from client |
| Billing without documentation | e.g., PT charges with no notes | Bill Y, line 12 | Request supporting records |
| Causation dispute | e.g., IME attributes symptoms to prior condition | IME report, p. 7 | Consider rebuttal expert |
| Excessive charges | e.g., charges above area norms | Bill Z, line 5 | Evaluate with billing expert |

---

## Step 7: Produce Final Report

Deliver a single structured report with these sections:

1. **Document Inventory** — what was reviewed
2. **Medical Timeline** — chronological table
3. **Treatment Summary** — narrative overview of injuries, treatment course, and current status
4. **Billing Summary** — totals by category with line-item detail available
5. **Causation Analysis** — supported chain with citations
6. **Issues and Red Flags** — table of flagged items with recommended actions
7. **Expert Needs** — identify where expert testimony may be required (life care planner, billing expert, medical specialist)

### Mandatory Front Matter

At the top of every report:

1. **Documents Reviewed** — complete inventory with date ranges
2. **Assumptions and Limitations** — missing records, incomplete billing data, unverified pre-existing conditions
3. **Open Items** — records requested but not received

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the initial analysis, ask:

1. Are there additional providers or records we haven't received yet?
2. Do the treatment gaps have explanations the client has provided?
3. Should we prioritize any specific causation disputes for deeper analysis?
4. Is a future care cost projection needed (requires life care plan or provider recommendations)?

If the user doesn't answer, recommend obtaining missing provider records (most common gap) and proceed if authorized.

---

## Quality Audit

Before finalizing, verify:

- [ ] Every factual finding cites a specific document and page number
- [ ] Medical timeline is complete and chronological with no unexplained gaps
- [ ] Billing totals reconcile (billed = paid + adjustments + patient responsibility)
- [ ] Causation statements quoted verbatim with source citations
- [ ] Pre-existing conditions identified and distinguished from incident-related injuries
- [ ] Duplicate charges identified and flagged
- [ ] IME/defense opinions cataloged separately from treating physician findings
- [ ] Missing records noted rather than assumed
- [ ] Dollar amounts presented consistently (no mixing rounded and exact figures)
- [ ] Future care costs extracted and itemized separately if projected by any provider
- [ ] No opinions on ultimate legal conclusions (liability, damages awards)

---

## Guidelines

- Cite specific documents and page numbers for every factual finding
- Never opine on ultimate legal conclusions (liability, damages awards)
- Distinguish between what treating physicians documented vs. IME/defense opinions
- Note where records are missing or incomplete rather than assuming
- Flag but do not resolve billing disputes — identify for attorney review
- If future care costs are projected by any provider, extract and itemize separately
- All dollar amounts should be presented consistently
- Do not invent medical findings, diagnoses, or causation opinions
- Do not fabricate document citations or page references
- **Attorney work product** — include scope notice: "Draft analysis requiring attorney review. Figures based on provided documentation and stated assumptions."
