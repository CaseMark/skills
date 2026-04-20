---
name: analyzing-midstream-infrastructure-assets
language: en
description: Evaluates midstream assets with throughput analysis, fee-based vs commodity-exposed revenue, and contract structure assessment. Use when analyzing midstream investments, evaluating pipeline assets, or assessing gathering systems.
tags:
  - analysis
  - real-assets-and-natural-resources
  - investment
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
# Analyzing Midstream Infrastructure Assets

Evaluates midstream assets with throughput analysis, fee-based vs commodity-exposed revenue, and contract structure assessment.

## When To Use

- Underwriting a pipeline, gathering system, processing plant, or terminal acquisition
- Evaluating an MLP or midstream C-corp equity or debt investment
- Assessing dropdown candidates within a sponsor/MLP structure
- Benchmarking contract quality across a midstream portfolio
- Reviewing counterparty concentration and basin-level production risk

## Inputs To Gather

- **Asset description**: asset type (pipeline, gathering, processing, fractionation, terminal), diameter/capacity, geography, interconnects
- **Throughput data**: historical monthly/quarterly volumes (Mcf/d, bbl/d), capacity utilization rates, and seasonal patterns
- **Contract book**: shipper agreements, acreage dedications, MVCs (minimum volume commitments), fee schedules, escalators, and remaining tenor
- **Revenue breakdown**: fee-based vs. percent-of-proceeds vs. keep-whole vs. commodity-exposed components with historical mix
- **Financial statements**: EBITDA, distributable cash flow (DCF), maintenance capex, growth capex, and leverage ratios
- **Counterparty data**: shipper/producer credit profiles, production forecasts for dedicated acreage, and rig count trends in connected basins
- **Regulatory/permits**: FERC tariff status (interstate vs. intrastate), right-of-way agreements, environmental permits [VERIFY: jurisdiction-specific permitting requirements]

## Workflow

1. **Classify the asset and revenue model**
   - Identify asset type and position in the midstream value chain (wellhead gathering → processing → long-haul transport → fractionation → terminal/export)
   - Categorize revenue: pure fee-based, fee with escalators, percent-of-proceeds, percent-of-index, keep-whole, or hybrid structures
   - Quantify the fee-based vs. commodity-exposed revenue split; flag any commodity margin exceeding 20% of gross margin as material exposure

2. **Analyze throughput and utilization**
   - Chart historical throughput against nameplate capacity to derive utilization rates
   - Identify volume trends: declining basin production, ramp-up from new well connections, or plateau behavior
   - Compare throughput to MVC floors — volumes consistently at or below MVCs signal producer stress or over-contracted capacity
   - Assess organic growth potential: available capacity headroom, pending interconnects, expansion optionality

3. **Evaluate the contract book**
   - Map weighted-average contract life (WACL) and remaining MVC tenor; flag contracts with <3 years remaining
   - Assess acreage dedication quality: size of dedicated area, drilling activity on dedicated acreage, decline rates of existing wells
   - Review fee escalation mechanisms (CPI-linked, fixed annual step-up, or redetermination) and historical realized escalation
   - Identify recontracting risk: contracts rolling off in any single year exceeding 20% of revenue warrant detailed recontracting assumptions

4. **Stress-test counterparty and basin risk**
   - Evaluate top-5 shipper/producer concentration — a single counterparty above 30% of revenue is a concentration flag
   - Cross-reference producer credit ratings, hedging programs, and breakeven economics against current commodity prices
   - Assess basin-level risks: regulatory moratoriums, water disposal constraints, takeaway bottlenecks, and competing infrastructure [VERIFY: state-level regulatory environment for target basin]
   - Model a downside case: reduce throughput 15-25% below base, apply MVC deficiency payment mechanics, and recalculate coverage

5. **Build the financial profile**
   - Calculate EBITDA, DCF, and distribution coverage ratio under base, upside, and stress scenarios
   - Separate maintenance capex (integrity, compliance, cathodic protection) from growth capex (looping, compression additions, new laterals)
   - Compute leverage (Debt/EBITDA) and compare to midstream sector benchmarks (typically 3.0x–4.5x for investment-grade)
   - Assess dropdown economics if asset sits within a sponsor/MLP structure: dropdown multiple vs. market trading multiple, IDR burden

6. **Synthesize findings and flag risks**
   - Summarize asset quality tier: core infrastructure with long-dated fee-based contracts vs. basin-dependent gathering with commodity exposure
   - Rank key risks: commodity sensitivity, recontracting cliff, counterparty concentration, regulatory, and volumetric decline
   - Identify value levers: expansion capex opportunities, fee escalator upside, recontracting at market rates, operational efficiency gains

## Output

Produce an **Analysis Report** containing:

- **Executive summary**: asset description, investment thesis (1-2 paragraphs), and key metrics table (EBITDA, DCF, coverage, leverage, WACL, utilization)
- **Revenue and contract analysis**: fee-based/commodity split, contract tenor waterfall chart, MVC coverage analysis, top counterparty table
- **Throughput analysis**: historical volume trends, utilization rates, basin production outlook
- **Financial projections**: base/upside/downside EBITDA and DCF with key assumptions stated
- **Risk matrix**: ranked risks with probability/impact assessment and mitigants
- **Valuation context**: implied EV/EBITDA vs. comparable midstream transactions and trading comps

## Quality Checks

- Confirm revenue split percentages reconcile to reported financials (fee-based + commodity-exposed = 100% of gross margin)
- Verify MVC volumes against actual throughput — flag any period where actuals fell below MVCs and confirm deficiency payment treatment
- Cross-check WACL calculation against individual contract expiry dates
- Ensure stress-test assumptions are internally consistent (e.g., volume decline should flow through to reduced variable O&M)
- Confirm all commodity price assumptions are dated and sourced (strip pricing with as-of date)
- Mark any regulatory or permitting assumptions with [VERIFY] where state or FERC-specific rules apply
- Validate that maintenance capex assumptions align with asset age, integrity management plan, and recent inspection data
