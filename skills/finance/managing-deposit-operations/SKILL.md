---
name: managing-deposit-operations
language: en
description: Structures deposit product analysis with pricing, retention analytics, and regulatory compliance. Use when analyzing deposits, evaluating pricing strategies, or managing deposit compliance.
tags:
  - management
  - commercial-banking
  - compliance
  - regulatory
metadata:
  author: casemark
  practice_areas:
    - Commercial Banking
    - Trade Finance
    - Lending
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Deposit Operations

## When To Use

- Analyzing deposit portfolio composition, concentration risk, or funding stability
- Evaluating deposit pricing strategies against market rates and cost-of-funds targets
- Reviewing deposit retention and attrition trends across product lines or customer segments
- Preparing for regulatory examinations related to deposit operations (Reg DD, Reg E, Reg CC) [VERIFY jurisdiction-specific regulations]
- Assessing liquidity risk contribution from deposit base volatility
- Managing exception pricing approvals, rate specials, or promotional campaigns

## Inputs To Gather

- **Portfolio data**: Current deposit balances by product type (DDA, NOW, MMDA, savings, time deposits), vintage, and customer segment
- **Pricing information**: Current offered rates, posted rates vs. exception rates, competitor rate surveys, internal cost-of-funds or FTP (funds transfer pricing) rates
- **Retention metrics**: Account attrition rates, renewal rates on maturing CDs, relationship depth indicators (number of products per household)
- **Regulatory context**: Most recent exam findings, compliance audit results, pending regulatory changes affecting deposit operations [VERIFY applicable regulations by charter type and state]
- **Operational data**: Account opening volumes, dormant account counts, escheatment pipeline, error/dispute rates on transaction accounts
- **Market benchmarks**: Peer group deposit cost comparisons, beta assumptions, deposit growth trends from call report data

## Workflow

1. **Segment the portfolio** — Break deposits into core vs. non-core, rate-sensitive vs. rate-insensitive, and retail vs. commercial/public funds. Identify top-10 depositor concentration and any single-depositor exposures exceeding 2% of total deposits.

2. **Analyze pricing position** — Compare current offering rates to the federal funds rate, peer median, and internal FTP hurdles. Calculate effective cost of funds by product. Identify products where pricing is above market without corresponding retention benefit, or below market with elevated attrition risk.

3. **Assess deposit stability** — Review historical decay rates and surge balances. Evaluate core deposit intangible assumptions against actual behavior. Flag any product categories where observed runoff exceeds model assumptions by more than 15%.

4. **Review compliance posture** — Confirm Reg DD truth-in-savings disclosures are current for all products. Verify Reg E error resolution timelines are being met. Check Reg CC funds availability schedules against actual hold practices. Confirm dormant account and escheatment procedures align with state unclaimed property laws. [VERIFY state-specific escheatment dormancy periods]

5. **Evaluate operational efficiency** — Review account opening cycle times, exception pricing approval turnaround, and deposit operations staffing ratios. Identify manual processes suitable for automation (e.g., CD maturity notices, rate change communications).

6. **Prepare management report** — Consolidate findings into an actionable summary with pricing recommendations, retention strategy adjustments, compliance remediation items, and operational improvement priorities.

## Output

Structure the management report with the following sections:

- **Executive Summary**: Portfolio size, growth trend, weighted average cost of deposits, and top 3 action items
- **Portfolio Composition**: Balances and mix percentages by product, segment, and maturity band; comparison to prior quarter and prior year
- **Pricing Analysis**: Rate positioning table showing each product vs. FTP, peer median, and top competitor; net interest margin impact of proposed rate changes
- **Retention Dashboard**: Attrition rates by product and segment, CD renewal rates, relationship depth trends, at-risk balance estimates
- **Compliance Status**: Open findings, remediation progress, upcoming regulatory deadlines, and any areas requiring [VERIFY] before next exam
- **Recommendations**: Prioritized list of pricing adjustments, product changes, compliance actions, and operational improvements with estimated balance and cost impact

## Quality Checks

- Confirm all balance figures reconcile to the general ledger or core system reports as of the stated reporting date
- Verify rate comparisons use consistent day-count conventions and compounding methods (APY vs. nominal rate)
- Ensure concentration percentages account for related-entity aggregation per regulatory guidance
- Check that compliance timelines reference current regulation versions — mark outdated citations with [VERIFY]
- Validate that FTP or cost-of-funds methodology is consistent with the institution's ALM framework
- Confirm dormant account and escheatment data reflects the correct state-specific dormancy periods [VERIFY by state]
- Flag any data gaps (missing segments, incomplete time series) explicitly rather than interpolating without disclosure
