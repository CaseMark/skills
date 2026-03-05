---
name: analyzing-trade-and-currency
description: Structures trade balance analysis with currency dynamics, competitiveness assessment, and tariff impact modeling. Use when analyzing trade data, evaluating currency trends, or assessing trade policy impact.
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
# Analyzing Trade And Currency

Structures trade balance analysis with currency dynamics, competitiveness assessment, and tariff impact modeling.

## When To Use

- Analyzing a country's or region's trade balance trajectory and underlying drivers
- Evaluating currency movement impacts on export competitiveness or import costs
- Modeling the effects of tariff changes, trade agreements, or sanctions on trade flows
- Assessing terms-of-trade shifts and their implications for current account sustainability
- Preparing policy briefs or investment memos that depend on trade/currency dynamics

## Inputs To Gather

- **Trade data**: Bilateral or aggregate exports/imports by commodity or sector (HS code level if available), time series spanning at least 3-5 years
- **Currency data**: Nominal and real effective exchange rate (NEER/REER) series; spot rates for key bilateral pairs
- **Policy context**: Current tariff schedules, recent trade agreement changes, active sanctions or quotas [VERIFY against latest trade authority publications]
- **Macro indicators**: GDP growth, inflation differentials, interest rate differentials, foreign reserve levels, capital account flows
- **Scope parameters**: Country/region pair, time horizon, whether the analysis is retrospective, current-state, or forward-looking

## Workflow

1. **Define scope and framing**
   - Confirm country/region pairs, commodity sectors, and time period
   - Identify whether the deliverable is a trade balance decomposition, currency impact assessment, tariff scenario model, or combined analysis
   - State the base currency and deflator conventions upfront

2. **Construct trade balance profile**
   - Decompose the trade balance into goods vs. services, and further by top commodity/sector categories
   - Calculate concentration ratios (e.g., top-5 export share) to assess vulnerability
   - Identify structural vs. cyclical components using trend/cycle decomposition or rolling averages

3. **Analyze currency dynamics**
   - Chart NEER and REER over the analysis window; note divergences between nominal and real rates
   - Assess pass-through: estimate how exchange rate movements translate into export/import price changes using historical elasticity benchmarks [VERIFY elasticity estimates against recent empirical literature for the specific economy]
   - Evaluate central bank intervention patterns (reserve changes, forward positions) and stated FX policy regime

4. **Assess competitiveness**
   - Compute unit labor cost indices or relative price indices vs. key trading partners
   - Compare revealed comparative advantage (RCA) indices across sectors to identify competitive positioning
   - Flag sectors where currency misalignment may mask or amplify underlying competitiveness shifts

5. **Model tariff and policy impacts**
   - For each tariff scenario, estimate direct price effects on affected trade lines using tariff-equivalent ad valorem rates
   - Apply trade elasticity estimates (import demand elasticity, export supply elasticity) to project volume changes [VERIFY elasticity values are appropriate for the product categories and country pair]
   - Account for trade diversion: identify likely substitute suppliers or destination markets
   - Quantify fiscal revenue effects of tariff changes where relevant

6. **Synthesize findings**
   - Link trade balance movements to currency trends and policy shifts in a unified narrative
   - Highlight feedback loops (e.g., trade surplus driving currency appreciation, eroding competitiveness)
   - Distinguish between short-run adjustment dynamics and medium-term structural trends

## Output

Structure the analysis report with:

- **Executive summary**: Key findings in 3-5 bullet points with quantified magnitudes
- **Trade balance analysis**: Decomposed by sector/partner with trend assessment
- **Currency dynamics section**: NEER/REER analysis, pass-through estimates, policy regime context
- **Competitiveness scorecard**: RCA shifts, unit cost comparisons, sectoral outlook
- **Scenario analysis table**: Tariff/policy scenarios with projected trade flow changes, revenue effects, and confidence ranges
- **Risk factors and limitations**: Data gaps, elasticity uncertainty, political/regulatory risks

Present currency figures with explicit base-year notation. Use constant-dollar or PPP-adjusted values for cross-country volume comparisons. Include source citations for all external data.

## Quality Checks

- Verify that trade data sums reconcile (exports + imports = total trade; bilateral flows cross-check with mirror data from partner countries)
- Confirm exchange rate series use consistent quotation conventions (direct vs. indirect) throughout
- Ensure elasticity estimates cited are sourced and time-period appropriate — flag any older than 10 years with [VERIFY]
- Check that tariff scenario results directionally align with economic intuition (e.g., higher tariffs reduce imports ceteris paribus)
- Validate that competitiveness indicators and trade balance trends tell a coherent story; investigate and explain any apparent contradictions
- Confirm all data vintages and revision statuses are noted — preliminary vs. final release matters for recent periods
