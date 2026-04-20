---
name: managing-chronic-kidney-disease
language: en
description: Tracks CKD staging with eGFR trends, nephrology referral criteria, and medication adjustments. Use when managing CKD, monitoring renal function, or adjusting renally-dosed medications.
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

# Managing Chronic Kidney Disease

Tracks CKD staging with eGFR trends, nephrology referral criteria, and medication adjustments.

## Why This Skill Exists

Chronic kidney disease (CKD) affects approximately 37 million U.S. adults (15% of the population), yet 90% are unaware of their diagnosis. CKD is the ninth leading cause of death and a potent multiplier of cardiovascular risk—a patient with CKD stage 3 is more likely to die of cardiovascular disease than to progress to dialysis. KDIGO (Kidney Disease: Improving Global Outcomes) 2024 guidelines provide the framework for staging, monitoring, and treatment, with transformative new evidence for SGLT2 inhibitors and finerenone.

Primary care clinicians manage the majority of CKD stages 1-3b and are responsible for early detection, cardiovascular risk reduction, medication dose adjustments, and timely nephrology referral. Common gaps include using outdated eGFR equations (race-based), missing albuminuria testing, delaying SGLT2 inhibitor initiation, and failing to adjust renally-cleared medications. This skill enforces KDIGO-based CKD management from screening through advanced disease coordination.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. What is the patient's most recent eGFR and date (CKD-EPI 2021 equation, race-neutral)? **Default: [REQUIRED]**
2. What is the most recent UACR (urine albumin-to-creatinine ratio)? **Default: [REQUIRED if not recently checked]**
3. Has CKD been confirmed (eGFR <60 or UACR ≥30 on ≥2 occasions ≥3 months apart)? **Default: confirm**
4. What is the CKD etiology (diabetes, hypertension, glomerulonephritis, PKD, other)? **Default: assess**
5. What medications require renal dose adjustment or are nephrotoxic? **Default: per med list**
6. Is the patient on an ACEi/ARB? An SGLT2 inhibitor? **Default: per med list**
7. What are the patient's most recent potassium, bicarbonate, calcium, phosphorus, PTH, and hemoglobin? **Default: pending**
8. Has the patient been referred to nephrology? **Default: assess if indicated**

### Documents to Request

- eGFR trend (minimum 3 values over 12 months for trajectory analysis)
- UACR trend (minimum 2 values to confirm persistence)
- Comprehensive metabolic panel with bicarbonate
- Phosphorus, intact PTH, 25-OH vitamin D
- CBC with hemoglobin trend
- Lipid panel
- Urinalysis with microscopy
- Renal ultrasound (if not previously obtained)
- Hepatitis B/C serology (if not previously tested)
- Current medication list annotated with renal clearance considerations

---

## Step 1: CKD Staging and Risk Classification

**KDIGO GFR Categories:**

| Stage | eGFR (mL/min/1.73m²) | Description |
|---|---|---|
| G1 | ≥90 | Normal or high (CKD only if albuminuria or structural abnormality present) |
| G2 | 60-89 | Mildly decreased (CKD only if albuminuria or structural abnormality present) |
| G3a | 45-59 | Mildly to moderately decreased |
| G3b | 30-44 | Moderately to severely decreased |
| G4 | 15-29 | Severely decreased |
| G5 | <15 | Kidney failure |

**KDIGO Albuminuria Categories:**

| Category | UACR (mg/g) | Description |
|---|---|---|
| A1 | <30 | Normal to mildly increased |
| A2 | 30-300 | Moderately increased (microalbuminuria) |
| A3 | >300 | Severely increased (macroalbuminuria) |

**Risk classification** uses the GxAx matrix to determine monitoring frequency and referral urgency. Higher GFR stage + higher albuminuria = higher risk of progression.

**CKD-EPI 2021 equation** (race-neutral): mandatory per NKF/ASN joint statement. Do NOT use race-based eGFR.

---

## Step 2: Slowing Progression — Core Interventions

