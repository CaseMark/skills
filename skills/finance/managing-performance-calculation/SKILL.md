---
name: managing-performance-calculation
description: Structures portfolio performance calculation with GIPS compliance, composite management, and attribution. Use when calculating returns, managing GIPS composites, or performing attribution analysis.
tags:
  - management
  - fund-operations
  - compliance
  - portfolio
metadata:
  author: casemark
  practice_areas:
    - Fund Administration
    - Investment Operations
    - Fund Accounting
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Performance Calculation

Structures portfolio performance calculation with GIPS compliance, composite management, and attribution.

## When To Use

- Calculating time-weighted or money-weighted returns for individual portfolios or composites
- Building or maintaining GIPS-compliant composite definitions and membership rules
- Performing return attribution (sector, factor, or Brinson-style) against a benchmark
- Reconciling performance figures across fund accounting, custodian, and front-office systems
- Preparing performance presentations or GIPS-compliant reports for prospective clients
- Validating return calculations during audits or verification engagements

## Inputs To Gather

- **Portfolio holdings and transactions**: Beginning/ending market values, cash flows with exact dates, accrued income, and trade-date vs. settlement-date positions
- **Benchmark data**: Index-level and constituent-level returns, weights, and classification schemes (GICS, ICB, custom)
- **Composite definition documents**: Inclusion/exclusion criteria, minimum asset thresholds, significant cash flow policy, composite description
- **Fee schedules**: Gross-of-fee and net-of-fee fee structures; model fee vs. actual fee treatment
- **Valuation frequency**: Daily, monthly, or other; sub-period break points for large external cash flows
- **GIPS version and firm definition**: Confirm whether GIPS 2020 or earlier standards apply; confirm the firm's definition of total firm assets [VERIFY]

## Workflow

1. **Validate source data**
   - Confirm market values tie to NAV or custodian statements
   - Reconcile cash flow timing (trade date vs. settlement date) to the firm's stated policy
   - Check for missing prices, stale valuations, or corporate-action adjustments
   - Flag any gaps with [VERIFY] for resolution before proceeding

2. **Calculate portfolio-level returns**
   - Apply time-weighted rate of return (TWRR) using Modified Dietz or true daily valuation, depending on valuation frequency
   - For private equity/illiquid vehicles, calculate since-inception IRR (SI-IRR) using money-weighted methodology [VERIFY — GIPS 2020 requires SI-IRR for closed-end pooled funds]
   - Compute both gross-of-fee and net-of-fee returns; document fee deduction methodology
   - Annualize returns only for periods of one year or longer (GIPS requirement)

3. **Manage composite construction**
   - Apply composite inclusion rules: new portfolios added at start of next full measurement period (or per firm policy)
   - Remove terminated portfolios after the last full measurement period
   - Apply significant cash flow policy — temporarily exclude portfolios exceeding the threshold [VERIFY — threshold percentage is firm-defined]
   - Calculate asset-weighted composite returns (beginning-of-period weighting or aggregate method)
   - Compute internal dispersion (equal-weighted std. dev., high-low, or interquartile range) for composites with ≥6 portfolios for the full year

4. **Perform return attribution**
   - Select attribution model: Brinson-Fachler (allocation + selection + interaction), factor-based, or risk-adjusted
   - Align portfolio and benchmark classification hierarchies; map any custom sectors to benchmark taxonomy
   - Calculate single-period attribution effects; for multi-period, apply geometric smoothing (Carino, Menchero, or firm-preferred method) to link effects without residual
   - Separate currency effects from local returns when applicable

5. **Compile GIPS-compliant presentation**
   - Include minimum required disclosures: composite description, benchmark description, fee schedule, creation date, firm definition, and number of portfolios
   - Present at least five years of annual performance (or since inception if shorter); build toward ten years
   - Show composite and benchmark returns, internal dispersion, and composite/firm assets
   - Include three-year annualized ex-post standard deviation (36-month) for both composite and benchmark [VERIFY — required for periods ending 2011 and later under GIPS 2020]

## Output

- **Performance summary table**: Portfolio and composite returns (gross and net), benchmark returns, excess return, and tracking error for each period
- **Composite statistics**: Number of portfolios, composite assets, percentage of firm assets, internal dispersion measure
- **Attribution report**: Allocation, selection, and interaction effects by sector/factor with linked multi-period totals
- **GIPS-compliant presentation**: Formatted per GIPS 2020 with all required disclosures, ready for verification review
- **Exception log**: List of data gaps, stale prices, reconciliation breaks, or policy deviations encountered, each tagged with resolution status

## Quality Checks

- Returns match or reconcile within tolerance (typically ±1–2 bps) to custodian/administrator-reported figures
- Composite membership changes are documented with effective dates and reasons
- Attribution effects sum to total excess return with no unexplained residual
- GIPS presentation includes all mandatory disclosures for the relevant composite type (broad distribution pooled fund, limited distribution, segregated account) [VERIFY]
- Annualization is not applied to periods shorter than one year
- Significant cash flow policy is consistently applied across all portfolios in the composite
- Fee deduction methodology is documented and consistently applied (actual vs. model fees)
- All [VERIFY] items are resolved or escalated before final delivery
