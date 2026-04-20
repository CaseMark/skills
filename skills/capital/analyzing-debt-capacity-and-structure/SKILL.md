---
name: analyzing-debt-capacity-and-structure
language: en
description: Evaluates target leverage capacity with cash flow coverage, stress testing, and optimal debt structure across term loans, revolver, and mezzanine. Use when analyzing debt capacity, structuring acquisition financing, or stress testing leverage.
tags:
  - analysis
  - private-equity
metadata:
  author: casemark
  practice_areas:
    - Private Equity
    - Leveraged Buyouts
    - Growth Equity
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Debt Capacity And Structure

Evaluates target leverage capacity with cash flow coverage, stress testing, and optimal debt structure across term loans, revolver, and mezzanine.

## When To Use

- Sizing acquisition debt for an LBO or growth equity recapitalization
- Evaluating how much leverage a target's cash flows can support under base and downside scenarios
- Structuring a multi-tranche debt package (senior term loan, revolver, second lien, mezzanine/sub debt)
- Stress testing an existing or proposed capital structure against covenant thresholds
- Preparing debt-capacity sections for investment committee memos or lender presentations

## Inputs To Gather

- **Historical financials**: 3-5 years of revenue, EBITDA, capex, working capital changes, and debt service history
- **Management projections or model**: Base-case P&L and cash flow forecast (minimum 5-year horizon)
- **Existing debt terms**: Outstanding balances, maturities, pricing, amortization schedules, and covenant packages
- **Comparable transaction leverage data**: Leverage multiples, pricing, and structures from recent precedent deals in the sector
- **Lender feedback** (if available): Indicative terms, hold sizes, or commitment letters
- **Asset base detail**: If asset-based lending is relevant — AR, inventory, PP&E appraisals
- **Sponsor equity check size and target returns**: Required IRR/MOIC driving the leverage need

## Workflow

1. **Normalize EBITDA and free cash flow**
   - Adjust for non-recurring items, run-rate synergies (haircut aggressively), and pro-forma cost structure
   - Calculate unlevered free cash flow (EBITDA − cash taxes − capex − change in NWC) as the base debt-service pool
   - Flag any add-backs exceeding 15-20% of reported EBITDA as [VERIFY] items for diligence

2. **Determine maximum leverage capacity**
   - Apply sector-appropriate leverage ceilings: Total Debt / EBITDA, Senior Debt / EBITDA, Net Debt / EBITDA
   - Cross-check against fixed charge coverage ratio (FCCR ≥ 1.0-1.2x) and debt service coverage ratio (DSCR ≥ 1.5-2.0x) [VERIFY — lender-specific minimums vary]
   - Benchmark against precedent transaction leverage for the sub-sector and credit-quality tier

3. **Structure the debt tranches**
   - **Revolver**: Size to cover seasonal working capital swings plus a liquidity cushion (typically 1.0-1.5x peak seasonal draw); confirm borrowing base if ABL
   - **Senior term loan (TLA/TLB)**: Size based on senior leverage target (typically 3.0-5.0x for middle-market; up to 6.0x+ for large-cap) [VERIFY — market-dependent]; set amortization (1-5% p.a. for TLB, higher for TLA)
   - **Second lien / mezzanine / sub debt**: Layer in to bridge the gap between senior capacity and total leverage need; note pricing step-up (typically 300-600 bps over first lien) and PIK toggle structures
   - **Seller notes or earnouts**: Consider as quasi-debt capacity if terms are favorable and subordination is clear

4. **Run stress tests and downside scenarios**
   - Revenue decline case: Model 10-20% revenue shortfall in Year 1-2 and check covenant headroom
   - Margin compression case: EBITDA margins contract 200-500 bps from base case
   - Combined downside: Simultaneous revenue miss + margin compression + capex overrun
   - For each scenario, calculate: leverage ratchet compliance, FCCR/DSCR, cash balance trajectory, and revolver availability
   - Identify the break-even EBITDA at which the capital structure triggers a covenant default

5. **Assess covenant package and structural protections**
   - Map financial maintenance covenants (leverage ratio, FCCR, minimum liquidity) against projected performance with cushion analysis (target ≥15-25% headroom)
   - Review incurrence covenants for permitted debt, restricted payments, and lien baskets
   - Evaluate call protection, prepayment penalties, and refinancing flexibility
   - Note any springing covenants or reclassification triggers [VERIFY — document-specific]

6. **Summarize optimal structure and recommendations**
   - Present recommended debt quantum by tranche with blended cost of debt
   - Show leverage walk: Entry leverage → Year 1 → Year 3 → Exit, with deleveraging trajectory
   - Highlight key risks and mitigants (cyclicality, customer concentration, capex lumpiness)
   - Provide sensitivity table: EBITDA vs. leverage multiple showing debt capacity range

## Output

- **Debt capacity summary table**: Maximum supportable debt by tranche, leverage multiples, coverage ratios at entry
- **Sources and uses**: Full capital structure with equity check, rollover equity, and debt breakdown
- **Stress test matrix**: Base, downside, and severe downside scenarios with key coverage and liquidity metrics per year
- **Covenant compliance dashboard**: Projected covenant metrics vs. thresholds with headroom percentages
- **Recommendation narrative**: 1-2 page summary of recommended structure, key sensitivities, and open diligence items

## Quality Checks

- EBITDA add-backs are individually justified and sourced — no unsubstantiated management adjustments
- Leverage multiples are cross-referenced against at least 3 comparable precedent transactions
- Stress tests produce a clear break-even EBITDA level, not just directional commentary
- Coverage ratios are calculated on a cash (not accrual) basis, with capex treated as a real cash outflow
- All lender-specific covenant thresholds and market-dependent pricing assumptions are marked [VERIFY]
- Debt maturity profile avoids concentration — no single year with >40% of total debt maturing
- Blended cost of debt is internally consistent with tranche-level pricing and fees
