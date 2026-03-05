---
name: managing-bank-regulatory-reporting
description: Structures regulatory report preparation including Call Reports, FR Y-9C, and other required filings. Use when preparing bank regulatory reports, filing Call Reports, or managing regulatory submissions.
tags:
  - management
  - commercial-banking
  - regulatory
metadata:
  author: casemark
  practice_areas:
    - Commercial Banking
    - Trade Finance
    - Lending
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Bank Regulatory Reporting

Structures the preparation, review, and submission workflow for recurring bank regulatory filings — Call Reports (FFIEC 031/041/051), FR Y-9C consolidated holding company reports, FR Y-9LP, and related schedules.

## When To Use

- Preparing quarterly Call Report or FR Y-9C filings
- Coordinating data collection across departments (finance, treasury, credit, operations) for regulatory submissions
- Reviewing draft filings for internal consistency and reconciliation to general ledger
- Managing restatements, amendments, or late-filing notices
- Onboarding a new filing period after charter changes, mergers, or system migrations

## Inputs To Gather

- **Filing identification**: Charter type (national bank, state member, state nonmember, savings association), RSSD ID, reporting form (031 vs. 041 vs. 051), holding company structure [VERIFY]
- **General ledger trial balance**: Period-end balances mapped to Call Report/Y-9C line items
- **Prior-period filings**: Last submitted XBRL instance and validation results for trend analysis
- **Supplemental data**: Off-balance-sheet items, derivatives notional amounts, loan segmentation by risk grade, allowance components (CECL or incurred-loss), interest rate sensitivity schedules
- **Regulatory calendar**: Filing deadlines (typically 30 days after quarter-end for Call Reports, 40 days for FR Y-9C) [VERIFY against current FFIEC/Federal Reserve instructions]
- **Threshold triggers**: Total asset size determining which schedules apply (e.g., Schedule RC-R Part II applicability at ≥$5B) [VERIFY]

## Workflow

1. **Map reporting scope**
   - Confirm which forms are required based on charter type, asset size, and holding company status
   - Identify new or sunset schedules from the latest FFIEC or Federal Reserve reporting updates
   - Assign schedule-level owners (e.g., Treasury owns RC-B securities, Credit owns RC-C loans, Operations owns RC-O)

2. **Extract and reconcile source data**
   - Pull period-end trial balance and sub-ledger detail
   - Reconcile GL balances to prior-quarter Call Report totals; investigate and document variances exceeding materiality threshold
   - Populate loan, securities, and deposit segmentation schedules from core banking system extracts
   - Verify off-balance-sheet commitments and derivatives notionals tie to source systems

3. **Populate schedules and run validation**
   - Enter data into filing software (e.g., Axiom, Wolters Kluwer, Abrigo, or in-house XBRL tool)
   - Run FFIEC/Federal Reserve edit checks — resolve quality edits and document explanations for validity edits that will be submitted
   - Cross-check inter-schedule consistency: RC-B to RC-R risk-weight buckets, RC-C to RC-N past-due and nonaccrual, RC-K to summary totals

4. **Internal review and sign-off**
   - Circulate draft to schedule owners for attestation
   - CFO or Controller performs top-level analytical review: quarter-over-quarter trends, peer benchmarking, ratio reasonableness (leverage, liquidity coverage, net interest margin implied by filings)
   - Board or designated committee reviews and authorizes submission [VERIFY governance policy]

5. **Submit and archive**
   - Transmit via CDR (Central Data Repository) for Call Reports or FR Y-9C Online for holding company reports
   - Retain confirmation receipt, XBRL instance document, validation summary, and all supporting workpapers per record retention policy [VERIFY — minimum 5 years typical but institution policy may differ]
   - Log any post-submission amendments and their justification

6. **Post-filing monitoring**
   - Track regulatory feedback or follow-up inquiries from FFIEC, OCC, FDIC, or Federal Reserve
   - Note edit-check failures or data quality flags for process improvement in next cycle
   - Update mapping templates if chart of accounts or system changes occurred during the quarter

## Output

- **Filing package**: Completed Call Report or FR Y-9C with all applicable schedules, ready for electronic submission
- **Reconciliation workpapers**: GL-to-schedule tie-outs with variance explanations
- **Validation summary**: Edit-check results with resolution notes for each quality and validity edit
- **Trend analysis**: Quarter-over-quarter comparison of key line items (total assets, total loans, total deposits, risk-weighted assets, tier 1 capital ratio)
- **Sign-off log**: Schedule-owner attestations and CFO/board approval documentation

## Quality Checks

- All FFIEC or Federal Reserve edit checks pass or have documented explanations
- Schedule RC (balance sheet) balances to total assets; total liabilities plus equity ties out
- RC-R risk-weighted assets reconcile to underlying schedule detail (RC-B, RC-C, RC-L)
- Loan schedules (RC-C) reconcile to past-due/nonaccrual schedules (RC-N) and charge-off schedules (RI-B)
- Interest income and expense on Schedule RI are directionally consistent with average balance and rate data
- Filing is submitted before the regulatory deadline; if extension is needed, Form FFIEC 009a or equivalent request is filed timely [VERIFY extension procedures by regulator]
- All [VERIFY] items in source data and thresholds have been confirmed against current regulatory instructions before submission
