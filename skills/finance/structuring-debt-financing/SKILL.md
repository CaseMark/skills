---
name: structuring-debt-financing
description: Designs acquisition financing structures with leverage analysis, covenant negotiation, and capital structure optimization. Use when structuring deal financing, analyzing debt capacity, or negotiating loan terms.
tags:
  - investment-banking
metadata:
  author: casemark
  practice_areas:
    - Investment Banking
    - Mergers and Acquisitions
    - Corporate Finance
  document_types:
    - Report
  skill_modes:
    - Analysis
---
# Structuring Debt Financing

## When To Use

- Designing the debt component of an acquisition financing package (LBO, strategic M&A, take-private)
- Evaluating a target's debt capacity and optimal leverage ratio prior to a bid
- Negotiating term sheets or commitment letters with arranging banks
- Comparing financing alternatives (bank debt vs. high-yield bonds vs. mezzanine vs. unitranche)
- Stress-testing a proposed capital structure under downside operating scenarios
- Advising on covenant packages and intercreditor arrangements

## Inputs To Gather

- **Target financials**: 3–5 years of historical income statements, balance sheets, and cash flow statements; management projections or a base-case operating model
- **Transaction details**: enterprise value, equity contribution, assumed purchase multiple, closing timeline, any rollover equity or seller notes
- **Market context**: current benchmark rates (SOFR/Term SOFR), indicative spreads for comparable credits, recent comp financing packages in the sector
- **Credit metrics**: target leverage (Total Debt / EBITDA, Senior / EBITDA), interest coverage (EBITDA / Interest, EBITDA − Capex / Debt Service), fixed charge coverage
- **Sponsor/buyer requirements**: target equity IRR, minimum cash-on-cash return, dividend recapitalization flexibility, desired amortization schedule
- **Regulatory or rating constraints**: any investment-grade rating targets, Basel III/IV capital treatment for bank lenders, industry-specific leverage caps [VERIFY: sector-specific regulatory leverage limits vary by jurisdiction and industry]

## Workflow

1. **Assess debt capacity**
   - Calculate sustainable leverage from normalized EBITDA (adjusting for one-time items, synergies, run-rate cost saves)
   - Benchmark against precedent transactions in the same sector and credit-rating cohort
   - Run a downside case (typically 15–25% EBITDA decline) to confirm debt serviceability through a cycle
   - Identify maximum total leverage and maximum senior-secured leverage the market will bear

2. **Design the capital structure**
   - Layer the debt stack: revolving credit facility, Term Loan A (amortizing), Term Loan B (institutional), second-lien, high-yield bonds, mezzanine/holdco PIK
   - Size each tranche based on market depth, pricing efficiency, and covenant flexibility trade-offs
   - Determine the revolver size by modeling seasonal working capital swings and contingency needs
   - Set amortization schedules; target 50%+ Term Loan A paydown by year 5 if investment-grade trajectory is desired
   - Evaluate call protection and prepayment premiums (especially on high-yield tranches)

3. **Model cash flows and credit metrics**
   - Build a detailed debt schedule with mandatory and optional amortization, cash sweeps, and excess cash flow recapture
   - Project leverage, coverage, and liquidity ratios through the hold period (typically 5–7 years)
   - Sensitivity-test key variables: revenue growth, margin compression, capex timing, working capital drift, interest rate movements
   - Calculate all-in cost of debt (weighted average coupon, OID, upfront fees, annual agency fees)

4. **Structure the covenant package**
   - Decide between maintenance covenants (tested quarterly) and incurrence covenants (tested only upon specified actions)
   - Draft key financial covenant levels: maximum leverage ratio, minimum interest coverage, maximum capex, minimum liquidity
   - Set covenant cushion (typically 15–25% headroom above projected performance)
   - Define baskets and carve-outs: permitted indebtedness, permitted liens, restricted payments, investments basket, asset sale proceeds reinvestment period
   - Address J-curve risk for platform acquisitions with add-back and EBITDA adjustment definitions [VERIFY: acceptable add-back caps vary by market and credit quality tier]

5. **Negotiate and finalize terms**
   - Prepare a sources & uses table and a term-sheet markup for lender discussions
   - Identify flex provisions in commitment letters (pricing flex, structure flex, market flex)
   - Evaluate syndication risk: hold levels for lead arrangers, target investor composition (CLOs, direct lenders, insurance companies)
   - Assess intercreditor mechanics for multi-tranche structures (payment waterfall, enforcement standstills, turnover provisions)
   - Confirm conditions precedent, representations, and MAC/MAE definitions

## Output

The deliverable should include:

- **Sources & Uses table** showing equity, each debt tranche, and transaction fees
- **Pro forma capitalization table** with leverage and coverage metrics at close
- **Debt schedule** projecting balances, interest expense, amortization, and credit metrics over the hold period
- **Covenant compliance matrix** showing projected metric performance versus covenant thresholds with headroom percentages
- **Sensitivity analysis** across EBITDA, interest rate, and exit multiple scenarios
- **Financing alternatives comparison** summarizing pricing, covenants, flexibility, and execution risk for each option considered
- **Key risk flags** and items requiring further diligence or lender negotiation

## Quality Checks

- Verify that pro forma leverage and coverage ratios tie back to the operating model — no orphaned assumptions
- Confirm interest rate assumptions reflect current market pricing; flag any stale benchmarks with [VERIFY]
- Ensure the debt structure survives the downside case without triggering covenant breaches or liquidity shortfalls
- Cross-check mandatory amortization totals against projected free cash flow to confirm no cash shortfall in any modeled period
- Validate that all-in cost of debt calculation includes OID amortization, commitment fees on undrawn revolver, and ticking fees
- Confirm intercreditor terms are internally consistent across the commitment letter, credit agreement summary, and intercreditor agreement summary
- Flag any covenant definitions (e.g., Adjusted EBITDA, Consolidated Net Income) that deviate from market-standard language [VERIFY]
