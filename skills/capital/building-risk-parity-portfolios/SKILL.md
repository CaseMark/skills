---
name: building-risk-parity-portfolios
description: Constructs risk parity allocation with equal risk contribution, leverage optimization, and asset class volatility targeting. Use when building risk parity, equalizing risk contribution, or designing leveraged balanced portfolios.
tags:
  - modeling
  - quantitative-capital-strategies
  - risk
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
# Building Risk Parity Portfolios

## When To Use

- Constructing a multi-asset portfolio where each asset class contributes equally to total portfolio risk
- Designing leveraged balanced strategies (e.g., Bridgewater All Weather–style allocations)
- Rebalancing an existing risk parity book to reflect updated covariance estimates
- Comparing risk parity weights against market-cap or equal-weight benchmarks
- Building a volatility-targeted overlay that scales gross exposure to a constant risk budget

## Inputs To Gather

- **Asset universe**: List of asset classes or instruments (e.g., equities, nominal bonds, TIPS, commodities, gold) with ticker-level mapping where applicable
- **Return series**: Total-return time series for each asset — minimum 10 years monthly, or 3 years daily; confirm frequency and currency [VERIFY]
- **Covariance estimation method**: Sample covariance, exponentially weighted (half-life), shrinkage (Ledoit-Wolf), or DCC-GARCH — confirm client preference
- **Risk-free rate**: Specify proxy (3-month T-bill, OIS, SOFR) and whether to subtract from returns before optimization [VERIFY]
- **Target portfolio volatility**: Annualized vol target for the levered portfolio (common range: 10–15%)
- **Leverage constraints**: Maximum gross exposure, borrowing cost assumption, margin/collateral rules [VERIFY]
- **Rebalance frequency**: Daily, weekly, monthly, or threshold-based (e.g., drift > 10% of target weight)
- **Lookback window**: Rolling window length for covariance estimation (e.g., 60-day, 252-day)

## Workflow

1. **Compute the covariance matrix**
   - Calculate returns at the chosen frequency; annualize if needed (√252 for daily)
   - Apply the selected estimation method; if shrinkage, report shrinkage intensity
   - Validate: check that the matrix is positive semi-definite; flag near-singular conditions

2. **Solve for risk parity weights**
   - Define the objective: each asset's marginal risk contribution (MRC) equals 1/N of total portfolio volatility
   - MRC_i = w_i × (Σw)_i / σ_p — iterate until MRC_i ≈ MRC_j for all i, j
   - Use numerical optimization (e.g., sequential least squares or Newton's method on the risk-budget Lagrangian)
   - Confirm weights sum to 1.0 (unlevered) or to gross exposure target (levered)

3. **Apply leverage scaling**
   - Compute unlevered portfolio volatility σ_unlevered from the risk parity weights
   - Leverage multiplier = Target Vol / σ_unlevered
   - Adjusted weights = raw weights × leverage multiplier
   - Subtract borrowing cost from expected return: cost = (gross exposure − 1) × funding rate [VERIFY funding rate assumption]

4. **Backtest and stress-test**
   - Run rolling or expanding-window backtest; report annualized return, vol, Sharpe, max drawdown, and Calmar ratio
   - Conduct stress scenarios: 2008 GFC, 2013 taper tantrum, 2020 COVID, 2022 rates shock — report portfolio P&L under each
   - Compare against 60/40, equal-weight, and inverse-vol benchmarks

5. **Sensitivity analysis**
   - Vary lookback window (30d, 60d, 120d, 252d) — show weight stability and turnover impact
   - Vary covariance method — compare sample vs. shrinkage vs. EWMA weights
   - Shock individual asset vols by ±2σ and correlation matrix by ±0.10 — report weight and risk-contribution shifts

6. **Document allocation model**
   - Final weight table with risk contribution breakdown (absolute and percentage)
   - Gross and net exposure, leverage ratio, estimated borrowing cost drag
   - Rebalance rule specification and estimated annual turnover
   - All assumptions flagged explicitly; mark jurisdiction-dependent constraints with [VERIFY]

## Output

Deliver a structured risk parity model package containing:

- **Weight schedule**: Asset-level weights, risk contributions, and leverage multiplier
- **Covariance summary**: Correlation heatmap, per-asset annualized vol, eigenvalue decomposition
- **Backtest report**: Equity curve, rolling Sharpe, drawdown chart, monthly return table
- **Stress-test matrix**: Scenario returns for the portfolio vs. benchmarks
- **Sensitivity exhibits**: Weight and turnover impact across parameter variations
- **Methodology memo**: Estimation method, optimization algorithm, rebalance logic, and all [VERIFY] items

## Quality Checks

- Confirm each asset's percentage risk contribution is within ±0.5% of 1/N target after optimization convergence
- Verify portfolio vol matches the stated target (tolerance: ±25 bps annualized)
- Check that weights are non-negative (unless short selling is explicitly permitted) and sum correctly
- Validate that the covariance matrix has no negative eigenvalues
- Ensure backtest does not use future information (no look-ahead bias in rolling windows)
- Cross-check leverage multiplier against margin and regulatory constraints [VERIFY applicable margin rules]
- Confirm borrowing cost assumption reflects current market rates, not stale inputs
