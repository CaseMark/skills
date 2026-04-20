---
name: reconciling-inpatient-medications
language: en
description: Compares admission, inpatient, and discharge medication lists to identify discrepancies. Use when performing medication reconciliation, identifying med changes, or verifying discharge prescriptions.
tags:
  - reconciliation
  - hospital-medicine
  - patient-care
metadata:
  author: casemark
  practice_areas:
    - Hospital Medicine
    - Internal Medicine
  document_types:
    - Reconciliation Report
  skill_modes:
    - Reconciliation
---

# Reconciling Inpatient Medications

## Why This Skill Exists

Medication discrepancies at care transitions cause approximately 50% of all hospital medication errors and up to 20% of adverse drug events. Inpatient medication reconciliation is distinct from pharmacy cross-setting reconciliation: it operates within the hospital stay lifecycle across three critical transition points — admission, transfer, and discharge — each with unique failure modes. Unreconciled medications lead to therapeutic duplications, omitted chronic therapies, drug interactions, and preventable readmissions. Joint Commission NPSG.03.06.01 mandates reconciliation at every transition of care. This skill enforces a structured, auditable process that catches discrepancies before they reach the patient.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Before beginning reconciliation, collect and confirm the following. Do NOT proceed until every required item is addressed or explicitly marked unavailable.

### A1. Identify Transition Point

| Transition | Source List | Target List | Key Risk |
|---|---|---|---|
| **Admission** | Best Possible Medication History (BPMH) | Admission orders | Omission of chronic meds; inappropriate continuation of home meds |
| **Transfer** | Sending-unit MAR | Receiving-unit orders | IV-to-PO conversion failures; dose drift from organ function changes |
| **Discharge** | Active inpatient MAR | Discharge prescriptions | Held meds not restarted; new meds missing from Rx; duplications |

State the transition type explicitly in all output.

### A2. Gather Available Medication Lists

Required sources (mark `[UNAVAILABLE]` if absent — never silently omit):

- **BPMH**: Patient/caregiver interview, community pharmacy records, PCP med list, prior discharge summaries, pill bottles/med cards
- **Active MAR**: Current medication administration record from EHR
- **Admission/Transfer/Discharge orders**: The target order set for the transition
- **Allergy and adverse reaction list**: Including severity and reaction type
- **Relevant labs**: Renal function (CrCl/eGFR), hepatic function (LFTs), INR/anti-Xa, drug levels, A1c, electrolytes

### A3. Assess Patient Complexity

Flag any of the following — each increases reconciliation error probability:

- [ ] Polypharmacy (10+ medications)
- [ ] High-risk medication classes present (see below)
- [ ] Renal or hepatic impairment requiring dose adjustment
- [ ] Multiple prescribers / care teams
- [ ] Cognitive impairment or limited health literacy
- [ ] Recent ICU stay
- [ ] Substance use history affecting medication selection
- [ ] Non-formulary medications on home list

**High-risk medication classes** (require line-by-line verification):

| Class | Examples | Specific Risk |
|---|---|---|
| Anticoagulants | warfarin, DOACs, heparin, enoxaparin | Bleeding / thrombosis if omitted or duplicated |
| Insulin / diabetes agents | insulin (all types), sulfonylureas, SGLT2i | Hypo/hyperglycemia; sulfonylureas often held inpatient |
| Cardiac medications | beta-blockers, antiarrhythmics, digoxin | Rebound tachycardia, arrhythmia if abruptly stopped |
| Seizure medications | levetiracetam, phenytoin, valproic acid | Seizure breakthrough; narrow therapeutic indices |
| Immunosuppressants | tacrolimus, mycophenolate, cyclosporine | Rejection / toxicity; level-dependent dosing |
| Opioids / controlled substances | oxycodone, methadone, buprenorphine | Withdrawal; diversion risk; dose conversion errors |
| Corticosteroids | prednisone, hydrocortisone, dexamethasone | Adrenal crisis if abruptly stopped after prolonged use |

---

## Workflow

### Step 1: Normalize Medication Data

For every medication on every source list, capture these seven fields. Missing fields get `[VERIFY]`.

