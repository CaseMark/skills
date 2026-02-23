---
name: means-test-calculation
description: Calculates the bankruptcy means test by analyzing paystub data to determine annualized gross income and comparing it against applicable state median income thresholds by household size. Covers the 6-month look-back period, YTD subtraction method, pro-rata adjustments, and median income comparison. Use when evaluating Chapter 7 eligibility, performing pre-filing income assessment, or preparing Form 122A-1.
tags:
  - analysis
  - litigation
---

# Bankruptcy Means Test Calculation

Analyzes paystub data to calculate annualized gross income and determine whether the debtor falls under or over the applicable state median income for the bankruptcy means test.

## Prerequisites

1. **Filing date** of the bankruptcy petition (actual or projected)
2. **State of residence** of the debtor
3. **Household size** — number of individuals in debtor's household
4. **Paystubs** covering at least seven months prior to filing, including:
   - Pay period start/end dates and pay date
   - Gross pay per period
   - Year-to-date (YTD) gross pay
   - Deductions: federal withholding, state withholding, Social Security, Medicare

## Process

### Step 1: Determine 6-Month Look-Back Period

Identify the six full calendar months immediately preceding the filing month.

| Filing Month | Look-Back Period |
|---|---|
| October 2025 | April 1 – September 30, 2025 |
| November 2025 | May 1 – October 31, 2025 |

### Step 2: Calculate Total Gross Income for Look-Back Period

**Primary method — YTD subtraction:**

1. Last paystub YTD **before end** of look-back period → `YTD_end`
2. Last paystub YTD **before start** of look-back period → `YTD_start`
3. Total gross = `YTD_end - YTD_start`

**Pro-rata adjustment:** If a pay period straddles the look-back start date, pro-rate and deduct the portion falling outside the look-back window from the YTD figure.

**Fallback method** (if YTD unreliable): Sum gross pay from all paychecks with pay dates falling within the 6-month window.

### Step 3: Compute Annualized Income

```
Average monthly gross = Total gross ÷ 6
Annualized gross     = Average monthly gross × 12
```

### Step 4: Look Up State Median Income

- Use the Census Bureau / USTP median income table effective as of the filing date
- Match by **state** and **household size**
- For households > 4 persons: add $11,100 per additional person to the 4-person threshold [VERIFY — confirm current per-capita add-on amount from USTP tables]

### Step 5: Compare and Conclude

| Condition | Result |
|---|---|
| Annualized gross ≤ state median | **Under Median** — presumption of abuse does not arise; Chapter 7 eligible |
| Annualized gross > state median | **Over Median** — full means test (Form 122A-2) required |

## Required Output

Produce a summary table:

```
6-Month Look-Back Period:    [start date] – [end date]
Total Gross Income (6 mo):   $XX,XXX.XX
Average Monthly Gross:       $XX,XXX.XX
Annualized Gross Income:     $XX,XXX.XX
State Median (HH size X):    $XX,XXX.XX
Result:                      Under Median / Over Median
```

## Guidelines

- **Gross income only** for the initial median test — do not net out deductions
- If debtor is **over median**, flag that payroll deductions (federal/state withholding, FICA, Medicare) become relevant for the full means test under Form 122A-2
- Pay attention to **pay date vs. pay period** — the means test keys off income *received* during the look-back period
- Median income tables update periodically; always confirm the table version effective on the filing date
- For joint filings, combined household income of both spouses must be included regardless of whether filing jointly or individually
