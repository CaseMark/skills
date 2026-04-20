---
name: evaluating-upstream-energy-assets
language: en
description: Assesses upstream oil and gas assets with reserve estimation, production decline curves, and net asset value modeling. Use when evaluating E&P assets, analyzing reserve reports, or modeling upstream economics.
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
    - Evaluation Report
  skill_modes:
    - Analysis
    - Assessment
---
# Evaluating Upstream Energy Assets

Assesses upstream oil and gas assets with reserve estimation, production decline curves, and net asset value modeling.

## When To Use

- Evaluating an acquisition or divestiture of producing properties, PDP reserves, or undeveloped acreage
- Reviewing a third-party reserve report (e.g., from DeGolyer & MacNaughton, Ryder Scott, or Netherland Sewell)
- Building or auditing a net asset value (NAV) model for an E&P company or asset package
- Benchmarking production decline rates against type curves for a given basin or formation
- Underwriting reserve-based lending (RBL) or mezzanine capital for upstream operators

## Inputs To Gather

- **Reserve report**: Proved (1P), proved + probable (2P), and proved + probable + possible (3P) volumes by category (PDP, PDNP, PUD) [VERIFY classification methodology — SPE-PRMS vs. SEC definitions]
- **Production history**: Monthly oil, gas, and NGL volumes by well or lease, ideally 24+ months
- **Decline curve parameters**: Initial production (IP) rates, b-factor, Di (initial decline rate), terminal decline rate
- **Commodity price assumptions**: Strip pricing or flat-price scenarios for WTI, Henry Hub, and relevant basis differentials
- **Operating cost data**: Lease operating expense (LOE) per BOE, workover frequency and cost, G&A allocation
- **Capital program**: Drilling & completion (D&C) cost per well, number of planned PUD locations, AFE detail if available
- **Fiscal terms**: Royalty burden, net revenue interest (NRI), severance/ad valorem tax rates [VERIFY by state/jurisdiction], any overriding royalty interests (ORRIs)
- **Acreage position**: Held-by-production (HBP) status, lease expirations, continuous drilling obligations

## Workflow

1. **Classify reserves and reconcile volumes**
   - Map reserves into PDP, PDNP, and PUD categories
   - Reconcile operator-reported reserves against third-party engineer estimates
   - Flag any reserve bookings that lack offset well support or rely on analogy from distant formations
   - Note the R/P ratio (reserves-to-production) for reasonableness — PDP R/P above 15 years or below 3 years warrants scrutiny

2. **Fit decline curves to production data**
   - Plot monthly production on a semi-log or log-log scale to identify decline regime (exponential, hyperbolic, harmonic)
   - Fit Arps decline parameters (b-factor, Di) to historical data; flag if b > 2.0 (physically implausible for boundary-dominated flow)
   - For unconventional wells (shale/tight), consider modified hyperbolic with a terminal decline switch (typically 5–8% annual)
   - Compare fitted EUR (estimated ultimate recovery) per well against reserve report EURs — variance > 15% needs explanation

3. **Build the net asset value (NAV) model**
   - Project production volumes by category using fitted decline curves for PDP and type curves for PUD
   - Apply commodity price deck (strip, management case, or stress case) with appropriate basis differentials and quality adjustments (API gravity, BTU content)
   - Deduct LOE, G&A, production taxes, and capital expenditures for PUD development
   - Discount net cash flows at 10% (SEC PV-10 standard) and at risk-adjusted rates (typically 12–20% depending on reserve category):
     - PDP: 10–12%
     - PDNP: 12–15%
     - PUD: 15–20%+ depending on development certainty
   - Deduct net debt, asset retirement obligations (ARO), and corporate overhead to arrive at equity NAV

4. **Stress-test key assumptions**
   - Run commodity price sensitivities (±$10/bbl WTI, ±$0.50/MMBtu gas)
   - Vary D&C costs ±15% to test PUD economics breakeven
   - Assess impact of accelerated decline (b-factor reduction) on PDP value
   - Evaluate lease expiration risk — quantify acreage at risk and associated PUD value exposure

5. **Assess operational and geological risk factors**
   - Well concentration: single-well or single-pad dependency
   - Midstream constraints: takeaway capacity, gas processing agreements, flaring limitations [VERIFY local regulations]
   - Water disposal: SWD well access, induced seismicity risk in sensitive basins (e.g., Oklahoma, parts of Permian)
   - Environmental/regulatory: plugging liability, bonding requirements, emissions compliance [VERIFY state-specific rules]
   - Operator quality: track record on cycle times, capital discipline, and LOE management

## Output

The evaluation report should include:

- **Executive summary**: Asset overview, headline NAV range, key value drivers and risks
- **Reserve summary table**: Volumes by category (oil/gas/NGL) with SEC and strip-price PV-10
- **Decline curve exhibit**: Production plots with fitted parameters and EUR comparison vs. reserve report
- **NAV waterfall**: PDP value → add PDNP → add PUD → deduct ARO/debt → equity NAV, shown at multiple price/discount rate scenarios
- **Sensitivity matrix**: NAV under commodity price, cost, and decline rate variations
- **Risk register**: Itemized geological, operational, regulatory, and fiscal risks with materiality assessment
- **Recommendation**: Buy/pass/conditional with identified diligence items

## Quality Checks

- Confirm reserve classifications align with SEC or SPE-PRMS definitions as appropriate [VERIFY which standard applies]
- Verify that decline curve fits use sufficient production history (minimum 6 months post-flush for unconventionals)
- Check that NRI and royalty burden sum correctly across all interests (working interest × (1 − royalty burden) = NRI)
- Ensure D&C cost assumptions reflect current service cost environment, not stale AFEs
- Validate that the price deck matches the stated date and source (NYMEX strip, OPIS, internal forecast)
- Confirm ARO estimates are based on current plugging cost data, not outdated flat assumptions
- Cross-check NAV output against recent comparable transactions ($/BOE, $/acre, $/flowing barrel) for reasonableness
