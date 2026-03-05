---
name: analyzing-esg-integration
description: Integrates ESG factors into investment analysis with scoring methodology and impact measurement. Use when implementing ESG integration, scoring ESG factors, or measuring sustainability impact.
tags:
  - analysis
  - asset-management
  - investment
  - esg
metadata:
  author: casemark
  practice_areas:
    - Portfolio Management
    - Asset Management
    - Wealth Management
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing ESG Integration

## When To Use

- Evaluating a portfolio or individual holding for environmental, social, and governance risk exposure
- Building or refining an ESG scoring methodology for an investment strategy
- Conducting due diligence on ESG claims made by fund managers or issuers
- Measuring portfolio-level sustainability impact against stated objectives (e.g., net-zero alignment, SDG contribution)
- Comparing ESG integration approaches across managers or mandates for asset-owner selection decisions

## Inputs To Gather

- **Investment universe or holdings list** — ticker/ISIN-level with sector, geography, and market cap
- **ESG data sources** — specify providers (e.g., MSCI, Sustainalytics, ISS, Bloomberg ESG, CDP) and vintages; note any proprietary or self-reported data
- **Framework alignment** — which standards apply: SASB materiality map, TCFD pillars, EU SFDR classification (Article 6/8/9), UN PRI integration expectations [VERIFY jurisdiction-specific disclosure regime]
- **Scoring parameters** — weighting scheme (equal-weight, materiality-adjusted, sector-relative), score scale, and handling of missing data (exclude, impute, penalize)
- **Benchmark and peer set** — ESG benchmark index (e.g., MSCI ESG Leaders, S&P Paris-Aligned) and relevant peer portfolios
- **Client or mandate constraints** — exclusion lists (controversial weapons, thermal coal thresholds, tobacco), minimum ESG score floors, impact KPIs

## Workflow

1. **Map material ESG factors to the investment universe**
   - Use the SASB materiality map (or equivalent) to identify the 3–5 most financially material E, S, and G factors per sector
   - For each holding, pull raw indicator data from the designated providers
   - Flag holdings with no coverage or stale data (>12 months) as [VERIFY]

2. **Normalize and score**
   - Convert raw indicators to a common scale (e.g., 0–10 or percentile rank within sector)
   - Apply the agreed weighting scheme — document the rationale for any materiality tilts
   - Calculate pillar scores (E, S, G) and a composite ESG score per holding
   - Handle controversies separately: overlay a controversy adjustment that can downgrade scores regardless of pillar performance

3. **Aggregate to portfolio level**
   - Compute weighted-average ESG scores using portfolio weights
   - Generate distribution analysis: histogram of holding-level scores, identification of bottom-quintile laggards
   - Compare portfolio scores against the benchmark and peer set on each pillar

4. **Assess impact metrics**
   - Map holdings to impact KPIs where applicable (carbon intensity in tCO2e/$M revenue, board gender diversity %, water withdrawal intensity)
   - Calculate portfolio-level impact metrics and year-over-year trajectory
   - For climate-specific mandates, run implied temperature rise (ITR) or Paris-alignment analysis [VERIFY methodology: SBTi, TPI, or proprietary]

5. **Identify risks and engagement opportunities**
   - Flag holdings with high ESG momentum (improving trend) vs. deteriorating profiles
   - Highlight governance red flags: dual-class structures, related-party transactions, auditor qualifications
   - Recommend engagement priorities for holdings where score improvement is achievable and material

6. **Document and deliver**
   - Compile the ESG integration report with executive summary, methodology appendix, and data-source inventory
   - Include limitations: data gaps, provider disagreements, and sectors with weak ESG disclosure

## Output

The deliverable is an **ESG Integration Analysis Report** containing:

- **Executive summary** — portfolio ESG positioning vs. benchmark, key risks, and top engagement targets
- **Scoring methodology** — factor selection, weighting rationale, controversy overlay logic, and missing-data treatment
- **Holding-level scorecards** — composite and pillar scores with underlying indicators for each position
- **Portfolio-level dashboard** — weighted-average scores, distribution charts, sector/geography heatmaps
- **Impact metrics table** — quantified KPIs (carbon intensity, diversity metrics, etc.) with benchmark comparison
- **Risk and opportunity register** — laggards, improvers, exclusion-boundary cases, and engagement recommendations
- **Data quality log** — coverage gaps, provider disagreements, and any [VERIFY] items requiring manual confirmation

## Quality Checks

- Confirm all ESG data vintages are within the agreed staleness threshold; flag any holding where providers materially disagree (>2 quintile spread)
- Verify weighting scheme sums to 100% at each aggregation level and that no single factor dominates due to data availability bias
- Cross-check exclusion screen results against the mandate's negative list — zero tolerance for misclassification on controversial weapons and sanctions [VERIFY applicable exclusion regulations]
- Validate portfolio carbon intensity calculation against a second source or manual spot-check of the top-10 contributors
- Ensure SFDR classification alignment if the product is marketed in the EU — Article 8 requires minimum environmental/social characteristics disclosure; Article 9 requires a sustainable investment objective [VERIFY latest RTS requirements]
- Review for internal consistency: a holding cannot score top-decile on governance while carrying an unresolved major controversy flag without explicit justification
