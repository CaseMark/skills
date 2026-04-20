---
name: analyzing-manager-selection
language: en
description: Evaluates and selects investment managers with quantitative screening and qualitative assessment. Use when selecting fund managers, conducting manager due diligence, or evaluating strategy fit.
tags:
  - analysis
  - asset-management
  - investment
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
# Analyzing Manager Selection

## When To Use

- Screening new investment managers for inclusion in a portfolio or platform
- Conducting periodic re-evaluation of existing manager relationships
- Comparing managers within the same asset class or strategy mandate
- Performing due diligence ahead of a fund commitment or allocation change
- Assessing whether a manager's style drift, personnel turnover, or performance degradation warrants replacement

## Inputs To Gather

- **Mandate definition**: Asset class, strategy type (e.g., long/short equity, core fixed income, venture), target geography, and any ESG or thematic constraints
- **Quantitative data**: Returns (gross and net), AUM history, inception date, benchmark used, fee schedule (management fee, carry/incentive, hurdle rate)
- **Risk metrics**: Standard deviation, Sharpe ratio, Sortino ratio, max drawdown, beta, tracking error, information ratio, up/down capture ratios
- **Peer universe**: Comparable manager set or index for relative ranking
- **Qualitative materials**: Pitch book or DDQ, organizational chart, key person bios, investment process narrative, operational due diligence reports
- **Reference checks**: Prior or current allocator references, if available
- **Existing portfolio context**: Current manager lineup, target allocation, overlap analysis inputs

## Workflow

1. **Define the search criteria**
   - Confirm asset class, strategy, geography, vehicle type (SMA, commingled fund, LP interest), and size constraints
   - Establish minimum track record length (typically 3–5 years; [VERIFY] against client IPS or committee policy)
   - Set quantitative screening thresholds (e.g., top-quartile returns over trailing 5 years, Sharpe > 0.5, max drawdown < 20%)

2. **Run quantitative screening**
   - Pull performance data across common periods (1Y, 3Y, 5Y, since inception) against the stated benchmark
   - Calculate risk-adjusted metrics: Sharpe, Sortino, information ratio, up/down capture
   - Flag managers with AUM growth > 50% in a single year (capacity risk) or AUM decline > 30% (redemption risk)
   - Rank candidates within peer universe; eliminate those below threshold on more than one key metric

3. **Conduct qualitative assessment**
   - **People**: Evaluate team stability (key person tenure, turnover rate), depth of analyst bench, succession planning, alignment of interest (co-investment, deferred comp)
   - **Process**: Assess repeatability of the investment process — idea generation, portfolio construction, position sizing, sell discipline
   - **Philosophy**: Confirm the stated philosophy matches observed portfolio behavior (e.g., a "value" manager should show consistent value factor exposure)
   - **Organization**: Review firm ownership structure, business concentration risk (single-strategy vs. diversified), regulatory history, compliance infrastructure

4. **Evaluate operational infrastructure**
   - Review custodian, administrator, auditor, and legal counsel independence
   - Assess valuation policy, especially for illiquid or hard-to-value holdings [VERIFY]
   - Check for any material findings in SOC 1 / SSAE 18 reports
   - Confirm insurance coverage (E&O, fidelity bond) adequacy relative to AUM

5. **Perform fee and terms analysis**
   - Compare management fees, incentive fees, hurdle rates, and clawback provisions against peer norms
   - Model net-of-fee return impact across scenarios (base, upside, downside)
   - Evaluate liquidity terms: lockup period, redemption notice, gate provisions [VERIFY]

6. **Score and rank finalists**
   - Apply a weighted scorecard across quantitative (typically 40–50%), qualitative (30–40%), and operational (15–20%) dimensions
   - Highlight any single-factor disqualifiers (regulatory action, key person departure, style drift beyond tolerance)
   - Prepare a side-by-side comparison matrix for the top 2–4 candidates

7. **Document recommendation**
   - Summarize the rationale for the recommended manager(s) with explicit reference to scorecard results
   - Note any conditions or monitoring triggers (e.g., "recommend allocation contingent on completion of on-site visit")
   - Include dissenting considerations or risks that the investment committee should weigh

## Output

- **Manager Selection Memo**: 3–5 page narrative covering search parameters, screening methodology, finalist profiles, scorecard results, and final recommendation
- **Comparison Matrix**: Side-by-side table of finalists across key quantitative, qualitative, and operational dimensions
- **Scorecard Summary**: Weighted scoring grid with category scores, weights, and composite rank
- **Risk Flag Register**: List of any amber or red flags identified during screening, with mitigation notes
- **Monitoring Plan**: Suggested ongoing review triggers (performance breach, key person change, AUM threshold, regulatory event)

## Quality Checks

- Confirm all return data uses the same calculation methodology (time-weighted vs. money-weighted) and fee basis (gross vs. net) across managers
- Verify benchmark alignment — each manager should be measured against the benchmark stated in their own materials, not a generic proxy
- Ensure the peer universe is appropriately constructed (same strategy, similar AUM band, comparable vintage)
- Check that qualitative assessments cite specific evidence (e.g., "PM tenure of 12 years" not just "experienced team")
- Validate that fee comparisons reflect the actual share class or negotiated terms, not headline rates [VERIFY]
- Confirm no conflicts of interest exist (revenue-sharing, placement agent fees, affiliated relationships) or that they are disclosed
- Flag any data gaps with [VERIFY] rather than interpolating or assuming
