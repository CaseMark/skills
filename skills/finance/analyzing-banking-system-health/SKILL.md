---
name: analyzing-banking-system-health
language: en
description: Structures banking system assessment with capital adequacy, asset quality, and systemic risk evaluation. Use when analyzing banking systems, assessing financial stability, or evaluating systemic risk.
tags:
  - analysis
  - economic-analysis
  - risk
  - valuation
metadata:
  author: casemark
  practice_areas:
    - Economic Research
    - Macroeconomics
    - Policy Analysis
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Banking System Health

Structures banking system assessment with capital adequacy, asset quality, and systemic risk evaluation.

## When To Use

- Evaluating a country's or region's banking sector stability for policy research or investment analysis
- Assessing systemic risk buildup across a group of financial institutions
- Benchmarking individual bank health metrics against sector-wide or peer-group standards
- Reviewing banking system resilience in the context of stress scenarios, macro shocks, or contagion risk
- Preparing financial stability reports or macroprudential policy briefs

## Inputs To Gather

- **Bank-level financial data**: Balance sheets, income statements, and regulatory filings for institutions in scope (call reports, FR Y-9C, pillar 3 disclosures, or local equivalents) [VERIFY jurisdiction-specific filing requirements]
- **Regulatory capital ratios**: CET1, Tier 1, Total Capital ratios, leverage ratios, and supplementary leverage ratios where applicable
- **Asset quality metrics**: Non-performing loan (NPL) ratios, loan-loss provisions, charge-off rates, and coverage ratios
- **Liquidity indicators**: Liquidity Coverage Ratio (LCR), Net Stable Funding Ratio (NSFR), loan-to-deposit ratios
- **Market and macro data**: Sovereign spreads, interbank lending rates, credit default swap spreads on major banks, yield curve shape, GDP growth, unemployment, and inflation trends
- **Supervisory and stress test results**: Central bank or regulator-published stress test outcomes (e.g., Fed DFAST/CCAR, EBA stress tests) [VERIFY which stress test framework applies]
- **Structural context**: Number and concentration of institutions, deposit insurance framework, resolution regime, government ownership stakes

## Workflow

1. **Define scope and time horizon**
   - Specify the banking system (national, regional, or a peer group of institutions)
   - Set the assessment date range and any forward-looking horizon
   - Identify the regulatory framework governing the system (Basel III/IV implementation status, local capital rules) [VERIFY local regulatory standards]

2. **Assess capital adequacy**
   - Calculate aggregate and distribution-based CET1, Tier 1, and Total Capital ratios across institutions
   - Compare against minimum regulatory thresholds and buffers (capital conservation buffer, countercyclical buffer, G-SIB/D-SIB surcharges) [VERIFY applicable buffer levels]
   - Identify institutions operating near minimum thresholds or showing deteriorating capital trends
   - Evaluate quality of capital: proportion of CET1 vs. AT1 instruments, deferred tax asset reliance, goodwill/intangible deductions

3. **Evaluate asset quality**
   - Aggregate NPL ratios by loan category (commercial, consumer, mortgage, CRE)
   - Assess loan-loss reserve adequacy: coverage ratio (provisions / NPLs), trend in net charge-offs
   - Identify sector or geographic concentrations in loan books that introduce correlated default risk
   - Flag forbearance or restructured loan volumes that may mask true asset deterioration

4. **Analyze liquidity and funding structure**
   - Review system-wide LCR and NSFR compliance
   - Evaluate funding mix: reliance on wholesale funding vs. stable retail deposits
   - Check for maturity mismatches and rollover risk in wholesale markets
   - Monitor interbank market conditions — spreads, volumes, and counterparty credit concerns

5. **Measure profitability and earnings resilience**
   - Calculate return on assets (ROA), return on equity (ROE), and net interest margin (NIM) across the system
   - Assess cost-to-income ratios and operating efficiency trends
   - Evaluate earnings capacity to absorb credit losses (pre-provision net revenue relative to projected losses)

6. **Assess systemic risk indicators**
   - Compute concentration metrics: share of total assets held by top 3–5 institutions (Herfindahl-Hirschman Index)
   - Map interbank exposures and counterparty networks to identify contagion channels
   - Review CDS spreads and equity market signals for distress pricing
   - Evaluate sovereign-bank nexus: bank holdings of domestic sovereign debt, government guarantees, and implicit backstop expectations
   - Consider cross-border exposures and foreign-currency lending vulnerabilities

7. **Stress-test sensitivity analysis**
   - Apply scenario-based shocks: interest rate shifts, GDP contraction, asset price declines, funding freezes
   - Estimate capital depletion under adverse scenarios and identify institutions that breach minimum thresholds
   - Assess second-round effects — fire-sale dynamics, credit contraction feedback loops

8. **Synthesize findings and assign risk rating**
   - Summarize each pillar (capital, asset quality, liquidity, earnings, systemic risk) with a qualitative rating (strong / adequate / weak)
   - Highlight the 2–3 most material vulnerabilities and their transmission mechanisms
   - Provide an overall banking system health assessment with directional outlook (improving / stable / deteriorating)

## Output

Produce a structured **Banking System Health Assessment Report** containing:

- **Executive summary**: Overall health rating, key vulnerabilities, and outlook in 3–5 sentences
- **Capital adequacy section**: Aggregate ratios, distribution, buffer analysis, and trend
- **Asset quality section**: NPL rates, coverage, concentration risks, forbearance flags
- **Liquidity and funding section**: LCR/NSFR compliance, funding mix, maturity profile
- **Profitability section**: ROA, ROE, NIM trends, loss-absorption capacity
- **Systemic risk section**: Concentration, interconnectedness, sovereign-bank nexus, contagion assessment
- **Stress scenario results**: Capital impact under adverse scenarios, institutions at risk
- **Risk matrix**: Summary table mapping each pillar to rating and key concern
- **Recommendations**: Policy or portfolio actions warranted by findings
- **Limitations and data gaps**: Disclose missing data, stale inputs, or analytical constraints

## Quality Checks

- All capital ratios verified against source regulatory filings — not derived from secondary summaries
- NPL definitions used consistently (90-day past due vs. local regulatory definition) [VERIFY local NPL classification rules]
- Stress test assumptions are explicit, internally consistent, and disclosed
- Concentration analysis uses current-period data, not lagged proxies
- Sovereign-bank nexus assessment accounts for both direct holdings and indirect channels (guarantees, collateral eligibility)
- Forward-looking statements clearly distinguished from historical observations
- All [VERIFY] markers resolved or flagged for human review before finalization
- Cross-check aggregate figures against central bank financial stability reports or IMF FSAP assessments where available
