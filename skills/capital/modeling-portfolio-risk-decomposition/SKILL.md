---
name: modeling-portfolio-risk-decomposition
language: en
description: Decomposes portfolio risk with factor attribution, idiosyncratic risk, and marginal contribution to risk analysis. Use when decomposing portfolio risk, attributing risk sources, or analyzing factor risk contribution.
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
# Modeling Portfolio Risk Decomposition

## When To Use

- Decomposing total portfolio variance into systematic (factor) and idiosyncratic (security-specific) components
- Attributing risk to individual factors (market, size, value, momentum, sector, rates, credit spread, etc.)
- Computing marginal contribution to risk (MCTR) and component contribution to risk (CCTR) for position-level decisions
- Evaluating whether portfolio risk budget aligns with intended factor tilts
- Preparing risk reports for investment committees, risk oversight, or investor communications
- Stress-testing factor exposure drift after rebalancing or new allocations

## Inputs To Gather

- **Position-level holdings**: Weights (w_i) for each security or asset in the portfolio
- **Factor exposure matrix (B)**: Security-level loadings on each factor (from regression, fundamental model, or vendor such as Barra/Axioma/Northfield)
- **Factor covariance matrix (F)**: Covariance among systematic factors over the chosen estimation window
- **Idiosyncratic variance matrix (D)**: Diagonal matrix of security-specific residual variances
- **Return series** (if estimating from scratch): Daily or monthly total returns for holdings and candidate factor proxies
- **Benchmark** (optional): Benchmark weights for active risk decomposition
- **Lookback window and frequency**: e.g., 252 trading days daily, 60 months monthly — confirm consistency with factor model vintage [VERIFY]

## Workflow

1. **Assemble the covariance structure**
   - Total portfolio covariance: V = B F Bᵀ + D
   - Confirm dimensions match (n securities × k factors)
   - If using a vendor model, verify the factor covariance vintage date matches the holdings date [VERIFY]

2. **Compute total portfolio variance**
   - σ²_p = wᵀ V w
   - Report as annualized volatility: σ_p = √(σ²_p × annualization scalar)
   - Typical annualization: ×252 for daily, ×12 for monthly returns

3. **Decompose into systematic and idiosyncratic**
   - Systematic variance: σ²_sys = wᵀ (B F Bᵀ) w
   - Idiosyncratic variance: σ²_idio = wᵀ D w
   - Report the ratio σ²_sys / σ²_p — well-diversified equity portfolios typically show 85–95% systematic; significantly lower values signal concentrated idiosyncratic bets

4. **Factor-level risk attribution**
   - Portfolio factor exposures: β_p = Bᵀ w (k × 1 vector)
   - Factor contribution to variance for factor j: β_p,j × Σ_k (F_jk × β_p,k)
   - Sum of all factor contributions should equal σ²_sys (use as a reconciliation check)
   - Rank factors by absolute contribution to identify dominant risk drivers

5. **Marginal contribution to risk (MCTR)**
   - MCTR_i = (V w)_i / σ_p — measures how a small increase in weight_i changes portfolio volatility
   - Component contribution to risk: CCTR_i = w_i × MCTR_i
   - Verify: Σ CCTR_i = σ_p (Euler decomposition identity)

6. **Active risk decomposition** (if benchmark provided)
   - Active weights: w_a = w_portfolio − w_benchmark
   - Tracking error: TE = √(w_aᵀ V w_a × annualization)
   - Decompose TE into factor-active and stock-specific-active components using the same B F Bᵀ + D split
   - Report active factor bets and their contribution to tracking error

7. **Sensitivity and stress analysis**
   - Shock individual factor returns (e.g., +/−1σ, +/−2σ) and recompute portfolio P&L impact
   - Test covariance regime shifts: substitute a crisis-period F (e.g., 2008, 2020 March) and recompute σ_p
   - Evaluate concentration: flag any single factor contributing >40% of total variance or any single name contributing >10% of CCTR

## Output

- **Risk summary table**: Total volatility, systematic vs. idiosyncratic split (absolute and percentage)
- **Factor attribution table**: Each factor's exposure, variance contribution, and percentage of total risk — sorted by magnitude
- **MCTR / CCTR table**: Per-position marginal and component contributions, highlighting top-10 risk contributors
- **Active risk panel** (if applicable): Tracking error, factor-active vs. stock-specific-active decomposition
- **Stress scenario results**: Portfolio impact under specified factor shocks and regime covariance matrices
- **Reconciliation checks**: Confirm variance decomposition sums match total; flag discrepancies >0.1%

## Quality Checks

- Factor contributions sum to systematic variance within rounding tolerance
- CCTR values sum to total portfolio volatility (Euler identity holds)
- No negative idiosyncratic variances (indicates data or model error)
- Lookback window is consistent across factor model, covariance estimation, and holdings snapshot [VERIFY]
- Factor model covers ≥90% of portfolio NAV by weight; flag uncovered positions and their assumed treatment (benchmark proxy, peer mapping, or exclusion)
- Cross-check volatility estimate against realized rolling volatility — deviations >30% warrant investigation
- If using third-party risk model, confirm model version and release date match intended analysis period [VERIFY]
