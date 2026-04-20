---
name: pricing-credit-derivatives
language: en
description: Structures credit derivative pricing with hazard rate calibration and default probability estimation. Use when pricing CDS, calculating credit spreads, or modeling default risk.
tags:
  - valuation
  - quantitative-finance
  - risk
  - credit
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
# Pricing Credit Derivatives

## When To Use

- Pricing single-name or index CDS contracts (standard or bespoke tenors)
- Bootstrapping hazard rates from quoted CDS spreads to build a term structure of default probabilities
- Calculating fair-value credit spreads for bonds, loans, or structured tranches relative to CDS-implied levels
- Marking credit derivative books to market or to model for P&L and risk reporting
- Modeling default and recovery scenarios for CVA/DVA adjustments on counterparty exposures
- Pricing credit-linked notes (CLNs), total return swaps (TRS), or nth-to-default baskets

## Inputs To Gather

- **Reference entity and obligation**: Legal name, RED code, reference obligation ISIN, seniority (senior unsecured, subordinated, secured), restructuring clause type (CR, MR, MM, XR) [VERIFY jurisdiction-specific ISDA definitions apply]
- **Market CDS spreads**: Par spreads or upfront quotes across standard tenors (6M, 1Y, 2Y, 3Y, 5Y, 7Y, 10Y); source (Markit, Bloomberg CDSW, dealer runs) and snapshot date
- **Recovery rate assumption**: Market-standard (typically 40% for senior unsecured corporates, 25% for subordinated, 20–25% for sovereigns) or entity-specific recovery from auction history [VERIFY against current ISDA credit event auction results]
- **Risk-free discount curve**: OIS or SOFR swap curve (post-LIBOR transition); specify curve date, source, and interpolation method [VERIFY which benchmark is contractually specified]
- **Contract terms**: Notional, trade date, effective date, maturity, coupon (running spread for legacy or standard 100/500 bps), payment frequency (quarterly), day count (ACT/360), business day convention
- **Correlation parameters** (for basket/tranche products): Base correlation surface or compound correlation by tranche attachment/detachment points

## Workflow

1. **Build the discount curve**
   - Strip OIS/SOFR swap rates to derive zero-coupon discount factors
   - Interpolate using log-linear on discount factors or monotone convex on zero rates
   - Confirm curve date aligns with CDS quote date (T+1 settlement convention for standard CDS)

2. **Bootstrap the hazard rate curve**
   - Start from the shortest tenor CDS spread; assume piecewise-constant hazard rates between standard tenors
   - For each tenor, solve for the hazard rate λ that equates the present value of the premium leg to the protection leg:
     - Premium leg PV = Σ (spread × Δt × DF(tᵢ) × Survival(tᵢ))  including accrued-on-default
     - Protection leg PV = Σ ((1 − R) × DF(tᵢ) × [Survival(tᵢ₋₁) − Survival(tᵢ)])
   - Survival probability: S(t) = exp(−∫₀ᵗ λ(s) ds)
   - Include accrual-on-default adjustment (integral of accrued premium over the payment period weighted by default probability)

3. **Price the target instrument**
   - **Single-name CDS**: Compute mark-to-market as the difference between protection leg PV and premium leg PV at the contract's running coupon; convert to upfront amount using ISDA Standard Model conventions
   - **CDS index**: Price as portfolio of single-name CDS with intrinsic/index basis adjustment; account for defaulted names (fixed recovery payment at settlement)
   - **Credit-linked note**: Bond-equivalent pricing = risk-free bond PV minus protection leg PV funded by note proceeds
   - **Nth-to-default basket**: Require correlation modeling; use Gaussian copula or Student-t copula to simulate joint defaults; compute expected loss on nth default
   - **Synthetic CDO tranche**: Apply base correlation framework—interpolate base correlations for attachment and detachment points; tranche expected loss = base EL(detachment) − base EL(attachment)

4. **Compute risk sensitivities**
   - **CS01 (Credit Spread 01)**: Bump each CDS spread by 1 bp, re-bootstrap, and re-price; report per-tenor and parallel CS01
   - **CR01 (Recovery 01)**: Shift recovery assumption by 1% and re-price
   - **IR01**: Bump discount curve by 1 bp to isolate interest rate sensitivity
   - **Jump-to-default (JTD)**: Compute loss on instantaneous default at assumed recovery vs. current MTM
   - **Theta/carry**: Estimate daily P&L from premium accrual and curve roll-down

5. **Cross-validate results**
   - Compare model price to Bloomberg CDSW, Markit CDS Calculator, or QuantLib output
   - Check that bootstrapped survival probabilities are monotonically decreasing and bounded in [0, 1]
   - Verify upfront vs. running spread conversion matches ISDA Standard Model (using standard 3% flat hazard rate for IMM date accruals) [VERIFY ISDA Standard Model version in use]
   - For indices, confirm model-implied index spread vs. quoted spread falls within expected basis range

## Output

- **Pricing summary table**: Fair value (upfront amount or PV), par spread, running spread + upfront, accrued premium, clean vs. dirty price
- **Hazard rate term structure**: Bootstrapped piecewise-constant hazard rates by tenor, with corresponding cumulative default probabilities and survival probabilities
- **Risk report**: CS01 (per-tenor and parallel), CR01, IR01, JTD exposure, theta/carry
- **Methodology statement**: Model used (ISDA Standard Model, reduced-form intensity, copula), recovery assumption, discount curve specification, interpolation method, and any deviations from standard conventions
- **Sensitivity analysis**: Price impact across a range of spread levels (±50, ±100 bps) and recovery assumptions (20%, 30%, 40%, 50%)

## Quality Checks

- Hazard rates must be non-negative; flag any negative implied hazard rates as indicative of curve fitting issues or stale quotes
- Premium leg PV + upfront payment should equal protection leg PV at fair value (no-arbitrage check)
- Par spread computed from bootstrapped curve should reproduce input market spreads within ±0.1 bps (round-trip consistency)
- For standard ISDA CDS contracts, upfront amount must reflect the correct standard coupon (100 or 500 bps) and settlement conventions [VERIFY Big Bang/Small Bang protocol applicability by region]
- Confirm day count (ACT/360), payment frequency (quarterly on IMM dates), and business day conventions match contract terms
- Recovery rate should be consistent between bootstrapping and pricing—mixing assumptions introduces arbitrage
- For tranche pricing, verify that base correlations are monotonically increasing with detachment point; non-monotonicity signals interpolation or data issues
