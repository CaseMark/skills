---
name: coordinating-care-transitions
language: en
description: Manages post-hospitalization follow-up with medication reconciliation and readmission prevention. Use when following up after discharge, preventing readmissions, or coordinating transitional care.
tags:
  - coordination
  - primary-care
metadata:
  author: casemark
  practice_areas:
    - Family Medicine
    - Internal Medicine
    - Primary Care
  document_types:
    - Coordination Plan
  skill_modes:
    - Coordination
---

# Coordinating Care Transitions

Manages post-hospitalization follow-up with medication reconciliation and readmission prevention.

## Why This Skill Exists

Hospital readmissions within 30 days affect approximately 14% of Medicare patients, costing $26 billion annually, with $17 billion considered preventable. CMS penalizes hospitals with excess readmission rates through the Hospital Readmissions Reduction Program (HRRP), and primary care practices face quality measure scrutiny under MIPS for transitional care management (TCM). The critical 48-72 hour post-discharge window is when medication errors, misunderstood discharge instructions, and missed follow-up most commonly lead to decompensation.

Effective care transitions require structured medication reconciliation, timely follow-up scheduling, patient/caregiver education, and coordinated communication among the hospital team, PCP, specialists, and community services. CMS reimburses Transitional Care Management (TCM) services under CPT 99495 (moderate complexity, follow-up within 14 days) and 99496 (high complexity, follow-up within 7 days), but billing requires specific documented elements. This skill enforces the complete TCM workflow.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. What was the admission diagnosis and discharge date? **Default: [REQUIRED]**
2. Has the discharge summary been received and reviewed? **Default: pending**
3. Was the initial interactive contact (phone/telehealth) made within 2 business days of discharge? **Default: schedule**
4. What is the target for face-to-face visit (within 7 days for high complexity, 14 days for moderate)? **Default: assess complexity**
5. What medications were changed during the hospitalization (new, adjusted, discontinued)? **Default: per discharge summary**
6. Does the patient have home health, skilled nursing, or other post-acute services ordered? **Default: per discharge plan**
7. Is there a caregiver or family member involved in the transition? **Default: identify**
8. What pending test results or follow-up appointments were listed in the discharge summary? **Default: review**

### Documents to Request

- Hospital discharge summary (must include: diagnoses, procedures, medication reconciliation, follow-up instructions, pending results)
- Inpatient medication administration record (MAR)
- Discharge medication list compared to pre-admission medication list
- Nursing discharge notes (functional status, patient education provided)
- Consultant notes from hospitalization
- Pending lab/imaging results at time of discharge
- Home health or SNF orders
- Patient's pre-hospitalization medication list from PCP records
- DME orders (oxygen, CPAP, wound care supplies)
- Social work or case management discharge assessment

---

## Step 1: Initial Contact Within 2 Business Days

CMS requires interactive contact within 2 business days of discharge for TCM billing:

**Phone or telehealth contact checklist:**
- [ ] Confirm patient is at home (or current location) and stable
- [ ] Review discharge diagnosis and ensure patient understanding
- [ ] Assess for red flag symptoms requiring immediate evaluation:
  - Chest pain, severe SOB, high fever, wound dehiscence, altered mental status
  - Inability to take medications due to nausea/vomiting/cost
  - Worsening of the condition that prompted hospitalization
- [ ] Confirm patient has discharge medications in hand (physically obtained from pharmacy)
- [ ] Identify medication questions or confusion
- [ ] Confirm follow-up appointments scheduled (PCP, specialists)
- [ ] Assess home safety and support (caregiver availability, food, mobility)
- [ ] Schedule face-to-face visit (within 7 or 14 days depending on complexity)

Document: date, time, who was contacted, method (phone/video), findings, and plan.

---

## Step 2: Comprehensive Medication Reconciliation

This is the single highest-impact intervention for preventing readmission:

| Step | Action | Common Errors Found |
|---|---|---|
| 1. Obtain discharge med list | From discharge summary + pharmacy fill records | Discharge list often incomplete or contains inpatient-only medications |
| 2. Compare to pre-admission list | Side-by-side comparison of every medication | Chronic medications inadvertently discontinued (statins, antidepressants, eye drops) |
| 3. Identify new medications | Document indication for each new medication | Patient doesn't know why new med was started |
| 4. Identify discontinued medications | Confirm intentional vs. accidental omission | Duplicate classes prescribed (two anticoagulants, two beta-blockers) |
| 5. Identify dose changes | Note changed doses with effective date | Patient still taking old dose from refilled prescription |
| 6. Check for interactions | Drug-drug and drug-disease interactions in combined list | New antibiotic + warfarin, new NSAID + CKD |
| 7. Assess adherence barriers | Cost, access, complexity, understanding | Patient cannot afford new specialty medication |

Generate a reconciled medication list with disposition for each drug: **CONTINUE** (unchanged), **NEW** (started in hospital), **CHANGED** (dose adjusted), **STOPPED** (discontinued with reason), **HOLD** (temporarily suspended).

---

## Step 3: Face-to-Face TCM Visit

Structure the TCM visit to capture all required elements for CPT 99495/99496:

**Medical decision-making components:**
- Review discharge summary findings with patient
- Focused physical exam relevant to hospitalization diagnosis
- Review and finalize medication reconciliation
- Assess functional status compared to baseline
- Address pending test results from hospitalization
- Update problem list and diagnoses

**Condition-specific follow-up protocols:**

