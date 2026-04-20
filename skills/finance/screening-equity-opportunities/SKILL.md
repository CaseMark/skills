---
name: screening-equity-opportunities
language: en
description: Applies quantitative and qualitative screens to filter investable equity universe by financial and strategic criteria. Use when screening stocks, filtering investment candidates, or building watchlists.
tags:
  - screening
  - equity-research
  - investment
metadata:
  author: casemark
  practice_areas:
    - Equity Research
    - Investment Management
  document_types:
    - Screening Report
  skill_modes:
    - Screening
    - Filtering
---
# Screening Equity Opportunities

## When To Use

- Building an initial watchlist from a broad equity universe (e.g., Russell 3000, S&P 500, MSCI EAFE)
- Narrowing candidates for a thematic or sector-specific investment thesis
- Identifying stocks meeting specific factor criteria (value, growth, quality, momentum)
- Refreshing an existing screen with updated financial data or revised parameters
- Generating a filtered candidate list for deeper fundamental analysis or portfolio construction

## Inputs To Gather

- **Investment universe**: Index, sector, geography, or market-cap range to screen against
- **Screening criteria**: Quantitative thresholds (valuation multiples, growth rates, profitability metrics, leverage ratios) and qualitative filters (sector exclusions, ESG constraints, governance standards)
- **Priority weighting**: Which criteria are hard cutoffs vs. soft preferences for ranking
- **Time horizon**: Short-term tactical vs. long-term strategic — affects which metrics matter most
- **Data source and vintage**: Confirm whether using trailing twelve months (TTM), last fiscal year (LFY), or forward consensus estimates; note the as-of date
- **Benchmark context**: Reference index or peer group for relative comparisons

## Workflow

1. **Establish the universe and parameters**
   - Confirm the starting universe size and any pre-filters (e.g., minimum market cap $500M, average daily volume > $5M, exclude ADRs)
   - Document hard exclusion criteria upfront (sector bans, sanctioned entities, regulatory restrictions)

2. **Define quantitative screen layers**
   - **Valuation**: P/E, EV/EBITDA, P/B, P/FCF — set thresholds relative to sector medians or absolute levels
   - **Growth**: Revenue CAGR, EPS growth rate, forward earnings revisions — specify lookback and forward periods
   - **Profitability**: ROE, ROIC, gross/operating margins — compare to cost of capital where relevant
   - **Financial health**: Net debt/EBITDA, interest coverage, current ratio, Altman Z-score for distress risk
   - **Momentum/technicals** (if applicable): Relative strength, 52-week price position, moving average crossovers

3. **Apply qualitative overlays**
   - Management quality flags: insider ownership trends, recent executive turnover, capital allocation track record
   - Industry positioning: competitive moat indicators, TAM trajectory, regulatory tailwinds/headwinds
   - ESG/exclusion filters: controversy scores, carbon intensity thresholds, board diversity metrics [VERIFY — ESG data provider methodology varies significantly]

4. **Run the screen and rank results**
   - Apply hard cutoffs first to reduce the universe, then score remaining names on soft criteria
   - Use composite scoring (e.g., weighted z-scores across factors) to produce a ranked list
   - Flag names near threshold boundaries — small data changes could move them in or out

5. **Validate and stress-test output**
   - Check for survivorship bias if using historical screens
   - Identify sector/geography concentration in results — excessive clustering may indicate an unintended factor tilt
   - Cross-reference top names against recent earnings surprises, analyst rating changes, or corporate actions (M&A, spinoffs) that may distort trailing data
   - Spot-check 3–5 names manually to confirm data accuracy and screen logic

6. **Document and deliver**
   - Produce the screening report with full methodology, parameter table, and ranked results
   - Note any data gaps, stale inputs, or names requiring [VERIFY] follow-up
   - Include pass/fail counts at each filter stage to show funnel attrition

## Output

The screening report should contain:

- **Methodology summary**: Universe definition, each filter with threshold values, weighting scheme, data source and as-of date
- **Funnel summary table**: Number of names passing each successive filter layer
- **Ranked results table**: Top candidates with key metrics displayed (ticker, name, market cap, sector, and the screening metrics used)
- **Concentration analysis**: Sector, geography, and market-cap distribution of the output set
- **Watchlist flags**: Names near cutoff boundaries, names with stale or missing data, names with pending corporate events
- **Exclusions log**: Notable names eliminated and the specific filter that removed them (useful for audit trail and thesis refinement)

## Quality Checks

- Confirm data vintage matches stated as-of date — mixing TTM and forward estimates without disclosure distorts comparisons
- Verify that sector classification system is consistent (GICS vs. ICB vs. custom) [VERIFY — classification differences can shift sector composition materially]
- Ensure screen logic handles missing data correctly (exclude vs. penalize vs. impute) — document the chosen approach
- Validate that no look-ahead bias exists if screen is meant to be backtested
- Check that the number of passing names is reasonable for the stated universe and criteria tightness — an unexpectedly high or low pass rate suggests a logic error
- Confirm compliance with any investment policy statement (IPS) constraints or client mandate restrictions before finalizing the watchlist
