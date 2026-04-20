---
name: analyzing-comparable-transactions
language: en
description: Structures precedent transaction analysis with deal multiples, premium calculation, and transaction characteristic comparison. Use when analyzing M&A precedents, calculating transaction multiples, or benchmarking deal terms.
tags:
  - analysis
  - investment-banking
metadata:
  author: casemark
  practice_areas:
    - Investment Banking
    - Mergers and Acquisitions
    - Corporate Finance
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Comparable Transactions

## When To Use

- Building a precedent transactions analysis for a sell-side or buy-side pitch book
- Benchmarking a proposed offer price or premium against historical M&A deals
- Supporting a fairness opinion with transaction-based valuation evidence
- Evaluating deal structure trends (cash vs. stock, earnouts, termination fees) across a sector
- Providing a board or special committee with market context on comparable deal terms

## Inputs To Gather

- **Target description**: Industry, sub-sector, size (revenue, EBITDA, assets), geographic focus, and business model
- **Transaction universe parameters**: Date range (typically 5–10 years), sector/SIC/NAICS codes, minimum deal size threshold, geographic scope
- **Deal data per transaction**: Announcement and close dates, acquirer identity, transaction type (merger, asset purchase, tender offer, take-private), total enterprise value (TEV), equity value, consideration mix (cash/stock/mixed), premium to unaffected price (1-day, 30-day VWAP)
- **Financial metrics for targets**: LTM and NTM revenue, EBITDA, EBIT, net income, total assets, book value — sourced at announcement date
- **Deal-specific qualitative factors**: Strategic vs. financial buyer, competitive auction vs. negotiated sale, hostile vs. friendly, regulatory hurdles, break-up fee as % of TEV
- **Source priority**: SEC filings (merger proxies, 14D-9, S-4), Capital IQ, Bloomberg, Refinitiv, PitchBook; note if any metric is derived rather than disclosed [VERIFY]

## Workflow

1. **Define the screening criteria** — Set sector, size, date range, deal type, and geography filters. Start broad, then narrow. Document every filter applied and the rationale for inclusion/exclusion thresholds.

2. **Build the transaction universe** — Pull all deals matching the screen. Record acquirer, target, announcement date, close date, TEV, equity value, and consideration type. Exclude withdrawn/terminated deals unless specifically relevant to the analysis narrative.

3. **Normalize financial metrics** — For each target, collect LTM and NTM revenue, EBITDA, and EBIT as of the announcement date (not close date). Adjust for non-recurring items, stock-based compensation, or restructuring charges only where disclosed and material. Flag any calendarization assumptions [VERIFY].

4. **Calculate deal multiples** — Compute TEV/Revenue, TEV/EBITDA, TEV/EBIT, and P/E for each transaction. If EBITDA is negative or unavailable, exclude that deal from EBITDA-based metrics rather than imputing. Present mean, median, 25th and 75th percentiles for each multiple.

5. **Calculate premiums** — Compute premium to unaffected share price at 1-day, 1-week, and 30-day prior to announcement (or first leak date if pre-announcement run-up occurred). Use VWAP where possible. Note whether price was affected by rumors or sector moves [VERIFY].

6. **Segment and annotate** — Group transactions by meaningful sub-categories: strategic vs. financial buyer, deal size tier, pre- vs. post-regulatory-change periods, auction vs. negotiated. Identify outliers and provide deal-specific context (e.g., distressed sale, competitive bidding, synergy-driven premium).

7. **Derive valuation range** — Apply selected multiples (typically median and interquartile range) to the subject company's financials to produce an implied valuation range. Cross-reference premium analysis against the subject's current trading price.

8. **Contextualize and caveat** — Note market conditions at the time of each precedent (credit environment, sector cycle, index levels). Acknowledge survivorship bias, data gaps, and any transactions where reported multiples may reflect non-public adjustments.

## Output

- **Transaction summary table**: One row per deal — target, acquirer, date, TEV, equity value, consideration type, TEV/Revenue, TEV/EBITDA, TEV/EBIT, premium (1-day, 30-day)
- **Statistical summary**: Mean, median, 25th/75th percentiles for each multiple and premium metric, with and without identified outliers
- **Segmented analysis**: Sub-tables or charts breaking out multiples by buyer type, deal size, time period, or other relevant dimension
- **Implied valuation range**: Table mapping selected multiples to subject company metrics, showing low/mid/high implied TEV and equity value
- **Narrative commentary**: 1–2 paragraphs summarizing key takeaways — where the subject deal sits relative to precedents, what drives the range, and which comparables are most analogous

## Quality Checks

- Every transaction multiple ties back to disclosed or clearly sourced financials — no orphaned numbers
- TEV calculation is consistent across all deals (same treatment of minority interest, preferred, debt, cash) [VERIFY]
- Premium calculations use the correct unaffected date; verify no pre-announcement price distortion
- Mean vs. median divergence is explained if greater than 15–20%
- At least 5–8 transactions in the universe; if fewer, disclose the thin dataset limitation prominently
- NTM estimates use consensus as of the announcement date, not current consensus [VERIFY]
- All excluded transactions are listed with exclusion rationale
- Output distinguishes between LTM and NTM multiples — never mix without labeling
- Implied valuation range is presented on both a TEV and per-share basis where applicable
