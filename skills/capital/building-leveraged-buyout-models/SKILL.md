---
name: building-leveraged-buyout-models
language: en
description: Constructs LBO models with sources/uses, debt schedules, operating projections, and returns analysis across entry/exit scenarios. Use when modeling leveraged buyouts, calculating sponsor returns, or analyzing leverage capacity.
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
    - Model
  skill_modes:
    - Modeling
---
# Building Leveraged Buyout Models

## When To Use

- Modeling a sponsor-backed acquisition to evaluate feasibility and returns
- Sizing debt capacity and structuring capital across tranches (senior, sub, mezzanine)
- Stress-testing leverage and coverage ratios under downside scenarios
- Comparing entry/exit multiple assumptions to derive IRR and MOIC targets
- Evaluating management rollover, co-invest, or earnout structures alongside sponsor equity

## Inputs To Gather

- **Target financials**: Last 3 years of revenue, EBITDA, capex, working capital; current-year budget or LTM figures
- **Transaction terms**: Purchase price or EV/EBITDA entry multiple, transaction fees (advisory, financing, legal), minimum cash on balance sheet
- **Debt terms**: Tranche sizes (revolver, Term Loan A/B, senior notes, mezzanine), interest rates (fixed vs. floating + spread), amortization schedules, mandatory prepayment sweep percentages, commitment fees
- **Operating projections**: Revenue growth rates, margin assumptions, capex as % of revenue, working capital days (DSO, DIO, DPO), tax rate [VERIFY jurisdiction-specific rates]
- **Exit assumptions**: Holding period (typically 3–7 years), exit multiple range, expected dividend recaps if applicable
- **Equity structure**: Sponsor equity contribution, management rollover %, option pool or incentive equity allocation

## Workflow

1. **Build sources & uses table**
   - Uses: enterprise value, refinanced debt, transaction fees (banker, legal, financing), cash to balance sheet
   - Sources: each debt tranche sized to leverage multiple (e.g., Senior at 4.0x EBITDA, Sub at 1.5x), sponsor equity as residual plug
   - Cross-check total sources = total uses

2. **Construct the debt schedule**
   - For each tranche: opening balance, mandatory amortization, optional prepayments (from excess cash flow sweep), closing balance
   - Calculate interest expense per tranche per period (handle PIK vs. cash-pay separately)
   - Model revolver draws/paydowns based on minimum cash balance constraint
   - Track total leverage (Total Debt / EBITDA) and senior leverage through the hold

3. **Build operating model projections**
   - Project revenue, EBITDA, and EBIT from base-case growth and margin assumptions
   - Derive unlevered free cash flow: EBITDA − taxes on EBIT − capex − change in net working capital
   - Apply mandatory debt service and sweep mechanics to determine cash available for optional prepayment
   - Confirm debt service coverage ratio (DSCR) exceeds covenant minimums each period [VERIFY lender covenant thresholds]

4. **Calculate returns at exit**
   - Apply exit multiple to projected EBITDA at end of hold period
   - Subtract net debt at exit to derive equity value to sponsors
   - Compute gross IRR and MOIC on sponsor equity (include any interim dividends or recap proceeds)
   - Back into implied entry vs. exit multiple arbitrage contribution to returns

5. **Run sensitivity and scenario analysis**
   - Two-way sensitivity tables: entry multiple vs. exit multiple, revenue growth vs. margin, leverage vs. exit multiple
   - Downside case: revenue miss of 10–20%, margin compression of 100–200 bps, no multiple expansion — confirm no covenant breach and positive equity value
   - Upside case: outperformance + earlier exit or dividend recap — show max returns
   - Flag any scenario where leverage ratio exceeds typical market thresholds (>6.0x total for middle-market, >7.0x for large-cap) [VERIFY current market leverage norms]

6. **Document the model package**
   - Assumption summary page: entry multiple, leverage, growth, margins, exit multiple
   - Key outputs page: IRR/MOIC at base/down/up, credit statistics through the hold, FCF conversion
   - Clearly label cells as input (blue font), formula (black), or linked (green) per modeling convention

## Output

- **Sources & Uses table** with complete reconciliation
- **Debt schedule** showing each tranche's balance, interest, amortization, and covenants through the hold
- **Operating projections** (income statement through unlevered FCF) for the hold period
- **Returns summary**: IRR, MOIC, and cash-on-cash at base, upside, and downside
- **Sensitivity tables**: two-way grids on key return drivers
- **Credit statistics**: leverage ratios, coverage ratios, and FCF yield by year

## Quality Checks

- Sources exactly equal uses — no unresolved plugs
- Debt balances never go negative; revolver does not exceed commitment size
- Balance sheet balances in every period (if full three-statement model)
- IRR and MOIC are internally consistent (cross-check IRR via XIRR against discrete cash flows)
- DSCR and leverage ratios are within stated covenant limits in the base case
- Circular references from cash sweep → interest → net income → cash sweep are resolved with an iteration toggle or copy-paste macro
- All hard-coded assumptions are isolated on a single inputs tab, not buried in formulas
- Tax rate, amortization of financing fees, and D&A treatment are consistent with target jurisdiction [VERIFY]
