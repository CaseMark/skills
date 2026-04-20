---
name: managing-clearing-and-settlement
language: en
description: Structures central clearing analysis with CCP margin methodology and default waterfall assessment. Use when managing clearing relationships, analyzing CCP margins, or evaluating default waterfalls.
tags:
  - management
  - quantitative-finance
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
# Managing Clearing And Settlement

Structures central clearing analysis with CCP margin methodology and default waterfall assessment.

## When To Use

- Onboarding to a new CCP or evaluating whether to clear a product through a specific clearinghouse
- Reviewing initial margin (IM) and variation margin (VM) requirements across CCPs for portfolio optimization
- Assessing default waterfall exposure and loss-allocation mechanisms after a clearing member default event
- Evaluating changes to CCP margin models (e.g., SPAN to VaR-based, PRISMA, CME CORE)
- Preparing management reporting on clearing costs, margin efficiency, and settlement risk
- Responding to regulatory inquiries on clearing obligations under EMIR, Dodd-Frank Title VII, or equivalent regimes [VERIFY jurisdiction-specific clearing mandates]

## Inputs To Gather

- **Portfolio data**: Cleared positions by CCP, product, and currency — including notional, tenor, and directionality
- **Margin statements**: Current IM, VM, and add-on charges (liquidity, concentration, wrong-way risk) from each CCP
- **Default fund contributions**: Clearing member guarantee fund (GF) assessments and any unfunded commitment obligations
- **CCP rulebooks**: Relevant sections on margin methodology, default management procedures, and loss-allocation rules
- **Settlement instructions**: SSI details, payment netting agreements, and settlement cycle timelines (T+0, T+1, T+2)
- **Regulatory context**: Applicable clearing mandates, capital treatment of cleared exposures (SA-CCR, CEM), and reporting obligations [VERIFY regulatory regime]

## Workflow

1. **Map the clearing landscape**
   - Inventory all cleared products and the CCPs servicing them
   - Identify which positions are subject to mandatory clearing vs. voluntarily cleared
   - Document clearing member vs. client clearing relationships and any intermediary FCM/GCM structures

2. **Analyze margin methodology**
   - For each CCP, identify the margin model in use (historical VaR, filtered historical simulation, SPAN, etc.)
   - Compare IM levels across CCPs for equivalent products — note margin period of risk (MPOR) assumptions
   - Assess add-on charges: concentration margins, liquidity charges, and any discretionary add-ons applied by the CCP risk team
   - Evaluate cross-margining and portfolio margining offsets available across asset classes

3. **Assess default waterfall and loss allocation**
   - Map each CCP's default waterfall: defaulter's margin → defaulter's GF contribution → CCP skin-in-the-game → non-defaulting members' GF → assessment powers → resolution tools
   - Quantify the firm's maximum exposure at each waterfall layer (funded GF + unfunded assessments + VM gains haircutting if applicable)
   - Stress-test exposure under hypothetical member default scenarios — identify whether CCP uses loss allocation via VMGH (variation margin gains haircutting), partial tear-up, or forced allocation [VERIFY CCP-specific rules]

4. **Evaluate settlement risk**
   - Review settlement cycles and identify any mismatches between trade execution and settlement finality
   - Assess payment-vs-payment (PvP) and delivery-vs-payment (DvP) protections in place
   - Flag any FX settlement risk (CLS eligibility, non-CLS currency exposures)
   - Document netting efficiency — bilateral vs. multilateral netting ratios

5. **Compile management report**
   - Summarize total margin posted across all CCPs with breakdowns by product, currency, and margin type
   - Present default fund exposure and worst-case loss-allocation scenarios
   - Highlight margin optimization opportunities (compression, cross-margining, clearing venue switches)
   - Include cost analysis: CCP fees, FCM clearing commissions, and funding cost of margin

## Output

The deliverable is a **Clearing and Settlement Management Report** containing:

- **CCP relationship summary**: Clearinghouses used, products cleared, and clearing access model (direct member vs. client)
- **Margin analysis**: IM/VM breakdown by CCP with trend analysis, margin model descriptions, and cross-CCP comparisons
- **Default waterfall assessment**: Layer-by-layer exposure quantification with stress scenario results
- **Settlement risk profile**: Settlement cycle mapping, netting ratios, and any identified settlement failures or near-misses
- **Optimization recommendations**: Actionable steps to reduce margin costs, improve netting, or rebalance clearing venue allocation
- **Risk flags**: Items requiring escalation — model changes, increased add-ons, regulatory developments, or CCP credit concerns

## Quality Checks

- Confirm all margin figures reconcile to CCP margin statements within tolerance
- Verify default fund contribution amounts against the latest CCP assessment notices
- Ensure margin model descriptions match current CCP methodology (CCPs update models periodically — check effective dates)
- Cross-check clearing mandate applicability against current regulatory scope [VERIFY product and counterparty exemptions]
- Validate that settlement instructions and SSIs are current and have been confirmed by operations
- Confirm that any cost figures (fees, funding rates) reflect current agreements, not stale rate cards
