---
name: analyzing-m-and-a-tax-implications
language: en
description: Evaluates tax implications of acquisition structures with 338(h)(10), 368 reorganization, and step-up analysis. Use when analyzing deal tax, structuring tax-efficient acquisitions, or evaluating tax-free reorganizations.
tags:
  - analysis
  - tax
metadata:
  author: casemark
  practice_areas:
    - Tax Planning
    - Tax Compliance
    - International Tax
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing M And A Tax Implications

Evaluates tax implications of acquisition structures, comparing asset vs. stock purchases, Section 338(h)(10) elections, Section 368 tax-free reorganizations, and basis step-up opportunities to identify the most tax-efficient deal structure.

## When To Use

- Buyer or seller needs a comparative tax analysis of proposed acquisition structures
- Evaluating whether a 338(h)(10) election yields net tax benefit over a straight stock purchase
- Determining if a transaction qualifies as a tax-free reorganization under Section 368
- Quantifying the present value of basis step-up through amortization/depreciation
- Assessing cross-border deal structures with international tax overlay (GILTI, BEAT, Subpart F)
- Pre-LOI structuring advisory or post-LOI tax diligence support

## Inputs To Gather

- **Deal parameters**: Purchase price, proposed structure (asset/stock/merger), target entity type (C-corp, S-corp, partnership, LLC)
- **Target financials**: Balance sheet with FMV estimates for key asset classes, inside vs. outside basis positions, net operating losses and credit carryforwards
- **Seller profile**: Shareholder composition (individuals, trusts, tax-exempts, foreign holders), holding periods, prior Section 338 elections
- **Buyer profile**: Entity type, existing NOLs, acquisition financing structure (debt/equity mix), strategic vs. financial buyer status
- **Asset detail**: Tangible asset classes with estimated useful lives, identifiable intangibles (customer lists, IP, covenants), goodwill estimate
- **Jurisdiction data**: State/local tax rates for buyer and seller, nexus footprint, apportionment factors [VERIFY state-specific rules]

## Workflow

1. **Classify the target entity and deal type**
   - Determine target entity tax classification (C-corp, S-corp, partnership, disregarded entity)
   - Map proposed deal mechanics: direct asset purchase, stock purchase, statutory merger (forward/reverse), or equity interest purchase
   - Identify whether Section 338(h)(10) election is available (requires target to be S-corp or member of consolidated/affiliated group)

2. **Model the asset purchase scenario**
   - Allocate purchase price across IRC Section 1060 asset classes (Classes I–VII)
   - Calculate depreciation/amortization schedules for each asset class (Section 168 for tangibles, Section 197 for intangibles/goodwill)
   - Compute present value of total tax shield from step-up using buyer's discount rate
   - Identify state-level conformity or deviation from federal asset allocation rules [VERIFY]

3. **Model the stock purchase scenario (no 338 election)**
   - Buyer acquires stock at cost basis equal to purchase price; no step-up in target's inside asset basis
   - Identify trapped tax attributes: NOLs subject to Section 382 limitations, built-in gains/losses
   - Calculate Section 382 annual limitation (long-term tax-exempt rate × equity value of target) [VERIFY current applicable federal rate]
   - Assess successor liability exposure and its tax implications

4. **Model the 338(h)(10) election scenario**
   - Treat the stock purchase as a deemed asset sale for tax purposes
   - Calculate deemed sale price (ADSP) using the formula: purchase price + target liabilities + tax on deemed sale
   - Run iterative tax calculation (deemed sale tax is circular — the tax affects ADSP which affects the tax)
   - Allocate ADSP across Section 1060 classes to establish new inside basis
   - Compare buyer step-up benefit against incremental seller tax cost; determine net deal benefit and who bears it

5. **Evaluate Section 368 reorganization qualification**
   - Test applicable reorganization type: Type A (statutory merger), Type B (stock-for-stock), Type C (stock-for-assets), or triangular variants
   - Verify continuity of interest (COI): at least 40% of consideration must be acquirer stock (based on IRS ruling guidelines) [VERIFY current COI threshold]
   - Verify continuity of business enterprise (COBE): acquirer must continue target's historic business or use a significant portion of target's assets
   - Assess boot received by target shareholders and resulting gain recognition under Section 356
   - Identify potential disqualifying elements (cash consideration exceeding limits, step-transaction doctrine risks)

6. **Cross-border and international overlay**
   - If target has foreign operations: evaluate GILTI inclusions (Section 951A), Subpart F income, and Section 245A dividends-received deduction
   - Assess BEAT applicability if post-acquisition base erosion payments exceed thresholds [VERIFY current BEAT base erosion percentage threshold]
   - Review treaty implications for withholding on cross-border payments
   - Evaluate Section 367 toll charges on outbound transfers of assets to foreign entities

7. **Comparative structure analysis**
   - Build side-by-side comparison matrix: asset purchase vs. stock purchase vs. 338(h)(10) vs. 368 reorganization
   - Quantify after-tax cost to buyer and after-tax proceeds to seller under each structure
   - Calculate net present value differential across structures
   - Identify structure-specific risks: successor liability (asset vs. stock), Section 382 limitations, recapture exposure
   - Flag purchase price allocation sensitivities and negotiation leverage points

## Output

- **Structure comparison matrix**: Side-by-side table showing total tax cost/benefit for buyer and seller under each modeled structure
- **Step-up analysis**: Asset class allocation with depreciation/amortization schedules and PV of tax shield
- **338(h)(10) analysis**: ADSP calculation, iterative tax computation, and net benefit quantification
- **368 qualification assessment**: Pass/fail on each requirement (COI, COBE, boot limits) with supporting rationale
- **Recommended structure**: Identification of optimal structure with quantified tax savings and key assumptions
- **Risk flags**: Successor liability, Section 382 limitations, recapture triggers, state nonconformity issues

## Quality Checks

- Verify Section 1060 allocation sums to total purchase price (no residual gaps)
- Confirm 338(h)(10) circular tax calculation converges (iterate until delta < $1)
- Validate Section 382 limitation uses current long-term tax-exempt rate [VERIFY]
- Cross-check that 368 analysis addresses all statutory requirements for the specific reorganization type claimed
- Ensure state tax analysis covers all jurisdictions where buyer and target have nexus [VERIFY state conformity with federal elections]
- Confirm discount rate used for PV calculations is consistent with buyer's weighted average cost of capital
- Flag any assumed asset FMVs that lack appraisal support as [VERIFY]
