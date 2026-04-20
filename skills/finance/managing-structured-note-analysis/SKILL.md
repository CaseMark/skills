---
name: managing-structured-note-analysis
language: en
description: Structures structured note evaluation with payoff analysis, embedded option decomposition, and fair value assessment. Use when analyzing structured notes, decomposing embedded options, or evaluating note pricing.
tags:
  - management
  - quantitative-finance
  - valuation
metadata:
  author: casemark
  practice_areas:
    - Derivatives
    - Quantitative Analysis
    - Structured Products
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Structured Note Analysis

Coordinates the end-to-end evaluation of structured notes by decomposing embedded derivatives, modeling payoff profiles, and assessing fair value relative to issuer pricing. Manages the analytical workflow across quantitative teams, risk functions, and portfolio managers.

## When To Use

- Evaluating a new structured note offering (reverse convertible, autocallable, principal-protected note, range accrual, etc.) before purchase or recommendation
- Decomposing an existing note into its component parts (bond floor + embedded option) for mark-to-market or risk reporting
- Comparing issuer indicative pricing against independent fair value estimates
- Assessing whether a note's fee-adjusted return profile is appropriate for the target investor or portfolio mandate
- Reviewing structured note inventory for ongoing suitability, concentration, or credit exposure

## Inputs To Gather

- **Term sheet or offering document** — coupon structure, maturity, barrier levels, participation rates, underlying reference(s), call schedule
- **Issuer details** — credit rating, CDS spread, issuer funding curve
- **Underlier data** — current spot price, dividend yield, historical and implied volatility surface, correlation matrix (for multi-asset notes)
- **Market rates** — risk-free yield curve, swap curve, relevant discount factors for the note's tenor
- **Investor context** — risk tolerance, yield target, holding period, tax status, existing portfolio exposures
- **Comparable notes** — similar structures from competing issuers for relative value benchmarking

## Workflow

1. **Classify the note structure**
   - Identify the note type: principal-protected, yield enhancement (reverse convertible, autocallable), participation/leverage, or hybrid
   - Map the payoff formula and list all contingent features (barriers, caps, floors, memory coupons, call triggers)
   - Identify the underlying reference asset(s) and any basket/worst-of mechanics

2. **Decompose into component instruments**
   - Separate the bond component (zero-coupon or coupon-bearing) from the embedded derivative(s)
   - Characterize each embedded option: type (put, call, digital, barrier), exercise style (European, American, Bermudan), and knock-in/knock-out features
   - For autocallables, map the discrete observation schedule and corresponding payoffs at each call date

3. **Value the bond floor**
   - Discount promised cash flows using the issuer's credit-adjusted curve (swap curve + issuer CDS spread)
   - Calculate the issuer credit charge — the difference between risk-free and credit-adjusted present values
   - Flag any subordination or bail-in risk that may not be captured by senior CDS spreads [VERIFY]

4. **Price the embedded derivatives**
   - Select an appropriate pricing model: Black-Scholes for vanilla European options, Monte Carlo simulation for path-dependent or multi-asset structures, finite difference methods for early-exercise features
   - Calibrate to the relevant volatility surface (use implied vols at the barrier/strike levels, not ATM)
   - For multi-asset notes, estimate and stress-test correlation assumptions using historical data and implied correlation where available
   - Run pricing under base case and at least two stress scenarios (vol shift ±5 pts, correlation shift ±0.15)

5. **Assess fair value and fee extraction**
   - Sum bond floor + embedded derivative value to derive independent fair value
   - Compare against the issuer's offer price (typically par = 100)
   - Calculate the implied fee (issuer markup) as: `Fee = Offer Price − Fair Value`
   - Benchmark the implied fee against market norms for the structure type (typically 1–3% for simple notes, 3–7% for complex autocallables) [VERIFY]

6. **Analyze risk and scenario outcomes**
   - Generate a payoff diagram across the full range of underlier outcomes at maturity
   - Calculate key risk metrics: delta, vega, credit DV01, and barrier distance (current spot vs. barrier as % of spot)
   - Model worst-case, base-case, and best-case return scenarios with assigned probability estimates
   - For autocallables, compute the probability-weighted average life and expected return across all call paths

7. **Compile findings and coordinate review**
   - Prepare a structured analysis report with clear buy/pass/conditional recommendation
   - Route to risk management for independent model validation on notes above a defined notional threshold [VERIFY — firm-specific threshold]
   - Escalate notes with implied fees outside acceptable ranges or with issuer credit concerns
   - Track the note through approval, execution, and post-trade booking confirmation

## Output

The deliverable is a **Structured Note Analysis Report** containing:

- **Executive summary** — note type, underlier, tenor, indicative coupon/participation, and recommendation
- **Structure diagram** — visual payoff at maturity with barrier, cap, and participation zones labeled
- **Component decomposition table** — bond floor value, embedded option value, issuer credit charge, and implied fee, each as a dollar amount and percentage of par
- **Scenario matrix** — return outcomes at maturity under 5+ underlier price scenarios (e.g., −40%, −20%, 0%, +20%, +40%)
- **Risk metrics summary** — delta, vega, barrier distance, credit DV01, probability-weighted expected return
- **Comparable analysis** — fee and payoff comparison against 2–3 similar notes from other issuers
- **Recommendation with conditions** — suitability assessment, position sizing guidance, and any hedging considerations

## Quality Checks

- Bond floor valuation uses issuer-specific credit spread, not generic investment-grade curves
- Embedded option pricing model is appropriate for the payoff's path dependency and dimensionality
- Volatility inputs are sourced from the correct strike/tenor point on the surface, not defaulted to ATM
- Correlation assumptions for multi-asset notes are stress-tested and documented
- Implied fee calculation is transparent and benchmarked against comparable structures
- Payoff diagram matches the term sheet formula — verify with at least three manual spot-price test cases
- All barrier levels, observation dates, and day-count conventions match the term sheet exactly
- Credit risk of the issuer is independently assessed and not solely reliant on rating agency opinions
- Report flags any liquidity constraints (secondary market bid-ask, early redemption penalties)
- Recommendations account for the investor's existing portfolio exposures to avoid concentration risk
