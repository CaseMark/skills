---
name: deposition-summary-page-line
description: Generates structured page-line deposition summaries from U.S. litigation transcripts, preserving exact page-and-line citations for key testimony, objections, exhibits, admissions, and inconsistencies. Produces PDF (searchable, bookmarked) and DOCX (annotatable) outputs optimized for motion practice, trial preparation, and impeachment. Supports post-delivery Q&A with citation-anchored responses. Use when summarizing deposition transcripts, preparing cross-examination outlines, identifying impeachment material, or building evidentiary records during discovery.
tags:
  - litigation
  - summarization
  - summary
---

# Deposition Summary — Page-Line Format

Transforms deposition transcripts into citation-anchored litigation tools with strategic flagging for admissions, inconsistencies, objections, and exhibits.

## Prerequisites

1. **Deposition transcript** — complete, with page and line numbers intact
2. **Matter context** *(optional)* — claims/defenses at issue, other depositions in the matter, key disputed facts
3. **Priority topics** *(optional)* — legal theories or factual disputes to emphasize

## Output Structure

### Phase 1 — Summary Document (deliver both formats)

| Format | Requirements |
|--------|-------------|
| **PDF** | Fully searchable; bookmarks for each major topic section |
| **DOCX** | Formatted for annotation; integrates into trial notebooks and case chronologies |

### Summary Sections

Each section uses **Page X, Lines Y–Z** citation format throughout.

| Section | Content |
|---------|---------|
| **Witness & Proceeding Header** | Name, date, matter, counsel present, court reporter |
| **Topical Testimony** | Organized by legal issue (not chronologically); all substantive statements cited |
| **Admissions** | Flagged statements establishing elements of claims or defenses |
| **Inconsistencies** | Side-by-side citations where testimony shifted, contradicted itself, or conflicted with referenced documents |
| **Evasion / Hedging** | Instances of non-responsive, equivocal, or certainty-shifted answers |
| **Objections Log** | Each objection with: grounds stated, ruling/outcome, whether answer was given |
| **Exhibits Referenced** | Exhibit ID, description, page-line of introduction, follow-up needed flag |
| **Timeline Entries** | Dates/events extracted; cross-referenced for internal inconsistency |

### Flagging Conventions

- `[ADMISSION]` — concedes element of claim or defense
- `[INCONSISTENT]` — conflicts with earlier testimony (cite both locations)
- `[CONFLICT-EXT]` — conflicts with documentary evidence or other deposition testimony
- `[EVASIVE]` — non-responsive or materially hedged answer
- `[EXHIBIT]` — document introduced or referenced
- `[FOLLOW-UP]` — gaps requiring additional discovery

---

### Phase 2 — Post-Delivery Q&A Mode

After delivering summary documents, respond to attorney queries with citation-supported analysis.

**Query types and handling:**

| Query Type | Example | Response Approach |
|------------|---------|-------------------|
| Factual retrieval | "What did the witness say about the contract signing?" | Provide all relevant testimony with exact citations |
| Comparative | "How does their account of the meeting differ from their earlier answer?" | Side-by-side citations with narrative of how testimony evolved |
| Evaluative | "Does this support our statute of limitations defense?" | Surface all relevant testimony with citations; note ambiguities; do not render legal conclusions |
| Impeachment | "What can we use to attack credibility on damages?" | Compile inconsistencies, hedging, and `[CONFLICT-EXT]` flags with citations |

Every answer must include **Page X, Lines Y–Z** references. If testimony on a topic spans multiple transcript locations, provide all citations and explain how the statements relate.

## Guidelines

- **Accuracy is paramount** — a wrong page-line citation wastes courtroom time and damages credibility; when uncertain, say so explicitly rather than guessing
- **Topical over chronological** — organize by legal issue, not questioning order
- **No legal conclusions** — present testimony and flag ambiguities; attorney assessment controls
- **Work product handling** — summaries may be shared across litigation teams, used in motions, and relied upon at trial; treat accordingly
- **Incomplete transcripts** — flag missing pages, inaudible markers, or formatting anomalies before delivering summary
- **Multi-deposition matters** — when prior depositions are available, cross-reference `[CONFLICT-EXT]` flags against them
- **Jurisdiction**: U.S. federal and state civil litigation; no jurisdiction-specific procedural rules applied unless specified
