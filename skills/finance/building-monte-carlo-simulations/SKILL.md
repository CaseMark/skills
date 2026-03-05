---
name: building-monte-carlo-simulations
description: Constructs Monte Carlo simulation frameworks with variance reduction and convergence analysis. Use when building MC simulations, implementing variance reduction, or assessing simulation accuracy.
tags:
  - modeling
  - quantitative-finance
metadata:
  author: casemark
  practice_areas:
    - Derivatives
    - Quantitative Analysis
    - Structured Products
  document_types:
    - Model
  skill_modes:
    - Modeling
---
# Building Monte Carlo Simulations

## When To Use

- Pricing path-dependent derivatives (Asian options, barrier options, lookbacks) where closed-form solutions are unavailable or unreliable
- Valuing structured products with complex payoff profiles, callable features, or multi-asset underlyings
- Estimating portfolio VaR/CVaR distributions under fat-tailed or correlated scenarios
- Modeling credit exposure profiles (PFE, EPE, EE) for counterparty risk
- Stress-testing structured note payoffs across thousands of market scenarios
- Validating or benchmarking analytical pricing models against simulation-based estimates

## Inputs To Gather

- **Underlying dynamics**: Stochastic process specification (GBM, Heston, SABR, local vol, jump-diffusion) with calibrated parameters (vol surface, mean-reversion speed, vol-of-vol, correlation matrix)
- **Payoff definition**: Terminal vs. path-dependent; barrier levels, averaging windows, autocall triggers, coupon schedules
- **Market data**: Spot prices, yield curves (OIS, SOFR), dividend schedules, credit spreads, FX rates as of valuation date
- **Simulation parameters**: Number of paths (N), time steps per path (M), time horizon, random seed policy
- **Variance reduction goals**: Target standard error, acceptable runtime budget, whether antithetic/control variate baselines exist
- **Discounting convention**: Risk-neutral vs. real-world measure; deterministic vs. stochastic rates [VERIFY: confirm measure and curve choice with desk]

## Workflow

1. **Specify the stochastic model**
   - Select the SDE(s) governing each risk factor (equity, rate, credit, FX)
   - Confirm calibration inputs: implied vol surface, correlation matrix, mean-reversion parameters
   - For multi-factor models, define the correlation structure and any factor reduction (PCA truncation)

2. **Design the path generation engine**
   - Choose discretization scheme: Euler-Maruyama for simple diffusions, Milstein or QE (quadratic-exponential) for Heston, log-Euler for GBM
   - Set time-step granularity — finer steps for barrier monitoring, coarser for vanilla European payoffs
   - Generate correlated normals via Cholesky decomposition of the correlation matrix
   - Implement random number generation with reproducible seeding (Mersenne Twister or Sobol sequences for quasi-MC)

3. **Implement variance reduction techniques**
   - **Antithetic variates**: Mirror each standard normal draw; halves variance for monotone payoffs at negligible cost
   - **Control variates**: Use a correlated instrument with known analytical price (e.g., vanilla European as control for an Asian option); estimate optimal beta coefficient from pilot run
   - **Importance sampling**: Shift drift to concentrate paths in the region that drives payoff variance (useful for deep OTM options or rare default scenarios)
   - **Stratified sampling**: Partition the uniform space into equal-probability strata; draw one sample per stratum to eliminate clustering
   - **Quasi-random sequences** (Sobol, Halton): Replace pseudo-random draws for faster convergence (O(1/N) vs. O(1/sqrt(N))); apply Brownian bridge construction to concentrate low-discrepancy benefit on key time steps

4. **Compute payoffs and discount**
   - Evaluate the payoff function along each simulated path (handle path-dependency: running max/min, arithmetic average, barrier crossings)
   - Discount each path payoff to valuation date using the appropriate curve
   - For American/Bermudan exercise, implement Longstaff-Schwartz (least-squares MC) regression at each exercise date

5. **Assess convergence and accuracy**
   - Compute sample mean and standard error: SE = sample_std / sqrt(N)
   - Build 95% and 99% confidence intervals around the price estimate
   - Run convergence diagnostics: plot price estimate vs. N; confirm SE decays at expected rate
   - Compare against closed-form benchmarks where available (Black-Scholes for vanillas, Heston semi-analytical for Europeans)
   - If SE exceeds tolerance, increase N or layer additional variance reduction before reporting

6. **Compute Greeks via simulation**
   - **Bump-and-reprice**: Shift each input parameter (spot, vol, rate) by a small delta; re-run simulation with same random seeds; finite-difference the prices
   - **Pathwise (IPA) method**: Differentiate the payoff along each path analytically for smooth payoffs — faster and lower variance than bump-and-reprice
   - **Likelihood ratio method**: For discontinuous payoffs (digitals, barriers) where pathwise fails
   - Report delta, gamma, vega, rho, theta with associated standard errors

## Output

- **Price estimate** with standard error, confidence interval, and number of paths used
- **Greeks table**: Delta, gamma, vega, rho, theta (with SEs) for each relevant risk factor
- **Convergence report**: SE vs. N plot, variance reduction efficiency ratios (variance with/without each technique)
- **Model specification summary**: SDE choice, discretization scheme, calibration inputs, time-step count
- **Assumptions and limitations log**: Which simplifications were made (constant rates, flat dividend yield, no jumps), and their expected impact on accuracy

## Quality Checks

- Confirm the simulation reproduces known analytical prices for vanilla test cases within 2 SEs
- Verify put-call parity holds (for European-style instruments) across simulated prices
- Check that antithetic/control variate application actually reduces SE (compare with and without)
- Validate that increasing N by 4x roughly halves the standard error (confirms sqrt(N) convergence)
- Ensure correlation matrix is positive semi-definite before Cholesky decomposition; flag and correct if not
- For barrier options, confirm that finer time steps reduce barrier-crossing bias (continuity correction applied where appropriate) [VERIFY: barrier monitoring frequency vs. contractual observation dates]
- Cross-check Greeks against analytical Greeks or trader intuition for sign and magnitude
- Confirm random seed reproducibility: identical seeds produce identical prices across runs
