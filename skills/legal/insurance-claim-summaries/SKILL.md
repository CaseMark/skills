---
name: insurance-claim-summaries
description: >-
  Generates structured summaries of U.S. insurance claims covering claim
  identification, incident narrative, claimant's position with alleged damages
  and policy citations, insurer's response including coverage decisions and
  exclusions relied upon, and resolution or current status. Use when
  synthesizing claim files for adjusters, legal counsel, policyholders, or
  claims managers during pre-filing review, discovery, or settlement
  preparation. Trigger keywords: claim summary, insurance claim, coverage
  summary, claim file review, adjuster summary, coverage denial, reservation
  of rights.
tags:
  - litigation
  - summarization
  - summary
---

# Insurance Claim Summary

Synthesizes a complete insurance claim file into a structured quick-reference summary covering incident facts, party positions, coverage analysis, and resolution status.

## Prerequisites

1. **Claim file** — initial submission, policy declarations, endorsements, correspondence
2. **Coverage position materials** — denial letters, reservation-of-rights letters, coverage position statements
3. **Investigation materials** — inspection reports, recorded statements, medical records, damage assessments
4. **Resolution documents** — settlement agreements, release language, payment records (if resolved)

## Output Structure

### 1. Claim Identification Header

| Field | Value |
|---|---|
| Claim Number | |
| Policy Number | |
| Named Insured | |
| Claimant (if different from insured) | |
| Date of Loss | |
| Date Claim Filed | |
| Coverage Type | |
| Current Status | Open / Closed / In Litigation / ADR Pending |

### 2. Incident Narrative
- What occurred, when, and where
- Circumstances triggering the claimed coverage
- Chronological sequence of key events with dates

### 3. Claimant's Position
- Alleged damages/injuries/losses with itemized breakdown by category
- Specific policy provisions or coverage grants cited by claimant
- Total amount claimed — label clearly as: claimed / paid / in dispute
- Key supporting evidence and documentation submitted

### 4. Insurer's Response
- Coverage determination: full acceptance / partial acceptance / denial
- If denied or limited:
  - Policy exclusions, conditions, or limitations relied upon (quote verbatim)
  - Coverage defenses raised: late notice, material misrepresentation, failure to cooperate, fraud
- Investigation scope, investigators, and key findings
- Insurer's independent valuation (if different from claimed amount)
- Reservation-of-rights status and scope

### 5. Resolution / Current Status

**If resolved:**
- Outcome: paid in full / negotiated settlement / denial upheld / claim withdrawn
- Amount paid and payment date
- Release scope: full release / partial release / rights preserved for future action

**If open or disputed:**
- Procedural posture: pre-suit / litigation filed / ADR pending
- Court/forum and docket number if in litigation
- Outstanding unresolved issues
- Next anticipated steps and key deadlines

### 6. Special Issues *(include only if applicable)*
- Bad faith allegations or regulatory compliance concerns
- Subrogation rights and recovery potential
- Coordination of benefits / other insurance provisions
- Third-party liability involvement
- Statute of limitations or contractual suit-limitation deadlines [VERIFY state-specific periods]

## Guidelines

- **Objectivity**: Do not characterize either party's position as stronger unless summarizing an adjudicator's findings
- **Disputed facts**: Attribute each version to its source; never state contested facts as established truth
- **Policy language**: Quote relevant provisions verbatim when interpretation is at issue; flag ambiguities explicitly
- **Monetary precision**: Label all figures as claimed, paid, or in dispute — never conflate categories
- **Source citations**: Reference documents by name and date to enable cross-referencing to the claim file
- **Accessibility**: Use plain language alongside legal terminology for non-legal readers
- **Jurisdiction**: US-focused; note applicable state-specific bad faith standards where raised [VERIFY]
