---
name: analyzing-inflation-linked-bonds
description: Evaluates TIPS and inflation-linked securities with breakeven analysis and real yield assessment. Use when analyzing inflation bonds, calculating breakeven inflation, or evaluating real return.
tags:
  - analysis
  - fixed-income
metadata:
  author: casemark
  practice_areas:
    - Fixed Income
    - Credit Research
    - Bond Trading
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Inflation Linked Bonds

## When To Use

- Evaluating U.S. TIPS or sovereign inflation-linked bonds (ILBs) for portfolio inclusion or trading
- Calculating breakeven inflation rates to compare inflation expectations vs. market pricing
- Assessing real yield attractiveness across maturities or against historical ranges
- Comparing TIPS vs. nominal Treasuries for relative value decisions
- Analyzing inflation accrual mechanics, seasonality effects, or index lag implications
- Reviewing inflation-linked exposure ahead of CPI prints or monetary policy shifts

## Inputs To Gather

- **Bond identifiers**: CUSIP, ISIN, or specific TIPS series (e.g., 0-7/8% Jan 2029 TIPS)
- **Current market data**: Real yield, nominal yield of comparable maturity Treasury, clean/dirty price, index ratio, accrued inflation compensation
- **Reference CPI data**: Base CPI at issuance, current reference CPI, interpolated daily index ratio [VERIFY current CPI-U reference values from BLS]
- **Curve data**: Real yield curve (TIPS), nominal Treasury curve, breakeven inflation curve
- **Holding period or horizon**: Investment timeframe for scenario analysis
- **Inflation assumptions**: Spot CPI, forward CPI expectations, consensus forecasts
- **Deflation floor relevance**: Whether the bond's par floor is in or out of the money

## Workflow

1. **Confirm bond structure and terms**
   - Identify coupon rate, maturity, issue date, base reference CPI
   - Determine if Canadian-model (lagged CPI with interpolation) or other structure [VERIFY jurisdiction-specific indexation method]
   - Note the 3-month CPI reference lag and daily interpolation convention for U.S. TIPS
   - Check whether deflation floor is currently relevant (index ratio < 1.0)

2. **Calculate breakeven inflation rate**
   - Breakeven = Nominal yield − Real yield (same maturity)
   - Decompose into: expected inflation + inflation risk premium
   - Compare breakeven to survey-based inflation expectations (e.g., Michigan, SPF, Cleveland Fed model)
   - Compute forward breakeven rates for specific horizons (e.g., 5y5y forward breakeven)
   - Flag if breakeven appears rich or cheap relative to historical percentile range

3. **Assess real yield and relative value**
   - Compare current real yield to historical range for the maturity point
   - Evaluate real yield vs. estimated neutral real rate (r*) [VERIFY current Fed estimates]
   - Compute carry and roll-down in real yield terms over the investment horizon
   - Compare TIPS vs. nominal carry: which outperforms if realized inflation equals breakeven?

4. **Model inflation accrual and total return scenarios**
   - Project principal adjustment under base-case, upside, and downside CPI scenarios
   - Calculate total return = real coupon income + inflation accrual + price change from real yield shift
   - Incorporate CPI seasonality (e.g., energy-driven Q1 effects) for short-horizon trades
   - Stress test: What CPI path makes TIPS underperform nominals? Quantify the margin of safety

5. **Evaluate technical and liquidity factors**
   - Assess bid-ask spread and on-the-run vs. off-the-run dynamics
   - Note upcoming TIPS auction supply and Fed holdings/reinvestment policy
   - Consider repo specialness or financing cost differentials
   - Flag any tax implications of phantom income on inflation accrual for taxable accounts

6. **Synthesize recommendation**
   - State whether TIPS look attractive, fair, or expensive vs. nominals at this maturity
   - Specify the implied inflation hurdle rate the investor must believe to prefer TIPS
   - Recommend position sizing or maturity selection if applicable
   - Identify key risks: CPI surprise direction, real rate volatility, liquidity events

## Output

Deliver a structured analysis report containing:

- **Bond summary table**: CUSIP, coupon, maturity, base CPI, current index ratio, accrued inflation
- **Breakeven analysis**: Current breakeven, historical percentile, forward breakevens, comparison to survey expectations
- **Real yield assessment**: Current level, historical context, carry/roll-down projections
- **Scenario matrix**: Total return under 3+ CPI/real yield scenarios (base, high inflation, deflation)
- **Relative value conclusion**: TIPS vs. nominals recommendation with breakeven hurdle clearly stated
- **Risk factors**: Key sensitivities, liquidity caveats, tax considerations

## Quality Checks

- Confirm index ratio and reference CPI values match published Treasury Direct or Bloomberg data [VERIFY]
- Validate that breakeven = nominal yield − real yield (no sign or compounding errors)
- Ensure scenario analysis covers both inflation upside and deflation/disinflation downside
- Check that carry/roll-down calculations use correct day count and curve interpolation
- Verify that deflation floor value is incorporated if index ratio is near or below 1.0
- Confirm forward breakeven derivation is arithmetically consistent with spot breakevens
- Flag any stale CPI data — reference CPI values change on a fixed monthly schedule
