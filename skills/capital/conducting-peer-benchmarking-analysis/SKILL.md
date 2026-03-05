---
name: conducting-peer-benchmarking-analysis
description: Evaluates fund performance against peer universes with vintage year comparison, quartile ranking, and strategy-specific benchmarking. Use when benchmarking fund performance, analyzing vintage comparisons, or assessing relative positioning.
tags:
  - process
  - investor-relations-and-lp-reporting
metadata:
  author: casemark
  practice_areas:
    - Investor Relations
    - LP Reporting
    - Fund Administration
  document_types:
    - Process Documentation
  skill_modes:
    - Process Management
---
# Conducting Peer Benchmarking Analysis

## When To Use

- Preparing quarterly or annual LP reports that require relative performance context
- Responding to LP due diligence requests for peer comparison data
- Evaluating fund positioning ahead of fundraising or investor meetings
- Assessing whether a fund's return profile warrants strategy adjustments
- Building track record presentations for new fund marketing materials

## Inputs To Gather

- **Fund performance data**: Net IRR, gross IRR, TVPI, DPI, RVPI, and PME ratios for each fund vehicle
- **Vintage year**: The year of first capital call (not final close) for accurate cohort matching
- **Strategy classification**: Buyout, growth equity, venture (early/late), real estate (value-add/opportunistic/core), credit, infrastructure, secondaries, or fund-of-funds
- **Geography focus**: North America, Europe, Asia-Pacific, global, or emerging markets
- **Fund size band**: Confirm AUM range to select the correct peer slice (e.g., small-cap buyout vs. mega-cap)
- **Benchmark source(s)**: Cambridge Associates, Preqin, Burgiss, PitchBook, Hamilton Lane, or proprietary LP datasets — note each source's methodology and universe construction [VERIFY]
- **Reporting date**: As-of date for all metrics; confirm alignment between fund data and benchmark data timestamps
- **Currency**: Base currency for the fund and whether benchmark data is hedged or unhedged

## Workflow

1. **Define the peer universe**
   - Match vintage year exactly; avoid blending adjacent vintages unless the universe is too small (< 15 funds)
   - Filter by strategy, geography, and fund size band
   - Document universe size (number of funds) and any exclusions applied
   - If using multiple benchmark providers, note universe overlap and methodology differences (e.g., Cambridge uses pooled IRR; Burgiss uses fund-level median)

2. **Normalize performance metrics**
   - Align as-of dates — if the fund reports on 12/31 but the benchmark updates on 9/30, flag the gap
   - Confirm net-to-LP vs. gross-of-fees basis; never compare net IRR to gross benchmarks
   - Convert to common currency if the fund and benchmark use different bases
   - For younger funds (vintage < 3 years), emphasize DPI and called capital % over IRR, which is volatile early in fund life

3. **Calculate quartile rankings**
   - Rank the fund within the peer universe for each metric: net IRR, TVPI, DPI
   - Assign quartile (Q1 = top 25%, Q2 = 25-50%, Q3 = 50-75%, Q4 = bottom 25%)
   - Report the exact percentile where available, not just the quartile band
   - Note the spread between quartile boundaries — a narrow Q1/Q2 boundary signals a compressed peer set

4. **Run PME analysis** (if applicable)
   - Select the appropriate public market index (e.g., S&P 500, MSCI World, Russell 2000) based on strategy and geography [VERIFY index selection against LP preferences]
   - Calculate Kaplan-Schoar PME, Long-Nickels PME, or Direct Alpha — document which method and why
   - A PME > 1.0 indicates outperformance vs. the public index on a cash-flow-weighted basis

5. **Contextualize the results**
   - Compare current quartile ranking to prior reporting periods — is the fund trending up or down?
   - Identify J-curve effects for younger funds that suppress early IRR
   - Note any survivorship bias in the benchmark dataset (liquidated underperformers may be excluded)
   - For funds nearing end of life, weight DPI and realized multiples more heavily than IRR

6. **Compile the benchmarking output**
   - Summary table: Fund metric | Peer median | Peer upper quartile | Fund quartile rank
   - Vintage year scatter plot or bar chart positioning the fund within the distribution
   - Narrative commentary explaining relative positioning, trends, and any caveats
   - Source attribution for all benchmark data with as-of dates

## Output

- **Peer benchmarking summary table** with fund metrics alongside peer median, upper quartile, and lower quartile for each KPI
- **Quartile ranking card** showing net IRR, TVPI, and DPI rankings with percentile positions
- **PME comparison** (where applicable) with index selection rationale
- **Narrative commentary** (2-4 paragraphs) contextualizing performance relative to peers, noting trends, J-curve effects, and data limitations
- **Data source disclosures** listing benchmark provider, universe size, vintage year, as-of date, and any filters applied

## Quality Checks

- Confirm vintage year assignment uses first capital call date, not final close date
- Verify net vs. gross alignment — never mix fee bases in a single comparison
- Check that peer universe size is disclosed; flag universes with fewer than 15 funds as potentially unreliable
- Ensure as-of dates match within one quarter between fund data and benchmark data
- Validate that quartile boundaries are calculated from the correct universe (not a broader or narrower slice)
- Confirm PME index selection is appropriate for the fund's strategy and geography
- Mark any stale benchmark data (> 6 months old) with [VERIFY] for updated figures
- Review for survivorship bias disclosure — note whether the benchmark includes liquidated or written-off funds
