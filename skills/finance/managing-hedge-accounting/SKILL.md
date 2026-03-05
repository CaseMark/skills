---
name: managing-hedge-accounting
description: Structures hedge accounting documentation with effectiveness testing and ASC 815/IFRS 9 compliance. Use when documenting hedge relationships, testing effectiveness, or managing hedge accounting compliance.
tags:
  - management
  - quantitative-finance
  - compliance
  - accounting
metadata:
  author: casemark
  practice_areas:
    - Derivatives
    - Quantitative Analysis
    - Structured Products
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Hedge Accounting

Structures hedge accounting documentation with effectiveness testing and ASC 815/IFRS 9 compliance.

## When To Use

- Designating a new hedge relationship (fair value, cash flow, or net investment hedge)
- Performing prospective or retrospective effectiveness testing at inception or on an ongoing basis
- Preparing or reviewing formal hedge documentation packages required at designation
- Assessing whether de-designation or rebalancing is needed after a change in hedged risk, hedging instrument, or hedge ratio
- Transitioning hedge relationships between ASC 815 and IFRS 9 frameworks (e.g., cross-listing, IFRS conversion)
- Responding to audit inquiries on hedge accounting qualification or effectiveness results

## Inputs To Gather

- **Hedging instrument details**: notional, maturity, counterparty, derivative type (swap, option, forward, cross-currency), trade confirmation
- **Hedged item/transaction details**: forecasted transaction description and probability assessment, recognized asset/liability carrying value, firm commitment terms
- **Risk management objective**: board-approved policy excerpt, risk being hedged (interest rate, FX, commodity price, credit), economic rationale
- **Hedge type designation**: fair value hedge, cash flow hedge, or net investment hedge
- **Critical terms**: comparison of hedged item vs. instrument terms (notional, tenor, index, reset dates, currency, payment frequency)
- **Historical data**: market data series for regression or dollar-offset testing, prior effectiveness test results
- **Applicable framework**: ASC 815 (U.S. GAAP) or IFRS 9, including any elections (e.g., ASC 815 shortcut method, critical-terms-match, IFRS 9 cost-of-hedging approach) [VERIFY]

## Workflow

1. **Document the hedge relationship at inception**
   - Draft formal designation memo: identify the hedging instrument, hedged item/transaction, nature of risk being hedged, and risk management objective
   - State the hedge type (fair value / cash flow / net investment) and the method for assessing effectiveness
   - Under ASC 815, confirm whether shortcut method or critical-terms-match qualifies; under IFRS 9, confirm the economic relationship and that credit risk does not dominate [VERIFY]
   - Record the hedge ratio and justify if other than 1:1

2. **Perform prospective effectiveness assessment**
   - For quantitative methods: run regression analysis (R-squared >= 0.80, slope between -0.80 and -1.25 is common threshold) or hypothetical derivative method on historical or simulated data [VERIFY thresholds against entity policy]
   - For qualitative methods (critical-terms-match): verify that all critical terms of the hedging instrument and hedged item match exactly — notional, maturity, underlying index, reset dates, and currency
   - Document the conclusion: "highly effective" expectation met or not

3. **Perform retrospective effectiveness testing (each reporting period)**
   - Dollar-offset method: compute ratio of cumulative change in fair value of hedging instrument to cumulative change in fair value of hedged item; ratio must fall within 80%-125% under ASC 815 [VERIFY — IFRS 9 does not require retrospective quantitative test but requires ongoing economic relationship validation]
   - Regression method: update regression with current-period data; confirm statistical validity
   - Record period-by-period results in an effectiveness log with date, method, result, and pass/fail determination

4. **Assess ineffectiveness and journal entries**
   - Calculate the ineffective portion of the hedge gain/loss
   - Fair value hedges: recognize both the change in fair value of the hedging instrument and the hedged item attributable to the hedged risk in earnings
   - Cash flow hedges: record the effective portion in OCI; reclassify to earnings when the hedged transaction affects earnings; recognize ineffectiveness immediately in earnings
   - Net investment hedges: record effective portion in CTA within OCI [VERIFY applicable translation method]

5. **Monitor for de-designation or rebalancing triggers**
   - Forecasted transaction no longer probable (cash flow hedge) — discontinue prospectively
   - Effectiveness test failure — discontinue and evaluate if redesignation is appropriate
   - Change in hedge ratio needed — under IFRS 9, rebalance without de-designation if the risk management objective remains unchanged; under ASC 815, de-designate and redesignate [VERIFY]
   - Hedging instrument expires, is sold, or terminated — discontinue

6. **Compile reporting package**
   - Summarize all active hedge relationships: instrument, hedged item, designation date, hedge type, effectiveness method, latest test result
   - Prepare disclosure support: notional amounts by hedge type, gain/loss in OCI and amounts reclassified to earnings, location of hedge gains/losses in the income statement
   - Flag any relationships approaching ineffectiveness thresholds or upcoming maturity requiring action

## Output

The deliverable is a hedge accounting management report containing:

- **Hedge designation memos** for each relationship (instrument, hedged item, risk, objective, method, hedge ratio)
- **Effectiveness testing log** with prospective and retrospective results per period
- **Ineffectiveness calculation** with supporting fair value data and journal entry recommendations
- **Active hedge relationship summary table** (hedge type, status, next action date)
- **Disclosure schedule** with amounts for financial statement footnotes (ASC 815-20/25/35 or IFRS 7 disclosures) [VERIFY specific disclosure paragraphs against current standards]
- **Exception report** listing any failed tests, de-designated hedges, or relationships requiring rebalancing

## Quality Checks

- Every hedge relationship has a formal designation memo dated on or before the designation date — no retroactive designations
- Effectiveness test method stated in the designation memo matches the method actually applied in testing
- Quantitative test results include raw data, calculation methodology, and explicit pass/fail conclusion — not just a summary ratio
- Cash flow hedge forecasted transactions include a documented probability assessment with supporting evidence (historical volumes, contractual commitments, budget forecasts)
- Journal entries for ineffectiveness tie to the effectiveness test calculations with a clear audit trail
- All critical-terms-match assessments explicitly confirm each critical term rather than stating a blanket conclusion
- Disclosure amounts reconcile to the general ledger OCI and earnings balances
- [VERIFY] that the applicable standard version is current — ASC 2017-12 amendments to ASC 815 and IFRS 9 (effective dates and transition provisions) are reflected in the methodology
