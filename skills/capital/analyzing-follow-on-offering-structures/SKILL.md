---
name: analyzing-follow-on-offering-structures
language: en
description: Evaluates secondary offering types including overnight blocks, marketed deals, ATMs, and bought deals with dilution analysis. Use when analyzing follow-on options, structuring secondary offerings, or evaluating dilution impact.
tags:
  - analysis
  - equity-capital-markets
metadata:
  author: casemark
  practice_areas:
    - ECM
    - IPO Advisory
    - Equity Origination
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Follow On Offering Structures

## When To Use

- Issuer is evaluating capital-raising alternatives after IPO (primary follow-on) or existing holders seek liquidity (secondary follow-on)
- Comparing execution strategies: overnight/block trade, marketed deal, at-the-market (ATM) program, or bought deal
- Quantifying dilution impact, pricing dynamics, and net proceeds under different structures
- Advising on timing, discount expectations, and lock-up considerations for a proposed offering

## Inputs To Gather

- **Issuer profile**: current share price, market cap, average daily trading volume (ADTV), public float, and existing share count (basic and fully diluted)
- **Offering parameters**: target gross proceeds, primary vs. secondary split, selling shareholder identity and stake size
- **Capital structure**: outstanding convertible instruments, warrants, options, and anti-dilution provisions
- **Market context**: recent stock volatility (30/60/90-day), sector index performance, comparable recent follow-on transactions
- **Regulatory status**: shelf registration (S-3) availability, WKSI eligibility, Rule 144 holding periods for selling holders [VERIFY]
- **Contractual constraints**: existing lock-up agreements, registration rights obligations, co-sale or tag-along provisions

## Workflow

1. **Classify offering type and eligibility**
   - Determine if issuer qualifies as WKSI (public float ≥ $700M) or meets S-3 primary offering thresholds [VERIFY current SEC thresholds]
   - Identify whether the offering is primary (new shares), secondary (existing holder selling), or a combination
   - Check shelf registration capacity remaining and any SEC comment history

2. **Structure comparison matrix**
   - **Overnight/block trade**: best for secondary sales of 3-8% of float; execution in hours; typical discount 3-5% to last close; minimal market impact if sized within ~25% of ADTV; no roadshow
   - **Marketed deal (1-2 day)**: suits $100M+ offerings requiring price discovery; 1-2 day bookbuild with limited marketing; discount typically 4-7%; anchor investor targeting
   - **Fully marketed deal**: 5-10 day roadshow for larger or more complex stories; broadest investor reach; discount 5-8%; higher execution risk from market movement during marketing
   - **ATM program**: best for programmatic issuance over weeks/months; sold at market with no fixed discount; minimal per-trade impact if daily sales kept under 10-15% of ADTV; lower gross spread (typically 1-2% vs. 3-5% for underwritten)
   - **Bought deal**: bank commits firm capital at a fixed price; fastest certainty of execution; deepest discount (5-10%) to compensate underwriter risk; used when speed or price certainty is paramount

3. **Dilution analysis**
   - Calculate basic dilution: new shares / (existing shares + new shares)
   - Calculate fully diluted impact including in-the-money options, warrants, and convertibles using treasury stock method
   - Model EPS dilution at target proceeds for each structure scenario
   - Assess impact on existing holders' voting power and ownership percentage thresholds (e.g., 5%, 10%, 20% blockers)

4. **Pricing and discount analysis**
   - Pull comparable precedent transactions: same sector, similar market cap, same offering type, last 12-24 months
   - Compute median/mean file-to-offer discount, offer-to-close performance (day 1, 5, 30), and gross spread
   - Adjust for current market volatility — wider discounts in high-vol environments
   - Flag whether VWAP or last-close pricing is more appropriate given trading pattern

5. **Net proceeds and cost comparison**
   - For each structure: gross proceeds – underwriting discount – estimated legal/accounting fees – SEC filing fees = net proceeds
   - Compare all-in cost as percentage of gross proceeds across structures
   - For ATM: model cumulative proceeds and weighted average sale price over projected selling period

6. **Risk and timing assessment**
   - Market risk exposure: overnight (hours) vs. marketed (days) vs. ATM (weeks/months)
   - Signaling risk: primary issuance may signal overvaluation; secondary may signal insider selling
   - Regulatory timing: blackout periods around earnings, pending material events, Regulation M compliance [VERIFY]
   - Lock-up implications for selling shareholders and new lock-up requirements for the issuer

## Output

Deliver a structured analysis report containing:

- **Executive summary**: recommended offering structure with rationale (1-2 paragraphs)
- **Structure comparison table**: side-by-side matrix of each offering type with columns for typical discount, execution timeline, spread, marketing requirement, and suitability assessment
- **Dilution impact table**: basic and fully diluted share counts, EPS impact, and ownership percentage changes at target proceeds
- **Precedent transaction summary**: 5-10 comparable deals with key metrics (issuer, date, size, discount, aftermarket performance)
- **Net proceeds waterfall**: gross proceeds to net proceeds bridge for each structure
- **Risk matrix**: key risks by structure type with likelihood and mitigation strategies
- **Recommendation**: preferred structure with supporting rationale, including backup alternative if market conditions shift

## Quality Checks

- Verify share counts against most recent 10-Q/10-K and any subsequent 8-K filings reporting option exercises or conversions
- Confirm S-3 eligibility and remaining shelf capacity from the most recent shelf registration statement [VERIFY]
- Cross-check precedent discount data against actual pricing supplements (424B filings), not press releases alone
- Validate ADTV figures using a consistent 30-day lookback from the analysis date
- Ensure dilution calculations account for all convertible instruments, not just common shares outstanding
- Flag any reliance on stale data (>5 trading days old for market data, >1 quarter for financials) with [VERIFY]
- Confirm that ATM projections use realistic daily volume participation assumptions (typically 10-25% of ADTV ceiling)
