---
name: modeling-variance-and-volatility-swaps
description: Prices variance and volatility swaps with replication methodology, convexity adjustment, and discrete monitoring analysis. Use when pricing vol products, modeling variance swaps, or evaluating volatility strategies.
tags:
  - modeling
  - derivatives-and-structured-products
metadata:
  author: casemark
  practice_areas:
    - Derivatives
    - Structured Products
    - Hedging
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Variance And Volatility Swaps

## When To Use

- Pricing a variance swap (fair strike Kvar) or volatility swap (fair strike Kvol) on an equity index, single stock, or FX pair
- Converting between variance and volatility strike using the convexity adjustment
- Evaluating the impact of discrete monitoring vs. continuous monitoring on swap value
- Marking an existing variance/volatility swap position to market mid-life
- Comparing implied variance from the options strip against realized variance for trade entry/exit decisions
- Hedging a volatility book by decomposing variance swap replication into a portfolio of options

## Inputs To Gather

- **Underlying specification**: ticker, asset class, currency, current spot price S₀
- **Contract terms**: notional (vega notional or variance notional), swap tenor, observation frequency (daily, weekly), annualization factor (typically 252 for equities), business day convention
- **Options market data**: full implied volatility surface (strikes and expiries), or at minimum a strip of OTM put and call prices spanning the replication range
- **Interest rates**: risk-free rate curve (OIS or SOFR) matching swap tenor [VERIFY: confirm curve convention with counterparty]
- **Dividend assumptions**: discrete dividend schedule or continuous dividend yield for the underlying
- **Realized vol data** (for MTM): historical daily log returns from swap inception to valuation date
- **Corridor/cap details** (if applicable): strike boundaries for capped variance swaps or corridor variance swaps

## Workflow

1. **Build the replication strip**
   - Collect OTM put prices for strikes K < F (forward price) and OTM call prices for K > F
   - Set the cutoff strike (typically the forward price or nearest listed strike); assign each option to the put or call wing
   - Weight each option by 1/K² to construct the portfolio that replicates the variance swap payoff per the Demeterfi-Derman-Kamal-Zou (DDKZ) methodology
   - Integrate numerically: Kvar² = (2/T) × [∫₀ᶠ (1/K²) P(K) dK + ∫ᶠ∞ (1/K²) C(K) dK], using trapezoidal or Simpson's rule across the discrete strike grid

2. **Apply discrete monitoring correction**
   - Continuous-monitoring fair strike overstates the discrete case; apply the correction factor: Kvar²(discrete) ≈ Kvar²(continuous) − (μ₃ / n) + O(1/n²), where n = number of observations and μ₃ captures the third moment of log returns [VERIFY: confirm observation count and whether overnight/holiday returns are included or excluded per term sheet]

3. **Derive volatility swap strike via convexity adjustment**
   - Kvol ≈ Kvar − (σ² of σ) / (2 × Kvar), where (σ² of σ) represents the variance of realized volatility (vol-of-vol)
   - Estimate vol-of-vol from historical data or calibrate from VIX-of-VIX / implied vol-of-vol surfaces if available
   - The convexity adjustment is always negative: Kvol < Kvar; typical magnitude is 0.5–2.0 vol points for equity indices

4. **Price capped or corridor variants (if applicable)**
   - Capped variance swap: cap the realized variance at Kvar² × (cap multiplier, often 2.5×); reprice by truncating the replication strip at the corresponding implied vol level
   - Corridor variance swap: only accrue variance when spot is within [L, U]; decompose into a combination of standard variance swaps and barrier-contingent variance legs

5. **Mark-to-market an existing position**
   - Decompose remaining value into: (a) accrued realized variance from inception to now, and (b) implied variance for remaining period from current options strip
   - Weighted-average formula: Kvar²(MTM) = (t/T) × σ²(realized) + ((T−t)/T) × σ²(implied, remaining)
   - PnL = variance notional × (Kvar²(MTM) − Kvar²(strike))
   - For vega-notional contracts, convert: variance notional = vega notional / (2 × Kvar(strike))

6. **Run sensitivity analysis**
   - Vega: sensitivity to parallel shift in the vol surface
   - Volga/vomma: second-order sensitivity (drives the variance-vs-volatility swap spread)
   - Skew sensitivity: impact of steepening/flattening the put wing on fair strike
   - Spot dependence: dollar gamma profile, particularly relevant for single-stock variance swaps with jump risk
   - Truncation risk: sensitivity of fair strike to the range of strikes included in the replication strip (wing extrapolation)

## Output

- **Fair strike table**: Kvar (variance strike in vol² terms), Kvar in vol terms (√Kvar²), and Kvol (volatility swap strike after convexity adjustment)
- **Replication portfolio**: list of option strikes, types (put/call), weights (1/K²), and notional amounts required to statically replicate the variance swap
- **Discrete monitoring adjustment**: magnitude and direction of the correction applied
- **Convexity adjustment breakdown**: vol-of-vol estimate used, adjustment magnitude, and resulting Kvol
- **MTM valuation** (if applicable): accrued realized variance, forward implied variance, blended variance, and PnL in dollar terms
- **Sensitivity dashboard**: vega, volga, skew sensitivity, and truncation risk metrics
- **Assumptions log**: annualization convention, observation frequency, dividend treatment, wing extrapolation method, and any overrides applied

## Quality Checks

- Confirm Kvar from replication matches the VIX-style calculation for the same tenor to within rounding tolerance (equity index case)
- Verify Kvol < Kvar; flag if the convexity adjustment exceeds 3 vol points (unusual outside EM or single stocks)
- Check that the replication strip spans at least 2–3 standard deviations on each wing; if truncated, note the estimated bias from missing tails
- Cross-check discrete monitoring correction direction: discrete fair strike should be lower than continuous for variance swaps
- Validate MTM PnL sign against intuition: if realized vol has exceeded the strike, long position should show positive MTM
- Ensure notional conversion between vega notional and variance notional is consistent throughout
- [VERIFY] Confirm day-count and annualization conventions match the ISDA variance swap confirmation or term sheet
- [VERIFY] Confirm whether the contract uses log returns or simple returns for realized variance calculation (nearly all use log returns, but verify)
