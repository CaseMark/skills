---
name: managing-share-repurchase-programs
description: Structures buyback program analysis with timing, accretion impact, and regulatory compliance documentation. Use when analyzing buybacks, modeling EPS accretion, or documenting repurchase programs.
tags:
  - management
  - corporate-finance
  - compliance
  - regulatory
metadata:
  author: casemark
  practice_areas:
    - Corporate Finance
    - Treasury
    - Financial Planning
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Share Repurchase Programs

Structures buyback program analysis with timing, accretion impact, and regulatory compliance documentation.

## When To Use

- Board has authorized a new or expanded share repurchase program and treasury needs an execution framework
- Management requests EPS accretion/dilution modeling to evaluate buyback size and timing
- Quarterly or annual reporting requires documentation of repurchase activity, remaining authorization, and compliance status
- Evaluating whether to execute via open-market purchases, accelerated share repurchase (ASR), or tender offer
- Preparing 10b-18 safe harbor compliance documentation or reviewing trading window restrictions

## Inputs To Gather

- **Board authorization**: Resolution text, total dollar amount authorized, expiration date, any per-period or per-day limits
- **Share data**: Current shares outstanding (basic and diluted), weighted-average shares, treasury shares, float
- **Financial projections**: Forward EPS estimates, net income forecasts, free cash flow projections, debt capacity
- **Market data**: Current share price, average daily trading volume (ADTV), historical price range, VWAP benchmarks
- **Capital structure context**: Existing leverage ratios, credit agreement buyback restrictions, rating agency thresholds
- **Regulatory parameters**: Blackout window calendar, insider trading policy dates, Rule 10b-18 volume/timing/price conditions [VERIFY jurisdiction-specific rules]
- **Prior program history**: Shares repurchased to date under current and prior authorizations, average purchase price, remaining capacity

## Workflow

1. **Size the program**: Compare authorized amount against free cash flow, debt headroom, and minimum cash/liquidity requirements. Flag if buyback exceeds 12-month FCF by more than 25% as a leverage risk indicator.

2. **Model EPS accretion**: Calculate pro forma EPS at multiple price points (current, +10%, -10%) and execution schedules (ratable quarterly, front-loaded, opportunistic). Include the offset cost of forgone interest income or incremental borrowing cost on repurchase funding. Present accretion as both absolute cents-per-share and percentage improvement.

3. **Select execution method**:
   - **Open-market (10b-18)**: Default for programs under 12 months; subject to daily volume cap (25% of ADTV), timing restrictions (no opening/closing 10 minutes), and price conditions (at or below highest independent bid) [VERIFY current SEC rule text]
   - **ASR**: Appropriate for large, rapid execution; model the forward contract economics including the dealer's hedge period and final share settlement true-up
   - **Tender offer**: Consider for substantial premium repurchases or Dutch auction structures; requires separate SEC filing and disclosure timeline

4. **Build compliance calendar**: Map blackout windows (earnings, M&A, material non-public information), 10b5-1 plan adoption/cooling-off periods [VERIFY cooling-off period requirements per current SEC rules], and board reporting dates. Identify permissible trading days per quarter.

5. **Document execution parameters**: Specify daily dollar limits, broker instructions, price ceilings, and escalation triggers (e.g., pause if stock exceeds target PE multiple or if leverage ratio approaches covenant threshold).

6. **Track and report**: Maintain a running log of shares purchased (date, quantity, price, broker), cumulative spend versus authorization, remaining capacity, and weighted-average purchase price. Calculate realized accretion versus the original model.

## Output

- **Program summary memo**: Authorization details, selected execution method, target size and timeline, accretion analysis at base/bull/bear price scenarios
- **EPS accretion model**: Spreadsheet-ready table showing quarterly share count reduction, interest cost offset, and net EPS impact through program completion
- **Compliance checklist**: 10b-18 safe harbor conditions, blackout calendar, 10b5-1 plan status, daily volume/price/timing parameters
- **Execution tracker**: Period-by-period log of purchases with running totals, average price, remaining authorization, and variance to plan
- **Board reporting package**: Quarterly summary of activity, market conditions during execution, accretion achieved, and recommendation for continuation/modification/suspension

## Quality Checks

- Confirm shares outstanding figures reconcile to the most recent 10-Q/10-K filing
- Verify that modeled repurchase volume does not exceed 25% of ADTV on any single day under 10b-18 [VERIFY if company uses modified safe harbor]
- Cross-check that total program spend plus existing debt does not breach credit agreement restricted payment baskets or leverage covenants
- Validate blackout window dates against the corporate insider trading policy and any deal-specific restrictions
- Ensure accretion calculations use the correct tax rate on forgone interest income and reflect the actual share reduction timing (not instantaneous)
- Confirm that 10b5-1 plan terms comply with current SEC cooling-off and certification requirements [VERIFY effective date of most recent SEC amendments]
