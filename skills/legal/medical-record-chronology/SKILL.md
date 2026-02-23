---
name: medical-record-chronology
description: Creates detailed chronological summaries of medical records for litigation use. Extracts treatment timelines, provider information, diagnoses, procedures, medications, and causation-relevant findings. Identifies gaps, inconsistencies, and records needing follow-up. Use when analyzing medical records in personal injury, medical malpractice, or disability cases.
tags:
  - analysis
  - litigation
  - summarization
  - summary
---

# Medical Record Chronology

Creates a structured, chronological summary of medical records for litigation, extracting treatment details, causation evidence, and strategic insights.

## Output Structure

### Patient and Case Information

| Field | Details |
|-------|---------|
| Patient name | |
| DOB | |
| Date of incident | |
| Case type | PI / Med Mal / Workers Comp / Disability |
| Pre-existing conditions | |
| Claimed injuries | |

### Provider Index

| # | Provider/Facility | Type | Date Range | Records Obtained |
|---|------------------|------|-----------|-----------------|
| 1 | [Name] | [ER/PCP/Specialist/PT] | [First-Last visit] | Yes/Partial/No |

### Chronological Summary

For each encounter, in date order:

**[Date] — [Provider Name] — [Facility] — [Visit Type]**

- **Chief complaint**: Patient's stated reason for visit
- **History**: Relevant history documented (mechanism of injury, symptom onset)
- **Examination findings**: Objective findings (vitals, physical exam, neurological)
- **Diagnostic studies**: Imaging, labs, EMG/NCV results
- **Diagnosis/Assessment**: ICD codes and narrative diagnoses
- **Treatment**: Procedures performed, medications prescribed, referrals made
- **Restrictions/Limitations**: Work restrictions, activity limitations
- **Follow-up**: Next appointment, recommended further care
- **Causation language**: Any provider statements connecting injuries to incident *(flag prominently)*
- **Page/Bates reference**: [Source: Bates ### or Provider records p. ##]

### Pre-Incident Medical History

Chronological summary of relevant treatment before the incident:
- Same body parts/conditions
- Prior injuries or accidents
- Medications at time of incident
- Baseline functional status

### Treatment Timeline (Visual)

```
[Incident Date] → ER → PCP → Ortho → MRI → PT (12 sessions) → IME → Ortho F/U → Surgery → PT (24 sessions) → MMI
```

### Diagnostic Summary

| Date | Study | Facility | Findings | Significance |
|------|-------|----------|----------|-------------|
| | X-ray | | | |
| | MRI | | | |
| | CT | | | |
| | EMG/NCV | | | |

### Medication History

| Medication | Prescribed By | Start Date | End Date | Purpose |
|-----------|--------------|-----------|---------|---------|
| | | | | |

### Damages Summary

- Total medical expenses (by provider)
- Lost time from work (dates and documentation)
- Functional limitations documented
- Permanency/MMI status
- Future treatment recommendations

## Strategic Analysis

**Favorable findings**: Medical evidence supporting causation and damages
**Adverse findings**: Pre-existing conditions, gaps in treatment, inconsistent histories, non-compliance
**Gaps in records**: Missing provider records, unexplained treatment gaps, records to request
**Inconsistencies**: Conflicting histories given to different providers, discrepancies between records
**Follow-up needed**: Additional records to request, provider depositions to schedule, IME considerations

## Guidelines

- Maintain strict chronological order — interleave records from different providers by date
- Quote exact provider language for causation opinions (in quotation marks with page/Bates citation)
- Flag any mention of pre-existing conditions, prior injuries, or prior treatment to the same body part
- Note gaps in treatment — opposing counsel will argue gap = no injury
- Track medication changes — escalation may show worsening, discontinuation may show resolution
- Distinguish objective findings (imaging, measurements) from subjective complaints
- Note every instance of mechanism-of-injury description — inconsistencies are impeachment material
- Include both favorable and unfavorable entries — the attorney needs the complete picture
