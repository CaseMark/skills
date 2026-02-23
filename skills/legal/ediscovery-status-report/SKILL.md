---
name: ediscovery-status-report
description: Generates a structured internal e-discovery status report tracking ESI lifecycle from collection through attorney review. Covers custodian-level data volumes, search term hit rates and precision, relevance and privilege coding statistics, reviewer productivity, and projected completion timelines. Output is marked attorney work product. Use during the discovery phase of U.S. commercial litigation to report e-discovery progress to counsel, case managers, and clients.
tags:
  - litigation
  - summarization
  - summary
---

# E-Discovery Collection & Review Status Report

Produces an internal work-product status report tracking ESI from collection through attorney review for U.S. commercial litigation.

## Prerequisites

1. **Vendor collection logs** — CSV/JSON/structured processing reports with custodian names, item counts, GB volumes, file types, processing status
2. **Review platform exports** — coding reports with document counts, reviewer IDs, coding dates, relevance/privilege/issue-tag designations
3. **Search term results** — hit counts per query string, and precision/validation sampling data if available
4. **Privilege log drafts or attorney review summaries** — finalized privilege assertions with custodian and document-type breakdowns

If any source is missing, flag the gap and request the data before proceeding. Document all gaps in the report with explicit caveats.

## Output Structure

### 1. Executive Summary
- Collection completeness status
- Search strategy effectiveness (one sentence)
- Review progress % and projected completion date
- Critical issues requiring immediate action

---

### 2. Collection Metrics by Custodian

| Custodian | GB Collected | Items | Email % | Office Doc % | Other % | Processing Status |
|-----------|-------------|-------|---------|-------------|---------|------------------|
| [Name]    | [X.X]       | [N]   | [X%]    | [X%]        | [X%]    | Complete / Pending / Error |

**Flags to surface:**
- Custodians with volume >2× matter average (possible over-collection or key player)
- Custodians with unexpectedly low volume (incomplete collection risk)
- Processing error rates >5% by custodian or file type

**Validation check:** Collected ≥ Processed ≥ Loaded to platform ≥ Reviewed. Explain any downward discrepancy.

---

### 3. Search Term Performance

| Search Term / Boolean String | Hits | Hit Rate (% of population) | Precision (if sampled) | Status |
|-----------------------------|------|---------------------------|----------------------|--------|
| [Term]                      | [N]  | [X%]                      | [X%]                 | Keep / Refine / Drop |

- Flag terms with hit rate >30% (likely overbroad) or <0.5% (likely underperforming)
- Calculate inter-term overlap; recommend consolidation where redundancy is high
- If precision data exists, project likely relevant yield from unreviewed hits

---

### 4. Review Progress

| Metric | Count | % of Loaded |
|--------|-------|------------|
| Documents loaded to platform | [N] | 100% |
| Reviewed | [N] | [X%] |
| Coded Relevant | [N] | [X%] |
| Coded Privileged | [N] | [X%] |
| Coded Non-Responsive | [N] | [X%] |
| Remaining | [N] | [X%] |

**Reviewer Productivity Table:**

| Reviewer | Docs Reviewed | Avg Docs/Hr | Relevance Rate | Privilege Rate |
|----------|--------------|-------------|---------------|---------------|
| [Name]   | [N]          | [X]         | [X%]          | [X%]          |

- Flag reviewers with coding patterns >15% above/below team average (QC concern)
- Review velocity trend: [accelerating / decelerating / stable], basis: [weekly rolling avg]
- **Projected completion:** [Date] at current pace of [N] docs/day — assumptions: [state clearly]

---

### 5. Privilege Analysis

| Custodian | Docs Reviewed | Privilege Assertions | Privilege Rate |
|-----------|--------------|---------------------|---------------|
| [Name]    | [N]          | [N]                 | [X%]          |

- Overall privilege rate: [X%] — [within/outside] expected range for this matter type
- Privilege rate by document type (email vs. office docs vs. other)
- Flag custodians with rates >2× matter average for senior attorney QC review

---

### 6. Recommendations & Timeline

- **Resource needs:** [additional reviewers / vendor remediation / search term refinement]
- **Search strategy adjustments:** [specific terms to modify]
- **QC actions:** [reviewer-specific or category-specific]
- **Risk items:** [gaps, processing failures, tight deadlines]
- **Milestone projections:**
  - Processing complete: [Date]
  - First-pass review complete: [Date]
  - Privilege log ready: [Date]

---

## Guidelines

- **Work product protection**: Mark final report "ATTORNEY WORK PRODUCT — PRIVILEGED AND CONFIDENTIAL." Limit distribution to litigation team members with case management need.
- **Custodian normalization**: Reconcile naming inconsistencies across vendor and platform exports into a single canonical custodian list before aggregating metrics.
- **Privilege statistics**: Present in aggregate only — do not reveal substance of privileged communications or attorney mental impressions.
- **Adverse findings**: Report collection gaps, QC failures, and search strategy weaknesses completely and without minimization so counsel can make informed decisions.
- **Audit trail**: Document how discrepancies were resolved and what validation steps were taken; this may be relevant if the e-discovery process is challenged.
- **Methodology transparency**: State assumptions underlying all projections explicitly in the report.
