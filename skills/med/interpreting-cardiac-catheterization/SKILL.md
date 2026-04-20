---
name: interpreting-cardiac-catheterization
language: en
description: Structures cath lab report interpretation with hemodynamics, angiographic findings, and intervention documentation. Use when reviewing cath reports, documenting PCI procedures, or interpreting hemodynamic data.
tags:
  - analysis
  - cardiology
metadata:
  author: casemark
  practice_areas:
    - Cardiology
    - Interventional Cardiology
    - Electrophysiology
  document_types:
    - Interpretation Report
  skill_modes:
    - Analysis
    - Interpretation
---

# Interpreting Cardiac Catheterization

Structures cath lab report interpretation with hemodynamics, angiographic findings, and intervention documentation.

## Why This Skill Exists

Cardiac catheterization remains the gold standard for coronary artery disease assessment and the definitive hemodynamic evaluation tool. Misinterpretation of coronary angiography — underestimating a left main lesion, failing to recognize FFR-significant stenosis, or missing anomalous coronary anatomy — can lead to inappropriate revascularization decisions or lethal delays. Similarly, hemodynamic data from right and left heart catheterization drives critical decisions in valvular disease, pulmonary hypertension, cardiomyopathy, and shock management.

The SCAI (Society for Cardiovascular Angiography and Interventions) and ACC mandate structured reporting of catheterization findings. This skill enforces systematic documentation of hemodynamics, coronary anatomy, lesion severity, intervention details, and complications.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. What was the indication for catheterization — ACS, stable angina, preoperative, valvular evaluation, hemodynamic assessment, or cardiomyopathy workup? (default: "Indication not specified")
2. Was this a diagnostic catheterization only, or was PCI performed? (default: "Diagnostic only")
3. Was right heart catheterization (RHC) performed in addition to left heart? (default: "LHC only")
4. What is the patient's baseline renal function (Cr, eGFR)? (default: "Not provided — flag contrast nephropathy risk")
5. Were any prior catheterizations performed? (default: "No prior cath available")
6. Are prior non-invasive stress test or imaging results available? (default: "Not provided")
7. What vascular access was used — radial, femoral, or other? (default: "Not specified")

### Documents to Request

- Full catheterization report with angiographic images
- Hemodynamic tracings (pressure waveforms)
- Prior catheterization reports for comparison
- Non-invasive testing results (stress echo, nuclear, CCTA)
- Echocardiogram (for valve correlation)
- Current medication list (antiplatelet, anticoagulant)
- Labs: BMP, CBC, coagulation studies, troponin trend if ACS

---

## Step 1: Hemodynamic Data Interpretation

**Normal Resting Hemodynamic Values:**

| Parameter | Normal Range |
|-----------|-------------|
| RA mean | 0–8 mmHg |
| RV systolic/diastolic | 15–30 / 0–8 mmHg |
| PA systolic/diastolic/mean | 15–30 / 4–12 / 9–18 mmHg |
| PCWP (mean) | 4–12 mmHg |
| LV systolic/EDP | 100–140 / 4–12 mmHg |
| Aortic systolic/diastolic/mean | 100–140 / 60–90 / 70–105 mmHg |
| Cardiac output (Fick) | 4.0–8.0 L/min |
| Cardiac index | 2.5–4.0 L/min/m² |
| SVR | 800–1200 dynes·s/cm⁵ |
| PVR | < 3 Wood units (< 240 dynes·s/cm⁵) |

**Key Hemodynamic Calculations:**
- Cardiac output (Fick) = VO₂ / (1.36 × Hgb × 10 × [SaO₂ − SvO₂])
- SVR = (MAP − RAP) × 80 / CO
- PVR = (mPAP − PCWP) × 80 / CO
- Valve area (Gorlin formula): AVA = CO / (44.3 × SEP × HR × √mean gradient)

**Hemodynamic Pattern Recognition:**

| Pattern | RA | PCWP | CO/CI | Diagnosis |
|---------|----|----- |-------|-----------|
| ↑ RA, ↑ PCWP, ↓ CO | High | High | Low | Cardiogenic shock |
| ↑ RA, normal PCWP, ↓ CO | High | Normal | Low | RV failure / PE / tamponade |
| Equalization of diastolic pressures | RA ≈ RVDP ≈ PADP ≈ PCWP | — | Low | Constrictive pericarditis or tamponade |
| ↑ PCWP with V waves | Normal-high | V wave > 2× mean PCWP | Variable | Severe mitral regurgitation |

---

## Step 2: Coronary Angiography Interpretation

**Standard Coronary Anatomy Reporting:**
- Left main (LM): length, caliber, disease
- Left anterior descending (LAD): proximal, mid, distal segments; diagonal branches (D1, D2)
- Left circumflex (LCx): proximal, distal; obtuse marginal branches (OM1, OM2)
- Right coronary artery (RCA): proximal, mid, distal; posterior descending (PDA), posterolateral (PLV)
- Dominance: right-dominant (85%), left-dominant (8%), co-dominant (7%)

**Lesion Severity Classification:**

