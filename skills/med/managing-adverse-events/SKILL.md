---
name: managing-adverse-events
description: Structures adverse event reports with causality assessment, severity grading, and regulatory reporting requirements using MedWatch and CIOMS formats. Use when documenting adverse drug reactions, preparing safety reports, or assessing adverse event causality.
tags:
  - compliance
  - pharmacovigilance
  - safety
metadata:
  author: casemark
  practice_areas:
    - Pharmacovigilance
    - Regulatory Affairs
  document_types:
    - Adverse Event Report
    - MedWatch
  skill_modes:
    - Assessment
    - Reporting
---

# Managing Adverse Events

Produces structured AE reports with regulatory compliance.

## Workflow

1. **Document** the event — description, onset, duration, outcome
2. **Assess** severity — CTCAE grading (Grade 1-5) or other scale
3. **Assess** causality — Naranjo algorithm or WHO-UMC system
4. **Determine** expectedness — listed in product labeling?
5. **Classify** reporting requirements — expedited vs. periodic
6. **Prepare** report — MedWatch (FDA) or CIOMS form (international)

## Output Template

```markdown
## Adverse Event Report

### Event Details
| Field | Value |
|-------|-------|
| Event term (MedDRA preferred) | [Term] |
| Onset date | [Date] |
| Severity grade | [CTCAE Grade 1-5] |
| Serious? | [Yes/No — criteria met] |
| Outcome | [Resolved/Ongoing/Fatal/etc.] |

### Suspect Product
| Product | Dose | Route | Start Date | Action Taken |
|---------|------|-------|-----------|-------------|

### Causality Assessment (Naranjo)
| Question | Score |
|----------|-------|
| Previous reports? | [+1/0/-1] |
| Event after drug? | [+2/+1/0] |
| Improved on withdrawal? | [+1/0] |
| Reappeared on rechallenge? | [+2/+1/0/-1] |
| Alternative causes excluded? | [-1/+1/+2] |
| Confirmed by objective evidence? | [+1/0] |
| **Total** | **[Score]** |
| **Classification** | [Definite/Probable/Possible/Doubtful] |

### Seriousness Criteria (check all that apply)
- [ ] Death
- [ ] Life-threatening
- [ ] Hospitalization (initial or prolonged)
- [ ] Disability/incapacity
- [ ] Congenital anomaly
- [ ] Medically important event

### Reporting Timeline
| Report Type | Deadline | Status |
|------------|---------|--------|
```

## Key Rules

- Serious + unexpected = expedited reporting (15 calendar days, 7 for fatal/life-threatening)
- Use MedDRA preferred terms for consistent coding
- Naranjo score: ≥9 Definite, 5-8 Probable, 1-4 Possible, ≤0 Doubtful
- "Serious" has a regulatory definition — not the same as "severe"
- Document the reporter's assessment AND the sponsor's assessment separately
- Concomitant medications and medical history affect causality assessment
