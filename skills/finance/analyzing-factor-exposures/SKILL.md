---
name: analyzing-factor-exposures
description: Decomposes portfolio factor exposures (value, growth, momentum, quality, size) with benchmark relative analysis. Use when analyzing factor tilts, decomposing returns, or managing style exposure.
tags:
  - analysis
  - asset-management
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
# Analyzing Factor Exposures

## When To Use

- Decomposing a portfolio's return drivers into systematic factor components (value, growth, momentum, quality, size, volatility)
- Evaluating active factor tilts relative to a benchmark (e.g., Russell 1000 Value, MSCI World)
- Diagnosing unintended style drift or concentration in factor bets
- Preparing factor attribution reports for investment committee or client review
- Stress-testing portfolio sensitivity to factor regime changes (e.g., value-to-growth rotation)

## Inputs To Gather

- **Portfolio holdings** — full position list with weights, sector, market cap, and identifiers (CUSIP/ISIN/ticker)
- **Benchmark composition** — constituent weights for the comparison index
- **Factor model specification** — which model to use (Barra, Fama-French 3/5-factor, AQR, proprietary) and factor definitions
- **Time horizon** — point-in-time snapshot vs. rolling window analysis; specify lookback period for return-based decomposition
- **Return series** (if return-based) — portfolio and benchmark total returns at the required frequency (daily/monthly)
- **Risk model data** — covariance matrix, factor returns, and specific risk estimates if available
- **Analysis date / rebalance date** — as-of date for holdings-based exposure calculation

## Workflow

1. **Validate holdings data** — Confirm position weights sum to ~100% (or expected net/gross for long-short). Flag any missing identifiers, stale prices, or unclassified securities. Mark gaps with [VERIFY].
2. **Map securities to factor characteristics** — For each holding, assign factor scores:
   - **Value**: P/E, P/B, EV/EBITDA, dividend yield, earnings yield
   - **Growth**: Earnings growth rate, revenue growth, forward EPS estimates
   - **Momentum**: 12-1 month trailing return, relative strength
   - **Quality**: ROE, debt-to-equity, earnings stability, accruals ratio
   - **Size**: Log market capitalization
   - **Volatility** (optional): Realized vol, beta, idiosyncratic risk
3. **Calculate portfolio-level exposures** — Compute weighted-average factor z-scores or loadings for the portfolio. Repeat for the benchmark. Derive active exposure as portfolio minus benchmark on each factor.
4. **Run factor return decomposition** (if return-based):
   - Regress excess portfolio returns against factor return series
   - Report factor betas, t-statistics, and R-squared
   - Separate systematic return (sum of factor contributions) from residual alpha
5. **Identify active tilts and outliers**:
   - Rank factors by magnitude of active exposure
   - Flag any single-factor tilt exceeding a materiality threshold (e.g., >0.5 standard deviations active)
   - Identify top/bottom holdings driving each factor tilt
6. **Assess factor interaction and crowding**:
   - Check for correlated factor bets (e.g., simultaneous value + low-momentum creating a "value trap" exposure)
   - Note factor crowding risk if portfolio holdings overlap heavily with popular factor ETFs or indices
7. **Contextualize with regime analysis** — Compare current factor tilts against recent factor performance and macro regime (rising rates favor value, risk-on favors momentum). Note whether tilts are intentional or residual.

## Output

Structure the factor exposure report with:

- **Executive Summary** — One paragraph: dominant factor tilts, largest active bets, and key risk observation
- **Factor Exposure Table** — Columns: Factor | Portfolio Score | Benchmark Score | Active Exposure | Percentile Rank (vs. history)
- **Top Contributors by Factor** — For each material factor tilt, list the 5 holdings contributing most to the active exposure with their individual factor scores and portfolio weights
- **Return Attribution** (if applicable) — Factor-by-factor contribution to period return, with residual/alpha component
- **Style Drift Indicator** — Rolling 12-month factor exposure chart description or data showing how tilts have evolved
- **Risk Observations** — Unintended bets, factor crowding concerns, concentration in correlated factors
- **Recommendations** — Specific rebalancing actions to reduce unintended exposures or increase intended tilts, with estimated trade size

## Quality Checks

- Portfolio and benchmark weights reconcile (sum check, sector coverage)
- Factor scores sourced from consistent vendor/model across all holdings — do not mix Barra and Fama-French scores in the same analysis
- Active exposures are expressed in comparable units (z-scores, standard deviations, or beta units) — state which
- Return-based regressions use a sufficient observation window (minimum 36 months for monthly data) [VERIFY appropriateness for specific factor model]
- All factor definitions match the stated model specification — confirm whether "value" means P/B (Fama-French) vs. composite (Barra) [VERIFY]
- Flag any holdings representing >2% of portfolio weight that lack factor score coverage
- Distinguish between holdings-based (point-in-time) and return-based (through-time) exposures — do not conflate the two methodologies
- Verify benchmark is appropriate for the portfolio's investment mandate before computing active tilts [VERIFY mandate/benchmark alignment]
