---
name: modeling-management-case-scenarios
language: en
description: Builds base, upside, and downside operating scenarios with key assumption sensitivity and return distribution analysis. Use when building operating cases, stress testing projections, or presenting scenario analysis.
tags:
  - modeling
  - private-equity
metadata:
  author: casemark
  practice_areas:
    - Private Equity
    - Leveraged Buyouts
    - Growth Equity
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Management Case Scenarios

Builds base, upside, and downside operating scenarios with key assumption sensitivity and return distribution analysis for PE-backed companies.

## When To Use

- Building operating cases around a management plan for IC memo or deal screening
- Stress testing a target's projections during diligence to bound downside risk
- Presenting scenario-driven return distributions to LP advisory committees
- Evaluating hold-period sensitivities for add-on acquisitions or bolt-ons
- Assessing covenant headroom across operating environments in leveraged structures

## Inputs To Gather

- **Management projections**: Revenue build-up, gross margin assumptions, opex plan, capex schedule, and working capital trends (typically 5-year horizon)
- **Historical financials**: 3-5 years of audited P&L, balance sheet, and cash flow to anchor base-case assumptions and establish trend lines
- **Deal structure**: Entry valuation (EV/EBITDA), capital structure (debt tranches, rates, amortization), equity check, and fee load
- **Key value drivers**: Identify 3-6 variables with outsized impact on returns (e.g., organic revenue growth, pricing power, margin expansion levers, customer churn)
- **Comparable benchmarks**: Sector median growth rates, margin profiles, and exit multiples from comps or prior deals for reasonableness checks
- **Exit assumptions**: Target hold period, anticipated exit multiple range, and potential exit routes (strategic sale, secondary, IPO)

## Workflow

1. **Anchor the base case on management's plan with adjustments**
   - Start from management projections; apply a historical-achievement haircut where management has a track record of missing (e.g., revenue growth reduced by the average miss over the last 3 years)
   - Normalize one-time items (add-backs, non-recurring revenue) and confirm recurring vs. non-recurring split
   - Build revenue from the bottom up where possible: units x price, customer count x ARPU, or segment-level detail

2. **Define upside and downside cases by toggling key drivers**
   - Select 3-6 assumption variables that most influence MOIC/IRR (typically: revenue growth, EBITDA margin, capex intensity, working capital days, exit multiple)
   - Upside case: reflect achievable outperformance — successful cross-sell, pricing increases stick, margin expansion from operational improvements
   - Downside case: model realistic stress — customer concentration loss, input cost spike, delayed synergy capture, multiple compression at exit
   - Avoid symmetric offsets; downside tails are typically fatter — weight assumptions accordingly

3. **Build the three-case P&L, balance sheet, and cash flow**
   - Project revenue, COGS, and opex line items for each scenario across the hold period
   - Flow through to EBITDA, apply D&A and interest expense from the debt schedule, compute net income and free cash flow
   - Model working capital changes using days-based assumptions (DSO, DIO, DPO) that flex with revenue
   - Ensure balance sheet balances via a cash sweep or revolver draw mechanism

4. **Construct the returns waterfall for each scenario**
   - Apply exit multiple to terminal EBITDA for each case; deduct net debt at exit to derive equity value
   - Calculate gross MOIC, net MOIC (after fees/carry), and IRR for each scenario
   - Show the equity bridge: entry equity → EBITDA growth contribution → multiple expansion/contraction → debt paydown → exit equity

5. **Run sensitivity tables and return distribution analysis**
   - Build two-variable sensitivity grids: entry multiple vs. exit multiple, revenue CAGR vs. margin at exit, leverage vs. growth
   - Identify the break-even assumptions — what growth rate or margin level is needed to return 1.0x equity
   - Summarize probability-weighted returns if scenario probabilities are assigned (e.g., 25% upside / 50% base / 25% downside)

6. **Compile scenario comparison output**
   - Side-by-side summary table: Revenue CAGR, exit EBITDA, exit EV, net debt at exit, equity value, MOIC, IRR for each case
   - Highlight key swing factors and which assumptions create the widest return dispersion
   - Flag any covenant breach triggers in the downside case (leverage ratio, fixed charge coverage, minimum EBITDA)

## Output

- **Scenario summary table**: Side-by-side base / upside / downside with key financial metrics and returns
- **Detailed P&L and cash flow projections** for each case across the hold period
- **Returns waterfall**: Entry equity → value creation components → exit equity for each scenario
- **Sensitivity grids**: 2-variable tables showing MOIC/IRR across assumption ranges
- **Key risks and mitigants**: Narrative summary of what drives the downside and what protections exist (covenants, earn-outs, reps)
- **Assumption log**: Explicit table of every toggled variable, its value in each case, and the rationale or source

## Quality Checks

- **Historical calibration**: Base-case growth and margin assumptions should be within the range of the company's historical performance unless a specific, documented catalyst justifies deviation
- **Balance sheet integrity**: Confirm assets = liabilities + equity in every period, every scenario; revolver/cash sweep functions correctly
- **Debt schedule consistency**: Interest expense ties to average debt balances; mandatory amortization is reflected; covenant tests are computed correctly [VERIFY specific covenant definitions against the credit agreement]
- **Return math verification**: Cross-check MOIC = exit equity / entry equity; IRR computed using actual cash flow dates (not approximations)
- **Downside plausibility**: Ensure the downside case is a genuine stress, not just base minus 5% — reference sector downturns, customer loss scenarios, or input cost shocks for calibration
- **Assumption sourcing**: Every key assumption should reference a source (management plan, diligence finding, comp data, or sponsor thesis) — mark unsupported assumptions with [VERIFY]
- **Exit multiple discipline**: Exit multiples should be benchmarked against current trading comps and precedent transactions; flag any scenario assuming multiple expansion beyond entry [VERIFY against current market conditions]
