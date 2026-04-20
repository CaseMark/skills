---
name: modeling-transaction-cost-analysis
language: en
description: Builds TCA frameworks with implementation shortfall, VWAP comparison, and market impact estimation across asset classes. Use when conducting TCA, measuring execution quality, or analyzing trading costs.
tags:
  - modeling
  - public-markets-and-trading
  - trading
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
# Modeling Transaction Cost Analysis

Builds TCA frameworks with implementation shortfall, VWAP comparison, and market impact estimation across asset classes.

## When To Use

- Evaluating execution quality for a completed trade or batch of orders against decision-price, VWAP, TWAP, or arrival-price benchmarks
- Estimating pre-trade market impact and optimal execution horizon for a proposed block or portfolio transition
- Comparing broker/algo performance across venues, time periods, or order-routing strategies
- Building or refining an ongoing TCA reporting framework for a trading desk, fund, or transition manager
- Responding to best-execution obligations under MiFID II, SEC Rule 606, or equivalent regulatory regimes [VERIFY jurisdiction-specific rules]

## Inputs To Gather

- **Order/execution data**: timestamps (order entry, first fill, last fill), side, quantity, limit price, filled quantity, average fill price, venue/broker tags
- **Market data**: consolidated bid/ask/mid at decision time, arrival time, and fill times; intraday VWAP and TWAP series; daily ADV and volatility for each instrument
- **Benchmark selection**: confirm which benchmarks are relevant (implementation shortfall, interval VWAP, close price, participation-weighted price)
- **Asset class specifics**: equity tick data differs from FX spot/forward, listed derivatives, or fixed-income RFQ workflows — confirm instrument universe
- **Cost components to isolate**: explicit costs (commissions, exchange fees, taxes, clearing) vs. implicit costs (spread, market impact, delay/timing cost, opportunity cost)
- **Grouping dimensions**: by broker, algorithm, trader, strategy, market-cap bucket, volatility regime, or time-of-day

## Workflow

1. **Normalize execution records** — align timestamps to a common clock, reconcile partial fills, and tag each execution with venue and algo identifiers. Remove or flag cancels, amendments, and erroneous prints.

2. **Calculate explicit costs** — sum commissions, SEC fees, stamp duties [VERIFY applicable fee schedules], clearing charges, and any exchange rebates/credits per order.

3. **Compute implementation shortfall (IS)** — decompose total IS into:
   - **Delay cost**: mid-price movement from decision time to order-entry time
   - **Market impact**: price movement from order entry to volume-weighted average fill price
   - **Timing cost**: price drift during the execution window attributable to market movement rather than the order itself
   - **Opportunity cost**: unfilled portion valued at closing price minus decision price
   - Express each component in basis points and in absolute currency.

4. **Run VWAP/TWAP comparison** — calculate the interval VWAP (or TWAP) over the execution window using consolidated market data; report slippage as fill price minus benchmark in bps. Flag orders where participation rate exceeded a threshold (e.g., >15% of interval volume) since benchmark validity erodes at high participation.

5. **Estimate market impact** — apply a square-root market impact model (e.g., σ × √(Q/ADV) × coefficient) calibrated to the asset class. Compare predicted impact to realized impact. If the desk has historical TCA data, fit coefficients empirically; otherwise use published coefficients [VERIFY source — common references: Almgren-Chriss, Kissell-Glantz, ITG/Virtu models].

6. **Segment and aggregate** — group results by the dimensions specified (broker, algo, trader, volatility regime, market-cap tier). Compute mean, median, and standard deviation of slippage within each group. Highlight statistically significant differences across groups.

7. **Sensitivity and regime analysis** — test how results shift under different benchmark windows, volatility bands, and participation-rate thresholds. Identify whether poor execution clusters in specific market conditions (e.g., high-vol opens, illiquid close auctions).

8. **Compile TCA report** — structure the output with an executive summary, per-benchmark scorecards, broker/algo league tables, outlier trade detail, and methodology notes.

## Output

- **Executive summary**: total explicit and implicit costs in bps and currency; headline IS and VWAP slippage across the analysis period
- **Benchmark scorecards**: IS decomposition table (delay, impact, timing, opportunity) and VWAP/TWAP slippage by instrument or portfolio segment
- **Market impact analysis**: predicted vs. realized impact scatter plot data; model fit statistics and residual analysis
- **Broker/algo league tables**: ranked performance by mean slippage, with sample size, standard deviation, and confidence intervals
- **Outlier register**: trades exceeding a defined slippage threshold with root-cause annotations (large block, illiquid name, news event, algo malfunction)
- **Methodology appendix**: benchmark definitions, model parameters, data sources, any exclusions or adjustments applied

## Quality Checks

- Confirm all timestamps are synchronized and in the same timezone; cross-check against exchange calendars for holidays and half-days
- Validate that VWAP denominators use the correct volume source (consolidated tape vs. primary exchange) [VERIFY per market convention]
- Ensure IS components sum to total IS within rounding tolerance
- Check that market impact model coefficients are appropriate for the asset class and liquidity tier — equity large-cap coefficients should not be applied to small-cap or credit instruments
- Verify that participation rate calculations exclude auction volume where appropriate
- Flag any instrument where ADV data is stale or missing — mark those rows with [VERIFY]
- Cross-reference explicit cost totals against broker confirmations or clearing statements before finalizing
