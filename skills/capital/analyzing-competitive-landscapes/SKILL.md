---
name: analyzing-competitive-landscapes
description: Maps competitive dynamics with market positioning, feature comparison, funding histories, and differentiation assessment. Use when analyzing startup competition, mapping market landscapes, or identifying competitive threats.
tags:
  - analysis
  - venture-capital
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
# Analyzing Competitive Landscapes

Maps competitive dynamics for venture-stage companies — positioning each player by product scope, go-to-market motion, funding trajectory, and defensibility. Designed for investment memos, deal screening, and portfolio strategy.

## When To Use

- Evaluating a target company's competitive position before a seed or Series A investment decision
- Building a market map for a new sector thesis or fund strategy memo
- Assessing whether a portfolio company's moat is widening or eroding
- Responding to LP questions about competitive risk in a specific deal or sector
- Comparing multiple deal opportunities within the same vertical

## Inputs To Gather

- **Target company name and sector** — the focal company or sector to map around
- **Known competitors** — any companies the user already tracks; prompt for both direct and adjacent competitors
- **Data sources available** — pitch decks, Crunchbase/PitchBook profiles, earnings transcripts, product demos, customer interviews
- **Funding history** — rounds raised, lead investors, valuations (if known) for each competitor
- **Scope boundaries** — geography (US-only vs. global), stage focus (pre-seed through growth), and time horizon for the analysis
- **Key evaluation dimensions** — e.g., product breadth, pricing model, distribution channel, team pedigree, IP/defensibility

## Workflow

1. **Define the competitive set**
   - Start with direct competitors (same ICP, same core use case), then layer in adjacent competitors (overlapping feature sets or converging roadmaps) and potential entrants (incumbents with resources to pivot in)
   - Confirm the list with the user before proceeding — missing a key player invalidates the map

2. **Build company profiles**
   - For each competitor, capture: founding year, HQ, headcount, total funding raised, last round details (date, size, lead investor, valuation if available), revenue model, primary customer segment, and notable customers or partnerships
   - Flag any data points sourced from estimates or secondhand reports with [VERIFY]

3. **Map market positioning**
   - Plot competitors on a 2×2 matrix using the two most strategically relevant dimensions (e.g., enterprise vs. SMB on one axis, vertical-specific vs. horizontal on the other)
   - Identify white-space quadrants — these represent potential positioning opportunities or underserved segments

4. **Compare product and GTM**
   - Build a feature comparison table covering core capabilities, integrations, pricing tiers, and deployment model (cloud/on-prem/hybrid)
   - Note each company's primary distribution channel: product-led growth, outbound sales, channel partnerships, or embedded/OEM
   - Highlight where the target company has clear feature parity gaps or unique differentiators

5. **Analyze funding trajectories**
   - Chart cumulative funding over time for the top 5–8 competitors
   - Identify inflection points: large rounds that signal acceleration, down rounds or flat extensions that suggest trouble, and strategic investors that imply distribution advantages
   - Note investor overlap — shared investors across competitors can signal thesis conviction or create information asymmetry risks [VERIFY investor conflict policies]

6. **Assess defensibility and moat**
   - Score each competitor on: network effects, switching costs, data/IP advantages, regulatory moats, and brand/community lock-in
   - Be explicit about which moats are structural vs. temporary (e.g., first-mover advantage without switching costs is temporary)

7. **Synthesize competitive risk assessment**
   - Rank the top 3 competitive threats to the target company with a brief rationale for each
   - Call out the most likely competitive scenario over the next 12–24 months (consolidation, feature convergence, new entrant disruption, or market expansion)

## Output

Structure the deliverable as follows:

- **Executive Summary** — 3–5 sentence overview of the competitive landscape and where the target company sits
- **Market Map** — 2×2 positioning matrix with brief annotations
- **Competitor Profiles** — one paragraph per company covering stage, traction, differentiation, and funding
- **Feature Comparison Table** — side-by-side grid of capabilities and GTM attributes
- **Funding Timeline** — chronological view of capital raised across the competitive set
- **Defensibility Scorecard** — moat ratings (strong / moderate / weak) per competitor across each dimension
- **Risk Assessment** — ranked competitive threats with scenario analysis
- **Data Gaps & Caveats** — list of unverified data points and information that could change the conclusions

## Quality Checks

- Every competitor profile includes at least funding data and product positioning; if either is missing, flag with [VERIFY]
- The 2×2 matrix uses dimensions that actually differentiate the players — avoid axes where all companies cluster in one quadrant
- Feature comparison is based on current shipping product, not roadmap claims, unless explicitly noted
- Funding data references specific rounds with dates, not just "raised $X total" without context
- Risk assessment distinguishes between competitors that are threats today vs. those that could become threats if they pivot or raise capital
- No investor names or valuation figures are presented without source attribution or [VERIFY] tags
- Analysis avoids conflating TAM size with the target company's realistic addressable share
