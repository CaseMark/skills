---
name: modeling-contingent-consideration
language: en
description: Structures earnout and contingent payment mechanisms with milestone definitions, measurement periods, and payout scenarios. Use when modeling earnouts, designing milestone-based payments, or valuing contingent consideration.
tags:
  - modeling
  - mergers-and-acquisitions
metadata:
  author: casemark
  practice_areas:
    - M&A Advisory
    - Corporate Development
    - Investment Banking
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Contingent Consideration

## When To Use

- Structuring earnout provisions in M&A purchase agreements where a portion of deal consideration is contingent on post-closing performance
- Valuing contingent consideration for ASC 805 fair value measurement at acquisition date and subsequent remeasurement periods
- Designing milestone-based payment schedules tied to revenue, EBITDA, product development, or regulatory approvals
- Evaluating earnout proposals from a buyer or seller perspective during deal negotiations
- Modeling payout scenarios for board presentations, fairness opinions, or deal committee materials

## Inputs To Gather

- **Deal parameters**: Total enterprise value, upfront cash/stock consideration, maximum earnout amount, earnout term (typically 1–3 years)
- **Milestone definitions**: Specific metrics (revenue, EBITDA, gross profit, unit sales, regulatory milestones), threshold vs. tiered structures, and whether milestones are cumulative or period-specific
- **Target financials**: Historical P&L (3+ years), management projections, and base-case budget for the earnout period
- **Measurement mechanics**: Accounting standard for metric calculation (GAAP vs. adjusted), permitted/excluded items, working capital treatment, and whether the business operates as standalone or integrated
- **Payment terms**: Timing of measurement and payment (quarterly, annual, end-of-term), caps and floors, acceleration triggers (e.g., change of control), and catch-up provisions
- **Discount rate inputs**: Risk-free rate, counterparty credit risk, metric-specific volatility, and comparable transaction earnout data
- **Dispute resolution**: Mechanism for disagreements on metric calculations (independent accountant, arbitration) — note for structural modeling, not valuation

## Workflow

1. **Classify the earnout type**
   - Financial metric-based (revenue, EBITDA, gross margin) vs. non-financial milestone-based (FDA approval, patent grant, customer retention)
   - Single-period vs. multi-period measurement; binary payout vs. linear/tiered interpolation
   - Determine if the earnout is compensatory (ASC 805-10-55-25 indicators) vs. part of purchase price [VERIFY against specific deal facts]

2. **Build the base-case scenario model**
   - Project the relevant metric across each measurement period using management forecasts as the starting point
   - Map metric outcomes to payout amounts using the earnout formula (threshold, cap, interpolation method)
   - Calculate present value of expected payouts using a risk-adjusted discount rate

3. **Construct scenario/probability framework**
   - Define 3–5 discrete scenarios (e.g., downside, below-plan, base, upside, stretch) with probability weights
   - For financial metrics: use Monte Carlo simulation or scenario-probability-weighted approach; calibrate volatility to comparable company revenue/EBITDA variability
   - For non-financial milestones: assign probability of achievement based on comparable precedents, pipeline stage, or expert input
   - Probability weights must sum to 100%; document the basis for each weight

4. **Apply valuation methodology**
   - **Scenario-based method (SBM)**: Probability-weight each scenario's payout, discount to present value; appropriate for linear or simple structures
   - **Option pricing method (OPM)**: Use for earnouts with caps, floors, or non-linear payoff profiles; model as a call spread or digital option on the underlying metric
   - **Monte Carlo simulation**: Required for path-dependent earnouts, correlated metrics, or complex tiered structures
   - Select discount rate: risk-free rate + credit spread for financial-metric earnouts; higher risk premium for non-financial milestones [VERIFY discount rate methodology with valuation team]

5. **Run sensitivity analysis**
   - Vary key assumptions: metric growth rate (±5–15%), probability weights (shift ±10%), discount rate (±100–200 bps), and volatility (±5–10%)
   - Produce a sensitivity table showing earnout fair value across a matrix of two key variables
   - Identify breakeven points: at what metric level does the earnout begin paying, hit the cap, or cross a tier

6. **Model structural protections and edge cases**
   - Acceleration on change of control or breach of operating covenants
   - Catch-up provisions if early periods miss but later periods exceed targets
   - Anti-sandbagging: model impact of buyer actions that could suppress metric (e.g., overhead allocation, revenue diversion, customer reassignment)
   - Pro-ration for partial-period measurements

## Output

- **Earnout summary table**: Metric thresholds, tiers, caps/floors, measurement periods, and maximum contingent consideration
- **Scenario waterfall**: Each scenario with metric projection, resulting payout, probability weight, weighted payout, and PV of weighted payout
- **Fair value summary**: Point estimate of contingent consideration fair value with range (e.g., 25th–75th percentile from simulation)
- **Sensitivity matrix**: Two-variable sensitivity table (e.g., revenue growth vs. discount rate) showing fair value at each intersection
- **Payout profile chart**: Visual showing payout amount as a function of the underlying metric, highlighting thresholds, linear interpolation zones, and caps
- **Key assumptions register**: Numbered list of every material assumption with source, rationale, and [VERIFY] flags where judgment-dependent

## Quality Checks

- Confirm earnout payout formula exactly matches the draft purchase agreement language — any ambiguity in "adjusted EBITDA" definitions, excluded items, or rounding conventions must be flagged
- Verify probability weights reflect current market conditions and target-specific risk, not generic assumptions
- Check that the discount rate is consistent with the risk profile of the metric (revenue earnouts carry less discount than EBITDA earnouts due to lower volatility)
- Ensure the model handles edge cases: zero payout scenario, maximum payout scenario, partial-period proration, and mid-term change of control
- Validate that fair value output is reasonable relative to maximum earnout amount (typical range: 30–70% of max for financial earnouts)
- Cross-check simulation outputs against closed-form solutions where possible to confirm model integrity
- Confirm ASC 805 classification: contingent consideration classified as liability requires remeasurement at each reporting date; equity classification does not [VERIFY classification with accounting advisors]
