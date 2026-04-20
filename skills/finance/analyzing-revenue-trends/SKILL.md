---
name: analyzing-revenue-trends
language: en
description: Structures revenue analysis with growth decomposition, cohort analysis, and leading indicator tracking. Use when analyzing revenue, decomposing growth drivers, or tracking revenue leading indicators.
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
# Analyzing Revenue Trends

Structures revenue analysis with growth decomposition, cohort analysis, and leading indicator tracking for FP&A, management accounting, and business intelligence teams.

## When To Use

- Periodic revenue performance reviews (monthly, quarterly, annual)
- Board or leadership reporting requiring growth driver explanations
- Investigating unexpected revenue acceleration or deceleration
- Evaluating pricing changes, product mix shifts, or geographic expansion impact
- Building revenue forecasts grounded in historical trend decomposition
- Assessing customer cohort health and retention-driven revenue dynamics

## Inputs To Gather

- **Revenue data**: Time-series revenue by period (monthly minimum), broken out by product/service line, geography, customer segment, and channel where available
- **Customer data**: New vs. existing customer revenue splits, customer counts by cohort (sign-up period), churn/retention rates, average revenue per account (ARPA)
- **Pricing data**: Price changes, discount rates, promotional periods, contract renewal terms
- **Volume data**: Units sold, transactions processed, seats/licenses, or other quantity metrics
- **Leading indicators**: Pipeline value, bookings/backlog, qualified leads, trial conversions, expansion MRR, net revenue retention (NRR)
- **Context**: Market conditions, competitive actions, product launches, or operational changes during the analysis period

## Workflow

1. **Define scope and segmentation**
   - Confirm time horizon (trailing 4Q, YoY, multi-year) and reporting granularity
   - Agree on segmentation axes: product line, geography, customer tier, channel
   - Identify the base period and comparison period(s)

2. **Decompose revenue growth**
   - Separate organic vs. inorganic (M&A) growth
   - Break organic growth into **price × volume** components
   - Further decompose volume into new customer acquisition, existing customer expansion, and churn/contraction
   - Calculate contribution of each segment to total growth (waterfall analysis)
   - Flag any one-time items (large deals, catch-up billing, contract true-ups) and normalize

3. **Run cohort analysis**
   - Group customers by acquisition period (monthly or quarterly cohorts)
   - Track revenue per cohort over time to identify retention curves
   - Calculate cohort-level metrics: gross retention, net retention, payback period
   - Compare recent cohorts against mature cohorts — flag deteriorating or improving trends
   - Identify cohort-specific drivers (e.g., product version, sales channel, pricing plan)

4. **Assess leading indicators**
   - Map each leading indicator to the revenue line it predicts (e.g., pipeline → new logo revenue, NRR → expansion revenue)
   - Calculate conversion rates and lag times between indicator movement and revenue impact
   - Identify divergences — where leading indicators conflict with trailing revenue trends
   - Highlight indicators signaling inflection points (acceleration, deceleration, or plateau)

5. **Synthesize findings**
   - Rank growth drivers by magnitude of contribution and sustainability
   - Identify the top 2–3 risks to revenue trajectory and the top 2–3 opportunities
   - Connect findings to actionable recommendations (pricing adjustments, segment investment, churn intervention)
   - Note confidence levels — distinguish data-supported conclusions from directional hypotheses

## Output

- **Executive summary**: 3–5 bullet narrative of revenue trajectory and primary drivers
- **Growth decomposition waterfall**: Visual or tabular breakdown of growth into price, volume (new/expansion/churn), and one-time components
- **Cohort retention table**: Revenue by cohort over time with gross and net retention rates
- **Leading indicator dashboard**: Current values, trend direction, and implied forward revenue impact
- **Risk/opportunity register**: Top risks and opportunities with estimated revenue impact ranges
- **Assumptions and limitations**: Data gaps, normalization choices, and items requiring follow-up

## Quality Checks

- Growth components sum to total reported revenue change (no unexplained residuals)
- Cohort revenue rolls up to total revenue — reconcile any discrepancies
- Price × volume decomposition is consistent with actual ASP and unit data [VERIFY against source systems]
- Leading indicator lag assumptions are grounded in historical conversion data, not assumed
- One-time items are identified and excluded from run-rate calculations
- Currency effects are isolated if multi-currency revenue is in scope [VERIFY reporting currency policy]
- Segment definitions match the organization's standard taxonomy — do not create ad hoc groupings
- All data sources and extraction dates are documented for reproducibility
