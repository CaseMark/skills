---
name: economic-loss-report
description: >-
  Generates a comprehensive Lost Wage & Economic Loss Report for personal
  injury litigation, calculating past lost wages, future lost wages,
  diminished earning capacity, medical expenses, and other out-of-pocket
  costs. Reviews case documents to extract facts, identifies information gaps,
  and structures defensible calculations with employer verification and
  present-value projections. Use when quantifying economic damages for
  plaintiff-side personal injury matters during discovery, pre-trial, or
  settlement phases. Trigger keywords: lost wages, economic damages, earning
  capacity, wage loss, medical expenses, damages calculation, personal injury
  damages.
tags:
  - analysis
  - litigation
  - summarization
  - summary
---

# Lost Wage & Economic Loss Report

Calculates all economic damages sustained by a claimant in a personal injury matter, structured to withstand scrutiny from opposing counsel, insurance adjusters, expert witnesses, and the court.

## Prerequisites

1. **Medical records** — diagnoses, treatment notes, prognosis, work restrictions, physician opinions on permanency
2. **Employment/wage records** — pay stubs (12-24 months pre-injury), W-2s, tax returns, employer verification letters
3. **Medical bills** — itemized bills, EOBs, payment records, receipts
4. **Incident documentation** — date, location, nature of injury-causing event
5. **Expert reports (if available)** — vocational evaluations, life care plans, economist reports

## Output Structure

### 1. Introduction & Claimant Profile

| Element | Details |
|---------|---------|
| Claimant identity | Full name, DOB, contact |
| Incident | Date, location, nature, parties |
| Injuries | All diagnoses, treatment timeline, current status, prognosis |
| Permanent impairments | Work restrictions with direct physician quotes and citations |
| Scope | Time periods covered; distinguish past vs. future losses |

Cite source document and page for every fact. Flag missing information for follow-up discovery.

### 2. Employment History & Pre-Injury Earnings

Extract from pay stubs, W-2s, tax returns, employer letters, and contracts:

| Component | Method |
|-----------|--------|
| Base wage/salary | Document rate + effective dates of raises |
| Overtime | Average from 12-24 month pre-injury period, month-by-month |
| Bonuses/commissions | Payment patterns and amounts |
| Benefits value | Health insurance premiums, retirement contributions, other |
| Secondary income | Any affected side employment |

**Output a monthly/quarterly earnings table** with columns: Period | Base | Overtime | Bonus/Commission | Total

Note seasonal variations, advancement trajectory (performance reviews, promotion history).

### 3. Past Lost Wages

Calculate from date of injury through present (or MMI date):

```
Net Lost Wages = "But-For" Earnings − Actual Earnings Received
```

**"But-for" earnings per period include:**
- Regular wages at normal schedule
- Predictable overtime (from historical patterns)
- Scheduled raises / COLAs
- Expected bonuses/commissions

**Offsets to subtract:**
- Modified-duty wages
- STD/LTD payments
- Workers' comp TD payments
- Alternative employment earnings

**Output table:** Month/Quarter | But-For Earnings | Actual Earnings | Net Lost Wages | Running Total

**Additional line items:**
- Lost employer health insurance (replacement cost)
- Lost retirement contributions
- Lost PTO, life insurance, other benefits
- Tax implications (gross vs. net per jurisdiction)

Flag any estimated periods and state the basis for estimation.

### 4. Future Economic Loss & Diminished Earning Capacity

| Factor | Source |
|--------|--------|
| Work-life expectancy | Age, occupation, pre-injury health |
| Recovery timeline | Treating physician opinions |
| Permanent restrictions | Medical records, vocational expert |
| Post-injury earning capacity | Vocational assessment, labor market data |

**For temporary future losses:** Project duration from medical opinions; apply same methodology as past wages with growth factors.

**For permanent diminished capacity:**
```
Annual Loss = Pre-Injury Earning Trajectory − Post-Injury Earning Capacity
Present Value = Σ (Annual Loss × Discount Factor) over work-life expectancy
```

**Include in projections:**
- Annual wage growth rate (from pre-injury history + inflation data)
- Career advancement adjustments
- Lost benefits over projection period
- Discount rate (jurisdiction-appropriate; cite source — typically Treasury rates)

**Show present value calculation:** Year | Projected Loss | Discount Factor | Present Value

**Sensitivity analysis:** Vary recovery timeline, earning capacity, discount rate, work-life expectancy. Label conservative vs. aggressive scenarios.

### 5. Medical Expenses

#### Past Medical Expenses Table

| Date | Provider | Service Type | Billed | Insurance Paid | Out-of-Pocket | Status |

**Categories:** Emergency/ambulance | Hospitalization | Surgery | Physician/specialist visits | PT/rehab | Diagnostics/imaging | Prescriptions | DME | Other

#### Future Medical Expenses

Source from physician opinions on future needs and/or life care plan:
- Ongoing therapy/rehab
- Future surgeries
- Long-term medications
- Equipment replacement
- Follow-up monitoring

Calculate present value using same discount methodology. Present both nominal and present value totals.

### 6. Other Economic Losses

| Category | Calculation Method |
|----------|-------------------|
| **Household services** | Hours/week × market rate per service type (cleaning, yard, childcare, cooking, maintenance) |
| **Transportation** | Medical visit count × mileage rate + parking; include family driver time |
| **Home modifications** | Ramps, bathroom mods, adaptive equipment — from receipts/estimates |
| **Miscellaneous** | OTC medications, supplies, damaged property replacement |

Distinguish past (incurred) vs. future (projected from permanent limitations).

### 7. Damages Summary

**Summary table:**

| Category | Amount |
|----------|--------|
| Past Lost Wages (date range) | $ |
| Future Lost Wages / Diminished Earning Capacity (PV) | $ |
| Past Medical Expenses | $ |
| Future Medical Expenses (PV) | $ |
| Household Services (past + future) | $ |
| Transportation | $ |
| Home Modifications / Other | $ |
| **TOTAL ECONOMIC DAMAGES** | **$** |

Provide gross total and after-tax total if jurisdiction requires.

Include 1-2 paragraph narrative highlighting key damage drivers (permanency, age/work-life expectancy, career trajectory loss, future care burden).

If ranges exist, present conservative and aggressive scenarios with the recommended figure clearly labeled.

### 8. Exhibit List

Number sequentially, organized by category:
- Employment/wage documents
- Medical records and bills
- Expert reports
- Receipts and invoices
- Other supporting documentation

Each entry: Exhibit # | Document Description | Date | Relevance to Calculation

## Guidelines

- **Every figure must cite a specific source document** with document name, date, and page
- **All calculations must be transparent and replicable** — show formulas and assumptions
- **Maintain objectivity** — no advocacy language; let the numbers speak
- **Preemptively address common challenges:**
  - Mitigation efforts (claimant's return-to-work attempts)
  - Pre-existing conditions (distinguish pre-existing vs. injury-caused limitations)
  - Earnings anomalies (explain any pre-injury income irregularities)
  - Projection reasonableness (ground in documented medical opinions)
- **Discount rates** must be jurisdiction-appropriate; state source
- **Plaintiff-side orientation** — but maintain credibility through conservative methodology
- **Flag gaps** — identify where additional discovery, vocational evaluation, life care plan, or economist report would strengthen the analysis
- **Jurisdiction note:** Tax treatment of damages, discount rate standards, and gross-vs-net calculation rules vary by state — confirm applicable rules
