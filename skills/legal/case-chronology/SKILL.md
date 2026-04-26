---
name: case-chronology
language: en
description: Produces U.S. litigation case chronologies with dated timelines, executive summaries, source attribution, gap analysis, and investigation recommendations. Use when asked for a chronology, timeline, case summary, or executive summary of a legal matter, or during case intake, deposition prep, or trial prep.
---

# Case Chronology

Timeline-centered case summary that lets counsel grasp key facts, documents, and strategic inflection points fast.

## Prerequisites

1. Document set or defined subset (with source IDs or filenames).
2. Party list with roles (plaintiff/defendant/non-party).
3. Date range and any known anchor events.
4. Known claims/defenses or legal issues (if available).

## Quick Start

```
- [ ] Gather documents, party list, and date range
- [ ] Draft executive summary
- [ ] Build chronology table in strict date order
- [ ] Add cross-references between related entries
- [ ] Identify gaps and inconsistencies
- [ ] Write strategic analysis
- [ ] List recommendations for further investigation
```

## Output Structure

### 1. Executive Summary

- Matter type, core dispute, key parties.
- Timeline span (earliest to latest date).
- 3-6 pivotal events driving liability, damages, or defenses.

### 2. Chronology Table

One row per event or document, strict date order. Label approximate dates as `circa`, `approx`, or date range.

| Date | Event/Doc Type | Parties | Source | What Happened | Significance |
|---|---|---|---|---|---|
| YYYY-MM-DD | Email / Contract / Filing / Payment / Incident | A > B | Doc ID / Filename | 1-3 sentence factual summary | Liability/Damages/Defense impact |

### 3. Cross-References

Link related entries by date or source ID.

Example: "See 2024-03-02 (Doc 18) re: notice; follow-up 2024-03-12 (Doc 22)."

### 4. Issues and Gaps

- Missing documents expected for this matter type.
- Date inconsistencies or conflicting accounts.
- Unexplained timeline gaps.

### 5. Strategic Analysis

- Patterns, turning points, or admissions.
- Evidence strengthening or weakening key claims/defenses.

### 6. Recommendations

- Additional documents to request.
- Witnesses to interview or depose.
- Targeted discovery topics.

## Rules

- Factual, neutral tone. Separate facts from inferences.
- Source attribution on every entry.
- Flag uncertainty with `approx` or `unknown date` — never guess dates.
- All dates in ISO format `YYYY-MM-DD` for sorting.
- Call out missing routine records (notices, invoices, logs, filings).
- No legal conclusions unless directly supported by the record.
- If citing statutes or procedural rules, mark `[VERIFY]` when unsure.
