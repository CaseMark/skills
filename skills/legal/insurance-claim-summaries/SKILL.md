---
name: insurance-claim-summaries
language: en
description: >-
  Generates structured summaries of U.S. insurance claim files covering
  identification, incident narrative, party positions, coverage analysis,
  and resolution status. Use when synthesizing claim files for adjusters,
  legal counsel, or claims managers during pre-filing review, discovery,
  or settlement preparation. Trigger keywords: claim summary, insurance
  claim, coverage summary, adjuster summary, coverage denial, reservation
  of rights.
---

# Insurance Claim Summary

Synthesizes a claim file into a structured quick-reference summary covering incident facts, party positions, coverage analysis, and resolution status.

## Prerequisites

Gather before starting:

- **Claim file** — submission, policy declarations, endorsements, correspondence
- **Coverage position** — denial letters, reservation-of-rights letters, position statements
- **Investigation** — inspection reports, statements, medical records, damage assessments
- **Resolution** (if applicable) — settlement agreements, releases, payment records

## Output Structure

### 1. Claim Identification Header

| Field | Value |
|---|---|
| Claim Number | |
| Policy Number | |
| Named Insured | |
| Claimant (if different) | |
| Date of Loss | |
| Date Claim Filed | |
| Coverage Type | |
| Current Status | Open / Closed / In Litigation / ADR Pending |

### 2. Incident Narrative

- What occurred, when, where
- Circumstances triggering coverage
- Chronological key events with dates

### 3. Claimant's Position

- Alleged damages/injuries/losses — itemized by category
- Policy provisions or coverage grants cited
- Total amount — label as: **claimed** / **paid** / **in dispute**
- Key supporting evidence submitted

### 4. Insurer's Response

- Coverage determination: full acceptance / partial / denial
- If denied or limited:
  - Exclusions, conditions, or limitations relied upon (quote verbatim)
  - Defenses raised: late notice, misrepresentation, failure to cooperate, fraud
- Investigation scope and key findings
- Insurer's independent valuation (if different from claimed)
- Reservation-of-rights status and scope

### 5. Resolution / Current Status

**If resolved:**
- Outcome: paid in full / negotiated settlement / denial upheld / withdrawn
- Amount paid and date
- Release scope: full / partial / rights preserved

**If open or disputed:**
- Posture: pre-suit / litigation filed / ADR pending
- Court/forum and docket number (if in litigation)
- Unresolved issues
- Next steps and key deadlines

### 6. Special Issues *(only if applicable)*

- Bad faith allegations or regulatory concerns
- Subrogation rights and recovery potential
- Coordination of benefits / other insurance
- Third-party liability
- Statute of limitations or suit-limitation deadlines [VERIFY state-specific periods]

## Guardrails

- **Objectivity** — Do not characterize either position as stronger unless summarizing an adjudicator's findings
- **Disputed facts** — Attribute each version to its source; never state contested facts as established
- **Policy language** — Quote verbatim when interpretation is at issue; flag ambiguities
- **Monetary precision** — Label all figures as claimed, paid, or in dispute — never conflate
- **Source citations** — Reference documents by name and date for cross-referencing
- **Jurisdiction** — US-focused; note state-specific bad faith standards where raised [VERIFY]
