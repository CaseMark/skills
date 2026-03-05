---
name: building-pe-fund-performance-reports
description: Constructs fund-level performance reporting with IRR, MOIC, DPI, RVPI, PME, and vintage year benchmarking. Use when building fund reports, calculating performance metrics, or preparing LP reporting packages.
tags:
  - modeling
  - private-equity
metadata:
  author: casemark
  practice_areas:
    - Private Equity
    - Leveraged Buyouts
    - Growth Equity
  document_types:
    - Model
  skill_modes:
    - Modeling
---
# Building Pe Fund Performance Reports

## When To Use

- Preparing quarterly or annual LP reporting packages with fund-level performance metrics
- Calculating IRR, MOIC, DPI, RVPI, or TVPI for a PE/growth equity fund
- Running Public Market Equivalent (PME) analysis against a benchmark index
- Benchmarking fund performance by vintage year against peer universes (Cambridge, Preqin, Burgiss)
- Responding to LP due diligence requests or ILPA-compliant reporting obligations
- Building GP-facing dashboards that roll up deal-level returns to fund-level aggregates

## Inputs To Gather

- **Cash flow schedule**: Date-stamped capital calls (drawdowns) and distributions for the fund, net of management fees and carried interest
- **NAV / residual value**: Most recent reported NAV with valuation date; confirm whether NAV is gross or net of carry/fees
- **Fund terms**: Vintage year, committed capital, investment period end date, fund term, fee structure (management fee rate, carry percentage, preferred return, GP catch-up)
- **Deal-level data** (if rolling up): Entry date, cost basis, realized proceeds, current fair value, and holding period per portfolio company
- **Benchmark reference**: Target benchmark index (e.g., S&P 500, Russell 2000, MSCI World) for PME; peer vintage year dataset source (Cambridge Associates, Preqin, Burgiss)
- **Reporting period**: As-of date and whether report covers inception-to-date, trailing period, or both

## Workflow

1. **Validate cash flow data**
   - Confirm all capital calls and distributions are net of fees/carry unless explicitly building gross metrics
   - Check that cash flow dates are sequential and complete — flag any gaps or duplicate entries
   - Reconcile total called capital against commitment amount; flag if called > committed

2. **Calculate core return metrics**
   - **Net IRR**: Compute using cash flow series (calls as negatives, distributions as positives) plus ending NAV as terminal value; use Newton-Raphson or bisection method; flag if multiple IRR solutions exist
   - **Gross IRR**: Repeat using pre-fee, pre-carry cash flows if GP reporting requires both
   - **MOIC (TVPI)**: (Total distributions + Residual value) / Total called capital
   - **DPI**: Total distributions / Total called capital (realized return measure)
   - **RVPI**: Residual value / Total called capital (unrealized return measure)
   - Confirm TVPI = DPI + RVPI as a cross-check

3. **Run PME analysis**
   - Select appropriate public index benchmark [VERIFY — confirm LP-agreed benchmark]
   - Apply Kaplan-Schoar PME: discount each cash flow by the corresponding index return from cash flow date to as-of date; PME > 1.0 indicates outperformance
   - Optionally compute Long-Nickels PME+ or Direct Alpha for a spread-based comparison
   - State index return source and total return vs. price return assumption

4. **Benchmark against vintage year peers**
   - Pull quartile breakpoints (upper quartile, median, lower quartile) from the selected peer dataset for the fund's vintage year
   - Plot fund IRR, MOIC, and DPI against peer quartiles
   - Note the peer universe size (n-count) and dataset date — stale benchmarks undercount recent performance [VERIFY — confirm benchmark data vintage]

5. **Build the LP report package**
   - **Fund summary page**: Fund name, vintage, committed capital, called %, invested %, key metrics (IRR, MOIC, DPI, RVPI, PME)
   - **Cash flow waterfall**: Period-by-period capital calls, distributions, and net cash flow with cumulative totals
   - **Portfolio company table**: Company name, sector, investment date, cost, fair value, realized proceeds, gross MOIC, status (realized/unrealized/partially realized)
   - **Vintage year benchmarking chart**: Quartile ranking visualization
   - **Valuation methodology note**: Basis for NAV (comparable transactions, public comps, DCF, third-party appraisal) with effective date

6. **Sensitize and stress-test**
   - Show IRR sensitivity to exit timing: what happens if NAV is realized 1–2 years earlier or later
   - Show MOIC sensitivity to residual value write-downs (e.g., NAV at 75%, 50%)
   - If fund is early (< 50% DPI), flag J-curve effect and note that IRR is heavily NAV-dependent

## Output

- Fund performance summary table with Net IRR, Gross IRR, MOIC, DPI, RVPI, and PME
- Cash flow schedule with cumulative called/distributed amounts
- Portfolio company roll-up with deal-level gross MOICs
- Vintage year benchmarking comparison (quartile placement)
- PME analysis with stated benchmark and methodology
- Sensitivity tables on IRR and MOIC under alternative exit/valuation scenarios
- Methodology notes and disclaimers

## Quality Checks

- **TVPI reconciliation**: Confirm TVPI = DPI + RVPI; any discrepancy indicates a data error
- **IRR reasonableness**: Cross-check IRR against MOIC and holding period — a 3.0x MOIC over 5 years should yield roughly 25% IRR, not 5% or 50%
- **Cash flow completeness**: Total capital called should not exceed committed capital; total distributions should tie to realized proceeds plus any recallable amounts
- **NAV consistency**: NAV used for RVPI and terminal IRR cash flow must match the stated valuation date; do not mix Q3 NAV with Q4 cash flows
- **Fee netting**: Confirm whether metrics are gross or net; never mix gross cash flows with net labels
- **PME index alignment**: Ensure index returns cover the full fund life from first cash flow to as-of date; gaps in index data will distort PME [VERIFY — confirm index data availability for full period]
- **Benchmark currency**: If fund reports in a non-USD currency, confirm peer benchmarks use the same currency or apply FX adjustment [VERIFY]
- **ILPA compliance**: If LP reporting, verify alignment with ILPA Reporting Template v3 standards for fee and expense disclosure [VERIFY — confirm ILPA version requirement]
