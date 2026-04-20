---
name: managing-concentrated-positions
language: en
description: Structures diversification strategies for concentrated single-stock positions with tax and risk considerations. Use when managing concentrated holdings, planning diversification, or evaluating exchange funds.
tags:
  - management
  - asset-management
  - risk
  - tax
metadata:
  author: casemark
  practice_areas:
    - Portfolio Management
    - Asset Management
    - Wealth Management
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Concentrated Positions

## When To Use

- Client holds >10–15% of liquid net worth in a single stock or small cluster of correlated positions
- Founder/executive equity from IPO, acquisition, or long-tenure stock compensation is vesting or lock-up is expiring
- Estate or gift planning requires reducing single-name exposure while managing capital gains
- Risk review flags portfolio volatility driven by concentrated holding
- Client requests evaluation of exchange funds, hedging overlays, or charitable disposition strategies

## Inputs To Gather

- **Position details**: ticker, share count, cost basis (including lot-level basis if available), acquisition dates, current market value
- **Restriction status**: Rule 144 holding periods, 10b5-1 plan status, insider trading windows, contractual lock-ups, pledging restrictions [VERIFY against issuer-specific policies]
- **Tax profile**: federal and state marginal rates, net investment income tax applicability, prior-year capital loss carryforwards, AMT exposure from ISO exercises
- **Client objectives**: target concentration threshold, liquidity needs and timeline, risk tolerance score, legacy/philanthropic goals
- **Existing hedges or prior transactions**: outstanding collars, prepaid variable forwards, prior gifting of appreciated shares
- **Regulatory constraints**: Section 16 status, affiliate vs. non-affiliate classification under Rule 144 [VERIFY]

## Workflow

1. **Quantify concentration risk**
   - Calculate position as percentage of total investable assets and liquid net worth
   - Run downside scenario analysis: 20%, 40%, 60% drawdown impact on overall portfolio
   - Estimate position beta and correlation to existing portfolio holdings
   - Compute marginal contribution to portfolio volatility

2. **Determine embedded tax cost**
   - Map lot-level cost basis and holding periods (short-term vs. long-term)
   - Calculate gross unrealized gain and effective tax rate on full liquidation
   - Identify loss lots or near-basis lots eligible for immediate sale with minimal tax impact
   - Model state tax variations if client has multi-state exposure [VERIFY state-specific rates]

3. **Evaluate diversification strategies**
   - **Direct sale and reinvest**: simplest path; model after-tax proceeds and reinvestment return needed to break even vs. holding
   - **Systematic sales (10b5-1 plan)**: staged liquidation over 12–36 months to spread gains across tax years; confirm Rule 10b5-1 cooling-off periods [VERIFY current SEC requirements]
   - **Exchange fund contribution**: evaluate eligibility (qualified purchaser, 7-year lock-up, diversification upon exit); compare fee drag vs. tax deferral benefit
   - **Hedging overlays**: zero-cost collars (cap upside, floor downside), prepaid variable forwards (monetize without current sale), protective puts (pure downside protection at premium cost); assess constructive sale risk under IRC §1259 [VERIFY]
   - **Charitable strategies**: donor-advised fund contribution of appreciated shares (full FMV deduction, avoid capital gains), charitable remainder trust (income stream + charitable deduction + diversification inside trust), charitable lead trust for transfer tax reduction
   - **Gift and estate transfers**: annual exclusion gifts of appreciated shares to lower-bracket family members, GRAT funding with concentrated stock, IDGT sale to remove appreciation from estate

4. **Build implementation plan**
   - Rank strategies by after-tax efficiency, liquidity generated, and alignment with client goals
   - Define target allocation post-diversification and transition timeline
   - Set volume limits for sales (SEC safe harbor: ≤1% of outstanding shares per quarter for affiliates) [VERIFY current thresholds]
   - Coordinate with estate planning, tax counsel, and compliance as needed
   - Draft 10b5-1 plan or hedge term sheet if applicable

5. **Monitor and adjust**
   - Track position concentration quarterly against target threshold
   - Reassess hedging economics if stock price moves significantly (collar strike recalibration)
   - Update tax projections annually to optimize gain recognition timing
   - Review lock-up and restriction expirations on rolling basis

## Output

The deliverable is a **Concentrated Position Management Report** containing:

- Position summary table: ticker, shares, cost basis, unrealized gain, % of portfolio
- Risk analysis: downside scenarios, volatility contribution, correlation metrics
- Strategy comparison matrix: each strategy scored on tax efficiency, liquidity, complexity, cost, and time horizon
- Recommended action plan with sequenced steps and decision milestones
- Tax projection: estimated capital gains liability under each scenario across relevant tax years
- Compliance checklist: trading window, Rule 144, Section 16, constructive sale safeguards

## Quality Checks

- Verify cost basis against brokerage statements — do not rely on client estimates alone
- Confirm insider/affiliate status and any blackout windows before recommending sale timing [VERIFY]
- Validate exchange fund eligibility: qualified purchaser status, minimum contribution, acceptable asset types
- Check constructive sale rules for any hedging strategy that eliminates substantially all risk of loss and opportunity for gain
- Ensure charitable deduction calculations use correct FMV methodology (publicly traded = closing price on contribution date)
- Cross-check state tax treatment — some states do not conform to federal long-term capital gains rates [VERIFY]
- Flag any strategy requiring board pre-clearance or Section 16 reporting within 2 business days
