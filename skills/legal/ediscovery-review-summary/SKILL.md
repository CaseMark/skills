---
name: ediscovery-review-summary
description: >-
  Produces an internal U.S. litigation e-discovery status summary covering ESI
  collection, processing, search term hits, review throughput,
  relevance/privilege rates, and completion forecasts. Use during discovery to
  brief counsel, case managers, or clients on progress, risks, and resource
  needs; trigger keywords: e-discovery, ESI, collection log, processing
  report, data load summary, review statistics, coding report, search term
  results, privilege review, status report.
tags:
  - litigation
  - summarization
  - summary
---

# E-Discovery Collection & Review Summary

Internal status report that tracks ESI from collection through attorney review and projects completion.

## Prerequisites

1. Custodian list with identifiers and collection scope (systems, date ranges, locations)
2. Collection logs and processing reports from vendor
3. Review platform exports for coding, reviewer activity, and search term results
4. Search term list or Boolean queries used in the matter
5. Review protocol (relevance, privilege, issue tags) and QC standards
6. Milestones or deadlines that the review must meet
7. Protective order or confidentiality requirements for reporting

## Output Structure / Process

**1) Source Inventory**

| Source | Expected Format | Required Fields | Status | Notes |
|---|---|---|---|---|
| Collection log | CSV/JSON | custodian, source, volume, item count, dates | | |
| Processing report | CSV/PDF | processed count, errors, deNIST, dedupe | | |
| Load summary | CSV | loaded count, load failures | | |
| Search term results | CSV | term, hit count, corpus size | | |
| Review stats | CSV | reviewer, docs reviewed, hours | | |
| Coding export | CSV | relevance, privilege, issue tags, date | | |
| Privilege log or summary | CSV/PDF | privilege type, counts | | |

**2) Normalization & Integrity Checks**

| Check | Method | Pass/Fail | Notes |
|---|---|---|---|
| Custodian name alignment | Create master mapping table | | |
| Pipeline totals | Collected ≥ Processed ≥ Loaded ≥ Reviewed | | |
| Missing search terms | Term list vs results export | | |
| Coding completeness | reviewer, date, relevance, privilege present | | |
| Error reconciliation | Processing errors vs re-runs | | |

**Custodian Mapping Table**

| Canonical Custodian | Variant Names/IDs | Source Systems | Notes |
|---|---|---|---|

**3) Core Metrics Tables**

**A. Collection & Processing by Custodian**

| Custodian | Collected GB | Items | Processed % | Load Failures | File Type Mix | Exceptions |
|---|---|---:|---:|---:|---|---|

**B. Search Term Effectiveness**

| Term/Query | Hits | Hit Rate % | Sample Precision % | Overlap % | Action |
|---|---:|---:|---:|---:|---|

**C. Review Status (Matter-Level)**

| Total Reviewable | Reviewed | % Reviewed | Relevant % | Privileged % | Non-Responsive % | Est. Completion Date |
|---:|---:|---:|---:|---:|---:|---|

**D. Reviewer Productivity**

| Reviewer/Team | Docs Reviewed | Hours | Docs/Hour | Relevant % | Privileged % | QC Rate % | Notes |
|---|---:|---:|---:|---:|---:|---:|---|

**E. Privilege Patterns**

| Custodian | Privileged % | Dominant Doc Types | Notes/Red Flags |
|---|---:|---|---|

**4) Definitions & Calculations**

| Metric | Formula |
|---|---|
| Hit Rate % | hits / total reviewable corpus |
| Precision % | relevant hits / sampled hits |
| Review Velocity | docs reviewed / time period |
| Completion ETA | remaining docs / current velocity |
| Privilege Rate % | privileged / reviewed |

**5) Executive Summary Template**

```text
Executive Summary
- Collection completeness: [status + anomalies]
- Processing health: [success % + key errors]
- Search term performance: [top/weak terms + overlap]
- Review progress: [reviewed %, relevance %, privilege %]
- Forecast: [ETA + assumptions]
- Risks & actions: [top 3]
```

**6) Findings, Risks, and Recommendations**

- List missing sources and resulting limitations.
- Flag custodians with outlier volumes or error rates.
- Identify low-precision or high-overlap search terms.
- Note reviewer inconsistencies and QC actions.
- Recommend resource changes or search term refinement.

**7) Assumptions & Gaps**

| Assumption or Gap | Impact | Mitigation |
|---|---|---|

**8) Work Product Legend**

Include the legend: “Attorney Work Product / Privileged & Confidential. Internal use only.”

## Guidelines

- Report only aggregate metrics; do not disclose privileged content.
- If counts conflict, surface the discrepancy and state the suspected cause.
- Use U.S. discovery terminology and confirm local rules if distributing externally.
- Mark any uncertain legal citations with `[VERIFY]`.
- Keep narrative neutral and data-driven; avoid strategy conclusions.
