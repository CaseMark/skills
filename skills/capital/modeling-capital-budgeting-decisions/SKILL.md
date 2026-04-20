---
name: modeling-capital-budgeting-decisions
language: en
description: Builds NPV, IRR, and payback models for capital investment decisions with hurdle rate calibration and risk adjustment. Use when evaluating capital investments, comparing project returns, or building capital allocation frameworks.
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
# Modeling Capital Budgeting Decisions

Builds NPV, IRR, and payback models for capital investment decisions with hurdle rate calibration and risk adjustment.

## When To Use

- Evaluating a proposed capital expenditure (new plant, equipment, technology platform, acquisition)
- Comparing two or more mutually exclusive projects competing for the same budget
- Setting or recalibrating a corporate hurdle rate for investment approvals
- Stress-testing an already-approved project under revised macro or operational assumptions
- Building a capital allocation ranking framework across business units or divisions

## Inputs To Gather

- **Project cash flows**: Initial outlay (CapEx), annual operating cash inflows/outflows, terminal or salvage value, and project life in years
- **Cost of capital components**: Risk-free rate, equity risk premium, beta (levered/unlevered), pre-tax cost of debt, target capital structure weights, marginal tax rate [VERIFY: tax rate by jurisdiction]
- **Hurdle rate policy**: Whether the firm uses a single corporate WACC, divisional hurdle rates, or project-specific rates; any stated premium above WACC for risk categories
- **Tax and depreciation schedule**: Depreciation method (straight-line, MACRS, declining balance), applicable asset class lives [VERIFY: depreciation schedules per local tax code]
- **Working capital requirements**: Incremental net working capital at launch, annual changes, and release at project end
- **Risk parameters**: Probability-weighted scenario definitions (base, upside, downside), key variable ranges for sensitivity analysis, correlation assumptions if running Monte Carlo

## Workflow

1. **Establish the discount rate**
   - Compute WACC from current capital structure, adjusting for project-specific risk if the investment's risk profile differs materially from the firm's overall portfolio
   - If divisional hurdle rates apply, confirm the appropriate segment rate and any board-mandated spread
   - Document whether the rate is nominal or real and ensure cash flow projections match

2. **Build the free cash flow projection**
   - Lay out year-by-year unlevered free cash flows: EBITDA − taxes on EBIT + depreciation tax shield − CapEx − ΔNet Working Capital
   - Include any phased investment (multi-year build-out) and ramp-up curves for revenue
   - Model terminal value using either perpetuity growth (Gordon Growth) or exit multiple, stating which and why

3. **Compute primary metrics**
   - **NPV**: Discount all FCFs at the hurdle rate; positive NPV = value-creating
   - **IRR**: Solve for the rate that zeroes the NPV; flag non-conventional cash flow streams where multiple IRRs may exist
   - **Payback period**: Simple (undiscounted) and discounted payback; note corporate policy threshold if one exists
   - **Profitability Index (PI)**: NPV ÷ initial investment; useful when capital is rationed across multiple projects

4. **Run sensitivity and scenario analysis**
   - One-variable sensitivity: toggle revenue growth, operating margin, discount rate, and CapEx ±10–20% to identify the highest-impact driver
   - Scenario matrix: define base / bull / bear cases with coherent assumption sets (not just single-variable swings)
   - Optional: Monte Carlo simulation with probability distributions on 3–5 key inputs; report P10 / P50 / P90 NPV outcomes

5. **Rank and recommend**
   - If comparing projects, present a ranking table by NPV, IRR, PI, and payback
   - Highlight conflicts (e.g., IRR ranking differs from NPV ranking due to project scale differences) and explain which metric should govern
   - State whether the project(s) clear the hurdle rate and by what margin

## Output

The deliverable is a structured capital budgeting model containing:

- **Assumptions table**: Every input clearly listed with source, date, and [VERIFY] flags where data needs confirmation
- **FCF schedule**: Year-by-year projection with line-item detail
- **Metrics summary**: NPV, IRR, payback (simple and discounted), PI — each with a brief interpretation
- **Sensitivity dashboard**: Tornado chart or table showing NPV sensitivity to each key variable
- **Scenario summary**: Base / bull / bear NPV and IRR with narrative on what drives each case
- **Recommendation**: Clear accept/reject/defer conclusion tied to the firm's hurdle rate policy and capital constraints

## Quality Checks

- NPV at the IRR equals zero (mechanical cross-check)
- Cash flows are internally consistent: depreciation ties to CapEx schedule, tax shield ties to depreciation, working capital release nets to zero over project life
- Discount rate is applied consistently (nominal-to-nominal or real-to-real; no mixing)
- Terminal value does not exceed 60–70% of total project NPV without explicit justification — if it does, flag concentration risk
- All tax rates, depreciation lives, and regulatory incentives carry [VERIFY] tags referencing the applicable jurisdiction
- Sensitivity ranges are realistic (not artificially narrow to make the project look safe)
- If IRR is used as the primary decision metric for mutually exclusive projects, confirm that the reinvestment rate assumption is appropriate; prefer NPV when projects differ in scale or timing
