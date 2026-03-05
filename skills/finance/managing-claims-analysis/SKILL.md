---
name: managing-claims-analysis
description: Structures claims data analysis with severity/frequency trending, case reserve monitoring, and litigation management. Use when analyzing claims data, trending claim frequency, or monitoring claim severity.
tags:
  - management
  - insurance
metadata:
  author: casemark
  practice_areas:
    - Insurance
    - Actuarial Science
    - Reinsurance
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Claims Analysis

Structures claims data analysis with severity/frequency trending, case reserve monitoring, and litigation management.

## When To Use

- Periodic review of open claims inventory (monthly, quarterly, annual)
- Analyzing shifts in claim frequency or severity by line of business, geography, or policy year
- Monitoring case reserves against incurred-but-not-reported (IBNR) expectations
- Preparing loss development triangles or actuarial exhibits for management or reinsurers
- Tracking litigated claims through disposition and evaluating defense counsel performance
- Identifying emerging loss trends (e.g., new peril types, social inflation effects, legislative changes)

## Inputs To Gather

- **Claims register / loss run**: Open, closed, and reopened claims with key fields — claim number, date of loss, report date, line of business, claimant, status, paid-to-date, case reserve, total incurred
- **Policy data**: Attachment points, limits, deductibles, policy period, coverage type
- **Prior period comparisons**: Previous loss runs or triangles for same evaluation dates
- **Reinsurance structure**: Treaty and facultative layers, retention levels, cession percentages
- **Litigation log**: Claims in suit with assigned counsel, jurisdiction, litigation phase, and next key date
- **Scope parameters**: Accident year vs. policy year, gross vs. net of reinsurance, confidence level for IBNR loads

## Workflow

1. **Validate data completeness**
   - Reconcile claim counts and total incurred against the source system
   - Confirm no duplicate claim entries or missing report-date fields
   - Flag any claims with zero reserves but open status — mark with [VERIFY] for adjuster confirmation

2. **Segment claims**
   - Group by line of business, accident year/quarter, and geography
   - Separate large losses (above a stated threshold, e.g., $250K or per-program excess point) from attritional claims
   - Isolate litigated vs. non-litigated claims for separate trending

3. **Build frequency and severity metrics**
   - Calculate claim frequency: reported claim count per earned exposure unit (policies in force, premium volume, or payroll as appropriate)
   - Calculate average severity: total incurred / closed claim count (exclude large losses for attritional severity)
   - Compute loss development factors from paid and incurred triangles; note any tail factor assumptions [VERIFY]
   - Compare current period metrics to prior periods and to industry benchmarks where available

4. **Analyze reserve adequacy**
   - Review case reserves on the top 10–25 claims by incurred value — note any that appear stale (no reserve change in 90+ days)
   - Compare aggregate case reserves to actuarial indicated IBNR by segment
   - Identify reserve strengthening or takedowns exceeding a materiality threshold
   - Flag any claims where paid amounts exceed prior case reserve (reserve "busts") for root-cause commentary

5. **Assess litigation exposure**
   - Summarize litigated claim inventory by jurisdiction, coverage line, and litigation stage
   - Track average duration from suit filing to resolution
   - Calculate litigation rate (litigated claims / total claims) and compare to prior periods
   - Note any claims with trial dates within 90 days or pending dispositive motions
   - Evaluate defense counsel billing against budgets and fee guidelines [VERIFY if fee guidelines are current]

6. **Identify trends and outliers**
   - Surface any acceleration in frequency or severity beyond two standard deviations from historical mean
   - Note geographic or product-line concentrations
   - Flag potential catastrophe or mass-tort aggregation issues
   - Highlight regulatory or legislative developments that may impact future loss costs [VERIFY jurisdiction-specific statutory changes]

7. **Compile management report**
   - Structure output with executive summary, detailed exhibits, and appendix
   - Include key metrics dashboard: frequency, severity, loss ratio, reserve development, litigation rate
   - Provide narrative commentary on material movements and recommended actions

## Output

- **Executive summary**: One-page overview of portfolio performance — claim counts, total incurred, loss ratio, and material changes from prior period
- **Frequency/severity exhibits**: Tables and trend lines by segment, with large-loss and attritional breakouts
- **Loss development triangles**: Paid and incurred triangles by accident year with selected development factors
- **Reserve adequacy section**: Top claims inventory, stale reserve flags, IBNR comparison, and reserve bust analysis
- **Litigation dashboard**: Claim counts in suit, litigation rate trend, average duration, defense spend summary
- **Trend alerts**: Flagged emerging issues with supporting data points and recommended next steps
- **Appendix**: Data sources, methodology notes, and glossary of terms

## Quality Checks

- Confirm all incurred totals foot to the underlying claims register — no rounding discrepancies
- Verify that large-loss thresholds are applied consistently across all segments
- Ensure loss development factors are sourced from current actuarial study or industry data [VERIFY vintage of development factors]
- Check that prior-period comparisons use the same valuation date and methodology
- Validate that litigation metrics exclude subrogation-only or recovery-only files unless explicitly in scope
- Confirm reinsurance cessions are correctly applied when reporting net figures
- Review narrative for unsupported conclusions — every material assertion should tie to a data exhibit
