---
name: interpreting-routine-labs
language: en
description: Analyzes comprehensive metabolic panels, CBCs, lipid panels, and thyroid function with clinical correlation. Use when reviewing outpatient labs, identifying abnormalities, or correlating lab trends.
tags:
  - analysis
  - primary-care
  - clinical
  - patient-care
metadata:
  author: casemark
  practice_areas:
    - Family Medicine
    - Internal Medicine
    - Primary Care
  document_types:
    - Interpretation Report
  skill_modes:
    - Analysis
    - Interpretation
---

# Interpreting Routine Labs

Analyzes comprehensive metabolic panels, CBCs, lipid panels, and thyroid function with clinical correlation.

## Why This Skill Exists

Outpatient laboratory interpretation is a core primary care competency that directly drives clinical decisions: medication adjustments, specialist referrals, diagnosis of new conditions, and monitoring of chronic diseases. Approximately 70% of medical decisions are influenced by lab results, yet abnormal values frequently go un-actioned—studies show 7-8% of abnormal outpatient labs lack documented follow-up. Errors in interpretation range from misattributing hemolysis artifacts to clinical significance to missing subtle trends in renal function decline.

This skill provides a structured framework for interpreting the most commonly ordered outpatient panels (CMP, CBC, lipids, thyroid, A1c, urinalysis) with emphasis on clinical correlation, trend analysis, and appropriate next steps. It ensures that every abnormal value is either explained by a known diagnosis, flagged for workup, or documented as clinically insignificant with rationale.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. What labs are being reviewed (CMP, CBC, lipids, TSH, A1c, UA, other)? **Default: all available**
2. What is the clinical context (routine annual, disease monitoring, symptom workup)? **Default: routine annual**
3. Does the patient have known chronic conditions affecting labs (CKD, liver disease, anemia, thyroid disorder, diabetes)? **Default: per problem list**
4. What medications may affect lab values (metformin, ACEi, diuretics, statins, anticoagulants, thyroid replacement)? **Default: per med list**
5. Were specimen collection conditions appropriate (fasting state, correct tube, timely processing)? **Default: assume standard**
6. Are prior lab values available for trend comparison? **Default: pull last 3 results**

### Documents to Request

- Complete lab result panel with reference ranges from the performing laboratory
- Prior 2-3 sets of comparable labs for trend analysis
- Current medication list with doses and recent changes
- Active problem list and relevant diagnosis codes
- Recent imaging or procedures that may affect lab interpretation (e.g., contrast dye, surgery)
- Patient-reported symptoms relevant to lab abnormalities

---

## Step 1: Comprehensive Metabolic Panel (CMP) Interpretation

| Analyte | Reference Range | Common Causes of High | Common Causes of Low | Critical Action Threshold |
|---|---|---|---|---|
| Sodium | 136-145 mEq/L | Dehydration, diabetes insipidus, excess salt | SIADH, diuretics, heart failure, cirrhosis | <120 or >160: urgent evaluation |
| Potassium | 3.5-5.0 mEq/L | ACEi/ARB, CKD, hemolysis (artifact), spironolactone | Diuretics, vomiting, diarrhea, insulin | <3.0 or >6.0: ECG, urgent correction |
| Chloride | 98-106 mEq/L | Dehydration, renal tubular acidosis | Vomiting, diuretics, metabolic alkalosis | Interpret with sodium and bicarb |
| CO2 (bicarb) | 22-29 mEq/L | Metabolic alkalosis, vomiting, diuretics | Metabolic acidosis (DKA, lactic, CKD), diarrhea | <15: urgent evaluation for acidosis |
| BUN | 7-20 mg/dL | Dehydration, GI bleed, high protein diet, CKD | Liver disease, malnutrition, overhydration | Interpret BUN:Cr ratio |
| Creatinine | 0.7-1.3 mg/dL (M); 0.6-1.1 (F) | CKD, AKI, muscle mass, dehydration, medications | Low muscle mass, amputation, malnutrition | Rise >0.3 mg/dL from baseline: evaluate AKI |
| eGFR | >60 mL/min/1.73m² | N/A | CKD staging: G3a 45-59, G3b 30-44, G4 15-29, G5 <15 | <30: nephrology referral |
| Glucose (fasting) | 70-99 mg/dL | Diabetes, prediabetes, stress, steroids | Insulin excess, oral hypoglycemics, adrenal insufficiency | >400 or <50: immediate action |
| Calcium | 8.5-10.5 mg/dL | Hyperparathyroidism, malignancy, thiazides, vitamin D excess | Hypoalbuminemia (correct), CKD, hypoparathyroidism | Correct for albumin: add 0.8 per 1g albumin below 4.0 |
| Albumin | 3.5-5.0 g/dL | Dehydration | Liver disease, nephrotic syndrome, malnutrition, inflammation | <2.0: significant malnutrition or liver failure |
| Total bilirubin | 0.1-1.2 mg/dL | Hemolysis, Gilbert syndrome, hepatitis, obstruction | Rare; not clinically significant | >3.0: evaluate direct vs. indirect; imaging if direct elevated |
| ALP | 44-147 IU/L | Bone disease, biliary obstruction, pregnancy, growth in children | Rare; zinc deficiency, hypothyroidism | Fractionate with GGT to distinguish bone vs. liver |
| AST | 10-40 IU/L | Hepatitis, alcohol, medications, MI, muscle injury | Not clinically significant | >1000: acute hepatitis workup |
| ALT | 7-56 IU/L | Hepatitis, NAFLD/NASH, medications, alcohol | Not clinically significant | ALT >3x ULN on statin: hold statin, evaluate |

