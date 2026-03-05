---
name: managing-inpatient-consultations
description: Structures consultation requests and responses with specific clinical questions and recommendations. Use when requesting consults, responding to consultations, or documenting specialist input.
tags:
  - management
  - hospital-medicine
  - clinical
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

# Managing Inpatient Consultations

Structures consultation requests and responses with specific clinical questions and recommendations for effective specialist collaboration.

## Why This Skill Exists

Inpatient consultations are a primary driver of both clinical quality and length of stay. Poorly structured consultation requests — vague questions, missing data, unclear urgency — delay specialist response by an average of 4-8 hours and result in non-actionable recommendations 30% of the time. The Goldman 10 Commandments of Effective Consultation, first published in 1983 and still widely referenced, established that consultation quality depends entirely on the specificity of the question asked.

Hospitalists manage an average of 2-5 consultation requests per patient admission. CMS requires that consultation notes document the clinical question, the consultant's evaluation, and specific recommendations. The Joint Commission expects that consultation recommendations are acknowledged by the requesting physician with documented agree/disagree/modify decisions. Failure to follow up on consultation recommendations is a top-10 cause of malpractice claims in hospital medicine.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Before requesting or documenting a consultation, confirm:

1. What is the **specific clinical question** you need answered? *(Default: Must be a question, not "please evaluate")*
2. What is the **urgency** — Emergent (< 1 hour), Urgent (< 4 hours), Routine (within 24 hours)? *(Default: Routine)*
3. What **workup has already been done** relevant to this question? *(Default: List labs, imaging, prior consults)*
4. What is the **working diagnosis** and relevant history? *(Default: Per admitting H&P and progress notes)*
5. Has the requesting physician **spoken directly** with the consultant (required for Emergent/Urgent)? *(Default: Phone call for Emergent/Urgent; EMR order for Routine)*
6. What does the requesting physician **think is going on** and what are they hoping the consultant will help with? *(Default: Document pre-consult differential)*
7. Is the patient's **code status** relevant to the consultation question? *(Default: Include if goals-of-care may affect recommendation)*

### Documents to Request

- Recent H&P and daily progress notes
- Relevant lab results (trending, not just most recent)
- Imaging reports and actual images available for consultant review
- Medication list with recent changes
- Prior consultation notes (from current and recent admissions)
- Allergy list
- Advance directives if goals-of-care impact is possible

---

## Step 1: Structure the Consultation Request (5 Cs Framework)

Use the 5 Cs to write effective consultation requests:

### Contact
- Requesting physician name, pager/phone, service
- Patient name, MRN, room number, admitting diagnosis

### Clinical Question
Write the question in one of these formats:
- **Diagnostic**: "Does this patient have [condition]? Supporting data includes [X, Y, Z]."
- **Management**: "Patient has confirmed [diagnosis]. What is the recommended treatment approach given [complicating factors]?"
- **Procedural**: "Patient requires [procedure]. Is the patient a candidate given [risk factors]?"
- **Risk assessment**: "What is this patient's risk for [outcome] given [clinical scenario]?"

**Bad examples** (vague, non-actionable):
- "Please evaluate" ← No question
- "Consult for management" ← No specificity
- "Abnormal labs" ← Which labs? What is the clinical concern?

**Good examples** (specific, actionable):
- "72F with new AFib with RVR on telemetry. CHA2DS2-VASc 4. Is rate control vs. rhythm control preferred, and what anticoagulation do you recommend given CrCl 35 mL/min?"
- "55M with cirrhosis, platelet count 45K, needs therapeutic paracentesis. Is platelet transfusion required pre-procedure?"

### Context
- Relevant PMH, medications, allergies
- Workup already completed with results
- Current treatment and response

### Constraints
- Time-sensitive factors (planned discharge, scheduled surgery)
- Patient preferences or goals-of-care considerations
- Insurance or formulary restrictions

### Communication Preference
- How should the consultant communicate recommendations — note only, call back, see urgently?
- Who should be contacted if the requesting physician is off service?

---

## Step 2: Process Consultant Recommendations

When a consultation note is received, the hospitalist must document:

