---
name: summarizing-pathology-reports
description: Structures pathology and biopsy reports into organized diagnosis, staging, margins, and biomarker summaries with standardized oncology reporting elements. Use when processing surgical pathology, cytology, or molecular pathology reports.
tags:
  - summarization
  - pathology
  - oncology
metadata:
  author: casemark
  practice_areas:
    - Pathology
    - Oncology
  document_types:
    - Pathology Report
  skill_modes:
    - Summarization
---

# Summarizing Pathology Reports

Extracts structured oncology and diagnostic data from pathology reports.

## Workflow

1. **Identify** specimen type and procedure
2. **Extract** diagnosis with histologic type and grade
3. **Stage** using TNM or appropriate system if stated
4. **Document** margins, lymphovascular invasion, perineural invasion
5. **Capture** biomarkers and molecular results (ER/PR, HER2, Ki-67, PD-L1, MSI, etc.)
6. **Note** synoptic vs. narrative format; extract synoptic fields if present

## Output Template

```markdown
## Pathology Summary

### Specimen
[Type, site, procedure]

### Diagnosis
[Histologic type, grade]

### Staging (if applicable)
- **T**: [Tumor size/extent]
- **N**: [Node status]
- **M**: [Metastasis]
- **Stage Group**: [Overall stage]

### Margins
| Margin | Status | Distance |
|--------|--------|----------|

### Prognostic Markers
| Marker | Result | Method |
|--------|--------|--------|

### Additional Findings
[Incidental findings, comments]
```

## Key Rules

- Preserve exact staging nomenclature (pT2N1M0, not "stage 2")
- Report margin distances in mm as stated
- Never infer staging components not explicitly stated
- Distinguish between immunohistochemistry and molecular/genomic testing
- Flag any "pending" or "addendum to follow" results