| Intervention | Target | Evidence | Agent/Action |
|---|---|---|---|
| RAAS blockade | UACR ≥30 or HTN with CKD | IDNT, RENAAL, REIN trials | ACEi or ARB (not both); titrate to max tolerated dose |
| SGLT2 inhibitor | eGFR ≥20, UACR ≥200 (or any CKD with eGFR 20-45) | DAPA-CKD, EMPA-KIDNEY, CREDENCE | Dapagliflozin 10mg or empagliflozin 10mg daily; can initiate down to eGFR 20 |
| Finerenone | T2DM + CKD with UACR ≥30, on max ACEi/ARB | FIDELIO-DKD, FIGARO-DKD | Finerenone 10-20mg daily; monitor K+ closely |
| Blood pressure control | <120/80 (SPRINT) or <130/80 (KDIGO) | SPRINT CKD subgroup | ACEi/ARB preferred; add CCB or diuretic as needed |
| Glycemic control | A1c <7% (individualize for CKD stage) | UKPDS, ADVANCE | Metformin OK if eGFR ≥30; reduce dose if eGFR 30-45; SGLT2i if eGFR ≥20 |
| Sodium restriction | <2g/day | KDIGO recommendation | Dietary counseling; enhances RAAS blockade efficacy |
| Avoid nephrotoxins | Ongoing | Standard of care | NSAIDs, IV contrast (minimize), aminoglycosides, high-dose PPI |

**eGFR dip protocol for ACEi/ARB and SGLT2i:**
- Expected initial eGFR decline of 10-30% is hemodynamic and renoprotective; do NOT discontinue
- Recheck BMP in 2-4 weeks after initiation or dose change
- Discontinue if: eGFR drop >30% from baseline, potassium >5.5 (despite dietary modification), or symptomatic hypotension

---

## Step 3: CKD Complications Management

| Complication | Screening | Target | Treatment |
|---|---|---|---|
| Anemia | Hemoglobin (Hgb) q6-12mo if eGFR <45 | Hgb 10-11.5 g/dL | Iron supplementation first (ferritin <200 or TSAT <20%); ESA if iron-replete with Hgb <10 (nephrology co-management) |
| Metabolite bone disease (CKD-MBD) | Phosphorus, calcium, PTH, 25-OH D; start at G3a | Phosphorus 2.5-4.5; PTH trend rather than absolute value | Dietary phosphorus restriction; phosphate binders (calcium acetate, sevelamer); vitamin D supplementation; calcimimetic if secondary hyperparathyroidism uncontrolled |
| Metabolic acidosis | Serum bicarbonate q3-6mo if eGFR <45 | Bicarb ≥22 mEq/L | Sodium bicarbonate 650mg TID (or sodium citrate); may slow CKD progression |
| Hyperkalemia | Potassium at each visit; more frequently with ACEi/ARB/SGLT2i changes | K+ 3.5-5.0 mEq/L | Dietary K+ restriction; patiromer 8.4g daily or SZC 10g daily if persistent hyperkalemia limits RAAS blockade |
| Volume overload | Weight, edema assessment | Euvolemia | Loop diuretic (furosemide dose increases as eGFR declines); sodium restriction |
| Cardiovascular risk | Lipid panel, BP, ASCVD risk | LDL per ASCVD guidelines | Statin (atorvastatin preferred—not renally cleared); antiplatelet per ASCVD guidelines |

---

## Step 4: Medication Dose Adjustments

| Medication | eGFR ≥60 | eGFR 30-59 | eGFR 15-29 | eGFR <15 |
|---|---|---|---|---|
| Metformin | Full dose (2000mg/day) | Reduce max to 1000mg/day if eGFR 30-45; hold if <30 | Discontinue | Discontinue |
| Gabapentin | 300-1200mg TID | 200-700mg BID | 100-300mg daily | 100-300mg daily |
| Allopurinol | 100-800mg daily | Start 100mg; max 200mg if eGFR 30-60 | Max 100mg daily | Avoid |
| DOACs (apixaban) | 5mg BID | 5mg BID (2.5mg if 2 of 3: age ≥80, weight ≤60kg, Cr ≥1.5) | 2.5mg BID (limited data) | Not recommended |
| DOACs (rivaroxaban) | 20mg daily | 15mg daily if eGFR 15-50 | Avoid if <15 | Avoid |
| NSAIDs | Use with caution | AVOID (accelerates CKD, causes AKI) | AVOID | AVOID |
| Nitrofurantoin | Full dose | Avoid if eGFR <30 (ineffective) | Avoid | Avoid |
| Contrast dye | Standard with hydration | Pre/post hydration; hold metformin 48h | Minimize or avoid; nephrology input | Avoid unless dialysis available |

---

## Step 5: Monitoring Schedule and Nephrology Referral

**Monitoring frequency by KDIGO risk category:**

