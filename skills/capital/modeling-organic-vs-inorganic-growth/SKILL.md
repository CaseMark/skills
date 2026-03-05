---
name: modeling-organic-vs-inorganic-growth
description: Compares build vs buy alternatives with risk-adjusted returns, time-to-value, and execution probability assessment. Use when evaluating growth strategies, comparing M&A vs organic investment, or analyzing make-vs-buy decisions.
tags:
  - modeling
  - capital-allocation-and-corporate-strategy
  - risk
  - investment
metadata:
  author: casemark
  practice_areas:
    - Corporate Strategy
    - Capital Allocation
    - Shareholder Value
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Organic Vs Inorganic Growth

Compares build vs. buy alternatives with risk-adjusted returns, time-to-value, and execution probability assessment for capital allocation decisions.

## When To Use

- Evaluating whether to build a capability internally or acquire it via M&A
- Comparing capital deployment options across organic R&D, partnerships, and acquisitions
- Assessing strategic alternatives for board or investment committee presentations
- Testing the sensitivity of a make-vs-buy decision to key assumptions (integration risk, time-to-revenue, market timing)

## Inputs To Gather

- **Organic path**: Estimated build cost (capex + opex), hiring plan, development timeline, expected ramp curve to steady-state revenue, probability of technical/market success
- **Inorganic path**: Target valuation range (EV/Revenue, EV/EBITDA comps), expected synergies (revenue and cost), integration cost and timeline, deal structure (cash/stock/earnout mix)
- **Shared baseline**: Current revenue and margin profile, cost of capital (WACC or hurdle rate), tax rate, terminal growth assumption, planning horizon (typically 5–7 years)
- **Risk parameters**: Execution probability for each path, integration failure rate benchmarks for the sector [VERIFY against industry data], competitive response assumptions

## Workflow

1. **Frame the decision** — Define the specific capability or market being targeted. Clarify whether the comparison is binary (build vs. one target) or multi-option (build vs. multiple acquisition candidates vs. partnership).

2. **Model the organic path**
   - Build a bottoms-up cost model: headcount, infrastructure, marketing spend to launch
   - Project a revenue ramp curve with explicit assumptions on time-to-first-revenue, penetration rate, and steady-state share
   - Apply a probability-of-success discount (e.g., 40–70% for new product lines depending on adjacency) [VERIFY probability assumptions against company track record]
   - Calculate NPV of risk-adjusted free cash flows

3. **Model the inorganic path**
   - Start with acquisition cost: purchase price, transaction fees (typically 2–5% of deal value), financing costs
   - Layer in integration costs: systems migration, redundancy/severance, customer attrition during transition (commonly 5–15% for B2B) [VERIFY attrition assumptions]
   - Project synergy realization timeline — cost synergies typically 12–18 months, revenue synergies 24–36 months
   - Apply an execution-probability haircut to synergies (full synergy realization is rare; use 60–80% of projected synergies as base case)
   - Calculate NPV including all-in acquisition cost as the upfront outflow

4. **Build the comparison framework**
   - Side-by-side NPV and IRR for each path at base, upside, and downside scenarios
   - Time-to-value comparison: months to breakeven contribution, months to target revenue run-rate
   - Risk-adjusted return: expected value (NPV × probability of success) for each path
   - Strategic optionality value: does one path create options the other forecloses (e.g., acqui-hire talent, platform for bolt-ons)?

5. **Run sensitivity and scenario analysis**
   - Tornado chart on the top 5 variables: discount rate, synergy realization %, time-to-revenue, purchase price multiple, organic success probability
   - Break-even analysis: at what acquisition premium does organic become preferred? At what organic delay does inorganic win?
   - Monte Carlo simulation if input distributions are available

6. **Synthesize the recommendation**
   - Summarize which path delivers higher risk-adjusted value and under what conditions
   - Identify the key swing variables that could change the conclusion
   - Flag any non-financial considerations: cultural fit, regulatory approval risk [VERIFY antitrust thresholds], talent retention, speed-to-market in a competitive window

## Output

Deliver a structured comparison memo containing:

- **Executive summary** — One-paragraph recommendation with the primary rationale and the margin of difference
- **Assumptions table** — All key inputs for both paths, sourced and flagged where estimated
- **Financial comparison** — Side-by-side NPV, IRR, payback period, and risk-adjusted expected value
- **Time-to-value chart** — Visual showing cumulative cash flow or revenue contribution over the planning horizon for each path
- **Sensitivity summary** — Tornado chart and break-even thresholds for critical variables
- **Risk register** — Top 3–5 risks per path with likelihood and impact ratings
- **Recommendation and conditions** — Preferred path with explicit conditions under which the recommendation would reverse

## Quality Checks

- NPV calculations use consistent discount rates across both paths (or justify differing rates, e.g., higher WACC for riskier organic build)
- Synergy projections are benchmarked against comparable transactions, not management aspirations alone
- Time-to-value estimates account for realistic ramp periods — not hockey-stick assumptions
- Integration costs are not understated; verify against post-mortem data from prior deals if available
- Probability-of-success discounts are applied to both paths, not just one
- The model does not double-count synergies (e.g., counting revenue synergies in both the target's standalone projection and the combined entity)
- Terminal value does not dominate total NPV (if >60% of value is in terminal, stress-test terminal assumptions separately)
- All [VERIFY] items are resolved or explicitly flagged for decision-maker review before finalizing
