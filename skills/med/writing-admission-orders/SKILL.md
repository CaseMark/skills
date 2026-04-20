---
name: writing-admission-orders
language: en
description: Generates structured admission order sets with diagnosis-specific protocols and safety checks. Use when admitting patients, creating admission orders, or setting up inpatient care plans.
tags:
  - drafting
  - hospital-medicine
  - patient-care
metadata:
  author: casemark
  practice_areas:
    - Hospital Medicine
    - Internal Medicine
  document_types:
    - Written Document
  skill_modes:
    - Drafting
---

# Writing Admission Orders

Generates structured admission order sets with diagnosis-specific protocols and safety checks for inpatient admissions.

## Why This Skill Exists

Admission order errors are a leading source of preventable harm in hospital medicine. Studies show that up to 30% of admission orders contain at least one error, including wrong doses, missed allergies, omitted VTE prophylaxis, or failure to reconcile home medications. The Joint Commission's National Patient Safety Goals (NPSGs) mandate medication reconciliation at every transition of care, and CMS Conditions of Participation require that all orders be complete, legible, and authenticated.

Hospitalists write an average of 15-25 admission order sets per shift. The ADC (Admit-Discharge-Consult) mnemonic and structured order sets reduce omission rates by 40-60% compared to free-text orders. This skill enforces the systematic approach required by institutional policy, evidence-based medicine, and regulatory standards to minimize harm during the high-risk admission window.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Before writing any admission orders, confirm the following:

1. What is the **admitting diagnosis** and ICD-10 code? *(Default: per ED or clinic assessment)*
2. What is the **admission status** — Inpatient vs. Observation? *(Default: Inpatient)*
3. What **level of care** is required — Floor, Telemetry, Step-down, ICU? *(Default: Floor/Med-Surg)*
4. Has **medication reconciliation** been completed with the home medication list? *(Default: Pending — flag [VERIFY])*
5. Are there **known drug allergies** with reaction types documented? *(Default: NKDA until confirmed)*
6. What is the patient's **code status**? *(Default: Full Code until goals-of-care discussion)*
7. Are there **isolation precautions** needed (Contact, Droplet, Airborne)? *(Default: Standard)*
8. Does the patient have a **VTE risk score** (Padua or Caprini) calculated? *(Default: Pending)*

### Documents to Request

- Emergency department H&P or clinic transfer note
- Current medication list (pharmacy fill history preferred)
- Recent lab results (within 24 hours)
- Imaging reports relevant to admitting diagnosis
- Allergy list with documented reaction types
- Advance directives or POLST form if available
- Insurance authorization or pre-certification (for observation cases)
- Prior discharge summaries (if readmission within 30 days)

---

## Step 1: Apply the ADC-VANDALISM Mnemonic

Use the ADC-VANDALISM framework to ensure no order category is omitted:

| Letter | Category | Required Content |
|--------|----------|------------------|
| **A** | Admit to | Service, attending, unit, bed type |
| **D** | Diagnosis | Primary + secondary diagnoses with ICD-10 |
| **C** | Condition | Stable / Guarded / Critical |
| **V** | Vitals | Frequency, parameters for notification |
| **A** | Allergies | Drug, food, environmental with reaction type |
| **N** | Nursing | Activity level, fall precautions, I&Os, daily weights |
| **D** | Diet | NPO, cardiac, renal, diabetic, regular |
| **A** | Activity | Bed rest, BRP, ambulate TID, PT/OT eval |
| **L** | Labs | Admission labs, AM labs, trending schedule |
| **I** | IV fluids | Type, rate, bolus parameters |
| **S** | Special | DVT prophylaxis, GI prophylaxis, glycemic protocol |
| **M** | Medications | Scheduled, PRN, home meds to continue/hold |

---

## Step 2: Write Diagnosis-Specific Order Bundles

For each primary diagnosis, include evidence-based order bundles:

**Community-Acquired Pneumonia (CAP)**
- Blood cultures x2 before antibiotics
- Procalcitonin level
- CURB-65 or PSI scoring documented
- Antibiotic selection per ATS/IDSA guidelines (ceftriaxone + azithromycin for floor; broader for ICU)
- Switch criteria: tolerating PO, afebrile 24h, hemodynamically stable

**Acute Heart Failure (CHF Exacerbation)**
- Daily weights (same time, same scale)
- Strict I&Os with net negative fluid balance target
- BNP or NT-proBNP trending
- Sodium and potassium monitoring Q12h
- IV diuretic with documented dose and frequency
- Cardiology consult if new-onset HF or EF < 35%

