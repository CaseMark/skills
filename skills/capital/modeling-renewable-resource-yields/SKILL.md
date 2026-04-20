---
name: modeling-renewable-resource-yields
language: en
description: Builds renewable energy yield models with resource assessment, capacity factor analysis, and P50/P90 production estimates. Use when modeling wind/solar yields, analyzing resource data, or evaluating production uncertainty.
tags:
  - modeling
  - real-assets-and-natural-resources
metadata:
  author: casemark
  practice_areas:
    - Natural Resources
    - Energy Capital
    - Commodity Investment
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Renewable Resource Yields

Builds renewable energy yield models with resource assessment, capacity factor analysis, and P50/P90 production estimates for wind, solar, and hybrid renewable projects.

## When To Use

- Underwriting a wind or solar asset acquisition and need independent yield expectations
- Structuring project finance debt sizing around P50/P90 production scenarios
- Comparing resource quality across candidate sites for development-stage projects
- Stress-testing existing yield assumptions during due diligence or refinancing
- Evaluating production shortfall risk for tax equity or hedge counterparty negotiations

## Inputs To Gather

- **Resource data**: TMY datasets (solar irradiance via NSRDB, Solargis, Meteonorm; wind speed/direction via reanalysis or on-site met mast data) — confirm measurement period length and data completeness percentage
- **Technology specs**: Turbine power curves (cut-in/cut-out/rated speeds), module datasheets (STC rating, temperature coefficients, bifacial gain), inverter efficiency curves
- **Site parameters**: Latitude/longitude, elevation, terrain roughness class, ground albedo, array layout and spacing, hub height or tracker configuration
- **Loss assumptions**: Electrical losses, soiling, snow, shading, curtailment, grid availability, turbine/inverter availability, wake losses (wind), clipping (solar)
- **Degradation rates**: Annual module degradation (typically 0.4–0.6%/yr for crystalline silicon), turbine performance degradation if applicable
- **Historical benchmarks**: Operational production data from comparable nearby projects if available [VERIFY availability]

## Workflow

1. **Assess resource quality**
   - For solar: compile GHI/DNI/DHI data, confirm data source vintage and spatial resolution, identify inter-annual variability (coefficient of variation)
   - For wind: analyze wind speed distributions (Weibull k and A parameters), wind rose directionality, vertical shear exponent, turbulence intensity at hub height
   - Flag any measurement gaps exceeding 5% of the dataset and document gap-filling methodology

2. **Configure energy conversion model**
   - Solar: run PVSyst-equivalent simulation — define system architecture (fixed-tilt vs. single-axis tracker), string sizing, GCR, backtracking algorithm, transposition model (Perez or similar)
   - Wind: apply power curve to wind speed distribution at hub height, account for air density correction, apply directional wake model (Jensen/Park or eddy-viscosity) for array losses
   - Document all software tools or analytical methods used [VERIFY against lender/investor IE standards]

3. **Apply loss stack**
   - Build a transparent waterfall from gross-to-net production: availability → electrical → soiling → snow → shading → curtailment → grid limitation → other
   - Benchmark each loss factor against industry ranges (e.g., soiling 1–5% depending on region, inverter clipping 1–3% for typical DC/AC ratios)
   - Identify which losses are modeled deterministically vs. probabilistically

4. **Generate P-values and uncertainty analysis**
   - Calculate P50 (median expected) net annual energy production (MWh/yr or GWh/yr)
   - Quantify uncertainty sources: resource inter-annual variability, measurement uncertainty, model uncertainty, long-term reference correlation uncertainty
   - Combine uncertainties (typically RSS for independent sources) to derive P75, P90, P95, P99 exceedance estimates
   - For debt sizing, confirm which P-value the lender requires (commonly P90 1-year or P99 1-year for merchant, P50 for equity base case) [VERIFY lender term sheet requirements]

5. **Derive capacity factor and benchmark**
   - Calculate net capacity factor = net annual production / (nameplate capacity × 8,760 hours)
   - Compare against regional benchmarks: U.S. utility-scale solar typically 20–30% (location-dependent), onshore wind 25–45%, offshore wind 40–55% [VERIFY against current EIA/NREL reference data]
   - Flag any result outside ±10% of regional comps for further review

6. **Sensitize key drivers**
   - Run sensitivities on: resource year variance (±1 standard deviation), degradation rate (±0.1%/yr), availability (base vs. stress), curtailment (0% to contractual cap)
   - Present tornado chart or scenario table showing production impact in MWh and revenue impact at contracted PPA price or merchant curve

## Output

- **Yield summary table**: Gross energy, loss waterfall, net energy (P50, P75, P90, P99), net capacity factor
- **Uncertainty breakdown**: Tabulated sources of uncertainty with individual and combined sigma values
- **Sensitivity matrix**: Key variable ranges and their impact on net production and DSCR (if debt-sized)
- **Resource data quality assessment**: Data completeness, measurement period, correlation methodology, and any flags
- **Assumptions register**: Every input assumption with source citation, date, and [VERIFY] tags where jurisdiction or contract-specific confirmation is needed

## Quality Checks

- Confirm gross-to-net loss stack sums correctly and no double-counting exists between loss categories
- Verify P90/P50 ratio falls within expected range (typically 0.82–0.92 for solar, 0.75–0.88 for wind depending on resource variability)
- Cross-check net capacity factor against NREL ATB or regional benchmarks — investigate deviations > 2 percentage points
- Ensure degradation is applied consistently (year 1 vs. mid-life vs. levelized) and matches financial model convention
- Validate that uncertainty sources are independent before applying RSS combination — correlated uncertainties require different treatment
- Confirm units consistency throughout (kWh vs. MWh vs. GWh, AC vs. DC nameplate)
- If operational data exists, compare modeled P50 to actual trailing-twelve-month production and explain variance
