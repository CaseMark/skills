---
name: analyzing-power-market-structures
description: Evaluates electricity market design with capacity payments, energy margins, ancillary services, and renewable intermittency management. Use when analyzing power markets, evaluating merchant exposure, or assessing capacity market dynamics.
tags:
  - analysis
  - real-assets-and-natural-resources
metadata:
  author: casemark
  practice_areas:
    - Natural Resources
    - Energy Capital
    - Commodity Investment
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Power Market Structures

Evaluates electricity market design with capacity payments, energy margins, ancillary services, and renewable intermittency management.

## When To Use

- Assessing merchant vs. contracted revenue exposure for a generation asset
- Evaluating capacity market participation economics (PJM RPM, ISO-NE FCM, NYISO ICAP) [VERIFY: current auction parameters and delivery years]
- Analyzing energy margin profiles across nodal pricing zones
- Modeling ancillary services revenue (frequency regulation, spinning reserves, voltage support)
- Quantifying intermittency risk for renewables in energy-only vs. capacity markets
- Comparing market structures across ISOs/RTOs for portfolio allocation decisions

## Inputs To Gather

- **Market and ISO identification**: Which ISO/RTO (PJM, ERCOT, CAISO, MISO, ISO-NE, NYISO, SPP) and relevant pricing zones/nodes
- **Asset characteristics**: Technology type, nameplate capacity, heat rate (thermal), capacity factor (renewables), dispatch profile, contract status (merchant vs. PPA vs. tolling)
- **Market data**: Locational marginal prices (LMP) — energy, congestion, and loss components; capacity auction clearing prices; ancillary service clearing rates
- **Fuel and variable cost inputs**: Gas basis differentials, delivered fuel cost, variable O&M, startup costs, emission allowance prices [VERIFY: current allowance pricing for RGGI, state-level carbon programs]
- **Regulatory context**: State-level capacity procurement mandates, clean energy standards, MOPR/buyer-side mitigation rules [VERIFY: current FERC rulings on minimum offer price rules]
- **Forward curves**: Power forwards, gas forwards, heat rate implied curves, capacity price forecasts

## Workflow

1. **Classify market structure**
   - Determine whether the relevant market is energy-only (ERCOT), energy + capacity (PJM, ISO-NE, NYISO), or hybrid with out-of-market payments
   - Identify scarcity pricing mechanisms: ORDC adders (ERCOT), capacity performance penalties (PJM), Pay-for-Performance (ISO-NE)
   - Map applicable ancillary service products and procurement methods

2. **Decompose revenue streams**
   - **Energy margin**: Calculate spark spread (power price minus fuel cost at market heat rate) or dark spread for coal; model hourly dispatch economics against LMP
   - **Capacity revenue**: Identify applicable auction format, qualification requirements, performance obligations, and penalty exposure; assess unforced capacity (UCAP) rating vs. nameplate
   - **Ancillary services**: Quantify regulation, reserves, and reactive power revenue potential based on asset ramp rate, response time, and market clearing data
   - **Renewable energy credits / carbon attributes**: Assess REC pricing, bundled vs. unbundled value, state compliance market dynamics [VERIFY: current REC pricing by state and vintage]

3. **Assess merchant exposure**
   - Quantify percentage of revenue from market-exposed vs. contracted sources
   - Model P10/P50/P90 energy margin scenarios using historical LMP volatility and forward curve distributions
   - Evaluate basis risk between hub pricing (e.g., PJM Western Hub) and nodal settlement points
   - Stress-test capacity revenue under demand destruction, new entry, and regulatory scenarios

4. **Evaluate intermittency and shape risk (renewables)**
   - Analyze hourly generation profile against price shape — identify correlation between output and low-price hours (solar duck curve, wind overnight weighting)
   - Calculate capture rate: effective revenue per MWh versus flat average LMP
   - Model curtailment risk from transmission constraints or negative pricing events
   - Assess storage pairing economics to shift generation into higher-priced intervals

5. **Analyze structural and regulatory risk**
   - Review pending FERC proceedings, state PUC orders, or legislative changes affecting market design [VERIFY]
   - Assess capacity market reform proposals (e.g., seasonal capacity, accreditation methodology changes)
   - Evaluate impact of interconnection queue depth on future supply/demand balance and clearing prices
   - Flag transmission congestion patterns that affect nodal pricing and basis risk

6. **Synthesize findings**
   - Compile revenue stack breakdown with scenario ranges
   - Rank market structure risks by probability and financial impact
   - Provide comparison matrix if evaluating multiple ISOs/markets
   - Deliver clear recommendation on merchant viability, hedging priorities, or contract structuring

## Output

- **Market structure overview**: ISO classification, pricing mechanisms, and key design features
- **Revenue decomposition table**: Energy margin, capacity, ancillary services, and attribute revenue with base/upside/downside cases
- **Merchant risk profile**: Exposure quantification, basis risk assessment, and volatility metrics
- **Capture rate analysis** (renewables): Effective pricing vs. flat average, curtailment exposure, shape risk
- **Regulatory risk register**: Pending proceedings and potential market design changes with estimated impact
- **Recommendation summary**: Actionable conclusions on asset valuation, hedging strategy, or market entry decisions

## Quality Checks

- Confirm LMP data granularity matches analysis requirements (hourly nodal vs. zonal averages)
- Verify capacity auction parameters reflect the correct delivery year and any recent rule changes [VERIFY]
- Cross-check heat rate assumptions against actual plant operating data, not generic benchmarks
- Ensure basis differential calculations use the correct hub-to-node pairing
- Validate that forward curves are sourced from a consistent date and broker consensus
- Confirm ancillary service revenue assumptions reflect actual qualification status, not theoretical eligibility
- Flag any reliance on expired or superseded tariff provisions