---

## Step 2: Complete Blood Count (CBC) Interpretation

| Parameter | Reference Range | Key Patterns |
|---|---|---|
| WBC | 4.5-11.0 × 10³/µL | Elevated: infection, stress, steroids, leukemia. Low: viral, medications, bone marrow suppression |
| Hemoglobin | 14-18 g/dL (M); 12-16 g/dL (F) | Anemia classification by MCV: microcytic (<80), normocytic (80-100), macrocytic (>100) |
| MCV | 80-100 fL | Low: iron deficiency, thalassemia. High: B12/folate deficiency, alcohol, hypothyroidism, MDS |
| RDW | 11.5-14.5% | Elevated: iron deficiency (early marker), mixed deficiency. Normal in thalassemia trait |
| Platelets | 150-400 × 10³/µL | High: reactive (infection, inflammation, iron deficiency), myeloproliferative. Low: ITP, medications, liver disease, DIC |

**Iron deficiency anemia workup** (MCV <80 + low ferritin):
- Ferritin <30 ng/mL: diagnostic. Ferritin 30-100: possible if inflammatory state (check CRP)
- Order: iron panel (iron, TIBC, ferritin), reticulocyte count
- If age >50 or no obvious source: colonoscopy to rule out GI malignancy

**Macrocytic anemia workup** (MCV >100):
- Order: B12, folate, reticulocyte count, peripheral smear
- If B12 <200 pg/mL: treat with B12 supplementation; check methylmalonic acid if borderline (200-400)
- Assess for alcohol use, hypothyroidism, medications (methotrexate, hydroxyurea, valproic acid)

---

## Step 3: Lipid Panel Interpretation

Apply ACC/AHA 2018 cholesterol guidelines:

| Component | Desirable | Borderline | High Risk |
|---|---|---|---|
| Total cholesterol | <200 mg/dL | 200-239 | ≥240 |
| LDL-C | <100 mg/dL (general); <70 (ASCVD) | 100-159 | ≥160; very high-risk ASCVD: <55 |
| HDL-C | ≥40 (M); ≥50 (F) | N/A | Low HDL is independent CV risk factor |
| Triglycerides | <150 mg/dL | 150-499 | ≥500: pancreatitis risk; initiate fibrate or omega-3 |
| Non-HDL-C | <130 mg/dL | 130-159 | ≥160 |

**Statin decision framework:**
1. Known ASCVD → High-intensity statin (atorvastatin 40-80mg or rosuvastatin 20-40mg)
2. LDL ≥190 → High-intensity statin without ASCVD risk calculation
3. Age 40-75, DM → Moderate-intensity statin; high-intensity if ASCVD risk ≥7.5%
4. Age 40-75, LDL 70-189, ASCVD risk ≥7.5% → Moderate-to-high intensity statin
5. Risk-enhancing factors (family history, hs-CRP >2, CAC >0): favor statin in borderline risk (5-7.5%)

