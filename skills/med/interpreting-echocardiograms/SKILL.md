---
name: interpreting-echocardiograms
description: Structures echocardiographic interpretation with chamber measurements, valve assessment, and functional parameters. Use when reading echo reports, documenting cardiac function, or evaluating valve disease.
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

# Interpreting Echocardiograms

Structures echocardiographic interpretation with chamber measurements, valve assessment, and functional parameters.

## Why This Skill Exists

Echocardiography is the most frequently ordered cardiac imaging study, with over 7 million performed annually in the US alone. Interpretation quality varies widely, and missed findings — an underestimated mitral regurgitation severity, an overlooked diastolic dysfunction pattern, or an unrecognized wall motion abnormality — directly alter surgical timing, device eligibility, and medical therapy decisions. The ASE (American Society of Echocardiography) guidelines mandate structured, quantitative reporting to reduce interpretive variability.

This skill enforces ASE-standard chamber quantification, valve assessment grading, and hemodynamic parameter documentation, ensuring every report is complete, reproducible, and actionable.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. What is the clinical indication for the echocardiogram? (default: "Evaluate cardiac structure and function")
2. What is the study type — transthoracic (TTE), transesophageal (TEE), stress echo, or contrast echo? (default: "TTE")
3. Is a prior echocardiogram available for comparison? (default: "No prior study available")
4. What is the patient's body surface area (BSA)? (default: "Not provided — will index to available BSA or flag")
5. Are there specific clinical questions — valve disease severity, LV function post-MI, pre-surgical evaluation, source of embolism? (default: "Comprehensive assessment")
6. Does the patient have a prosthetic valve, cardiac device, or prior cardiac surgery? (default: "None known")
7. What is the image quality — adequate, limited, or technically difficult? (default: "To be determined on review")

### Documents to Request

- Complete echocardiogram study (DICOM or structured report)
- Prior echocardiogram for comparison
- Patient height and weight for BSA calculation
- Recent ECG (for rhythm context during echo interpretation)
- Clinical referral note with specific question
- Relevant labs: BNP/NT-proBNP, troponin if applicable
- Cardiac catheterization data if available (for hemodynamic correlation)

---

## Step 1: LV Size and Systolic Function Assessment

**LV Chamber Quantification (ASE Reference Ranges):**

| Parameter | Normal Male | Normal Female | Mild | Moderate | Severe |
|-----------|------------|---------------|------|----------|--------|
| LVIDd (cm) | 4.2–5.8 | 3.8–5.2 | 5.9–6.3 / 5.3–5.6 | 6.4–6.8 / 5.7–6.1 | ≥ 6.9 / ≥ 6.2 |
| LVEF (%) | ≥ 52 | ≥ 54 | 41–51 / 41–53 | 30–40 | < 30 |
| LV mass index (g/m²) | ≤ 115 | ≤ 95 | 116–131 / 96–108 | 132–148 / 109–121 | ≥ 149 / ≥ 122 |

**LVEF Assessment Methods (in order of preference):**
1. Biplane Simpson's method of discs — standard for 2D
2. 3D volumetric assessment — most accurate when image quality permits
3. Visual estimation — acceptable for experienced readers, but quantitative method must be documented

**Wall Motion Analysis:**
- Score each of the 17 AHA segments: 1 = normal, 2 = hypokinetic, 3 = akinetic, 4 = dyskinetic, 5 = aneurysmal
- Wall motion score index (WMSI) = sum of scores / number of segments visualized
- WMSI > 1.0 indicates regional dysfunction; map to coronary territories

**Global Longitudinal Strain (GLS):**
- Normal: −18% to −22% (more negative = better function)
- Abnormal: > −16% (less negative)
- GLS can detect subclinical LV dysfunction before LVEF declines — critical for cardiotoxicity screening

---

## Step 2: Diastolic Function Assessment

**ASE/EACVI 2016 Diastolic Grading Algorithm:**

| Parameter | Normal | Grade I | Grade II | Grade III |
|-----------|--------|---------|----------|-----------|
| E/A ratio | 0.8–2.0 | < 0.8 | 0.8–2.0 | > 2.0 |
| E/e' (average) | < 10 | < 10 | 10–14 | > 14 |
| TR velocity (m/s) | < 2.8 | < 2.8 | > 2.8 | > 2.8 |
| LA volume index (mL/m²) | < 34 | < 34 | ≥ 34 | ≥ 34 |

**Key Rules:**
- If LVEF is normal: check average E/e', TR velocity, and LA volume index. If ≥ 2 of 3 are abnormal → diastolic dysfunction present; then grade using E/A ratio
- If E/A < 0.8 and E/e' < 10: Grade I (impaired relaxation)
- If E/A 0.8–2.0 with ≥ 2 abnormal parameters: Grade II (pseudonormal)
- If E/A > 2.0, deceleration time < 160 ms: Grade III (restrictive)

