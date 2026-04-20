---
name: analyzing-inflation-dynamics
language: en
description: Structures inflation analysis with component decomposition, expectations tracking, and Phillips curve assessment. Use when analyzing inflation, decomposing CPI/PCE, or tracking inflation expectations.
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
# Analyzing Inflation Dynamics

Structures inflation analysis with component decomposition, expectations tracking, and Phillips curve assessment.

## When To Use

- Decomposing CPI or PCE inflation into component drivers (food, energy, shelter, core goods, core services)
- Assessing whether current inflation is demand-pull, cost-push, or expectations-driven
- Tracking inflation expectations across market-based and survey-based measures
- Evaluating Phillips curve dynamics (output gap vs. inflation tradeoff)
- Preparing macro research notes, policy briefs, or investment committee memos on the inflation outlook
- Analyzing pass-through effects from commodity prices, wages, or supply shocks

## Inputs To Gather

- **Headline and core inflation series**: CPI-U, CPI-W, Core CPI (ex food & energy), PCE, Core PCE, trimmed-mean PCE, median CPI — specify frequency (monthly, quarterly, annual) and time horizon
- **Component-level data**: BLS CPI component weights and contributions; shelter (OER, rent of primary residence), medical care, transportation, apparel, etc.
- **Inflation expectations measures**: 5y5y breakeven, TIPS breakeven spreads, University of Michigan survey (1-year, 5-year), NY Fed Survey of Consumer Expectations, SPF median forecasts
- **Labor market inputs**: unemployment rate, NAIRU estimate, unit labor costs, average hourly earnings, employment cost index (ECI)
- **Supply-side indicators**: commodity price indices (WTI, Henry Hub, FAO food index), shipping rates, ISM prices-paid, supplier delivery times
- **Policy context**: current federal funds rate, Fed dot plot, recent FOMC statement language, QT pace, fiscal impulse estimates

## Workflow

1. **Establish the inflation snapshot**
   - Report latest headline and core readings for CPI and PCE (month-over-month, 3-month annualized, year-over-year)
   - Compare to Fed's 2% PCE target and recent trend
   - Flag any divergence between CPI and PCE due to weighting or methodological differences [VERIFY methodology changes in current BLS/BEA releases]

2. **Decompose by component**
   - Break headline CPI into major categories: food at home, food away from home, energy (gasoline, electricity, natural gas), shelter, core goods, core services ex-shelter
   - Calculate contribution to headline change for each component (weight x price change)
   - Identify sticky vs. flexible components using Atlanta Fed sticky-price CPI
   - Flag any one-off or seasonal distortions (e.g., used car index volatility, airfare seasonal adjustment issues)

3. **Assess underlying inflation momentum**
   - Compute trimmed-mean PCE (Dallas Fed) and median CPI (Cleveland Fed) to strip outliers
   - Track supercore (core services ex-housing PCE) as the Fed's preferred demand-sensitive gauge
   - Evaluate 3-month annualized vs. 12-month to detect acceleration or deceleration trends
   - Determine if diffusion is broadening (share of CPI components above 2%, 3%, 5% thresholds)

4. **Analyze inflation expectations**
   - Compare market-based measures: 5y breakeven, 5y5y forward, inflation swap rates
   - Compare survey-based measures: Michigan 1y and 5y, SPF, NY Fed SCE
   - Assess whether expectations remain anchored near 2% or show de-anchoring risk
   - Note any divergence between short-term and long-term expectations (signal of transitory vs. persistent perception)

5. **Evaluate Phillips curve and macro drivers**
   - Estimate output gap position (CBO potential GDP vs. actual) [VERIFY latest CBO estimates]
   - Compare unemployment rate to NAIRU/natural rate estimates [VERIFY current Fed/CBO NAIRU range]
   - Track unit labor cost growth and wage-price spiral indicators (ECI vs. productivity growth)
   - Assess fiscal impulse: government spending contribution to aggregate demand

6. **Identify supply-side and pass-through dynamics**
   - Track commodity input costs and their lagged pass-through to consumer prices
   - Evaluate supply chain normalization (supplier delivery times, inventory-to-sales ratios)
   - Assess exchange rate pass-through for import prices
   - Note any sector-specific shocks (e.g., insurance, auto repair, housing supply constraints)

7. **Synthesize outlook and risk assessment**
   - State base case inflation trajectory (next 6-12 months) with key assumptions
   - Identify upside risks (energy shock, wage acceleration, fiscal expansion, de-anchored expectations)
   - Identify downside risks (demand destruction, credit tightening, commodity deflation, productivity gains)
   - Assess policy implications: likelihood of rate cuts/hikes, QT continuation, forward guidance shift

## Output

- **Inflation Dashboard Table**: latest headline CPI, core CPI, headline PCE, core PCE, trimmed-mean PCE, supercore — each with MoM, 3M annualized, and YoY
- **Component Contribution Chart Description**: ranked list of components by contribution to headline change
- **Expectations Summary**: table of market-based and survey-based expectations with trend arrows
- **Phillips Curve Assessment**: current positioning (unemployment vs. inflation) and directional call
- **Outlook Narrative**: 2-4 paragraph synthesis with base case, risk skew, and policy implication
- **Key Monitoring Points**: 3-5 specific data releases or thresholds to watch going forward

## Quality Checks

- Confirm CPI and PCE readings match official BLS/BEA releases — do not rely on stale data [VERIFY release dates]
- Verify component weights are current (BLS updates CPI weights annually in January) [VERIFY weight revision timing]
- Ensure breakeven inflation figures are adjusted for inflation risk premium and liquidity premium where relevant
- Cross-check survey expectations against the most recent release dates (Michigan is preliminary then final; SPF is quarterly)
- Distinguish between seasonally adjusted and non-seasonally adjusted figures — never mix them in comparisons
- Flag if analysis period spans a methodological change (e.g., OER calculation updates, geometric mean vs. arithmetic mean)
- Mark any forward-looking projection as an estimate, not a forecast guarantee
