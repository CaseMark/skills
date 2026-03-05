---
name: creating-management-dashboards
description: Designs management reporting dashboards with KPI selection, visualization, and drill-down structure. Use when building financial dashboards, selecting KPIs, or designing management reports.
tags:
  - drafting
  - financial-planning-and-analysis
metadata:
  author: casemark
  practice_areas:
    - FP&A
    - Management Accounting
    - Business Intelligence
  document_types:
    - New Document
  skill_modes:
    - Drafting
    - Planning
---
# Creating Management Dashboards

## When To Use

- Designing a new executive or departmental dashboard from scratch
- Selecting and structuring KPIs for a specific business unit, function, or management audience
- Rebuilding or rationalizing an existing reporting pack that has grown unwieldy
- Translating a CFO or controller's reporting wish-list into a concrete dashboard specification
- Creating drill-down hierarchies so users can move from summary to root-cause detail

## Inputs To Gather

- **Audience & decision context**: Who will use the dashboard (C-suite, department heads, board)? What decisions does it support (resource allocation, performance reviews, forecasting)?
- **KPI candidates**: Existing metrics already tracked, plus any new metrics requested. For each, confirm definition, data source, refresh frequency, and owner.
- **Data sources & availability**: ERP/GL system, CRM, HRIS, budgeting tool, or data warehouse. Note any gaps or manual feeds.
- **Reporting cadence**: Real-time, daily, weekly, monthly, quarterly. Determine whether the dashboard replaces or supplements existing reports.
- **Benchmark & target context**: Internal targets (budget, prior year, rolling forecast) and external benchmarks (industry peers, analyst consensus) to display alongside actuals.
- **Constraints**: BI platform in use (Power BI, Tableau, Looker, Excel), data-access permissions, branding/style-guide requirements.

## Workflow

1. **Define the dashboard purpose statement** — Write a one-sentence scope: audience + decision supported + cadence. Example: "Monthly P&L dashboard for the CFO to monitor margin performance against forecast and flag variances > 5%."

2. **Select and tier KPIs**
   - **Tier 1 (headline)**: 4–6 KPIs visible at a glance (e.g., Revenue, Gross Margin %, EBITDA, Cash Conversion Cycle, Headcount, NRR).
   - **Tier 2 (supporting)**: Metrics that explain Tier 1 movement, accessible via drill-down (e.g., revenue by segment, COGS breakdown, DSO vs. DPO).
   - **Tier 3 (diagnostic)**: Granular data reached through a second drill-down (e.g., invoice-level detail, SKU-level margin).
   - For each KPI, document: name, formula/calculation, data source, refresh lag, owner, and RAG threshold definitions (green/amber/red). [VERIFY] that formulas match the organization's accounting policies (e.g., adjusted vs. GAAP EBITDA).

3. **Design the layout structure**
   - **Summary page**: Tier 1 KPIs as scorecards or gauges with trend sparklines and variance callouts.
   - **Detail pages**: One per functional area (Revenue, Cost, Working Capital, Workforce, etc.) showing Tier 2 metrics with comparison columns (actual vs. budget vs. prior year).
   - **Drill-down paths**: Define click-through navigation from each Tier 1 card to its detail page, and from detail rows to Tier 3 data.
   - **Filter bar**: Standard slicers for period, business unit, geography, and product line.

4. **Specify visualization types**
   - Use bar/column charts for period-over-period comparisons.
   - Use waterfall charts for variance bridges (budget → actual).
   - Use line charts for trend and forecast overlays.
   - Use tables with conditional formatting for dense data (e.g., GL-level detail).
   - Avoid pie charts for more than 4 categories; use horizontal bar instead.
   - Include a consistent color palette: one color for actuals, one for budget/forecast, red/amber/green for RAG status.

5. **Define interactivity and alerts**
   - Specify cross-filtering behavior between visuals.
   - Define exception-based alerts (e.g., email trigger when a KPI crosses its red threshold).
   - Document tooltip content for each visual (metric definition, data-as-of date, source).

6. **Map data pipeline requirements**
   - List each source system, extraction method (API, ODBC, flat file), transformation logic, and load schedule.
   - Identify any manual adjustments or journal entries that must be incorporated. [VERIFY] timing of month-end close vs. dashboard refresh to avoid stale data.

7. **Draft the dashboard specification document**
   - Compile the above into a spec: purpose statement, KPI dictionary, wireframe layouts, visual specs, data pipeline notes, and RAG threshold table.

## Output

Deliver a **Dashboard Specification Package** containing:

- **Purpose & audience statement**
- **KPI dictionary** — table with name, formula, source, owner, cadence, RAG thresholds
- **Wireframe layouts** — page-by-page description of visual placement, chart types, filter bar, and drill-down paths
- **Data pipeline map** — source → transform → load schedule per metric
- **Interactivity spec** — cross-filters, alerts, tooltip definitions
- **Implementation notes** — platform-specific considerations, access/role requirements, known data gaps marked [VERIFY]

## Quality Checks

- Every Tier 1 KPI has a defined drill-down path to at least Tier 2
- KPI formulas are explicitly documented and reconcilable to source systems
- RAG thresholds are defined with stakeholder sign-off, not arbitrary defaults
- Visualization choices match the data type (categorical vs. time-series vs. part-to-whole)
- Dashboard does not exceed 6–8 visuals per page to avoid cognitive overload
- Refresh cadence aligns with the data pipeline schedule — no visual shows data newer than its source supports
- [VERIFY] that metric definitions match the organization's chart of accounts and reporting standards (GAAP/IFRS)
- [VERIFY] data-access permissions ensure sensitive cost-center or compensation data is restricted by role
