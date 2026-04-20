---
name: tracking-incidental-findings
language: en
description: Manages incidental finding follow-up using ACR White Paper recommendations. Use when tracking incidentalomas, scheduling follow-up imaging, or managing unexpected findings.
tags:
  - monitoring
  - radiology
metadata:
  author: casemark
  practice_areas:
    - Radiology
    - Diagnostic Imaging
  document_types:
    - Tracking Report
  skill_modes:
    - Monitoring
---

# Tracking Incidental Findings

Manages incidental finding follow-up using ACR White Paper recommendations.

## Why This Skill Exists

Incidental findings — abnormalities discovered on imaging performed for an unrelated indication — occur in up to 40% of CT scans. The ACR Incidental Findings Committee has published organ-specific white papers providing evidence-based management algorithms for adrenal, renal, hepatic, pancreatic, splenic, and thyroid incidentalomas. Without structured tracking, incidental findings are lost to follow-up at alarming rates: studies show 30–70% of incidental findings with recommended follow-up never receive it. Lost follow-up exposes patients to delayed cancer diagnosis and represents a major medicolegal liability for radiologists and referring providers.

The Joint Commission and CMS Conditions of Participation require systems for critical result communication, and many institutions extend this to actionable incidental findings. ACR accreditation standards expect that radiology reports include specific, evidence-based follow-up recommendations for incidentalomas rather than vague "clinical correlation" statements. This skill provides the systematic framework for categorizing, recommending, tracking, and closing the loop on incidental findings.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. **What organ/structure is the incidental finding in?** (Default: Identify from imaging report)
2. **What is the size of the finding?** (Default: Measure from imaging; record in mm)
3. **What imaging modality detected the finding?** (Default: CT — specify if MRI, US, or other)
4. **Was contrast administered?** (Default: Yes — impacts characterization ability)
5. **Does the patient have relevant risk factors?** (Default: No known malignancy, cirrhosis, or endocrine disorder)
6. **Are prior studies available showing this finding?** (Default: No — first identification)
7. **What was the original clinical indication for the study?** (Default: Document the primary reason)
8. **Is there an institutional incidental-findings tracking system?** (Default: Verify with department)

### Documents to Request

- Original imaging study and report identifying the finding
- Prior imaging (any modality) for comparison
- Patient medical history, especially cancer history and risk factors
- Lab values (TSH for thyroid, catecholamines for adrenal, AFP for liver, eGFR for renal)
- Institutional incidental-findings policy and tracking-system workflow
- ACR Incidental Findings Committee white papers (organ-specific)

---

## Step 1: Categorize the Incidental Finding

### ACR Incidental Findings — Organ-Specific Decision Matrix

| Organ | Finding Type | Key Characterization Features | Primary Reference |
|-------|-------------|------------------------------|-------------------|
| Adrenal | Nodule | Size, attenuation (HU on non-con CT), washout characteristics | ACR Adrenal White Paper 2017 |
| Kidney | Cystic mass | Bosniak v2019 classification (septations, enhancement, wall features) | ACR Renal White Paper 2017 |
| Kidney | Solid mass | Size, enhancement pattern | ACR Renal White Paper 2017 |
| Liver | Hepatic lesion | Patient population (cirrhosis vs. no), enhancement pattern, size | ACR Liver White Paper 2017 |
| Pancreas | Cystic lesion | Size, duct communication, mural nodularity, main duct dilatation | ACR Pancreas White Paper 2017 |
| Thyroid | Nodule on CT/MRI | Size, suspicious features (calcification, invasion) | ACR Thyroid White Paper 2015 |
| Spleen | Lesion | Homogeneity, enhancement, number | ACR Spleen White Paper 2017 |
| Lung | Nodule (non-screening) | Size, morphology, patient risk factors | Fleischner Society 2017 |

---

## Step 2: Apply Size- and Feature-Based Management Algorithms

### Adrenal Incidentaloma

| Size | Attenuation | Recommendation |
|------|-------------|----------------|
| ≤1 cm | Any | Benign; no follow-up required |
| 1–4 cm | ≤10 HU on non-contrast CT | Lipid-rich adenoma; no follow-up |
| 1–4 cm | >10 HU | Adrenal CT washout protocol or chemical-shift MRI |
| >4 cm | Any | Surgical consultation (concern for adrenal carcinoma/pheochromocytoma) |
| Any | Suspicious features (heterogeneous, hemorrhage, invasion) | Urgent surgical referral |

**Adrenal washout criteria:** Absolute washout >60% or relative washout >40% at 15-minute delay = adenoma.

### Renal Incidentaloma — Bosniak v2019

| Bosniak Class | Features | Management |
|--------------|----------|------------|
| I | Simple cyst: thin wall, no septa, no enhancement | No follow-up |
| II | Few thin septa, fine calcification, hyperdense (≤3 cm, homogeneous, non-enhancing) | No follow-up |
| IIF | Minimal thickening, many septa, thick calcification | Follow-up: 6, 12, 24 months |
| III | Thickened irregular septa or wall, measurable enhancement | Surgical or active surveillance |
| IV | Enhancing soft-tissue component | Surgical management |

### Pancreatic Cystic Lesion

