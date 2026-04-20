---
name: modeling-economic-profit-analysis
language: en
description: Builds economic profit (EVA) models with capital charge calculation, value spread analysis, and long-term value creation measurement. Use when calculating economic profit, analyzing EVA trends, or measuring value creation.
tags:
  - modeling
  - capital-allocation-and-corporate-strategy
metadata:
  author: casemark
  practice_areas:
    - Corporate Strategy
    - Capital Allocation
    - Shareholder Value
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Economic Profit Analysis

Builds economic profit (EVA) models that quantify whether a business unit, division, or enterprise earns returns above its cost of capital, enabling capital allocation and value creation decisions.

## When To Use

- Evaluating whether business units create or destroy shareholder value
- Comparing capital allocation efficiency across divisions or investment alternatives
- Building multi-year EVA trend analysis for strategic planning
- Assessing acquisition targets on an economic profit basis (not just accounting earnings)
- Supporting incentive compensation design tied to value creation metrics

## Inputs To Gather

- **Income statement data**: Revenue, operating expenses, NOPAT reconciliation items (tax rate, non-cash charges, unusual items)
- **Balance sheet data**: Total assets, current liabilities, off-balance-sheet items (operating leases capitalized, R&D amortization if applying Stern Stewart adjustments)
- **Capital structure**: Debt/equity mix, cost of debt (pre- and post-tax), equity risk premium assumptions
- **WACC inputs**: Risk-free rate, beta, equity market premium, company-specific risk premium, target vs. actual capital structure [VERIFY: confirm whether to use book or market weights]
- **Accounting adjustments**: List of EVA adjustments to apply (e.g., LIFO reserve, goodwill amortization add-back, restructuring charge normalization, deferred tax treatment) [VERIFY: confirm which Stern Stewart adjustments are in scope — full list exceeds 160]
- **Time horizon**: Historical periods for trend analysis and forecast years

## Workflow

1. **Calculate NOPAT**
   - Start from operating income (EBIT)
   - Apply cash operating tax rate (not statutory rate — exclude tax shields from financing)
   - Add back non-cash charges per agreed adjustment list (e.g., goodwill amortization, LIFO reserve changes, R&D capitalization amortization)
   - Result: NOPAT = Adjusted EBIT × (1 − Cash Tax Rate)

2. **Determine Invested Capital**
   - Begin with total assets, subtract non-interest-bearing current liabilities (accounts payable, accrued expenses)
   - Add back accumulated goodwill amortization, capitalize operating leases (present value of future lease payments), capitalize R&D if applicable
   - Compute beginning-of-period invested capital (or average, per convention) [VERIFY: confirm beginning vs. average capital convention]
   - Track invested capital vintage by year for trend analysis

3. **Compute Capital Charge**
   - Establish WACC: weight cost of equity (CAPM or build-up) and after-tax cost of debt by target capital structure
   - Capital Charge = Invested Capital × WACC
   - Document each WACC component with source (e.g., risk-free rate from 10-year Treasury, beta from Bloomberg/Capital IQ)

4. **Calculate Economic Profit**
   - Economic Profit = NOPAT − Capital Charge
   - Equivalently: Economic Profit = (ROIC − WACC) × Invested Capital
   - The value spread (ROIC − WACC) isolates the rate of value creation from the scale of capital deployed

5. **Build Multi-Period Model**
   - Populate 3–5 years historical and 3–5 years forecast
   - Decompose EP changes year-over-year: volume effect (capital growth × prior spread) vs. spread effect (spread change × current capital)
   - Cumulative EP and present value of EP stream for valuation bridge

6. **Segment and Compare**
   - If multi-division: allocate corporate overhead and shared assets using agreed methodology [VERIFY: allocation keys for shared capital]
   - Rank business units by EP, value spread, and capital turnover
   - Identify value creators (positive EP) vs. value destroyers (negative EP)

7. **Sensitivity and Scenario Analysis**
   - Flex WACC ±50–100 bps and show EP impact
   - Scenario-test key NOPAT drivers (margin compression, revenue decline)
   - Show breakeven ROIC (the WACC rate) and margin of safety

## Output

- **EP Summary Table**: NOPAT, invested capital, capital charge, economic profit, ROIC, WACC, and value spread by period
- **Trend Chart**: Multi-year EP with decomposition into spread and volume effects
- **Divisional Ranking** (if applicable): Business units sorted by EP and value spread with capital deployed
- **Sensitivity Matrix**: EP under WACC and margin scenarios
- **Valuation Bridge**: From accounting book value to intrinsic value using capitalized EP (Market Value = Invested Capital + PV of Future EP)
- **Assumptions Register**: Every input sourced and dated; adjustment rationale documented

## Quality Checks

- ROIC × Invested Capital must reconcile to NOPAT (arithmetic identity check)
- EP calculated via both methods (NOPAT − Capital Charge and Spread × Capital) must match
- WACC components should be internally consistent — cost of equity must exceed cost of debt; blended rate should fall between them
- Verify that accounting adjustments net to zero across the full model (e.g., capitalizing R&D increases both NOPAT and invested capital)
- Confirm tax rate used is cash operating tax rate, not statutory or effective book rate
- Cross-check ROIC against industry benchmarks — flag outliers above 30% or below 0% for investigation
- Ensure invested capital never goes negative (signals missing liabilities or over-adjustment)
