---
name: managing-interest-rate-risk-banking
description: Structures bank interest rate risk analysis with EVE, NII sensitivity, and gap analysis. Use when managing bank IRR, modeling NII sensitivity, or analyzing repricing gaps.
tags:
  - management
  - commercial-banking
  - risk
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
# Managing Interest Rate Risk Banking

Structures bank interest rate risk analysis combining Economic Value of Equity (EVE), Net Interest Income (NII) sensitivity, and repricing gap analysis to support ALCO decision-making and regulatory compliance.

## When To Use

- Preparing ALCO packages with rate-sensitivity metrics for board or committee review
- Running scenario analysis for parallel and non-parallel yield curve shifts (e.g., +/- 100, 200, 300 bps)
- Assessing repricing mismatches across the balance sheet by time bucket
- Responding to regulatory examination findings on IRR management [VERIFY: OCC/FDIC/Fed guidance applicable to charter type]
- Evaluating hedging strategies (swaps, caps, floors) against the bank's risk appetite statement
- Modeling NII impact of loan/deposit mix changes, new product launches, or M&A integration

## Inputs To Gather

- **Balance sheet data**: Current outstanding balances by product, with contractual maturity and repricing dates
- **Rate assumptions**: Current market rates, forward curve, and management's rate outlook scenarios
- **Prepayment models**: CPR/PSA assumptions for mortgage and amortizing loan portfolios [VERIFY: model vendor and last validation date]
- **Non-maturity deposit (NMD) assumptions**: Decay rates, beta coefficients, and repricing lags for DDAs, savings, and MMDAs
- **Risk appetite statement**: Board-approved EVE and NII limits (e.g., EVE decline ≤ 15% for +200 bps shock; NII decline ≤ 10% for same)
- **Hedging positions**: Notional amounts, terms, and mark-to-market on existing derivative positions
- **Prior period results**: Previous quarter's IRR metrics for trend comparison

## Workflow

1. **Compile repricing gap schedule**
   - Bucket all rate-sensitive assets (RSA) and rate-sensitive liabilities (RSL) into time bands: overnight, 1-30 days, 31-90 days, 91-180 days, 181-365 days, 1-3 years, 3-5 years, 5+ years
   - Calculate cumulative gap and gap-to-assets ratio per bucket
   - Flag any bucket where cumulative gap exceeds policy limits

2. **Run NII sensitivity analysis**
   - Model NII under base case, rising-rate, and falling-rate scenarios (minimum: +/- 100, 200, 300 bps parallel shifts)
   - Incorporate non-parallel scenarios: flattening, steepening, and inversion of the yield curve
   - Apply NMD beta assumptions and repricing lags — document the source and last validation of each assumption
   - Calculate dollar and percentage change in NII versus base for each scenario
   - Compare results against board-approved NII-at-risk limits

3. **Perform EVE analysis**
   - Discount all asset and liability cash flows at current rates to establish base EVE
   - Re-discount under each shock scenario to compute stressed EVE
   - Calculate EVE change as a percentage of base EVE and as a percentage of total assets
   - Identify which asset/liability categories contribute most to EVE sensitivity (duration attribution)

4. **Assess hedging effectiveness**
   - Evaluate existing derivatives: notional coverage ratio, remaining tenor, counterparty exposure
   - Test whether hedge positions offset the identified gap or NII exposure
   - Model incremental hedging strategies if current positions leave residual risk outside appetite

5. **Prepare ALCO management report**
   - Summarize gap, NII, and EVE results in a dashboard format with traffic-light indicators against limits
   - Highlight breaches or near-breaches of any risk appetite threshold
   - Include trend analysis comparing current quarter to prior quarters
   - Recommend specific actions: balance sheet repositioning, hedging adjustments, deposit pricing changes, or limit modifications

## Output

The deliverable is an **Interest Rate Risk Management Report** containing:

- **Executive summary**: Key metrics, limit utilization, and recommended actions
- **Repricing gap table**: Time-bucketed RSA, RSL, periodic gap, cumulative gap, and gap ratios
- **NII sensitivity table**: Dollar and percentage NII change across all scenarios, with limit comparison
- **EVE sensitivity table**: Base EVE, stressed EVE, and percentage decline per scenario
- **Duration and convexity summary**: Effective duration of assets, liabilities, and equity
- **Hedge position summary**: Current derivatives with notional, fair value, and maturity profile
- **Action items**: Numbered recommendations with owners and target dates for ALCO follow-up

## Quality Checks

- Verify that total assets and liabilities in the gap schedule reconcile to the general ledger within an acceptable tolerance (typically < 1%)
- Confirm NMD assumptions (decay rates, betas) were reviewed and validated within the past 12 months [VERIFY: institution's model validation policy and cycle]
- Ensure all scenarios required by the institution's IRR policy are included — check against the board-approved policy document
- Validate that prepayment speed assumptions reflect current market conditions, not stale defaults
- Cross-check EVE results against any third-party vendor model output (e.g., QRM, ZM Financial, Empyrean) for reasonableness [VERIFY: vendor in use]
- Confirm derivative positions tie to trade confirmations and counterparty statements
- Review that the report complies with applicable regulatory guidance: Interagency Advisory on Interest Rate Risk Management (2010), OCC Bulletin 2010-1, and FDIC FIL-2-2010 [VERIFY: current guidance updates and institution's primary regulator]
