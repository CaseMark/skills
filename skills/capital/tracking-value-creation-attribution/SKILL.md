---
name: tracking-value-creation-attribution
description: Decomposes PE returns into revenue growth, margin expansion, multiple expansion, leverage paydown, and multiple contraction components. Use when attributing value creation, analyzing return drivers, or preparing exit case studies.
tags:
  - monitoring
  - private-equity
metadata:
  author: casemark
  practice_areas:
    - Private Equity
    - Leveraged Buyouts
    - Growth Equity
  document_types:
    - Tracking Report
  skill_modes:
    - Monitoring
---
# Tracking Value Creation Attribution

Decomposes PE returns into revenue growth, margin expansion, multiple expansion, leverage paydown, and multiple contraction components. Used for periodic monitoring, exit case studies, IC memos, and LP reporting.

## When To Use

- Quarterly or annual portfolio company performance reviews requiring return decomposition
- Exit preparation to build the value creation narrative for prospective buyers or LPs
- IC memos where the team needs to attribute realized or unrealized gains to specific drivers
- Fund-level attribution for LP annual meetings or advisory board presentations
- Comparing value creation profiles across portfolio companies or across vintage years
- Post-mortem analysis on exited deals to inform future underwriting

## Inputs To Gather

- **Entry metrics**: acquisition date, entry enterprise value (EV), entry equity value, entry EBITDA (or relevant earnings metric), entry EV/EBITDA multiple, acquisition debt quantum and structure
- **Current/exit metrics**: reporting-date EV, current equity value, current EBITDA, current EV/EBITDA multiple, current net debt (by tranche if available)
- **Revenue bridge**: entry revenue, current revenue, organic vs. acquisitive growth split if applicable
- **Margin detail**: entry EBITDA margin, current EBITDA margin, key margin drivers (pricing, cost reduction, mix shift, add-backs)
- **Debt schedule**: original debt balance, cumulative amortization, any refinancings, cash sweep payments, current net debt
- **Capital flows**: any follow-on equity injections, dividends or recaps, management rollover amounts
- **Benchmark data** (optional): sector trading multiples at entry and current date for context on multiple expansion/contraction

## Workflow

1. **Anchor the equity bridge** — Start with entry equity value and target current (or exit) equity value. The total value created equals the difference. Express as both absolute dollars and gross MOIC.

2. **Decompose EBITDA growth into revenue and margin components**:
   - Revenue growth contribution = (Current Revenue − Entry Revenue) × Entry EBITDA Margin. This isolates the profit impact of top-line growth at constant margins.
   - Margin expansion contribution = Current Revenue × (Current EBITDA Margin − Entry EBITDA Margin). This captures the profit impact of efficiency gains on the full current revenue base.
   - Cross-check: Revenue contribution + Margin contribution should equal total EBITDA change (Current EBITDA − Entry EBITDA). If using organic/inorganic splits, further decompose revenue growth into same-store and M&A-driven components.

3. **Calculate multiple expansion (or contraction)**:
   - Multiple effect = Current EBITDA × (Current EV/EBITDA − Entry EV/EBITDA).
   - If multiples contracted, this will be a negative contributor — label clearly as multiple contraction.
   - Note whether multiple movement reflects sector re-rating, company-specific quality improvement, or transaction-specific dynamics (e.g., competitive auction premium). [VERIFY] that multiple calculations use consistent EBITDA definitions (LTM, NTM, pro forma).

4. **Quantify leverage/debt paydown contribution**:
   - Debt paydown effect = Entry Net Debt − Current Net Debt (positive value means equity accrued to sponsors via deleveraging).
   - Include mandatory amortization, voluntary prepayments, and cash sweep proceeds.
   - If there were dividend recaps or follow-on equity injections, net these against the debt paydown figure or break them out as a separate line item.

5. **Reconcile and allocate residual**:
   - Sum all components: Revenue Growth + Margin Expansion + Multiple Expansion + Debt Paydown should equal Total Equity Value Created.
   - Any residual typically arises from interaction effects (e.g., EBITDA growth × multiple change simultaneously). Allocate proportionally or present as a separate "cross/interaction" term.
   - Express each component as a percentage of total value created and as an implied MOIC contribution.

6. **Build the attribution waterfall**:
   - Present as a bridge chart: Entry Equity → +Revenue Growth → +Margin Expansion → +/−Multiple Change → +Debt Paydown → −Follow-on Equity (if any) → Current Equity.
   - Include a summary table with absolute dollar values, percentage of total, and implied MOIC contribution per driver.

## Output

- **Equity bridge waterfall** (tabular and/or chart-ready format) showing each value creation component from entry equity to current/exit equity
- **Summary attribution table** with columns: Component | $ Value Created | % of Total | MOIC Contribution
- **Key narrative points**: 2-3 sentences per driver explaining what specifically caused the value change (e.g., "Margin expansion of 340bps driven primarily by procurement savings initiative and SG&A leverage on fixed cost base")
- **Context and caveats**: note any material adjustments, pro forma assumptions, or EBITDA definition differences between entry and current reporting
- **Benchmark comparison** (if data provided): how the portfolio company's multiple expansion compares to sector trading multiple movement over the same period

## Quality Checks

- Entry Equity + Total Value Created = Current Equity (must tie exactly)
- Sum of all attribution components = Total Value Created (residual/interaction term < 5% of total, or explicitly disclosed)
- EBITDA figures used in multiple calculations match the EBITDA figures in revenue/margin decomposition (no mixing LTM vs. NTM without disclosure)
- Debt paydown figure reconciles to the actual change in net debt on the balance sheet
- [VERIFY] that any pro forma or run-rate EBITDA adjustments are consistently applied at both entry and current measurement points
- [VERIFY] that management fee offsets, transaction fees, and monitoring fees are treated consistently (gross vs. net returns)
- If organic/inorganic split is presented, confirm add-on acquisition EBITDA contribution is properly separated from same-store growth
- MOIC and IRR figures cross-check against fund administrator or portfolio monitoring system outputs
