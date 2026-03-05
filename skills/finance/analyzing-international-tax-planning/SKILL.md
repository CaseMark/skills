---
name: analyzing-international-tax-planning
description: Evaluates international tax structures with BEPS considerations, treaty analysis, and repatriation planning. Use when planning international tax, analyzing tax treaties, or structuring cross-border operations.
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
# Analyzing International Tax Planning

Evaluates international tax structures with BEPS considerations, treaty analysis, and repatriation planning.

## When To Use

- Assessing cross-border holding, financing, or IP structures for tax efficiency
- Reviewing treaty networks for withholding tax optimization on dividends, interest, or royalties
- Evaluating BEPS exposure under OECD Pillar One and Pillar Two (Global Minimum Tax)
- Planning repatriation of offshore earnings (dividends, loan repayments, service fees, liquidations)
- Structuring inbound or outbound investment into new jurisdictions
- Responding to CbCR (Country-by-Country Reporting) findings or tax authority inquiries on transfer pricing

## Inputs To Gather

- **Entity structure chart** — legal entities, jurisdictions, ownership percentages, and functional roles
- **Intercompany transaction map** — loans, royalties, management fees, cost-sharing arrangements with amounts
- **Treaty matrix** — applicable bilateral tax treaties for each corridor (source → residence)
- **Financial data** — revenue, EBITDA, and effective tax rates per entity; consolidated group revenue
- **Transfer pricing documentation** — master file, local files, benchmarking studies
- **Regulatory context** — any pending tax audits, rulings, APAs, or MAP proceedings
- **Repatriation targets** — cash needs by jurisdiction, timing, and intended use of repatriated funds
- **Pillar Two data** — GloBE information return data, jurisdictional ETR calculations, top-up tax exposure

## Workflow

1. **Map the structure** — Diagram entity chain from ultimate parent to operating subsidiaries. Identify conduit entities, hybrid entities, and stateless income streams. Flag entities with no substantial economic activity (employees, office space, decision-making).

2. **Analyze treaty positions** — For each cross-border payment corridor, identify the applicable treaty, withholding rates, and limitation-on-benefits (LOB) or principal purpose test (PPT) exposure. Note treaties that lack coverage or where treaty shopping risk exists. [VERIFY] specific treaty article numbers and rates, as treaties are frequently renegotiated.

3. **Assess BEPS and Pillar Two exposure** — Calculate jurisdictional effective tax rates under GloBE rules. Identify jurisdictions below the 15% minimum rate. Evaluate whether Qualified Domestic Minimum Top-up Taxes (QDMTT) apply. Flag substance-based income exclusions (payroll and tangible asset carve-outs). [VERIFY] local Pillar Two implementation status, as adoption timelines vary by jurisdiction.

4. **Evaluate transfer pricing alignment** — Review intercompany pricing against arm's-length standard. Identify high-risk transactions: management fees to low-tax jurisdictions, royalty payments to IP holding companies, thin capitalization arrangements. Assess whether DEMPE functions (Development, Enhancement, Maintenance, Protection, Exploitation) align with where profits are booked.

5. **Model repatriation pathways** — Compare options for moving cash to parent: dividends (participation exemption availability), loan repayments, service fees, return of capital, or liquidation. Calculate total tax cost per pathway including withholding tax, CFC inclusion risk, and foreign tax credit utilization. Identify trapped cash situations.

6. **Identify risks and restructuring options** — Summarize anti-avoidance exposure (GAAR, CFC rules, anti-hybrid rules under ATAD/BEPS Action 2). Propose restructuring alternatives with estimated tax savings and implementation complexity. Rank options by risk-adjusted benefit.

## Output

Structure the analysis report with these sections:

- **Executive Summary** — Key findings, total international tax cost, top 3 risks, and recommended actions
- **Structure Overview** — Entity chart with jurisdictional ETRs and functional characterizations
- **Treaty Analysis Table** — Payment corridors, treaty rates, LOB/PPT status, and net withholding costs
- **Pillar Two Impact Assessment** — Jurisdictional ETR schedule, top-up tax estimates, QDMTT applicability
- **Transfer Pricing Risk Matrix** — Transactions ranked by risk (high/medium/low) with remediation notes
- **Repatriation Analysis** — Side-by-side comparison of pathways with total tax cost modeling
- **Recommendations** — Prioritized actions with estimated savings, implementation steps, and timeline
- **Appendix** — Assumptions log, data sources, and items marked [VERIFY]

## Quality Checks

- Confirm all intercompany flows are accounted for in both directions (payment and receipt)
- Verify that treaty rate assumptions reflect the most recent protocol or amendment [VERIFY]
- Ensure Pillar Two calculations use the correct GloBE accounting standard (not local GAAP unless QDMTT requires it)
- Check that CFC rules in the parent jurisdiction are addressed for each low-tax subsidiary
- Validate that substance requirements are assessed for every entity claiming treaty benefits or reduced rates
- Confirm repatriation modeling accounts for foreign tax credit limitations and ordering rules
- Flag any jurisdiction where anti-hybrid mismatch rules (ATAD II or equivalent) could deny deductions or impose inclusion
- Mark all jurisdiction-specific statutory rates, thresholds, and effective dates with [VERIFY]
