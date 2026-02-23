---
name: contract-summarization
description: Generates structured summaries of U.S. contracts capturing parties, business terms, legal provisions, termination, and dispute resolution. Flags one-sided, ambiguous, or missing standard provisions. Use when summarizing agreements for due diligence, transaction management, contract review, or compliance monitoring — including multi-document sets with exhibits, schedules, and amendments.
tags:
  - agreement
  - summarization
  - summary
  - transactional
---

# Contract Summarization

Produces a structured contract summary covering all material terms, obligations, rights, and risks — enabling informed decisions without a full read.

## Prerequisites

1. **Contract document(s)** — main agreement plus any exhibits, schedules, amendments, or SOWs
2. **Counterparty context** (optional) — role of reviewing party (buyer/seller, licensor/licensee, etc.) to calibrate risk flags
3. **Purpose** (optional) — due diligence, compliance monitoring, negotiation, closing review

## Output Structure

Organize the summary with the following sections, citing section numbers for each extracted term:

### 1. Contract Overview
| Field | Detail |
|---|---|
| Parties | Full legal names + roles |
| Effective Date | |
| Term / Expiration | Duration + auto-renewal trigger |
| Subject Matter | One-line description of agreement purpose |
| Governing Law / Venue | |

### 2. Core Business Terms
- **Scope of Work / Deliverables** — what each party must do or provide
- **Pricing & Payment** — amounts, timing, invoicing, late fees (quote figures exactly)
- **Performance Obligations** — milestones, SLAs, acceptance criteria

### 3. Legal Provisions
- **Representations & Warranties** — by each party; survival period
- **Indemnification** — scope, carve-outs, procedures (notice, control of defense)
- **Limitation of Liability** — caps (quote amounts/multiples), excluded damages, exclusions to cap
- **IP Ownership & Licensing** — work-for-hire, license grants, residuals
- **Confidentiality / NDA** — scope, duration, exceptions, return/destroy obligations
- **Non-Compete / Non-Solicit** — duration, geographic scope, covered activities (if present)

### 4. Termination & Renewal
- Termination for cause — triggering events, cure period, notice
- Termination for convenience — availability, notice period, payment on exit
- Effects of termination — wind-down, surviving obligations, return of materials
- Auto-renewal terms and opt-out deadlines

### 5. Dispute Resolution
- Governing law and jurisdiction
- Mandatory arbitration or mediation (rules, seat, language)
- Jury trial waiver
- Fee-shifting provisions

### 6. Special Provisions & Risk Flags
- Unusual or one-sided terms
- Missing standard provisions for this contract type
- Internal inconsistencies or conflicts between main agreement and exhibits
- Ambiguous language requiring clarification

## Guidelines

- **Quote precisely**: monetary amounts, dates, notice periods, and defined terms as written
- **Cite sections**: every extracted term should reference the contract section or page
- **Objective tone**: summarize as written; flag concerns without inserting legal opinion unless requested
- **Multi-document sets**: capture terms from all related documents; note which document governs on conflicts
- **Jurisdiction**: skill optimized for U.S. agreements; flag if non-U.S. law governs
- **Length**: 2–5 pages depending on complexity; prioritize completeness over brevity for complex deals
