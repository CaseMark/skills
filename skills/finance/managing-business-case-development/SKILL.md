---
name: managing-business-case-development
language: en
description: Structures business case documentation with financial impact, risk assessment, and decision criteria. Use when building business cases, justifying investments, or documenting project proposals.
tags:
  - management
  - financial-planning-and-analysis
  - risk
  - investment
metadata:
  author: casemark
  practice_areas:
    - FP&A
    - Management Accounting
    - Business Intelligence
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Business Case Development

Structures business case documentation with financial impact, risk assessment, and decision criteria for investment proposals, capital projects, and strategic initiatives.

## When To Use

- Justifying a new capital expenditure, technology investment, or headcount request
- Documenting a make-vs-buy or build-vs-partner decision
- Preparing an initiative proposal for executive or board review
- Comparing competing project alternatives with quantified trade-offs
- Supporting annual planning with prioritized investment recommendations

## Inputs To Gather

- **Problem statement or opportunity description** — what triggers the investment need
- **Strategic alignment** — which corporate objectives, OKRs, or strategic pillars this supports
- **Cost estimates** — one-time (capex, implementation) and recurring (opex, maintenance, licenses)
- **Revenue or savings projections** — volume assumptions, pricing, efficiency gains, cost avoidance
- **Timeline** — implementation phases, key milestones, expected go-live
- **Baseline metrics** — current-state KPIs to measure improvement against
- **Risk factors** — market, execution, technology, regulatory, and dependency risks
- **Stakeholder input** — sponsor expectations, finance assumptions, operations constraints
- **Discount rate or WACC** — confirm the rate used for NPV calculations [VERIFY]
- **Tax treatment** — depreciation method, amortization schedule, tax credits if applicable [VERIFY]

## Workflow

1. **Frame the decision** — Define the problem or opportunity in one paragraph. State the decision being asked of the audience (approve, fund, prioritize). Identify the decision-maker and approval threshold [VERIFY].

2. **Define alternatives** — Present at minimum three options: (a) do nothing / status quo, (b) recommended option, (c) one or more viable alternatives. For each, summarize scope, approach, and high-level cost range.

3. **Build the financial model** — For each alternative, construct:
   - **Total Cost of Ownership (TCO)** over the evaluation horizon (typically 3–5 years)
   - **Net Present Value (NPV)** using the confirmed discount rate
   - **Internal Rate of Return (IRR)** where cash flows are estimable
   - **Payback period** — simple and discounted
   - **Sensitivity analysis** on the two or three variables with the highest uncertainty (e.g., adoption rate, unit cost, implementation timeline)

4. **Assess non-financial factors** — Score each alternative on:
   - Strategic fit and alignment
   - Implementation complexity and organizational readiness
   - Scalability and optionality for future phases
   - Stakeholder and change-management impact

5. **Quantify risks** — For each material risk, assign likelihood (high/medium/low), potential financial impact, and a mitigation action. Use a risk-adjusted NPV or expected-value adjustment where data supports it.

6. **Formulate the recommendation** — State the preferred alternative, the primary financial and strategic rationale, and the key assumptions that must hold. Present a concise decision matrix comparing all alternatives on cost, benefit, risk, and strategic alignment.

7. **Define implementation roadmap** — Outline phases, resource requirements, governance checkpoints, and the criteria for a go/no-go decision at each gate.

## Output

The business case document should contain:

- **Executive summary** (one page) — problem, recommendation, headline financials, and ask
- **Strategic context** — linkage to corporate strategy, market drivers
- **Options analysis** — side-by-side comparison table of alternatives
- **Financial analysis** — TCO, NPV, IRR, payback, and sensitivity tables
- **Risk assessment** — risk register with likelihood, impact, and mitigations
- **Implementation plan** — phased roadmap with milestones and resource needs
- **Decision matrix** — weighted scoring across financial and non-financial criteria
- **Appendices** — detailed assumptions log, supporting data, model inputs

## Quality Checks

- Every financial projection traces back to a stated assumption; no orphan numbers
- Sensitivity analysis covers at least the top three variables by impact magnitude
- The "do nothing" option is costed realistically — not set up as a straw man
- NPV, IRR, and payback calculations are internally consistent and use the same cash-flow timeline
- All assumptions are explicitly labeled; uncertain inputs are marked [VERIFY]
- The recommendation clearly states what happens if key assumptions prove wrong (downside scenario)
- Approval thresholds and governance requirements match the organization's delegation of authority [VERIFY]
- Document is structured for the audience — executive summary is self-contained for senior leadership; appendices carry the detail for finance reviewers
