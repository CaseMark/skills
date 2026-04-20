---
name: managing-osteoporosis
language: en
description: Applies FRAX scoring with DXA interpretation and treatment algorithms for bone health. Use when assessing fracture risk, interpreting bone density, or selecting osteoporosis treatment.
tags:
  - management
  - primary-care
  - risk
  - treatment
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

# Managing Osteoporosis

Applies FRAX scoring with DXA interpretation and treatment algorithms for bone health.

## Why This Skill Exists

Osteoporosis affects approximately 10 million Americans, with an additional 44 million having low bone density (osteopenia). It causes over 2 million fractures annually, including 300,000 hip fractures with a 20-30% one-year mortality rate. Despite effective screening (DXA) and treatments that reduce fracture risk by 40-70%, osteoporosis remains severely underdiagnosed and undertreated—fewer than 25% of women who sustain a hip fracture receive osteoporosis treatment within 12 months.

The USPSTF recommends DXA screening for all women ≥65 and younger postmenopausal women with equivalent fracture risk (Grade B). The NOF/AACE/Endocrine Society guidelines provide treatment thresholds based on FRAX scoring and DXA T-scores. This skill structures the complete workflow from screening through treatment selection, monitoring, and drug holiday decisions to close the treatment gap.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. What is the patient's age, sex, menopausal status (if applicable)? **Default: [REQUIRED]**
2. Has a DXA scan been performed? T-scores at lumbar spine, femoral neck, and total hip? **Default: pending or schedule**
3. What is the patient's FRAX 10-year fracture probability (major osteoporotic and hip)? **Default: calculate**
4. Has the patient had a prior fragility fracture (vertebral, hip, wrist, humerus)? **Default: no**
5. Is the patient taking glucocorticoids (≥5mg prednisone equivalent daily for ≥3 months)? **Default: no**
6. What is the patient's calcium and vitamin D intake (diet + supplements)? **Default: unknown**
7. Is there a secondary cause of bone loss (hyperparathyroidism, celiac disease, hyperthyroidism, hypogonadism)? **Default: assess**
8. What osteoporosis treatment is the patient currently on (if any)? Duration? **Default: none**

### Documents to Request

- DXA scan report with T-scores at lumbar spine (L1-L4), femoral neck, and total hip
- FRAX calculation output (with or without BMD; specify country)
- Vertebral fracture assessment (VFA) or lateral thoracolumbar X-ray
- Labs: calcium (corrected), 25-OH vitamin D, phosphorus, alkaline phosphatase, PTH, BMP
- CBC, TSH, total testosterone (men), celiac panel (if suspected)
- 24-hour urine calcium (to assess absorption and renal calcium handling)
- Prior DXA scans for trend analysis
- Medication list including glucocorticoids, aromatase inhibitors, anticonvulsants, PPIs, SSRIs
- Fall risk assessment (Timed Up and Go, balance testing)

---

## Step 1: Screening and DXA Interpretation

**USPSTF screening recommendations:**
- Women ≥65: DXA screening (Grade B)
- Postmenopausal women <65: screen if FRAX 10-year major osteoporotic fracture risk ≥9.3% (equivalent to 65-year-old white woman)
- Men: USPSTF states insufficient evidence (Grade I) for routine screening; however, NOF recommends DXA for men ≥70 or men 50-69 with risk factors
- Repeat DXA: every 2 years while on treatment; sooner if new risk factor or treatment change

**DXA T-score classification (WHO):**

| T-score | Classification | Action |
|---|---|---|
| ≥ -1.0 | Normal | Reassess per risk factors; repeat DXA per guideline |
| -1.0 to -2.5 | Osteopenia (low bone mass) | Calculate FRAX; treat if meets treatment threshold |
| ≤ -2.5 | Osteoporosis | Initiate treatment |
| Any T-score + fragility fracture | Severe/established osteoporosis | Initiate treatment regardless of T-score |

