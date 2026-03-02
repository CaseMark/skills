---
name: summarizing-discharge-notes
description: Transforms hospital discharge paperwork into structured patient summaries with medications, follow-up appointments, activity restrictions, and warning signs. Use when processing discharge documents, creating patient handoffs, or preparing transition-of-care summaries.
tags:
  - summarization
  - hospital-medicine
  - patient-care
metadata:
  author: casemark
  practice_areas:
    - Hospital Medicine
    - Internal Medicine
  document_types:
    - Summary Report
  skill_modes:
    - Summarization
---

# Summarizing Discharge Notes

Transforms hospital discharge paperwork into structured patient summaries with medications, follow-up appointments, activity restrictions, and warning signs.

## Workflow

1. **Collect** source documents and verify completeness
2. **Extract** key data points, findings, and structured elements
3. **Normalize** terminology and format for consistency
4. **Structure** output using the template below
5. **Validate** completeness against source material — flag gaps explicitly

## Key Rules

- Always verify source data completeness before beginning
- Flag assumptions explicitly — never present inferred data as confirmed
- Use consistent terminology throughout the output
- Note limitations and scope boundaries in the final output
- When in doubt about a data point, mark with [VERIFY] rather than guessing

## Guidelines

- This skill operates within the **Hospital Medicine** domain
- Relevant practice areas: Hospital Medicine, Internal Medicine
- Output should be actionable for domain professionals
- Include appropriate disclaimers for compliance-sensitive outputs
- Escalate to human review when confidence is low or stakes are high
