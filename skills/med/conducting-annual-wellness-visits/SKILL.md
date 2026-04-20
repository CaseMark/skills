---
name: conducting-annual-wellness-visits
language: en
description: Structures Medicare Annual Wellness Visit documentation with HRA, prevention plan, and advance care planning. Use when performing wellness visits, documenting AWVs, or creating personalized prevention plans.
tags:
  - process
  - primary-care
metadata:
  author: casemark
  practice_areas:
    - Family Medicine
    - Internal Medicine
    - Primary Care
  document_types:
    - Process Documentation
  skill_modes:
    - Process Management
---

# Conducting Annual Wellness Visits

Structures Medicare Annual Wellness Visit documentation with HRA, prevention plan, and advance care planning.

## Why This Skill Exists

The Medicare Annual Wellness Visit (AWV) is a distinct preventive service established under the Affordable Care Act (Section 4103) that differs fundamentally from a routine physical exam. CMS requires specific elements—Health Risk Assessment (HRA), personalized prevention plan, and cognitive screening—without which the visit cannot be billed under G0438 (Initial) or G0439 (Subsequent). Improper documentation leads to claim denials, audit liability, and missed quality measure opportunities under MIPS/APMs.

Primary care practices frequently conflate the AWV with a problem-focused visit or standard annual exam, resulting in undercoding, overbilling, or omission of mandatory elements. This skill enforces the CMS-mandated structure to ensure every AWV captures required data, generates a compliant Personalized Prevention Plan Summary (PPPS), and triggers appropriate USPSTF-recommended screenings based on patient demographics and risk profile.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. Is this an Initial AWV (G0438, no prior AWV) or Subsequent AWV (G0439)? **Default: G0439**
2. What is the patient's age, sex assigned at birth, and current gender identity? **Default: [REQUIRED]**
3. Has the Health Risk Assessment (HRA) questionnaire been completed by the patient? **Default: pending**
4. What is the patient's Medicare enrollment status and Part B effective date? **Default: active**
5. Is there an existing Personalized Prevention Plan Summary on file from a prior AWV? **Default: none**
6. Does the patient have a documented advance directive or healthcare proxy? **Default: unknown**
7. Has a cognitive assessment been performed within the past 12 months? **Default: no**
8. What chronic conditions are listed in the current problem list? **Default: per EHR**

### Documents to Request

- Completed HRA questionnaire (CMS model or practice-specific validated tool)
- Current medication list including OTCs and supplements
- Most recent immunization records from state IIS registry
- Prior year's Personalized Prevention Plan Summary (if Subsequent AWV)
- Advance directive or POLST if available
- Family history updated within past 3 years
- Functional status assessment (ADLs/IADLs for patients 65+)
- Depression screening result (PHQ-2 or PHQ-9 within past 12 months)

---

## Step 1: Health Risk Assessment Review

Parse the completed HRA to extract and document the following CMS-required domains:

| HRA Domain | Required Elements | Documentation Standard |
|---|---|---|
| Demographics | Age, sex, race/ethnicity, primary language | Structured fields |
| Psychosocial risks | Living situation, caregiver status, social isolation | Free text with codes |
| Behavioral risks | Tobacco, alcohol (AUDIT-C), physical activity, diet, seatbelt use | Standardized scores |
| Functional status | ADL/IADL assessment, hearing, vision, fall history | Validated instruments |
| Mental health | PHQ-2 screening; if positive (≥3), administer PHQ-9 | Numeric score documented |
| Home safety | Home hazards, fall prevention measures, DME needs | Checklist format |

Flag any HRA domain that is incomplete with [INCOMPLETE - REQUIRED FOR BILLING]. The AWV cannot be finalized until all domains are addressed.

---

## Step 2: Cognitive Assessment and Detection

CMS requires a structured cognitive assessment at every AWV, distinct from the depression screen.

- Administer a validated instrument: Mini-Cog (preferred for brevity), MMSE, MoCA, or GPCOG
- Document the instrument used, raw score, and interpretation
- Mini-Cog scoring: 3-word recall (0-3) + clock draw (0 or 2); total 0-2 = positive screen
- If screen is positive: document plan for full diagnostic workup per NIA-AA criteria
- If patient declines cognitive screening: document refusal and medical decision-making rationale
- Note: Do NOT use ICD-10 code R41.81 (age-related cognitive decline) unless diagnostic workup supports it

---

## Step 3: Personalized Prevention Plan Summary (PPPS)

Generate the PPPS containing all CMS-required elements:

