---
name: managing-diabetes-mellitus
language: en
description: Structures diabetes management with ADA standards including A1c targets, medication algorithms, and complication screening. Use when managing diabetes, adjusting insulin regimens, or tracking glycemic control.
tags:
  - management
  - primary-care
metadata:
  author: casemark
  practice_areas:
    - Family Medicine
    - Internal Medicine
    - Primary Care
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---

# Managing Diabetes Mellitus

Structures diabetes management with ADA standards including A1c targets, medication algorithms, and complication screening.

## Why This Skill Exists

Diabetes mellitus affects over 37 million Americans (11.3% of the population), with Type 2 accounting for 90-95% of cases. The American Diabetes Association (ADA) Standards of Care, updated annually, provide the evidence-based framework for glycemic management, but translating these guidelines into individualized care plans remains a persistent challenge. Uncontrolled diabetes drives microvascular complications (retinopathy, nephropathy, neuropathy) and macrovascular events (MI, stroke, PAD), making it the leading cause of blindness, kidney failure, and non-traumatic amputation in adults.

Primary care clinicians manage the majority of patients with Type 2 diabetes and are responsible for complication screening, medication titration, and coordination with endocrinology, ophthalmology, podiatry, and nutrition. This skill enforces the ADA Standards of Care workflow to ensure individualized A1c targets, evidence-based pharmacotherapy, and timely complication screening at every encounter.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. What is the diabetes type (Type 1, Type 2, gestational, other)? **Default: Type 2**
2. What is the most recent A1c and date obtained? **Default: [REQUIRED]**
3. What is the patient's current diabetes medication regimen with doses? **Default: [REQUIRED]**
4. Does the patient have established ASCVD, heart failure, or CKD? **Default: no**
5. What is the patient's current eGFR and UACR? **Default: pending**
6. When were the last retinal exam, foot exam, and dental exam? **Default: unknown**
7. Is the patient on a CGM or performing SMBG? What is the time-in-range (TIR)? **Default: SMBG**
8. Has the patient had any hypoglycemic events (glucose <54 mg/dL) in the past 3 months? **Default: none reported**

### Documents to Request

- A1c trend (at least 3 values over 12 months)
- CGM ambulatory glucose profile (AGP) or SMBG log (14 days minimum)
- Comprehensive metabolic panel including creatinine, eGFR, potassium
- Urine albumin-to-creatinine ratio (UACR)
- Lipid panel (fasting or non-fasting)
- Retinal exam report within past 12 months (or 24 months if prior exam normal)
- Podiatry or monofilament exam documentation
- Current medication list including insulin pen/vial details
- Nutrition counseling or DSMES (Diabetes Self-Management Education and Support) records

---

## Step 1: Individualized A1c Target Setting

Set the A1c target per ADA risk-benefit framework:

| Patient Profile | A1c Target | Rationale |
|---|---|---|
| Most non-pregnant adults | <7.0% | Reduces microvascular complications (DCCT/UKPDS) |
| Newly diagnosed, long life expectancy, no CVD | <6.5% | If achievable without significant hypoglycemia |
| History of severe hypoglycemia, limited life expectancy, extensive comorbidities | <8.0% | Avoid harm from overtreatment |
| Older adults, healthy | <7.0-7.5% | Per ADA geriatric guidelines |
| Older adults, complex/intermediate health | <8.0% | Focus on symptom management |
| Older adults, very complex/poor health | Avoid symptomatic hyperglycemia | A1c less reliable; focus on avoiding hypo/hyperglycemia |
| Pregnancy (pre-existing DM) | <6.5% if achievable without hypoglycemia | Tighter control for fetal outcomes |

Document the individualized target with explicit rationale for deviation from <7.0%.

---

## Step 2: Pharmacotherapy Algorithm (Type 2)

Apply ADA 2024 consensus algorithm:

**First-line**: Metformin 500mg twice daily, titrate to 1000mg twice daily over 4-8 weeks (hold if eGFR <30; reduce dose if eGFR 30-45)

**Second-line selection based on comorbidities**:

| Comorbidity | Preferred Add-On | Key Evidence |
|---|---|---|
| Established ASCVD | GLP-1 RA (semaglutide, liraglutide) or SGLT2i (empagliflozin, dapagliflozin) | SUSTAIN-6, LEADER, EMPA-REG |
| Heart failure (HFrEF or HFpEF) | SGLT2i (empagliflozin, dapagliflozin) | EMPEROR-Preserved/Reduced, DAPA-HF |
| CKD (eGFR 20-60 or UACR >200) | SGLT2i first; add finerenone for persistent albuminuria | CREDENCE, DAPA-CKD, FIDELIO-DKD |
| No ASCVD/HF/CKD, need A1c reduction | GLP-1 RA (highest efficacy: semaglutide >1.5% A1c reduction) | SUSTAIN trials |
| Cost is primary barrier | Sulfonylurea (glipizide, glimepiride) or TZD (pioglitazone) | Generic availability |
| Weight loss priority | GLP-1 RA or dual GIP/GLP-1 (tirzepatide) | SURMOUNT, STEP trials |

