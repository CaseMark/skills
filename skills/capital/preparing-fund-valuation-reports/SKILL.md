---
name: preparing-fund-valuation-reports
language: en
description: Structures fund NAV reporting with investment-level valuations, methodology disclosure, and fair value hierarchy classification. Use when preparing NAV reports, documenting valuation methodology, or presenting fair value analysis.
tags:
  - preparation
  - investor-relations-and-lp-reporting
  - investment
  - valuation
metadata:
  author: casemark
  practice_areas:
    - Investor Relations
    - LP Reporting
    - Fund Administration
  document_types:
    - Preparation Document
  skill_modes:
    - Preparation
---
# Preparing Fund Valuation Reports

Structures fund NAV reporting with investment-level valuations, methodology disclosure, and fair value hierarchy classification.

## When To Use

- Preparing quarterly or annual NAV statements for LP distribution
- Documenting valuation methodology for auditor or advisory committee review
- Classifying portfolio holdings across the ASC 820 / IFRS 13 fair value hierarchy
- Responding to LP requests for investment-level valuation detail
- Onboarding a new fund administrator and establishing valuation report templates

## Inputs To Gather

- **Portfolio schedule**: Current holdings with cost basis, ownership percentage, investment date, and instrument type (equity, debt, convertible, warrant)
- **Valuation data by investment**: Most recent marks, comparable transaction multiples, DCF assumptions, or third-party appraisals
- **Prior-period NAV report**: Previous valuations for roll-forward and change commentary
- **Fund terms**: Management fee calculation basis, carried interest waterfall parameters, hurdle rate, catch-up provisions
- **Fair value hierarchy classifications**: Existing Level 1 / 2 / 3 designations and any reclassification events
- **Valuation policy**: Fund's adopted valuation policy, including frequency, governance approvals, and permitted methodologies
- **Fee and expense data**: Accrued management fees, fund expenses, organizational costs, and any fee offsets or waivers
- **LP commitment schedule**: Committed capital, called capital, unfunded commitments, and distributions to date per LP

## Workflow

1. **Validate source data** — Reconcile the portfolio schedule against the general ledger. Confirm every holding has a current-period valuation input. Flag any investment missing a mark or carrying a stale valuation (>90 days without update) with [VERIFY].

2. **Classify fair value hierarchy** — Assign each investment to Level 1 (quoted prices in active markets), Level 2 (observable inputs such as comparable company multiples or recent transaction prices), or Level 3 (unobservable inputs such as DCF models or management estimates). Document the primary valuation technique and key inputs for each Level 3 holding.

3. **Build the investment-level valuation table** — For each holding, present:
   - Company/asset name, instrument type, and acquisition date
   - Cost basis and current fair value
   - Valuation methodology (market approach, income approach, or cost approach)
   - Key assumptions (e.g., revenue multiple of 8.2x applied to LTM revenue; discount rate of 12%)
   - Unrealized gain/loss and percentage change from prior period

4. **Calculate fund-level NAV** — Sum investment fair values, add cash and receivables, subtract accrued fees, expenses, and payables. Present the NAV roll-forward: beginning NAV → contributions → distributions → realized gains/losses → change in unrealized → expenses → ending NAV.

5. **Prepare methodology disclosure** — Draft a narrative section covering:
   - Valuation policy summary and governance (e.g., quarterly valuation committee approval)
   - Description of each methodology used and when it applies
   - Significant assumptions and sensitivity for material Level 3 positions
   - Any changes in methodology from prior period and rationale

6. **Compute per-LP allocations** — Apply the waterfall provisions from the LPA to allocate NAV across LP classes. Show each LP's share of NAV, unrealized carry accrual, and management fee charges. [VERIFY] waterfall mechanics against the specific LPA terms.

7. **Draft the report package** — Assemble into standard sections:
   - Executive summary with headline NAV, period-over-period change, and key drivers
   - Investment-level valuation schedule
   - Fair value hierarchy summary table (aggregate by level with percentage of total)
   - NAV roll-forward bridge
   - Methodology and assumptions disclosure
   - LP allocation schedule (if included in the distribution package)

## Output

The final deliverable is a fund valuation report containing:

- **NAV summary**: Total fund NAV, NAV per unit/share, and comparison to prior period
- **Investment schedule**: Line-item valuations with methodology, key inputs, and fair value hierarchy level
- **Fair value hierarchy table**: Aggregate amounts at Level 1, 2, and 3 with transfers between levels noted
- **Roll-forward bridge**: Beginning-to-ending NAV reconciliation
- **Methodology narrative**: Plain-language disclosure of valuation approaches and material assumptions
- **LP allocation table** (where applicable): Per-LP NAV, carry accrual, and fee detail

Format as a structured report suitable for LP quarterly letters, advisory committee materials, or auditor work papers.

## Quality Checks

- Every investment in the portfolio schedule appears in the valuation table — no orphaned or omitted positions
- Fair value hierarchy levels are consistent with the valuation inputs actually used (e.g., a DCF-only valuation must not be classified as Level 2)
- NAV roll-forward reconciles to the ending investment schedule total within rounding tolerance
- Management fee and expense accruals tie to the fund's fee terms and accounting records
- Prior-period comparisons use the same methodology unless a change is explicitly disclosed
- Sensitivity analysis is provided for any Level 3 position exceeding 10% of total NAV
- [VERIFY] compliance with ASC 820 / IFRS 13 disclosure requirements based on the fund's reporting framework
- [VERIFY] LP allocation waterfall against the governing LPA, side letters, and any fee arrangement modifications
