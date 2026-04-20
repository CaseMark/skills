---
name: managing-esg-data-quality
language: en
description: Structures ESG data quality assessment with source comparison, estimation methodology, and disclosure gaps. Use when evaluating ESG data, comparing data providers, or assessing data quality.
tags:
  - management
  - sustainable-finance
  - esg
metadata:
  author: casemark
  practice_areas:
    - ESG
    - Impact Investing
    - Sustainable Finance
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing ESG Data Quality

## When To Use

- Evaluating the reliability of ESG data from company disclosures, third-party providers (MSCI, Sustainalytics, Bloomberg, ISS), or internal collection systems
- Comparing ESG scores or metrics across multiple data providers to identify divergence and its root causes
- Assessing disclosure gaps ahead of regulatory filings (CSRD, SEC climate rules, ISSB/IFRS S1-S2) or investor reporting
- Auditing estimation methodologies used to fill missing Scope 1/2/3 emissions, water usage, or social metrics
- Building or improving an ESG data governance framework for portfolio-level or enterprise-level reporting

## Inputs To Gather

- **Data sources under review**: Identify each provider, self-reported dataset, or survey instrument; note vintage year and update frequency
- **Metric scope**: List specific KPIs (e.g., GHG Scope 1-3 in tCO2e, water withdrawal in m3, board diversity %, LTIR)
- **Reporting framework(s)**: Which standards apply — GRI, SASB, ISSB, TCFD, EU Taxonomy, CSRD/ESRS, CDP questionnaire [VERIFY applicable framework versions]
- **Coverage universe**: Number of entities, asset classes, or facilities; geographic distribution
- **Known gaps or disputes**: Any metrics previously flagged by auditors, regulators, or data consumers

## Workflow

1. **Map the data landscape**
   - Catalog every ESG metric required by the target framework(s)
   - For each metric, record: source, collection method (reported / estimated / modeled), refresh cadence, and coverage rate (% of universe with actual data)
   - Flag metrics sourced from estimates vs. verified disclosures

2. **Score data quality per metric**
   - Apply a consistent rubric across five dimensions:
     - **Completeness**: % of entities with non-null values
     - **Accuracy**: Cross-check against primary filings (annual reports, CDP responses, EPA GHGRP) where available
     - **Timeliness**: Lag between reporting period end and data availability
     - **Consistency**: Year-over-year variance analysis; flag anomalies exceeding sector norms
     - **Comparability**: Methodological alignment across providers (e.g., whether Scope 3 categories included differ)
   - Assign a rating (High / Adequate / Low / Unavailable) to each metric-dimension pair

3. **Analyze provider divergence**
   - Where multiple providers cover the same metric, compute divergence (absolute difference, rank correlation)
   - Identify root causes: differing sector classifications (GICS vs. BICS vs. proprietary), estimation model assumptions, inclusion/exclusion of subsidiaries, treatment of avoided emissions
   - Document which provider methodology best aligns with the selected reporting framework

4. **Assess estimation methodology**
   - For any estimated metric, document the model type (sector-average, revenue-intensity, physical-activity-based, econometric)
   - Evaluate estimation uncertainty: sample size, proxy quality, geographic representativeness
   - Note whether the estimation approach is accepted under the target standard [VERIFY — e.g., GHG Protocol permits spend-based Scope 3 estimation but CSRD/ESRS may require activity-based data for certain categories]

5. **Identify disclosure gaps and remediation actions**
   - List metrics with Low or Unavailable quality ratings
   - For each gap, recommend a remediation path: direct engagement with portfolio companies, alternative data sources (satellite, IoT, supply-chain platforms), or improved estimation with documented uncertainty bands
   - Prioritize gaps by materiality (financial impact, regulatory requirement, stakeholder sensitivity)

6. **Compile the data quality assessment report**
   - Structure output per the format below
   - Include a summary heatmap or matrix showing quality ratings across metrics and dimensions

## Output

Structure the deliverable as follows:

- **Executive summary**: Key findings, overall data quality posture, top 3-5 action items
- **Data quality matrix**: Metric x Dimension grid with ratings (High / Adequate / Low / Unavailable)
- **Provider comparison table**: Side-by-side methodology notes, coverage rates, and divergence metrics for each provider evaluated
- **Estimation methodology inventory**: For each estimated metric — model type, key assumptions, uncertainty range, framework acceptance status
- **Gap register**: Metric, current quality rating, materiality tier, recommended remediation, estimated timeline, responsible party
- **Appendix**: Raw data samples, methodology references, glossary of terms

## Quality Checks

- Every metric rated Low or Unavailable has a corresponding entry in the gap register with a remediation action
- Provider divergence analysis covers at least the top 10 most material metrics, not just those with obvious discrepancies
- Estimation methodologies are evaluated against the specific framework version in scope — do not assume GHG Protocol defaults apply to all frameworks [VERIFY]
- Timeliness assessment accounts for regulatory filing deadlines (e.g., CSRD phased timelines, SEC compliance dates) [VERIFY current effective dates]
- No estimated value is presented without an explicit confidence qualifier or uncertainty range
- Cross-check that Scope 3 category boundaries are consistent across all sources compared; mismatched category inclusion is the most common source of false divergence
- Flag any metric where the provider's coverage rate falls below 60% of the target universe — partial coverage can distort portfolio-level aggregations
