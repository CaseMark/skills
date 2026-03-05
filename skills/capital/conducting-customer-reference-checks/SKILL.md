---
name: conducting-customer-reference-checks
description: Structures customer diligence with interview guides, NPS analysis, switching cost assessment, and usage pattern evaluation. Use when conducting customer references, validating product-market fit, or assessing customer satisfaction.
tags:
  - process
  - venture-capital
  - valuation
metadata:
  author: casemark
  practice_areas:
    - Venture Capital
    - Seed/Series Investing
    - Startup Ecosystems
  document_types:
    - Process Documentation
  skill_modes:
    - Process Management
---
# Conducting Customer Reference Checks

Structures customer diligence with interview guides, NPS analysis, switching cost assessment, and usage pattern evaluation.

## When To Use

- During Series A+ diligence to validate founder claims about product-market fit, retention, and expansion
- When evaluating seed-stage companies where customer count is small but reference signal is high-leverage
- To pressure-test net revenue retention (NRR) narratives before committing to a term sheet
- When a deal's thesis hinges on customer love, switching costs, or category creation

## Inputs To Gather

- **Customer list from founder**: Full roster segmented by cohort, ACV tier, and use case — note any references the founder specifically suggested vs. those you sourced independently
- **Product usage data**: Monthly/weekly active usage metrics, seat utilization rates, feature adoption curves if available from the data room
- **Contract details**: ACV, contract term, renewal dates, expansion history, and any concessions (discounts, custom SLAs, free pilots)
- **Competitive landscape**: Which alternatives customers evaluated or used previously — needed to frame switching cost questions
- **Churn log**: Lost customers with win/loss notes; request backdoor references from at least 1-2 churned accounts

## Workflow

1. **Segment the reference pool**
   - Categorize customers by: ACV band, tenure (< 6 mo / 6-12 mo / 12+ mo), use case, and geography
   - Flag founder-provided references separately from independently sourced ones (LinkedIn, G2 reviews, conference attendee lists)
   - Aim for 6-10 references total; at least 30% should be independently sourced and at least 1 churned or downsell account

2. **Build the interview guide**
   - **Discovery block**: How they found the product, what they replaced, buying process and timeline
   - **Value block**: Top 3 problems solved, quantified ROI if possible, time-to-value from contract signing
   - **Stickiness block**: What would break if they turned it off tomorrow? Who else internally depends on it? Have they expanded seats/modules?
   - **NPS/satisfaction block**: Unprompted willingness to recommend (0-10), biggest complaint, feature they'd add first
   - **Competitive block**: Alternatives considered, why they chose this product, what would make them switch
   - Tailor question depth to the customer's ACV tier — enterprise references warrant 30-45 min calls; SMB references can be 15-20 min

3. **Conduct reference calls**
   - Open with context on your role (investor conducting diligence) and confidentiality assurance
   - Let the customer talk — use open-ended prompts, not leading questions
   - Probe for specifics: "You mentioned ROI — can you quantify that?" or "What was onboarding actually like in the first 30 days?"
   - Document verbatim quotes for key claims; paraphrase is insufficient for investment committee memos

4. **Assess switching costs and lock-in**
   - Identify integration depth (API connections, data pipelines, workflow dependencies)
   - Evaluate organizational embedding — how many teams/departments use it, is it in critical workflows?
   - Gauge contractual lock-in vs. genuine preference — multi-year contracts mask churn risk if product satisfaction is low
   - Score switching cost as Low / Medium / High with supporting rationale

5. **Analyze patterns across references**
   - Map NPS scores and note distribution (bimodal scores signal segment-specific product-market fit, not broad PMF)
   - Compare founder-provided vs. independent references — significant divergence is a yellow flag
   - Identify common objections or feature gaps cited by multiple references
   - Assess whether expansion revenue is pull (customer-initiated) or push (sales-driven upsell)

6. **Synthesize findings into diligence memo**

## Output

The deliverable is a **Customer Reference Diligence Memo** containing:

- **Executive summary**: 3-5 sentence verdict on customer quality, satisfaction depth, and switching cost profile
- **Reference matrix**: Table of all references with segment, tenure, ACV, NPS score, and one-line takeaway
- **Key themes**: Grouped findings on value drivers, competitive positioning, and common complaints
- **NPS analysis**: Score distribution, comparison to SaaS benchmarks by stage [VERIFY against current benchmark sources], and qualitative color behind the numbers
- **Switching cost assessment**: Low / Medium / High rating per customer with rationale; aggregate assessment for the portfolio
- **Risk flags**: Concentration risk (top customer % of ARR), founder-reference bias, feature gaps cited by 2+ references, any signs of churn risk
- **Verbatim quotes**: Curated quotes supporting key positive and negative findings — labeled by reference ID, not customer name, for confidentiality

## Quality Checks

- At least 30% of references were independently sourced (not founder-provided)
- Churned or downsell references were attempted — if none available, note this as a gap
- NPS scores are accompanied by qualitative context, not presented as standalone metrics
- Switching cost ratings are supported by specific integration or workflow evidence, not subjective impressions
- Verbatim quotes are attributed by reference ID and not editorialized
- Founder claims about retention, NRR, or customer love are explicitly confirmed, partially confirmed, or contradicted by reference findings
- [VERIFY] Any SaaS NPS or NRR benchmarks cited are sourced and current (benchmarks shift year to year)
- Memo flags where reference pool is too small or too homogeneous to draw reliable conclusions