**DXA interpretation pitfalls:**
- Degenerative changes at lumbar spine can falsely elevate T-score; use femoral neck if >2 level discordance
- T-scores are validated only for postmenopausal women and men ≥50; use Z-scores for premenopausal women and men <50
- Z-score ≤ -2.0 in younger patients: evaluate for secondary causes

---

## Step 2: FRAX Risk Assessment

Calculate 10-year fracture probability at https://frax.shef.ac.uk using:
- Age, sex, BMI, prior fracture, parental hip fracture, smoking, alcohol (≥3 units/day), glucocorticoids, rheumatoid arthritis, secondary osteoporosis, femoral neck BMD (optional)

**NOF treatment thresholds (for osteopenia with FRAX):**
- 10-year hip fracture probability ≥3% → treat
- 10-year major osteoporotic fracture probability ≥20% → treat

**FRAX limitations:**
- Does not account for fall risk, dose-response for glucocorticoids, or number of prior fractures
- Underestimates risk in patients with multiple vertebral fractures or very high glucocorticoid doses
- Trabecular Bone Score (TBS) can be applied as a FRAX adjustment in some calculators

---

## Step 3: First-Line Pharmacotherapy

| Agent | Class | Dosing | Fracture Reduction | Key Considerations |
|---|---|---|---|---|
| Alendronate (Fosamax) | Bisphosphonate | 70mg PO weekly | Spine 44%, hip 40% | Take fasting, upright 30 min, with water only; avoid if eGFR <30-35 |
| Risedronate (Actonel) | Bisphosphonate | 35mg PO weekly or 150mg monthly | Spine 41%, hip 30% | Same administration rules as alendronate |
| Zoledronic acid (Reclast) | IV bisphosphonate | 5mg IV annually | Spine 70%, hip 41% | For patients intolerant of oral; check calcium/vit D before infusion; adequate hydration |
| Denosumab (Prolia) | RANKL inhibitor | 60mg SQ every 6 months | Spine 68%, hip 40% | No renal dose adjustment; MUST NOT be delayed >7 months (rebound vertebral fractures) |
| Teriparatide (Forteo) | PTH(1-34) analog (anabolic) | 20mcg SQ daily | Spine 65%, nonvertebral 35% | Max 2 years; for severe osteoporosis or bisphosphonate failure; avoid if Paget's, bone cancer, or prior radiation |
| Abaloparatide (Tymlos) | PTHrP analog (anabolic) | 80mcg SQ daily | Spine 86%, nonvertebral 43% | Max 2 years; same precautions as teriparatide |
| Romosozumab (Evenity) | Sclerostin inhibitor (anabolic) | 210mg SQ monthly × 12 months | Spine 73%, hip 38% | Black box: increased CV risk; avoid if MI or stroke within 12 months |

**Treatment selection framework:**
- Mild-moderate osteoporosis, no recent fracture → oral bisphosphonate (first-line)
- Severe osteoporosis (T-score ≤ -3.0, multiple fractures) → anabolic agent first (teriparatide, abaloparatide, or romosozumab) followed by antiresorptive
- Bisphosphonate intolerance or contraindication → denosumab or IV zoledronic acid
- Glucocorticoid-induced osteoporosis → bisphosphonate; consider teriparatide for high risk (per ACR 2022)

---

## Step 4: Calcium, Vitamin D, and Lifestyle

| Nutrient | Daily Recommendation | Source |
|---|---|---|
| Calcium | 1000mg (men 51-70); 1200mg (women >50, men >70) | Dietary preferred; supplement if intake inadequate (calcium carbonate with food; calcium citrate without) |
| Vitamin D | 800-1000 IU daily; may need 2000-4000 IU to achieve 25-OH >30 ng/mL | Cholecalciferol (D3) preferred over D2 |

**Lifestyle interventions:**
- Weight-bearing and resistance exercise 3-5 days/week (reduces fall and fracture risk)
- Balance training (tai chi) for fall prevention in elderly
- Fall risk assessment: home safety evaluation, vision correction, medication review (sedatives, antihypertensives)
- Smoking cessation and alcohol moderation (<3 drinks/day)

---

## Step 5: Monitoring and Drug Holiday Decision

