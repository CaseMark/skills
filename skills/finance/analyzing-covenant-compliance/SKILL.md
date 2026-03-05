---
name: analyzing-covenant-compliance
description: Reviews financial covenant compliance calculations with cure provisions and default trigger analysis. Use when checking covenant compliance, calculating coverage ratios, or evaluating covenant headroom.
tags:
  - analysis
  - fixed-income
  - compliance
metadata:
  author: casemark
  practice_areas:
    - Fixed Income
    - Credit Research
    - Bond Trading
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Covenant Compliance

## When To Use

- Evaluating whether a bond issuer or borrower is in compliance with financial maintenance covenants (leverage ratio, interest coverage, fixed charge coverage, minimum net worth, etc.)
- Calculating covenant headroom to assess proximity to a potential default trigger
- Reviewing cure provisions (equity cure rights, add-back mechanics) and their remaining availability
- Assessing the impact of a proposed transaction (acquisition, dividend, asset sale) on incurrence covenants
- Preparing credit surveillance reports or event-driven covenant analysis for trading decisions

## Inputs To Gather

- **Credit agreement or indenture** — the governing document containing covenant definitions, calculation mechanics, and cure provisions
- **Financial statements** — most recent quarterly/annual financials (income statement, balance sheet, cash flow statement) as delivered under the credit agreement
- **Compliance certificate** — borrower's own covenant compliance certificate if available, with management's calculations
- **Permitted adjustments schedule** — EBITDA add-backs, pro forma adjustments for acquisitions/dispositions, and any run-rate synergies claimed
- **Cure history** — record of any prior equity cures exercised, with amounts and dates
- **Amendment/waiver history** — any covenant amendments, holidays, or waivers that modify baseline thresholds

## Workflow

1. **Map covenant definitions to financials**
   - Identify each financial maintenance and incurrence covenant (e.g., Total Leverage Ratio, Interest Coverage Ratio, Fixed Charge Coverage Ratio, Minimum Liquidity)
   - Extract the precise calculation methodology from the credit agreement — note defined terms for "Consolidated EBITDA," "Consolidated Total Debt," "Net Debt," etc.
   - Flag any definitional mismatches between the borrower's compliance certificate and the governing document [VERIFY]

2. **Recalculate each covenant ratio independently**
   - Compute trailing-twelve-month (TTM) or last-quarter-annualized figures as specified by the agreement
   - Apply permitted add-backs and pro forma adjustments — verify each add-back against the cap or basket limit in the credit agreement
   - Calculate the ratio using the agreement's numerator/denominator definitions, not generic financial metrics
   - Compare your result to the borrower's reported compliance certificate figure; investigate any variance exceeding 0.05x

3. **Assess covenant headroom**
   - For each covenant, calculate the cushion between actual performance and the trigger threshold (in absolute terms and as a percentage)
   - Model sensitivity: determine how much EBITDA decline, debt increase, or revenue shortfall would trip each covenant
   - Identify the tightest covenant — this is the binding constraint and the focus of default-risk analysis
   - Flag any step-down or step-up schedules that tighten thresholds in upcoming periods [VERIFY]

4. **Evaluate cure provisions and default triggers**
   - Determine whether equity cure rights exist and their terms: maximum number of cures per term, consecutive-quarter limits, minimum cure amount, deemed EBITDA treatment vs. debt paydown
   - Count remaining cure capacity (cures used vs. total permitted)
   - Assess whether a potential breach would trigger a cross-default to other facilities or bond indentures
   - Review grace periods and notice requirements before a covenant breach becomes an event of default [VERIFY]

5. **Analyze incurrence covenants for proposed transactions**
   - For asset sales, restricted payments, or additional debt, test whether the proposed action satisfies the applicable incurrence test (e.g., pro forma leverage ≤ threshold, Fixed Charge Coverage ≥ 2.0x)
   - Verify basket availability and capacity (general basket, builder basket, available amount)
   - Confirm whether the transaction uses a ratio-based exception or a flat-dollar basket

6. **Summarize findings and risk flags**
   - Present a covenant compliance summary table with: covenant name, required threshold, actual result, headroom, and pass/fail status
   - Highlight any covenant within 10% of its trigger as "watch" status
   - Note any reliance on contested add-backs, aggressive pro forma adjustments, or unusual definitional interpretations

## Output

- **Covenant Compliance Summary Table** — covenant name | definition reference (section #) | required threshold | actual ratio | headroom | status (Pass / Watch / Breach)
- **Headroom Sensitivity Analysis** — for the tightest covenant, show breakeven EBITDA decline and incremental debt capacity
- **Cure Provision Status** — cures exercised, cures remaining, conditions for exercise
- **Risk Flags** — list of items requiring attention: approaching thresholds, aggressive add-backs, upcoming step-downs, cross-default exposure
- **Recommended Actions** — monitoring frequency, amendment considerations, or trading implications

## Quality Checks

- Every ratio recalculation ties back to specific line items in the financial statements with clear sourcing
- Defined terms match the credit agreement exactly — do not substitute generic financial definitions
- Add-back caps and basket limits are verified against agreement language, not approximated
- Cure provision analysis accounts for all contractual limitations (frequency, amount, deemed treatment)
- Any jurisdiction-specific enforceability issues (e.g., intercreditor agreement override, local insolvency law implications) are flagged with [VERIFY]
- Headroom calculations use the correct testing period and step-down schedule for the relevant quarter
- Cross-default provisions are identified across all related facilities and indentures
