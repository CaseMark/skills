---
name: conducting-monte-carlo-portfolio-analysis
language: en
description: Runs Monte Carlo simulations for portfolio analysis with return distribution, tail risk, and path-dependent scenario evaluation. Use when running portfolio simulations, estimating tail risk, or analyzing return distributions.
tags:
  - process
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
    - Process Documentation
  skill_modes:
    - Process Management
---
# Conducting Monte Carlo Portfolio Analysis

Runs Monte Carlo simulations for portfolio analysis, producing return distributions, tail-risk metrics, and path-dependent scenario evaluations for multi-asset portfolios.

## When To Use

- Estimating the probability distribution of portfolio returns over a defined horizon (1-month to 30-year)
- Quantifying tail risk (CVaR/ES, max drawdown distributions, left-tail probabilities)
- Evaluating path-dependent features: sequence-of-returns risk, cash-flow overlays, rebalancing triggers, or option-like payoffs
- Stress-testing portfolio allocations under regime-switching or fat-tailed assumptions
- Comparing allocation candidates when closed-form analytics are insufficient (e.g., non-normal returns, leverage constraints, dynamic hedging)

## Inputs To Gather

- **Asset universe and weights** — tickers or asset classes, target allocation, and any constraints (min/max bounds, sector caps)
- **Return assumptions** — historical lookback window OR forward capital-market assumptions (expected return, volatility, correlation matrix)
- **Distribution model** — normal, Student-t (specify degrees of freedom), skew-normal, or empirical bootstrap [VERIFY: confirm distributional choice suits the asset classes]
- **Simulation parameters** — number of paths (default: 10,000; use 50,000+ for stable tail estimates), time step (daily/monthly), horizon length
- **Correlation structure** — static Pearson matrix, DCC-GARCH, copula specification (Gaussian vs. Clayton/Gumbel for tail dependence) [VERIFY: copula choice with portfolio manager]
- **Path-dependent rules** — rebalancing frequency and bands, cash inflows/outflows, drawdown-triggered de-risking, tax-loss harvesting logic
- **Risk-free rate and inflation assumption** — for real-return or Sharpe-ratio computations
- **Benchmark** (optional) — index or liability stream for relative-return analysis

## Workflow

1. **Validate inputs**
   - Confirm the correlation matrix is positive semi-definite; apply nearest-PSD correction if not
   - Check for stale or missing return series; flag gaps > 5 trading days
   - Verify that weight vector sums to 1.0 (or intended leverage ratio)

2. **Calibrate the return-generation model**
   - Fit chosen distribution to each asset's return series (MLE or method-of-moments)
   - Estimate correlation/copula parameters; report goodness-of-fit (e.g., Anderson-Darling p-values)
   - If using regime-switching: estimate Hidden Markov Model states (bull/bear/crisis) with transition probabilities [VERIFY: number of regimes]

3. **Generate simulation paths**
   - Draw correlated random variates via Cholesky decomposition (normal) or copula sampling (non-normal)
   - Construct cumulative return paths for each asset; apply portfolio weights at each rebalancing step
   - Enforce path-dependent rules: execute rebalances, apply transaction costs, overlay cash flows

4. **Compute output statistics**
   - **Distribution metrics** — mean, median, standard deviation, skewness, kurtosis of terminal wealth or annualized return
   - **Tail-risk metrics** — VaR and CVaR at 95% and 99% confidence; maximum drawdown distribution (median, 95th percentile); probability of loss exceeding a user-defined threshold
   - **Path statistics** — median path, 5th/25th/75th/95th percentile fan chart; time-to-recovery distribution after drawdowns > X%
   - **Scenario analysis** — conditional statistics for worst 5% of paths (crisis regime analysis)

5. **Sensitivity and robustness checks**
   - Re-run with ±1 standard error on expected returns and volatilities to assess input sensitivity
   - Compare results across distribution assumptions (normal vs. Student-t vs. bootstrap)
   - Confirm convergence: verify that key metrics stabilize as path count doubles

6. **Compile report**
   - Present results in summary table plus fan-chart visualization specification
   - Highlight key risk findings: probability of failing a return threshold, worst-case drawdown, and left-tail scenarios
   - State all assumptions, model limitations, and data vintage

## Output

- **Summary statistics table** — expected return (annualized), volatility, Sharpe ratio, VaR (95/99), CVaR (95/99), max drawdown (median and 95th percentile), probability of negative return, probability of meeting target return
- **Distribution chart spec** — histogram of terminal returns with VaR/CVaR markers; fan chart of cumulative wealth paths (5/25/50/75/95 percentile bands)
- **Sensitivity matrix** — key metrics under alternative return, volatility, and correlation assumptions
- **Path-dependent analysis** — impact of rebalancing frequency, cash-flow timing, and drawdown-triggered rules on terminal wealth distribution
- **Assumption log** — distribution model, calibration method, number of simulations, random seed (for reproducibility), data sources and dates

## Quality Checks

- Simulation count is sufficient: tail metrics (99% CVaR) should not shift > 2% when re-run with a different random seed
- Mean simulated return approximates the input expected return within ±10 bps (sanity check on the generation engine)
- Correlation of simulated asset returns matches input matrix within ±0.02
- Path-dependent rules are verified against at least one manually traced scenario
- All [VERIFY] items are resolved or explicitly flagged as pending before delivery
- Results are not presented as forecasts — disclaim that outputs reflect model assumptions, not predictions of future performance