| CKD Stage | eGFR Check | UACR Check | BMP/K+ | Additional Labs |
|---|---|---|---|---|
| G1-G2, A1 | Annually | Annually | Annually | Per comorbidities |
| G3a, A1-A2 | Every 6-12 months | Every 6-12 months | Every 6 months | Phosphorus, PTH annually |
| G3b, A2-A3 | Every 3-6 months | Every 3-6 months | Every 3-6 months | CBC, phosphorus, PTH, bicarb q6mo |
| G4 | Every 3 months | Every 3 months | Every 1-3 months | Full panel q3mo; AV fistula discussion |
| G5 | Every 1-3 months | Every 1-3 months | Monthly-q3mo | Dialysis preparation |

**Nephrology referral criteria (refer when ANY of the following):**
- eGFR <30 mL/min/1.73m² (G4-G5)
- Rapid eGFR decline (>5 mL/min/year sustained)
- UACR >300 mg/g (A3 / nephrotic-range proteinuria)
- Persistent hematuria with proteinuria (glomerulonephritis evaluation)
- Refractory hypertension despite ≥4 agents
- Persistent hyperkalemia (>5.5) limiting RAAS blockade
- Unexplained anemia with eGFR <45
- CKD of unknown etiology
- Hereditary kidney disease (PKD, Alport syndrome)
- Recurrent nephrolithiasis with CKD progression
- eGFR <20: discuss dialysis modality and AV access planning

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Is CKD staged by both GFR category and albuminuria category (e.g., G3a-A2)?
2. Is the patient on an ACEi/ARB if UACR ≥30 or hypertensive?
3. Has an SGLT2 inhibitor been initiated or documented as not indicated?
4. Are all renally-cleared medications dose-adjusted for current eGFR?
5. Has nephrology referral been triggered if criteria met?

---

## Quality Audit

- [ ] CKD diagnosis confirmed with ≥2 eGFR or UACR values ≥3 months apart
- [ ] CKD staged by both GFR category (G1-G5) and albuminuria category (A1-A3)
- [ ] CKD-EPI 2021 race-neutral equation used for eGFR calculation
- [ ] eGFR trajectory plotted (at least 3 values over 12 months) to assess rate of decline
- [ ] UACR checked at least annually (more frequently if A2-A3)
- [ ] ACEi or ARB prescribed and titrated to max tolerated dose if UACR ≥30 or HTN
- [ ] SGLT2 inhibitor prescribed if eGFR ≥20 and UACR ≥200 (or other KDIGO indications)
- [ ] Finerenone considered for T2DM + CKD with persistent albuminuria on max ACEi/ARB
- [ ] Potassium and creatinine checked within 2-4 weeks of RAAS/SGLT2i initiation or dose change
- [ ] Nephrotoxic medications identified and discontinued or dose-adjusted (NSAIDs, aminoglycosides)
- [ ] CKD complications screened: anemia, acidosis, hyperkalemia, CKD-MBD
- [ ] Nephrology referral placed if eGFR <30, rapid decline, or refractory complications
- [ ] Vaccination status reviewed (Hepatitis B series if not immune; influenza, pneumococcal)
- [ ] Patient educated on CKD stage, prognosis, and self-management (sodium restriction, medication safety)

---

## Guidelines

- Never use race-based eGFR equations; the CKD-EPI 2021 race-neutral equation is the current standard per NKF/ASN joint statement
- ACEi and ARB should NOT be combined (dual RAAS blockade increases hyperkalemia and AKI without additional benefit per ONTARGET/VA NEPHRON-D)
- An initial eGFR dip of up to 30% after starting ACEi/ARB or SGLT2i is expected and hemodynamically mediated; this is NOT a reason to discontinue unless the decline is greater than 30% or accompanied by hyperkalemia
- SGLT2 inhibitors can be initiated at eGFR ≥20 mL/min/1.73m² and continued until dialysis per DAPA-CKD and EMPA-KIDNEY data; do NOT withhold based on older eGFR cutoffs
- NSAIDs are CONTRAINDICATED in CKD regardless of stage due to hemodynamic effects on GFR and direct nephrotoxicity; this includes OTC ibuprofen and naproxen
- Metformin is safe at eGFR ≥30 but should be reduced to 1000mg/day if eGFR 30-45 and discontinued below 30; the 2016 FDA safety update relaxed the prior eGFR <60 restriction
- Patients with CKD G4-G5 should have AV fistula discussion and nephrology co-management for dialysis planning ≥12 months before anticipated dialysis start
- Every CKD patient should be offered the complete Hepatitis B vaccine series if not already immune (anti-HBs titer); CKD patients have impaired vaccine response and may need higher doses
