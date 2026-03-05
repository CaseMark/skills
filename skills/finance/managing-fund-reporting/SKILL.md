---
name: managing-fund-reporting
description: Structures LP fund reporting with NAV calculation, performance attribution, and portfolio updates. Use when preparing LP reports, calculating fund performance, or creating quarterly updates.
tags:
  - management
  - private-equity
  - portfolio
metadata:
  author: casemark
  practice_areas:
    - Private Equity
    - Venture Capital
    - Growth Equity
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Fund Reporting

Structures LP fund reporting with NAV calculation, performance attribution, and portfolio updates for limited partners across PE, VC, and growth equity funds.

## When To Use

- Preparing quarterly or annual LP reports with fund-level and portfolio-level performance data
- Calculating or validating Net Asset Value (NAV) for a reporting period
- Building performance attribution analysis (gross/net IRR, TVPI, DPI, RVPI)
- Drafting portfolio company updates with operational and financial KPIs
- Responding to ad hoc LP data requests or ILPA-template reporting obligations
- Consolidating data across co-investment vehicles or parallel fund structures

## Inputs To Gather

- **Fund terms**: LPA-defined management fee structure, carried interest waterfall, preferred return, GP commitment percentage
- **Capital account data**: Cumulative capital calls, distributions, recallable amounts, and unfunded commitments per LP
- **Portfolio company financials**: Revenue, EBITDA, net income, cash position, debt levels, and any board-approved projections
- **Valuation marks**: Most recent fair value estimates per ASC 820 / IFRS 13, valuation methodology used (comparable transactions, DCF, market multiples), and date of last third-party valuation [VERIFY jurisdiction-specific fair value standards]
- **Cash flow schedule**: Drawdowns, distributions (return of capital vs. gain), and recycling activity during the period
- **Fee and expense detail**: Management fees accrued/paid, fund-level expenses, organizational costs amortization, broken-deal costs
- **Benchmark data**: Target benchmark indices (Cambridge Associates, Preqin, public market equivalent) for comparative context

## Workflow

1. **Validate source data**
   - Reconcile the trial balance and capital account statements from the fund administrator
   - Confirm all portfolio company valuations have been updated for the reporting period
   - Cross-check cash flow waterfall inputs against bank statements and call/distribution notices
   - Flag any stale valuations (>90 days old) or missing data points with [VERIFY]

2. **Calculate NAV**
   - Start with prior-period NAV, add capital called, subtract distributions, apply unrealized gain/loss adjustments
   - Deduct accrued management fees, fund expenses, and carried interest accrual per the waterfall
   - Reconcile ending NAV to the administrator's statement; investigate variances >0.5%
   - For multi-currency funds, document FX rates used and hedging adjustments

3. **Compute performance metrics**
   - **Gross IRR / Net IRR**: Use actual cash flow dates; specify whether SI-IRR or pooled methodology is applied
   - **TVPI** (Total Value to Paid-In): (NAV + cumulative distributions) / cumulative contributions
   - **DPI** (Distributions to Paid-In): Cumulative distributions / cumulative contributions
   - **RVPI** (Residual Value to Paid-In): NAV / cumulative contributions
   - **PME** (Public Market Equivalent): Calculate Kaplan-Schoar or Direct Alpha against the stated benchmark [VERIFY LP-agreed benchmark index]
   - Present since-inception, trailing 1-year, and current-quarter figures

4. **Build performance attribution**
   - Break down portfolio-level returns by investment vintage, sector, geography, and deal size
   - Identify top/bottom contributors to gross return with realized vs. unrealized splits
   - Include write-ups/write-downs with brief explanatory notes (e.g., new financing round, revenue miss, multiple expansion)

5. **Draft portfolio company updates**
   - For each active holding: investment date, cost basis, current fair value, ownership %, and board representation
   - Key operating metrics: revenue growth, EBITDA margin, customer/user counts, headcount, LTM trends
   - Material events: new rounds, management changes, M&A activity, regulatory developments
   - Expected hold period and path to exit (IPO pipeline, sponsor-to-sponsor, strategic)

6. **Assemble the LP report**
   - Cover letter from GP summarizing fund activity, market conditions, and outlook
   - Fund summary table: committed capital, drawn, distributed, NAV, net IRR, TVPI, DPI
   - Capital account statement per LP (or representative LP schedule)
   - Portfolio summary with individual company pages
   - Fee and expense disclosure
   - ESG / DEI reporting section if required by side letter or ILPA guidelines [VERIFY LP-specific reporting obligations]

## Output

- **Quarterly/Annual LP Report** formatted to ILPA Reporting Template standards or GP's custom template, including:
  - Fund-level financial summary and performance table
  - Individual capital account statements
  - Portfolio company detail pages with KPIs and valuation bridge
  - Cash flow summary (calls, distributions, net cash flow)
  - Fee and expense schedule
  - Benchmark comparison chart
- All figures should tie to the fund administrator's NAV statement with variance explanations for any differences

## Quality Checks

- NAV reconciliation: Ending NAV matches administrator statement within acceptable tolerance; all variances documented
- IRR validation: Cash flow dates are accurate, no duplicate entries, and IRR calculation converges (check for multiple IRR scenarios on unusual cash flow patterns)
- TVPI / DPI / RVPI arithmetic cross-checks: TVPI = DPI + RVPI
- Valuation support: Every portfolio company mark has a documented methodology and is no more than one quarter stale
- Waterfall accuracy: Carried interest and preferred return calculations follow LPA terms exactly [VERIFY specific waterfall structure — American vs. European style]
- Consistency: All figures in the report (cover letter, tables, capital accounts, portfolio pages) are internally consistent with no conflicting numbers
- Disclosure completeness: Side letter reporting obligations, ILPA best practices, and any regulatory requirements (e.g., Form PF data points) are addressed [VERIFY applicable regulatory filings]
