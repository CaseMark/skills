---
name: modeling-sum-of-parts-valuations
description: Builds SOTP valuations for conglomerates and multi-segment companies with segment-appropriate methodologies. Use when valuing diversified companies, calculating conglomerate discounts, or modeling segment breakups.
tags:
  - modeling
  - equity-research
  - valuation
metadata:
  author: casemark
  practice_areas:
    - Equity Research
    - Investment Management
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Sum Of Parts Valuations

## When To Use

- Valuing conglomerates or diversified companies operating across distinct business segments (e.g., GE, Berkshire Hathaway, Siemens)
- Quantifying conglomerate discount or premium versus pure-play peers
- Modeling spin-off, divestiture, or breakup scenarios to estimate unlock value
- Stress-testing whether a company trades at a discount to intrinsic segment-level value
- Supporting activist investor theses or strategic review recommendations

## Inputs To Gather

- **Segment financials**: Revenue, EBITDA, EBIT, and capital expenditures per reportable segment from 10-K/annual report segment disclosures (typically 3-5 years of history)
- **Corporate/unallocated costs**: Central overhead, shared services, and elimination entries not assigned to segments
- **Segment-specific comps**: Pure-play comparable company sets for each segment with current trading multiples (EV/EBITDA, EV/Revenue, P/E as appropriate)
- **Precedent transactions**: Relevant M&A multiples for segments where transaction data is more informative than trading comps
- **DCF inputs** (if applicable): Segment-level WACC components, long-term growth rates, and terminal value assumptions
- **Net debt and adjustments**: Total consolidated net debt, pension liabilities, minority interests, equity method investments, NOLs, and other non-operating assets/liabilities
- **Conglomerate discount benchmarks**: Historical discount ranges for the specific industry mix [VERIFY: discount ranges vary by market cycle and region]

## Workflow

1. **Map reportable segments** — Identify each operating segment from SEC filings or annual reports. Reconcile segment totals to consolidated financials. Flag any "Other/Corporate" residual bucket and determine whether it contains operating businesses or only overhead.

2. **Select valuation methodology per segment** — Assign the most appropriate method to each segment:
   - **EV/EBITDA comps**: Default for mature, cash-generative segments with clear pure-play peers
   - **EV/Revenue comps**: Use for high-growth or pre-profit segments (SaaS, biotech pipelines)
   - **DCF**: Use when segment has unique growth profile with no close comps, or for regulated utilities/infrastructure
   - **NAV/book value**: Use for financial services segments, real estate portfolios, or investment holding segments
   - **Precedent transactions**: Layer in when recent M&A provides more relevant pricing than trading comps

3. **Build pure-play comp sets** — For each segment, identify 4-8 publicly traded comparables. Screen for business model alignment, geographic mix, margin profile, and growth stage. Calculate median and mean multiples; document outlier exclusions.

4. **Calculate segment enterprise values** — Apply selected multiples to forward segment metrics (NTM EBITDA, revenue, etc.). Produce low/mid/high range using 25th percentile, median, and 75th percentile of comp set. For DCF segments, build a 5-year explicit forecast with terminal value.

5. **Allocate corporate costs** — Decide treatment of unallocated corporate overhead:
   - **Capitalize as negative value**: Apply a corporate overhead multiple (typically 6-8x) to annual unallocated costs
   - **Allocate pro-rata to segments**: Distribute to segments by revenue or headcount share before applying multiples
   - Document which approach is used and why — this choice materially impacts the result

6. **Bridge to equity value** — Sum segment enterprise values, subtract net debt, adjust for minority interests (at fair value, not book), add equity method investments and other non-operating assets (excess cash, NOL value, real estate). Divide by diluted share count for per-share implied value.

7. **Calculate conglomerate discount/premium** — Compare implied SOTP equity value to current market capitalization. Express as percentage discount or premium. Benchmark against historical trading range and sector-typical conglomerate discounts [VERIFY: typical conglomerate discounts range 10-25% but vary significantly by region and sector].

8. **Run sensitivity analysis** — Build a matrix showing implied equity value across:
   - Multiple ranges (±1-2 turns of EBITDA) per segment
   - Varying corporate cost treatment
   - Different terminal growth or WACC assumptions for DCF segments
   - Scenario toggle for full breakup vs. partial divestiture

## Output

- **SOTP summary table**: Segment name | Metric used | Metric value | Multiple range (low/mid/high) | Implied EV range per segment
- **Corporate adjustments bridge**: Unallocated costs, net debt, minority interests, non-operating assets, share count
- **Implied equity value**: Per-share range (low/mid/high) with current price reference and implied upside/downside
- **Conglomerate discount analysis**: Current implied discount vs. historical range
- **Comp set detail**: Per-segment comparable companies with key financial metrics and selected multiples
- **Sensitivity tables**: 2-way matrices for key segment multiple and cost assumption toggles
- **Methodology notes**: Rationale for methodology selection per segment, key assumptions, and data sources

## Quality Checks

- Segment EV values sum correctly and reconcile with adjustments to total implied equity value
- Each segment's applied multiple falls within the documented comp set range — no cherry-picked outliers
- Corporate unallocated costs are fully accounted for (not inadvertently dropped)
- Net debt figure matches most recent balance sheet and includes off-balance-sheet items (operating leases if pre-IFRS 16, pension deficits)
- Diluted share count includes in-the-money options and convertibles using treasury stock method
- Implied per-share value range is internally consistent across low/mid/high (no crossed ranges)
- Conglomerate discount calculation uses consistent EV-to-equity bridge
- All externally sourced multiples and financial data include as-of dates
- Mark any segment with fewer than 3 pure-play comps with [VERIFY] for reliability
- Cross-check SOTP implied value against consolidated DCF or comparable company analysis for reasonableness
