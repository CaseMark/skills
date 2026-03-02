---
name: abstracting-medical-records
description: Abstracts bulk medical records into chronological case summaries for litigation review, disability evaluation, or quality assessment. Use when preparing medical chronologies, case abstracts for attorneys, or clinical audit summaries.
tags:
  - abstraction
  - medical-records
  - chronology
metadata:
  author: casemark
  practice_areas:
    - Medical-Legal
    - Quality Assurance
  document_types:
    - Medical Records
    - Case Abstract
  skill_modes:
    - Abstraction
    - Summarization
---

# Abstracting Medical Records

Produces structured medical chronologies from voluminous records.

## Workflow

1. **Index** all documents — type, date, provider, facility
2. **Sort** chronologically
3. **Abstract** each encounter — date, provider, chief complaint, key findings, assessment, plan
4. **Cross-reference** — link related encounters, test results to ordering notes
5. **Flag** — gaps in records, inconsistencies, critical events
6. **Summarize** — executive summary with key events timeline

## Output Template

```markdown
## Medical Record Abstract

### Record Inventory
| Document Type | Date Range | Pages | Provider/Facility |
|--------------|-----------|-------|-------------------|

### Chronological Abstract

#### [Date] — [Provider] — [Facility]
**Type**: [Visit type]
**Chief Complaint**: [CC]
**Key Findings**: [Relevant exam/test findings]
**Assessment**: [Diagnosis/impression]
**Plan**: [Treatment decisions]

[Repeat for each encounter]

### Key Events Timeline
- [Date]: [Critical event — injury, surgery, diagnosis change, etc.]

### Record Gaps
- [Missing period or expected-but-absent documents]

### Inconsistencies Noted
- [Conflicting information across records]
```

## Key Rules

- Attribute every statement to its source document and page
- Do not interpret — abstract what is stated
- Note illegible portions rather than guessing
- Distinguish between patient-reported history and provider findings
- Flag any records that appear out of order or potentially misfiled

For medical-legal abstracting conventions, see [references/ABSTRACTING-GUIDE.md](references/ABSTRACTING-GUIDE.md).
