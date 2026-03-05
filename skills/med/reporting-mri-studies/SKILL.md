---
name: reporting-mri-studies
description: Structures MRI interpretation with sequence-specific analysis and standardized reporting. Use when reading MRI studies, creating MRI reports, or analyzing multisequence findings.
tags:
  - reporting
  - radiology
metadata:
  author: casemark
  practice_areas:
    - Radiology
    - Diagnostic Imaging
  document_types:
    - Report
  skill_modes:
    - Reporting
---

# Reporting MRI Studies

Generates structured, standards-compliant MRI reports with sequence-specific analysis, standardized lexicon, and actionable impression statements.

## Why This Skill Exists

Unstructured MRI reports are a leading source of diagnostic ambiguity. The ACR Practice Parameter for Communication of Diagnostic Imaging Findings (revised 2020) mandates that reports contain specific elements: clinical indication, comparison studies, technique, findings organized by anatomic region, and an impression that directly addresses the clinical question. Studies show that structured reporting reduces clinically significant omission rates from ~30% to under 5% (Schwartz et al., Radiology 2011). RSNA's RadReport initiative provides specialty-specific templates, and lexicon systems such as BI-RADS (breast), PI-RADS v2.1 (prostate), LI-RADS v2018 (liver), and O-RADS (ovarian) exist precisely because free-text reporting leads to inconsistent management recommendations.

An AI agent drafting MRI reports must understand that each pulse sequence encodes distinct tissue contrast: T1-weighted images highlight fat and gadolinium enhancement; T2-weighted images highlight fluid; FLAIR suppresses CSF to reveal periventricular lesions; DWI/ADC maps detect restricted diffusion in acute ischemia, abscess, and hypercellular tumors; SWI detects microhemorrhages and calcification; MRA/MRV map vascular anatomy. A report that fails to correlate findings across sequences — or omits a sequence entirely — is an incomplete report. This skill ensures no sequence is skipped, measurements follow RECIST 1.1 or disease-specific criteria, and the impression maps to a defined category or recommendation tier.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Before drafting, gather the following from the user. Apply the listed defaults if no answer is provided.

1. **Body region and clinical indication?** (e.g., "Brain MRI for new-onset seizure") — no default; must be specified.
2. **Sequences available?** (e.g., T1, T1+C, T2, FLAIR, DWI/ADC, SWI, MRA) — default: assume standard protocol for the body region.
3. **Field strength?** (1.5T or 3T) — default: 3T.
4. **Contrast administered?** (agent, dose, route) — default: gadolinium-based, 0.1 mmol/kg IV, if post-contrast images present.
5. **Comparison studies available?** (modality, date) — default: "No prior studies available for comparison."
6. **Applicable structured lexicon?** (BI-RADS, PI-RADS v2.1, LI-RADS v2018, O-RADS, MS McDonald criteria, mRECIST, etc.) — default: none; use descriptive reporting.
7. **Measurement standard?** (RECIST 1.1, WHO, iRECIST, disease-specific) — default: RECIST 1.1 for oncologic, longest axis otherwise.
8. **Referring clinician's specific question?** — default: infer from clinical indication.

### Documents to Request

- Requisition / order with clinical history and specific question
- Prior imaging reports (most recent same-modality study minimum)
- Relevant lab values (eGFR if contrast, PSA if prostate, AFP/bilirubin if liver)
- Surgical or treatment history affecting the imaged region
- Sequence list / protocol sheet from the scanner console
- Any outside images on CD/PACS for comparison

---

## Step 1: Technical Assessment and Protocol Verification

Review the study for technical adequacy before interpreting findings.

| Check | Pass Criteria | Action if Fail |
|---|---|---|
| All expected sequences present | Protocol matches body-region standard | Note missing sequence; state limitation in report |
| Motion artifact | No significant degradation of diagnostic quality | Grade: none / mild / moderate / severe; note affected sequences |
| Coverage | Entire region of interest included | Note truncation (e.g., "Inferior cerebellum excluded from FOV") |
| Contrast timing | Arterial, portal-venous, delayed phases as required | Note missing phase; flag if LI-RADS/PI-RADS scoring is compromised |
| Fat suppression quality | Uniform suppression without swap artifacts | Note regional failure and affected anatomy |
| DWI b-values | At minimum b=0 and b=1000 for body; b=0 and b=1000+ for neuro | Note if only low b-value available; ADC map may be unreliable |

**Deliverable:** A "Technique" paragraph listing field strength, sequences obtained, contrast agent/dose/route, and any technical limitations.

---

## Step 2: Systematic Sequence-by-Sequence Analysis

For each sequence, document findings using the following framework. Do NOT skip a sequence — if a sequence is normal, state so explicitly.

