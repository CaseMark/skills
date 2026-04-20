---
name: analyzing-saas-business-metrics
language: en
description: Deconstructs SaaS operating metrics including ARR, NRR, gross retention, magic number, rule of 40, and cohort economics. Use when analyzing SaaS businesses, benchmarking software metrics, or evaluating subscription model health.
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
# Analyzing Saas Business Metrics

Deconstructs SaaS operating metrics including ARR, NRR, gross retention, magic number, rule of 40, and cohort economics.

## When To Use

- Evaluating a SaaS company for growth equity or late-stage investment
- Benchmarking a portfolio company's operating metrics against peer cohorts
- Assessing subscription model health during due diligence or quarterly reviews
- Analyzing expansion revenue dynamics and churn trends for board-level reporting
- Comparing "efficient growth" profiles across competing deal opportunities

## Inputs To Gather

- **Revenue data**: Monthly or quarterly MRR/ARR schedules covering at least 12–24 months; breakdown by new, expansion, contraction, and churned revenue
- **Customer data**: Beginning-of-period and end-of-period customer counts by cohort (sign-up quarter or ACV tier); logo churn counts
- **Expense data**: Fully loaded S&M spend by quarter (including headcount costs); COGS broken out to show hosting, support, and CS costs separately
- **Cohort schedules**: Revenue by vintage cohort showing retention and expansion over time (ideally 8+ quarterly cohorts)
- **Billing & contract details**: Contract term mix (monthly vs. annual vs. multi-year), average ACV, and gross-to-net revenue adjustments
- **Context**: Industry vertical, target customer segment (SMB/mid-market/enterprise), and pricing model (seat-based, usage-based, platform fee)

## Workflow

1. **Validate the ARR bridge**
   - Reconstruct ARR from Beginning ARR + New + Expansion − Contraction − Churn = Ending ARR
   - Confirm each component ties to underlying MRR schedules; flag any reconciliation gaps with [VERIFY]
   - Distinguish between committed ARR and run-rate ARR if usage-based revenue is material

2. **Calculate core retention metrics**
   - **Gross Dollar Retention (GDR)**: (Beginning ARR − Contraction − Churn) / Beginning ARR. Healthy benchmark: >90% for enterprise, >80% for SMB [VERIFY against current market benchmarks]
   - **Net Dollar Retention (NDR/NRR)**: (Beginning ARR + Expansion − Contraction − Churn) / Beginning ARR. Best-in-class: >120% enterprise, >110% mid-market
   - **Logo retention**: 1 − (churned logos / beginning logos). Separate from dollar retention to isolate unit economics from mix effects
   - Note whether retention is calculated on a trailing-12-month basis or quarterly annualized — results differ materially

3. **Assess growth efficiency**
   - **Magic Number**: Net New ARR (current quarter) / S&M Spend (prior quarter). Targets: >0.75 indicates efficient spend; >1.0 is strong; <0.5 signals concern
   - **CAC Payback**: Fully loaded S&M per new customer / (new ARR per customer × gross margin). Express in months; <18 months is generally attractive for enterprise SaaS
   - **LTV/CAC**: (ARR per customer × gross margin) / (1 − GDR) / CAC. Minimum threshold typically >3x
   - Separate new-logo acquisition efficiency from expansion-driven growth — blended metrics can mask deteriorating new-business economics

4. **Evaluate profitability and the Rule of 40**
   - Rule of 40 = YoY ARR growth rate (%) + FCF margin (%) or EBITDA margin (%). Score ≥40 is the benchmark; identify which component is driving the result
   - Break out **gross margin** (target >70% for pure SaaS, >60% if managed services are included [VERIFY]). Scrutinize hosting costs, capitalized development, and professional services pass-throughs
   - Examine operating leverage: is S&M as a % of revenue declining as revenue scales? Is G&A staying flat or growing?

5. **Analyze cohort economics**
   - Build a cohort waterfall: for each vintage, show cumulative revenue as a multiple of first-period revenue at 4, 8, 12, and 16+ quarters
   - Identify whether newer cohorts retain and expand at the same rate as older ones — declining cohort quality is a red flag
   - Calculate **cohort payback**: quarters until cumulative gross profit from a cohort exceeds the S&M cost to acquire it
   - Flag if expansion is concentrated in a small number of large accounts vs. broad-based

6. **Benchmark and contextualize**
   - Compare all key metrics against relevant public SaaS comps and private benchmarks (e.g., Bessemer Cloud Index, ICONIQ Growth reports, KeyBanc SaaS survey) [VERIFY data sources are current]
   - Adjust for company stage (e.g., $10M ARR vs. $100M ARR expectations differ), end-market, and contract structure
   - Highlight where the company is top-quartile, median, or below-median on each metric

## Output

Produce a structured SaaS Metrics Analysis containing:

- **Executive summary**: 3–5 sentence assessment of subscription model health and growth quality
- **ARR bridge table**: Quarterly ARR waterfall with all components for the trailing 8+ quarters
- **Retention dashboard**: GDR, NDR, and logo retention trended over time with commentary on drivers
- **Efficiency scorecard**: Magic number, CAC payback, LTV/CAC, and Rule of 40 — each with a benchmark comparison
- **Cohort matrix**: Vintage cohort retention/expansion grid with visual highlighting of trends
- **Key findings**: Bulleted list of 5–10 specific observations (strengths, risks, and areas requiring further diligence)
- **Open items**: Any metrics that could not be calculated due to missing data, marked [VERIFY]

## Quality Checks

- ARR bridge reconciles to within 1% of reported ending ARR; any variance is explained
- Retention metrics are calculated on a consistent basis (same period definition) throughout
- Magic number uses prior-quarter S&M spend (not same-quarter) to reflect the sales cycle lag
- Gross margin excludes capitalized software development costs unless explicitly noted
- Cohort analysis covers enough vintages (minimum 4) to identify trend vs. noise
- All benchmark comparisons cite the source and vintage of the benchmark data
- No metric is presented without context — raw numbers always accompanied by what "good" looks like for the company's stage and segment
- Assumptions about annualization, seasonality adjustments, or pro-forma treatments are stated explicitly
