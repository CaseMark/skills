---
name: calculating-value-at-risk
language: en
description: Computes VaR using parametric, historical simulation, and Monte Carlo methods with backtesting validation. Use when calculating VaR, comparing risk methodologies, or backtesting risk models.
tags:
  - analysis
  - risk-management
  - risk
metadata:
  author: casemark
  practice_areas:
    - Risk Management
    - Enterprise Risk
    - Market Risk
  document_types:
    - Calculation Worksheet
  skill_modes:
    - Calculation
---
# Calculating Value At Risk

## When To Use

- Computing portfolio VaR at specified confidence levels (typically 95% or 99%) and holding periods (1-day, 10-day)
- Comparing risk estimates across parametric (variance-covariance), historical simulation, and Monte Carlo approaches
- Backtesting an existing VaR model against realized P&L to assess model adequacy
- Supporting regulatory capital calculations under Basel framework internal models approach [VERIFY: Basel III/IV applicability for jurisdiction]
- Producing risk reports for portfolio managers, risk committees, or regulators

## Inputs To Gather

- **Portfolio composition**: Asset classes, positions, notional values, currency denominations
- **Market data**: Historical returns series (minimum 1 year for historical simulation; 3-5 years preferred), closing prices, FX rates, yield curves
- **Parameters**: Confidence level (e.g., 99% for regulatory, 95% for internal), holding period, lookback window length
- **Correlation/covariance data**: Correlation matrix or raw return series for parametric method; decay factor if using exponentially weighted moving average (EWMA)
- **Distribution assumptions**: Normal, Student-t, or empirical for parametric; number of simulations and random seed for Monte Carlo
- **Benchmark P&L**: Realized daily P&L series for backtesting (minimum 250 trading days)

## Workflow

### 1. Data Preparation
- Collect and align time series to consistent trading calendar (handle holidays, missing data)
- Compute log returns or arithmetic returns (state choice and rationale)
- Check for stale prices, outliers, and corporate actions; flag gaps with [VERIFY]
- Convert multi-currency positions to base currency using consistent FX rates

### 2. Methodology Selection
- **Parametric (Variance-Covariance)**: Best for linear portfolios (equities, FX). Compute portfolio variance as w'Σw. VaR = z_α × σ_p × √(holding period). Note: assumes normal returns — underestimates tail risk for fat-tailed distributions
- **Historical Simulation**: Rank historical portfolio P&L; VaR = the (1-α) percentile loss. No distributional assumption required. Sensitive to lookback window choice — shorter windows react faster to regime changes
- **Monte Carlo**: Fit stochastic model to risk factors, simulate N paths (10,000+ recommended), revalue portfolio on each path, extract percentile. Required for portfolios with options or path-dependent instruments. Specify random number generator and variance reduction technique (antithetic variates, importance sampling)

### 3. VaR Calculation
- Run selected method(s); compute VaR at each requested confidence level and holding period
- For 10-day VaR from 1-day: use square-root-of-time scaling only if returns are i.i.d. [VERIFY: whether autocorrelation or volatility clustering invalidates scaling rule]
- Calculate Component VaR and Marginal VaR to attribute risk to individual positions or asset classes
- If running multiple methods, present side-by-side comparison table

### 4. Backtesting
- Compare realized P&L breaches against VaR predictions over the test window
- **Kupiec POF test**: Binomial test on number of exceptions vs. expected count — report p-value
- **Christoffersen test**: Check for independence of exceptions (clustered breaches indicate model failure)
- Classify model in Basel traffic-light zones: Green (0-4 exceptions at 99%/250 days), Yellow (5-9), Red (10+) [VERIFY: current regulatory thresholds for applicable regime]
- Document exception dates and magnitudes; investigate any breach exceeding 2× VaR

### 5. Stress & Sensitivity Analysis
- Compute Conditional VaR (Expected Shortfall / CVaR) as the average loss beyond VaR threshold
- Run sensitivity on key parameters: vary lookback window (250, 500, 750 days), confidence level, and decay factor
- Report how VaR changes under stressed correlation assumptions (e.g., correlations → 1 in crisis)

## Output

Produce a **VaR Calculation Worksheet** containing:

- **Summary table**: VaR figures by method, confidence level, and holding period
- **Component VaR breakdown**: Top 10 risk contributors by position or asset class
- **Backtest results**: Exception count, Kupiec p-value, Christoffersen p-value, traffic-light classification
- **CVaR / Expected Shortfall**: For each method and confidence level
- **Sensitivity table**: VaR under alternative parameter choices
- **Assumptions log**: Every distributional, data, and modeling assumption stated explicitly
- **Methodology narrative**: Plain-language explanation of approach suitable for risk committee review

## Quality Checks

- VaR at 99% must exceed VaR at 95% for the same method and holding period — flag if violated
- Component VaR values should sum approximately to diversified portfolio VaR (exact for parametric; approximate for simulation methods)
- Monte Carlo VaR should converge as simulation count increases — run at 10K and 50K and confirm difference < 5%
- Backtest exception rate should fall within 2 standard deviations of expected rate — otherwise flag model inadequacy
- Confirm holding-period scaling is appropriate: if significant autocorrelation exists in returns, do not apply square-root-of-time rule without adjustment
- Cross-check: historical simulation VaR should be broadly consistent with parametric VaR for linear portfolios with near-normal returns; large divergence signals fat tails or non-linearity
- All market data sources and observation dates must be cited; any interpolated or proxy data marked [VERIFY]
