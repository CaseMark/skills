---
name: condensing-patient-histories
description: Condenses multi-year electronic health record notes into longitudinal patient narratives with organized problem lists, surgical history, and treatment progression. Use when reviewing complex patient charts, preparing for specialist consultations, or creating patient timeline summaries.
tags:
  - summarization
  - clinical
  - ehr
metadata:
  author: casemark
  practice_areas:
    - General Practice
    - Internal Medicine
  document_types:
    - Patient History
    - EHR Notes
  skill_modes:
    - Summarization
    - Synthesis
---

# Condensing Patient Histories

Produces navigable longitudinal summaries from extensive medical records.

## Workflow

1. **Scan** all notes chronologically — identify distinct episodes of care
2. **Build** problem list — active, resolved, chronic conditions with onset dates
3. **Track** treatment progression — what was tried, response, why changed
4. **Compile** surgical/procedural history with dates
5. **Summarize** current state — active problems, current medications, pending workup

## Output Template

```markdown
## Longitudinal Patient Summary

### Demographics
[Age, sex, relevant social history]

### Active Problem List
| Problem | Onset | Status | Current Management |
|---------|-------|--------|--------------------|

### Resolved/Historical Problems
| Problem | Period | Resolution |
|---------|--------|------------|

### Surgical/Procedural History
| Procedure | Date | Outcome |
|-----------|------|---------|

### Treatment Timeline
[Chronological narrative of major treatment decisions and responses]

### Current Medications
[Reconciled current list]

### Pending/Upcoming
- [Upcoming tests, referrals, procedures]
```

## Key Rules

- Organize by clinical significance, not just chronology
- Distinguish between confirmed diagnoses and "rule out" assessments
- Track medication changes with reasons when documented
- Note gaps in care (periods without visits)
- Flag inconsistencies across provider notes
