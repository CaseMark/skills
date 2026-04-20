---
name: analyzing-liquidity-risk
language: en
description: Assesses portfolio liquidity with redemption stress testing and market impact estimation. Use when analyzing liquidity risk, stress testing redemptions, or evaluating market impact.
tags:
  - analysis
  - asset-management
  - risk
  - portfolio
metadata:
  author: casemark
  practice_areas:
    - Portfolio Management
    - Asset Management
    - Wealth Management
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Liquidity Risk

## When To Use

- Evaluating whether a fund or portfolio can meet redemption requests under normal and stressed conditions
- Sizing position-level liquidation costs and timeframes before rebalancing or exiting concentrated holdings
- Preparing liquidity risk sections for regulatory filings, fund board reports, or investor due diligence responses
- Stress testing a portfolio against historical or hypothetical redemption scenarios (e.g., 10% weekly outflow, 25% monthly gate breach)
- Assessing market impact of unwinding positions in thin or fragmented markets

## Inputs To Gather

- **Holdings data**: Position-level detail including asset class, notional/market value, currency, exchange/venue, and any lock-up or side-pocket designations
- **Volume & depth metrics**: Average daily trading volume (ADV), bid-ask spreads, order-book depth, and days-to-liquidate estimates per position
- **Fund terms**: Redemption frequency, notice periods, gate provisions, lock-up schedules, and any swing pricing or anti-dilution mechanisms
- **Liability profile**: Investor concentration (top-10 holders as % of AUM), historical redemption patterns, and committed but uncalled capital obligations
- **Stress parameters**: Redemption shock sizes (e.g., 5%/10%/25% of NAV), market stress multipliers for spread widening, and any regulatory-prescribed scenarios [VERIFY — scenario requirements vary by jurisdiction: SEC, FCA, ESMA, MAS]

## Workflow

1. **Classify holdings by liquidity tier**
   - Bucket each position into tiers (e.g., Highly Liquid / Liquid / Less Liquid / Illiquid) using ADV, bid-ask spread, and settlement cycle
   - For fixed income, factor in issue size, credit rating, and dealer inventory availability
   - For alternatives (PE, real assets, private credit), use contractual terms and secondary-market pricing frequency

2. **Calculate time-to-liquidation and cost-to-liquidate**
   - Estimate days to liquidate each position at ≤20% of ADV without material price impact
   - Compute market-impact cost using a participation-rate model (e.g., Almgren-Chriss framework or square-root model)
   - Aggregate at portfolio level to produce a liquidation cost curve (% of portfolio vs. days)

3. **Run redemption stress tests**
   - Model at least three scenarios: normal redemption cadence, moderate stress (historical worst-quarter outflow), severe stress (gate-threshold breach)
   - For each scenario, determine whether liquid-tier assets cover the outflow without forced selling of illiquid positions
   - Calculate the residual portfolio's liquidity profile post-redemption (watch for concentration drift toward illiquid holdings)

4. **Assess liability-side risks**
   - Evaluate investor concentration — flag if any single investor or affiliated group exceeds 10% of AUM
   - Cross-reference redemption notice periods against position liquidation timelines
   - Identify maturity or commitment mismatches (e.g., open-ended fund holding closed-end assets)

5. **Quantify market-impact under stress**
   - Apply spread-widening multipliers (2x–5x normal bid-ask) to reflect crisis conditions
   - Re-run cost-to-liquidate with stressed spreads to determine incremental liquidation cost
   - Compare stressed liquidation cost against the fund's swing pricing threshold or redemption fee trigger [VERIFY — applicable fee/swing mechanisms depend on fund domicile and prospectus terms]

6. **Compile findings and flag breaches**
   - Map results against internal risk limits, regulatory thresholds, and fund prospectus constraints
   - Highlight any positions where days-to-liquidate exceed the fund's redemption frequency
   - Recommend remedial actions: position trimming, liquidity buffer sizing, redemption gate adjustments, or credit facility drawdowns

## Output

Produce a **Liquidity Risk Analysis Report** containing:

- **Executive summary**: Portfolio-level liquidity score, key vulnerabilities, and headline stress-test results
- **Liquidity tiering table**: Each position with tier classification, ADV, bid-ask, days-to-liquidate, and estimated market-impact cost
- **Liquidation cost curve**: Chart showing cumulative portfolio value recoverable over 1/5/10/20/30 trading days under normal and stressed conditions
- **Redemption stress-test results**: For each scenario — outflow amount, liquid coverage ratio, residual illiquid concentration, and any gate/limit breaches
- **Investor concentration analysis**: Top-holder breakdown and single-investor redemption impact
- **Risk limit dashboard**: Current metrics vs. internal limits and regulatory thresholds, with breach/near-breach flags
- **Recommendations**: Prioritized actions ranked by urgency and implementation complexity

## Quality Checks

- Confirm holdings data is as-of a consistent date and reconciles to NAV
- Verify ADV and spread data sources are recent (stale data in illiquid markets can severely understate risk)
- Ensure stress scenarios cover both asset-side (spread widening, volume collapse) and liability-side (concentrated redemptions) shocks simultaneously
- Cross-check liquidity tier assignments against any regulatory tier definitions applicable to the fund [VERIFY — SEC Rule 22e-4 defines specific liquidity classification requirements for US registered funds; non-US funds follow local regulator guidance]
- Validate that market-impact model assumptions (participation rate, decay parameters) are documented and defensible
- Flag any position where estimated liquidation cost exceeds 2% of position value as a material liquidity concern
- Mark all jurisdiction-dependent thresholds and regulatory references with [VERIFY]
