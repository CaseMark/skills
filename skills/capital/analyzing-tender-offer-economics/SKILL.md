---
name: analyzing-tender-offer-economics
language: en
description: Evaluates tender offer structures with premium analysis, proration risk, and conditional tender strategies. Use when analyzing tender offers, calculating tender economics, or evaluating proration scenarios.
tags:
  - analysis
  - activist-and-event-driven-investing
  - risk
metadata:
  author: casemark
  practice_areas:
    - Activist Investing
    - Event-Driven Strategy
    - Special Situations
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Tender Offer Economics

Evaluates tender offer structures including premium/discount analysis, proration mechanics, conditional tender strategies, and expected-value modeling for event-driven investment decisions.

## When To Use

- A company or activist announces a tender offer (self-tender, third-party, or Dutch auction) and you need to quantify the trade
- Evaluating whether to tender shares, hold through expiration, or trade around the offer
- Modeling proration outcomes when the offer is oversubscribed or partial
- Comparing conditional vs. unconditional tender strategies
- Assessing odd-lot exemptions, back-end merger terms, or two-tier offer structures

## Inputs To Gather

- **Offer terms**: Price per share (or price range for Dutch auction), number of shares sought, minimum/maximum conditions, expiration date and extension provisions
- **Current market data**: Undisturbed price (pre-announcement), current trading price, 30/60/90-day VWAP, shares outstanding, public float
- **Ownership structure**: Top holders and known tender intentions, insider ownership, index fund holdings (typically do not tender), short interest
- **Conditions**: Minimum tender condition (e.g., majority of outstanding), financing condition, regulatory approvals, MAC clauses
- **Back-end terms**: If two-tier, what consideration applies to non-tendered shares; merger agreement terms if applicable
- **Timeline**: Offer launch date, initial expiration, any extension rights, expected regulatory review period [VERIFY against current SEC Rule 14e-1 timing requirements]

## Workflow

1. **Calculate the gross spread**
   - Gross spread = Offer price − Current market price
   - Annualize the spread: (Gross spread / Current price) × (365 / Days to expected close)
   - Compare offer premium to undisturbed price, 30-day VWAP, and 52-week high/low

2. **Model proration risk**
   - Estimate total shares likely tendered: start with float, subtract likely non-tenderers (index funds ~unlikely to tender in partial offers, insiders with lock-ups, short sellers)
   - Proration factor = Shares sought / Estimated shares tendered
   - If proration factor < 1.0, calculate blended return: (Proration % × Offer price) + ((1 − Proration %) × Expected back-end price)
   - Sensitivity-test proration at 60%, 70%, 80%, 90% participation rates

3. **Evaluate conditional tender strategies**
   - Odd-lot tenders (< 100 shares): determine if odd-lot exemption applies — if so, odd lots avoid proration [VERIFY: confirm offer documents specify odd-lot priority]
   - Conditional tenders: model the payoff if you set a minimum acceptance condition (e.g., "I tender only if proration ≥ 80%") — reduces downside if proration is severe but risks missing the offer entirely
   - Guaranteed delivery procedures: note deadlines for late tenders

4. **Assess deal-break/extension scenarios**
   - Probability-weight outcomes: (P(completion) × Tendered return) + (P(failure) × Post-break price)
   - Estimate post-break price using pre-announcement level, peer multiples, or stated activist floor
   - Factor in extension risk: each extension delays the annualized return; model 1–2 extensions

5. **Analyze two-tier and squeeze-out economics**
   - If back-end merger at same price: tender is economically neutral except for time-value
   - If back-end at lower price or uncertain: quantify the penalty for non-tender
   - Appraisal rights: note jurisdiction and whether appraisal arbitrage is viable [VERIFY: state appraisal statute — Delaware § 262 vs. other jurisdictions]

6. **Compile expected-value summary**
   - Build a scenario table: Bull (high proration, quick close), Base, Bear (low proration, extensions, or deal break)
   - Assign probabilities and calculate weighted expected return
   - Express as annualized return and absolute dollar P&L per share

## Output

- **Premium analysis table**: Offer price vs. undisturbed, VWAP, 52-week range — with percentage premiums
- **Proration sensitivity matrix**: Expected blended return at varying participation rates
- **Scenario-weighted expected value**: Bull / Base / Bear with probabilities, per-share returns, and annualized returns
- **Strategy recommendation**: Tender unconditionally, tender conditionally (with threshold), hold for back-end, or avoid — with rationale
- **Risk factors**: Key conditions that could alter the analysis (regulatory, financing, minimum condition waiver)
- **Timeline**: Key dates with days-to-close assumptions

## Quality Checks

- Confirm offer price and share counts match the Schedule TO or Offer to Purchase filing [VERIFY against SEC EDGAR filings]
- Validate that proration math accounts for shares sought, not total outstanding
- Ensure annualized return calculations use realistic close dates (not just the initial expiration)
- Cross-check odd-lot exemption applicability — not all tender offers include it
- Verify minimum condition threshold and whether the offeror has discretion to waive it
- Flag any regulatory approvals (HSR, CFIUS, sector-specific) that could delay or block completion [VERIFY]
- Confirm back-end merger terms are sourced from the definitive agreement, not press release summaries
