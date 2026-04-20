---
name: modeling-growth-equity-returns
language: en
description: Builds growth equity return models with minority/majority economics, participation rights, and preference stack analysis. Use when modeling growth equity returns, projecting minority investment outcomes, or analyzing preference structures.
tags:
  - modeling
  - growth-equity
  - investment
metadata:
  author: casemark
  practice_areas:
    - Growth Equity
    - Expansion Capital
    - Late-Stage Investing
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Growth Equity Returns

## When To Use

- Projecting gross and net returns for a minority or majority growth equity investment
- Analyzing how liquidation preference stacks, participation rights, and anti-dilution provisions affect investor economics across exit scenarios
- Comparing return profiles between participating preferred, non-participating preferred, and common equity structures
- Stress-testing entry valuation, hold period, and exit multiple assumptions for an expansion-stage deal
- Evaluating co-invest or follow-on allocation decisions within a growth equity portfolio

## Inputs To Gather

- **Deal terms**: Investment amount, pre-money valuation, ownership percentage, share class, liquidation preference multiple (1x, 1.5x, etc.), participation cap (if any), anti-dilution mechanism (broad-based weighted average vs. full ratchet)
- **Capital structure**: Existing cap table with all prior preferred rounds, option pool size, outstanding convertible instruments (SAFEs, notes), any pay-to-play provisions
- **Operating forecasts**: Revenue, EBITDA/EBIT, or net income projections for each year of hold period; gross margin trajectory; expected cash burn or free cash flow profile
- **Exit assumptions**: Target hold period (typically 3–7 years), exit revenue/EBITDA multiples, probability-weighted exit scenarios (IPO, strategic sale, secondary, recap)
- **Follow-on / dilution**: Expected future funding rounds, anticipated dilution per round, pro-rata rights and whether the fund intends to exercise them
- **Fee and carry structure** (for fund-level returns): Management fee rate, carry percentage, preferred return/hurdle rate, GP catch-up, fund-level recycling assumptions

## Workflow

1. **Map the cap table** — Build the current ownership waterfall including all preferred layers, common, and option pool. Confirm conversion ratios and any ratchet triggers. [VERIFY] anti-dilution provision language from the term sheet or charter.

2. **Construct the preference stack** — Order liquidation preferences by seniority (pari passu vs. stacked). Model each layer's claim: preference amount, accrued dividends (if cumulative), and participation rights. Calculate the "as-converted" breakpoint where preferred holders would elect to convert to common.

3. **Build exit waterfall scenarios** — For each exit value (e.g., 0.5×–5× of post-money):
   - Pay senior preferences first, then junior preferences
   - Distribute remaining proceeds per participation rights (uncapped, capped, or non-participating)
   - Compare participating vs. as-converted payout at each exit value to determine optimal election
   - Output investor cash-on-cash and IRR at each scenario point

4. **Model the operating case** — Project revenue and margin over the hold period using management forecasts and comparable company benchmarks. Apply a base, upside, and downside case. Tie exit enterprise value to exit-year revenue or EBITDA × selected multiple.

5. **Layer in dilution and follow-on** — Simulate future rounds with estimated pre-money valuations. Reduce ownership proportionally unless pro-rata is exercised. Recalculate waterfall economics post-dilution.

6. **Calculate return metrics** — For each scenario compute:
   - Gross MOIC (multiple on invested capital)
   - Gross IRR
   - Net MOIC and net IRR (after management fees and carried interest)
   - DPI (distributions to paid-in) if modeling interim liquidity events

7. **Run sensitivity analysis** — Build two-way data tables varying entry multiple vs. exit multiple, and hold period vs. revenue growth rate. Highlight breakeven and target-return thresholds (e.g., 3× MOIC, 25% IRR).

## Output

- **Waterfall summary table**: For each exit scenario, show total proceeds, preference payouts by layer, common distribution, and investor share
- **Return matrix**: Gross and net MOIC/IRR across base, upside, and downside cases
- **Sensitivity tables**: Two-way tables on key variable pairs (entry valuation vs. exit multiple; growth rate vs. hold period)
- **Breakeven analysis**: Minimum exit value required to achieve 1× return, target MOIC, and target IRR
- **Key assumptions register**: Itemized list of every assumption with source or [VERIFY] flag

## Quality Checks

- Waterfall total distributions equal total exit proceeds in every scenario (zero residual)
- As-converted breakpoint is correctly identified — preferred holders convert only when common payout exceeds preference + participation
- IRR and MOIC are internally consistent (IRR derived from actual cash flow timing, not approximated)
- Dilution math is additive across rounds — total ownership percentages sum to 100% after each modeled round
- Participation cap, if present, is correctly applied so that capped holders stop receiving pro-rata above the cap threshold
- Sensitivity ranges bracket realistic outcomes — entry and exit multiples aligned to comparable transaction data [VERIFY]
- Net return calculations correctly sequence management fees (on committed vs. invested capital) and carry (American vs. European waterfall) per fund terms [VERIFY]
