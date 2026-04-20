---
name: analyzing-real-estate-markets
language: en
description: Structures real estate market analysis with supply/demand dynamics, absorption rates, and rent growth projections. Use when analyzing real estate markets, forecasting market conditions, or evaluating market fundamentals.
tags:
  - analysis
  - real-estate-finance
metadata:
  author: casemark
  practice_areas:
    - Real Estate Finance
    - REIT Analysis
    - Property Investment
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Real Estate Markets

Structures real estate market analysis with supply/demand dynamics, absorption rates, and rent growth projections.

## When To Use

- Evaluating a target market for acquisition, development, or disposition timing
- Underwriting a property and needing market-level assumptions for rent growth, vacancy, and cap rates
- Preparing investor memos or IC packages that require market context
- Benchmarking a submarket against metro-wide or national trends
- Assessing REIT portfolio exposure to specific market fundamentals

## Inputs To Gather

- **Geographic scope**: Metro area, submarket, or micro-market (zip/neighborhood level)
- **Property type**: Multifamily, office, industrial, retail, hospitality, or specialty
- **Time horizon**: Historical lookback period (typically 3–10 years) and forward projection window
- **Data sources**: CoStar, CBRE-EA, RealPage, Yardi Matrix, REIS, Census/BLS, or client-provided datasets
- **Comparable set**: Competitive properties or peer submarkets for benchmarking
- **Investment thesis context**: What decision this analysis supports (buy/sell/hold/develop)

## Workflow

1. **Define market boundaries**
   - Confirm the submarket delineation (CoStar submarket, CBSA, custom polygon)
   - Identify the competitive set of properties by vintage, class, and size
   - Note any boundary quirks that affect data interpretation (e.g., submarket includes both CBD and suburban nodes)

2. **Analyze supply dynamics**
   - Quantify existing inventory (total SF or units by class)
   - Catalog the construction pipeline: under construction, planned, and proposed
   - Calculate pipeline-to-inventory ratio to gauge supply pressure
   - Identify entitled but unbuilt land parcels and zoning changes that could unlock future supply
   - [VERIFY] Local permitting and entitlement timelines, which vary by jurisdiction

3. **Analyze demand dynamics**
   - Pull net absorption data (trailing 4–12 quarters) and identify trend direction
   - Decompose demand drivers: employment growth by sector, population migration, household formation
   - For office: track tenant-in-the-market (TIM) data and sublease inventory as demand signals
   - For industrial: monitor e-commerce penetration, port volumes, and reshoring trends
   - For multifamily: assess rent-to-income ratios and homeownership affordability as demand ceilings

4. **Calculate key market metrics**
   - **Vacancy rate**: Current, trailing average, and long-run equilibrium vacancy
   - **Absorption rate**: Net absorption as a percentage of inventory; months of supply for new deliveries
   - **Rent growth**: Nominal and real (inflation-adjusted) asking and effective rent trends
   - **Cap rate spreads**: Current cap rates vs. historical averages and vs. risk-free rate (10-year Treasury)
   - **Concessions**: Free rent, TI allowances, or other concessions as a share of gross rent

5. **Develop forward projections**
   - Model rent growth using supply/demand balance: if absorption exceeds deliveries, project above-trend rent growth; if pipeline exceeds absorption, project softening
   - Estimate stabilized vacancy based on pipeline delivery schedule and historical absorption pace
   - Sensitivity-test projections under bull/base/bear employment scenarios
   - Flag any structural shifts (remote work, AI-driven space reduction, demographic changes) that may break historical patterns

6. **Benchmark and contextualize**
   - Compare submarket metrics to the broader MSA and national averages
   - Rank the submarket on key dimensions (rent growth, supply risk, demand depth, liquidity)
   - Identify where the market sits in the real estate cycle (recovery, expansion, hypersupply, recession)

## Output

Structure the deliverable as follows:

- **Executive summary**: 2–3 paragraphs stating market outlook, key risks, and investment implications
- **Market overview table**: Snapshot of inventory, vacancy, absorption, rent, and cap rate metrics with YoY changes
- **Supply/demand analysis**: Detailed narrative with supporting charts or data tables
- **Forward projections**: Base/bull/bear scenarios with key assumptions stated explicitly
- **Risk factors**: Concentration risk, regulatory risk, supply overhang, demand fragility
- **Data sources and limitations**: List all sources, vintage of data, and known gaps

## Quality Checks

- Verify that absorption and vacancy figures reconcile (net absorption should explain vacancy movement after accounting for new supply)
- Confirm rent growth figures distinguish between asking vs. effective rents and same-store vs. market-wide
- Ensure cap rate data reflects comparable transaction types (institutional vs. all-comers, portfolio vs. single-asset)
- Check that forward projections have explicit assumption tables — never embed assumptions silently in outputs
- [VERIFY] Tax abatement programs, rent control regulations, or inclusionary zoning rules that affect achievable rents
- [VERIFY] Local employment data sources and reporting lags, which can differ by metro area
- Flag any data points older than 6 months for refresh before use in active underwriting
