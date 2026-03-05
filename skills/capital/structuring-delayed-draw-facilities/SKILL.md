---
name: structuring-delayed-draw-facilities
description: Designs delayed-draw term loan structures with commitment fees, draw conditions, and availability period mechanics. Use when structuring DDTL facilities, designing draw-down mechanisms, or analyzing delayed-draw economics.
tags:
  - credit-and-institutional-lending
metadata:
  author: casemark
  practice_areas:
    - Credit Markets
    - Leveraged Lending
    - Direct Lending
  document_types:
    - Report
  skill_modes:
    - Analysis
---
# Structuring Delayed Draw Facilities

Designs delayed-draw term loan structures including commitment fee mechanics, draw-down conditions, availability periods, and economic analysis for leveraged and direct lending transactions.

## When To Use

- Structuring a delayed-draw term loan (DDTL) tranche alongside a closing-date term loan or revolver
- Designing draw-down mechanics for acquisition financing with identified but unsigned bolt-on targets
- Evaluating commitment fee structures and ticking fee step-ups during the availability window
- Analyzing borrower-side cost of carry vs. lender-side yield implications of delayed-draw economics
- Reviewing DDTL provisions in existing credit agreements for amendment or repricing transactions

## Inputs To Gather

- **Transaction context**: Sponsor/borrower name, transaction type (LBO, add-on, recap), total capital structure
- **DDTL sizing**: Committed amount, relationship to total first-lien or unitranche facility
- **Availability period**: Outside date, any extension mechanics, permitted draw schedule (single vs. multiple draws)
- **Draw conditions**: Conditions precedent to each draw (e.g., acquisition consummation, pro forma compliance, material adverse change carve-outs, officer certificates)
- **Pricing terms**: Applicable margin (matching or spread to initial TL), OID on funded draws, commitment/ticking fee rate and step-up schedule
- **Amortization and maturity**: Whether drawn amounts share the same amortization schedule and maturity as the initial term loan
- **Credit agreement provisions**: MFN protections, sunset provisions, fungibility with initial TL after funding
- **Lender syndication context**: Whether DDTL is held by the same lender group or separately syndicated

## Workflow

1. **Map the capital structure** — Position the DDTL within the overall debt stack. Identify the initial term loan, any revolver, and where the DDTL sits in priority, maturity, and margin relative to other tranches.

2. **Define the availability window** — Specify the start date (typically closing), outside draw date, minimum/maximum draw amounts, and whether partial draws are permitted. Flag whether unused commitments terminate automatically at the outside date or require affirmative cancellation.

3. **Structure draw conditions** — Draft or review conditions precedent for each draw request:
   - Pro forma leverage ratio compliance (specify test level and calculation methodology) [VERIFY: confirm whether ratio is tested on a pro forma basis including the acquired EBITDA]
   - No default or event of default at draw date
   - Accuracy of representations (specify which reps must be accurate — "material" vs. full bring-down)
   - Delivery of acquisition-related documents (purchase agreement, officer certificate, legal opinions)
   - Minimum draw amounts and notice periods (typically 3–5 business days)

4. **Design fee economics** — Model the commitment fee and ticking fee structure:
   - **Commitment fee**: Flat rate on undrawn DDTL commitments from closing (typical range: 50–100% of applicable margin) [VERIFY: market rate for comparable credits]
   - **Ticking fee step-up**: Whether the fee increases after a specified period (e.g., 50 bps for first 6 months, stepping to 100 bps thereafter)
   - **OID on funding**: Whether drawn amounts are funded at par or at a discount matching the initial TL OID
   - **MFN protection**: Spread and OID floors that apply if the DDTL margin exceeds the initial TL margin by more than a specified threshold (commonly 50 bps)

5. **Address fungibility and post-draw treatment** — Determine whether funded DDTL amounts are treated as a single tranche with the initial term loan for voting, amortization, prepayment waterfall, and CUSIP purposes. Specify whether the DDTL has a separate CUSIP during the availability period.

6. **Analyze borrower cost of carry** — Calculate the total cost to the borrower of maintaining the undrawn commitment versus drawing at closing, accounting for commitment fees, ticking fees, potential OID differential, and interest savings on unfunded amounts. Compare against alternative structures (e.g., an incremental facility or accordion).

7. **Assess lender-side economics** — Evaluate the yield profile for lenders holding DDTL commitments: fee income during the availability period, deployment risk, and blended yield if drawn at various points in the window.

## Output

Deliver a structured DDTL analysis containing:

- **Term sheet / structure summary**: DDTL size, availability period, draw mechanics, fee schedule, and conditions precedent in term-sheet format
- **Fee economics table**: Commitment fee, ticking fee schedule, OID, and effective cost of carry across scenarios (draw at month 3, 6, 9, expiry)
- **Comparison matrix**: DDTL vs. incremental facility vs. accordion — cost, certainty, conditionality, and flexibility trade-offs
- **Key negotiation points**: Flagged provisions where borrower and lender interests diverge (e.g., breadth of draw conditions, MFN sunset, partial draw minimums)
- **[VERIFY] markers** on jurisdiction-specific items: UCC perfection requirements for delayed-draw collateral, tax withholding on commitment fees [VERIFY], and regulatory capital treatment for lender bank holding companies [VERIFY]

## Quality Checks

- Confirm commitment fee calculation methodology matches credit agreement definitions (365-day vs. 360-day basis) [VERIFY]
- Verify MFN protection mechanics — confirm whether the sunset applies from closing or from the first DDTL draw date
- Cross-check that draw conditions do not inadvertently block draws for permitted acquisitions that were part of the original underwriting
- Ensure amortization and prepayment provisions correctly incorporate funded DDTL amounts into the existing schedule
- Validate that the availability period outside date aligns with the anticipated timeline for the identified use of proceeds
- Flag any inconsistencies between DDTL provisions and the corresponding sections of the initial term loan (definitions, events of default, covenant levels)
