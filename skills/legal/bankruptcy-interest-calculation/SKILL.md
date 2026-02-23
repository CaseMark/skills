---
name: bankruptcy-interest-calculation
description: Reference guide for calculating pre-petition interest on bankruptcy claims. Covers simple interest formulas, daily accrual method, day-count conventions, interest rate source hierarchy (contract → judgment → state statutory → federal), post-petition interest rules under 11 U.S.C. § 506(b), and late fee/attorney fee inclusion standards. Generates a completed interest calculation worksheet suitable for attachment to a proof of claim. Use when preparing the interest component of a proof of claim, calculating creditor claim amounts, or verifying interest calculations.
tags:
  - analysis
  - checklist
  - litigation
---

# Bankruptcy Claim Interest Calculation

Calculates pre-petition interest for bankruptcy proofs of claim and produces a defensible worksheet for filing.

## Prerequisites

1. Principal balance as of last payment or accrual date
2. Annual interest rate and governing source (contract, judgment, or statute)
3. Last payment date and petition date (to determine accrual period)
4. Underlying agreement (to verify day-count convention and fee authorization)

## Output Structure / Process

### 1. Determine Interest Rate

| Priority | Source | Notes |
|----------|--------|-------|
| 1 | Contract rate | Express provision in loan agreement or promissory note |
| 2 | Judgment rate | Rate specified in pre-petition judgment |
| 3 | State statutory | Applicable state's prejudgment interest rate |
| 4 | Federal rate | 28 U.S.C. § 1961 (Treasury bill rate) |

Always cite the source in the proof of claim and attach supporting documentation.

### 2. Select Day-Count Convention

| Convention | Formula | Common Usage |
|------------|---------|--------------|
| Actual/365 | Actual days ÷ 365 | Consumer loans, mortgages (default if unspecified) |
| Actual/360 | Actual days ÷ 360 | Commercial loans, some credit facilities |
| 30/360 | Assumes 30-day months | Bonds, some commercial paper |

### 3. Calculate Interest

**Simple interest (most common):**
```
Per Diem = (Principal × Annual Rate) ÷ 365
Pre-Petition Interest = Per Diem × Days from Last Payment to Petition Date
```

**Example:**
```
Principal:   $50,000.00  |  Rate: 8.5%  |  Days: 138
Per Diem  = ($50,000 × 0.085) ÷ 365 = $11.64
Interest  = $11.64 × 138           = $1,606.32
Total Claim = $50,000.00 + $1,606.32 = $51,606.32
```

### 4. Post-Petition Interest Rules

| Claim Type | Post-Petition Interest |
|------------|----------------------|
| Unsecured | ❌ Not allowed (stop at petition date); exception: solvent-debtor cases |
| Secured (oversecured) | ✅ Allowed under 11 U.S.C. § 506(b) — only to extent of equity cushion |
| Secured (undersecured) | ❌ Not allowed |
| Priority | ❌ Generally not allowed |

### 5. Additional Charges Checklist

**Late fees** — include only if:
- [ ] Contract expressly authorizes the fee (cite section)
- [ ] Fee was assessed pre-petition
- [ ] Fee is not punitive or unconscionable

**Attorney fees** — include only if:
- [ ] Contract contains fee-shifting provision, OR statute authorizes recovery
- [ ] Attach itemized statement: dates, hours, rates, work descriptions
- [ ] Only pre-petition fees; post-petition collection fees excluded

### 6. Calculation Worksheet

```
═══════════════════════════════════════════════════════════
              INTEREST CALCULATION WORKSHEET
Case: [Debtor Name], Case No. [XX-XXXXX]
Creditor: [Creditor Name]   Account No.: [Number]
═══════════════════════════════════════════════════════════

PRINCIPAL
─────────────────────────────────────────────────────────
Original Debt Amount:                        $____________
Less: Payments Received:                    ($____________)
Principal Balance as of [Last Payment Date]: $____________

INTEREST
─────────────────────────────────────────────────────────
Principal Balance:                           $____________
Annual Interest Rate:                        ____________%
Rate Source: [ ] Contract §___  [ ] Judgment  [ ] Statutory  [ ] Federal

Accrual Period:
  From: [Last Payment Date]                  ____________
  To:   [Petition Date]                      ____________
  Days:                                       ____________
Day-Count: [ ] Actual/365  [ ] Actual/360  [ ] 30/360

Per Diem = ($_______ × ____%) ÷ _____ =     $____________
Interest = $_______ × _____ days =          $____________

PRE-PETITION INTEREST TOTAL:                 $____________

OTHER CHARGES
─────────────────────────────────────────────────────────
Late Fees (Contract §___):                   $____________
NSF/Returned Check Fees:                     $____________
Attorney Fees (see itemization):             $____________
Other: _________________________:            $____________
OTHER CHARGES TOTAL:                         $____________

CLAIM SUMMARY
─────────────────────────────────────────────────────────
Principal:                                   $____________
Pre-Petition Interest:                       $____________
Other Charges:                               $____________
─────────────────────────────────────────────────────────
TOTAL CLAIM AS OF PETITION DATE:             $____________
═══════════════════════════════════════════════════════════
Prepared by: ____________________  Date: _______________
```

## Guidelines

- **Stop interest at petition date** for unsecured and priority claims — including post-petition interest is a common and objection-triggering error
- **Match contract methodology exactly** — do not compound if contract specifies simple interest; do not use 360-day year if contract specifies 365
- **Verify day count** using an actual calendar or date calculator; do not estimate
- **Use balance after last credited payment** as principal — not original loan amount
- **Always cite rate source** with contract section number or statutory citation; unsupported rates invite objection
- **Attach documentation**: rate source excerpt, payment history, fee authorization clause

### Common Errors

| Error | Correct Approach |
|-------|-----------------|
| Post-petition interest on unsecured claim | Stop at petition date |
| Wrong day-count denominator | Follow contract; default to Actual/365 |
| Compounding on simple-interest contract | Match contract methodology |
| Unauthorized fees | Only include contractually/statutorily permitted charges |
| Wrong principal starting point | Balance after last payment, not original amount |

### Key Authorities
- 11 U.S.C. § 502(b) — Allowance of claims; interest limitations
- 11 U.S.C. § 506(b) — Post-petition interest for oversecured creditors
- 28 U.S.C. § 1961 — Federal post-judgment interest rate
