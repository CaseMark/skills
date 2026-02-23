---
name: child-support-worksheet
description: Drafts a Child Support Guidelines Worksheet for family law cases by extracting financial data from case documents, applying jurisdiction-specific guideline models (income shares, percentage of income), calculating gross/adjusted income, deductions, basic obligation, add-on expenses, proportionate shares, and deviation analysis. Use when preparing child support calculations, support modification filings, or guideline worksheets for court.
tags:
  - checklist
  - drafting
  - litigation
---

# Child Support Guidelines Worksheet

Produces a court-ready child support calculation worksheet compliant with the applicable state's guideline model and statutory requirements.

## Prerequisites

1. **Jurisdiction identified** — state whose guidelines apply; confirm guideline model (income shares, percentage of income, hybrid)
2. **Income documentation for both parents** — pay stubs, W-2s, 1099s, tax returns, financial affidavits, business records
3. **Children's information** — names, DOBs, residence, special needs or medical conditions
4. **Custody arrangement** — current order or proposed plan with parenting-time percentages
5. **Existing obligations** — prior child support or spousal support orders (case numbers, amounts)
6. **Child-related expenses** — childcare costs, health insurance premiums, extraordinary medical, education, extracurricular
7. **Court filing requirements** — local form mandates, caption format, filing procedures

## Output Structure

### Section 1: Case Caption & Party Information

Use jurisdiction's official form if mandated. Include:

| Field | Parent A | Parent B |
|-------|----------|----------|
| Full legal name | | |
| DOB | | |
| SSN (if required) | | |
| Address | | |
| Employer | | |
| Attorney (if any) | | |

List each child: name, DOB, current residence, special needs.

### Section 2: Gross Monthly Income

Calculate for each parent. Convert all figures to **monthly** amounts.

| Income Source | Parent A | Parent B | Notes |
|---------------|----------|----------|-------|
| Wages/salary | | | YTD ÷ months or annual ÷ 12 |
| Overtime | | | Apply jurisdiction's inclusion rules |
| Bonuses/commissions | | | Multi-year average if irregular |
| Self-employment (net) | | | Gross receipts minus ordinary/necessary business expenses only; exclude personal expenses, excessive depreciation |
| Rental income | | | |
| Investment/interest | | | |
| Retirement distributions | | | |
| Other income | | | |
| **Imputed income** | | | If voluntarily unemployed/underemployed — cite earning capacity basis |
| **Total Gross Monthly** | | | |

- Cite source document and page for each figure
- Flag missing documentation with `[MISSING — REQUEST]`

### Section 3: Allowable Deductions

| Deduction | Parent A | Parent B |
|-----------|----------|----------|
| Federal income tax | | |
| State income tax | | |
| FICA (Social Security + Medicare) | | |
| Mandatory retirement contributions | | |
| Health insurance (self only) | | |
| Pre-existing child support (case #) | | |
| Pre-existing spousal support (case #) | | |
| Other statutory deductions | | |
| **Total Deductions** | | |
| **Adjusted Gross Monthly Income** | | |

- Exclude voluntary retirement contributions unless jurisdiction permits
- Self-employed: calculate both employee + employer FICA portions

### Section 4: Basic Support Obligation

```
Combined Adjusted Gross Income:  $________
Number of children:              ________
Basic Support Obligation:        $________ (from guideline schedule, cite table/section)
```

- Verify guideline schedule effective date
- If income exceeds schedule maximum: apply jurisdiction's extrapolation method (extend percentage, flat rate, or judicial discretion standard) and document methodology

### Section 5: Additional Expenses

| Expense | Monthly Cost | Parent A Share (%) | Parent B Share (%) |
|---------|-------------|-------------------|-------------------|
| Work-related childcare | | | |
| Children's health insurance premium | | | |
| Extraordinary medical (uninsured) | | | |
| Private school/tutoring | | | |
| Extracurricular activities | | | |
| **Total Additional** | | | |

- Each parent's percentage = their adjusted income ÷ combined adjusted income
- Note whether jurisdiction adds these to basic obligation before apportioning or treats as separate add-ons

### Section 6: Proportionate Shares & Final Calculation

```
Parent A percentage:  ___% ($_____ ÷ $_____ combined)
Parent B percentage:  ___%

Total obligation (basic + additional):  $_____
Parent A share:                         $_____
Parent B share:                         $_____

Parenting time adjustment (if applicable): $_____

MONTHLY SUPPORT PAYMENT:  $_____ from [Parent _] to [Parent _]
Payment frequency:        Monthly, due the ___ of each month
Payment method:           [per local rules]
```

- Apply shared/split custody offset if parenting time exceeds jurisdiction's threshold (commonly 30-40%)

### Section 7: Health Insurance & Medical Allocation

- [ ] Designate parent ordered to maintain coverage
- [ ] Children's premium share: $___/month; credit to providing parent
- [ ] Uninsured expense split: ___% / ___%
- [ ] Threshold for shared expenses (e.g., first $250/year absorbed by custodial parent)
- [ ] Reimbursement procedure: submission deadline, documentation required, payment deadline
- [ ] Tax dependency allocation (note federal exemption elimination; check state benefits)

### Section 8: Deviation Analysis

Only if guideline amount is arguably unjust. Address:

| Deviation Factor | Applicable? | Evidence | Proposed Adjustment |
|-----------------|-------------|----------|-------------------|
| Extraordinary income disparity | | | |
| Child's special needs | | | |
| Significant parenting-time variance | | | |
| Child's independent resources | | | |
| Extraordinary debt for child's benefit | | | |
| Other statutory factor | | | |

- Cite statutory deviation provision: [VERIFY — jurisdiction-specific section]
- Presumption favors guideline amount; deviation requires clear justification
- Calculate proposed deviated amount with methodology explanation

### Section 9: Filing Checklist

- [ ] Official worksheet form used (if mandated)
- [ ] Case caption with court name, case number, parties
- [ ] All calculations shown step-by-step
- [ ] Guideline provisions and schedule sections cited
- [ ] Supporting exhibits attached (income docs, invoices, medical records)
- [ ] Signature blocks for both parents (and attorneys if represented)
- [ ] Declaration/certification under penalty of perjury (if required)
- [ ] Notarization (if required)
- [ ] Correct number of copies per local rules
- [ ] Filed as standalone or attached to motion per local practice

## Guidelines

- **Jurisdiction controls everything** — guideline model, schedule, deduction rules, deviation standards, and form requirements vary dramatically by state. Always confirm the current version of the guidelines.
- **Document every figure** — cite source document and page for each income/expense entry
- **Do not guess income** — if documentation is missing, flag it; do not fabricate figures
- **Self-employment scrutiny** — courts disallow personal expenses disguised as business deductions; apply the jurisdiction's standards for allowable business expenses
- **Imputation requires basis** — imputing income to an unemployed/underemployed parent requires evidence of earning capacity (work history, education, local wage data)
- **Mark uncertain citations** with `[VERIFY]` — child support statutes are frequently amended
- **FRE considerations** — financial affidavit statements may be admissions; ensure accuracy
- **Distinguish mandatory vs. voluntary** — only mandatory retirement contributions are deductible in most jurisdictions
