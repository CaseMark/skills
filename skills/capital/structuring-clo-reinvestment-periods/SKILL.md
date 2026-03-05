---
name: structuring-clo-reinvestment-periods
description: Designs CLO reinvestment criteria with portfolio quality tests, trading guidelines, and concentration limits. Use when structuring CLO reinvestment, setting portfolio constraints, or analyzing manager flexibility.
tags:
  - structured-finance
  - investment
  - portfolio
  - trading
metadata:
  author: casemark
  practice_areas:
    - Structured Finance
    - Securitization
    - ABS/MBS/CLO
  document_types:
    - Report
  skill_modes:
    - Analysis
---
# Structuring CLO Reinvestment Periods

Designs CLO reinvestment criteria with portfolio quality tests, trading guidelines, and concentration limits.

## When To Use

- Structuring or amending the reinvestment period for a new or refinanced CLO
- Defining portfolio quality tests (WARF, WAS, WAL, diversity score, minimum recovery rate)
- Drafting or reviewing trading guidelines that govern discretionary and credit-risk/credit-improved sales
- Setting concentration limits by obligor, industry, rating bucket, or asset type
- Evaluating manager flexibility versus investor protection trade-offs during reinvestment
- Comparing reinvestment criteria across a manager's CLO platform or against market benchmarks

## Inputs To Gather

- **Deal term sheet or indenture draft** — reinvestment period length, non-call period, WAL test end date
- **Target portfolio parameters** — par amount, expected WARF, WAS, WAL, diversity score, recovery rate assumptions
- **Rating agency methodology** — Moody's, S&P, or Fitch CLO criteria in effect [VERIFY current version]
- **Concentration limit schedule** — maximum single obligor, industry (Moody's 33-industry or S&P classification), CCC bucket, second-lien/covenant-lite caps
- **Trading flexibility provisions** — discretionary sale baskets (percentage of principal balance), credit-risk and credit-improved definitions, reinvestment overcollateralization conditions
- **Manager track record** — historical turnover rates, default rates, par build/erosion across prior deals
- **Market comparables** — recent BSL CLO indentures from comparable managers for benchmarking

## Workflow

1. **Map the reinvestment timeline** — Confirm reinvestment period start/end, non-call end, and any step-down or amortization trigger dates. Identify whether the deal includes a post-reinvestment trading period and its constraints.

2. **Define portfolio quality tests** — Specify each collateral quality test with its initial target and covenant level:
   - Maximum WARF (e.g., 2850)
   - Minimum WAS (e.g., 3.50%)
   - Maximum WAL (e.g., 7.5 years declining to 4.0 by stated maturity)
   - Minimum diversity score (e.g., 60)
   - Minimum weighted-average recovery rate (e.g., 44.5%)
   - Determine whether tests are measured at time of trade vs. time of settlement [VERIFY indenture convention]

3. **Set concentration limits** — Build the concentration schedule:
   - Single obligor cap (typically 1.5%–2.0% of par)
   - Industry concentration (Moody's 33-industry: max per industry, e.g., 10%–12%; aggregate top-3 cap) [VERIFY applicable industry classification]
   - CCC-rated exposure cap (typically 7.5% par; excess haircut in OC tests)
   - Second-lien, covenant-lite, DIP loan, and non-U.S. obligor sub-limits
   - Fixed-rate asset cap and related hedge requirements

4. **Draft trading guidelines** — Define permissible reinvestment trades:
   - **Credit-risk sales** — obligor downgraded below threshold or placed on watch-negative; no volume cap
   - **Credit-improved sales** — obligor upgraded or spread tightened beyond threshold; often subject to annual basket (e.g., 20% of portfolio)
   - **Discretionary trades** — subject to maintaining or improving all collateral quality tests post-trade
   - Specify reinvestment criteria: acquired asset must satisfy eligibility criteria and not cause any quality test breach

5. **Calibrate OC and IC coverage tests** — Confirm overcollateralization and interest coverage trigger levels for each tranche and how reinvestment is restricted upon a test breach (e.g., diversion of interest proceeds to senior notes).

6. **Benchmark against comparables** — Compare proposed criteria to 3–5 recent deals from the same manager and 3–5 deals from peer managers. Flag any terms meaningfully tighter or looser than market.

7. **Stress-test flexibility** — Model scenarios (spread compression, credit deterioration, high default wave) to assess whether the reinvestment criteria provide sufficient manager flexibility without excessive par erosion risk.

## Output

Produce a **CLO Reinvestment Period Structuring Report** containing:

- **Reinvestment timeline summary** — key dates, non-call/reinvestment/WAL test schedule
- **Collateral quality test matrix** — each test, its target level, covenant level, measurement convention, and cure mechanism
- **Concentration limit schedule** — tabular format with limit type, threshold, and haircut/excess treatment in OC tests
- **Trading guidelines summary** — permitted trade types, volume baskets, post-trade compliance requirements
- **OC/IC test levels** — per-tranche trigger and default levels with reinvestment lockout mechanics
- **Comparable deal benchmarking table** — side-by-side comparison of key reinvestment terms
- **Manager flexibility assessment** — qualitative view of how constraining the proposed terms are relative to market, with specific call-outs for atypical provisions
- **Risk flags** — any terms that may draw rating agency or investor pushback

## Quality Checks

- All collateral quality tests reference the correct rating agency methodology version [VERIFY]
- Concentration limits are internally consistent (sub-limits do not exceed parent limits; aggregate caps are coherent)
- Trading guidelines clearly distinguish credit-risk, credit-improved, and discretionary buckets with no overlap or gap
- OC/IC trigger levels are consistent with the capital structure and rating agency required subordination
- WAL test step-down schedule aligns with expected portfolio amortization profile
- Benchmarking uses deals from the same vintage (within 12 months) and comparable portfolio type (BSL vs. MM)
- No quality test is set at a level that would be immediately breached by the target portfolio
- All dollar and percentage thresholds are expressed on a consistent basis (par amount vs. aggregate principal balance)
