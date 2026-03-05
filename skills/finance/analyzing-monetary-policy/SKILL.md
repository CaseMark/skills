---
name: analyzing-monetary-policy
description: Structures central bank policy analysis with rate decision assessment, forward guidance interpretation, and market impact. Use when analyzing Fed policy, interpreting FOMC statements, or assessing monetary policy impact.
tags:
  - analysis
  - economic-analysis
metadata:
  author: casemark
  practice_areas:
    - Economic Research
    - Macroeconomics
    - Policy Analysis
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Monetary Policy

Structures central bank policy analysis with rate decision assessment, forward guidance interpretation, and market impact.

## When To Use

- Analyzing an FOMC statement, minutes, or press conference for policy signals
- Assessing a rate decision (hold, hike, or cut) against market expectations
- Interpreting forward guidance language changes between consecutive meetings
- Evaluating monetary policy impact on yield curves, credit spreads, or equity risk premiums
- Comparing policy stances across central banks (Fed, ECB, BOJ, BOE) for relative-value or macro positioning
- Preparing pre-meeting or post-meeting research notes for portfolio managers or clients

## Inputs To Gather

- **Statement text**: Current and prior FOMC statement (or equivalent central bank communiqué) for diff analysis
- **Rate decision**: Announced target rate, vote split (dissents and their direction), and any changes to administered rates (IOER/ON RRP) [VERIFY current facility names]
- **Economic projections**: Summary of Economic Projections (SEP) including dot plot, GDP, unemployment, PCE inflation, and core PCE forecasts
- **Press conference transcript or key quotes**: Chair's remarks on risks, data dependency, and balance sheet policy
- **Market data at decision time**: Fed funds futures strip, 2y/10y Treasury yields, USD index (DXY), S&P 500 level, and credit spreads (IG/HY OAS)
- **Consensus expectations**: Pre-meeting survey medians (Bloomberg, Reuters) for rate decision and dot plot shifts
- **Prior meeting context**: Previous statement language, minutes highlights, and any inter-meeting communications (speeches, testimony)

## Workflow

1. **Diff the statement** — Compare current vs. prior statement line by line. Flag every language addition, deletion, or substitution. Categorize changes as relating to: economic activity, labor market, inflation, risks, or forward guidance.

2. **Assess the rate decision relative to expectations** — Classify the outcome as hawkish surprise, dovish surprise, or in-line. Note the vote count and characterize any dissents (hawkish dissent = member preferred tighter policy; dovish dissent = preferred looser).

3. **Decode forward guidance** — Identify the operative guidance phrase (e.g., "further increases," "maintain the target range," "prepared to adjust"). Map it on a spectrum: explicit tightening bias → neutral/data-dependent → explicit easing bias. Note any conditionality tied to specific data thresholds (e.g., "sustained progress toward 2 percent").

4. **Analyze the dot plot and projections (if SEP meeting)** — Calculate median and modal dot shifts vs. prior SEP. Identify the number of dots pricing cuts vs. hikes over the next four quarters. Flag any meaningful revision to the longer-run neutral rate estimate (r*). Compare GDP and inflation forecast revisions to assess the Committee's growth-inflation trade-off assessment.

5. **Evaluate balance sheet policy** — Note any changes to QT pace (Treasury and MBS caps), reinvestment policy, or signals about balance sheet end-state. Quantify the monthly runoff rate and remaining reserves trajectory if data is available. [VERIFY current QT parameters]

6. **Map market reaction** — Document the immediate (first 30 min) and session-close moves in: fed funds futures (current meeting and 12-month-out contract), 2-year and 10-year yields, USD (DXY), S&P 500, and IG/HY credit spreads. Attribute moves to specific statement or press conference catalysts where possible.

7. **Synthesize the policy stance shift** — Summarize the net directional change in policy stance on a hawk-dove scale. State whether the meeting was a turning point, continuation, or recalibration. Identify the binding constraint on the Committee (inflation persistence, labor market cooling, financial stability risk).

8. **Assess forward implications** — Project the likely path for the next 1–3 meetings based on guidance language, dot plot trajectory, and stated data dependencies. Identify the key data releases (CPI, NFP, PCE) that could alter the path. Note any asymmetry in the reaction function (e.g., Committee more responsive to upside inflation surprises than downside growth surprises).

## Output

Structure the analysis report with these sections:

- **Decision Summary** — Rate action, vote split, one-sentence characterization (hawkish/dovish/neutral relative to expectations)
- **Statement Diff Analysis** — Table or annotated diff of key language changes with interpretation
- **Forward Guidance Assessment** — Current guidance stance, direction of change, and data conditions for next move
- **Projections & Dot Plot** (if applicable) — Median dot path, notable shifts, inflation and growth forecast revisions
- **Balance Sheet Update** — QT pace, any policy changes, reserves outlook
- **Market Reaction** — Rate, FX, equity, and credit moves with attribution
- **Outlook & Risks** — Base case for next 1–3 meetings, key data triggers, and tail risk scenarios

## Quality Checks

- Every characterization (hawkish/dovish) is supported by specific language or data, not editorial judgment alone
- Statement diff covers all substantive changes — not just the headline paragraph
- Dot plot analysis uses median, not mean, and accounts for rotating voter composition [VERIFY current rotation year]
- Market reaction separates statement release impact from press conference impact where timing data permits
- Forward path assessment explicitly states the data conditions that would invalidate the base case
- All rate levels, spreads, and futures prices are sourced with timestamps — never estimated from memory
