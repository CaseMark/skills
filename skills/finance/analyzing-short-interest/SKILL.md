---
name: analyzing-short-interest
description: Monitors short interest dynamics with days-to-cover calculations and squeeze risk assessment. Use when tracking short interest, analyzing borrowing costs, or assessing short squeeze risk.
tags:
  - analysis
  - equity-research
  - risk
metadata:
  author: casemark
  practice_areas:
    - Equity Research
    - Investment Management
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Short Interest

Monitors short interest dynamics with days-to-cover calculations and squeeze risk assessment.

## When To Use

- Evaluating whether a stock faces elevated short squeeze risk before initiating or sizing a position
- Screening a portfolio or watchlist for unusual short interest changes between reporting periods
- Assessing the cost and availability of borrow for a prospective short position
- Investigating price dislocations where short covering may be a contributing factor
- Building a contrarian thesis around heavily shorted names

## Inputs To Gather

- **Short interest data**: Shares sold short (current and prior reporting period) from exchange filings [VERIFY reporting dates — FINRA publishes twice monthly with ~10 business day lag]
- **Float and shares outstanding**: From latest SEC filing (10-Q/10-K) or data vendor; confirm any recent dilution events (offerings, warrant exercises, conversions)
- **Average daily volume (ADTV)**: Use 20-day and 90-day ADTV to calculate days-to-cover under different liquidity assumptions
- **Borrow rate / fee rate**: Securities lending data from prime broker, ORTEX, S3 Partners, or similar source; note whether rate is annualized
- **Institutional ownership**: 13F filings — high institutional ownership with low float amplifies squeeze dynamics
- **Options open interest**: Put/call ratio, concentrated strike prices, and upcoming expiration dates relevant to gamma squeeze potential
- **Catalyst calendar**: Earnings dates, FDA decisions, index rebalance dates, lock-up expirations, or other events that could trigger covering

## Workflow

1. **Calculate core metrics**
   - **Short interest ratio (SI % of float)**: Shares short / free float. Flag >15% as elevated, >25% as extreme
   - **Days to cover (DTC)**: Shares short / ADTV. Use both 20-day and 90-day ADTV. DTC >5 days signals meaningful covering difficulty; >10 days is a squeeze setup prerequisite
   - **Short interest change**: Period-over-period delta. Rapid increases (>20% change between reporting periods) warrant attention
   - **Utilization rate**: Shares on loan / lendable supply. Above 90% indicates tight borrow conditions

2. **Assess borrow conditions**
   - Classify borrow: General Collateral (<1% fee), Warm (1–10% fee), Hard-to-Borrow (>10% fee), or Special (fee spikes, recall risk)
   - Note any recent borrow rate trajectory — rising rates with stable SI suggest supply contraction
   - Identify forced buy-in risk if utilization is near 100% and lenders are recalling shares

3. **Evaluate squeeze risk factors**
   - Score each squeeze catalyst dimension:
     - **Liquidity trap**: DTC >7 days AND low float (<50M shares)
     - **Borrow squeeze**: Utilization >90% AND fee rate rising
     - **Gamma ramp**: Heavy call open interest at strikes 10–30% above current price near expiration
     - **Catalyst proximity**: Binary event within 30 days that could force directional resolution
     - **Ownership concentration**: Top 10 holders own >60% of outstanding, leaving thin tradeable supply
   - Assign overall squeeze risk: Low / Moderate / Elevated / Critical

4. **Contextualize with fundamental overlay**
   - Determine whether the short thesis is based on valuation, fraud allegation, secular decline, or event-driven catalyst
   - Assess whether recent fundamental developments (earnings beat, partnership, regulatory approval) undermine the short thesis
   - Note any activist short seller public reports or 13D/13G filings from known short-biased funds

5. **Identify actionable signals**
   - For long investors: Quantify asymmetric upside if covering accelerates; define entry triggers (price levels, volume thresholds)
   - For short sellers: Assess risk/reward of maintaining position given borrow cost drag and squeeze exposure
   - For risk managers: Flag positions where short interest dynamics create outsized tail risk

## Output

Produce a **Short Interest Analysis Report** containing:

- **Summary table**: Ticker, SI shares, SI % of float, DTC (20d/90d), utilization, borrow rate, period change
- **Squeeze risk scorecard**: Each factor rated with brief rationale, overall risk level assigned
- **Borrow cost analysis**: Current fee, trend, estimated annualized cost drag on a short position
- **Trend chart description**: SI % of float over last 6–12 reporting periods with key events annotated
- **Catalysts and triggers**: Upcoming events that could accelerate covering or increase short conviction
- **Actionable conclusion**: Clear statement of what the short interest dynamics imply for the investment thesis

## Quality Checks

- Confirm short interest data date and that it corresponds to the correct settlement period [VERIFY exchange reporting schedule]
- Cross-reference float figures — discrepancies between data vendors are common; note the source used
- Verify that DTC calculation uses the matching ADTV period and that volume isn't distorted by a single anomalous session
- Ensure borrow rate data is current (intraday rates can move sharply); note timestamp
- Check that SI % of float doesn't exceed 100% without explanation (legitimate in cases of rehypothecation, but flag it)
- [VERIFY] Reg SHO threshold list status — if the security appears on the threshold list, note duration and implications
- Disclaim that short interest data is lagged and that real-time positioning may differ materially from reported figures
