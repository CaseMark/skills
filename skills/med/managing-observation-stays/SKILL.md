---
name: managing-observation-stays
language: en
description: Tracks observation status criteria, time-based requirements, and conversion-to-inpatient triggers. Use when managing observation patients, determining inpatient conversion, or documenting observation criteria.
tags:
  - management
  - hospital-medicine
  - patient-care
metadata:
  author: casemark
  practice_areas:
    - Hospital Medicine
    - Internal Medicine
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---

# Managing Observation Stays

Tracks observation status criteria, time-based requirements, and conversion-to-inpatient triggers for hospitalized patients.

## Why This Skill Exists

Observation status is one of the most complex and financially consequential designations in hospital medicine. Under CMS rules, observation is an outpatient service — patients in observation status are not "admitted" to the hospital, which affects Medicare Part A eligibility for post-acute SNF coverage (the "3-midnight rule"), patient copayment obligations, and hospital reimbursement. Incorrect status designation costs hospitals an estimated $1-3 billion annually in denied claims and appeals.

The Two-Midnight Rule (CMS-1599-F, effective October 2013) establishes that if the physician expects the patient to require hospital care spanning at least two midnights, inpatient admission is appropriate. If the expected stay is fewer than two midnights, observation status is presumed unless the patient meets specific inpatient-only procedure criteria. Hospitalists are the primary decision-makers for observation vs. inpatient status, and must document the clinical reasoning supporting their determination to withstand utilization review and Medicare auditor scrutiny.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Before placing or managing a patient in observation status, confirm:

1. What is the **clinical indication** for hospital-based care? *(Default: Per ED evaluation or direct admission indication)*
2. What is the **expected duration** of the hospital stay? *(Default: Physician estimate based on clinical scenario)*
3. Does the expected stay meet the **Two-Midnight threshold** for inpatient admission? *(Default: Assess at time of placement)*
4. What **objective criteria** support observation placement — risk stratification scores, clinical pathways? *(Default: Apply condition-specific criteria below)*
5. What is the patient's **insurance type** — Medicare, Medicaid, commercial? *(Default: Verify at registration — affects financial impact significantly)*
6. Has the patient or family been notified of **observation status** per the Medicare Outpatient Observation Notice (MOON)? *(Default: Required within 36 hours for Medicare patients)*
7. Are there **SNF placement needs** that would be affected by observation status (3-midnight rule)? *(Default: Assess and discuss with case management)*

### Documents to Request

- ED evaluation and clinical decision-making documentation
- Risk stratification scores (HEART, Wells, CURB-65, etc.)
- CMS Two-Midnight Rule reference materials
- Institutional observation protocols and clinical pathways
- Utilization review criteria (InterQual, Milliman)
- MOON form template
- Prior admission/observation history (30-day lookback)

---

## Step 1: Apply Condition-Specific Observation Criteria

Common observation-appropriate conditions (expected stay < 2 midnights):

| Condition | Observation Criteria | Conversion Triggers (→ Inpatient) |
|-----------|---------------------|-----------------------------------|
| **Chest pain** | Low-to-intermediate HEART score (0-6), serial troponins negative | Positive troponin, new ECG changes, hemodynamic instability |
| **Syncope** | San Francisco Syncope Rule low risk, no cardiac history | New arrhythmia on telemetry, structural heart disease, recurrent syncope |
| **CHF exacerbation** | Mild volume overload, responsive to single IV diuretic dose | O2 requirement, IV diuretic > 24h, renal function worsening |
| **Asthma/COPD** | Responsive to nebulizers Q4h, SpO2 > 92% on ≤ 2L | Requiring continuous nebulizers, BiPAP, ICU-level care |
| **Cellulitis** | Limited area, no systemic toxicity, responsive to IV antibiotics | Spreading despite IV antibiotics, systemic sepsis, surgical consult needed |
| **TIA** | ABCD2 score < 4, imaging negative, symptom resolved | Persistent deficits, positive imaging, cardioembolic source found |
| **Hypoglycemia** | Corrected with treatment, identifiable cause, stable monitoring | Recurrent episodes, no identifiable cause, requiring IV dextrose drip |
| **Dehydration** | Responsive to 1-2L IV fluid bolus, tolerating PO | Persistent hemodynamic instability, unable to tolerate PO, AKI |

---

## Step 2: Document Medical Necessity for Status Determination

Every observation or inpatient status decision must include documented clinical reasoning:

