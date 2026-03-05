---
name: conducting-stress-testing
description: Designs and executes portfolio and enterprise stress tests with scenario specification and result analysis. Use when stress testing portfolios, designing stress scenarios, or analyzing stress test results.
tags:
  - process
  - risk-management
  - portfolio
metadata:
  author: casemark
  practice_areas:
    - Risk Management
    - Enterprise Risk
    - Market Risk
  document_types:
    - Process Documentation
  skill_modes:
    - Process Management
---
# Conducting Stress Testing

## When To Use

- Designing scenario-based stress tests for portfolios, business lines, or enterprise-wide exposures
- Running regulatory stress tests (CCAR, DFAST, EBA/ECB exercises) or internal capital adequacy assessments
- Evaluating portfolio resilience to hypothetical or historical shock events
- Analyzing concentration risk, liquidity gaps, or tail-risk exposures under adverse conditions
- Preparing board-level or regulatory stress test reports with P&L impact and capital impact estimates

## Inputs To Gather

- **Portfolio data**: Current positions, asset classes, notional values, maturities, counterparty exposures, and hedges
- **Scenario specifications**: Macro variables to shock (GDP, unemployment, interest rates, credit spreads, FX, equity indices, commodity prices) with severity levels and time horizons
- **Historical reference events**: Specific episodes to replicate (e.g., 2008 GFC, COVID-19 March 2020, 2022 rate hiking cycle, SVB contagion)
- **Risk factor mappings**: How portfolio holdings map to stressed risk factors (betas, sensitivities, duration, convexity, Greeks)
- **Model assumptions**: Correlation behavior under stress, recovery rates, prepayment speeds, liquidity haircuts
- **Regulatory parameters**: Prescribed scenario variables and reporting templates if running a supervisory exercise [VERIFY: confirm applicable regulatory framework — Fed SR 12-7, EBA Guidelines, PRA SS3/21, or local equivalent]
- **Thresholds and limits**: Capital ratios, risk appetite limits, and early-warning triggers to evaluate against results

## Workflow

1. **Define scope and scenario design**
   - Classify test type: sensitivity (single-factor), scenario (multi-factor), reverse stress test, or enterprise-wide
   - For historical scenarios, source actual market moves for the reference period and calibrate shocks to current portfolio composition
   - For hypothetical scenarios, specify narrative (e.g., "stagflation with sovereign contagion"), translate to quantified risk factor shocks, and document the transmission channels
   - Set time horizon (instantaneous shock, 1-quarter, 9-quarter CCAR window) and granularity (daily, monthly, quarterly)

2. **Map exposures to risk factors**
   - Link each position or sub-portfolio to the stressed variables using factor sensitivities, regression betas, or full revaluation models
   - Identify second-order effects: margin calls, collateral shortfalls, funding cost increases, behavioral responses (deposit flight, drawdowns on credit lines)
   - Flag any positions with no clear risk factor mapping — mark with [VERIFY] and document proxy assumptions

3. **Execute stress calculations**
   - Apply shocks to compute stressed P&L at position, desk, business-line, and consolidated levels
   - Calculate stressed capital ratios (CET1, Tier 1, Total Capital) incorporating pre-provision net revenue (PPNR) projections under the scenario
   - Run liquidity stress: project cash inflows/outflows under the scenario, compute survival horizon, and test against LCR/NSFR minimums [VERIFY: applicable liquidity metrics for jurisdiction]
   - For reverse stress tests, solve backwards from a failure threshold (e.g., CET1 < 4.5%) to determine the scenario severity required

4. **Analyze and interpret results**
   - Rank loss contributors by magnitude — identify the top 5-10 drivers of stressed losses
   - Compare results across scenarios to isolate which risk factors matter most
   - Assess whether losses breach risk appetite limits, regulatory minimums, or internal early-warning triggers
   - Evaluate hedging effectiveness under stress: do hedges perform as expected or do correlation breakdowns erode protection?
   - Identify concentration risks that only become visible under stress conditions

5. **Document and report**
   - Produce an executive summary: scenario narrative, aggregate loss estimate, capital impact, key vulnerabilities
   - Include granular breakdowns by asset class, geography, counterparty, and business line
   - Present sensitivity analysis around key assumptions (e.g., +/-50bps on recovery rate, alternative correlation assumptions)
   - State all model limitations, data gaps, and proxy assumptions explicitly
   - Recommend management actions: position reductions, hedge adjustments, contingent capital planning, limit recalibrations

## Output

- **Stress test results report** containing: scenario descriptions, aggregate and segmented P&L impacts, capital ratio trajectories, liquidity projections, and breach analysis against limits
- **Heat map or dashboard view** ranking portfolios/business lines by vulnerability severity
- **Management action recommendations** with estimated risk reduction impact
- **Assumption and limitation disclosures** with [VERIFY] flags on jurisdiction-dependent parameters
- **Appendix** with detailed methodology, risk factor shock tables, and model validation notes

## Quality Checks

- Confirm all portfolio positions are captured — reconcile total notional/market value against source systems before and after stress
- Validate shock magnitudes against historical precedent (stressed moves should not be implausibly mild or extreme without justification)
- Check arithmetic consistency: sum of position-level losses should equal portfolio-level loss (absent diversification/correlation adjustments, which must be disclosed)
- Verify capital ratio calculations use correct RWA methodology and starting capital figures [VERIFY: confirm RWA approach — standardized vs. IRB/IMA]
- Ensure scenario narratives are internally consistent (e.g., a deflationary scenario should not assume rising commodity prices without explanation)
- Confirm results are presented in consistent units (same base currency, same reporting date, same accounting treatment)
- Review that all [VERIFY] items have been resolved or escalated before final submission
