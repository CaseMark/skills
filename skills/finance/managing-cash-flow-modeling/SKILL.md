---
name: managing-cash-flow-modeling
language: en
description: Models portfolio cash flows for liability-driven and income-oriented investment strategies. Use when modeling portfolio cash flows, planning income distributions, or managing liability matching.
tags:
  - management
  - asset-management
  - investment
  - portfolio
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
# Managing Cash Flow Modeling

Models portfolio cash flows for liability-driven and income-oriented investment strategies.

## When To Use

- Building or updating a liability-driven investment (LDI) cash flow schedule
- Planning periodic income distributions (retirement drawdown, endowment spending, trust distributions)
- Stress-testing a portfolio's ability to meet known future obligations (pension payments, insurance reserves, debt service)
- Evaluating reinvestment risk when bonds mature or coupons reset
- Comparing candidate portfolio allocations on a cash-flow-sufficiency basis

## Inputs To Gather

- **Liability schedule**: Dates, amounts, and confidence level (contractual vs. actuarial estimate) for each future obligation
- **Current holdings**: Position-level detail — instrument type, par/notional, coupon/dividend rate, payment frequency, maturity/call dates, amortization terms
- **Yield/spread assumptions**: Current curve (Treasury, swap, or relevant benchmark), credit spreads, prepayment speed assumptions (CPR/PSA for MBS) [VERIFY against current market data]
- **Reinvestment assumptions**: Rate at which interim cash flows are assumed to be redeployed; specify flat rate, forward curve, or custom schedule
- **Distribution policy**: Spending rate, smoothing rules, floor/ceiling constraints, timing (monthly, quarterly, annual)
- **Tax treatment**: Taxable vs. tax-exempt status; applicable rate for coupon income vs. capital gains [VERIFY jurisdiction-specific rates]
- **Modeling horizon**: Start date, end date, and granularity (monthly, quarterly, annual buckets)

## Workflow

1. **Map the liability stream** — Lay out each obligation by period. For actuarial liabilities (pensions, insurance), note the discount rate used and flag sensitivity to rate changes. Separate hard (contractual) from soft (discretionary) liabilities.

2. **Project asset cash flows** — For each holding, generate the expected cash flow timeline:
   - Fixed-rate bonds: coupon payments + principal at maturity/call date
   - Floating-rate instruments: project coupons using forward curve or stated spread + index
   - MBS/ABS: apply prepayment model (CPR/PSA) to project principal return schedule [VERIFY prepayment speed assumption is current]
   - Equities/alternatives: apply dividend yield or distribution rate assumption; note higher uncertainty
   - Maturing principal: slot into reinvestment pool at assumed reinvestment rate

3. **Aggregate by period** — Sum inflows (coupons, dividends, principal returns, reinvestment income) and outflows (liability payments, management fees, taxes) per period. Compute net cash flow per bucket.

4. **Run surplus/deficit analysis** — For each period, calculate cumulative surplus or shortfall. Identify the first period of deficit (if any) and the magnitude. Flag periods where surplus is thin relative to liability volatility.

5. **Stress-test key assumptions**:
   - **Interest rate shift**: parallel +/- 100 bps; steepener/flattener scenarios
   - **Prepayment shock**: for MBS-heavy portfolios, test fast (2x baseline) and slow (0.5x baseline) CPR
   - **Credit event**: model default/downgrade on largest credit exposures and impact on expected cash flows
   - **Longevity/inflation**: for pension/retirement portfolios, extend liability horizon or inflate future payments [VERIFY actuarial assumptions with plan actuary]

6. **Evaluate reinvestment risk** — Quantify how much of the portfolio matures within the next 1, 3, and 5 years. Model the impact of reinvesting at current forwards vs. stressed rate scenarios on future income.

7. **Summarize and recommend** — Present the cash flow model results with a clear recommendation on portfolio adequacy, timing of any shortfalls, and suggested adjustments (extend duration, add higher-coupon assets, build cash reserve buffer).

## Output

The deliverable should include:

- **Cash flow schedule table**: Period-by-period inflows, outflows, net cash flow, and cumulative surplus/deficit
- **Surplus/deficit chart**: Visual timeline showing cumulative position relative to zero
- **Sensitivity summary**: Table showing net surplus under each stress scenario (rate shift, prepayment, credit, inflation)
- **Reinvestment risk profile**: Maturity runoff schedule with income-at-risk under adverse reinvestment rates
- **Key assumptions register**: Every assumption used (reinvestment rate, prepayment speed, discount rate, tax rate, distribution policy) listed with source and date
- **Action items**: Specific portfolio adjustments recommended to close any identified gaps

## Quality Checks

- Verify that total projected asset cash flows reconcile to current portfolio market value plus expected income (no double-counting or omissions)
- Confirm liability amounts and timing match the most recent actuarial valuation or contractual schedule [VERIFY with plan sponsor or trustee]
- Ensure reinvestment rate assumptions are internally consistent with the yield curve used for discounting
- Check that stress scenarios cover the primary risk factors for the specific portfolio composition (e.g., don't omit prepayment stress for an MBS-heavy book)
- Validate that the model horizon extends at least to the longest-dated liability
- Confirm tax treatment is applied correctly — gross vs. net cash flows must be clearly labeled
- Flag any holdings with missing data (e.g., no call schedule, no prepayment model) with [VERIFY] rather than silently assuming defaults
