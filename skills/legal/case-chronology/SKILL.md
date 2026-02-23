---
name: case-chronology
description: Produces U.S. litigation case chronologies that synthesize documents and events into a dated timeline with executive summary, source attribution, gaps, inconsistencies, and investigation recommendations. Use for case intake, onboarding, deposition prep, trial prep, or when asked for a chronology, timeline, case summary, or executive summary of a matter.
tags:
  - analysis
  - litigation
  - summarization
  - summary
---

# Case Chronology

Deliver a timeline-centered case summary that lets counsel grasp key facts, documents, and strategic inflection points fast.

## Prerequisites

1. Complete document set or defined subset (with source IDs or filenames).
2. Party list with roles (plaintiff/defendant/non-party; individual/entity).
3. Date range of interest and any known anchor events.
4. Known claims/defenses or legal issues (if available).

## Output Structure / Process

1. **Executive Summary**
   - Matter type, core dispute, key parties.
   - Timeline span (earliest date to latest date).
   - 3–6 pivotal events that drive liability, damages, or defenses.

2. **Chronology Table** (strict date order)
   - Use one row per event or document.
   - If date is approximate, label as `circa`, `approx`, or date range.

| Date | Event/Doc Type | Parties | Source | What Happened | Significance |
|---|---|---|---|---|---|
| YYYY-MM-DD | Email / Contract / Call / Filing / Payment / Incident | A ↔ B | Doc ID / Filename | 1–3 sentence factual summary | Liability/Damages/Defense impact |

3. **Cross-References**
   - Explicitly link related entries by date or source IDs.
   - Example: “See 2024-03-02 (Doc 18) re: notice; follow-up 2024-03-12 (Doc 22).”

4. **Issues & Gaps**
   - Missing documents expected for this matter.
   - Date inconsistencies or conflicting accounts.
   - Unexplained timeline gaps.

5. **Strategic Analysis**
   - Patterns, turning points, or admissions.
   - Evidence that strengthens or weakens key claims/defenses.

6. **Recommendations**
   - Additional documents to request.
   - Witnesses to interview or depose.
   - Targeted discovery topics.

## Guidelines

- Use factual, neutral tone; separate facts from inferences.
- Include source attribution for every entry.
- Flag uncertainty with `approx` or `unknown date` instead of guessing.
- Call out missing routine records (notices, invoices, logs, filings).
- Avoid legal conclusions unless directly supported by the record.
- If citing statutes or procedural rules, verify and mark `[VERIFY]` if unsure.
- Keep all dates in ISO format `YYYY-MM-DD` for sorting.
