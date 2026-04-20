---
name: analyzing-premium-pricing
language: en
description: Structures actuarial pricing analysis with loss cost estimation, expense loading, and rate adequacy testing. Use when analyzing premium rates, calculating rate indications, or assessing pricing adequacy.
tags:
  - analysis
  - insurance
metadata:
  author: casemark
  practice_areas:
    - Insurance
    - Actuarial Science
    - Reinsurance
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Premium Pricing

Structures actuarial pricing analysis with loss cost estimation, expense loading, and rate adequacy testing.

## When To Use

- Evaluating whether current premium rates are adequate for a book of business or product line
- Calculating rate indications for rate filing support or internal pricing reviews
- Comparing indicated vs. charged rates to measure pricing shortfall or excess
- Reviewing reinsurance pricing layers, ceding commissions, or treaty terms
- Assessing the impact of loss trend, development, or mix changes on required premium

## Inputs To Gather

- **Loss data**: Accident-year or policy-year incurred losses (paid + case reserves), ideally 5–10 years; confirm whether IBNR is included or must be estimated
- **Earned premium**: On-level earned premium by year; identify any rate changes applied historically so premiums can be trended to current level
- **Expense data**: Fixed and variable expense ratios — commissions, general & administrative, taxes/licenses/fees, LAE (allocated and unallocated)
- **Loss development factors (LDFs)**: Triangle or selected cumulative development factors by maturity; note whether from internal data or industry benchmarks [VERIFY source]
- **Trend assumptions**: Loss cost trend (severity and frequency separately if available) and premium trend; specify trend period and basis
- **Target profit & contingency**: Required underwriting profit margin or combined ratio target; any catastrophe or contingency load
- **Line of business / coverage details**: Confirm coverage type, territory, policy limits, deductibles, and any sub-segments to be analyzed separately

## Workflow

1. **On-level premium** — Restate historical earned premiums to current rate level using cumulative rate change factors. Verify each rate change effective date and confirm whether changes were applied uniformly or varied by sub-segment.

2. **Develop losses to ultimate** — Apply selected loss development factors to each accident year. If using a blend of methods (paid vs. incurred, chain-ladder vs. Bornhuetter-Ferguson), document selections and rationale. Flag any years with large losses or abnormal development patterns.

3. **Trend losses to prospective period** — Apply annual frequency and severity trend factors to bring ultimate losses from historical midpoint to the future policy period midpoint. State the trend period explicitly (e.g., from AY 2022 midpoint to prospective period midpoint of 7/1/2027). [VERIFY trend selections against industry studies or internal actuarial memoranda]

4. **Calculate pure loss cost indication** — Divide trended ultimate losses by on-level earned premium for each year to produce loss ratios. Select an all-year weighted or ex-cat weighted average, excluding or capping anomalous years with stated justification.

5. **Apply expense and profit loading** — Build up the permissible loss ratio:
   - Fixed expense ratio (general & administrative per premium dollar)
   - Variable expense ratio (commissions, premium taxes, assessments)
   - Profit and contingency provision
   - Permissible loss ratio = 1.0 − (variable expense ratio + fixed expense ratio + profit load)

6. **Derive rate indication** — Indicated rate change = (selected loss ratio ÷ permissible loss ratio) − 1.0. Express as a percentage change. Break out the indication by major drivers (loss trend, development, expense changes, profit target adjustment).

7. **Assess rate adequacy** — Compare indicated premium to current charged premium. Identify segments where adequacy diverges materially. If reinsurance pricing is in scope, evaluate the adequacy of ceding commissions relative to underlying expense loads and loss experience.

8. **Sensitivity testing** — Test key assumptions:
   - ±1–2 points on loss trend
   - Alternative LDF selections (higher/lower tail factors)
   - Inclusion vs. exclusion of catastrophe or shock losses
   - Document the range of indicated rate changes under each scenario

## Output

- **Rate indication summary table**: By accident year — on-level earned premium, ultimate losses, trended ultimate losses, loss ratios, selected loss ratio, permissible loss ratio, indicated rate change
- **Expense breakdown**: Variable, fixed, profit/contingency components with sources
- **Assumption schedule**: LDF selections, trend factors, large-loss treatment, years included/excluded
- **Sensitivity analysis**: Range of indications under alternative assumptions
- **Key findings narrative**: Plain-language summary of whether rates are adequate, the magnitude and direction of any needed adjustment, and primary drivers

## Quality Checks

- Confirm on-leveling factors chain correctly and match documented rate change history
- Verify loss development factors produce reasonable ultimates — compare implied IBNR to prior analyses
- Check that trend period aligns with the prospective effective date, not the filing date
- Ensure the permissible loss ratio components sum correctly (variable + fixed + profit ≤ 1.0)
- Validate that the indicated change formula is applied consistently (indicated LR ÷ permissible LR − 1)
- Flag any selected loss ratio that deviates more than 3 points from the all-year average without explanation
- Mark jurisdiction-specific regulatory constraints on maximum rate changes or minimum loss ratio standards with [VERIFY]
- Confirm large-loss or catastrophe treatment is consistent with the company's filed methodology [VERIFY]
