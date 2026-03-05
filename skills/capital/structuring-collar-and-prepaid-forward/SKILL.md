---
name: structuring-collar-and-prepaid-forward
description: Designs equity monetization structures with zero-cost collars, prepaid variable forwards, and exchange fund alternatives. Use when structuring equity monetization, designing collars, or evaluating concentrated stock solutions.
tags:
  - derivatives-and-structured-products
metadata:
  author: casemark
  practice_areas:
    - Derivatives
    - Structured Products
    - Hedging
  document_types:
    - Report
  skill_modes:
    - Analysis
---
# Structuring Collar And Prepaid Forward

Designs equity monetization structures with zero-cost collars, prepaid variable forwards, and exchange fund alternatives for concentrated equity positions.

## When To Use

- Client holds a concentrated single-stock position and needs liquidity without triggering an immediate taxable sale
- Evaluating hedging strategies for executives or founders with lock-up or Rule 144 constraints
- Comparing zero-cost collars, prepaid variable forwards (PVFs), and exchange fund eligibility
- Structuring monetization around margin loan alternatives for large equity blocks
- Advising on post-IPO or post-vesting liquidity planning for restricted stockholders

## Inputs To Gather

- **Position details**: ticker, share count, cost basis, acquisition date, holding period status (long-term vs. short-term)
- **Ownership constraints**: Rule 144 volume limits, lock-up expiry dates, Section 16 insider status, 10b5-1 plan existence
- **Liquidity target**: dollar amount needed, timing requirements, ongoing cash-flow needs vs. one-time extraction
- **Tax profile**: federal and state marginal rates, net investment income tax exposure, prior capital gains/losses, estate planning horizon
- **Risk tolerance**: acceptable downside floor, willingness to cap upside, preference for retaining dividends and voting rights
- **Current market data**: spot price, implied volatility surface, dividend yield, interest rate curve, borrow cost for the underlying
- **Counterparty context**: investment bank or prime broker proposed terms, ISDA/CSA status, credit support requirements

## Workflow

1. **Assess position and constraints**
   - Confirm holding period qualifies for long-term capital gains treatment [VERIFY: jurisdiction-specific rates and NIIT thresholds]
   - Identify Rule 144 limitations, contractual lock-ups, and any blackout windows
   - Determine whether Section 1259 constructive sale rules constrain available structures

2. **Model the zero-cost collar**
   - Select tenor (typically 2–5 years) matching client's liquidity and tax deferral horizon
   - Set the put strike (floor) at 80–95% of spot to define downside protection level
   - Solve for the call strike (cap) that zeros out net premium — wider collar = more upside retained
   - Evaluate collar economics: effective monetization rate, dividend pass-through, voting retention
   - Flag if collar strikes are too narrow, risking constructive sale treatment under IRC Section 1259 [VERIFY]

3. **Model the prepaid variable forward**
   - Calculate upfront cash advance (typically 75–90% of spot) based on interest rates and implied vol
   - Define settlement terms: variable delivery ratio between floor and cap at maturity
   - Compare PVF advance rate against collar + margin loan equivalent economics
   - Confirm PVF does not trigger constructive sale — requires meaningful spread between floor and cap delivery ratios [VERIFY: Rev. Rul. 2003-7 guidance and subsequent developments]

4. **Evaluate exchange fund alternative**
   - Determine eligibility: position must be marketable securities, client must be a qualified purchaser or accredited investor [VERIFY: fund-specific requirements]
   - Model diversification benefit — contribution of concentrated stock into a partnership holding multiple positions
   - Assess 7-year holding requirement and tax consequences at exit
   - Compare exchange fund illiquidity cost against collar/PVF optionality cost

5. **Run comparative analysis**
   - Build side-by-side table: immediate sale vs. collar + loan vs. PVF vs. exchange fund
   - Quantify after-tax proceeds, upside participation retained, liquidity timing, and credit/counterparty risk
   - Stress test under ±30% underlying price moves and interest rate shifts
   - Factor in estate planning overlay — stepped-up basis at death vs. lifetime monetization trade-off

6. **Structure recommendation and documentation**
   - Select optimal structure (or hybrid) with rationale tied to client priorities
   - Draft term sheet outline with key economic terms for counterparty negotiation
   - Identify required legal documentation: ISDA Master Agreement, CSA, collar/PVF confirmation, pledge agreements
   - Note regulatory filings: Form 4 for insiders, Schedule 13D/G amendments if applicable [VERIFY]

## Output

- **Structure comparison matrix**: side-by-side of collar, PVF, exchange fund, and outright sale showing net proceeds, tax deferral period, upside/downside economics, and liquidity timeline
- **Recommended structure memo**: 2–4 page narrative with rationale, key economic terms, risk factors, and tax treatment summary
- **Sensitivity analysis**: tables or charts showing outcomes across spot price scenarios, vol changes, and rate movements
- **Implementation checklist**: sequenced action items covering counterparty selection, documentation, regulatory filings, and settlement mechanics

## Quality Checks

- Confirm Section 1259 constructive sale analysis is addressed for every collar and PVF structure — document the spread between floor and cap that preserves tax deferral [VERIFY: current safe harbor guidance]
- Validate that Rule 144 volume and manner-of-sale conditions are satisfied for any hedging overlay on restricted shares
- Verify cost basis and holding period inputs — errors here cascade through all after-tax calculations
- Cross-check upfront advance rates and collar strikes against current market data (implied vol, rates, dividends)
- Ensure estate planning implications are flagged: monetization locks in current value while forfeiting potential stepped-up basis
- Confirm all regulatory filing obligations are identified for insider or large-holder clients [VERIFY: Form 4 timing, 13D/G amendment thresholds]
