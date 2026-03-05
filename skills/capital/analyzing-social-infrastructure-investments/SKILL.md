---
name: analyzing-social-infrastructure-investments
description: Evaluates social infrastructure including healthcare, education, and government facilities with availability-based revenue structures. Use when analyzing social infrastructure, evaluating availability payments, or assessing government-backed projects.
tags:
  - analysis
  - infrastructure-and-project-finance
metadata:
  author: casemark
  practice_areas:
    - Project Finance
    - Infrastructure Investment
    - PPP
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Social Infrastructure Investments

Evaluates social infrastructure including healthcare, education, and government facilities with availability-based revenue structures.

## When To Use

- Assessing a PPP/P3 project involving hospitals, schools, courthouses, social housing, or government office buildings
- Evaluating availability-based payment structures where revenue depends on facility readiness rather than user demand
- Comparing social infrastructure assets across a portfolio or fund allocation
- Conducting due diligence on concession agreements with public-sector counterparties
- Reviewing lifecycle cost assumptions and handback condition obligations

## Inputs To Gather

- **Project agreement / concession contract** — payment mechanism, term, performance standards, deduction regime
- **Availability payment schedule** — base payment, indexation methodology (CPI or custom), step-up/step-down triggers
- **Deduction matrix** — categories (safety, availability, performance), severity tiers, rectification periods, cure caps
- **Counterparty credit profile** — sovereign or sub-sovereign rating, budgetary appropriation mechanism, payment history [VERIFY jurisdiction-specific appropriation risk]
- **Capital structure** — senior debt terms, debt service reserve, equity IRR targets, distribution lock-up triggers
- **Lifecycle/renewal model** — major maintenance reserve, replacement schedule, handback condition specification
- **Insurance program** — required coverages, deductibles, uninsurable risk allocation
- **Construction status** — if pre-completion: EPC contract type (fixed-price/GMP), LD regime, completion test criteria

## Workflow

1. **Classify the asset and payment mechanism**
   - Identify sub-sector (healthcare, education, judicial, social housing, government accommodation)
   - Confirm revenue is availability-based (not demand/volume-based); flag any hybrid elements (e.g., ancillary revenue, parking)
   - Map the payment mechanism: base availability payment + service payments + lifecycle components

2. **Analyze the deduction regime**
   - Review deduction categories and weighting — availability deductions vs. performance deductions
   - Assess severity of penalty curve: linear vs. exponential deductions, termination thresholds
   - Model historical deduction experience if operational; estimate deduction exposure if greenfield
   - Identify rectification periods and whether they are commercially reasonable

3. **Evaluate counterparty credit risk**
   - Determine whether payments are a direct government obligation, appropriation-dependent, or backed by a special-purpose vehicle [VERIFY: appropriation risk framework varies by jurisdiction]
   - Review sovereign/sub-sovereign credit rating and fiscal capacity
   - Assess payment track record on comparable PPP contracts in the same jurisdiction
   - Flag any change-of-law or political risk provisions

4. **Model cash flows and returns**
   - Build or review base-case financial model with availability payment indexation
   - Stress-test: deduction scenarios (5%, 10%, 15% of base payment), inflation variance, interest rate sensitivity
   - Calculate equity IRR, cash-on-cash yield, and payback period under base and downside cases
   - Verify debt service coverage ratios (DSCR) against lock-up (typically 1.10x–1.15x) and default thresholds (typically 1.05x) [VERIFY: lender-specific covenants]

5. **Assess lifecycle and handback risk**
   - Review lifecycle cost model against independent technical advisor benchmarks
   - Evaluate adequacy of major maintenance reserve funding profile
   - Identify handback condition obligations and residual-life requirements
   - Flag any lifecycle scope gaps (e.g., technology refresh in healthcare facilities, HVAC in education)

6. **Review risk allocation**
   - Map key risks to responsible party: construction, commissioning, operations, lifecycle, force majeure, change in law
   - Assess whether FM contractor obligations are back-to-back with project company obligations
   - Identify retained risks and uncapped exposures
   - Evaluate termination compensation mechanics (voluntary, concessionaire default, authority default, force majeure)

7. **Benchmark and conclude**
   - Compare key metrics (equity IRR, DSCR, deduction headroom, lifecycle reserve adequacy) against comparable social infrastructure transactions
   - Assign overall risk rating or investment recommendation with supporting rationale

## Output

Produce a structured analysis report containing:

- **Executive summary** — asset type, jurisdiction, concession term, payment mechanism, headline return metrics, and investment thesis
- **Payment mechanism analysis** — availability payment structure, indexation, deduction exposure quantification
- **Counterparty assessment** — credit quality, appropriation risk, payment history
- **Financial summary** — base-case and downside IRR, DSCR profile, distribution forecast, sensitivity tables
- **Lifecycle risk assessment** — reserve adequacy, key renewal items, handback gap analysis
- **Risk matrix** — allocated vs. retained risks with materiality ranking
- **Recommendation** — proceed / proceed with conditions / decline, with stated assumptions

## Quality Checks

- Confirm availability payment indexation matches the contractual formula exactly — errors here cascade through the entire model
- Verify deduction model reflects the actual penalty matrix, not a simplified proxy
- Cross-check DSCR calculations against lender model or term sheet covenants
- Ensure lifecycle cost estimates are supported by an independent technical report, not solely sponsor assumptions
- Validate that termination compensation calculations cover both debt and equity recovery under each termination scenario
- Confirm counterparty credit assessment references current ratings and fiscal data [VERIFY: rating agency and date]
- Flag any assumptions about refinancing, contract extensions, or supplementary revenue that are not contractually committed
