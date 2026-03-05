---
name: managing-syndicated-loan-operations
description: Structures syndicated loan participation with allocation, settlement, and agent bank coordination. Use when managing syndicated loans, processing loan allocations, or coordinating agent bank functions.
tags:
  - management
  - commercial-banking
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
# Managing Syndicated Loan Operations

## When To Use

- Onboarding a new syndicated loan facility and establishing operational workflows across lender groups
- Processing primary allocations after bookrunner finalizes syndicate composition
- Managing secondary trade settlements (par/near-par or distressed) through agent bank coordination
- Handling interest/fee calculations, rate-setting notices, and waterfall distributions across participants
- Coordinating drawdowns, rollovers, prepayments, or amendments requiring lender consent
- Producing operational status reports for agent bank, borrower, or internal credit committees

## Inputs To Gather

- **Credit agreement and related documents**: Facility terms, amortization schedule, pricing grid, fee letter, intercreditor agreement (if applicable)
- **Syndicate composition**: Lender names, commitment amounts, pro-rata shares, fronting/swingline exposure, voting thresholds
- **Trade/allocation data**: Primary allocation notices, secondary trade confirmations (LSTA/LMA standard forms), settlement instructions
- **Rate and payment details**: Reference rate (SOFR/EURIBOR/term rate), spread, interest period elections, day-count convention, payment dates
- **Agent bank details**: Administrative agent identity, sub-agent roles (paying agent, collateral agent), contact and wire information
- **Borrower notices**: Drawdown requests, rollover/conversion notices, prepayment notices, compliance certificates

## Workflow

1. **Map the facility structure**
   - Parse the credit agreement for facility tranches (revolver, term loan A/B, delayed-draw), commitment amounts, and maturity dates
   - Identify voting thresholds: required lenders (typically >50% of commitments), supermajority matters, unanimous consent items
   - Note any accordion/incremental facility provisions and MFN protections [VERIFY against specific credit agreement]

2. **Process allocations and settlements**
   - For primary syndication: validate allocation amounts against total commitment, confirm each lender's pro-rata share, and reconcile with bookrunner's final allocation notice
   - For secondary trades: confirm trade terms (par amount, trade price, settlement date, T+standard per LSTA/LMA), match buyer/seller confirmations, and verify assignment/participation structure
   - Prepare or review assignment and assumption agreements; confirm borrower/agent consent requirements [VERIFY — some facilities allow assignments without borrower consent above a threshold or to existing lenders]

3. **Manage ongoing operations**
   - **Rate setting**: Calculate interest based on the applicable reference rate plus spread, applying the correct day-count convention (ACT/360 for USD, ACT/365 for GBP) [VERIFY convention per credit agreement]
   - **Drawdowns/rollovers**: Process borrower notices within required lead times (typically 3 business days for SOFR loans), allocate across lenders pro rata, and issue funding notices
   - **Prepayments**: Distinguish mandatory prepayments (excess cash flow sweep, asset sale proceeds) from voluntary prepayments; apply to tranches per the waterfall specified in the credit agreement
   - **Fee calculations**: Compute commitment fees on unused commitments, letter of credit fees, fronting fees, and agent fees per the fee letter schedule

4. **Coordinate agent bank functions**
   - Distribute interest and fee payments to lenders via wire transfer on each payment date
   - Maintain the lender register (official record of assignments and commitments)
   - Circulate borrower compliance certificates and financial statements to the syndicate
   - Process amendment/waiver requests: track lender votes against required thresholds, manage consent deadlines, and issue effectiveness notices

5. **Compile operational reporting**
   - Produce a facility summary showing current outstandings, available commitments, accrued interest/fees, and upcoming payment dates
   - Generate a lender position report with each participant's commitment, funded amount, pro-rata share, and unfunded obligation
   - Flag any operational exceptions: late payments, documentation gaps, pending consent items, or upcoming maturity/amortization events

## Output

- **Facility operations summary**: Tranche-level breakdown of commitments, outstandings, pricing, and key dates
- **Lender position schedule**: Participant-by-participant allocation with pro-rata percentages and contact/wire details
- **Payment/distribution ledger**: Interest, fees, and principal payments calculated per lender share with supporting rate and day-count detail
- **Action items and exception log**: Pending trades awaiting settlement, consent requests in progress, documentation deficiencies, and upcoming operational deadlines

## Quality Checks

- Verify that all lender commitments sum to the total facility size for each tranche
- Confirm pro-rata shares are calculated consistently and reconcile to 100%
- Cross-check reference rate fixings against published sources (e.g., CME Term SOFR, Bloomberg) on each rate-setting date
- Validate day-count convention and business day convention against the credit agreement [VERIFY]
- Ensure payment waterfalls follow the contractual priority of payments, especially for mandatory prepayments
- Confirm assignment minimum thresholds (typically $1M–$5M) and any restrictions on eligible assignees [VERIFY per credit agreement]
- Flag any discrepancies between trade confirmations and agent bank records before settlement
- Mark jurisdiction-specific regulatory requirements (e.g., KYC/AML for new lenders, withholding tax forms) with [VERIFY]
