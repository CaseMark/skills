---
name: analyzing-volatility-surfaces
description: Constructs and interprets implied volatility surfaces with skew analysis and term structure assessment. Use when analyzing vol surfaces, interpreting skew, or modeling volatility dynamics.
tags:
  - analysis
  - quantitative-finance
metadata:
  author: casemark
  practice_areas:
    - Derivatives
    - Quantitative Analysis
    - Structured Products
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Volatility Surfaces

## When To Use

- Constructing an implied volatility surface from option chain data across strikes and expirations
- Analyzing skew dynamics (put skew, call skew, smile shape) for a single underlier or cross-asset comparison
- Evaluating term structure of volatility for calendar spread positioning or structured product pricing
- Identifying vol surface anomalies that signal mispricing, liquidity dislocations, or event risk
- Supporting pricing or risk review of exotic/structured products that depend on vol surface interpolation

## Inputs To Gather

- **Option chain data**: Bid/ask implied vols (or prices to back-solve) across strikes and expirations; specify underlier (equity index, single stock, FX pair, commodity)
- **Underlier spot/forward**: Current spot price, dividend yield or carry assumptions, and forward curve if available
- **Expiration set**: Which tenors to include (e.g., weekly, monthly, quarterly, LEAPS); confirm whether to use listed expirations or interpolated constant-maturity tenors
- **Strike convention**: Absolute strike, moneyness (K/S), delta-space, or log-moneyness — confirm which convention to use for surface construction
- **Model context**: Whether surface is for mark-to-market, exotic pricing (local vol, stochastic vol), or relative value analysis
- **Reference date and market hours**: As-of date/time for the snapshot; whether to use settlement vols or intraday marks

## Workflow

1. **Validate and clean input data**
   - Filter out stale quotes, zero-volume strikes, and obvious bad ticks (e.g., implied vol < 1% or > 300%)
   - Flag wide bid/ask spreads — use mid-market only when spread is within acceptable threshold [VERIFY: firm-specific threshold]
   - Confirm put-call parity consistency; reconcile any violations by adjusting forward/dividend assumptions

2. **Construct the raw surface**
   - Map implied vols onto a strike × expiration grid using the chosen strike convention
   - For each expiration slice, fit a parametric curve (SVI, SABR, or cubic spline) or use raw market points
   - Interpolate across tenors to fill gaps — use variance-linear interpolation (total variance = σ²·T should increase monotonically in T)
   - Check for calendar spread arbitrage: total variance must be non-decreasing in maturity at every strike
   - Check for butterfly arbitrage: the local variance surface must produce non-negative probability densities

3. **Analyze skew**
   - Compute 25-delta risk reversal (25d call vol − 25d put vol) and 25-delta butterfly (average of 25d wings − ATM vol) for each tenor
   - Measure skew slope: dσ/dK or dσ/d(log-moneyness) around ATM
   - Compare current skew level to historical distribution (percentile rank over 1Y, 3Y windows)
   - Identify skew regime: steep/flat relative to realized skewness of returns, demand-driven vs. fundamental

4. **Analyze term structure**
   - Plot ATM vol across tenors; identify contango (upward-sloping) vs. backwardation (inverted)
   - Calculate vol carry: ATM implied vol minus short-dated realized vol at each tenor point
   - Flag event-driven kinks (earnings, FOMC, expiration clustering) that create localized term structure humps
   - Compare term structure shape to historical norms and cross-asset benchmarks

5. **Assess surface dynamics and Greeks exposure**
   - Estimate vega, vanna (dVega/dSpot), and volga (dVega/dVol) profiles across the surface
   - Identify regions of high convexity or sensitivity relevant to the portfolio or trade under review
   - If for exotic pricing: note where local vol or stochastic vol model choice materially affects valuation (e.g., barriers near skew-sensitive strikes)

6. **Synthesize findings**
   - Summarize surface shape, skew regime, and term structure posture
   - Highlight actionable observations: relative value opportunities, mispriced strikes, or risk concentrations
   - Flag any data quality issues or model-dependent conclusions

## Output

- **Surface summary table**: ATM vols, 25d RR, 25d BF for each tenor
- **Skew analysis section**: Current skew metrics with historical percentile context; skew slope chart data
- **Term structure section**: ATM vol curve, vol carry estimates, event-adjusted term structure
- **Arbitrage check results**: Calendar and butterfly arbitrage flags with specific strike/tenor locations
- **Key findings and trade implications**: 3–5 bullet points with actionable takeaways
- **Data quality notes**: Stale quotes excluded, wide-spread strikes flagged, parity violations observed

## Quality Checks

- Total variance is monotonically non-decreasing in maturity at every strike (no calendar arbitrage)
- Butterfly spreads produce non-negative payoffs at all points (no butterfly arbitrage)
- Interpolated surface reproduces input market quotes within bid/ask tolerance
- Strike convention and delta convention are applied consistently — do not mix sticky-strike and sticky-delta frameworks without explicit notation
- Skew and term structure metrics are compared to correct historical benchmarks (same underlier, same convention) [VERIFY: data source for historical vol percentiles]
- All implied vols are derived using the correct exercise style (American vs. European) and dividend treatment for the underlier [VERIFY: exercise convention for specific product]
- Mark any model-dependent conclusions (e.g., local vol extrapolation beyond liquid strikes) with explicit caveats
