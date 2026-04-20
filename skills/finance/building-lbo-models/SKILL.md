---
name: building-lbo-models
language: en
description: Constructs leveraged buyout models with debt capacity, returns analysis, and exit scenarios. Use when modeling LBOs, calculating sponsor returns, or analyzing leveraged transactions.
tags:
  - modeling
  - investment-banking
metadata:
  author: casemark
  practice_areas:
    - Investment Banking
    - Mergers and Acquisitions
    - Corporate Finance
  document_types:
    - Model
  skill_modes:
    - Modeling
---
# Building LBO Models

## When To Use

- Modeling a financial sponsor's acquisition of a target company using significant debt financing
- Evaluating debt capacity, optimal capital structure, and leverage multiples for a buyout
- Calculating sponsor IRR and MOIC under base, upside, and downside scenarios
- Stress-testing exit assumptions (timing, multiple, and method) to assess risk-adjusted returns
- Comparing LBO returns across multiple potential acquisition targets or bid levels

## Inputs To Gather

- **Target financials**: Historical income statement (3–5 years), balance sheet, and cash flow statement; latest available LTM figures
- **Transaction assumptions**: Purchase price or entry EV/EBITDA multiple, transaction fees (advisory, financing, legal — typically 2–4% of TEV), minimum cash balance
- **Debt structure**: Tranches (revolver, Term Loan A/B, senior notes, subordinated/mezzanine, seller note), interest rates (fixed vs. floating + spread), amortization schedules, mandatory vs. optional prepayment terms, commitment fees
- **Operating projections**: Revenue growth rates, EBITDA margin trajectory, capex (maintenance vs. growth), working capital assumptions (days sales outstanding, days payable outstanding, days inventory outstanding)
- **Exit assumptions**: Holding period (typically 3–7 years), exit EV/EBITDA multiple, potential dividend recaps or partial exits
- **Sponsor parameters**: Target equity check size, fund return hurdles (e.g., 20%+ IRR, 2.5x+ MOIC), management rollover percentage

## Workflow

1. **Build the Sources & Uses table**
   - Sources: equity contribution, each debt tranche, any rollover equity or seller financing
   - Uses: equity purchase price, transaction fees, debt issuance costs, refinanced existing debt
   - Verify sources = uses; if they don't balance, recheck assumptions before proceeding

2. **Construct the operating model**
   - Project revenue, EBITDA, EBIT, and unlevered free cash flow over the hold period
   - Model working capital changes using historical days metrics, not flat percentages
   - Separate maintenance capex (tied to D&A) from growth capex (tied to revenue expansion)
   - Calculate tax using effective rate; flag any NOL carryforwards or tax shield assumptions [VERIFY]

3. **Build the debt schedule**
   - For each tranche: beginning balance → mandatory amortization → cash sweep (if applicable) → optional prepayment → ending balance
   - Calculate interest expense per tranche (apply SOFR + spread for floating-rate debt [VERIFY current benchmark rate])
   - Model revolver draws/repayments based on cash flow shortfalls; track commitment fees on undrawn amounts
   - Enforce leverage covenant tests (e.g., Total Debt / EBITDA ≤ 6.0x) and flag covenant breaches

4. **Calculate returns at exit**
   - Apply exit multiple to projected EBITDA at each potential exit year
   - Subtract net debt at exit to derive equity value to sponsor
   - Compute IRR and MOIC on total invested equity (including any add-on investments)
   - Model dividend recaps separately if applicable — show returns with and without recap

5. **Run sensitivity and scenario analysis**
   - Build two-way data tables: entry multiple vs. exit multiple, EBITDA growth vs. leverage
   - Stress-test downside: revenue decline of 10–20%, margin compression of 100–300 bps, one-year exit delay
   - Test debt paydown scenarios: aggressive vs. minimum mandatory amortization
   - Identify the breakeven entry multiple at which the sponsor achieves its minimum return hurdle

6. **Assess credit metrics and debt capacity**
   - Track Total Debt / EBITDA, Senior Debt / EBITDA, Interest Coverage (EBITDA / Interest), and Fixed Charge Coverage through each projection year
   - Compare against typical market thresholds (e.g., senior leverage ≤ 4.0x, total leverage ≤ 6.0x [VERIFY against current credit market conditions])
   - Confirm the business generates sufficient FCF for mandatory debt service in all scenarios

## Output

- **Sources & Uses summary** with clearly labeled equity and debt components
- **5-year operating projection** with revenue, EBITDA, unlevered FCF, and key margins
- **Debt schedule** showing balance, interest, and amortization for each tranche by year
- **Returns matrix**: IRR and MOIC at various exit multiples and exit years
- **Sensitivity tables**: Entry price vs. returns, EBITDA growth vs. leverage, exit timing vs. returns
- **Credit metrics dashboard**: Leverage ratios, coverage ratios, and covenant compliance by year
- **Key assumptions page** listing every material input with source or [VERIFY] flag

## Quality Checks

- Sources & Uses must balance to zero — no rounding gaps
- Ending cash balance never goes negative in any scenario; if it does, the revolver must draw or the model is broken
- Debt balances decline monotonically unless add-on acquisitions are modeled
- IRR and MOIC are internally consistent (a 2.0x MOIC over 5 years ≈ 15% IRR)
- Exit equity value must equal entry equity plus cumulative FCF to equity minus distributions (cash flow identity check)
- Interest expense ties exactly to average debt balances and stated rates — no hardcoded interest figures
- Circular reference handling: if using iterative calculations for cash sweeps, document the approach and confirm convergence
- All market-dependent assumptions (multiples, rates, leverage thresholds) are tagged [VERIFY] with date of last validation