| Field | Description |
|---|---|
| Medication | Generic name (note brand if relevant for narrow therapeutic index) |
| Dose | Numeric dose with unit |
| Route | PO, IV, SQ, IM, topical, inhaled, etc. |
| Frequency | Specific schedule (not just "as directed") |
| Indication | Why the patient takes it — required for disposition decisions |
| Status | Active, held, discontinued, new, changed |
| Source | Which list(s) this medication appears on |

### Step 2: Cross-Reference and Match

Align medications across source and target lists. For each medication, assign one disposition:

| Disposition | Definition | When to Use |
|---|---|---|
| **Continued** | Same med, dose, route, frequency | No change needed across transition |
| **Modified** | Same med, different dose/route/frequency | Dose adjustment, IV→PO conversion, frequency change |
| **Substituted** | Different med, same therapeutic class | Formulary swap (e.g., home atorvastatin → hospital rosuvastatin) |
| **Held** | Intentionally paused | NPO status, perioperative, acute kidney injury, etc. |
| **Discontinued** | Stopped permanently | No longer indicated, adverse effect, therapeutic change |
| **Omitted** | On source list but absent from target with no documented reason | **This is the primary error to catch** |
| **New** | On target list but not on source | Started during this encounter |

### Step 3: Transition-Specific Checks

#### Admission (Home → Inpatient)

- Compare every BPMH medication against admission orders
- Flag chronic medications not ordered on admission (unintentional omission vs. intentional hold)
- Verify home PRN medications are addressed — do not silently drop
- Check for therapeutic substitutions and confirm equivalent dosing
- Confirm allergy list matches home records
- Flag OTC medications, supplements, and herbals that may interact

#### Transfer (Unit → Unit)

- Map all IV continuous infusions to floor-appropriate equivalents (e.g., IV diltiazem drip → PO diltiazem ER)
- Recalculate renal-dose adjustments if function has changed since admission
- Verify ICU-specific medications are appropriately discontinued (e.g., propofol, vasopressors)
- Confirm stress ulcer prophylaxis is reassessed (discontinue if no longer indicated)
- Check VTE prophylaxis transitions (e.g., heparin drip → enoxaparin)

#### Discharge (Inpatient → Home/Facility)

- Every pre-admission medication must have an explicit disposition: continued, modified, held (with restart plan), or discontinued (with reason)
- All new medications started during stay must appear on discharge Rx with indication and duration
- Held medications: document whether to restart, when, and at what dose
- Verify discharge doses account for any inpatient adjustments (e.g., uptitrated beta-blocker)
- Confirm no inpatient-only medications are sent home (e.g., IV antibiotics without OPAT plan, heparin SQ prophylactic dose)
- Cross-check discharge Rx against active MAR at time of discharge

### Step 4: Generate Discrepancy Report

For every discrepancy found, document:

| Field | Content |
|---|---|
| Medication | Drug name and dose |
| Discrepancy type | Omission, duplication, dose mismatch, route mismatch, interaction, unaddressed hold |
| Source | Which list(s) show the conflict |
| Severity | **Critical** (high-risk class or immediate harm potential), **Major** (clinical significance), **Minor** (documentation gap) |
| Recommended action | Specific resolution with rationale |
| Status | Open, resolved, escalated |

### Step 5: Compile Reconciled Medication List

Produce the final reconciled list using the template in `references/INPATIENT-MED-REC-TEMPLATE.md`. Every medication on the final list must have all seven fields populated. No `[VERIFY]` tags may remain in the final output — unresolved items must be escalated.

---

## Output Templates

### Reconciliation Summary Header

```
MEDICATION RECONCILIATION — [TRANSITION TYPE]
Patient: [ID/Name]       Date: [YYYY-MM-DD]
Transition: [Admission / Transfer (from → to) / Discharge]
Total Source Medications: [N]    Total Target Medications: [N]
Discrepancies Found: [N]  (Critical: [N] | Major: [N] | Minor: [N])
High-Risk Classes Present: [list]
Reconciler: [Name/Role]    Verifier: [Name/Role]
```

### I-PASS Integration for Handoff

When reconciliation accompanies a handoff, structure the medication summary using I-PASS:

