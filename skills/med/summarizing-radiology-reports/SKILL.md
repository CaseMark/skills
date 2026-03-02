---
name: summarizing-radiology-reports
description: Structures radiology report text into organized findings, impressions, and follow-up recommendations with standardized severity indicators. Use when processing imaging reports, creating clinical summaries, or triaging radiology findings.
tags:
  - summarization
  - radiology
  - imaging
metadata:
  author: casemark
  practice_areas:
    - Radiology
    - Diagnostic Imaging
  document_types:
    - Radiology Report
  skill_modes:
    - Summarization
---

# Summarizing Radiology Reports

Extracts structured data from free-text radiology reports.

## Workflow

1. **Parse** report sections (clinical history, technique, findings, impression)
2. **Categorize** findings by anatomical region and severity
3. **Extract** measurements and comparisons to prior studies
4. **Identify** actionable recommendations (follow-up imaging, biopsy, clinical correlation)
5. **Flag** critical/urgent findings

## Output Template

```markdown
## Radiology Summary

### Study: [Modality] [Body Part] — [Date]
**Clinical Indication**: [Reason for study]

### Key Findings
| Finding | Location | Severity | Change from Prior |
|---------|----------|----------|-------------------|

### Measurements
| Structure/Lesion | Current | Prior | Change |
|-----------------|---------|-------|--------|

### Impression
[Verbatim or near-verbatim from report]

### Recommended Follow-Up
- [Action] — [Timeframe] — [Urgency]

### Critical Flags
- [Any urgent/emergent findings requiring immediate action]
```

## Key Rules

- Never reinterpret findings beyond what the radiologist stated
- Preserve exact measurements — do not round
- Distinguish "stable" from "unchanged" from "no prior for comparison"
- ACR BI-RADS, Lung-RADS, LI-RADS categories should be preserved exactly
- Flag any recommendation for tissue sampling or short-interval follow-up as high priority
