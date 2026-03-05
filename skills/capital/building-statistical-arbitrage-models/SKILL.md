---
name: building-statistical-arbitrage-models
description: Constructs stat arb strategies with pair selection, signal generation, and portfolio optimization under market neutrality constraints. Use when building stat arb models, designing market-neutral strategies, or optimizing pair portfolios.
tags:
  - modeling
  - quantitative-capital-strategies
  - portfolio
metadata:
  author: casemark
  practice_areas:
    - Quantitative Investing
    - Systematic Strategies
    - Factor Investing
  document_types:
    - Model
  skill_modes:
    - Modeling
---
# Building Statistical Arbitrage Models

## When To Use

- Designing a pairs trading or multi-leg market-neutral strategy from scratch
- Selecting cointegrated or correlated asset pairs from a candidate universe
- Generating entry/exit signals based on spread dynamics (z-score, Kalman filter, Ornstein-Uhlenbeck)
- Constructing a portfolio of stat arb positions with sector/beta neutrality constraints
- Backtesting and stress-testing an existing stat arb model before live deployment
- Migrating a discretionary relative-value approach into a systematic framework

## Inputs To Gather

- **Asset universe**: equity tickers, ETFs, futures, or other instruments with sufficient liquidity and history (minimum 3–5 years daily data recommended)
- **Pair selection criteria**: cointegration test choice (Engle-Granger, Johansen), minimum half-life, correlation thresholds, sector/industry filters
- **Signal parameters**: lookback window, z-score entry/exit thresholds, regime-detection toggles
- **Risk constraints**: target gross/net exposure, maximum single-pair allocation, sector neutrality tolerance, beta-to-benchmark cap
- **Cost assumptions**: commission per share, estimated slippage model, borrow cost/availability for short legs [VERIFY against current prime broker schedule]
- **Backtest parameters**: in-sample vs. out-of-sample split, rebalance frequency, transaction cost treatment

## Workflow

### 1. Universe Screening and Pair Formation

- Pull adjusted close prices for the candidate universe; verify for survivorship bias and corporate actions
- Compute pairwise cointegration tests across the universe; rank by test statistic significance
- Filter pairs: discard those with half-life outside target range (e.g., 5–60 trading days), insufficient cointegration p-value (< 0.05), or same-entity overlap
- Group surviving pairs by sector or factor exposure to ensure portfolio diversification

### 2. Spread Construction and Signal Design

- For each pair, estimate the hedge ratio via OLS, total least squares, or Kalman filter (dynamic hedge ratio preferred for non-stationary betas)
- Construct the spread series: `spread_t = price_A_t − hedge_ratio × price_B_t`
- Normalize spread to a z-score using a rolling lookback window; calibrate window length to the estimated half-life
- Define signal rules:
  - **Entry long spread**: z-score < −entry_threshold (e.g., −2.0)
  - **Entry short spread**: z-score > +entry_threshold
  - **Exit**: z-score reverts within ±exit_threshold (e.g., ±0.5) or stop-loss at ±stop_threshold (e.g., ±4.0)
- Optionally layer regime filters (e.g., suppress signals when realized spread volatility exceeds 2× its historical median)

### 3. Portfolio Construction Under Neutrality Constraints

- Allocate capital across active pairs using risk-parity, equal-dollar, or mean-variance weighting
- Enforce constraints:
  - Net dollar exposure ≤ target (e.g., ±5% of gross)
  - Net beta-to-index ≤ tolerance (e.g., ±0.10)
  - Single-pair concentration ≤ max allocation (e.g., 5% of gross)
  - Sector net exposure ≤ sector cap [VERIFY sector classification source: GICS, ICB, or custom]
- Rebalance at defined frequency; recalculate hedge ratios and re-run cointegration tests at each rebalance to retire degraded pairs

### 4. Backtest and Performance Attribution

- Run full backtest on the in-sample period with realistic transaction costs and borrow costs
- Compute key metrics: annualized return, Sharpe ratio, max drawdown, average holding period, win rate, profit factor
- Decompose PnL by pair, sector, and signal type to identify concentration risk
- Re-run on the out-of-sample period; flag any Sharpe degradation > 30% as potential overfit indicator
- Perform sensitivity analysis on entry/exit thresholds, lookback window, and hedge-ratio method

### 5. Risk and Stress Testing

- Simulate spread blow-ups: what happens if a pair's cointegration breaks permanently (structural break scenario)?
- Test under regime-specific stress periods (e.g., 2008 credit crisis, 2020 COVID dislocation, 2022 rate shock) [VERIFY data availability for chosen stress windows]
- Evaluate margin/liquidity impact: model margin calls under 3× normal spread volatility
- Check correlation of pair PnLs during stress — if pairwise correlation spikes, the portfolio loses diversification benefit

## Output

Deliver a stat arb model package containing:

- **Pair selection report**: list of qualifying pairs with cointegration statistics, half-life, and sector labels
- **Signal specification**: entry/exit rules with parameterized thresholds and regime filters
- **Portfolio allocation matrix**: pair weights, gross/net exposure, beta exposure, and sector exposure
- **Backtest results**: equity curve, performance metrics (Sharpe, max drawdown, Calmar), in-sample vs. out-of-sample comparison
- **Risk report**: stress-test outcomes, break-even cost analysis, sensitivity tables for key parameters
- **Implementation notes**: rebalance schedule, hedge-ratio update cadence, pair retirement criteria, and data pipeline requirements

## Quality Checks

- Confirm cointegration tests use the correct critical values for the number of pairs tested (Bonferroni or Holm correction for multiple comparisons)
- Verify hedge ratios are estimated on properly aligned, split/dividend-adjusted data
- Ensure backtest does not embed look-ahead bias (signals use only data available at signal time)
- Validate that transaction cost assumptions reflect current market conditions [VERIFY borrow costs for hard-to-borrow names]
- Check that portfolio-level neutrality constraints are satisfied at every rebalance point, not just on average
- Confirm out-of-sample period is truly held out and not used for any parameter tuning
- Flag any pair where the spread half-life drifts above the maximum threshold during the backtest as a candidate for early retirement
