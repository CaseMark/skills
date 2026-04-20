---
name: modeling-scenario-based-valuations
language: en
description: Builds probability-weighted valuation models with multiple exit scenarios, timing assumptions, and risk-adjusted returns. Use when building growth equity valuations, modeling scenario-weighted outcomes, or analyzing risk-adjusted returns.
tags:
  - modeling
  - growth-equity
  - risk
  - valuation
metadata:
  author: casemark
  practice_areas:
    - Growth Equity
    - Expansion Capital
    - Late-Stage Investing
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Scenario Based Valuations

Builds probability-weighted valuation models with multiple exit scenarios, timing assumptions, and risk-adjusted returns for growth equity and late-stage investments.

## When To Use

- Evaluating a growth equity or expansion capital investment where the outcome range is wide (e.g., IPO vs. secondary sale vs. down-round recap)
- Stress-testing an existing valuation under different macro, operational, or exit-timing assumptions
- Building an investment committee memo that requires a probability-weighted expected value and IRR/MOIC sensitivity
- Comparing risk-adjusted returns across multiple deal opportunities in a portfolio context
- Modeling management-case vs. investor-case divergence to frame negotiation anchors on entry price

## Inputs To Gather

- **Company financials**: Last 3 years of revenue, EBITDA/operating income, gross margin, and net revenue retention (for SaaS/recurring models). Trailing-twelve-month run-rate if available.
- **Growth plan**: Management projections or consensus forecasts for revenue and margin trajectory over the hold period (typically 3–7 years).
- **Comparable multiples**: Current and historical EV/Revenue, EV/EBITDA, or P/E multiples for public comps and recent transactions in the sector. [VERIFY] sector-specific multiple ranges against current market conditions.
- **Capital structure**: Existing equity ownership, option pool, outstanding convertible instruments, liquidation preferences, and any participating preferred terms that affect waterfall distributions.
- **Exit assumptions**: Realistic exit channels (IPO, strategic M&A, sponsor-to-sponsor, secondary, recap/dividend) with indicative timing windows and probability weights.
- **Discount rate / hurdle**: Fund-level target return (e.g., 20–30% gross IRR for growth equity) and any LP-driven constraints on hold period or concentration.

## Workflow

### 1. Define Scenarios

Construct at minimum three discrete scenarios — each must differ on at least two independent variables:

| Scenario | Typical Drivers | Example Weight |
|----------|----------------|----------------|
| **Bull** | Accelerated growth, multiple expansion, early exit | 20–30% |
| **Base** | Plan-case growth, stable multiples, mid-horizon exit | 40–50% |
| **Bear** | Growth deceleration, multiple compression, delayed or distressed exit | 20–30% |

Optionally add a **Downside/Wipeout** scenario (5–10%) for capital-loss cases (e.g., liquidation preference recovery only). Probability weights must sum to 100%.

### 2. Build Per-Scenario Cash Flows

For each scenario:
- Project revenue, EBITDA, and free cash flow through the exit year
- Apply the relevant exit multiple to the terminal metric (Revenue or EBITDA) to derive enterprise value at exit
- Run the equity waterfall: subtract net debt, apply liquidation preferences and participation caps, distribute remaining proceeds to common/preferred holders
- Calculate gross proceeds to the fund's position, then compute **MOIC** and **IRR** for that scenario
- If interim cash flows exist (dividends, recaps), include them in IRR computation

### 3. Compute Probability-Weighted Returns

- Weighted MOIC = Σ (scenario probability × scenario MOIC)
- Weighted IRR: solve for the discount rate that equates the probability-weighted cash flow stream to zero NPV (do not simply average IRRs — this is mathematically incorrect)
- Report both the weighted expected return and the full range (min IRR to max IRR)

### 4. Run Sensitivity Analysis

Build two-way sensitivity tables on the most impactful variable pairs:
- **Entry multiple vs. exit multiple** (shows valuation discipline impact)
- **Revenue growth rate vs. exit timing** (shows execution risk)
- **Probability weight shifts** (e.g., shift 10% from Bull to Bear — how does weighted MOIC move?)

Highlight the break-even entry price at which the weighted IRR hits the fund's hurdle rate.

### 5. Validate and Stress-Test

- Cross-check implied exit valuations against public comp ceilings — flag any scenario where the implied exit is above the 75th percentile of comps [VERIFY]
- Confirm that the Bear case is genuinely adverse, not just "slightly below plan"
- Test for liquidation preference drag: in the Bear case, does the preferred structure consume most of the equity value?
- Verify IRR math by independently discounting cash flows at the computed rate

## Output

The deliverable should include:

- **Scenario summary table**: Each scenario with key assumptions (growth rate, exit multiple, exit year, probability weight) and resulting MOIC / IRR
- **Probability-weighted return**: Single expected MOIC and IRR with range band
- **Sensitivity tables**: At least two two-way tables with conditional formatting highlighting cells above/below hurdle
- **Waterfall exhibit**: Showing how exit proceeds distribute across the cap table under each scenario
- **Key assumptions register**: Every input assumption listed with its source (management, investor estimate, market data) and confidence level
- **Narrative summary**: 1–2 paragraphs interpreting the results, calling out the primary risk factors and the entry price sensitivity

## Quality Checks

- Probability weights sum to exactly 100%
- IRR is solved iteratively (not averaged across scenarios)
- Exit multiples are benchmarked to current comps, not aspirational peak multiples [VERIFY]
- Bear case models genuine downside — not just a 10% haircut on the base case
- Liquidation preferences and participation correctly modeled in the waterfall for every scenario
- All assumptions sourced and labeled; unsourced assumptions marked [VERIFY]
- Terminal values do not imply growth rates above the nominal GDP growth rate in perpetuity
- Model ties out: entry equity check size × MOIC = gross proceeds in each scenario
