---
name: conducting-reserve-and-resource-analysis
language: en
description: Evaluates mineral and hydrocarbon reserves with classification methodology, resource conversion rates, and valuation per unit analysis. Use when analyzing reserve reports, validating resource estimates, or assessing depletion profiles.
tags:
  - process
  - real-assets-and-natural-resources
  - valuation
metadata:
  author: casemark
  practice_areas:
    - Natural Resources
    - Energy Capital
    - Commodity Investment
  document_types:
    - Process Documentation
  skill_modes:
    - Process Management
---
# Conducting Reserve And Resource Analysis

Evaluates mineral and hydrocarbon reserves with classification methodology, resource conversion rates, and valuation per unit analysis.

## When To Use

- Reviewing a Competent Person's Report (CPR), NI 43-101 technical report, or SEC-compliant reserve filing
- Validating proved/probable/possible (1P/2P/3P) reserve classifications prior to an acquisition or financing
- Assessing resource-to-reserve conversion ratios for mine-stage or field-development economics
- Building depletion schedules for NAV models on oil & gas or mining assets
- Benchmarking reserve replacement ratios, finding & development costs, or reserve life indices across a portfolio

## Inputs To Gather

- **Reserve/resource report** — the third-party or internal engineering estimate (identify preparer, effective date, reporting standard)
- **Commodity type** — oil/gas (specify BOE conversion ratios used), hard-rock mineral, coal, or other
- **Classification standard** — PRMS (SPE/WPC), CRIRSCO-aligned code (JORC, CIM, SAMREC), SEC Subpart 1200, or NI 43-101 [VERIFY which standard governs the filing jurisdiction]
- **Price deck** — strip pricing, SEC trailing 12-month average, or operator forecast; note date and source
- **Production history** — at least 3 years of monthly production data if available; type-curve parameters for undeveloped locations
- **Cost assumptions** — OPEX per unit, CAPEX for development/infill, abandonment/reclamation obligations
- **Fiscal terms** — royalty rates, production taxes, PSC terms, or mining royalty/tax regime [VERIFY jurisdiction-specific rates]

## Workflow

1. **Identify the reporting framework and audit the classification**
   - Confirm whether the report follows PRMS, JORC, CIM, SEC S-K 1200, or another standard
   - Map each category to a confidence tier: Proved/Measured → ≥90%, Probable/Indicated → ≥50%, Possible/Inferred → lower confidence
   - Flag any categories labeled "contingent resources" or "exploration target" — these sit outside reserves and must not be treated as bookable

2. **Reconcile reserves to production history**
   - Compare prior-year reserve bookings to actual production and revisions; compute the reserve replacement ratio (net additions ÷ production)
   - Identify technical revisions vs. price revisions vs. discoveries; large negative technical revisions signal estimation risk
   - For mining assets, reconcile mill feed grades against the block-model predictions to assess estimation bias

3. **Evaluate resource-to-reserve conversion potential**
   - Determine what fraction of indicated/probable resources can convert to measured/proved given planned development CAPEX
   - Assess modifying factors: metallurgical recovery, cut-off grade sensitivity, well-spacing assumptions, regulatory permits outstanding [VERIFY permitting status]
   - Assign a probability-weighted conversion rate (e.g., 60-80% for brownfield infill, 20-40% for greenfield exploration upside)

4. **Build the depletion profile**
   - For oil & gas: apply decline-curve analysis (hyperbolic/exponential) using fitted b-factor, Di, and terminal decline rate; cross-check against type curves for analogous wells
   - For mining: construct a life-of-mine (LOM) schedule from the mine plan, sequencing ore blocks by grade and strip ratio
   - Sensitize the profile to ±10-20% recovery factor or grade variation

5. **Compute per-unit valuation metrics**
   - Calculate in-ground value: commodity price × net revenue interest × recovery factor, less development CAPEX per unit
   - Derive NAV per proved BOE (or per recoverable ounce/ton) using a DCF at an appropriate discount rate (typically 10% for SEC PV-10)
   - Benchmark against recent comparable transactions ($/BOE, $/oz, $/lb in-situ)

6. **Assess risk factors and flag uncertainties**
   - Geological risk: structural complexity, fault compartmentalization, grade continuity
   - Regulatory risk: outstanding permits, environmental liabilities, indigenous land claims [VERIFY jurisdiction]
   - Commercial risk: price sensitivity (run breakeven at ±20% commodity price), infrastructure access, offtake agreements

## Output

- **Reserve summary table** — quantities by category (1P/2P/3P or Measured/Indicated/Inferred), commodity, and asset/field, with effective date and reporting standard noted
- **Depletion schedule** — annual production forecast through reserve life, with key assumptions (decline parameters, mine sequencing, recovery factors)
- **Valuation summary** — NAV per unit at base, upside, and downside price cases; PV-10 or NPV at stated discount rate; comparison to market transaction benchmarks
- **Conversion and replacement analysis** — resource-to-reserve conversion assumptions, historical reserve replacement ratio, F&D cost per unit
- **Risk register** — itemized geological, regulatory, and commercial risks with [VERIFY] tags on jurisdiction-dependent items

## Quality Checks

- Reserve categories match the definitions of the stated reporting standard — do not conflate contingent resources with proved reserves
- Price deck date and source are explicitly stated; SEC filings must use the prescribed trailing average [VERIFY current SEC pricing rule]
- Decline-curve or LOM parameters are cross-referenced against at least one independent data point (analogous field, historical actuals, or third-party audit)
- BOE conversion ratios are stated and consistent (standard: 6 Mcf = 1 BOE for energy equivalence; note if economic equivalence is used instead)
- All per-unit metrics use a consistent denominator (net vs. gross acres, WI vs. NRI volumes, recoverable vs. in-situ resource)
- Abandonment and reclamation obligations are included in NAV calculations — omission overstates asset value
- Any estimate carrying greater than ±30% uncertainty range is flagged for further engineering review
