---
name: far-subcontract
description: Drafts FAR-compliant subcontract agreements between prime contractors and subcontractors under U.S. federal government prime contracts. Handles mandatory flow-down of FAR, DFARS, and agency-specific clauses, pricing structures by contract type, security/clearance requirements, IP/data rights, and termination provisions. Use when drafting government subcontracts, federal subcontracting agreements, FAR flow-down clauses, or prime-sub agreements.
tags:
  - agreement
  - drafting
  - regulatory
---

# FAR-Compliant Subcontract Agreement

Drafts a comprehensive subcontract agreement between a prime contractor and subcontractor under a U.S. federal government prime contract, ensuring full regulatory compliance and appropriate risk allocation.

## Prerequisites

1. **Prime contract documents** — contract number, issuing agency, contract type (FFP, CR, T&M), period of performance, total value, Section I clause list
2. **Party identification** — full legal names, principal places of business, DUNS/UEI numbers, CAGE codes, SAM registration status for both prime and sub
3. **Scope definition** — portions of prime contract SOW to be subcontracted, deliverables, milestones, labor categories
4. **Security requirements** — clearance levels (facility and personnel), CUI/CDI handling, NIST SP 800-171 assessment status
5. **Special requirements** — Buy American/TAA applicability, small business subcontracting goals, export control (ITAR/EAR) applicability, key personnel designations

## Output Structure

### Document Sections

| Section | Key Contents |
|---|---|
| **Preamble & Recitals** | Effective date, full legal entity names per SAM, prime contract number, agency, program description, sub's acknowledgment of prime contract review |
| **Statement of Work** | Task descriptions, performance standards, deliverable specs, acceptance criteria, milestone schedule, labor categories, GFP/GFI, work location |
| **Flow-Down Clauses** | Incorporation by reference with substitution rules (see Flow-Down Schedule below) |
| **Pricing & Payment** | CLIN structure, invoicing requirements, payment terms, withholding rights, retention, final payment/release |
| **Warranties & Representations** | Workmanship warranty, SAM registration, no debarment/suspension, OCI disclosure, compliance certifications |
| **Indemnification & Insurance** | Mutual indemnity (broad for sub, narrow for prime), insurance minimums, additional insured, waiver of subrogation |
| **IP & Data Rights** | Background IP licenses, foreground IP ownership, government data rights per applicable FAR/DFARS clauses, Bayh-Dole compliance |
| **Personnel & Security** | Key personnel, clearance requirements, NISPOM/DD-254 compliance, cybersecurity controls, CUI handling |
| **Lower-Tier Subcontracting** | Consent thresholds, flow-down obligations, sub remains responsible, assignment restrictions |
| **Changes & Equitable Adjustments** | Written change orders, REA procedures (30-day submission), constructive changes, duty to proceed |
| **Inspection & Acceptance** | QA system requirements, government inspection rights, rejection/correction procedures, acceptance only upon written notice |
| **Termination** | T4C and T4D provisions mirroring applicable FAR clauses, cure notice procedures, conversion of improper T4D to T4C |
| **Disputes** | Written claim → management escalation (30-60 days) → binding resolution; duty to proceed; sponsorship of prime contract claims |
| **General Provisions** | Integration, order of precedence, notices, severability, force majeure, independent contractor, confidentiality, record retention (3+ years), audit rights |
| **Execution** | Signature blocks, authority representations, effective date/conditions precedent, government consent contingency, counterparts/e-signatures |

### Flow-Down Clause Schedule

Organize by category. Include clause number, title, and date for each:

| Category | Key Clauses (adapt to contract type) |
|---|---|
| **Contract Administration** | FAR 52.243-1 (Changes—FFP) or 52.243-2 (Changes—CR) |
| **Termination** | FAR 52.249-2 (T4C—FFP) or 52.249-6 (T4C—CR); 52.249-8 (T4D—FFP) |
| **Disputes** | FAR 52.233-1 (Disputes) |
| **Socioeconomic** | FAR 52.219-8/52.219-9 (Small Business); 52.222-26 (EEO); 52.222-35 (Veterans); 52.222-36 (Disabilities); 52.222-50 (Trafficking) |
| **Data Rights** | FAR 52.227-14 (Data Rights) or DFARS 252.227-7013/7014 (Tech Data/Computer Software—defense) |
| **Cybersecurity** (defense) | DFARS 252.204-7012 (Safeguarding CDI); 252.204-7019/7020 (NIST 800-171 Assessment); 252.204-7021 (CMMC) |
| **Cost Accounting** (CR only) | FAR 52.230-2/3/6 (CAS); FAR 52.216-7 (Allowable Cost & Payment) |
| **Audit** | FAR 52.215-2 (Audit & Records) |

