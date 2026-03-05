---
name: structuring-structured-equity-instruments
description: Designs structured equity with participating preferred, PIK dividends, conversion mechanics, and downside protection features. Use when structuring growth equity instruments, designing preference terms, or modeling structured returns.
tags:
  - growth-equity
metadata:
  author: casemark
  practice_areas:
    - Growth Equity
    - Expansion Capital
    - Late-Stage Investing
  document_types:
    - Report
  skill_modes:
    - Analysis
---
# Structuring Structured Equity Instruments

Designs structured equity instruments combining preferred equity features — participating preferred, PIK dividends, conversion mechanics, and downside protection — tailored to growth equity and late-stage investment contexts.

## When To Use

- Structuring a growth equity or expansion capital investment where straight common or simple preferred is insufficient
- Designing preference stacks with participating vs. non-participating features and cap structures
- Modeling PIK dividend accrual and its impact on effective ownership and exit returns
- Evaluating conversion mechanics (mandatory, optional, automatic) and their triggers
- Building downside protection via liquidation preferences, ratchets, or guaranteed minimum returns
- Comparing structured equity alternatives against convertible notes, SAFEs, or mezzanine debt

## Inputs To Gather

- **Deal parameters**: Investment amount, pre-money valuation, target ownership percentage, expected hold period
- **Company financials**: Current revenue, EBITDA, growth trajectory, existing cap table and prior preference stacks
- **Return targets**: Investor IRR/MOIC hurdles, fund mandate constraints (e.g., minimum 2.0x gross MOIC)
- **Governance requirements**: Board seats, consent rights, information rights, protective provisions sought
- **Exit assumptions**: Expected exit timing, likely exit modality (M&A, IPO, secondary), valuation range at exit
- **Existing instruments**: Any outstanding preferred series, convertible notes, warrants, or option pools that interact with the new instrument

## Workflow

1. **Define return profile and risk allocation**
   - Establish investor IRR/MOIC targets and acceptable downside scenarios
   - Identify which risks the structured instrument must address (valuation risk, dilution risk, timing risk, downside loss)
   - Determine whether the structure should optimize for downside protection, upside participation, or both

2. **Select core structural components**
   - **Liquidation preference**: Choose 1x non-participating, 1x participating (with or without cap), or multiple preference [VERIFY: check market norms for the specific deal stage and sector]
   - **Dividend mechanism**: Decide between cash-pay, PIK accrual, or cumulative/non-cumulative preferred dividend; set coupon rate (typically 6-12% for growth equity PIK)
   - **Conversion rights**: Define optional conversion ratio, automatic conversion triggers (e.g., IPO above a threshold valuation), and anti-dilution adjustment method (broad-based weighted average vs. full ratchet)
   - **Downside protection**: Structure minimum return guarantees, liquidation preference multiples, or ratchet mechanisms tied to performance milestones

3. **Model economic outcomes across scenarios**
   - Build a waterfall model showing distributions at 3-5 exit valuations (e.g., 0.5x, 1.0x, 2.0x, 3.0x, 5.0x entry valuation)
   - Calculate effective ownership and returns under both the as-converted and as-preferred paths at each scenario
   - Model PIK accrual over the hold period and its compounding effect on the preference stack
   - Identify the crossover point where conversion becomes economically rational versus holding preferred
   - Stress-test for dilution from future rounds, option pool expansion, and anti-dilution triggers

4. **Evaluate interaction with existing cap table**
   - Map pari passu vs. senior/junior ranking relative to existing preferred series
   - Assess pay-to-play provisions, drag-along/tag-along rights, and their interaction with the new instrument
   - Confirm that the aggregate preference stack does not create a scenario where common holders (including management) receive insufficient exit proceeds to maintain incentive alignment

5. **Draft term summary and sensitivity analysis**
   - Produce a structured term sheet summary of all economic and governance terms
   - Include a sensitivity table showing investor MOIC/IRR across exit valuation and timing permutations
   - Flag areas where terms deviate from market standards or where founder pushback is likely

## Output

Deliver a structured equity instrument report containing:

- **Executive summary**: Investment thesis, instrument type selected, and headline economics (entry valuation, ownership, target returns)
- **Term structure table**: Liquidation preference, dividend rate/type, conversion mechanics, anti-dilution provisions, participation features with caps if applicable
- **Waterfall analysis**: Distribution waterfall at multiple exit valuations showing proceeds to each stakeholder class
- **Scenario matrix**: MOIC and IRR sensitivity across exit valuation (rows) and hold period (columns)
- **Crossover analysis**: Identification of the valuation at which conversion becomes optimal relative to holding preferred
- **Cap table impact**: Pro forma cap table showing pre- and post-investment ownership on both as-issued and as-converted bases
- **Key risk factors**: Identified structural risks (e.g., preference stack overhang, misaligned incentives, anti-dilution triggers)
- **Recommended terms**: Final recommended structure with rationale for each component choice

## Quality Checks

- Waterfall distributions sum to 100% of exit proceeds at every modeled scenario
- PIK accrual calculations use correct compounding (typically quarterly or semi-annual) and match stated coupon rate
- Conversion ratios and anti-dilution adjustments are mathematically consistent with stated formulas
- Participation cap, if any, is applied correctly — investor receives the lesser of (participation proceeds) and (cap amount) before converting
- As-converted ownership percentages reconcile to the cap table and reflect all dilutive instruments (options, warrants, convertibles)
- All jurisdiction-dependent terms (e.g., corporate law governing preferred stock rights, tax treatment of PIK dividends) are marked with [VERIFY]
- Scenario analysis covers both base case and stress cases, including a down-round and a flat exit
- Terms are benchmarked against current market norms for comparable deal stage and sector [VERIFY: market data recency]
