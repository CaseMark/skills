---
name: managing-cardiac-imaging-protocols
description: Selects appropriate cardiac imaging modality based on clinical question and pretest probability. Use when choosing cardiac imaging, selecting stress testing modality, or ordering cardiac CT/MRI.
tags:
  - management
  - cardiology
  - clinical
metadata:
  author: casemark
  practice_areas:
    - Cardiology
    - Interventional Cardiology
    - Electrophysiology
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---

# Managing Cardiac Imaging Protocols

Selects appropriate cardiac imaging modality based on clinical question and pretest probability.

## Why This Skill Exists

Cardiac imaging is the highest-volume diagnostic category in cardiology, yet inappropriate utilization remains a persistent problem. The ACC Appropriate Use Criteria (AUC) define when specific imaging modalities add clinical value vs. when they provide no incremental benefit or unnecessary radiation exposure. Choosing the wrong modality — ordering a nuclear stress test when a treadmill ECG would suffice, or missing a CMR when viability assessment is needed — leads to wasted resources, patient harm from unnecessary radiation, and delayed diagnoses.

The 2021 ACC/AHA Chest Pain Guideline introduced a framework for selecting between exercise ECG, stress echo, SPECT, PET, CCTA, and CMR based on pretest probability, patient characteristics, and the specific clinical question. This skill ensures every imaging order is justified, appropriate, and targeted to the clinical decision it must inform.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. What is the clinical question driving the imaging request? (default: "Clinical question not stated")
2. What is the pretest probability of CAD — low (< 15%), intermediate (15–85%), or high (> 85%)? (default: "Pretest probability not calculated")
3. Can the patient exercise on a treadmill? (default: "Exercise capacity unknown")
4. Is the baseline ECG interpretable for ischemia (no LBBB, LVH with repolarization, WPW, paced rhythm, digoxin)? (default: "Baseline ECG interpretability not assessed")
5. What is the patient's BMI? (default: "BMI not documented — relevant for image quality")
6. What is the renal function (eGFR)? (default: "eGFR not documented — relevant for contrast agents")
7. Are there contraindications to specific modalities — claustrophobia, MRI-incompatible device, allergy to contrast or regadenoson? (default: "No known contraindications")
8. Has prior cardiac imaging been performed? (default: "No prior studies")

### Documents to Request

- Referral note with specific clinical question
- Recent ECG (for interpretability assessment)
- Prior cardiac imaging reports
- Medication list (beta-blockers for CT protocol, caffeine for vasodilator stress)
- Renal function (eGFR for contrast clearance)
- BMI/body habitus documentation
- Allergy history (iodinated contrast, gadolinium)
- Device information if applicable (MRI-conditional status)
- ACC AUC rating for the intended study (if available)

---

## Step 1: Clinical Question Classification

**Common Clinical Questions and Appropriate Modality:**

| Clinical Question | First-Line Modality | Alternative |
|-------------------|-------------------|------------|
| Stable chest pain, intermediate pretest probability, can exercise, interpretable ECG | Exercise ECG (treadmill) | CCTA |
| Stable chest pain, cannot exercise | Pharmacologic stress with imaging (SPECT, PET, echo, CMR) | CCTA |
| Stable chest pain, uninterpretable ECG | Stress imaging (stress echo, SPECT, PET) | CCTA |
| Acute chest pain, low-risk, troponin negative | CCTA (fast rule-out) | Stress testing |
| Known CAD — functional significance of lesion | Stress imaging (SPECT, PET, stress echo) | FFR at cath |
| New-onset HF — ischemic vs. non-ischemic | CMR (scar/viability) or CCTA (coronary anatomy) | Stress imaging |
| Viability assessment before revascularization | CMR (gold standard) or PET | Dobutamine echo |
| Pericardial disease evaluation | CMR | Echo, CT |
| Cardiac mass evaluation | CMR | CT, echo |
| Pre-TAVR/structural planning | Cardiac CT (gated) | TEE |
| Aortic disease (aneurysm, dissection) | CTA aorta | CMR, TEE |

---

## Step 2: Modality-Specific Protocols and Requirements

**Exercise ECG (Treadmill):**
- Requirements: able to exercise, interpretable baseline ECG, no LBBB/WPW/paced/LVH-repolarization/digoxin
- Protocol: Bruce or modified Bruce
- Strengths: low cost, functional capacity assessment, no radiation
- Limitations: lower sensitivity (68%) and specificity (77%) than imaging; cannot localize ischemia

**Stress Echocardiography:**
- Exercise or dobutamine stress
- Strengths: no radiation, valve assessment, diastolic function, portable
- Limitations: operator-dependent; limited acoustic windows in obese patients
- Exercise stress echo preferred when patient can exercise

**SPECT Myocardial Perfusion Imaging:**
- Pharmacologic (regadenoson, adenosine, dipyridamole) or exercise
- Radiation: 8–12 mSv (Tc-99m); higher with Tl-201
- Strengths: widely available, established prognostic data, quantitative perfusion analysis
- Limitations: attenuation artifacts (diaphragm in men, breast in women), radiation exposure
- Caffeine must be held 12–24 hours for vasodilator stress

**PET Myocardial Perfusion:**
- Pharmacologic stress (regadenoson)
- Radiation: 2–4 mSv (Rb-82)
- Strengths: higher sensitivity/specificity than SPECT, absolute myocardial blood flow quantification, lower radiation
- Detects balanced ischemia missed by SPECT
- Limitations: limited availability, requires on-site generator (Rb-82)

