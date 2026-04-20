---
name: analyzing-renewable-energy-project-finance
language: en
description: Evaluates renewable energy project economics with PPA structures, merchant tail risk, and production profile analysis. Use when analyzing wind/solar projects, evaluating PPA terms, or modeling renewable energy cash flows.
tags:
  - analysis
  - infrastructure-and-project-finance
  - risk
metadata:
  author: casemark
  practice_areas:
    - Project Finance
    - Infrastructure Investment
    - PPP
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Renewable Energy Project Finance

Evaluates renewable energy project economics with PPA structures, merchant tail risk, and production profile analysis.

## When To Use

- Underwriting or due-diligencing a wind or solar project financing (construction or refinancing)
- Evaluating a PPA term sheet or comparing offtake structures (fixed-price, proxy-revenue swap, virtual/financial PPA)
- Assessing merchant tail risk beyond PPA tenor for debt sizing or equity return sensitivity
- Reviewing an independent engineer's production estimate (P50/P75/P99) against lender assumptions
- Modeling cash flows for tax equity structures (ITC/PTC partnership flips, sale-leasebacks) [VERIFY: current ITC/PTC eligibility rules under applicable tax code]

## Inputs To Gather

- **Technology and site data**: nameplate capacity (MW-DC/MW-AC), location, COD date, expected useful life, degradation curve
- **Production estimates**: independent resource assessment with P-values (P50, P75, P90, P99), basis for exceedance probabilities, measurement period
- **Offtake contracts**: PPA term, price ($/MWh), escalator, settlement hub, volume commitment (unit-contingent vs. firm), curtailment allocation, credit support
- **Capital structure**: construction budget, debt quantum and terms (mini-perm vs. fully amortizing), DSRA sizing, LC facilities, tax equity commitment and flip mechanics
- **Operating assumptions**: O&M contracts (scope, escalation, availability guarantees), major maintenance reserve schedule, insurance program, land lease terms
- **Market inputs**: forward power curves at settlement hub, basis differential to project node, REC pricing and tenor [VERIFY: REC market and applicable RPS requirements by state/jurisdiction]
- **Tax assumptions**: ITC vs. PTC election, bonus depreciation schedule, MACRS period, prevailing wage / apprenticeship requirements, domestic content adders [VERIFY: current Inflation Reduction Act guidance and IRS safe harbors]

## Workflow

1. **Validate production profile** — Compare the independent engineer's P50 net capacity factor against comparable operating assets in the region. Confirm degradation assumptions (typically 0.4–0.5%/yr for solar, 0.1–0.2%/yr for wind). Check that the P-distribution spread is reasonable (a P90/P50 ratio below ~85% for wind warrants scrutiny). Flag any single-source resource assessment.

2. **Map the offtake structure** — Identify contracted vs. merchant periods. For the PPA tenor, confirm price, escalator, and settlement mechanics (physical vs. financial, busbar vs. hub). Quantify basis risk between the PPA settlement point and the project node. For proxy-revenue swaps, isolate shape and balancing risk retained by the project.

3. **Model pre-tax cash flows** — Build annual revenue from contracted (PPA price × expected generation) and merchant (forward curve × merchant volume) streams. Layer in O&M, insurance, land lease, and major maintenance reserve contributions. Confirm EBITDA margins are consistent with asset class benchmarks (typically 75–85% for solar, 65–80% for wind).

4. **Size and stress-test the debt** — Calculate DSCRs under P50 base case and P90/1-year downside. Typical project finance targets: ≥1.30x min DSCR at P50, ≥1.10x at P90 for investment-grade offtakers [VERIFY: lender-specific DSCR thresholds]. Test merchant tail scenarios using stressed power price decks (e.g., −20% from forward curve). Evaluate sculpted vs. flat amortization profiles and confirm debt tenor vs. PPA tenor coverage.

5. **Evaluate tax equity economics** — Model after-tax yields to the tax equity investor under the elected structure (partnership flip, inverted lease). Confirm flip timing, target IRR, and DRO/deficit restoration obligations. Quantify the impact of ITC vs. PTC election on sponsor vs. tax equity returns. Run sensitivity on tax rate changes and production shortfall.

6. **Assess merchant tail and residual value** — For post-PPA years, apply a conservative power price forecast. Stress-test with flat real pricing and a carbon-price-absent scenario. Consider recontracting assumptions and remaining useful life. Quantify terminal value contribution to equity IRR (typically 15–30% of levered equity returns come from the merchant tail).

7. **Synthesize risk factors** — Summarize key risks: resource variability, basis exposure, curtailment, counterparty credit, regulatory change (RPS modifications, interconnection queue risk), technology performance, and interest rate exposure on floating-rate tranches.

## Output

- **Executive summary**: project overview, key return metrics (levered/unlevered IRR, equity multiple, yield-on-cost), and investment recommendation
- **Cash flow model outputs**: annual revenue, EBITDA, DSCR, debt balance, and after-tax distributions by investor class
- **Sensitivity tables**: IRR and DSCR sensitivity to production (P50/P75/P90), power price (±10–20%), and basis differential
- **Risk matrix**: ranked risk factors with probability/impact assessment and available mitigants (contractual, structural, insurance)
- **PPA comparison** (if applicable): side-by-side offtake term comparison with NPV-equivalent pricing

## Quality Checks

- DSCRs foot to the cash flow model and reflect correct waterfall priority (O&M → debt service → reserves → distributions)
- Tax equity flip timing is consistent with after-tax yield targets and does not violate partnership allocation rules [VERIFY: IRS partnership anti-abuse and economic substance requirements]
- Production estimates reference a named independent engineer and state the measurement basis (e.g., 15-year wind dataset, TMY solar irradiance)
- Merchant revenue assumptions are sourced to a dated forward curve with explicit hub and vintage
- Degradation, availability, and curtailment assumptions are individually stated, not buried in a single net capacity factor
- All [VERIFY] items have been checked against current statutes, IRS guidance, and lender term sheets before finalizing
