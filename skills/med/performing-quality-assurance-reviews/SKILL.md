---
name: performing-quality-assurance-reviews
language: en
description: Structures radiology peer review and quality assurance with discrepancy classification. Use when conducting peer review, classifying discrepancies, or documenting QA findings.
tags:
  - process
  - radiology
metadata:
  author: casemark
  practice_areas:
    - Radiology
    - Diagnostic Imaging
  document_types:
    - Procedure Note
  skill_modes:
    - Execution
---

# Performing Quality Assurance Reviews

Structures radiology peer review and quality assurance with discrepancy classification.

## Why This Skill Exists

Radiology peer review is mandated by The Joint Commission (OPPE/FPPE requirements), CMS Conditions of Participation, and ACR accreditation standards. Peer review serves as the primary mechanism for identifying diagnostic errors, measuring individual and departmental performance, and driving continuous quality improvement. The ACR Practice Parameter for Peer Review recommends that every radiologist have a representative sample of cases reviewed — the RADPEER system, developed by the ACR, provides a standardized scoring framework used by over 1,000 radiology practices nationwide.

Effective peer review requires structured discrepancy classification, non-punitive culture, actionable feedback, and integration with departmental quality metrics. Without a systematic approach, peer review devolves into either rubber-stamping (no errors found) or punitive witch-hunts (discouraging participation). The goal is to identify patterns — individual learning opportunities, systemic workflow issues, and equipment problems — that can be addressed to improve patient care. This skill provides the framework for conducting defensible, productive, and accreditation-compliant peer review.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. **What type of review is being conducted?** (Default: Prospective RADPEER, retrospective case review, focused review, or sentinel event review)
2. **What is the review scope?** (Default: Individual case, batch review, or thematic review)
3. **Is there a clinical discrepancy that triggered this review?** (Default: Routine random vs. triggered by clinical concern)
4. **Who is the reviewing radiologist?** (Default: Peer of equivalent or higher subspecialty training)
5. **Is this OPPE (Ongoing Professional Practice Evaluation) or FPPE (Focused Professional Practice Evaluation)?** (Default: OPPE)
6. **What is the institutional peer-review protection status?** (Default: Verify state-specific peer-review privilege protections)

### Documents to Request

- Original radiology report and images
- Current/subsequent imaging for comparison
- Clinical outcome data (surgical findings, pathology, clinical course)
- Institutional peer-review policy and scoring criteria
- RADPEER scoring reference materials
- Prior peer-review history for the radiologist (if OPPE/FPPE)
- State peer-review privilege statute reference

---

## Step 1: RADPEER Scoring System

### ACR RADPEER Score Definitions

| Score | Definition | Description |
|-------|-----------|-------------|
| **1** | Agree with interpretation | No discrepancy identified |
| **2a** | Discrepancy — NOT clinically significant | Finding was missed or misinterpreted but would not have changed management |
| **2b** | Discrepancy — diagnosis should have been made; clinically significant | The missed/incorrect finding would have changed management at the time of original interpretation |
| **3a** | Misinterpretation — NOT clinically significant | Major diagnostic error that did not impact clinical outcome |
| **3b** | Misinterpretation — diagnosis should have been made; clinically significant | Major diagnostic error that impacted or could have impacted clinical outcome |
| **4** | Non-gradable | Poor image quality, incomplete study, or inadequate clinical information prevents meaningful review |

### Scoring Decision Tree

```
Was a finding missed or misinterpreted?
├── No → Score 1 (Agree)
└── Yes → Was it a significant discrepancy?
    ├── Discrepancy (understandable miss) → 
    │   ├── Clinically significant? → 2b
    │   └── Not clinically significant? → 2a
    └── Misinterpretation (should have been caught) →
        ├── Clinically significant? → 3b
        └── Not clinically significant? → 3a
```

---

## Step 2: Discrepancy Root-Cause Analysis

### Error Classification Taxonomy

| Error Type | Definition | Examples |
|-----------|-----------|---------|
| **Perceptual** | Finding visible in retrospect but not detected | Missed lung nodule, overlooked fracture |
| **Cognitive** | Finding detected but incorrectly interpreted | Mass called benign that was malignant; wrong classification |
| **Communication** | Finding correctly identified but inadequately communicated | Critical result not communicated; vague impression language |
| **System** | Error caused by workflow, technology, or process failure | Wrong patient images, prior studies unavailable, workstation display issue |
| **Satisfaction of search** | Stopped looking after finding one abnormality | Missed second finding after identifying the first |

### Contributing Factors to Document

| Factor Category | Examples |
|----------------|---------|
| Workload | High volume at time of interpretation; fatigue |
| Image quality | Suboptimal study, motion artifact, poor technique |
| Clinical information | Inadequate history, misleading indication |
| Prior availability | No priors available that would have aided interpretation |
| Subspecialty expertise | Case outside reviewer's primary subspecialty |
| Technology | Workstation display, hanging protocol, CAD availability |
| Time pressure | Stat reads, stroke code, trauma activation |

---

## Step 3: Conducting the Review — Workflow

### Prospective RADPEER (Random Sampling)

1. **Case selection** — Random cases from each radiologist's workload (minimum per ACR: variable by institution; typically 3–5% of interpretations or set number per quarter)
2. **Blinded review** — Reviewing radiologist interprets the current study independently before reading the original report
3. **Comparison** — Compare reviewer's interpretation with original report
4. **Score assignment** — Apply RADPEER score with written justification for scores ≥2
5. **Documentation** — Record in peer-review database with case details
6. **Feedback** — Communicate results to the reviewed radiologist per institutional policy

