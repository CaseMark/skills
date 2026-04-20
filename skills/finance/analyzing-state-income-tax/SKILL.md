---
name: analyzing-state-income-tax
language: en
description: Evaluates multi-state income tax positions with apportionment, nexus, and combined reporting analysis. Use when analyzing state tax, calculating apportionment, or managing multi-state filing.
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
# Analyzing State Income Tax

Evaluates multi-state income tax positions with apportionment, nexus, and combined reporting analysis.

## When To Use

- Entity has operations, employees, property, or sales in multiple states and needs to determine filing obligations
- Assessing whether physical presence, economic nexus, or factor-presence thresholds trigger income tax liability in a new state [VERIFY: state-specific nexus thresholds]
- Calculating apportionment of income across filing states under single-sales-factor, three-factor, or modified formulas
- Evaluating whether combined/unitary reporting is required or elective and modeling the tax impact
- Reviewing entity structure (pass-through vs. C-corp, holding companies, disregarded entities) for state tax efficiency
- Responding to a state audit notice, voluntary disclosure agreement (VDA), or amnesty program

## Inputs To Gather

- **Entity details**: Legal structure, affiliated group chart, state of incorporation/formation, fiscal year-end
- **State footprint**: States with offices, employees, remote workers, warehouses, inventory, independent contractors, or significant customers
- **Revenue data**: Gross receipts by state (sourced by market-based vs. cost-of-performance), intercompany transactions, and throwback/throwout exposure
- **Apportionment factors**: Property (owned and rented), payroll, and sales for each state, with detail on how each factor is currently sourced
- **Prior filings**: Last 3–4 years of state returns, nexus questionnaires, and any prior VDA or audit history
- **Elections in effect**: Combined reporting elections, water's-edge elections, PL 86-272 reliance positions, SALT cap workaround (PTE tax) elections [VERIFY: availability and mechanics vary by state]

## Workflow

1. **Map nexus exposure**
   - For each state, assess physical-presence nexus (offices, employees, inventory) and economic-nexus thresholds (revenue or transaction counts) [VERIFY: each state's current bright-line thresholds]
   - Determine whether PL 86-272 protection applies — confirm activities do not exceed solicitation of orders for tangible personal property; note that most states now exclude digital goods and services from protection [VERIFY: state-specific PL 86-272 guidance post-MTC revised statement]

2. **Determine filing methodology per state**
   - Identify whether each state requires or permits combined/unitary reporting; define the unitary group using predominant tests (contribution-or-dependency, flow-of-value)
   - Confirm water's-edge vs. worldwide election status and intercompany elimination requirements
   - For pass-through entities, check composite return or withholding obligations for nonresident owners [VERIFY: state composite filing rules]

3. **Calculate apportionment**
   - Apply each state's apportionment formula: single-sales-factor (majority of states), equally weighted three-factor, or modified weights [VERIFY: current formula per state]
   - Source sales using market-based sourcing (destination of benefit) or cost-of-performance, as required by each state
   - Evaluate throwback and throwout rules for sales into states where the entity is not taxable
   - Identify special-industry apportionment rules (financial institutions, airlines, trucking, broadcasters) if applicable

4. **Model tax liability and planning opportunities**
   - Compute estimated state tax liability under current structure and filing positions
   - Quantify exposure from unfiled states (back-year liability, penalties, interest) and compare VDA vs. quiet filing risk
   - Model planning alternatives: entity restructuring, elective PTE taxes to bypass the federal SALT cap, transfer-pricing adjustments, use of NOLs and credit carryforwards, and IRC §199A or state-level deductions
   - Assess state tax credits (R&D, job creation, investment) available to offset liability [VERIFY: credit availability, caps, and carryforward periods by state]

5. **Document positions and risk ratings**
   - Assign a risk tier (low / medium / high) to each material state tax position
   - For uncertain positions, evaluate whether ASC 740-10 (FIN 48) reserves are needed and at what confidence level
   - Prepare a state-by-state summary matrix showing nexus status, filing method, apportionment factors, estimated liability, and risk tier

## Output

- **Nexus matrix**: Table listing each state, nexus trigger (physical/economic/PL 86-272 protected), and filing requirement status
- **Apportionment schedules**: Factor detail (property, payroll, sales) and resulting apportionment percentages per state
- **Tax liability summary**: Estimated current-year liability by state, plus back-year exposure for any unfiled jurisdictions
- **Planning recommendations**: Ranked list of actionable strategies with estimated annual tax savings and implementation complexity
- **Risk assessment**: Position-by-position risk ratings with supporting authority citations and any [VERIFY] items requiring further state-specific research

## Quality Checks

- Confirm apportionment factors sum correctly and that sales are not double-counted or omitted across states
- Verify that throwback/throwout adjustments are applied only in states that impose them and only for sales into non-nexus states
- Cross-check that combined group inclusions are consistent with each state's unitary definition
- Ensure PL 86-272 reliance is not claimed for service revenue or digital goods in states that have adopted the MTC revised position
- Validate that all nexus thresholds reference current-year statutes or regulations — mark any outdated figures with [VERIFY]
- Confirm that estimated liabilities reconcile to supporting apportionment schedules and rate tables
