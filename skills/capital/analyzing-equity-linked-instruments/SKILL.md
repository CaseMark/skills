---
name: analyzing-equity-linked-instruments
language: en
description: Evaluates convertible bond and mandatory convertible structures with equity sensitivity, credit floor, and Greeks analysis. Use when analyzing convertible offerings, pricing equity-linked instruments, or modeling conversion economics.
tags:
  - analysis
  - equity-capital-markets
  - credit
metadata:
  author: casemark
  practice_areas:
    - ECM
    - IPO Advisory
    - Equity Origination
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Equity Linked Instruments

Evaluates convertible bond and mandatory convertible structures with equity sensitivity, credit floor, and Greeks analysis.

## When To Use

- Pricing or reviewing a new convertible bond offering (vanilla, mandatory, contingent)
- Assessing conversion economics for an existing equity-linked instrument
- Comparing convertible structures across issuers or maturities
- Modeling sensitivity of instrument value to equity price, volatility, or credit spread changes
- Evaluating investor returns under various stock-price and credit scenarios

## Inputs To Gather

- **Instrument terms**: coupon rate, maturity, conversion price, conversion ratio, call/put provisions, reset features, contingent conversion triggers
- **Issuer data**: current stock price, historical and implied volatility, dividend yield, credit rating, outstanding debt structure
- **Market data**: risk-free rate curve, credit spread curve for issuer or comparable credits, equity borrow cost
- **Structure type**: vanilla convertible, mandatory convertible (PERCS, DECS, MCPS), exchangeable, contingent convertible (CoCo)
- **Analysis scope**: full valuation, relative value comparison, scenario analysis, or Greeks snapshot

## Workflow

1. **Classify the instrument**
   - Identify structure type (vanilla convertible, mandatory convertible, CoCo, exchangeable)
   - Map key embedded options: equity call, issuer call, investor put, reset provisions, contingent triggers
   - Note any non-standard features (make-whole, dividend protection, change-of-control puts)

2. **Decompose into components**
   - **Bond floor (credit component)**: discount contractual cash flows at the issuer's credit spread to derive straight-debt value
   - **Equity option component**: value the embedded conversion right using a binomial tree or Black-Scholes variant adjusted for dilution, dividends, and call features
   - For mandatory convertibles, model the capped-call / written-put payoff structure (upper and lower strike boundaries)
   - For CoCos, incorporate trigger probability modeling (mechanical vs. discretionary triggers) [VERIFY: trigger type and loss-absorption mechanism — write-down vs. conversion]

3. **Calculate key metrics**
   - **Conversion premium**: (conversion price / current stock price − 1) × 100
   - **Bond floor premium**: (market price / bond floor − 1) × 100
   - **Investment premium**: (market price / parity − 1) × 100
   - **Break-even period**: conversion premium ÷ (coupon yield − dividend yield on equivalent shares)
   - **Parity**: conversion ratio × current stock price
   - **Expected yield**: YTM on bond floor, current yield on convertible

4. **Run Greeks and sensitivity analysis**
   - **Delta**: sensitivity of convertible price to underlying equity moves
   - **Gamma**: rate of change of delta as equity moves
   - **Vega**: sensitivity to implied volatility changes
   - **Rho (credit)**: sensitivity to credit spread widening/tightening
   - **Theta**: time decay of the embedded option
   - Produce an equity sensitivity table: convertible value at stock prices ±5%, ±10%, ±20%, ±30% from spot

5. **Assess credit floor integrity**
   - Verify bond floor using issuer credit spread or CDS levels [VERIFY: use issuer-specific CDS if available vs. synthetic spread]
   - Stress-test bond floor under 100bp, 200bp, and 500bp spread widening scenarios
   - Evaluate recovery assumptions if issuer is below investment grade
   - Flag instruments where parity is far below bond floor (busted convertibles) or far above (equity-like behavior)

6. **Scenario and relative-value analysis**
   - Model bull/base/bear equity scenarios and map convertible returns vs. straight equity and straight debt
   - Compare conversion premium, delta, and break-even across peer issuances
   - For mandatory convertibles, chart payoff profile showing capped upside and full downside participation below lower strike

7. **Compile findings**
   - Summarize instrument profile: equity-sensitive, balanced, or credit-sensitive positioning
   - Highlight asymmetric return features (downside protection via bond floor, upside participation via delta)
   - Note risks: call risk, credit deterioration, dividend changes, volatility crush, dilution impact on common shareholders
   - Flag any terms requiring issuer-level or regulatory verification

## Output

- **Instrument Summary Table**: structure type, key terms, conversion metrics (premium, parity, break-even)
- **Valuation Breakdown**: bond floor value, equity option value, theoretical fair value vs. market price (cheap/rich indicator)
- **Greeks Dashboard**: delta, gamma, vega, credit rho, theta at current spot
- **Equity Sensitivity Grid**: convertible price and delta across a range of stock prices
- **Credit Stress Table**: bond floor and total value under spread-widening scenarios
- **Scenario Returns Matrix**: convertible total return vs. equity return under bull/base/bear
- **Risk Flags**: call features approaching trigger, thin bond-floor cushion, upcoming dividend changes, liquidity concerns

## Quality Checks

- Confirm bond floor does not exceed market price (if it does, verify credit assumptions or flag potential arbitrage)
- Validate that delta falls between 0 and 1, and that delta + bond-floor-weight ≈ 1 for properly decomposed instruments
- Verify break-even calculation uses the correct yield advantage (coupon minus forgone dividends)
- Cross-check conversion ratio and conversion price are consistent with prospectus terms [VERIFY: confirm against offering circular or indenture]
- Ensure Greeks are internally consistent (e.g., higher delta for lower conversion premiums, gamma peak near at-the-money)
- For mandatory convertibles, confirm payoff replicates the correct collar structure (long stock + short call + long put, or equivalent)
- Mark any assumed volatility, credit spread, or dividend inputs with source and as-of date
