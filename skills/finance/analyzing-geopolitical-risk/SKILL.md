---
name: analyzing-geopolitical-risk
description: Structures geopolitical risk assessment with scenario planning, market impact analysis, and portfolio implications. Use when analyzing geopolitical events, assessing political risk, or evaluating conflict scenarios.
tags:
  - analysis
  - economic-analysis
  - risk
  - portfolio
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
# Analyzing Geopolitical Risk

## When To Use

- Evaluating how a specific geopolitical event (conflict, sanctions, election, coup, trade dispute) affects asset classes, sectors, or portfolios
- Building scenario trees for emerging political crises with probability-weighted market outcomes
- Assessing sovereign or country risk for investment allocation, credit exposure, or supply-chain decisions
- Providing macro backdrop analysis for investment committee memos or client advisories
- Stress-testing portfolio exposures against escalation/de-escalation scenarios

## Inputs To Gather

- **Event description**: The specific geopolitical situation — parties involved, timeline, current status, and triggering developments
- **Asset/portfolio scope**: Which holdings, sectors, regions, or asset classes need assessment (equities, fixed income, commodities, FX, alternatives)
- **Time horizon**: Near-term tactical (days/weeks), medium-term strategic (months), or structural (years)
- **Exposure data** (if available): Current portfolio weights, country/sector allocations, supply-chain dependencies
- **Historical analogues**: Prior events the user considers comparable (e.g., 2014 Crimea annexation, 2018 US-China tariffs, 1973 oil embargo)
- **Risk tolerance context**: Client type, mandate constraints, regulatory environment

## Workflow

1. **Frame the event and stakeholders**
   - Identify the principal actors (state, non-state, multilateral), their objectives, and leverage points
   - Map the escalation ladder: what triggers move the situation from current state to higher/lower severity
   - Classify risk type: armed conflict, sanctions/trade war, regime change, regulatory shift, resource disruption, cyber/hybrid

2. **Build scenario tree**
   - Define 3-4 discrete scenarios (e.g., de-escalation, status quo, limited escalation, full escalation)
   - Assign probability weights to each scenario with explicit reasoning — cite diplomatic signals, military posture, economic incentives, and domestic political pressures
   - For each scenario, specify the key observable indicators that would confirm or disconfirm it (leading signals)
   - [VERIFY] Probability assignments against current consensus from credible geopolitical risk firms or sovereign CDS spreads

3. **Map transmission channels to markets**
   - **Commodity supply**: Identify disrupted production, transit routes, or refining capacity (oil, gas, grain, metals)
   - **Trade flows**: Tariff escalation, export controls, sanctions lists, secondary sanctions risk
   - **Capital flows**: Sanctions on sovereign debt, SWIFT exclusion, capital controls, FDI freezes
   - **Sentiment/contagion**: Flight-to-safety dynamics (USD, UST, gold, CHF, JPY), risk-off correlation spikes
   - **FX and rates**: Central bank policy response, inflation pass-through from commodity shocks, EM currency stress
   - Quantify where possible: historical drawdowns in comparable episodes, implied vol shifts, basis-point impact on spreads

4. **Assess portfolio implications**
   - For each scenario, estimate P&L impact on relevant positions or sectors using sensitivity analysis
   - Identify concentrated exposures: direct country exposure, revenue dependency, supply-chain chokepoints
   - Flag second-order risks: sanctions compliance obligations, counterparty exposure to affected sovereigns, forced selling from index exclusion
   - Propose hedging or rebalancing options: put spreads on exposed indices, commodity hedges, duration adjustments, geographic diversification

5. **Determine monitoring triggers**
   - Define specific observable events that would shift scenario probabilities (e.g., UN vote outcome, troop movements, sanctions announcement)
   - Set review cadence tied to event timeline — daily during acute phase, weekly during extended tensions
   - Identify data sources for real-time tracking: government press releases, satellite imagery services, CDS/FX spot levels, shipping/AIS data

## Output

Structure the deliverable as follows:

- **Executive Summary** (1 paragraph): Event, base-case scenario, headline portfolio impact, recommended action
- **Event Overview**: Stakeholders, timeline, current status, and classification
- **Scenario Matrix**: Table with scenario name, description, probability, key triggers, and market impact per asset class
- **Transmission Channel Analysis**: For the base case and worst case, detail the specific channels through which risk propagates to the portfolio
- **Portfolio Impact Assessment**: Quantified exposure analysis with scenario-conditional P&L estimates where data permits
- **Recommended Actions**: Specific hedging, rebalancing, or monitoring steps ranked by urgency
- **Monitoring Dashboard**: Table of leading indicators, data sources, and threshold levels that would trigger reassessment

## Quality Checks

- Every scenario has explicit probability reasoning, not just a label — avoid "possible" without quantification
- Transmission channels are specific to the event (e.g., "Strait of Hormuz oil transit" not "commodity disruption")
- Historical analogues are used to calibrate, not to predict — note structural differences from prior episodes
- [VERIFY] Sanctions references against current OFAC/EU/UN consolidated lists and effective dates
- [VERIFY] Commodity production and trade-flow statistics against IEA, USDA, or USGS data
- Portfolio recommendations are implementable — specify instrument type, tenor, and approximate sizing rationale
- Flag where analysis relies on assumptions about government behavior that could change rapidly
- Include explicit disclaimer that geopolitical forecasting carries inherent uncertainty and is not investment advice unless embedded in a formal advisory
