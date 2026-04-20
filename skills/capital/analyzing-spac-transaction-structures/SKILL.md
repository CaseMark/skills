---
name: analyzing-spac-transaction-structures
language: en
description: Evaluates SPAC de-SPAC transaction economics with sponsor dilution, redemption risk, PIPE analysis, and warrant impact. Use when analyzing SPAC deals, evaluating sponsor economics, or modeling de-SPAC outcomes.
tags:
  - analysis
  - equity-capital-markets
  - risk
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
# Analyzing Spac Transaction Structures

Evaluates SPAC de-SPAC transaction economics with sponsor dilution, redemption risk, PIPE analysis, and warrant impact.

## When To Use

- Assessing a proposed de-SPAC business combination for a target company or investor
- Modeling sponsor economics (founder shares, promote structure, earnouts) to quantify dilution to public shareholders
- Evaluating redemption scenarios and their impact on trust value available at closing
- Analyzing PIPE commitments alongside trust proceeds to determine total cash-to-balance-sheet
- Reviewing warrant overhang and its effect on post-closing equity value per share
- Comparing a SPAC path-to-market against a traditional IPO or direct listing

## Inputs To Gather

- **SPAC IPO terms**: Trust size, unit composition (share + fraction of warrant), IPO price per unit, trust interest earned
- **Sponsor structure**: Number of founder shares, promote percentage, any sponsor forfeiture or earnout arrangements, sponsor warrants (private placement warrants)
- **De-SPAC deal terms**: Pro forma enterprise value, equity value, exchange ratio, earnout milestones if any
- **Redemption data**: Historical redemption rates for comparable SPACs, any non-redemption agreements or backstop commitments, minimum cash condition [VERIFY against definitive proxy]
- **PIPE details**: PIPE size, price per share, any discount or structural sweeteners (e.g., reset provisions, additional warrants), investor lock-up terms
- **Warrant terms**: Strike price, redemption triggers (e.g., $18.00 cashless redemption), expiration, diluted share count at exercise [VERIFY warrant agreement for make-whole or anti-dilution provisions]
- **Fee structure**: Deferred underwriting fees, advisory fees, transaction expenses held in trust or paid from operating cash

## Workflow

1. **Map the capital structure pre- and post-closing**
   - Build a sources-and-uses table: trust cash (net of redemptions), PIPE proceeds, rollover equity, any seller financing
   - Identify all share classes post-closing: public shares, founder shares (net of forfeitures), PIPE shares, earnout shares, public warrants, private placement warrants
   - Calculate fully diluted share count under treasury-stock method at various price levels ($10, $12, $15, $20)

2. **Quantify sponsor dilution**
   - Compute the sponsor promote as a percentage of post-closing equity at deal-price and at various share-price scenarios
   - If the sponsor has agreed to forfeit shares or convert to earnout shares, model the contingent dilution and the trigger thresholds
   - Compare effective sponsor economics to typical 20% promote benchmark and note any deviations

3. **Stress-test redemption scenarios**
   - Model low (10%), base (50%), and high (80%+) redemption cases
   - For each scenario, calculate remaining trust cash, total closing cash (trust + PIPE), and resulting cash-per-share to the combined entity
   - Identify the minimum cash condition threshold and flag whether high-redemption scenarios breach it [VERIFY minimum cash condition in the definitive agreement]
   - Note any non-redemption agreements or backstop arrangements that cap downside

4. **Evaluate PIPE terms and investor alignment**
   - Assess PIPE pricing relative to trust value ($10.00/share) and implied deal price
   - Flag structural features: price resets, make-wholes, convertible PIPEs, additional warrant coverage
   - Calculate PIPE investors' breakeven and effective discount to public shareholders
   - Review registration rights and lock-up period to gauge near-term selling pressure

5. **Analyze warrant overhang**
   - Calculate total warrants outstanding (public + private placement) and their dilutive impact at exercise
   - Model cashless-redemption scenarios if the SPAC has a forced-conversion feature at a share-price trigger
   - Estimate warrant overhang as a percentage of post-closing fully diluted shares and the dollar value of dilution at target share prices

6. **Compute implied valuation metrics**
   - Derive implied EV/Revenue, EV/EBITDA, and EV/target metric at the deal price, adjusting for sponsor dilution and warrant dilution
   - Compare to public-market trading comps and precedent de-SPAC transactions in the same sector
   - Sensitize valuation multiples across redemption scenarios to show the range of effective entry prices

## Output

- **Sources & Uses Table**: Clear breakdown of where closing cash comes from and how it is deployed
- **Dilution Waterfall**: Share-count bridge from trust shares through founder shares, PIPE shares, warrant exercises, and earnouts, showing dilution at each step
- **Redemption Sensitivity Matrix**: Grid showing trust cash remaining, total closing cash, cash-per-share, and implied valuation at low/base/high redemption rates
- **Sponsor Economics Summary**: Effective promote percentage, cost basis per founder share, and comparison to market norms
- **Warrant Impact Analysis**: Diluted share counts and value-per-share impact at multiple price scenarios
- **Valuation Comparison Table**: Implied multiples at deal price vs. sector comps, sensitized for redemptions and dilution
- **Key Risks & Flags**: Itemized list of structural risks (high redemption exposure, aggressive PIPE terms, outsized warrant overhang, near-term lock-up expirations)

## Quality Checks

- Verify that sources equal uses in the S&U table — any imbalance indicates a missing item
- Confirm fully diluted share count reconciles to the proxy filing's capitalization table [VERIFY against definitive proxy/S-4]
- Ensure redemption scenarios correctly reduce trust cash and public shares (not PIPE or founder shares)
- Check that warrant dilution is applied using treasury-stock method at each price point, not as a flat addition
- Validate PIPE terms against the subscription agreement — pricing, shares, and any reset or conversion features [VERIFY]
- Cross-check sponsor forfeitures or earnout triggers against the sponsor support agreement [VERIFY]
- Flag any assumption about trust interest, transaction expenses, or excise tax on redemptions that was estimated rather than sourced from filings
