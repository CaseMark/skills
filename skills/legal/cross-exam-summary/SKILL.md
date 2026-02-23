---
name: cross-exam-summary
description: Generates a structured cross-examination summary from depositions, exhibits, and discovery to identify impeachment points, inconsistencies, admissions, and strategic opportunities organized by witness and theme with precise citations. Use when preparing for trial cross-examination, deposition analysis, witness impeachment planning, or courtroom reference sheets in commercial litigation.
tags:
  - analysis
  - litigation
  - summarization
  - summary
---

# Cross-Examination Key Points Summary

Produces an actionable cross-examination reference organized by witness and theme, with precise citations for courtroom use.

## Prerequisites

1. **Depositions and transcripts** — all witness depositions with page/line numbers available
2. **Exhibits** — documents, emails, contracts, and physical evidence referenced in testimony
3. **Discovery responses** — interrogatory answers, RFAs, and document production
4. **Witness list** — anticipated opposing witnesses for trial
5. **Case theory** — client's legal theory and key elements to prove/defend

## Output Structure

### 1. Quick-Reference Table (Top of Document)

| Witness | Top Impeachment Point | Source | Theme |
|---------|----------------------|--------|-------|
| {Name} | {One-line summary} | {Doc:page:line} | {Theme} |

List the 2-3 highest-impact points per witness.

### 2. Per-Witness Sections

For each witness, organize by **theme** (not chronology):

```
## [Witness Name] — [Role/Relationship to Case]

### Theme: [e.g., "Knowledge of Defect"]

**Strategic Purpose:** [Impeachment | Favorable Admission | Foundation for Exclusion | Element Proof]

- **Point:** {Concise statement of the cross-exam point}
  - **Prior Statement:** "{Exact quote}" — [Deposition, p.XX:LL-LL]
  - **Contradicting Evidence:** "{Quote or exhibit description}" — [Exhibit XX]
  - **Suggested Q Line:** {Leading question sequence}
  - **Objection Risk:** {Likely objection + response/exception}
  - **Evasion Prep:** {Anticipated dodge + follow-up to close escape}
```

### 3. Point Categories

Tag each point with its function:

| Tag | Purpose |
|-----|---------|
| `IMPEACH` | Prior inconsistent statement (FRE 613) |
| `ADMIT` | Elicit favorable admission |
| `FOUNDATION` | Establish/undermine foundation for testimony |
| `CREDIBILITY` | Bias, interest, motive, perception, memory |
| `ELEMENT` | Directly proves/negates a claim element |
| `EXPERT` | Challenge methodology, assumptions, qualifications |

### 4. Expert Witness Sections

For experts, additionally address:
- Challenges to methodology (Daubert/Frye factors)
- Factual assumptions that are unsupported or contradicted
- Qualification gaps relevant to opinions offered
- Prior inconsistent opinions in other cases
- Reliance on incomplete or inaccurate data

### 5. Exhibit Cross-Reference Table

| Exhibit # | Description | Witnesses Referencing | Key Contradiction |
|-----------|-------------|----------------------|-------------------|
| {Ex. #} | {Brief desc} | {Names + cite} | {What it undermines} |

## Guidelines

- **Citation format:** Always use `[Document Name, p.XX:LL-LL]` — every point must have a pinpoint cite
- **Sequence points strategically:** Lead with control questions, build to the impeachment payoff
- **Side-by-side contradictions:** When a witness's statements conflict across depositions or with documents, present both quotes together with full citations
- **Leading questions only:** All suggested question lines must be leading (answerable yes/no)
- **Flag hearsay paths:** Note when a line of questioning may open the door to otherwise inadmissible evidence
- **Lay vs. expert tone:** Adjust complexity — simple concrete questions for lay witnesses, technical precision for experts
- **Do not fabricate testimony:** Only include statements actually found in provided materials
- **Jurisdiction note:** Impeachment rules vary by jurisdiction; flag any state-specific procedural requirements (e.g., "Queen Caroline's Rule" states requiring foundation before extrinsic evidence)
