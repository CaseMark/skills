---
name: modeling-stub-value-analysis
description: Calculates stub equity value with subsidiary attribution, holding company discount, and sum-of-parts residual analysis. Use when analyzing stub values, evaluating holding company discounts, or identifying negative stub situations.
tags:
  - modeling
  - activist-and-event-driven-investing
metadata:
  author: casemark
  practice_areas:
    - Activist Investing
    - Event-Driven Strategy
    - Special Situations
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Stub Value Analysis

## When To Use

- Evaluating whether a parent company's equity trades at an implied discount (or negative value) after subtracting the market value of publicly traded subsidiaries
- Screening for activist or event-driven opportunities where a holding company discount is mispriced
- Assessing spin-off, split-off, or divestiture catalysts that could unlock trapped stub value
- Building sum-of-the-parts (SOTP) frameworks for conglomerates or multi-segment holding companies
- Quantifying the residual equity value attributable to non-listed assets, corporate overhead, or net debt at the parent level

## Inputs To Gather

- **Parent company data**: Market cap, share count, current stock price, net debt at the parent (holdco) level, corporate overhead/G&A
- **Public subsidiary stakes**: Ticker, ownership percentage, current market cap, share count, and any lock-up or contractual restrictions on disposition
- **Private subsidiary estimates**: Revenue, EBITDA, or other operating metrics plus comparable company multiples for each non-public segment
- **Cross-holdings and minority interests**: Carrying values, fair value estimates, and any recent transactions providing marks
- **Tax and friction costs**: Estimated tax leakage on hypothetical disposition of subsidiary stakes (capital gains, withholding taxes), transaction costs [VERIFY jurisdiction-specific tax rates]
- **Historical context**: Prior stub value levels, historical holding company discount range, and any announced catalysts (activist filings, board reviews, strategic alternatives)

## Workflow

1. **Map the ownership structure** — Diagram the parent-subsidiary tree with ownership percentages, noting direct vs. indirect holdings and any intercompany loans or guarantees
2. **Mark public subsidiaries to market** — For each publicly traded subsidiary, compute the parent's attributable equity value: subsidiary market cap x ownership %. Apply a liquidity/block discount if the parent's stake exceeds thresholds where orderly disposition is impaired (typically >10% of subsidiary float)
3. **Value private subsidiaries** — Select comparable public companies or precedent transactions for each private segment. Apply EV/EBITDA or EV/Revenue multiples to the segment's trailing or forward metrics. Use a range (low/mid/high) rather than a point estimate. Flag any segment lacking reliable data with [VERIFY]
4. **Aggregate gross asset value (GAV)** — Sum the attributed values of all public and private subsidiaries plus any other assets (real estate, investments, tax assets)
5. **Deduct holdco-level liabilities** — Subtract parent-level net debt (holdco debt minus holdco cash), estimated tax leakage on hypothetical subsidiary dispositions, capitalized corporate overhead (apply a multiple to annual G&A), and any contingent liabilities
6. **Calculate stub equity value** — Stub = Parent market cap minus attributed value of public subsidiaries. Compare this to the estimated value of private assets net of holdco liabilities. A negative stub implies the market assigns zero or negative value to the remaining assets
7. **Compute holding company discount** — Holdco discount = 1 - (Parent market cap / NAV). Benchmark against historical average discount for the company and peer holding companies
8. **Run sensitivity analysis** — Vary key assumptions: subsidiary multiples (+/- 1-2x), ownership-adjusted values, tax friction rates, and corporate overhead multiples. Present a matrix showing stub value across scenarios

## Output

The final model should include:

- **Ownership structure diagram** with percentage stakes and entity relationships
- **SOTP valuation table** showing each subsidiary's attributed value (low/mid/high), methodology used, and key assumptions
- **Stub value calculation** stepping from parent market cap to residual equity, with each deduction itemized
- **Holding company discount** expressed as a percentage with historical comparison
- **Sensitivity matrix** on stub value across key variable ranges
- **Catalyst timeline** listing events that could narrow or eliminate the discount (activist campaigns, announced divestitures, regulatory changes, tax law shifts)
- **Summary conclusion** stating whether the stub is mispriced and the magnitude of potential upside if the discount normalizes

## Quality Checks

- Verify that the sum of attributed subsidiary values plus stub equals parent market cap (the math must tie)
- Confirm ownership percentages match the most recent proxy or annual filing — do not rely on stale data [VERIFY against latest 10-K/20-F]
- Ensure tax leakage estimates use the correct jurisdiction's capital gains rate and any applicable treaty benefits [VERIFY]
- Cross-check private subsidiary valuations against any recent arms-length transactions, analyst estimates, or management commentary
- Validate that the holding company discount range is consistent with observed discounts for comparable holdcos (typically 10-30% for diversified conglomerates)
- Confirm that net debt is isolated at the correct entity level — subsidiary-level debt should not be double-counted in the holdco deduction
- Flag any circular references (e.g., cross-holdings between parent and subsidiary) and handle them iteratively or note as a limitation
