---
name: modeling-fresh-start-accounting
description: Structures fresh-start accounting analysis with reorganization value allocation, new basis determination, and emergence balance sheet. Use when modeling fresh-start accounting, preparing emergence financials, or allocating reorganization value.
tags:
  - modeling
  - distressed-and-restructuring
  - accounting
metadata:
  author: casemark
  practice_areas:
    - Restructuring
    - Distressed Investing
    - Turnaround
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Fresh Start Accounting

## When To Use

- Debtor has confirmed a Chapter 11 plan and meets both ASC 852 eligibility tests: (1) reorganization value of emerging entity's assets is less than total post-petition liabilities and allowed claims, and (2) pre-petition voting shares lost majority control
- Preparing day-one emergence balance sheet for SEC filing, lender reporting, or investor due diligence
- Allocating reorganization value across identifiable assets and goodwill for a post-emergence entity
- Modeling the financial impact of plan-of-reorganization scenarios on emergence equity value
- Advising distressed investors on expected book-value basis in post-emergence equity or debt

## Inputs To Gather

- **Pre-emergence balance sheet** — last filed debtor balance sheet (10-Q/10-K or monthly operating report)
- **Confirmed plan of reorganization** — treatment of each class, new equity allocation, reinstated/new debt terms
- **Enterprise / reorganization value** — from disclosure statement valuation (DCF, comparable companies, precedent transactions) or negotiated plan value
- **Fair value appraisals** — third-party or management estimates for PP&E, intangibles, real estate, inventory
- **Debt schedules** — exit facility term sheets, reinstated debt terms, accrued interest through effective date
- **Tax attributes** — NOL carryforward schedule, Section 382 limitation estimate, deferred tax asset/liability detail [VERIFY against debtor's tax advisors]
- **Claim reconciliation** — allowed claims by class versus scheduled amounts, any disputed/contingent reserves

## Workflow

1. **Confirm fresh-start eligibility**
   - Test reorganization value < total post-petition liabilities + allowed claims
   - Test pre-petition shareholders received < 50% of new voting equity
   - Document both tests with specific figures and sources

2. **Establish reorganization value**
   - Use midpoint of disclosure-statement valuation range unless plan specifies a different basis
   - Reconcile enterprise value to equity value: EV − exit debt − other priority claims = equity reorganization value
   - Note any negotiated plan adjustments that override standard valuation

3. **Mark assets to fair value**
   - Revalue each asset class to fair value: cash (par), receivables (net realizable), inventory (NRV or replacement), PP&E (appraised), identified intangibles (relief-from-royalty, multi-period excess earnings, or cost approach as appropriate)
   - Eliminate historical goodwill entirely
   - Record deferred tax impact of fair-value step-ups/step-downs [VERIFY — jurisdiction-specific tax rates and Section 382 limitations apply]

4. **Mark liabilities to fair value**
   - Exit debt at par (new issuance) or fair value (reinstated obligations)
   - Record lease liabilities under ASC 842 at emergence terms
   - Adjust pension/OPEB to current actuarial value
   - Settle pre-petition claims per plan: convert to new equity, cash, or new notes

5. **Allocate reorganization value excess**
   - Compute excess: reorganization value of assets − sum of fair-valued identifiable net assets
   - Positive excess → new goodwill on emergence balance sheet
   - Negative excess → reduce long-lived asset values pro-rata (intangibles first, then PP&E) until eliminated; any remainder recognized as a bargain-purchase gain [VERIFY — rare but occurs in deeply distressed cases]

6. **Build emergence balance sheet**
   - Present a clean day-one balance sheet with all fresh-start adjustments in a bridge/waterfall format
   - Columns: pre-emergence book → plan adjustments (debt discharge, equity conversion) → fresh-start adjustments (fair value marks, goodwill) → post-emergence balance sheet
   - Equity section: new common equity at reorganization value, no retained earnings (reset to zero), no AOCI carryover

7. **Sensitivity and scenario analysis**
   - Flex reorganization value ±10–20% and show impact on goodwill and emergence equity
   - Scenario-test key valuation assumptions (discount rate, terminal growth, EBITDA margin)
   - Show impact of Section 382 limitation on usable NOLs and resulting DTA adjustment

## Output

- **Fresh-start bridge table** — waterfall from pre-emergence to post-emergence balance sheet with plan-adjustment and fresh-start-adjustment columns
- **Reorganization value allocation schedule** — line-by-line asset/liability fair values, identifiable intangible breakdown, and residual goodwill
- **Emergence balance sheet** — day-one balance sheet formatted for 8-K or lender-presentation use
- **Sensitivity matrix** — goodwill and equity sensitivity to reorganization value range
- **Assumptions log** — numbered list of every material assumption with source reference and [VERIFY] flags

## Quality Checks

- Emergence balance sheet balances (assets = liabilities + equity) — confirm to the dollar
- Reorganization value of total assets ties back to enterprise value build-up
- Goodwill is non-negative; if negative, confirm long-lived assets were reduced per ASC 852-10-45
- Eliminated items: historical goodwill is zero, retained earnings is zero, AOCI is zero
- Exit debt face value matches confirmed plan term sheets
- DTA/DTL reflects post-382 limitation on NOLs, not pre-petition full carryforward [VERIFY]
- All fair-value marks have a cited source (appraisal, management estimate, or model output)
- No stale pre-petition accrual balances carried through — each liability line reconciled to plan treatment
