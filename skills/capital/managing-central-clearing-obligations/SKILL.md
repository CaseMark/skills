---
name: managing-central-clearing-obligations
language: en
description: Coordinates central clearing requirements with CCP selection, margin optimization, and clearing threshold monitoring. Use when managing clearing obligations, optimizing CCP selection, or analyzing clearing economics.
tags:
  - management
  - derivatives-and-structured-products
metadata:
  author: casemark
  practice_areas:
    - Derivatives
    - Structured Products
    - Hedging
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Central Clearing Obligations

Coordinates central clearing requirements across CCP selection, margin optimization, clearing threshold monitoring, and regulatory compliance for OTC derivatives portfolios.

## When To Use

- Evaluating whether new or existing derivative positions trigger mandatory clearing obligations under Dodd-Frank Title VII, EMIR, or equivalent regimes [VERIFY jurisdiction-specific thresholds]
- Selecting or re-evaluating central counterparties (CCPs) for cleared swap portfolios
- Optimizing initial margin (IM) and variation margin (VM) across clearing accounts
- Monitoring aggregate notional positions against clearing threshold triggers (e.g., EMIR Category 3/4 thresholds) [VERIFY current threshold amounts]
- Analyzing clearing economics: fee structures, margin offsets, and capital treatment under SA-CCR or CEM
- Preparing for clearing mandate expansions to new product classes or jurisdictions

## Inputs To Gather

- **Portfolio data**: Trade-level detail for all OTC derivatives — product type, notional, tenor, counterparty, current clearing status
- **Threshold tracking**: Aggregate gross notional by asset class (IR, Credit, FX, Equity, Commodity) for clearing determination calculations
- **CCP information**: Eligible CCPs per product, fee schedules, margin methodologies (e.g., SPAN, PRISMA, VaR-based), default fund contributions
- **Margin data**: Current IM/VM postings per CCP, eligible collateral schedules, haircut tables, and cross-margining arrangements
- **Regulatory filings**: Most recent NFC/FC classification, clearing obligation notifications, any exemption elections (intragroup, pension fund) [VERIFY applicable exemptions by jurisdiction]
- **FCM/clearing broker details**: Clearing agreements, customer margin segregation model (LSOC, individual, omnibus), portability provisions

## Workflow

1. **Classify clearing obligation status**
   - Determine entity classification (swap dealer, MSP, financial counterparty, NFC+/NFC−) under each applicable regime
   - Calculate aggregate notional by asset class against clearing thresholds
   - Identify trades subject to mandatory clearing vs. voluntarily cleared vs. bilateral
   - Flag any exemption elections in effect (intragroup, hedging, pension scheme) [VERIFY exemption validity and expiry]

2. **Evaluate CCP selection and access model**
   - Map clearable products to available CCPs (e.g., LCH SwapClear, CME, Eurex, JSCC)
   - Compare margin methodologies — assess netting efficiency and portfolio margining benefits across CCPs
   - Evaluate access model: direct clearing member vs. client clearing via FCM
   - Review default waterfall exposure, default fund sizing, and loss mutualization risk per CCP
   - Assess CCP recovery and resolution frameworks and QCCP status for capital purposes

3. **Optimize margin and collateral**
   - Analyze IM requirements under each CCP's model; identify compression and netting opportunities
   - Evaluate cross-margining programs (e.g., CME–LCH basis, futures-swaps offsets)
   - Review eligible collateral schedules and optimize collateral allocation by cheapest-to-deliver
   - Calculate margin period of risk and liquidity buffer requirements
   - Model impact of trade allocation across CCPs on total margin consumption

4. **Analyze clearing economics**
   - Build total cost comparison: CCP fees (trade registration, maintenance, compression runs), FCM commissions, margin funding cost, capital charges (SA-CCR RWA for cleared exposures at 2% or 4% risk weight) [VERIFY current risk weight under applicable capital framework]
   - Compare bilateral vs. cleared all-in economics for each product type
   - Assess netting set efficiency gains from consolidating clearing at fewer CCPs vs. diversification benefits

5. **Monitor and report**
   - Track threshold proximity — set early warning alerts at 80% and 90% of clearing thresholds
   - Monitor CCP margin calls, intraday calls, and default fund adjustments
   - Report clearing status by product, CCP, and counterparty to front office, risk, and compliance
   - Track regulatory developments: new clearing mandates, margin rule phase-ins, CCP supervisory actions

## Output

- **Clearing obligation matrix**: Product-level table showing clearing status (mandatory/voluntary/exempt), applicable CCP(s), and regulatory basis
- **CCP comparison analysis**: Side-by-side comparison of CCPs by margin efficiency, cost, netting benefit, and operational considerations
- **Margin optimization report**: Current vs. optimized margin allocation, collateral utilization, and projected savings from compression or rebalancing
- **Threshold monitoring dashboard**: Current notional vs. clearing thresholds by asset class with trend and alert status
- **Economics summary**: All-in cost of clearing per product type, bilateral vs. cleared comparison, and recommendations on clearing venue allocation

## Quality Checks

- Confirm all notional figures are current (T or T-1) and reconciled to risk systems
- Verify CCP fee schedules and margin parameters reflect latest published rates [VERIFY against CCP rulebook effective date]
- Validate clearing threshold calculations use the correct netting and exclusion methodology per regime
- Cross-check exemption elections against regulatory filing records and expiry dates
- Ensure margin optimization recommendations do not create unacceptable concentration risk at a single CCP
- Confirm capital treatment assumptions align with the firm's applicable prudential framework (CRR/CRD, US Basel III) [VERIFY]