| Severity | % Stenosis | Clinical Significance |
|----------|-----------|----------------------|
| Mild | 1–49% | Non-obstructive |
| Moderate | 50–69% | Borderline — consider FFR/iFR |
| Severe | 70–99% | Obstructive — revascularization candidate |
| Total occlusion | 100% | CTO — assess collateral supply |
| Left main | ≥ 50% | Significant by definition |

**Physiologic Assessment:**
- FFR (fractional flow reserve): ≤ 0.80 = hemodynamically significant
- iFR (instantaneous wave-free ratio): ≤ 0.89 = significant
- IVUS/OCT: used for plaque characterization, stent optimization, left main assessment

**Lesion Morphology (ACC/AHA Classification):**
- Type A: discrete (< 10 mm), concentric, non-calcified → high PCI success
- Type B1: tubular (10–20 mm), eccentric, moderate calcification → moderate risk
- Type B2: two or more Type B features → higher risk
- Type C: diffuse (> 20 mm), total occlusion, degenerated graft → highest risk

---

## Step 3: PCI Documentation (If Intervention Performed)

Document each intervention with:
1. Target vessel and segment
2. Lesion characteristics (length, calcification, bifurcation involvement)
3. Pre-intervention stenosis percentage
4. Guidewire and catheter used
5. Pre-dilation details (balloon size, pressure, result)
6. Stent deployed (DES type, dimensions, deployment pressure)
7. Post-dilation (if performed)
8. Final angiographic result (residual stenosis, TIMI flow grade)
9. Complications (dissection, perforation, no-reflow, side branch loss)

**TIMI Flow Grading:**
| Grade | Definition |
|-------|-----------|
| 0 | No perfusion — complete occlusion |
| 1 | Penetration without perfusion — contrast passes but fails to opacify the distal bed |
| 2 | Partial perfusion — distal bed opacifies but with delayed filling or clearance |
| 3 | Complete perfusion — normal filling and clearance |

---

## Step 4: Ventriculography and Additional Findings

**LV Function by Ventriculography:**
- Qualitative: normal, mild/moderate/severe hypokinesis, akinesis, dyskinesis
- LVEF estimation from RAO 30° projection
- Wall motion abnormalities mapped to coronary territories

**Additional Assessments:**
- Aortography: aortic regurgitation grading (1+ to 4+), aortic root dimensions
- Shunt assessment: step-up in O₂ saturation (Qp:Qs > 1.5 = significant L→R shunt)
- Transplant evaluation: right heart hemodynamics, PVR calculation, vasoreactivity testing

---

## Step 5: Post-Procedure Assessment and Complications

**Immediate Post-Cath Monitoring:**
- Access site: hematoma, retroperitoneal bleed, pseudoaneurysm, AV fistula
- Renal: contrast-induced nephropathy risk (hydrate; check Cr at 48–72 hours)
- Vascular: limb ischemia if femoral approach, radial artery occlusion
- Cardiac: post-PCI chest pain, stent thrombosis, coronary dissection

**Dual Antiplatelet Therapy (DAPT) Post-PCI:**
- After DES: aspirin + P2Y12 inhibitor (clopidogrel, ticagrelor, or prasugrel)
- ACS: minimum 12 months DAPT
- Stable CAD: minimum 6 months DAPT (3 months in high bleeding risk)
- Triple therapy (DOAC + DAPT) if concurrent AF: minimize duration; de-escalate to DOAC + single antiplatelet

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Are all hemodynamic values documented with normal references?
2. Is every coronary artery segment reported with dominance stated?
3. For PCI: is the lesion, device, and result fully documented with TIMI flow?
4. Are complications assessed and documented or their absence noted?
5. Is the post-procedure antiplatelet plan specified with duration?

---

## Quality Audit

- [ ] Indication for catheterization clearly stated
- [ ] Vascular access site and technique documented
- [ ] Complete hemodynamic data with normal reference ranges
- [ ] Coronary dominance identified
- [ ] All coronary arteries and major branches described
- [ ] Lesion severity quantified (%) for each stenosis
- [ ] FFR/iFR reported for intermediate lesions (50–70%)
- [ ] PCI details complete: lesion, equipment, stent specs, final result
- [ ] TIMI flow grade documented pre- and post-intervention
- [ ] LV function assessed (by ventriculography or prior echo)
- [ ] Complications listed or "no complications" explicitly stated
- [ ] Contrast volume documented (nephropathy risk)
- [ ] Post-procedure medication plan (DAPT) documented
- [ ] Comparison with prior catheterization if available

---

## Guidelines

1. Report coronary dominance in every catheterization interpretation — it affects the clinical significance of RCA vs. LCx lesions.
2. Intermediate stenoses (50–69%) should trigger documentation of whether physiologic assessment (FFR/iFR) was performed or planned.
3. For left main disease ≥ 50%, always document referral to Heart Team discussion for CABG vs. PCI per ACC/AHA guidelines.
4. Hemodynamic waveforms should be correlated with clinical context — giant V waves on PCWP tracing must be reported and correlated with MR severity on echo.
5. Contrast volume should be documented and kept below 3–4× eGFR to minimize nephropathy risk.
6. When CTO is identified, document the presence and grade of collateral supply (Rentrop classification).
7. Post-PCI DAPT duration must account for bleeding risk, ischemic risk, and concurrent anticoagulation needs — document the rationale for chosen duration.
