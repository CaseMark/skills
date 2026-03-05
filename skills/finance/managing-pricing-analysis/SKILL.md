---
name: managing-pricing-analysis
description: Structures pricing analysis with margin impact, competitive positioning, and elasticity assessment. Use when analyzing pricing, evaluating margin impact, or assessing pricing strategies.
tags:
  - management
  - financial-planning-and-analysis
metadata:
  author: casemark
  practice_areas:
    - FP&A
    - Management Accounting
    - Business Intelligence
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Pricing Analysis

Structures pricing analysis with margin impact, competitive positioning, and elasticity assessment.

## When To Use

- Evaluating proposed price changes across product lines or service tiers
- Assessing margin erosion from discount programs, promotions, or volume rebates
- Benchmarking pricing against competitors or market indices
- Modeling price elasticity to forecast volume and revenue effects
- Preparing pricing recommendations for executive review or pricing committee

## Inputs To Gather

- **Revenue and volume data**: Unit sales, ASP (average selling price), and revenue by SKU/product line for trailing 12+ months
- **Cost structure**: COGS breakdown (materials, labor, overhead), variable vs. fixed cost allocation per unit
- **Current pricing architecture**: List prices, discount schedules, contract pricing tiers, promotional calendars
- **Competitive intelligence**: Competitor published prices, win/loss data with price as cited factor, market share estimates [VERIFY sourcing methodology]
- **Customer segmentation**: Revenue concentration by customer tier, price sensitivity indicators, churn rates by segment
- **Volume and elasticity history**: Prior price change events and observed volume response (minimum two data points for regression)

## Workflow

1. **Baseline current state**
   - Calculate gross margin, contribution margin, and margin-per-unit at current pricing
   - Map the price waterfall from list price through to pocket price (list -> invoice -> pocket), identifying leakage points (discounts, rebates, freight absorption, payment terms)
   - Segment margin performance by product line, customer tier, and channel

2. **Assess competitive positioning**
   - Plot relative price position against top 3-5 competitors for comparable offerings
   - Identify price premium/discount percentage and whether it aligns with differentiation strategy
   - Flag products priced below cost-plus floor or above value ceiling [VERIFY competitor data recency]

3. **Model price elasticity**
   - Use historical price-volume pairs to estimate arc elasticity for key SKUs or categories
   - Where historical data is insufficient, apply analogous product benchmarks or conjoint survey data and label as estimated
   - Classify products as elastic (|E| > 1), unit elastic, or inelastic and note implications for pricing power

4. **Run scenario analysis**
   - Model 2-4 pricing scenarios (e.g., +5%, +10%, selective increase on inelastic items, competitive parity adjustment)
   - For each scenario, project: revenue impact, volume change, gross margin dollars, and gross margin percentage
   - Include a breakeven volume loss calculation — the maximum volume decline that still preserves total margin dollars

5. **Synthesize recommendations**
   - Rank scenarios by margin-dollar improvement and strategic fit
   - Identify implementation sequencing (which products/segments to adjust first)
   - Note customer communication and contractual constraints (e.g., MFN clauses, annual price adjustment caps) [VERIFY contract terms]

## Output

Structure the deliverable as a management report with these sections:

- **Executive summary**: One-paragraph recommendation with projected annual margin impact in dollars and percentage points
- **Price waterfall analysis**: Visual or tabular breakdown from list to pocket price, highlighting top three leakage sources
- **Competitive price map**: Positioning chart or table showing relative pricing vs. key competitors
- **Elasticity summary table**: Product/category, estimated elasticity coefficient, confidence level (historical vs. estimated), and pricing implication
- **Scenario comparison matrix**: Side-by-side table of scenarios showing revenue, volume, margin dollars, and margin percentage
- **Breakeven analysis**: Maximum tolerable volume loss per scenario
- **Implementation roadmap**: Phased timeline with responsible owners, customer notification requirements, and system update steps

## Quality Checks

- Verify that margin calculations reconcile to source P&L data — pocket margin should trace back to reported gross margin within 2% tolerance
- Confirm elasticity estimates are based on at least two independent price-change observations or are clearly flagged as analogous/estimated
- Ensure competitive data is dated and sourced — reject comparisons older than 6 months without [VERIFY] notation
- Validate that scenario projections use consistent assumptions (cost held constant vs. cost inflation included) and state which assumption applies
- Check that breakeven volume loss is calculated correctly: breakeven % = margin increase % / (margin % + margin increase %)
- Confirm no recommended price falls below fully-loaded cost floor unless a strategic rationale (market entry, loss leader) is explicitly documented
- Flag any product where recommended price exceeds the highest observed competitor price without a stated value justification
