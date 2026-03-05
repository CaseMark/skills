---
name: analyzing-demographic-trends
description: Structures demographic analysis with population projections, dependency ratios, and economic impact assessment. Use when analyzing demographics, projecting population trends, or assessing demographic economic impact.
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
# Analyzing Demographic Trends

Structures demographic analysis with population projections, dependency ratios, and economic impact assessment.

## When To Use

- Projecting population size, age distribution, or growth rates for a country, region, or market
- Calculating dependency ratios (youth, old-age, total) and assessing fiscal/labor-market implications
- Evaluating how demographic shifts affect consumer demand, housing, healthcare costs, or pension solvency
- Supporting macroeconomic forecasts, sovereign credit analysis, or policy impact assessments with demographic foundations
- Comparing demographic trajectories across geographies or time horizons

## Inputs To Gather

- **Geographic scope**: Country, region, metro area, or custom market definition
- **Time horizon**: Historical base period and projection window (e.g., 2000–2025 historical, 2025–2050 projected)
- **Data sources**: UN World Population Prospects, national census/vital statistics, Eurostat, World Bank, or proprietary datasets — note vintage and revision date
- **Key variables requested**: Total population, age-sex pyramids, fertility (TFR), mortality/life expectancy, net migration, urbanization rate
- **Scenario assumptions**: Fertility variant (low/medium/high), migration policy scenarios, pandemic or conflict adjustments
- **End-use context**: Investment thesis, policy memo, sovereign rating, sector strategy — determines which derived metrics matter most

## Workflow

1. **Define scope and scenarios**
   - Confirm geography, time horizon, and projection variants
   - Identify which dependency ratios and derived indicators the end user needs (e.g., working-age share, median age, support ratio)

2. **Compile and validate base data**
   - Collect historical population by 5-year age cohort and sex
   - Record total fertility rate (TFR), life expectancy at birth (e0), and net migration rate for the base period
   - Cross-check source consistency — flag discrepancies between national statistics and UN estimates [VERIFY]
   - Note census year, intercensal adjustment method, and any known undercount issues

3. **Build population projections**
   - Apply cohort-component method: project each age-sex cohort forward using age-specific fertility, mortality, and migration assumptions
   - Run at least two scenarios (e.g., UN medium variant + one stress case) to bracket uncertainty
   - Calculate annual or 5-year snapshots of total population, age-group shares (0–14, 15–64, 65+), and median age

4. **Compute dependency and support ratios**
   - **Youth dependency ratio**: Pop 0–14 / Pop 15–64
   - **Old-age dependency ratio**: Pop 65+ / Pop 15–64
   - **Total dependency ratio**: (Pop 0–14 + Pop 65+) / Pop 15–64
   - **Potential support ratio**: Pop 15–64 / Pop 65+ (inverse of old-age dependency)
   - Present ratios as time series and note inflection points (e.g., year old-age ratio exceeds youth ratio)

5. **Assess economic and fiscal impact**
   - **Labor supply**: Project working-age population growth; estimate labor force participation adjustments for aging
   - **Savings and consumption**: Relate age-structure shifts to aggregate savings rate and consumption composition (healthcare, education, housing)
   - **Fiscal pressure**: Estimate directional impact on pension expenditure, healthcare spend, and tax-base erosion using dependency-ratio trends
   - **Sector-level demand**: Map age-cohort growth to relevant sectors (e.g., 65+ growth → healthcare, pharma, senior housing)
   - Flag where GDP-per-capita projections embed implicit demographic assumptions [VERIFY]

6. **Contextualize and compare**
   - Benchmark against peer economies or regions at similar demographic stages
   - Identify demographic dividend windows (rising working-age share) or demographic drag periods
   - Note policy levers that could alter the trajectory: immigration reform, pronatalist incentives, retirement-age changes [VERIFY jurisdiction-specific policy context]

## Output

Deliver a structured demographic analysis report containing:

- **Executive summary**: Key takeaway on population trajectory, dependency-ratio outlook, and top economic implication in 2–3 sentences
- **Data tables**: Historical and projected population by age group, TFR, life expectancy, net migration — with source citations and vintage dates
- **Dependency ratio time series**: Charts or tables showing youth, old-age, and total dependency ratios across the projection window
- **Economic impact assessment**: Narrative sections on labor supply, fiscal pressure, consumption shifts, and sector demand — each tied to specific demographic drivers
- **Scenario comparison**: Side-by-side view of baseline vs. alternative scenario outcomes
- **Assumptions and limitations**: Explicit list of fertility/mortality/migration assumptions, data gaps, and model limitations

## Quality Checks

- All population figures cite a specific source, vintage year, and revision number
- Dependency ratios are internally consistent with the underlying age-group totals (ratios recalculate correctly from the data tables)
- Projection scenarios use clearly labeled, distinct assumption sets — no blending of variants without disclosure
- Economic impact claims trace back to a demographic driver, not to unsupported assertions
- Historical data and projections are clearly delineated — no silent transition from observed to estimated figures
- Peer comparisons use the same data source and definition of age groups to avoid apples-to-oranges distortion
- Any jurisdiction-specific policy, statutory retirement age, or fiscal rule is marked [VERIFY]
