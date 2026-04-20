---
name: managing-foreign-currency-accounting
language: en
description: Structures foreign currency transaction and translation accounting with hedge documentation. Use when accounting for FX transactions, translating foreign operations, or documenting FX hedges.
tags:
  - management
  - accounting
metadata:
  author: casemark
  practice_areas:
    - Financial Reporting
    - Audit
    - Accounting
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Foreign Currency Accounting

Structures foreign currency transaction and translation accounting, including hedge documentation under ASC 830 (formerly FAS 52) and IAS 21/IFRS 9.

## When To Use

- Recording foreign currency–denominated transactions (purchases, sales, intercompany balances, debt)
- Translating financial statements of foreign subsidiaries or branches for consolidation
- Documenting FX hedge relationships (cash flow, fair value, or net investment hedges)
- Performing remeasurement of entities using a functional currency different from local currency
- Preparing period-end FX gain/loss analysis and CTA (cumulative translation adjustment) rollforwards

## Inputs To Gather

- **Entity structure**: List of foreign entities, their local currencies, and determined functional currencies
- **Exchange rates**: Spot rates at transaction dates, period-end closing rates, and weighted-average rates for the period
- **Trial balances**: Local-currency trial balances for each foreign entity
- **Intercompany detail**: Intercompany receivables/payables with currency denomination and settlement terms
- **Hedge instruments**: FX forward, option, or cross-currency swap confirmations with notional, maturity, and counterparty
- **Hedge designation memos**: Existing documentation of hedged risk, hedged item, effectiveness testing method
- **Prior-period CTA balances**: Opening accumulated other comprehensive income (AOCI) balances by entity
- **Accounting policy elections**: Spot-rate vs. forward-rate method for hedge effectiveness; excluded component treatment [VERIFY]

## Workflow

1. **Determine functional currency for each entity**
   - Apply the primary economic environment indicators: cash flows, sales prices, expenses, financing, and intercompany activity
   - Document the conclusion and any judgment calls; reassess if business circumstances change materially
   - [VERIFY] Whether entity qualifies as operating in a highly inflationary economy (requires remeasurement to parent currency under ASC 830-10-45-11 / IAS 29)

2. **Record foreign currency transactions**
   - Translate each transaction at the spot rate on the transaction date (or a reasonable approximation such as weekly/monthly average if rates do not fluctuate significantly)
   - At each balance sheet date, remeasure monetary assets and liabilities at the closing spot rate
   - Recognize transaction gains/losses in the income statement (typically in Other Income/Expense)
   - Identify and segregate intercompany balances that are of a long-term investment nature (gains/losses bypass income statement and flow to CTA under ASC 830-20-35-3)

3. **Translate foreign entity financial statements**
   - **Current-rate method** (standard for self-sustaining subsidiaries): assets and liabilities at closing rate; revenue and expenses at weighted-average rate; equity at historical rates
   - **Temporal (remeasurement) method** (for entities whose functional currency differs from local currency): monetary items at closing rate; non-monetary items at historical rates; revenue/expense at rates in effect when recognized
   - Compute the translation adjustment and post to CTA within AOCI
   - Prepare a CTA rollforward: opening balance → current-period translation adjustment → reclassifications on disposal → closing balance

4. **Document FX hedge relationships**
   - For each hedge, prepare or update the designation memo covering:
     - Hedging instrument (type, notional, maturity, counterparty)
     - Hedged item or forecasted transaction (nature, amount, expected timing)
     - Risk being hedged (FX risk on functional-currency equivalent cash flows, fair value, or net investment)
     - Effectiveness assessment method (dollar-offset, regression, or critical-terms-match for perfectly aligned hedges)
   - Perform prospective and retrospective effectiveness testing each reporting period
   - Record effective portion in OCI (cash flow hedge) or adjust carrying amount of hedged item (fair value hedge)
   - Recognize ineffectiveness immediately in earnings
   - [VERIFY] Treatment of time value, forward points, or cross-currency basis spread as excluded components under ASC 815-20-25-83A or IFRS 9 6.5.15

5. **Prepare period-end FX analysis and disclosures**
   - Summarize realized and unrealized FX gains/losses by entity and by account category
   - Reconcile FX impact on the income statement to expectations based on rate movements and exposure levels
   - Draft disclosure footnotes covering: functional currency policies, translation methods used, aggregate transaction gain/loss, CTA movements, and hedge positions with fair values
   - [VERIFY] Sensitivity disclosure requirements under local GAAP or IFRS 7

## Output

- **FX Transaction Journal Entries**: Dated entries with rate sources for each foreign-currency transaction and remeasurement
- **Translation Workpapers**: Entity-by-entity schedules showing local-currency balances, rates applied, and translated amounts
- **CTA Rollforward**: Period-over-period reconciliation of cumulative translation adjustments per entity
- **Hedge Documentation Package**: Designation memos, effectiveness test results, and OCI/earnings allocation schedules
- **FX Gain/Loss Summary**: Consolidated report of realized and unrealized FX impacts by category, with variance commentary
- **Disclosure Draft**: Footnote language covering policies, methods, material exposures, and hedge positions

## Quality Checks

- Confirm functional currency determinations are consistent with prior periods unless a substantive change in circumstances is documented
- Verify that exchange rates used (spot, average, historical) tie to an approved rate source and are applied consistently across entities
- Check that intercompany balances eliminate fully on consolidation after translation; investigate residual differences
- Ensure CTA rollforward reconciles to the AOCI line in the consolidated balance sheet
- Validate that hedge effectiveness ratios fall within the 80–125% band (if using dollar-offset method) or meet the statistical threshold chosen [VERIFY]
- Confirm no transaction gains/losses were incorrectly classified as translation adjustments or vice versa
- Cross-check that highly inflationary economy assessments are current (cumulative three-year inflation ≥ 100%) [VERIFY]
- Review that disposed-of-entity CTA reclassifications to earnings are recorded in the correct period and amount
