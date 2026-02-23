---
name: contract-abstracts
description: Generates structured contract abstracts distilling key terms, obligations, rights, liabilities, and commercial provisions from lengthy agreements into a standardized reference document. Flags ambiguities, non-standard provisions, and missing terms. Ideal for corporate and transactional matters during negotiation, formation, due diligence, and closing. Use when abstracting commercial contracts, NDAs, licensing agreements, M&A ancillaries, or any multi-page agreement requiring rapid comprehension or portfolio management.
tags:
  - agreement
  - analysis
  - corporate
  - summarization
  - summary
  - transactional
---

# Contract Abstract

Produces a standardized, permanent-reference abstract of a contract's material terms, reducing review time while preserving legal precision.

## Prerequisites

1. **Full contract document** — including all exhibits, schedules, and amendments
2. **Contract type context** — (e.g., SaaS, asset purchase, services, license) to calibrate market-standard flagging
3. **Intended audience** — legal, executive, or transaction team (affects emphasis)

## Output Structure

### Header Block

| Field | Value |
|---|---|
| Agreement Title | |
| Execution Date | |
| Effective Date / Term | |
| Party A | Name, entity type, jurisdiction |
| Party B | Name, entity type, jurisdiction |
| Governing Law / Venue | |
| Contract Type | |

### Executive Summary
3–5 sentences covering the agreement's essential nature and most critical terms.

---

### Section-by-Section Abstract

For each material provision, provide:
- **§ Ref** — exact section number from the contract
- **Provision** — concise description using contract's own defined terms
- **Key Conditions / Deadlines / Thresholds** — dates, dollar amounts, notice periods

Cover these categories in order:

**1. Subject Matter & Scope**
- Services/goods/license being provided
- Exclusivity, territory, permitted use limitations

**2. Financial Terms**
- Pricing structure and payment schedule
- Expense reimbursement, taxes
- Price adjustment mechanisms (escalation, CPI, earn-outs)
- Penalties or liquidated damages

**3. Performance Obligations**
- Deliverables and milestones with dates
- SLAs, acceptance criteria, remediation rights

**4. Representations & Warranties**
- By each party (authority, compliance, IP ownership, non-infringement, etc.)
- Survival period

**5. Indemnification**
- Indemnifying party, indemnified party, covered claims
- Scope limitations, carve-outs, procedural conditions

**6. Liability**
- Cap amount and basis (e.g., 12-month fees)
- Excluded damages categories
- Exceptions to cap

**7. IP Ownership & Licensing**
- Ownership of background, foreground, and derivative IP
- License grants: scope, exclusivity, sublicensing rights
- Work-for-hire designations

**8. Confidentiality**
- Definition of confidential information
- Obligations, exceptions, duration post-termination

**9. Term & Termination**
- Initial term and auto-renewal mechanics
- Termination for cause: trigger events, cure periods, notice
- Termination for convenience: notice period, fees owed
- Effects of termination (wind-down, data return, survival)

**10. Assignment & Change of Control**
- Consent requirements
- Change of control triggers and remedies

**11. Dispute Resolution**
- Mechanism: negotiation → mediation → arbitration / litigation
- Arbitration rules, seat, number of arbitrators (if applicable)
- Governing law and exclusive jurisdiction

**12. Miscellaneous / Non-Standard Provisions**
- Most-favored-nation clauses
- Audit rights
- Insurance requirements
- Force majeure scope
- Any provisions deviating from market standard — flag with ⚠️

---

### Attachments & Exhibits

List all referenced schedules, exhibits, statements of work, and pricing annexes with a one-line description of each.

---

### Flags & Issues

| Type | § Ref | Description |
|---|---|---|
| ⚠️ Ambiguous | | |
| ⚠️ Non-standard | | |
| ⚠️ Missing term | | |
| ⚠️ Monitoring required | | |

## Guidelines

- Use the contract's exact defined terms — do not paraphrase in ways that alter legal meaning
- When a provision has multiple conditions, enumerate them as sub-elements preserving logical relationships
- Note where definitions governing a provision are located if not inline
- Flag provisions requiring ongoing compliance monitoring (notice deadlines, renewal windows, reporting obligations)
- Do not render legal opinions — flag issues for attorney review
- Proportionate length: simple agreements → 1–2 pages; complex multi-party agreements → up to 4 pages
- Jurisdiction: US default; note if foreign law governs any provision
