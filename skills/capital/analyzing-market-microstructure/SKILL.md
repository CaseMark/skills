---
name: analyzing-market-microstructure
language: en
description: Evaluates market structure dynamics with order book analysis, spread decomposition, and information asymmetry assessment. Use when analyzing market structure, evaluating trading venues, or assessing execution quality.
tags:
  - analysis
  - public-markets-and-trading
  - trading
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
# Analyzing Market Microstructure

Evaluates market structure dynamics with order book analysis, spread decomposition, and information asymmetry assessment.

## When To Use

- Assessing execution quality across trading venues (exchanges, ATSs, dark pools)
- Decomposing bid-ask spreads to identify adverse selection, inventory, and order-processing cost components
- Evaluating order book depth, resilience, and price impact for a specific instrument or venue
- Measuring information asymmetry between informed and uninformed flow
- Benchmarking market maker quoting behavior and fill rates
- Analyzing venue selection or smart order routing logic

## Inputs To Gather

- **Instrument identifiers** — ticker, ISIN, asset class, listing venue
- **Time window** — date range, intraday granularity (tick, second, minute)
- **Data sources** — Level I (NBBO/top-of-book), Level II (full depth), trade-and-quote (TAQ), FIX logs, or proprietary execution management system exports
- **Venue universe** — which exchanges, ECNs, ATSs, or dark pools are in scope
- **Benchmark prices** — arrival price, VWAP, TWAP, midpoint at order entry, or interval close
- **Contextual parameters** — average daily volume (ADV), volatility regime, index membership, event calendar (earnings, dividends, rebalances)

## Workflow

1. **Define scope and hypothesis**
   - Clarify whether the analysis targets a single instrument, a portfolio basket, or a venue comparison
   - State the question explicitly (e.g., "Is adverse selection cost on Venue X higher than the lit market average?")

2. **Prepare and validate data**
   - Align timestamps across sources to a common clock (exchange timestamps vs. SIP vs. direct feed) [VERIFY timestamp source and latency assumptions]
   - Filter for regular trading hours vs. pre/post-market as appropriate
   - Flag stale quotes, crossed/locked markets, and obvious outliers (e.g., clearly erroneous prints)

3. **Compute spread decomposition**
   - **Quoted spread** — best ask minus best bid at each observation point
   - **Effective spread** — 2 × |trade price − midpoint at time of trade|, signed by aggressor side
   - **Realized spread** — effective spread minus price impact measured at a fixed horizon (e.g., 5 seconds, 1 minute, 5 minutes) [VERIFY horizon convention used by the desk]
   - **Price impact (adverse selection component)** — effective spread minus realized spread
   - Report each in absolute terms and in basis points of midpoint

4. **Analyze order book dynamics**
   - Depth at best: average displayed size at NBBO across the observation window
   - Depth beyond best: cumulative size within N ticks or basis points of midpoint
   - Book imbalance: (bid size − ask size) / (bid size + ask size) at top of book and deeper levels
   - Resilience: time for the book to replenish after a large trade or sweep
   - Quote-to-trade ratio and cancel-to-fill ratio by venue

5. **Assess information asymmetry**
   - Probability of informed trading (PIN) model or volume-synchronized PIN (VPIN) if data supports it [VERIFY whether tick data granularity is sufficient for PIN estimation]
   - Toxicity metrics: adverse selection per share by order flow segment (retail, institutional, algorithmic)
   - Correlation between order flow imbalance and subsequent price moves at multiple horizons

6. **Venue and execution quality comparison**
   - Effective-over-quoted spread ratio by venue (values near 1.0 suggest minimal price improvement)
   - Fill rate, time-to-fill, and partial fill frequency
   - Venue-specific price improvement statistics (dark pool midpoint fills vs. lit executions)
   - Segmentation of flow: maker vs. taker, displayed vs. non-displayed

7. **Synthesize findings**
   - Rank venues or time periods by cost and toxicity metrics
   - Identify structural drivers (e.g., tick-size regime, maker-taker vs. inverted fee schedule, speed bumps)
   - Note any regime sensitivity (e.g., metrics shift materially around earnings or high-volatility events)

## Output

Deliver a structured **Market Microstructure Analysis Report** containing:

- **Executive summary** — one paragraph stating the key finding and its trading/execution implication
- **Spread decomposition table** — quoted, effective, realized spreads and adverse selection component by venue and time period
- **Order book profile** — depth charts, imbalance time series, resilience statistics
- **Information asymmetry metrics** — PIN/VPIN estimates, toxicity breakdown by flow type
- **Venue comparison matrix** — side-by-side metrics (spread, fill rate, price improvement, latency)
- **Recommendations** — actionable changes to venue selection, order type usage, or timing strategy
- **Appendix** — data sources, timestamp conventions, parameter choices, and any [VERIFY] items requiring desk confirmation

## Quality Checks

- Confirm that effective spread is never negative (sanity check on trade-side classification; Lee-Ready or similar algorithm should be documented)
- Verify that realized spread + adverse selection component = effective spread within rounding tolerance
- Cross-check volume totals against consolidated tape to ensure no missing prints
- Ensure venue-level metrics sum or average correctly to the aggregate
- Flag any period where spread metrics are distorted by halts, circuit breakers, or auction-only sessions [VERIFY halt/auction handling]
- Validate that PIN/VPIN estimates use sufficient sample size and that confidence intervals are reported
- Confirm fee schedule assumptions (maker-taker, payment for order flow) are current [VERIFY exchange fee schedules effective date]
