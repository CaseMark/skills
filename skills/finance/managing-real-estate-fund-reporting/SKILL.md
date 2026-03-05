---
name: managing-real-estate-fund-reporting
description: Structures real estate fund reporting with property-level performance, valuation updates, and distribution analysis. Use when preparing real estate fund reports, calculating fund returns, or documenting property performance.
tags:
  - management
  - real-estate-finance
  - valuation
metadata:
  author: casemark
  practice_areas:
    - Real Estate Finance
    - REIT Analysis
    - Property Investment
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Real Estate Fund Reporting

Structures real estate fund reporting with property-level performance, valuation updates, and distribution analysis.

## When To Use

- Preparing quarterly or annual investor reports for open-end or closed-end real estate funds
- Calculating fund-level and property-level returns (gross/net IRR, equity multiple, cash-on-cash)
- Documenting NAV per unit/share with supporting valuation detail
- Summarizing distribution waterfalls, promote calculations, and LP/GP splits
- Reporting on portfolio composition, occupancy trends, and capital deployment status
- Producing REIT-specific metrics (FFO, AFFO, same-store NOI growth) for public or non-traded vehicles

## Inputs To Gather

- **Fund structure details**: fund name, vintage year, fund size, investment period status, vehicle type (open-end, closed-end, REIT)
- **Property-level financials**: rent rolls, operating statements (actual vs. budget), capital expenditure schedules, and debt summaries for each asset
- **Valuation data**: most recent third-party appraisals or internal valuations, cap rate assumptions, discount rate inputs, and comparable sale data
- **Capital account records**: contributions called, unfunded commitments, distributions paid (return of capital vs. income), and current LP/GP account balances
- **Waterfall terms**: preferred return hurdle(s), catch-up provisions, carried interest splits, clawback triggers from the LPA
- **Market data**: submarket vacancy rates, rent growth trends, transaction volume, and macroeconomic indicators relevant to asset class
- **Prior period reports**: previous quarter's NAV, return figures, and any restatements or methodology changes

## Workflow

1. **Validate source data** — Reconcile property-level operating statements to the general ledger. Confirm that appraisal dates are current (within reporting quarter). Cross-check capital account balances against the fund administrator's records. Flag any asset with stale valuation data as [VERIFY].

2. **Calculate property-level performance** — For each asset, compute:
   - Net Operating Income (NOI) actual vs. budget and vs. prior period
   - Occupancy rate (physical and economic)
   - Debt service coverage ratio and loan-to-value
   - Unrealized gain/loss based on current valuation vs. cost basis
   - Capital expenditure spend vs. approved budget

3. **Roll up fund-level metrics** — Aggregate property results into portfolio-level figures:
   - Gross and net asset value (NAV), with a bridge from prior-period NAV (contributions + appreciation + income − distributions − fees − depreciation)
   - Gross and net IRR (since inception and for the reporting period) [VERIFY calculation methodology against LPA]
   - Total value to paid-in capital (TVPI) and distributions to paid-in capital (DPI)
   - For REIT vehicles: FFO, AFFO, and same-store NOI growth

4. **Run distribution waterfall** — Apply the LPA waterfall to determine:
   - Preferred return accrual and whether the hurdle has been met
   - Catch-up allocation status
   - Carried interest earned (realized and unrealized)
   - Projected next distribution amount and composition (return of capital vs. gain vs. income)

5. **Draft narrative sections** — Write a portfolio overview covering:
   - Market conditions and their impact on fund strategy
   - Significant leasing events, dispositions, acquisitions, or refinancings during the period
   - Material risks: lease expirations, tenant credit concerns, floating-rate debt exposure, construction delays
   - Capital deployment pipeline and remaining dry powder

6. **Assemble the report** — Organize into standard sections: executive summary, portfolio summary table, individual property pages, financial statements, capital account statement, waterfall summary, and appendices (glossary, methodology notes).

## Output

A structured fund report containing:

- **Executive summary** with headline metrics (NAV, IRR, equity multiple, distributions paid)
- **Portfolio dashboard** showing each property's NOI, occupancy, valuation, and debt metrics in a comparative table
- **Individual property pages** with operating detail, tenancy schedule highlights, and valuation commentary
- **Capital account statement** showing LP/GP balances, contributions, distributions, and ending balances
- **Waterfall summary** with preferred return status, promote calculation, and projected next distribution
- **Market commentary** section tying macro and submarket trends to fund positioning
- **NAV bridge** reconciling beginning to ending NAV with each component identified

## Quality Checks

- Confirm NAV bridge balances — beginning NAV plus all components must equal ending NAV exactly
- Verify IRR and equity multiple calculations against an independent model or fund administrator output [VERIFY]
- Ensure property valuations are dated within the reporting period; flag any appraisal older than six months
- Check that waterfall calculations conform to the specific LPA terms — preferred return day-count convention, compounding frequency, and hurdle reset provisions vary by fund [VERIFY against LPA]
- Validate that REIT metrics (FFO/AFFO) follow NAREIT definitions if the fund reports under that standard [VERIFY]
- Confirm all distributions are correctly classified (return of capital, capital gains, ordinary income) for tax reporting consistency
- Cross-check that total fund-level NOI equals the sum of individual property NOIs after eliminations
- Review for consistent rounding, date references, and terminology across all sections