**Acknowledgment Template:**
```
Consultant: [Name, Specialty]
Date of consultation: [Date]
Clinical question: [Restate]
Key recommendations:
1. [Recommendation 1] — AGREE / DISAGREE / MODIFY
2. [Recommendation 2] — AGREE / DISAGREE / MODIFY
3. [Recommendation 3] — AGREE / DISAGREE / MODIFY

Rationale for any disagreement or modification: [Explain]
Orders placed based on recommendations: [List]
Follow-up plan with consultant: [One-time vs. ongoing, next contact]
```

---

## Step 3: Manage Multiple Consultants

For patients with 3+ active consultants, prevent fragmentation:

1. **Maintain a consultation tracker** in the progress note:

| Specialty | Consultant | Question | Status | Key Recs | Follow-up |
|-----------|-----------|----------|--------|----------|-----------|
| Cardiology | Dr. Smith | Rate control for AFib | Active | Diltiazem drip, target HR < 110 | Daily |
| ID | Dr. Jones | Duration of IV abx for osteo | Pending | — | Awaiting MRI |
| Nephrology | Dr. Lee | AKI management | Completed | Hold ACE, IVF at 75 mL/hr | PRN |

2. **Identify the primary decision-maker** for each clinical issue — the hospitalist owns the overall care plan
3. **Resolve conflicting recommendations** — When two consultants disagree, document the conflict and the hospitalist's resolution with rationale
4. **Set expectations for follow-up frequency** — "Consultant will follow daily" vs. "One-time consult, recs only"

---

## Step 4: Consultation Etiquette and Efficiency

Follow these evidence-based practices to optimize consultation:

- **Call before clicking**: For urgent/emergent consults, always call the consultant before placing the EMR order
- **One question per consult**: Avoid "kitchen sink" consult requests — multiple unrelated questions reduce response quality
- **Provide the data**: Ensure labs and imaging are resulted before requesting the consult
- **Respect scope**: Do not request consultants to manage problems outside their specialty
- **Follow up promptly**: Acknowledge consultation recommendations within 24 hours
- **Close the loop**: When a one-time consult is complete, document that the consultant has signed off

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After processing each consultation:

1. Is the **clinical question** specific and answerable?
2. Have all consultant **recommendations** been acknowledged with agree/disagree/modify?
3. Are **orders** reflecting accepted recommendations actually placed?
4. Is the **follow-up plan** documented (ongoing vs. one-time, next contact)?
5. Have **conflicting recommendations** from multiple consultants been resolved and documented?

---

## Quality Audit

- [ ] Consultation request contains a specific, answerable clinical question
- [ ] Urgency level is documented and communicated appropriately
- [ ] Relevant workup results are available to the consultant at time of request
- [ ] Direct physician communication occurred for Emergent/Urgent consults
- [ ] Consultant note is reviewed within 24 hours of completion
- [ ] Each recommendation has documented agree/disagree/modify response
- [ ] Orders reflecting accepted recommendations are placed promptly
- [ ] Conflicting consultant recommendations are resolved with documentation
- [ ] Consultation tracker is maintained for patients with 3+ consults
- [ ] Follow-up frequency is documented (daily, PRN, one-time, signed off)
- [ ] Curbside consultations that result in management changes are documented as formal consults
- [ ] Code status is communicated to consultants when relevant

---

## Guidelines

- The consultation question drives the quality of the response — invest time in writing a precise question
- Never place a consultation request without first reviewing what workup has already been done
- Emergent and Urgent consults require direct verbal communication — an EMR order alone is insufficient
- The hospitalist remains the primary coordinator of care — consultant recommendations are advisory, not directive
- When a consultant recommends a test or treatment, the hospitalist is responsible for evaluating it in the context of the full clinical picture
- Document disagreements respectfully and with clinical rationale — "Declining cardiology recommendation for cardiac catheterization given patient's comfort-measures-only code status and documented goals-of-care discussion"
- Curbside consultations (informal phone advice) should not be used for complex clinical decisions — if the recommendation changes management, convert to a formal consult
- Close out consultations explicitly — "Endocrinology signing off per Dr. X, insulin regimen optimized, follow up as outpatient"
