---
name: analyzing-convertible-bonds
description: Evaluates convertible bond structures with equity sensitivity, credit floor, and Greeks calculation. Use when analyzing convertibles, calculating conversion premiums, or evaluating hybrid instruments.
tags:
  - analysis
  - fixed-income
  - credit
metadata:
  author: casemark
  practice_areas:
    - Fixed Income
    - Credit Research
    - Bond Trading
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Convertible Bonds

## When To Use

- Evaluating a new convertible bond issuance for investment suitability
- Calculating conversion premium, parity, and breakeven horizon for an existing position
- Determining the credit floor (bond floor / investment value) to assess downside protection
- Analyzing equity sensitivity (delta) and Greeks for hedging or relative-value trades
- Comparing convertible structures across issuers or maturities (mandatory vs. optional conversion, contingent conversion triggers, make-whole provisions)
- Assessing forced-conversion risk or call-spread overlay economics

## Inputs To Gather

- **Bond terms**: coupon rate, maturity, par value, conversion ratio, conversion price, call schedule (hard call / soft call dates and prices), put schedule if any
- **Issuer credit profile**: credit rating (Moody's/S&P/Fitch), CDS spread or comparable straight-debt spread, sector, leverage metrics
- **Equity data**: current stock price, dividend yield, historical and implied volatility, borrow cost
- **Market data**: risk-free rate curve, credit spread curve for the issuer's rating tier, recovery assumption
- **Structure specifics**: contingent conversion (CoCo) triggers, make-whole fundamental change provisions, cash/share/combo settlement, reset features, cap/floor on conversion ratio
- **Portfolio context** (if applicable): existing equity or credit exposure to the issuer, hedging objectives

## Workflow

1. **Parse the indenture terms**
   - Extract conversion ratio, conversion price, coupon, maturity, call/put schedule, and any contingent features
   - Identify settlement method (physical, cash, net-share) — this affects delta hedging and tax treatment [VERIFY: settlement method and tax treatment vary by jurisdiction]

2. **Calculate core metrics**
   - **Conversion parity** = conversion ratio × current stock price
   - **Conversion premium** = (bond price − parity) / parity, expressed as %
   - **Premium payback period** = conversion premium / (coupon yield − dividend yield on equivalent shares); flag if dividend yield exceeds coupon yield (negative carry)
   - **Bond floor (investment value)** = PV of coupon and principal cash flows discounted at issuer's straight-debt yield; this is the credit floor
   - **Risk premium over bond floor** = (bond price − bond floor) / bond floor

3. **Assess equity sensitivity and Greeks**
   - **Delta**: estimate via a convertible pricing model (binomial tree or Black-Scholes adjusted for credit) — typical ranges: busted (<0.2), hybrid (0.3–0.7), equity-like (>0.8)
   - **Gamma**: rate of delta change; highest near the conversion price — relevant for gamma-trading strategies
   - **Vega**: sensitivity to implied vol; long vega is a core convertible feature
   - **Rho**: interest-rate sensitivity of the bond floor component
   - **Theta**: time decay of the embedded option; accelerates approaching maturity or hard-call date

4. **Evaluate credit component**
   - Compare bond floor to par to gauge downside cushion
   - Stress-test the bond floor under spread-widening scenarios (+50 bps, +100 bps, +200 bps)
   - Assess recovery value assumption in default scenario (typically 30–40% for unsecured converts) [VERIFY: recovery assumptions against current sector norms]

5. **Analyze call and put features**
   - Determine if the issuer can force conversion (stock trading above call price × conversion ratio for required period)
   - Calculate probability-weighted expected life given soft-call triggers
   - Evaluate investor put rights and their impact on yield-to-put vs. yield-to-maturity

6. **Run scenario analysis**
   - Upside: stock +20%, +50% — compute bond price, delta shift, and forced-conversion likelihood
   - Downside: stock −20%, −50% — compute bond price vs. bond floor, credit deterioration risk
   - Spread scenarios: parallel shift in credit spreads, rating downgrade impact on bond floor
   - Volatility scenarios: vol crush (−10 pts) and vol spike (+10 pts) effect on theoretical value

7. **Relative-value comparison** (if applicable)
   - Compare cheapness/richness vs. theoretical value from a pricing model
   - Benchmark against comparable convertibles (same sector, similar delta profile)
   - Assess vs. synthetic alternative (buying straight bond + equity call option)

## Output

Structure the analysis report as follows:

- **Summary**: one-paragraph investment thesis — is this convert cheap/fair/rich, and what profile does it offer (equity substitute, credit-plus-optionality, busted/distressed)?
- **Term sheet recap**: key terms in tabular format (coupon, maturity, conversion price/ratio, call schedule, settlement)
- **Valuation metrics table**: parity, premium, premium payback, bond floor, risk premium over floor, delta, gamma, vega, theoretical value, cheap/rich assessment
- **Scenario matrix**: bond price, delta, and P&L under the equity/credit/vol scenarios above
- **Risk factors**: forced-conversion risk, credit deterioration, dividend increases reducing option value, liquidity risk, structural subordination
- **Recommendation / positioning**: buy/sell/hold with sizing context, or hedging recommendation (e.g., delta-neutral, credit-hedged)

## Quality Checks

- Verify conversion ratio and conversion price are internally consistent (par / conversion price = conversion ratio)
- Confirm bond floor is calculated using the issuer's straight-debt spread, not the risk-free rate
- Ensure delta and Greeks are derived from a model that incorporates credit risk (not plain Black-Scholes on a risk-free basis)
- Check that premium payback calculation correctly handles the sign when dividend yield exceeds coupon yield
- Validate call schedule dates against the indenture — soft-call trigger conditions (e.g., stock trading above 130% of conversion price for 20 of 30 trading days) must be stated precisely [VERIFY: exact trigger language from the indenture]
- Cross-check theoretical value against at least one independent source or model
- Flag any make-whole or change-of-control provisions that materially affect valuation
