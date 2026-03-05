---
name: managing-model-portfolio-governance
description: Structures investment committee processes with model approval, modification, and compliance documentation. Use when managing model portfolios, documenting investment decisions, or tracking portfolio changes.
tags:
  - management
  - asset-management
  - compliance
  - investment
metadata:
  author: casemark
  practice_areas:
    - Portfolio Management
    - Asset Management
    - Wealth Management
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Model Portfolio Governance

Structures investment committee processes with model approval, modification, and compliance documentation.

## When To Use

- Onboarding a new model portfolio for committee approval
- Proposing changes to existing model allocations (rebalance, drift correction, tactical tilt)
- Documenting investment committee decisions for compliance and audit trail
- Conducting periodic model portfolio reviews (quarterly, annual)
- Responding to regulatory or internal audit requests for model governance records
- Tracking exceptions, overrides, or client-level deviations from approved models

## Inputs To Gather

- **Model portfolio specification**: asset class targets, benchmark, allowable ranges, risk parameters
- **Proposed change details**: which holdings or weights change, rationale, effective date
- **Investment committee roster**: voting members, quorum requirements, recusal disclosures
- **Performance and risk data**: returns vs. benchmark, tracking error, drawdown, Sharpe ratio for the review period
- **Compliance constraints**: IPS limits, regulatory concentration rules [VERIFY jurisdiction-specific limits], ESG/exclusion screens
- **Prior meeting minutes**: last approval date, outstanding action items, prior exception log
- **Client deviation report**: accounts deviating from the model beyond stated tolerance bands

## Workflow

1. **Prepare the committee packet**
   - Compile current model holdings, weights, and benchmark comparison
   - Attach performance attribution (sector, security, currency contributions)
   - Summarize risk metrics: tracking error, VaR/CVaR, max drawdown since last review
   - Flag any holdings that breach concentration or liquidity thresholds [VERIFY firm-specific limits]
   - Include proposed changes with supporting investment thesis and expected impact on risk/return

2. **Document the approval process**
   - Record quorum confirmation and any member recusals or conflicts of interest
   - Log each agenda item: new model approval, modification request, or sunset recommendation
   - Capture the vote outcome (unanimous, majority, dissent with rationale)
   - Note any conditional approvals (e.g., "approved subject to CIO sign-off on EM allocation > 8%")

3. **Formalize the decision record**
   - Produce meeting minutes with date, attendees, motions, and votes
   - Attach the approved model specification with effective date and transition timeline
   - Record implementation instructions: trade execution window, cash raise sequence, tax-lot method
   - Assign responsibility for trade execution and post-trade reconciliation

4. **Update compliance and monitoring framework**
   - Revise pre-trade and post-trade compliance rules to reflect new targets and bands
   - Update drift-monitoring thresholds and rebalance triggers
   - Log any approved exceptions with expiration dates and escalation criteria
   - Ensure the updated model is reflected in portfolio management and order management systems

5. **Track ongoing deviations and exceptions**
   - Generate a deviation report: accounts outside tolerance bands, reason codes, remediation timeline
   - Distinguish between intentional client customizations (documented IPS overrides) and unintended drift
   - Escalate unresolved deviations beyond the firm's remediation window [VERIFY firm policy on remediation deadlines]

## Output

- **Investment committee minutes**: structured record with date, quorum, agenda items, votes, and action items
- **Approved model specification**: target weights, allowable ranges, benchmark, effective date
- **Change log**: chronological record of every model modification with rationale and approver
- **Deviation and exception report**: current accounts out of tolerance, exception justifications, expiration dates
- **Compliance checklist**: confirmation that pre-trade rules, monitoring thresholds, and system configurations are updated

## Quality Checks

- Every model change links back to a documented committee vote or delegated-authority approval
- Minutes capture dissenting views, not just outcomes
- Allowable ranges are internally consistent (individual sleeve limits sum to no more than 100%; cash range accommodates rebalance buffer)
- Deviation reports distinguish client-directed overrides from operational drift
- Effective dates and transition timelines are realistic given market liquidity and trading windows
- Regulatory concentration and diversification rules are met at both model and account level [VERIFY applicable regulation: Investment Company Act, UCITS, MiFID II, etc.]
- All [VERIFY] items are resolved or flagged for human review before finalizing governance records
