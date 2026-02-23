---
name: criminal-case-summary
description: >-
  Produces structured U.S. criminal case summaries covering charges, statutes,
  evidence, procedural history, trial or plea, verdict, and sentencing. Use
  when summarizing criminal defense or prosecution files, preparing case
  overviews, drafting status memos, or compiling procedural histories. Trigger
  keywords: criminal case summary, charges, statute, evidence summary,
  procedural history, trial summary, plea summary, verdict, sentencing.
tags:
  - litigation
  - summarization
  - summary
---

# Criminal Case Summary

Generate a neutral, verifiable summary of a criminal case from initiation through disposition.

## Prerequisites

1. **Charging documents** — complaint, information, indictment, superseding filings
2. **Docket or case timeline** — key dates, hearings, rulings
3. **Motions and orders** — suppression, discovery, continuances, evidentiary rulings
4. **Transcripts** — hearings, trial, plea, sentencing
5. **Evidence inventory** — exhibits, reports, forensic results, witness lists
6. **Disposition records** — verdict forms, plea agreement, judgment, sentencing order

## Output Structure / Process

Use the following structure and fill every section. If a section is not applicable, state “Not applicable” and explain why.

### 1) Case Header

| Field | Value |
|---|---|
| Court / Jurisdiction | |
| Case No. | |
| Parties | |
| Judge | |
| Prosecutor | |
| Defense Counsel | |
| Defendant Status | in custody / out / pretrial supervision |

### 2) Charges

List all charges, including amended or dismissed counts.

| Count | Statute | Charge Name | Level | Enhancements / Special Allegations | Disposition |
|---|---|---|---|---|---|
| | | | felony / misdemeanor | | pending / dismissed / convicted / acquitted |

Notes:
- Include statute citations. If not fully verified, mark with `[VERIFY]`.
- Note charging changes with dates and authority (e.g., superseding indictment).

### 3) Core Facts (Neutral)

Provide a concise, non-argumentative fact narrative.

Checklist:
- Key incident date(s)
- Alleged conduct tied to each count
- Victim and witness identifiers (use initials if privacy-sensitive)
- Arrest or charging basis
- Any relevant context needed to understand the charges

### 4) Evidence Summary

Summarize both prosecution and defense evidence.

| Evidence Item | Source | Relevance to Count(s) | Admitted / Excluded | Ruling / Notes |
|---|---|---|---|---|
| | | | | |

Checklist:
- Physical evidence
- Documentary evidence
- Digital evidence
- Witness testimony
- Expert testimony
- Forensic analysis
- Demonstrative exhibits
- Suppression issues and rulings

### 5) Procedural History

Chronological timeline of material events.

| Date | Event | Outcome / Ruling | Citation |
|---|---|---|---|
| | | | |

Include:
- Arraignment
- Pretrial motions and dispositions
- Discovery disputes
- Continuances or mistrials
- Trial dates or plea hearings

### 6) Trial Summary (If Tried)

| Phase | Key Points |
|---|---|
| Jury selection | |
| Openings | |
| Prosecution case | |
| Defense case | |
| Rebuttal | |
| Closing arguments | |
| Jury instructions | |
| Deliberations | |

Include significant objections and rulings only if outcome-relevant.

### 7) Plea Summary (If Plea)

| Item | Details |
|---|---|
| Plea type | |
| Counts pled | |
| Dismissed counts | |
| Factual basis | |
| Sentencing terms | |
| Waivers | |

### 8) Verdict / Findings

| Count | Verdict | Special Findings | Notes |
|---|---|---|---|
| | | | |

### 9) Sentencing

| Count | Sentence | Concurrent / Consecutive | Credits | Fines / Restitution | Supervision Conditions |
|---|---|---|---|---|---|
| | | | | | |

Include:
- Total custodial term
- Probation or supervised release
- Conditions (mandatory and special)

### 10) Post-Trial / Post-Conviction

Checklist:
- Motions for new trial
- Appeals filed and status
- Post-conviction relief petitions
- Sentence modifications

### 11) Open Issues / Unknowns

List missing documents or unresolved factual or procedural gaps.

## Guidelines

- Maintain strict neutrality; no advocacy or opinion.
- Tie evidence and facts to specific counts where possible.
- Use citations to docket entries, transcripts, or exhibits when available.
- Flag uncertain statutory citations or procedural points with `[VERIFY]`.
- Respect jurisdictional variations in terminology (e.g., information vs indictment).
- Do not infer facts not supported by the record.
