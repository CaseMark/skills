---
name: structuring-pairs-trading-strategies
language: en
description: Designs statistical arbitrage pairs with cointegration analysis, spread dynamics, and entry/exit signal calibration. Use when building pairs trades, analyzing cointegration, or designing mean-reversion strategies.
tags:
  - public-markets-and-trading
metadata:
  author: casemark
  practice_areas:
    - Trading
    - Market Making
    - Execution
  document_types:
    - Report
  skill_modes:
    - Analysis
---
# Structuring Pairs Trading Strategies

Designs statistical arbitrage pairs with cointegration analysis, spread dynamics, and entry/exit signal calibration.

## When To Use

- Building a new pairs trading strategy from candidate universe screening through live signal generation
- Evaluating whether two or more instruments exhibit a stable, tradeable cointegrating relationship
- Calibrating entry/exit thresholds and position sizing for an existing spread
- Diagnosing strategy decay — determining whether a pair's statistical relationship has broken down
- Comparing multiple candidate pairs to select the highest-conviction opportunities

## Inputs To Gather

- **Instrument universe**: Tickers, asset class (equities, ETFs, futures, FX), and exchange/venue
- **Historical price data**: Adjusted close prices; minimum 2–5 years daily or equivalent intraday bars; confirm corporate action adjustments for equities
- **Fundamental linkage rationale**: Sector/industry overlap, supply-chain relationship, macro factor exposure, or structural reason the pair should mean-revert
- **Trading constraints**: Account size, margin requirements, borrow availability/cost, maximum holding period, commission/slippage assumptions
- **Risk parameters**: Maximum drawdown tolerance, per-trade loss limit, gross/net exposure caps, correlation budget within broader portfolio
- **Regime context**: Current volatility regime (VIX level, realized vol percentile), recent structural breaks in the sector, pending catalysts (earnings, M&A, index rebalance) [VERIFY against live market data]

## Workflow

1. **Screen candidate pairs**
   - Filter universe by sector, market cap, liquidity (minimum ADV), and borrow availability
   - Compute rolling pairwise correlations (60d, 120d, 252d) and rank by stability
   - Apply Engle-Granger or Johansen cointegration tests on log-price series; retain pairs with p-value < 0.05 across multiple lookback windows [VERIFY test assumptions: stationarity of residuals, no structural break in sample]

2. **Estimate spread dynamics**
   - Fit the cointegrating regression: log(P_A) = β · log(P_B) + μ + ε; record hedge ratio β and intercept
   - Test residual series for stationarity (ADF, KPSS); estimate half-life of mean reversion via Ornstein-Uhlenbeck calibration
   - Compute rolling z-score of the spread; assess distribution properties (skew, kurtosis, fat tails)
   - If half-life exceeds maximum holding period constraint, flag pair as unsuitable

3. **Calibrate entry/exit signals**
   - Set entry thresholds: typically ±1.5–2.5σ from spread mean; optimize via walk-forward backtest, not in-sample curve-fitting
   - Set exit thresholds: mean reversion target (0σ) and/or profit-take level; define stop-loss at ±3–4σ or dollar-based max loss
   - Evaluate asymmetric entry (long-spread vs. short-spread) if spread distribution is skewed
   - Determine position sizing: equal-dollar, beta-neutral, or volatility-weighted; compute notional per leg

4. **Backtest and stress-test**
   - Run walk-forward backtest with realistic transaction costs (commissions, bid-ask spread, borrow cost, market impact)
   - Report: Sharpe ratio, Sortino ratio, max drawdown, win rate, average holding period, profit factor
   - Stress-test against regime changes: 2008 credit crisis, 2020 COVID dislocation, sector rotation events
   - Test sensitivity to hedge ratio drift — re-estimate β on rolling windows and measure P&L degradation
   - Confirm no survivorship bias or look-ahead bias in data

5. **Define execution and monitoring plan**
   - Specify order types (limit vs. MOC), leg sequencing (simultaneous vs. legged), and execution venue preferences
   - Set re-hedge frequency for β drift (e.g., weekly recalibration if β moves > 5%)
   - Define kill criteria: pair is closed and removed if cointegration test fails on trailing 6-month window or if cumulative loss exceeds stop threshold
   - Document escalation triggers for manual review (spread hitting 4σ+, sudden liquidity drop, corporate event on either leg)

## Output

Deliver a **Pairs Trade Strategy Report** containing:

- **Pair summary table**: Ticker pair, sector, hedge ratio (β), spread half-life, cointegration p-value, correlation
- **Spread chart**: Historical spread with z-score overlay, entry/exit bands, and marked trade signals
- **Signal parameters**: Entry z-score, exit z-score, stop-loss z-score, position sizing method, notional per leg
- **Backtest results**: Performance metrics table (Sharpe, Sortino, max DD, win rate, avg hold, profit factor), equity curve, drawdown chart
- **Risk summary**: Max concurrent exposure, worst-case scenario P&L, margin requirement estimate, borrow cost impact
- **Execution plan**: Order type, rebalancing schedule, kill criteria, monitoring dashboard requirements
- **Assumptions and limitations log**: All [VERIFY] items, data quality notes, model limitations

## Quality Checks

- Cointegration holds across at least two independent lookback windows (e.g., 2-year and 5-year)
- Hedge ratio is economically plausible (not extreme values suggesting spurious fit)
- Backtest Sharpe > 1.0 after realistic transaction costs; if below, flag as marginal
- No single trade accounts for >25% of total backtest P&L (guards against curve-fitting)
- Half-life is within feasible holding period (typically 5–60 trading days for daily strategies)
- Walk-forward out-of-sample results do not degrade >30% vs. in-sample
- All data is survivorship-bias-free and adjusted for splits, dividends, and delistings [VERIFY data vendor methodology]
- Borrow availability confirmed for short leg; cost incorporated into P&L estimates [VERIFY with prime broker or locate desk]
