---
name: modeling-portfolio-optimization
description: Builds mean-variance, Black-Litterman, and risk parity optimization models with constraint management and rebalancing rules. Use when optimizing portfolios, implementing risk parity, or applying Black-Litterman views.
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
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Portfolio Optimization

Builds mean-variance, Black-Litterman, and risk parity optimization models with constraint management and rebalancing rules.

## When To Use

- Constructing or rebalancing a multi-asset or multi-factor portfolio against a risk/return objective
- Incorporating subjective market views into equilibrium weights via Black-Litterman
- Implementing risk parity or equal risk contribution across asset classes or factors
- Evaluating constraint sets (position limits, sector caps, turnover budgets) and their impact on the efficient frontier
- Stress-testing portfolio allocations under regime-change or tail-risk scenarios

## Inputs To Gather

- **Return estimates**: Historical return series (frequency, lookback window, asset universe) or forward-looking expected returns from a separate alpha model
- **Covariance / risk model**: Sample covariance, shrinkage estimator (Ledoit-Wolf), factor-based risk model, or DCC-GARCH specification — document which and why
- **Benchmark or equilibrium reference**: Market-cap weights for Black-Litterman implied returns; benchmark index if tracking error is a constraint
- **Investor views** (Black-Litterman): Absolute or relative views, confidence levels (tau, omega matrix calibration)
- **Constraints**: Min/max position sizes, sector/geography/factor exposure limits, long-only vs. long-short, turnover cap, transaction cost estimates
- **Risk budget** (risk parity): Target risk contribution per asset or factor; marginal risk contribution tolerances
- **Rebalancing rules**: Calendar-based (monthly, quarterly) vs. threshold-based (drift bands), tax-lot considerations if applicable

## Workflow

1. **Select optimization framework**
   - Mean-variance (Markowitz): Use when you have credible expected return estimates and want to target a point on the efficient frontier or maximize Sharpe ratio.
   - Black-Litterman: Use when starting from equilibrium (market-cap) weights and blending in discretionary or model-driven views. Specify tau (scaling factor for uncertainty in equilibrium returns) and construct the pick matrix (P) and view vector (Q) with confidence-weighted omega.
   - Risk parity / equal risk contribution: Use when the goal is balanced risk allocation without relying on return forecasts. Solve for weights where each asset's marginal contribution to portfolio volatility is equal (or proportional to a risk budget).

2. **Prepare inputs**
   - Clean return series: handle missing data, survivorship bias, corporate actions. State lookback period and frequency.
   - Estimate covariance matrix. For large universes (>50 assets), apply shrinkage or factor decomposition to avoid singular or unstable matrices. Document eigenvalue floor if regularizing.
   - For Black-Litterman: derive implied equilibrium returns (π = δΣw_mkt), then combine with views using the BL formula. State delta (risk aversion coefficient) derivation.

3. **Formulate and solve**
   - Define the objective function (e.g., maximize w'μ − (λ/2)w'Σw for mean-variance; minimize Σ(RC_i − RC_target)^2 for risk parity).
   - Encode all constraints as linear or second-order cone constraints for convex solvers.
   - Solve using quadratic programming (mean-variance), sequential least-squares (risk parity), or closed-form BL posterior.
   - If the solver fails to converge, relax the tightest binding constraint incrementally and document the trade-off.

4. **Analyze outputs**
   - Report optimal weights, expected return, expected volatility, Sharpe ratio, and max drawdown (historical backtest).
   - Decompose risk: contribution by asset, by factor, and by sector. Identify concentration risks.
   - Run sensitivity analysis: perturb expected returns ±50–100 bps, shift correlations ±0.05–0.10, vary tau (BL) across 0.01–0.10 range. Report weight stability.
   - Compare to benchmark or current portfolio: active weights, tracking error, information ratio.

5. **Define rebalancing protocol**
   - Specify trigger mechanism: calendar schedule or drift threshold (e.g., rebalance when any weight deviates >2% from target).
   - Incorporate transaction cost model (fixed + proportional) into the rebalance decision — only rebalance if expected utility gain exceeds estimated round-trip cost.
   - For tax-sensitive accounts, apply tax-lot optimization and short-term vs. long-term gain awareness. [VERIFY: tax-lot rules per jurisdiction]

6. **Document and deliver**
   - Produce a model specification sheet: objective, constraints, solver, input sources, date range, key parameters.
   - Include an assumptions register with explicit flags for any estimated or inferred input.
   - Attach backtest results with appropriate caveats (in-sample vs. out-of-sample, transaction cost assumptions, look-ahead bias checks).

## Output

- **Optimal weight table**: Asset/factor, target weight, current weight, trade direction, position size
- **Risk decomposition**: Marginal and percentage contribution to risk by asset, factor, and sector
- **Efficient frontier chart** (mean-variance) or **risk contribution bar chart** (risk parity)
- **Sensitivity matrix**: Weight changes under perturbed inputs (returns, correlations, tau)
- **Rebalancing rule summary**: Trigger type, cost threshold, expected annual turnover
- **Model specification sheet**: Full parameter documentation for reproducibility and audit

## Quality Checks

- Weights sum to 1.0 (or target net exposure for long-short) and satisfy all stated constraints
- Covariance matrix is positive semi-definite — check smallest eigenvalue > 0 (or applied regularization)
- Black-Litterman posterior returns lie between equilibrium returns and views — extreme tilts signal omega miscalibration
- Risk parity solution achieves risk contributions within tolerance (e.g., ±0.5% of target) — if not, flag solver convergence issue
- Backtest Sharpe ratio is plausible relative to asset class history — ratios above 2.0 for traditional assets warrant scrutiny for overfitting
- No single asset exceeds concentration limit; sector/factor exposures within policy bands
- Transaction cost assumptions are realistic for the asset class and trade size [VERIFY: market-specific bid-ask and commission schedules]
- All assumptions, data sources, and parameter choices are documented — no "magic numbers" without justification
