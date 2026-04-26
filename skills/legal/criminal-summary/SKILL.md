---
name: criminal-summary
language: en
description: Generates structured U.S. criminal case summaries from docket materials, filings, transcripts, and exhibits. Covers charge history, evidentiary posture, procedural timeline, plea/trial outcome, and sentencing. Use when asked to summarize a criminal matter, produce a case recap, compile a charge-to-sentencing timeline, or create a neutral case brief.
---

# Criminal Case Summary

Produce a neutral, source-grounded summary from case initiation through final disposition. Every factual claim must cite a source document.

## Prerequisites

Gather before starting:

- **Identifiers**: jurisdiction, court, case number, filing date, parties, counsel
- **Charging documents**: complaint, information, indictment, docket index
- **Transcripts**: arraignment, pretrial hearings, trial, sentencing (cite gaps if missing)
- **Motions/rulings**: suppression, discovery, continuance, evidentiary, plea, dismissal, restitution, guidelines, appeal-related orders
- **Disposition records**: verdict forms, judgment, sentence order, restitution order, sentencing transcript

## Quick Start

1. Collect all available documents and note what is missing.
2. Build the summary sections in order (see below).
3. Populate the charge-evidence crosswalk and timeline tables.
4. Write a short narrative connecting key inflection points.
5. Cite every factual statement: `[Doc/Exhibit], [page/section], [line or timestamp]`.
6. Run the QA checklist.

## Summary Sections

Assemble in this order:

| Section | Required Fields |
|---|---|
| Case Header | Court, jurisdiction, case ID, charged persons, counsel, procedural phase, status |
| Charges & Theory | Initial charges, statute, offense grade, enhancements, amendments, merged counts, dismissals |
| Evidence Matrix | Category, source, custodian, relevance per charge, offering party, admission/exclusion status |
| Motions & Rulings | Type, legal basis, filing date, ruling, appellate effect, unresolved follow-up |
| Timeline | Key procedural events by date and impact |
| Trial/Plea Track | Plea offers, admissions, factual basis, hearing outcome, witness sequence, jury instructions, objections, verdict |
| Disposition | Conviction/acquittal/dismissal, special findings, enhancements, custody status |
| Sentencing | Count-by-count sentence, concurrent/consecutive, custody credits, fines, restitution, supervision, ancillary orders |
| Post-Resolution | Pending motions, appeal posture, collateral consequences, compliance obligations |

## Charge-Evidence Crosswalk

| Charge ID | Statute | Count | Status | Prosecution Evidence | Defense Evidence | Flags |
|---|---|---|---|---|---|---|
| C1 | | | Filed / Amended / Dismissed / Convicted / Acquitted | | | Hearsay, tainted, excluded, contested |

## Timeline Table

| Date | Event | Actor(s) | Ruling/Result | Case Impact |
|---|---|---|---|---|

## Narrative Block

After tables, write a brief narrative covering:

- What moved the case forward
- Major evidentiary inflection points
- Procedural departures (mistrials, continuances, substitutions)
- Disposition risks requiring follow-up

## QA Checklist

End every summary with:

```
Source completeness:
- Reviewed: [documents/transcripts]
- Missing: [critical missing items]
- Conflicts: [inconsistent dates/rulings]
- Confidence: High / Medium / Low
```

## Pitfalls

- **No invented facts.** Never fabricate conclusions, motives, or guilt findings.
- **Neutral language only.** Stay record-based; separate statutory basis from factual findings.
- **Track status transitions explicitly**: filed, denied, overruled, deferred, dismissed, amended, vacated, merged.
- **Flag jurisdiction ambiguity.** Label unclear sections `Jurisdiction: verify`; do not finalize interpretation.
- **Mark inferences.** Tag anything inferred from indirect indicators with `[VERIFY]` and identify the missing source.
- **State-vs-federal awareness.** Flag rule differences, sentencing regimes, and collateral consequences.
