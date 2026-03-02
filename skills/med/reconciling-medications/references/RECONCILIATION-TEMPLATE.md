# Reconciliation Report — Output Templates

Use these templates when generating the final medication reconciliation report.
Copy the relevant sections and populate with patient-specific data.

---

## 1. Report Header

```
═══════════════════════════════════════════════════════════════
  MEDICATION RECONCILIATION REPORT
═══════════════════════════════════════════════════════════════
  Patient:          [NAME / MRN / DOB]
  Transition Type:  [Admission | Transfer | Discharge | Clinic]
  Date/Time:        [YYYY-MM-DD HH:MM]
  Sending:          [Facility — Unit — Provider]
  Receiving:        [Facility — Unit — Provider]
  Prepared By:      [Pharmacist Name, Credentials]
═══════════════════════════════════════════════════════════════
```

---

## 2. Summary Dashboard

```
┌──────────────────────────┬───────┐
│ Total Medications        │   ##  │
├──────────────────────────┼───────┤
│ Continued (no change)    │   ##  │
│ Dose Changed             │   ##  │
│ New                      │   ##  │
│ Discontinued             │   ##  │
│ Omitted — Unintentional? │   ##  │
│ Therapeutic Duplicate    │   ##  │
│ Duplicate                │   ##  │
│ Held                     │   ##  │
│ Substituted              │   ##  │
├──────────────────────────┼───────┤
│ DISCREPANCIES            │       │
│   Critical               │   ##  │
│   High                   │   ##  │
│   Moderate               │   ##  │
│   Low                    │   ##  │
└──────────────────────────┴───────┘
```

---

## 3. Reconciliation Matrix

One row per unique medication. Sort critical discrepancies to the top, then
high, moderate, low, and finally CONTINUED rows alphabetically.

| # | Generic Name | Brand | Dose | Route | Freq | Indication | Home List | Admit Orders | Inpatient MAR | Discharge Rx | Status | Severity | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | metoprolol succinate | Toprol-XL | 50 mg | PO | daily | HTN | ✓ 50 mg | ✓ 50 mg | ✓ 50 mg | ✓ 50 mg | CONTINUED | — | |
| 2 | warfarin | Coumadin | 5 mg | PO | daily | AFib/DVT ppx | ✓ 5 mg | ✓ 5 mg | ✓ 7.5 mg | ✓ 7.5 mg | DOSE CHANGED | **Critical** | ⚠ HIGH-ALERT. Dose ↑ inpatient per INR. Confirm new dose at discharge. |
| 3 | omeprazole | Prilosec | 20 mg | PO | daily | GERD | ✓ 20 mg | ✗ | ✗ | ✗ | OMITTED | **High** | Home med not ordered on admission. Intentional? |
| 4 | gabapentin | Neurontin | 300 mg | PO | TID | Neuropathy | ✓ 300 mg TID | ✓ 300 mg TID | ✓ 100 mg TID | ✓ 100 mg TID | DOSE CHANGED | **High** | Dose ↓ for AKI (CrCl 38). Confirm continuation at discharge. |

**Legend:**
- ✓ = present on that list (dose shown if different from home)
- ✗ = absent from that list
- ⚠ = high-alert medication

---

## 4. High-Alert Medication Detail

Complete one block for **each** high-alert medication that has any status other
than CONTINUED.

```
┌─ HIGH-ALERT MEDICATION ──────────────────────────────────────
│ Drug:          [generic name (brand)]
│ ISMP Class:    [Anticoagulant | Insulin | Opioid | ...]
│ Status:        [DOSE CHANGED | NEW | DISCONTINUED | ...]
│ Severity:      [Critical | High]
│
│ Home:          [dose / route / freq — or NOT ON HOME LIST]
│ Admission:     [dose / route / freq — or NOT ORDERED]
│ Inpatient:     [dose / route / freq — or HELD / D/C]
│ Discharge:     [dose / route / freq — or NOT PRESCRIBED]
│
│ Discrepancy:   [Concise description of the change/issue]
│ Clinical Note: [Rationale if documented, or "No rationale
│                 found in chart — VERIFY with provider"]
│ Monitoring:    [Required labs, vitals, or assessments]
│ Action Needed: [Specific next step for the receiving team]
└──────────────────────────────────────────────────────────────
```

---

## 5. Allergy & Interaction Findings

### 5a. Allergy Cross-Check

| Documented Allergy | Reaction Type | Conflicting Medication | Action |
|---|---|---|---|
| Penicillin | Anaphylaxis | amoxicillin (discharge Rx) | **CONTRAINDICATED — remove immediately** |
| Sulfa | Rash | sulfamethoxazole/trimethoprim | **CONTRAINDICATED — remove or obtain allergy override** |
| — | — | — | No allergy conflicts identified ✓ |

### 5b. Drug-Drug Interactions (Major / Contraindicated)

| Drug A | Drug B | Severity | Mechanism | Clinical Concern | Action |
|---|---|---|---|---|---|
| warfarin | amiodarone | Major | CYP inhibition ↑ INR | Bleeding risk | Monitor INR closely; consider dose ↓ |
| metformin | IV contrast | Contraindicated | Lactic acidosis risk | Hold metformin 48 h post-contrast | Verify hold order + renal function |
| — | — | — | — | — | No major interactions identified ✓ |

---

## 6. Renal & Hepatic Dose Flags

| Medication | Clearance | Patient Value | Recommended Adj. | Current Dose | Status |
|---|---|---|---|---|---|
| gabapentin | Renal (CrCl) | CrCl 38 mL/min | 100–300 mg BID | 300 mg TID | ⚠ Dose adjustment needed |
| metformin | Renal (eGFR) | eGFR 52 | Max 1000 mg/day | 1000 mg BID | ⚠ Exceeds renal dose limit |
| — | — | — | — | — | No renal/hepatic flags ✓ |

> If renal or hepatic labs are unavailable, insert:
> `⚠ Renal/hepatic function not available — dose appropriateness not verified for
> renally/hepatically cleared medications. Recommend obtaining labs before finalizing.`

---

## 7. Unresolved Items

Collect **every** `[VERIFY]` and `[NOT PROVIDED]` tag from the report here.

| # | Item | Source | Issue | Assigned To |
|---|---|---|---|---|
| 1 | omeprazole omission | Admission orders | Not ordered — intentional? | Admitting physician |
| 2 | Home med list sourcing | Patient interview only | `[UNVERIFIED — SINGLE SOURCE]` | Pharmacy — obtain refill records |
| 3 | Renal function | Labs | `[NOT PROVIDED]` | Ordering provider |

---

## 8. Pharmacist Attestation

```
───────────────────────────────────────────────────────────────
I have reviewed the medication lists from the sources identified
above and performed reconciliation in accordance with
organizational policy and Joint Commission NPSG.03.06.01.

Discrepancies, high-alert medications, allergy conflicts, and
interaction findings are documented as noted. Items marked
[VERIFY] require provider resolution before the reconciled
list is considered final.

Pharmacist:   ______________________________
Credentials:  ______________________________
Date/Time:    ______________________________
Signature:    ______________________________
───────────────────────────────────────────────────────────────
```

---

## Usage Notes

- **Column adaptation:** If fewer source lists are available (e.g., clinic visit
  with only Home List and Clinic Orders), remove unused columns from the matrix
  rather than leaving them blank.
- **Multiple pages:** For patients on > 20 medications, split the matrix across
  pages but keep the summary dashboard and high-alert section on page 1.
- **EHR integration:** When generating for EHR import, strip ASCII box-drawing
  characters and output as pipe-delimited tables or structured JSON.
