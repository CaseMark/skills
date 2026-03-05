---
name: managing-nutrition-support
description: Assesses nutritional status and coordinates enteral/parenteral nutrition protocols. Use when evaluating nutritional needs, initiating feeding protocols, or managing TPN orders.
tags:
  - management
  - hospital-medicine
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

# Managing Nutrition Support

Assesses nutritional status and coordinates enteral/parenteral nutrition protocols for hospitalized patients.

## Why This Skill Exists

Malnutrition affects 30-50% of hospitalized patients and is independently associated with increased length of stay, higher complication rates, impaired wound healing, increased infection risk, and elevated mortality. Despite its prevalence, malnutrition is underdiagnosed and undertreated — only 7-8% of malnourished patients have a malnutrition diagnosis documented in their medical record, resulting in missed reimbursement (malnutrition is a CC/MCC that affects DRG assignment) and suboptimal care.

The Joint Commission requires nutritional screening within 24 hours of admission, and ASPEN (American Society for Parenteral and Enteral Nutrition) guidelines provide evidence-based frameworks for nutrition assessment and intervention. CMS recognizes malnutrition-related ICD-10 codes (E43, E44, E46) as comorbidities affecting case mix. Early nutrition support — initiated within 24-48 hours of admission — improves clinical outcomes, reduces ICU stays, and lowers 30-day readmission rates. Hospitalists must coordinate with dietitians, pharmacists, and nursing to ensure timely and appropriate nutrition delivery.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Before assessing or initiating nutrition support, confirm:

1. Has **nutritional screening** been completed — MUST (Malnutrition Universal Screening Tool) or NRS-2002 (Nutritional Risk Screening)? *(Default: Check admission nursing assessment)*
2. What is the patient's **current oral intake** status — NPO, clear liquids, regular diet, poor appetite? *(Default: Review diet order and nursing intake documentation)*
3. How many days has the patient been **NPO or with inadequate intake**? *(Default: Calculate from admission or last adequate intake)*
4. Does the patient have a **functioning GI tract**? *(Default: Assess bowel sounds, flatus, bowel movements, absence of obstruction/ileus)*
5. What is the patient's **weight trajectory** — stable, losing, unable to weigh? *(Default: Admission weight vs. baseline; daily weights if ordered)*
6. Does the patient have **conditions requiring specialized nutrition** — diabetes, renal failure, hepatic failure, pancreatitis, short bowel? *(Default: Review problem list)*
7. Is there a **dietitian consultation** in place? *(Default: Order if nutritional risk identified)*
8. Does the patient have **enteral access** — NG tube, PEG, PEJ, or need for one? *(Default: Assess if unable to eat by mouth)*

### Documents to Request

- Admission nutritional screening (MUST or NRS-2002) results
- Dietitian assessment (if completed)
- Pre-albumin, albumin, and total protein levels (note: albumin is an inflammatory marker, not a nutritional marker in acute illness)
- Daily weight log
- Calorie count records (if ordered)
- Intake and output records
- Medication list (assess impact on nutrition — appetite suppressants, GI motility agents)
- Swallow evaluation results (if dysphagia is a concern)

---

## Step 1: Nutritional Screening and Assessment

### MUST (Malnutrition Universal Screening Tool)

| Step | Parameter | Score |
|------|-----------|-------|
| 1 | **BMI** | > 20.0 = 0; 18.5-20.0 = 1; < 18.5 = 2 |
| 2 | **Unplanned weight loss** (3-6 months) | < 5% = 0; 5-10% = 1; > 10% = 2 |
| 3 | **Acute disease effect** (NPO or likely to be NPO > 5 days) | No = 0; Yes = 2 |

**Total score:**
| Score | Risk | Action |
|-------|------|--------|
| 0 | Low | Repeat screening weekly (inpatient) or monthly (outpatient) |
| 1 | Medium | Document dietary intake for 3 days; if adequate, repeat screen; if inadequate, treat as high risk |
| ≥ 2 | High | Dietitian referral, nutrition intervention, set goals and monitoring plan |

### ASPEN Malnutrition Criteria (for formal diagnosis)

