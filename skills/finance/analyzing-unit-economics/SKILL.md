---
name: analyzing-unit-economics
description: Structures unit economic analysis with CAC, LTV, payback period, and cohort-based measurement. Use when analyzing unit economics, calculating LTV/CAC, or evaluating customer economics.
tags:
  - analysis
  - financial-planning-and-analysis
metadata:
  author: casemark
  practice_areas:
    - FP&A
    - Management Accounting
    - Business Intelligence
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Unit Economics

Structures unit economic analysis with CAC, LTV, payback period, and cohort-based measurement for evaluating whether a business acquires and monetizes customers profitably.

## When To Use

- Evaluating customer acquisition efficiency (CAC trending, channel-level CAC)
- Calculating customer lifetime value (LTV) and LTV/CAC ratios
- Determining payback period on acquisition spend
- Comparing unit economics across customer segments, cohorts, or product lines
- Stress-testing business model sustainability for board decks, fundraising, or strategic planning
- Assessing whether to scale, hold, or cut spend on a specific acquisition channel

## Inputs To Gather

- **Revenue data**: MRR/ARR per customer or ARPU by period; gross margin percentage or contribution margin per unit
- **Acquisition cost data**: Total sales & marketing spend by channel; number of new customers acquired per period; breakdown of paid vs. organic vs. referral acquisition
- **Retention/churn data**: Logo churn rate and revenue churn rate by cohort; expansion revenue (upsell/cross-sell) rates if applicable
- **Cohort definitions**: Time-based cohorts (monthly/quarterly sign-up date), segment-based cohorts (plan tier, geography, company size)
- **Time horizon**: Analysis window length and whether to use historical actuals, forward projections, or both
- **Discount rate** (if computing discounted LTV): Weighted average cost of capital or hurdle rate [VERIFY — confirm with finance team which rate applies]

## Workflow

1. **Define the unit**: Clarify what constitutes a "unit" — individual customer, account, seat, contract, or transaction. This choice drives every downstream calculation.
2. **Calculate CAC**:
   - Fully loaded CAC = (Sales & marketing spend + attributed overhead) / New customers acquired
   - Segment by channel (paid search, outbound sales, partnerships, organic) where data permits
   - Flag whether CAC includes or excludes sales team base salaries — state the convention explicitly
3. **Calculate LTV**:
   - Simple LTV = ARPU × Gross Margin % × (1 / Churn Rate)
   - Cohort-based LTV: Track actual cumulative gross profit per cohort over time; fit a retention curve (exponential decay, shifted beta-geometric, or log-linear) to project remaining life
   - If expansion revenue is material, compute net revenue retention (NRR) and use it in place of simple churn: LTV = ARPU × Gross Margin % × (1 / (1 − NRR))
   - For discounted LTV, apply the agreed discount rate period-by-period [VERIFY]
4. **Compute core ratios**:
   - **LTV/CAC ratio**: Target benchmark is ≥ 3× for SaaS; adjust expectations by industry [VERIFY — benchmark varies by business model]
   - **CAC payback period**: Months to recover CAC = CAC / (ARPU × Gross Margin %). For non-subscription models, use average order frequency × contribution margin per order
   - **Contribution margin per unit**: Revenue per unit minus all variable costs directly attributable to serving that unit
5. **Cohort analysis**:
   - Build a cohort retention table (rows = cohort, columns = period since acquisition)
   - Plot retention curves and identify whether newer cohorts retain better or worse than older ones
   - Calculate cumulative revenue and cumulative gross profit per cohort to see when each cohort "pays back"
6. **Sensitivity and scenario testing**:
   - Vary churn rate ±20% and show impact on LTV and LTV/CAC
   - Model the effect of a CAC increase (e.g., rising CPMs) on payback period
   - Test what gross margin improvement is needed to hit target LTV/CAC if current ratio is below threshold
7. **Interpret and contextualize**:
   - Compare current metrics to prior periods and to industry benchmarks [VERIFY — source benchmarks from credible surveys or databases]
   - Identify the primary lever (reduce churn, increase ARPU, lower CAC) with the largest marginal impact
   - Note any data gaps that limit confidence (e.g., insufficient cohort maturity, blended channel costs)

## Output

Produce a structured **Unit Economics Analysis Report** containing:

- **Executive summary**: One-paragraph verdict on unit economic health with headline LTV/CAC ratio and payback period
- **Metric table**: CAC, LTV, LTV/CAC, payback period, contribution margin — shown overall and by segment/channel
- **Cohort retention chart**: Heatmap or line chart of retention by cohort
- **Cumulative gross profit curves**: Per-cohort view showing time to payback
- **Sensitivity table**: Key metrics under bull/base/bear assumptions
- **Recommendations**: Ranked list of actions (scale channel X, reduce churn via Y, raise price on segment Z) with expected metric impact
- **Assumptions & limitations log**: Every assumption stated, every data gap flagged with [VERIFY]

## Quality Checks

- Confirm CAC denominator counts only *new* customers, not reactivations, unless reactivation cost is separately tracked
- Verify that LTV uses gross margin, not revenue — overstating LTV by ignoring COGS is the most common error
- Ensure churn rate and ARPU are measured over the same time period (monthly churn with monthly ARPU, not mixing annual and monthly)
- Check that cohort data has sufficient maturity (at least 6–12 months of history) before projecting long-tail retention
- Cross-check total CAC spend × customer count against the P&L sales & marketing line to catch allocation errors
- Validate that LTV/CAC ratio is not artificially inflated by excluding below-the-line costs from CAC (e.g., onboarding, customer success)
- If using discounted LTV, confirm the discount rate is consistently applied and disclosed