| Treatment Phase | Action | Timing |
|---|---|---|
| On bisphosphonate | Repeat DXA every 2 years; reassess at 3-5 years | DXA at 2 years; treatment review at 3 years (risedronate) or 5 years (alendronate) |
| Drug holiday consideration | After 5 years oral or 3 years IV bisphosphonate if: T-score > -2.5 at femoral neck AND no fractures on treatment | Holiday length 2-3 years; recheck DXA and FRAX; restart if bone loss or fracture |
| On denosumab | NEVER take a drug holiday; discontinuation causes rapid bone loss and rebound vertebral fractures | If stopping, must transition to bisphosphonate (zoledronic acid preferred) |
| Post-anabolic therapy | Transition to antiresorptive (bisphosphonate or denosumab) to maintain gains | Start within 1-2 months of completing anabolic course |
| Monitoring labs | 25-OH vitamin D, calcium annually; bone turnover markers (CTX, P1NP) if assessing treatment response | P1NP suppression confirms bisphosphonate adherence |

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Has the DXA been interpreted correctly with T-scores at all sites documented?
2. Is the FRAX calculation documented with treatment decision aligned to NOF thresholds?
3. Has a secondary cause workup been considered (labs ordered or documented as not indicated)?
4. Is the treatment selection appropriate for osteoporosis severity and patient risk profile?
5. Is the monitoring plan documented with DXA interval and drug holiday considerations?

---

## Quality Audit

- [ ] DXA screening performed per USPSTF recommendation (women ≥65 or younger with risk equivalent)
- [ ] T-scores reported at lumbar spine, femoral neck, and total hip
- [ ] WHO classification applied (normal, osteopenia, osteoporosis)
- [ ] FRAX calculated with treatment decision documented
- [ ] Secondary causes of bone loss evaluated (vitamin D, calcium, PTH, TSH minimum)
- [ ] Fragility fracture history documented (including morphometric vertebral fractures via VFA)
- [ ] First-line treatment selected with rationale documented
- [ ] Bisphosphonate administration instructions provided to patient
- [ ] Calcium and vitamin D intake assessed and supplementation prescribed if inadequate
- [ ] Fall risk assessment performed (Timed Up and Go or equivalent)
- [ ] Exercise prescription documented (weight-bearing + balance training)
- [ ] DXA follow-up interval scheduled (2 years on treatment; per risk if untreated)
- [ ] Drug holiday eligibility assessed after 3-5 years of bisphosphonate therapy
- [ ] Denosumab discontinuation risks documented if patient on Prolia
- [ ] Dental clearance recommended before initiating bisphosphonate or denosumab (ONJ risk)

---

## Guidelines

- Never initiate bisphosphonate therapy without first ensuring adequate vitamin D levels (25-OH ≥20 ng/mL, ideally ≥30 ng/mL) and calcium intake; hypocalcemia can result
- Denosumab must NEVER be stopped without transitioning to a bisphosphonate; rebound vertebral fractures occur within 12-18 months of the last dose, sometimes causing multiple simultaneous vertebral fractures
- Oral bisphosphonates must be taken on an empty stomach with 8oz plain water, remaining upright for 30 minutes to prevent esophageal erosion
- Bisphosphonates and denosumab carry a rare risk of osteonecrosis of the jaw (ONJ); dental evaluation before starting therapy is recommended, especially for denosumab
- Atypical femoral fractures are associated with long-term bisphosphonate use (>5-7 years); prodromal thigh pain should prompt X-ray evaluation
- Z-scores (not T-scores) should be used for premenopausal women and men under 50; the diagnosis of "osteoporosis" in these populations requires a Z-score ≤ -2.0 plus a secondary cause or fragility fracture
- Glucocorticoid-induced osteoporosis should be addressed proactively: start bisphosphonate if prednisone ≥2.5mg/day expected for ≥3 months per ACR guidelines
- Vertebral fracture assessment (VFA) or lateral spine X-ray should be obtained in women ≥70 and men ≥80 to detect asymptomatic compression fractures that change management
