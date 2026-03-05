---
name: analyzing-fx-derivatives
description: Structures FX option and forward pricing with cross-currency basis analysis and volatility assessment. Use when pricing FX derivatives, analyzing currency options, or evaluating cross-currency basis.
tags:
  - analysis
  - quantitative-finance
metadata:
  author: casemark
  practice_areas:
    - Derivatives
    - Quantitative Analysis
    - Structured Products
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing FX Derivatives

Structures FX option and forward pricing with cross-currency basis analysis and volatility assessment.

## When To Use

- Pricing vanilla or exotic FX options (European, American, barrier, digital, quanto)
- Calculating FX forward points and outright forward rates from spot and interest rate differentials
- Analyzing cross-currency basis spreads and their impact on hedging costs
- Evaluating implied volatility surfaces for currency pairs (smile, skew, term structure)
- Assessing hedging strategies for FX exposure using options or forwards
- Structuring FX-linked notes, dual-currency deposits, or PRDCs

## Inputs To Gather

- **Currency pair(s)**: Specify base/quote convention (e.g., EUR/USD, USD/JPY) and confirm market convention for quoting
- **Spot rate**: Current mid-market spot and bid/ask spread
- **Interest rate curves**: Deposit rates or OIS curves for both currencies across relevant tenors
- **Volatility data**: ATM vols, 25-delta and 10-delta risk reversals and butterflies for relevant tenors
- **Cross-currency basis**: Basis swap spreads for the currency pair at target tenors
- **Trade parameters**: Notional, tenor, strike(s), barrier levels, settlement convention (cash vs. physical), premium currency
- **Market date and cut time**: Valuation date, expiry convention (NY cut, Tokyo cut), and delivery convention [VERIFY]

## Workflow

1. **Establish forward curve**
   - Derive forward points from spot rate and interest rate differential for each tenor
   - Apply cross-currency basis adjustment: the basis spread modifies the synthetic funding cost, shifting forward points from covered interest rate parity
   - Confirm forward points align with market quotes; flag discrepancies exceeding 0.5 pips

2. **Construct volatility surface**
   - Map ATM volatilities across the term structure (1W through 2Y minimum)
   - Convert risk reversal and butterfly quotes into individual delta-strike volatilities (25D call, 25D put, 10D call, 10D put)
   - Interpolate between tenors using flat forward variance or SABR parameterization
   - Check for calendar spread arbitrage (variance must be non-decreasing in time) and butterfly arbitrage (call spreads must be non-negative)

3. **Price the derivative**
   - **Vanilla options**: Use Garman-Kohlhagen (Black-Scholes adapted for FX with domestic/foreign rate inputs); confirm premium quotation convention (% of domestic, % of foreign, or pips) [VERIFY]
   - **Barrier options**: Apply analytical formulas where available (single-barrier with continuous monitoring); for discrete barriers, adjust using Broadie-Glasserman correction or Monte Carlo
   - **Forwards/NDFs**: Calculate outright from spot + forward points; for NDFs, confirm fixing source and settlement currency [VERIFY]
   - **Structured products**: Decompose into component vanilla/barrier options and forwards; price each leg and aggregate

4. **Analyze cross-currency basis impact**
   - Quantify how the basis spread affects all-in hedging cost vs. uncollateralized forward
   - Compare CSA-discounted vs. non-CSA pricing for collateralized trades
   - Assess basis directionality: negative basis in EUR/USD or JPY/USD widens USD funding advantage
   - For multi-year structures, show basis term structure sensitivity (DV01-equivalent per tenor bucket)

5. **Run risk sensitivities**
   - Delta and gamma (spot sensitivity)
   - Vega across tenors (parallel and bucketed)
   - Rho for both domestic and foreign rates
   - Theta (time decay)
   - For barriers: pin risk near barrier, gap risk for discrete monitoring
   - Cross-gamma between spot and vol (vanna), vol-of-vol sensitivity (volga)

6. **Evaluate hedging strategy**
   - Compare delta-hedging cost (gamma P&L vs. theta) against static option replication
   - Assess whether risk reversals or seagulls reduce premium while maintaining acceptable protection
   - Quantify worst-case scenario under stress moves (e.g., 3-sigma spot move, vol spike, basis blowout)

## Output

- **Pricing summary table**: Instrument type, notional, strike, premium (in multiple conventions), break-even rate, and max loss
- **Forward curve**: Table of spot, forward points, outright forwards, and basis-adjusted forwards per tenor
- **Volatility surface snapshot**: ATM, 25D RR, 25D BF, and derived strike vols per tenor
- **Greeks dashboard**: Delta, gamma, vega, theta, rho for each leg and net position
- **Basis impact analysis**: Cost comparison of hedging with and without basis adjustment
- **Scenario analysis**: P&L under 2-3 stress scenarios (spot shock, vol shock, basis widening)
- **Recommendations**: Preferred structure with rationale, noting trade-offs between cost, protection level, and complexity

## Quality Checks

- Verify put-call parity holds for all quoted option pairs (synthetic forward from call minus put equals market forward)
- Confirm forward points are consistent with interest rate differential and basis; any residual should be explainable by bid/ask or day-count conventions [VERIFY day-count conventions: ACT/360 vs. ACT/365 varies by currency]
- Validate that volatility surface is arbitrage-free (no negative butterfly spreads, no calendar spread violations)
- Cross-check Garman-Kohlhagen inputs: ensure domestic rate = rate of premium currency and foreign rate = rate of underlying currency — a common source of mispricing
- Confirm settlement and delivery conventions match market standard for the pair [VERIFY: T+2 is standard for most G10, but USD/CAD is T+1, and some EM pairs have non-standard settlement]
- Ensure notional and premium currency are consistent throughout; flag any mismatch between trade economics and risk reports
- For structured products, verify that component prices sum correctly and that knock-in/knock-out conditions are mutually consistent