### Triggered/Focused Review

| Trigger | Review Scope | Timeline |
|---------|-------------|----------|
| Clinical discrepancy reported by referring provider | Specific case + 5–10 similar recent cases | Within 48 hours |
| Surgical/pathology discordance | Specific case + related studies | Within 1 week |
| Pattern identified in routine RADPEER | Targeted review of similar case types (50+ cases) | Within 1 month |
| Near-miss or sentinel event | Root-cause analysis with full case reconstruction | Immediate |
| FPPE (new or re-credentialed radiologist) | First 50–100 cases across modalities | First 3–6 months |

---

## Step 4: Quality Metrics and Reporting

### Individual Radiologist Metrics

| Metric | Calculation | Benchmark |
|--------|-----------|-----------|
| Agreement rate | Score 1 / Total reviewed cases | >95% (RADPEER national aggregate) |
| Clinically significant discrepancy rate | (2b + 3b) / Total reviewed cases | <3% (ACR benchmark) |
| Major discrepancy rate | (3a + 3b) / Total reviewed cases | <1% |
| Score distribution | Percentage in each RADPEER category | Compare to department and national averages |

### Department-Level Metrics

| Metric | Purpose |
|--------|---------|
| Overall discrepancy rate by modality | Identify modality-specific quality issues |
| Discrepancy rate by exam type | Identify challenging study types |
| Error-type distribution | Perceptual vs. cognitive vs. communication vs. system |
| Trend over time | Quarterly/annual improvement tracking |
| Communication compliance | Critical-result communication rate and timeliness |
| Addendum rate | Frequency of report amendments — high rates suggest workflow issues |
| Prelim-to-final discrepancy rate | For resident/fellow reads vs. attending final |

### Reporting Requirements

| Audience | Frequency | Content |
|----------|-----------|---------|
| Individual radiologist | Each reviewed case + quarterly summary | RADPEER scores, feedback, improvement suggestions |
| Department/section | Quarterly | Aggregate metrics, trends, identified patterns |
| Medical staff / credentials committee | Semi-annual (OPPE) | Individual performance summary, benchmarking |
| Hospital quality committee | Annual | Department performance, improvement initiatives |
| ACR (if DIR/QI participant) | Per program schedule | Aggregated quality data |

---

## Step 5: Improvement Actions and Follow-Up

### Action Plans Based on RADPEER Patterns

| Pattern | Action |
|---------|--------|
| Isolated 2a score | Educational feedback; no formal action |
| Recurring 2a scores in same modality | Targeted CME; case review session |
| Any 2b or 3a score | Individual case discussion; root-cause review |
| 3b score | Formal peer-review committee discussion; corrective action plan |
| Pattern of 2b+ in same area | FPPE (focused professional practice evaluation) |
| Systemic errors (multiple radiologists) | Workflow/process improvement; protocol update; technology review |

### Peer-Review Committee Structure

| Role | Responsibility |
|------|---------------|
| Chair | Leads committee meetings; reports to medical staff leadership |
| Subspecialty representatives | Review cases in their area of expertise |
| Quality coordinator | Manages database, tracks metrics, prepares reports |
| Medical director | Oversees corrective actions; interfaces with credentialing |
| Legal counsel (as needed) | Advises on peer-review protection and privilege |

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Is the correct RADPEER score assigned with written justification?
2. Is the error type classified (perceptual, cognitive, communication, system)?
3. Are contributing factors documented?
4. Is clinical significance assessed (impact on patient management)?
5. Is the review documented within the peer-review-protected system?

---

## Quality Audit

- [ ] Review type is specified (RADPEER, triggered, OPPE, FPPE)
- [ ] RADPEER score is assigned per ACR definitions
- [ ] Written justification accompanies scores ≥2a
- [ ] Error type is classified (perceptual, cognitive, communication, system)
- [ ] Contributing factors are documented
- [ ] Clinical significance is assessed
- [ ] Outcome data (surgical/pathology) is referenced when available
- [ ] Review is documented in a peer-review-protected database
- [ ] Individual feedback is provided to the reviewed radiologist
- [ ] Aggregate metrics are tracked and trended quarterly
- [ ] Action plans are defined for significant or recurring discrepancies
- [ ] Department-level metrics are reported to quality committee
- [ ] Peer-review privilege protection is maintained per state statute
- [ ] FPPE cases meet minimum volume requirements for new/re-credentialed radiologists

---

## Guidelines

1. Peer review must be conducted in a non-punitive, educational framework — the goal is quality improvement, not individual blame.
2. Apply RADPEER scores using ACR definitions precisely; do not conflate discrepancy severity categories.
3. Always document clinical significance — a missed finding that would not have changed management is categorically different from one that would.
4. Root-cause analysis should identify system factors (workflow, workload, technology) as well as individual factors — most errors have systemic contributors.
5. Maintain peer-review documentation within the legally protected peer-review system per state statute; mingling QA data with non-protected records risks loss of privilege.
6. FPPE for newly credentialed radiologists should include a minimum of 50–100 cases across the radiologist's scope of practice within the first 3–6 months.
7. Trend data is more actionable than individual case scores — a single 2a is unremarkable, but a pattern of 2a scores in a specific modality warrants targeted intervention.
