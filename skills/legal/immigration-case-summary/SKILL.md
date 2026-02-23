---
name: immigration-case-summary
description: >-
  Produces structured, concise U.S. immigration case summaries capturing
  applicant background, benefit sought, INA/regulatory basis, procedural
  history, posture, and outcomes. Use when preparing immigration case
  summaries, intake briefs, handoffs, supervision reviews, or client
  consultations. Trigger keywords: immigration case summary, asylum,
  adjustment of status, I-589, I-485, I-130, I-140, NTA, RFE, NOID, EOIR, BIA,
  USCIS.
tags:
  - regulatory
  - summarization
  - summary
---

# Immigration Case Summary

Summarizes an immigration matter into a scan-ready legal brief of facts, law, posture, and outcome.

## Prerequisites

1. **Complete case file** — filings, notices, decisions, transcripts, correspondence.
2. **Benefit/relief type** — e.g., asylum, AOS, family-based, removal defense, appeal.
3. **Forum(s)** — USCIS, EOIR (IJ), BIA, federal circuit, or mixed.
4. **Key dates** — filing, RFE/NOID, interview/hearing, decisions, appeal deadlines.
5. **Confidentiality scope** — redactions or sensitivity flags for trauma, medical, minors.

## Output Structure / Process

**Process Checklist**

1. Identify benefit/relief and governing authority from the record.
2. Extract applicant background and eligibility elements with cited evidence.
3. Build a chronological procedural timeline with agency/court actions.
4. State current posture and deadlines; note risks and open items.
5. Flag missing records or conflicts.

**Summary Template**

```markdown
## Matter Snapshot
| Field | Value |
|---|---|
| Client/Applicant | |
| Country of Origin | |
| A-Number / USCIS Receipt(s) | |
| Benefit/Relief Sought | |
| Forum(s) | |
| Counsel of Record | |
| Current Posture | |
| Last Updated | |

## Applicant Background
- Immigration history (entries, status changes, overstays):
- Family relationships (petitioner/beneficiary, derivatives):
- Employment/education:
- Relevant vulnerabilities or equities:
- Adverse factors (criminal, fraud, removability grounds):

## Legal Basis
- Statute/Regulation/Policy: list exact INA/CFR/PM citations from record.
- Eligibility elements: map each element to evidence.
- Discretionary factors (if applicable):

## Evidence Inventory
| Element / Issue | Key Evidence | Gaps |
|---|---|---|

## Procedural History (Chronological)
| Date | Event | Forum | Outcome / Notes |
|---|---|---|---|

## Decisions & Outcomes
- Decision(s): approvals/denials/termination/remand with dates.
- Grounds for decision (quote/summary from decision).
- Appeal/motion status and deadlines.

## Key Issues / Risks
- Inconsistencies or adverse evidence:
- Statutory bars or procedural defects:
- Credibility concerns or corroboration gaps:

## Next Steps
- Required filings and deadlines:
- Evidence to obtain:
- Strategy notes:
```

## Guidelines

- Use exact document titles, receipt numbers, and dates for cross-reference.
- Do not invent citations; mark uncertain legal citations as `[VERIFY]`.
- Distinguish forum-specific standards (USCIS vs EOIR vs BIA vs circuit).
- Capture RFE/NOID/NTA details verbatim when critical to posture.
- Maintain confidentiality; omit sensitive details unless required for analysis.
- If records conflict, note the conflict and cite both sources.
