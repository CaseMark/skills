---
name: prior-art-summary
description: Generates structured summaries of prior art references for patent prosecution, validity analysis, and freedom-to-operate assessments. Extracts publication dates, inventors, technical fields, key disclosures, and claim-element mappings with precise citations. Use when summarizing prior art, analyzing patent landscapes, mapping prior art to claims, or preparing office action responses.
tags:
  - analysis
  - litigation
  - summarization
  - summary
  - transactional
---

# Prior Art Summarization

Synthesizes multiple prior art references into a structured summary that maps disclosures to claim elements and enables rapid assessment of the prior art landscape.

## Prerequisites

1. **Prior art references** — patents, published applications, technical publications, product documentation, or other public disclosures
2. **Invention description** — claims or specification of the invention under analysis
3. **Scope directive** — prosecution support, validity/invalidity analysis, or FTO assessment

## Output Structure

### 1. Executive Overview

| Field | Content |
|-------|---------|
| Total references reviewed | Count |
| Most material references | Top 3-5 by relevance, with one-line rationale each |
| Key gaps in prior art | Claim elements with no or weak coverage |
| Art type breakdown | Patents / applications / publications / other |

### 2. Individual Reference Summaries

For each reference, provide:

| Field | Content |
|-------|---------|
| Document ID | Patent/pub number, DOI, or other identifier |
| Title | Full title |
| Date | Publication or issue date (note effective prior art date if different) |
| Inventor(s)/Author(s) | Names |
| Technical field | CPC/IPC classes if patent; subject domain if publication |
| Assignee/Publisher | Entity |

**Disclosure summary** — 2-4 sentences on the core technical contribution.

**Key features disclosed** — Bulleted list of specific components, methods, or systems relevant to the analysis. For each:
- Quote exact language from the reference
- Cite precise location (¶ number, col:line, page, figure)

**Limitations / gaps** — What the reference does NOT disclose relative to the invention.

### 3. Claim-Element Mapping Table

| Claim Element | Ref. 1 | Ref. 2 | Ref. 3 | ... |
|--------------|--------|--------|--------|-----|
| Element A | ¶[0032], Fig. 3 | — | p. 12 | |
| Element B | — | Col. 4:15-22 | — | |
| Element C | ¶[0045] | ¶[0018] | — | |

Use `✓` for full disclosure, `~` for partial, `—` for absent. Always include the citation location.

### 4. Combination Analysis

For each potentially obvious combination:
- **References combined** — identify which refs
- **Motivation to combine** — analogous art rationale, explicit suggestions, design incentives
- **Missing elements** — what remains undisclosed even in combination

### 5. Timeline

Chronological list of references by effective date, noting any critical date boundaries (priority date, filing date, publication date of application under review).

## Guidelines

- **Cite precisely**: Every factual assertion about a reference must include ¶, col:line, page, or figure number
- **No legal conclusions**: Do not state that claims are anticipated or obvious; organize facts so the attorney can reach those conclusions
- **Analogous art**: Flag references outside the immediate technical field with a note on why they may qualify as analogous art
- **Prior art status**: Note any references whose prior art qualification depends on date analysis (e.g., pre-AIA vs. AIA 35 U.S.C. § 102 categories) [VERIFY]
- **Foreign-language references**: Flag language, provide translated key passages, note if only machine-translated
- **Figures and drawings**: Describe relevant depicted features in enough detail to be useful without viewing the original
- **Technical terms**: Define specialized terminology on first use in brackets if the term is not standard legal vocabulary
- **Organize by relevance** to claim elements as default; use chronological order only if specifically requested or if the timeline itself is analytically significant
