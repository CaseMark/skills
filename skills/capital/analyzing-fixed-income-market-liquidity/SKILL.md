---
name: analyzing-fixed-income-market-liquidity
language: en
description: Evaluates bond market liquidity with bid-ask spread analysis, dealer inventory assessment, and electronic trading penetration. Use when analyzing bond liquidity, assessing execution conditions, or evaluating venue selection.
tags:
  - analysis
  - public-markets-and-trading
  - trading
metadata:
  author: casemark
  practice_areas:
    - Trading
    - Market Making
    - Execution
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Fixed Income Market Liquidity

## When To Use

- Evaluating execution conditions before sizing or routing a bond trade
- Comparing liquidity across sectors (IG corporates, HY, munis, agency MBS, sovereigns) for portfolio rebalancing
- Assessing dealer willingness to warehouse risk in current market conditions
- Selecting optimal execution venue (voice, RFQ, portfolio trade, all-to-all)
- Monitoring liquidity regime shifts that may affect mark-to-market or redemption risk
- Preparing pre-trade cost analysis or transaction cost analysis (TCA) reviews

## Inputs To Gather

- **Security identifiers**: CUSIP/ISIN, issuer, coupon, maturity, sector, rating
- **Market data**: Recent bid-ask spreads, trade counts (TRACE/FINRA for USD; MiFID II reporting for EUR), dealer axe sheets
- **Dealer inventory signals**: Primary dealer position data (Fed NY weekly release), inventory proxies from axe frequency [VERIFY: data source availability and lag]
- **Electronic trading metrics**: Platform volumes (MarketAxess, Tradeweb, Bloomberg), RFQ response rates, hit ratios
- **Benchmark comparisons**: On-the-run vs. off-the-run treasury spreads, index-eligible vs. non-index spread differentials
- **Macro context**: Fed/ECB policy stance, recent volatility (MOVE index), credit spread levels (CDX IG/HY)
- **Trade parameters**: Notional size, urgency, direction (buy vs. sell), and any portfolio-trade context

## Workflow

1. **Define scope and segmentation**
   - Identify the specific bond or sector to analyze
   - Segment by credit quality (IG/HY/distressed), maturity bucket (short/intermediate/long), and issue size
   - Note whether analysis is pre-trade (execution planning) or post-trade (TCA/surveillance)

2. **Measure bid-ask spread conditions**
   - Pull recent bid-ask spreads from dealer quotes or composite sources
   - Compare current spreads to 30-day, 90-day, and 1-year rolling averages
   - Distinguish between round-lot and odd-lot spreads — odd lots typically show 2–5x wider spreads in corporates
   - Flag any securities where quoted spreads have widened >1 standard deviation from recent norms

3. **Assess dealer inventory and market-making depth**
   - Review primary dealer net positions for the relevant sector [VERIFY: publication frequency and reporting lag]
   - Analyze axe sheet frequency — higher axe activity on a specific bond signals willingness to trade
   - Note concentration risk: if fewer than 3 dealers are actively quoting, flag as thin liquidity
   - Evaluate block trade capacity — can the street absorb the contemplated size in one print, or is work-up needed?

4. **Evaluate electronic trading penetration and venue dynamics**
   - Compare share of volume executed electronically vs. voice for the sector
   - For IG corporates: electronic share typically 35–45% by volume; HY significantly lower (~15–25%) [VERIFY: current platform-reported figures]
   - Assess RFQ response rates and average number of competing responses
   - Consider all-to-all platforms for less liquid names where dealer quotes are sparse
   - Evaluate portfolio trading suitability if multiple line items are involved (typically 50+ lines for efficiency)

5. **Quantify liquidity score and regime classification**
   - Assign a composite liquidity score incorporating: bid-ask spread (40%), trade frequency (25%), dealer depth (20%), electronic accessibility (15%)
   - Classify current regime: **Normal**, **Stressed**, or **Dislocated** based on spread z-scores and volume drop-off
   - Benchmark against historical episodes (e.g., Mar 2020 dislocation, 2022 rate volatility, SVB event)

6. **Develop execution recommendations**
   - For liquid names (score ≥ 7/10): electronic RFQ with 5+ dealers, limit order acceptable
   - For semi-liquid (score 4–6): voice negotiation with 2–3 axed dealers, consider working order over 1–2 sessions
   - For illiquid (score < 4): principal bid wanted in competition (BWIC), or patient approach with targeted dealer outreach
   - Size-adjust recommendations — execution cost rises non-linearly with size in illiquid sectors

## Output

The deliverable should include:

- **Liquidity dashboard**: Summary table with bid-ask spread (current vs. average), daily trade count, dealer depth count, e-trading share, and composite liquidity score per security or sector
- **Regime assessment**: Current liquidity regime classification with supporting metrics and historical comparison
- **Execution strategy memo**: Recommended venue, protocol (RFQ/voice/BWIC/portfolio trade), dealer shortlist, and suggested execution horizon
- **Cost estimate**: Expected transaction cost in basis points, broken into bid-ask component and market impact component
- **Risk flags**: Securities or sectors where liquidity deterioration may affect portfolio NAV, redemption capacity, or compliance limits

## Quality Checks

- Verify that bid-ask data reflects actual executable quotes, not stale or indicative levels
- Confirm trade count data source and ensure reporting completeness (TRACE dissemination covers ~99% of USD corporates; muni and ABS coverage varies) [VERIFY: current TRACE dissemination rules for the specific sector]
- Cross-check dealer inventory signals against multiple sources — single-source reliance creates false confidence
- Ensure liquidity scores are calibrated to the relevant sector; a 5 bp spread is tight for HY but wide for on-the-run treasuries
- Validate that execution recommendations account for current market hours and settlement conventions (T+1 for treasuries, T+2 for corporates) [VERIFY: settlement cycle for jurisdiction and instrument type]
- Flag any data gaps or stale inputs explicitly rather than interpolating silently
