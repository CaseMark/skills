---
name: analyzing-credit-default-swaps
language: en
description: Interprets CDS markets with basis analysis, curve dynamics, and credit event monitoring. Use when analyzing CDS spreads, monitoring credit events, or evaluating CDS basis.
tags:
  - analysis
  - fixed-income
  - credit
metadata:
  author: casemark
  practice_areas:
    - Fixed Income
    - Credit Research
    - Bond Trading
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Credit Default Swaps

Interprets CDS markets with basis analysis, curve dynamics, and credit event monitoring.

## When To Use

- Evaluating single-name or index CDS spreads for relative value or directional views
- Monitoring credit events (failure to pay, restructuring, bankruptcy) and their settlement implications
- Analyzing CDS-bond basis to identify mispricing between cash and synthetic credit exposure
- Assessing CDS curve shape (term structure) for credit deterioration or recovery signals
- Building or unwinding CDS positions as part of hedging or speculative strategies

## Inputs To Gather

- **Reference entity and tier**: Identify the reference entity, seniority (senior unsecured, subordinated), and applicable restructuring clause (CR, MR, MM, XR) [VERIFY clause convention by region — CR for North America, MM/MR common in Europe]
- **CDS spread data**: Current and historical par spreads across standard tenors (1Y, 3Y, 5Y, 7Y, 10Y); source (e.g., Markit, Bloomberg CDSW)
- **Cash bond comparables**: Comparable bond yields, asset-swap spreads, or Z-spreads for basis analysis
- **Recovery rate assumptions**: Market-implied recovery vs. historical sector recovery rates
- **Credit event triggers**: Any pending or recent ISDA Determinations Committee rulings, succession events, or restructuring notices
- **Index context**: Relevant CDS index series (CDX.NA.IG, CDX.NA.HY, iTraxx Europe) and the entity's index membership/weight

## Workflow

1. **Establish the reference entity profile**
   - Confirm ISDA documentation terms: 2003 or 2014 definitions, applicable restructuring type
   - Note the deliverable obligation characteristics and any cheapest-to-deliver (CTD) considerations
   - Identify sector, rating, and recent rating agency actions

2. **Analyze spread levels and curve dynamics**
   - Plot the CDS term structure; assess steepness or inversion
   - A steep curve suggests near-term stability with longer-term concern; an inverted curve signals acute near-term stress
   - Compare current spread to 6-month, 1-year, and 3-year percentile ranks
   - Decompose spread moves into systematic (index/sector beta) vs. idiosyncratic components

3. **Compute and interpret the CDS-bond basis**
   - Basis = CDS spread − asset-swap spread (or Z-spread) of comparable cash bond
   - Negative basis (CDS tighter than cash): may indicate a negative basis trade opportunity (buy bond + buy protection)
   - Positive basis (CDS wider than cash): often driven by funding costs, repo availability, or counterparty risk
   - Evaluate basis stability — transient dislocations vs. structural factors (e.g., illiquid bond, CTD optionality)

4. **Monitor credit event risk**
   - Track ISDA DC filings and credit event notices at www.cdsdeterminationscommittees.org [VERIFY current URL]
   - For restructuring events, assess whether the event qualifies under the applicable restructuring clause
   - Model auction settlement mechanics: recovery rate scenarios, deliverable basket composition, and potential CTD dynamics
   - Flag succession events that may split or reassign CDS contracts

5. **Assess relative value and positioning**
   - Compare single-name spread vs. index-implied spread (intrinsic spread) for rich/cheap signals
   - Evaluate curve trades: flatteners (sell long-dated / buy short-dated protection) vs. steepeners
   - For index positions, calculate jump-to-default (JTD) exposure and skew between index and constituent spreads
   - Size positions using DV01 (spread duration × notional) and consider roll-down P&L over the holding period

6. **Evaluate counterparty and collateral factors**
   - Note CSA terms, margin thresholds, and potential collateral calls under stress scenarios
   - For large notional positions, consider market impact and liquidity (bid-ask spreads widen significantly beyond ~$10M notional in off-the-run names) [VERIFY liquidity thresholds for specific names]

## Output

- **Spread summary table**: Current spreads by tenor, change over 1D/1W/1M/3M, percentile rank
- **Basis analysis**: Computed basis with explanation of drivers; flag actionable dislocations
- **Curve assessment**: Shape characterization (steep, flat, inverted) with historical context
- **Credit event status**: Active or pending ISDA DC determinations; settlement timeline if applicable
- **Trade recommendation or risk flag**: Directional view, relative value trade, or risk warning with defined entry/exit levels and stop-loss thresholds
- **Key risks and limitations**: Model assumptions, data staleness, liquidity caveats

## Quality Checks

- Confirm restructuring clause matches regional convention and ISDA documentation version
- Verify that spread data source and snapshot time are consistent across tenors
- Cross-check basis calculation inputs — ensure bond and CDS reference the same seniority and maturity bucket
- Validate recovery rate assumptions against both market-implied and historical benchmarks
- Ensure any credit event analysis references the correct ISDA Definitions (2003 vs. 2014) and applicable supplement [VERIFY which supplement applies to the specific event type]
- Flag any data points older than 24 hours as potentially stale in fast-moving credit situations
- Confirm index series is on-the-run and that roll effects are accounted for when comparing to off-the-run data
