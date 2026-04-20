---
name: screening-preventive-health
language: en
description: Applies USPSTF screening recommendations by age, sex, and risk factors. Use when ordering preventive screenings, creating screening schedules, or applying evidence-based prevention guidelines.
tags:
  - screening
  - primary-care
  - risk
metadata:
  author: casemark
  practice_areas:
    - Family Medicine
    - Internal Medicine
    - Primary Care
  document_types:
    - Screening Report
  skill_modes:
    - Screening
    - Filtering
---

# Screening Preventive Health

Applies USPSTF screening recommendations by age, sex, and risk factors.

## Why This Skill Exists

The U.S. Preventive Services Task Force (USPSTF) issues evidence-based screening recommendations graded A through D, plus "I" (insufficient evidence). Grade A and B recommendations carry a mandate under the ACA: non-grandfathered health plans must cover these services with zero cost-sharing. Failure to apply USPSTF guidelines results in missed cancers, undetected cardiovascular risk, and preventable morbidity—while also exposing practices to quality measure penalties under MIPS (Merit-based Incentive Payment System).

Primary care clinicians must match the right screening to the right patient at the right interval. Over-screening (e.g., PSA without shared decision-making, mammography in low-risk women under 40) drives unnecessary biopsies and patient anxiety. Under-screening (e.g., missed lung cancer screening in eligible smokers, skipped HCV testing) misses the window for curative intervention. This skill maps USPSTF grades to patient demographics to produce a precise, defensible screening schedule.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. What is the patient's age and sex assigned at birth? **Default: [REQUIRED]**
2. What is the patient's smoking history (pack-years, current/former/never, quit date)? **Default: never**
3. Does the patient have a first-degree family history of breast, colorectal, ovarian, or lung cancer? **Default: no**
4. What is the patient's BMI? **Default: calculate from vitals**
5. Has the patient ever been tested for HIV, Hepatitis B, or Hepatitis C? **Default: unknown**
6. Is the patient sexually active? Number of partners, contraceptive use? **Default: per patient report**
7. Does the patient have a history of gestational diabetes, PCOS, or prediabetes? **Default: no**
8. What screenings have been completed in the past 1-5 years? **Default: per EHR**

### Documents to Request

- EHR preventive health maintenance module / health maintenance alert summary
- Prior screening results (mammogram, colonoscopy, Pap, LDCT, DXA, labs)
- Immunization records from state IIS
- Family history pedigree (first- and second-degree relatives)
- Risk calculators already completed (Gail model, Tyrer-Cuzick, ASCVD risk)
- Genetic testing results if applicable (BRCA, Lynch syndrome)
- Social history including sexual health, substance use, occupational exposures

---

## Step 1: Universal Adult Screenings (Apply to All)

These USPSTF Grade A/B recommendations apply regardless of specific risk factors:

| Screening | Population | Interval | Grade |
|---|---|---|---|
| Blood pressure | Adults ≥18 | Annually if normal; confirm elevated with ABPM/HBPM | A |
| Depression (PHQ-2/PHQ-9) | Adults ≥18 | Annually with adequate systems for treatment | B |
| HIV | Adults 15-65 | At least once; more frequently if high-risk | A |
| Hepatitis C (anti-HCV) | Adults 18-79 | Once (unless ongoing risk) | B |
| Hepatitis B (HBsAg) | Adolescents and adults at increased risk | Per risk assessment | B |
| Unhealthy alcohol use (AUDIT-C) | Adults ≥18 | Annually with brief intervention | B |
| Unhealthy drug use | Adults ≥18 | Annual screening with brief intervention | B |
| Obesity (BMI) | Adults ≥18 | Every visit; refer to intensive behavioral counseling if BMI ≥30 | B |
| Tobacco use | Adults ≥18 | Every visit; offer cessation interventions | A |
| Statin for CVD prevention | Adults 40-75 with ≥1 CVD risk factor and 10-year risk ≥10% | Per ASCVD risk calculation | B |
| Prediabetes/T2DM | Adults 35-70 who are overweight or obese | Every 3 years if normal | B |

---

## Step 2: Cancer Screenings by Demographics

| Cancer | Population | Method | Interval | Grade | Notes |
|---|---|---|---|---|---|
| Breast | Women 50-74 | Mammography | Every 2 years | B | 40-49: individualized per 2024 update (Grade B) |
| Cervical | Women 21-65 | Pap alone (21-29); Pap+HPV co-test or HPV primary (30-65) | Every 3 years (Pap); every 5 years (co-test/HPV primary) | A | Stop at 65 if adequate prior screening |
| Colorectal | Adults 45-75 | Colonoscopy q10y, FIT annually, FIT-DNA q1-3y, CT colonography q5y | Per modality | A | 76-85: individualized (Grade C) |
| Lung | Adults 50-80, ≥20 pack-year history, current or quit <15 years | Low-dose CT (LDCT) | Annually | B | Shared decision-making required |
| Prostate | Men 55-69 | PSA | Individualized | C | Shared decision-making required; Grade D for ≥70 |
| Skin | General population | Whole-body exam | N/A | I | Insufficient evidence for routine screening |

