---
name: analyzing-competitive-moat-durability
language: en
description: Evaluates competitive advantage sustainability with switching costs, network effects, data assets, and brand strength analysis. Use when assessing competitive moats, analyzing defensibility, or evaluating long-term positioning.
tags:
  - analysis
  - growth-equity
metadata:
  author: casemark
  practice_areas:
    - Growth Equity
    - Expansion Capital
    - Late-Stage Investing
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Competitive Moat Durability

## When To Use

- Evaluating a growth-equity or late-stage investment target's defensibility before committing capital
- Stress-testing an existing portfolio company's competitive position during annual reviews or follow-on funding decisions
- Comparing moat quality across multiple deal candidates in a sector screen
- Assessing whether a company's margins are structurally protected or temporarily inflated

## Inputs To Gather

- **Product & pricing data**: Current pricing, historical price changes, feature comparison vs. top 3 competitors
- **Customer metrics**: Net revenue retention (NRR), logo churn, average contract length, expansion revenue as % of ARR
- **Switching cost evidence**: Integration depth (API calls, data volume, workflow embedding), migration cost estimates, contractual lock-in periods
- **Network effects indicators**: User/node growth curves, cross-side engagement ratios (for platforms), marginal value per incremental user
- **Proprietary data assets**: Volume, uniqueness, refresh rate, and regulatory barriers to replication of core datasets
- **Brand & mindshare signals**: Unaided recall surveys, NPS, organic inbound as % of pipeline, share-of-search trends
- **Competitive landscape**: Funded competitors, recent entrants, open-source alternatives, vertical-specific substitutes

## Workflow

1. **Classify moat type(s)**. Map the company's advantages to one or more moat categories: switching costs, network effects, proprietary data, brand/trust, scale economies, or regulatory/IP barriers. Most durable positions combine two or more.

2. **Score each moat dimension (1–5)**:
   - **Switching costs**: 1 = commodity/easily replaced; 5 = deeply embedded system of record with >12-month migration cost
   - **Network effects**: 1 = linear/no network value; 5 = strong cross-side effects with demonstrated viral loops
   - **Data assets**: 1 = publicly replicable data; 5 = proprietary, continuously compounding dataset with regulatory protection
   - **Brand strength**: 1 = no differentiation, price-driven; 5 = category-defining brand with pricing power >20% premium
   - **Scale economies**: 1 = cost structure mirrors competitors; 5 = structural unit-cost advantage that widens with volume

3. **Assess erosion risks**. For each scored dimension, identify the most plausible threat:
   - Technology shifts that reduce switching costs (e.g., standardized APIs, open formats)
   - Platform leakage or multi-tenanting that weakens network effects
   - Regulatory changes enabling data portability [VERIFY against jurisdiction-specific data regulations]
   - New entrants with deep funding targeting the same segment

4. **Quantify durability horizon**. Estimate how many years each moat dimension remains intact under base-case and downside scenarios. Flag any dimension with <3-year durability as a material risk.

5. **Synthesize composite moat rating**. Weight dimensions by relevance to the company's specific value chain. Produce an overall durability rating (Strong / Moderate / Weak) with a 3–5 sentence rationale.

## Output

Deliver a structured moat durability report containing:

- **Moat classification table**: Dimension | Score (1–5) | Key evidence | Primary erosion risk | Durability horizon
- **Composite rating**: Overall moat durability (Strong / Moderate / Weak) with weighted rationale
- **Red flags**: Any dimension scoring ≤2 or with a durability horizon under 3 years
- **Comparison to sector benchmarks**: Where the target sits vs. peer-set moat profiles (if peer data is available)
- **Investor implications**: How moat quality affects underwriting assumptions—specifically margin sustainability, defensible growth rate, and terminal value sensitivity

## Quality Checks

- Every score must cite at least one concrete data point (metric, customer quote, or market data)—no unsupported ratings
- Confirm that NRR, churn, and expansion figures are from the same time period and definition [VERIFY cohort definitions with management]
- Cross-reference stated switching costs against actual customer interviews or churn-reason data where available
- Verify that network-effect claims reflect genuine value-per-node growth, not just user count growth
- Ensure erosion-risk analysis considers at least one funded competitor and one technology disruption vector
- Mark any dimension where data is based on management assertions without third-party validation as [VERIFY]
