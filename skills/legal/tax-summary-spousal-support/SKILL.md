---
name: tax-summary-spousal-support
description: Analyzes tax returns, W-2s, 1099s, K-1s, and business filings to produce structured financial summaries for spousal support proceedings. Extracts income sources, deductions, tax liabilities, and multi-year trends to illuminate financial capacity, ability to pay, or need for support. Use when preparing financial analyses for discovery, pre-trial, settlement negotiations, or court filings in family law matters involving alimony or maintenance.
tags:
  - analysis
  - litigation
  - summarization
  - summary
---

# Tax Summary for Spousal Support

Produces a structured financial analysis from tax records to support spousal support determinations in family law proceedings.

## Prerequisites

1. **Tax returns** — Federal (Form 1040) and state returns for 2–3 most recent years minimum
2. **Income documents** — W-2s, 1099s (all types), K-1s, Schedule C/E/F as applicable
3. **Business returns** — Partnership (1065), S-Corp (1120-S), or C-Corp (1120) if party owns business interests
4. **Party identification** — Specify whether analysis covers petitioner, respondent, or both
5. **Jurisdiction** — State governing spousal support calculation (affects income definitions)

## Output Structure

### 1. Executive Overview

| Metric | Year 1 | Year 2 | Year 3 | Trend |
|--------|--------|--------|--------|-------|
| Gross Income (all sources) | | | | ↑/↓/→ |
| Adjusted Gross Income | | | | |
| Taxable Income | | | | |
| Total Tax Liability (fed + state) | | | | |
| Effective Tax Rate | | | | |
| Net After-Tax Income | | | | |

### 2. Income Source Breakdown

For each year, itemize:

| Source | Amount | % of Total | Form/Line Reference |
|--------|--------|-----------|---------------------|
| Wages/salary (W-2) | | | |
| Self-employment (Sch C) | | | |
| Business distributions (K-1) | | | |
| Rental income (Sch E) | | | |
| Interest/dividends (Sch B) | | | |
| Capital gains (Sch D) | | | |
| Retirement distributions | | | |
| Other (specify) | | | |

### 3. Tax Liability Analysis

- Federal and state obligations separately
- Effective vs. marginal rates
- Significant credits (child tax credit, earned income, etc.)
- Estimated tax payments and withholding patterns
- AMT exposure if applicable

### 4. Deductions and Adjustments

| Deduction | Amount | Support-Relevant? | Notes |
|-----------|--------|--------------------|-------|
| Retirement contributions | | Yes — reduces cash but builds assets | |
| Health insurance (self-employed) | | Yes — mandatory expense | |
| Business expenses | | Review for personal benefit | |
| Mortgage interest | | Lifestyle indicator | |
| Charitable contributions | | Discretionary capacity | |
| Depreciation | | **Not actual cash outflow** | |

### 5. Business Income Reconciliation (if applicable)

For self-employed parties or business owners, reconcile:

- **Reported taxable income** vs. **actual economic benefit**
- Add back: depreciation, amortization, one-time write-offs, personal expenses run through business
- Identify: owner perks (vehicle, travel, meals, insurance, retirement funded by entity)
- Retained earnings and distributions vs. salary
- Cash flow available vs. tax-reported income

### 6. Multi-Year Trend Analysis

- Income trajectory (growth, decline, volatility)
- Changes in filing status and their tax impact
- Shifts in income composition (e.g., W-2 to 1099 transition)
- Marital standard of living indicators from expenditure patterns

### 7. Observations and Flags

- [ ] Inconsistencies between reported income and lifestyle
- [ ] Unusual deductions or sudden changes in deduction patterns
- [ ] Unreported or underreported income indicators
- [ ] Hidden income through entity structures
- [ ] Areas requiring forensic accounting or expert testimony
- [ ] Missing documentation gaps

## Guidelines

- **Tax income ≠ support income**: Courts often define income for support differently than the IRS. Depreciation, accelerated deductions, and pre-tax retirement contributions may be added back for support calculations. Flag these adjustments explicitly.
- **Source attribution required**: Cite specific tax year, form, and line number for every figure (e.g., "2024 Form 1040, Line 9: $185,000").
- **Filing status transitions**: Note the shift from MFJ to MFS/Single/HoH and quantify the tax liability difference — this directly affects disposable income post-separation.
- **Imputed income**: If voluntarily underemployed or income appears suppressed, note the basis for potential imputation but do not calculate — flag for attorney review.
- **Confidentiality**: All financial data is protected under applicable discovery rules. Note any documents produced under protective order.
- **Limitations**: Clearly state what documents were unavailable and how gaps affect the analysis. Recommend specific additional documents that would strengthen the summary.
- **Neutral tone**: Present findings objectively regardless of which party the analysis serves. Advocacy framing is counsel's role.
