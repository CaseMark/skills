---
name: analyzing-lab-results
description: Analyzes laboratory panel data to flag abnormal values, identify trends, and suggest differential considerations based on result patterns. Use when reviewing lab work, monitoring chronic conditions, or preparing lab result summaries for clinical review.
tags:
  - analysis
  - laboratory
  - diagnostics
metadata:
  author: casemark
  practice_areas:
    - Laboratory Medicine
    - Internal Medicine
  document_types:
    - Lab Panel
    - Lab Report
  skill_modes:
    - Analysis
---

# Analyzing Lab Results

Interprets lab panels with trend analysis and clinical correlation.

## Workflow

1. **Organize** results by panel type (CBC, BMP, CMP, LFTs, lipids, thyroid, coag, etc.)
2. **Flag** abnormals against standard reference ranges (note: ranges vary by lab)
3. **Trend** — compare to prior values if available; note direction and velocity
4. **Pattern** recognition — identify clinically meaningful combinations
5. **Suggest** differential considerations based on patterns (do NOT diagnose)

## Output Template

```markdown
## Lab Result Analysis

### Panel: [Panel Name] — [Date]

| Test | Result | Units | Reference Range | Flag | Trend |
|------|--------|-------|----------------|------|-------|

### Abnormal Values Summary
| Test | Value | Deviation | Clinical Significance |
|------|-------|-----------|----------------------|

### Trend Analysis (if prior results available)
| Test | [Date 1] | [Date 2] | [Date 3] | Direction |
|------|----------|----------|----------|-----------|

### Pattern Notes
- [Clinically relevant combinations observed]

### Considerations
- [Possible explanations — not diagnoses]
```

## Key Rules

- Always specify which reference range is being used
- Critical values (e.g., K+ >6.5, Na+ <120) must be flagged prominently
- Note hemolyzed/lipemic/icteric specimens if mentioned — affects results
- Don't diagnose — suggest "consistent with" or "consider"
- Age and sex affect reference ranges — adjust when known

For reference ranges by panel, see [references/LAB-REFERENCE-RANGES.md](references/LAB-REFERENCE-RANGES.md).
