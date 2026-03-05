---
name: modeling-purchase-price-allocation
description: Structures PPA analysis with tangible/intangible asset identification, useful life estimation, and goodwill calculation. Use when modeling purchase accounting, allocating deal price, or estimating amortization impact.
tags:
  - modeling
  - mergers-and-acquisitions
  - accounting
metadata:
  author: casemark
  practice_areas:
    - M&A Advisory
    - Corporate Development
    - Investment Banking
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Purchase Price Allocation

Structures PPA analysis with tangible/intangible asset identification, useful life estimation, and goodwill calculation.

## When To Use

- Modeling purchase accounting for a completed or contemplated acquisition under ASC 805 / IFRS 3 [VERIFY: applicable standard based on reporting framework]
- Allocating total deal consideration (cash, stock, earnouts, assumed liabilities) across acquired tangible and intangible assets
- Estimating post-close amortization impact on pro forma earnings and accretion/dilution analysis
- Preparing preliminary PPA for board books, fairness opinions, or integration planning
- Stress-testing goodwill levels to assess impairment risk under various purchase price scenarios

## Inputs To Gather

- **Total consideration**: Cash at close, stock component (exchange ratio, share price, shares issued), deferred consideration, earnout terms and estimated fair value, assumed debt
- **Target balance sheet**: Most recent audited or management-prepared balance sheet with asset and liability line items at book value
- **Tangible asset detail**: PP&E schedules, real estate appraisals, inventory breakdown (raw/WIP/finished), lease schedules
- **Intangible asset identification**: Customer lists and churn data, technology/IP descriptions, brand/trade name revenue attribution, in-process R&D status, non-compete agreements, favorable/unfavorable contracts
- **Valuation inputs**: Discount rates (WACC, IRR of transaction), royalty rates for relief-from-royalty method, attrition/decay rates for customer relationships, revenue/cost projections for MEEM analysis, comparable transaction multiples
- **Tax information**: Applicable tax rate, whether transaction is asset vs. stock deal [VERIFY: Section 338(h)(10) election status], deferred tax liability/asset implications of step-up

## Workflow

1. **Calculate total consideration**
   - Sum cash, fair value of equity issued (shares x price), present value of deferred payments, estimated fair value of contingent consideration (earnouts), and net assumed liabilities
   - Identify and separate transaction costs (not part of consideration under ASC 805)

2. **Mark tangible assets to fair value**
   - Revalue PP&E from book to appraised fair value; note step-up or step-down
   - Revalue inventory: finished goods to selling price less costs to sell and reasonable profit on selling effort; raw materials to replacement cost
   - Adjust other balance sheet items (receivables to collectible value, debt to market value)

3. **Identify and value intangible assets**
   - **Customer relationships**: Multi-period excess earnings method (MEEM) — project revenue, subtract contributory asset charges, discount at appropriate rate; assign useful life based on attrition curve
   - **Technology / IP**: Relief-from-royalty method — apply market royalty rate to projected revenue, tax-effect, discount to present value; or cost-to-recreate approach for proprietary systems
   - **Trade names / brands**: Relief-from-royalty with brand-specific royalty rate; determine definite vs. indefinite life [VERIFY: indefinite-life treatment requires annual impairment testing]
   - **In-process R&D**: Estimate probability-weighted completion cost and post-launch cash flows; indefinite-life until project completes or is abandoned
   - **Non-compete agreements**: With-and-without method — model cash flows with and without the agreement, discount the difference
   - **Favorable/unfavorable contracts**: Present value of above- or below-market terms over remaining contract life

4. **Calculate deferred tax impact**
   - Compute DTL on book-tax basis differences created by asset step-ups (fair value less tax basis x tax rate)
   - DTL itself reduces net identifiable assets, which increases residual goodwill — solve iteratively or use gross-up formula: Goodwill = (Consideration - Net FV tangible - Intangibles + DTL) where DTL = (Intangible step-up) x tax rate / (1 - tax rate) for the circular component [VERIFY: confirm gross-up formula applicability with tax advisor]

5. **Derive goodwill**
   - Goodwill = Total consideration - Fair value of net identifiable tangible assets - Fair value of identified intangible assets + Net deferred tax liability on step-ups
   - Benchmark goodwill as a percentage of total consideration against comparable transactions; flag if outlier (typically 30-60% for asset-light targets, lower for asset-heavy)

6. **Build amortization schedule**
   - Assign useful lives to each definite-life intangible (customer relationships: 8-15 yrs; technology: 3-7 yrs; trade names: 10-20 yrs or indefinite; non-competes: contract term) [VERIFY: useful life estimates against industry norms and valuation specialist guidance]
   - Model straight-line or accelerated amortization as appropriate
   - Calculate annual pre-tax amortization expense and after-tax EPS impact for accretion/dilution model

7. **Sensitivity and scenario analysis**
   - Vary purchase price +/- 10-20% and show impact on goodwill and annual amortization
   - Test key valuation assumptions: royalty rates +/- 1%, discount rates +/- 100 bps, attrition rates +/- 2%
   - Model goodwill impairment trigger scenarios (revenue decline thresholds where reporting unit FV falls below carrying value)

## Output

- **PPA summary table**: Total consideration breakdown, fair value of each asset/liability class, identified intangibles with valuation method and useful life, residual goodwill
- **Intangible asset detail**: One tab/section per intangible with valuation methodology, key assumptions, and sensitivity ranges
- **Amortization schedule**: Year-by-year amortization by intangible asset with totals, pre-tax and after-tax
- **Goodwill analysis**: Goodwill as % of deal value, benchmarked against precedent transactions, impairment scenario summary
- **Assumption log**: Every material assumption tagged with source (management, third-party appraisal, comparable data, or [VERIFY] if unconfirmed)

## Quality Checks

- Total consideration components reconcile to signed purchase agreement or LOI terms
- Sum of allocated values (tangible FV + intangible FV + goodwill - DTL) ties back to total consideration with zero residual
- Intangible asset useful lives are consistent with valuation methodology decay/attrition assumptions
- Discount rates used for intangible valuations are internally consistent (weighted average return on assets reconciles to transaction IRR)
- Goodwill percentage is reasonable relative to comparable M&A transactions in the sector
- Amortization schedule correctly flows into pro forma income statement and accretion/dilution analysis
- All tax rate assumptions and asset/stock deal structure implications are flagged for tax advisor confirmation [VERIFY]
- No intangible asset is double-counted (e.g., customer relationships and favorable contracts from the same customer base)
