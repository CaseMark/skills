---
name: managing-securities-lending
language: en
description: Structures securities lending operations with borrower management, collateral monitoring, and revenue optimization. Use when managing sec lending, monitoring loan collateral, or optimizing lending revenue.
tags:
  - management
  - fund-operations
metadata:
  author: casemark
  practice_areas:
    - Fund Administration
    - Investment Operations
    - Fund Accounting
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Securities Lending

Structures securities lending operations covering borrower management, collateral monitoring, loan recall workflows, and revenue optimization across agency and principal lending programs.

## When To Use

- Setting up or reviewing a securities lending program (agency or principal model)
- Onboarding new borrower counterparties or evaluating existing borrower credit limits
- Monitoring collateral adequacy, margin calls, and mark-to-market adjustments
- Analyzing lending revenue splits, fee schedules, and utilization rates
- Managing loan recalls for corporate actions, proxy voting, or portfolio rebalancing
- Preparing periodic lending activity reports for fund boards or investment committees
- Evaluating reinvestment guidelines and cash collateral pool performance

## Inputs To Gather

- **Lending authorization**: Fund prospectus or board resolution authorizing securities lending; any lendable asset restrictions (e.g., ESG exclusions, concentration limits)
- **Borrower roster**: Approved counterparties with credit ratings, borrowing limits, and master securities lending agreement (MSLA) status
- **Loan inventory**: Current on-loan positions by security, borrower, loan type (term vs. open), and rate/rebate terms
- **Collateral schedule**: Accepted collateral types (cash, government bonds, equities), required margin percentages (typically 102% domestic / 105% international) [VERIFY against specific program guidelines]
- **Revenue terms**: Fee splits between fund and lending agent; any minimum spread or guaranteed-fee arrangements
- **Reinvestment parameters**: Approved investment guidelines for cash collateral pools (WAM limits, credit quality, liquidity buckets)
- **Corporate action calendar**: Upcoming dividends, votes, and mandatory events requiring recall decisions

## Workflow

1. **Map the lending program structure**
   - Confirm whether program operates as agency (via lending agent) or principal (fund lends directly)
   - Identify the lending agent, tri-party custodian, and collateral management platform
   - Document fee split arrangement and any revenue guarantees or indemnification provisions

2. **Review borrower exposure**
   - Pull current borrower-level loan balances and compare against approved credit limits
   - Flag any borrower exceeding concentration thresholds (single-borrower or aggregate)
   - Check MSLA/GMSLA execution status and netting opinion coverage for each borrower [VERIFY jurisdiction-specific netting enforceability]

3. **Monitor collateral adequacy**
   - Verify daily mark-to-market of loaned securities vs. posted collateral
   - Confirm margin calls were issued and settled for any deficit positions (typically T+1 cure)
   - Review non-cash collateral eligibility against program guidelines (haircuts, asset type, issuer concentration)
   - Check cash collateral reinvestment pool NAV stability, WAM, and compliance with 2a-7-style constraints [VERIFY if Rule 2a-7 standards apply to the specific program]

4. **Manage loan recalls and returns**
   - Identify securities requiring recall for corporate actions (record dates, proxy deadlines)
   - Evaluate whether to recall for proxy voting based on materiality of the vote and lending revenue trade-off
   - Track recall execution — confirm borrower returns within standard settlement window (typically T+3 for equities) [VERIFY market-specific settlement cycles]
   - Process voluntary returns initiated by borrowers; update loan inventory accordingly

5. **Analyze revenue and utilization**
   - Calculate gross and net lending revenue by security, borrower, and fund
   - Assess utilization rate (on-loan value / lendable supply) and identify underutilized high-demand securities ("specials")
   - Compare realized lending spreads to market benchmarks (e.g., IHS Markit, DataLend benchmarks)
   - Identify opportunities to shift open loans to term structures for rate certainty on high-demand names

6. **Prepare reporting and governance deliverables**
   - Generate lending activity summary: new loans, returns, recalls, revenue accrued
   - Produce borrower exposure report with credit limit utilization percentages
   - Compile collateral adequacy report showing margin coverage ratios
   - Draft board/committee report covering program performance, risk metrics, and any policy exceptions

## Output

The final management report should include:

- **Program overview**: Aggregate on-loan balance, number of active borrowers, total lendable supply
- **Revenue summary**: Gross revenue, agent fees, net revenue to fund; period-over-period trend
- **Utilization analysis**: Overall utilization rate, top-earning securities, specials vs. GC breakdown
- **Borrower exposure table**: Each borrower's outstanding balance, credit limit, utilization %, MSLA status
- **Collateral summary**: Collateral type mix, average margin coverage, any margin call exceptions
- **Cash reinvestment pool snapshot**: NAV, WAM, WAL, yield, any guideline breaches
- **Recall activity log**: Recalls issued, settled, and any fails with borrower and days outstanding
- **Risk flags and exceptions**: Limit breaches, collateral shortfalls, reinvestment guideline violations, or recall fails requiring escalation

## Quality Checks

- Verify loan balances reconcile between lending agent reports and fund accounting/custody records
- Confirm collateral margin percentages meet or exceed program minimums — no unresolved deficits
- Ensure revenue accruals tie to lending agent statements and are booked to the correct fund/share class
- Validate that all securities with upcoming record dates have been flagged for recall decision
- Check borrower credit limits against most recent credit assessments (not stale ratings)
- Confirm cash collateral reinvestment pool compliance with WAM, credit quality, and liquidity guidelines
- Cross-reference any indemnification triggers (e.g., borrower default, settlement fail) with agent contractual terms
- Mark any data points sourced from estimates or prior-period figures with [VERIFY]
