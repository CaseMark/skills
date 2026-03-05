---
name: interpreting-electrocardiograms
description: Systematically interprets 12-lead ECGs with rate, rhythm, axis, intervals, and morphology analysis. Use when reading ECGs, documenting EKG interpretations, or identifying cardiac arrhythmias.
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

# Interpreting Electrocardiograms

Systematically interprets 12-lead ECGs with rate, rhythm, axis, intervals, and morphology analysis.

## Why This Skill Exists

Missed or misinterpreted ECG findings remain one of the leading sources of diagnostic error in emergency and ambulatory cardiology. A delayed STEMI call, an overlooked Brugada pattern, or a missed high-degree AV block can result in preventable death or permanent disability. The ACC/AHA and ESC mandate structured, systematic ECG interpretation to reduce cognitive bias and ensure no finding is overlooked.

Accurate ECG interpretation underpins virtually every downstream cardiology decision — from cath lab activation to antiarrhythmic selection. This skill enforces the disciplined, stepwise approach taught in electrophysiology fellowships: rate, rhythm, axis, intervals, morphology, and clinical correlation, in that order, every time.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. What is the clinical context for this ECG? (default: "Routine screening — no acute symptoms reported")
2. Is a prior ECG available for comparison? (default: "No prior ECG available")
3. What is the patient's age and sex? (default: "Adult, sex not specified")
4. Is the patient currently on any rate- or rhythm-altering medications (beta-blockers, calcium channel blockers, antiarrhythmics, digoxin)? (default: "Medication list not provided")
5. Are there electrolyte abnormalities suspected or confirmed (K+, Ca2+, Mg2+)? (default: "Unknown")
6. What is the clinical question — arrhythmia evaluation, ischemia workup, preoperative clearance, or syncope evaluation? (default: "General interpretation requested")
7. Was the ECG obtained during symptoms? (default: "Timing relative to symptoms unknown")
8. Are there any known conduction abnormalities, pacemaker, or prior cardiac surgery? (default: "None known")

### Documents to Request

- The 12-lead ECG tracing (PDF or image at minimum 300 dpi)
- Prior ECGs for serial comparison (at least one, ideally the most recent)
- Current medication list with dosages
- Most recent basic metabolic panel (BMP) with potassium, calcium, magnesium
- Clinical note or reason for referral
- Echocardiogram report if available (for structural correlation)
- Device interrogation report if pacemaker/ICD present

---

## Step 1: Technical Quality and Calibration Assessment

Before interpreting any waveform, confirm the tracing is technically adequate.

**Calibration Check:**
- Standard calibration: 25 mm/s paper speed, 10 mm/mV gain
- Confirm calibration box is present and measures 10 mm tall × 5 mm wide
- If non-standard calibration is used, annotate all measurements accordingly

**Artifact Assessment:**
- Baseline wander — respiratory, movement, or electrode contact issue
- 60 Hz interference — electrical noise from nearby equipment
- Muscle tremor artifact — especially in limb leads
- Lead reversal — suspect if lead I is inverted or aVR shows upright P and QRS

**Lead Placement Verification:**
- Normal P-wave axis should be upright in leads I, II, aVF and inverted in aVR
- If P waves are inverted in lead I with upright P in aVR, suspect LA/RA reversal
- Precordial R-wave progression should increase from V1 to V5

---

## Step 2: Rate and Rhythm Determination

**Heart Rate Calculation:**
| Method | Technique | Best For |
|--------|-----------|----------|
| 300 method | 300 ÷ (large boxes between R-R) | Regular rhythms |
| 1500 method | 1500 ÷ (small boxes between R-R) | Precise regular rhythm |
| 6-second strip | Count QRS complexes in 30 large boxes × 10 | Irregular rhythms |
| R-R interval | 60 ÷ R-R interval in seconds | Any rhythm |

**Rhythm Assessment Checklist:**
1. Is there a P wave before every QRS? Is there a QRS after every P?
2. Are the P waves uniform in morphology?
3. Is the P-P interval regular? Is the R-R interval regular?
4. What is the P:QRS ratio?
5. Is the rhythm narrow complex (< 120 ms) or wide complex (≥ 120 ms)?

**Sinus Rhythm Criteria:** Upright P in I, II, aVF; inverted in aVR; rate 60–100 bpm; constant PR interval 120–200 ms; P:QRS ratio 1:1.

---

## Step 3: Axis, Intervals, and Conduction

**QRS Axis Determination:**
| Axis Category | Lead I | aVF | Degrees |
|---------------|--------|-----|---------|
| Normal axis | + | + | −30° to +90° |
| Left axis deviation | + | − | −30° to −90° |
| Right axis deviation | − | + | +90° to +180° |
| Extreme axis | − | − | −90° to −180° |

**Interval Reference Ranges:**
| Interval | Normal Range | Clinical Significance of Prolongation |
|----------|-------------|--------------------------------------|
| PR | 120–200 ms | First-degree AV block (> 200 ms); short PR (< 120 ms) suggests pre-excitation |
| QRS | < 120 ms | 120–149 ms: incomplete BBB; ≥ 150 ms: complete BBB or ventricular rhythm |
| QTc | ♂ < 450 ms; ♀ < 460 ms | > 500 ms: high risk torsades de pointes |

