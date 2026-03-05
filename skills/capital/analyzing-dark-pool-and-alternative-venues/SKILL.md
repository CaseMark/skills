---
name: analyzing-dark-pool-and-alternative-venues
description: Evaluates alternative trading systems with fill rate analysis, information leakage assessment, and venue toxicity measurement. Use when analyzing dark pools, evaluating ATS venues, or assessing execution venue quality.
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
# Analyzing Dark Pool And Alternative Venues

Evaluates alternative trading systems with fill rate analysis, information leakage assessment, and venue toxicity measurement.

## When To Use

- Comparing execution quality across dark pools and ATS venues for order routing decisions
- Investigating information leakage or adverse selection on a specific venue
- Performing periodic venue analysis required under Rule 606 or best execution obligations
- Evaluating whether to add, remove, or re-weight a venue in smart order router (SOR) configuration
- Assessing venue toxicity after noticing degraded fill quality or increased markouts

## Inputs To Gather

- **Execution data**: Fill rates, fill sizes, time-to-fill distributions, and midpoint vs. far-touch fill ratios per venue over the analysis window (minimum 20 trading days recommended)
- **Markout data**: Short-term price reversion at standard intervals (e.g., 1s, 5s, 30s, 1min, 5min post-fill) per venue
- **Order flow profile**: Breakdown of order types routed (midpoint peg, limit, IOC, conditional) and average order size relative to venue ADV
- **Venue metadata**: ATS Form ATS-N filings, subscriber segmentation rules, anti-gaming controls, minimum quantity thresholds, and crossing logic (continuous vs. periodic) [VERIFY against current SEC EDGAR filings]
- **Benchmark data**: Arrival price, VWAP, or interval VWAP for the relevant period to contextualize fill quality
- **Market context**: Average daily volume, volatility (realized and implied), and spread regime for the securities analyzed

## Workflow

1. **Define scope and segmentation**
   - Specify the universe of securities (large-cap, mid-cap, small-cap, ETFs) and time window
   - Segment analysis by market-cap tier, spread bucket (sub-penny, 1–3¢, 3¢+), and volatility regime — venue performance varies materially across these dimensions
   - Identify the set of venues to compare (include lit exchanges as a control benchmark)

2. **Calculate fill quality metrics**
   - **Fill rate**: Orders filled / orders routed, segmented by order type and urgency
   - **Effective spread**: Execution price vs. midpoint at time of fill, expressed in bps
   - **Price improvement**: Percentage of fills that improve on the NBBO, and average improvement in mils per share
   - **Fill size ratio**: Average fill size / average order size — flags venues that consistently partial-fill
   - **Time-to-fill**: Distribution of latency from order arrival to execution; flag venues with bimodal distributions (may indicate information-dependent crossing)

3. **Assess information leakage and adverse selection**
   - Compute markout curves per venue at 1s, 5s, 30s, 1min, and 5min intervals post-execution
   - Negative markouts (price moves against you after fill) indicate adverse selection; compare venue markout to lit-exchange baseline
   - Flag venues where markout deteriorates sharply beyond 5 seconds — suggests informed flow or latency arbitrage
   - Review reversion asymmetry: if buys mark out worse than sells (or vice versa), investigate whether venue subscriber mix is skewed

4. **Measure venue toxicity**
   - Calculate **VPIN** (Volume-Synchronized Probability of Informed Trading) or similar toxicity proxy per venue if tick data is available
   - Track the ratio of aggressive-to-passive fills — high aggressive ratios may signal predatory flow
   - Evaluate the venue's **anti-gaming controls**: Does it offer minimum rest times, order randomization, periodic auctions, or size priority? Cross-reference with Form ATS-N disclosures [VERIFY current ATS-N filings for each venue]
   - Compare toxicity metrics to the venue's stated subscriber segmentation (e.g., does the venue claim to exclude high-frequency participants but show HFT-consistent markout patterns?)

5. **Benchmark and rank venues**
   - Normalize all metrics to a common scale (e.g., z-scores within each spread/size bucket)
   - Produce a composite venue scorecard weighting: fill rate (20%), effective spread (25%), markout at 1min (25%), fill size ratio (15%), toxicity score (15%) — adjust weights to reflect desk priorities
   - Rank venues within each security tier; highlight venues that rank well on fill rate but poorly on markout (classic "toxic fill" pattern)

6. **Formulate routing recommendations**
   - Recommend SOR weight adjustments: increase allocation to venues with favorable markout-adjusted fill rates, reduce or eliminate venues showing persistent adverse selection
   - Identify conditional routing rules (e.g., route to Venue X only for orders >5,000 shares where its periodic auction adds value)
   - Flag venues warranting further investigation or a probationary period before removal

## Output

Deliver a **Dark Pool & ATS Venue Analysis Report** containing:

- **Executive summary**: Top-line findings, worst/best performing venues, and headline routing changes recommended
- **Venue scorecard table**: Composite scores and component metrics per venue, segmented by security tier
- **Markout curve charts**: Overlay markout profiles across venues at standardized intervals
- **Information leakage flags**: Specific venues and security segments where adverse selection exceeds threshold (e.g., >1.5× lit baseline)
- **Routing recommendations**: Specific SOR configuration changes with expected impact on execution cost (bps saved per share)
- **Data limitations**: Note any gaps in execution data, short sample windows, or venues with insufficient fill counts for statistical significance

## Quality Checks

- Confirm markout calculations use the correct midpoint timestamp (execution time, not order arrival) — a common source of error
- Verify fill data excludes auction prints, odd lots, or other non-representative executions unless explicitly in scope
- Ensure statistical significance: venues with fewer than 100 fills per bucket should be flagged as low-confidence
- Cross-check venue-reported fill statistics (from ATS quarterly reports on FINRA) against internally computed metrics — discrepancies may indicate data feed issues [VERIFY FINRA ATS transparency data for current quarter]
- Validate that spread and markout calculations account for tick-size regime (sub-penny venues vs. tick-constrained names)
- Confirm that the analysis period does not overlap with abnormal market events (e.g., volatility spikes, exchange outages) without explicit notation
