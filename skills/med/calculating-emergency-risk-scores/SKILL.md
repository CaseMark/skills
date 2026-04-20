---
name: calculating-emergency-risk-scores
language: en
description: Computes validated risk scores (HEART, PERC, Wells, Ottawa, CURB-65) from clinical data. Use when calculating clinical decision scores, risk-stratifying ED patients, or applying clinical prediction rules.
tags:
  - analysis
  - emergency-medicine
  - risk
  - clinical
metadata:
  author: casemark
  practice_areas:
    - Emergency Medicine
  document_types:
    - Calculation Worksheet
  skill_modes:
    - Calculation
---

# Calculating Emergency Risk Scores

Computes validated clinical prediction rules (HEART, PERC, Wells, Ottawa, CURB-65) from clinical data to risk-stratify emergency department patients and guide disposition decisions.

## Why This Skill Exists

Clinical decision rules reduce diagnostic uncertainty, decrease unnecessary testing, and standardize care. The HEART score alone has been validated in over 30 studies involving >100,000 patients and can safely reduce cardiac testing by 20% in low-risk chest pain patients. Failure to apply validated scoring tools leads to both overutilization (unnecessary CT pulmonary angiograms, cardiac stress tests) and underutilization (missed pulmonary emboli, discharged ACS). Emergency physicians evaluate approximately 8-10 million chest pain visits annually in the US, and clinical prediction rules are the primary evidence-based mechanism for risk stratification.

CMS and major insurers increasingly reference clinical decision rules in coverage determinations and quality metrics. Applying these scores correctly — and documenting the calculation — supports both clinical quality and reimbursement compliance. Incorrect score calculation (data entry errors, misapplied criteria) undermines the entire purpose of the tool and can be worse than not using it at all.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. What is the clinical question to be answered? (Default: identify primary complaint driving score selection)
2. What are the patient's demographics (age, sex)? (Default: required for most scoring systems)
3. What are the current vital signs? (Default: full set required before scoring)
4. What laboratory values are available (troponin, D-dimer, lactate, BNP, creatinine)? (Default: collect before calculating dependent scores)
5. What is the patient's medical history relevant to the scoring system? (Default: query PMH, DVT/PE history, cancer history, prior cardiac history)
6. Is the patient pregnant? (Default: pregnancy modifies applicability of several scores)
7. What imaging results are available? (Default: collect CXR, ECG results before scoring)

### Documents to Request

- Complete vital signs with time stamps
- Laboratory results (troponin, D-dimer, BMP, CBC, coagulation studies, lactate)
- 12-lead ECG
- Chest X-ray report
- Prior cardiac testing results (stress test, catheterization)
- Problem list and medication list

---

## Step 1: HEART Score (Chest Pain / ACS Risk)

**Use for:** Adult chest pain patients being evaluated for acute coronary syndrome.

| Component | 0 Points | 1 Point | 2 Points |
|-----------|----------|---------|----------|
| **H**istory | Slightly suspicious | Moderately suspicious | Highly suspicious |
| **E**CG | Normal | Non-specific repolarization abnormality | Significant ST deviation |
| **A**ge | <45 | 45-64 | ≥65 |
| **R**isk factors | No known risk factors | 1-2 risk factors (HTN, DM, obesity, smoking, hyperlipidemia, family hx) | ≥3 risk factors OR history of atherosclerotic disease |
| **T**roponin | ≤ normal limit | 1-3× normal limit | >3× normal limit |

**Risk stratification:**

| Score | Risk | 6-Week MACE Rate | Recommended Action |
|-------|------|------------------|-------------------|
| 0-3 | Low | 0.9-1.7% | Discharge with PCP follow-up, no further cardiac testing |
| 4-6 | Moderate | 12-16.6% | Observation, serial troponins, consider stress test or CCTA |
| 7-10 | High | 50-65% | Admission, cardiology consult, invasive strategy likely |

**Documentation requirement:** Record each component value and total score. Example: "HEART score: H=1, E=0, A=2, R=1, T=0 = 4 (moderate risk)."

---

## Step 2: PERC Rule and Wells Score (Pulmonary Embolism)

### Pre-Test Probability: Wells Score for PE

| Criterion | Points |
|-----------|--------|
| Clinical signs/symptoms of DVT | 3.0 |
| PE is #1 diagnosis or equally likely | 3.0 |
| Heart rate >100 bpm | 1.5 |
| Immobilization ≥3 days or surgery within 4 weeks | 1.5 |
| Previous DVT/PE | 1.5 |
| Hemoptysis | 1.0 |
| Active cancer (treatment within 6 months or palliative) | 1.0 |

| Score | Risk Category | PE Prevalence | Next Step |
|-------|--------------|---------------|-----------|
| ≤4 | PE unlikely | ~8% | Apply PERC; if negative, stop. If PERC fails → D-dimer |
| >4 | PE likely | ~28% | Skip D-dimer → CTA pulmonary angiogram |

### PERC Rule (applies only if Wells ≤4)

All 8 criteria must be negative to rule out PE without D-dimer:

1. Age <50
2. Heart rate <100
3. SpO2 ≥95% on room air
4. No unilateral leg swelling
5. No hemoptysis
6. No surgery or trauma within 4 weeks
7. No prior DVT/PE
8. No estrogen use (OCP, HRT)

**If all 8 negative:** PE effectively excluded (miss rate <2%, below test threshold). No D-dimer or CTA needed.
**If any positive:** Obtain D-dimer. If D-dimer negative (age-adjusted: <age × 10 for patients >50) → PE excluded. If positive → CTA.

---

## Step 3: Ottawa Ankle and Knee Rules

### Ottawa Ankle Rules

