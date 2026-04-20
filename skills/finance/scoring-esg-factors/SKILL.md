---
name: scoring-esg-factors
language: en
description: Structures ESG scoring methodology with environmental, social, and governance pillar assessment. Use when scoring ESG, evaluating sustainability, or building ESG frameworks.
tags:
  - assessment
  - sustainable-finance
  - esg
metadata:
  author: casemark
  practice_areas:
    - ESG
    - Impact Investing
    - Sustainable Finance
  document_types:
    - Score Card
  skill_modes:
    - Assessment
    - Calculation
---
# Scoring ESG Factors

Structures ESG scoring methodology across environmental, social, and governance pillars, producing a weighted composite score with pillar-level breakdowns suitable for investment screening, portfolio analytics, or sustainability reporting.

## When To Use

- Scoring a company or asset against ESG criteria for investment due diligence
- Building or calibrating an ESG scoring framework for a fund or portfolio
- Comparing ESG performance across peer companies or sectors
- Preparing ESG score cards for LP reporting, impact disclosures, or regulatory filings
- Evaluating alignment with frameworks such as SASB, GRI, TCFD, UN PRI, or EU SFDR

## Inputs To Gather

- **Entity identifier**: Company name, ticker, ISIN, or fund/asset name
- **Sector and geography**: GICS/ICB sector classification and domicile jurisdiction
- **Data sources**: Sustainability reports, CDP disclosures, proxy statements, third-party ESG data feeds (MSCI, Sustainalytics, ISS, Bloomberg)
- **Framework selection**: Which standard(s) to align scores with (SASB materiality map, GRI indicators, TCFD pillars, EU Taxonomy)
- **Weighting scheme**: Equal-weight across pillars, materiality-adjusted, or client-specified weights
- **Scoring scale**: Numeric range (e.g., 0–100), letter grades (AAA–CCC), or quintile buckets
- **Reporting period**: Fiscal year or trailing 12-month window for data

## Workflow

1. **Define scope and framework alignment**
   - Confirm which ESG framework(s) govern the scoring methodology
   - Select material indicators per sector using the SASB materiality map or equivalent [VERIFY sector-specific materiality indicators against the latest SASB standards]
   - Establish the scoring scale, weighting scheme, and any override rules

2. **Score the Environmental pillar**
   - Assess: GHG emissions (Scope 1, 2, 3), carbon intensity, science-based targets, energy mix, water usage, waste/circularity, biodiversity impact
   - Score each indicator on the defined scale; note data gaps
   - Flag any self-reported metrics lacking third-party assurance

3. **Score the Social pillar**
   - Assess: workforce diversity and inclusion, employee health & safety (TRIR/DART), labor practices, supply chain standards, community impact, data privacy, product safety
   - Evaluate controversies: strikes, discrimination lawsuits, product recalls
   - Apply penalties or adjustments for unresolved material controversies

4. **Score the Governance pillar**
   - Assess: board independence and diversity, executive compensation alignment, audit committee effectiveness, shareholder rights, anti-corruption policies, related-party transactions, ESG oversight at board level
   - Review proxy voting history and any governance-related shareholder proposals
   - Check for regulatory enforcement actions or restatements

5. **Calculate composite score**
   - Apply pillar weights (e.g., E: 40%, S: 30%, G: 30% — or materiality-adjusted)
   - Compute weighted composite score
   - Assign overall rating on chosen scale
   - Run sensitivity analysis: show how composite changes if pillar weights shift ±10%

6. **Benchmark and contextualize**
   - Compare entity score against sector peers and index median
   - Identify top-quartile and bottom-quartile indicators driving the score
   - Highlight momentum (improving/declining trends over 2–3 reporting periods)

## Output

Produce a structured ESG Score Card containing:

- **Summary table**: Entity name, sector, reporting period, composite score, pillar scores (E / S / G)
- **Pillar detail sections**: Each pillar with indicator-level scores, data sources, and flags
- **Materiality heat map**: Which indicators carry the most weight for this sector
- **Controversy overlay**: Material controversies with severity rating and score impact
- **Peer comparison**: Composite and pillar scores vs. sector peer group (table or rank)
- **Sensitivity analysis**: Composite score under alternative weighting scenarios
- **Data quality notes**: Indicators with missing data, self-reported only, or stale data marked [VERIFY]
- **Methodology appendix**: Framework version, weighting rationale, scoring scale definitions

## Quality Checks

- Every indicator score traces to a named data source and reporting period — no unsourced scores
- Pillar weights sum to 100%; composite math is replicable from pillar scores
- Sector-specific material indicators are included; immaterial indicators for the sector are excluded or down-weighted
- Controversies are cross-referenced against at least two sources (news, regulatory filings, NGO reports)
- Scores distinguish between "zero/low risk" and "no data available" — missing data is never treated as a positive signal
- [VERIFY] Alignment claims against specific frameworks (SFDR Article 8/9, EU Taxonomy eligibility) are confirmed against current regulatory definitions
- Sensitivity analysis is included so users understand score stability under different assumptions