**Substitution rule**: Where clauses reference "the Government," "the Contracting Officer," or "the Contractor," substitute the prime contractor, *except* where context requires the U.S. Government to retain its direct rights (audit, inspection, data rights).

### Contract-Type-Specific Pricing

| Contract Type | Pricing Provisions |
|---|---|
| **Firm-Fixed-Price** | Total price by CLIN/milestone; price includes all costs; no cost breakdown required in invoices |
| **Cost-Reimbursement** | Allowable costs per FAR Part 31; fee structure (fixed/award/incentive); funded/unfunded ceiling; limitation of funds/cost clauses; adequate accounting system required |
| **Time-and-Materials** | Labor rates by category (fully burdened); materials at cost (or with handling rate); ceiling price; labor mix controls |

### Payment Terms Template

```
Invoice Requirements:
- Subcontract number and prime contract number
- CLIN/milestone identification
- Description of work performed in billing period
- Amount claimed per CLIN
- Cost backup (CR/T&M only)
- Authorized representative certification

Payment Timeline:
- Prime reviews/approves within [14] business days of proper invoice
- Payment within [30] days of approval
- Subject to receipt of corresponding government payment
- Prompt Payment Act flow-down if applicable

Withholding Rights:
- Defective/nonconforming deliverables
- Failure to pay lower-tier subs
- Disputed amounts
- Cure period required before withholding (except for disputed amounts)
```

### Termination for Convenience Recovery Formula

```
Recovery = (Price for accepted work)
         + (Allowable costs for work-in-progress per FAR Part 31)
         + (Reasonable settlement expenses)
         + (Reasonable profit on work performed)
         - (Prior payments)
         - (Setoffs)

Cap: Total subcontract price
Obligation: Sub must mitigate (stop work, cancel orders, settle lower-tier claims)
Submission deadline: [1 year] from effective termination date
```

### Insurance Minimums

| Coverage | Minimum Limits |
|---|---|
| Commercial General Liability | $1M per occurrence / $2M aggregate |
| Workers' Compensation | Statutory |
| Automobile Liability | $1M combined single limit |
| Professional Liability (if services) | $1M per claim |
| Cyber Liability (if CUI/CDI) | $2M per claim |

Requirements: Prime as additional insured (CGL, auto); waiver of subrogation; 30-day advance cancellation notice; certificates before work commences.

## Guidelines

- **Identify contract type first** — it drives pricing structure, termination clauses, cost accounting requirements, and flow-down clause selection
- **Always verify the prime contract's Section I** — do not assume which FAR/DFARS clauses apply; flow down only what is actually in the prime contract plus any mandatory by-operation-of-law clauses
- **Government consent** — check FAR 52.244-2; if prime contract requires consent for subcontracts above the threshold, make the agreement contingent on CO approval
- **Pay-when-paid vs. pay-if-paid** — structure payment contingency carefully; some jurisdictions void pay-if-paid clauses; use "pay within X days of receipt of proper invoice, subject to receipt of corresponding government payment" formulation
- **Order of precedence** — subcontract terms > incorporated FAR/DFARS clauses > attachments/exhibits > SOW (this is a common structure but confirm with client)
- **Do not reproduce full FAR clause text** — incorporate by reference with citation, title, and date; full text incorporation bloats the document and creates amendment-tracking problems
- **CAS applicability** — Cost Accounting Standards apply to CR subcontracts above $2M (CAS 52.230-2) unless exempt; verify threshold and exemptions [VERIFY current threshold]
- **Cybersecurity (defense)** — DFARS 252.204-7012 and CMMC requirements must flow down to any sub handling CDI/CUI; confirm sub's SPRS score or CMMC level
- **Export controls** — if ITAR/EAR applies, include specific clauses prohibiting disclosure to foreign persons without authorization; this is separate from and in addition to security classification requirements
- **Record retention** — minimum 3 years after final payment; longer if specified in prime contract or if claims are pending
- **Small business subcontracting plans** — if prime contract includes FAR 52.219-9 and sub is other-than-small, sub may need its own subcontracting plan
- **Mark uncertain citations with [VERIFY]** — especially for current dollar thresholds, CMMC implementation dates, and recently amended clauses