**Observation status documentation:**
```
STATUS DETERMINATION NOTE

Status: Observation
Date/Time of placement: [Timestamp]
Clinical indication: [Diagnosis with supporting objective data]
Expected duration: [< 2 midnights — specify estimated hours]
Two-Midnight Rule assessment: Expected hospital stay does not span 
  two midnights because [clinical rationale]
Disposition plan: [Discharge criteria and expected discharge timeline]
Reassessment plan: [When to re-evaluate status — typically at 24 hours]
```

**Inpatient conversion documentation:**
```
STATUS CONVERSION NOTE

Previous status: Observation (placed [date/time])
New status: Inpatient (effective [date/time])
Reason for conversion: [Clinical change that now requires stay ≥ 2 midnights]
Supporting criteria: [New findings, failed treatment, complications]
Retroactive admission: Yes/No — if yes, admit effective [original date/time]
```

---

## Step 3: Track Time-Based Requirements

Monitor these critical time milestones:

| Milestone | Time Threshold | Action Required |
|-----------|---------------|-----------------|
| **MOON notification** | Within 36 hours of observation start (Medicare patients) | Deliver and document patient acknowledgment |
| **24-hour reassessment** | 24 hours from observation start | Re-evaluate status: discharge, continue observation, or convert to inpatient |
| **Two-Midnight boundary** | Approaching midnight #2 | If patient still requires care, strongly consider inpatient conversion |
| **48-hour review** | 48 hours in observation | Mandatory UR review; prolonged observation is a red flag for auditors |
| **3-midnight SNF impact** | If patient needs SNF | Observation days do not count toward Medicare's 3-midnight qualifying stay |

---

## Step 4: Manage the MOON (Medicare Outpatient Observation Notice)

CMS requires the MOON for all Medicare/Medicare Advantage patients in observation status:

1. **Timing**: Deliver no later than 36 hours after observation services begin
2. **Content**: Must explain observation status, the difference from inpatient, financial implications (copays, SNF eligibility)
3. **Delivery**: Provide to patient (or representative) in person
4. **Acknowledgment**: Patient signs and dates the form; if patient refuses to sign, document refusal
5. **Documentation**: Keep signed MOON in the medical record

---

## Step 5: Coordinate with Utilization Review

Proactive UR collaboration prevents denials:

- Provide clinical documentation supporting the status determination within the first 24 hours
- If UR disagrees with your status determination, discuss the case directly — understand their criteria (InterQual, Milliman) and address gaps
- Document severity of illness (SI) and intensity of service (IS) that justify the chosen status
- For patients crossing the two-midnight threshold: initiate conversion proactively rather than waiting for UR to flag

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

For each observation patient:

1. Is the **status determination** documented with clinical reasoning?
2. Has the **MOON** been delivered and signed (Medicare patients)?
3. Is there a **24-hour reassessment** plan for status re-evaluation?
4. Have **SNF implications** been discussed with case management and the patient/family?
5. Are **discharge criteria** clearly defined with an expected timeline?

---

## Quality Audit

- [ ] Observation status has documented clinical rationale
- [ ] Two-Midnight Rule assessment is explicit in the medical record
- [ ] Risk stratification score is documented for the observation-appropriate condition
- [ ] MOON delivered within 36 hours for Medicare patients
- [ ] 24-hour reassessment completed and documented
- [ ] Conversion to inpatient is documented with changed clinical criteria
- [ ] Discharge criteria are defined at time of observation placement
- [ ] Patient/family informed of observation status and financial implications
- [ ] SNF eligibility impact assessed and communicated to case management
- [ ] UR review completed for observation stays > 48 hours
- [ ] Disposition plan includes follow-up appointment within 48-72 hours
- [ ] Status determination is consistent across physician notes, orders, and case management records

---

## Guidelines

- Make the status determination at the time of placement, not retrospectively — document "I expect this patient to require hospital care for [X] hours, which is [less than / at least] two midnights"
- Never place a patient in observation solely for financial reasons — the determination must be based on clinical judgment and expected duration of care
- Reassess observation patients at 24 hours without exception — prolonged observation without reassessment is a CMS audit trigger
- The Two-Midnight Rule is a presumption, not an absolute — procedures on the Inpatient-Only list and rare clinical exceptions exist
- Always discuss SNF implications proactively with patients who may need post-acute care — observation days do not count toward the 3-midnight qualifying stay
- Document clinical decision-making contemporaneously — retrospective status changes invite auditor scrutiny
- If a patient's condition worsens and the stay will exceed two midnights, convert to inpatient promptly and consider retroactive admission to the original date
- Educate patients that observation status means they are technically outpatients and may face different copay structures
