---
name: analyzing-market-size-and-timing
description: Structures TAM/SAM/SOM analysis with bottom-up and top-down methodology and market timing assessment. Use when sizing markets, validating market opportunity, or assessing timing risk.
tags:
  - analysis
  - venture-capital
  - risk
metadata:
  author: casemark
  practice_areas:
    - Venture Capital
    - Seed/Series Investing
    - Startup Ecosystems
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Market Size And Timing

## When To Use

- Evaluating a startup's market opportunity during due diligence for seed or Series A investment
- Validating founder claims about addressable market in a pitch deck or investment memo
- Assessing whether market timing supports the investment thesis (too early, right window, too late)
- Comparing market size across competing deals in the same vertical
- Stress-testing SAM/SOM assumptions before presenting to an investment committee

## Inputs To Gather

- **Company data**: product description, target customer profile, pricing model, current revenue/ARR if any
- **Founder claims**: any TAM/SAM/SOM figures from the pitch deck or data room
- **Industry reports**: analyst estimates from Gartner, IDC, PitchBook, CB Insights, or vertical-specific sources [VERIFY availability and recency of cited reports]
- **Comparable companies**: public comps, recent exits, or late-stage private companies in the same market
- **Regulatory/macro context**: relevant policy shifts, technology adoption curves, or demographic trends that affect timing
- **Geographic scope**: whether the analysis is US-only, multi-market, or global

## Workflow

1. **Define the market boundary**
   - State the product category and end-user segment precisely (e.g., "cloud-based LIMS for contract research organizations," not "lab software")
   - Distinguish between the broader category (TAM) and the segment the company can realistically address (SAM) given its product, geography, and go-to-market

2. **Run top-down sizing**
   - Start with a credible industry-level revenue figure from an analyst report or public filing
   - Apply segmentation filters: geography, customer type, price tier, use case
   - Arrive at a top-down TAM and SAM; note every filter and its source

3. **Run bottom-up sizing**
   - Count addressable customer units (companies, users, transactions) from a primary or secondary data source
   - Multiply by realistic average revenue per unit based on the company's pricing or comparable pricing
   - Cross-check the bottom-up SAM against the top-down SAM; flag divergences greater than 2x

4. **Derive SOM (Serviceable Obtainable Market)**
   - Estimate realistic market share at 3-5 year horizon based on: competitive density, sales capacity, distribution advantages, switching costs
   - Anchor SOM to comparable company trajectories at similar stage — avoid assuming >5% share in a fragmented market without justification

5. **Assess market timing**
   - **Technology readiness**: Is the enabling technology mature enough for mainstream adoption, or still early-adopter phase? Reference adoption S-curve position
   - **Demand signals**: Customer pull (inbound interest, RFPs, organic search trends) vs. requiring heavy evangelism
   - **Regulatory tailwinds/headwinds**: Pending legislation, enforcement trends, or compliance deadlines that accelerate or delay adoption [VERIFY jurisdiction-specific regulatory timelines]
   - **Competitive window**: Are incumbents asleep, pivoting, or already building? Is the window opening, open, or closing?
   - Classify timing as: **Too Early** (market needs 3+ years of development), **Right Window** (demand inflecting, competition nascent), or **Late** (dominant players established, commoditization underway)

6. **Triangulate and stress-test**
   - Compare top-down, bottom-up, and founder-claimed figures side by side
   - Identify the weakest assumption in each approach and test sensitivity (e.g., halve the price assumption or customer count)
   - State a confidence-weighted range rather than a single point estimate

## Output

Produce a structured market sizing memo with:

- **Market definition**: one-paragraph boundary statement
- **TAM / SAM / SOM table**: top-down and bottom-up figures side by side, with sources and key assumptions per line
- **Timing assessment**: classification (Too Early / Right Window / Late) with 3-5 supporting data points
- **Key assumptions log**: numbered list of every material assumption, flagged as high/medium/low confidence
- **Risk factors**: what would invalidate the sizing (e.g., regulatory reversal, platform risk, technology substitute)
- **Recommendation**: whether the market size and timing support the investment thesis, with caveats

## Quality Checks

- TAM is not conflated with SAM — the segmentation step is explicit and sourced
- Bottom-up and top-down approaches are both present; divergence is explained, not ignored
- SOM is grounded in comparable company data, not aspirational percentages
- Timing assessment includes at least one quantitative signal (search trends, adoption rates, regulatory deadline) rather than pure narrative
- Every dollar figure has a cited source or is clearly labeled as an assumption
- [VERIFY] tags are present for any statistic, regulation, or market figure that is date-sensitive or jurisdiction-dependent
- No single data source accounts for more than 60% of the analysis — triangulation is required
