---
name: expert-omissions-analysis
description: Analyzes expert witness testimony and reports against complete medical record sets to identify omissions, inconsistencies, and gaps in the expert's review. Generates a structured report with citations, bias patterns, and strategic recommendations for cross-examination and Daubert/Frye challenges. Use when reviewing opposing expert reports, preparing cross-examination, filing motions to exclude, or retaining rebuttal experts in personal injury or medical malpractice cases.
tags:
  - analysis
  - litigation
---

# Expert Witness Medical Records Omissions Analysis

Identifies records the expert missed or ignored, evaluates impact on their opinions, and produces an impeachment-ready report.

## Prerequisites

1. **Complete medical record set** — all records produced in discovery, Bates-stamped or indexed
2. **Expert materials** — report(s), deposition transcript(s), CV, and any supplemental declarations
3. **Expert's stated materials-reviewed list** — extract from report or deposition testimony
4. **Case chronology** — timeline of treatment, injuries, and key medical events

## Process

### Step 1 — Inventory & Cross-Reference

Build a comparison matrix:

| Column | Source |
|---|---|
| Record ID / Bates range | Case medical records |
| Date of service | Medical records |
| Provider / facility | Medical records |
| Record type | Clinical note, imaging, lab, operative, etc. |
| Cited by expert? | Yes / No / Partial |
| Expert report page / depo cite | Expert materials |

Flag every record where **Cited by expert = No or Partial**.

### Step 2 — Classify Omissions

For each flagged record, assign a category and priority:

| Priority | Criteria |
|---|---|
| **Critical** | Contradicts expert's opinion, documents alternative causation, or reveals undisclosed pre-existing condition |
| **High** | Fills a gap the expert's chronology skips, documents treatment decisions expert failed to address |
| **Moderate** | Provides context that would qualify or weaken expert's conclusions |
| **Low** | Cumulative or unlikely to affect opinion's foundation |

### Step 3 — Analyze Methodology Deficiencies

Evaluate the expert's review process for:

- [ ] Did the expert provide a complete materials-reviewed list?
- [ ] Does the expert's chronology match the actual medical timeline?
- [ ] Are there factual assertions contradicted by records the expert *claims* to have reviewed?
- [ ] Did the expert acknowledge and explain any gaps?
- [ ] Does the expert's methodology satisfy Daubert/Frye reliability factors?

### Step 4 — Identify Bias Patterns

Look for systematic patterns in what was omitted:

- Omissions cluster around records supporting opposing theory
- Pre-existing conditions consistently excluded
- Unfavorable imaging or lab results ignored while favorable ones cited
- Selective quotation from records (partial citation)
- Temporal gaps that obscure intervening causes

### Step 5 — Generate Report

Structure the deliverable as follows:

```
EXPERT OMISSIONS ANALYSIS
Case: [Case Name] | Expert: [Name, Specialty] | Date: [Date]

I.   EXECUTIVE SUMMARY
     - Total records in file: [n]
     - Records not cited by expert: [n]
     - Critical/High omissions: [n]
     - Key finding: [1-2 sentences]

II.  OMISSIONS TABLE
     [Full matrix from Step 1, filtered to omitted records, sorted by priority]

III. CRITICAL OMISSIONS — DETAILED ANALYSIS
     For each Critical/High item:
     A. Omitted record: [ID, date, provider, type]
     B. Content summary: [key findings in the record]
     C. Expert's statement: [quote + cite]
     D. Impact: [how omission affects opinion's foundation]

IV.  METHODOLOGY DEFICIENCIES
     [Checklist results from Step 3 with supporting citations]

V.   BIAS PATTERN ANALYSIS
     [Patterns from Step 4 with statistical support where possible]

VI.  STRATEGIC RECOMMENDATIONS
     A. Cross-examination questions [numbered, with pin cites]
     B. Daubert/Frye challenge points
     C. Rebuttal expert focus areas
     D. Deposition follow-up topics (if discovery ongoing)
```

## Guidelines

- **Pin-cite everything** — every assertion must reference a specific Bates number, deposition page:line, or report page
- **Distinguish genuine impeachment from minor gaps** — flag low-priority items but do not overstate their significance
- **Maintain objectivity** — note where omissions may be defensible (e.g., record is cumulative or irrelevant to the specific opinion rendered)
- **Daubert factors to address**: testability, peer review, error rate, general acceptance, fit to facts [VERIFY: *Daubert v. Merrell Dow Pharmaceuticals*, 509 U.S. 579 (1993)]
- **Frye jurisdictions**: flag if applicable — standard is general acceptance only [VERIFY: *Frye v. United States*, 293 F. 1013 (D.C. Cir. 1923)]
- Adapt for both **plaintiff-side** (challenging defense IME expert) and **defense-side** (challenging treating physician opinions or plaintiff's retained expert)
- Do not render medical opinions — identify what the records say and what the expert missed, not whether the expert's medical conclusion is correct
