---
name: interpreting-emergency-ecgs
description: Analyzes 12-lead ECGs for acute findings requiring emergent intervention. Use when reading emergency ECGs, identifying STEMI patterns, or flagging critical arrhythmias.
tags:
  - analysis
  - emergency-medicine
metadata:
  author: casemark
  practice_areas:
    - Emergency Medicine
  document_types:
    - Interpretation Report
  skill_modes:
    - Analysis
    - Interpretation
---

# Interpreting Emergency ECGs

Analyzes 12-lead ECGs for acute findings requiring emergent intervention, using a systematic approach to identify STEMI patterns, life-threatening arrhythmias, and high-risk ECG signatures.

## Why This Skill Exists

The 12-lead ECG is the single most important initial diagnostic test in acute chest pain evaluation and is required within 10 minutes of ED arrival per ACC/AHA guidelines. STEMI misdiagnosis or delayed cath lab activation carries catastrophic consequences — door-to-balloon time >90 minutes is associated with a 7.5% increase in in-hospital mortality per 30-minute delay. Conversely, false-positive cath lab activations waste resources and expose patients to unnecessary invasive procedures (false activation rates range 10-30% across institutions).

Beyond ACS, the emergency ECG must be screened for lethal arrhythmias (complete heart block, wide-complex tachycardia), metabolic emergencies (severe hyperkalemia), drug toxicity (sodium channel blockade, QT prolongation), and structural pathology (PE, pericarditis, Brugada). Emergency physicians must interpret ECGs with higher sensitivity than specificity — the cost of a miss far exceeds the cost of a false alarm. This skill provides a systematic, reproducible framework for emergency ECG interpretation.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. What is the clinical context (chief complaint, age, sex)? (Default: always interpret in clinical context)
2. Is a prior ECG available for comparison? (Default: request from EMR if available)
3. What is the time of symptom onset relative to the ECG acquisition? (Default: document both timestamps)
4. Is the patient currently symptomatic during this ECG? (Default: document symptom status at time of tracing)
5. What medications is the patient taking (digoxin, antiarrhythmics, QT-prolonging agents)? (Default: query medication list)
6. Does the patient have a pacemaker or ICD? (Default: document device presence and type)
7. What is the patient's potassium level if known? (Default: check point-of-care metabolic panel)

### Documents to Request

- Prior ECG tracings (most recent and baseline)
- Current medication list with focus on cardiac and QT-prolonging drugs
- Pacemaker/ICD interrogation report if applicable
- Prior cardiac catheterization or stress test results
- Known baseline bundle branch block or axis deviation

---

## Step 1: Systematic Rate and Rhythm Assessment

Follow this exact sequence on every ECG before pattern recognition:

### Rate Calculation
- Regular rhythm: 300 / (number of large boxes between R-R) = rate
- Irregular rhythm: count QRS complexes in 10 seconds × 6
- Normal: 60-100 bpm | Bradycardia: <60 | Tachycardia: >100

### Rhythm Determination Checklist
1. Is the rhythm regular or irregular?
2. Is there a P wave before every QRS?
3. Is there a QRS after every P wave?
4. Is the PR interval constant?
5. Is the QRS narrow (<120 ms) or wide (≥120 ms)?

### Axis Assessment
- Normal axis: Lead I (+), aVF (+)
- Left axis deviation: Lead I (+), aVF (−) — consider LAFB, LVH, inferior MI
- Right axis deviation: Lead I (−), aVF (+) — consider RVH, PE, lateral MI, LPFB
- Extreme axis: Lead I (−), aVF (−) — consider ventricular rhythm, lead misplacement

---

## Step 2: Interval Measurement and Block Identification

