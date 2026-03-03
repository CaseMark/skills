# Discharge Summary Output Template

Use this template as the structural scaffold for every discharge summary produced by the `summarizing-discharge-notes` skill. Not every section applies to every patient — omit sections that are clinically irrelevant rather than filling them with "N/A."

---

## Front Matter (Always First)

| Field | Value |
|---|---|
| Patient Name | |
| DOB | |
| MRN | |
| Admission Date | |
| Discharge Date | |
| Length of Stay | |
| Discharge Disposition | Home / SNF / Rehab / Home with Services / AMA |
| Attending Physician | |
| Primary Care Provider | |
| Allergy Status | List all drug allergies with reaction type. If none documented: `[ALLERGY STATUS NOT DOCUMENTED — VERIFY]` |

### Assumptions Used

> List: source documents reviewed, target audience, complexity tier applied, any defaults used.

### Open Items / Needed Inputs

> List: missing source documents, unreconciled medications, unresolved `[VERIFY]` tags, items requiring provider follow-up.

---

## 1. Diagnoses

### Primary Diagnosis

| Diagnosis | ICD-10 | Status at Discharge | Follow-Up Plan |
|---|---|---|---|

### Secondary / Comorbid Diagnoses

| # | Diagnosis | ICD-10 | Status at Discharge | Follow-Up Plan |
|---|---|---|---|---|
| 1 | | | Active / Stable / Resolved | |
| 2 | | | | |
| 3 | | | | |

---

## 2. Hospital Course

> Concise narrative synthesis (3-8 sentences for moderate complexity, up to 15 for complex):
>
> - Why admitted
> - Key clinical events and decision points
> - Response to treatment
> - Condition at discharge relative to admission

---

## 3. Procedures Performed

| Procedure | Date | Performing Provider | Findings / Outcome | Follow-Up Needed |
|---|---|---|---|---|
| | | | | |

If no procedures: omit this section.

---

## 4. Discharge Medications

### Standing Medications

| Medication | Dose | Route | Frequency | Status | Change Reason | Special Instructions |
|---|---|---|---|---|---|---|
| | | | | NEW | | |
| | | | | CHANGED | Dose increased from X to Y due to Z | |
| | | | | CONTINUED | | |

### PRN Medications

| Medication | Dose | Route | Frequency / Max | Indication | Special Instructions |
|---|---|---|---|---|---|
| | | | | | |

### Discontinued Medications

| Medication | Previous Dose | Reason for Discontinuation |
|---|---|---|
| | | |

### High-Alert Medication Callouts

> List any of the following with explicit dosing, monitoring, and safety instructions:
> - Anticoagulants (warfarin, DOACs, enoxaparin)
> - Insulin (basal, prandial, correction scale — specify each)
> - Opioids (include taper plan if applicable)
> - Immunosuppressants
> - Narrow therapeutic index drugs (digoxin, phenytoin, lithium, theophylline)

### Reconciliation Notes

> Document any discrepancies found between admission and discharge medication lists. Flag unresolved items:
>
> - "Home medication X not addressed in discharge documents `[VERIFY — continue or discontinue?]`"
> - "Discharge list includes Y but MAR shows it was held on HD3 and not restarted `[RECONCILE]`"

---

## 5. Pending Results

| Item | Ordered Date | Expected Result Date | Responsible Provider | Action if Abnormal |
|---|---|---|---|---|
| | | | | |

If no pending items: "No pending results identified in available source documents."

---

## 6. Follow-Up Appointments

| Provider / Specialty | Timeframe | Purpose | Scheduled (Y/N) | Contact Info |
|---|---|---|---|---|
| PCP | Within 7 days | Med reconciliation, wound check | | |
| Cardiology | Within 2 weeks | Echo follow-up | | |
| Surgery | 6 weeks post-op | Staple removal | | |

---

## 7. Activity Restrictions

| Restriction | Duration | Conditions / Details |
|---|---|---|
| No lifting > 10 lbs | 6 weeks | Post-surgical; reassess at surgery follow-up |
| No driving | Until off opioids for 24h | Also applies if sedation was used within 24h |
| Fall precautions | Ongoing | New balance impairment; use walker at all times |

If no restrictions: omit this section.

---

## 8. Diet

| Diet Order | Rationale | Duration |
|---|---|---|
| 2g sodium restriction | New CHF diagnosis | Indefinite — reassess with cardiology |
| Mechanical soft | Post-oral surgery | 2 weeks |
| Diabetic / carb-controlled | A1c 9.2, new insulin regimen | Ongoing |

If regular diet with no restrictions: omit this section.

---

## 9. Wound / Device / Drain Care

| Site | Description | Dressing / Care Instructions | Change Frequency | Signs of Complication | Contact for Issues |
|---|---|---|---|---|---|
| RLQ incision | 8cm, closed with staples, steri-strips | Dry gauze, keep clean and dry | Daily | Redness, warmth, drainage, dehiscence, fever >101.0F | Surgeon office: (xxx) xxx-xxxx |
| PICC line (R arm) | 4Fr dual lumen | Flush per home health protocol | Dressing q7d by home health | Redness at site, swelling of arm, fever | Home health agency |

If no wounds / devices / drains: omit this section entirely.

---

## 10. Return Precautions (Warning Signs)

> **These must be diagnosis-specific.** Do not use generic boilerplate.

### For [Primary Diagnosis]:

**Seek emergency care (call 911 or go to ER) if:**
- [Specific symptom 1]
- [Specific symptom 2]

**Call your doctor's office within 24 hours if:**
- [Specific symptom 3]
- [Specific symptom 4]

### For [Secondary Diagnosis if applicable]:

**Seek emergency care if:**
- [Specific symptom]

**Call your doctor's office if:**
- [Specific symptom]

### General Return Precautions:

- Fever > 101.0F (38.3C) not responding to acetaminophen
- Inability to tolerate oral medications or fluids
- New or worsening confusion

---

## 11. Additional Notes

> Use this section for anything that doesn't fit the above categories:
> - Social work / case management notes
> - Insurance / prior authorization issues for discharge medications
> - Interpreter needs or health literacy concerns
> - Advance directive status
> - Code status at discharge

---

## Patient / Caregiver Version (Lane 2)

When generating the patient-facing version, transform the above into plain language:

- Replace medical terminology with plain English (e.g., "heart failure" not "CHF with reduced EF")
- List each medication with its purpose in one sentence (e.g., "Metoprolol 25mg — take one tablet by mouth twice a day to help your heart beat at a normal rate")
- Use bullet points, not tables
- Reading level target: 6th grade
- No abbreviations (spell out everything)
- Bold the warning signs section
- Include the specific phone numbers to call for each type of concern
