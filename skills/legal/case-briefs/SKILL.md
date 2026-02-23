---
name: case-briefs
description: Generates structured case briefs from judicial opinions, extracting caption, procedural posture, facts, issues, holdings, reasoning, and significance. Use when the user provides a court opinion and needs a case brief, case summary for research, or a distillation of a judicial decision.
tags:
  - analysis
  - brief
  - corporate
  - litigation
  - regulatory
  - summarization
  - transactional
---

# Case Brief Generation

Produces a structured case brief from a judicial opinion or case reporter entry.

## Output Structure

```
1. Case Caption & Procedural Posture
   - Full case name, court, date, citation
   - How the case reached this court
   - Lower court decision and basis for review

2. Statement of Facts
   - Material facts chronologically
   - Distinguish background, operative, and procedural facts
   - Only facts the court deemed relevant

3. Legal Issues Presented
   - Frame as precise yes/no questions or standard-identification questions
   - One issue per entry

4. Holding & Disposition
   - Court's answer to each issue
   - Narrow holding vs. broader principles announced
   - Affirmed / reversed / remanded / other

5. Reasoning & Analysis
   - Doctrines, statutes, precedents relied upon
   - Analytical framework or test applied
   - Concurrences and dissents with key departures

6. Significance & Implications
   - New precedent, clarification, or notable application
   - Impact on future cases and practice
```

## Guidelines

- Use exact language from the opinion for legal standards, tests, and doctrines
- Mark direct quotations clearly
- Target 1-3 pages depending on complexity
- If the source is incomplete on any element, note the limitation rather than speculating
- For opinions addressing multiple issues, organize systematically with clear separation
- Maintain objective, analytical tone throughout
