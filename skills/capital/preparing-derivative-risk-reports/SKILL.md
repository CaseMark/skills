---
name: preparing-derivative-risk-reports
language: en
description: Structures derivative portfolio risk reporting with Greeks aggregation, scenario analysis, and limit monitoring. Use when preparing derivative risk reports, aggregating portfolio Greeks, or monitoring risk limits.
tags:
  - preparation
  - derivatives-and-structured-products
  - risk
  - portfolio
metadata:
  author: casemark
  practice_areas:
    - Derivatives
    - Structured Products
    - Hedging
  document_types:
    - Preparation Document
  skill_modes:
    - Preparation
---
# Preparing Derivative Risk Reports

Structures derivative portfolio risk reporting with Greeks aggregation, scenario analysis, and limit monitoring for options, swaps, futures, and structured products.

## When To Use

- Producing daily, weekly, or ad-hoc derivative portfolio risk reports for trading desks, risk committees, or management
- Aggregating Greeks (delta, gamma, vega, theta, rho) across positions, asset classes, or counterparties
- Running scenario and stress-test analyses on derivative books
- Monitoring risk limits (notional, VaR, Greeks thresholds) and flagging breaches
- Preparing risk summaries for regulatory filings or internal audit

## Inputs To Gather

- **Position data**: Full derivative position listing with instrument type (vanilla options, exotics, swaps, futures), notional, maturity, strike/coupon, and underlying reference
- **Market data snapshot**: Spot prices, implied volatility surfaces, yield curves, credit spreads, and FX rates as of report date
- **Greeks per position**: Pre-computed or model-sourced delta, gamma, vega, theta, rho; cross-gamma and vanna where relevant for exotics
- **Risk limits schedule**: Approved limit thresholds by desk, strategy, asset class, and counterparty (notional caps, VaR limits, Greeks ceilings)
- **Scenario definitions**: Standard shocks (e.g., ±1-2 SD moves, parallel/non-parallel curve shifts, vol surface shifts) and any ad-hoc scenarios requested by risk committee
- **Prior report**: Previous period's risk report for trend comparison and P&L attribution context
- **Valuation models used**: Black-Scholes, local vol, stochastic vol, Monte Carlo — note model and calibration date [VERIFY model governance requirements per firm policy]

## Workflow

1. **Validate position and market data**
   - Reconcile position counts against trade blotter; flag stale or missing prices
   - Confirm market data timestamps align with report cut-off time
   - Identify any positions with missing or suspect Greeks (e.g., gamma spikes near expiry)

2. **Aggregate Greeks by reporting dimension**
   - Roll up delta, gamma, vega, theta, rho by: underlying, asset class, desk/strategy, maturity bucket, and counterparty
   - Net offsetting positions where appropriate; show gross and net exposures
   - Compute portfolio-level Greeks and weighted-average metrics (e.g., weighted vega by tenor)

3. **Run scenario and stress analysis**
   - Apply standard scenarios: spot shocks (±5%, ±10%, ±20%), vol shocks (±5 vol points), rate shifts (±25bp, ±100bp parallel; bull/bear steepener/flattener)
   - Run tail-risk scenarios: historical replay of key events (e.g., 2008 credit crisis, 2020 March vol spike, SVB rates dislocation) [VERIFY which historical scenarios are required by firm policy]
   - Compute P&L impact per scenario at position and portfolio level
   - For structured products, run credit spread widening and correlation stress

4. **Assess limit utilization and breaches**
   - Compare current exposures against each applicable limit (notional, VaR, individual Greeks, concentration)
   - Calculate utilization percentages; flag any threshold above warning level (typically 80%) and hard breaches (100%+)
   - For breaches, note date first exceeded, magnitude, and whether a limit exception request is pending

5. **Compile trend and attribution analysis**
   - Compare Greeks and VaR to prior period; explain material changes (new trades, expiries, market moves)
   - Attribute P&L to delta, gamma, vega, theta, and residual/unexplained
   - Highlight any significant model-driven valuation changes

6. **Draft the report**
   - Executive summary: portfolio size (notional, position count), top-3 risk concentrations, limit status (green/amber/red), and key scenario outcomes
   - Detailed tables: Greeks by dimension, scenario P&L matrix, limit utilization dashboard
   - Commentary: explain drivers, flag items requiring action, note data quality issues
   - Appendices: position-level detail, methodology notes, glossary of terms

## Output

The deliverable is a structured risk report containing:

- **Executive summary** with portfolio headline metrics, limit status indicators, and action items
- **Greeks aggregation tables** with net/gross views across reporting dimensions
- **Scenario analysis matrix** showing P&L impact for each defined shock
- **Limit monitoring dashboard** with utilization percentages and breach flags
- **Trend analysis** comparing current period to prior period with attribution
- **Data quality notes** listing any stale prices, missing Greeks, or reconciliation breaks
- **Methodology appendix** documenting models, assumptions, and calibration dates

Format: Use consistent sign conventions (positive = long risk), clearly label units ($ thousands, basis points, vol points), and timestamp all data. [VERIFY reporting currency and unit conventions per desk/firm standards]

## Quality Checks

- All positions in the blotter are accounted for in the aggregation — no orphaned trades
- Greeks sum correctly across dimensions (spot-check: portfolio delta = sum of sub-portfolio deltas)
- Scenario P&L figures are internally consistent (e.g., a small spot shock P&L should approximate delta × shock size)
- Limit utilization figures tie to the approved limits schedule — confirm limit values haven't been updated since last report [VERIFY]
- No stale market data older than the report cut-off without explicit notation
- Prior-period comparisons use consistent methodology; flag any changes in model or aggregation logic
- Report clearly distinguishes between exchange-traded and OTC positions where margin/collateral treatment differs
- All [VERIFY] items resolved or escalated before distribution
