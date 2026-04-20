---
name: analyzing-credit-derivative-structures
language: en
description: Evaluates CDS, CDX, and bespoke credit derivative structures with spread analysis and credit event mechanics. Use when analyzing credit derivatives, pricing CDS, or evaluating index tranche products.
tags:
  - analysis
  - derivatives-and-structured-products
  - credit
metadata:
  author: casemark
  practice_areas:
    - Derivatives
    - Structured Products
    - Hedging
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Credit Derivative Structures

Evaluates CDS, CDX, and bespoke credit derivative structures with spread analysis and credit event mechanics.

## When To Use

- Pricing or re-marking single-name CDS contracts on corporate or sovereign reference entities
- Analyzing CDX or iTraxx index positions, including on-the-run vs. off-the-run roll dynamics
- Evaluating bespoke tranche opportunities (equity, mezzanine, senior) on synthetic CDO portfolios
- Assessing basis trades (CDS vs. cash bond spread) for relative-value positioning
- Reviewing credit event determination mechanics (failure to pay, restructuring, bankruptcy) and settlement protocols
- Hedging concentrated credit exposures with single-name or index overlays

## Inputs To Gather

- **Reference entity / obligation details**: entity name, ticker, RED code, reference obligation (bond CUSIP/ISIN), seniority (senior unsecured, subordinated), currency
- **Contract terms**: trade date, effective date, scheduled termination, notional amount, fixed coupon (100 bps or 500 bps standard), payment frequency, day-count convention (ACT/360)
- **Market data**: current CDS spread (mid), bid/ask, recovery rate assumption, credit curve term structure (1Y–10Y), ISDA benchmark quotes
- **Index details (if applicable)**: index series and version, on-the-run status, constituent list, factor (for partially defaulted indices), attachment/detachment points for tranches
- **Counterparty / CSA terms**: collateral thresholds, eligible collateral, minimum transfer amount, independent amounts
- **Credit event history**: any prior succession events, restructuring triggers, or ISDA DC determinations on the reference entity

## Workflow

1. **Identify product type and contract terms**
   - Classify as single-name CDS, index (CDX IG, CDX HY, iTraxx Europe, iTraxx Crossover), or bespoke tranche
   - Confirm ISDA documentation version (2003 vs. 2014 definitions) and applicable credit event types [VERIFY]
   - Note whether the contract uses Standard North American (SNA) or Standard European (SE) conventions

2. **Build or validate the credit curve**
   - Source CDS spreads across the term structure from dealer runs or market data vendors
   - Bootstrap hazard rates (default intensity) from quoted spreads using the ISDA Standard Model
   - Confirm recovery rate assumption — 40% for senior unsecured corporate, 25% for subordinated, 25% for sovereign (standard assumptions; adjust if market-implied recovery differs) [VERIFY]

3. **Price the contract / calculate mark-to-market**
   - Compute the risky PV of the premium leg (fixed coupon stream) and the contingent leg (protection payment upon credit event)
   - MTM = PV(contingent leg) − PV(premium leg) for the protection buyer; sign-flip for seller
   - For upfront-trading names (HY or distressed), convert running spread to upfront points using the ISDA Standard Model with the 500 bps fixed coupon
   - For index tranches, use a correlation model (Gaussian copula base correlation framework) to price attachment/detachment points

4. **Analyze spread dynamics and sensitivities**
   - CS01 (credit spread sensitivity): PV change per 1 bp parallel shift in the credit curve
   - CR01 (recovery rate sensitivity): PV change per 1% change in assumed recovery
   - Jump-to-default (JTD) exposure: loss upon immediate credit event net of recovery
   - Carry and roll-down: accrued premium income vs. expected curve roll over holding period
   - For index positions, decompose risk into systematic (index-level) and idiosyncratic (single-name) components

5. **Evaluate credit event mechanics**
   - Map applicable credit events under the contract's ISDA definitions: bankruptcy, failure to pay (with grace period and payment threshold), restructuring type (CR, MR, MMR, NR) [VERIFY]
   - Review ISDA Determinations Committee (DC) process for triggering credit events and auction settlement
   - For restructuring credit events, check maturity limitation dates and deliverable obligation characteristics
   - Assess physical vs. cash settlement protocols and deliverable obligation criteria (not bearer, not contingent, specified currencies)

6. **Assess basis and relative value (if applicable)**
   - Calculate CDS-bond basis: CDS spread minus asset-swap spread (or Z-spread) on the reference obligation
   - Identify drivers of basis (funding costs, repo availability, delivery option, counterparty risk, regulatory capital)
   - For negative basis trades, evaluate carry profile, financing cost, and unwind scenarios
   - For index vs. intrinsics, compare index spread to the notional-weighted average of constituent single-name spreads (skew)

7. **Review counterparty and operational risk**
   - Evaluate CSA terms: collateral posting frequency, dispute resolution, rehypothecation rights
   - Check for wrong-way risk (correlation between counterparty default and reference entity credit deterioration)
   - Confirm trade is cleared through a CCP (ICE Clear Credit, LCH) or bilateral, and note initial margin requirements [VERIFY]

## Output

- **Structure summary**: product type, reference entity, notional, tenor, coupon, documentation version
- **Valuation table**: current spread, upfront amount, MTM, accrued premium
- **Risk metrics**: CS01, CR01, JTD, DV01, carry/roll-down over 1M/3M/6M horizons
- **Credit event analysis**: applicable events, settlement type, key contractual triggers and thresholds
- **Basis / relative value assessment** (if applicable): current basis level, historical percentile, trade P&L scenarios
- **Key risks and caveats**: model assumptions, liquidity considerations, counterparty exposure, regulatory capital impact

## Quality Checks

- Verify that the ISDA definitions version and credit event types match the actual confirmation or master agreement [VERIFY]
- Confirm hazard rate bootstrapping reproduces quoted market spreads within 0.25 bps tolerance
- Cross-check upfront pricing against at least one independent source (dealer quote, Markit, Bloomberg CDSW)
- Ensure recovery rate assumption is consistent across pricing, JTD calculation, and scenario analysis
- Validate that index factor and constituent weights are current (post any credit events or succession events)
- For tranche products, confirm that base correlation inputs are sourced from liquid tranche quotes and that interpolation methodology is documented
- Flag any reference entities on ISDA DC watch list or with near-term maturity of the cheapest-to-deliver obligation
