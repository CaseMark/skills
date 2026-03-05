---
name: analyzing-productivity-trends
description: Structures productivity analysis with labor productivity, TFP estimation, and growth accounting decomposition. Use when analyzing productivity, estimating TFP, or decomposing growth drivers.
tags:
  - analysis
  - economic-analysis
  - accounting
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
# Analyzing Productivity Trends

## When To Use

- Measuring labor productivity (output per hour or per worker) across sectors, countries, or time periods
- Estimating total factor productivity (TFP) as a residual after accounting for capital and labor contributions
- Decomposing GDP or output growth into factor accumulation vs. efficiency gains (growth accounting)
- Evaluating productivity slowdowns, convergence patterns, or structural breaks
- Supporting policy memos on competitiveness, wage-productivity gaps, or technology adoption impacts

## Inputs To Gather

- **Output data**: Real GDP, gross value added (GVA) by sector, or firm-level revenue — specify deflator and base year [VERIFY base year and price index source]
- **Labor inputs**: Total hours worked, employment headcount, or quality-adjusted labor input (QALI) — note whether self-employed are included
- **Capital inputs**: Capital stock series (perpetual inventory method preferred), capital services index, or investment flows with depreciation assumptions [VERIFY depreciation rates by asset class]
- **Factor shares**: Labor and capital income shares from national accounts or firm data — confirm whether mixed income is allocated
- **Time frame and frequency**: Quarterly vs. annual; specify if cyclical adjustment (HP filter, production function approach) is needed
- **Scope**: Economy-wide, sectoral (ISIC/NAICS classification level), or firm-level panel

## Workflow

1. **Define the productivity measure**
   - Labor productivity: Y/L (output per hour) or Y/N (output per worker)
   - Capital productivity: Y/K (output per unit of capital services)
   - TFP: residual from a production function specification (typically Cobb-Douglas or translog)
   - Decide between level comparisons (PPP-adjusted cross-country) vs. growth rate analysis

2. **Prepare and validate data**
   - Align output and input series to common time periods and sectoral classifications
   - Check for structural breaks (reunification, reclassification, methodology changes) [VERIFY national accounts revision dates]
   - Convert nominal series to real terms using appropriate deflators — GDP deflator for aggregate, producer price indices for sectoral
   - For cross-country work, apply PPP conversion factors [VERIFY PPP vintage — ICP round matters]

3. **Compute labor productivity**
   - Calculate Y/L growth rates (log differences for continuous compounding or simple percentage changes)
   - Decompose into within-sector productivity growth vs. between-sector reallocation (shift-share analysis)
   - Standard shift-share: static effect + dynamic (cross-term) effect; or use the Fabricant/Tang-Wang decomposition

4. **Estimate TFP using growth accounting**
   - Specify production function: Y = A * F(K, L) — typically Y = A * K^α * L^(1-α)
   - Growth accounting identity: ΔlnA = ΔlnY − α·ΔlnK − (1−α)·ΔlnL
   - Set α from factor income shares (commonly 0.30–0.40 for advanced economies) [VERIFY country-specific capital share]
   - For quality-adjusted inputs: weight labor by education/experience cells; weight capital by asset-type rental prices
   - Report TFP as a residual — flag that it captures measurement error, scale effects, and omitted factors, not just "technology"

5. **Perform sensitivity and robustness checks**
   - Vary α ± 0.05 to test sensitivity of TFP estimates to capital share assumptions
   - Compare results under different capital stock assumptions (varying depreciation rates, initial stock estimates)
   - Test alternative functional forms if data supports it (translog allows variable elasticity of substitution)
   - Check whether results change with cyclical adjustment (capacity utilization correction for capital)

6. **Interpret trends and structural patterns**
   - Identify acceleration/deceleration periods — link to known shocks (oil crises, financial crisis, pandemic)
   - Assess convergence: are lagging sectors/countries catching up? (β-convergence regression if cross-sectional)
   - Decompose TFP into allocative efficiency vs. within-firm technical change where micro data permits
   - Evaluate the wage-productivity gap: compare real compensation growth to labor productivity growth, noting deflator differences (CPI vs. GDP deflator)

## Output

Structure the analysis report as follows:

- **Executive summary**: Key productivity metric, direction of trend, and primary driver (factor accumulation vs. TFP)
- **Data and methodology**: Sources, time coverage, production function specification, factor share assumptions
- **Labor productivity results**: Level and growth tables, shift-share decomposition if multi-sector
- **Growth accounting results**: Contributions of capital deepening, labor quality, and TFP to output growth — present in tabular form with sub-period breakdowns
- **Sensitivity analysis**: Range of TFP estimates under alternative assumptions
- **Interpretation**: Structural drivers (technology diffusion, regulation, human capital), cyclical vs. secular decomposition
- **Limitations**: Data gaps, measurement issues (intangible capital, platform economy), residual interpretation caveats

Include charts: labor productivity index (base year = 100), stacked bar of growth contributions, TFP trend line with confidence band if estimated econometrically.

## Quality Checks

- Factor contributions must sum to total output growth (accounting identity) — any discrepancy indicates a computation error
- TFP growth should be plausible in magnitude (typically 0.5–2.0% annually for advanced economies; flag outliers)
- Labor share + capital share = 1 under constant returns to scale — confirm this holds or document deviation
- Cross-country comparisons use consistent PPP benchmarks and sectoral classifications [VERIFY OECD STAN vs. EU KLEMS vs. Penn World Table version consistency]
- Shift-share components must sum to aggregate labor productivity growth — verify the decomposition is exhaustive
- Mark any imputed or interpolated data points with [VERIFY] in output tables
- Distinguish between labor productivity (partial measure) and TFP (multi-factor residual) clearly in all narrative — never conflate the two
