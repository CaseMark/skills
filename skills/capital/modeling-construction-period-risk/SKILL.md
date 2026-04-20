---
name: modeling-construction-period-risk
language: en
description: Analyzes construction risk with EPC contract review, delay and cost overrun scenarios, and completion guarantee structures. Use when modeling construction risk, evaluating EPC terms, or stress testing project timelines.
tags:
  - modeling
  - infrastructure-and-project-finance
  - risk
metadata:
  author: casemark
  practice_areas:
    - Project Finance
    - Infrastructure Investment
    - PPP
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Construction Period Risk

## When To Use

- Modeling construction-phase cash flows and risk exposure for infrastructure or energy projects
- Evaluating EPC/turnkey contract terms for bankability and risk allocation
- Stress-testing project timelines against delay and cost overrun scenarios
- Assessing completion guarantee structures (parent guarantees, surety bonds, LC-backed facilities)
- Underwriting construction-period debt sizing and draw schedules
- Reviewing PPP/concession projects where construction risk drives financial close conditions

## Inputs To Gather

- **EPC contract** — fixed-price vs. cost-plus structure, GMP caps, scope of work, change order provisions, LD schedule (delay LDs and performance LDs), force majeure definition, termination triggers
- **Construction budget** — total EPC price, owner's costs, development fees, contingency allocation (typically 5-15% for greenfield), IDC assumptions
- **Construction schedule** — milestone timeline, critical path items, long-lead equipment delivery dates, commissioning/testing period, target COD
- **Funding plan** — equity/debt split, draw schedule, construction facility terms (commitment fees, margin during construction), equity contribution agreement timing
- **Contractor profile** — EPC contractor credit rating, track record on comparable projects, bonding capacity, subcontractor reliance
- **Insurance program** — builder's risk, delay-in-startup (DSU/ALOP) coverage, deductibles, sub-limits
- **Site/permitting status** — land acquisition status, environmental permits, interconnection agreements, offtake contract conditions precedent [VERIFY: jurisdiction-specific permitting requirements]

## Workflow

1. **Map the EPC risk allocation** — Extract key risk provisions from the EPC contract: price structure (lump-sum turnkey vs. open-book), LD caps (typical range: 15-20% of contract price for aggregate LDs), warranty scope, defect liability period, and carve-outs from contractor liability (force majeure, owner-caused delays, change-in-law)

2. **Build the construction cost model** — Structure total project cost as: EPC price + owner's costs + development fees + financing costs (IDC + fees) + contingency. Model contingency drawdown assumptions. Separate hard costs from soft costs. Flag any cost items outside the EPC wrap [VERIFY: treatment of sales tax/VAT on construction costs by jurisdiction]

3. **Model the draw schedule** — Create monthly or quarterly construction draw curves. Standard S-curve or milestone-based draws tied to EPC payment schedule. Layer in equity-first vs. pro-rata vs. debt-first contribution mechanics. Calculate IDC based on drawn balances and construction facility pricing

4. **Run delay scenarios** — Model 3-6-12 month delay cases:
   - Revenue impact: lost operating cash flow during delay period
   - Cost impact: additional IDC, extended owner's costs, standby charges
   - LD recovery: delay LD accrual ($/day) capped at contract maximum
   - Funding gap: does contingency cover the shortfall? Is there a cost overrun facility?
   - Debt service: impact on first principal payment date, tail ratios, sculpted repayment profile

5. **Run cost overrun scenarios** — Model 10-20-30% cost overrun cases:
   - Within EPC wrap: contractor absorbs (verify LD and liability caps)
   - Outside EPC wrap: owner's cost escalation, scope changes, unforeseen conditions
   - Funding response: contingency drawdown → cost overrun facility → equity cure → lender step-in rights
   - Assess whether completion guarantee or sponsor support agreement covers the gap

6. **Evaluate completion guarantee structures** — Assess the enforceability and credit backing of:
   - Sponsor completion guarantees (cost and date certain)
   - Surety bonds / performance bonds (typically 10-30% of EPC price)
   - Standby letters of credit
   - Contingent equity commitments
   - DSU insurance as partial backstop for delay risk

7. **Stress-test debt metrics during construction** — Calculate construction-period covenant compliance: maximum loan-to-cost ratio, minimum equity contribution percentage, conditions precedent to each draw (independent engineer certification, budget-to-complete test). Model whether delay/overrun scenarios trigger draw-stop events or covenant breaches

## Output

- **Construction risk matrix** — tabular mapping of risk category → contractual allocation → residual exposure → mitigation mechanism
- **Base case construction budget and draw schedule** — monthly/quarterly with IDC, contingency, and funding source breakdown
- **Delay scenario dashboard** — 3/6/12-month delay impact on total cost, funding gap, LD recovery, and debt metrics
- **Cost overrun waterfall** — sequential funding response (contingency → overrun facility → equity cure → guarantee call) with breakpoints
- **Completion guarantee assessment** — credit quality of guarantor, cap adequacy, trigger conditions, gap analysis
- **Key risk flags** — items requiring lender/investor attention (uncapped risks, thin contingency, weak contractor credit, permit gaps)

## Quality Checks

- Verify EPC LD caps are correctly applied as % of contract price — not total project cost
- Confirm IDC calculation uses actual draw schedule timing, not a flat average
- Check that contingency is sized relative to identified risks, not just a blanket percentage
- Ensure delay scenarios capture cascading effects (IDC + lost revenue + extended owner's costs simultaneously)
- Validate that completion guarantee coverage matches or exceeds modeled worst-case funding gap
- Cross-check construction facility commitment amount against peak draw requirement plus headroom
- Confirm all cost and schedule assumptions are sourced (independent engineer report, EPC contract, or sponsor estimate) — mark unsourced items with [VERIFY]
- Flag any scenario where the project cannot reach financial completion under stress without additional uncommitted support
