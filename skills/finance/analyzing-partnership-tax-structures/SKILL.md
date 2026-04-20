---
name: analyzing-partnership-tax-structures
language: en
description: Evaluates partnership tax arrangements with allocation waterfall, basis tracking, and carried interest treatment. Use when analyzing partnership tax, modeling distribution waterfalls, or tracking outside basis.
tags:
  - analysis
  - tax
  - treatment
metadata:
  author: casemark
  practice_areas:
    - Tax Planning
    - Tax Compliance
    - International Tax
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Partnership Tax Structures

Evaluates partnership tax arrangements with allocation waterfall, basis tracking, and carried interest treatment.

## When To Use

- Reviewing or structuring allocation provisions in a partnership or LLC operating agreement
- Modeling distribution waterfalls (return of capital, preferred return, catch-up, carried interest splits)
- Tracking a partner's outside basis for loss limitation, distribution, or disposition purposes
- Analyzing carried interest treatment under IRC Section 1061 and the three-year holding period rule
- Evaluating substantial economic effect under IRC Section 704(b) and the regulations thereunder
- Assessing a partnership's compliance posture for Schedule K-1 reporting, including hot asset allocations under Section 751

## Inputs To Gather

- **Partnership/operating agreement** — allocation provisions, distribution waterfall terms, capital account maintenance rules, and any special or targeted allocations
- **Capital account schedule** — beginning balances, contributions, allocations of income/loss/gain, distributions, and ending balances for each partner
- **Outside basis schedule** — per-partner basis tracking including share of liabilities (recourse, nonrecourse, qualified nonrecourse) under Sections 752 and 1.752 regulations
- **Distribution history** — timing and amounts of actual and deemed distributions, including property distributions and their FMV/basis
- **Tax return data** — Form 1065, Schedules K and K-1, Section 704(c) method elections, and any Section 754 election history
- **Waterfall model or term sheet** — economic terms for preferred returns, hurdle rates, catch-up provisions, and promote/carry splits
- **Entity structure diagram** — tiered partnership structures, blocker entities, and any PFIC or CFC considerations for international partners

## Workflow

1. **Map the allocation framework**
   - Identify whether the agreement uses a targeted capital account (target allocation) method or a traditional layered allocation method
   - Confirm capital account maintenance satisfies the economic effect safe harbor (maintain capital accounts per Section 1.704-1(b)(2)(iv), liquidation in accordance with capital accounts, deficit restoration obligation or qualified income offset)
   - Flag any allocations that lack substantial economic effect and may be reallocated under Section 704(b) [VERIFY against current partnership agreement language]

2. **Model the distribution waterfall**
   - Build or verify the waterfall tiers: return of capital → preferred return (note compounding convention) → GP/LP catch-up → residual carried interest split
   - Calculate carried interest promote at each tier; identify whether carry is deal-by-deal or whole-fund
   - Confirm clawback provisions and whether escrow/holdback mechanics exist for GP giveback obligations

3. **Track outside basis per partner**
   - Start with contributed cash/property basis, add share of liabilities (classify recourse vs. nonrecourse vs. qualified nonrecourse financing per Section 752)
   - Adjust for allocable income, gain, loss, deduction, and tax-exempt income
   - Reduce for distributions (cash and deemed under Section 752 liability shifts) — flag any distribution exceeding basis triggering gain under Section 731
   - Identify at-risk limitations (Section 465) and passive activity limitations (Section 469) that may suspend losses beyond basis [VERIFY partner-level activity status]

4. **Analyze carried interest under Section 1061**
   - Determine whether the partnership interest qualifies as an "applicable partnership interest" (API)
   - Apply the three-year holding period requirement — recharacterize LTCG as STCG for holding periods under three years
   - Identify exclusions: capital interests, Section 1231 gains, and interests acquired for capital contribution [VERIFY current IRS guidance and proposed regulations status]

5. **Evaluate Section 704(c) and hot asset issues**
   - Identify contributed property with built-in gain/loss; confirm the 704(c) method elected (traditional, traditional with curative, remedial)
   - For any partner transfer or distribution, assess Section 751(b) hot asset reallocation (unrealized receivables and substantially appreciated inventory)
   - Check for Section 754 election and compute any Section 743(b) basis adjustments for transferee partners

6. **Assess international and tiered structure considerations**
   - For foreign partners: identify ECI exposure, withholding obligations under Section 1446, and FIRPTA implications on disposition
   - For tiered partnerships: trace allocations through upper-tier/lower-tier structures; confirm aggregation or segregation approach for basis and 704(c) layers
   - Flag treaty-based positions and any required disclosure on Form 8833 [VERIFY applicable treaty provisions]

## Output

- **Allocation analysis memo** — summary of allocation provisions, economic effect testing, and any provisions requiring restructuring
- **Waterfall model** — tabular computation showing each distribution tier, cumulative distributions per partner class, and carried interest amounts
- **Outside basis schedule** — per-partner basis rollforward with liability share detail, flagging any negative basis or at-risk issues
- **Section 1061 analysis** — identification of API holders, recharacterization amounts, and holding period tracking
- **Section 704(c) / 751 summary** — built-in gain/loss layers, method elections, and hot asset exposure on transfers
- **Risk and compliance flags** — items requiring additional diligence, elections to be filed, or positions needing disclosure

## Quality Checks

- Confirm capital account balances reconcile to the partnership's balance sheet (Schedule L to Schedule M-2 tie-out)
- Verify that the sum of all partners' outside bases equals the partnership's inside basis plus any Section 743(b) adjustments
- Cross-check waterfall outputs against actual K-1 allocations for prior periods
- Ensure all Section 704(c) layers are tracked from contribution date forward and not collapsed prematurely
- Validate liability allocations sum to total partnership debt and are classified consistently with guarantee and pledge structures
- Flag any position where substantial authority is uncertain with [VERIFY] and recommend disclosure under Section 6662
