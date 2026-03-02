---
name: drafting-clinical-notes
description: Generates clinical documentation in SOAP, DAP, or narrative formats from encounter data with specialty-appropriate terminology and structure. Use when drafting progress notes, encounter documentation, or clinical visit summaries.
tags:
  - drafting
  - clinical
  - documentation
metadata:
  author: casemark
  practice_areas:
    - General Practice
    - Specialty Medicine
  document_types:
    - SOAP Note
    - H&P
    - Progress Note
  skill_modes:
    - Drafting
---

# Drafting Clinical Notes

Produces specialty-appropriate clinical documentation.

## Workflow

1. **Select** note format based on context (SOAP, DAP, H&P, procedure note)
2. **Structure** encounter data into appropriate sections
3. **Apply** specialty conventions (orthopedic exam terminology differs from psychiatric)
4. **Include** required billing elements (HPI elements, exam components, MDM complexity)
5. **Review** for completeness against documentation requirements

## Formats

### SOAP Note
```
**S (Subjective)**: Patient-reported symptoms, history
**O (Objective)**: Exam findings, vitals, lab results
**A (Assessment)**: Diagnoses with clinical reasoning
**P (Plan)**: Treatment, orders, follow-up
```

### H&P Format
```
**CC**: Chief complaint
**HPI**: History of present illness (8 elements)
**ROS**: Review of systems
**PMH/PSH/FH/SH**: Past medical, surgical, family, social
**Exam**: Physical examination by system
**Assessment & Plan**: Problem-based A/P
```

## Key Rules

- HPI must include: location, quality, severity, duration, timing, context, modifying factors, associated signs/symptoms
- Use precise medical terminology but define unusual abbreviations
- Assessment should link findings to diagnoses logically
- Plan must be specific: drug names with doses, not "start antibiotic"
- Always include follow-up timeframe
- Flag any documentation that would not support the billed E/M level

For specialty-specific templates, see [references/NOTE-TEMPLATES.md](references/NOTE-TEMPLATES.md).
