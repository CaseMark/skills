---
name: calculating-fund-performance-metrics
language: en
description: Computes fund performance with gross/net IRR, MOIC, DPI, RVPI, TVPI, PME, and direct alpha methodologies. Use when calculating fund performance, reconciling return metrics, or benchmarking against peer groups.
tags:
  - analysis
  - investor-relations-and-lp-reporting
metadata:
  author: casemark
  practice_areas:
    - Investor Relations
    - LP Reporting
    - Fund Administration
  document_types:
    - Calculation Worksheet
  skill_modes:
    - Calculation
---
# Calculating Fund Performance Metrics

## When To Use

- Preparing quarterly or annual LP performance reports requiring IRR, MOIC, and multiple-based metrics
- Reconciling gross vs. net return figures across portfolio companies or fund segments
- Benchmarking fund returns against public market equivalents (PME) or peer group composites
- Responding to LP due diligence requests that require auditable performance calculations
- Validating administrator-produced performance figures before distribution

## Inputs To Gather

- **Cash flow schedule**: Date-stamped capital calls (drawdowns) and distributions for each LP and the fund overall, including recallable distributions if applicable
- **NAV / residual values**: Most recent fair market value of unrealized holdings, broken out by portfolio company; confirm valuation date and methodology (ASC 820 / IPEV guidelines) [VERIFY]
- **Fee and carry structure**: Management fee rate, fee basis (committed vs. invested capital), catch-up percentage, carried interest rate, preferred return / hurdle rate, GP clawback terms
- **Benchmark index data**: Total-return index series (e.g., S&P 500 TR, Russell 2000 TR, MSCI World) aligned to fund cash flow dates for PME and direct alpha calculations
- **Fund terms**: Vintage year, commitment period end date, fund term, any recycling provisions that affect DPI/RVPI interpretation
- **FX rates** (if multi-currency): Spot rates at each cash flow date and reporting date

## Workflow

1. **Validate the cash flow ledger**
   - Confirm every capital call and distribution has a settlement date (not just call/notice date)
   - Reconcile total called capital against the capital account statement
   - Flag any netting of calls against distributions on the same date — separate them for IRR accuracy

2. **Calculate gross return metrics (deal-level)**
   - **Gross IRR**: XIRR across deal-level cash flows (cost basis in, proceeds + remaining FMV out). Use actual dates; do not approximate with quarterly periods
   - **Gross MOIC**: (Realized proceeds + Unrealized FMV) / Total invested cost
   - If partial realizations exist, split realized vs. unrealized MOIC components

3. **Calculate net return metrics (fund-level)**
   - Build a net cash flow series: LP contributions (capital calls including fees) as outflows, LP distributions as inflows, ending NAV (net of accrued carry and expenses) as terminal inflow
   - **Net IRR**: XIRR on the net LP cash flow series
   - **Net MOIC**: (Cumulative distributions + Net NAV) / Cumulative contributions
   - **DPI** (Distributions to Paid-In): Cumulative distributions / Cumulative contributions
   - **RVPI** (Residual Value to Paid-In): Net NAV / Cumulative contributions
   - **TVPI** (Total Value to Paid-In): DPI + RVPI (cross-check: must equal Net MOIC)

4. **Compute public market equivalent (PME) metrics**
   - **Kaplan-Schoar PME (KS-PME)**: Compound each fund cash flow at the benchmark index return to the reporting date. KS-PME = FV of distributions / FV of contributions. Value > 1.0 indicates outperformance
   - **Direct Alpha**: Discount/compound all fund cash flows at benchmark returns; compute IRR on the residual series. The resulting rate is the annualized excess return over the index
   - **PME+ (Long-Nickels)**: Scale distributions by a factor λ so that the NAV of the hypothetical public investment equals the fund's residual NAV; compute IRR on the scaled series [VERIFY methodology variant if LP has a preferred convention]

5. **Perform reasonableness and cross-checks**
   - TVPI must equal DPI + RVPI within rounding tolerance
   - Net IRR must be lower than gross IRR (if not, investigate fee/carry application)
   - For mature funds (>75% DPI), RVPI should be a small fraction of TVPI
   - Compare IRR to MOIC-implied return for the holding period — large divergence signals cash flow timing issues or J-curve distortion
   - Confirm KS-PME and direct alpha directionally agree on outperformance/underperformance

6. **Present results**
   - Organize into a calculation worksheet with clearly labeled sections: Gross Metrics, Net Metrics, PME/Benchmark Metrics
   - State the as-of date, benchmark index used, and NAV valuation date
   - Footnote any assumptions (e.g., "distributions assumed reinvested at index return for PME")

## Output

A structured calculation worksheet containing:

- **Gross metrics table**: Gross IRR, Gross MOIC (total / realized / unrealized) per deal and aggregate
- **Net metrics table**: Net IRR, Net MOIC, DPI, RVPI, TVPI at fund level (and by vintage or strategy segment if requested)
- **PME summary**: KS-PME ratio, direct alpha (annualized), benchmark used, observation period
- **Methodology notes**: IRR solver used (XIRR convention), valuation basis for unrealized, fee/carry netting approach
- **Reconciliation checks**: TVPI = DPI + RVPI confirmation, gross-to-net bridge summary

## Quality Checks

- IRR calculations use exact dates (XIRR), not period-approximated IRR, to avoid distortion from uneven cash flow timing
- Management fees are applied on the correct basis (committed capital during commitment period, invested capital thereafter) [VERIFY against LPA terms]
- Carried interest is computed net of preferred return and catch-up, consistent with the fund's distribution waterfall [VERIFY waterfall structure — American vs. European]
- PME index series is total-return (dividends reinvested), not price-only
- All metrics use the same as-of / valuation date — mixing dates across metrics invalidates comparisons
- If fund recycles distributions, DPI and TVPI may exceed typical ranges; note recycling impact explicitly
- Mark any input sourced from preliminary or unaudited financials with [VERIFY]
