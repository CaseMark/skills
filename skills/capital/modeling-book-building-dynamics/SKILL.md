---
name: modeling-book-building-dynamics
language: en
description: Structures book-building analysis with demand tiers, allocation methodology, and price sensitivity assessment. Use when managing book-building, analyzing investor demand, or optimizing allocation strategies.
tags:
  - modeling
  - equity-capital-markets
metadata:
  author: casemark
  practice_areas:
    - ECM
    - IPO Advisory
    - Equity Origination
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Book Building Dynamics

Structures book-building analysis with demand tiers, allocation methodology, and price sensitivity assessment for IPOs, follow-ons, and accelerated bookbuilds.

## When To Use

- Building or updating a demand book for an equity offering (IPO, FPO, block trade, ABB)
- Analyzing investor order quality to inform pricing and allocation recommendations
- Stress-testing price sensitivity across the indicated range to find the clearing price
- Preparing allocation proposals for syndicate desk or issuer review
- Comparing book composition against comparable deal benchmarks

## Inputs To Gather

- **Deal parameters**: filing range (low–high), base deal size, greenshoe option, share structure (primary vs. secondary)
- **Order book snapshot**: investor name, investor type (long-only, hedge fund, sovereign wealth, retail), order size (shares and dollars), limit price (if any), indication type (strike, limit, step)
- **Investor quality tiers**: internal tier ratings (Tier 1 / 2 / 3) or equivalent classification from syndicate desk
- **Comparable deal data**: recent IPO/FPO books in same sector—subscription levels, allocation patterns, aftermarket performance
- **Issuer preferences**: target shareholder base, geographic mix, concentration limits, cornerstone commitments already locked

## Workflow

1. **Ingest and clean the order book**
   - Normalize all orders to a common unit (shares at midpoint price)
   - Flag duplicate or amended orders; keep only the latest revision per investor
   - Tag each order with investor type, tier, geography, and limit-price bucket

2. **Build the demand curve**
   - Aggregate cumulative demand at each $0.50 (or appropriate) price increment across the filing range
   - Segment the curve by investor tier and type to show quality-weighted demand
   - Calculate subscription multiples at low, mid, and high price points (total book ÷ base deal size)

3. **Assess price sensitivity**
   - Identify the volume of limit orders that drop off at each price step ("drop-off analysis")
   - Compute the "quality-adjusted coverage" at each price—weight Tier 1 long-only orders more heavily than Tier 3 hedge fund orders
   - Flag the price level where quality-adjusted coverage falls below 3× (typical comfort threshold) [VERIFY: issuer/syndicate comfort threshold may vary]

4. **Model allocation scenarios**
   - Scenario A: Pro-rata across all valid orders at proposed price
   - Scenario B: Priority allocation favoring Tier 1 long-only with minimum fills for Tier 2/3
   - Scenario C: Issuer-directed allocation incorporating cornerstone locks and strategic investors
   - For each scenario, output allocation percentages by investor type, geographic split, and top-10 holder concentration (Herfindahl or CR-10)

5. **Run aftermarket stability analysis**
   - Estimate likely "flippers" based on investor historical holding periods and order behavior (late orders, price-sensitive limits)
   - Model first-day float assuming a flip rate for each tier [VERIFY: use desk's historical flip-rate benchmarks]
   - Stress-test: if top 5 allocated investors sell 50% within 30 days, what is the impact on free-float supply vs. average daily volume of comparable issuers?

6. **Prepare pricing and allocation recommendation**
   - Recommend a specific price (or narrow band) supported by the demand curve and quality analysis
   - Attach the preferred allocation scenario with rationale
   - Highlight risks: concentration risk, flip risk, geographic imbalance, limit-order cliff

## Output

- **Demand summary table**: subscription multiples at low / mid / high, broken out by tier and investor type
- **Demand curve chart data**: cumulative demand (shares) at each price increment, with quality-weighted overlay
- **Drop-off schedule**: orders lost at each price step above the midpoint, by investor category
- **Allocation scenario comparison**: side-by-side table of Scenarios A/B/C showing % by type, geography, and concentration metrics
- **Pricing recommendation memo**: 1-page narrative with recommended price, allocation rationale, key risks, and sensitivity footnotes
- **Aftermarket stability estimate**: projected first-day float, estimated flip volume, and days-to-absorb metric

## Quality Checks

- Subscription multiples should reconcile back to raw order count—cross-check totals before segmenting
- Confirm no single investor exceeds issuer's stated concentration cap in any allocation scenario [VERIFY: typical caps range 5–10% of deal; confirm issuer/regulatory limit]
- Verify limit-order encoding: a "$22 limit" order should appear in demand at $22 and below, not above
- Demand at the low end of the range should always exceed demand at the high end; if not, investigate data errors
- Comparable deal benchmarks should be from the same sector and within the last 12–18 months; flag stale comps
- All dollar and share figures must tie to a consistent share count (pre- or post-greenshoe; state which)
- Mark any assumed flip rates, tier weightings, or comfort thresholds with [VERIFY] if not sourced from the syndicate desk
