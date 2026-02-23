---
name: safe-agreement
description: Drafts Simple Agreements for Future Equity (SAFE) for early-stage venture capital financing. Generates conversion-ready instruments with valuation cap and discount mechanics, investor qualification provisions, and securities law compliance language. Use when drafting SAFEs, pre-seed investment documents, convertible equity instruments, or YC-style SAFE notes.
tags:
  - agreement
  - corporate
  - drafting
---

# Simple Agreement for Future Equity (SAFE)

Drafts a SAFE instrument granting investors future equity rights upon triggering events without immediate ownership or debt obligations.

## Prerequisites

1. **Company information** — exact legal name per certificate of incorporation, jurisdiction, state of formation
2. **Investor information** — full legal name, entity type, accredited investor basis
3. **Economic terms** — purchase amount, valuation cap, discount rate (if any)
4. **Cap table** — existing SAFEs, convertible notes, fully-diluted share count
5. **Special provisions** — MFN clause, pro rata rights, side letters, or modifications

## Document Structure

### Header & Recitals

| Element | Requirement |
|---|---|
| Company ID | Full legal name matching certificate of incorporation, entity type, jurisdiction |
| Investor ID | Legal name, entity type, capacity to contract |
| Purchase amount | Exact dollar figure |
| Core exchange | Capital now → contractual right to future equity; explicitly state: no debt, no interest accrual, no current stockholder status |

### Conversion Mechanics

Draft three triggering events with the following mechanics:

**1. Equity Financing (automatic conversion)**

- Converts into same series of preferred stock issued to new investors
- Conversion price = lesser of:
  - **Cap price**: Valuation Cap ÷ Pre-money fully-diluted capitalization
  - **Discount price**: New investor price per share × (1 − Discount Rate)
- Shares issued = Purchase Amount ÷ Conversion Price (using lower price)
- Include a worked numerical example demonstrating both calculations

**2. Liquidity Event (acquisition, merger, IPO)**

- Investor elects one of:
  - Cash payment = Purchase Amount, OR
  - Common stock shares = Purchase Amount ÷ Liquidity Price (derived from valuation cap)
- Specify election timeline and default if no election made

**3. Dissolution Event**

- Cash payment = Purchase Amount, paid pre-dissolution
- Priority waterfall: senior to common stockholders, subordinate to creditors and debt holders

### Valuation Terms Table

| Term | Function |
|---|---|
| Valuation Cap | Ceiling on effective conversion valuation; investor gets larger stake if company valuation exceeds cap |
| Discount Rate | Percentage reduction from new investor price; rewards early-stage risk |
| Interaction rule | Cap and discount are **alternative** (not additive); investor gets the more favorable result |

### Investor Representations

Include all of the following:

- [ ] Investment purpose (not for resale/distribution — supports private placement exemption)
- [ ] Accredited investor status — provide pathways for:
  - Individual: income test OR net worth test (exclude primary residence)
  - Entity: total assets, equity owner accreditation, or institutional qualification
- [ ] Risk acknowledgments: speculative nature, total loss risk, no liquid market, indefinite hold period
- [ ] Sophistication: sufficient knowledge/experience or engagement of qualified advisors

### Company Representations

- [ ] Valid incorporation and good standing
- [ ] Corporate power and authority to execute
- [ ] Board/stockholder approvals obtained
- [ ] Binding obligation (subject to standard bankruptcy/equitable exceptions)
- [ ] No conflict with charter documents, material contracts, or applicable law

### Rights & Restrictions

**Pre-conversion — no stockholder rights:**
- No voting, dividends, distributions, information rights, preemptive rights, or meeting participation
- Rights are purely contractual per SAFE terms only

**Transfer restrictions:**
- No transfer without company's prior written consent
- Unauthorized transfers are void
- Optional exceptions: affiliates, family/estate planning, retirement accounts (specify conditions and notice requirements)

**Securities compliance:**
- SAFE and conversion shares are unregistered
- Restrictive legends required on all certificates/book entries
- Investor acknowledges inability to liquidate

### Administrative Provisions

| Provision | Standard |
|---|---|
| Governing law | State of incorporation or principal place of business |
| Dispute resolution | Specify litigation venue OR arbitration (rules, arbitrator count, seat, cost allocation) |
| Amendments | Written instrument signed by both parties only |
| Waivers | Explicit, in writing; no implied waiver of subsequent breaches |
| Integration | Entire agreement; supersedes all prior negotiations |
| Notices | Email, certified mail, or national courier; specify addresses; state when deemed received per method |
| Severability | Invalid provisions reformed to minimum extent; remainder survives |

### Signature Blocks

- Space for manual/electronic signature, printed name, title (for entities), date
- Both Company and Investor blocks

## Guidelines

1. **Defined terms** — capitalize consistently; define before first use or in a definitions section
2. **Mathematical precision** — conversion formulas must be unambiguous to any competent financial professional
3. **Cross-references** — verify all internal section references are accurate
4. **No bracketed placeholders** — replace all `[brackets]` with actual terms before finalizing
5. **YC SAFE compatibility** — if the company references YC standard SAFEs, align with the applicable YC template version (post-money vs. pre-money) and flag any deviations
6. **State-specific securities exemptions** — confirm the applicable federal exemption (typically Reg D, Rule 506(b) or 506(c)) and any state blue sky requirements
7. **Existing instrument conflicts** — check for MFN clauses in prior SAFEs that could be triggered
8. **Missing information** — if critical terms are unavailable, identify gaps explicitly and request from user before finalizing
