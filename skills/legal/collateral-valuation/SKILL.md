---
name: collateral-valuation
description: >-
  Provides a structured reference to value collateral for U.S. bankruptcy
  secured claims, allocate secured vs unsecured portions, and apply Chapter 7
  liquidation and Chapter 13 replacement-value standards (Rash), 910-day rule,
  and § 506(b) oversecured interest. Use when preparing proofs of claim, plan
  treatment analyses, cramdown disputes, or deficiency calculations. Trigger
  keywords: bankruptcy, proof of claim, secured claim, collateral valuation,
  deficiency, Chapter 7, Chapter 13, Rash, 910-day, § 506, § 1325.
tags:
  - analysis
  - litigation
---

# Collateral Valuation (Bankruptcy)

Value collateral and split secured vs. unsecured claim amounts under U.S. bankruptcy standards.

## Prerequisites

1. **Collateral inventory** — type, identifiers, condition, location
2. **Debt details** — principal, accrued interest, fees, contract rate
3. **Bankruptcy context** — chapter, filing date, plan posture
4. **Evidence sources** — appraisals, guides, comps, sales data, photos

## Output Structure / Process

### 1. Identify Collateral Category

Use the first matching category and the associated source hierarchy.

**Real Property**

| Source | Reliability | Use Case |
|---|---|---|
| Professional appraisal (MAI) | Highest | High-value, commercial, or contested valuations |
| BPO | Medium | Residential, mid-value, quick turnaround |
| Tax assessment | Low-Medium | Baseline only |
| Automated estimates (Zillow/Redfin) | Low | Preliminary only; not for court |

Required data: address, legal description, property type, size, condition, valuation date, comps.

**Vehicles**

| Source | Reliability | Notes |
|---|---|---|
| NADA Guides | High | Lender-standard |
| Kelley Blue Book | High | Commonly accepted |
| Black Book | High | Wholesale/auction focus |
| Dealer quote | Medium | Must be in writing |

Required data: year/make/model/trim, VIN, mileage, condition, options, retail vs wholesale.

**Equipment and Machinery**

| Source | Reliability | Notes |
|---|---|---|
| Certified appraisal | Highest | Specialized or high-value |
| Industry guides | Medium | Sector-specific (e.g., Rouse) |
| Auction comps | Medium | Recent comparable sales |
| Depreciated book value | Low | Accounting, not market |

Consider age, remaining life, maintenance, obsolescence, market demand, removal/transport costs.

**Accounts Receivable**

Net collectible value:

```
Gross A/R Balance:                    $______________
Less: Doubtful/uncollectible         ($______________)
Less: Disputed amounts               ($______________)
Less: Contra accounts/offsets        ($______________)
Less: Aging discount                 ($______________)
------------------------------------------------------
Net Collectible Value:                $______________
```

Typical aging adjustments:

| Aging | Collection Rate | Discount |
|---|---|---|
| 0-30 days | 95-100% | 0-5% |
| 31-60 days | 85-90% | 10-15% |
| 61-90 days | 70-80% | 20-30% |
| 91-120 days | 40-60% | 40-60% |
| 120+ days | 10-30% | 70-90% |

Adjust for industry norms and historical collections.

**Inventory**

| Type | Method |
|---|---|
| Raw materials | Lower of cost or market |
| Work in progress | % completion x expected finished value |
| Finished goods | Net realizable value (price minus costs to sell) |
| Obsolete/slow-moving | Liquidation value |

Consider FIFO/LIFO, seasonality, shelf life, selling costs, and need for going-concern operations.

### 2. Apply Chapter-Specific Valuation Standard

| Chapter | Standard | Practical Effect |
|---|---|---|
| Chapter 7 | Liquidation value | Lower value, larger unsecured deficiency |
| Chapter 13 | Replacement value | Higher value, larger secured claim |

Replacement value is defined by *Associates Commercial Corp. v. Rash*, 520 U.S. 953 (1997).

### 3. Calculate Secured vs Unsecured Portions

```
Total Debt Owed:                      $______________
Collateral Value:                     $______________

If Debt <= Collateral:
  Secured Claim:                      $______________
  Unsecured Deficiency:               $0

If Debt > Collateral:
  Secured Claim:                      $______________
  Unsecured Deficiency:               $______________
```

### 4. Special Rules Checklist

- 910-day vehicle rule (Chapter 13): full debt treated as secured if personal-use vehicle purchased within 910 days. 11 U.S.C. § 1325(a) [VERIFY]
- Principal residence anti-modification (Chapter 13): claim not crammed down. 11 U.S.C. § 1322(b)(2) [VERIFY]
- Oversecured interest: allowed under 11 U.S.C. § 506(b).
- Undersecured: no post-petition interest on secured portion.

### 5. Documentation Package

Required elements:

1. **Source** — preparer and qualifications
2. **Date** — reasonably current as of petition/valuation date
3. **Method** — market, cost, income
4. **Assumptions** — material assumptions disclosed
5. **Comparables** — sales, listings, auctions
6. **Condition** — photos and narrative condition assessment

### 6. Dispute Prep (If Contested)

Checklist:

1. Obtain professional appraisal if not already done.
2. Compile comparable sales/auction evidence.
3. Photograph collateral and document condition.
4. Identify title defects or liens affecting value.
5. Compare debtor/trustee methodology to yours.

## Guidelines

- Use liquidation value in Chapter 7 unless the court orders otherwise.
- Use replacement value for personal property in Chapter 13 per *Rash*.
- Do not rely on automated estimates for court filings.
- Keep valuation sources current and well-documented.
- Mark any uncertain statutory cites with `[VERIFY]` before filing.

References: 11 U.S.C. § 506; 11 U.S.C. § 1325(a) [VERIFY]; FRBP 3012; *Associates Commercial Corp. v. Rash*, 520 U.S. 953 (1997); *Till v. SCS Credit Corp.*, 541 U.S. 465 (2004).
