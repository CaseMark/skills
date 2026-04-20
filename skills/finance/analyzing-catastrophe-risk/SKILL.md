---
name: analyzing-catastrophe-risk
language: en
description: Structures catastrophe risk assessment with model output interpretation and accumulation monitoring. Use when analyzing cat risk, interpreting cat model results, or managing cat exposure.
tags:
  - analysis
  - insurance
  - risk
metadata:
  author: casemark
  practice_areas:
    - Insurance
    - Actuarial Science
    - Reinsurance
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Catastrophe Risk

Structures catastrophe risk assessment with model output interpretation and accumulation monitoring.

## When To Use

- Evaluating portfolio exposure to natural catastrophe perils (hurricane, earthquake, flood, wildfire, severe convective storm)
- Interpreting output from vendor cat models (AIR, RMS, CoreLogic) for underwriting or reinsurance placement decisions
- Monitoring aggregate accumulations against defined tolerance limits or PML thresholds
- Preparing cat risk reports for reinsurance renewals, rating agency reviews, or board risk committees
- Assessing adequacy of cat reinsurance programs relative to modeled loss distributions

## Inputs To Gather

- **Exposure data**: SOV (statement of values) or policy-level TIV schedules with geocoded locations, construction type, occupancy, year built, and number of stories
- **Cat model output**: EP (exceedance probability) curves, AEP/OEP tables, AAL (average annual loss), standard deviation, and event loss tables from one or more vendor models
- **Accumulation data**: Current aggregate exposures by peril, geography (CRESTA zone, county, state), and line of business
- **Reinsurance structure**: Treaty terms including attachment points, limits, co-participation, reinstatement provisions, and cascading layers
- **Risk appetite parameters**: Board-approved PML tolerances (e.g., 1-in-100 OEP net of reinsurance ≤ X% of surplus), concentration limits by zone
- **Historical loss experience**: Prior catastrophe claims data by event, including gross/ceded/net splits

## Workflow

1. **Validate exposure data quality**
   - Check geocoding hit rates — flag portfolios with >5% county-level or worse resolution
   - Confirm TIV completeness: replacement cost vs. actual cash value, inclusion of business interruption and extra expense
   - Identify secondary modifiers: roof type, cladding, roof-to-wall connection [VERIFY against model-specific vulnerability requirements]
   - Reconcile SOV totals against in-force premium system

2. **Run and interpret cat model output**
   - Compare results across available vendor models (AIR Touchstone, RMS RiskLink/Intelligent Risk Platform, CoreLogic) — note model vintage and version
   - Extract key metrics at required return periods: AAL, 1-in-50, 1-in-100, 1-in-250 OEP and AEP, both gross and net of reinsurance
   - Decompose losses by peril, sub-peril (e.g., wind vs. storm surge for hurricane), and geography
   - Evaluate demand surge, loss amplification, and secondary uncertainty assumptions
   - Identify tail risk: review coefficient of variation and shape of EP curve beyond 1-in-250

3. **Assess accumulation exposure**
   - Map aggregate TIV by CRESTA zone, county, and custom-defined accumulation zones
   - Compare current accumulations against tolerance limits — highlight breaches or near-breaches
   - Evaluate clash potential across lines (property, auto physical damage, workers' comp from single event)
   - Test for concentration risk: percentage of total portfolio TIV within hurricane/earthquake wind speed or shaking intensity contours

4. **Evaluate reinsurance program adequacy**
   - Model net loss position after applying treaty structure layer by layer
   - Stress-test against historical benchmark events (e.g., Andrew, Katrina, Northridge, Joplin) and synthetic scenarios
   - Calculate expected recoveries, reinstatement costs, and residual net exposure above program exhaustion
   - Assess cost-efficiency: rate-on-line, payback period, ROL index relative to modeled expected loss [VERIFY current market benchmarks]

5. **Compile risk assessment report**
   - Summarize key findings with quantified metrics (not qualitative generalities)
   - Present modeled results in tabular and graphical format (EP curves, geographic heat maps, waterfall charts showing gross-to-net)
   - Highlight model divergence where vendor outputs differ materially (>15% at key return periods)
   - State all material assumptions: demand surge on/off, storm surge inclusion, fire-following earthquake, secondary uncertainty treatment
   - Recommend actions: reinsurance restructuring, underwriting restrictions by zone, data quality remediation

## Output

- **Executive summary**: Portfolio AAL, key return period PMLs (gross/net), accumulation status vs. limits, and top 3 risk concerns
- **Detailed EP curve analysis**: Tabular AEP and OEP results at standard return periods with year-over-year comparison
- **Accumulation dashboard**: Geographic concentration by peril zone with breach/headroom indicators
- **Reinsurance adequacy assessment**: Program performance under modeled and historical scenarios, coverage gap analysis
- **Model comparison matrix**: Side-by-side vendor results with commentary on drivers of divergence
- **Recommendations**: Prioritized action items with estimated risk reduction impact

## Quality Checks

- Confirm EP curve results are monotonically increasing (higher return period = higher loss) — non-monotonic results indicate data or modeling errors
- Verify AAL × multiplier reasonableness against market loss cost benchmarks [VERIFY against current industry loss ratios by peril/region]
- Cross-check net results against reinsurance treaty terms — ensure attachment, limit, and co-participation are correctly modeled
- Validate that all material perils are included (do not overlook flood in hurricane zones or fire-following in earthquake zones)
- Ensure exposure data vintage matches the effective period under analysis — stale SOVs produce misleading results
- Confirm that model settings (e.g., near-term vs. long-term hurricane view, warm SST assumptions) align with the company's stated risk philosophy
- Flag any use of flat rates or judgment-based overrides to modeled output — document rationale
