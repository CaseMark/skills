---
name: analyzing-housing-markets
description: Structures housing market analysis with price trends, inventory dynamics, and affordability metrics. Use when analyzing housing data, tracking home prices, or assessing affordability.
tags:
  - analysis
  - economic-analysis
metadata:
  author: casemark
  practice_areas:
    - Economic Research
    - Macroeconomics
    - Policy Analysis
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Housing Markets

Structures housing market analysis with price trends, inventory dynamics, and affordability metrics for a defined geography and time horizon.

## When To Use

- Evaluating residential real estate conditions in a metro, state, or national market
- Tracking home price trajectories and identifying inflection points
- Assessing housing affordability for policy briefs or investment memos
- Comparing supply-demand dynamics across submarkets or time periods
- Supporting macro forecasts that depend on housing-sector inputs (GDP, consumer wealth, construction employment)

## Inputs To Gather

- **Geographic scope**: Metro/MSA, county, ZIP, or national; specify whether single-market or comparative
- **Time frame**: Historical lookback period and forward projection horizon (if any)
- **Price data**: Median sale price, price-per-square-foot, repeat-sale indices (Case-Shiller, FHFA HPI) [VERIFY data vintage and seasonal adjustment method]
- **Inventory data**: Active listings, months of supply, new listings rate, days on market
- **Construction data**: Housing starts, building permits, completions (single-family vs. multifamily split)
- **Demand-side inputs**: Population/migration trends, employment growth, household formation rates, mortgage rate environment
- **Affordability inputs**: Median household income, mortgage payment-to-income ratio, rent-to-own breakeven, first-time buyer qualification thresholds
- **Policy context**: Zoning changes, rent control measures, tax incentives, GSE policy shifts [VERIFY jurisdiction-specific rules]

## Workflow

1. **Define scope and baseline**
   - Confirm target geography, time window, and purpose (investment, policy, macro research)
   - Select appropriate price index — Case-Shiller for major metros, FHFA HPI for broader coverage, Zillow ZHVI for ZIP-level granularity [VERIFY index methodology matches use case]
   - Establish a baseline period for year-over-year and cycle-peak comparisons

2. **Analyze price trends**
   - Compute nominal and real (inflation-adjusted) price growth rates
   - Decompose price movement: organic demand vs. constrained supply vs. speculative activity
   - Identify divergences between asking prices, pending sale prices, and closed sale prices as leading indicators
   - Flag markets where price-to-rent ratios exceed historical norms by >1 standard deviation

3. **Assess inventory dynamics**
   - Calculate months of supply (active inventory ÷ monthly closed sales); benchmark: <3 months = seller's market, 3–6 = balanced, >6 = buyer's market
   - Track new-listing flow rate vs. absorption rate to detect tightening or loosening
   - Evaluate construction pipeline: permits issued vs. completions, typical lag of 12–18 months for single-family
   - Note distressed inventory share (foreclosures, short sales) and REO-to-listing conversion rates

4. **Compute affordability metrics**
   - **Payment-to-income ratio**: Monthly PITI on median-priced home ÷ median household monthly income; stress-test at current rate and +100 bps
   - **NAR Affordability Index** or equivalent: qualifying income vs. actual median income [VERIFY which index version the audience expects]
   - **Rent-vs-buy breakeven**: Compare all-in ownership cost (PITI + maintenance + opportunity cost of down payment) to equivalent rent; compute breakeven holding period
   - Segment by buyer profile: first-time (5% down, FHA) vs. move-up (20% down, conventional)

5. **Evaluate macro and policy drivers**
   - Map mortgage rate sensitivity: estimate price elasticity per 50 bps rate change using historical regressions or rule-of-thumb (1 pp rate rise ≈ 8–10% purchasing-power decline)
   - Incorporate employment and wage growth forecasts for the target market
   - Assess demographic tailwinds/headwinds: millennial household formation, baby-boomer downsizing, net migration
   - Flag pending regulatory or tax changes that could shift supply or demand [VERIFY effective dates and jurisdictions]

6. **Synthesize and stress-test**
   - Assign a market characterization: overheated / healthy appreciation / stagnant / correcting
   - Run scenario analysis: base case, rate-shock, recession, supply-surge
   - Highlight leading indicators to watch for thesis confirmation or invalidation (e.g., permits trend, pending sales momentum, cancellation rates)

## Output

- **Executive summary**: 2–3 sentences stating market characterization, key price trend, and primary risk factor
- **Price trend section**: Charts or tables showing nominal/real appreciation, index comparisons, and price-tier segmentation
- **Supply-demand dashboard**: Months of supply, listing velocity, construction pipeline summary
- **Affordability scorecard**: Payment-to-income ratio, rent-vs-buy breakeven, qualification thresholds by buyer segment
- **Risk and scenario matrix**: Base, upside, and downside scenarios with trigger indicators
- **Data sources and limitations**: Enumerated sources, data lags, and seasonal-adjustment caveats

## Quality Checks

- Confirm all price series are consistently seasonally adjusted (or explicitly not) — do not mix adjusted and unadjusted data
- Verify that affordability calculations use contemporaneous income data, not stale Census estimates [VERIFY ACS vintage]
- Cross-check months-of-supply calculation against at least two sources to catch listing-count discrepancies
- Ensure real price adjustments use CPI-U (or CPI-Shelter if isolating housing) and state the deflator used
- Flag any data gap >2 months in time series; interpolated values must be marked [VERIFY]
- Confirm that comparative analyses use the same geography definition (MSA boundaries shift across Census vintages)
- Review scenario assumptions for internal consistency — a recession scenario should pair lower demand with rising unemployment, not just a rate shock
