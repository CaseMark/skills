---
name: analyzing-fiscal-policy
language: en
description: Evaluates government fiscal policy with budget impact, multiplier effects, and deficit/debt trajectory analysis. Use when analyzing fiscal policy, evaluating budget proposals, or assessing government spending impact.
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
# Analyzing Fiscal Policy

Evaluates government fiscal policy proposals and outcomes through budget impact scoring, fiscal multiplier estimation, and deficit/debt trajectory modeling to produce actionable analysis for economists, policy advisors, and institutional researchers.

## When To Use

- Assessing a proposed or enacted government budget (federal, state/provincial, municipal)
- Estimating the macroeconomic impact of tax changes, transfer programs, or public investment
- Projecting deficit and debt-to-GDP trajectories under alternative policy scenarios
- Comparing fiscal stimulus vs. austerity packages during business cycle inflection points
- Evaluating sustainability of entitlement spending, debt service costs, or revenue assumptions

## Inputs To Gather

- **Policy specification**: Legislative text, budget proposal, or executive order with spending/revenue line items
- **Baseline budget data**: Current-year revenues, outlays, deficit, and outstanding debt levels
- **Macroeconomic assumptions**: GDP growth rate, inflation, unemployment, interest rate forecasts [VERIFY against latest CBO/IMF/central bank projections]
- **Time horizon**: Typically 5-year or 10-year scoring window; confirm with requester
- **Scoring convention**: Static vs. dynamic scoring preference; if dynamic, specify model class (Keynesian multiplier, DSGE, reduced-form)
- **Jurisdiction**: Federal vs. subnational — balanced-budget requirements and borrowing constraints vary significantly [VERIFY]

## Workflow

1. **Establish the baseline**
   - Document current fiscal position: revenues, mandatory outlays, discretionary outlays, net interest, primary balance
   - Record debt-to-GDP ratio and weighted-average cost of borrowing
   - Identify the official baseline projection source (e.g., CBO baseline, OBR forecast, IMF Article IV) [VERIFY source vintage and assumptions]

2. **Decompose the policy change**
   - Separate revenue measures (tax rate changes, base broadening, credit/deduction modifications) from expenditure measures (new programs, funding level changes, sunset provisions)
   - Classify each component as temporary vs. permanent and mandatory vs. discretionary
   - Quantify gross budgetary cost/savings per year over the scoring window using static assumptions first

3. **Estimate fiscal multipliers**
   - Assign multiplier ranges by spending category:
     - Direct government purchases: typically 0.8–1.5x [VERIFY for current output gap conditions]
     - Transfer payments (unemployment, SNAP): typically 0.8–2.1x depending on marginal propensity to consume
     - Tax cuts — high-income: typically 0.3–0.6x; broad-based: 0.5–1.0x
     - Infrastructure investment: typically 1.0–2.0x over multi-year horizon
   - Adjust multipliers for monetary policy accommodation (zero lower bound vs. active tightening), exchange rate regime, and economy's position in the cycle
   - Note: multiplier estimates are model-dependent — present ranges, not point estimates

4. **Model deficit and debt trajectory**
   - Project annual deficits incorporating dynamic revenue feedback (if dynamic scoring requested)
   - Calculate debt-to-GDP path using assumed nominal GDP growth and effective interest rate
   - Test sensitivity to interest rate shocks (+100bp, +200bp), growth shortfalls (−1pp), and inflation deviations
   - Compute the fiscal gap or primary balance adjustment needed for debt stabilization over the horizon

5. **Assess macro and distributional effects**
   - Estimate GDP impact (level and growth rate) under the policy vs. baseline
   - Identify crowding-out risk: does increased government borrowing raise long-term rates or displace private investment?
   - Note distributional incidence where data permits (quintile-level tax burden shifts, transfer benefit changes)
   - Flag potential supply-side effects (labor supply responses to marginal tax rate changes, investment incentive shifts)

6. **Identify risks and structural concerns**
   - Highlight reliance on optimistic growth or revenue assumptions ("rosy scenario" risk)
   - Flag sunset provisions or budget gimmicks that mask true long-run cost
   - Assess political feasibility of assumed spending cuts or revenue raisers
   - Note contingent liabilities (loan guarantees, pension obligations) not captured in headline numbers

## Output

Structure the analysis report as follows:

- **Executive Summary**: One-paragraph verdict on net fiscal impact, multiplier-adjusted GDP effect, and debt sustainability assessment
- **Baseline Fiscal Position**: Table of current revenues, outlays, deficit, debt, and key macro assumptions
- **Policy Score**: Year-by-year static budget impact table (revenues, outlays, net deficit change)
- **Dynamic Effects**: Multiplier-adjusted GDP and revenue feedback estimates with stated assumptions
- **Debt Trajectory**: Chart-ready data showing debt-to-GDP under baseline, policy, and stress scenarios
- **Risk Factors**: Bullet list of key vulnerabilities (assumption sensitivity, political risk, structural imbalances)
- **Conclusion**: Net assessment with explicit confidence level (high/medium/low) and recommendation for further analysis if warranted

## Quality Checks

- Verify that static scores sum correctly across the scoring window and reconcile with any official scores available
- Confirm multiplier values are sourced and appropriate for the current macro environment — do not use textbook defaults without adjustment
- Ensure debt trajectory arithmetic is internally consistent (debt_t = debt_{t-1} + deficit_t; debt-to-GDP uses matching nominal GDP series)
- Check that sensitivity scenarios cover at least interest rate and growth downside cases
- Flag every jurisdiction-specific rule, statutory constraint, or data source with [VERIFY] where the analyst must confirm applicability
- Confirm the scoring window matches the requester's specification and any legislative convention (e.g., 10-year CBO window for US federal)
- Ensure no policy component is double-counted between revenue and expenditure sides
