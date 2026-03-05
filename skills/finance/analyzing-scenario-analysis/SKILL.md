---
name: analyzing-scenario-analysis
description: Structures forward-looking scenario analysis with macroeconomic assumptions and portfolio impact assessment. Use when conducting scenario analysis, modeling macro scenarios, or assessing portfolio vulnerability.
tags:
  - analysis
  - risk-management
  - portfolio
metadata:
  author: casemark
  practice_areas:
    - Risk Management
    - Enterprise Risk
    - Market Risk
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Scenario Analysis

Structures forward-looking scenario analysis by defining macroeconomic assumptions, modeling transmission channels, and quantifying portfolio-level impact across base, adverse, and tail scenarios.

## When To Use

- Stress-testing a portfolio against potential macroeconomic shifts (recession, rate shocks, geopolitical disruption)
- Evaluating how changes in GDP growth, inflation, unemployment, or credit spreads cascade through asset classes
- Preparing risk committee or board-level scenario summaries for regulatory or internal governance purposes
- Assessing vulnerability of concentrated exposures under plausible-but-severe conditions
- Comparing portfolio resilience across multiple forward-looking narratives (e.g., soft landing vs. stagflation vs. hard landing)

## Inputs To Gather

- **Portfolio composition**: Asset class weights, sector/geography breakdown, top exposures, duration/convexity profile
- **Baseline macro assumptions**: Current consensus forecasts for GDP, CPI, fed funds rate, unemployment, credit spreads, and commodity prices
- **Scenario definitions**: Number of scenarios (typically 3–5), each with a narrative label, probability weight, and time horizon (6M, 1Y, 3Y)
- **Shock parameters per scenario**: Specific deviations from baseline for each macro variable (e.g., "GDP −3.5%, CPI +2.0pp, 10Y yield +150bps")
- **Transmission mappings**: How each macro variable links to asset-class returns—equity beta to GDP, credit spread sensitivity, duration impact on fixed income, FX pass-through [VERIFY: confirm institution-specific factor models or vendor models in use]
- **Historical reference periods**: Analogous episodes (e.g., 2008 GFC, 2020 COVID, 2022 rate-hiking cycle) to anchor severity calibration
- **Risk limits and thresholds**: Drawdown tolerances, VaR/CVaR limits, liquidity coverage ratios that define "breach" under stress

## Workflow

1. **Define scenario narratives** — Write a concise macro story for each scenario (2–3 sentences). Assign probability weights. Ensure scenarios span a range of outcomes: at minimum a base case, a moderate adverse case, and a severe/tail case.

2. **Set macro variable paths** — For each scenario, specify the trajectory of key variables across the time horizon. Present in a table:
   | Variable | Base | Adverse | Severe |
   |----------|------|---------|--------|
   | Real GDP growth | +2.1% | −0.5% | −3.5% |
   | CPI (YoY) | 2.4% | 4.0% | 6.5% |
   | Fed funds rate | 4.25% | 5.50% | 3.00% |
   | IG credit spread | 110bps | 200bps | 350bps |
   | Unemployment | 4.0% | 5.8% | 8.2% |

3. **Map transmission channels** — For each asset class or sub-portfolio, document how macro shocks translate to P&L impact:
   - Equities: earnings growth sensitivity to GDP, multiple compression under rising rates
   - Fixed income: duration × yield change, spread widening on credit
   - Alternatives: illiquidity discount, NAV lag adjustments
   - FX: carry unwind, safe-haven flows
   - Flag any non-linear or threshold effects (e.g., covenant breaches at spread > 300bps)

4. **Compute portfolio impact** — Apply shocks through the transmission model. For each scenario, calculate:
   - Total portfolio return / P&L change
   - Contribution by asset class and top individual positions
   - Change in risk metrics (VaR, CVaR, max drawdown estimate)
   - Liquidity impact: redemption capacity, margin call exposure

5. **Identify vulnerabilities and concentrations** — Highlight positions or sectors where losses are disproportionate to portfolio weight. Flag scenarios where risk limits are breached.

6. **Formulate risk-mitigation options** — For each material vulnerability, propose actionable hedges or rebalancing steps (e.g., "Add 2Y put spread on S&P to cap equity tail loss" or "Reduce HY allocation by 5pp to stay within CVaR limit under adverse scenario").

## Output

Structure the deliverable as follows:

- **Executive Summary**: One-paragraph overview of the most decision-relevant finding (e.g., "Under the severe scenario, portfolio drawdown reaches −18%, breaching the −15% board limit, driven primarily by HY credit and EM equity exposure").
- **Scenario Definitions Table**: Narratives, probability weights, macro variable paths.
- **Portfolio Impact Matrix**: Scenario × asset class P&L grid with total portfolio row.
- **Risk Metric Dashboard**: VaR, CVaR, max drawdown, liquidity coverage under each scenario vs. limits.
- **Vulnerability Heat Map**: Positions or sectors flagged red/amber/green by severity of scenario loss relative to weight.
- **Mitigation Recommendations**: Prioritized list of hedges or allocation changes with estimated cost and risk-reduction impact.
- **Assumptions & Limitations**: Explicitly state model limitations (e.g., linear approximation, no credit migration, static portfolio assumption). Mark jurisdiction- or regulation-dependent items with [VERIFY].

## Quality Checks

- Each scenario narrative is internally consistent (e.g., a deflationary recession should not pair with rising commodity prices without explanation)
- Macro variable paths are cross-checked against historical analogs for plausibility—no variable exceeds the most extreme observed move without explicit justification
- Portfolio impact sums to total—asset-class contributions reconcile to the aggregate P&L number
- Risk metric breaches are clearly flagged with reference to the specific limit or policy threshold
- Transmission assumptions are documented and source-attributed (vendor model, internal factor model, or regression-based) [VERIFY: confirm which factor/risk model framework the institution uses]
- Probability weights across scenarios sum to approximately 100%
- All data vintage dates are stated—stale inputs are flagged
