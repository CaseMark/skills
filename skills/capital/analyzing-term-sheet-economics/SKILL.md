---
name: analyzing-term-sheet-economics
language: en
description: Deconstructs VC term sheets with liquidation preference waterfalls, anti-dilution mechanics, and option pool impact analysis. Use when analyzing term sheets, comparing investor terms, or modeling founder dilution.
tags:
  - analysis
  - venture-capital
metadata:
  author: casemark
  practice_areas:
    - Venture Capital
    - Seed/Series Investing
    - Startup Ecosystems
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Term Sheet Economics

Deconstructs VC term sheets to quantify the real economic impact on founders, existing shareholders, and new investors. Covers liquidation preference waterfalls, anti-dilution mechanics, option pool sizing, pay-to-play provisions, and participation rights across single and multi-round scenarios.

## When To Use

- Founder or counsel receives a term sheet and needs to understand true economic impact beyond headline valuation
- Comparing competing term sheets from multiple investors on the same round
- Modeling how current-round terms cascade into future rounds (dilution stacking)
- Evaluating whether a bridge note or SAFE conversion creates unexpected preference overhang
- Reviewing recap or down-round scenarios where anti-dilution triggers materially shift ownership

## Inputs To Gather

- **Term sheet(s):** Full text including economic terms, governance provisions, and any side letters
- **Cap table:** Current fully-diluted cap table with all share classes, option pool grants (vested/unvested), outstanding SAFEs, and convertible notes
- **Prior round terms:** Liquidation preferences, participation caps, and anti-dilution type for each existing preferred series
- **Proposed round parameters:** Pre-money valuation, round size, option pool target (pre- or post-money), and any warrant coverage
- **Exit scenarios to model:** Specify target exit values (e.g., 1x, 3x, 5x, 10x of post-money) or provide a specific range
- **Note/SAFE details (if applicable):** Valuation caps, discount rates, interest rates, maturity dates, and MFN provisions

## Workflow

1. **Parse economic terms** — Extract pre-money valuation, round size, price per share, option pool increase, and any warrants. Identify whether the option pool is created pre-money (founder-dilutive) or post-money. Calculate the effective pre-money valuation after option pool adjustment.

2. **Map the preference stack** — For each preferred series (existing + proposed), document: liquidation preference multiple (1x, 2x, etc.), participation rights (non-participating, full participating, capped participating), and seniority structure (pari passu vs. stacked/senior). Build the waterfall order from most senior to most junior.

3. **Model anti-dilution mechanics** — Identify the anti-dilution protection type for each series: full ratchet, broad-based weighted average, or narrow-based weighted average. For each, calculate the adjusted conversion price under a hypothetical down-round (e.g., 50% of current round price) and quantify the incremental dilution to common holders. [VERIFY] Confirm the exact weighted-average formula in the charter — numerator/denominator definitions vary.

4. **Run the liquidation waterfall** — Model payouts across at least four exit scenarios:
   - **Below preference stack:** Total proceeds < aggregate liquidation preferences (shows who gets wiped out)
   - **At preference stack:** Proceeds = aggregate preferences (shows breakeven for common)
   - **Moderate upside:** 3-5x of post-money valuation (shows where participation caps trigger conversion)
   - **High upside:** 10x+ of post-money valuation (shows as-converted economics)

   For each scenario, calculate per-share proceeds for every class and the effective ownership percentage realized.

5. **Quantify option pool impact** — Calculate the "true" cost of the option pool shuffle: how much of the pre-money valuation is allocated to the new pool vs. existing shareholders. Show the effective price per share for founders before and after pool creation. If the pool is oversized relative to a hiring plan, flag the excess as hidden valuation reduction.

6. **Analyze protective provisions and pay-to-play** — Identify provisions that have economic consequences: pay-to-play (conversion to common on failure to participate), dividend rights (cumulative vs. non-cumulative), and redemption rights. Note any drag-along thresholds that could force a sale at preference-favorable valuations.

7. **Compare competing offers (if multiple term sheets)** — Build a side-by-side matrix on: effective valuation (post option pool adjustment), total preference overhang, founder ownership post-close (fully diluted), breakeven exit value for common, and governance control points. Rank on economic impact, not headline valuation.

## Output

Produce an **economics analysis report** containing:

- **Summary table:** Pre-money (headline vs. effective), post-money, price per share, round size, option pool %, founder ownership post-close
- **Preference waterfall chart:** Table showing payout by share class across 4+ exit scenarios
- **Anti-dilution sensitivity:** Dilution impact under 25%, 50%, and 75% down-round scenarios
- **Option pool analysis:** Cost allocation breakdown showing who bears the dilution
- **Key findings:** 3-5 bullet points highlighting the most material economic terms (e.g., "2x participating preferred adds $X preference overhang, pushing common breakeven to $Y exit")
- **Red flags:** Any terms that are significantly off-market or create outsized downside risk for founders (e.g., full ratchet anti-dilution, cumulative dividends, uncapped participation)
- **Comparison matrix** (if multiple term sheets): Side-by-side ranking with recommendation rationale

## Quality Checks

- Verify all share counts reconcile to the cap table — fully-diluted totals must match before and after the round
- Confirm the option pool treatment (pre-money vs. post-money) matches term sheet language exactly
- Cross-check that the waterfall produces correct results at boundary cases: proceeds = 0, proceeds = total preferences, and very large exits (should converge to as-converted percentages)
- Ensure anti-dilution calculations use the correct formula variant from the actual charter or term sheet, not a textbook default [VERIFY]
- Flag any terms where market norms differ by stage (seed vs. Series A vs. growth) — e.g., participation rights are common in growth rounds but a red flag in seed deals [VERIFY]
- Confirm that all SAFE/note conversion mechanics are modeled with the correct trigger events (qualified financing threshold, valuation cap vs. discount interactions)