**Obtain ankle X-ray only if:**
- Bone tenderness at posterior edge or tip of lateral malleolus (distal 6 cm), OR
- Bone tenderness at posterior edge or tip of medial malleolus (distal 6 cm), OR
- Inability to bear weight (4 steps) immediately and in ED

**Obtain foot X-ray only if:**
- Bone tenderness at base of 5th metatarsal, OR
- Bone tenderness at navicular bone, OR
- Inability to bear weight (4 steps) immediately and in ED

**Sensitivity:** 98-100% for clinically significant fractures. Specificity: 40-50%.
**Exclusions:** Age <18, intoxication, distracting injuries, diminished sensation, pregnant, isolated skin injury.

### Ottawa Knee Rule

**Obtain knee X-ray only if any of the following present:**
1. Age ≥55
2. Isolated tenderness of the patella (no other bony tenderness)
3. Tenderness at the fibular head
4. Inability to flex knee to 90°
5. Inability to bear weight (4 steps) immediately and in ED

**Sensitivity:** 98.5% for knee fractures.

---

## Step 4: CURB-65 (Pneumonia Severity)

| Criterion | Points |
|-----------|--------|
| **C**onfusion (new disorientation to person, place, or time) | 1 |
| **U**rea (BUN >19 mg/dL or >7 mmol/L) | 1 |
| **R**espiratory rate ≥30/min | 1 |
| **B**lood pressure (SBP <90 or DBP ≤60) | 1 |
| Age **65** or older | 1 |

| Score | 30-Day Mortality | Disposition |
|-------|-----------------|-------------|
| 0-1 | 1.5% | Outpatient treatment |
| 2 | 9.2% | Short inpatient or supervised outpatient |
| 3-5 | 22% | Inpatient; score ≥4 consider ICU |

**CRB-65 variant:** When BUN is unavailable (e.g., clinic setting), drop the U criterion. Score ≥2 suggests hospitalization.

---

## Step 5: Additional Commonly Used ED Risk Scores

### Canadian CT Head Rule (Minor Head Injury, GCS 13-15)

**High risk for neurosurgical intervention (any one = CT):**
1. GCS <15 at 2 hours post-injury
2. Suspected open or depressed skull fracture
3. Any sign of basal skull fracture (Battle's sign, raccoon eyes, CSF otorrhea/rhinorrhea, hemotympanum)
4. ≥2 episodes of vomiting
5. Age ≥65

**Medium risk for brain injury on CT (any one = CT):**
6. Amnesia before impact >30 minutes
7. Dangerous mechanism (pedestrian struck, ejection from vehicle, fall >3 feet or >5 stairs)

### NEXUS Criteria (C-Spine Clearance)

C-spine imaging NOT required if ALL five criteria met:
1. No posterior midline cervical tenderness
2. No focal neurologic deficit
3. Normal alertness (GCS 15)
4. No intoxication
5. No painful distracting injury

### San Francisco Syncope Rule (CHESS)

Admit or pursue workup if any present:
- **C**HF history
- **H**ematocrit <30%
- **E**CG abnormal (non-sinus rhythm or new changes)
- **S**hortness of breath
- **S**ystolic BP <90 mmHg

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Was the appropriate scoring tool selected for the clinical question being addressed?
2. Were all individual score components documented with their respective values?
3. Is the total score correctly calculated and the risk category accurately assigned?
4. Does the documented clinical plan align with the score's recommended disposition?
5. Were exclusion criteria checked (scores have populations where they are not validated)?

---

## Quality Audit

- [ ] Correct scoring tool selected for the clinical question
- [ ] All individual component values documented (not just the total score)
- [ ] Total score calculated correctly with arithmetic verified
- [ ] Risk category assigned matches the score range
- [ ] Exclusion criteria for the scoring tool checked and documented
- [ ] Clinical plan aligns with score-recommended disposition pathway
- [ ] Score version specified (e.g., HEART score, Wells PE criteria — original vs. simplified)
- [ ] Patient population validated for the tool (age, pregnancy, prior diagnosis exclusions)
- [ ] Troponin assay type documented for HEART score (conventional vs. high-sensitivity)
- [ ] D-dimer threshold specified (standard vs. age-adjusted) for PE pathway
- [ ] Score documented in the medical record MDM section
- [ ] Override of score-recommended pathway documented with explicit rationale
- [ ] Serial scoring documented if applicable (e.g., repeat HEART score with 3-hour troponin)

---

## Guidelines

1. Always document the specific version of each scoring tool used — Wells PE has original and simplified versions with different cutoffs; HEART score troponin criteria differ by assay type.
2. Clinical prediction rules are decision aids, not decision makers — they do not replace clinical judgment, and overriding a score recommendation is acceptable when documented with specific reasoning.
3. Never apply a scoring tool to a population for which it was not validated — the PERC rule is not validated in pregnant patients, Ottawa rules exclude intoxicated patients, and CURB-65 is for community-acquired pneumonia only.
4. Document each individual component, not just the total score — a HEART score of "4" is meaningless without the component breakdown for downstream providers.
5. Use age-adjusted D-dimer thresholds (age × 10 ng/mL for patients >50) — this is endorsed by ACEP and reduces unnecessary CTA by 12% without increasing missed PE.
6. When a score falls at a decision boundary (e.g., HEART 3 vs. 4), document the clinical reasoning for the disposition decision rather than relying solely on the number.
7. Serial scoring (e.g., HEART score at 0 and 3 hours) adds prognostic value — document both calculations with timestamps.
8. Communicate the score and its clinical meaning to the patient during shared decision-making: "Your risk of a major heart event in the next 6 weeks is approximately 1-2% based on your HEART score of 3."
