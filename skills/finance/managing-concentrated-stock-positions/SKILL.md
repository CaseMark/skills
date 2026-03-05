---
name: managing-concentrated-stock-positions
description: Evaluates strategies for concentrated equity positions with tax-efficient diversification and hedging analysis. Use when managing concentrated positions, planning diversification, or evaluating hedging strategies.
tags:
  - management
  - wealth-management
  - tax
metadata:
  author: casemark
  practice_areas:
    - Wealth Management
    - Private Banking
    - Financial Planning
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Concentrated Stock Positions

## When To Use

- Client holds a single equity position exceeding 10-15% of liquid net worth
- Founder/executive approaching lock-up expiration or 10b5-1 plan window
- Triggering event: IPO, secondary offering, M&A closing, or vesting cliff
- Client requests diversification but faces significant embedded capital gains
- Portfolio risk review flags single-name concentration risk
- Estate or charitable planning where appreciated stock is a core asset

## Inputs To Gather

- **Position details**: Ticker, share count, cost basis (lot-level if available), acquisition dates, holding period status (short-term vs. long-term)
- **Restriction status**: Rule 144 holding periods, lock-up agreements, 10b5-1 plan status, Section 16 insider status, blackout windows [VERIFY with counsel]
- **Client profile**: Risk tolerance, liquidity needs, time horizon, income tax bracket (federal + state), net investment income tax exposure
- **Existing hedges**: Outstanding collars, prepaid variable forwards (PVFs), exchange fund commitments, or margin loans against the position
- **Tax situation**: Current-year realized gains/losses, loss carryforwards, AMT exposure, state of residence [VERIFY state tax treatment for each strategy]
- **Estate and philanthropic goals**: Charitable intent, generation-skipping objectives, trust structures in place
- **Corporate governance**: Any contractual or company-policy restrictions on hedging or pledging shares

## Workflow

1. **Quantify concentration risk**
   - Calculate position as % of liquid net worth and total net worth
   - Run downside scenario analysis: -20%, -40%, -60% drawdowns and impact on financial plan
   - Estimate portfolio volatility contribution vs. a diversified benchmark
   - Identify correlation with client's human capital (e.g., tech executive holding tech stock)

2. **Assess tax cost of outright sale**
   - Compute federal + state capital gains liability per lot
   - Model after-tax proceeds vs. current value
   - Identify high-basis lots eligible for lower-cost liquidation
   - Factor in net investment income tax (3.8%) and any state surcharges [VERIFY current rates]

3. **Evaluate diversification strategies**
   - **Staged open-market sales**: Spread across tax years to manage bracket exposure; pair with harvested losses
   - **10b5-1 plan**: Appropriate for insiders; establish during open trading window with required cooling-off period [VERIFY SEC Rule 10b5-1 amendments for cooling-off requirements]
   - **Exchange funds (swap funds)**: Contribute concentrated stock into a diversified partnership; requires 7-year lock-up and meeting qualifying asset mix rules under IRC 721(a)/351 [VERIFY fund-specific terms and accredited investor thresholds]
   - **Charitable strategies**: Donor-advised fund contributions of appreciated shares (up to 30% AGI), charitable remainder trusts (CRTs) for income stream + partial deduction, charitable lead trusts (CLTs) for estate reduction
   - **Gifting**: Annual exclusion gifts or completed gifts to irrevocable trusts to shift future appreciation; GRATs funded with concentrated stock

4. **Evaluate hedging strategies**
   - **Costless collars (zero-premium)**: Set protective put floor and covered call cap; no upfront cost but caps upside. Evaluate constructive sale risk under IRC 1259 [VERIFY collar width to avoid constructive sale treatment]
   - **Prepaid variable forwards (PVFs)**: Monetize position while deferring tax recognition; receive upfront cash (typically 75-90% of current value). Assess loan-vs-sale characterization risk [VERIFY with tax counsel]
   - **Protective puts**: Outright downside protection; premium cost but unlimited upside. Best for shorter-term risk windows (earnings, lock-up expiration)
   - **Margin loans / securities-backed lending**: Borrow against position for liquidity without triggering a sale; monitor loan-to-value covenants and margin call risk

5. **Model combined strategy scenarios**
   - Build 3-5 scenarios combining partial sale, hedging, and charitable giving
   - For each scenario: project after-tax wealth at 1, 3, 5, and 10 years under base, bull, and bear market assumptions
   - Compare effective tax rates, liquidity generated, remaining concentration %, and estate transfer efficiency
   - Stress test margin loan scenarios for forced liquidation at worst-case valuations

6. **Document recommendation and implementation plan**
   - Rank strategies by tax efficiency, liquidity, and alignment with client objectives
   - Specify execution timeline: trading windows, 10b5-1 plan adoption dates, exchange fund closing dates, charitable contribution deadlines (year-end)
   - Identify required third parties: tax counsel, corporate secretary (for pre-clearance), options desk, exchange fund sponsor, trust/estate attorney

## Output

Produce a **Concentrated Position Management Report** containing:

- **Executive summary**: Current concentration level, estimated unrealized gain, key risk metrics, and recommended strategy
- **Position profile table**: Shares, cost basis by lot, holding period, restriction status, current market value
- **Strategy comparison matrix**: Each strategy scored on tax efficiency, liquidity, risk reduction, complexity, and cost
- **Scenario projections**: After-tax wealth outcomes under recommended vs. alternative approaches across market scenarios
- **Implementation timeline**: Sequenced action items with responsible parties and deadlines
- **Risk disclosures**: Constructive sale risk, margin call exposure, regulatory filing obligations (Form 4, Form 144), and strategy-specific risks

## Quality Checks

- Confirm all cost basis data is lot-level and sourced from custodial records, not client estimates
- Verify insider status and trading restrictions with corporate counsel before recommending any sale or hedge [VERIFY]
- Ensure collar strike prices are wide enough to avoid constructive sale treatment under IRC 1259 [VERIFY with tax advisor]
- Validate that exchange fund qualifies under IRC 721(a) diversification rules and that client meets accredited investor requirements
- Check that charitable contribution deduction calculations use correct AGI limitation (30% for appreciated capital gain property to public charity) [VERIFY for private foundation gifts: 20% AGI limit]
- Confirm PVF terms do not trigger current income recognition under IRS prepaid forward guidance
- Stress test all margin/lending scenarios at 40-50% drawdown to confirm client can meet margin calls without forced liquidation
- Flag any state-specific tax treatment differences (e.g., California sources gains based on residency at time of sale) [VERIFY state rules]
