---
name: modeling-credit-fund-portfolios
language: en
description: Builds credit fund portfolio models with yield attribution, default/recovery scenarios, and portfolio-level return analysis. Use when modeling credit funds, projecting portfolio returns, or analyzing yield components.
tags:
  - modeling
  - credit-and-institutional-lending
  - portfolio
  - credit
metadata:
  author: casemark
  practice_areas:
    - Credit Markets
    - Leveraged Lending
    - Direct Lending
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Credit Fund Portfolios

Builds credit fund portfolio models with yield attribution, default/recovery scenarios, and portfolio-level return analysis for direct lending, broadly syndicated loan, and private credit strategies.

## When To Use

- Projecting net returns for a credit fund across base, stress, and downside scenarios
- Decomposing portfolio yield into coupon, OID, fee income, and PIK components
- Modeling default waterfalls with recovery timing and severity assumptions
- Evaluating the impact of leverage (subscription lines, asset-level facilities) on equity returns
- Preparing LP reporting models or IC memoranda that require portfolio-level return attribution

## Inputs To Gather

- **Portfolio composition**: loan tape or representative pool (borrower, commitment size, drawn %, spread, floor, OID, maturity, asset type)
- **Fund terms**: management fee rate, incentive fee / carried interest structure, hurdle rate, preferred return, catch-up, GP commitment %
- **Leverage assumptions**: advance rate, cost of borrowing on credit facility, commitment fee on undrawn, covenant headroom
- **Credit assumptions**: annual default rate, loss given default (LGD) or recovery rate, recovery lag (months), prepayment rate (CPR or voluntary)
- **Deployment schedule**: ramp period, reinvestment period end, harvest / wind-down timeline
- **Fee income**: upfront origination fees, amendment/waiver fees, prepayment penalties, LIBOR/SOFR floor benefit [VERIFY: confirm current reference rate and transition status]

## Workflow

1. **Build the loan tape model**
   - Populate each position with par amount, spread (S + margin), SOFR floor, OID amortization schedule, maturity, and PIK toggle if applicable
   - Calculate weighted-average spread, weighted-average life (WAL), and cash vs. PIK yield split
   - Flag any floating-rate mismatches between assets and liabilities

2. **Construct yield attribution**
   - Separate gross portfolio yield into: (a) cash coupon, (b) OID accretion, (c) origination/amendment fee amortization, (d) PIK accrual, (e) SOFR floor benefit
   - Sum to gross asset yield; subtract cost of fund-level leverage to arrive at net asset yield
   - Layer in management fees and fund expenses to compute net investment income (NII)

3. **Model default and recovery scenarios**
   - Define scenarios — e.g., base (1–2% annual default, 60–70% recovery), stress (4–5% default, 40–50% recovery), severe (8%+ default, 25–35% recovery) [VERIFY: adjust ranges to match fund vintage and asset class norms]
   - Apply defaults as random or front-loaded timing vectors across the portfolio life
   - Model recovery cash flows with a lag (typically 12–24 months post-default) and haircut to par
   - Calculate net credit losses per period and cumulative loss rate

4. **Layer leverage and compute equity returns**
   - Model subscription-line draws during ramp, converting to term asset-level leverage post-ramp
   - Calculate interest expense on drawn leverage, undrawn commitment fees, and facility amortization
   - Compute levered vs. unlevered returns: gross ROA → levered gross return → net-of-fee return to LPs
   - Derive gross and net IRR, MOIC, and DPI across the fund life for each scenario

5. **Build the waterfall and carried interest schedule**
   - Map cash flows through the distribution waterfall: return of capital → preferred return → GP catch-up → carried interest split
   - Compute GP economics (management fees + carry) and LP net returns separately
   - Sensitivity-test the waterfall on deployment pace, default timing, and prepayment speed

6. **Run sensitivity and scenario tables**
   - Two-way tables: default rate vs. recovery rate → net IRR to LPs
   - Two-way tables: spread compression vs. prepayment speed → gross yield
   - Toggle leverage on/off to isolate leverage contribution to returns
   - Stress-test SOFR path scenarios (parallel shift, inversion) on floating-rate NIM

## Output

- **Portfolio summary**: position count, total commitments, drawn balance, WAL, WA spread, WA OID, cash/PIK mix
- **Yield attribution table**: line-item decomposition from gross asset yield to LP net return
- **Scenario matrix**: base / stress / severe cases showing gross IRR, net IRR, MOIC, DPI, cumulative loss rate
- **Leverage impact summary**: unlevered vs. levered returns with advance rate and borrowing cost shown
- **Waterfall schedule**: period-by-period cash flows to LP and GP, with carry crystallization timing
- **Sensitivity tables**: two-way grids on key drivers (default/recovery, spread/prepay, SOFR path)

## Quality Checks

- Confirm WAL and WA spread match the loan tape; reconcile any differences from PIK or OID treatment
- Verify that gross-to-net bridge is fully traceable (no unexplained leakage between gross yield and LP net return)
- Ensure default timing vectors sum to the stated cumulative default rate over fund life
- Check that recovery cash flows are lagged correctly and do not exceed par
- Validate waterfall math: LP preferred return accrues correctly; catch-up and carry split match fund LPA terms [VERIFY: confirm specific waterfall mechanics against the fund's LPA]
- Cross-check levered return math — leverage should amplify both upside and downside symmetrically relative to the advance rate and spread-over-borrow differential
- Confirm SOFR floor benefit is calculated only when reference rate falls below the contractual floor
- Test edge cases: 100% prepayment in year 1, zero defaults, and full portfolio wipeout to ensure model stability
