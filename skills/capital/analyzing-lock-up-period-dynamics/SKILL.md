---
name: analyzing-lock-up-period-dynamics
description: Evaluates lock-up expiration impact with float analysis, insider selling patterns, and supply overhang assessment. Use when analyzing lock-up expirations, modeling supply dynamics, or assessing post-IPO trading patterns.
tags:
  - analysis
  - equity-capital-markets
  - trading
metadata:
  author: casemark
  practice_areas:
    - ECM
    - IPO Advisory
    - Equity Origination
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Lock Up Period Dynamics

Evaluates lock-up expiration impact with float analysis, insider selling patterns, and supply overhang assessment.

## When To Use

- Approaching lock-up expiration on a recently completed IPO (typically 90–180 days post-pricing)
- Evaluating whether to pursue an early lock-up release for a secondary offering
- Advising issuer management or board on insider selling strategy around expiration
- Modeling supply overhang for institutional investors sizing post-lock-up positions
- Assessing staggered or partial lock-up structures with multiple expiration tranches

## Inputs To Gather

- **Share structure**: Total shares outstanding, IPO shares sold (primary + secondary), greenshoe allocation and exercise status
- **Lock-up schedule**: Expiration date(s), any staggered tranches, early release provisions, waiver history by the lead underwriter
- **Locked share breakdown by holder type**: Founder/management shares, pre-IPO investor shares (by fund vintage and hold period), employee/option shares (vested vs. unvested at expiration), directed share program (DSP) allocations
- **Current float data**: Public float shares, average daily trading volume (ADTV) over 30/60/90 days, short interest and days-to-cover
- **Price and performance context**: Current price vs. IPO price, 52-week range, sector index performance since IPO
- **Comparable precedents**: Lock-up expiration trading patterns for sector peers and same-vintage IPOs
- **Known disposition signals**: 10b5-1 plan filings, Form 144 filings, any Rule 701 or Reg S considerations [VERIFY jurisdiction-specific registration exemptions]

## Workflow

1. **Map the lock-up structure**
   - Identify all expiration dates and the share count unlocking at each tranche
   - Classify locked shares by holder type (founders, VCs/PEs, employees, other insiders)
   - Flag any early-release triggers (e.g., price-based thresholds, underwriter discretion windows)
   - Note any contractual selling restrictions that survive lock-up expiration (e.g., volume limitations, blackout windows)

2. **Calculate supply overhang ratios**
   - Unlocking shares as a multiple of current public float (overhang ratio)
   - Unlocking shares as a multiple of trailing 30-day ADTV (days-to-clear ratio)
   - Segment overhang by holder type — VC/PE funds near end-of-life or past target hold periods have higher selling probability than founders

3. **Assess selling probability by holder cohort**
   - **Pre-IPO investors**: Check fund vintage, fund life remaining, DPI (distributions to paid-in) pressure, prior portfolio company selling patterns
   - **Founders/management**: Evaluate diversification needs, pledged-share exposure, any 10b5-1 plans already filed, compensation structure dependency on equity
   - **Employees**: Estimate option exercise economics (strike price vs. current price), tax-lot timing for long-term capital gains eligibility, prior employee selling in comparable IPOs
   - Assign qualitative selling probability (high / moderate / low) to each cohort

4. **Model potential selling volume scenarios**
   - **Base case**: Historical average insider sell-through rate for sector (typically 10–20% of unlocked shares in first 30 days) [VERIFY against current market conditions]
   - **Bear case**: Elevated selling — apply higher sell-through rate reflecting fund liquidation pressure or price decline below IPO
   - **Bull case**: Minimal selling — strong price performance discourages near-term disposition
   - Express each scenario as daily selling volume relative to ADTV

5. **Analyze historical precedents**
   - Pull trading data for 5–10 comparable lock-up expirations (same sector, similar float/overhang profile)
   - Measure price action windows: T-10 to T+30 relative to expiration date
   - Identify average drawdown at expiration, recovery period, and volume spike patterns
   - Note outliers and the drivers behind them (e.g., concurrent earnings, analyst initiation, secondary offering announced pre-expiration)

6. **Evaluate structural mitigants**
   - Is the underwriter likely to offer an organized secondary or block trade to manage supply?
   - Has the company signaled a buyback authorization?
   - Are there any contractual orderly-marketing arrangements?
   - Is short interest elevated enough that covering could absorb incremental supply?

7. **Synthesize findings and frame recommendations**
   - Summarize net supply impact with scenario-weighted expected selling volume
   - Identify the highest-risk expiration tranche and most likely large sellers
   - For issuer-side advisory: recommend communication strategy, potential early-release secondary, or blackout period guidance
   - For buy-side analysis: frame entry-point thesis around expected post-expiration price recovery

## Output

Deliver a structured Lock-Up Expiration Analysis Report containing:

- **Executive summary**: Key expiration date(s), total shares unlocking, overhang ratio, and headline selling probability assessment
- **Share structure table**: Breakdown of locked shares by holder type, tranche, and expiration date
- **Supply overhang metrics**: Overhang ratio, days-to-clear, and selling probability by cohort
- **Scenario analysis table**: Base / bear / bull selling volumes with price impact estimates
- **Precedent comparison**: Summary table of comparable lock-up expirations with price/volume outcomes
- **Risk factors and mitigants**: Structural features that amplify or dampen expiration impact
- **Recommendations**: Actionable next steps tailored to the client's position (issuer, underwriter, or investor)

## Quality Checks

- Confirm total locked shares reconcile to prospectus/S-1 share tables and any subsequent Form 3/4 filings
- Verify expiration date calculation accounts for weekends, holidays, and any contractual "next business day" language
- Cross-check ADTV figures against multiple data sources (Bloomberg, exchange data) to avoid stale or adjusted numbers
- Ensure selling probability assumptions are supported by observable data (fund filings, 13F changes, Form 144s) — not speculation
- Validate precedent comparables are genuinely comparable (similar sector, float size, market regime) rather than cherry-picked
- Confirm all per-share and percentage calculations use the correct denominator (shares outstanding vs. float vs. locked shares)
- Mark any jurisdiction-specific regulatory constraints with [VERIFY] (e.g., Rule 144 volume limits, non-US lock-up regimes)
