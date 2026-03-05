---
name: generating-client-portfolio-reports
description: Creates client-facing portfolio reports with performance, allocation, commentary, and outlook. Use when producing client reports, preparing quarterly reviews, or creating portfolio summaries.
tags:
  - asset-management
  - portfolio
metadata:
  author: casemark
  practice_areas:
    - Portfolio Management
    - Asset Management
    - Wealth Management
  document_types:
    - Report
  skill_modes:
    - Analysis
---
# Generating Client Portfolio Reports

## When To Use

- Producing quarterly or annual client portfolio reviews
- Preparing ad-hoc performance summaries for client meetings or investment committee presentations
- Creating onboarding portfolio snapshots for new relationship managers
- Generating consolidated reports across multiple accounts or strategies for a single client household

## Inputs To Gather

- **Account/portfolio identifiers** — account numbers, strategy names, vehicle types (SMA, fund, trust)
- **Reporting period** — start/end dates, comparison periods (QoQ, YoY, since-inception)
- **Holdings and transactions** — current positions, cash flows (contributions, withdrawals, dividends, fees)
- **Benchmark selections** — primary and secondary benchmarks (e.g., S&P 500, Bloomberg Agg, blended 60/40)
- **Return data** — time-weighted returns (TWR) and/or money-weighted returns (MWR/IRR) as appropriate; gross-of-fee and net-of-fee figures
- **Client preferences** — level of detail, preferred asset-class taxonomy, any excluded sections, prior report for tone/format continuity
- **Market and macro context** — relevant economic data, central bank actions, sector themes for the commentary section

## Workflow

1. **Validate data completeness** — Confirm holdings reconcile to custodian records. Verify return calculations tie to the performance system. Flag any stale prices, missing corporate actions, or unreconciled cash with [VERIFY].

2. **Build the performance section**
   - Present returns for MTD, QTD, YTD, 1-year, 3-year, 5-year, and since-inception periods
   - Show gross and net returns side by side; state the fee methodology (accrued vs. deducted)
   - Include benchmark returns for the same periods and compute excess return (alpha)
   - For multi-account households, include composite-level and account-level views
   - [VERIFY] Return calculation methodology complies with GIPS standards if the firm claims GIPS compliance

3. **Construct asset allocation summary**
   - Current allocation by asset class (equities, fixed income, alternatives, cash)
   - Compare to target/policy allocation and prior-period allocation
   - Highlight meaningful drift (e.g., >2% from target) and any rebalancing actions taken
   - Provide sub-asset-class detail where useful (e.g., US large-cap vs. international developed vs. EM)

4. **Draft attribution and commentary**
   - Identify top contributors and detractors to performance (by sector, geography, or position)
   - Explain key portfolio decisions during the period (additions, trims, tactical shifts)
   - Connect decisions to market events — avoid generic statements; tie actions to specific catalysts
   - Keep tone factual and forward-looking; avoid hindsight framing ("we correctly predicted…")

5. **Write market outlook section**
   - Summarize the macro environment: GDP trajectory, inflation, rates, earnings
   - State the firm's or PM's positioning view and any anticipated allocation changes
   - Identify key risks and tail scenarios the portfolio is monitored against
   - Keep outlook concise (3–5 paragraphs); avoid speculative price targets

6. **Compile supplemental exhibits**
   - Holdings schedule with position sizes (% of portfolio and market value)
   - Transaction summary for the period (buys, sells, income received)
   - Fee schedule and fees charged during the period
   - Risk metrics if appropriate (standard deviation, Sharpe ratio, max drawdown, beta)

## Output

The final report should follow this structure:

- **Cover page** — client name, account(s), reporting period, firm branding
- **Executive summary** — 2–3 sentence portfolio overview with headline return and key takeaway
- **Performance summary table** — multi-period returns vs. benchmarks
- **Asset allocation chart and table** — current vs. target vs. prior period
- **Portfolio commentary** — attribution, decisions, rationale
- **Market outlook** — macro view and positioning
- **Appendices** — holdings detail, transactions, fee disclosure, risk statistics
- **Disclosures** — standard regulatory disclaimers, benchmark definitions, calculation methodology notes

## Quality Checks

- Returns match the performance system output to the basis point; no manual overrides without documentation
- Benchmark comparisons use the correct index and time period — mismatch is a common error
- Asset allocation percentages sum to 100% (handle rounding explicitly)
- Commentary is consistent with the data — do not describe "strong equity performance" if equities underperformed the benchmark
- Fee disclosure is accurate and compliant with ADV Part 2A brochure commitments [VERIFY]
- All [VERIFY] tags are resolved or escalated before client delivery
- Report passes firm compliance review for marketing rule (SEC Rule 206(4)-1) and performance advertising requirements [VERIFY]
- Prior-period data matches previously delivered reports — no unexplained restatements without a restatement notice
