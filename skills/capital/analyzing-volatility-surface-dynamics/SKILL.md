---
name: analyzing-volatility-surface-dynamics
language: en
description: Evaluates implied volatility surfaces with skew analysis, term structure dynamics, and surface fitting methodologies. Use when analyzing vol surfaces, assessing skew dynamics, or calibrating volatility models.
tags:
  - analysis
  - derivatives-and-structured-products
metadata:
  author: casemark
  practice_areas:
    - Derivatives
    - Structured Products
    - Hedging
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Volatility Surface Dynamics

## When To Use

- Evaluating implied volatility surfaces across strikes and tenors for options books or structured product pricing
- Diagnosing skew changes (steepening, flattening, or inversion) that signal shifting market risk sentiment
- Calibrating local volatility, stochastic volatility, or parametric models (SVI, SABR) to market data
- Assessing term structure dynamics ahead of catalysts (earnings, central bank decisions, macro releases)
- Comparing realized vs. implied volatility regimes to identify relative value or hedging opportunities

## Inputs To Gather

- **Option chain data**: strikes, expirations, bid/ask IVs, open interest, and volume for the target underlier
- **Underlier reference data**: spot price, dividend yield or forward curve, borrow rate if applicable
- **Market context**: recent realized volatility (10d, 20d, 60d), upcoming events calendar, recent vol regime
- **Model specification**: fitting method in scope (raw interpolation, SVI parameterization, SABR, local vol, etc.)
- **Analysis scope**: single name vs. index, cross-asset comparison, specific tenor range, or full surface

## Workflow

1. **Construct the raw surface**
   - Organize IV data by moneyness (delta or % strike) and days-to-expiry
   - Filter illiquid strikes (low OI or wide bid-ask) — flag any gaps with [VERIFY]
   - Interpolate missing points using cubic spline or linear in variance space; note method chosen

2. **Analyze skew structure**
   - Compute 25-delta risk reversal (RR) and butterfly (BF) for each tenor
   - Classify skew shape: normal negative skew, smile, smirk, or inverted
   - Compare current skew levels to 3-month and 12-month percentile ranks
   - Identify any put-skew premium or call-skew premium anomalies and hypothesize drivers (e.g., hedging demand, event risk)

3. **Evaluate term structure**
   - Plot ATM IV across tenors; identify contango (upward-sloping) vs. backwardation
   - Compute roll-down P&L for key tenors (e.g., 30d to 7d) under static vol assumption
   - Assess kink points around event dates — isolate event-implied moves using variance decomposition
   - Flag any calendar spread anomalies (non-monotonic total variance) as arbitrage signals [VERIFY]

4. **Fit parametric model (if in scope)**
   - **SVI**: Fit raw SVI parameters (a, b, rho, m, sigma) per slice; check Durrleman's no-butterfly-arbitrage condition
   - **SABR**: Calibrate alpha, beta (typically fixed), rho, nu per expiry; assess fit residuals at wings
   - **Local vol**: Apply Dupire's formula on the fitted total variance surface; inspect for negative local variances
   - Report goodness-of-fit metrics: RMSE, max absolute error, and any systematic bias at wings vs. body

5. **Assess dynamics and relative value**
   - Compare current surface snapshot to historical norm — is vol cheap or rich on a z-score basis?
   - Identify sticky-strike vs. sticky-delta behavior in recent moves
   - Evaluate skew convexity: how does RR change per unit move in ATM vol?
   - If cross-asset: compare vol ratios, correlation-implied vs. realized, or dispersion levels

6. **Formulate observations and trade implications**
   - Summarize surface state: overall level, skew posture, term structure shape
   - Highlight actionable signals: mispriced wings, event premium over/under-estimation, calendar spread value
   - Note hedging implications: gamma/vega distribution, preferred hedge tenor, skew exposure from structured positions

## Output

Deliver an **Analysis Report** containing:

- **Surface snapshot**: table or heatmap of IV by moneyness and tenor with color-coded deviations from historical median
- **Skew metrics**: 25d RR, 25d BF, and skew slope per tenor with percentile ranks
- **Term structure summary**: ATM IV curve, event-date variance contributions, contango/backwardation characterization
- **Model calibration results** (if applicable): parameter values, fit diagnostics, arbitrage condition checks
- **Key findings**: 3-5 bullet observations ranked by significance
- **Trade ideas / hedging adjustments**: specific suggestions tied to findings (e.g., "sell 3m 25d put spread vs. buy 1m — skew term structure at 90th %ile")

## Quality Checks

- Confirm total variance is non-decreasing in tenor for every strike — violations indicate bad data or fit error [VERIFY]
- Verify no-arbitrage conditions: no negative butterfly spreads, no negative calendar spreads in price space
- Cross-check ATM levels against consensus (broker screens, exchange settlement vols) [VERIFY]
- Ensure skew metrics use consistent delta convention (spot delta vs. forward delta) throughout
- Validate that parameterized model extrapolation at deep wings does not produce implausible IV levels (e.g., >200% or <1%)
- Mark any data sourced from single-dealer quotes or end-of-day snaps with staleness caveat
- If the analysis supports a structured product pricing decision, flag that independent price verification is required before execution
