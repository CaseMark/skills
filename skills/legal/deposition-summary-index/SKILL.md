---
name: deposition-summary-index
description: >-
  Creates concise, neutral summaries of U.S. deposition transcripts for
  commercial litigation and links each topic to exhibit and transcript
  page/line citations for fast navigation. Use when a user provides a
  deposition transcript and requests a deposition digest, witness review,
  cross-examination prep, exhibit index, or discovery-analysis packet. Trigger
  terms: deposition transcript, witness summary, exhibit index, transcript
  cite, page-line reference, document link, discovery preparation, deposition
  analysis.
tags:
  - analysis
  - litigation
  - summarization
  - summary
---

# Deposition Summary with Key Document Index

Produces a topic-based deposition summary with mapped exhibit evidence for rapid review and litigation use.

## Prerequisites

1. Complete deposition transcript with stable page and line numbers.
2. Exhibit register with IDs, filenames, and any privilege/redaction labels.
3. Verified witness identifier and reporter formatting conventions (Q/A labels, speaker names).
4. Matter context: jurisdiction, governing procedural rules, and target deliverable format (DOCX/PDF).
5. Explicit instruction on redaction scope, confidentiality controls, and distribution limits.

## Output Structure / Process

1. Validate inputs and normalize identifiers.
- Canonicalize exhibit IDs (e.g., `Exh. 1`, `DEF. EXH. 2`, `PX-3`) to one consistent form.
- Extract transcript range boundaries, witness name, counsel speakers, and any objections/sidebars.
- Merge duplicate or split exhibit references (e.g., informal mentions like “the invoice” to formal exhibit ID).

2. Segment transcript into topic blocks.
- Define topic boundaries by explicit question shifts or sustained thematic changes.
- Keep topic labels plain and specific.
- Draft each topic summary in exactly 2–3 neutral sentences capturing facts, dates, actions, and uncertainties.

3. Build the topic summary table.
- Use a two-column source mapping approach: transcript span on the left, narrative on the right.
- Attach only evidence-based links to exhibits and transcript anchors.

Template to generate:

```markdown
| Topic | Transcript Span | Summary (2-3 sentences, neutral) | Linked Exhibits/Anchors |
|---|---|---|---|
| Contract negotiation and execution | 12:1-14:22 | ... | [Exh. 3], [12:18-12:30] |
| Billing disputes and payment practice | 31:4-38:10 | ... | [Exh. 8], [33:14-33:40] |
```

4. Build the key document index table.
- Include every exhibit mentioned, with exact transcript cites and how the witness described it.
- Flag authentication gaps, hearsay concerns, missing metadata, and contradiction risks.

Template to generate:

```markdown
| Exhibit ID | Transcript Mentions | Witness Characterization | Substance Attributed | Risk Notes |
|---|---|---|---|---|
| Exh. 3 | 12:10, 12:19-12:24 | “Contract signed by [witness] on [date].” | Supports formation details and parties’ signatures | [VERIFY] date ambiguity |
```

5. Produce final artifacts.
- Export identical-content DOCX and PDF deliverables.
- Preserve clickable anchors for both exhibit files and page/line citations.
- Maintain professional heading hierarchy and consistent spacing for direct filing/review use.

6. Run completion checks.
- Confirm all transcript exhibit references appear in the index.
- Verify no index item references exhibits absent from transcript.
- Verify all page/line spans and exhibit links are accurate and functional.
- Remove or isolate privileged/sealed content per instruction.

## Guidelines

1. Stay strictly neutral; do not add legal conclusions, argument, or advocacy language.
2. Do not infer intent, motive, or legal duty unless explicitly admitted on the record.
3. If source text is unclear, mark with `[VERIFY]` and do not over-interpret.
4. Keep testimony paraphrase faithful; avoid rhetorical language and avoid combining unrelated statements.
5. For US filings, preserve citation style consistent with counsel preferences unless told otherwise.
6. Escalate immediately if privilege logs, sealing orders, or confidentiality instructions are missing before final output.
