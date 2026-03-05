---
name: synthesizing-financial-statements
description: Analyzes 10-K/10-Q filings to extract key metrics, identify trends, and create structured YoY comparisons. Use when analyzing SEC filings, comparing financial statements, or tracking company financial trends.
tags:
  - synthesis
  - accounting
metadata:
  author: casemark
  practice_areas:
    - Financial Reporting
    - Audit
    - Accounting
  document_types:
    - Synthesis Report
  skill_modes:
    - Synthesis
---
# Synthesizing Financial Statements

## When To Use

- Comparing financial performance across two or more fiscal periods from 10-K or 10-Q filings
- Building a consolidated view of revenue, expenses, margins, and cash flow from SEC filings
- Preparing YoY or QoQ trend analysis for investment memos, audit workpapers, or board presentations
- Extracting key metrics from financial statements when the source data spans multiple documents or exhibits
- Identifying material changes, restatements, or reclassifications between reporting periods

## Inputs To Gather

- **SEC filings**: 10-K (annual) and/or 10-Q (quarterly) for each period under comparison — confirm the filing date and amendment status (e.g., 10-K/A)
- **Specific statements needed**: Income statement, balance sheet, cash flow statement, and statement of stockholders' equity
- **Period scope**: Define the comparison window (e.g., FY2023 vs. FY2024, or Q3 2024 vs. Q3 2025)
- **Segment or entity scope**: Whether analysis covers consolidated results only or includes segment-level breakdowns (check Item 7 / MD&A for segment reporting)
- **Accounting standards**: Confirm GAAP vs. IFRS basis; note any changes in accounting policies disclosed in the footnotes (ASC 606 adoption, lease standard changes, etc.)
- **Non-GAAP metrics**: Identify whether the user needs adjusted EBITDA, free cash flow, or other non-GAAP measures reported in earnings releases or MD&A

## Workflow

1. **Verify filing completeness**
   - Confirm each filing is the final version (check for /A amendments on EDGAR)
   - Confirm fiscal year-end date — not all companies use Dec 31
   - Note the auditor's opinion type (unqualified, qualified, adverse, disclaimer) from the audit report in the 10-K

2. **Extract core financial data**
   - Pull line items from each of the three primary statements (income, balance sheet, cash flow)
   - Record amounts exactly as stated; do not round until the output stage
   - Capture reported segment data if segment-level analysis is in scope
   - Extract non-GAAP reconciliation tables from MD&A or earnings supplements when requested

3. **Normalize and align**
   - Map line items across periods — watch for reclassifications (e.g., "Cost of revenue" renamed to "Cost of goods sold")
   - Convert all figures to a consistent unit (thousands, millions, or full dollars) — state the unit clearly
   - Align fiscal periods: if comparing companies with different fiscal year-ends, note the date mismatch explicitly
   - Flag any restatements or prior-period adjustments disclosed in the footnotes [VERIFY]

4. **Compute comparative metrics**
   - Calculate YoY or QoQ dollar change and percentage change for each line item
   - Derive key ratios: gross margin, operating margin, net margin, current ratio, debt-to-equity, return on equity, free cash flow conversion
   - Identify the top 3–5 drivers of material changes using MD&A commentary and footnote disclosures
   - Flag items with >10% period-over-period change for narrative explanation

5. **Structure the synthesis report**
   - **Header**: Company name, CIK, ticker, periods compared, filing types, currency, unit of measure
   - **Executive summary**: 3–5 bullet narrative of the most significant trends and changes
   - **Comparative tables**: Side-by-side income statement, balance sheet, and cash flow with change columns
   - **Key ratios table**: Margin, liquidity, leverage, and efficiency ratios for each period
   - **Material items narrative**: Explanation of significant variances, citing specific footnote or MD&A references
   - **Segment breakdown** (if applicable): Revenue and operating income by segment with change analysis
   - **Flags and open items**: Any [VERIFY] markers, data gaps, or items requiring human review

6. **Validate against source**
   - Cross-check totals: net income on the income statement should tie to the cash flow statement's starting figure
   - Confirm balance sheet balances (total assets = total liabilities + equity)
   - Verify that computed ratios are mathematically consistent with the extracted figures
   - Ensure no line items were omitted from comparative tables

## Output

The synthesis report should include:

- **Comparative financial tables** with absolute and percentage changes, clearly labeled with periods and units
- **Ratio dashboard** covering profitability, liquidity, solvency, and efficiency metrics
- **Variance narrative** explaining material changes with citations to specific filing sections (e.g., "Per Note 4 to the FY2024 10-K...")
- **[VERIFY] flags** on any figures that could not be confirmed, involved estimates, or depend on accounting policy elections that vary by jurisdiction or standard [VERIFY]
- **Scope limitations** section noting any excluded items, data gaps, or assumptions made during normalization

## Quality Checks

- All extracted figures trace directly to a specific page or exhibit in the source filing — no unsourced numbers
- Dollar changes and percentage changes are arithmetically correct (spot-check at least 5 line items)
- Balance sheet equation holds for every period presented
- Net income on the income statement reconciles to the starting line of the cash flow statement
- Non-GAAP figures tie back to the company's own reconciliation tables — do not create independent non-GAAP adjustments
- Fiscal period labels are accurate (e.g., do not label a 10-Q figure as annual)
- Any change in accounting policy or restatement is called out in the variance narrative, not buried in a footnote
- Report does not present inferred or estimated data as confirmed — all assumptions are explicitly marked