**Chest Pain / ACS Rule-Out**
- Serial troponins at 0, 3, 6 hours (high-sensitivity protocol)
- Continuous telemetry monitoring
- 12-lead ECG on admission and with any symptom change
- ASA 325 mg unless contraindicated
- HEART score documented in assessment

---

## Step 3: Medication Safety Checks

Perform the following mandatory checks before finalizing medication orders:

1. **Allergy cross-reference** — Verify every ordered medication against documented allergies
2. **Renal dosing** — Adjust for CrCl < 60 mL/min (Cockcroft-Gault preferred); flag metformin, gabapentin, DOACs, enoxaparin
3. **Hepatic dosing** — Check Child-Pugh for acetaminophen caps, statins, opioids
4. **Drug interactions** — Flag QTc-prolonging combinations (fluoroquinolones + ondansetron), serotonin syndrome risk, duplicate anticoagulation
5. **High-alert medications** — Double-check insulin (units, not "U"), anticoagulants (indication documented), opioids (PCA parameters), potassium (rate limits)
6. **Home medication reconciliation** — Explicitly document continue / hold / modify for each home medication with rationale

---

## Step 4: VTE and Prophylaxis Orders

All admitted patients require VTE risk assessment within 24 hours of admission:

| Risk Level | Padua Score | Prophylaxis |
|------------|-------------|-------------|
| Low risk | < 4 | Early ambulation only |
| High risk | >= 4 | Enoxaparin 40 mg SQ daily OR heparin 5000 units SQ Q8h |
| Contraindication to pharmacologic | Any | SCDs (sequential compression devices) |
| High bleeding risk | HAS-BLED >= 3 or active bleed | SCDs + reassess daily |

Also include GI prophylaxis (PPI or H2 blocker) if patient has 2+ risk factors: ICU admission, mechanical ventilation, coagulopathy, history of GI bleed, or concurrent anticoagulation + antiplatelet therapy.

---

## Step 5: Nursing Communication Orders

Ensure nursing orders include actionable parameters:

- **Vital sign frequency**: Q4h routine; Q1-2h for step-down; continuous for ICU
- **Notification parameters**: HR < 50 or > 120, SBP < 90 or > 180, RR < 10 or > 24, O2 sat < 92%, temp > 38.3°C, UOP < 30 mL/hr
- **Fall precautions**: Based on Morse Fall Scale score (see managing-fall-prevention skill)
- **Activity orders**: Specific (ambulate 3x daily with assist x1) not vague ("activity as tolerated")
- **Restraint orders**: Time-limited, with 1:1 sitter considered first, documented justification

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

Before submitting admission orders, verify:

1. Does every medication have a documented **indication**?
2. Has **VTE prophylaxis** been addressed (ordered or contraindication documented)?
3. Are **code status** and **isolation precautions** explicitly ordered?
4. Have **notification parameters** been set for all vitals?
5. Is there a **follow-up plan** — AM labs, pending studies, consultant contact?

---

## Quality Audit

- [ ] Admitting diagnosis matches H&P assessment with ICD-10 code
- [ ] Admission status (Inpatient vs. Observation) explicitly stated
- [ ] Level of care (Floor/Tele/ICU) matches clinical acuity
- [ ] All allergies listed with reaction types
- [ ] Medication reconciliation completed — each home med addressed
- [ ] Renal/hepatic dose adjustments applied where indicated
- [ ] VTE prophylaxis ordered or contraindication documented
- [ ] Diet order is specific (not just "regular" without clinical consideration)
- [ ] Vital sign notification parameters included
- [ ] Code status documented
- [ ] DVT/GI prophylaxis addressed
- [ ] No duplicate therapeutic classes ordered
- [ ] High-alert medications include required safety parameters
- [ ] Pending labs/imaging have specific time frames
- [ ] Attending physician identified for authentication

---

## Guidelines

- Always use the ADC-VANDALISM framework to prevent category omissions
- Document rationale for holding any home medication during admission
- Never abbreviate "units" as "U" or "daily" as "QD" — use ISMP Do Not Use list
- Include weight-based dosing for anticoagulants and specify actual body weight vs. ideal body weight
- Set telemetry orders with a defined indication and planned duration (not indefinite)
- Flag any order that requires pharmacy verification before first dose (e.g., anticoagulant bridging, TPN)
- Escalate to attending when admission status (Inpatient vs. Observation) is ambiguous — this has major billing and patient liability implications
- Re-evaluate all PRN orders at 24 hours and convert to scheduled if used >= 3 times
