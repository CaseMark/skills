---
name: analyzing-payment-flows
language: en
description: Structures payment system analysis with transaction flow mapping, interchange economics, and settlement timing. Use when analyzing payment systems, mapping transaction flows, or understanding interchange.
tags:
  - analysis
  - financial-technology
metadata:
  author: casemark
  practice_areas:
    - Fintech
    - Payments
    - Digital Banking
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Payment Flows

Structures payment system analysis with transaction flow mapping, interchange economics, and settlement timing.

## When To Use

- Mapping end-to-end transaction flows for a payment product (card-present, card-not-present, ACH, RTP, wire, wallet-based)
- Evaluating interchange economics, scheme fees, and processor margins for a given payment method
- Analyzing settlement timing and funding lag across acquirer, network, and issuer
- Comparing payment rail options (card networks, ACH/Nacha, FedNow, SWIFT, SEPA) for a specific use case
- Reviewing payment architecture during due diligence, vendor selection, or platform migration
- Investigating transaction failure rates, decline codes, or reconciliation gaps

## Inputs To Gather

- **Payment method(s) in scope**: Card (Visa/Mastercard/Amex), ACH (same-day vs. standard), RTP, wire, digital wallet, BNPL, or hybrid
- **Transaction type**: Purchase, refund, chargeback, recurring/subscription, disbursement, P2P transfer
- **Participants**: Cardholder/payer, merchant/payee, issuer, acquirer/processor, payment network/scheme, gateway, PSP, sponsor bank
- **Volume and ticket size**: Average transaction value, monthly volume, peak patterns
- **Geography and currency**: Domestic vs. cross-border, single-currency vs. multi-currency [VERIFY — interchange categories and scheme rules differ by region]
- **Existing documentation**: Network rules, processor agreements, fee schedules, settlement reports, reconciliation logs

## Workflow

1. **Define the transaction lifecycle**
   - Identify every entity that touches the transaction from initiation to final settlement
   - Map the authorization request path: payer → gateway → acquirer/processor → network → issuer → response back
   - Map the clearing and settlement path separately (batch vs. real-time, net vs. gross settlement)
   - Note where tokenization, 3DS authentication, or fraud screening inserts into the flow

2. **Break down interchange and fee economics**
   - Identify the interchange category (e.g., CPS Retail, e-Commerce Preferred, Data Rate II) based on transaction qualifications [VERIFY — interchange tables are network-specific and updated semi-annually]
   - Layer on scheme/assessment fees (network access, NABU/APF for Visa, NABU equivalent for Mastercard)
   - Add acquirer/processor markup (basis points + per-transaction fee)
   - Calculate effective merchant discount rate (MDR) = interchange + scheme fees + acquirer markup
   - For ACH: map Nacha fees, ODFI/RDFI fees, and return/NOC handling costs

3. **Analyze settlement timing and funding**
   - Document T+N settlement windows for each rail (card networks typically T+1 or T+2; ACH standard T+1 to T+2; same-day ACH same-day with cutoff windows; RTP/FedNow near-real-time) [VERIFY — settlement timing varies by processor agreement and network]
   - Identify holdback or reserve requirements imposed by acquirer or PSP
   - Map net settlement vs. gross settlement mechanics and their cash-flow impact
   - Flag any funding-lag risks (weekend/holiday gaps, cross-border settlement delays, currency conversion timing)

4. **Identify failure points and risk vectors**
   - Map common decline reasons at authorization (insufficient funds, fraud flags, AVS/CVV mismatch, velocity limits)
   - Trace chargeback and dispute flows with timelines (120-day liability windows for card, 60-day ACH return windows) [VERIFY — dispute windows vary by network and reason code]
   - Identify reconciliation break points between gateway, processor, and bank settlement reports
   - Note regulatory touchpoints: PCI DSS scope, Reg E for consumer electronic transfers, EFTA protections, Durbin Amendment routing requirements

5. **Synthesize findings and recommendations**
   - Summarize the cost stack per transaction with a unit-economics table
   - Highlight optimization opportunities (interchange qualification improvements, surcharging/cash discount programs, rail switching for specific transaction types)
   - Quantify settlement timing impact on working capital
   - Flag compliance or operational risks that require remediation

## Output

Deliver a structured payment flow analysis containing:

- **Transaction flow diagram** (text-based): Authorization path and clearing/settlement path shown as sequential participant-to-participant steps
- **Fee economics table**: Interchange rate, scheme fees, processor markup, and total MDR per transaction type
- **Settlement timeline**: T+N summary per rail with funding-lag analysis
- **Failure and risk map**: Decline categories, dispute exposure windows, and reconciliation gap areas
- **Recommendations**: Ranked list of cost optimization, speed improvement, and risk mitigation actions

## Quality Checks

- Every participant in the flow is explicitly named — no black-box "processor handles it" steps
- Interchange categories cited match the transaction qualifications described (card type, entry mode, data level) [VERIFY]
- Settlement timing reflects actual processor/network terms, not generic assumptions
- Fee calculations are additive and auditable (interchange + scheme + markup = MDR)
- Cross-border flows separately address FX conversion timing and markup if applicable
- All network-specific rules and regulatory thresholds are marked [VERIFY] for jurisdiction-dependent confirmation
- Chargeback/dispute timelines reference the correct network reason code families, not generic windows
