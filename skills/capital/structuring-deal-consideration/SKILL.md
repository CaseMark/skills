---
name: structuring-deal-consideration
description: Evaluates cash vs stock vs mixed consideration structures with tax, accounting, and shareholder impact analysis. Use when structuring deal terms, comparing consideration alternatives, or analyzing tax-efficient structures.
tags:
  - mergers-and-acquisitions
  - accounting
  - tax
metadata:
  author: casemark
  practice_areas:
    - M&A Advisory
    - Corporate Development
    - Investment Banking
  document_types:
    - Report
  skill_modes:
    - Analysis
---
# Structuring Deal Consideration

Evaluates cash vs. stock vs. mixed consideration structures across tax, accounting, and shareholder impact dimensions to recommend optimal deal terms.

## When To Use

- Buyer and seller are negotiating consideration mix (all-cash, all-stock, or hybrid)
- Comparing tax-deferred reorganization structures against taxable acquisition formats
- Assessing EPS accretion/dilution under different consideration scenarios
- Evaluating earn-out, CVR, or contingent consideration components
- Advising on collar mechanisms, walk-away rights, or fixed vs. floating exchange ratios

## Inputs To Gather

- **Deal parameters**: Enterprise value, equity value, net debt, target share count, buyer share price and market cap
- **Consideration alternatives**: At least two structures to compare (e.g., 100% cash, 100% stock, 60/40 mix)
- **Tax profiles**: Target shareholder tax basis composition (high-basis institutional vs. low-basis founders), buyer NOLs or tax attributes, jurisdiction of both parties [VERIFY]
- **Accounting data**: Buyer and target trailing and projected EPS, combined pro forma financials, purchase price allocation estimates (identifiable intangibles, goodwill)
- **Financing assumptions**: Available cash on hand, committed debt facilities, cost of debt, buyer's leverage targets
- **Shareholder context**: Target shareholder register composition, buyer's authorized-but-unissued shares, any shareholder approval thresholds [VERIFY]
- **Regulatory considerations**: HSR filing thresholds, foreign investment review triggers, exchange listing rules for stock issuance [VERIFY]

## Workflow

1. **Frame the consideration alternatives**
   - Define each scenario explicitly (e.g., Scenario A: $45/share all-cash; Scenario B: 0.75x fixed exchange ratio all-stock; Scenario C: $20 cash + 0.40x stock per share)
   - Specify whether exchange ratios are fixed or floating, and any collar bounds

2. **Tax structure analysis**
   - Determine whether each scenario qualifies as a tax-free reorganization under IRC Section 368 (Type A, B, or C) or taxable acquisition [VERIFY — jurisdiction-specific]
   - For taxable structures: estimate aggregate target shareholder tax liability, calculate after-tax value per share
   - For tax-free structures: confirm continuity of interest requirements (typically 40%+ stock), continuity of business enterprise
   - Evaluate Section 338(h)(10) or Section 336(e) elections for asset step-up in taxable deals — quantify PV of depreciation/amortization shield
   - Assess buyer impact: stock consideration preserves cash but does not generate tax basis step-up unless taxable

3. **Accounting impact analysis**
   - All scenarios use acquisition method (ASC 805) — calculate goodwill and identifiable intangible assets under each
   - Model pro forma EPS accretion/dilution for each scenario at Year 1 and Year 3
   - For stock consideration: calculate dilution to existing buyer shareholders (shares outstanding increase)
   - For cash/debt consideration: model incremental interest expense impact on EPS
   - Note: stock deals may show accretion on EPS but dilute ownership; cash deals preserve ownership but may reduce EPS from financing costs

4. **Shareholder and market impact**
   - Analyze target shareholder preference: tax-sensitive founders may prefer stock; institutional holders may prefer cash certainty
   - Assess buyer shareholder dilution and likely market reaction (stock deals in premium-valued buyers vs. cash deals signaling confidence)
   - Evaluate deal certainty: cash offers have higher closing certainty; stock deals introduce market risk and may require collars
   - For mixed consideration: model election mechanics (e.g., cash election with proration, stock election with cap)

5. **Contingent consideration**
   - If earn-outs or CVRs are proposed: define triggers, measurement periods, payment caps
   - Note ASC 805 fair value measurement requirement at closing — contingent consideration creates post-close P&L volatility
   - Evaluate alignment of earn-out metrics with seller's ability to influence outcomes post-close

6. **Build comparison matrix**
   - Construct side-by-side table: after-tax value to target shareholders, EPS impact to buyer, dilution %, leverage impact, deal certainty score, tax structure qualification, regulatory complexity

## Output

Deliver a structured consideration analysis report containing:

- **Executive summary**: Recommended consideration structure with 2–3 sentence rationale
- **Scenario comparison table**: Side-by-side across all key metrics (after-tax value, EPS accretion/dilution, dilution %, pro forma leverage, tax structure, deal certainty)
- **Tax analysis section**: Structure qualification, aggregate tax impact, step-up value if applicable
- **Accounting section**: Pro forma EPS bridge, goodwill calculation, intangible amortization schedule
- **Shareholder impact section**: Target shareholder after-tax proceeds by holder type, buyer ownership dilution
- **Risk factors**: Market risk (floating exchange ratios), financing risk (debt capacity), regulatory risk, approval risk
- **Sensitivity analysis**: Key variable ranges (buyer stock price movement, interest rate changes, tax rate assumptions)

## Quality Checks

- Verify tax-free reorganization requirements against current IRC provisions and recent IRS guidance [VERIFY]
- Confirm EPS calculations use consistent share count methodology (basic vs. diluted, treasury stock method for options)
- Validate that pro forma leverage ratios remain within buyer's stated credit parameters and existing covenant limits
- Cross-check exchange ratio implied premium against comparable transaction premiums
- Ensure consideration election mechanics are modeled with realistic proration assumptions
- Flag any scenario where HSR, shareholder vote thresholds, or listing rules create incremental closing risk [VERIFY]
- Mark all jurisdiction-specific tax conclusions with [VERIFY] — rules differ materially across US, UK, EU, and other regimes
