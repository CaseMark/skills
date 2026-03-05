---
name: modeling-dividend-recapitalizations
description: Structures dividend recap analysis with leverage impact, credit agreement compliance, and return enhancement calculation. Use when modeling dividend recaps, evaluating interim distributions, or analyzing recapitalization options.
tags:
  - modeling
  - private-equity
  - compliance
  - credit
metadata:
  author: casemark
  practice_areas:
    - Private Equity
    - Leveraged Buyouts
    - Growth Equity
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Dividend Recapitalizations

Structures dividend recap analysis with leverage impact, credit agreement compliance, and return enhancement calculation.

## When To Use

- Sponsor is considering an interim cash distribution funded by incremental debt prior to exit
- Evaluating whether a portfolio company can support additional leverage for a dividend recap
- Comparing a dividend recap against alternative liquidity events (partial sale, secondary, continuation fund)
- Stress-testing credit agreement headroom before approaching lenders for recap financing
- Quantifying IRR and MOIC enhancement from accelerating cash-on-cash returns

## Inputs To Gather

- **Current capital structure**: Senior debt outstanding (revolver drawn, term loan balances), subordinated/mezzanine layers, total equity invested at cost
- **Credit agreement terms**: Maximum leverage ratio (Total Debt / EBITDA), secured leverage cap, fixed charge coverage minimum, restricted payments basket language, pro forma incurrence test thresholds [VERIFY against actual credit agreement]
- **Company financials**: Trailing twelve-month (TTM) EBITDA, forward projections (2–3 years), capex requirements, working capital seasonality, cash on balance sheet
- **Proposed recap parameters**: Target dividend amount, proposed new debt instrument (term loan B, second lien, holdco PIK), indicative pricing (spread, OID, floor), expected tenor
- **Sponsor economics**: Equity check at entry, any prior distributions, current fund vintage and deployment pace, LP reporting considerations

## Workflow

1. **Establish pre-recap baseline**
   - Build or refresh the operating model with TTM financials and management projections
   - Calculate current leverage (Total Debt / EBITDA, Net Debt / EBITDA, Senior / EBITDA)
   - Compute current free cash flow profile and debt service coverage ratio (DSCR)

2. **Size the dividend**
   - Determine maximum incremental debt capacity under credit agreement covenants
   - Apply the restricted payments basket test — identify whether the dividend falls within builder basket, general basket, or requires an incurrence-based exception [VERIFY covenant language for specific permitted payment carve-outs]
   - Deduct transaction fees (arrangement fees, legal, advisory) from gross proceeds to derive net distributable amount
   - Sense-check dividend size against market comps for similar recap transactions (typically 1.0×–2.5× incremental turns of leverage)

3. **Model pro forma capital structure**
   - Layer in new debt tranche with proposed terms (rate, amortization, maturity, call protection)
   - Recalculate blended cost of debt and weighted average maturity
   - Produce pro forma leverage and coverage ratios at close and for each projected period
   - Confirm no covenant breach at closing or within the projection horizon under the base case

4. **Assess credit impact**
   - Run downside scenarios: revenue decline of 10–20%, margin compression of 100–300 bps, working capital blow-out
   - Identify the EBITDA breakeven level at which covenant thresholds are breached
   - Calculate cushion percentages on each financial covenant post-recap
   - Evaluate rating agency implications if applicable (Moody's/S&P leverage thresholds for the sector) [VERIFY sector-specific rating benchmarks]

5. **Quantify return enhancement**
   - Recalculate sponsor IRR and MOIC with the dividend included as an interim cash flow
   - Compare gross and net IRR/MOIC pre- and post-recap across multiple exit timing scenarios (e.g., exit in Year 3, 4, 5)
   - Compute DPI (distributions to paid-in) impact on fund-level metrics
   - Show cash-on-cash return at the time of the dividend (dividend ÷ equity invested)

6. **Sensitivity and scenario analysis**
   - Build a two-way sensitivity table: dividend size vs. exit EBITDA multiple
   - Vary interest rate assumptions (fixed vs. floating, hedge cost) to stress debt service
   - Model early repayment of recap debt from excess cash flow to show deleveraging trajectory
   - Present bear/base/bull return profiles with and without the recap

## Output

- **Executive summary**: One-page overview of proposed recap — dividend amount, pro forma leverage, covenant headroom, and IRR/MOIC enhancement
- **Pro forma capitalization table**: Pre- and post-recap side-by-side with all debt tranches, rates, maturities, and total equity value
- **Covenant compliance matrix**: Each financial covenant tested at close and through the projection period with cushion percentages
- **Returns waterfall**: Sponsor IRR and MOIC with and without recap, across exit timing scenarios
- **Sensitivity tables**: Dividend size vs. leverage, EBITDA decline vs. covenant breach, exit multiple vs. IRR
- **Risk flags**: Identified risks including refinancing exposure, floating rate sensitivity, and covenant tightness

## Quality Checks

- Pro forma leverage ratios tie exactly to the credit agreement definitions (confirm EBITDA add-backs, pro forma adjustments match lender methodology) [VERIFY]
- Restricted payments test uses the correct basket and references the operative credit agreement section
- IRR calculations use actual cash flow dates — not period-end approximations
- All incremental debt terms reflect current market conditions for the company's credit profile
- Downside scenarios are genuinely stressful, not cosmetic — test at least a 15% EBITDA decline
- Dividend amount plus fees plus minimum cash does not exceed gross debt proceeds
- Model cross-checks: ending cash balance ties to cash flow statement, debt schedule ties to balance sheet, interest expense ties to average balances × applicable rates
