---
name: analyzing-go-to-market-efficiency
language: en
description: Evaluates sales efficiency with CAC payback, sales cycle analysis, channel economics, and pipeline conversion metrics. Use when assessing GTM efficiency, analyzing sales productivity, or evaluating distribution strategy.
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
# Analyzing Go To Market Efficiency

## When To Use

- Evaluating a growth-stage company's sales efficiency as part of due diligence or portfolio monitoring
- Assessing whether a company's GTM model can scale efficiently before committing expansion capital
- Benchmarking sales productivity across channels, segments, or cohorts
- Diagnosing deteriorating unit economics or lengthening sales cycles in a portfolio company
- Comparing GTM efficiency across multiple investment targets in the same vertical

## Inputs To Gather

- **Revenue data**: MRR/ARR by month for at least 12–24 months, broken out by channel and customer segment
- **Sales & marketing spend**: Fully loaded S&M costs by quarter (headcount, paid acquisition, events, SDR/BDR costs, tooling)
- **Pipeline data**: Stage-by-stage pipeline snapshots with deal counts, values, and timestamps (CRM export preferred)
- **Customer acquisition records**: New logo count by period, source/channel attribution, contract values (ACV/TCV)
- **Sales team data**: Rep count by role (AE, SDR, CSM), ramp timelines, quota attainment distribution, tenure
- **Churn/expansion data**: Logo and revenue churn rates, expansion revenue by cohort (needed for LTV-side of CAC payback)
- **Pricing structure**: Current pricing tiers, average discount rates, deal size distribution

## Workflow

1. **Calculate CAC and CAC payback period**
   - Compute fully loaded CAC = total S&M spend ÷ new customers acquired (use same period)
   - Calculate CAC payback = CAC ÷ (average ACV × gross margin %). Express in months
   - Segment CAC by channel (inbound, outbound, partner, paid) and by customer tier (SMB, mid-market, enterprise)
   - Flag any channel where CAC payback exceeds 18 months [VERIFY against sector-specific benchmarks]

2. **Analyze sales cycle length and velocity**
   - Measure median days from opportunity creation to closed-won, segmented by deal size and channel
   - Track sales cycle trend over trailing 4–6 quarters — increasing cycles signal market resistance or segment mismatch
   - Calculate pipeline velocity = (qualified opportunities × win rate × average deal size) ÷ sales cycle length
   - Compare velocity per rep against quota to identify capacity vs. productivity gaps

3. **Evaluate channel economics**
   - For each acquisition channel, compute: CAC, conversion rate (lead → opportunity → closed-won), and contribution margin
   - Identify channel-level LTV:CAC ratios — target ≥ 3:1 for healthy channels [VERIFY: threshold varies by stage and vertical]
   - Assess channel concentration risk — if >60% of new ARR comes from a single channel, flag dependency
   - For partner/reseller channels, account for revenue share and co-marketing costs in the fully loaded CAC

4. **Assess pipeline conversion and funnel health**
   - Map stage-by-stage conversion rates (MQL → SQL → opportunity → proposal → closed-won)
   - Identify the largest drop-off point — this is the primary efficiency bottleneck
   - Calculate pipeline coverage ratio = total qualified pipeline value ÷ quota target (healthy: 3–4×)
   - Evaluate pipeline aging — deals sitting >2× median cycle length are likely stale and inflate coverage metrics

5. **Benchmark sales productivity**
   - Compute ARR per quota-carrying rep (fully ramped vs. all reps)
   - Measure average ramp time (months to first quota attainment) and ramped rep retention
   - Assess quota attainment distribution — a healthy org has 60–70% of reps at or above quota [VERIFY]
   - Calculate magic number = net new ARR ÷ prior-period S&M spend (>0.75 is efficient, >1.0 is strong)

6. **Synthesize findings and flag risks**
   - Rank channels by efficiency (LTV:CAC, payback period, scalability potential)
   - Identify structural GTM risks: channel dependency, elongating cycles, declining rep productivity, rising CAC
   - Assess whether current GTM model supports the company's growth plan without disproportionate S&M spend increases

## Output

The deliverable is a GTM Efficiency Analysis Report containing:

- **Executive summary**: One-paragraph verdict on GTM efficiency with the 2–3 most critical findings
- **CAC analysis table**: Blended and channel-segmented CAC, CAC payback, and LTV:CAC ratios
- **Sales cycle analysis**: Median cycle by segment, trend over time, pipeline velocity metrics
- **Channel economics matrix**: Per-channel unit economics with efficiency ranking
- **Funnel conversion waterfall**: Stage-by-stage conversion rates with bottleneck identification
- **Sales productivity scorecard**: Rep-level productivity, ramp metrics, quota attainment distribution, magic number
- **Risk flags and recommendations**: Prioritized list of GTM risks with suggested actions

## Quality Checks

- All CAC calculations use fully loaded S&M costs (not just direct acquisition spend) — confirm headcount costs, tooling, and overhead are included
- CAC payback uses gross-margin-adjusted revenue, not raw ACV
- Pipeline metrics exclude churned or disqualified deals that were never truly in-cycle
- Sales cycle calculations use median (not mean) to avoid skew from outlier mega-deals
- LTV estimates account for gross churn and expansion revenue, not just initial contract value
- Channel attribution methodology is documented — flag if attribution model is last-touch only vs. multi-touch
- All benchmark comparisons cite the source and vintage of the benchmark data [VERIFY]
- If fewer than 12 months of data are available, note limited statistical significance in findings
