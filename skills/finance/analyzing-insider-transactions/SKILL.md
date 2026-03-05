---
name: analyzing-insider-transactions
description: Structures insider trading analysis with pattern identification and significance assessment. Use when tracking insider activity, analyzing Form 4 filings, or evaluating insider buying/selling patterns.
tags:
  - analysis
  - equity-research
  - trading
metadata:
  author: casemark
  practice_areas:
    - Equity Research
    - Investment Management
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Insider Transactions

## When To Use

- Evaluating insider buying or selling clusters ahead of earnings, catalysts, or corporate events
- Screening Form 4 filings for actionable signals across a watchlist or sector
- Building conviction around a long/short thesis using insider activity as confirming or contradicting evidence
- Monitoring C-suite and director transaction patterns for governance or activist-investing research
- Assessing whether insider selling reflects routine diversification versus informed pessimism

## Inputs To Gather

- **Ticker(s) / Company identifiers** — single name or portfolio-level screen
- **Time window** — lookback period (e.g., 90 days, 1 year, custom range)
- **Filing data source** — SEC EDGAR Form 4 filings, third-party aggregators (e.g., OpenInsider, InsiderMonkey, Bloomberg OWNR)
- **Insider scope** — all insiders, officers only, directors only, 10%+ beneficial owners
- **Transaction types of interest** — open-market purchases, open-market sales, option exercises, gifts, 10b5-1 plan transactions
- **Context data** — recent earnings dates, blackout window calendars, stock price history, compensation disclosures (DEF 14A)
- **Benchmark** — sector/peer insider activity for relative comparison

## Workflow

1. **Extract filings** — Pull Form 4 data for the target company/companies within the specified window. Record for each transaction: filer name, title/relationship, transaction date, transaction code (P, S, M, G, etc.), shares transacted, price, shares owned post-transaction, and whether a 10b5-1 plan is indicated.

2. **Classify transactions** — Separate into categories:
   - Open-market purchases (Code P) — highest signal value
   - Open-market sales (Code S) — moderate signal; context-dependent
   - Option exercises and same-day sales (Code M + S) — generally low signal (compensation-driven)
   - Gifts (Code G) and private transactions (Code J, K) — typically noise for trading purposes
   - Planned 10b5-1 sales — lower signal; flag but de-weight

3. **Identify patterns** — Look for:
   - **Cluster buying/selling** — 3+ insiders transacting in the same direction within 30 days
   - **Magnitude** — transaction size relative to insider's existing holdings (>10% of position = meaningful)
   - **Dollar significance** — absolute dollar value of purchases/sales; purchases > $100K by officers carry more weight [VERIFY: adjust threshold for company market cap]
   - **Role weighting** — CEO/CFO transactions > VP-level > directors > 10% owners for information asymmetry
   - **Timing** — proximity to earnings, FDA decisions, M&A announcements, or end of blackout windows
   - **Reversal of pattern** — insider who has only sold for years begins buying, or vice versa

4. **Contextualize** — Evaluate each pattern against:
   - Stock price performance leading into the transactions (buying after a sell-off vs. buying at highs)
   - Compensation structure — heavy stock-based comp creates natural selling pressure that is not bearish
   - Liquidity events — IPO/SPAC lock-up expirations, estate planning, divorce
   - Peer comparison — is insider buying unusual for this sector, or is it sector-wide?
   - Regulatory filings — check 13D/13G amendments for activist accumulation

5. **Score and rank** — Assign a signal-strength rating to each transaction cluster:
   - **Strong bullish** — multiple officers buying open-market, material size, no 10b5-1, near 52-week low
   - **Moderate bullish** — single officer purchase, meaningful size, no planned sale offset
   - **Neutral** — routine 10b5-1 selling, option exercises, small transactions
   - **Moderate bearish** — cluster selling by officers outside of 10b5-1, especially after run-up
   - **Strong bearish** — CEO/CFO selling large portions of holdings, accelerating 10b5-1 plan amendments, multiple officers exiting simultaneously

6. **Synthesize** — Summarize the overall insider sentiment for the company with a clear directional conclusion or "insufficient data" determination.

## Output

Structure the analysis report with these sections:

- **Summary** — One-paragraph insider sentiment overview with signal rating and key takeaway
- **Transaction table** — Tabulated filing data sorted by date, with columns: Date, Insider, Title, Type, Shares, Price, Value, Post-Txn Holdings, 10b5-1 Flag
- **Pattern analysis** — Narrative identifying clusters, outliers, and role-weighted signals
- **Contextual factors** — Compensation structure, blackout windows, price action, peer benchmarking
- **Signal assessment** — Overall rating (Strong Bullish / Moderate Bullish / Neutral / Moderate Bearish / Strong Bearish) with reasoning
- **Limitations** — Data gaps, caveats on 10b5-1 opacity, lag between transaction and filing dates [VERIFY: SEC requires Form 4 filing within 2 business days of transaction]

## Quality Checks

- Confirm all Form 4 transaction codes are correctly classified — do not conflate option exercises (M) with open-market purchases (P)
- Verify that 10b5-1 plan indicators are captured; omitting this flag inflates bearish signal from routine sales
- Cross-check transaction dates against earnings blackout windows [VERIFY: company-specific blackout policy if available]
- Ensure dollar values are calculated using the actual transaction price from the filing, not the closing price on that date
- Validate that "shares owned post-transaction" figures are consistent across sequential filings for the same insider
- Flag any late filings (filed beyond the 2-business-day deadline) as potential compliance concerns worth noting
- Do not present insider transaction analysis as a standalone investment recommendation — frame as one input within a broader thesis
