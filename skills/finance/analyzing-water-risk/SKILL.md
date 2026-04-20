---
name: analyzing-water-risk
language: en
description: Structures water risk assessment with water stress mapping, usage analysis, and regulatory exposure evaluation. Use when analyzing water risk, mapping water stress, or evaluating water-related financial exposure.
tags:
  - analysis
  - sustainable-finance
  - regulatory
  - risk
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
# Analyzing Water Risk

## When To Use

- Evaluating a portfolio company or asset for exposure to water stress, scarcity, or quality degradation
- Conducting pre-investment due diligence on water-intensive sectors (agriculture, mining, semiconductors, beverages, textiles, utilities)
- Assessing regulatory risk from emerging water pricing, allocation caps, or discharge limits
- Scoring water risk as part of a broader ESG or climate-risk integration framework
- Responding to CDP Water Security questionnaire items or TNFD water-related disclosures

## Inputs To Gather

- **Asset/company identifiers**: Facility locations (latitude/longitude or basin names), sector/NAICS codes, revenue segments
- **Water usage data**: Withdrawal volumes, consumption vs. discharge, water intensity ratios (m³ per unit of output or revenue)
- **Basin-level stress indicators**: WRI Aqueduct scores, WWF Water Risk Filter results, or equivalent basin stress metrics for each operating location
- **Regulatory landscape**: Applicable water rights regime, discharge permit conditions, pending legislation on water pricing or allocation [VERIFY jurisdiction-specific rules]
- **Supply chain exposure**: Tier-1 and Tier-2 supplier locations and water dependency where available
- **Financial data**: CAPEX/OPEX tied to water procurement, treatment, and compliance; insurance claims history for flood or drought events

## Workflow

1. **Define scope and materiality threshold**
   - Confirm whether analysis covers direct operations, supply chain, or both
   - Set materiality threshold (e.g., facilities representing >5% of revenue or withdrawal volume)
   - Identify the reporting framework driving the analysis (CDP, TNFD, SASB, internal risk policy)

2. **Map water stress exposure by location**
   - Overlay facility coordinates against WRI Aqueduct Baseline Water Stress, Seasonal Variability, and Projected Change layers
   - Classify each site as Low / Low-Medium / Medium-High / High / Extremely High stress
   - Flag sites in regions with declining groundwater trends or recent drought declarations
   - Note any sites co-located with competing high-demand users (large-scale agriculture, municipal systems)

3. **Quantify operational water dependency**
   - Calculate water intensity metrics: m³ per unit produced, per $M revenue, and per employee
   - Benchmark against sector peers using SASB or CDP sector medians
   - Identify single-source dependencies (one aquifer, one municipal intake) that create concentration risk
   - Assess recycling/reuse rates and whether current efficiency gains are plateauing

4. **Evaluate regulatory and pricing exposure**
   - Catalog current water rights, permits, and pricing structures per facility [VERIFY local water law regime]
   - Identify jurisdictions with pending or proposed water pricing reforms, cap-and-trade for allocations, or tightening discharge standards
   - Estimate cost impact under plausible regulatory scenarios (e.g., 20%/50% price increase, allocation reduction)
   - Flag any history of permit violations, enforcement actions, or community opposition

5. **Assess physical risk scenarios**
   - Model exposure under IPCC SSP2-4.5 and SSP5-8.5 scenarios for 2030 and 2050 horizons
   - Evaluate flood risk for coastal or floodplain-adjacent facilities
   - Consider compound risks: drought + heat stress on cooling systems, flood + contamination of intake sources

6. **Score and prioritize**
   - Assign a composite water risk score per facility combining stress level, dependency, regulatory exposure, and physical scenario impact
   - Aggregate to portfolio or company level using revenue-weighted or withdrawal-weighted roll-up
   - Rank facilities/companies into risk tiers for action prioritization

7. **Identify mitigation levers and residual risk**
   - Map existing mitigation measures (efficiency programs, alternative sourcing, storage, insurance)
   - Estimate residual risk after mitigation
   - Recommend targeted interventions for highest-risk sites (source diversification, on-site treatment, engagement with local water authorities)

## Output

Deliver a structured **Water Risk Assessment Report** containing:

- **Executive summary**: Top-line risk rating, key hotspots, and recommended actions
- **Facility-level risk matrix**: Table with location, basin stress score, water intensity, regulatory exposure flag, physical scenario rating, and composite score
- **Heat map visualization guidance**: Specify data fields for a geographic heat map overlay (tool-agnostic; reference WRI Aqueduct or equivalent layer)
- **Regulatory exposure register**: Jurisdiction, current regime, pending changes, estimated cost impact [VERIFY each jurisdiction]
- **Scenario analysis summary**: Cost and operational impact under modeled regulatory and physical scenarios
- **Mitigation recommendations**: Prioritized by risk reduction potential and implementation feasibility
- **Data gaps and limitations**: Explicitly note missing supplier data, unverified self-reported volumes, or basins lacking reliable stress data

## Quality Checks

- Every facility with >5% of total withdrawal volume is individually assessed — no material site omitted
- Basin stress classifications cite a named data source and vintage year (e.g., "WRI Aqueduct 4.0, 2023 baseline")
- Water intensity benchmarks reference a stated peer set and data year
- Regulatory exposure flags include [VERIFY] markers where rules vary by sub-national jurisdiction or are subject to pending legislative change
- Scenario assumptions (time horizon, SSP pathway, price increase magnitude) are stated explicitly, not embedded silently
- Composite scoring methodology is transparent — weights and thresholds documented so a reviewer can reproduce the rating
- Report distinguishes between verified data and estimates/proxies throughout