1. **Screening schedule** — Apply USPSTF Grade A/B recommendations based on age, sex, and risk factors:
   - Colorectal cancer: age 45-75 (Grade A); 76-85 individualized (Grade C)
   - Breast cancer: mammography every 2 years, age 50-74 (Grade B)
   - Lung cancer: low-dose CT annually if age 50-80, ≥20 pack-year history, current smoker or quit within 15 years (Grade B)
   - Cervical cancer: Pap q3y ages 21-29; Pap+HPV co-test q5y ages 30-65
   - AAA: one-time ultrasound for males 65-75 who have ever smoked (Grade B)
   - Hepatitis C: universal screening for adults 18-79 (Grade B)

2. **Immunization schedule** — Per current ACIP recommendations:
   - Influenza annually
   - Pneumococcal: PCV20 alone OR PCV15 followed by PPSV23 ≥1 year later (age ≥65 or high-risk)
   - Td/Tdap booster every 10 years
   - Shingrix: 2-dose series for age ≥50
   - COVID-19: per current CDC guidance

3. **Risk factor reduction** — Specific interventions for each identified behavioral risk
4. **Referrals** — Specialist, community, or social service referrals based on HRA findings
5. **Advance care planning** — Document discussion or offer; bill 99497 if ≥16 minutes spent

---

## Step 4: Medical History and Examination Update

Update the longitudinal record with:

- Current weight, height, BMI with trend from prior AWV
- Blood pressure with notation of measurement technique (seated, appropriate cuff size)
- Visual acuity screening (Snellen chart or equivalent)
- Hearing assessment (whispered voice test or audiometry referral)
- Fall risk: Ask about falls in past 12 months; if ≥1 fall, perform Timed Up and Go (TUG)
- Review and update surgical history, family history (first-degree relatives), and social history
- Medication reconciliation: compare patient-reported list against EHR; flag discrepancies with [RECONCILE]

---

## Step 5: Advance Care Planning Documentation

If advance care planning (ACP) is discussed:

- Document who was present (patient, family, healthcare proxy)
- Record the nature of the discussion: goals of care, resuscitation preferences, healthcare proxy designation
- Note any existing documents reviewed: living will, DPOA-HC, POLST/MOLST
- If time spent on ACP ≥16 minutes face-to-face: bill 99497 as add-on to AWV
- If ≥30 additional minutes: bill 99498
- Store completed advance directive in EHR with scan of signed document

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Are all six HRA domains documented with responses or marked as patient-declined?
2. Does the PPPS include at least three age/sex-appropriate screening recommendations with USPSTF grades?
3. Is the cognitive screen documented with instrument name, score, and interpretation?
4. Has medication reconciliation been completed with discrepancy count noted?
5. Is the billing code (G0438 or G0439) supported by all required documentation elements?

---

## Quality Audit

- [ ] HRA completed and all six domains documented
- [ ] Correct visit code selected (G0438 for initial, G0439 for subsequent)
- [ ] Cognitive screening performed with validated tool and score recorded
- [ ] Depression screening (PHQ-2 minimum) performed and scored
- [ ] Personalized Prevention Plan Summary generated with screening schedule
- [ ] USPSTF recommendations applied correctly for patient demographics
- [ ] Immunization status reviewed against ACIP schedule with updates ordered
- [ ] Functional status (ADLs/IADLs) assessed and documented
- [ ] Fall risk assessed with TUG if history of falls
- [ ] Advance care planning discussed or offered; ACP time documented if billed
- [ ] Medication reconciliation completed with discrepancy resolution
- [ ] BMI calculated and plotted against prior trend
- [ ] Referrals generated for identified risk factors
- [ ] Patient received written copy of PPPS
- [ ] Next AWV scheduling recommended at 12-month interval

---

## Guidelines

- Never combine AWV billing with a problem-focused E/M code on the same visit unless a significant, separately identifiable condition is addressed and modifier -25 is appended to the E/M code
- The AWV does NOT include a hands-on physical examination by CMS definition; any exam performed must be billed separately
- HRA must be completed by the patient (or proxy) prior to or during the visit—clinician-completed HRAs do not meet CMS requirements
- Cognitive screening is mandatory at every AWV regardless of patient age or prior results
- USPSTF Grade D recommendations (e.g., PSA screening in men >70 without symptoms) should not appear in the PPPS unless specifically requested by the patient with shared decision-making documented
- Advance care planning time must be face-to-face time with the physician or qualified healthcare professional; MA-administered forms do not count toward ACP billing time
- Document all patient refusals of recommended screenings with the specific screening refused and brief rationale
- State immunization information system (IIS) must be queried and reconciled at each AWV per state reporting requirements
