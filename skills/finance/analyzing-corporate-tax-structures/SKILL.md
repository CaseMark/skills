---
name: analyzing-corporate-tax-structures
description: Structures corporate tax analysis with entity selection, state nexus, and effective tax rate optimization. Use when analyzing tax structures, selecting entity types, or optimizing corporate tax positions.
tags:
  - analysis
  - tax
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
# Analyzing Corporate Tax Structures

## When To Use

- Evaluating entity type selection (C-corp, S-corp, LLC, LP, partnership) for a new venture or restructuring
- Assessing multi-state nexus exposure and apportionment impact on effective tax rate
- Modeling the tax consequences of a proposed M&A transaction, reorganization, or conversion
- Comparing pass-through vs. double-taxation structures under current rate schedules
- Reviewing international tax posture including GILTI, FDII, Subpart F, and treaty positions
- Optimizing the blended effective tax rate across federal, state, and international jurisdictions

## Inputs To Gather

- **Entity details**: Current entity type, jurisdiction of formation, ownership structure, and any existing elections (e.g., S-election, check-the-box)
- **Financial data**: Projected or historical revenue, EBIT, taxable income, and distributions/dividends
- **State footprint**: States where the entity has physical presence, employees, sales, or economic nexus triggers
- **Ownership profile**: Number and type of owners (individuals, trusts, foreign persons, other entities), ownership percentages
- **International operations**: Foreign subsidiaries, intercompany transactions, transfer pricing arrangements, treaty jurisdictions
- **Transaction context**: If restructuring, the proposed deal structure (asset vs. stock sale, merger, conversion, spin-off)
- **Tax attributes**: NOL carryforwards, credit carryforwards, built-in gains exposure, Section 382 limitations

## Workflow

1. **Define scope and objectives**
   - Confirm whether the analysis covers entity selection, restructuring, rate optimization, or a combination
   - Identify the decision the stakeholder needs to make and the alternatives under consideration

2. **Map entity structure and ownership**
   - Diagram the current (or proposed) entity chart with ownership percentages
   - Flag any ownership constraints (e.g., S-corp eligibility limits, partnership allocation rules)

3. **Calculate federal tax impact by alternative**
   - For each entity option, compute taxable income, entity-level tax, and owner-level tax on distributions
   - Apply current statutory rates: C-corp at 21% federal [VERIFY — confirm current rate]; qualified dividend rate at 20% + 3.8% NIIT [VERIFY]; individual pass-through rates with §199A deduction where applicable [VERIFY eligibility and phase-outs]
   - Model total tax burden including self-employment tax exposure for pass-through entities

4. **Analyze state and local tax exposure**
   - Identify nexus-creating activities in each state using both physical presence and economic nexus thresholds [VERIFY — state-specific thresholds vary]
   - Determine apportionment methodology per state (single sales factor vs. three-factor) [VERIFY by state]
   - Calculate state effective rate for each entity alternative, accounting for entity-level taxes (e.g., California LLC fee, Texas margin tax, Illinois PTE tax) [VERIFY current rates]
   - Assess availability of PTE tax elections and corresponding owner-level SALT deduction benefits

5. **Evaluate international tax considerations** (if applicable)
   - Identify CFC status and Subpart F income categories
   - Model GILTI inclusion and §250 deduction (50% deduction for C-corps, unavailable to pass-throughs) [VERIFY current deduction percentage]
   - Assess FDII benefit for domestic C-corps with export income
   - Review applicable tax treaties and withholding rates on cross-border payments
   - Flag transfer pricing risks on intercompany transactions

6. **Model transaction-specific impacts** (if restructuring)
   - Compare taxable vs. tax-free reorganization paths (Type A, B, C, D, F reorganizations)
   - Quantify built-in gains exposure for S-corp conversions within recognition period [VERIFY — currently 5 years]
   - Calculate Section 338(h)(10) or Section 336(e) election impacts for stock-deal-treated-as-asset scenarios
   - Assess Section 382 limitations on post-acquisition NOL utilization

7. **Compute blended effective tax rate**
   - Aggregate federal, state, and international tax for each alternative into a single blended ETR
   - Present side-by-side comparison table showing total tax dollars and ETR by scenario

## Output

The analysis report should include:

- **Executive summary**: Recommended structure with headline ETR and key drivers
- **Entity comparison matrix**: Side-by-side table of 2–4 alternatives showing federal tax, state tax, international tax, total tax, and blended ETR
- **State nexus map**: List of nexus states with apportionment factors and entity-level tax obligations
- **International tax summary** (if applicable): CFC chart, GILTI/FDII calculations, treaty rate table
- **Sensitivity analysis**: Impact of ±10–20% income variance on ETR and total tax across alternatives
- **Implementation steps**: Specific elections, filings, and deadlines required to execute the recommended structure
- **Risk factors and limitations**: Assumptions made, regulatory uncertainty, and items requiring further diligence

## Quality Checks

- Confirm all statutory rates and thresholds are current — mark with [VERIFY] any rate that may have changed since last update
- Validate that entity eligibility requirements are met (e.g., S-corp shareholder limits, partnership substantial economic effect)
- Ensure apportionment calculations use the correct state-specific methodology and sourcing rules
- Cross-check that pass-through income allocations tie to ownership percentages and any special allocation provisions
- Verify NOL and credit carryforward utilization does not exceed applicable limitations (Section 382, SRLY rules)
- Confirm international calculations account for foreign tax credits and avoid double-counting
- Flag any position that may trigger disclosure requirements (e.g., uncertain tax positions under ASC 740, reportable transactions)
