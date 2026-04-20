---
name: tracking-portfolio-company-metrics
language: en
description: Monitors portfolio company KPIs including burn rate, runway, MRR growth, CAC/LTV, and cohort performance. Use when tracking portfolio metrics, assessing company health, or preparing portfolio reviews.
tags:
  - monitoring
  - venture-capital
  - portfolio
metadata:
  author: casemark
  practice_areas:
    - Venture Capital
    - Seed/Series Investing
    - Startup Ecosystems
  document_types:
    - Tracking Report
  skill_modes:
    - Monitoring
---
# Tracking Portfolio Company Metrics

Monitors portfolio company KPIs including burn rate, runway, MRR growth, CAC/LTV, and cohort performance to assess company health, flag emerging risks, and support portfolio review preparation.

## When To Use

- Preparing for quarterly or annual portfolio reviews with LPs
- Evaluating whether a portfolio company is on track between board meetings
- Deciding whether to participate in a follow-on round
- Triaging companies that may need operational support or bridge financing
- Building a standardized reporting cadence across a fund's portfolio

## Inputs To Gather

- **Monthly/quarterly financial reports** from portfolio companies (P&L, balance sheet, cash flow)
- **Revenue data**: MRR/ARR, net new MRR, expansion vs. contraction, churn
- **Cash position and burn**: current cash balance, gross burn, net burn, last funding date and amount
- **Customer/unit economics**: CAC, LTV, LTV/CAC ratio, payback period, gross margin
- **Growth indicators**: revenue growth rate (MoM/QoQ), logo count, NDR (net dollar retention)
- **Cohort data**: retention curves by signup month, revenue per cohort over time
- **Headcount and hiring plan**: current FTEs, open roles, department breakdown
- **Cap table and ownership data**: current fund ownership percentage, dilution from subsequent rounds
- **Company-provided narrative updates**: product milestones, pipeline, key wins/losses

## Workflow

1. **Normalize reporting data** — Align each company's financials to a common template (month-end periods, consistent revenue recognition). Flag companies with missing or late submissions.

2. **Calculate core financial health metrics**
   - **Burn rate**: gross burn (total monthly cash outflow) and net burn (gross burn minus revenue)
   - **Runway**: current cash / net burn = months remaining. Flag any company below 6 months runway as critical, below 12 months as watch-list.
   - **Burn multiple**: net burn / net new ARR. Healthy early-stage target is <2x; >3x warrants scrutiny.

3. **Assess revenue trajectory**
   - MRR/ARR and month-over-month growth rate. Compare against the company's own plan and against stage benchmarks (e.g., seed-stage SaaS: 15–20% MoM, Series A: 10–15% MoM). [VERIFY benchmarks against current market environment]
   - Net dollar retention (NDR): >120% strong, 100–120% adequate, <100% signals churn risk.
   - Break out expansion revenue vs. new logo revenue to understand growth composition.

4. **Evaluate unit economics**
   - **CAC**: total S&M spend / new customers acquired (blended) or by channel if data available.
   - **LTV**: (average revenue per account × gross margin) / monthly churn rate.
   - **LTV/CAC ratio**: target >3x for sustainable economics; <1.5x is a red flag.
   - **Payback period**: CAC / (monthly gross profit per customer). Target <18 months for SaaS.

5. **Analyze cohort performance**
   - Plot retention curves (logo and revenue) by monthly or quarterly signup cohort.
   - Identify whether recent cohorts retain better or worse than older ones — improving cohorts suggest product-market fit is strengthening.
   - Calculate revenue per cohort at 3, 6, and 12 months post-acquisition.

6. **Score and tier portfolio companies**
   - Assign a health rating (e.g., Green / Yellow / Red) based on composite of runway, growth rate, unit economics, and execution against plan.
   - Green: on plan, >12 months runway, healthy unit economics.
   - Yellow: behind plan on one dimension or runway 6–12 months.
   - Red: multiple metrics off-track, <6 months runway, or material execution failure.

7. **Compile tracking report**
   - One-page summary per company: health rating, key metrics table, trend arrows (improving/declining/flat), and 2–3 sentence narrative.
   - Portfolio-level rollup: aggregate fair value, TVPI/DPI progression, reserve allocation status, companies by tier.
   - Action items: follow-on decisions, board seat follow-ups, introductions needed, companies requiring triage calls.

## Output

A structured **Portfolio Tracking Report** containing:

- **Portfolio dashboard**: summary table with each company's health tier, latest ARR, runway, growth rate, and ownership percentage
- **Per-company detail sheets**: metrics table, cohort charts, burn/runway projection, and narrative update
- **Watch list**: companies flagged Yellow or Red with specific risk factors and recommended next steps
- **Reserve and follow-on analysis**: which companies may need bridge capital, pro-rata allocation for upcoming rounds
- **Trend analysis**: quarter-over-quarter comparison showing which companies are accelerating vs. decelerating

## Quality Checks

- Confirm all financial figures tie back to company-provided source data — no unverified estimates in final metrics
- Validate that runway calculations use the most recent month's net burn (not averages) unless explicitly noted
- Cross-check MRR figures against reported ARR (ARR = MRR × 12) for consistency
- Ensure LTV/CAC calculations use the same time period for both numerator and denominator
- Verify cohort data covers at least 3 complete cohorts before drawing retention conclusions
- Mark any metric derived from incomplete data with [VERIFY]
- Confirm ownership percentages reflect the latest cap table (post any recent rounds or conversions)
- Review health tier assignments against defined thresholds — no subjective overrides without documented rationale
