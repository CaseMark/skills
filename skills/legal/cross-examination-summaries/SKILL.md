---
name: cross-examination-summaries
description: Generates structured thematic cross-examination summaries from deposition transcripts, prior sworn statements, interrogatory responses, affidavits, and discovery materials. Highlights inconsistencies, contradictions, impeachable admissions, credibility weaknesses, and favorable concessions with precise page-and-line citations. Produces trial-ready reference documents organized for rapid courtroom use. Use when preparing to cross-examine a witness, building an impeachment strategy, or synthesizing testimony across multiple witnesses for trial.
tags:
  - analysis
  - litigation
  - summarization
  - summary
---

# Cross-Examination Summary

Transforms raw witness testimony and discovery materials into a trial-ready, thematically organized impeachment reference with precise citations.

## Prerequisites

1. **Deposition transcript(s)** — with page and line numbers intact
2. **Prior sworn statements** — affidavits, interrogatory responses, hearing testimony
3. **Informal statements** — emails, texts, recorded communications attributable to the witness
4. **Relevant exhibits** — documents, physical evidence, or other witness statements that contradict or corroborate
5. **Case theory summary** — client's narrative and key issues the examination must address

## Output Structure

### 1. Witness Profile (½ page)

| Field | Content |
|---|---|
| Name / Role | Relationship to parties, capacity (fact witness, expert, party) |
| Key Topics | Issues this witness covers |
| Credibility Flags | Bias, motive, prior convictions, interest in outcome |
| Examination Goal | Concessions to secure / narrative to establish / credibility to destroy |

---

### 2. Thematic Sections

Organize by **case issue**, not transcript chronology. For each theme:

```
## [Theme: e.g., "Knowledge of Defect / Notice"]

### Witness Position
[Concise paraphrase of witness's stated position on this issue]

### Key Testimony
> "[Exact quote]"
> — [Source], p. [X], ll. [Y–Z]

### Inconsistencies / Contradictions
- Prior statement: "[Quote]" — [Source], p. [X], ll. [Y–Z]
- Contradicting exhibit: [Ex. No.], [relevant portion]
- Other witness: [Name], [Source], p. [X], ll. [Y–Z]

### Favorable Concessions
- [Fact witness cannot dispute] — [Source], p. [X], ll. [Y–Z]

### Knowledge / Perception Gaps
- Lacks personal knowledge of [X] — [Source], p. [X], ll. [Y–Z]
- Testimony based on hearsay / assumption — [Source], p. [X], ll. [Y–Z]

### Impeachment Approach
[1–2 sentence tactic note: foundation required, suggested sequence, exhibit to use]
```

Repeat for each major theme (typically 4–8 sections).

---

### 3. Impeachment Priority Matrix

| Rank | Impeachment Opportunity | Source Citation | Exhibit | Impact |
|---|---|---|---|---|
| 1 | [Description] | [Doc, p/ll] | [Ex. No.] | High / Med / Low |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

---

### 4. Concessions Checklist

Facts to lock in early before confrontational impeachment:

- [ ] [Fact] — [Source], p. [X], ll. [Y–Z]
- [ ] [Fact] — [Source], p. [X], ll. [Y–Z]
- [ ] [Fact] — [Source], p. [X], ll. [Y–Z]

---

### 5. Exhibit Integration Map

| Exhibit | Relevant Portion | Testimony It Contradicts / Supports | When to Deploy |
|---|---|---|---|
| Ex. [#] | [Description] | [Source], p. [X], ll. [Y–Z] | [Theme / sequence] |

---

### 6. Cross-Witness Impeachment (if applicable)

Where this witness's testimony can be used to impeach others (or vice versa):

| This Witness | Conflicts With | Other Witness | Citation |
|---|---|---|---|
| "[Quote]" — [Source] | | [Name], [Source] | |

---

### 7. Strategic Overview

- **Examination sequence**: [Open with concessions → move to impeachment → close on [X]]
- **Top 3 moments**: [Identify the three highest-impact confrontations]
- **Witness control risks**: [Note if witness is evasive, volatile, or over-explains]
- **Narrative thread**: [One sentence connecting examination arc to case theory]

## Guidelines

- Cite every statement: document name, page number, line numbers — no paraphrased citations
- Use exact quotes for any testimony intended for impeachment at trial
- Flag evasive, rehearsed, or suspiciously precise answers in the theme section notes
- Do not characterize testimony argumentatively in the body — reserve advocacy for the Strategic Overview
- Verify all page/line citations before delivering; credibility of the summary depends on citation accuracy
- For multi-witness matters, generate one summary per witness; use Section 6 for cross-witness linkage
- US jurisdiction assumed; flag any state-specific impeachment rules (e.g., prior conviction admissibility under FRE 609 [VERIFY applicability in specific forum])
