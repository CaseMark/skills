---
name: structuring-fund-of-funds-vehicles
description: Designs fund-of-funds structures with layer-on-layer economics, allocation methodology, and portfolio construction guidelines. Use when structuring FoF vehicles, analyzing layered fee impact, or designing multi-manager programs.
tags:
  - fund-formation-and-structuring
  - portfolio
metadata:
  author: casemark
  practice_areas:
    - Fund Formation
    - Fund Structuring
    - Partnership Law
  document_types:
    - Report
  skill_modes:
    - Analysis
---
# Structuring Fund Of Funds Vehicles

Designs fund-of-funds structures with layer-on-layer economics, allocation methodology, and portfolio construction guidelines.

## When To Use

- Structuring a new fund-of-funds (FoF) vehicle investing across multiple underlying managers or funds
- Evaluating layered fee impact (management fee + carry at both FoF and underlying fund levels)
- Designing allocation methodology for capital deployment across a portfolio of sub-funds
- Analyzing existing FoF structures for economic efficiency, GP/LP alignment, or restructuring
- Building multi-manager or multi-strategy platform vehicles with shared economics

## Inputs To Gather

- **Vehicle parameters**: Target fund size, investor base (institutional vs. HNW), domicile preference (Delaware LP, Cayman, Luxembourg) [VERIFY jurisdiction-specific entity requirements]
- **Underlying fund universe**: Target number of sub-funds, strategy types (PE, VC, credit, real assets), vintage year diversification goals
- **Fee structure at FoF level**: Proposed management fee rate, carry percentage, hurdle rate, catch-up provisions
- **Underlying fund economics**: Typical fee loads of target sub-funds (management fees, carried interest, transaction fees)
- **Allocation policy**: Concentration limits, diversification targets, commitment pacing schedule, over-commitment ratio
- **LP terms**: Side letter expectations, MFN provisions, co-investment rights, reporting cadence
- **Regulatory constraints**: Investment Company Act considerations, ERISA limits, tax pass-through requirements [VERIFY applicable exemptions]

## Workflow

1. **Define vehicle structure and domicile**
   - Select entity type (limited partnership, LLC, offshore feeder) based on investor tax profiles
   - Determine whether a master-feeder, parallel fund, or single-entity structure fits the LP base
   - Identify need for blocker entities for tax-exempt or non-US investors [VERIFY UBTI/ECI exposure]
   - Map out GP entity, management company, and any advisory board governance

2. **Model layered fee economics**
   - Calculate aggregate fee drag: FoF management fee + weighted-average underlying fund management fees
   - Model total carried interest exposure at both layers under base, upside, and downside return scenarios
   - Quantify net-to-LP return differential versus direct fund investing (the "cost of diversification")
   - Evaluate fee offset or rebate mechanisms — pass-through of underlying fund fee breaks, portfolio company fee offsets
   - Test whether FoF-level hurdle rate adequately protects LPs given double-layer carry

3. **Design allocation and commitment methodology**
   - Set target allocation by strategy, geography, vintage year, and manager size
   - Define over-commitment ratio (typically 1.2x–1.5x for PE FoFs) with cash flow modeling to avoid capital calls exceeding available capital
   - Establish concentration limits per underlying fund (commonly 10–20% of FoF commitments)
   - Build re-up and pacing framework — annual deployment targets, reserves for follow-on commitments
   - Specify secondary market and co-investment allocation buckets if applicable

4. **Draft portfolio construction guidelines**
   - Manager selection criteria: track record length, AUM thresholds, key-person requirements, operational due diligence standards
   - Emerging manager allocation carve-out (if any), with distinct underwriting standards
   - Liquidity management: cash reserve policy, credit facility sizing for bridging capital calls
   - Conflict-of-interest policies for GP affiliates in the underlying portfolio

5. **Structure LP terms and governance**
   - Define advisory committee composition, consent rights (related-party transactions, allocation policy changes)
   - Draft side letter framework: fee discounts for anchor LPs, MFN election mechanics
   - Co-investment policy: allocation priority, fee/carry terms on co-invest vehicles
   - Reporting obligations: quarterly NAV, annual audited financials, underlying fund look-through reporting
   - Key-person and cause events at the FoF GP level — triggers and consequences

6. **Address regulatory and tax structuring**
   - Confirm Investment Company Act exemption path (Section 3(c)(1) or 3(c)(7)) [VERIFY investor count and qualification]
   - Assess ERISA "plan asset" exposure — whether underlying funds' VCOC/REOC exemptions flow through [VERIFY benefit plan investor percentage]
   - Structure for tax efficiency: avoid entity-level taxation, manage UBTI for tax-exempt LPs, minimize withholding for non-US investors
   - Evaluate state/local tax obligations and filing requirements [VERIFY nexus rules per jurisdiction]

## Output

Deliver a **FoF Structuring Report** containing:

- **Structure diagram**: Visual map of FoF entity, GP, feeders/blockers, and underlying fund relationships
- **Fee waterfall analysis**: Side-by-side comparison of gross returns, FoF-level fees, underlying fund fees, and net-to-LP returns across scenarios
- **Allocation framework**: Target portfolio by strategy/geography/vintage with concentration limits and pacing schedule
- **Over-commitment model**: Cash flow projections showing commitment capacity versus available capital under stress scenarios
- **Term sheet summary**: Key FoF-level economic and governance terms in tabular format
- **Regulatory checklist**: Exemption analysis and compliance requirements with [VERIFY] flags for jurisdiction-dependent items

## Quality Checks

- Confirm net-to-LP return projections account for all fee layers including organizational expenses and fund-level transaction costs
- Verify over-commitment model stress-tests accelerated capital calls and delayed distributions simultaneously
- Ensure allocation guidelines are internally consistent (percentages sum correctly, concentration limits don't conflict with minimum diversification targets)
- Check that GP clawback and FoF-level waterfall mechanics align — whole-fund vs. deal-by-deal at each layer
- Validate that regulatory exemption analysis reflects current investor composition, not just target composition [VERIFY]
- Confirm side letter MFN provisions don't inadvertently collapse the fee structure across all LPs
- Flag any underlying fund terms that restrict or condition FoF-level transfer, reporting, or co-investment rights
