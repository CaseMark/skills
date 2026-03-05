---
name: analyzing-investor-concentration-risk
description: Monitors LP base composition with concentration analysis, redemption risk, and re-up probability assessment. Use when analyzing investor concentration, assessing re-up risk, or managing LP base diversification.
tags:
  - analysis
  - investor-relations-and-lp-reporting
  - risk
metadata:
  author: casemark
  practice_areas:
    - Investor Relations
    - LP Reporting
    - Fund Administration
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Investor Concentration Risk

Monitors LP base composition with concentration analysis, redemption risk, and re-up probability assessment.

## When To Use

- Preparing for a new fundraise and need to assess re-up likelihood across the existing LP base
- An LP provides notice of a potential redemption or signals reduced allocation appetite
- Fund leadership requests a diversification analysis ahead of advisory committee meetings
- Periodic (quarterly or annual) review of LP base health and concentration exposure
- Evaluating whether adding or losing a single LP would breach internal concentration thresholds

## Inputs To Gather

- **LP commitment schedule**: Each LP's committed capital, called capital, unfunded commitment, and vintage
- **Ownership breakdown**: Percentage of total fund commitments attributable to each LP and each LP category (pension, endowment, family office, sovereign wealth, fund-of-funds, etc.)
- **Historical re-up data**: Prior fund participation by each LP (Fund I, II, III, etc.) and commitment size trajectory
- **Redemption/liquidity terms**: Side letter provisions, lock-up periods, early redemption penalties, and gate provisions [VERIFY against fund LPA and side letters]
- **LP relationship intelligence**: Recent meeting notes, known allocation changes, CIO turnover, or regulatory shifts affecting the LP
- **Internal concentration policy**: Fund-level or GP-level thresholds (e.g., no single LP > 20% of commitments; no single LP type > 40%)

## Workflow

1. **Build the concentration snapshot**
   - Calculate each LP's share of total commitments and rank by size
   - Compute Herfindahl-Hirschman Index (HHI) for the LP base to quantify overall concentration
   - Segment LPs by type, geography, and regulatory regime; calculate category-level concentration

2. **Assess single-LP risk**
   - Flag any LP exceeding internal concentration thresholds
   - For each top-5 LP, model the impact of full withdrawal on fund size, management fee revenue, and carry economics
   - Note any LP whose unfunded commitment represents a material portion of remaining callable capital

3. **Evaluate re-up probability**
   - Score each LP on re-up likelihood (High / Medium / Low) based on:
     - Historical participation pattern (consistent, growing, declining, or first-time)
     - Known allocation policy changes or portfolio rebalancing signals
     - Relationship health indicators (responsiveness, advisory board engagement, co-investment activity)
   - Weight scores by commitment size to produce a capital-weighted re-up probability for the fund

4. **Assess redemption and liquidity risk**
   - Identify LPs with upcoming lock-up expirations or opt-out windows [VERIFY dates against LPA]
   - Flag side letter provisions that allow early liquidity or reduced notice periods
   - Estimate worst-case redemption scenario (simultaneous exercise of all available liquidity rights) and its effect on fund operations

5. **Identify diversification opportunities**
   - Compare current LP mix against target diversification profile
   - Highlight underrepresented LP categories or geographies that would reduce concentration
   - Recommend target allocation ranges for the next fundraise to improve base resilience

6. **Synthesize and document**
   - Compile findings into a structured concentration risk report
   - Assign an overall LP base risk rating (Low / Moderate / Elevated / High)
   - Provide actionable recommendations ranked by impact and urgency

## Output

The deliverable is an **Investor Concentration Risk Report** containing:

- **Executive summary**: Overall risk rating, top concentration concerns, and priority actions
- **Concentration metrics table**: Per-LP and per-category commitment percentages, HHI score, and threshold comparisons
- **Re-up probability matrix**: Each LP scored and weighted, with aggregate re-up capital estimate
- **Redemption risk timeline**: Calendar view of lock-up expirations, opt-out windows, and gate trigger dates
- **Scenario analysis**: Impact of losing the top 1, 2, or 3 LPs on fund economics (management fees, carry, operational viability)
- **Diversification gap analysis**: Current vs. target LP mix with specific fundraising recommendations
- **Appendix**: Data sources, assumptions, and items marked [VERIFY]

## Quality Checks

- Confirm all commitment figures reconcile to the fund administrator's capital account statements
- Verify that concentration percentages sum correctly and reflect the most recent capital call/distribution activity
- Ensure re-up scores are supported by documented evidence (meeting notes, allocation letters), not speculation—mark unsupported assessments with [VERIFY]
- Cross-check redemption windows and side letter terms against executed documents, not summaries [VERIFY]
- Validate that internal concentration thresholds referenced match current GP policy (these may update annually)
- Confirm scenario analyses use consistent assumptions (e.g., management fee offsets, recycling provisions)
- Review for LP-identifying information handling—ensure the report complies with confidentiality obligations before distribution
