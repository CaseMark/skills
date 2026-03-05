---
name: tracking-13d-and-13g-filing-patterns
description: Monitors beneficial ownership filings with accumulation pattern analysis, intent assessment, and historical activist progression. Use when tracking 13D filings, analyzing accumulation patterns, or identifying potential activist situations.
tags:
  - monitoring
  - activist-and-event-driven-investing
metadata:
  author: casemark
  practice_areas:
    - Activist Investing
    - Event-Driven Strategy
    - Special Situations
  document_types:
    - Tracking Report
  skill_modes:
    - Monitoring
---
# Tracking 13d And 13g Filing Patterns

Monitors beneficial ownership filings with accumulation pattern analysis, intent assessment, and historical activist progression.

## When To Use

- A new Schedule 13D or 13D/A is filed and you need to assess the filer's intent, accumulation trajectory, and potential activist playbook
- Monitoring a 13G-to-13D conversion that signals a shift from passive to active posture
- Building a historical profile of a known activist's filing behavior across multiple targets
- Screening for early-stage accumulation patterns that may precede public campaigns or proxy contests
- Evaluating whether a 13D amendment reflects escalation (board seats, merger proposals) or de-escalation (stake reduction, standstill)

## Inputs To Gather

- **Filing details**: EDGAR CIK, filer name, filing date, amendment number, Schedule type (13D, 13D/A, 13G, 13G/A)
- **Ownership data**: Shares held (sole/shared voting and dispositive power), percentage of class, source of funds
- **Item 4 narrative**: Purpose of transaction text — the core signal for intent classification
- **Historical filings**: Prior 13D/13G filings by the same filer across all targets (build the activist's track record)
- **Target company context**: Market cap, share price at filing date, float, institutional ownership concentration, upcoming catalysts (earnings, proxy season, M&A rumors)
- **Group membership**: Whether filer is part of a group (Section 13(d)(3)) and identity of co-filers

## Workflow

1. **Parse the filing**
   - Extract ownership percentages, share counts, and changes from prior amendments
   - Isolate Item 4 (Purpose of Transaction) language for intent signals
   - Flag any new exhibits: voting agreements, letters to the board, nominee lists, or standstill agreements

2. **Classify filing type and intent**
   - **Passive (13G)**: Investment-only; confirm filer qualifies as QII, exempt investor, or passive investor under Rule 13d-1(b)/(c)/(d) [VERIFY: current rule thresholds — SEC amended 13D/G rules effective 2024]
   - **Active (13D)**: Categorize purpose language into: governance reform, board representation, strategic alternatives (sale/merger), operational changes, capital return, or opposition to pending transaction
   - **Conversion (13G → 13D)**: Flag as high-priority signal; note the date gap between 13G and 13D and any accumulation during that window

3. **Analyze accumulation pattern**
   - Plot ownership percentage over time using all amendments
   - Calculate accumulation velocity: shares added per filing period, average days between amendments
   - Identify patterns: steady accumulation, burst buying near catalysts, toehold-then-pause, or creeping toward board-demand thresholds (typically 5-10%)
   - Note any derivative positions, swaps, or economic-only exposure disclosed in Item 6

4. **Assess activist progression signals**
   - Compare Item 4 language across amendments for escalation markers:
     - Early: "may engage in discussions with management"
     - Mid: "intends to seek board representation" or "has sent a letter to the board"
     - Late: "has nominated candidates" or "intends to solicit proxies"
   - Cross-reference filer's historical playbook on other targets — typical timeline from initial filing to public campaign
   - Check for parallel actions: 13D filed alongside DFAN14A (exempt proxy solicitation), 8-K responses from the target, or poison pill adoption

5. **Evaluate group dynamics and co-filer network**
   - Map relationships between co-filers (shared GP, common LPs, prior joint campaigns)
   - Assess whether group formation itself is the signal (wolfpack assembly)
   - Note any disclaimers of group status and whether they appear credible given coordination evidence

6. **Generate tracking report**
   - Compile a structured brief with: filer profile, accumulation timeline, intent classification, escalation probability, and recommended monitoring cadence
   - Assign an alert tier: Routine (passive 13G, no change), Watch (new 13D, early-stage language), Elevated (board demands, proxy filing imminent), Critical (proxy contest launched, tender offer)

## Output

- **Filing Summary Table**: Filer, target, date, schedule type, shares, percentage, change from prior, Item 4 classification
- **Accumulation Timeline Chart** (or structured data for charting): Date, cumulative ownership %, event annotations
- **Intent Classification**: Passive / Monitoring / Engagement / Campaign — with supporting Item 4 excerpts
- **Activist Profile Card**: Filer's historical win rate, average campaign duration, preferred tactics, sector focus, typical exit
- **Alert Tier Assignment**: Routine / Watch / Elevated / Critical — with rationale and recommended next review date
- **Escalation Indicators**: Specific language or actions that would trigger a tier upgrade

## Quality Checks

- Verify ownership math: confirm share counts and percentages align with the target's shares outstanding as reported in the most recent 10-Q/10-K [VERIFY]
- Confirm filing deadlines were met — late filings themselves are a signal (potential stealth accumulation) [VERIFY: current 13D filing deadline is 5 business days under amended rules]
- Cross-check filer identity against known activist databases (13D Monitor, SharkWatch, FactSet) for historical context
- Ensure Item 4 language is quoted directly, not paraphrased, when used to support intent classification
- Flag any discrepancies between reported beneficial ownership and institutional holdings data (13F filings)
- Mark all jurisdiction-dependent thresholds and deadline assumptions with [VERIFY] — rules vary internationally and SEC amendments may shift US thresholds
