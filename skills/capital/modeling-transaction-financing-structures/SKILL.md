---
name: modeling-transaction-financing-structures
description: Constructs acquisition financing models with debt capacity, leverage analysis, coverage ratios, and capital structure optimization. Use when modeling deal financing, analyzing leverage capacity, or structuring acquisition debt.
tags:
  - modeling
  - mergers-and-acquisitions
metadata:
  author: casemark
  practice_areas:
    - M&A Advisory
    - Corporate Development
    - Investment Banking
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Transaction Financing Structures

## When To Use

- Structuring the debt/equity mix for a proposed acquisition
- Sizing debt capacity against a target's cash flow profile
- Evaluating leverage scenarios (e.g., senior secured vs. mezzanine vs. seller note)
- Stress-testing covenant headroom under downside operating cases
- Comparing financing alternatives for a management presentation or lender pitch

## Inputs To Gather

- **Target financials**: 3–5 years of historical revenue, EBITDA, capex, working capital, and existing debt schedules
- **Transaction terms**: Enterprise value or equity value, assumed purchase price multiples, transaction fees and expenses
- **Debt term sheets or indicative terms**: Pricing (spread, OID), tenor, amortization schedule, commitment fees, call protection
- **Tranche structure**: Revolver size, term loan A/B splits, high-yield or mezzanine layers, any seller financing or earnouts
- **Covenant package**: Maximum leverage ratio, minimum interest/fixed-charge coverage, restricted payments basket, excess cash flow sweep percentages
- **Equity contribution**: Sponsor equity check, rollover equity from management or seller, any co-invest or preferred equity
- **Operating projections**: Management case and at least one downside case for the projection period (typically 5–7 years)

## Workflow

1. **Build the sources & uses table**
   - Purchase price (equity value + net debt adjustment + transaction expenses)
   - Sources: each debt tranche at par, equity contribution, any rollover or seller paper
   - Confirm sources = uses to the penny; flag any funding gap immediately

2. **Construct the debt schedule**
   - For each tranche: opening balance, mandatory amortization, optional prepayments (from excess cash flow sweeps), and closing balance
   - Model revolver draws/repayments based on minimum cash balance assumptions
   - Calculate cash interest, PIK interest, and commitment fees separately
   - Track call premiums or prepayment penalties if applicable

3. **Calculate credit metrics on a quarterly and annual basis**
   - Total Debt / EBITDA (gross and net of cash)
   - Senior Secured Debt / EBITDA
   - Interest Coverage Ratio (EBITDA / Cash Interest Expense)
   - Fixed Charge Coverage Ratio (EBITDA − Capex − Taxes − Distributions) / (Cash Interest + Mandatory Amortization)
   - Debt / Total Capitalization
   - [VERIFY] Confirm the exact EBITDA definition per the credit agreement — addbacks for run-rate synergies, one-time costs, and stock-based compensation vary by deal

4. **Run covenant compliance tests**
   - Map each projected period against maintenance covenant thresholds
   - Flag any period where headroom falls below 10–15% of the covenant level
   - In the downside case, identify the first period of potential covenant breach and quantify the EBITDA shortfall required to trip

5. **Optimize the capital structure**
   - Compare blended cost of capital (WACC) across 2–3 alternative structures (e.g., higher leverage/lower equity vs. conservative structure)
   - Sensitize sponsor IRR to leverage level, holding entry multiple constant
   - Evaluate trade-offs: lower leverage = wider covenant cushion but lower equity returns; higher leverage = tighter cushion but higher returns
   - Consider refinancing scenarios at Year 2–3 if rate environment or credit profile improves

6. **Sensitize key outputs**
   - Leverage and coverage ratios vs. EBITDA growth assumptions (±5%, ±10%)
   - Sponsor IRR vs. exit multiple (±0.5x turns) and leverage level
   - Debt paydown timeline vs. excess cash flow sweep percentage (50%, 75%, 100%)
   - Covenant headroom vs. working capital swings or capex overruns

## Output

- **Sources & Uses summary** — single-page table with all funding components
- **Debt schedule** — annual (and optionally quarterly) balances, interest, amortization, and fees by tranche
- **Credit metrics dashboard** — leverage, coverage, and capitalization ratios across the projection period for base and downside cases
- **Covenant compliance matrix** — pass/fail by period with headroom percentages
- **Capital structure comparison** — side-by-side of 2–3 structures showing WACC, IRR, covenant cushion, and paydown speed
- **Sensitivity tables** — IRR vs. exit multiple/leverage; leverage ratio vs. EBITDA growth; coverage vs. capex variance

## Quality Checks

- Sources exactly equal uses — no rounding gaps
- Debt balances tie to the balance sheet; interest expense ties to the income statement and cash flow statement
- Revolver balance never exceeds committed facility size and never goes negative
- Leverage ratios at close match the term sheet (e.g., 4.0x senior, 5.5x total)
- [VERIFY] EBITDA adjustments match the credit agreement definition, not the management presentation definition
- Excess cash flow sweep calculation uses the contractual formula (not a simplified approximation)
- Downside case reflects a realistic stress (e.g., revenue decline of 10–15%, margin compression of 200–300 bps) rather than an arbitrary haircut
- All interest rate assumptions are internally consistent (SOFR base + spread, with floor if applicable)
- [VERIFY] Confirm any intercreditor subordination terms that affect payment waterfall priority
- Model is auditable: every hardcoded assumption is labeled, color-coded, and sourced
