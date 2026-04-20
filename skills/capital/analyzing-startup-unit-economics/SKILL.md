---
name: analyzing-startup-unit-economics
language: en
description: Deconstructs unit economics with CAC, LTV, payback period, gross margin, and contribution margin analysis. Use when analyzing unit economics, validating SaaS metrics, or assessing business model efficiency.
tags:
  - analysis
  - venture-capital
metadata:
  author: casemark
  practice_areas:
    - Venture Capital
    - Seed/Series Investing
    - Startup Ecosystems
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Startup Unit Economics

Deconstructs unit economics with CAC, LTV, payback period, gross margin, and contribution margin analysis.

## When To Use

- Evaluating a startup's business model viability during due diligence for seed or Series A/B rounds
- Benchmarking a portfolio company's efficiency metrics against cohort or industry standards
- Assessing whether a company's growth spending is sustainable before follow-on investment
- Validating founder-reported metrics in a pitch deck or data room against raw financials
- Stress-testing margin assumptions in financial models or projections

## Inputs To Gather

- **Revenue data**: MRR/ARR broken out by cohort, contract type, and pricing tier
- **Customer acquisition costs**: Total sales & marketing spend, headcount costs, paid channel spend, attribution breakdown (blended vs. channel-specific CAC)
- **Churn and retention**: Monthly/annual logo churn, revenue churn (gross and net), cohort retention curves
- **Gross margin inputs**: COGS breakdown — hosting/infrastructure, customer support, onboarding, payment processing, third-party API costs
- **Customer count and segmentation**: Number of customers by plan/tier, ACV distribution, enterprise vs. SMB mix
- **Expansion revenue**: Upsell/cross-sell revenue, seat expansion, usage-based overage
- **Time period**: Confirm trailing period (T-3, T-6, T-12 months) and whether data is accrual or cash-basis

## Workflow

1. **Validate raw data** — Reconcile reported metrics against source financials. Check that total revenue ties to MRR x months, that S&M spend matches P&L line items, and that customer counts are internally consistent. Flag discrepancies with [VERIFY].

2. **Calculate core unit economics**:
   - **CAC** = Total S&M spend / New customers acquired (calculate blended and per-channel)
   - **Gross Margin** = (Revenue − COGS) / Revenue — itemize COGS components; flag if founder excludes typical line items (e.g., customer success salaries)
   - **Contribution Margin** = Gross Profit − Variable Operating Costs per unit (include variable S&M, variable G&A if applicable)
   - **LTV** = ARPU × Gross Margin / Monthly Churn Rate (or use DCF-based LTV for longer contract businesses; note the method used)
   - **LTV:CAC Ratio** = LTV / CAC — target ≥ 3:1 for venture-scale businesses [VERIFY against sector-specific benchmarks]
   - **CAC Payback Period** = CAC / (ARPU × Gross Margin) — express in months; ≤12 months is strong for SMB SaaS, ≤18-24 months acceptable for enterprise [VERIFY by segment]

3. **Assess cohort behavior** — Plot retention curves by acquisition cohort. Identify whether recent cohorts retain better or worse than older ones. Calculate net dollar retention (NDR); >120% NDR signals strong expansion economics. Note if data depth is insufficient for mature cohort analysis.

4. **Analyze margin trajectory** — Determine whether gross margin is expanding, stable, or compressing over time. Identify drivers: infrastructure cost leverage, support cost scaling, pricing changes, mix shift. Distinguish between current-state margins and at-scale projected margins.

5. **Benchmark and contextualize** — Compare metrics against relevant benchmarks:
   - Stage-appropriate medians (e.g., Bessemer Cloud Index, OpenView SaaS Benchmarks) [VERIFY benchmark source is current]
   - Business-model norms: usage-based vs. seat-based vs. platform pricing models carry different margin and retention profiles
   - Note where the company is an outlier (positive or negative) and why

6. **Identify risks and sensitivities** — Stress-test key assumptions:
   - What happens to LTV:CAC if churn increases 20%?
   - How does CAC payback shift if blended CAC rises with channel saturation?
   - Are gross margins artificially high due to deferred costs (e.g., free onboarding that won't scale)?
   - Is expansion revenue masking poor logo retention?

## Output

Structure the deliverable as follows:

- **Executive Summary** (2-3 sentences): Headline assessment of unit economics health and investability signal
- **Core Metrics Table**: CAC, LTV, LTV:CAC, payback period, gross margin, contribution margin, NDR — with trailing 6- and 12-month values where available
- **Cohort Analysis**: Retention curve summary with visual description or table; NDR by cohort vintage
- **Margin Analysis**: Current gross margin breakdown with trend and at-scale projection
- **Key Risks**: Ranked list of unit economics risks with magnitude estimates
- **Benchmarking Context**: Where the company sits relative to stage/sector peers
- **Data Gaps & Assumptions**: Explicit list of missing inputs, assumptions made, and [VERIFY] items

## Quality Checks

- Every calculated metric traces back to identified source data — no orphaned numbers
- CAC calculation method is stated (blended vs. fully-loaded vs. channel-specific); ensure S&M denominator includes all relevant costs (salaries, tools, attribution)
- LTV method is stated (simple vs. DCF); discount rate noted if DCF is used
- Gross margin COGS is itemized — confirm no material costs are excluded or misclassified as operating expense
- All benchmarks cite a specific source and vintage year
- Sensitivity analysis covers at least churn, CAC, and gross margin variables
- [VERIFY] tags are present for any jurisdiction-specific tax treatment, benchmark thresholds, or accounting-method-dependent figures
- If data covers <6 months or <100 customers, flag statistical reliability limitations explicitly
