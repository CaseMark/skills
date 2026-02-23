---
name: deposition-summarization
description: Summarizes deposition transcripts with precise page-line citations. Supports page-line summary format, deep analysis with strategic assessment, and topic-based summaries with document index. Use when the user provides a deposition transcript and needs a deposition summary, depo digest, testimony analysis, or impeachment identification.
tags:
  - analysis
  - litigation
  - summarization
  - summary
---

# Deposition Summarization

Produces deposition summaries with precise page:line citations from transcript source material.

## Output Formats

Choose based on the user's needs (default to Format A if unspecified):

### Format A: Page-Line Summary

Sequential summary preserving transcript order. Each entry includes the page:line range and a neutral summary of the testimony.

```
pp. 12:3-14:8 — Deponent described the sequence of events on March 15,
stating he arrived at the facility at approximately 8:30 AM and met with
[Name] in the conference room. [Ex. 3 marked and identified.]

pp. 14:9-16:22 — On cross-examination regarding prior statements, deponent
acknowledged signing the memorandum (Ex. 4) but stated he did not read it
before signing.
```

### Format B: Topic-Based Summary

Organizes testimony by subject matter rather than transcript order. Each topic gets a 2-3 sentence neutral summary with page:line citations.

```
## Employment History
Deponent worked at [Company] from 2018 to 2022 as Senior VP of Operations
(pp. 8:12-9:4). He reported directly to the CEO and supervised a team of
12 (pp. 9:15-10:8).

## Knowledge of Transaction
Deponent first learned of the proposed acquisition in January 2022 (pp.
22:3-22:18). He attended three board meetings where the transaction was
discussed (pp. 23:1-25:14, pp. 31:8-33:2, pp. 45:6-47:11).
```

### Format C: Deep Analysis (Strategic)

Includes everything in Format A or B, plus:

**Admissions Against Interest**: Testimony that hurts the deponent's party's position, with exact quotes and citations.

**Inconsistencies**: Contradictions within the deposition, between this deposition and other testimony, or between testimony and documentary evidence.

**Impeachment Opportunities**: Prior inconsistent statements, basis for bias, lack of personal knowledge.

**Key Exhibits**: Table of exhibits marked, identified, or discussed:

| Exhibit | Description | Pages Discussed | Authenticated? |
|---------|-------------|----------------|---------------|
| Ex. 1 | [Description] | pp. 15:3-17:8 | Yes — pp. 15:10 |

**Credibility Assessment**: Evasive answers, non-responsive testimony, frequent "I don't recall" responses (with count and page ranges).

## Guidelines

- Always cite page:line ranges — never summarize without citation
- Use neutral, objective language in summaries (save analysis for Format C sections)
- Preserve exact quotes for admissions and key testimony — use quotation marks
- Note all objections and their basis
- Flag designations (Confidential, AEO) if present
- Note stipulations made on the record
- If exhibits are referenced but not provided, note: "[Exhibit not provided for review]"