---

## Step 3: Reproductive and Sexual Health Screenings

| Screening | Population | Interval | Grade |
|---|---|---|---|
| Chlamydia | Sexually active women ≤24; older women at increased risk | Annually | B |
| Gonorrhea | Sexually active women ≤24; older women at increased risk | Annually | B |
| Syphilis | Persons at increased risk | Per risk assessment | A |
| Intimate partner violence | Women of reproductive age | Screening with referral resources | B |
| Preeclampsia prevention | Pregnant women at high risk | Low-dose aspirin after 12 weeks gestation | B |
| Gestational diabetes | Pregnant women ≥24 weeks | OGTT or two-step glucose challenge | B |
| Rh incompatibility | Pregnant women at first prenatal visit | Blood typing and antibody screen | A |
| BRCA-related cancer risk | Women with family history suggestive of BRCA1/2 | Risk assessment tool → genetic counseling referral | B |

---

## Step 4: Age-Stratified Prevention Schedule

Generate a schedule customized to the patient's age band:

**Ages 18-39:**
- BP annually, BMI every visit, depression screen annually
- HIV once, HCV once (18-79), STI screening per risk
- Cervical cancer screening per Step 2
- Folic acid supplementation for women planning pregnancy (Grade A)

**Ages 40-49:**
- All of above plus: diabetes screening if overweight/obese
- ASCVD risk calculation; statin discussion if 10-year risk ≥10%
- Breast cancer: individualized mammography discussion
- Lung cancer: begin LDCT if meets smoking criteria

**Ages 50-64:**
- All of above plus: colorectal cancer screening (if not started at 45)
- Lung cancer screening annually if eligible
- Mammography every 2 years
- DXA for postmenopausal women with risk factors (FRAX)

**Ages 65-75:**
- All age-appropriate screenings
- AAA: one-time ultrasound for men who have ever smoked (Grade B)
- Osteoporosis: DXA for all women ≥65 (Grade B)
- Cease cervical cancer screening if adequate prior screening
- Hearing screening (USPSTF Grade I, but commonly performed)

**Ages 76+:**
- Individualize all screening based on life expectancy, functional status, patient preference
- Colorectal cancer: 76-85 individualized (Grade C); stop after 85
- Discontinue mammography when life expectancy <10 years

---

## Step 5: Documentation and Shared Decision-Making

For each screening:
- Document whether screening was performed, ordered, or deferred
- If deferred: record patient-specific rationale (declined, not indicated, contraindicated)
- For Grade C recommendations (e.g., PSA, CRC 76-85): document shared decision-making discussion including benefits, harms, and patient preference
- Generate a patient-facing prevention summary with due dates for next screenings
- Update EHR health maintenance module to trigger future reminders

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Are all Grade A/B recommendations addressed for the patient's age and sex?
2. Have Grade C recommendations been handled with documented shared decision-making?
3. Are screening intervals correct for each modality (e.g., colonoscopy q10y, mammogram q2y)?
4. Has family history triggered any enhanced screening protocols (e.g., early colonoscopy, BRCA assessment)?
5. Are declined screenings documented with patient rationale?

---

## Quality Audit

- [ ] Age and sex correctly applied to USPSTF recommendation matrix
- [ ] All Grade A recommendations documented as completed, ordered, or patient-declined
- [ ] All Grade B recommendations documented as completed, ordered, or patient-declined
- [ ] Grade C recommendations addressed with shared decision-making note
- [ ] Grade D recommendations NOT ordered (e.g., no routine PSA for men ≥70)
- [ ] Cancer screening intervals match USPSTF guidelines for the chosen modality
- [ ] Smoking history documented with pack-years to determine lung cancer screening eligibility
- [ ] HIV screening offered at least once for adults 15-65
- [ ] Hepatitis C screening offered once for adults 18-79
- [ ] ASCVD risk calculated for adults 40-75 with statin decision documented
- [ ] Immunizations reviewed against ACIP schedule
- [ ] Patient-facing prevention plan generated with next screening due dates
- [ ] Health maintenance module in EHR updated with current screening status
- [ ] MIPS quality measure alignment checked for reportable screenings

---

## Guidelines

- Never apply USPSTF recommendations without considering individual risk factors—Grade B screenings may need earlier initiation in high-risk patients (e.g., colonoscopy at 40 if first-degree relative diagnosed before 60)
- Grade I (insufficient evidence) does not mean "do not screen"—it means the evidence is inadequate to assess the balance of benefits and harms; clinical judgment applies
- USPSTF recommendations apply to asymptomatic individuals; symptomatic patients require diagnostic evaluation, not screening
- Screening benefits diminish as life expectancy shortens; avoid screening when the time horizon for benefit exceeds estimated survival
- Document the USPSTF grade for each screening ordered to support medical necessity and insurance coverage
- STI screening questions must be asked in a non-judgmental, culturally sensitive manner with confidentiality assurances
- Lung cancer screening with LDCT requires a shared decision-making visit including discussion of false positive rates (approximately 25% per round)
- Update screening protocols annually as USPSTF issues new or revised recommendations; check uspstf.org for current grades
