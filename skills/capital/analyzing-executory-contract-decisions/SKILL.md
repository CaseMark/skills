---
name: analyzing-executory-contract-decisions
description: Evaluates assumption, rejection, and assignment decisions for executory contracts and unexpired leases in bankruptcy. Use when analyzing contract decisions, evaluating lease rejections, or modeling cure cost exposure.
tags:
  - analysis
  - distressed-and-restructuring
metadata:
  author: casemark
  practice_areas:
    - Restructuring
    - Distressed Investing
    - Turnaround
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Executory Contract Decisions

Evaluates assumption, rejection, and assignment decisions for executory contracts and unexpired leases in bankruptcy under §365 of the Bankruptcy Code.

## When To Use

- Debtor is preparing schedules of executory contracts and unexpired leases for assumption/rejection motions
- Distressed investor is underwriting a target with significant lease or contract exposure
- Turnaround advisor needs to model cure cost scenarios and rejection claim liabilities
- Evaluating whether a contract qualifies as executory under the Countryman test (material unperformed obligations on both sides)
- Assessing assignability of contracts despite anti-assignment clauses (§365(f)) or applicable law restrictions

## Inputs To Gather

- Complete list of executory contracts and unexpired leases from debtor's schedules (Schedule G)
- Cure amounts for each contract (pre-petition arrearages, penalties, fees)
- Counterparty identity, financial condition, and strategic importance
- Contract terms: remaining term, renewal options, termination provisions, change-of-control clauses
- Market comparables for lease rates or service pricing (to assess above/below market status)
- Any anti-assignment provisions, IP license restrictions, or personal-services clauses
- Applicable non-bankruptcy law governing assignment restrictions [VERIFY — varies by jurisdiction and contract type]
- Debtor's go-forward business plan identifying operationally critical contracts

## Workflow

1. **Classify each contract** — Confirm executory status using the Countryman test. Flag contracts where executory status is disputed (e.g., fully paid licenses, expired-but-holdover leases). Separate real property leases from personal property leases and non-lease contracts, as different statutory provisions apply.

2. **Categorize by decision** — Sort contracts into three buckets:
   - **Assume** — Contract is operationally necessary and at or below market terms; debtor can cure defaults and provide adequate assurance of future performance
   - **Reject** — Contract is above-market, non-essential, or burdensome; rejection damages are quantifiable and manageable as a general unsecured claim
   - **Assume and assign** — Contract has value to a purchaser in a §363 sale; assess whether anti-assignment provisions are overridden under §365(f) [VERIFY — certain exceptions apply for personal-services, financial accommodation, and non-residential real property leases in shopping centers]

3. **Calculate cure costs** — For each contract proposed for assumption, quantify:
   - Pre-petition monetary defaults (rent arrearages, unpaid invoices)
   - Non-monetary defaults that must be cured (if applicable under controlling circuit law) [VERIFY — circuits split on whether non-monetary defaults must be cured]
   - Penalties, late fees, and interest through the anticipated cure date
   - Aggregate cure exposure and rank by magnitude

4. **Model rejection claim exposure** — For rejected contracts, estimate:
   - Rejection damages claim (breach treated as pre-petition unsecured claim)
   - For real property leases: statutory cap under §502(b)(6) — the greater of one year's rent or 15% of remaining term (not to exceed three years), plus unpaid pre-petition rent [VERIFY — confirm current statutory formula]
   - For employment contracts: statutory cap under §502(b)(7)
   - Impact on unsecured claims pool and projected recovery rates

5. **Assess adequate assurance** — For contracts to be assumed, evaluate whether the debtor (or assignee) can demonstrate adequate assurance of future performance, including:
   - Financial wherewithal to perform going forward
   - Track record and operational capacity
   - Shopping center lease requirements under §365(b)(3) (tenant mix, use clauses, radius restrictions) [VERIFY — applicable only to shopping center leases]

6. **Evaluate strategic and timing considerations** — Flag deadline-sensitive issues:
   - Non-residential real property lease assumption deadline (§365(d)(4)): 120 days after petition, extendable by 90 days for cause [VERIFY — confirm current statutory deadlines]
   - Personal property lease performance obligations under §365(d)(5) and (d)(10)
   - Impact of plan confirmation timeline on contract decisions
   - Counterparty leverage and likelihood of contested cure amounts

## Output

- **Contract decision matrix** — Table listing each contract with counterparty, contract type, recommended action (assume/reject/assign), cure amount, rejection claim estimate, and strategic rationale
- **Cure cost summary** — Aggregate cure exposure by category with high/base/low scenarios
- **Rejection claim impact analysis** — Projected rejection claims and effect on unsecured creditor recovery
- **Risk flags** — Contracts with disputed executory status, contested cure amounts, assignability challenges, or imminent statutory deadlines
- **Recommendation narrative** — Summary of key findings with prioritized action items for the debtor, purchaser, or investment committee

## Quality Checks

- Verify that every contract on Schedule G is accounted for in the analysis — no gaps
- Confirm cure amounts tie to debtor's books and records or counterparty cure notices
- Validate rejection claim cap calculations against the current statutory formula
- Ensure anti-assignment analysis addresses both §365(f) override scope and applicable exceptions
- Check that adequate assurance analysis reflects the specific requirements for the contract type (especially shopping center leases)
- Flag any contracts where the executory determination is uncertain and note the analytical basis for the classification
- Mark all jurisdiction-dependent conclusions with [VERIFY] for local counsel review