---

## Step 3: Valve Assessment

**Aortic Stenosis Severity (ACC/AHA 2020):**

| Parameter | Mild | Moderate | Severe |
|-----------|------|----------|--------|
| Peak velocity (m/s) | 2.0–2.9 | 3.0–3.9 | ≥ 4.0 |
| Mean gradient (mmHg) | < 20 | 20–39 | ≥ 40 |
| AVA (cm²) | > 1.5 | 1.0–1.5 | < 1.0 |
| AVAi (cm²/m²) | — | — | < 0.6 |

**Mitral Regurgitation Severity (ASE Integrated Approach):**

| Parameter | Mild | Moderate | Severe |
|-----------|------|----------|--------|
| Vena contracta (cm) | < 0.3 | 0.3–0.69 | ≥ 0.7 |
| EROA (cm²) | < 0.2 | 0.2–0.39 | ≥ 0.4 |
| Regurgitant volume (mL) | < 30 | 30–59 | ≥ 60 |
| Regurgitant fraction (%) | < 30 | 30–49 | ≥ 50 |

For each valve, document: morphology, leaflet mobility, calcification, stenosis severity, regurgitation severity, and mechanism of dysfunction.

---

## Step 4: Right Heart and Hemodynamic Assessment

**RV Assessment:**
- TAPSE (tricuspid annular plane systolic excursion): Normal ≥ 17 mm
- RV S' (tissue Doppler at tricuspid annulus): Normal ≥ 9.5 cm/s
- RV fractional area change: Normal ≥ 35%
- RV free-wall longitudinal strain: Normal < −20%

**Pulmonary Artery Pressure Estimation:**
- RVSP = 4 × (TR velocity)² + RAP
- RAP estimation by IVC: < 2.1 cm with > 50% collapse = 3 mmHg; > 2.1 cm with < 50% collapse = 15 mmHg

**Pericardial Assessment:**
- Effusion size: trivial (< 0.5 cm), small (0.5–1 cm), moderate (1–2 cm), large (> 2 cm)
- Tamponade physiology: RA diastolic collapse, RV diastolic collapse, respiratory variation > 25% mitral inflow

---

## Step 5: Structured Report Synthesis

Compile findings into a structured report following ASE reporting format:
1. Study indication and clinical context
2. LV size, wall thickness, systolic function (LVEF, GLS if obtained)
3. Regional wall motion abnormalities (if any, mapped to coronary territories)
4. Diastolic function grade with supporting parameters
5. Each valve: morphology, stenosis grade, regurgitation grade
6. RV size and function
7. PA pressure estimate
8. Pericardium
9. Aortic root dimensions
10. Comparison with prior study
11. Summary impression with clinical recommendations

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Is LVEF reported quantitatively with the method used?
2. Is diastolic function formally graded using the ASE 2016 algorithm?
3. Are all four valves assessed for both stenosis and regurgitation?
4. Is RV function quantified (not just "qualitatively normal")?
5. Does the summary impression directly address the clinical question?

---

## Quality Audit

- [ ] LV dimensions indexed to BSA where appropriate
- [ ] LVEF reported with method (Simpson biplane, 3D, visual)
- [ ] Wall motion assessed by 17-segment model or abnormalities listed by segment
- [ ] Diastolic function graded I–III with at least 3 supporting parameters
- [ ] All four valves assessed and severity graded
- [ ] Aortic stenosis evaluated with velocity, gradient, and valve area (discordance addressed if present)
- [ ] Mitral regurgitation assessed with at least two quantitative parameters
- [ ] RV size and function quantified (TAPSE minimum)
- [ ] PA pressure estimated or "TR insufficient for estimate" documented
- [ ] Pericardial space assessed
- [ ] Aortic root measured at sinuses of Valsalva
- [ ] Prior study comparison made or absence documented
- [ ] Image quality limitations acknowledged
- [ ] Clinical correlation and recommendations provided

---

## Guidelines

1. Always index chamber dimensions and volumes to BSA — absolute measurements alone are insufficient for clinical grading.
2. When aortic stenosis severity parameters are discordant (e.g., low gradient with small valve area), document the discrepancy and consider low-flow states, measurement error, or dobutamine stress echo.
3. For mitral regurgitation, never rely on a single parameter — use the ASE integrated approach with at least two quantitative measures.
4. GLS should be included when available, especially for oncology patients on cardiotoxic therapy (anthracyclines, trastuzumab) and pre-operative assessments.
5. Diastolic function cannot be reliably graded in atrial fibrillation using standard E/A ratios — use E/e' and LA volume index as primary parameters.
6. Always note whether contrast was used and whether it changed the LVEF assessment.
7. Report any incidental findings (pleural effusions, ascites, lung consolidation) visible on the echo study.
