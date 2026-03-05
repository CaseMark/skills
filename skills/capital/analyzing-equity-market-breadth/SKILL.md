---
name: analyzing-equity-market-breadth
description: Evaluates market breadth with advance-decline analysis, new high/low tracking, and sector participation assessment. Use when analyzing market breadth, assessing rally quality, or identifying divergences.
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
# Analyzing Equity Market Breadth

## When To Use

- Assessing whether a rally or selloff is broad-based or narrow (e.g., concentrated in mega-cap tech)
- Identifying breadth divergences that precede trend reversals (index making new highs while fewer stocks participate)
- Evaluating sector rotation patterns and capital flow shifts across market segments
- Screening for deteriorating internals beneath a stable headline index level
- Supporting risk-on / risk-off allocation decisions with participation data

## Inputs To Gather

- **Advance-decline data**: Daily advancers vs. decliners for the target index or exchange (NYSE, NASDAQ, or composite) [VERIFY exchange-specific data source and reporting cutoff time]
- **Cumulative A/D line**: Running sum of net advances to establish trend direction
- **New 52-week highs and lows**: Daily counts, ideally broken out by exchange
- **Sector-level performance**: Returns and A/D ratios for each GICS sector (or equivalent classification)
- **Volume breadth**: Up-volume vs. down-volume ratios to weight participation by capital commitment
- **Index composition details**: Number of constituents, weighting scheme (cap-weighted, equal-weighted), top-N concentration
- **Time horizon**: Intraday, daily, weekly, or multi-week lookback depending on the analysis purpose

## Workflow

1. **Establish baseline context**
   - Identify the index or universe under analysis (S&P 500, Russell 2000, NASDAQ Composite, etc.)
   - Note the weighting methodology — cap-weighted indices can mask breadth weakness when a handful of large names drive returns
   - Record the analysis date range and comparison periods

2. **Compute advance-decline metrics**
   - Calculate daily net advances (advancers minus decliners) and the cumulative A/D line
   - Compare A/D line trend to the price trend of the headline index — flag divergences where the index rises but the A/D line flattens or declines
   - Compute the A/D ratio (advancers / decliners) and note readings above 2:1 (strong breadth) or below 0.5:1 (weak breadth)

3. **Analyze new high / new low data**
   - Track the daily count of new 52-week highs minus new 52-week lows (NH-NL differential)
   - A rising index with a shrinking NH-NL differential signals narrowing leadership
   - Sustained negative NH-NL readings during an index advance are a classic bearish divergence signal

4. **Assess sector participation**
   - Determine how many of the 11 GICS sectors are trading above their 50-day and 200-day moving averages
   - Identify which sectors are leading vs. lagging — defensive sector leadership (utilities, staples, healthcare) during a rally often signals fragile breadth
   - Flag any single sector contributing a disproportionate share of index returns

5. **Evaluate volume breadth**
   - Compare up-volume to down-volume; readings above 90% up-volume ("breadth thrust") are historically bullish confirmation signals [VERIFY specific threshold definitions per the indicator variant used]
   - Persistent low up-volume ratios during price advances suggest lack of conviction

6. **Synthesize and classify breadth regime**
   - Classify the current environment: broad participation, narrowing breadth, divergence, or breadth thrust
   - Identify the most actionable signal (e.g., "A/D line divergence persisting for 3+ weeks while index is within 1% of highs")
   - Note any historical analogs if relevant

## Output

- **Breadth Summary Table**: Date range, index, A/D ratio, cumulative A/D line trend, NH-NL differential, sectors above 50-DMA / 200-DMA, up-volume ratio
- **Divergence Flags**: Explicit callouts where breadth metrics conflict with headline index direction, with severity rating (early, developing, confirmed)
- **Sector Participation Map**: Heatmap or ranked list showing sector-level breadth contribution
- **Signal Classification**: Current breadth regime label with supporting evidence
- **Actionable Implications**: What the breadth picture suggests for position sizing, hedging, or sector rotation — framed for trading and execution desks

## Quality Checks

- Confirm data covers the full trading session (not partial or pre-market only) [VERIFY data source timestamp conventions]
- Cross-check A/D data against at least one independent source to catch reporting errors
- Ensure new high/low counts use a consistent lookback window (52-week standard; some sources use shorter periods)
- Verify that sector breakdowns use the same index universe — mixing S&P 500 sector data with Russell 2000 index-level data produces misleading conclusions
- Flag any days with unusual market structure events (half-days, index rebalances, options expiration) that distort breadth readings
- Do not present breadth signals as predictive with certainty — note historical base rates and false-positive frequency where available