**Insulin initiation**: Start basal insulin (glargine, degludec) 10 units or 0.1-0.2 units/kg/day when A1c remains above target on ≥2 oral agents + GLP-1 RA, or if A1c >10% or symptomatic hyperglycemia at diagnosis.

---

## Step 3: Hypoglycemia Risk Management

- Classify: Level 1 (<70 mg/dL), Level 2 (<54 mg/dL), Level 3 (severe, requiring assistance)
- High-risk medications: insulin, sulfonylureas, meglitinides
- Mitigation: CGM for patients on MDI or with hypoglycemia unawareness; reduce sulfonylurea before adding insulin
- Rule of 15: treat Level 1 with 15g fast-acting carbohydrate, recheck in 15 minutes
- Prescribe glucagon (nasal or auto-injector) for all patients on insulin
- If CGM available, target Time-in-Range (70-180 mg/dL) >70% and Time-Below-Range (<54 mg/dL) <1%

---

## Step 4: Complication Screening Schedule

| Complication | Screening Test | Frequency | Action Threshold |
|---|---|---|---|
| Retinopathy | Dilated fundoscopic exam or validated retinal imaging | Annually (T2: at diagnosis; T1: within 5 years of diagnosis) | Refer ophthalmology if any retinopathy |
| Nephropathy | eGFR + UACR | Annually (more frequent if abnormal) | UACR ≥30 mg/g: start ACEi/ARB; refer nephrology if eGFR <30 |
| Neuropathy | 10g monofilament + 128Hz tuning fork or pinprick | Annually | Positive screen: foot care education, podiatry referral |
| Cardiovascular risk | Lipid panel, BP, ASCVD risk calculator | Annually | Statin per ASCVD risk; BP <130/80 |
| Foot exam | Visual inspection + pedal pulses + monofilament | Every visit for high-risk; annually for low-risk | Ulcer, deformity, PAD: urgent podiatry referral |
| Dental | Periodontal exam | Every 6 months | Periodontal disease exacerbates glycemic control |

---

## Step 5: Monitoring and Titration Protocol

| Metric | Target | Frequency | Action if Off-Target |
|---|---|---|---|
| A1c | Individualized (see Step 1) | Every 3 months if above target; every 6 months if at target | Intensify per algorithm |
| Fasting glucose | 80-130 mg/dL | Per SMBG schedule | Adjust basal insulin by 2 units every 3 days |
| Post-prandial glucose | <180 mg/dL | Per SMBG or CGM | Consider prandial insulin or GLP-1 RA |
| eGFR | Stable or declining <3 mL/min/year | Every 3-6 months if CKD | Adjust medications per eGFR thresholds |
| UACR | <30 mg/g or ≥30% reduction | Every 3-6 months if elevated | Maximize ACEi/ARB; add SGLT2i or finerenone |
| Weight | 5-10% loss for overweight patients | Every visit | Reinforce lifestyle; consider GLP-1 RA |
| BP | <130/80 mmHg | Every visit | Titrate per HTN skill |

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Is the A1c target individualized with documented rationale?
2. Does the medication selection address comorbidities (ASCVD, HF, CKD) per ADA algorithm?
3. Are all annual complication screenings scheduled or documented as completed?
4. Has hypoglycemia risk been assessed with mitigation plan for high-risk agents?
5. Is the follow-up interval appropriate for the current management phase?

---

## Quality Audit

- [ ] Diabetes type correctly classified and documented
- [ ] A1c target individualized with rationale recorded
- [ ] Metformin started or contraindication documented
- [ ] Comorbidity-driven agent selection documented (ASCVD → GLP-1 RA/SGLT2i; HF → SGLT2i; CKD → SGLT2i)
- [ ] Insulin initiation criteria met before starting insulin
- [ ] Hypoglycemia risk assessed; glucagon prescribed if on insulin
- [ ] Retinal exam current or scheduled
- [ ] UACR and eGFR checked within past 12 months
- [ ] Foot exam performed with monofilament testing documented
- [ ] Statin therapy addressed per ASCVD risk (moderate-intensity for age 40-75 with DM; high-intensity if ASCVD)
- [ ] Blood pressure target <130/80 documented with current readings
- [ ] DSMES referral offered or documented
- [ ] Smoking status assessed; cessation counseling if applicable
- [ ] Vaccination status reviewed (influenza, pneumococcal, Hepatitis B for age 19-59)

---

## Guidelines

- Never initiate SGLT2 inhibitors if eGFR <20 mL/min/1.73m²; may continue if already started and tolerated until dialysis
- Metformin should be held 48 hours before and after iodinated contrast procedures if eGFR <30
- A1c may be unreliable in patients with hemoglobinopathies, chronic kidney disease, recent transfusion, or iron deficiency anemia—use fructosamine or CGM metrics instead
- GLP-1 receptor agonists are contraindicated in patients with personal or family history of medullary thyroid carcinoma or MEN2 syndrome
- Insulin dose adjustments should not exceed 10-20% of total daily dose per week to avoid hypoglycemia
- SGLT2 inhibitors require sick-day rules education: hold during acute illness, dehydration, or perioperatively to prevent euglycemic DKA
- Sulfonylureas should be deprescribed when insulin is initiated to reduce hypoglycemia risk
- Document shared decision-making when treatment intensification is declined by the patient
