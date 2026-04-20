---
name: managing-co-investment-reporting
language: en
description: Structures co-investment reporting with deal-level performance, fee/carry calculations, and co-invest program aggregate analysis. Use when reporting co-invest performance, tracking deal-level returns, or preparing co-invest summaries.
tags:
  - management
  - investor-relations-and-lp-reporting
  - investment
metadata:
  author: casemark
  practice_areas:
    - Investor Relations
    - LP Reporting
    - Fund Administration
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Co Investment Reporting

## When To Use

- Preparing quarterly or annual co-investment performance reports for LPs
- Reporting deal-level returns (gross and net) on co-invest vehicles or SPVs
- Calculating fee and carried interest allocations specific to co-investment structures
- Aggregating co-invest program-level metrics across multiple deals
- Responding to LP data requests for co-investment track record or attribution analysis
- Reconciling co-invest capital accounts against the main fund

## Inputs To Gather

- **Deal data**: Investment name, sector, entry date, exit date (if realized), cost basis, current fair value, and valuation methodology per deal
- **Capital structure**: Each co-investor's committed capital, called capital, unfunded commitment, and distribution history per co-invest vehicle or SPV
- **Fee terms**: Management fee rate (if any), carried interest percentage, preferred return/hurdle rate, catch-up provisions, and any fee offset or rebate arrangements [VERIFY against co-invest side letter or SPV LPA]
- **Waterfall parameters**: Whole-fund vs. deal-by-deal carry, GP clawback provisions, escrow percentages
- **Valuations**: Most recent NAV per deal, valuation date, write-ups/write-downs since prior period, and basis for marks (comparable transactions, DCF, third-party appraisal)
- **FX data**: Original currency of investment and reporting currency; exchange rates at entry, current period-end, and exit
- **Benchmark data**: Main fund performance for same deals (to enable co-invest vs. fund return comparison)

## Workflow

1. **Validate deal universe** — Confirm the complete list of active and realized co-investments. Cross-reference against the co-invest register or SPV formation records. Flag any deals missing valuation updates or with stale marks older than one quarter.

2. **Build deal-level performance table** — For each co-investment, compute:
   - Gross MOIC (total value / invested capital)
   - Gross IRR (using cash-flow dates: calls, distributions, and residual NAV)
   - Realized vs. unrealized breakdown
   - Holding period in years
   - [VERIFY] that IRR calculations use actual cash-flow dates, not approximated quarterly midpoints

3. **Calculate fee and carry** — Apply the co-invest fee schedule to each deal or vehicle:
   - Management fees (often reduced or zero for co-invests — confirm per vehicle terms)
   - Carried interest allocation using the applicable waterfall (deal-by-deal or whole-program)
   - Preferred return accrual and catch-up computation
   - Net MOIC and net IRR after fees and carry
   - [VERIFY] waterfall mechanics against each SPV's governing documents, as terms frequently differ across co-invest vehicles

4. **Aggregate program-level metrics** — Roll up individual deal metrics into program totals:
   - Total co-invest capital committed, called, distributed, and NAV
   - Program-level gross and net IRR and MOIC (pooled, not simple average)
   - DPI (distributions to paid-in), RVPI (residual value to paid-in), and TVPI (total value to paid-in)
   - Sector, geography, and vintage year diversification summaries
   - Comparison of co-invest returns vs. main fund returns on the same underlying deals

5. **Prepare LP-facing output** — Structure the report with:
   - Executive summary of co-invest program performance and key movements in the period
   - Deal-level detail table with standardized columns
   - Capital account statement per co-investor (beginning balance, calls, distributions, ending NAV)
   - Footnotes explaining valuation methodology, FX treatment, and any material assumptions
   - Attribution of period-over-period NAV change (new investments, realizations, valuation changes, FX impact)

6. **Reconcile and cross-check** — Tie reported figures back to fund admin records and the general ledger. Verify that aggregate co-invest distributions plus NAV equal total value. Ensure net performance figures reconcile with fee and carry calculations.

## Output

A co-investment performance report containing:

- **Deal summary table**: One row per co-investment with cost, fair value, gross/net MOIC, gross/net IRR, DPI, and status (unrealized/partially realized/fully realized)
- **Program aggregate section**: Pooled gross and net returns, total capital metrics (committed, called, distributed, NAV), TVPI/DPI/RVPI
- **Capital account statements**: Per-investor breakdown showing beginning balance, contributions, distributions, gain/loss allocation, and ending balance
- **Fee and carry schedule**: Management fees charged, carried interest accrued or distributed, preferred return status per vehicle
- **Co-invest vs. fund comparison**: Side-by-side return comparison on overlapping deals
- **Period commentary**: Narrative on new co-investments, realizations, material valuation changes, and outlook

## Quality Checks

- IRR calculations use actual cash-flow dates and are verified against an independent calculator or fund admin output
- Gross-to-net bridge is arithmetically consistent (gross return minus fees minus carry equals net return)
- Capital account balances tie to fund administrator records within an acceptable tolerance
- MOIC and TVPI figures are cross-verified (TVPI should equal DPI + RVPI; MOIC should equal total value / cost)
- All unrealized valuations carry a date stamp and methodology notation
- FX gains/losses are separately identified and not blended into operating returns without disclosure
- Report formatting is consistent with prior-period reports to enable LP trend analysis
- Any deal with a valuation older than 90 days is flagged with [VERIFY]
- Carried interest calculations are tested against at least one worked example from the SPV waterfall
