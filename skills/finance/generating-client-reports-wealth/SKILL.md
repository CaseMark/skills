---
name: generating-client-reports-wealth
description: Creates wealth management client reports with performance, net worth, and planning progress documentation. Use when preparing client reviews, creating wealth reports, or documenting planning progress.
tags:
  - wealth-management
metadata:
  author: casemark
  practice_areas:
    - Wealth Management
    - Private Banking
    - Financial Planning
  document_types:
    - Report
  skill_modes:
    - Analysis
---
# Generating Client Reports Wealth

## When To Use

- Preparing for a quarterly or annual client review meeting
- Producing periodic wealth reports (performance, net worth, cash flow)
- Documenting progress against financial planning milestones (retirement, education, estate, philanthropy)
- Responding to ad hoc client requests for portfolio or planning status
- Onboarding summaries that consolidate a new client's held-away and custodied assets

## Inputs To Gather

- **Reporting period**: Start/end dates; comparison periods (prior quarter, YTD, since inception)
- **Account and custodian data**: Custodial statements, held-away account extracts, alternative-investment capital account statements
- **Asset allocation targets**: Current IPS or model allocation; any recent changes approved by client
- **Performance benchmarks**: Blended or asset-class-specific benchmarks agreed upon in IPS
- **Net worth components**: Real estate appraisals, business valuations, liabilities (mortgages, lines of credit, notes payable), insurance CSV, vested equity compensation
- **Planning milestones**: Financial plan assumptions (return, inflation, spending), goal-funding status, Monte Carlo or deterministic projection outputs
- **Tax and cash flow data**: Realized gains/losses, estimated tax payments, income and distribution schedules
- **Client preferences**: Level of detail (executive summary vs. full book), preferred visualizations, any topics the advisor wants highlighted

## Workflow

1. **Confirm scope and period**
   - Agree on reporting date, comparison periods, and which accounts/entities to include
   - Identify whether report is performance-only, net-worth-only, or comprehensive (performance + net worth + planning)

2. **Aggregate and reconcile data**
   - Pull holdings, transactions, and valuations from all custodians and held-away sources
   - Reconcile beginning-of-period market values to prior report's ending values
   - Flag any stale prices, missing cost basis, or unpriced alternatives with [VERIFY]

3. **Calculate performance**
   - Compute time-weighted returns (TWR) at portfolio and asset-class level for each period
   - Where applicable, compute money-weighted returns (IRR) for private capital accounts
   - Compare to agreed benchmarks; calculate excess return and contribution/detraction by asset class
   - [VERIFY] Confirm fee methodology (gross vs. net of advisory fees, net of fund-level fees)

4. **Build net worth statement**
   - List investable assets, non-investable assets (real estate, business interests, collectibles), and liabilities
   - Show period-over-period change with sources of change (market movement, contributions/withdrawals, debt paydown)
   - Note any values based on estimates or prior-period appraisals with [VERIFY]

5. **Summarize planning progress**
   - Restate top goals (e.g., retirement at age 62, education funding for 3 children, $X legacy target)
   - Report current funding status or probability of success for each goal
   - Highlight material assumption changes (spending, returns, life expectancy) and their impact
   - Note action items from prior review and their completion status

6. **Draft narrative and commentary**
   - Write a concise executive summary (3-5 paragraphs) covering market context, portfolio actions taken, key results, and recommended next steps
   - Use plain language; avoid jargon the specific client is unlikely to understand
   - Flag any recommended rebalancing, tax-loss harvesting, or planning adjustments

7. **Assemble and format report**
   - Structure sections: Executive Summary, Performance Review, Asset Allocation, Net Worth, Planning Progress, Action Items
   - Include tables for returns (with benchmarks), asset allocation vs. target, and net worth schedule
   - Attach or reference supporting schedules (transaction log, realized gain/loss, fee summary)

## Output

- **Client Review Report** containing:
  - Executive summary with market commentary and key takeaways
  - Performance table: portfolio and asset-class TWR vs. benchmarks for QTD, YTD, 1-yr, 3-yr, since inception
  - Asset allocation snapshot: current vs. target with drift analysis
  - Net worth statement: assets, liabilities, total net worth, period-over-period delta
  - Planning progress dashboard: goal names, target values, current funded status, probability of success
  - Action items: open items from prior meeting, new recommendations, responsible party, and target dates
- Supporting schedules as appendices where applicable

## Quality Checks

- All return calculations reconcile to custodian-reported performance within acceptable tolerance (typically < 5 bps)
- Beginning market values tie to prior-period ending values; any breaks are explained
- Asset allocation percentages sum to 100%; benchmark blend weights match IPS
- Net worth totals foot correctly; assets minus liabilities equals stated net worth
- Every stale valuation, missing data point, or assumed figure is tagged [VERIFY]
- No forward-looking return projections are presented without clear disclosure that they are hypothetical
- [VERIFY] Report complies with firm's regulatory obligations (e.g., SEC Marketing Rule for performance advertising, GIPS if claimed)
- Client name, account numbers, and period dates are accurate on every page
- Narrative tone is appropriate for the client's sophistication level and preferences
