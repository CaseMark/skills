---
name: modeling-carried-interest-mechanics
language: en
description: Builds carry waterfall models with preferred return hurdles, catch-up provisions, and clawback mechanics across deal-by-deal and whole-fund structures. Use when modeling carry economics, comparing waterfall structures, or analyzing GP incentive alignment.
tags:
  - modeling
  - fund-formation-and-structuring
metadata:
  author: casemark
  practice_areas:
    - Fund Formation
    - Fund Structuring
    - Partnership Law
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Carried Interest Mechanics

Builds carry waterfall models with preferred return hurdles, catch-up provisions, and clawback mechanics across deal-by-deal and whole-fund structures.

## When To Use

- Modeling GP carry economics during fund formation or LPA negotiation
- Comparing European (whole-fund) vs. American (deal-by-deal) waterfall structures
- Analyzing the impact of preferred return hurdles, catch-up splits, and tiered carry rates
- Stress-testing clawback exposure under different portfolio performance scenarios
- Evaluating GP/LP alignment across varying fund return profiles
- Preparing carry allocation exhibits for side letter or advisory committee discussions

## Inputs To Gather

- **Fund terms**: committed capital, GP commitment percentage, management fee rate and offset mechanics
- **Waterfall structure**: European (whole-fund) or American (deal-by-deal), or hybrid
- **Preferred return**: hurdle rate (typically 7–9% IRR), compounding method (simple, compound, or continuous), and whether it is cumulative [VERIFY against LPA]
- **Catch-up provision**: GP catch-up percentage (commonly 100% or 80/20), and whether catch-up is full or partial
- **Carry split tiers**: standard 80/20, any tiered escalation thresholds (e.g., 80/20 below 2x MOIC, 70/30 above)
- **Clawback terms**: interim clawback triggers, true-up frequency, escrow/holdback percentage (typically 20–50% of carry), and any tax-distribution gross-up [VERIFY]
- **Deal-level assumptions** (for deal-by-deal): projected entry/exit values, hold periods, and recycling provisions
- **Fee offsets**: whether management fees reduce contributed capital for waterfall purposes

## Workflow

1. **Confirm waterfall type and key terms**
   - Identify European vs. American vs. hybrid structure from LPA or term sheet
   - Map each tier: return of capital → preferred return → GP catch-up → carried interest split
   - Note any netting or aggregation provisions for deal-by-deal structures

2. **Build the capital account framework**
   - Track LP and GP contributed capital, cumulative distributions, and unrealized value per period
   - For whole-fund: aggregate all investments into a single waterfall calculation
   - For deal-by-deal: model each investment's waterfall independently, then aggregate for clawback analysis

3. **Model the preferred return hurdle**
   - Apply the stated hurdle rate to LP contributed capital (net of any fee offsets)
   - Calculate accrued preferred return per period using the specified compounding convention
   - Determine the cumulative preferred return shortfall or surplus at each distribution event

4. **Apply catch-up and carry tiers**
   - Once LP preferred return is satisfied, allocate distributions to GP catch-up until the GP has received its pro-rata carry share of all profits to that point
   - After catch-up is complete, split remaining distributions per the stated carry ratio (e.g., 80/20)
   - For tiered structures, apply escalating carry percentages at each MOIC or IRR threshold

5. **Model clawback and escrow mechanics**
   - Calculate the GP's cumulative carry received vs. the carry the GP would be entitled to if the fund were liquidated at current values
   - Identify interim clawback triggers (if any) and end-of-fund clawback obligations
   - Model the escrow reserve—carry withheld from GP distributions and released upon fund wind-down or true-up
   - Account for tax-distribution gross-up provisions that reduce the effective clawback amount [VERIFY against LPA]

6. **Run scenario and sensitivity analysis**
   - Vary portfolio returns (e.g., 0.5x–3.0x gross MOIC) to map carry across outcomes
   - Test the impact of loss investments on deal-by-deal carry vs. whole-fund carry
   - Stress-test clawback exposure: model a scenario where early exits are profitable but later exits are at loss
   - Compare GP economics across structures (side-by-side European vs. American output)

7. **Produce final model and documentation**
   - Generate a waterfall schedule showing distributions at each tier per period
   - Summarize GP carry, LP net returns, and clawback exposure at each scenario level
   - Document all assumptions, including hurdle compounding method, fee treatment, and recycling rules

## Output

- **Waterfall distribution schedule**: period-by-period allocation across return of capital, preferred return, catch-up, and carry tiers
- **GP carry summary**: total carry earned, carry as percentage of profits, effective carry rate across return scenarios
- **Clawback analysis**: maximum clawback exposure, escrow adequacy, and net-of-tax clawback obligation
- **Scenario matrix**: GP carry and LP net multiples/IRRs across a range of gross fund returns (table or chart)
- **Structure comparison** (if applicable): side-by-side economics of European vs. American waterfall under identical assumptions

## Quality Checks

- Verify that LP preferred return is fully satisfied before any carry is allocated—no leakage into catch-up prematurely
- Confirm catch-up math: after catch-up, GP's cumulative share of total profits should equal the stated carry percentage
- Ensure clawback calculation nets to zero at fund wind-down—GP's total carry equals the stated percentage of total fund profits above the hurdle
- Cross-check: under a whole-fund model with uniform returns, deal-by-deal and whole-fund carry should converge
- Validate that GP commitment is treated correctly (carried alongside or excluded from carry base) [VERIFY against LPA]
- Confirm management fee offset treatment matches LPA terms—100% offset, 80% offset, or no offset
- Flag any interim distribution assumptions that could trigger premature clawback obligations