**QTc Correction Formulas:**
- Bazett: QTc = QT / √RR (most common; less accurate at extremes of HR)
- Fridericia: QTc = QT / ∛RR (preferred when HR < 60 or > 100)

**Bundle Branch Block Criteria:**
- RBBB: rsR' in V1–V2, wide S in I and V6, QRS ≥ 120 ms
- LBBB: Broad notched R in I, aVL, V5–V6; absent Q in I; QRS ≥ 120 ms
- LBBB invalidates ST-segment analysis for ischemia — apply Sgarbossa criteria

---

## Step 4: ST-Segment and T-Wave Morphology

**STEMI Recognition (ACC/AHA criteria):**
- ≥ 1 mm ST elevation in ≥ 2 contiguous limb leads
- ≥ 2 mm ST elevation in ≥ 2 contiguous precordial leads (≥ 2.5 mm in men < 40)
- ≥ 0.5 mm ST elevation in V7–V9 for posterior MI
- New LBBB with Sgarbossa criteria (concordant STE ≥ 1 mm in any lead = 5 points; concordant STD ≥ 1 mm in V1–V3 = 3 points; discordant STE ≥ 5 mm = 2 points; score ≥ 3 = STEMI equivalent)

**Coronary Territory Mapping:**
| Leads | Territory | Artery |
|-------|-----------|--------|
| V1–V4 | Anterior/septal | LAD |
| I, aVL, V5–V6 | Lateral | LCx |
| II, III, aVF | Inferior | RCA (85%) or LCx (15%) |
| V7–V9 | Posterior | RCA or LCx |
| V3R–V4R | Right ventricle | Proximal RCA |

**T-Wave Abnormalities:**
- Hyperacute T waves: tall, peaked, symmetric — earliest sign of acute MI
- Wellens syndrome: deep symmetric T-wave inversions V2–V3 (Type A) or biphasic T waves V2–V3 (Type B) — critical LAD stenosis
- De Winter T waves: upsloping ST depression > 1 mm with tall symmetric T waves in precordial leads — LAD occlusion equivalent

---

## Step 5: Pattern Recognition for Life-Threatening Findings

**Immediate-Action Patterns:**
- Ventricular fibrillation or polymorphic VT — emergency defibrillation
- Complete heart block with wide escape — pacing readiness
- Massive PE pattern: S1Q3T3, right axis, anterior T-wave inversions, sinus tachycardia
- Brugada Type 1: Coved ST elevation ≥ 2 mm in V1–V2 with T-wave inversion
- Hyperkalemia progression: Peaked T → PR prolongation → P-wave loss → widened QRS → sine wave

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Was every step of the systematic approach completed (rate, rhythm, axis, intervals, ST/T, patterns)?
2. Were all intervals measured and compared to reference ranges?
3. Were STEMI criteria explicitly evaluated and documented, even if negative?
4. Were prior ECGs compared, and new vs. old findings clearly distinguished?
5. Does the clinical correlation match the referring question?

---

## Quality Audit

- [ ] Calibration and paper speed confirmed and documented
- [ ] Heart rate calculated using appropriate method for rhythm regularity
- [ ] Rhythm classified with P-wave analysis and P:QRS relationship
- [ ] QRS axis category stated with supporting lead data
- [ ] PR, QRS, and QTc intervals measured and flagged if abnormal
- [ ] ST-segment analysis performed in all 12 leads
- [ ] STEMI criteria explicitly addressed (positive or negative)
- [ ] T-wave morphology described per territory
- [ ] Life-threatening patterns screened (Brugada, hyperkalemia, Wellens, PE)
- [ ] Prior ECG comparison documented or "no prior available" stated
- [ ] Lead reversal and artifact excluded
- [ ] Clinical correlation provided linking findings to reason for study
- [ ] All uncertain findings flagged with [VERIFY]
- [ ] Final impression includes structured summary with clinical priority

---

## Guidelines

1. Always interpret in a fixed sequence: rate → rhythm → axis → intervals → ST/T → patterns → clinical correlation. Skipping steps invites missed findings.
2. Never interpret ST segments in the presence of LBBB without applying Sgarbossa or modified Sgarbossa criteria.
3. When QTc is borderline prolonged, recalculate using Fridericia formula and note both values.
4. Document all negative findings explicitly — "No ST elevation, no pathologic Q waves, no conduction delay" is more defensible than silence.
5. Always report the ventricular rate separately from the atrial rate when they differ (e.g., atrial flutter with variable block).
6. Computer-generated interpretations must be overread and corrected — never accept machine reads as final.
7. For any new STEMI or STEMI-equivalent pattern, the interpretation must include a timestamp and the phrase "emergent cardiology notification recommended" or document why it was not indicated.
8. When paced rhythm is present, note the pacing mode and evaluate only the non-paced beats for native conduction assessment.
