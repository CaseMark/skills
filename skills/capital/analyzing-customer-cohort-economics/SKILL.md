---
name: analyzing-customer-cohort-economics
description: Deconstructs customer cohort behavior with retention curves, LTV progression, and vintage-over-vintage comparison analysis. Use when analyzing cohort data, assessing customer quality, or modeling lifetime value trajectories.
tags:
  - analysis
  - growth-equity
metadata:
  author: casemark
  practice_areas:
    - Growth Equity
    - Expansion Capital
    - Late-Stage Investing
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Customer Cohort Economics

Deconstructs customer cohort behavior with retention curves, LTV progression, and vintage-over-vintage comparison analysis for growth equity and expansion capital due diligence.

## When To Use

- Evaluating a SaaS or subscription company's customer quality during investment diligence
- Assessing whether net revenue retention is improving, stable, or deteriorating across vintages
- Modeling payback period and LTV/CAC trajectories by acquisition cohort
- Comparing cohort behavior pre- and post-product changes, pricing shifts, or go-to-market pivots
- Stress-testing management's revenue projections against actual cohort decay curves

## Inputs To Gather

- **Cohort revenue data**: Monthly or quarterly revenue by customer sign-up cohort (minimum 8–12 cohorts with 12+ months of maturity preferred)
- **Customer count by cohort**: Number of logos acquired per period, with retention/churn counts over time
- **Revenue breakdown**: Split between new, expansion, contraction, and churned revenue per cohort per period
- **CAC data**: Fully-loaded customer acquisition cost by cohort period (sales + marketing spend / new customers)
- **Segmentation dimensions**: Customer size tier, channel, product line, geography, or industry vertical for sub-cohort cuts
- **Pricing/packaging history**: Dates and nature of any pricing changes that may create discontinuities between vintages
- [VERIFY] Confirm whether revenue data is recognized (GAAP/IFRS) or bookings/billings — this changes interpretation of retention curves

## Workflow

1. **Normalize cohort data** — Align all cohorts to a common T+0 starting point. Index each cohort's revenue to 100 at month 0 (or first full month). Confirm cohort definitions are consistent (e.g., sign-up date vs. first invoice date).

2. **Build retention curves** — Plot logo retention and net dollar retention for each cohort on a common time axis. Calculate:
   - Gross dollar retention (GDR): revenue retained excluding expansion
   - Net dollar retention (NDR): revenue retained including expansion/upsell
   - Logo retention: percentage of customers still active

3. **Calculate LTV progression** — For each cohort, compute cumulative revenue per customer at each period. Estimate terminal LTV using observed retention rates extrapolated to steady state. Compare LTV to CAC to derive payback period and LTV/CAC ratio.

4. **Run vintage-over-vintage comparison** — Overlay cohort curves to identify whether newer cohorts retain better or worse than older ones. Flag any cohort that deviates materially (>5pp retention difference at equivalent maturity). Investigate drivers: product changes, customer mix shift, pricing, or macro factors.

5. **Segment and decompose** — Cut cohorts by customer size, channel, or product to isolate whether retention trends are broad-based or driven by a specific segment. Identify if enterprise vs. SMB mix shifts explain apparent retention improvement.

6. **Assess unit economics trajectory** — Determine whether LTV/CAC is improving, stable, or degrading. Evaluate whether expansion revenue is masking underlying churn problems (GDR vs. NDR divergence). Calculate implied steady-state NDR at maturity for recent cohorts.

7. **Stress-test management projections** — Compare management's forward revenue model against actual cohort behavior. Apply the most recent cohort's retention curve (rather than blended historical) to new customer additions to build a bottom-up revenue bridge.

## Output

Structure the analysis report with:

- **Executive summary**: One-paragraph assessment of customer cohort quality and trajectory (improving, stable, or deteriorating)
- **Retention curve exhibit**: Indexed cohort chart showing NDR and GDR over time, with vintage overlay
- **LTV/CAC table**: By cohort vintage showing CAC, cumulative revenue per customer at 12/24/36 months, implied LTV, payback period, and LTV/CAC
- **Vintage comparison matrix**: Retention at common maturity points (Month 6, 12, 18, 24) across all cohorts, with color-coding for trends
- **Segmented findings**: Key differences in retention behavior by customer tier, channel, or product
- **Risk flags**: Specific concerns (e.g., "2024 cohorts show 8pp lower GDR at Month 12 vs. 2023 cohorts; driven by SMB mix increase")
- **Implications for underwriting**: How cohort economics affect revenue build, terminal growth rate assumptions, and valuation

## Quality Checks

- Confirm cohort revenue sums reconcile to total company revenue within 2% — discrepancies indicate missing or double-counted customers
- Verify that the number of cohorts with sufficient maturity (18+ months) supports conclusions about long-term retention
- Check that expansion revenue is not conflated with price increases on existing contracts vs. genuine upsell/cross-sell
- Ensure CAC calculations include all relevant costs (not just direct marketing) — [VERIFY] whether company includes SDR salaries, marketing ops, and attribution overhead
- Flag any cohort with fewer than 30 customers as statistically unreliable for retention conclusions
- Validate that retention improvements are not artifacts of changed cohort definitions, revenue recognition timing, or contract structure shifts
- Cross-check NDR figures against company-reported metrics — material differences require explanation
