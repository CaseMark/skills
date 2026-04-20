---
name: conducting-growth-due-diligence
language: en
description: Structures growth-focused DD with revenue quality, customer concentration, technology scalability, and organizational readiness. Use when conducting growth DD, validating revenue sustainability, or assessing scale capability.
tags:
  - process
  - growth-equity
metadata:
  author: casemark
  practice_areas:
    - Growth Equity
    - Expansion Capital
    - Late-Stage Investing
  document_types:
    - Process Documentation
  skill_modes:
    - Process Management
---
# Conducting Growth Due Diligence

## When To Use

- Evaluating a growth-stage company for minority or majority equity investment
- Validating whether reported revenue growth is sustainable and repeatable
- Assessing whether a company's infrastructure (technology, people, processes) can support 2–5x scale
- Conducting commercial DD alongside financial DD for expansion-capital or late-stage deals
- Re-underwriting a portfolio company ahead of a follow-on round

## Inputs To Gather

- **Financial data**: Monthly P&L (36+ months), cohort revenue schedules, bookings vs. billings vs. revenue reconciliation, deferred revenue roll-forward
- **Customer data**: Full customer list with ARR/revenue by account, contract start/end dates, expansion and churn history by cohort
- **Sales & pipeline data**: CRM export (stage, close date, ACV, source), quota attainment by rep, win/loss analysis
- **Product & technology**: Architecture overview, infrastructure cost trends, tech debt assessment, product roadmap, uptime/SLA history
- **Organization**: Org chart, key-person dependencies, open headcount plan, employee tenure distribution, Glassdoor/pulse survey data
- **Market context**: TAM/SAM sizing from third-party sources, competitive landscape, pricing benchmarking

## Workflow

### 1. Revenue Quality Analysis

- Decompose revenue into new, expansion, and renewal components by quarter
- Calculate net revenue retention (NRR), gross retention, and logo retention by cohort vintage
- Identify one-time, non-recurring, or channel-stuffed revenue; strip out and restate organic growth rate
- Assess ASP trends — are deals getting larger (land-and-expand working) or compressing (discounting to hit targets)?
- Test revenue recognition timing against cash collections; flag divergences > 10% [VERIFY against applicable accounting standards]

### 2. Customer Concentration & Dependency

- Compute top-1, top-5, top-10, and top-20 customer concentration as % of total revenue
- Flag any single customer > 10% of ARR or any top-5 cohort > 30%
- Evaluate contract structures for at-risk customers: auto-renew vs. opt-in, termination-for-convenience clauses, pricing renegotiation windows
- Cross-reference largest customers against public financial health indicators and industry headwinds
- Map customer acquisition channels — over-reliance on a single channel (e.g., one partnership) is a concentration risk

### 3. Go-to-Market Scalability

- Calculate CAC payback period, LTV/CAC ratio, and magic number by quarter and by channel
- Assess sales capacity model: quota-carrying reps × average attainment vs. bookings plan
- Evaluate ramp time for new reps and historical quota attainment curves (cohort of hire date)
- Review marketing funnel conversion rates stage-by-stage; identify bottleneck stages
- Test pricing power: history of price increases, competitive pricing position, willingness-to-pay data if available

### 4. Technology & Product Scalability

- Review infrastructure architecture for horizontal scaling capability and single points of failure
- Analyze cloud/hosting cost as % of revenue over time — should be flat or declining at scale
- Assess tech debt burden: what % of engineering time goes to maintenance vs. new features?
- Evaluate product-market fit signals: NPS/CSAT scores, feature adoption rates, support ticket trends
- Review security posture: SOC 2 status, penetration test history, incident response plan [VERIFY compliance requirements by industry]

### 5. Organizational Readiness

- Map key-person risk: identify roles where a single departure would materially impair operations
- Assess management team completeness against the next stage of scale (e.g., does a $30M ARR company have a real CFO, VP Sales, VP Engineering?)
- Review employee retention data — regrettable attrition > 15% annually in critical functions is a red flag
- Evaluate board composition and governance maturity relative to stage
- Identify cultural or process gaps: is the company still running on founder heroics or has it built repeatable systems?

### 6. Synthesis & Risk Mapping

- Score each workstream (revenue quality, concentration, GTM, technology, org) on a 1–5 risk scale
- Identify the 3–5 "must-believe" theses required for the investment to work
- Map key risks to mitigants (contractual protections, post-close initiatives, management commitments)
- Quantify downside scenarios: what happens to growth if NRR drops 10pts, if the top customer churns, if rep productivity declines?

## Output

Deliver a structured growth DD memo containing:

- **Executive summary**: Investment thesis, key strengths, top 3–5 risks, and overall DD verdict (proceed / proceed with conditions / pass)
- **Revenue quality section**: Restated organic growth rates, cohort retention analysis, revenue composition breakdown
- **Customer analysis**: Concentration tables, renewal risk calendar, dependency flags
- **GTM assessment**: Unit economics summary, sales capacity model, channel analysis
- **Technology review**: Scalability assessment, cost trajectory, tech debt impact
- **Org readiness**: Key-person risk matrix, hiring gap analysis, management scorecard
- **Risk register**: Tabulated risks with severity, likelihood, mitigant, and residual risk rating
- **Diligence items outstanding**: Open questions, data requests pending, items requiring [VERIFY]

## Quality Checks

- Every quantitative claim traces back to a named data source (e.g., "per CRM export dated MM/DD" or "per management-provided cohort schedule")
- Cohort math is internally consistent — individual cohort retentions must reconcile to blended NRR
- Customer concentration percentages sum correctly and match the revenue totals used elsewhere
- All [VERIFY] markers are preserved for jurisdiction-dependent, regulation-dependent, or unconfirmed data points
- Revenue restatements clearly separate management-reported figures from analyst-adjusted figures
- Downside scenarios use explicit, stated assumptions rather than arbitrary haircuts
- The memo distinguishes between confirmed findings and management representations not yet independently validated