### Neuro MRI Sequence Checklist

| Sequence | Primary Tissue Contrast | Key Pathology to Assess |
|---|---|---|
| T1 pre-contrast | Fat = bright, fluid = dark | Subacute hemorrhage (met-Hb), fat-containing lesions, cortical laminar necrosis |
| T1 post-contrast | Enhancement = bright | Blood-brain barrier breakdown, leptomeningeal disease, dural enhancement |
| T2 | Fluid = bright, muscle = intermediate | Edema, gliosis, cysts, demyelination |
| FLAIR | Fluid suppressed, edema = bright | Periventricular WM lesions, subarachnoid hemorrhage, cortical infarcts |
| DWI / ADC | Restricted diffusion = DWI bright + ADC dark | Acute ischemia (<6h), abscess, epidermoid, hypercellular tumor |
| SWI / GRE | Susceptibility = dark blooming | Microhemorrhages, cavernomas, calcification, vascular malformations |
| MRA (TOF or CE) | Flow-related signal | Stenosis, occlusion, aneurysm (report size, morphology, parent vessel) |
| MRS (if obtained) | Metabolite ratios | NAA (neuronal marker), Choline (cell turnover), Lactate (anaerobic), Lipid (necrosis) |

### Body MRI Additional Sequences

| Sequence | Key Application |
|---|---|
| T1 in/out-of-phase (Dixon) | Hepatic steatosis (signal drop on out-of-phase), adrenal adenoma characterization |
| Dynamic contrast-enhanced (DCE) | Arterial phase hyperenhancement (APHE) for HCC, PI-RADS scoring for prostate |
| Hepatobiliary phase (gadoxetate) | Hepatocyte uptake defect = hypointensity (HCC, FNH vs. adenoma differentiation) |
| MRCP | Biliary/pancreatic ductal anatomy, strictures, filling defects |
| Diffusion (body) | Restricted diffusion in lymph nodes, peritoneal implants, rectal tumors |

**Deliverable:** A findings section organized by anatomic compartment, with each finding cross-referenced across all relevant sequences.

---

## Step 3: Lesion Characterization and Measurement

For every discrete lesion, document the following in a structured table:

| Field | Requirement |
|---|---|
| Location | Anatomic site using standard nomenclature (e.g., "right frontal lobe, subcortical white matter") |
| Size | Three-axis measurements in mm (AP x TR x CC); for RECIST, report longest axis; for lymph nodes, short axis |
| Signal characteristics | T1 signal, T2 signal, FLAIR signal, DWI/ADC behavior, enhancement pattern (homogeneous, ring, peripheral, none) |
| Morphology | Shape (round, oval, irregular), margins (well-defined, ill-defined, infiltrative), internal architecture (solid, cystic, complex) |
| Mass effect | Midline shift (mm), effacement of sulci/ventricles/cisterns, uncal herniation |
| Comparison | Change from prior: new, increased, decreased, stable. Provide prior measurement and date. |
| Category (if applicable) | BI-RADS 1-6, PI-RADS 1-5, LI-RADS LR-1 through LR-5/LR-M/LR-TIV, O-RADS 0-5 |

### Measurement Rules

- **RECIST 1.1:** Longest diameter in axial plane. Minimum 10 mm for measurable; lymph nodes require short axis >= 15 mm. [VERIFY] measurement plane consistency with prior study.
- **PI-RADS v2.1:** Peripheral zone lesions measured on DWI; transition zone lesions measured on T2. Report largest dimension.
- **LI-RADS v2018:** Observations measured on the sequence/phase showing largest dimension. APHE must be unequivocal. Non-rim APHE + one of: enhancing capsule, threshold growth (>= 50% in <= 6 months), washout = LR-5.
- **McDonald Criteria (MS):** Count T2/FLAIR lesions by location (periventricular, cortical/juxtacortical, infratentorial, spinal cord). Dissemination in space requires >= 1 lesion in >= 2 of 4 areas. [VERIFY] whether enhancing lesions coexist with non-enhancing to satisfy dissemination in time.

---

## Step 4: Synthesize the Impression

The impression is the most-read section. It must:

1. **Answer the clinical question first.** ("No acute intracranial abnormality to account for the patient's seizures.")
2. **Prioritize by clinical significance** — list the most actionable finding first, incidental findings last.
3. **Assign a category** when a structured lexicon applies, including the recommended management action.
4. **Quantify change** when prior comparison exists (e.g., "Dominant right hepatic lobe lesion measures 3.2 cm, previously 2.1 cm, consistent with interval progression per RECIST 1.1").
5. **Recommend next steps** when appropriate (e.g., "Short-interval follow-up MRI in 3 months recommended per LI-RADS LR-3 management guidelines").

