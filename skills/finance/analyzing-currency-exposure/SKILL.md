---
name: analyzing-currency-exposure
description: Evaluates and manages portfolio currency risk with hedging strategy analysis and cost assessment. Use when analyzing FX exposure, planning currency hedges, or assessing hedging costs.
tags:
  - analysis
  - asset-management
  - risk
  - portfolio
metadata:
  author: casemark
  practice_areas:
    - Portfolio Management
    - Asset Management
    - Wealth Management
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Currency Exposure

## When To Use

- Assessing FX risk across a multi-currency portfolio (equity, fixed income, alternatives)
- Evaluating whether to hedge, partially hedge, or leave currency exposure unhedged
- Comparing hedging instruments (forwards, options, cross-currency swaps) on a cost-benefit basis
- Reviewing existing hedge ratios after market moves, rebalancing events, or mandate changes
- Preparing currency risk commentary for client reporting or investment committee review

## Inputs To Gather

- **Portfolio holdings** with currency denomination, market value, and asset class for each position
- **Base (reporting) currency** of the portfolio or client mandate
- **Benchmark composition** — currency weights in the benchmark, if applicable
- **Current FX rates** and forward points for relevant currency pairs
- **Interest rate differentials** (carry) between base currency and each foreign currency
- **Hedging policy constraints** — mandate limits, minimum/maximum hedge ratios, permitted instruments
- **Historical volatility and correlation data** for relevant currency pairs (minimum 3-year lookback recommended)
- **Existing hedge positions** — notional, maturity, strike (for options), mark-to-market values
- **Transaction cost estimates** — bid-ask spreads, roll costs, margin/collateral requirements

## Workflow

1. **Map gross currency exposure**
   - Aggregate holdings by currency of denomination
   - Distinguish between direct exposure (asset currency) and indirect exposure (revenue currency of underlying companies, if relevant to mandate)
   - Calculate each currency's weight as a percentage of total portfolio NAV
   - Compare portfolio currency weights to benchmark weights to identify active currency bets

2. **Quantify currency risk contribution**
   - Compute standalone volatility of each currency pair vs. base currency
   - Estimate portfolio-level FX contribution to tracking error or total risk using variance-covariance or historical simulation
   - Identify which currency exposures are the largest contributors to overall portfolio risk
   - Flag concentrated exposures exceeding policy thresholds [VERIFY against mandate IPS limits]

3. **Evaluate hedging strategies**
   - **Passive (static) hedge**: rolling forward contracts at fixed hedge ratio (e.g., 50%, 100%)
   - **Active (dynamic) hedge**: adjusting hedge ratios based on valuation signals, momentum, or carry
   - **Option-based protection**: purchasing puts or collars to cap downside while retaining upside
   - For each strategy, estimate:
     - Carry cost or pickup (forward points / interest rate differential)
     - Roll cost over the hedge horizon (typically quarterly rolls)
     - Basis risk if hedge tenor or notional does not perfectly match exposure
     - Collateral / margin drag on portfolio liquidity

4. **Assess cost-benefit trade-offs**
   - Compare annualized hedge cost against expected risk reduction (e.g., cost per unit of volatility eliminated)
   - Model scenarios: base case, currency stress (+/- 2 standard deviations), and carry reversal
   - For option strategies, evaluate breakeven levels and premium decay
   - Consider tax implications of hedge gains/losses if relevant to the client structure [VERIFY jurisdiction-specific tax treatment]

5. **Formulate recommendation**
   - Recommend target hedge ratios by currency, supported by cost-benefit analysis
   - Specify instrument selection, tenor, and roll schedule
   - Note any residual unhedged exposure and rationale (e.g., positive carry, diversification benefit, low materiality)
   - Identify triggers for hedge ratio adjustment (e.g., FX move > X%, rebalancing threshold, policy review date)

## Output

- **Currency Exposure Summary Table** — columns: currency, gross exposure (%), benchmark weight (%), active weight (%), hedged notional, net exposure (%)
- **Risk Contribution Breakdown** — FX contribution to total portfolio volatility and tracking error, by currency
- **Hedging Strategy Comparison** — side-by-side table of passive, active, and option-based approaches with annualized cost, expected risk reduction, and implementation complexity
- **Scenario Analysis** — P&L impact under base, adverse, and stress FX scenarios, with and without hedges
- **Recommendation Memo** — concise narrative (1-2 pages) stating proposed hedge ratios, instruments, costs, and review triggers

## Quality Checks

- Confirm all currency exposures sum to 100% of portfolio NAV (no missing or double-counted positions)
- Verify forward points and rate quotes are same-day and sourced consistently
- Ensure hedge cost calculations use correct day-count conventions for each currency pair [VERIFY market convention: ACT/360 vs. ACT/365]
- Cross-check that recommended hedge ratios fall within mandate-permitted ranges
- Validate scenario assumptions are internally consistent (e.g., interest rate moves align with FX moves in stress scenarios)
- Flag any illiquid or restricted currencies where standard hedging instruments may not be available (e.g., CNY onshore vs. CNH offshore, BRL, INR) [VERIFY NDF market availability and cost]
- Mark all jurisdiction-dependent tax or regulatory points with [VERIFY]
