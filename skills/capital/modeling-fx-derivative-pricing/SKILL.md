---
name: modeling-fx-derivative-pricing
language: en
description: Prices FX options and exotic structures with Garman-Kohlhagen, local volatility, and stochastic volatility models. Use when pricing FX derivatives, evaluating FX options, or modeling cross-currency products.
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
# Modeling FX Derivative Pricing

Prices FX options and exotic structures using Garman-Kohlhagen, local volatility, and stochastic volatility frameworks. Covers vanilla European/American FX options, barrier options, digital options, and cross-currency swaps.

## When To Use

- Pricing vanilla FX calls/puts (European or American exercise) on spot or forward
- Valuing exotic FX structures: barriers (knock-in/knock-out), digitals, range accruals, quanto options
- Marking an FX options book to market or generating independent price verification (IPV)
- Evaluating hedge costs for corporate treasury FX exposures
- Structuring cross-currency basis swaps or dual-currency notes
- Stress-testing FX derivative portfolios under volatility surface shifts

## Inputs To Gather

- **Currency pair and notional**: e.g., EUR/USD, 10M EUR notional; confirm quoting convention (domestic/foreign)
- **Spot rate**: current mid-market spot from a reliable source (Bloomberg, Reuters, central bank fix)
- **Interest rates**: domestic and foreign risk-free rates matching the option tenor; use OIS or deposit rates as appropriate [VERIFY: confirm curve source and day-count convention per currency]
- **Volatility data**: at-the-money implied vol at minimum; for exotics, the full vol surface (delta or strike pillars × tenors), smile/skew parameters, or calibrated model parameters
- **Option terms**: strike, expiry date, cut time (NY 10am or Tokyo 3pm), settlement convention (cash or physical), premium currency
- **Exotic features** (if applicable): barrier levels and monitoring frequency (continuous vs. discrete), rebate amounts, averaging dates, correlation inputs for quanto/basket
- **Model choice justification**: Garman-Kohlhagen for vanilla European; local vol (Dupire) for barrier/digital sensitivity to skew; stochastic vol (Heston, SABR) for smile dynamics and vega hedging

## Workflow

1. **Select the pricing model**
   - Vanilla European FX option → Garman-Kohlhagen (modified Black-Scholes with foreign rate as continuous dividend yield)
   - Barrier, digital, or path-dependent → local volatility surface calibrated via Dupire's formula; verify fit to market smile at relevant strikes
   - Products sensitive to vol-of-vol or forward smile → stochastic volatility (Heston or SABR); calibrate to market-quoted vols across strikes and tenors
   - American exercise → use finite-difference or binomial lattice with early-exercise boundary

2. **Calibrate model inputs**
   - Build or import the implied volatility surface; interpolate via SVI, SABR, or cubic spline
   - Verify put-call parity holds across the surface (arbitrage-free check)
   - For local vol: invert the Dupire equation numerically; check that local vol values are positive and smooth
   - For Heston: fit parameters (v₀, κ, θ, σ_v, ρ) to market vols using least-squares or differential evolution; report calibration error per strike/tenor

3. **Price the derivative**
   - Compute closed-form price (Garman-Kohlhagen) or run Monte Carlo / PDE solver
   - For Monte Carlo: specify number of paths (≥100k for vanillas, ≥500k for barriers), time steps, and variance reduction technique (antithetic, control variate)
   - Report price in both premium currencies (e.g., USD pips and % of notional)

4. **Compute Greeks and risk sensitivities**
   - Delta (spot and forward), gamma, vega (parallel and pillar), theta, rho (domestic and foreign)
   - For barriers: report pin risk near barrier, vanna, volga
   - Express Greeks in standard market conventions (e.g., delta as % of foreign notional)

5. **Run scenario and sensitivity analysis**
   - Spot bump: ±1%, ±5%, ±10%
   - Vol bump: ±1 vol point parallel shift; ±25-delta risk reversal shift
   - Rate bump: ±25 bps domestic and foreign independently
   - Time decay: price at T−1d, T−1w, T−1m
   - For barriers: sensitivity to barrier monitoring frequency (continuous vs. daily)

6. **Document and deliver**
   - State model choice and rationale
   - List all inputs with sources and value dates
   - Present pricing results in a summary table
   - Attach Greeks and scenario grids
   - Flag any inputs that were assumed or interpolated with [VERIFY]

## Output

- **Pricing summary table**: option terms, model used, theoretical price (bid/mid/ask if spread is modeled), premium in both currencies
- **Greeks table**: delta, gamma, vega, theta, rho per leg or per option
- **Volatility surface snapshot**: implied vol at key pillars; local vol or Heston parameter set if used
- **Scenario matrix**: P&L impact across spot/vol/rate shifts
- **Calibration diagnostics** (for local/stochastic vol): calibration error by strike/tenor, parameter stability notes
- **Assumptions and limitations log**: model limitations (e.g., constant correlation assumption, no jumps), data staleness, interpolation choices

## Quality Checks

- Verify put-call parity: C − P = e^(−r_f T) S − e^(−r_d T) K; flag deviations > 0.5 bps of notional
- Confirm Greeks sum correctly for structured packages (e.g., risk reversal delta = call delta + put delta)
- Cross-check vanilla prices against Garman-Kohlhagen closed-form even when using Monte Carlo or PDE methods
- Ensure barrier option prices converge as barrier moves far from spot to the corresponding vanilla price
- Validate that digital option prices equal the negative of the derivative of the vanilla price with respect to strike (call spread approximation)
- Check that local vol surface produces no negative variances or calendar spread arbitrage
- [VERIFY] Interest rate day-count conventions match market standard for each currency (ACT/360 for USD, ACT/365 for GBP, etc.)
- [VERIFY] Vol surface source date matches trade date; stale vol data invalidates pricing
- [VERIFY] Settlement convention (T+2 for most G10 pairs; exceptions for CAD, TRY, RUB)
