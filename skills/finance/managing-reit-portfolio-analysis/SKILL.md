---
name: managing-reit-portfolio-analysis
language: en
description: Structures REIT portfolio evaluation with property-level analysis, geographic diversification, and tenant concentration. Use when analyzing REIT portfolios, evaluating property mix, or assessing concentration risk.
tags:
  - management
  - real-estate-finance
  - risk
  - portfolio
metadata:
  author: casemark
  practice_areas:
    - Real Estate Finance
    - REIT Analysis
    - Property Investment
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing REIT Portfolio Analysis

Structures REIT portfolio evaluation with property-level analysis, geographic diversification, tenant concentration assessment, and sector allocation review.

## When To Use

- Evaluating an equity or mortgage REIT's property holdings for investment due diligence
- Assessing geographic and tenant concentration risk within a REIT portfolio
- Comparing sector allocation (office, industrial, retail, residential, specialty) against benchmarks or peers
- Reviewing portfolio quality ahead of capital raises, credit facility renewals, or rating agency presentations
- Monitoring portfolio drift from stated investment mandate or target allocation

## Inputs To Gather

- **Property schedule**: Full asset list with property name, type, location (MSA/state), square footage or unit count, acquisition date, and acquisition cost or current carrying value
- **Rent roll summary**: Top tenants by annualized base rent (ABR) or percentage of total revenue, lease expiration schedule, weighted-average lease term (WALT)
- **Financial data**: Net operating income (NOI) per property or segment, same-store NOI growth, occupancy rates, cap rates at acquisition vs. current market
- **Debt schedule**: Property-level or pool-level encumbrances, LTV ratios, maturity profile
- **Benchmark data**: Peer REIT allocations, NAREIT sector indices, or internal target allocation policy [VERIFY: confirm which benchmark set the stakeholder uses]

## Workflow

1. **Compile property-level data**
   - Normalize property types into standard categories (office, industrial, multifamily, retail, healthcare, data center, self-storage, specialty)
   - Confirm total gross asset value (GAV) or enterprise value denominator for percentage calculations
   - Flag any properties with missing NOI, occupancy, or valuation data as [VERIFY]

2. **Analyze sector allocation**
   - Calculate each property type's share of GAV, NOI contribution, and square footage
   - Compare against the REIT's stated strategy and peer median allocations
   - Identify overweight/underweight positions relative to benchmarks

3. **Assess geographic diversification**
   - Map properties by MSA, state, and region
   - Calculate concentration metrics: percentage of GAV and NOI in top 1, 3, 5, and 10 markets
   - Flag single-market concentrations exceeding 20% of GAV or NOI as elevated risk
   - Note exposure to markets with adverse demand trends (e.g., office in high-vacancy MSAs) [VERIFY: current market conditions for flagged MSAs]

4. **Evaluate tenant concentration**
   - Rank tenants by ABR contribution; identify top 10 tenants and their cumulative share
   - Flag any single tenant representing >5% of ABR, or top 10 tenants exceeding 40% collectively
   - Assess tenant credit quality (investment-grade vs. non-rated) where data is available [VERIFY: credit ratings current as of analysis date]
   - Map lease expiration schedule by year for the next 5 years; highlight any year with >15% of ABR rolling

5. **Review portfolio quality metrics**
   - Calculate weighted-average occupancy across portfolio
   - Compute weighted-average remaining lease term
   - Assess same-store NOI growth trend (trailing 4–8 quarters)
   - Identify bottom-quartile assets by occupancy, NOI margin, or cap rate spread

6. **Synthesize risk and opportunity flags**
   - Summarize concentration risks (geographic, tenant, sector)
   - Identify assets that may be disposition candidates (underperforming, non-core)
   - Note any upcoming lease expirations or debt maturities that cluster in the same period
   - Highlight alignment or divergence from the REIT's stated investment thesis

## Output

Produce a structured management report containing:

- **Executive summary**: Portfolio size, sector mix, key concentration metrics, and top-line risk assessment (2–3 paragraphs)
- **Sector allocation table**: Property type, property count, GAV, NOI, % of total for each
- **Geographic heat map data**: Top 10 MSAs by GAV and NOI with concentration percentages
- **Tenant concentration table**: Top 10 tenants, ABR, % of total ABR, credit rating, WALT
- **Lease expiration schedule**: Annual ABR rolling for years 1–5, cumulative percentage
- **Risk flag summary**: Itemized list of concentration breaches, data gaps, and market-level concerns
- **Recommendations**: Specific next steps (rebalancing targets, disposition candidates, further diligence items)

## Quality Checks

- All percentages sum correctly to 100% within rounding tolerance (±0.5%)
- NOI and GAV totals reconcile to source financial statements or supplemental data
- Tenant names and lease terms match the most recent rent roll; stale data is marked [VERIFY]
- Geographic classifications use consistent MSA definitions (e.g., Census Bureau CBSA boundaries) [VERIFY: confirm MSA definition standard used]
- Concentration thresholds applied match the REIT's own policy limits or credit facility covenants before flagging breaches
- Report clearly distinguishes between confirmed data and analyst estimates
