---
name: conducting-traffic-and-demand-studies
language: en
description: Evaluates demand forecasts for toll roads, airports, and ports with independent engineer review and scenario sensitivity analysis. Use when analyzing traffic studies, validating demand forecasts, or stress testing revenue projections.
tags:
  - process
  - infrastructure-and-project-finance
metadata:
  author: casemark
  practice_areas:
    - Project Finance
    - Infrastructure Investment
    - PPP
  document_types:
    - Process Documentation
  skill_modes:
    - Process Management
---
# Conducting Traffic And Demand Studies

## When To Use

- Reviewing an independent traffic consultant's demand forecast for a toll road, managed lane, bridge, or tunnel concession
- Evaluating passenger or cargo throughput projections for airport or port financings
- Stress-testing revenue assumptions in a P3/PPP financial model prior to financial close
- Assessing ramp-up risk during construction-to-operations transition
- Comparing competing demand studies submitted by sponsor vs. lender's independent engineer (IE)

## Inputs To Gather

- **Traffic/demand study report** from the independent traffic consultant (e.g., Steer, CDM Smith, AECOM)
- **Base-case financial model** with revenue line items linked to volume assumptions
- **Socioeconomic data inputs** used in the model (population growth, employment, GDP, vehicle registrations)
- **Network and route assumptions** — competing facilities, planned capacity additions, toll/tariff schedules
- **Historical traffic data** (if brownfield) — at least 5 years of monthly volumes by vehicle class or passenger type
- **Concession/PPP agreement** sections on toll escalation, revenue sharing, and minimum traffic guarantees
- **Independent engineer report** and any lender technical advisor commentary on the demand study
- **Comparable asset benchmarks** — ramp-up curves and mature-year volumes from similar facilities [VERIFY jurisdiction-specific data availability]

## Workflow

1. **Validate methodology and model structure**
   - Confirm the demand model type (four-step transport model, stated-preference survey, gravity model, econometric regression) and whether it is appropriate for the asset class
   - Check that the model's zone system, network coding, and assignment algorithm are consistent with the study area
   - For airports: verify air traffic movement forecasts use unconstrained demand adjusted for capacity constraints
   - For ports: confirm TEU/tonnage projections account for hinterland competition and shipping route shifts

2. **Audit socioeconomic assumptions**
   - Compare population and employment growth rates against independent government or third-party forecasts (e.g., census bureau, state demographer, Woods & Poole)
   - Assess whether GDP elasticity assumptions are within accepted ranges for the asset type (typically 0.8–1.2 for toll roads, 1.5–2.5 for airports) [VERIFY against current industry benchmarks]
   - Flag any assumption that deviates materially from the IE's independent view

3. **Evaluate ramp-up profile**
   - For greenfield assets, benchmark the ramp-up curve against comparable facilities — typical toll road ramp-up is 3–5 years to reach stabilized demand
   - Assess whether the study accounts for induced demand, mode shift, and traveler learning curves
   - Check that Year 1 volumes reflect realistic day-one capture, not annualized mature-year demand

4. **Test toll/tariff sensitivity**
   - Verify price elasticity values used in the model (typical range: −0.1 to −0.4 for toll roads) [VERIFY asset-specific elasticity ranges]
   - Confirm that toll escalation assumptions (CPI-linked, fixed schedule, dynamic pricing) match the concession agreement
   - Run or review scenarios with +/−20% volume variance and corresponding revenue impact

5. **Perform scenario and downside analysis**
   - **Base case**: consultant's central forecast
   - **Rating agency case**: typically 70–80% of base-case volumes (S&P/Moody's/Fitch methodology) [VERIFY current rating agency haircut conventions]
   - **Bankable case / P90**: downside used for debt sizing, often 80–90% of base
   - **Stress case**: recession scenario with GDP contraction and demand drop of 20–30%
   - Calculate DSCR under each scenario and confirm covenant compliance

6. **Cross-check against comparable assets**
   - Compile volume data from comparable toll roads, airports, or ports at similar stages of maturity
   - Identify whether the study's forecasts sit within the reasonable range of comparables
   - Flag outlier assumptions (e.g., per-capita trip rates significantly above peer facilities)

7. **Assess independent engineer and lender advisor positions**
   - Summarize the IE's haircuts or adjustments to the sponsor's traffic study
   - Note any unresolved disagreements between the traffic consultant and the IE
   - Identify conditions precedent tied to traffic study acceptance

## Output

- **Demand Study Review Memo** containing:
  - Executive summary of forecast reasonableness (supportable / conditionally supportable / not supportable)
  - Methodology assessment with identified strengths and weaknesses
  - Socioeconomic assumption comparison table (study vs. independent sources)
  - Ramp-up benchmarking chart against comparable assets
  - Scenario matrix: volumes, revenues, and DSCRs across base/downside/stress cases
  - Elasticity sensitivity table showing revenue impact of toll/tariff changes
  - Risk register of key demand-side risks (competing routes, policy changes, autonomous vehicles, remote work trends)
  - Recommendations for structuring protections (reserve accounts, minimum revenue guarantees, traffic band mechanisms)

## Quality Checks

- All socioeconomic inputs are cross-referenced against at least two independent data sources
- Elasticity values fall within published ranges for the asset class; outliers are justified or flagged with [VERIFY]
- Ramp-up assumptions are benchmarked against at least three comparable facilities
- DSCR calculations under the rating agency case confirm the project meets minimum coverage thresholds (typically 1.20x–1.40x for investment-grade toll roads) [VERIFY lender/rating agency specific thresholds]
- The financial model's revenue line items reconcile to the traffic study's volume and toll/tariff outputs
- Competing facility analysis reflects committed and funded projects, not speculative proposals
- Any assumption inherited from the sponsor without independent verification is explicitly marked
