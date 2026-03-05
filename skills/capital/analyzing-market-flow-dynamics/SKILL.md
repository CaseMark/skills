---
name: analyzing-market-flow-dynamics
description: Evaluates institutional flow patterns with fund flow analysis, positioning data, and sentiment indicator synthesis. Use when analyzing market flows, tracking institutional positioning, or assessing market sentiment.
tags:
  - analysis
  - public-markets-and-trading
metadata:
  author: casemark
  practice_areas:
    - Trading
    - Market Making
    - Execution
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Market Flow Dynamics

Evaluates institutional flow patterns by synthesizing fund flow data, positioning reports, and sentiment indicators to produce actionable intelligence for trading, market-making, and execution desks.

## When To Use

- Assessing whether institutional money is rotating into or out of a sector, asset class, or single name
- Evaluating positioning crowdedness before entering or sizing a trade
- Monitoring sentiment shifts (e.g., put/call ratios, AAII, fund manager surveys) to gauge contrarian or momentum signals
- Preparing pre-trade flow context for execution teams or portfolio managers
- Analyzing ETF creation/redemption activity as a proxy for institutional demand

## Inputs To Gather

- **Fund flow data**: EPFR, ICI, or prime broker aggregate flow reports; specify asset class, geography, and time window
- **Positioning data**: CFTC Commitments of Traders (COT), prime broker positioning snapshots, short interest reports, securities lending data
- **Sentiment indicators**: Put/call ratios (equity and index), VIX term structure, AAII/Investors Intelligence surveys, CNN Fear & Greed or equivalent composite
- **Market microstructure context**: Recent volume profiles, block trade prints, dark pool activity percentages [VERIFY data source availability and recency]
- **Scope parameters**: Asset class or instrument universe, lookback period, benchmark or reference index

## Workflow

1. **Define scope and timeframe** — Confirm which asset classes, instruments, or sectors are in scope. Agree on lookback window (e.g., trailing 1-week, 4-week, 13-week) and whether the analysis is point-in-time or trend-based.

2. **Aggregate fund flow data** — Pull net flows by fund category (equity, fixed income, commodity, money market). Decompose by geography (US, EM, Europe, Asia) and vehicle type (ETF vs. mutual fund). Flag any single-week flows that exceed ±2 standard deviations from trailing average.

3. **Assess positioning** — Review COT net speculative positioning for relevant futures contracts. Overlay prime broker or securities lending data where available. Classify positioning as light, neutral, crowded long, or crowded short relative to historical percentile ranks (e.g., 1-year and 3-year lookbacks). [VERIFY COT report date — data lags by 3 business days]

4. **Synthesize sentiment indicators** — Compile put/call ratios (5-day moving average preferred), volatility term structure slope, and survey-based sentiment. Assign each indicator a directional reading (bullish, neutral, bearish) and note any divergences between indicator categories.

5. **Identify flow-positioning-sentiment alignment or divergence** — The core analytical step. Determine whether flows, positioning, and sentiment are confirming the same directional thesis or sending conflicting signals:
   - **Aligned bullish**: Strong inflows + light/neutral positioning + bearish sentiment (contrarian buy signal)
   - **Aligned bearish**: Persistent outflows + crowded long positioning + euphoric sentiment (contrarian sell signal)
   - **Divergent**: Flag the divergence explicitly and assess which signal has historically led in the specific asset class

6. **Contextualize with microstructure** — Review volume patterns, block activity, and dark pool share. Note any unusual prints or systematic flow signatures (e.g., large delta-hedging flows, index rebalance effects, options expiration gamma exposure). [VERIFY expiration calendar for relevant derivatives]

7. **Formulate actionable conclusions** — Translate findings into directional bias, timing considerations, and risk factors. Specify confidence level (high/medium/low) and identify the key variable that could invalidate the thesis.

## Output

Structure the deliverable as follows:

- **Executive Summary** (2–3 sentences): Directional bias, confidence level, and primary driver
- **Flow Analysis**: Net flows by category with trend context; highlight outlier weeks
- **Positioning Assessment**: Current positioning percentile ranks with crowdedness flags
- **Sentiment Dashboard**: Indicator readings in a compact table (indicator | current | signal | historical percentile)
- **Alignment Matrix**: Summary table showing whether flows, positioning, and sentiment confirm or diverge
- **Microstructure Notes**: Relevant volume, block, or options-driven flow observations
- **Actionable Takeaway**: Recommended directional lean, key levels or triggers to monitor, and primary risk to the thesis
- **Data Limitations**: Sources used, lag periods, and any gaps flagged with [VERIFY]

## Quality Checks

- Confirm all flow data covers the same time period — mismatched windows distort the synthesis
- Verify COT and short interest data publication dates; do not treat stale data as current
- Ensure positioning percentile ranks use a consistent lookback across all instruments
- Check that sentiment indicators are not double-counted (e.g., a composite index that already includes put/call ratios should not be listed alongside standalone put/call data)
- Flag any instrument where daily volume is too thin for flow analysis to be meaningful
- Confirm that contrarian interpretations are explicitly labeled as such — do not conflate "bearish sentiment" with "bearish outlook"
- Mark jurisdiction- or exchange-specific data quirks with [VERIFY] (e.g., European short-selling disclosure thresholds differ from US)
