---
name: summarizing-discharge-notes
description: Transforms hospital discharge paperwork into structured patient summaries with medications, follow-up appointments, activity restrictions, and warning signs. Use when processing discharge documents, creating patient handoffs, or preparing transition-of-care summaries.
tags:
  - summarization
  - clinical
metadata:
  author: casemark
  practice_areas:
    - Hospital Medicine
    - Primary Care
  document_types:
    - Discharge Summary
  skill_modes:
    - Summarization
---

# Summarizing Discharge Notes

Converts verbose discharge documentation into actionable, structured summaries.

## Workflow

1. **Extract** key sections from discharge note (diagnosis, procedures, medications, instructions)
2. **Normalize** medication list (generic names, dosages, frequencies, duration)
3. **Structure** follow-up requirements (provider, timeframe, purpose)
4. **Flag** critical items (new medications, activity restrictions, red-flag symptoms)
5. **Validate** completeness against discharge summary checklist

## Output Template

```markdown
## Patient Discharge Summary

### Primary Diagnosis
[Diagnosis with ICD-10 if available]

### Procedures Performed
- [Procedure] — [Date]

### Discharge Medications
| Medication | Dose | Frequency | Duration | New/Changed? |
|-----------|------|-----------|----------|--------------|

### Follow-Up Schedule
| Provider | Timeframe | Purpose |
|----------|-----------|---------|

### Activity Restrictions
- [Restriction] — [Duration]

### Red-Flag Symptoms (Seek Immediate Care)
- [Symptom]

### Patient Education Points
- [Key instruction]
```

## Key Rules

- Always distinguish NEW medications from CONTINUED medications
- Flag any medication changes (dose adjustments, discontinuations)
- If discharge note is missing expected sections, note the gap explicitly
- Never infer diagnoses not stated in the source document
- Include "return to ED if..." criteria verbatim when present

## Common Pitfalls

- Confusing admission medications with discharge medications
- Missing conditional instructions ("if pain persists after 48 hours...")
- Dropping PRN medications from the list

For detailed discharge format variations (VA, academic, community), see [references/DISCHARGE-FORMATS.md](references/DISCHARGE-FORMATS.md).
