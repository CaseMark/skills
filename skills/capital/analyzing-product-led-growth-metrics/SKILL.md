---
name: analyzing-product-led-growth-metrics
language: en
description: Evaluates PLG dynamics with viral coefficients, freemium conversion, product-qualified leads, and expansion revenue mechanics. Use when analyzing PLG companies, assessing virality, or evaluating product-driven acquisition.
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
# Analyzing Product Led Growth Metrics

Evaluates PLG dynamics with viral coefficients, freemium conversion, product-qualified leads, and expansion revenue mechanics.

## When To Use

- Diligencing a growth-equity or late-stage investment in a PLG company
- Benchmarking a portfolio company's self-serve funnel against category peers
- Assessing whether a company's growth is genuinely product-driven versus sales-assisted
- Evaluating expansion revenue sustainability and net-dollar-retention trajectory
- Comparing acquisition efficiency between organic/viral channels and paid channels

## Inputs To Gather

- **User funnel data**: Visitor → signup → activation → paid conversion rates with cohort breakdowns (monthly or weekly)
- **Viral/referral metrics**: Invitation rate per user, invite acceptance rate, viral cycle time, and calculated viral coefficient (K-factor)
- **Freemium-to-paid conversion**: Free-to-paid conversion rate by cohort, median time-to-convert, and conversion triggers (feature gates, usage limits, seat thresholds)
- **Product-Qualified Lead (PQL) definitions**: Company's PQL criteria, PQL-to-opportunity rate, PQL-to-closed-won rate, and average PQL deal size vs. sales-sourced deals
- **Expansion revenue data**: Net Dollar Retention (NDR), logo retention, seat expansion rate, upsell/cross-sell attach rates, and expansion revenue as a percentage of new ARR
- **Unit economics**: CAC by channel (organic, viral, paid, sales-assisted), CAC payback period, and LTV/CAC ratio segmented by acquisition source
- **Engagement/usage telemetry**: DAU/MAU ratio, feature adoption depth, time-to-value for new signups, and usage-based churn predictors

## Workflow

1. **Validate the PLG claim** — Determine what percentage of revenue is truly self-serve versus sales-assisted. Calculate the ratio of product-sourced pipeline to total pipeline. A company where >60% of new ARR originates from self-serve or PQL-driven motions is genuinely PLG; below that, treat it as a hybrid model and adjust expectations accordingly.

2. **Analyze the viral loop** — Compute the viral coefficient (K = invites per user × acceptance rate). Assess viral cycle time (shorter is better; under 3 days is strong). K > 1.0 implies organic viral growth; K between 0.3–1.0 indicates meaningful but not self-sustaining virality. Flag whether viral growth is inherent (product requires collaboration, e.g., Slack) or incentivized (referral credits) — inherent virality is more durable. [VERIFY] Compare K-factor against category benchmarks, which vary significantly by vertical.

3. **Evaluate freemium conversion mechanics** — Assess the free-to-paid conversion funnel: what gates trigger conversion (feature limits, usage caps, seat thresholds, compliance requirements)? Strong PLG companies show 3–8% visitor-to-free conversion and 5–15% free-to-paid conversion. Examine time-to-convert distribution — a long tail (>90 days) may indicate a weak conversion trigger or overly generous free tier. [VERIFY] Benchmark conversion rates against comparable PLG companies at similar scale.

4. **Score PQL effectiveness** — Review the company's PQL definition and compare PQL-to-close rates against MQL-to-close rates. PQLs should convert at 2–5× the rate of MQLs and carry higher average deal values. Assess whether the PQL scoring model is behavioral (usage-based) or firmographic — behavioral models correlate more strongly with conversion. Identify what percentage of total closed deals originate from PQLs versus outbound sales.

5. **Assess expansion revenue and NDR** — Compute NDR and decompose it into gross retention, seat expansion, upsell, and cross-sell components. NDR above 120% is elite for PLG; 110–120% is strong; below 110% warrants scrutiny on pricing power. Evaluate whether expansion is usage-driven (natural seat growth) or sales-driven (upsell motions). Usage-driven expansion is more predictable and capital-efficient.

6. **Calculate acquisition efficiency by channel** — Segment CAC into organic/viral, PQL-assisted, and outbound-sales channels. Compute blended and channel-specific LTV/CAC ratios. PLG companies should show organic/viral CAC at <25% of outbound CAC. Evaluate CAC payback period — under 12 months for self-serve, under 18 months for sales-assisted. Flag any trend of rising blended CAC, which may indicate the self-serve channel is saturating.

7. **Stress-test durability** — Assess whether PLG metrics are improving, stable, or deteriorating on a cohort basis. Newer cohorts with lower activation rates or slower viral coefficients suggest the easy market is captured. Evaluate competitive moats: network effects, data advantages, switching costs, and ecosystem lock-in that protect the PLG flywheel.

## Output

Produce an **Analysis Report** structured as:

- **PLG Classification**: Pure PLG / PLG-dominant hybrid / sales-led with PLG assist — with supporting data
- **Viral Loop Assessment**: K-factor, cycle time, virality type (inherent vs. incentivized), sustainability outlook
- **Conversion Funnel Scorecard**: Visitor → signup → activation → paid conversion rates benchmarked against category
- **PQL Effectiveness Summary**: PQL definition quality, conversion premium over MQLs, pipeline contribution
- **Expansion Revenue Profile**: NDR decomposition, expansion drivers, cohort trends
- **Acquisition Efficiency Matrix**: Channel-level CAC, LTV/CAC, payback periods, blended trend
- **Risk Flags**: Declining cohort metrics, over-reliance on a single viral channel, free-tier cannibalization, or rising blended CAC
- **Investment Implications**: How PLG dynamics affect underwriting assumptions for growth rate, margin trajectory, and capital efficiency

## Quality Checks

- All K-factor and conversion rate calculations are traceable to underlying data; no black-box numbers
- NDR is computed consistently (dollar-weighted, not logo-weighted) and decomposed into components
- Cohort analysis covers at least 6–12 months of data; single-period snapshots are flagged as insufficient
- Benchmarks are sourced from comparable companies at similar scale and stage — not mismatched comparisons (e.g., seed-stage benchmarks applied to a $50M ARR company)
- PQL analysis distinguishes between the company's defined PQL criteria and actual behavioral conversion patterns
- Any metric without sufficient underlying data is marked [VERIFY] rather than estimated
- Report clearly separates product-sourced growth from sales-sourced growth throughout — no conflation of channels
