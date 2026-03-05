---
name: building-rolling-forecasts
description: Structures rolling forecast process with driver-based projections and continuous planning methodology. Use when creating rolling forecasts, updating financial projections, or managing continuous planning.
tags:
  - modeling
  - financial-planning-and-analysis
metadata:
  author: casemark
  practice_areas:
    - FP&A
    - Management Accounting
    - Business Intelligence
  document_types:
    - Model
  skill_modes:
    - Modeling
---
# Building Rolling Forecasts

## When To Use

- Creating or refreshing a rolling forecast (typically 12–18 month horizon that advances each period)
- Replacing or supplementing a static annual budget with continuous planning
- Updating projections mid-cycle after actuals post or when business conditions shift materially
- Building a driver-based forecast framework for a new business unit, product line, or entity
- Preparing management reporting that compares forecast vs. actuals with variance explanations

## Inputs To Gather

- **Forecast horizon and cadence**: Number of forward periods (e.g., 12 months, 6 quarters) and refresh frequency (monthly, quarterly)
- **Actuals data**: Latest closed-period financials — income statement, balance sheet, and cash flow as applicable
- **Key business drivers**: Revenue drivers (volume, price, mix, win rates), cost drivers (headcount, utilization, input costs), and working capital drivers (DSO, DPO, DIO)
- **Operating assumptions**: Planned hires, pricing changes, capacity expansions, contract renewals, seasonality patterns
- **Macro/external inputs**: FX rates, commodity prices, interest rate curves, inflation indices [VERIFY applicability per entity]
- **Prior forecast or budget**: Last iteration for trend comparison and variance bridge
- **Management guidance**: Strategic priorities, growth targets, margin expectations, or capital allocation directives

## Workflow

1. **Set forecast architecture**
   - Define the rolling window (e.g., current month + 11, current quarter + 5) and granularity (monthly vs. quarterly periods)
   - Identify the P&L / BS / CF line items in scope; exclude or simplify immaterial lines
   - Select driver-based vs. trend-based methodology per line item — use driver-based for lines where identifiable business levers exist and trend/run-rate for stable, low-variability items

2. **Lock actuals and establish the base**
   - Import closed-period actuals into the model and reconcile to the GL or reporting package
   - Calculate trailing metrics (growth rates, margins, ratios) that will seed forward assumptions
   - Document the cutoff date and any known post-close adjustments

3. **Build driver assumptions**
   - For each major line item, specify the driver formula:
     - Revenue: units × price, or pipeline × conversion rate, or recurring base ± net adds × ARPU
     - COGS: variable cost per unit × volume, plus fixed cost base ± step-function changes
     - OpEx: headcount × fully-loaded cost, plus discretionary spend tied to revenue % or fixed budgets
     - Working capital: revenue × (DSO / 365), COGS × (DIO / 365), OpEx × (DPO / 365)
   - Tag each assumption as confirmed, estimated, or placeholder [VERIFY with business owners before finalizing]
   - Apply seasonality indices where historical patterns are meaningful (flag if fewer than 2 years of history)

4. **Project forward periods**
   - Extend the driver model across the forecast horizon
   - Build in known discrete events: contract starts/ends, headcount ramp schedules, capex delivery dates, debt maturities
   - Ensure balance sheet balances and cash flow ties to the change in cash each period
   - Include an automated check row for BS balance and CF reconciliation

5. **Run scenarios and sensitivities**
   - Define base, upside, and downside cases by varying 2–4 key drivers (e.g., volume ±10%, price ±5%, hiring pace ±3 months)
   - Calculate impact on EBITDA, free cash flow, and any covenant or liquidity metrics
   - Highlight the drivers with the highest sensitivity coefficient for management focus

6. **Prepare variance bridge**
   - Compare the new forecast to the prior forecast and/or original budget
   - Decompose variances into volume, price, mix, cost, timing, and FX components where applicable
   - Provide concise narrative explanations for each material variance (>5% or >$X threshold — confirm threshold with stakeholders)

7. **Package output and document**
   - Produce a summary dashboard: key financial metrics by period, scenario comparison, and variance waterfall
   - Document all assumption sources, owner names, and refresh dates in an assumptions register
   - Flag items requiring management decision or further data before next refresh

## Output

- **Rolling forecast model**: Period-by-period P&L, BS, and CF projections with driver formulas visible and assumption cells clearly marked
- **Assumptions register**: Table listing each assumption, its value, source, owner, confidence level, and last-updated date
- **Scenario summary**: Base / upside / downside outcomes for key metrics (revenue, EBITDA, FCF, liquidity)
- **Variance bridge**: Waterfall or tabular decomposition showing forecast-to-forecast and forecast-to-budget changes with narrative
- **Management summary**: 1-page narrative highlighting key changes, risks, and decision points for leadership review

## Quality Checks

- All balance sheet periods balance (assets = liabilities + equity) — zero-tolerance check
- Cash flow statement reconciles to change in BS cash line each period
- Revenue and cost driver formulas are internally consistent (no circular references unless intentional and controlled)
- Seasonal patterns in the forecast align with historical seasonality within a reasonable tolerance
- Scenario outputs bracket historical actual ranges unless a structural change is documented
- No hard-coded values in projection periods — all forward cells trace to an assumption input or driver
- Assumption register has no blank owner or source fields for material line items
- Variance explanations cover ≥90% of total variance magnitude
- [VERIFY] Tax rate, depreciation method, and intercompany elimination assumptions align with current accounting policy and jurisdiction
