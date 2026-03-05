---
name: structuring-equity-derivative-strategies
description: Designs equity derivative strategies with call spreads, put spreads, straddles, and ratio combinations for investment and hedging. Use when structuring equity strategies, designing option combinations, or evaluating strategy payoffs.
tags:
  - derivatives-and-structured-products
  - investment
metadata:
  author: casemark
  practice_areas:
    - Derivatives
    - Structured Products
    - Hedging
  document_types:
    - Report
  skill_modes:
    - Analysis
---
# Structuring Equity Derivative Strategies

Designs equity derivative strategies using vanilla and exotic option combinations for directional positioning, income generation, volatility capture, and portfolio hedging. Produces structured strategy reports with payoff profiles, breakeven analysis, Greeks exposure, and scenario-based P&L.

## When To Use

- Constructing call spreads, put spreads, straddles, strangles, butterflies, condors, or ratio spreads for a specific market view
- Evaluating hedging overlays for concentrated equity positions or portfolio tail risk
- Comparing strategy alternatives based on cost, payoff asymmetry, and risk/reward tradeoffs
- Structuring collar or protective put strategies with financing considerations
- Analyzing margin and capital requirements for multi-leg option positions
- Designing yield enhancement strategies (covered calls, cash-secured puts, overwriting programs)

## Inputs To Gather

- **Underlying**: Ticker, current price, dividend yield, and borrow cost if applicable
- **Market view**: Directional bias (bullish/bearish/neutral), expected magnitude of move, and time horizon
- **Volatility context**: Current implied volatility (IV) vs. historical volatility (HV), skew shape, term structure (contango/backwardation)
- **Objective**: Hedging (downside protection, tail risk), income generation, directional speculation, or volatility trading
- **Constraints**: Maximum premium outlay or credit target, margin limits, notional sizing, delta budget, regulatory restrictions (e.g., covered-only accounts)
- **Expiration preferences**: Target tenor, roll frequency if applicable
- **Existing positions**: Current equity or option holdings that the strategy must complement

## Workflow

1. **Define objective and market thesis** — Clarify whether the goal is hedging, income, directional exposure, or volatility capture. State the expected price range, time horizon, and conviction level.

2. **Screen candidate structures** — Match thesis to strategy archetypes:
   - *Bullish*: Bull call spread, call ratio backspread, risk reversal, synthetic long
   - *Bearish*: Bear put spread, put ratio backspread, reverse risk reversal, synthetic short
   - *Neutral/range-bound*: Iron condor, iron butterfly, calendar spread, short straddle/strangle
   - *Volatility long*: Long straddle, long strangle, long butterfly (reverse), backspread
   - *Hedging*: Protective put, costless collar, put spread collar, tail-risk put ladder
   - *Income*: Covered call, cash-secured put, call overwrite, put write

3. **Construct the strategy** — Specify each leg: option type (call/put), strike, expiration, quantity, and direction (long/short). Calculate:
   - Net premium (debit or credit)
   - Maximum profit and maximum loss
   - Breakeven point(s)
   - Payoff diagram description (or table at key price levels)

4. **Analyze Greeks exposure** — Report aggregate delta, gamma, theta, and vega at inception. Highlight how Greeks shift as underlying moves toward key strikes and as time decays. Flag any dangerous gamma or vega concentration near expiration.

5. **Run scenario analysis** — Model P&L across at least three scenarios:
   - Base case (expected move)
   - Upside stress (e.g., +2 standard deviations)
   - Downside stress (e.g., -2 standard deviations)
   - Include IV shock scenarios (vol crush / vol expansion) where relevant

6. **Evaluate margin and capital** — Estimate initial margin (Reg-T or portfolio margin as specified), maintenance requirements, and buying power reduction. Note whether the strategy qualifies as defined-risk or undefined-risk. [VERIFY margin methodology against broker/clearing rules]

7. **Compare alternatives** — Present at least two strategy variants side-by-side (e.g., bull call spread vs. risk reversal) with a comparison table covering cost, max gain, max loss, breakevens, and Greeks.

8. **Document roll and exit plan** — Specify conditions for early exit, roll triggers (e.g., delta threshold, days-to-expiration cutoff, profit target), and assignment/exercise handling procedures.

## Output

The strategy report should include:

- **Strategy summary**: Name, legs, net premium, and one-sentence rationale
- **Payoff table**: P&L at underlying prices spanning the strike range in incremental steps (e.g., 5% intervals), at expiration and at a mid-horizon checkpoint
- **Breakeven analysis**: Exact breakeven price(s) with percentage distance from current spot
- **Greeks snapshot**: Delta, gamma, theta (daily), vega per contract and in aggregate
- **Scenario matrix**: P&L under base/upside/downside and vol-shift scenarios
- **Risk metrics**: Maximum loss (dollars and percentage of notional), margin requirement, and risk/reward ratio
- **Comparison table**: Side-by-side of candidate strategies if multiple were evaluated
- **Execution notes**: Recommended order type (limit, market, spread order), liquidity considerations (open interest, bid-ask width), and any leg sequencing advice
- **Roll/exit plan**: Trigger conditions and target adjustments

## Quality Checks

- Verify all strike prices exist in the listed option chain for the chosen expiration [VERIFY against live chain data]
- Confirm net premium arithmetic: sum of individual leg premiums must equal stated net debit/credit
- Ensure breakeven calculations are consistent with payoff table values
- Check that max profit and max loss figures account for all legs, including assignment risk on short options
- Validate that Greeks net correctly across legs (e.g., delta of a bull call spread = long call delta minus short call delta)
- Confirm margin estimates align with the applicable margin framework (Reg-T vs. portfolio margin) [VERIFY with broker margin calculator]
- Flag early exercise risk on American-style options, especially around ex-dividend dates for short calls
- Note any pin risk for strikes near current price as expiration approaches
- Include disclaimer that all values are based on theoretical models and actual execution prices may differ
