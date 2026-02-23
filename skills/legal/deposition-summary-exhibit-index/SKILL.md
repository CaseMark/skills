---
name: deposition-summary-exhibit-index
description: Produces a topic-based U.S. deposition summary with precise page/line ranges and a keyed exhibit index linking testimony to documents. Neutral 2-3 sentence summaries per topic, plus exhibit references, authentication notes, and citation-ready transcript anchors. Use when creating a deposition summary, key document index, exhibit-linked transcript digest, or discovery testimony map in commercial litigation.
tags:
  - analysis
  - litigation
  - summarization
  - summary
---

# Deposition Summary with Exhibit Index

Create a concise, topic-based deposition summary with an integrated exhibit index tied to page/line citations.

## Prerequisites

1. Full deposition transcript with page/line numbering
2. Exhibit list with IDs/labels and filenames or Bates ranges
3. Access paths or links for exhibits (file paths or document IDs)
4. Any protective order or confidentiality designations
5. Parties, witness name/role, date, and caption block details

## Output Structure / Process

Use the following structure and templates.

**Cover Block**

- Caption (case name, court, case no.)
- Deposition witness name and role
- Date of deposition
- Deponent represented by
- Reporting service (if known)
- Prepared by, date prepared

**Topic Summary Table**

Use a two-column structure with topic headers and page/line ranges.

Table format:

| Page/Line Range | Topic Summary |
|---|---|
| p. 12:3–18:22 | **Topic: Formation of Master Services Agreement**. 2–3 sentence neutral summary. Include key admissions, denials, or qualifiers. Cite exact page/line for critical statements. Reference exhibits inline using IDs. |
| p. 19:1–24:6 | **Topic: Scope of Services and Deliverables**. 2–3 sentence neutral summary. Note any uncertainty, lack of knowledge, or evasive answers. Link to exhibits discussed. |

Rules for topic summaries:

- 2–3 sentences per topic, neutral tone
- No legal conclusions or argument
- Include page/line cites for critical admissions or contradictions
- Use descriptive, specific topic titles
- If a topic spans multiple subtopics, split into separate rows

Inline exhibit references (use the exact ID format):

- “Ex. 12 (Invoice 1043)” or “PX-12 (Invoice 1043)”
- If linking is possible, make the exhibit label the clickable text

**Exhibit Index**

Create a keyed index mapping each exhibit to testimony.

Table format:

| Exhibit | Description | Testimony Page/Line | Witness Characterization |
|---|---|---|---|
| Ex. 12 | Invoice 1043 dated 3/5/2023 | p. 45:2–46:20 | Identified as company invoice; witness states it reflects services rendered |

Rules for exhibit index:

- Include every exhibit mentioned in the transcript
- Provide all page/line references where the exhibit is discussed
- Summarize authentication or characterization in one sentence
- If an exhibit is referenced informally, map to the correct ID

**Key Admissions / Contradictions (Optional Section)**

If requested, provide a short list with exact citations.

Format:

- Admission: “Witness acknowledged no written approval existed for change order.” (p. 78:4–10)
- Contradiction: “Witness claimed no notice of default, later admitted receipt of 6/2/2023 email.” (p. 102:11–16; p. 148:3–9)

**Output Deliverables**

- DOCX with hyperlinks to exhibits and transcript anchors
- PDF with active hyperlinks and searchable text

If hyperlinks are not technically feasible, provide explicit file paths or document IDs in brackets after each reference.

## Guidelines

- Use neutral, fact-only summaries; no advocacy.
- Preserve exact page/line ranges; do not guess.
- Keep topics scoped; split when testimony shifts.
- Include every exhibit discussed; avoid adding unmentioned exhibits.
- Flag potential privilege or confidentiality issues; do not reproduce protected content.
- If transcript is incomplete or exhibits are missing, state the gap explicitly.
- Confirm compliance with any protective order or redaction protocol.
- Use `[VERIFY]` if any citation or exhibit ID is uncertain.
