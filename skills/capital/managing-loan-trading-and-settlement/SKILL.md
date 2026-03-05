---
name: managing-loan-trading-and-settlement
description: Coordinates loan trading with LSTA standard documentation, delayed settlement compensation, and trade settlement mechanics. Use when managing loan trades, processing LSTA documentation, or coordinating trade settlement.
tags:
  - management
  - credit-and-institutional-lending
  - trading
metadata:
  author: casemark
  practice_areas:
    - Credit Markets
    - Leveraged Lending
    - Direct Lending
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Loan Trading And Settlement

Coordinates loan trading with LSTA standard documentation, delayed settlement compensation, and trade settlement mechanics.

## When To Use

- Processing a par or distressed loan trade from execution through settlement
- Preparing or reviewing LSTA trade confirmations and assignment agreements
- Calculating delayed settlement compensation (cost of carry / delayed comp)
- Tracking T+7 (par) or T+20 (distressed) settlement timelines and identifying fails
- Coordinating between buyer, seller, agent bank, and operations teams on trade settlement
- Managing consent requirements, KYC/AML clearance, and sub-minimum denomination issues

## Inputs To Gather

- **Trade details**: trade date, settlement date, commitment amount, purchase price (percentage of par), trade type (par/distressed), accrued interest convention
- **Counterparty information**: buyer and seller legal entity names, LSTA member status, agent bank identity
- **Credit agreement provisions**: minimum assignment amount, consent requirements (borrower, agent), transfer restrictions, blackout periods, disqualified lender lists
- **LSTA documentation**: applicable form (Par/Distressed Trade Confirmation, Assignment Agreement, Participation Agreement)
- **Settlement instructions**: wire details, custodian/trustee information, CUSIP/LoanX ID (LXID)
- **Market data**: LSTA standard settlement calendar, any buy-in/sell-out notices, current SOFR rate for delayed comp calculations [VERIFY: confirm applicable benchmark rate]

## Workflow

1. **Capture trade terms** — Record counterparties, facility, commitment amount, price, trade date, expected settlement date, and par/distressed designation. Confirm trade type drives the applicable LSTA standard form and settlement window.

2. **Generate trade confirmation** — Prepare the LSTA-form trade confirmation matching the trade type. For par trades, use the LSTA Standard Terms and Conditions for Par/Near Par Trade Confirmations. For distressed trades, use the Distressed Trade Confirmation with the applicable "Agreed Upon Procedures" and credit risk/settlement risk allocation. [VERIFY: confirm current LSTA form version in effect]

3. **Clear assignment prerequisites** — Identify consent requirements under the credit agreement (agent consent, borrower consent if applicable, lender-of-record verification). Check the disqualified lender list. Confirm minimum assignment denomination or obtain sub-minimum waiver if needed. Track KYC/AML documentation submission to the agent bank.

4. **Prepare assignment documentation** — Draft the LSTA-form Assignment and Assumption Agreement (or Fronting/Participation Agreement if assignment is not available). Attach required exhibits: credit agreement schedules, tax forms (W-9/W-8), compliance certificates.

5. **Calculate delayed settlement compensation** — If settlement extends beyond the standard window (T+7 par, T+20 distressed), calculate delayed compensation:
   - **Par trades**: buyer entitled to interest/fees accruing on the traded position from expected settlement date to actual settlement date, minus the seller's cost of carry (funded at the benchmark rate on the purchase price).
   - **Distressed trades**: delayed comp accrues from the "delayed compensation start date" per LSTA terms.
   - Track the applicable rate (typically SOFR + spread) and day count convention (Actual/360). [VERIFY: confirm current LSTA delayed comp methodology and benchmark]

6. **Coordinate settlement execution** — Confirm settlement date with agent bank. Ensure wire instructions are verified. Coordinate simultaneous delivery of assignment effectiveness notice, funding of purchase price, and transfer of position on the agent bank's register. Confirm trade on ClearPar/MarketAxess (if applicable).

7. **Post-settlement reconciliation** — Verify the agent bank has updated the lender-of-record register. Confirm buyer is receiving interest/fee distributions. Reconcile any break amounts (accrued interest true-up, facility fee proration). Document final settlement amounts and archive trade file.

## Output

- **Trade blotter entry** with all economic terms, dates, and counterparty details
- **LSTA trade confirmation** (par or distressed form) fully populated
- **Assignment and Assumption Agreement** with required exhibits and consents tracked
- **Delayed compensation calculation** worksheet showing accrual period, rate, and amounts owed
- **Settlement status tracker** showing each prerequisite (consent, KYC, documentation) with status flags
- **Post-settlement memo** confirming register update, first distribution confirmation, and file close-out

## Quality Checks

- Confirm trade type (par vs. distressed) drives the correct LSTA form and settlement timeline throughout all documents
- Verify purchase price and commitment amount are consistent across confirmation, assignment agreement, and wire instructions
- Validate delayed compensation calculation against LSTA standard methodology — confirm start date, end date, rate, and day count
- Check that all credit agreement consent requirements are satisfied before settlement (agent, borrower, minimum denomination)
- Confirm no disqualified lender or sanctioned party issues with the buyer
- Ensure tax forms (W-8/W-9) are current and match the assigning/assuming entity
- Cross-check settlement amounts: purchase price + accrued interest adjustments + delayed comp = total wire amount
- Flag any open items with [VERIFY] — do not assume consent status, rate applicability, or regulatory clearance without confirmation
