---
name: analyzing-fraudulent-transfer-exposure
language: en
description: Evaluates fraudulent conveyance risk for leveraged transactions with solvency analysis and reasonably equivalent value assessment. Use when analyzing fraudulent transfer risk, conducting solvency tests, or evaluating historical transactions.
tags:
  - analysis
  - distressed-and-restructuring
  - risk
metadata:
  author: casemark
  practice_areas:
    - Restructuring
    - Distressed Investing
    - Turnaround
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Fraudulent Transfer Exposure

Evaluates fraudulent conveyance risk for leveraged transactions with solvency analysis and reasonably equivalent value assessment.

## When To Use

- Assessing a leveraged buyout, dividend recapitalization, or leveraged recapitalization for constructive fraud risk
- Evaluating whether a debtor received reasonably equivalent value in a pre-bankruptcy transaction
- Conducting solvency analysis at the time of a challenged transfer
- Reviewing historical transactions within the look-back period for actual or constructive fraud
- Supporting litigation defense or creditor claims in avoidance actions under Bankruptcy Code §§ 544, 548, or state UFTA/UVTA statutes [VERIFY: applicable state statute — UFTA vs. UVTA adoption varies]

## Inputs To Gather

- **Transaction documents**: purchase agreement, credit agreements, security agreements, intercompany notes, and closing statements showing consideration flow
- **Financial statements**: audited or reviewed balance sheets, income statements, and cash flow statements for the transferor entity at the time of transfer and for the 2 years preceding
- **Projections and budgets**: management forecasts, board-approved budgets, and lender models used to underwrite the transaction
- **Solvency opinions or fairness opinions**: any third-party opinions obtained at closing
- **Capital structure detail**: pre- and post-transaction debt schedules, guaranty obligations, contingent liabilities, and off-balance-sheet exposures
- **Industry and market context**: comparable company multiples, sector distress indicators, and macroeconomic conditions at the transfer date
- **Look-back period**: confirm the relevant statute of limitations — typically 2 years under § 548, up to 6 years under state law [VERIFY: jurisdiction-specific look-back periods]

## Workflow

1. **Map the transaction flow**
   - Diagram the movement of funds, assets, and obligations among all parties (buyer, target, lender, seller, guarantors)
   - Identify each discrete transfer and the entity that bore economic loss or gained value
   - Flag intercompany transfers, upstream guarantees, and cross-collateralization structures

2. **Determine the applicable legal framework**
   - Identify whether claims arise under § 548 (federal), § 544(b) incorporating state law, or direct state UFTA/UVTA actions [VERIFY]
   - Distinguish actual fraud (intent-based, badge-of-fraud analysis) from constructive fraud (solvency + value tests)
   - Note any safe harbors (e.g., § 546(e) securities safe harbor for settlement payments) and current circuit-level interpretations [VERIFY: post-Merit Management scope in relevant circuit]

3. **Conduct the solvency analysis (constructive fraud)**
   - **Balance sheet test**: compare fair value of assets against total liabilities (including contingent and unliquidated claims) as of the transfer date; use both book value and fair market value / going-concern value
   - **Cash flow test**: assess whether the entity could pay debts as they became due in the ordinary course, using projected cash flows and debt maturity schedules
   - **Adequate capitalization test**: evaluate whether the entity was left with unreasonably small capital to operate its business given reasonably foreseeable risks
   - Document each test result independently — a single failure is sufficient for constructive fraud exposure

4. **Assess reasonably equivalent value**
   - Quantify what the transferor entity received in exchange for what it gave up or guaranteed
   - For guarantees and pledges by non-borrower entities, analyze indirect benefits (synergies, access to credit, shared services) and whether they constitute value
   - Apply the "net effect" or "economic substance" approach used in the relevant jurisdiction [VERIFY]

5. **Analyze badges of fraud (actual fraud)**
   - Review for insider status of transferee, retention of control by transferor, concealment, timing relative to pending claims, consideration adequacy, and debtor's financial condition
   - Apply the multi-factor test from the applicable jurisdiction's fraudulent transfer statute [VERIFY: factor list varies by state]

6. **Quantify exposure**
   - Calculate the maximum avoidable amount (full transfer value) and the likely avoidable amount (net of value received)
   - Assess downstream recovery risk to subsequent transferees under § 550
   - Model impact on distributions in a hypothetical liquidation or plan scenario

7. **Evaluate defenses and mitigants**
   - Good-faith transferee defense under § 548(c) — assess whether the transferee took for value and in good faith
   - Statute of limitations and tolling arguments
   - Strength of any solvency opinion or fairness opinion obtained at closing (methodology, assumptions, qualifications)

## Output

- **Executive summary**: one-paragraph risk rating (high / moderate / low) with key drivers
- **Transaction flow diagram**: visual map of transfers, consideration, and guaranty obligations
- **Solvency analysis matrix**: results of balance sheet, cash flow, and adequate capitalization tests with supporting figures
- **Reasonably equivalent value assessment**: value given vs. value received for each challenged transfer
- **Badges of fraud checklist**: factor-by-factor evaluation with supporting evidence
- **Exposure quantification**: range of avoidable amounts and recovery risk
- **Defense assessment**: strength rating of each available defense with gaps identified
- **Appendix**: key assumptions, data sources, and items requiring further diligence

## Quality Checks

- Solvency tests are performed as of the exact transfer date, not a later or earlier date
- Fair value of assets reflects market conditions at the transfer date, not hindsight valuations
- Contingent liabilities are included in the balance sheet test at their estimated probable amount
- Reasonably equivalent value analysis accounts for indirect benefits, not just direct cash consideration
- Look-back period is calculated correctly from the petition date or complaint filing date [VERIFY]
- All assumptions and data gaps are flagged with [VERIFY] rather than silently estimated
- Analysis distinguishes between exposure at the entity level (target, guarantor, pledgor) rather than treating the transaction as a single unit