Diagnose malnutrition when ≥ 2 of the following are present:
- Insufficient energy intake
- Weight loss (> 5% in 1 month, > 7.5% in 3 months, > 10% in 6 months)
- Loss of muscle mass (temporal wasting, interosseous wasting)
- Loss of subcutaneous fat (orbital, triceps)
- Localized or generalized fluid accumulation (may mask weight loss)
- Diminished functional status (handgrip strength)

**Classification**: Acute illness-related (severe) vs. chronic disease-related vs. social/environmental

---

## Step 2: Calculate Nutritional Requirements

**Caloric needs estimation:**

| Method | Calculation | Use Case |
|--------|-------------|----------|
| **Simple estimate** | 25-30 kcal/kg/day (use IBW for obese patients, ABW for normal weight) | General medical patients |
| **Critical illness (early)** | 15-20 kcal/kg/day (trophic feeding) | ICU days 1-4 |
| **Critical illness (later)** | 25-30 kcal/kg/day | ICU day 5+ |
| **Obesity (BMI > 30)** | 11-14 kcal/kg ABW/day OR 22-25 kcal/kg IBW/day | Obese patients to prevent overfeeding |
| **Renal failure (non-dialysis)** | 25-30 kcal/kg/day; protein 0.6-0.8 g/kg/day | CKD stages 3-5 without dialysis |
| **Renal failure (dialysis)** | 25-35 kcal/kg/day; protein 1.2-1.5 g/kg/day | Hemodialysis or peritoneal dialysis |
| **Hepatic failure** | 25-35 kcal/kg/day; protein 1.0-1.5 g/kg/day (do NOT restrict protein unless grade 3-4 HE unresponsive to lactulose) | Cirrhosis |

**Protein needs:**
- General medical: 1.2-1.5 g/kg/day
- Wound healing: 1.5-2.0 g/kg/day
- Critical illness: 1.2-2.0 g/kg/day
- Burns: 1.5-2.5 g/kg/day (based on burn severity)

---

## Step 3: Select the Nutrition Delivery Route

Follow the decision hierarchy: **Oral > Enteral > Parenteral**

```
Can the patient eat by mouth?
├── YES → Optimize oral intake (diet orders, supplements, snacks, 
│         appetite stimulants if indicated)
│         Target: ≥ 60% of estimated needs by mouth
└── NO (NPO, aspiration risk, obtunded, intubated)
    └── Is the GI tract functional?
        ├── YES → Enteral nutrition (tube feeds)
        │         Route: NG/OG (short-term < 4 weeks) 
        │                PEG/PEJ (long-term > 4 weeks)
        │         Start within 24-48 hours of admission if intake 
        │         inadequate
        └── NO (ileus, obstruction, severe pancreatitis, 
                short bowel, high-output fistula)
            └── Parenteral nutrition (TPN)
                Start if enteral not feasible and patient will be NPO 
                > 7 days (or > 3-5 days if already malnourished)
```

---

## Step 4: Enteral Nutrition Management

**Initiating tube feeds:**
- Select formula based on clinical needs (standard, high-protein, renal, hepatic, diabetic, semi-elemental)
- Start rate: 10-20 mL/hr
- Advance by 10-20 mL/hr every 4-8 hours as tolerated
- Goal rate: Calculated to meet caloric and protein targets
- Check gastric residual volumes (GRV) per institutional protocol — hold feeds if GRV > 500 mL (ASPEN 2016 guideline no longer recommends routine GRV checks in ICU, but institutional practices vary)

**Monitoring:**
- Daily: Weight, I&Os, tolerance (nausea, vomiting, abdominal distension, diarrhea)
- Every 48-72h: BMP (electrolytes, glucose, renal function)
- Weekly: Prealbumin (half-life 2 days — more responsive to acute changes than albumin), phosphorus, magnesium

**Common complications and management:**
| Complication | Intervention |
|-------------|--------------|
| Diarrhea | Rule out C. diff; consider fiber-containing formula; review medications (sorbitol in liquid meds, magnesium) |
| High GRV | Elevate HOB 30-45°; consider prokinetic (metoclopramide); post-pyloric tube placement |
| Tube clogging | Flush with warm water; do not crush extended-release medications |
| Aspiration risk | HOB elevation 30-45°; post-pyloric feeding; continuous (not bolus) for high-risk patients |
| Hyperglycemia | Insulin protocol; consider diabetic formula (e.g., Glucerna) |