---

## Step 4: Thyroid Function and A1c

**TSH interpretation:**
| TSH (mIU/L) | Free T4 | Interpretation | Action |
|---|---|---|---|
| 0.4-4.0 | Normal | Euthyroid | No action |
| >4.0, <10 | Normal | Subclinical hypothyroidism | Repeat in 6-12 weeks; treat if symptomatic, pregnant, or TSH >10 |
| >10 | Low | Overt hypothyroidism | Start levothyroxine 1.6 mcg/kg/day; lower in elderly/cardiac |
| <0.4 | Normal | Subclinical hyperthyroidism | Repeat in 6-12 weeks; refer endocrinology if persistent |
| <0.1 | High | Overt hyperthyroidism | Urgent endocrinology referral; check T3, TSI/TRAb |

**A1c interpretation:**
- <5.7%: Normal
- 5.7-6.4%: Prediabetes (confirm with fasting glucose or OGTT)
- ≥6.5%: Diabetes (confirm with repeat A1c or second diagnostic test)
- Unreliable if: hemoglobinopathy (HbS, HbC, HbE), recent transfusion, iron deficiency, CKD stage 4-5, pregnancy

---

## Step 5: Trend Analysis and Action Plan

For each abnormal value:
1. Compare to prior 2-3 values to determine if new, worsening, stable, or improving
2. Correlate with clinical context (symptoms, medications, known diagnoses)
3. Assign one of four dispositions:
   - **Expected**: abnormal value explained by known condition (e.g., elevated creatinine in CKD stage 3)
   - **Monitor**: mild abnormality requiring repeat testing (e.g., borderline TSH, mildly low vitamin D)
   - **Act**: abnormality requiring medication change, workup, or referral (e.g., new anemia, rising creatinine)
   - **Urgent**: critical value requiring same-day action (e.g., potassium >6.0, glucose >500, Hgb <7)

Document each disposition with rationale and timeline for follow-up.

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Has every abnormal value been addressed with a documented disposition?
2. Are trends identified for values that have changed from prior results?
3. Has medication influence on lab values been considered (e.g., ACEi → creatinine rise, statin → ALT)?
4. Are critical values flagged for urgent action?
5. Is the recommended follow-up timeline specific for each abnormality?

---

## Quality Audit

- [ ] All ordered panels reviewed with each abnormal value addressed
- [ ] Reference ranges from the performing laboratory used (not generic ranges)
- [ ] Trend analysis performed against ≥2 prior results where available
- [ ] Medication effects on lab values considered and documented
- [ ] Corrected calcium calculated when albumin is low
- [ ] eGFR calculated using CKD-EPI equation (race-neutral per 2021 update)
- [ ] Anemia classified by MCV with appropriate iron studies ordered if microcytic
- [ ] Lipid panel interpreted with ASCVD risk calculation and statin recommendation
- [ ] TSH abnormality has free T4 ordered or planned
- [ ] A1c interpreted with consideration for conditions affecting reliability
- [ ] Critical values identified with urgent action plan
- [ ] Patient notification plan documented (phone call, portal message, visit)
- [ ] Follow-up lab timing specified for each monitored abnormality

---

## Guidelines

- Never interpret a single lab value in isolation; always correlate with clinical presentation, medication list, and prior trends
- Hemolyzed specimens falsely elevate potassium, LDH, and AST—request recollection before acting on mildly elevated potassium from a hemolyzed sample
- The CKD-EPI 2021 equation is now race-neutral; do not use race-based eGFR adjustments
- Fasting is no longer required for lipid panels per 2018 ACC/AHA guidelines, but triglycerides >400 from non-fasting specimen should be confirmed fasting
- Isolated ALP elevation in an otherwise normal liver panel should prompt GGT testing to differentiate hepatic from bone source
- Low-normal B12 (200-400 pg/mL) may represent deficiency; check methylmalonic acid for confirmation in patients with macrocytosis or neuropathy
- Always document the specific lab values discussed with the patient, the clinical significance communicated, and the agreed-upon follow-up plan
- Flag any lab result that arrives after the patient has left the office for asynchronous follow-up within 72 hours per practice protocol