### Impression Template

```
IMPRESSION:
1. [Primary finding addressing clinical question]. [Category if applicable].
   - Recommendation: [Specific follow-up or management per guideline].
2. [Secondary finding]. [Measurement and comparison if applicable].
3. [Incidental finding]. [Follow-up recommendation per ACR Incidental Findings Committee guidelines if applicable].
```

---

## Step 5: Assemble the Final Report

Combine all sections into the standard radiology report format:

```
EXAMINATION: MRI [Body Region] [with/without contrast]
CLINICAL INDICATION: [History and specific question]
COMPARISON: [Modality, date] or "None available"
TECHNIQUE: [Field strength, sequences, contrast agent/dose/route, any limitations]

FINDINGS:

[Organized by anatomic compartment]
[Each compartment: normal statement or abnormality with sequence-specific detail]
[Lesion table for discrete lesions]

IMPRESSION:
[Numbered, prioritized, with categories and recommendations]
```

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

Before finalizing, confirm with the user:

1. Does the impression directly answer the referring clinician's question?
2. Are all measurable lesions reported with three-axis dimensions and comparison to prior?
3. If a structured lexicon applies (BI-RADS, PI-RADS, LI-RADS, O-RADS), is the category explicitly stated with the management recommendation?
4. Are technical limitations (motion, missing sequences, suboptimal contrast timing) documented in the Technique section?
5. Are incidental findings addressed with appropriate follow-up recommendations per ACR Incidental Findings Committee white papers?

---

## Quality Audit

### Completeness

- [ ] Clinical indication and specific question are stated
- [ ] All comparison studies are listed with modality and date
- [ ] Every acquired sequence is mentioned in Technique or addressed in Findings
- [ ] Each anatomic compartment relevant to the body region is explicitly addressed (normal or abnormal)

### Accuracy

- [ ] Signal descriptions are sequence-appropriate (e.g., not describing a lesion as "bright on T1" without specifying pre- or post-contrast)
- [ ] DWI findings always include corresponding ADC correlation (true restricted diffusion vs. T2 shine-through)
- [ ] Enhancement patterns specify phase (arterial, venous, delayed) when dynamic imaging was performed
- [ ] Measurements use the correct standard (RECIST 1.1, PI-RADS, LI-RADS) and are in millimeters

### Standardized Reporting

- [ ] Structured lexicon category is assigned when applicable and matches the described imaging features
- [ ] Management recommendation accompanies every assigned category
- [ ] Impression findings are numbered and ordered by clinical significance

### Safety

- [ ] No unsupported definitive diagnoses — pathologic correlation recommended where appropriate
- [ ] `[VERIFY]` tags placed on any measurement or comparison where source data is ambiguous
- [ ] Critical or unexpected findings flagged for direct communication per ACR Practice Parameter
- [ ] Laterality is explicitly stated for all paired structures (e.g., "right kidney" not "the kidney")

---

## Guidelines

1. **Use standard radiology lexicon.** Describe signal intensity as hyperintense, isointense, or hypointense relative to a named reference tissue (e.g., "T2 hyperintense relative to skeletal muscle"). Never use vague terms like "abnormal signal."
2. **Always correlate DWI with ADC.** A finding that is DWI bright but ADC bright is T2 shine-through, not restricted diffusion. State this distinction explicitly.
3. **Report negative pertinent findings.** If the clinical question is stroke, explicitly state "No restricted diffusion to suggest acute infarct." Absence of a statement is not the same as a negative finding.
4. **Apply the ACR Incidental Findings Committee recommendations.** For renal cysts use Bosniak v2019; for adrenal nodules use chemical-shift analysis; for thyroid nodules on neck MRI use ACR TI-RADS size thresholds adapted for MRI. Cite the specific guideline.
5. **Never omit the hepatobiliary phase.** If gadoxetate-enhanced MRI was performed, hepatobiliary phase findings must be reported for every hepatic observation. Failure to report uptake/non-uptake is an incomplete LI-RADS assessment.
6. **Treat the impression as a clinical decision tool.** Each impression item should allow the referring clinician to take action without re-reading the Findings section. Include the diagnosis or differential, the category, and the recommended next step.
7. **Flag critical findings per ACR guidelines.** Findings requiring urgent communication (e.g., acute stroke, cauda equina compression, new intracranial mass with herniation) must be marked in the report and communicated directly to the ordering provider with documentation of the communication in the report.
8. **Maintain measurement consistency across time points.** Always measure in the same plane, same sequence, and same phase as the prior study. If the prior measurement methodology is unknown, state this as a limitation and mark with `[VERIFY]`.