**Coronary CT Angiography (CCTA):**
- HR control: target < 65 bpm (metoprolol IV or oral)
- Sublingual nitroglycerin for coronary vasodilation
- Radiation: 1–5 mSv (with dose-reduction techniques)
- Strengths: high NPV (> 99%), anatomic detail, coronary calcium score
- Limitations: calcium blooming artifact, requires HR control, contrast exposure
- Renal: eGFR > 30 preferred; hydrate if borderline

**Cardiac MRI (CMR):**
- No radiation
- Strengths: gold standard for viability, myocardial tissue characterization (edema, fibrosis, infiltration, iron), RV assessment, pericardial disease
- Late gadolinium enhancement (LGE): detects scar pattern (ischemic vs. non-ischemic)
- T1/T2 mapping: detects diffuse fibrosis, edema, amyloid
- Limitations: long scan time (45–90 min), claustrophobia, MRI-incompatible devices, gadolinium contraindicated in eGFR < 30 (NSF risk)

---

## Step 3: ACC Appropriate Use Criteria Application

**AUC Rating Categories:**
- **Appropriate (A, score 7–9):** Test is generally acceptable and reasonable for the indication
- **May be Appropriate (M, score 4–6):** Test may be acceptable; clinical judgment required
- **Rarely Appropriate (R, score 1–3):** Test is not generally acceptable; unlikely to improve outcomes

**Common Rarely Appropriate Scenarios (avoid ordering):**
- Stress imaging in asymptomatic patients with low pretest probability
- Repeat stress imaging within 2 years without new symptoms or clinical change
- Routine preoperative stress testing for low-risk surgery in asymptomatic patients
- CCTA in patients with known significant CAD (prior PCI/CABG) without new symptoms
- Nuclear stress in patients who can exercise with interpretable ECG (exercise ECG is sufficient)

---

## Step 4: Radiation Safety and Contrast Considerations

**Radiation Dose Comparison:**

| Modality | Typical Effective Dose (mSv) |
|----------|---------------------------|
| Chest X-ray | 0.02 |
| Coronary calcium score | 1–3 |
| CCTA (modern) | 1–5 |
| SPECT (Tc-99m) | 8–12 |
| SPECT (Tl-201) | 15–20 |
| PET (Rb-82) | 2–4 |
| Cardiac cath (diagnostic) | 5–10 |
| CMR | 0 (no ionizing radiation) |

**ALARA Principle:** Use the lowest radiation modality that answers the clinical question. PET preferred over SPECT when available. CCTA with dose-reduction protocols preferred over older high-dose techniques.

**Contrast Agent Safety:**
- Iodinated contrast (CT): check eGFR; hydrate if eGFR 30–44; relative contraindication if eGFR < 30
- Gadolinium (MRI): avoid in eGFR < 30 due to NSF risk; Group II agents (gadobutrol, gadoterate) have lower risk
- Allergic reactions: premedicate with prednisone 50 mg at 13h, 7h, and 1h + diphenhydramine 50 mg at 1h before study

---

## Step 5: Reporting and Follow-Up

**Structured Report Requirements:**
1. Clinical indication and specific clinical question
2. AUC rating for the ordered study
3. Protocol used (stress agent, imaging technique, radiation dose)
4. Findings organized by clinical question
5. Comparison with prior imaging
6. Conclusion addressing the specific clinical question
7. Recommendations for next steps (if applicable)

**When Results Are Discordant with Clinical Suspicion:**
- Document the discordance explicitly
- Recommend alternative modality for confirmation
- Example: normal SPECT but high clinical suspicion → consider PET (detects balanced ischemia) or CCTA (anatomic assessment)

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Is the clinical question clearly stated and matched to the imaging modality?
2. Is the ACC AUC rating documented for the ordered study?
3. Are patient-specific factors (exercise capacity, ECG interpretability, BMI, renal function) addressed?
4. Is radiation exposure documented and ALARA principle applied?
5. Does the conclusion directly answer the clinical question?

---

## Quality Audit

- [ ] Clinical question explicitly stated before modality selection
- [ ] Pretest probability of CAD estimated
- [ ] Exercise capacity and baseline ECG interpretability assessed
- [ ] ACC AUC rating referenced for the selected study
- [ ] Modality matches clinical question and patient characteristics
- [ ] Contraindications to selected modality checked
- [ ] Medication instructions documented (beta-blocker for CT, caffeine hold for vasodilator)
- [ ] Contrast agent safety confirmed (eGFR, allergy history)
- [ ] Radiation dose documented and ALARA applied
- [ ] Findings structured and clinical question answered
- [ ] Comparison with prior imaging documented
- [ ] Discordant results addressed with alternative plan
- [ ] Rarely appropriate indications avoided or justified

---

## Guidelines

1. Always start with the clinical question — the modality follows from the question, not the reverse. Ordering a test without a specific clinical question is inappropriate.
2. Exercise ECG is sufficient for intermediate-risk patients who can exercise with an interpretable ECG — do not reflexively add imaging.
3. CCTA is the preferred first-line test for acute chest pain rule-out in low-to-intermediate risk patients in the ED (PROMISE, SCOT-HEART trials).
4. CMR is the gold standard for viability assessment — use before revascularization decisions in patients with ischemic cardiomyopathy and significant CAD.
5. PET is superior to SPECT for obese patients and for detecting balanced ischemia — prefer PET when available and clinically appropriate.
6. For pre-TAVR structural assessment, cardiac CT is mandatory — it provides annular sizing, access vessel evaluation, and coronary height assessment that echo cannot.
7. Routine stress testing in asymptomatic patients without risk factors is rarely appropriate — do not order for "peace of mind" without clinical justification.
8. When ordering pharmacologic stress with vasodilators, confirm caffeine hold (12–24 hours) and check for contraindications (second/third-degree AV block, active bronchospasm for adenosine/regadenoson).
