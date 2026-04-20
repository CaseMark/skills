---
name: managing-economic-scenario-development
language: en
description: Structures macroeconomic scenario design with consistent variable paths and probability assessment. Use when building economic scenarios, designing stress test scenarios, or creating macro forecasts.
tags:
  - management
  - economic-analysis
metadata:
  author: casemark
  practice_areas:
    - Economic Research
    - Macroeconomics
    - Policy Analysis
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Economic Scenario Development

Structures macroeconomic scenario design with consistent variable paths and probability assessment.

## When To Use

- Building a scenario set for strategic planning, capital allocation, or risk management
- Designing stress test scenarios for regulatory submissions (CCAR, DFAST, ICAAP) or internal risk frameworks
- Creating baseline, upside, and downside macro forecasts for investment committees or board presentations
- Developing conditional forecasts around specific policy actions (rate decisions, fiscal stimulus, trade policy shifts)
- Coordinating multi-analyst scenario exercises where variable consistency across teams is critical

## Inputs To Gather

- **Forecast horizon**: short-term (1-4 quarters), medium-term (1-3 years), or long-term (5-10 years)
- **Geographic scope**: single-country, regional bloc, or global multi-economy
- **Core macro variables required**: GDP growth, inflation (CPI/PCE), unemployment, policy rates, yield curves, credit spreads, FX rates, commodity prices, housing prices [VERIFY which variables are mandated by the specific regulatory or internal framework]
- **Number of scenarios**: typically 3 (base/upside/downside) or 5+ for full distribution analysis
- **Probability weighting approach**: subjective expert assignment, model-derived, or hybrid
- **Narrative anchors**: the key shock or theme driving each non-base scenario (e.g., "prolonged stagflation," "rapid disinflation with rate cuts," "geopolitical supply disruption")
- **Existing constraints**: regulatory scenario parameters, board-mandated severity thresholds, or prior-period scenario continuity requirements

## Workflow

1. **Define the scenario architecture**
   - Set the number of scenarios, horizon, and periodicity (quarterly, annual)
   - Assign each scenario a narrative label and a 1-2 sentence thesis describing the primary economic mechanism
   - Establish probability weights summing to 100%; document the rationale for each weight

2. **Specify variable paths for the baseline**
   - Start with the consensus or internal house view for each macro variable
   - Ensure internal consistency: e.g., if GDP growth is above trend, unemployment should decline and capacity utilization should rise
   - Cross-check against current data releases and central bank forward guidance [VERIFY latest data vintage and release calendar]

3. **Build alternative scenario paths**
   - For each non-base scenario, identify the primary shock and trace its transmission through the macro system
   - Apply directional logic: a demand shock affects GDP and unemployment first, then inflation with a lag; a supply shock hits inflation and output simultaneously
   - Calibrate severity using historical analogues (e.g., magnitude of 2008 GDP decline, 1970s inflation spike, 2020 labor market shock) — state which analogue is referenced
   - Ensure variable paths are mutually consistent within each scenario; flag any deliberate deviations from standard macro relationships

4. **Validate cross-scenario consistency**
   - Check that the probability-weighted average of all scenarios is close to the baseline (it need not match exactly, but large deviations signal imbalance)
   - Verify that downside scenarios are sufficiently severe relative to the stated probability — a 10% probability scenario should reflect a genuinely adverse outcome, not a mild slowdown
   - Compare scenario spreads to historical realized volatility for each variable [VERIFY relevant historical sample period]

5. **Build the variable path tables**
   - Create a matrix: rows = variables, columns = time periods, layers = scenarios
   - Include quarter-over-quarter and year-over-year changes alongside levels where applicable
   - Add peak-to-trough metrics for stress scenarios (max drawdown in GDP, peak unemployment, widest credit spread)

6. **Document assumptions and limitations**
   - List every material assumption (e.g., "assumes no change in trade policy," "central bank follows forward guidance through Q2")
   - Note model dependencies: which variables are model-driven vs. judgment-based
   - Flag tail risks not captured in the scenario set

7. **Coordinate review and sign-off**
   - Route baseline to economics team lead; route stress scenarios to risk management
   - Resolve inter-team inconsistencies (e.g., equity research using different GDP assumptions than credit)
   - Lock the scenario set with a version number and effective date

## Output

The deliverable is a **Scenario Design Report** containing:

- **Executive summary**: scenario count, horizon, key themes, and probability weights
- **Narrative descriptions**: 1-paragraph thesis for each scenario explaining the driving mechanism and key risks
- **Variable path tables**: full numeric paths for all specified macro variables across all scenarios and time periods
- **Historical calibration exhibit**: table comparing scenario severity to selected historical episodes
- **Probability-weighted summary statistics**: expected values and ranges for key variables
- **Assumption log**: complete list of stated assumptions, judgment overrides, and data vintage references
- **Limitations and exclusions**: risks or variables deliberately excluded from the scenario set

## Quality Checks

- Every macro variable path is internally consistent within its scenario (no conflicting directional signals without explicit justification)
- Probability weights are documented with rationale and sum to 100%
- At least one downside scenario meets or exceeds the severity of a relevant historical stress episode
- Variable paths cover the full specified horizon with no gaps in periodicity
- All data sources and vintages are cited; stale inputs are flagged with [VERIFY]
- The probability-weighted mean is compared to the baseline and any material divergence is explained
- Scenario narratives match the numeric paths — if the narrative says "deep recession," GDP paths must reflect contraction, not mild slowdown
- Cross-team variable consistency is confirmed (same GDP, rate, and inflation assumptions used by all downstream consumers)
