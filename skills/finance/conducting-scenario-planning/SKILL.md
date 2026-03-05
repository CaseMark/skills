---
name: conducting-scenario-planning
description: Structures financial scenario analysis with assumption modeling, sensitivity testing, and decision frameworks. Use when modeling scenarios, testing assumptions, or evaluating strategic options.
tags:
  - process
  - financial-planning-and-analysis
metadata:
  author: casemark
  practice_areas:
    - FP&A
    - Management Accounting
    - Business Intelligence
  document_types:
    - Process Documentation
  skill_modes:
    - Process Management
---
# Conducting Scenario Planning

Structures financial scenario analysis with assumption modeling, sensitivity testing, and decision frameworks for strategic and operational planning.

## When To Use

- Annual or quarterly budgeting cycles requiring upside/downside forecasts
- Evaluating capital allocation decisions (M&A, capex, new product lines)
- Stress-testing a business plan against macro or market disruptions
- Board or leadership presentations that need a range of financial outcomes
- Assessing go/no-go thresholds for strategic initiatives
- Contingency planning for supply chain, pricing, or demand shocks

## Inputs To Gather

- **Baseline financial model** — P&L, cash flow, and balance sheet projections with current assumptions
- **Key assumption variables** — the 5–10 drivers with the highest impact on outcomes (e.g., revenue growth rate, COGS %, customer churn, FX rates, interest rates)
- **Historical ranges** — actual min/max/mean values for each variable over a relevant lookback period (typically 3–5 years)
- **External benchmarks** — industry comps, analyst consensus, or macro forecasts that bound plausible ranges
- **Management hypotheses** — specific strategic actions or events to model (e.g., price increase, market entry, headcount freeze)
- **Decision criteria** — the metrics stakeholders will use to choose between scenarios (e.g., EBITDA margin, FCF breakeven, covenant compliance, IRR hurdle)

## Workflow

1. **Define scenario architecture**
   - Select the scenario framework: discrete scenarios (base/bull/bear), Monte Carlo simulation, or combinatorial matrix
   - For discrete scenarios, name and narratively define each case (e.g., "Bear: recession + 15% volume decline + 200bps rate increase")
   - Identify which variables shift between scenarios and which remain constant

2. **Set assumption ranges**
   - For each key variable, assign a value per scenario or a probability distribution
   - Document the source and rationale for every assumption (historical data, management estimate, third-party forecast)
   - Flag any assumption lacking empirical support with [VERIFY]

3. **Build scenario outputs**
   - Run each scenario through the financial model to produce projected P&L, cash flow, and balance sheet
   - Calculate decision-relevant metrics: revenue, EBITDA, net income, FCF, leverage ratios, liquidity runway, ROI/IRR
   - Capture the delta vs. baseline for each metric to highlight scenario impact

4. **Perform sensitivity analysis**
   - Isolate individual variables via one-at-a-time sensitivity (tornado chart)
   - Identify breakeven thresholds — the variable value at which a key metric crosses a critical boundary (e.g., "revenue must exceed $X for covenant compliance")
   - Run two-way sensitivity tables for the top correlated variable pairs

5. **Assess probability and risk**
   - Assign subjective or data-driven probability weights to each scenario if stakeholders require an expected-value view
   - Map scenarios to a risk matrix (likelihood × financial impact)
   - Identify tail-risk scenarios that, while low-probability, would be existential or covenant-breaking

6. **Develop decision framework**
   - Link each scenario outcome to a recommended action or contingency trigger
   - Define early-warning indicators that signal which scenario is materializing (e.g., "if Q1 bookings fall below $Y, activate cost-reduction playbook")
   - Present a decision table: scenario → metric outcome → recommended action → trigger/timeline

7. **Document and present**
   - Summarize findings in an executive brief: key takeaways, scenario comparison table, sensitivity highlights, and recommended path
   - Include an appendix with full assumption tables, model outputs, and methodology notes
   - Clearly separate facts, assumptions, and recommendations throughout

## Output

- **Scenario summary table** — side-by-side comparison of 3–5 scenarios across all decision metrics
- **Sensitivity analysis exhibits** — tornado chart ranking variable impact; two-way tables for top pairs; breakeven thresholds
- **Decision matrix** — scenario-to-action mapping with triggers and timelines
- **Assumption register** — complete list of every variable, its value per scenario, source, and confidence level
- **Executive narrative** — 1–2 page summary suitable for board or leadership review

## Quality Checks

- Every assumption has a documented source; unsupported assumptions are tagged [VERIFY]
- Scenario definitions are mutually distinct and collectively span a realistic range — no two scenarios overlap excessively
- Model mechanics are validated: baseline scenario ties back to the approved budget or latest forecast within acceptable tolerance [VERIFY against current approved numbers]
- Sensitivity analysis covers all variables identified as high-impact; no material driver is omitted
- Decision triggers are specific and measurable, not vague ("monitor closely")
- Outputs are stress-tested for internal consistency — e.g., cash flow aligns with P&L and balance sheet movements
- Tax rates, depreciation schedules, and working capital assumptions are jurisdiction-appropriate [VERIFY]
- Presentation distinguishes clearly between deterministic outputs and probability-weighted expected values