| Discharge Diagnosis | Critical Follow-Up Actions | Timeline |
|---|---|---|
| Heart failure | Daily weights, fluid restriction counseling, diuretic adjustment, BMP in 3-7 days | f/u within 7 days |
| COPD exacerbation | Inhaler technique review, OCS taper plan, pulmonary rehab referral | f/u within 7 days |
| Pneumonia | Repeat CXR at 6-8 weeks (if age >50 or smoker); complete antibiotics | f/u within 14 days |
| ACS / PCI | Verify DAPT compliance, statin optimization, cardiac rehab referral, BP control | f/u within 7 days |
| Hip/knee replacement | Wound assessment, DVT prophylaxis compliance, PT progress, pain management | f/u within 14 days |
| Diabetic ketoacidosis | Insulin regimen review, sick-day rules education, endocrine follow-up | f/u within 7 days |
| Stroke/TIA | Neurology follow-up, antiplatelet/anticoagulant management, rehabilitation status | f/u within 7 days |

---

## Step 4: Care Coordination and Communication

| Task | Responsible Party | Deadline |
|---|---|---|
| Send reconciled medication list to patient's pharmacy | PCP office | Within 3 days of TCM visit |
| Follow up on pending inpatient results (cultures, pathology, imaging) | PCP office | Within 7 days of discharge |
| Schedule specialist follow-up as recommended | PCP office or patient | Within timeframe specified in discharge summary |
| Notify home health agency of medication changes | PCP office | Day of TCM visit |
| Update specialist(s) on post-discharge status | PCP via portal/fax/secure message | Within 7 days of TCM visit |
| Coordinate DME needs | PCP office or case manager | Within 3 days of TCM visit |
| Social work referral if needed | PCP office | At TCM visit |

**High-risk patient identification for intensive follow-up:**
- LACE index (Length of stay, Acuity, Comorbidities, ED visits): score ≥10 = high readmission risk
- HOSPITAL score: ≥7 = high risk
- Patients with HF, COPD, AMI, pneumonia, hip/knee surgery (HRRP conditions)
- Patients with ≥3 chronic conditions, polypharmacy (≥10 medications), or lack of social support

---

## Step 5: TCM Billing Documentation

| CPT Code | Complexity | Face-to-Face Timing | Requirements |
|---|---|---|---|
| 99495 | Moderate medical decision complexity | Within 14 calendar days of discharge | Interactive contact within 2 business days + face-to-face visit + medication reconciliation |
| 99496 | High medical decision complexity | Within 7 calendar days of discharge | Same as 99495 but higher complexity and earlier visit |

**Required documentation elements:**
1. Date of discharge from facility
2. Date and method of interactive contact within 2 business days
3. Date of face-to-face visit
4. Medical decision complexity (moderate or high) with supporting documentation
5. Medication reconciliation documented with comparison of discharge vs. current list
6. Care coordination activities performed (referrals, communication with specialists/facilities)
7. Medical services provided during the 30-day TCM period

**Billing rules:**
- Only one provider can bill TCM per patient per 30-day period
- TCM cannot be billed if the patient is readmitted within the 30-day period before the face-to-face visit
- TCM is payable by Medicare, most Medicaid, and many commercial payers
- TCM is billable for discharge from hospital, SNF, LTAC, IRF, or psychiatric facility (not observation stays for some payers)

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Was the initial interactive contact made within 2 business days of discharge?
2. Is the complete medication reconciliation documented with disposition for every medication?
3. Did the face-to-face visit occur within the appropriate window (7 or 14 days)?
4. Are all pending results from the hospitalization tracked with follow-up plan?
5. Is the TCM billing documentation complete with all required elements?

---

## Quality Audit

- [ ] Discharge summary received and reviewed by PCP within 48 hours of discharge
- [ ] Interactive contact completed within 2 business days (date, time, method documented)
- [ ] Red flag symptoms screened during initial contact
- [ ] Patient confirmed to have discharge medications in hand
- [ ] Medication reconciliation completed: every medication has a disposition (continue, new, changed, stopped, hold)
- [ ] Drug duplications and interactions identified and resolved
- [ ] Face-to-face visit completed within 7 days (99496) or 14 days (99495)
- [ ] Condition-specific follow-up protocol applied
- [ ] Pending test results tracked with responsible party and timeline
- [ ] Specialist follow-up appointments scheduled per discharge recommendations
- [ ] Home health/SNF communication completed if applicable
- [ ] Readmission risk assessed (LACE or HOSPITAL score)
- [ ] TCM billing requirements documented (all required elements present)
- [ ] 30-day post-discharge period care plan documented

---

## Guidelines

- Never assume the discharge medication list is correct; always compare against the pre-admission list and clarify discrepancies with the discharging team
- The 2-business-day interactive contact is a hard CMS requirement for TCM billing; a voicemail or portal message does NOT count—it must be an interactive exchange (live phone, video, or in-person)
- High-complexity TCM (99496) requires both high-complexity MDM and a face-to-face visit within 7 days; do not upcode if either criterion is unmet
- Medication reconciliation must be documented as a distinct activity, not just a medication list in the chart; show the comparison and decisions made for each medication
- Heart failure patients discharged on new or adjusted diuretics/ACEi/ARB require a BMP within 3-7 days to check potassium and creatinine; this is the most commonly missed post-discharge lab
- Patients discharged on anticoagulants (especially new starts) require INR check within 3-5 days (warfarin) or renal function monitoring (DOACs) and bleeding precaution education
- If the discharge summary has not been received within 48 hours, actively contact the discharging facility; do not wait for it to arrive passively
- Document all care coordination activities (phone calls, faxes, referrals, communications) with date, time, and content summary to support TCM billing
