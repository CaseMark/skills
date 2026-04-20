---
name: managing-working-capital
language: en
description: Optimizes working capital with DSO, DPO, and DIO analysis and improvement initiative tracking. Use when managing working capital, analyzing cash conversion cycle, or improving collection/payment terms.
tags:
  - management
  - corporate-finance
metadata:
  author: casemark
  practice_areas:
    - Corporate Finance
    - Treasury
    - Financial Planning
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Working Capital

## When To Use

- Analyzing the cash conversion cycle (CCC) and identifying bottlenecks in receivables, payables, or inventory turnover
- Preparing working capital dashboards or management reports for CFO/Treasury review
- Evaluating whether collection terms, payment terms, or inventory policies need adjustment
- Tracking improvement initiatives aimed at freeing trapped cash from operating cycle components
- Benchmarking DSO, DPO, and DIO against industry peers or internal targets
- Supporting M&A due diligence on target working capital positions or peg calculations

## Inputs To Gather

- **Receivables data**: Aging schedule (current, 30, 60, 90+ day buckets), revenue by period, credit terms by customer segment
- **Payables data**: Aging schedule, COGS or direct spend by period, standard payment terms by vendor tier, early-pay discount terms available
- **Inventory data**: Raw materials, WIP, and finished goods balances; COGS for DIO calculation; obsolescence reserves
- **Period selection**: Trailing 3-, 6-, or 12-month basis; specify whether using period-end or average balances
- **Benchmark targets**: Internal KPI targets, prior-period actuals, or industry medians for comparison
- **Initiative tracker** (if updating): List of active working capital improvement projects with owners, status, and projected cash impact

## Workflow

1. **Calculate Core Metrics**
   - DSO = (Accounts Receivable / Revenue) × Days in Period
   - DPO = (Accounts Payable / COGS) × Days in Period
   - DIO = (Inventory / COGS) × Days in Period
   - CCC = DSO + DIO − DPO
   - Compute each on both period-end and average-balance basis; note which method is used

2. **Trend and Variance Analysis**
   - Compare current-period metrics to prior period, prior year, and budget/target
   - Flag any metric that moved more than ±3 days or ±10% from the prior period
   - Decompose DSO movement into volume vs. mix vs. collection efficiency drivers
   - For DPO, separate organic changes from shifts caused by early-pay discount take-up rates
   - For DIO, distinguish raw-material build-up from finished-goods accumulation

3. **Receivables Deep-Dive**
   - Analyze aging migration: what percentage of current balances are rolling into 30+ buckets
   - Identify top 10 overdue accounts by dollar value; note any with dispute or credit-hold flags
   - Calculate collection effectiveness index (CEI) if beginning receivables data is available
   - Recommend actions: dunning escalation, credit-limit review, factoring evaluation [VERIFY applicability of factoring programs based on jurisdiction and entity structure]

4. **Payables Optimization Review**
   - Map early-pay discount terms (e.g., 2/10 net 30) and compute annualized return of taking vs. forgoing
   - Flag vendors where extending terms would yield material CCC improvement without relationship risk
   - Assess supply-chain financing or reverse-factoring program fit [VERIFY program availability with treasury/banking partners]

5. **Inventory Efficiency Assessment**
   - Break DIO into sub-components: days of raw materials, days of WIP, days of finished goods
   - Identify slow-moving or obsolete SKUs exceeding threshold (e.g., >180 days without movement)
   - Evaluate safety-stock levels relative to demand variability and lead times
   - Recommend inventory reduction levers: demand planning improvements, vendor-managed inventory, consignment

6. **Cash Impact Quantification**
   - For each identified lever, estimate incremental cash release: Δ Days × (Annual Revenue or COGS / 365)
   - Rank initiatives by cash impact, implementation effort, and time-to-benefit
   - Summarize total addressable working capital opportunity in dollar terms

7. **Initiative Tracking Update**
   - Update status of each active improvement initiative (on-track / at-risk / completed)
   - Record actual cash impact realized vs. projected for completed initiatives
   - Identify new initiatives from the analysis and assign preliminary owners and timelines

## Output

Produce a **Working Capital Management Report** containing:

- **Executive Summary**: CCC current vs. target, total cash trapped/freed vs. prior period, top 3 action items
- **Metrics Dashboard**: DSO, DPO, DIO, CCC with trend lines (current, prior period, prior year, target)
- **Variance Commentary**: Narrative explaining material movements in each metric with root causes
- **Component Analysis**: Receivables aging summary, payables term optimization table, inventory stratification
- **Opportunity Register**: Ranked list of working capital improvement levers with estimated cash impact, owner, and timeline
- **Initiative Tracker**: Status table for active and completed initiatives with actual vs. projected results

## Quality Checks

- Confirm that CCC = DSO + DIO − DPO; reconcile any rounding differences
- Verify revenue and COGS figures tie to the general ledger or financial statements for the period
- Ensure aging schedules foot to the total AR/AP balances on the balance sheet
- Check that average vs. period-end basis is applied consistently across all metrics
- Validate that cash-impact estimates use the correct denominator (revenue for AR, COGS for AP/inventory)
- Confirm benchmark comparisons use the same calculation methodology (e.g., same day-count convention)
- Flag any data gaps (e.g., missing sub-ledger detail) with [VERIFY] and note impact on analysis reliability
- Review initiative cash-impact projections for double-counting across overlapping levers
