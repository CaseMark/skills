---
name: evaluating-litigation-driven-catalysts
description: Assesses litigation outcome impact with settlement probability, damage range estimation, and stock price sensitivity analysis. Use when evaluating litigation catalysts, modeling legal outcomes, or analyzing litigation-driven opportunities.
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
    - Evaluation Report
  skill_modes:
    - Analysis
    - Assessment
---
# Evaluating Litigation Driven Catalysts

Assesses litigation outcome impact with settlement probability, damage range estimation, and stock price sensitivity analysis.

## When To Use

- A public company faces material pending litigation (securities fraud, patent infringement, antitrust, product liability, government enforcement) and you need to model the investment implications
- Evaluating an event-driven or special situations position where a legal outcome is the primary catalyst for price movement
- Sizing the asymmetry between market-implied litigation discount and your independent estimate of probable outcomes
- Screening activist targets where litigation resolution could unlock value (e.g., settlement removes overhang, judgment triggers buyback capacity)

## Inputs To Gather

- **Case filings and docket**: complaint, key motions, court rulings, scheduling orders, and trial date [VERIFY jurisdiction and current procedural posture]
- **Company financials**: market cap, enterprise value, cash position, insurance coverage, and balance sheet capacity to absorb adverse judgment
- **Comparable settlements/verdicts**: prior outcomes in the same area of law, same jurisdiction, or involving the same plaintiff's counsel
- **Analyst and market data**: current stock price, implied volatility, options skew, and any sell-side litigation-adjusted price targets
- **Expert or counsel commentary**: law firm memos, litigation analytics platforms (Lex Machina, Docket Alarm), or expert depositions indicating likely outcome range
- **Timeline markers**: discovery cutoff, summary judgment deadline, trial date, appeal windows

## Workflow

1. **Classify the litigation type and stage** — Determine whether the case is securities class action, patent, antitrust, regulatory enforcement, mass tort, or other. Identify current procedural phase (pre-discovery, post-class-certification, summary judgment briefing, trial, appeal). Stage drives both probability calibration and time-to-resolution.

2. **Estimate outcome probabilities** — Build a discrete probability tree with at least three branches:
   - Dismissal / defendant win (assign probability based on motion-to-dismiss success rates for this case type [VERIFY against jurisdiction-specific data])
   - Settlement (most frequent resolution — calibrate using comparable case data, median settlement-to-damages ratios)
   - Plaintiff verdict at trial (use base rates; e.g., securities class actions reach trial <5% of the time)
   - Assign sub-branches if partial outcomes are plausible (e.g., some claims survive, others dismissed)

3. **Estimate damage ranges per branch** — For each non-dismissal outcome:
   - Low / base / high damage estimate anchored to statutory frameworks, expert reports, and comparable awards
   - Net-of-insurance recovery (confirm D&O or other policy limits and retention layers [VERIFY policy terms if available])
   - Tax treatment of settlement payments (deductible vs. non-deductible penalties) [VERIFY under IRC and relevant state law]

4. **Calculate expected litigation cost** — Probability-weighted expected value across all branches. Express as total dollar cost, per-share cost, and percentage of current market cap.

5. **Run stock price sensitivity analysis** — Model share price impact under each branch:
   - Overhang removal premium: estimate the re-rating if litigation resolves favorably (compare multiples to peers without litigation drag)
   - Adverse scenario: model dilution if company raises capital, or credit impact if judgment impairs balance sheet
   - Time-value adjustment: discount delayed outcomes to present value using appropriate rate

6. **Assess market pricing vs. your estimate** — Compare your expected litigation cost to the implied discount in the current stock price. Derive the "litigation mispricing" — the gap between your probability-weighted outcome and what the market appears to price. Confirm with options market signals (put skew, event vol).

7. **Identify key catalysts and decision points** — Map upcoming dates that will update probabilities: class certification ruling, Markman hearing, summary judgment order, mediation sessions, trial commencement. Flag which events have binary risk and which are incremental.

## Output

Produce a **Litigation Catalyst Evaluation Report** containing:

- **Executive summary**: one-paragraph thesis on whether the litigation creates an investable asymmetry
- **Case overview table**: parties, claims, jurisdiction, judge, procedural posture, next key date
- **Probability tree**: visual or tabular display of outcome branches with assigned probabilities and rationale
- **Damage range matrix**: low / base / high estimates per outcome branch, net of insurance, with per-share translation
- **Expected value calculation**: probability-weighted cost and per-share impact
- **Sensitivity table**: stock price under each scenario (dismissal, settlement at various multiples, adverse verdict)
- **Market-implied vs. estimated discount**: quantified mispricing with supporting data
- **Catalyst calendar**: timeline of upcoming inflection points with expected probability updates
- **Risk factors**: key assumptions that, if wrong, most change the conclusion (e.g., insurance coverage dispute, judge reassignment, legislative change)

## Quality Checks

- Probabilities across all branches sum to 100%
- Damage estimates are anchored to at least two comparable cases or statutory frameworks, not invented
- Per-share math reconciles with share count (diluted) and market cap used
- Insurance offset is explicitly stated and sourced, not assumed
- All jurisdiction-dependent assumptions (statute of limitations, damages caps, fee-shifting rules) are marked [VERIFY]
- Time-to-resolution estimate is consistent with the court's historical docket pace
- Report distinguishes between litigation risk (probability of loss) and litigation exposure (magnitude of loss) — both are quantified separately
- Sensitivity analysis includes at least one scenario where the position thesis is wrong
