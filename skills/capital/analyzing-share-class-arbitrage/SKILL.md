---
name: analyzing-share-class-arbitrage
language: en
description: Evaluates dual-class share structures with discount analysis, unification catalysts, and governance reform probability assessment. Use when analyzing share class spreads, evaluating unification likelihood, or assessing dual-class dynamics.
tags:
  - analysis
  - activist-and-event-driven-investing
metadata:
  author: casemark
  practice_areas:
    - Activist Investing
    - Event-Driven Strategy
    - Special Situations
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Share Class Arbitrage

Evaluates dual-class share structures with discount analysis, unification catalysts, and governance reform probability assessment.

## When To Use

- Assessing the spread between voting and non-voting (or limited-voting) share classes for a potential arbitrage position
- Evaluating whether a dual-class unification is likely and pricing the probability-weighted upside
- Analyzing governance reform catalysts (activist campaigns, index inclusion pressure, regulatory changes, founder transitions)
- Screening for share class discount compression opportunities across a universe of dual-class issuers
- Supporting an activist thesis that includes a unification demand or governance simplification proposal

## Inputs To Gather

- **Share class structure**: Number of classes, voting rights per share, economic rights per share, conversion ratios, and any sunset provisions [VERIFY sunset clause details against charter/articles]
- **Market data**: Current prices for each share class, historical spread (3-year minimum), trading volumes, and float for each class
- **Ownership breakdown**: Insider/founder voting control percentage, institutional ownership by class, index fund holdings
- **Corporate governance documents**: Articles of incorporation, bylaws, any shareholder agreements governing class conversion or unification [VERIFY jurisdiction-specific rules on charter amendments]
- **Catalyst timeline inputs**: Founder age/succession planning signals, upcoming index rebalancing dates, pending regulatory proposals (e.g., stock exchange listing standard changes), activist 13D/13F filings
- **Comparable transactions**: Prior unification transactions in the same sector or jurisdiction, including exchange ratios and premiums paid

## Workflow

1. **Map the share class structure**
   - Document each class's voting power, economic entitlement, and conversion mechanics
   - Identify any automatic sunset triggers (time-based, ownership threshold, death/incapacity of founder)
   - Flag any anti-unification provisions (supermajority vote requirements, board-only conversion authority)

2. **Calculate the current discount and historical range**
   - Compute the non-voting (or low-vote) discount: `(Price_High_Vote - Price_Low_Vote) / Price_High_Vote`
   - Chart the discount over 1-, 3-, and 5-year windows to identify trend direction
   - Benchmark against peer dual-class issuers in the same sector and market cap range

3. **Identify and score unification catalysts**
   - For each potential catalyst, assign a probability estimate (low / medium / high) and expected time horizon:
     - **Founder transition**: Aging founder, succession planning announcements, estate planning signals
     - **Index pressure**: Exclusion from or conditional inclusion in major indices (S&P 500, FTSE Russell) [VERIFY current index provider policies on dual-class eligibility]
     - **Activist engagement**: Existing 13D filings, proxy contest history, public letter campaigns
     - **Regulatory/exchange action**: Proposed listing standard changes, SEC rulemaking
     - **Capital markets need**: Company likely to issue equity, pursue M&A, or seek debt refinancing where simplified structure helps
   - Weight each catalyst by its historical success rate in comparable situations

4. **Model the unification economics**
   - Estimate the likely exchange ratio (typically 1:1, but review precedent transactions for premium/discount adjustments)
   - Calculate the probability-weighted return: `Expected Return = P(unification) × (Upside at unification) - (1 - P(unification)) × (Carry cost + Discount drift risk)`
   - Sensitivity-test key assumptions: probability of unification, time to unification, and exchange ratio
   - Factor in dividend differentials between classes (if any) as carry income or cost

5. **Assess risks and friction**
   - **Controlling shareholder blocking power**: Can insiders single-handedly block a charter amendment? [VERIFY vote threshold requirements under applicable state/country corporate law]
   - **Liquidity risk**: Low-float share classes may have wide bid-ask spreads and slippage on exit
   - **Time decay**: Opportunity cost if the discount persists for years without a catalyst
   - **Adverse selection**: Insiders may have informational advantages about the likelihood of unification

6. **Formulate the trade structure**
   - Long the discounted class / short the premium class (classic convergence trade), or
   - Outright long the discounted class with a catalyst thesis (directional)
   - Size the position relative to liquidity constraints and portfolio risk limits

## Output

The deliverable is a **Share Class Arbitrage Analysis Report** containing:

- **Executive summary**: Ticker, share classes analyzed, current discount, top catalyst, and recommendation (trade / monitor / pass)
- **Structure overview table**: Side-by-side comparison of each class (votes, economics, conversion rights, float, volume)
- **Discount analysis**: Current level, historical range, percentile ranking, peer comparison chart
- **Catalyst scorecard**: Each catalyst rated by probability, timing, and impact, with an aggregate unification probability estimate
- **Return model**: Base, bull, and bear scenario returns with explicit assumptions for each
- **Risk matrix**: Key risks ranked by severity and likelihood, with mitigants identified
- **Trade recommendation**: Entry structure, sizing guidance, target exit levels, and stop-loss parameters

## Quality Checks

- Confirm all voting and economic rights are sourced from the actual charter or articles of incorporation, not secondary summaries
- Verify that the discount calculation uses contemporaneous pricing (same date/time for both classes)
- Ensure catalyst probabilities are grounded in comparable precedent transactions, not arbitrary estimates
- Check that the return model accounts for borrow costs (if shorting the premium class) and dividend differentials
- Validate that jurisdiction-specific vote thresholds for charter amendments are correctly applied [VERIFY]
- Confirm no stale data: index policy dates, activist filing dates, and founder biographical details should be current
- Flag any situation where the analysis relies on a single catalyst — diversified catalyst support strengthens conviction
