---
name: analyzing-structured-note-payoffs
language: en
description: Deconstructs structured note payoffs with embedded option identification, issuer credit risk, and all-in cost analysis. Use when analyzing structured notes, evaluating embedded options, or assessing structured product costs.
tags:
  - analysis
  - derivatives-and-structured-products
  - risk
  - credit
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
# Analyzing Structured Note Payoffs

Deconstructs structured note payoffs with embedded option identification, issuer credit risk, and all-in cost analysis.

## When To Use

- Evaluating a structured note term sheet or offering document before purchase
- Reverse-engineering the payoff profile to identify embedded derivatives
- Comparing all-in cost of a structured note against replicating the position with vanilla instruments
- Assessing issuer credit risk embedded in unsecured note obligations
- Reviewing suitability of a structured product for a portfolio or hedging program

## Inputs To Gather

- **Term sheet or offering supplement** — maturity, coupon structure, underlier(s), barrier levels, participation rates, caps/floors
- **Underlier data** — current spot price, dividend yield, historical and implied volatility for relevant tenors
- **Issuer credit profile** — CDS spread or credit rating, senior unsecured spread curve
- **Risk-free rate curve** — swap or Treasury curve matching the note's currency and tenor
- **Comparable vanilla pricing** — broker quotes or model prices for the component options (calls, puts, digital options, knock-in/knock-out barriers)
- **Fee disclosures** — stated issuance fees, placement agent commissions, estimated hedging costs if available

## Workflow

1. **Map the payoff formula.** Parse the term sheet to express the note's return as a piecewise function of the underlier at maturity (and at observation dates for autocallables or barrier-monitoring notes). Identify all scenarios: full principal return, enhanced upside, partial protection, full loss.

2. **Decompose into component instruments.** Break the payoff into a combination of:
   - Zero-coupon bond (issuer credit)
   - Long/short vanilla calls or puts at stated strikes
   - Digital (binary) options for fixed coupon triggers
   - Barrier options (knock-in puts, knock-out calls) with specified levels
   - Worst-of or basket features if multi-underlier

3. **Price each component independently.**
   - Value the bond component by discounting at the issuer's credit spread over the risk-free curve
   - Price option components using Black-Scholes, local volatility, or Monte Carlo as appropriate for the payoff complexity
   - For barrier and autocall features, use Monte Carlo with correlation assumptions for multi-asset notes [VERIFY correlation inputs against market data]
   - Sum component values to derive a theoretical fair value for the note

4. **Calculate the all-in cost.**
   - Compare fair value to par (issue price): the difference represents the total embedded cost to the investor
   - Express as annualized cost drag (bps/year) over the note's expected life
   - Decompose cost into identifiable buckets: issuer funding advantage, option premium markup, placement fees

5. **Assess issuer credit risk.**
   - Quantify the credit spread component — how much yield is the investor forgoing by holding unsecured issuer paper vs. a risk-free instrument
   - Evaluate whether the note's coupon or enhanced return adequately compensates for issuer default risk
   - Flag if issuer CDS spread has moved materially since issuance [VERIFY current CDS levels]

6. **Scenario and sensitivity analysis.**
   - Run payoff under spot moves of -30%, -15%, flat, +15%, +30% at maturity
   - Test sensitivity to implied volatility shifts (+/- 5 vol points)
   - For autocallables, model probability of early call at each observation date
   - For worst-of notes, stress correlation assumptions (e.g., correlation drops from 0.7 to 0.3)

7. **Compare to replication portfolio.** Estimate the cost of replicating the note's payoff using exchange-traded or OTC options plus a money-market position. If replication is cheaper, quantify the savings.

## Output

Structure the analysis report with these sections:

- **Note Summary** — issuer, maturity, underlier(s), key terms (barrier, participation rate, cap, coupon)
- **Payoff Diagram** — describe or tabulate the piecewise payoff across underlier price ranges
- **Embedded Option Decomposition** — table listing each component, notional, strike/barrier, and individual fair value
- **Fair Value vs. Issue Price** — total note fair value, cost to investor in dollar and annualized basis-point terms
- **Issuer Credit Assessment** — credit spread, implied default probability over note tenor, rating
- **Scenario Table** — payoff under each scenario with probability-weighted expected return
- **Replication Comparison** — cost and feasibility of replicating via vanilla instruments
- **Key Risks** — maximum loss scenario, barrier proximity, correlation risk, early call risk, liquidity risk (secondary market)

## Quality Checks

- Verify the sum of decomposed component values approximates the issue price (residual = embedded cost); flag if residual exceeds 5% of notional without explanation
- Confirm barrier levels and strike prices match the term sheet exactly — transcription errors here invalidate the entire analysis
- Ensure the discount rate used for the bond component reflects the issuer's actual credit curve, not a generic spread [VERIFY]
- For multi-underlier notes, confirm correlation assumptions are sourced from market data, not assumed
- Check that scenario analysis covers the maximum-loss case (e.g., underlier drops below knock-in barrier)
- Validate that annualized cost calculation uses the correct day count convention and expected life (not stated maturity for autocallables) [VERIFY day count convention per term sheet]
- Flag any terms that create asymmetric issuer optionality (e.g., issuer call provisions, discretionary coupon features)
