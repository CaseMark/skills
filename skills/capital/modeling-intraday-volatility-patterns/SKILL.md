---
name: modeling-intraday-volatility-patterns
language: en
description: Analyzes intraday volatility dynamics with open/close effects, lunch-time patterns, and event-driven volatility estimation. Use when modeling intraday volatility, timing order execution, or analyzing time-of-day effects.
tags:
  - modeling
  - public-markets-and-trading
metadata:
  author: casemark
  practice_areas:
    - Trading
    - Market Making
    - Execution
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Intraday Volatility Patterns

## When To Use

- Constructing volatility curves across the trading day for VWAP/TWAP execution scheduling
- Estimating open-auction and close-auction volatility premiums for order sizing
- Quantifying lunch-time liquidity troughs and their impact on spread and slippage
- Building event-window volatility overlays (e.g., FOMC announcements, earnings releases, index rebalances)
- Calibrating intraday risk limits or dynamic hedging intervals for market-making books

## Inputs To Gather

- **Tick or bar data**: Trade prices and volumes at 1-min (or finer) intervals for the target instrument(s); minimum 60 trading days for stable seasonality estimates
- **Session boundaries**: Exchange open/close times, auction windows, early-close calendar [VERIFY against exchange-specific schedules]
- **Event calendar**: Scheduled macro releases (FOMC, NFP, CPI), earnings dates, index rebalance dates, options expiration dates
- **Reference volatility**: Daily realized volatility (close-to-close or Yang-Zhang) and implied volatility term structure for normalization
- **Market structure context**: Tick size, lot size, average daily volume, primary vs. consolidated feed [VERIFY for each venue/asset class]

## Workflow

1. **Clean and align data**
   - Remove pre-market / after-hours prints unless explicitly modeling extended sessions
   - Align timestamps to exchange time; handle daylight-saving shifts
   - Filter obvious bad ticks (price > 3× median absolute deviation from rolling median)

2. **Compute raw intraday volatility profile**
   - Calculate return variance per interval bin (e.g., each 5-min bucket across all sample days)
   - Use Garman-Klass or Parkinson estimators on OHLC bars for efficiency when tick data is sparse
   - Normalize each day's profile by that day's total realized variance to isolate the seasonal shape from the level

3. **Estimate the U-shape (or W-shape) seasonal component**
   - Average the normalized variance profiles across the sample to extract the deterministic intraday pattern
   - Confirm the characteristic open spike, mid-morning decay, possible lunch trough, and closing ramp
   - Fit a flexible functional form (Fourier series with 3–5 harmonics, or cubic spline with knots at open, 10:00, 12:00, 14:00, close) for smooth interpolation

4. **Overlay event-driven adjustments**
   - Partition sample days into event vs. non-event subsets
   - Compute the incremental variance ratio at each interval during event windows (e.g., ±30 min around FOMC release)
   - Express event impact as a multiplicative scaling factor on the baseline seasonal curve

5. **Validate the model**
   - Hold out the most recent 20% of trading days for out-of-sample testing
   - Compare predicted interval variance to realized interval variance; report RMSE and mean absolute percentage error per bucket
   - Check that the model correctly ranks high-vol vs. low-vol intervals at least 80% of the time (concordance test)
   - Stress-test on known anomaly days (flash crashes, circuit-breaker halts) to confirm degradation is bounded

6. **Produce outputs and integrate**
   - Generate a per-interval volatility multiplier table (baseline + event-adjusted) for use in execution algorithms
   - Derive recommended participation-rate adjustments: increase participation during low-vol intervals, reduce during spikes to limit impact
   - Package as a callable function or lookup table consumable by the OMS/EMS

## Output

- **Intraday volatility curve**: Normalized variance (or standard deviation) by interval, with confidence bands
- **Event overlay table**: Multiplicative volatility scalars keyed by event type and time-offset from release
- **Execution timing recommendations**: Suggested participation-rate schedule or optimal slice boundaries for VWAP/IS algos
- **Model diagnostics**: Out-of-sample fit statistics, residual autocorrelation plots, day-type breakdown (Monday effect, triple-witching, etc.)
- **Assumptions log**: Data window, estimator choice, outlier-filter parameters, event classification rules

## Quality Checks

- Confirm the seasonal curve integrates to 1.0 (variance shares must sum to total daily variance)
- Verify open and close buckets show statistically significant elevation vs. midday (t-test or bootstrap)
- Ensure event scaling factors are estimated on ≥ 15 event instances to avoid small-sample bias [VERIFY for less-frequent events like Fed emergency meetings]
- Cross-check volatility levels against implied volatility for the same tenor; flag divergences > 2 vol points
- Validate that lunch-trough depth is consistent with observed spread widening in the underlying market data
- Mark any asset-class-specific assumptions (e.g., equity vs. futures session times, FX 24-hour cycle) with [VERIFY]
