---
name: asset-liability-summaries
description: >-
  Analyzes financial documents to produce structured asset and liability
  summaries for legal proceedings. Extracts valuations, ownership structures,
  and encumbrances across all asset classes and debt types, then outputs an
  executive net-worth overview, categorized schedules, disputed-item flags,
  and documentation gaps. Use when preparing financial summaries for
  divorce/dissolution, estate planning, bankruptcy, business valuation,
  settlement negotiations, or financial litigation. Trigger keywords: net
  worth summary, marital estate, balance sheet, asset schedule, liability
  schedule, community property, separate property.
tags:
  - analysis
  - litigation
  - summarization
  - summary
  - transactional
---

# Asset & Liability Summary

Produces a court-ready financial summary covering all assets and liabilities — with ownership classification, valuations, encumbrances, and source citations.

## Prerequisites

1. **Source financial documents** — bank/brokerage statements, tax returns, mortgage statements, loan documents, business financials, appraisals, retirement account statements
2. **Effective date** — the valuation date controlling all figures (e.g., date of separation, petition date, death date)
3. **Matter type** — divorce, estate, bankruptcy, business valuation, or general litigation (drives community/separate property analysis and categorization logic)
4. **Jurisdiction** — relevant for community property vs. equitable distribution states and exemption rules (bankruptcy)

## Output Structure

### 1. Executive Overview

| | Amount |
|---|---|
| **Total Assets** | $ |
| **Total Liabilities** | $ |
| **Net Worth / Equity** | $ |
| **Effective Valuation Date** | |
| **Disputed Items (not included above)** | $ |

---

### 2. Asset Schedule

Group by category. For each asset:

| Field | Capture |
|---|---|
| Description | Asset name, account number (last 4), address |
| Category | Real property / Financial account / Retirement / Business interest / Vehicle / Personal property / IP / Other |
| Ownership | Separate / Community / Joint / Entity-held |
| Fair Market Value | $ as of valuation date |
| Encumbrances / Liens | $ outstanding; creditor name |
| Net Equity | FMV minus encumbrances |
| Acquisition Date | If legally relevant (marital matters, step-up basis) |
| Source | Document name, page/exhibit number |

**Asset categories to cover:**
- [ ] Real property (primary, rental, vacation, timeshare)
- [ ] Bank accounts (checking, savings, CDs, money market)
- [ ] Investment accounts (brokerage, mutual funds, crypto)
- [ ] Retirement accounts (401k, IRA, pension — note tax-deferred status)
- [ ] Business interests (ownership %, valuation method)
- [ ] Vehicles (cars, boats, aircraft)
- [ ] Life insurance (cash surrender value)
- [ ] Intellectual property / royalties
- [ ] Receivables / promissory notes owed to party
- [ ] Personal property of significant value (jewelry, art, collectibles)

---

### 3. Liability Schedule

Group by category. For each liability:

| Field | Capture |
|---|---|
| Creditor / Obligee | Name and account identifier |
| Category | Mortgage / HELOC / Auto loan / Student loan / Credit card / Tax / Judgment / Business debt / Other |
| Outstanding Balance | $ as of valuation date |
| Interest Rate | % |
| Secured / Unsecured | If secured, collateral asset |
| Responsible Party | Individual / Joint / Entity |
| Source | Document name, page/exhibit number |

**Liability categories to cover:**
- [ ] Mortgages and HELOCs
- [ ] Auto / vehicle loans
- [ ] Student loans
- [ ] Credit card balances
- [ ] Personal loans
- [ ] Tax obligations (federal, state, local — include penalties/interest)
- [ ] Judgments and legal obligations
- [ ] Business-related debt
- [ ] Deferred compensation / obligations

---

### 4. Disputed & Uncertain Items

List all assets or liabilities where ownership, value, or existence is contested or unverified:

| Item | Issue | Recommended Action |
|---|---|---|
| [Asset/Liability] | [Value dispute / ownership dispute / missing docs] | [Appraisal / subpoena / expert valuation] |

---

### 5. Notes & Recommendations

- **Valuation methodology**: Note method used for each non-liquid asset (appraisal, book value, tax assessment, account statement)
- **Missing documentation**: List any items referenced in documents but lacking corroboration
- **Discrepancies**: Flag conflicts between documents (e.g., differing balances across statements)
- **Tax considerations**: Flag retirement accounts (pre-tax), real property (carryover basis, depreciation recapture), and installment obligations
- **Expert valuation needed**: Flag business interests, real property without recent appraisal, and complex financial instruments
- **Assumptions**: State all assumptions made where documentation was incomplete

## Guidelines

- Maintain consistent valuation date across all items; flag any items valued on a different date
- In marital matters: distinguish separate property (pre-marital, gift, inheritance) from community/marital property — apply jurisdiction's default rules
- In bankruptcy: note exemption eligibility (homestead, retirement, vehicle) alongside each asset
- Cite source document and page for every figure — this summary must survive discovery scrutiny
- Do not impute values not supported by documents; use `[NEEDS VALUATION]` placeholder where data is absent
- Flag retirement accounts as tax-deferred; gross value ≠ net value after tax — note if after-tax figure is needed
- If business interest present, note whether valuation reflects enterprise value, equity value, or book value and flag if formal appraisal is needed
