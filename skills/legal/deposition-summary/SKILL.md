---
name: deposition-summary
description: Generates topic-based deposition summaries for commercial litigation with integrated exhibit indexing, condensing transcript testimony into neutral 2-3 sentence overviews per topic in a two-column table (page:line | summary). Links each topic to referenced exhibits and key transcript citations. Use when summarizing depositions, creating deposition digests, indexing deposition exhibits, or preparing witness testimony summaries during discovery.
tags:
  - analysis
  - litigation
  - summarization
  - summary
---

# Deposition Summary with Key Document Index

Transforms a deposition transcript into a topic-based summary table with integrated exhibit cross-references, enabling rapid navigation between testimony and documentary evidence.

## Prerequisites

1. **Complete deposition transcript** — standard format with page and line numbering
2. **Exhibit list and files** — all exhibits referenced or marked during the deposition
3. **Case context** — party names, key contract sections, and claims at issue

## Process

### Step 1: Full Transcript Review

Read the entire transcript and identify:
- Natural topic breaks (explicit subject changes + subtle thematic shifts)
- Every exhibit reference — formal (by number/letter) and informal ("the email we just reviewed," "this invoice")
- Key admissions, contradictions, evasive answers, and authentication testimony

### Step 2: Topic Extraction

For each topic identified:

| Element | Requirement |
|---|---|
| **Topic heading** | Specific and descriptive — e.g., "Witness Knowledge of Payment Default Under Section 4.2" not "Payment Issues" |
| **Page:line range** | Start and end of testimony on that topic |
| **Summary** | 2-3 sentences, neutral, no legal conclusions |
| **Exhibits referenced** | Exhibit number + how witness characterized/authenticated it |
| **Notable moments** | Admissions, contradictions, refusals to answer |

### Step 3: Exhibit Index

Build a master exhibit cross-reference:

| Exhibit | Description | Transcript References (pg:ln) | Witness Characterization |
|---|---|---|---|
| Ex. 1 | [doc type] | 45:3-47:12, 102:8-103:1 | [how witness described/authenticated] |

### Step 4: Assemble Summary Table

Produce a two-column table as the primary deliverable:

```
| Transcript Cite | Topic & Summary |
|-----------------|-----------------|
| pp. 12:4-18:22  | **Formation of the Supply Agreement**
|                 | [2-3 sentence neutral summary]. See Ex. 3
|                 | (Supply Agreement, discussed at 14:8-15:2).
|                 | Notable: Witness admitted not reading §4.2
|                 | before signing (15:18-22). |
```

Within each summary cell:
- Embed references to exhibit files discussed
- Cite specific page:line for key admissions or important statements
- Use hierarchical headings for major topics vs. subtopics

### Step 5: Output Formats

Produce both:
1. **DOCX** — formatted table with functional hyperlinks to exhibits and transcript locations, editable styling
2. **PDF** — preserved hyperlinks, full-text searchable, locked format for filing/distribution

## Quality Checklist

- [ ] Every exhibit mentioned in testimony appears in the summary and exhibit index
- [ ] No exhibits referenced that weren't actually discussed
- [ ] All page:line citations verified against transcript
- [ ] Summaries reflect actual testimony — no interpretation or legal conclusions
- [ ] All hyperlinks resolve to correct targets (exhibits and transcript locations)
- [ ] Topic headings are specific enough for at-a-glance navigation
- [ ] No privileged communications, work product, or improperly redacted material included
- [ ] Consistent formatting: uniform heading hierarchy, font styling, spacing
- [ ] Grammar and spelling reviewed

## Guidelines

- **Neutral tone only** — summarize what the witness said, not what it means for the case
- **Specificity over brevity** — "Witness denied receiving the October 14 demand letter" not "Witness denied receiving correspondence"
- **Capture authentication testimony** — note when a witness identifies, authenticates, or disputes a document
- **Flag evasive responses** — mark where witness was non-responsive, claimed lack of memory, or gave qualified answers
- **Organize by substance, not by questioner** — if redirect revisits a topic from direct, consolidate under the same heading
- **Commercial litigation focus areas** — contract formation/interpretation, business communications, financial transactions, performance obligations, damages calculations
