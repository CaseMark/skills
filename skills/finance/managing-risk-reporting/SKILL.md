---
name: managing-risk-reporting
language: en
description: Structures risk reporting dashboards with limit utilization, risk metric trends, and exception documentation. Use when creating risk reports, designing risk dashboards, or documenting risk positions.
tags:
  - management
  - risk-management
  - risk
metadata:
  author: casemark
  practice_areas:
    - Risk Management
    - Enterprise Risk
    - Market Risk
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Risk Reporting

Structures risk reporting dashboards with limit utilization, risk metric trends, and exception documentation.

## When To Use

- Building periodic risk reports for board, C-suite, or risk committees (daily, weekly, monthly, quarterly)
- Designing or restructuring a risk dashboard layout covering market, credit, liquidity, or operational risk
- Documenting limit breaches, near-misses, or exception approvals for audit trail purposes
- Consolidating risk positions across desks, business units, or legal entities into a unified view
- Preparing ad-hoc risk summaries triggered by market events, regulatory inquiries, or internal escalations

## Inputs To Gather

- **Reporting scope**: asset classes, desks, legal entities, and risk types (market, credit, liquidity, operational) covered
- **Risk metrics**: VaR (parametric, historical, Monte Carlo), Expected Shortfall / CVaR, stress test P&L, Greeks, DV01, CS01, duration, notional exposure, concentration ratios
- **Limit framework**: approved limits by metric and hierarchy level (desk → business unit → firm), temporary limit increases, and escalation thresholds (warning / soft / hard)
- **Current positions**: portfolio-level and aggregated exposures, mark-to-market values, collateral balances
- **Breach and exception log**: date/time of breach, metric breached, magnitude, responsible desk, remediation action, approver, and resolution status
- **Time horizon and frequency**: intraday, end-of-day, weekly, or monthly; rolling windows vs. point-in-time snapshots
- **Benchmark / peer data** (if applicable): industry percentiles, regulatory minimums, internal targets
- **Data sources and cut-off times**: upstream systems, pricing feeds, reconciliation status — flag any stale or missing data

## Workflow

1. **Define report structure**
   - Confirm audience (board summary vs. trading desk detail) and tailor granularity accordingly
   - Select the risk metrics and limit categories relevant to the report scope
   - Establish the reporting date, data cut-off time, and base currency

2. **Collect and validate data**
   - Pull position, P&L, and risk metric data from upstream risk systems
   - Reconcile key figures against independent sources (back-office, accounting, collateral management)
   - Flag any gaps, stale prices, or model overrides — mark with [VERIFY] if unresolved

3. **Build limit utilization section**
   - Present each limit as: current usage | approved limit | utilization % | headroom
   - Use traffic-light indicators: green (< 80%), amber (80–99%), red (≥ 100% or breached)
   - Include trend arrows or sparklines showing utilization over the trailing period (e.g., 5-day, 30-day)

4. **Compile risk metric trends**
   - Show time-series of key metrics (e.g., 10-day VaR, stressed VaR, ES) with consistent scaling
   - Highlight inflection points: sudden jumps, sustained drift toward limits, or significant reductions
   - Add context annotations for material moves (new positions, market events, model changes)

5. **Document exceptions and breaches**
   - For each breach: metric, limit level, breach magnitude, duration, desk/entity, root cause
   - Record remediation steps taken or planned, approver identity, and expected resolution date
   - Classify breaches: active (unresolved), cured (position reduced), or approved (temporary increase granted)

6. **Add commentary and forward-looking notes**
   - Summarize the top 3–5 risk themes for the period
   - Note upcoming events that could affect risk posture (expiries, rebalancing, macro releases)
   - State any model limitations, parameter changes, or methodology updates applied during the period

7. **Format and distribute**
   - Apply consistent table formatting, conditional color coding, and chart labeling
   - Include a version stamp, data-as-of timestamp, and distribution list
   - Route through appropriate review and sign-off before distribution

## Output

The deliverable is a structured risk report containing:

- **Executive summary**: 3–5 bullet-point overview of risk posture, material changes, and key actions
- **Limit utilization table**: metric | current | limit | utilization % | status, with traffic-light coding
- **Risk metric trends**: time-series charts or tables with annotations for significant moves
- **Breach / exception log**: tabular record of all breaches with status, root cause, and remediation
- **Commentary section**: narrative covering risk themes, outlook, and methodology notes
- **Appendix** (as needed): detailed position breakdowns, back-test results, stress scenario outputs

## Quality Checks

- Every metric has a clearly stated measurement methodology and confidence level [VERIFY methodology aligns with firm's approved risk policy]
- Limit utilization figures reconcile to the official limit register — no orphaned or outdated limits
- Breach counts and statuses match the exception management system of record
- All data points carry a clear as-of date/time; stale or estimated figures are explicitly labeled
- Report uses consistent units (currency, basis points, percentage) and rounding conventions throughout
- Trend comparisons use the same calculation window and parameters as prior periods — methodology changes are called out
- [VERIFY] regulatory capital metrics (e.g., FRTB IMA/SA, Basel III/IV ratios) reference the applicable regime and any transitional provisions in effect
- Sign-off by the appropriate risk officer or committee chair is documented before distribution