| Element | Medication Reconciliation Content |
|---|---|
| **I**llness severity | Patient acuity and medication complexity tier |
| **P**atient summary | Key diagnoses driving medication regimen |
| **A**ction list | Discrepancies requiring resolution; pending medication decisions |
| **S**ituation awareness | High-risk medications; drug levels pending; renal function trend |
| **S**ynthesis | Anticipated medication changes in next 12-24 hours |

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After generating the reconciled list, verify every item below. Do not finalize until all pass.

- [ ] Every source medication has an explicit disposition (no medication silently dropped)
- [ ] Every high-risk medication class present has been individually verified
- [ ] All discrepancies are categorized by severity and have a recommended action
- [ ] Held medications include a restart plan or explicit discontinuation rationale
- [ ] New medications include indication and intended duration
- [ ] Therapeutic substitutions include dose-equivalence confirmation
- [ ] Allergy/adverse reaction list is consistent across all sources
- [ ] Route and frequency are clinically appropriate for the care setting (no IV meds on a floor discharge, no TID dosing for a once-daily drug)
- [ ] Output uses standardized terminology — no abbreviations on the Joint Commission "Do Not Use" list
- [ ] All `[VERIFY]` tags resolved or escalated to human review

---

## Quality Audit

### Compliance Anchors

| Standard | Requirement | How This Skill Addresses It |
|---|---|---|
| Joint Commission NPSG.03.06.01 | Maintain accurate medication list; reconcile at transitions | Structured reconciliation at admission, transfer, discharge |
| CMS CoP §482.24(c) | Medication orders reviewed for appropriateness | Disposition table with indication and rationale |
| WHO High 5s: Medication Reconciliation | Systematic BPMH; compare against orders | BPMH as mandatory source; cross-reference workflow |

### Error-Prevention Checklist

| Error Type | Detection Method |
|---|---|
| Omission of chronic med | Source-to-target gap analysis (Step 2, "Omitted" disposition) |
| Therapeutic duplication | Same-class check across all lists |
| Dose/route mismatch | Field-by-field comparison in normalization (Step 1) |
| Held med not restarted at discharge | Discharge-specific check (Step 3, Discharge section) |
| IV med on discharge Rx | Route validation against care setting |
| Formulary swap without dose equivalence | Substitution verification (Step 2, "Substituted" disposition) |
| Drug-drug interaction introduced | New-medication interaction screen |

### Known Limitations

- This skill does not replace pharmacist clinical judgment — all critical discrepancies require human verification
- Drug interaction screening depends on completeness of the medication list provided
- OTC, supplement, and herbal product history is frequently incomplete — flag this gap explicitly
- Dose equivalence for therapeutic substitutions should be confirmed against current formulary references
- This skill does not calculate renal/hepatic dose adjustments — it flags the need for them

### When to Escalate to Human Review

- Any critical-severity discrepancy
- Patient on 3+ high-risk medication classes simultaneously
- Conflicting information between sources that cannot be resolved from available data
- Medication identified that the agent has low confidence in (unfamiliar drug, unusual dose)
- Any controlled substance discrepancy

---

## Guidelines

- Always verify high-alert medications (anticoagulants, insulin, opioids, immunosuppressants, antiarrhythmics) individually at every transition point — never batch-reconcile these classes with lower-risk medications.
- Formulary substitutions must include documented dose-equivalence rationale. When substituting therapeutic equivalents (e.g., home atorvastatin → hospital rosuvastatin), record the conversion basis and alert the patient to the temporary change.
- Discharge medication lists must be finalized and reconciled within 2 hours of the discharge order. Delays beyond this window increase the risk of the patient leaving with an outdated or incomplete medication list.
- Held medications require an explicit restart plan at discharge — including the restart date, dose, and any monitoring required. A medication marked "held" without a disposition at discharge is a reconciliation failure.
- For patients on 3+ controlled substances, perform an independent verification against the state Prescription Drug Monitoring Program (PDMP) database before finalizing the discharge medication list.
- Every reconciliation must be performed or verified by a licensed pharmacist or credentialed provider. AI-generated reconciliation output is a draft tool, not a final clinical document, until human attestation is completed.
- When conflicting information exists between the patient-reported medication history and pharmacy records, document both versions and escalate to the prescribing provider for resolution rather than choosing one source over the other.
- Non-formulary home medications that cannot be therapeutically substituted must be flagged for the discharge planning team at least 24 hours before anticipated discharge to ensure prescription coverage and pharmacy availability.
