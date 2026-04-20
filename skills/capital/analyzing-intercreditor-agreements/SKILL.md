---
name: analyzing-intercreditor-agreements
language: en
description: Evaluates intercreditor and subordination provisions with lien priority, payment waterfall, and enforcement rights analysis. Use when analyzing intercreditor terms, evaluating subordination structures, or assessing lender priority.
tags:
  - analysis
  - credit-and-institutional-lending
  - credit
metadata:
  author: casemark
  practice_areas:
    - Credit Markets
    - Leveraged Lending
    - Direct Lending
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Intercreditor Agreements

Evaluates intercreditor and subordination provisions with lien priority, payment waterfall, and enforcement rights analysis.

## When To Use

- Reviewing an intercreditor agreement (ICA) between first-lien and second-lien lenders in a leveraged financing
- Evaluating subordination mechanics in a unitranche with an Agreement Among Lenders (AAL)
- Assessing enforcement standstill periods, purchase option rights, or turnover obligations before a new deal closes
- Comparing intercreditor terms against market standards for a credit committee memo
- Analyzing split-collateral or cross-collateral structures in multi-tranche facilities

## Inputs To Gather

- **Intercreditor agreement or AAL** — full executed document (including all exhibits and schedules)
- **Related credit agreements** — first-lien and second-lien (or senior/mezzanine) facility agreements to cross-reference definitions and covenants
- **Collateral descriptions** — security agreements, pledge agreements, and any collateral allocation schedules
- **Structural diagram** (if available) — organizational chart showing borrower/guarantor entities and lien attachment points
- **Deal context** — transaction type (LBO, recap, add-on), approximate leverage levels, and whether the ICA is being negotiated or reviewed post-execution

## Workflow

1. **Classify the ICA structure**
   - Determine agreement type: first-lien/second-lien, senior/mezzanine, unitranche AAL, or split-collateral
   - Identify the controlling creditor class and the agent hierarchy
   - Note governing law and any jurisdiction-specific enforcement rules [VERIFY]

2. **Map lien priority and collateral allocation**
   - Confirm which asset categories are shared collateral vs. exclusive collateral for each tranche
   - Review lien subordination vs. payment subordination distinctions
   - Check for carve-outs (e.g., second-lien permitted to hold liens on specific asset classes)
   - Flag any "equal and ratable" provisions or springing lien mechanics

3. **Analyze the payment waterfall**
   - Trace the distribution hierarchy: fees → first-lien interest → first-lien principal → second-lien interest → second-lien principal → residual
   - Identify permitted payments to junior creditors (scheduled interest, excess cash flow sweeps, voluntary prepayments)
   - Locate any payment blockage triggers and their duration caps [VERIFY — typical market range is 179–365 days]
   - Assess whether the waterfall resets after a blockage period expires

4. **Evaluate enforcement and standstill provisions**
   - Determine the standstill period length during which junior creditors cannot exercise remedies [VERIFY — market standard varies by deal type, commonly 90–180 days]
   - Identify standstill termination triggers (acceleration by senior, insolvency filing, senior inaction for a specified period)
   - Review whether junior creditors can challenge senior enforcement actions or participate in collateral sales
   - Check for "X-clause" provisions allowing junior lenders to take enforcement action after standstill expiry even if senior has not acted

5. **Review purchase option and right of first refusal**
   - Confirm whether junior creditors have the right to purchase senior debt at par (or at a discount) upon an enforcement trigger
   - Note the exercise window and procedural requirements (notice periods, deposit obligations)
   - Assess whether the purchase option survives bankruptcy filing [VERIFY]

6. **Assess bankruptcy and insolvency protections**
   - Review DIP financing consent rights — can junior creditors object to senior-proposed DIP?
   - Evaluate adequate protection waiver scope (whether junior creditors waive rights to adequate protection on shared collateral)
   - Check voting and plan support restrictions — are junior creditors prohibited from supporting a plan that is not accepted by senior?
   - Identify "toggling" provisions that change priority upon insolvency filing

7. **Flag non-standard or borrower-favorable terms**
   - Incremental debt accommodation — does the ICA automatically extend to cover future incremental tranches?
   - Release provisions — can collateral be released without junior creditor consent in connection with permitted asset sales?
   - "Serta-style" uptier protections or anti-priming language [VERIFY — market adoption is evolving post-2020 litigation]
   - Amendment provisions — what voting thresholds are required to modify waterfall or lien priority terms?

## Output

Produce a structured analysis report containing:

- **Executive Summary** — one-paragraph assessment of the ICA's key risk characteristics and whether terms are market-standard or borrower/sponsor-favorable
- **Structure Overview** — table identifying each creditor tranche, agent, collateral pool, and priority position
- **Waterfall Diagram** — step-by-step payment distribution sequence with blockage triggers noted
- **Enforcement Rights Matrix** — standstill periods, permitted remedies by tranche, and termination triggers in tabular format
- **Key Risk Flags** — numbered list of provisions that deviate from market norms or create subordination risk
- **Recommendations** — specific negotiation points or protective provisions to request if the ICA is under negotiation

## Quality Checks

- Confirm every lien priority assertion is traceable to a specific section of the ICA — do not infer priority from deal summaries alone
- Verify that defined terms (Collateral, Obligations, Discharge) are pulled from the ICA itself, not assumed from the related credit agreement
- Cross-check payment waterfall terms against both the ICA and the underlying credit agreements for consistency
- Ensure standstill periods and blockage periods are stated with exact day counts, not approximations
- Mark any provision whose enforceability depends on state UCC law, bankruptcy code interpretation, or recent case law with [VERIFY]
- Confirm whether the analysis covers all amendments, supplements, and side letters to the ICA
