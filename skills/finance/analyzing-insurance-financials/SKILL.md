---
name: analyzing-insurance-financials
language: en
description: Structures insurance company financial analysis with combined ratio, reserve adequacy, and capital metrics. Use when analyzing insurance financials, evaluating combined ratios, or assessing reserve strength.
tags:
  - analysis
  - insurance
metadata:
  author: casemark
  practice_areas:
    - Insurance
    - Actuarial Science
    - Reinsurance
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Insurance Financials

Structures insurance company financial analysis around underwriting profitability, reserve adequacy, investment performance, and capital strength to produce actionable assessments of insurer financial health.

## When To Use

- Evaluating an insurer's underwriting discipline via combined ratio decomposition
- Assessing loss reserve adequacy for due diligence, M&A, or regulatory review
- Benchmarking capital and solvency metrics against rating agency thresholds
- Analyzing reinsurance program effectiveness and net retention exposure
- Reviewing statutory filings (Annual Statement, Quarterly Statement) or GAAP financials for trend analysis
- Supporting investment decisions in insurance equities, surplus notes, or ILS

## Inputs To Gather

- **Financial statements**: Statutory Annual/Quarterly Statements (filed with NAIC), GAAP 10-K/10-Q, or IFRS 17 reports
- **Line-of-business detail**: Schedule P (loss development triangles), Schedule H (accident & health), or equivalent breakdowns
- **Investment portfolio**: Schedule D (bonds), Schedule BA (other invested assets), asset quality distribution
- **Reinsurance structure**: Schedule F (ceded reinsurance), Schedule S (reinsurance assumed), treaty summaries
- **Rating agency reports**: AM Best, S&P, Moody's, or Fitch insurer financial strength ratings and rationale
- **Peer/industry benchmarks**: NAIC industry aggregates, SNL/S&P Capital IQ comparables, or relevant cohort data
- **Time horizon**: Minimum 3-5 years of historical data for trend analysis; 10 years preferred for reserve development

## Workflow

1. **Classify the insurer** — Identify line mix (P&C vs. life/health vs. multiline), domicile, and regulatory regime. Note whether analysis uses statutory accounting (SAP), GAAP, or IFRS 17. [VERIFY] applicable accounting framework and jurisdictional requirements.

2. **Decompose the combined ratio**
   - Calculate loss ratio (net incurred losses / net earned premiums) by accident year and calendar year
   - Calculate expense ratio (underwriting expenses / net written premiums for SAP; / net earned premiums for GAAP trade ratio)
   - Break out loss adjustment expense (LAE) into defense & cost containment (DCC) vs. adjusting & other (A&O)
   - Compute combined ratio = loss ratio + expense ratio; flag any result above 100% (underwriting loss)
   - Analyze trends over 3-5 years; identify deteriorating or improving lines of business

3. **Evaluate reserve adequacy**
   - Review Schedule P loss development triangles (paid and incurred) for the most recent 10 accident years
   - Calculate development factors and compare to industry benchmarks
   - Identify adverse or favorable prior-year reserve development and quantify impact on calendar-year results
   - Assess carried reserves vs. actuarial central estimate — note any margin (redundancy) or deficiency
   - Flag lines with long-tail exposure (e.g., general liability, workers' comp, professional liability) for deeper review

4. **Analyze investment portfolio and yield**
   - Compute net investment income yield (NII / average invested assets)
   - Review asset allocation: percentage in investment-grade bonds, equities, alternatives, real estate, cash
   - Assess credit quality distribution (NAIC designation 1-6 for statutory; rating agency equivalents)
   - Calculate total return on invested assets including realized/unrealized gains
   - Evaluate asset-liability duration matching — flag significant mismatches

5. **Assess capital adequacy and leverage**
   - Calculate net premiums written to policyholders' surplus (NPW/PHS) — flag if >3:1 for P&C [VERIFY] threshold by line
   - Review Risk-Based Capital (RBC) ratio (Total Adjusted Capital / Authorized Control Level) — regulatory minimum is 200% company action level
   - Compute net leverage ratio (net liabilities / PHS) and gross leverage including reinsurance recoverables
   - Analyze quality of surplus: note any surplus notes, goodwill, DTA, or non-admitted assets reducing adjusted surplus
   - Compare to AM Best Capital Adequacy Ratio (BCAR) thresholds for target rating level

6. **Evaluate reinsurance program**
   - Assess ceded ratio (ceded premiums / gross written premiums) — high cession may indicate capital constraints
   - Review reinsurer credit quality and concentration risk (Schedule F penalties for unauthorized/undercollateralized reinsurers)
   - Analyze net retention relative to surplus for catastrophe and per-risk exposures
   - Identify any commutation activity or material disputes in reinsurance recoverables

7. **Benchmark and synthesize**
   - Compare all key metrics to peer group and industry medians
   - Identify outlier metrics (positive or negative) and explain drivers
   - Assign qualitative assessment of financial strength: strong / adequate / marginal / weak
   - Highlight key risks: reserve uncertainty, catastrophe exposure, investment concentration, reinsurance dependency

## Output

Structure the analysis report with the following sections:

- **Executive Summary**: One-paragraph financial health assessment with key metrics and conclusion
- **Company Profile**: Line mix, domicile, size (DPW, total assets, surplus), rating history
- **Underwriting Analysis**: Combined ratio decomposition with 3-5 year trend tables by line
- **Reserve Analysis**: Development triangle summary, prior-year development history, adequacy assessment
- **Investment Analysis**: Portfolio composition, yield analysis, credit quality, duration
- **Capital & Leverage**: RBC ratio, NPW/PHS, net leverage, surplus quality, BCAR positioning
- **Reinsurance Review**: Ceded ratio, reinsurer quality, net retention adequacy
- **Peer Comparison**: Side-by-side table of key metrics vs. selected comparables
- **Key Risks & Considerations**: Bullet list of material risk factors with severity indication
- **Appendix**: Supporting schedules, data sources, glossary of metrics

## Quality Checks

- Confirm all ratios use consistent numerator/denominator definitions (SAP vs. GAAP vs. trade basis) — do not mix frameworks
- Verify that loss development triangles foot to Schedule P Part 1 summary and that incurred = paid + case reserves + IBNR
- Cross-check that NPW reconciles across the income statement, balance sheet, and Schedule T (state page)
- Ensure RBC ratio uses the correct formula for entity type (P&C vs. life vs. health) [VERIFY]
- Validate that reinsurance recoverables on the balance sheet tie to Schedule F detail
- Confirm peer benchmarks are from the same reporting period and use the same accounting basis
- Flag any metric where data was estimated, interpolated, or unavailable with [VERIFY]
- Check that all trend commentary is supported by the underlying numerical data — no unsupported qualitative claims
