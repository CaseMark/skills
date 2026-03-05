---
name: modeling-debt-capacity-analysis
description: Calculates borrower debt capacity with cash flow coverage, leverage multiples, and stress-tested servicing ability. Use when sizing debt facilities, analyzing leverage capacity, or determining optimal capital structure.
tags:
  - modeling
  - debt-capital-markets
metadata:
  author: casemark
  practice_areas:
    - DCM
    - Leveraged Finance
    - Debt Origination
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Debt Capacity Analysis

## When To Use

- Sizing a new term loan, revolver, or bond issuance for a corporate or sponsor-backed borrower
- Evaluating how much incremental leverage a borrower can support for an acquisition or recapitalization
- Stress-testing an existing capital structure ahead of a refinancing or covenant amendment
- Providing lender-side analysis of maximum supportable debt in a credit approval process
- Comparing debt capacity across capital structure alternatives (senior secured vs. unsecured, fixed vs. floating)

## Inputs To Gather

- **Historical financials** — 3 years minimum of income statement, balance sheet, and cash flow statement
- **Management projections** — Base-case revenue, EBITDA, and capex forecasts for the projection period (typically 5–7 years)
- **Existing debt schedule** — All outstanding obligations with maturity dates, interest rates, amortization terms, and covenant packages
- **Industry comps** — Leverage multiples (Total Debt / EBITDA, Senior Debt / EBITDA) and coverage ratios for comparable credits [VERIFY: confirm peer set and data source recency]
- **Applicable credit agreement terms** — Permitted indebtedness baskets, restricted payment capacity, EBITDA add-back definitions, and financial maintenance covenants
- **Tax rate and NOL schedule** — Effective tax rate and any available tax shield carryforwards
- **Interest rate assumptions** — Current reference rate (SOFR, etc.), applicable credit spread, and floor if any [VERIFY: confirm current benchmark rate]

## Workflow

1. **Normalize EBITDA**
   - Start from reported EBITDA; apply recurring add-backs (stock-based comp, non-recurring restructuring, run-rate synergies with haircut)
   - Reconcile against credit agreement EBITDA definition if an existing facility is in place
   - Flag any add-back exceeding 15–20% of reported EBITDA for scrutiny

2. **Calculate free cash flow available for debt service**
   - EBITDA less cash taxes, maintenance capex, cash interest, and required working capital investment
   - Exclude growth capex and discretionary items to isolate mandatory cash obligations
   - Derive unlevered free cash flow (pre-interest) and levered free cash flow (post-interest) separately

3. **Apply leverage capacity constraints**
   - **Coverage-based**: Set minimum DSCR (typically 1.20–1.50x for investment grade; 1.00–1.20x for leveraged) and solve for maximum debt service, then back into principal
   - **Multiple-based**: Apply market-clearing leverage multiples (e.g., 4.0–6.0x Total Debt / EBITDA for leveraged credits) to normalized EBITDA [VERIFY: current market leverage multiples for the relevant sector and rating tier]
   - **Amortization-based**: Model mandatory amortization (typically 1–5% p.a. for term loans) and ensure cash flow covers scheduled principal plus interest
   - Take the **minimum** of the three approaches as the binding constraint

4. **Build the debt capacity waterfall**
   - Senior secured tranche: sized first, at lowest leverage multiple (e.g., 3.0–4.0x)
   - Second lien / mezzanine: incremental capacity between senior ceiling and total leverage cap
   - Unsecured or subordinated: residual capacity if total leverage headroom permits
   - Sum tranches to arrive at total debt capacity; compare against equity check and LTV constraints if applicable

5. **Stress-test under downside scenarios**
   - Revenue decline case: typically –10% to –25% from base, depending on industry cyclicality
   - Margin compression case: EBITDA margin reduction of 200–500 bps
   - Interest rate shock: +200–300 bps on floating-rate tranches
   - Combined stress: revenue decline plus rate increase simultaneously
   - For each scenario, verify that DSCR stays above 1.0x and leverage stays within covenant thresholds through the projection period

6. **Sensitivity tables**
   - 2-variable tables: debt capacity as a function of (a) EBITDA level vs. leverage multiple, (b) interest rate vs. DSCR floor
   - Highlight breakeven points where covenants would trip or cash flow turns negative

## Output

- **Debt capacity summary table**: Maximum supportable debt by tranche (senior, sub, total) with corresponding leverage multiples and coverage ratios
- **Cash flow waterfall**: Annual projection showing EBITDA → cash taxes → capex → interest → amortization → free cash flow surplus/deficit
- **Covenant compliance matrix**: Projected leverage and coverage ratios vs. covenant thresholds across base and stress cases
- **Sensitivity grids**: Debt capacity under varying EBITDA, rate, and margin assumptions
- **Key assumptions register**: Documented inputs, sources, and any items marked [VERIFY]

## Quality Checks

- Confirm EBITDA adjustments reconcile to audited financials or management bridge — no unexplained gaps
- Verify interest expense is calculated on average debt balances (not period-end) with correct day-count convention
- Ensure amortization schedules sum to stated maturity amounts and cash sweep mechanics are modeled if applicable
- Check that downside stress scenarios produce DSCR below base case — if not, the stress is too mild
- Cross-check leverage multiples against recent comparable transactions and rating agency benchmarks [VERIFY: source and date of comp data]
- Validate that the binding constraint is clearly identified and that no tranche exceeds its individual sizing cap
- Confirm all circular references (interest ↔ debt balance ↔ cash sweep) are resolved via iteration or macro
