---
name: building-merger-consequence-models
description: Constructs accretion/dilution analysis with pro forma financials, synergy phasing, and purchase price allocation. Use when modeling merger outcomes, calculating EPS accretion, or analyzing deal structures.
tags:
  - modeling
  - mergers-and-acquisitions
metadata:
  author: casemark
  practice_areas:
    - M&A Advisory
    - Corporate Development
    - Investment Banking
  document_types:
    - Model
  skill_modes:
    - Modeling
---
# Building Merger Consequence Models

## When To Use

- Evaluating whether a proposed acquisition is accretive or dilutive to acquirer EPS
- Modeling pro forma combined financial statements for board presentations or fairness opinions
- Stress-testing deal structures across varying consideration mixes (cash vs. stock vs. mixed)
- Phasing synergy realization schedules for integration planning
- Analyzing purchase price allocation (PPA) impact on goodwill, intangibles, and future amortization
- Comparing multiple deal scenarios (e.g., different offer prices, financing structures, or synergy assumptions)

## Inputs To Gather

**Acquirer financials:**
- Latest reported and consensus forecast EPS, net income, shares outstanding, share price
- Existing debt balances, interest rates, cash position, and tax rate
- Current P/E multiple and market capitalization

**Target financials:**
- Latest reported and consensus forecast EPS, net income, shares outstanding, share price
- Revenue and EBITDA for synergy sizing baseline
- Existing debt to be assumed or refinanced

**Deal terms:**
- Offer price per share or total equity value
- Consideration mix: % cash, % stock, any CVRs or earnouts
- Expected transaction and financing fees
- Assumed financing terms for any new debt (rate, tenor, amortization)

**Synergy assumptions:**
- Cost synergies: run-rate amount, phase-in schedule (typically 25%/50%/75%/100% over Years 1–4)
- Revenue synergies (if modeled): run-rate amount, phase-in, associated costs to achieve
- One-time integration/restructuring costs and their timing
- Tax treatment of synergies and integration costs

**PPA estimates:**
- Fair value step-ups for tangible and identifiable intangible assets
- Estimated useful lives for amortizable intangibles (customer relationships, technology, trade names)
- Deferred tax liability created by asset step-ups [VERIFY: tax rate and jurisdiction rules]

## Workflow

1. **Build standalone projections** — Set up acquirer and target income statements on a consistent basis (same fiscal year, same line-item granularity). Calendarize if fiscal years differ. Normalize for non-recurring items.

2. **Calculate purchase price and goodwill** — Compute equity offer value, add assumed net debt to get enterprise value. Allocate purchase price: fair value of net tangible assets + identifiable intangibles + residual goodwill. Compute any deferred tax liabilities from step-ups.

3. **Model financing structure** — For cash consideration: determine funding source (cash on hand, new debt, or mix). Calculate incremental interest expense net of foregone interest income on cash used. For stock consideration: compute new shares issued using the exchange ratio (offer price / acquirer share price). For mixed deals: model both components.

4. **Construct pro forma income statement** — Combine acquirer + target standalone projections. Layer in adjustments:
   - (+) Cost synergies per phase-in schedule, net of tax
   - (+) Revenue synergies (if included), net of associated costs and tax
   - (−) Incremental intangible amortization from PPA
   - (−) Incremental interest expense from acquisition debt
   - (+) Interest income saved on target's refinanced debt (if applicable)
   - (−) One-time integration costs (typically excluded from recurring accretion/dilution but shown separately)
   - Apply blended effective tax rate to pre-tax adjustments [VERIFY: combined entity tax rate]

5. **Calculate accretion/dilution** — Compute pro forma EPS = pro forma net income / pro forma diluted shares outstanding. Compare to acquirer standalone EPS. Express result as % accretive or dilutive for each projection year. Show both with and without synergies to isolate synergy contribution.

6. **Run sensitivity analysis** — Build tables varying:
   - Offer price (±5–15% range)
   - Consideration mix (0%/25%/50%/75%/100% stock)
   - Synergy realization level (50%/75%/100%/125% of base case)
   - Interest rate on acquisition financing (±50–150 bps)
   - Breakeven synergy required to achieve EPS neutrality

7. **Prepare output tables** — Format results for presentation: summary accretion/dilution by year, pro forma EPS bridge (waterfall from standalone to pro forma), sensitivity matrices, and PPA summary.

## Output

- **Accretion/dilution summary**: Year 1–3 (or longer) showing pro forma EPS vs. standalone EPS, $ and % impact, with and without synergies
- **Pro forma income statement**: Combined P&L with clearly labeled merger adjustments as separate line items
- **EPS bridge / waterfall**: Standalone acquirer EPS → target earnings contribution → synergies → financing cost → amortization → pro forma EPS
- **Purchase price allocation table**: Fair values assigned to tangible assets, identifiable intangibles (by category and useful life), goodwill, and associated deferred tax impacts
- **Synergy phase-in schedule**: Annual run-rate build, costs to achieve, and net after-tax contribution
- **Sensitivity tables**: Accretion/dilution across offer price, consideration mix, synergy level, and financing cost scenarios
- **Key assumptions page**: All inputs, sources, and items flagged [VERIFY]

## Quality Checks

- **EPS math integrity**: Pro forma net income / pro forma shares = stated pro forma EPS (no rounding shortcuts)
- **Shares outstanding consistency**: New shares issued in stock deals = target shares × exchange ratio; verify diluted share count includes in-the-money target options converted at the exchange ratio
- **Goodwill reasonableness**: Total PPA should equal purchase price; goodwill should not be negative unless a bargain purchase is intended [VERIFY: bargain purchase gain treatment under ASC 805]
- **Tax consistency**: Verify the same tax rate is applied to synergies, amortization add-backs, and interest adjustments; confirm treatment of non-deductible goodwill
- **Synergy double-counting**: Ensure cost synergies are not also embedded in target's standalone projections
- **Financing circularity**: If using acquirer stock, confirm share price assumption is consistent (fixed vs. floating exchange ratio); if debt-funded, confirm interest rate reflects current market for acquirer's credit profile [VERIFY]
- **Sign conventions**: Accretive = positive (pro forma EPS > standalone); dilutive = negative — confirm this is consistent throughout all tables
- **Cross-check**: Compare implied transaction multiples (EV/EBITDA, P/E on offer) to precedent transactions for reasonableness
