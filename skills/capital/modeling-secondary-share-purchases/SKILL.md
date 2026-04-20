---
name: modeling-secondary-share-purchases
language: en
description: Structures secondary direct transactions with pricing methodology, transfer restriction analysis, and ROFR navigation. Use when modeling secondary purchases, pricing founder/employee shares, or structuring tender offers.
tags:
  - modeling
  - growth-equity
metadata:
  author: casemark
  practice_areas:
    - Growth Equity
    - Expansion Capital
    - Late-Stage Investing
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Secondary Share Purchases

Structures secondary direct transactions with pricing methodology, transfer restriction analysis, and ROFR navigation.

## When To Use

- Pricing founder, employee, or early-investor shares in a direct secondary purchase
- Structuring a company-sponsored tender offer or investor-led secondary block trade
- Evaluating discount-to-last-round pricing and whether implied valuation is defensible
- Navigating ROFR, co-sale, and transfer restriction mechanics before closing a secondary deal
- Benchmarking secondary pricing against 409A valuations, recent primary rounds, or comparable public multiples

## Inputs To Gather

- **Cap table snapshot**: Fully diluted share count, share classes, liquidation preferences, participation rights, and conversion ratios
- **Last primary round terms**: Price per share, pre/post-money valuation, date, and lead investor
- **Most recent 409A valuation**: Common stock FMV, valuation date, methodology used (OPM, PWERM, hybrid)
- **Transfer restriction documents**: Stockholders' agreement, ROFR provisions, co-sale rights, board consent requirements, company bylaws [VERIFY specific restriction language in governing docs]
- **Seller details**: Share class held, vesting status, holding period, grant date (for tax treatment analysis)
- **Company financials**: Trailing and projected revenue, EBITDA/burn rate, cash position, runway
- **Comparable transaction data**: Recent secondary market pricing (e.g., Forge, Nasdaq Private Market), comparable public company multiples

## Workflow

1. **Map the cap table and waterfall**
   - Build a fully diluted cap table including all option pools, warrants, SAFEs, and convertible notes
   - Model the liquidation waterfall at relevant exit values to determine per-share value by class
   - Calculate conversion economics — identify whether preferred converts or takes liquidation preference at target exit ranges

2. **Establish pricing methodology**
   - **Last-round benchmark**: Apply discount to last primary round PPS; typical secondary discounts range 10–30% depending on liquidity, information asymmetry, and time since round [VERIFY current market discount ranges]
   - **409A-anchored**: Use common stock FMV as floor; assess whether 409A methodology (OPM vs. PWERM) aligns with deal context
   - **Comparable multiples**: Apply revenue or EBITDA multiples from public comps or recent private transactions to derive enterprise value, then walk down the waterfall to per-share value
   - **Blended approach**: Weight multiple methods and document rationale for weighting

3. **Analyze transfer restrictions and ROFR mechanics**
   - Identify whether ROFR is held by the company, existing investors, or both [VERIFY governing document hierarchy]
   - Determine notice period, matching rights timeline, and waiver process
   - Flag co-sale (tag-along) rights that could expand the transaction scope
   - Confirm whether board consent is required and assess likelihood of approval
   - Check for lock-up provisions, market standoff agreements, or contractual holding periods

4. **Model transaction scenarios**
   - **Base case**: Agreed PPS at target discount with standard transfer mechanics
   - **ROFR exercise case**: Company or existing investors match — model impact on buyer allocation
   - **Partial fill case**: Seller offers X shares but ROFR claws back a portion — model net allocation
   - **Tender offer structure**: If company-sponsored, model participation caps, proration mechanics, and pricing uniformity requirements

5. **Run sensitivity analysis**
   - Sensitivity on discount-to-last-round (5% increments across 0–40% range)
   - Sensitivity on exit timing and exit multiple to show IRR and MOIC outcomes
   - Sensitivity on liquidation preference participation — show breakpoints where preferred converts vs. takes preference
   - Scenario table: bull / base / bear with key assumptions for revenue growth, margin trajectory, and exit multiple

6. **Assess tax and structural considerations**
   - Determine seller's tax treatment: long-term vs. short-term capital gains, QSBS eligibility [VERIFY holding period and Section 1202 requirements]
   - Flag whether transaction triggers Section 409A issues for option holders
   - Note any withholding or reporting obligations for company-facilitated transactions
   - If structuring as a forward contract or SPV wrapper, document rationale and additional complexity

## Output

- **Pricing summary**: Recommended PPS with methodology, discount applied, and implied fully diluted valuation
- **Waterfall analysis**: Per-share value by class at 3–5 exit scenarios
- **Transfer restriction memo**: ROFR timeline, consent requirements, and recommended process steps
- **Scenario matrix**: IRR and MOIC across discount levels and exit assumptions
- **Sensitivity tables**: Key variable ranges with clearly labeled base case
- **Transaction checklist**: Required approvals, notice deadlines, and document execution sequence

## Quality Checks

- Confirm fully diluted share count ties to the company's official cap table or transfer agent records — do not rely on outdated or partial data
- Verify that liquidation waterfall correctly handles participation caps, carve-outs, and pay-to-play provisions
- Cross-check implied valuation against last primary round, 409A, and public comps — flag outliers exceeding 20% divergence
- Ensure ROFR timeline and notice mechanics match the exact language in governing documents, not summary terms [VERIFY]
- Validate that discount assumptions are supported by observable secondary market data or documented negotiation rationale
- Confirm tax treatment analysis references current IRC provisions and accounts for state-level variations [VERIFY applicable state tax rules]
- Mark any assumption derived from management projections rather than audited financials with [VERIFY]
