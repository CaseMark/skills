---
name: conducting-profitability-analysis
language: en
description: Structures product, customer, and segment profitability analysis with cost allocation methodology. Use when analyzing profitability, allocating costs, or evaluating segment performance.
tags:
  - process
  - financial-planning-and-analysis
metadata:
  author: casemark
  practice_areas:
    - FP&A
    - Management Accounting
    - Business Intelligence
  document_types:
    - Process Documentation
  skill_modes:
    - Process Management
---
# Conducting Profitability Analysis

## When To Use

- Evaluating product-level, customer-level, or business-segment profitability
- Determining whether to retain, reprice, or discontinue a product line or customer relationship
- Allocating shared costs (overhead, SG&A, shared services) to profit centers
- Supporting pricing decisions with fully-loaded cost visibility
- Preparing segment reporting for management review or board presentations
- Benchmarking margin performance across divisions or time periods

## Inputs To Gather

- **Revenue data** — gross revenue by product/customer/segment, including volume, price, and mix breakdowns
- **Direct costs** — COGS, direct labor, materials, commissions, and any costs traceable to a single profit unit
- **Indirect costs** — overhead, shared services, corporate allocations, and facility costs requiring allocation
- **Allocation bases** — headcount, revenue share, square footage, machine hours, transaction counts, or other drivers already in use [VERIFY which bases the organization currently uses]
- **Period scope** — trailing 12 months, YTD, quarterly, or specific project window
- **Organizational structure** — chart of accounts hierarchy, cost center mapping, and any existing segment definitions
- **Prior analyses** — previous profitability studies, transfer pricing policies, or management allocation methodologies already approved

## Workflow

1. **Define the profitability dimension**
   - Confirm the unit of analysis: product, SKU family, customer, customer tier, channel, geographic segment, or business unit
   - Agree on the margin layers to compute: gross margin, contribution margin, segment operating margin, fully-loaded net margin

2. **Map revenue streams**
   - Disaggregate revenue into the chosen dimension; reconcile to the general ledger total
   - Separate recurring vs. non-recurring revenue if relevant (e.g., license vs. services)
   - Identify intercompany revenue and decide whether to include or eliminate [VERIFY transfer pricing treatment]

3. **Classify and assign direct costs**
   - Trace every cost that is unambiguously attributable to a single profit unit
   - Compute contribution margin (Revenue minus Direct Variable Costs) as the first profitability layer
   - Flag any costs currently pooled that could be directly traced with better data

4. **Allocate indirect costs**
   - Select allocation methodology — activity-based costing (ABC), revenue-weighted, headcount-weighted, or hybrid
   - Document each cost pool, its total, the chosen driver, and the rationale
   - Run allocation calculations; show the per-unit or per-segment burden clearly
   - Sensitivity-test at least one alternative allocation basis to show how results shift

5. **Compute margin layers and rank**
   - Build a waterfall from gross revenue down through each cost layer to fully-loaded margin
   - Rank segments/products/customers by absolute profit contribution and by margin percentage
   - Identify the top and bottom deciles; flag any units operating below breakeven

6. **Analyze drivers and root causes**
   - For underperforming units: isolate whether the issue is pricing, volume, cost structure, or allocation drag
   - For outperformers: assess sustainability — are margins dependent on one-time factors or structural advantages?
   - Calculate customer/product concentration risk (e.g., top 10 customers as % of total profit)

7. **Formulate recommendations**
   - Tier findings into action categories: reprice, restructure cost base, cross-sell, discontinue, or investigate further
   - Quantify the profit impact of each recommended action where possible
   - Note dependencies — e.g., contractual commitments, minimum order obligations, strategic accounts exempt from pure profitability criteria

## Output

- **Profitability summary table** — rows by dimension (product/customer/segment), columns for revenue, direct costs, contribution margin, allocated costs, operating margin, margin %
- **Margin waterfall chart** — visual cascade from gross revenue to net margin for each key segment
- **Ranking schedule** — segments ordered by profit contribution with cumulative percentage (Pareto view)
- **Cost allocation appendix** — each pool, driver, rate, and resulting allocation per segment
- **Sensitivity analysis** — margin impact under at least one alternative allocation basis
- **Recommendation memo** — prioritized actions with estimated profit uplift and implementation considerations

## Quality Checks

- Total allocated costs reconcile to total indirect cost pool (zero residual)
- Sum of segment revenues reconciles to consolidated revenue (no double-counting or gaps)
- Contribution margins are computed before any allocation — never blend direct and allocated costs in a single line
- Allocation drivers are sourced from auditable operational data, not estimates [VERIFY data source for each driver]
- Negative-margin segments include root-cause narrative, not just the numbers
- Any transfer pricing or intercompany elimination treatment is disclosed and consistent with corporate policy [VERIFY]
- Sensitivity analysis covers at least one materially different allocation method to test robustness of conclusions
