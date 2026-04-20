---
name: modeling-venture-fund-economics
language: en
description: Builds LP-level fund models with management fees, carried interest, clawback provisions, and waterfall distributions. Use when modeling fund economics, projecting LP returns, or analyzing fund terms.
tags:
  - modeling
  - venture-capital
metadata:
  author: casemark
  practice_areas:
    - Venture Capital
    - Seed/Series Investing
    - Startup Ecosystems
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Venture Fund Economics

Builds LP-level fund models projecting LP net returns through management fees, carried interest waterfalls, clawback mechanics, and portfolio-level cash flow timing.

## When To Use

- Modeling projected net returns for a new fund's LPA terms during fundraising
- Comparing GP economics across different fee/carry structures (e.g., 2/20 vs. 1.5/25 with a hurdle)
- Projecting LP cash flows (capital calls and distributions) over fund life
- Analyzing clawback exposure under various portfolio outcome scenarios
- Evaluating impact of fund-level vs. deal-by-deal carry on GP and LP economics
- Stress-testing fund returns under different deployment paces, hold periods, and exit multiples

## Inputs To Gather

- **Fund terms**: Fund size, GP commitment percentage, management fee rate and basis (committed vs. invested capital), fee step-down schedule, fund term and extension provisions
- **Carry structure**: Carried interest percentage, preferred return (hurdle rate), catch-up provision (full vs. partial), European vs. American waterfall [VERIFY: confirm LPA waterfall type]
- **Deployment assumptions**: Number of investments, average check size, deployment pace (years 1–4 typical), reserve ratio for follow-ons
- **Portfolio outcome assumptions**: Target gross MOIC range, distribution of outcomes (power-law vs. uniform), expected hold periods per investment, exit timing distribution
- **Recycling provisions**: Whether and to what extent realized proceeds can be redeployed before triggering distributions [VERIFY: check LPA recycling terms]
- **Fund expenses**: Organizational expenses cap, operating expenses, broken-deal costs

## Workflow

1. **Map the fee schedule** — Calculate annual management fees over the full fund life. Model the fee basis shift (committed capital during investment period → invested capital or NAV post-investment period). Apply any fee offsets from portfolio company monitoring/transaction fees. Compute total fee load as a percentage of committed capital.

2. **Build the deployment schedule** — Lay out capital calls by quarter or year across the investment period. Allocate between new investments and follow-on reserves. Track invested capital, unfunded commitments, and recycled capital at each period.

3. **Model portfolio outcomes** — Assign gross return multiples and exit timing to each investment (or investment cohort). For early-stage VC, apply a power-law distribution: ~50–65% write-offs/minimal returns, ~20–30% moderate (1–3x), ~5–10% outsized (5x+). Calculate gross proceeds per exit event.

4. **Run the waterfall** — Apply the distribution waterfall per LPA terms:
   - **Return of contributed capital** — LPs receive back their drawn capital (including fees and expenses, or net of fees, depending on LPA)
   - **Preferred return** — If applicable, compound the hurdle (typically 8% IRR) on LP contributions net of prior distributions
   - **GP catch-up** — If full catch-up, 100% to GP until carry split is achieved on cumulative profits; if partial (e.g., 50/50), split accordingly
   - **Carried interest split** — Remaining profits split per LPA (typically 80/20 LP/GP)
   - For American-style (deal-by-deal) waterfalls, run the waterfall per realization and track interim carry vs. escrow/holdback

5. **Calculate clawback exposure** — Model scenarios where early profitable exits generate carry, but later write-offs reduce aggregate fund returns below the hurdle. Quantify the GP's clawback obligation. Note whether the clawback is net-of-tax [VERIFY: confirm clawback tax gross-up provisions in LPA].

6. **Compute LP net metrics** — Calculate net MOIC, net IRR (using actual cash flow timing), DPI (distributions to paid-in), RVPI (residual value to paid-in), and TVPI at key intervals (end of investment period, year 7, year 10, final liquidation).

7. **Run sensitivity analysis** — Vary key assumptions across a matrix:
   - Gross MOIC: 1.5x / 2.0x / 2.5x / 3.0x
   - Deployment pace: 2-year vs. 4-year full deployment
   - Hold period: 4-year vs. 7-year average
   - Fee structure variations
   - Show net IRR and net MOIC under each scenario combination

## Output

- **Fee analysis table**: Annual management fees, cumulative fee load, fee drag on returns
- **Cash flow schedule**: Period-by-period capital calls and distributions for both LP and GP
- **Waterfall calculation**: Step-by-step distribution waterfall showing preferred return accrual, catch-up, and carry split
- **Return summary**: Net IRR, net MOIC, DPI, RVPI, TVPI at multiple time horizons
- **Sensitivity matrix**: Net returns across key variable ranges
- **GP economics summary**: Total management fees, total carried interest, GP net revenue under base and stress cases
- **Clawback analysis**: Scenarios triggering clawback, estimated GP obligation amounts

## Quality Checks

- Confirm that total LP distributions + remaining NAV + total fees + carry = total gross portfolio proceeds (cash-on-cash reconciliation)
- Verify the waterfall math: LP preferred return is fully satisfied before any carry flows to GP (European), or escrow/holdback is adequate (American)
- Check that net IRR calculation uses actual cash flow dates, not simplified annual periods
- Validate that management fee basis correctly shifts from committed to invested capital at the right trigger point
- Ensure GP commitment is included in LP-side economics only if GP co-invests alongside LPs (not fee-waiver-based)
- Confirm recycling does not exceed LPA-permitted limits [VERIFY: recycling cap percentage]
- Cross-check that power-law portfolio assumptions produce a reasonable gross MOIC (typically 2.0–3.5x for early-stage VC funds)
- Verify clawback calculation accounts for tax distributions and any net-of-tax provisions
