---
name: building-custom-factor-definitions
description: Constructs proprietary factor definitions with signal specification, universe application, and orthogonalization methodology. Use when defining custom factors, creating proprietary signals, or building factor libraries.
tags:
  - modeling
  - quantitative-capital-strategies
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
# Building Custom Factor Definitions

## When To Use

- Defining a new proprietary signal (e.g., custom momentum, quality, or alternative-data factor) for systematic portfolio construction
- Extending an existing factor library with additional alpha or risk factors
- Formalizing an ad-hoc trading signal into a documented, production-ready factor definition
- Orthogonalizing a raw signal against standard risk factors (market, size, value, momentum) to isolate residual alpha
- Specifying universe filters, rebalance cadence, and neutralization rules for a new factor

## Inputs To Gather

- **Signal hypothesis**: Economic rationale for why the signal should predict returns (e.g., earnings revision momentum captures analyst under-reaction)
- **Raw data source(s)**: Vendor, frequency, history depth, point-in-time availability, and known gaps [VERIFY data lag and survivorship-bias treatment]
- **Investment universe**: Index membership, liquidity floor (e.g., minimum ADV), market-cap band, sector/country scope
- **Benchmark and risk model**: Which risk model (Barra, Axioma, in-house PCA) the factor will be orthogonalized against
- **Rebalance parameters**: Signal refresh frequency, portfolio rebalance cadence, and turnover constraints
- **Back-test window**: In-sample vs. out-of-sample date ranges; any structural-break dates to segment

## Workflow

1. **Specify the raw signal**
   - Define the formula or computation graph (e.g., `z-score of 3-month EPS revision breadth, winsorized at +/- 3σ`)
   - Document every transformation: scaling, winsorization, log-transform, lag
   - State the look-back window and decay function if applicable

2. **Apply universe and timing rules**
   - Filter the investable universe by liquidity, listing status, and sector exclusions
   - Align signal observation dates to point-in-time data availability — no look-ahead bias
   - Define the rebalance calendar (month-end, quarter-end, event-driven)

3. **Normalize and cross-section adjust**
   - Cross-sectional z-score or rank-normalize within appropriate groups (sector, country, or full universe)
   - Handle missing data: drop, fill-forward with decay, or impute with group median — document the choice
   - Winsorize or truncate outliers and state thresholds

4. **Orthogonalize against risk factors**
   - Regress the normalized signal on the chosen risk-model exposures (e.g., Barra style/industry factors)
   - Retain the residual as the pure alpha signal
   - Record R-squared and coefficient stability across rolling windows [VERIFY orthogonalization frequency matches rebalance cadence]

5. **Back-test and evaluate**
   - Construct long/short quintile or decile portfolios; compute annualized return, Sharpe ratio, IC/IR, max drawdown, and turnover
   - Split in-sample (model fitting) and out-of-sample (validation) periods
   - Run decay analysis: how quickly does signal efficacy fade after formation?
   - Check for crowding proxies (short-interest, ETF overlap) that could erode the signal forward

6. **Stress-test and robustness checks**
   - Vary look-back windows, winsorization bounds, and rebalance frequency
   - Test across sub-periods (pre/post regime changes, volatility regimes)
   - Confirm the factor is not subsumed by existing library factors (spanning test)

7. **Document the factor definition card**
   - Produce a single-page factor definition card (see Output section) plus a detailed methodology appendix

## Output

**Factor Definition Card** containing:

- **Factor name and mnemonic** (e.g., `EPS_REV_BREADTH_3M`)
- **Economic rationale** — one-paragraph hypothesis
- **Signal formula** — unambiguous mathematical or pseudo-code specification
- **Universe and rebalance rules** — eligibility criteria, calendar, turnover cap
- **Normalization method** — z-score vs. rank, group structure, outlier treatment
- **Orthogonalization spec** — risk model used, regression details, residual extraction
- **Back-test summary table** — annualized return, Sharpe, IC, IR, max drawdown, turnover (in-sample and out-of-sample)
- **Decay profile** — IC at T+1, T+5, T+20, T+60
- **Known limitations** — data gaps, regime sensitivity, crowding risk
- **Version and changelog** — factor version, author, date, and diffs from prior version

## Quality Checks

- **No look-ahead bias**: Confirm every data point is available strictly before the signal observation date
- **Point-in-time integrity**: Verify vendor timestamps; flag any restated financials or backfilled data [VERIFY]
- **Survivorship bias**: Universe must include delisted securities during the back-test window
- **Transaction cost realism**: Apply realistic spread and market-impact estimates; confirm net-of-cost Sharpe > threshold
- **Redundancy test**: Correlation with existing factor library < 0.5 (or fails spanning regression) to justify inclusion
- **Stability**: IC sign and magnitude stable across rolling 36-month windows; no single sub-period drives aggregate result
- **Reproducibility**: Another quant can recreate the signal from the definition card alone, producing matching quintile returns within rounding tolerance
