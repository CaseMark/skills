---
name: analyzing-commodity-derivatives
language: en
description: Structures commodity derivative pricing with forward curve construction and convenience yield estimation. Use when pricing commodity derivatives, analyzing forward curves, or modeling commodity markets.
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
# Analyzing Commodity Derivatives

## When To Use

- Pricing commodity futures, options, or swaps on energy, metals, or agricultural underlyings
- Constructing or validating a forward curve from observed futures prices and basis quotes
- Estimating convenience yield for physical-delivery commodities (crude oil, natural gas, copper, grains)
- Evaluating structured commodity products such as collars, accumulators, or storage deals
- Assessing contango/backwardation dynamics and their implications for hedging or trading strategies

## Inputs To Gather

- **Spot and futures prices**: Current spot price plus settlement prices across available contract maturities (source: exchange data, broker screens, or OTC quotes)
- **Interest rate curve**: Risk-free rates (e.g., SOFR or Treasury curve) for corresponding tenors
- **Storage and carry costs**: Warehousing fees, insurance, financing costs, and any applicable transport/delivery premiums [VERIFY against current exchange fee schedules]
- **Historical volatility data**: Realized vol on the underlying commodity, implied vol surface if options are in scope
- **Contract specifications**: Lot size, delivery location, quality grade, settlement method (physical vs. cash), and expiry calendar [VERIFY against exchange contract specs]
- **Seasonal patterns**: Known demand/supply cycles (e.g., heating oil winter demand, grain harvest windows)

## Workflow

1. **Define the analysis scope**
   - Identify the commodity, exchange, and contract months in scope
   - Confirm whether the analysis covers futures only or includes options/structured products
   - Establish the pricing date and data snapshot time

2. **Construct the forward curve**
   - Collect settlement prices for all liquid contract months
   - Interpolate between observed points using cubic spline or piecewise-linear methods for illiquid tenors
   - Apply calendar-spread adjustments for roll periods
   - Validate curve shape: flag any inversions or discontinuities that may indicate stale data or market stress

3. **Estimate convenience yield**
   - Back out implied convenience yield from the cost-of-carry model: F(T) = S * exp((r + c - y) * T), solving for y
   - Compare implied convenience yield across tenors — typically higher at short maturities during supply tightness
   - Cross-check against physical market indicators: inventory levels, basis differentials, draw/injection rates
   - Note: convenience yield is not directly observable; always present as an estimate with stated assumptions

4. **Price the derivative instrument**
   - **Futures**: Mark-to-market using constructed forward curve; compute basis risk if hedging a non-standard delivery point
   - **Vanilla options**: Apply Black-76 model using forward price as underlying, with implied vol from the vol surface; report Greeks (delta, gamma, vega, theta)
   - **Swaps**: Calculate fixed-for-floating swap value by discounting the difference between the fixed price and the forward curve at each settlement date
   - **Structured products**: Decompose into component instruments (e.g., a collar = long put + short call on the commodity forward); price each leg independently, then aggregate

5. **Assess market structure and risk**
   - Characterize the term structure: contango (upward-sloping, storage costs dominate) vs. backwardation (downward-sloping, convenience yield dominates)
   - Quantify roll yield impact for positions held across contract rolls
   - Run sensitivity analysis: parallel shift in forward curve (+/- 5-10%), vol shock (+/- 20% relative), and interest rate bump
   - Identify key risk factors: liquidity concentration in specific tenors, delivery optionality, and regulatory position limits [VERIFY position limit rules per exchange and jurisdiction]

## Output

- **Forward curve table and chart**: Observed prices, interpolated curve, and implied convenience yield by tenor
- **Derivative valuation summary**: Fair value, mark-to-market P&L (if an existing position), and decomposition by component for structured products
- **Greeks and sensitivities**: Delta, gamma, vega, theta for options; DV01/duration-equivalent for swaps; scenario-based P&L for all instruments
- **Market structure commentary**: Contango/backwardation assessment, roll yield estimate, and comparison to historical term structure patterns
- **Risk flags**: Any data gaps, illiquid tenors used in interpolation, large convenience yield deviations, or positions near regulatory limits

## Quality Checks

- Verify forward curve is arbitrage-free: no negative calendar spreads in a full-carry market without a plausible convenience yield explanation
- Confirm option pricing recovers observed market premiums within bid-ask spread tolerance
- Ensure convenience yield estimates are consistent with physical market fundamentals (inventory reports, shipping rates)
- Validate that swap valuations net to zero at inception for at-market swaps
- Cross-check Greeks by bumping inputs numerically and comparing to analytical values
- Flag any assumed correlations (e.g., between delivery locations or commodity grades) with [VERIFY] markers
- Confirm all contract specifications match the relevant exchange rulebook [VERIFY expiry dates, delivery terms, and tick sizes]
