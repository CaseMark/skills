---
name: building-restructuring-plan-models
language: en
description: Constructs plan of reorganization models with debt-for-equity conversion, new money injection, and emergence capital structure. Use when modeling restructuring plans, designing emergence capital structures, or analyzing plan feasibility.
tags:
  - modeling
  - distressed-and-restructuring
metadata:
  author: casemark
  practice_areas:
    - Restructuring
    - Distressed Investing
    - Turnaround
  document_types:
    - Model
  skill_modes:
    - Modeling
---
# Building Restructuring Plan Models

## When To Use

- Modeling a Chapter 11 plan of reorganization or out-of-court exchange offer
- Designing the emergence capital structure (debt/equity split post-restructuring)
- Analyzing creditor recovery waterfalls under competing plan proposals
- Evaluating debt-for-equity conversion ratios and new money injection terms
- Testing plan feasibility against projected cash flows and coverage covenants

## Inputs To Gather

- **Pre-petition capital structure**: All tranches of debt (revolver, term loans, bonds, mezz, sub debt) with face values, accrued interest, maturity dates, coupon rates, and security/priority
- **Claims register or estimated claims**: Administrative claims, priority claims, secured claims, unsecured claims, intercompany claims, equity interests
- **Enterprise valuation**: Reorganization value (DCF, comparable company, precedent transactions) with low/mid/high range
- **Projected financials**: 3–5 year post-emergence revenue, EBITDA, capex, working capital, and free cash flow projections
- **Plan term sheet**: Proposed treatment of each class — reinstatement, paydown, debt-for-equity swap, rights offering, new money terms
- **New money details**: DIP-to-exit conversion terms, rights offering size and backstop, exit facility commitments, fees
- **Tax attributes**: NOL carryforwards, Section 382 limitations, cancellation-of-debt income estimates [VERIFY against debtor's tax advisors]

## Workflow

1. **Map the pre-petition capital structure**
   - List each tranche with principal, accrued/unpaid interest, applicable premiums, and priority ranking
   - Identify the fulcrum security (tranche where value breaks) based on enterprise valuation range
   - Calculate total allowed claims per class including make-whole or prepayment penalties [VERIFY claim allowance assumptions with counsel]

2. **Build the recovery waterfall**
   - Allocate reorganization value top-down by absolute priority: administrative → secured → unsecured → equity
   - For each class, compute recovery as percentage of allowed claim
   - Model alternative distributions if the plan proposes deviations from absolute priority (cramdown scenarios) [VERIFY cramdown requirements under Section 1129(b)]

3. **Model debt-for-equity conversion**
   - Define conversion mechanics: what percentage of new equity each converting class receives
   - Calculate implied equity value per share at emergence based on reorganization value minus new exit debt
   - Compute dilution from management incentive plan (MIP), typically 5–15% of emergence equity, with strike prices and vesting
   - Show pre- and post-dilution ownership tables for all stakeholder classes

4. **Structure new money and exit facilities**
   - Model rights offering: size, subscription price (discount to plan equity value), backstop commitment fee, and resulting pro forma ownership
   - Build exit facility assumptions: revolver size, term loan tranches, coupon (fixed vs. floating), amortization schedule, maturity
   - Calculate total emergence debt and resulting credit metrics: Total Debt/EBITDA, Net Debt/EBITDA, Interest Coverage, Fixed Charge Coverage
   - Benchmark emergence leverage against comparable restructurings in the sector

5. **Run feasibility and sensitivity analysis**
   - Project debt service (interest + mandatory amortization) against free cash flow for 3–5 years post-emergence
   - Test the "feasibility" standard: confirm the reorganized entity is not likely to require further restructuring [VERIFY Section 1129(a)(11) feasibility requirements]
   - Run sensitivities on enterprise value (±10–20%), EBITDA margins, revenue growth, and exit multiples
   - Show recovery sensitivity tables for each class across valuation scenarios

6. **Compile plan comparison (if applicable)**
   - If multiple competing plans, build side-by-side recovery comparison
   - Highlight key differences: implied equity value, creditor recoveries, governance terms, timeline to emergence
   - Flag which classes are impaired and expected to vote for/against each plan

## Output

- **Emergence capital structure summary**: Table showing each tranche of exit debt and equity, with amounts, rates, maturities, and key terms
- **Creditor recovery waterfall**: Class-by-class recovery percentages at low/mid/high valuations
- **Ownership table**: Pro forma equity ownership at emergence — converting creditors, new money investors, MIP reserve, existing equity (if any recovery)
- **Credit metrics dashboard**: Emergence leverage, coverage ratios, and liquidity position
- **Sensitivity tables**: Recovery and leverage sensitivities across valuation and operating scenarios
- **Feasibility check**: Cash flow vs. debt service projection confirming plan viability

## Quality Checks

- Confirm total distributed value (debt + equity + cash) equals reorganization value — no value leakage
- Verify recovery waterfall respects absolute priority unless cramdown is explicitly modeled and justified
- Cross-check emergence leverage against sector norms and lender underwriting thresholds (typically 3.0–5.0x Total Debt/EBITDA)
- Ensure MIP dilution is applied consistently across all ownership calculations
- Validate that rights offering proceeds plus exit facility commitments cover all cash-pay claims and emergence liquidity needs
- Confirm NOL/tax attribute treatment is flagged for specialist review [VERIFY Section 382 limitation calculations]
- Test that model balances: sources of funds (new debt + new equity + asset value) = uses of funds (claim payments + fees + cash to balance sheet)
