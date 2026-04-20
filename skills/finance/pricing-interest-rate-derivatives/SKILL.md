---
name: pricing-interest-rate-derivatives
language: en
description: Structures interest rate swap, cap, floor, and swaption pricing with curve construction and valuation. Use when pricing IR derivatives, building yield curves, or valuing swap portfolios.
tags:
  - valuation
  - quantitative-finance
  - portfolio
metadata:
  author: casemark
  practice_areas:
    - Derivatives
    - Quantitative Analysis
    - Structured Products
  document_types:
    - Valuation Report
  skill_modes:
    - Valuation
    - Calculation
---
# Pricing Interest Rate Derivatives

Structures interest rate swap, cap, floor, and swaption pricing with yield curve construction, discounting frameworks, and volatility modeling.

## When To Use

- Pricing a new or existing interest rate swap (fixed-for-floating, basis, cross-currency)
- Valuing interest rate caps, floors, or collars for hedging or portfolio marking
- Pricing European or Bermudan swaptions for risk management or trade structuring
- Constructing or auditing discount and forward curves from market instruments
- Marking a swap portfolio to market or computing CVA/DVA adjustments
- Sensitivity analysis (DV01, gamma, vega) for IR derivative positions

## Inputs To Gather

- **Trade terms**: Notional, effective/maturity dates, fixed rate, floating index (SOFR, EURIBOR, TONA, etc.), payment frequency, day count conventions (ACT/360, 30/360, ACT/365), reset lag, compounding method [VERIFY: confirm index and convention per jurisdiction]
- **Market data as of valuation date**:
  - Overnight/term rate fixings (e.g., SOFR, Fed Funds)
  - Deposit rates, futures prices (SOFR 1M/3M futures), and par swap rates across tenors
  - OIS discount curve instruments (if separate from projection curve)
  - Cap/floor implied volatility surface (strike × tenor) or swaption vol cube (expiry × tenor × strike) — normal (bp) vs. lognormal convention [VERIFY]
- **Collateral/CSA terms**: Collateral currency, interest on collateral rate, threshold and MTA — these determine the discount curve selection
- **Valuation context**: Mid-market vs. exit price, regulatory framework (e.g., IFRS 13 fair value hierarchy), purpose (trade pricing, portfolio MTM, hedge effectiveness)

## Workflow

1. **Curve Construction**
   - Select bootstrapping instruments: deposits (O/N to 6M), futures (front 8–12 contracts), and par swap rates (2Y–50Y)
   - Build the OIS discount curve first (stripped from OIS swap rates)
   - Build the forward projection curve for the relevant index (e.g., 3M SOFR) using the multi-curve framework — discount on OIS, project on the index curve
   - Interpolation: use monotone convex or log-linear on discount factors; cubic spline on zero rates for smoothness [VERIFY: confirm firm/system interpolation convention]
   - Validate: reprice input instruments to within 0.01 bp; check forward rates are positive and smooth

2. **Swap Pricing**
   - Generate fixed and floating leg cash flow schedules respecting business day conventions (Modified Following, etc.), holiday calendars [VERIFY: confirm applicable calendar], and stub periods
   - For the floating leg, compute forward rates from the projection curve for each accrual period; apply compounding-in-arrears or averaging if applicable (e.g., SOFR compounded daily)
   - Discount each cash flow using the OIS curve discount factor to the payment date
   - NPV = PV(floating leg) − PV(fixed leg) from the receiver's perspective
   - Par swap rate = rate that sets NPV to zero; solve via annuity factor: Par Rate = (DF_start − DF_end) / Annuity

3. **Cap/Floor Pricing**
   - Decompose cap (floor) into a strip of caplets (floorlets), one per reset period
   - Price each caplet using Black's model (lognormal) or Bachelier's model (normal vol) — confirm market convention [VERIFY: post-LIBOR markets predominantly use normal vol]
   - Caplet PV = DF × τ × [F·N(d1) − K·N(d2)] (Black) or the normal-model equivalent
   - Sum caplet PVs; cross-check via put-call parity: Cap − Floor = Swap (at same strike/tenor)

4. **Swaption Pricing**
   - European swaption: use Black's model on the forward swap rate with the appropriate annuity as numéraire
   - Inputs: forward swap rate, strike, swaption vol (from vol cube), time to expiry, annuity factor
   - For Bermudan swaptions, use a short-rate model (Hull-White 1F) or LGM calibrated to co-terminal European swaptions; value via backward induction on a lattice or Monte Carlo with Longstaff-Schwartz
   - Payer swaption PV = Annuity × [F·N(d1) − K·N(d2)] (Black); receiver via put-call parity

5. **Risk Sensitivities**
   - DV01 / PV01: bump each input rate by 1 bp, revalue, compute finite-difference delta per tenor bucket
   - Gamma: second-order bump (±1 bp) for convexity
   - Vega: bump vol surface by 1 bp (normal) or 1% relative (lognormal), revalue caps/swaptions
   - Cross-gamma and correlation sensitivities for basis or cross-currency structures
   - Report key-rate durations and total portfolio DV01

## Output

- **Valuation Summary**: NPV, par rate or premium, accrued interest, clean vs. dirty price
- **Curve Data**: Discount factors, zero rates, and forward rates at standard tenors; plot forward curve
- **Cash Flow Schedule**: Date, notional, rate, accrual fraction, cash flow amount, discount factor, PV per period
- **Greeks Table**: DV01 by tenor bucket, gamma, vega (by expiry/tenor), theta
- **Methodology Notes**: Models used, interpolation method, vol convention (normal/lognormal), day count, calendar, data sources with timestamps
- **Sensitivity Scenarios**: Parallel shift ±25/50/100 bp, curve steepener/flattener, vol shock

## Quality Checks

- Reprice all bootstrapping instruments — residual < 0.01 bp
- Verify cap-floor-swap parity holds within bid-ask tolerance
- Confirm put-call parity for swaptions at the same strike
- Check that forward rates are continuous and non-negative (flag inversions)
- Cross-validate NPV against an independent system or dealer quote where available
- Validate DV01 direction and magnitude: a 10Y receiver swap ~7–9 bp/bp notional is a reasonable sanity check
- Confirm CSA-consistent discounting — using the wrong discount curve is a common and material error
- Ensure day count and business day convention consistency between legs and across the curve build
- Flag any market data staleness (timestamps older than T−1) with [VERIFY]
