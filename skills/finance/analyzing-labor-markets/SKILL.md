---
name: analyzing-labor-markets
description: Structures employment data analysis with payroll, wage, and participation rate interpretation. Use when analyzing employment, interpreting jobs data, or assessing labor market conditions.
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
# Analyzing Labor Markets

Structures employment data analysis with payroll, wage, and participation rate interpretation.

## When To Use

- Interpreting a new BLS Employment Situation report (nonfarm payrolls, unemployment rate, hourly earnings)
- Assessing labor supply tightness for monetary policy or investment positioning
- Comparing regional or sectoral employment trends over time
- Evaluating wage growth dynamics relative to inflation and productivity
- Building a labor market dashboard for macro research or policy briefings

## Inputs To Gather

- **Headline data release**: Nonfarm payrolls change, unemployment rate (U-3), underemployment rate (U-6)
- **Wage data**: Average hourly earnings (month-over-month and year-over-year), Employment Cost Index if available
- **Participation metrics**: Labor force participation rate (LFPR), prime-age (25–54) LFPR, employment-population ratio
- **Supplemental indicators**: JOLTS (openings, quits, hires), initial and continuing jobless claims, ADP private payrolls
- **Scope parameters**: Time horizon, geographic focus (national vs. state/MSA), sector breakdown (goods-producing vs. services)
- **Revision history**: Prior two months' payroll revisions and net revision direction

## Workflow

1. **Anchor the headline numbers**
   - Record nonfarm payrolls change, unemployment rate, and average hourly earnings
   - Note prior-month revisions (net positive or negative) — revisions often matter more than the headline
   - Compare headline payrolls to consensus estimate and the 3-month / 6-month / 12-month moving averages

2. **Decompose the establishment survey**
   - Break payrolls by sector: goods-producing (manufacturing, construction, mining/logging) vs. private services (leisure/hospitality, healthcare, professional/business services, retail) vs. government
   - Identify which sectors drove the majority of the gain or loss
   - Flag any sector showing three or more consecutive months of contraction
   - Note temporary help services trend — a leading indicator of broader hiring momentum [VERIFY: confirm current BLS series ID for temp help]

3. **Analyze the household survey**
   - Compare household employment change to establishment payrolls change; persistent divergence signals measurement issues or structural shifts
   - Assess LFPR and prime-age LFPR — distinguish cyclical recovery from demographic drag (aging population effects)
   - Calculate U-6 minus U-3 spread; a widening spread indicates rising involuntary part-time or marginally attached workers
   - Review duration of unemployment distribution (median and mean weeks) for hysteresis risk

4. **Evaluate wage and cost dynamics**
   - Report average hourly earnings MoM and YoY; compare to core PCE or CPI to gauge real wage growth
   - Note composition effects: if low-wage sectors dominate hiring, aggregate wage growth may be biased downward
   - Where available, cross-reference with ECI (quarterly) for a composition-adjusted wage measure
   - Assess wage-productivity gap: wage growth persistently above productivity growth signals unit labor cost pressure [VERIFY: latest BLS productivity release quarter]

5. **Integrate leading and supplemental indicators**
   - JOLTS: openings-to-unemployed ratio (Beveridge curve position), quits rate as a confidence gauge
   - Initial claims: 4-week moving average trend direction; level relative to pre-recession baseline
   - Conference Board Help Wanted Online Index or Indeed job postings data if available
   - ISM employment sub-indices (manufacturing and services) for forward momentum

6. **Synthesize and frame implications**
   - Classify the labor market regime: overheating, full employment, softening, or contracting
   - Map findings to policy implications: Fed rate path expectations, fiscal policy pressure points
   - Identify two or three key risks (e.g., participation plateau, sector concentration, wage-price spiral risk)
   - State the investment or policy conclusion supported by the data

## Output

Deliver a structured labor market analysis report containing:

- **Executive summary** (3–5 sentences): headline verdict, key surprise vs. consensus, and primary implication
- **Data table**: payrolls (headline + revisions), unemployment rate, LFPR, average hourly earnings MoM/YoY, U-6, JOLTS openings (most recent)
- **Sector breakdown**: top three gaining and losing sectors by payroll change
- **Wage and participation assessment**: real wage trajectory, participation trend, composition caveats
- **Leading indicator dashboard**: claims trend, JOLTS quits rate, ISM employment
- **Regime classification**: current labor market characterization with supporting evidence
- **Implications**: 2–3 bullet points on monetary policy, fiscal, or market positioning takeaways
- **Risks and watch items**: factors that could shift the assessment in the next 1–3 months

## Quality Checks

- Payroll numbers cite the correct reference month and vintage (preliminary vs. revised)
- Revisions to prior months are explicitly stated — never silently use unrevised figures
- Seasonal adjustment noted; flag if analyzing non-seasonally-adjusted data [VERIFY: confirm SA vs. NSA series used]
- Unemployment rate denominator (civilian labor force) is correctly defined; do not conflate with working-age population
- Wage growth comparisons use consistent periodicity (MoM vs. YoY not mixed without labeling)
- Any cross-country or cross-state comparisons use matching definitions and survey methodologies
- Claims about "trend" require at least three data points; single-month moves labeled as such
- Mark all forward-looking statements (Fed expectations, recession probability) as analyst interpretation, not data fact
- [VERIFY] tags applied to any statute, regulation, or BLS methodology detail that may have changed since last confirmed update
