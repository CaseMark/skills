---
name: modeling-merger-arbitrage-spreads
language: en
description: Calculates merger arb risk/reward with annualized spread, deal break probability, and downside scenario analysis. Use when analyzing merger arb, calculating spread returns, or evaluating deal completion probability.
tags:
  - modeling
  - activist-and-event-driven-investing
  - risk
metadata:
  author: casemark
  practice_areas:
    - Activist Investing
    - Event-Driven Strategy
    - Special Situations
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Merger Arbitrage Spreads

## When To Use

- Evaluating risk/reward on an announced merger or acquisition before entering an arb position
- Sizing existing positions by quantifying annualized return vs. deal-break downside
- Comparing multiple pending deals to allocate capital across a merger arb book
- Stress-testing a deal's attractiveness under varying close timelines or regulatory outcomes
- Reviewing a deal after material developments (amended terms, regulatory challenge, competing bid)

## Inputs To Gather

- **Deal terms**: Offer price (cash, stock, or mixed consideration), exchange ratio (if stock deal), collar provisions, CVRs or earnouts, election mechanics
- **Current market prices**: Target current trading price, acquirer current price (for stock deals)
- **Timeline**: Announcement date, expected close date, outside date / drop-dead date, key regulatory milestones (HSR expiry, EC Phase I/II deadlines, CFIUS review windows) [VERIFY jurisdiction-specific regulatory timelines]
- **Deal break probability estimate**: Base rate from comparable deal universe, adjusted for deal-specific factors (regulatory risk, financing conditions, shareholder vote risk, MAC clause breadth)
- **Downside price (deal-break scenario)**: Target's unaffected pre-announcement price, comparable trading multiples, analyst consensus standalone valuation
- **Financing & cost of carry**: Borrow cost for short leg (stock deals), dividend expectations on both legs, margin/capital requirements
- **Risk-free rate**: Current Treasury yield matching expected deal duration for annualization benchmark

## Workflow

1. **Calculate gross spread**
   - Cash deal: `(Offer Price − Target Price) / Target Price`
   - Stock deal: `(Exchange Ratio × Acquirer Price − Target Price) / Target Price`
   - Mixed consideration: weight cash and stock components proportionally
   - Adjust for dividends receivable/payable during holding period and short borrow costs (stock deals)

2. **Annualize the spread**
   - Estimate days to close from current date to expected completion
   - `Annualized Spread = Gross Spread × (365 / Days to Close)`
   - Flag deals where annualized spread is below risk-free rate as potentially mispriced or low-risk consensus deals

3. **Estimate deal break probability**
   - Start with historical base rate for deal type (e.g., strategic cash deals ~3-5%, cross-border with antitrust review ~8-15%) [VERIFY against current deal completion databases]
   - Adjust upward/downward for: regulatory complexity, financing conditionality, bidder strategic commitment, target board unanimity, shareholder composition, litigation risk
   - Document the rationale for each adjustment explicitly

4. **Model downside scenario**
   - Determine target's standalone value absent the deal (pre-announcement price, peer-group multiples, DCF if available)
   - `Downside Loss = (Target Price − Standalone Value) / Target Price`
   - For stock deals, also estimate acquirer price recovery on deal break (acquirer often rises)

5. **Calculate expected return**
   - `Expected Return = (Probability of Close × Gross Spread) − (Probability of Break × Downside Loss)`
   - `Annualized Expected Return = Expected Return × (365 / Days to Close)`
   - Compare against hurdle rate and portfolio opportunity cost

6. **Run sensitivity analysis**
   - Vary deal break probability in increments (e.g., 5%, 10%, 15%, 20%, 30%)
   - Vary days to close (base case, +30 days, +90 days for regulatory delay)
   - Vary downside price (−5%, −10%, −15% from current standalone estimate)
   - Identify breakeven deal break probability where expected return = 0

7. **Assess deal-specific risk factors**
   - Antitrust: market concentration, overlapping product lines, jurisdiction (DOJ/FTC, EC, CMA, SAMR) [VERIFY relevant regulatory bodies]
   - Financing: committed vs. uncommitted financing, market conditions, material adverse change triggers
   - Shareholder vote: required approval thresholds, activist or dissenting shareholder positions
   - Competing bids: likelihood of topping bid, break-up fee magnitude as % of deal value

## Output

- **Spread summary table**: Current spread (%), annualized spread (%), days to expected close, gross P&L per share
- **Probability-weighted return**: Expected return at base-case break probability, annualized
- **Sensitivity matrix**: Grid showing annualized expected return across break probability × days to close combinations
- **Breakeven analysis**: Deal break probability at which expected return reaches zero
- **Risk factor scorecard**: Qualitative assessment (Low / Medium / High) for each major risk category with brief rationale
- **Position sizing implication**: Suggested position weight relative to portfolio given Kelly-style or risk-parity framework (flagged as illustrative, not a recommendation)

## Quality Checks

- Verify that gross spread calculation matches observable market data (cross-check with broker or data terminal quotes)
- Confirm annualized spread uses calendar days and accounts for any known interim milestones that may accelerate or delay close
- Ensure downside estimate is grounded in pre-announcement trading levels or fundamental valuation, not arbitrary haircuts
- Check that deal break probability adjustments are directionally consistent and documented with reasoning
- Validate that sensitivity ranges cover plausible tail scenarios, not just narrow base-case variations
- For stock deals, confirm exchange ratio type (fixed vs. floating) and collar bounds are correctly modeled [VERIFY deal-specific merger agreement terms]
- Flag any assumption that relies on a single data source or undisclosed estimate with [VERIFY]
