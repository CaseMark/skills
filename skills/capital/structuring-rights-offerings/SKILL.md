---
name: structuring-rights-offerings
language: en
description: Designs rights issue structures with subscription ratios, pricing discounts, and standby underwriting arrangements. Use when structuring rights offerings, analyzing dilution protection, or evaluating capital raise alternatives.
tags:
  - equity-capital-markets
metadata:
  author: casemark
  practice_areas:
    - ECM
    - IPO Advisory
    - Equity Origination
  document_types:
    - Report
  skill_modes:
    - Analysis
---
# Structuring Rights Offerings

Designs rights issue structures with subscription ratios, pricing discounts, and standby underwriting arrangements.

## When To Use

- Issuer needs to raise equity capital while giving existing shareholders pre-emptive participation
- Board is evaluating a rights offering versus a marketed follow-on, private placement, or PIPE
- Analyzing dilution impact on shareholders who do not exercise subscription rights
- Structuring standby underwriting or backstop commitments to ensure full subscription
- Pricing a rights offering discount relative to theoretical ex-rights price (TERP)
- Evaluating oversubscription privilege mechanics and allocation methodology

## Inputs To Gather

- **Issuer profile**: current share price, shares outstanding, market capitalization, float, and major shareholder register
- **Capital requirement**: target gross proceeds, intended use of funds, and minimum acceptable raise
- **Market context**: recent trading volume, volatility, sector comps, and prevailing market sentiment
- **Shareholder base**: institutional vs. retail mix, geographic distribution, and any known holders likely to lapse [VERIFY jurisdiction-specific foreign holder exclusion requirements]
- **Regulatory framework**: listing rules governing maximum discount, record date requirements, subscription period length, and prospectus obligations [VERIFY exchange-specific rules — NYSE, LSE, ASX, HKEX each differ materially]
- **Existing constraints**: anti-dilution provisions in convertible instruments, shareholder approval thresholds, and any pre-existing standby or underwriting commitments

## Workflow

1. **Determine subscription ratio and offer price**
   - Calculate shares needed: target proceeds / offer price per new share
   - Set subscription ratio (e.g., 1-for-4 means 1 new share for every 4 held)
   - Price the discount to TERP — typical range is 15–35% depending on deal size and market conditions
   - Compute TERP: ((existing shares x current price) + (new shares x offer price)) / total post-offer shares
   - Sensitivity-test the ratio and discount across a range of market price movements (±10%, ±20%)

2. **Model dilution and value transfer**
   - Calculate theoretical value per right: (current price − offer price) / (ratio denominator + 1)
   - Show dilution impact for non-exercising shareholders (% ownership reduction and economic dilution)
   - Model outcomes at full take-up, partial take-up (e.g., 70%, 85%), and minimum take-up scenarios
   - Assess impact on EPS, NAV per share, and leverage ratios post-raise

3. **Design subscription mechanics**
   - Define record date, ex-rights date, subscription period (typically 10–21 trading days) [VERIFY local listing rules for minimum period]
   - Determine whether rights are renounceable (tradeable) or non-renounceable
   - If renounceable: specify rights trading period and settlement mechanics
   - Structure oversubscription privilege — capped or uncapped, pro-rata among over-subscribers
   - Address fractional entitlements: aggregate and sell, round down, or round up

4. **Structure underwriting / backstop**
   - Evaluate standby underwriting (underwriter takes unsubscribed shares) vs. hard underwriting (full commitment)
   - Negotiate sub-underwriting syndicate if deal size warrants it
   - Set underwriting fee (typically 1.5–3.0% of gross proceeds) and standby fee on uncommitted portion
   - Include termination events (MAC clauses, market-out conditions, force majeure)
   - If backstop by major shareholder: address related-party considerations and creep provisions [VERIFY takeover code thresholds — e.g., 30% mandatory bid trigger under UK Takeover Code]

5. **Assess regulatory and documentation requirements**
   - Determine prospectus vs. cleansing notice vs. exemption pathway [VERIFY — Reg D, Section 708, EU Prospectus Regulation thresholds]
   - Confirm any shareholder approval requirement based on discount or dilution size
   - Prepare timeline: announcement → record date → despatch → subscription close → allotment → trading
   - Identify restricted jurisdictions for foreign shareholders and structure sell-down or nominee arrangements

## Output

Deliver a structured rights offering analysis containing:

- **Term sheet summary**: subscription ratio, offer price, discount to TERP, gross/net proceeds, key dates
- **Dilution table**: pre- and post-offer shareholding at full, partial, and minimum take-up
- **Financial impact analysis**: pro forma EPS, NAV/share, net debt/EBITDA, and interest coverage post-raise
- **Rights valuation**: theoretical value per right, breakeven share price for exercise decision
- **Underwriting structure**: fee schedule, commitment levels, sub-underwriting allocation, and termination triggers
- **Scenario matrix**: outcomes across different take-up rates and share price movements
- **Comparative analysis**: rights offering vs. alternative structures (accelerated bookbuild, placement, PIPE) on cost, dilution, timeline, and certainty of proceeds
- **Timeline and process chart**: critical path from board approval through allotment

## Quality Checks

- TERP calculation cross-checks: verify arithmetic by working backward from TERP to implied proceeds
- Subscription ratio produces whole-number entitlements for round lots (or fractional handling is specified)
- Discount falls within exchange-permitted maximum [VERIFY — e.g., ASX generally caps at ~25% VWAP discount]
- Dilution percentages are internally consistent across full, partial, and zero exercise scenarios
- Underwriting fees benchmark against recent comparable rights offerings in the same market
- Pro forma financial metrics tie to issuer's latest reported financials plus the modeled raise
- Timeline respects minimum regulatory notice periods and trading day requirements
- All jurisdiction-dependent assumptions are flagged with [VERIFY] for counsel review
