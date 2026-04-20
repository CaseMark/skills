---
name: modeling-mining-project-economics
language: en
description: Builds mining project financial models with resource estimation, mine plan integration, and commodity price sensitivity analysis. Use when modeling mining investments, analyzing feasibility studies, or evaluating mineral assets.
tags:
  - modeling
  - real-assets-and-natural-resources
  - investment
metadata:
  author: casemark
  practice_areas:
    - Natural Resources
    - Energy Capital
    - Commodity Investment
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Mining Project Economics

Builds mining project financial models with resource estimation, mine plan integration, and commodity price sensitivity analysis.

## When To Use

- Evaluating a mining project at PEA, pre-feasibility, or bankable feasibility stage
- Modeling acquisition economics for an operating or development-stage mineral asset
- Running commodity price sensitivity on an existing mine plan
- Stress-testing capital structure or financing scenarios for a mining investment
- Comparing multiple deposit or project alternatives on a risk-adjusted basis

## Inputs To Gather

- **Resource/reserve statement** — NI 43-101 or JORC-compliant technical report with measured, indicated, and inferred tonnages and grades
- **Mine plan** — annual production schedule (tonnes mined, strip ratio or development metres, processing throughput), mine life, and phasing
- **Metallurgical recovery** — process flow, expected recoveries by ore type, and concentrate specifications
- **Capital cost estimates** — initial capex (direct and indirect), sustaining capex schedule, closure/reclamation costs, and contingency percentages
- **Operating cost breakdown** — mining cost per tonne moved, processing cost per tonne milled, G&A, transport, and refining/treatment charges (TC/RC)
- **Commodity price assumptions** — spot, forward curve, broker consensus, and long-term real price deck; specify currency and inflation basis
- **Fiscal regime** — royalty structure (NSR, ad valorem, profit-based), corporate tax rate, depreciation/amortization rules, withholding taxes, and any stability agreements [VERIFY jurisdiction-specific rates and royalty formulas]
- **Financing terms** — debt quantum, interest rate, tenor, repayment profile, hedging commitments, stream/royalty obligations if applicable
- **Discount rate inputs** — risk-free rate, equity risk premium, country risk premium, beta, and any project-specific risk adjustments

## Workflow

1. **Structure the production model**
   - Map annual mine plan into the model: ore tonnes, waste tonnes, strip ratio, mill feed, head grade, and recovery
   - Separate open-pit and underground if both methods apply
   - Apply grade-tonnage curves to test sensitivity around cut-off grade assumptions

2. **Build the revenue module**
   - Calculate payable metal production (recovered metal × payable percentage)
   - Deduct treatment charges, refining charges, and transport costs to arrive at net smelter return (NSR)
   - Link revenue to the commodity price deck; allow toggling between spot, consensus, and user-defined scenarios

3. **Model operating costs**
   - Structure costs as mining, processing, G&A, and selling/transport on a per-unit basis (cost per tonne mined, cost per tonne milled)
   - Escalate costs annually using relevant inflation indices (CPI, diesel, labour, power)
   - Calculate all-in sustaining cost (AISC) and all-in cost (AIC) per payable ounce/pound/tonne for benchmarking

4. **Populate the capital schedule**
   - Phase initial capex across the construction timeline; apply drawdown curves
   - Schedule sustaining capex, deferred stripping or development, and expansion capex
   - Include closure and rehabilitation provisions with timing assumptions

5. **Apply the fiscal regime**
   - Model royalty calculations specific to jurisdiction (NSR-based, profit-based, sliding scale) [VERIFY]
   - Build tax depreciation schedules (straight-line, declining balance, or units-of-production as applicable) [VERIFY]
   - Calculate taxable income, tax losses carried forward, and cash tax payable
   - Include any tax holidays, investment incentives, or stability agreement terms [VERIFY]

6. **Construct the cash flow waterfall**
   - Build pre-tax and after-tax free cash flow (FCF) from revenue through capex and taxes
   - Layer in debt service (drawdowns, interest, principal repayment) to derive levered FCF and equity cash flows
   - If streaming or royalty financing exists, model as a separate cash flow deduction

7. **Calculate valuation metrics**
   - NPV at multiple discount rates (typically 5%, 8%, 10% real)
   - IRR (project-level and equity-level)
   - Payback period (simple and discounted)
   - NPV/capex ratio as a capital efficiency indicator

8. **Run sensitivity and scenario analysis**
   - One-variable sensitivity: commodity price, grade, recovery, capex, opex, discount rate, FX rate
   - Two-variable tornado chart: price vs. grade, price vs. capex
   - Scenario analysis: base case, upside (higher price / higher grade), downside (lower price / cost overrun / delayed ramp-up)
   - Monte Carlo simulation inputs if probabilistic analysis is required (define distributions for key variables)

## Output

- **Executive summary** — project NPV, IRR, payback, and AISC at base case with 2–3 key sensitivities highlighted
- **Annual cash flow schedule** — production, revenue, opex, capex, taxes, and FCF by year over the mine life
- **Sensitivity tables** — NPV and IRR across a matrix of commodity prices and discount rates
- **Tornado chart** — ranking of variables by impact on NPV
- **Unit cost analysis** — cash cost, AISC, and AIC benchmarked against industry peers
- **Financing summary** — debt coverage ratios (DSCR, LLCR) if project finance is modeled
- **Assumption register** — every input with source, date, and [VERIFY] flags for jurisdiction-dependent items

## Quality Checks

- Confirm resource classification (measured/indicated vs. inferred) matches the study stage — do not include inferred resources in feasibility-level economics without flagging
- Reconcile total mine production in the model against the mine plan in the technical report (within ±2%)
- Verify that AISC calculation follows World Gold Council or equivalent industry standard methodology
- Cross-check tax and royalty calculations against published fiscal terms for the jurisdiction [VERIFY]
- Ensure discount rate assumptions are consistent with the project's risk profile and peer comparables
- Validate that the model balances: opening cash + sources = uses + closing cash in every period
- Test boundary conditions — zero price, zero grade, and maximum capex overrun should produce logical (negative) results, not errors
- Flag any circular references (e.g., tax ↔ interest ↔ debt sizing) and document the resolution method (iteration or hard-code break)
