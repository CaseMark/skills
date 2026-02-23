---
name: shareholder-meeting-summary
description: Generates structured summaries of shareholder meetings from minutes, transcripts, presentations, and related materials. Captures metadata, agenda items, resolutions, voting outcomes, and dissents for official corporate records. Use for minute books, regulatory filings, governance compliance, annual meeting summaries, or special meeting documentation.
tags:
  - corporate
  - summarization
  - summary
---

# Shareholder Meeting Summary

Produces a structured, record-quality summary of a shareholder meeting suitable for minute books, SEC filings, and governance compliance.

## Prerequisites

1. **Meeting materials** — minutes, transcripts, audio/video recordings, presentation decks, or related correspondence
2. **Corporate context** — company legal name, jurisdiction of incorporation, relevant bylaw provisions (especially quorum and voting thresholds)

## Output Structure

### 1. Meeting Metadata

| Field | Content |
|---|---|
| Corporation | Full legal name |
| Meeting type | Annual / Special (state purpose if special) |
| Date & time | Start time; adjournment time |
| Location | Physical address or virtual platform |
| Presiding officer | Name and title |
| Secretary / recorder | Name and title |
| Quorum | Present shares vs. required threshold; method of determination |

**Attendance table:**

| Name | Role | Shares Represented | Present / Proxy |
|---|---|---|---|

### 2. Agenda Items

For each agenda item, in sequence:

- **Item number and title**
- **Substance** — what was proposed or presented
- **Material discussion** — key arguments for/against (factual, not editorialized)
- **Management recommendation** (if shareholder proposal)
- **Resolution text** — full operative language for adopted resolutions
- **Voting results:**

| For | Against | Abstain | Broker Non-Votes | Method | Result |
|---|---|---|---|---|---|

### 3. Special Documentation

Capture if present:

- [ ] Dissenting shareholder statements (verbatim or detailed summary)
- [ ] Exercise of appraisal rights
- [ ] Demands for record inspection
- [ ] Fiduciary duty concerns raised
- [ ] Procedural irregularities or challenges
- [ ] Contested elections

### 4. Closing

- Other business conducted
- Announcements (future meetings, corporate actions)
- Time of adjournment

## Guidelines

- **Neutral tone** — document what was said and decided; do not characterize discussions as "heated" or "contentious" unless the official minutes use those terms
- **Precision on votes** — verify all vote counts and percentages; attribute each tally to its specific resolution
- **Flag gaps** — if materials omit exact vote counts or other details, note the limitation explicitly rather than assuming
- **High-scrutiny items** — apply extra care to votes on mergers, charter/bylaw amendments, director elections, executive compensation, and related-party transactions
- **No editorial commentary** — report procedural irregularities and objections objectively
- **Consistent format** — use tabular presentation for all voting results
