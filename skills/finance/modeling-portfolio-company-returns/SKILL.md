---
name: modeling-portfolio-company-returns
language: en
description: Builds PE return models with entry/exit multiples, leverage analysis, and value creation attribution. Use when modeling PE returns, calculating IRR/MOIC, or attributing value creation drivers.
tags:
  - modeling
  - private-equity
metadata:
  author: casemark
  practice_areas:
    - Private Equity
    - Venture Capital
    - Growth Equity
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Portfolio Company Returns

## When To Use

- Modeling projected or realized returns for a PE/growth equity portfolio company
- Calculating IRR, MOIC, and cash-on-cash returns across holding periods
- Attributing value creation to revenue growth, margin expansion, multiple expansion, and leverage paydown
- Comparing entry vs. exit economics for investment committee memos or LP reporting
- Stress-testing return sensitivity to purchase price, leverage, and exit assumptions

## Inputs To Gather

- **Entry transaction details**: purchase price (enterprise value), equity check size, entry EV/EBITDA multiple, transaction fees, and sources & uses
- **Capital structure at entry**: senior debt, subordinated debt, mezzanine, seller notes, rollover equity, management equity; interest rates and amortization schedules
- **Operating projections**: revenue, EBITDA, and free cash flow forecasts for the hold period (typically 3–7 years); capex, working capital, and tax assumptions
- **Exit assumptions**: target exit EV/EBITDA multiple, expected exit year, transaction costs at exit
- **Additional cash flows**: add-on acquisitions, dividend recaps, management fees, monitoring fees, or other interim distributions
- **Benchmark context**: comparable transaction multiples, sector median returns, or fund-level return targets for reasonableness checks

## Workflow

1. **Build the sources & uses table**
   - Map total enterprise value, transaction fees, and financing fees on the uses side
   - Lay out debt tranches, sponsor equity, rollover equity, and any co-invest on the sources side
   - Confirm total sources equal total uses

2. **Construct the operating model**
   - Project revenue, EBITDA, and unlevered free cash flow year-by-year through the hold period
   - Apply working capital changes, capex, and tax assumptions to derive free cash flow available for debt service
   - If add-on acquisitions are modeled, layer in incremental EBITDA and purchase price in the relevant year

3. **Model the debt schedule**
   - For each tranche: opening balance, mandatory amortization, cash sweep (if applicable), interest expense, and closing balance
   - Calculate total debt remaining at each projected exit year
   - Track cumulative cash interest vs. PIK interest separately

4. **Calculate exit proceeds and equity waterfall**
   - Apply exit multiple to projected EBITDA at each candidate exit year
   - Deduct remaining net debt and transaction costs to arrive at equity value at exit
   - Run equity proceeds through the waterfall: preferred return hurdles, GP catch-up, carried interest splits, and management option pool dilution where applicable

5. **Compute return metrics**
   - **MOIC**: total equity distributions ÷ total equity invested
   - **Gross IRR**: internal rate of return on equity cash flows (entry, interim distributions, exit)
   - **Net IRR**: after management fees and carried interest [VERIFY fund-level fee structure]
   - **Cash-on-cash**: cumulative cash returned ÷ equity invested (useful for dividend recap scenarios)
   - **DPI / TVPI**: for fund-level context if aggregating across portfolio

6. **Perform value creation bridge**
   - Decompose total equity return into four drivers:
     - **Revenue/EBITDA growth**: EBITDA increase at constant entry multiple
     - **Margin expansion**: incremental EBITDA from margin improvement at constant revenue
     - **Multiple expansion**: delta between entry and exit multiples applied to exit EBITDA
     - **Leverage effect (FCF and debt paydown)**: equity accretion from debt reduction over the hold period
   - Present as a waterfall chart or bridge table summing to total equity gain

7. **Run sensitivity and scenario analysis**
   - Two-way sensitivity tables on entry multiple vs. exit multiple and on EBITDA growth vs. leverage
   - Downside, base, and upside scenarios with clearly labeled assumption sets
   - Breakeven analysis: minimum exit multiple or EBITDA level needed to return 1.0x MOIC

## Output

- **Sources & uses table** with clearly labeled debt and equity components
- **Annual operating projections** with revenue, EBITDA, FCF, and debt balances
- **Return summary table**: MOIC, gross IRR, net IRR for each exit year (Year 3 through Year 7)
- **Value creation bridge**: quantified attribution across growth, margin, multiple, and leverage drivers
- **Sensitivity tables**: at minimum, entry/exit multiple grid and EBITDA growth/exit multiple grid
- **Key assumptions register**: every material assumption listed with source or [VERIFY] tag

## Quality Checks

- Sources & uses must balance to the penny — flag any rounding discrepancy
- IRR calculation must use actual cash flow dates (or mid-year convention if specified); confirm no circular references in debt sweep calculations
- Exit equity value must reconcile: exit EV minus net debt minus fees equals equity to sponsors
- Value creation bridge components must sum to total equity gain within ±0.1x MOIC rounding tolerance
- Confirm leverage ratios (Debt/EBITDA) stay within covenant levels at each projection year [VERIFY specific covenant thresholds from credit agreement]
- Cross-check modeled returns against sector benchmarks — flag if gross IRR exceeds 40% or falls below 10% as warranting additional assumption review
- Verify tax treatment of carried interest and management fee offsets align with fund LPA terms [VERIFY jurisdiction-specific tax rates and fund terms]
