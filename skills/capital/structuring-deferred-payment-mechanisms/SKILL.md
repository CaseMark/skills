---
name: structuring-deferred-payment-mechanisms
language: en
description: Designs deferred and contingent payment structures for secondary transactions with earnout mechanics and escrow arrangements. Use when structuring deferred payments, designing earnout mechanisms, or managing payment timing.
tags:
  - secondaries-and-gp-led
metadata:
  author: casemark
  practice_areas:
    - Secondaries
    - GP-Led Transactions
    - LP Portfolio Management
  document_types:
    - Report
  skill_modes:
    - Analysis
---
# Structuring Deferred Payment Mechanisms

## When To Use

- Structuring purchase price in LP portfolio sales where buyer and seller disagree on NAV or asset valuation
- Designing earnout mechanics for GP-led continuation fund transactions tied to future fund performance
- Building escrow arrangements to cover indemnification obligations, NAV true-ups, or clawback exposure
- Bridging bid-ask spreads in secondary transactions through contingent payment components
- Addressing stale NAV risk when closing occurs well after reference date pricing

## Inputs To Gather

- **Transaction type**: LP interest sale, GP-led continuation vehicle, direct secondary, or preferred equity
- **Reference NAV and date**: Most recent audited or unaudited NAV, how stale the pricing is, and any known material events since valuation date
- **Bid-ask gap**: Spread between buyer's offered price and seller's target, expressed as % of NAV
- **Underlying fund details**: Fund vintage, strategy, remaining life, distribution pace, unfunded commitments, and GP track record
- **Portfolio composition**: Concentration risk, asset-level liquidity profiles, public vs. private mix
- **Buyer requirements**: IRR targets, preferred return thresholds, maximum deferred exposure tolerance
- **Seller constraints**: Minimum upfront cash needs, regulatory capital treatment of deferred amounts, and accounting treatment preferences
- **Credit and counterparty risk**: Buyer creditworthiness, need for credit support or collateral

## Workflow

1. **Quantify the valuation gap** — Decompose the bid-ask spread into identifiable risk components (stale NAV risk, concentration risk, J-curve exposure, unfunded commitment liability). Assign a dollar range to each component to determine how much of the gap deferred structures need to bridge.

2. **Select deferred mechanism type**:
   - **Escrow holdback**: Fixed percentage (typically 5–15% of purchase price) held in escrow pending NAV true-up, indemnification period, or resolution of a specific contingency. Best for known, time-bounded risks.
   - **Earnout / contingent value right (CVR)**: Additional payments triggered when underlying fund distributions exceed agreed thresholds (e.g., buyer receives first X% IRR, then seller participates in upside). Best for bridging genuine disagreement on future performance.
   - **Deferred purchase price installments**: Scheduled payments over 12–36 months, often tied to distribution waterfall from the acquired interests. Best when buyer needs to fund from portfolio cash flows.
   - **Seller note / seller financing**: Promissory note for a portion of purchase price, with or without interest, sometimes subordinated to buyer's other financing. Best when buyer has limited upfront capital.
   - **Preferred equity strip**: Seller retains a preferred return position in a continuation vehicle. Common in GP-led transactions.

3. **Define trigger events and measurement mechanics**:
   - Specify measurement dates, calculation agents, and dispute resolution for each contingent payment
   - For earnouts, define the performance metric (fund-level IRR, MOIC, or distribution-based), measurement period, and cap/floor
   - For escrow, define release conditions, partial release schedules, and claim procedures
   - For NAV true-ups, specify which NAV report controls (audited vs. unaudited) and adjustment methodology

4. **Structure credit protection**:
   - Assess whether deferred amounts need collateral, letters of credit, or guarantees
   - For seller notes, determine security interest, subordination, and acceleration triggers
   - For escrow, select escrow agent and define investment parameters for escrowed funds
   - Consider buyer's fund-level obligations and whether distributions can be directed to satisfy deferred payments

5. **Model economic outcomes** — Run scenario analysis across base, upside, and downside cases showing effective purchase price as % of NAV under each scenario. Calculate buyer IRR and seller total proceeds under each outcome. Verify the structure does not create misaligned incentives (e.g., buyer incentivized to delay distributions to reduce earnout).

6. **Address tax and regulatory considerations**:
   - Determine whether deferred payments create installment sale treatment [VERIFY: jurisdiction-specific tax treatment]
   - For regulated sellers (insurers, banks, pension funds), confirm balance sheet treatment of deferred receivables [VERIFY: applicable accounting standards — GAAP vs. IFRS]
   - Assess withholding tax implications for cross-border transactions [VERIFY: treaty applicability]

7. **Draft term summary** — Produce a structured summary of the deferred payment mechanism for inclusion in LOI, PSA, or side letter.

## Output

Deliver a structured report containing:

- **Mechanism summary table**: Type of deferred component, notional amount, trigger conditions, payment timeline, and credit support for each element
- **Scenario analysis matrix**: Effective price as % of NAV, buyer IRR, and seller total proceeds across at least three scenarios (downside, base, upside)
- **Key terms sheet**: Measurement dates, calculation methodology, dispute resolution, escrow release schedule, and cap/floor provisions
- **Risk allocation map**: Which party bears each identified risk (stale NAV, concentration, J-curve, counterparty credit, FX) and how the deferred structure addresses it
- **Open items and [VERIFY] flags**: Jurisdiction-dependent tax treatment, regulatory capital implications, and any inputs requiring confirmation

## Quality Checks

- Confirm that the total of upfront payment plus maximum deferred/contingent payments equals or brackets the agreed headline price range
- Verify earnout formulas do not create perverse incentives (e.g., buyer withholding capital calls to manipulate MOIC)
- Ensure escrow holdback percentages are market-appropriate for the transaction type and risk profile
- Check that measurement mechanics are objective and verifiable — avoid subjective triggers that invite disputes
- Validate that deferred payment timing aligns with expected distribution pace of underlying assets
- Confirm credit protection is proportionate to counterparty risk and deferred payment duration
- Flag any assumption about NAV, distribution pace, or fund life that has not been confirmed by the GP or auditor with [VERIFY]