| Interval | Normal | Abnormal | Emergency Significance |
|----------|--------|----------|----------------------|
| PR | 120-200 ms | >200 ms = 1st degree AV block; progressively lengthening = 2nd degree Type I; dropped beats without lengthening = 2nd degree Type II; complete dissociation = 3rd degree | 2nd degree Type II and 3rd degree = emergent pacing |
| QRS | <120 ms | 120-200 ms = BBB or aberrancy; >200 ms = ventricular origin or severe toxicity | New BBB in ACS context = consider STEMI equivalent |
| QTc | <440 ms (M), <460 ms (F) | >500 ms = high risk for Torsades de Pointes | Discontinue offending agents, replete Mg2+ and K+ |

### Bundle Branch Block Differentiation

**RBBB (V1 = rSR', V6 = qRS, wide S in I and V6):**
- Commonly benign but new RBBB in acute chest pain = consider PE or RV strain

**LBBB (V1 = rS or QS, V6 = tall R without Q, I = monomorphic R):**
- New LBBB + symptoms = cath lab activation per Sgarbossa criteria
- **Sgarbossa Criteria (≥3 points = STEMI):**
  - Concordant ST elevation ≥1 mm in leads with positive QRS = 5 points
  - ST depression ≥1 mm in V1-V3 = 3 points
  - Discordant ST elevation ≥5 mm (or use Smith-modified ratio >0.25) = 2 points

---

## Step 3: ST Segment and Acute Ischemia Evaluation

### STEMI Recognition by Territory

| Territory | Leads with ST Elevation | Culprit Artery |
|-----------|------------------------|----------------|
| Anterior | V1-V4 | LAD |
| Lateral | I, aVL, V5-V6 | LCx or diagonal |
| Inferior | II, III, aVF | RCA (85%) or LCx (15%) |
| Right ventricular | V4R (obtain if inferior STEMI) | Proximal RCA |
| Posterior | V7-V9 (obtain if tall R in V1-V2 with ST depression) | PDA or LCx |

**STEMI criteria (in ≥2 contiguous leads):**
- ST elevation ≥1 mm in limb leads
- ST elevation ≥2 mm in V2-V3 (men ≥40), ≥2.5 mm V2-V3 (men <40), ≥1.5 mm V2-V3 (women)

### STEMI Equivalents (require same urgency)
- de Winter T waves: upsloping ST depression at J point with tall symmetric T waves in precordial leads (LAD occlusion)
- Wellens syndrome: deep T-wave inversions or biphasic T waves in V2-V3 (critical LAD stenosis — NOT during pain)
- Hyperacute T waves: tall, broad, symmetric T waves preceding ST elevation (very early STEMI)
- New LBBB with positive Sgarbossa criteria
- Posterior STEMI: ST depression V1-V3 with tall R waves (confirm with V7-V9)

### Non-STEMI Patterns
- Diffuse ST depression with ST elevation in aVR = left main or severe 3-vessel disease — cardiology emergent consult
- Dynamic T-wave inversions in the same territory = unstable angina or NSTEMI evolution

---

## Step 4: Non-ACS Emergency Patterns

| Pattern | ECG Findings | Emergency Action |
|---------|-------------|------------------|
| Hyperkalemia | Peaked T waves → widened QRS → sine wave → asystole | Calcium gluconate 10 mL of 10% IV over 2-3 min |
| Severe hypokalemia | Prominent U waves, flattened T waves, ST depression | Replete K+ aggressively, cardiac monitoring |
| PE (right heart strain) | S1Q3T3, RBBB, TWI V1-V4, sinus tachycardia, RAD | CTA pulmonary angiography, anticoagulation |
| Pericarditis | Diffuse ST elevation (concave up), PR depression, Spodick sign | NSAIDs + colchicine, rule out myocarditis |
| Brugada Type 1 | Coved ST elevation ≥2 mm in V1-V2 with T-wave inversion | Cardiology consult, avoid triggering drugs, consider ICD |
| Digitalis toxicity | Scooped ST ("Salvador Dali"), PAT with block, bidirectional VT | Digibind (digoxin-specific Fab fragments) |
| Sodium channel blockade (TCA, cocaine) | Wide QRS >100 ms, tall R in aVR >3 mm | Sodium bicarb boluses 1-2 mEq/kg IV |
| WPW | Short PR, delta wave, wide QRS | If AFib with WPW: procainamide or cardioversion; AVOID AV nodal blockers |

---

## Step 5: Documentation and Communication

### ECG Interpretation Documentation Template

```
ECG Time: [HH:MM]  |  Clinical Context: [chief complaint, age, sex]
Rate: [  ] bpm  |  Rhythm: [regular/irregular, sinus/non-sinus]
Axis: [normal/LAD/RAD]  |  PR: [  ] ms  |  QRS: [  ] ms  |  QTc: [  ] ms
ST Changes: [describe by lead group]
T-Wave Changes: [describe]
Comparison to Prior: [new/unchanged/improved]
Interpretation: [final impression]
Action Taken: [cath lab activation / serial ECG ordered / cardiology consulted / none needed]
```

### Critical Value Communication
- STEMI or STEMI-equivalent: verbal notification to attending + cath lab activation within 3 minutes of identification
- New complete heart block or wide-complex tachycardia: immediate bedside physician notification
- QTc >500 ms: alert provider, review medication list, place on telemetry
- Hyperkalemia pattern: immediate point-of-care potassium + treatment protocol

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Was the ECG interpreted using a systematic approach (rate → rhythm → axis → intervals → ST/T)?
2. Were STEMI criteria applied correctly with contiguous lead requirements and sex-specific thresholds?
3. Were STEMI equivalents (de Winter, Wellens, posterior MI) actively screened for?
4. Were non-ACS emergencies (hyperkalemia, PE, toxicity) considered in the differential?
5. Was the interpretation communicated to the treating provider with appropriate urgency?

---

## Quality Audit

- [ ] ECG acquisition time documented and within 10 minutes of arrival for chest pain
- [ ] Rate, rhythm, axis, and all intervals (PR, QRS, QTc) explicitly stated
- [ ] ST segment changes described by lead group with millimeter measurements
- [ ] STEMI criteria evaluated using sex-and-age-appropriate thresholds
- [ ] STEMI equivalents actively screened (de Winter, Wellens, hyperacute T, posterior MI)
- [ ] Comparison to prior ECG documented (or "no prior available")
- [ ] Non-ACS emergency patterns screened (hyperkalemia, PE, WPW, toxicity)
- [ ] Clinical context stated in interpretation (not interpreted in isolation)
- [ ] Critical findings communicated verbally with time and recipient documented
- [ ] Serial ECG plan documented if initial ECG non-diagnostic with ongoing symptoms
- [ ] Lead placement quality assessed (appropriate R-wave progression, no lead reversal signs)
- [ ] QTc calculated and medication list cross-checked if prolonged
- [ ] Pacemaker or device presence noted in interpretation if applicable

---

## Guidelines

1. Never interpret an ECG in clinical isolation — always correlate with the presenting complaint, age, sex, and symptom timeline.
2. Obtain a 12-lead ECG within 10 minutes of arrival for any patient with chest pain, dyspnea, syncope, or palpitations — this is a CMS core quality measure.
3. If the first ECG is non-diagnostic but symptoms persist, repeat the ECG every 15-30 minutes — STEMI can evolve from a normal baseline in minutes.
4. Always obtain right-sided leads (V4R) in inferior STEMI to evaluate for RV involvement — RV infarction contraindicates nitroglycerin and requires volume resuscitation.
5. A normal ECG does not exclude ACS — sensitivity of a single ECG for acute MI is only 45-60%.
6. Treat the patient, not the ECG — if clinical suspicion for STEMI is high despite an ambiguous tracing, activate the cath lab and let the interventionalist make the final call.
7. QTc >500 ms is a medical emergency requiring medication review, electrolyte repletion (Mg2+ ≥2.0, K+ ≥4.0), and continuous telemetry monitoring.
8. In wide-complex tachycardia of uncertain origin, treat as ventricular tachycardia until proven otherwise — the safest initial approach is always to assume the worst-case diagnosis.
