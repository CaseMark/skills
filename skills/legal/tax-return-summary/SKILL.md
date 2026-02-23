---
name: tax-return-summary
description: Analyzes tax returns (Form 1040, schedules, W-2s) to produce structured legal summaries with cited line numbers for divorce, personal injury, and bankruptcy cases. Extracts income sources, deductions, credits, and flags red flags like income manipulation or unreported sources. Use when summarizing tax returns, analyzing financial discovery, assessing earning capacity, reviewing 1040s, or preparing financial profiles for litigation.
tags:
  - analysis
  - litigation
  - summarization
  - summary
---

# Tax Return Summary for Legal Analysis

Produces a structured, citation-backed summary of tax returns for use in divorce, personal injury, and bankruptcy proceedings.

## Prerequisites

1. **Uploaded tax returns** — Form 1040s, all filed schedules, W-2s, 1099s for each year under review
2. **Case type identified** — divorce/family law, personal injury, or bankruptcy
3. **Years in scope** — which tax years to analyze and compare

## Process

Search all uploaded documents to locate returns, schedules, and supporting forms. Extract figures directly from source materials. Cite every amount as `(Form [X], Line [Y])` so attorneys can verify.

### Section 1: Executive Financial Overview

Write a synthesized narrative (not a data dump) covering:

| Element | Detail |
|---|---|
| Primary income sources | Wages, business, investments — rank by magnitude |
| Income trajectory | Stable, growing, declining, or volatile across years |
| Filing status pattern | Note any changes signaling life events |
| Material deductions/credits | Items significantly affecting liability or true economic position |
| Immediate red flags | Inconsistencies, anomalies, or items requiring attorney attention |

### Section 2: Multi-Year Comparison

When multiple years are in scope, trace the financial evolution year over year:

- Filing status, AGI, taxable income, and total tax liability per year
- Calculate and explain significant year-over-year percentage changes
- Filing status transitions (e.g., MFJ → HOH) and their implications
- Dependent changes and relevance to custody/support
- Schedule C swings — explore underlying expense/revenue shifts
- Sporadic items: large capital gains, unusual charitable deductions, early retirement distributions (limit to 3–5 key observations per year)

### Section 3: Current Year Profile

Establish foundational facts for the primary tax year:

- **Tax year and filing status**
- **Taxpayer identification** — full legal name per Form 1040, last four of SSN
- **Dependents** — name, age, relationship, last four SSN, notable indicators (education credits suggesting student status, elderly parent suggesting financial support obligations)
- **Occupation** — per return and W-2/Schedule C; describe all income streams and their relative contribution

### Section 4: Income Source Analysis

Analyze each income category in narrative form with citations:

| Source | Form/Schedule | Key Analysis Points |
|---|---|---|
| Wages | 1040 Line 1, W-2s | Employer breakdown, YOY changes, job changes |
| Self-employment | Schedule C | Gross receipts, major expense categories, scrutinize vehicle/travel/home office/family payments, profit vs. lifestyle disconnect |
| Investment income | Schedule B, D | Interest, dividends, capital gains/losses; asset ownership implications |
| Rental income | Schedule E | Per-property gross rents, expenses, net; note depreciation masking positive cash flow |
| Pass-through entities | Schedule E (K-1s) | Partnership/S-corp/trust interests as potential marital or creditor-reachable assets |
| Retirement income | 1040 Lines 4–5 | Regular vs. premature distributions; financial stress indicators |
| Other | 1040 Lines 7–8 | Unemployment, alimony received, misc. sources |

### Section 5: Deductions and Credits

- **Standard vs. itemized** — note which and what it reveals
- **Schedule A breakdown** — mortgage interest (debt level inference), SALT, charitable (discretionary income signal), medical (health/unreimbursed cost indicator)
- **Self-employment deductions** — SE tax, health insurance, retirement contributions
- **Credits** — Child Tax Credit, EITC (income-level indicator), education credits (college expenses), Child/Dependent Care Credit (childcare costs relevant to support)

### Section 6: Red Flags

Flag issues in measured, professional language — describe the concern and its significance without accusing:

- [ ] Significant income drops coinciding with litigation commencement
- [ ] Schedule C expense inflation or personal expenses run through business
- [ ] Lifestyle/income mismatch suggesting unreported income
- [ ] Known income sources missing from returns
- [ ] Discrepancies between returns and loan applications, financial affidavits, or other discovery
- [ ] Income timing manipulation (deferred bonuses, shifted entity structures)
- [ ] New entity formation during litigation period
- [ ] Sudden shift from distributions to salary (S-corp strategy)

### Section 7: Legal Implications and Next Steps

Tailor conclusions to case type:

**Divorce/Family Law:**
- Income available for support calculations
- Assets revealed (investment accounts, rental properties, business interests) for marital estate
- Tax filing strategies requiring settlement attention (filing status, dependent claims)

**Personal Injury:**
- Pre-injury earning history and capacity baseline
- Post-injury income decline quantified with connection to claimed injuries
- Disability income or benefits on subsequent returns
- Medical expense deductions suggesting pre-existing conditions

**Bankruptcy:**
- Means testing inputs
- Income sources subject to creditor claims
- Preferential transfers or unusual pre-filing asset dispositions
- Undisclosed income/assets risk

**All Cases — Recommended Follow-Up:**

| Finding | Recommended Discovery |
|---|---|
| Understated business income | Bank statements, P&L, balance sheets |
| Inconsistent investment income | Brokerage statements via subpoena |
| Aggressive deductions | Supporting documentation request |
| Precipitous income decline | Employment verification, vocational analysis |
| Complex entity structures | Forensic accountant / business valuator |

Close with a clear roadmap: what the returns **definitively establish**, what they **suggest but do not prove**, and what **questions remain**.

## Guidelines

- Cite every figure as `(Form [X], Line [Y])` — summaries must withstand verification
- Maintain objectivity; present facts and observations, reserve legal conclusions for attorneys
- Format output with section headings, clean paragraph breaks, suitable for PDF/Word download and inclusion in case files
- When business shows tax loss but positive cash flow (due to depreciation), explicitly note the distinction
- Do not assume figures — extract only from uploaded documents
- Flag items needing additional documentation rather than speculating on explanations
