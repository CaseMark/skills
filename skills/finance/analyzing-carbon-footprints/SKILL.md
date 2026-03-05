---
name: analyzing-carbon-footprints
description: Structures carbon footprint analysis with Scope 1/2/3 measurement and intensity benchmarking. Use when measuring carbon emissions, analyzing Scope 3, or benchmarking carbon intensity.
tags:
  - analysis
  - sustainable-finance
metadata:
  author: casemark
  practice_areas:
    - ESG
    - Impact Investing
    - Sustainable Finance
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Carbon Footprints

## When To Use

- Measuring a company's or portfolio's greenhouse gas (GHG) emissions across Scope 1, 2, and 3
- Benchmarking carbon intensity (tCO2e per $M revenue, per unit produced, or per square foot)
- Evaluating Scope 3 supply-chain or financed-emissions exposure for investment decisions
- Preparing data for TCFD, CDP, CSRD, or SEC climate-related disclosures [VERIFY: applicable disclosure framework]
- Comparing portfolio holdings against sector decarbonization pathways (e.g., SBTi, IEA Net Zero)

## Inputs To Gather

- **Entity scope**: company name, ticker, GICS sector/sub-industry, reporting boundary (operational control vs. equity share)
- **Emissions data sources**: sustainability reports, CDP responses, annual reports, GHG inventories, third-party databases (e.g., MSCI, ISS, Trucost, Bloomberg)
- **Scope 1 data**: direct fuel combustion, fleet, fugitive emissions, process emissions (with fuel types and volumes if available)
- **Scope 2 data**: purchased electricity, steam, heating, cooling — obtain both location-based and market-based figures
- **Scope 3 categories**: identify which of the 15 GHG Protocol categories are material — at minimum review purchased goods/services (Cat 1), capital goods (Cat 2), fuel- and energy-related activities (Cat 3), upstream transportation (Cat 4), use of sold products (Cat 11), and investments/financed emissions (Cat 15)
- **Normalization denominators**: revenue, EVIC, production units, headcount, or square footage for intensity calculations
- **Temporal scope**: reporting year(s), base year for trajectory analysis
- **Peer set**: comparable companies or sector averages for benchmarking

## Workflow

1. **Classify emission scopes**
   - Map each data point to Scope 1, 2 (location-based and market-based), or the relevant Scope 3 category per the GHG Protocol Corporate Standard
   - Flag any category where data is estimated vs. measured; note the estimation methodology (spend-based, activity-based, supplier-specific)

2. **Aggregate and convert to CO2-equivalent**
   - Apply GWP factors from the appropriate IPCC Assessment Report [VERIFY: AR5 vs. AR6 GWP values per reporting framework requirements]
   - Sum emissions in metric tonnes CO2e (tCO2e) by scope and category
   - If partial data exists, document gap-filling assumptions (e.g., extrapolation, sector-average emission factors)

3. **Calculate intensity metrics**
   - Revenue intensity: tCO2e / $M revenue
   - EVIC intensity: tCO2e / $M enterprise value including cash (for financed-emissions analysis per PCAF)
   - Physical intensity: tCO2e / unit of output (sector-specific — MWh for utilities, tonne of product for materials)
   - Compare against sector median, top-quartile, and Paris-aligned benchmarks

4. **Analyze Scope 3 materiality**
   - Rank Scope 3 categories by absolute emissions contribution
   - Identify the top 3-5 categories driving total footprint
   - Assess data quality per PCAF scoring (1 = verified, 5 = estimated) for each category
   - Highlight where supplier-specific data could replace spend-based estimates

5. **Benchmark and trajectory analysis**
   - Compare entity's absolute and intensity metrics to sector peers and index averages
   - Plot historical trend (minimum 3 years if available) and calculate year-over-year change rate
   - Assess alignment with decarbonization pathways: SBTi sectoral targets, IEA Net Zero 2050, or national NDC targets [VERIFY: relevant pathway for entity's sector]
   - Flag whether the entity has a validated science-based target, net-zero commitment, or interim milestones

6. **Identify risks and opportunities**
   - Carbon pricing exposure: estimate potential cost under $50, $100, $150/tCO2e scenarios [VERIFY: applicable carbon pricing regime]
   - Transition risk: high-intensity operations, stranded asset potential, regulatory timeline
   - Opportunity signals: declining intensity trend, renewable energy procurement, credible reduction roadmap

## Output

Structure the analysis report as follows:

- **Executive Summary**: total footprint (tCO2e), scope breakdown (pie chart data), headline intensity metric, peer ranking, trajectory assessment (on-track / lagging / no target)
- **Scope Breakdown Table**: Scope 1, Scope 2 (location and market), Scope 3 by category — absolute and percentage of total
- **Intensity Benchmarking**: entity vs. sector median, top quartile, and Paris-aligned threshold
- **Scope 3 Deep Dive**: materiality ranking, data quality scores, key hotspot categories
- **Trajectory & Target Assessment**: historical trend, forward-looking pathway alignment, gap to target
- **Risk Quantification**: carbon price sensitivity, regulatory exposure summary
- **Data Quality & Limitations**: sources used, estimation methods, coverage gaps, confidence level per scope

## Quality Checks

- Scope 1 + Scope 2 totals cross-referenced against at least two independent sources (e.g., CDP vs. sustainability report)
- Scope 2 reports both location-based and market-based figures — do not default to one without noting the other
- Scope 3 categories explicitly marked as "reported," "estimated," or "not assessed" — never leave gaps silent
- Intensity denominators match the reporting period of emissions data (no mixing FY2023 emissions with FY2024 revenue)
- GWP conversion factors cited with specific IPCC AR version
- All estimated or gap-filled data points flagged with [VERIFY] or stated confidence interval
- Peer benchmarks use consistent scope boundaries (e.g., all Scope 1+2, or all Scope 1+2+3) — do not compare mismatched scopes
- Carbon pricing scenario assumptions stated explicitly (price per tonne, year, jurisdiction)
