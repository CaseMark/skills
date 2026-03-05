---
name: analyzing-alternative-investments
description: Evaluates alternative investment strategies (hedge funds, real assets, private markets) with risk-return and liquidity analysis. Use when analyzing alternatives, evaluating fund strategies, or assessing illiquidity premiums.
tags:
  - analysis
  - asset-management
  - risk
  - investment
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
# Analyzing Alternative Investments

Evaluates alternative investment strategies across hedge funds, private equity, private credit, real assets, and other non-traditional allocations. Produces structured risk-return and liquidity analysis to support allocation decisions.

## When To Use

- Evaluating a specific fund or strategy for inclusion in a portfolio
- Comparing alternative strategies against each other or against public-market benchmarks
- Assessing the illiquidity premium and lock-up trade-offs of a proposed allocation
- Reviewing existing alternative allocations for rebalancing or redemption decisions
- Conducting due diligence on a fund's reported performance and risk characteristics

## Inputs To Gather

- **Fund documents**: PPM, offering memorandum, fact sheets, investor letters, audited financials
- **Performance data**: Monthly/quarterly net returns, benchmark returns, vintage year (for PE/VC)
- **Fee structure**: Management fee, carried interest/incentive fee, hurdle rate, clawback provisions
- **Liquidity terms**: Lock-up period, redemption frequency, notice period, gate provisions, side-pocket usage
- **Portfolio context**: Current asset allocation, total portfolio size, target alternatives weighting, investor liquidity needs and time horizon
- **Strategy specifics**: Investment mandate, leverage policy, concentration limits, use of derivatives

## Workflow

1. **Classify the strategy**
   - Category: hedge fund (L/S equity, global macro, event-driven, relative value, multi-strategy, CTA/managed futures), private equity (buyout, growth, venture), private credit (direct lending, mezzanine, distressed), real assets (real estate, infrastructure, natural resources, commodities), or hybrid/fund-of-funds
   - Identify primary return drivers and the economic exposure being harvested

2. **Analyze risk-return profile**
   - Compute annualized return, annualized volatility, Sharpe ratio, and Sortino ratio
   - For PE/VC: calculate IRR, TVPI (total value to paid-in), DPI (distributions to paid-in), and RVPI; note J-curve implications
   - For hedge funds: assess maximum drawdown, drawdown duration, skewness, and kurtosis of return distribution
   - Compare against relevant benchmarks (e.g., HFRI sub-index, Cambridge Associates PE benchmark, NCREIF for real estate) [VERIFY benchmark availability and vintage alignment]
   - Evaluate alpha generation: regression against common factor exposures (equity beta, credit spread, interest rate, momentum) to separate beta replication from genuine alpha

3. **Assess fees and net-of-fee impact**
   - Model total fee drag under base-case and upside return scenarios
   - Calculate break-even gross return needed to match a passive alternative after fees
   - Flag high-water mark resets, fee crystallization frequency, and any non-standard fee layers (admin, servicing, fund-of-funds overlay)

4. **Evaluate liquidity and structural terms**
   - Map lock-up, redemption windows, and notice periods against the investor's liquidity needs
   - Identify gate provisions, suspension clauses, and side-pocket mechanisms that could delay capital return
   - For closed-end structures: model capital call pacing and distribution timing against commitment size
   - Estimate illiquidity premium: is the excess return over liquid alternatives sufficient compensation? [VERIFY current market estimates for relevant illiquidity premia]

5. **Conduct operational and structural due diligence**
   - Confirm fund administrator, auditor, and prime broker/custodian independence
   - Review valuation policy: frequency, use of third-party pricing, percentage of Level 3 assets
   - Check for key-person risk, succession planning, and alignment of interest (GP commitment)
   - Flag regulatory registration status and any disclosed regulatory actions [VERIFY jurisdiction-specific registration requirements]

6. **Contextualize within the portfolio**
   - Model the marginal impact on total portfolio return, volatility, and Sharpe ratio
   - Assess correlation to existing holdings — determine whether the allocation genuinely diversifies or duplicates existing exposures
   - Stress-test under adverse scenarios (2008 GFC, 2020 COVID drawdown, rising-rate environment)
   - Check that the combined alternatives allocation stays within policy limits and total illiquid exposure thresholds

## Output

Structure the analysis report with these sections:

- **Executive Summary**: Strategy type, recommendation (allocate / pass / watchlist), and one-paragraph rationale
- **Strategy Overview**: Description, AUM, vintage/inception, investment team summary
- **Performance Analysis**: Return and risk metrics table with benchmark comparison; factor attribution summary
- **Fee Analysis**: Fee structure summary and net-of-fee impact under modeled scenarios
- **Liquidity Profile**: Lock-up/redemption terms, capital call pacing (if applicable), liquidity score relative to investor needs
- **Operational Review**: Administrator, auditor, valuation policy, key-person and regulatory flags
- **Portfolio Fit**: Marginal impact on portfolio metrics, correlation analysis, stress-test results
- **Key Risks and Mitigants**: Top 3-5 risks with corresponding mitigants or monitoring triggers
- **Conclusion and Conditions**: Final recommendation with any conditions (e.g., co-investment rights, fee negotiation, reporting requirements)

## Quality Checks

- All return figures are net-of-fees unless explicitly labeled otherwise
- IRR and multiple calculations use actual cash flow dates, not simplifying assumptions
- Benchmark comparisons use strategy-appropriate indices with matching time periods and vintage years
- Illiquidity and structural risks are explicitly quantified, not just mentioned qualitatively
- Factor regression uses an appropriate model for the strategy type (not a single-factor equity beta for a credit fund)
- Any data gaps, stale valuations, or self-reported figures are flagged with [VERIFY]
- Fee drag analysis includes realistic scenarios, not just the fund's own marketing projections
- Portfolio-level analysis reflects actual current holdings, not a generic model allocation
