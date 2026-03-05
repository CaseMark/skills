---
name: analyzing-venture-deal-terms
description: Evaluates VC term sheet provisions with economic and control analysis and cap table impact. Use when analyzing term sheets, negotiating deal terms, or modeling cap table outcomes.
tags:
  - analysis
  - private-equity
metadata:
  author: casemark
  practice_areas:
    - Private Equity
    - Venture Capital
    - Growth Equity
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Venture Deal Terms

Evaluates VC term sheet provisions across economic terms, control provisions, and cap table impact to support founders, investors, or counsel in deal negotiation and structuring.

## When To Use

- Reviewing a new term sheet before signing or counter-proposing
- Comparing multiple term sheets from competing investors
- Modeling dilution and payout scenarios across financing rounds
- Advising founders or boards on protective provisions, liquidation preferences, or anti-dilution mechanics
- Preparing for Series A through growth-stage financings, bridge notes, or SAFE conversions

## Inputs To Gather

- **Term sheet or LOI** — full text including all exhibits and side letters
- **Current cap table** — shares outstanding by class, option pool size, convertible instruments (SAFEs, notes) with caps/discounts
- **Prior round documents** — previous preferred stock terms, existing protective provisions, prior liquidation preferences
- **Company financials** — latest valuation, revenue run-rate, and burn rate (for context on pricing reasonableness)
- **Investor identity** — lead investor, co-investors, and any strategic investors (affects governance analysis)
- **Founder/management goals** — control retention priorities, exit timeline expectations, follow-on funding plans

## Workflow

1. **Parse economic terms**
   - Extract pre-money valuation, round size, price per share, and implied post-money valuation
   - Identify liquidation preference structure: 1x non-participating vs. participating (capped or uncapped)
   - Note anti-dilution provision type: broad-based weighted average, narrow-based, or full ratchet
   - Flag pay-to-play provisions and their trigger conditions
   - Identify any dividends (cumulative vs. non-cumulative, rate, and accrual terms)

2. **Analyze control and governance provisions**
   - Map board composition: investor seats, founder seats, independent seats, and observer rights
   - List protective provisions (veto rights) — categorize as standard vs. aggressive
   - Standard: amendments to charter affecting preferred, new senior/pari passu equity, change of control, dissolution
   - Aggressive: annual budget approval, executive hiring/firing, debt above low thresholds, any related-party transaction
   - Review drag-along and tag-along rights, triggers, and thresholds
   - Assess voting agreement terms and any investor consent requirements for future rounds

3. **Model cap table impact**
   - Build pre-money and post-money cap tables showing ownership percentages by stakeholder
   - Calculate option pool expansion (pre-money shuffle) and its dilutive effect on founders
   - Model SAFE/note conversion mechanics: identify conversion price, discount application, and cap interaction
   - Run waterfall analysis for at least three exit scenarios:
     - Downside (1x–2x invested capital)
     - Base case (3x–5x invested capital)
     - Upside (10x+ invested capital)
   - Show per-share proceeds and total payout by class at each scenario, highlighting participation cap breakpoints

4. **Benchmark against market norms**
   - Compare valuation multiples to sector/stage comparables [VERIFY: current market data source]
   - Flag terms that deviate from NVCA model documents or prevailing market standards
   - Note any unusual provisions: redemption rights, IPO ratchets, milestone-based tranches, full-ratchet anti-dilution

5. **Identify negotiation priorities**
   - Rank terms by economic impact (quantified where possible) and control significance
   - Distinguish must-fix terms from nice-to-have improvements
   - Suggest specific counter-proposal language for high-priority items

## Output

Structure the analysis report with these sections:

- **Deal Summary** — one-paragraph overview: round size, valuation, lead investor, key headline terms
- **Economic Terms Analysis** — table of economic provisions with market benchmark comparison (standard / favorable / aggressive)
- **Control & Governance Analysis** — board composition diagram, protective provision matrix, and risk flags
- **Cap Table Model** — pre/post cap tables, option pool impact, and waterfall payout tables at three exit scenarios
- **Key Findings** — numbered list of the 5–10 most significant terms with plain-language explanation of impact
- **Negotiation Recommendations** — prioritized list of proposed changes with rationale and suggested language
- **Open Items** — any missing information, ambiguous terms, or items requiring [VERIFY] confirmation

## Quality Checks

- Verify that all share counts and percentages reconcile across cap table calculations
- Confirm liquidation preference stacking order matches the actual seniority of each preferred series
- Ensure anti-dilution modeling uses the correct formula (broad-based weighted average denominators include all common equivalents) [VERIFY: confirm instrument-specific conversion terms]
- Cross-check that protective provision analysis accounts for existing preferred series rights, not just the new round
- Validate that option pool percentage is calculated on a post-money basis (standard) vs. pre-money — flag if term sheet is ambiguous
- Confirm SAFE/note conversion scenarios account for both cap-based and discount-based pricing, using the more favorable to the holder
- Flag any term where jurisdiction-specific securities law may affect enforceability [VERIFY: state of incorporation, blue sky requirements]
