---
name: analyzing-property-casualty-lines
language: en
description: Evaluates P&C insurance lines with market cycle analysis, loss cost trending, and competitive assessment. Use when analyzing P&C markets, tracking insurance cycles, or evaluating line profitability.
tags:
  - analysis
  - insurance
metadata:
  author: casemark
  practice_areas:
    - Insurance
    - Actuarial Science
    - Reinsurance
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Property Casualty Lines

## When To Use

- Evaluating profitability and underwriting performance of specific P&C lines (commercial auto, GL, property, workers' comp, professional liability, etc.)
- Tracking market cycle position (hard vs. soft market) for pricing and capacity decisions
- Performing loss cost trending to project future loss development
- Assessing competitive positioning within a line or geographic market
- Supporting reinsurance purchasing decisions with line-level performance data
- Preparing portfolio reviews for underwriting committees or investor reporting

## Inputs To Gather

- **Line-of-business data**: Written premium, earned premium, incurred losses (paid + reserved), ALAE/ULAE splits, policy counts by line
- **Loss triangles**: Accident-year or policy-year development triangles (paid and incurred) with a minimum of 5–10 development periods
- **Rate change history**: Rate filings, rate adequacy studies, or renewal rate change tracking by quarter
- **Expense data**: Commission rates, acquisition costs, general expenses, and combined ratio components
- **Market benchmarks**: Industry combined ratios, rate-on-line indices, AM Best or S&P segment reports, ISO/NCCI aggregate data [VERIFY: benchmark availability varies by line and jurisdiction]
- **Catastrophe exposure**: PMLs, AALs, or cat model output for property-exposed lines
- **Regulatory context**: Rate filing requirements, prior-approval vs. file-and-use status by state [VERIFY: filing requirements by state and line]

## Workflow

1. **Define scope and segmentation**
   - Identify target lines (e.g., commercial property, general liability, personal auto)
   - Set the analysis period (typically 5–10 accident years for trend credibility)
   - Determine segmentation: by state, policy size, distribution channel, or coverage sub-type

2. **Develop loss costs**
   - Select development method (chain-ladder, Bornhuetter-Ferguson, or Cape Cod) based on data maturity and volatility
   - Apply loss development factors to bring immature years to ultimate
   - Trend historical losses to prospective cost level using loss cost trend factors (severity + frequency)
   - Adjust for one-time events: strip out or cap large losses, isolate catastrophe losses from attritional
   - On-level earned premiums to current rate levels to enable apples-to-apples comparison

3. **Analyze market cycle position**
   - Plot historical combined ratios and rate changes over 10+ years to identify cycle phase
   - Compare current rate adequacy to indicated loss costs — gap signals where the cycle is heading
   - Assess supply-side indicators: carrier entries/exits, capacity changes, reinsurance pricing shifts
   - Evaluate demand-side factors: exposure growth, insured value inflation, emerging liability trends
   - Classify current position: hardening, hard, softening, or soft, with supporting evidence

4. **Perform competitive assessment**
   - Benchmark combined ratio, loss ratio, and expense ratio against top-5 and industry-average peers
   - Identify market share trends: growing, stable, or contracting relative to competitors
   - Evaluate product differentiation: coverage breadth, endorsement strategy, claims service reputation
   - Assess distribution advantage: agency relationships, binding authority, digital channel penetration
   - Note competitive moats or vulnerabilities (e.g., data advantage in niche lines, adverse selection risk)

5. **Synthesize findings and recommendations**
   - Rank lines by risk-adjusted return: calendar-year combined ratio, accident-year loss ratio, and reserve adequacy
   - Flag lines requiring remediation (rate increases, non-renewal actions, coverage restriction)
   - Identify growth opportunities where rate adequacy exceeds target and competitive position is strong
   - Quantify reinsurance implications: lines where volatility warrants increased cession or restructured treaties

## Output

- **Line Performance Summary Table**: Each line with earned premium, loss ratio (calendar and accident year), expense ratio, combined ratio, rate change trend, and cycle position classification
- **Loss Development Exhibit**: Selected ultimate losses by accident year with selected LDFs and methodology notes
- **Market Cycle Chart**: Visual overlay of combined ratio and rate changes over time with cycle phase annotations
- **Competitive Positioning Matrix**: 2×2 or ranked grid showing relative profitability vs. market share position
- **Recommendations**: Prioritized action items per line — grow, maintain, remediate, or exit — with supporting rationale

## Quality Checks

- Confirm loss triangles reconcile to financial statement Schedule P or statutory filings [VERIFY: reconciliation targets depend on reporting entity type]
- Validate that on-leveling factors correctly reflect cumulative rate changes, not just filed changes
- Verify trend selections are supportable: compare selected severity/frequency trends against industry benchmarks and historical fit
- Ensure catastrophe vs. attritional loss separation is consistent across all accident years
- Cross-check combined ratio components sum correctly (loss ratio + DCCE ratio + expense ratio = combined ratio)
- Confirm market benchmark data is from the same reporting period and line definition as the subject portfolio
- Flag any line where data credibility is low (fewer than 1,000 claims or 3 development periods) with [VERIFY]
