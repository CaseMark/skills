---
name: analyzing-institutional-investor-demand
language: en
description: Maps institutional investor targeting with AUM analysis, sector allocation preferences, and historical participation patterns. Use when targeting investors, analyzing demand profiles, or building investor marketing lists.
tags:
  - analysis
  - equity-capital-markets
metadata:
  author: casemark
  practice_areas:
    - ECM
    - IPO Advisory
    - Equity Origination
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Institutional Investor Demand

## When To Use

- Building an investor target list for an IPO, follow-on, block trade, or convertible offering
- Evaluating likely demand depth and price sensitivity ahead of bookbuilding
- Profiling anchor, cornerstone, or strategic investor candidates
- Assessing sector rotation trends to time equity offerings
- Comparing investor participation patterns across comparable recent transactions

## Inputs To Gather

- **Issuer profile**: sector (GICS), market cap range, geography, index eligibility
- **Deal parameters**: offering type (IPO/FO/block/convert), estimated size, structure, use of proceeds
- **Comparable transactions**: 5–15 recent deals in same sector/size bracket with allocation data if available
- **Investor universe**: institutional holders from 13F filings, beneficial ownership reports, or syndicate desk data
- **Existing shareholder register**: current top holders, recent buying/selling activity, lock-up status
- **Market context**: current volatility, sector ETF flows, recent deal performance (aftermarket returns)

## Workflow

1. **Define the targeting universe**
   - Filter institutional investors by AUM tier (mega-cap >$100B, large $20–100B, mid $2–20B, emerging <$2B)
   - Screen by investment style: long-only, GARP, deep value, growth, index/quasi-index, hedge fund (L/S, event-driven, quant)
   - Narrow by sector allocation — identify funds with existing overweight or underweight in the issuer's GICS sector
   - Flag geographic constraints (US-only mandates, global, EM-focused) [VERIFY against each fund's prospectus or ADV]

2. **Analyze historical participation patterns**
   - Pull allocation data from recent comparable offerings (same sector, similar deal size)
   - Rank investors by frequency of participation and average order size as % of deal
   - Identify "anchor" candidates — investors who consistently take 5%+ allocations in comparable deals
   - Note investors who participated in prior rounds or PIPE transactions for the issuer
   - Flag any investors with pattern of quick flipping (selling within 30–90 days post-pricing)

3. **Assess demand quality indicators**
   - **AUM capacity**: investor's total equity AUM vs. typical position size — can they absorb a meaningful allocation?
   - **Sector conviction**: recent 13F changes showing increased/decreased sector exposure
   - **Holding period**: median hold duration for comparable positions (long-term holders vs. tactical)
   - **Price sensitivity**: historical behavior at various discount/premium levels in bookbuilds
   - **Relationship strength**: prior deal participation with lead bookrunners, attendance at NDRs

4. **Build tiered target list**
   - **Tier 1 (High Priority)**: strong sector fit, proven participation history, long holding periods, large AUM capacity
   - **Tier 2 (Core)**: good fit on most criteria, moderate participation history, may need more marketing effort
   - **Tier 3 (Opportunistic)**: situational interest — event-driven funds, crossover investors, new entrants to sector
   - Assign estimated order size ranges per investor based on historical patterns
   - Calculate aggregate demand estimate vs. deal size to gauge potential oversubscription

5. **Map demand against deal structure**
   - Estimate total book coverage at various price points within the filing range
   - Identify concentration risk — if top 10 investors represent >50% of expected demand, flag for diversification
   - Assess sensitivity to greenshoe exercise and potential stabilization needs
   - Recommend marketing priorities: which investors need 1-on-1 meetings vs. group lunches vs. virtual-only

## Output

Deliver a structured **Institutional Demand Analysis** containing:

- **Executive summary**: headline demand assessment (strong/moderate/soft), key risks, and recommended actions
- **Investor target matrix**: tabular list with columns for investor name, style, AUM, sector allocation %, comparable deal participation count, estimated order size, tier ranking, and recommended marketing approach
- **Demand waterfall**: visual or tabular breakdown of estimated demand at low/mid/high price points, showing contribution by investor tier
- **Comparable deal benchmarks**: table of 5–10 recent transactions with pricing outcome, oversubscription level, aftermarket performance, and top allocatees
- **Risk flags**: concentration risk, flipper exposure, sector rotation headwinds, or calendar conflicts with competing offerings
- **Recommended roadshow strategy**: prioritized cities/meetings based on where highest-quality demand is concentrated

## Quality Checks

- Confirm all 13F data is from the most recent available filing period — stale data (>1 quarter old) must be flagged [VERIFY filing dates]
- Cross-check investor style classifications against multiple sources (eVestment, Morningstar, PitchBook) — self-reported styles often diverge from actual behavior
- Validate that comparable transactions are genuinely comparable (same sector, ±50% deal size, same deal type, within 18 months)
- Ensure estimated demand totals are internally consistent — sum of individual investor estimates should reconcile to aggregate demand figure
- Verify no restricted or wall-crossed investors are included in open-market targeting lists [VERIFY compliance status]
- Confirm that any fund-level data respects aggregation rules — separate accounts, sub-advised mandates, and fund-of-funds positions should not be double-counted
