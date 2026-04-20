---
name: pricing-lp-interest-portfolios
language: en
description: Evaluates LP interest portfolios with fund-by-fund NAV assessment, J-curve positioning, and portfolio-level pricing methodology. Use when pricing secondary portfolios, evaluating LP interest bids, or analyzing fund vintages.
tags:
  - valuation
  - secondaries-and-gp-led
  - portfolio
metadata:
  author: casemark
  practice_areas:
    - Secondaries
    - GP-Led Transactions
    - LP Portfolio Management
  document_types:
    - Valuation Report
  skill_modes:
    - Valuation
    - Calculation
---
# Pricing Lp Interest Portfolios

Evaluates LP interest portfolios with fund-by-fund NAV assessment, J-curve positioning, and portfolio-level pricing methodology.

## When To Use

- Pricing a portfolio of LP interests for a secondary sale or bid evaluation
- Assessing an incoming secondary bid against internal fair value estimates
- Performing vintage-year analysis across a multi-fund LP book
- Supporting investment committee memos with fund-by-fund NAV discount/premium rationale
- Evaluating GP-led continuation vehicle pricing relative to LP secondary alternatives

## Inputs To Gather

- **Fund-level data**: Most recent GP-reported NAV, NAV date, fund vintage year, strategy (buyout, growth, venture, credit, real assets), fund size, and GP name
- **Cash flow history**: Capital called to date, distributions to date, remaining unfunded commitment per fund
- **J-curve indicators**: Fund age relative to typical investment period, % invested, DPI and RVPI multiples
- **GP quarterly reports**: Underlying portfolio company revenue/EBITDA multiples, write-ups/write-downs, and exit pipeline commentary
- **Market benchmarks**: Recent secondary transaction pricing by strategy and vintage (e.g., Greenhill, Jefferies, Evercore secondary market reports) [VERIFY: confirm availability of latest quarterly secondary pricing data]
- **Buyer constraints**: Target IRR/MOIC, portfolio concentration limits, GP relationship considerations

## Workflow

1. **Organize the portfolio into fund-level line items.** For each fund, record: GP name, vintage, strategy, fund size, LP commitment, called %, NAV as of reporting date, unfunded commitment, DPI, TVPI, and RVPI.

2. **Classify each fund by J-curve position.**
   - *Early (0–3 yrs)*: Predominantly unfunded; NAV reflects cost or slight markdowns. Discount typically 15–40% of NAV depending on strategy and GP track record.
   - *Mid-life (3–7 yrs)*: Active value creation period; NAV reflects marked-up assets. Discount range narrows to 0–20% for top-quartile GPs; wider for lower-quartile.
   - *Mature/Tail (7+ yrs)*: Harvesting phase; NAV concentrated in fewer holdings. Premium possible for near-term exit visibility; discount for stale or hard-to-exit assets.

3. **Apply strategy-specific discount/premium adjustments.**
   - Buyout: Anchor to public comparable EV/EBITDA multiples vs. GP marks; adjust for leverage and sector mix.
   - Venture/Growth: Haircut unrealized markups on late-stage private rounds; cross-check against recent public listing comps. Wider discount bands typical (20–50% for early-stage venture).
   - Credit/Real Assets: Assess yield-to-maturity and current income; narrower discount ranges where cash flows are contractual.
   - [VERIFY: confirm current secondary market clearing spreads by strategy from latest broker reports]

4. **Price unfunded commitments separately.** Unfunded obligations represent a future capital call liability. Value them as: `Unfunded × (1 − expected loss ratio)` discounted at buyer's required return, or apply a fixed cent-on-the-dollar rate consistent with market convention (often 0–5% cost for high-quality GPs, higher for lower-conviction names).

5. **Calculate fund-level bid prices.** For each fund: `Bid Price = (NAV × Discount/Premium Factor) − (Unfunded Commitment Cost)`. Express as % of NAV and as absolute dollar value.

6. **Aggregate to portfolio-level pricing.**
   - Sum fund-level bid prices for total portfolio value.
   - Calculate blended portfolio discount to NAV.
   - Compute portfolio-level expected return metrics (IRR, MOIC) using projected cash flow scenarios.
   - Assess concentration risk: top-5 fund exposure, single-GP exposure, strategy tilt, vintage clustering.

7. **Run sensitivity analysis.** Stress-test portfolio pricing across:
   - NAV adjustment scenarios (−10%, base, +10%)
   - Exit timing delays (6-month, 12-month pushback)
   - Public market drawdown impact on unrealized marks
   - Unfunded call pace acceleration

## Output

Produce a **Portfolio Pricing Summary** containing:

- **Portfolio overview table**: Fund name, vintage, strategy, NAV, unfunded, DPI/TVPI, J-curve stage, fund-level bid (% of NAV and $)
- **Blended pricing**: Aggregate bid as % of total NAV, total dollar bid, weighted-average discount
- **Return projections**: Base-case IRR and MOIC with stated assumptions on exit timing and pacing
- **Sensitivity matrix**: Pricing across NAV adjustment and exit delay scenarios
- **Key risk flags**: Concentration issues, stale NAVs (>6 months old), GP-specific concerns, large unfunded exposure
- **Recommendation**: Suggested bid range with rationale tied to fund-level analysis

## Quality Checks

- Confirm NAV dates are within acceptable staleness window (typically ≤2 quarters); flag older marks with [VERIFY]
- Cross-check fund-level TVPI/DPI against benchmark databases (Cambridge Associates, Preqin, Burgiss) [VERIFY: confirm benchmark data access]
- Validate that discount/premium assumptions align with recent comparable secondary transactions
- Ensure unfunded commitment treatment is internally consistent across all funds
- Verify arithmetic: fund-level bids must sum to portfolio-level total; IRR/MOIC models must tie to cash flow inputs
- Confirm strategy classification matches GP-reported strategy (e.g., don't classify a growth equity fund as buyout)
- Flag any fund where GP-reported NAV diverges >20% from implied public market equivalent
