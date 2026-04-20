---
name: analyzing-stranded-asset-risk
language: en
description: Evaluates stranded asset exposure for fossil fuel and carbon-intensive investments with transition modeling. Use when analyzing stranded assets, evaluating fossil fuel exposure, or modeling transition risk.
tags:
  - analysis
  - sustainable-finance
  - risk
  - investment
metadata:
  author: casemark
  practice_areas:
    - ESG
    - Impact Investing
    - Sustainable Finance
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Stranded Asset Risk

Evaluates stranded asset exposure for fossil fuel and carbon-intensive investments with transition modeling.

## When To Use

- Assessing portfolio exposure to fossil fuel reserves that may become uneconomic under climate policy or market transition scenarios
- Evaluating capital expenditure plans for carbon-intensive assets against decarbonization timelines
- Modeling write-down risk for upstream oil & gas, thermal coal, or high-emission infrastructure holdings
- Stress-testing investment theses against IEA Net Zero, NGFS, or custom transition pathways
- Supporting TCFD-aligned reporting on transition risk and asset impairment

## Inputs To Gather

- **Asset or portfolio data**: reserve estimates (proved/probable/possible), production profiles, remaining useful life, book value vs. fair value, and capital committed
- **Commodity price assumptions**: current forward curves plus scenario-based price decks (e.g., IEA STEPS, APS, NZE by 2050)
- **Policy and regulatory landscape**: carbon pricing (current and projected), phase-out timelines, subsidy removal schedules [VERIFY jurisdiction-specific carbon tax rates and cap-and-trade parameters]
- **Technology substitution curves**: renewable levelized cost trajectories, electrification rates, CCUS cost assumptions
- **Transition scenario selection**: NGFS orderly/disorderly/hot-house, IEA scenarios, or bespoke client scenarios
- **Discount rate and time horizon**: typically 10-30 year horizon; clarify whether using WACC, social cost of carbon, or risk-adjusted rate
- **Counterparty/operator data**: breakeven costs per barrel/ton, hedging positions, decommissioning liabilities

## Workflow

1. **Define scope and materiality threshold**
   - Identify which asset classes are in scope (upstream reserves, midstream infrastructure, power generation, heavy industry)
   - Set a materiality threshold (e.g., assets representing >1% of portfolio NAV or >X Mt CO2e)
   - Confirm the transition scenarios to model (minimum two: a base/reference case and at least one accelerated-transition case)

2. **Build the asset-level exposure profile**
   - Map each asset to its carbon intensity (Scope 1+2 at minimum; Scope 3 for fossil fuel reserves)
   - Calculate the unburnable carbon fraction: compare reserve volumes against carbon budgets under each scenario
   - Estimate breakeven prices and compare against scenario price decks — assets with breakeven above scenario price are flagged as stranding candidates

3. **Model transition pathways and impairment triggers**
   - For each scenario, project revenue streams using scenario-specific demand and price curves
   - Apply policy cost overlays: carbon tax escalation, emissions trading costs, regulatory compliance capex
   - Identify the stranding year — the point at which operating costs plus carbon costs exceed revenue under each scenario
   - Quantify potential write-down as the difference between current book value and discounted cash flows under the stranded scenario

4. **Assess portfolio-level impact**
   - Aggregate asset-level stranding losses to portfolio level
   - Calculate stranded asset ratio: (value at risk from stranding) / (total portfolio value)
   - Segment results by geography, commodity, and time horizon (near-term 2030, mid-term 2040, long-term 2050)
   - Compare against peer portfolios or benchmark indices where data is available

5. **Evaluate mitigation options**
   - Identify assets with credible transition plans (fuel switching, CCUS retrofits, repurposing)
   - Assess divestment timing vs. managed decline economics
   - Flag assets where decommissioning liabilities may exceed residual value
   - Note hedging or insurance instruments that offset near-term stranding risk

6. **Compile findings and recommendations**
   - Summarize stranding exposure by scenario in a comparison table
   - Highlight the highest-risk positions and recommended actions (divest, hedge, engage, hold-and-monitor)
   - Note key assumptions and sensitivity drivers (carbon price sensitivity, demand elasticity, technology cost learning rates)

## Output

The analysis report should contain:

- **Executive summary**: headline stranding exposure figures across scenarios, top 5 at-risk positions
- **Scenario comparison table**: rows = asset/sector groupings, columns = scenarios, cells = estimated impairment ($ and % of book value)
- **Asset-level detail cards**: for each material position — breakeven price, stranding year by scenario, mitigation feasibility rating (high/medium/low)
- **Sensitivity analysis**: tornado chart or table showing which input assumptions most affect total stranding exposure
- **Recommendation matrix**: action (divest/hedge/engage/monitor) mapped to each material position with rationale
- **Methodology appendix**: scenario sources, carbon budget assumptions, discount rates, data vintage

## Quality Checks

- Confirm carbon budget figures align with cited IPCC/IEA report vintage — do not mix AR5 and AR6 budgets [VERIFY which IPCC assessment cycle the client references]
- Validate breakeven cost data against recent operator filings or industry databases (Rystad, Wood Mackenzie)
- Ensure scenario price decks are internally consistent (e.g., NZE demand destruction should match NZE price levels)
- Check that discount rates are appropriate for the asset type and do not inadvertently minimize long-dated stranding risk
- Verify decommissioning liability estimates against regulatory requirements in each operating jurisdiction [VERIFY local decommissioning bond/fund requirements]
- Cross-check Scope 3 emissions factors against recognized databases (EXIOBASE, EPA emission factors) [VERIFY emission factor vintage]
- Confirm that the analysis does not constitute investment advice unless appropriately disclaimed — include standard disclaimer language for the output jurisdiction
