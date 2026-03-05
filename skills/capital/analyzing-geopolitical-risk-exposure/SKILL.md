---
name: analyzing-geopolitical-risk-exposure
description: Evaluates geopolitical risk impact on investment portfolios with sanctions exposure, conflict risk, and supply chain disruption analysis. Use when analyzing geopolitical risk, assessing sanctions impact, or evaluating political event exposure.
tags:
  - analysis
  - cross-border-capital
  - risk
  - investment
metadata:
  author: casemark
  practice_areas:
    - International Finance
    - Cross-Border Transactions
    - Emerging Markets
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Geopolitical Risk Exposure

Evaluates geopolitical risk impact on investment portfolios with sanctions exposure, conflict risk, and supply chain disruption analysis.

## When To Use

- Assessing portfolio-level exposure to sovereign or sub-sovereign political events (elections, coups, regime transitions, territorial disputes)
- Screening direct and indirect sanctions exposure across OFAC, EU, UK, and UN consolidated lists
- Evaluating supply chain concentration risk tied to geopolitically unstable corridors
- Stress-testing cross-border investment theses against conflict escalation, trade restriction, or expropriation scenarios
- Performing pre-investment due diligence on emerging-market or frontier-market allocations

## Inputs To Gather

- **Portfolio holdings data**: Issuer names, domiciles, revenue-by-geography breakdown, and counterparty chain where available
- **Target scope**: Specific countries, regions, sectors, or asset classes to focus on (or full-portfolio sweep)
- **Time horizon**: Near-term event-driven (0–6 months) vs. structural risk assessment (1–5 years)
- **Sanctions lists**: Current OFAC SDN/SSI, EU consolidated, UK sanctions list, UN Security Council lists [VERIFY current list versions and any recent amendments]
- **Client risk appetite**: Tolerance thresholds for sanctions proximity, conflict-zone revenue percentage, and single-country concentration
- **Existing risk policies**: Any internal compliance screens, restricted-country lists, or ESG exclusion criteria already in place

## Workflow

1. **Map geographic exposure**: For each holding or target, identify country-of-domicile, country-of-operations, and revenue-by-geography. Flag any mismatch (e.g., domiciled in Ireland but 60% revenue from Russia-adjacent markets).

2. **Screen sanctions exposure**:
   - Run issuer names, subsidiaries, and key principals against OFAC SDN, Sectoral Sanctions (SSI), and non-SDN lists [VERIFY which OFAC programs apply to the asset class]
   - Cross-check against EU, UK, and UN lists for multi-jurisdictional mandates
   - Identify secondary sanctions risk (e.g., non-US entities transacting with sanctioned counterparties that could trigger US secondary sanctions)
   - Flag 50% ownership rule implications where sanctioned persons hold aggregate 50%+ stakes [VERIFY current OFAC guidance on ownership aggregation]

3. **Assess conflict and instability risk**:
   - Classify each country exposure using a tiered framework: active conflict, frozen conflict, elevated political instability, stable but watchlisted
   - Evaluate likelihood and impact of escalation triggers (upcoming elections, territorial flashpoints, resource competition, alliance realignment)
   - Quantify portfolio NAV-at-risk for each conflict scenario (base case, escalation, de-escalation)

4. **Analyze supply chain and trade-route disruption**:
   - Map critical supply chain nodes (manufacturing, raw materials, logistics chokepoints) by geography
   - Identify single-point-of-failure dependencies on geopolitically sensitive corridors (e.g., Strait of Hormuz, Taiwan Strait, Red Sea/Suez, Black Sea)
   - Assess tariff, export control, and trade restriction exposure [VERIFY current trade policy status for identified corridors]

5. **Score and rank exposures**:
   - Assign composite risk scores combining probability-weighted impact across sanctions, conflict, and supply chain dimensions
   - Rank holdings or positions from highest to lowest composite geopolitical risk
   - Identify concentration clusters (multiple holdings exposed to the same geopolitical trigger)

6. **Develop mitigation options**:
   - Propose hedging strategies (FX hedges, CDS on sovereign exposure, geographic diversification)
   - Identify positions for reduction or exit based on risk-appetite thresholds
   - Recommend monitoring triggers (specific events that would warrant portfolio action)

## Output

The deliverable is a **Geopolitical Risk Exposure Report** containing:

- **Executive summary**: Top 3–5 geopolitical risks to the portfolio, ranked by severity, with recommended actions
- **Sanctions screening results**: Pass/flag/fail status for each holding with detail on flagged items and secondary exposure
- **Country risk heat map**: Tabular or visual summary of portfolio allocation by country risk tier
- **Scenario analysis table**: NAV impact estimates under base, escalation, and de-escalation scenarios for material exposures
- **Supply chain vulnerability summary**: Critical chokepoints and single-source dependencies identified
- **Concentration risk flags**: Holdings with correlated geopolitical triggers
- **Recommended actions**: Specific hedging, reduction, or monitoring steps with priority ranking
- **Data limitations and assumptions**: Explicit disclosure of data gaps, stale inputs, or modeled estimates

## Quality Checks

- Every sanctioned-entity flag includes the specific list, program, and date verified — no bare pass/fail without citation
- Revenue-by-geography data is sourced from issuer filings or credible third-party databases; estimated breakdowns are marked as such
- Scenario impact estimates state the methodology and assumptions used (historical analogy, quantitative model, expert judgment)
- No holding is excluded from screening without documented justification
- Secondary sanctions analysis covers the full counterparty chain, not just direct issuer exposure
- All jurisdiction-dependent conclusions (sanctions applicability, export control scope, treaty obligations) are marked [VERIFY] where the analysis depends on the investor's domicile or regulatory jurisdiction
- Report discloses the as-of date for all sanctions lists and political risk assessments used