| Size | Features | Recommendation |
|------|----------|---------------|
| <1.5 cm | No worrisome features | No follow-up or MRI in 2 years (varies by institution) |
| 1.5–2.5 cm | No worrisome features | MRI in 1 year, then extend interval |
| >2.5 cm | No worrisome features | MRI/EUS, consider multidisciplinary discussion |
| Any | Mural nodule, main duct >5 mm, solid component | EUS with FNA; surgical consultation |

### Thyroid Incidentaloma on CT/MRI

| Finding | Recommendation |
|---------|---------------|
| ≤1.0 cm, no suspicious features | No further workup in most patients |
| >1.0 cm without suspicious features | Thyroid US recommended |
| >1.5 cm | Thyroid US recommended |
| Any size with suspicious features (calcification, lymphadenopathy, invasion) | Thyroid US + possible FNA |
| Known thyroid cancer history | Thyroid US regardless of size |

---

## Step 3: Document the Finding in the Report

Every incidental finding report entry must include:

1. **Finding identifier** — organ, location, unique descriptor
2. **Size** — measured in standard axis for the organ system
3. **Characterization** — imaging features used for classification
4. **Classification** — ACR white paper category or Fleischner tier
5. **Recommendation** — specific modality, timing, and contrast requirement
6. **Urgency** — routine follow-up vs. expedited workup vs. urgent referral
7. **Communication** — to whom the finding was communicated and when

### Report Language Template
```
Incidental [size] [descriptor] [organ] [location].
Per ACR Incidental Findings Committee [organ] White Paper [year]:
Recommendation: [specific modality] in [timeframe].
[Communication documentation if required.]
```

---

## Step 4: Tracking System Entry and Closure

### Tracking Workflow

1. **Log entry** — Record finding in institutional tracking system with unique case ID
2. **Referring provider notification** — Document communication (name, date, time, method)
3. **Patient notification** — Per institutional policy (letter, portal message, phone)
4. **Follow-up scheduling** — Verify follow-up order is placed
5. **Follow-up completion** — Confirm follow-up study was performed
6. **Disposition** — Close the loop: resolved (benign), upgraded (further workup), stable (continue tracking)

### Tracking Data Elements

| Field | Description |
|-------|-------------|
| Patient MRN | Unique patient identifier |
| Finding | Organ, type, size, laterality |
| Detection date | Date of original study |
| ACR category | Classification per white paper |
| Recommended follow-up | Modality + timeframe |
| Due date | Calculated from detection date + recommended interval |
| Ordering provider | Name, NPI, contact |
| Communication date | When provider was notified |
| Follow-up status | Pending, scheduled, completed, lost, patient declined |
| Outcome | Benign, malignant, indeterminate, still tracking |

---

## Step 5: Escalation and Lost-to-Follow-Up Protocol

| Trigger | Action |
|---------|--------|
| Follow-up overdue by 30 days | Alert to ordering provider via EMR message |
| Follow-up overdue by 60 days | Escalate to department quality lead |
| Follow-up overdue by 90 days | Direct patient contact per institutional policy |
| Patient declines follow-up | Document informed refusal; notify ordering provider |
| Finding upgraded on follow-up | Expedited referral; update tracking status |
| Patient transferred care | Forward tracking record to new provider |

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Is the correct ACR white paper applied for the organ and finding type?
2. Does the recommendation include specific modality, timing, and contrast requirement?
3. Is the communication to the referring provider documented with name, date, and time?
4. Is the finding logged in the institutional tracking system with a due date?
5. Are patient risk factors accounted for in the management recommendation?

---

## Quality Audit

- [ ] Finding is categorized per the correct ACR Incidental Findings white paper
- [ ] Size is measured in the standard axis for the organ system
- [ ] Characterization features (HU, enhancement, morphology) are documented
- [ ] Management recommendation matches the ACR algorithm for the finding's size and features
- [ ] Follow-up includes specific modality, timing, and contrast requirement
- [ ] Referring provider is notified with documentation of name, date, time, method
- [ ] Tracking system entry is created with all required data elements
- [ ] Due date is calculated and recorded
- [ ] Patient risk factors are assessed and factored into management
- [ ] Prior studies are reviewed to determine if finding is new or stable
- [ ] Report avoids vague language ("clinical correlation recommended") in favor of specific recommendations
- [ ] Critical incidental findings (e.g., suspicious mass) trigger same-day communication
- [ ] Lost-to-follow-up protocol is in place with defined escalation timeline
- [ ] Finding closure is documented when follow-up is completed

---

## Guidelines

1. Every incidental finding must have a specific follow-up recommendation — "clinical correlation recommended" is never acceptable as the sole management plan.
2. Apply the most current ACR Incidental Findings Committee white paper for the relevant organ system; do not use outdated criteria.
3. Adrenal nodule characterization requires non-contrast HU or washout calculation; do not characterize on contrast-enhanced images alone unless washout is performed.
4. Bosniak v2019 criteria differ from earlier versions — use the current classification and document the version applied.
5. Institutions must have a closed-loop tracking system; if none exists, recommend implementation as a quality-improvement initiative.
6. Risk factors change management — a thyroid incidentaloma in a patient with prior head/neck radiation or thyroid cancer history requires workup regardless of size.
7. Document patient refusal of follow-up in the medical record and ensure the referring provider is aware.
8. When multiple incidental findings coexist, each requires its own classification and tracking entry.
