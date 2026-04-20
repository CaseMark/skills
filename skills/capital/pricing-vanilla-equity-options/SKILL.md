---
name: pricing-vanilla-equity-options
language: en
description: Calculates option values with Black-Scholes, binomial, and Monte Carlo methods including Greeks sensitivity analysis. Use when pricing equity options, calculating Greeks, or evaluating option strategies.
tags:
  - valuation
  - derivatives-and-structured-products
metadata:
  author: casemark
  practice_areas:
    - Derivatives
    - Structured Products
    - Hedging
  document_types:
    - Valuation Report
  skill_modes:
    - Valuation
    - Calculation
---
# Pricing Vanilla Equity Options

## When To Use

- Pricing European or American calls/puts on single-name equities or equity indices
- Computing Greeks (delta, gamma, vega, theta, rho) for hedging or risk reporting
- Comparing theoretical fair value against quoted market prices to identify mispricings
- Evaluating simple option strategies (spreads, straddles, covered calls) at inception
- Generating sensitivity tables for trade approval memos or client-facing valuation reports

## Inputs To Gather

| Input | Description | Source Notes |
|---|---|---|
| **Spot price (S)** | Current underlying equity price | Live market feed or last close |
| **Strike price (K)** | Contract strike | Term sheet or exchange listing |
| **Time to expiry (T)** | Years (or fraction) to expiration date | Contract terms; use ACT/365 unless specified |
| **Risk-free rate (r)** | Continuously compounded rate matching tenor | Treasury yield curve or OIS rate [VERIFY tenor match] |
| **Dividend yield / schedule (q)** | Continuous yield or discrete dividend dates and amounts | Bloomberg/Refinitiv; confirm ex-dates [VERIFY] |
| **Volatility (σ)** | Implied vol from market, or historical/realized vol | Volatility surface, ATM quote, or historical window |
| **Option type** | Call or put | Contract terms |
| **Exercise style** | European or American | Contract terms — drives model choice |

## Workflow

### 1. Validate and Normalize Inputs

- Confirm spot, strike, and expiry are internally consistent (no expired contracts, no negative values).
- Convert discrete dividends to a continuous yield if using Black-Scholes, or keep discrete for binomial/Monte Carlo.
- Select the volatility input: implied vol (preferred for mark-to-market) vs. historical vol (fallback or scenario analysis). Note which is used.
- Match the risk-free rate tenor to option expiry. Interpolate the yield curve if an exact tenor is unavailable. [VERIFY rate convention: continuous vs. simple]

### 2. Select Pricing Model

- **Black-Scholes (closed-form):** Default for European options with continuous dividend yield. Fast and analytically tractable. Not suitable for American puts with early exercise value or discrete dividends of material size.
- **Binomial tree (CRR or Leisen-Reimer):** Use for American options or when discrete dividends must be modeled explicitly. Choose ≥200 steps for convergence; confirm convergence by doubling steps and checking price stability (tolerance < 0.01).
- **Monte Carlo simulation:** Use when payoff is path-dependent or when extending to multi-asset baskets. For vanilla options it serves as a cross-check. Use ≥100,000 paths with antithetic variates and report standard error.

### 3. Calculate Option Value and Greeks

- Compute the theoretical price under the chosen model.
- Calculate first-order Greeks: **Delta (Δ), Gamma (Γ), Vega (ν), Theta (Θ), Rho (ρ)**.
- For Black-Scholes, use closed-form Greek formulas. For tree/MC models, use finite-difference bumps:
  - Delta: bump spot ±0.5%; Gamma: second-order from same bumps; Vega: bump vol ±1 vol point; Rho: bump rate ±10 bps.
- Compute **implied volatility** if a market price is provided (Newton-Raphson or Brent's method on Black-Scholes).

### 4. Cross-Check and Validate

- **Put-call parity:** For Europeans, verify C − P = S·e^(−qT) − K·e^(−rT) within a tolerance of ±0.01.
- **Boundary conditions:** Option price ≥ intrinsic value; call ≤ S; put ≤ K·e^(−rT).
- **Early exercise premium:** For American options, confirm price ≥ European equivalent.
- **Greeks sign checks:** Delta in [0,1] for calls, [−1,0] for puts; gamma ≥ 0; vega ≥ 0; theta typically ≤ 0 for long options.
- If two models are run, compare prices and flag divergences > 1%.

### 5. Build Sensitivity Analysis

- Generate a **spot vs. vol matrix** showing option price across ±10–20% spot moves and ±5 vol point shifts.
- Produce a **time decay profile** showing theta bleed at weekly intervals to expiry.
- If relevant, show **dividend sensitivity** — price impact of ±10% change in dividend assumption.

## Output

Structure the deliverable as follows:

1. **Summary table** — Option type, spot, strike, expiry, vol, rate, dividend assumption, model used, theoretical price.
2. **Greeks table** — Delta, gamma, vega (per 1 vol point), theta (per day), rho (per 100 bps).
3. **Sensitivity matrix** — Spot × vol grid of prices (and optionally delta).
4. **Model notes** — Which model was used, number of steps/paths, convergence checks, and any assumptions or approximations.
5. **Flags** — Mark any [VERIFY] items, data staleness warnings, or cases where early exercise premium is significant.

## Quality Checks

- [ ] Put-call parity holds within tolerance for European options
- [ ] All Greeks pass sign and magnitude reasonableness checks
- [ ] Binomial tree convergence confirmed (step-doubling test)
- [ ] Volatility source clearly labeled (implied vs. historical, tenor, date)
- [ ] Risk-free rate tenor matches option expiry; interpolation method noted if used
- [ ] Dividend treatment documented (continuous yield vs. discrete schedule) [VERIFY ex-dates]
- [ ] Sensitivity tables cover a meaningful range of scenarios
- [ ] No stale market data — spot, vol, and rate quotes dated within one business day unless noted
