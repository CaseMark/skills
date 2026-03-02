---
name: extracting-study-endpoints
description: Extracts and structures clinical trial endpoints from publications including primary, secondary, and safety endpoints with statistical results. Use when building evidence tables, comparing trial outcomes, or preparing regulatory submissions.
tags:
  - extraction
  - clinical-trials
  - research
metadata:
  author: casemark
  practice_areas:
    - Clinical Research
    - Regulatory Affairs
  document_types:
    - Endpoint Extraction
  skill_modes:
    - Extraction
---

# Extracting Study Endpoints

Structures trial endpoint data from publications.

## Workflow

1. **Identify** study design and registration (NCT number)
2. **Extract** primary endpoint(s) — definition, timepoint, result
3. **Extract** secondary endpoints — same structure
4. **Extract** safety endpoints — adverse events, serious adverse events, discontinuations
5. **Note** statistical methods and pre-specified analysis plan
6. **Flag** any discrepancies between registered and reported endpoints

## Output Template

```markdown
## Endpoint Extraction: [Study Name / NCT#]

### Study Overview
| Field | Value |
|-------|-------|
| Design | [RCT, single-arm, etc.] |
| N | [Total enrolled / analyzed] |
| Duration | [Follow-up period] |
| Registration | [NCT number] |

### Primary Endpoint(s)
| Endpoint | Definition | Timepoint | Intervention | Control | Effect Size | 95% CI | p-value | Met? |
|----------|-----------|-----------|-------------|---------|-------------|--------|---------|------|

### Secondary Endpoints
[Same table format]

### Safety Summary
| Event | Intervention N (%) | Control N (%) | Notes |
|-------|-------------------|--------------|-------|

### Analysis Notes
- [ITT vs. per-protocol vs. modified ITT]
- [Handling of missing data]
- [Subgroup analyses]
- [Registered vs. reported endpoint discrepancies]
```

## Key Rules

- Always capture the NCT number for cross-referencing with clinicaltrials.gov
- Report effect sizes with CIs, not just p-values
- Note if the primary endpoint was changed from the registered version
- Distinguish ITT from per-protocol populations
- Safety data must include both rates and absolute numbers
- Flag any post-hoc analyses separately from pre-specified