---

## Step 5: Parenteral Nutrition (TPN) Management

**Initiation criteria:**
- GI tract non-functional or inaccessible
- Expected NPO duration > 7 days (or > 3-5 days if malnourished)
- Failure of enteral nutrition trial

**TPN composition:**
| Component | Standard Range | Monitoring |
|-----------|---------------|------------|
| Dextrose | 150-250 g/day (start low: 150-200 g/day) | Glucose Q6h initially; BMP daily |
| Amino acids | 1.0-1.5 g/kg/day | BUN, prealbumin weekly |
| Lipids | 0.5-1.0 g/kg/day (do not exceed 2.5 g/kg/day) | Triglycerides weekly (hold if > 400 mg/dL) |
| Electrolytes | Per BMP and clinical needs | BMP daily until stable, then 2-3x/week |
| Vitamins/trace elements | Standard multivitamin, trace elements | Zinc, copper, selenium if prolonged TPN |

**Refeeding syndrome prevention:**
- High risk: BMI < 16, > 10% weight loss in 3-6 months, NPO > 10 days, baseline low phosphorus/potassium/magnesium
- Start at 50% of estimated caloric needs for first 2-3 days
- Supplement: Thiamine 200-300 mg IV daily for first 3 days BEFORE starting feeds
- Monitor phosphorus, potassium, and magnesium Q12h for first 72 hours
- Replete aggressively: Phosphorus < 2.0, K < 3.5, Mg < 1.5

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

For each patient on nutrition support:

1. Has **nutritional screening** been completed and documented?
2. Is the **nutrition delivery route** appropriate — oral optimized before tube feeds, enteral before TPN?
3. Are **caloric and protein targets** calculated and documented?
4. Is **refeeding syndrome risk** assessed with prophylactic measures in place?
5. Is there a **monitoring plan** for labs, tolerance, and weight?

---

## Quality Audit

- [ ] Nutritional screening (MUST or NRS-2002) completed within 24 hours of admission
- [ ] Dietitian consultation ordered for patients at nutritional risk
- [ ] Malnutrition diagnosis documented with ICD-10 code when criteria met
- [ ] Caloric and protein targets calculated and documented
- [ ] Oral intake optimized before advancing to enteral or parenteral nutrition
- [ ] Enteral nutrition initiated within 24-48 hours when oral intake inadequate
- [ ] TPN indicated only when enteral route is not feasible
- [ ] Refeeding syndrome risk assessed for malnourished patients
- [ ] Thiamine supplemented before refeeding in high-risk patients
- [ ] Electrolytes monitored per protocol (daily during initiation, 2-3x/week when stable)
- [ ] Tube feed tolerance assessed daily (GRV, bowel function, abdominal exam)
- [ ] Glycemic management addressed for patients on enteral or parenteral nutrition
- [ ] Nutrition plan reassessed at least weekly by dietitian

---

## Guidelines

- "If the gut works, use it" — enteral nutrition is always preferred over parenteral for safety, cost, and physiologic benefit
- Do not wait until a patient is severely malnourished to initiate nutrition support — start early (within 24-48 hours) when oral intake is inadequate
- Albumin is NOT a nutritional marker in acute illness — it is a negative acute-phase reactant that drops with inflammation; use prealbumin or clinical assessment instead
- Protein restriction in hepatic encephalopathy is outdated — current ASPEN/ESPEN guidelines recommend 1.0-1.5 g/kg/day for cirrhotic patients
- Document malnutrition when criteria are met — it affects DRG coding and reimbursement and is one of the most under-coded diagnoses in hospital medicine
- Refeeding syndrome kills — always assess risk and start low-and-slow with thiamine preloading for at-risk patients
- When patients are on TPN, transition to enteral as soon as GI function returns — do not maintain TPN "just in case"
- Involve the dietitian as a core member of the care team, not an afterthought — they should participate in multidisciplinary rounds
