---
name: tracking-consensus-estimates
description: Monitors sell-side consensus estimates with revision tracking and surprise analysis. Use when tracking estimate revisions, analyzing consensus changes, or monitoring analyst expectations.
tags:
  - monitoring
  - equity-research
metadata:
  author: casemark
  practice_areas:
    - Equity Research
    - Investment Management
  document_types:
    - Tracking Report
  skill_modes:
    - Monitoring
---
# Tracking Consensus Estimates

Monitors sell-side consensus estimates with revision tracking and surprise analysis for equities, enabling portfolio managers and analysts to identify inflection points in analyst sentiment before they are fully priced in.

## When To Use

- Ahead of earnings season to establish baseline consensus expectations and flag names with divergent or tightly clustered estimates
- After an earnings print to quantify the surprise (beat/miss) and capture the initial revision wave
- When a material event (guidance change, management turnover, sector shock) triggers mid-quarter estimate revisions
- During periodic portfolio reviews to assess whether consensus trajectory supports or undermines the investment thesis
- When building or updating a stock pitch that relies on earnings momentum or mean-reversion arguments

## Inputs To Gather

- **Ticker(s) and reporting period(s)** — specify fiscal quarter/year and whether tracking GAAP vs. adjusted figures
- **Metric set** — at minimum: Revenue, EPS; optionally EBITDA, FCF, gross margin, segment-level KPIs
- **Analyst coverage list** — broker names, analyst names, latest estimate dates; note any recent initiations or dropped coverage
- **Historical consensus snapshots** — estimates at 90-day, 60-day, 30-day, and 7-day marks prior to reporting date [VERIFY data source and snapshot availability]
- **Actual reported figures** — for completed periods, the as-reported numbers and any company-defined adjusted metrics
- **Guidance** — management's explicit guidance range (if provided) and any qualitative commentary on outlook
- **Comparable context** — peer consensus trends and sector-level estimate revision ratios for relative positioning

## Workflow

1. **Build the estimate matrix** — Organize each analyst's estimates by metric and period. Record estimate date, prior estimate, and current estimate. Flag stale estimates (>60 days without update) as potentially unreliable.

2. **Calculate consensus statistics** — For each metric/period: compute mean, median, high, low, standard deviation, and number of contributing analysts. Use median as the primary consensus figure when the distribution is skewed or the sample is small (<6 analysts).

3. **Track revision momentum** — Compare current consensus to prior snapshots (90d/60d/30d/7d). Calculate:
   - Net revision ratio: (upgrades − downgrades) / total revisions
   - Magnitude-weighted revision: average percentage change in estimates over the window
   - Identify analysts who revised against the trend (potential contrarian signals)

4. **Analyze earnings surprise (post-report)** — Compute surprise as: (Actual − Consensus) / |Consensus|. Categorize: beat >2%, inline ±2%, miss <−2% [VERIFY threshold conventions used by the firm]. Cross-reference surprise magnitude against historical surprise distribution for the name.

5. **Assess post-surprise revision response** — Within 1–5 days after the print, track how many analysts have revised forward estimates. Gauge whether the surprise is being extrapolated (revisions in the same direction) or faded (revisions revert). Compare forward-quarter revision velocity to the trailing-quarter surprise.

6. **Contextualize against guidance and peers** — Map the consensus trajectory against any management guidance range. Flag if consensus sits above the high end or below the low end of guidance. Compare revision trends to sector peers to separate company-specific signals from macro/sector rotation.

7. **Summarize and flag actionable signals** — Produce a concise tracking report highlighting: current consensus vs. prior snapshots, revision breadth and direction, notable outlier analysts, surprise history, and any divergence from guidance or peer trends.

## Output

The tracking report should include:

- **Header**: Ticker, company name, reporting period, report date, number of covering analysts
- **Consensus snapshot table**: Metric | Current Consensus (Mean/Median) | 30d Prior | 60d Prior | 90d Prior | High | Low | Std Dev
- **Revision summary**: Net revision ratio, magnitude-weighted revision, count of upgrades/downgrades/reiterations per window
- **Surprise analysis** (if actuals available): Actual vs. consensus, surprise %, historical surprise percentile, whisper number delta if available
- **Post-surprise revision tracker**: Analysts revised within 1/3/5 days, direction and magnitude of forward estimate changes
- **Guidance alignment**: Consensus positioning relative to management guidance range
- **Peer comparison**: Relative revision momentum vs. 3–5 closest comps
- **Signal flags**: Bullet list of actionable observations (e.g., "FY2 EPS consensus up 8% in 30 days on 5 of 7 analysts revising higher — strongest upward momentum in 4 quarters")

## Quality Checks

- Verify analyst count matches known coverage universe; investigate any discrepancy (dropped coverage, new initiation) [VERIFY against broker research portal]
- Confirm estimate dates are current — consensus built on stale estimates produces misleading revision signals
- Cross-check actuals against both the company's earnings release and a second data source to avoid transcription errors
- Ensure GAAP vs. adjusted alignment is consistent across all analysts; note any known definitional differences (e.g., stock-based comp treatment)
- Validate surprise calculations use the same consensus vintage (typically the final pre-report snapshot, not an intra-day moving target)
- Flag any metric where standard deviation exceeds 15% of the mean — wide dispersion reduces consensus reliability and warrants a range-based presentation rather than a point estimate
- Note data-provider-specific conventions that may affect comparability [VERIFY whether estimates are calendarized or fiscal-aligned]
