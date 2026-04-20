---
name: building-real-estate-pro-formas
language: en
description: Constructs property pro forma models with rent roll analysis, expense projections, and cash flow forecasting. Use when building real estate models, projecting property cash flows, or analyzing investment returns.
tags:
  - modeling
  - real-estate-finance
  - investment
metadata:
  author: casemark
  practice_areas:
    - Real Estate Finance
    - REIT Analysis
    - Property Investment
  document_types:
    - Model
  skill_modes:
    - Modeling
---
# Building Real Estate Pro Formas

Constructs property pro forma models with rent roll analysis, expense projections, and cash flow forecasting.

## When To Use

- Underwriting an acquisition or disposition of income-producing property
- Modeling a development or value-add repositioning from ground-up or renovation budget through stabilization
- Preparing annual asset-management budgets or reforecasts for an existing portfolio asset
- Evaluating refinancing scenarios by stress-testing debt service coverage
- Supporting REIT-level NAV or FFO/AFFO analysis that rolls up individual property cash flows

## Inputs To Gather

- **Rent roll**: Unit-level or tenant-level detail — tenant name, suite/unit, SF or unit count, lease start/end, base rent (per SF or per unit), escalation schedule, renewal probability, free-rent or abatement periods
- **Market data**: Comparable rents, vacancy rates, absorption trends, and cap rate benchmarks for the submarket [VERIFY — source CoStar, CBRE, or local broker comps]
- **Operating expenses**: Historical T-12 or T-3 actuals broken out by line item (property taxes, insurance, utilities, R&M, management fees, payroll, G&A, contract services)
- **Capital expenditure plan**: Near-term capex reserves, tenant improvement allowances (TI), leasing commissions (LC), and any deferred maintenance or renovation budget
- **Financing terms**: Loan amount or LTV, interest rate (fixed/floating), amortization period, IO period, term, prepayment provisions, debt covenants (DSCR floors, LTV caps)
- **Hold period and exit assumptions**: Projected hold (typically 5–10 years), exit cap rate, disposition costs (brokerage, transfer tax)
- **Tax and entity structure**: Property tax assessment schedule, depreciation method (27.5 yr residential / 39 yr commercial), any tax abatement or PILOT [VERIFY — jurisdiction-specific]

## Workflow

1. **Build the revenue module**
   - Lay out each lease on a unit-by-unit or tenant-by-tenant basis across the projection period
   - Apply contractual escalations (fixed bumps, CPI-linked, or percentage rent)
   - Model lease expirations: assign renewal probability and downtime assumptions; re-lease at projected market rent
   - Calculate gross potential rent (GPR), then deduct vacancy and credit loss (typically 3–10% depending on asset class and market) [VERIFY — market-specific vacancy]
   - Add ancillary income: parking, laundry, storage, expense recoveries (CAM/NNN reimbursements), percentage rent overages

2. **Build the expense module**
   - Start from the T-12 actuals; inflate each line item at an appropriate growth rate (general inflation for most; separate escalator for property taxes and insurance)
   - Management fee: typically 3–5% of EGI for institutional assets [VERIFY — per management agreement]
   - Replacement reserves: $150–$300/unit for multifamily or $0.15–$0.30/SF for commercial [VERIFY — lender/investor requirements]
   - Net operating income (NOI) = Effective Gross Income minus total operating expenses

3. **Build the capital and TI/LC module**
   - Schedule tenant improvement allowances and leasing commissions at each lease rollover
   - Include any renovation or repositioning capex phased by quarter or year
   - Separate "above-the-line" capex (capitalized into basis) from operating expense repairs

4. **Build the financing module**
   - Model debt service: monthly P&I during amortizing periods, IO payments during interest-only periods
   - Calculate DSCR (NOI / annual debt service) each year; flag any year where DSCR falls below covenant threshold (commonly 1.20–1.25x)
   - If floating-rate, show base-case rate path plus stressed scenarios (+100 bps, +200 bps)

5. **Calculate return metrics**
   - Unlevered cash flow = NOI minus capex/TI/LC
   - Levered cash flow = Unlevered cash flow minus debt service
   - Exit value = forward NOI / exit cap rate, less disposition costs
   - Equity waterfall: preferred return, catch-up, and promote splits if applicable
   - Compute IRR, equity multiple, cash-on-cash yield, and average annual return for both unlevered and levered scenarios

6. **Run sensitivity and scenario analysis**
   - Sensitivity table on exit cap rate vs. rent growth (or vacancy)
   - Downside scenario: higher vacancy, slower rent growth, cap rate expansion
   - Upside scenario: faster lease-up, above-market escalations, cap rate compression
   - Break-even analysis: identify occupancy or rent level at which DSCR = 1.0x or IRR = 0%

## Output

- **Summary page**: Property name, address, asset class, SF/units, acquisition price, going-in cap rate, stabilized yield, target IRR/equity multiple
- **Annual cash flow projection** (typically 5–10 year hold): GPR, vacancy, EGI, operating expenses by category, NOI, capex/TI/LC, unlevered cash flow, debt service, levered cash flow
- **Return metrics table**: Unlevered IRR, levered IRR, equity multiple, cash-on-cash by year, peak equity outstanding
- **Sensitivity matrix**: Two-variable table (e.g., exit cap rate x rent growth) showing IRR and equity multiple at each intersection
- **Key assumptions schedule**: Clearly list every assumption — growth rates, vacancy, cap rates, financing terms, TI/LC per SF — with source or basis noted
- **Footnotes and flags**: Mark any assumption lacking market support with [VERIFY]; note where historical data was extrapolated

## Quality Checks

- **NOI sanity check**: Compare modeled NOI margin to submarket benchmarks; multifamily typically 55–70%, office 60–75% of EGI [VERIFY — asset class and market]
- **Cap rate cross-check**: Going-in cap rate should align with recent comparable transactions; flag divergence >25 bps
- **DSCR covenant compliance**: Confirm no year breaches the lender's minimum DSCR; if it does, note the shortfall and potential cash sweep or reserve trigger
- **Rent growth reasonableness**: Projected rent escalation should not materially exceed historical submarket CAGR without explicit justification
- **Expense ratio consistency**: Total opex as % of EGI should be stable year-over-year absent a known structural change
- **IRR back-check**: Reverse-engineer the exit price implied by the target IRR; confirm it implies a realistic exit cap rate
- **Unit economics**: Per-unit or per-SF revenue and expense figures should fall within market ranges; outliers need annotation
- **Circular reference check**: Ensure no unresolved circularity between debt sizing, equity, and return calculations
