---
name: evaluating-sum-of-parts-activism
language: en
description: Assesses conglomerate break-up activism with segment valuation, separation feasibility, and tax-free qualification analysis. Use when evaluating SOTP activism, analyzing break-up proposals, or modeling separation value.
tags:
  - analysis
  - activist-and-event-driven-investing
  - valuation
  - tax
metadata:
  author: casemark
  practice_areas:
    - Activist Investing
    - Event-Driven Strategy
    - Special Situations
  document_types:
    - Evaluation Report
  skill_modes:
    - Analysis
    - Assessment
---
# Evaluating Sum Of Parts Activism

## When To Use

- An activist investor files a 13D or white paper advocating a conglomerate break-up, spin-off, or asset sale
- Evaluating whether a multi-segment company trades at a meaningful conglomerate discount
- Modeling the standalone value of individual business units versus the consolidated entity
- Assessing feasibility and timeline for a proposed separation (spin-off, split-off, carve-out, or asset sale)
- Determining whether a separation can qualify as tax-free under IRC §355 or requires a taxable structure

## Inputs To Gather

- **Segment financials**: Revenue, EBITDA, capital expenditure, and working capital by reportable segment (from 10-K segment disclosures and quarterly supplements)
- **Activist materials**: 13D filing, investor presentation, white paper, or public letter detailing the proposed break-up thesis
- **Peer trading data**: EV/EBITDA, EV/Revenue, and P/E multiples for pure-play comparables in each segment's industry
- **Precedent transactions**: Recent M&A multiples for similar businesses in each segment vertical
- **Corporate overhead allocation**: Shared services costs, corporate G&A, and intercompany transfer pricing arrangements
- **Capital structure details**: Debt covenants, change-of-control provisions, cross-default clauses, pension obligations, and guarantee structures
- **Tax basis information**: Inside basis of assets by segment, E&P history, and any prior §355 transactions within the past five years
- **Synergy and dissynergy estimates**: Revenue synergies at risk, shared procurement savings, and incremental standalone public-company costs (board, audit, IT, insurance)

## Workflow

1. **Compute the SOTP valuation**
   - Value each segment independently using a blended median of trading comps and precedent transaction multiples
   - Apply a range (e.g., 25th–75th percentile) to bracket valuation uncertainty per segment
   - Subtract net debt, pension/OPEB obligations, minority interests, and unallocated corporate costs from the aggregate segment value
   - Compare the resulting SOTP equity value to the current market cap to quantify the conglomerate discount (typically expressed as a percentage)

2. **Assess separation feasibility**
   - Map intercompany dependencies: shared IT systems, supply agreements, co-mingled manufacturing, cross-selling arrangements
   - Estimate one-time separation costs (IT carve-out, legal/advisory fees, branding, facility separation) and ongoing dis-synergies (duplicated overhead, lost procurement scale)
   - Identify stranded costs — corporate overhead that does not naturally migrate to any single segment
   - Review debt instruments for change-of-control triggers, consent requirements, and make-whole provisions that affect separation cost
   - Evaluate management bandwidth and board composition for running a separation while operating the business

3. **Analyze tax-free qualification (IRC §355)**
   - Confirm the distributing corporation has controlled the subsidiary for at least five years (the "control" requirement) [VERIFY against current §355(a)(1)(D) rules]
   - Verify both the distributing and controlled corporations have an active trade or business satisfying the five-year active-business test under §355(b) [VERIFY]
   - Assess whether a valid corporate business purpose exists (not merely shareholder-level tax avoidance)
   - Check device restrictions — whether the transaction is principally a device for distributing E&P (analyze asset composition, post-spin sale plans, and nature of consideration)
   - Evaluate continuity of interest and continuity of business enterprise requirements
   - Flag any §355(e) "plan or series of related transactions" risk if an acquisition of either entity is anticipated within two years pre- or post-spin
   - Determine whether a private letter ruling (PLR) will be sought or whether the transaction proceeds on opinion-only basis [VERIFY IRS current PLR policy for §355 transactions]

4. **Model value creation versus leakage**
   - Build a bridge from current market cap to post-separation aggregate value: SOTP uplift minus separation costs, tax friction (if taxable), dis-synergies, and incremental standalone costs
   - Sensitivity-test the discount closure: what percentage of the conglomerate discount must close to break even after all friction costs?
   - Model the timeline — typical spin-off execution takes 9–18 months from announcement to completion; factor in SEC Form 10 registration, IRS ruling timeline, and any required regulatory approvals

5. **Evaluate activist credibility and strategic alternatives**
   - Review the activist's track record with SOTP campaigns (win rate, timeline to outcome, typical discount closure achieved)
   - Assess the company's likely defensive response: accelerated capital return, portfolio review, strategic alternatives process, or governance concessions
   - Identify whether a negotiated settlement (board seats, capital allocation changes) could unlock partial value without full separation
   - Consider whether a third-party acquirer for individual segments is more likely than a spin-off

## Output

Produce an **SOTP Activism Evaluation Report** containing:

- **Executive summary**: Headline conglomerate discount, feasibility grade (High / Medium / Low), and tax-qualification preliminary assessment
- **Segment valuation table**: Each segment with revenue, EBITDA, applied multiple range, and implied enterprise value
- **Conglomerate discount calculation**: Aggregate SOTP value vs. current market cap with a clear walk from gross SOTP to net equity value
- **Separation feasibility matrix**: Key dependencies, estimated separation costs, timeline, and identified blockers
- **Tax-free qualification checklist**: Each §355 requirement with pass/fail/uncertain status and [VERIFY] flags for jurisdiction-dependent items
- **Value bridge**: Waterfall showing gross SOTP uplift, minus tax leakage, separation costs, dis-synergies, and incremental public-company costs, arriving at net value creation
- **Risk factors**: Top 3–5 risks to the thesis (regulatory, execution, market, management entrenchment)
- **Recommendation**: Probability-weighted expected value of the activism campaign relative to current share price

## Quality Checks

- Confirm all segment EBITDA figures reconcile to consolidated EBITDA after eliminations and unallocated corporate costs
- Verify that comparable company multiples are sourced from the same fiscal period and adjusted for non-recurring items
- Ensure tax-qualification analysis flags every element that depends on specific fact patterns with [VERIFY]
- Cross-check separation cost estimates against disclosed costs from recent comparable spin-offs (e.g., SEC filings of completed separations)
- Validate that the value bridge accounts for all friction costs — no "free" discount closure assumed
- Confirm debt covenant analysis reflects the most restrictive indenture or credit agreement terms currently in effect
