---
name: criminal-summary
description: Generates structured U.S. criminal case summaries from docket materials, filings, transcripts, and exhibits. Captures charge history, evidentiary posture, procedural timeline, trial or plea outcome, and sentencing into a single legal-reference document for onboarding, defense strategy, appeals prep, and status reporting. Use when asked to summarize a criminal matter, produce a case recap, compile a charge-to-sentencing timeline, or create a neutral case brief.
tags:
  - litigation
  - summarization
  - summary
---

# Criminal Case Summary

Create a neutral, source-grounded summary from case initiation through final disposition for quick, reliable review.

## Prerequisites

1. Case identifiers: jurisdiction, court, case number, filing date, parties, assigned counsel.
2. Charging documents: complaint, information, indictment, and docket index.
3. Full or partial transcript access: arraignment, pretrial hearings, trial, sentencing; if missing, cite the gap.
4. Motions/rulings package: suppression, discovery, continuance, evidentiary, plea, dismissal, restitution, guideline/allocution, and appeal-related orders.
5. Charge and disposition records: verdict forms, judgment, probation/sentence order, restitution order, sentencing transcript.

## Output Structure / Process

1. Assemble a standardized sectioned summary in this exact order.

| Section | Required fields |
|---|---|
| Case Header | Court, jurisdiction, case ID, charged persons, counsel, current procedural phase, matter status |
| Charges & Theory | Initial charges, statute/citation, offense grade, enhancements/reattrictions, any amendments, merged/combined counts, dismissals |
| Evidence Matrix | Evidence category, source, custodian, relevance to each charge, party offered by, admission/exclusion status |
| Motions & Rulings | Motion type, legal basis, filing date, ruling, appellate effect, unresolved follow-up |
| Timeline | Key procedural events by date and impact |
| Trial/Plea Track | Plea/offers, admissions, factual basis, hearing outcome, witness sequence, jury instructions, objections, verdict or withdrawal |
| Disposition | Conviction/acquittal/dismissal/other, special findings, enhancement decisions, custody status |
| Sentencing | Count-by-count sentence, structure (concurrent/consecutive), custody credits, fines, restitution, fees, supervision terms, ancillary orders |
| Post-Resolution | Motions pending, appeal posture, collateral consequences, compliance/case-management obligations |

2. Use charge-evidence crosswalk table to tie proof to outcomes:

| Charge ID | Statute | Count | Charge Status | Prosecution Evidence | Defense Evidence | Evidentiary Flags |
|---|---|---|---|---|---|---|
| C1 | | | Filed/Amended/Dismissed/Convicted/Acquitted | | | Hearsay, tainted, excluded, contested |

3. Maintain a timeline table for all procedural landmarks:

| Date | Event | Actor(s) | Ruling/Result | Case Impact |
|---|---|---|---|---|
| | | | | |

4. After tables, include a short narrative with:
- What moved the case forward
- Major evidentiary inflection points
- Major procedural departures (mistrials, continuances, substitutions)
- Disposition risks for immediate follow-up

5. Cite every factual statement with source shorthand.

```text
Source format:
- [Doc/Exhibit], [page/section], [line or transcript timestamp]
```

6. If any item is inferred from indirect record indicators, mark explicitly:
- `[VERIFY]` and identify the missing confirming source.

7. Finish with a QA block:

```text
Source completeness:
- Reviewed: [documents/transcripts]
- Missing: [critical missing items]
- Conflicts: [inconsistent dates/rulings]
- Confidence: High / Medium / Low
```

## Guidelines

- Do not invent facts, legal conclusions, motives, or guilt findings.
- Keep language neutral and record-based.
- Distinguish statutory law basis from factual finding; never merge them into one claim.
- Record status transitions explicitly: filed, denied, overruled, deferred, dismissed, amended, vacated, merged.
- Flag jurisdiction-specific issues (state-vs-federal rule differences, sentencing regime, collateral consequences).
- If jurisdiction or statute is unclear, label the section `Jurisdiction: verify` and do not finalize interpretation.
- For any ambiguous legal authority, add `[VERIFY]` rather than guessing.
