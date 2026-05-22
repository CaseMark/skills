---
name: habeas-style-citation-synthesis
language: en
description: >-
  Produces paragraph-level cited legal analysis grounded in primary
  sources (case law, legislation, regulations). Use when the user needs
  research with pinpoint citations, extracted passages, and source-level
  verification — similar to Habeas.ai's approach. Trigger keywords:
  cited legal analysis, paragraph citation, pinpoint citation, primary
  source research, legislation citation, case law synthesis with quotes.
tags:
  - research
  - analysis
  - litigation
---

# Cited Legal Synthesis (Habeas-Style)

Generates legally-grounded analysis with paragraph-level citations to
primary sources, enabling source verification and reducing hallucination risk.

## Prerequisites
- Defined legal question or issue
- Jurisdiction scope (state, federal, specific country)
- Preferred primary sources (case law, statutes, regulations)

## Workflow
1. **Question Framing** — Convert the user's legal question into a
  searchable query spanning cases, statutes, and regulations.
2. **Primary Source Retrieval** — Pull relevant authorities with
  full-text excerpts, citing specific sections and paragraphs.
3. **Holding Extraction** — For each case, extract the specific
  holding, reasoning, and any dicta that bears on the question.
4. **Citation-Linked Synthesis** — Compose the analysis with inline
  citations to paragraph-level passages, allowing the reader to
  verify every claim against the source.
5. **Conflicting Authority Check** — Identify and surface any
  contradictory cases or overruled precedents.
6. **Verify Extracts** — Confirm that quoted text matches the source
  document exactly. Flag any passages where the AI cannot verify.

## Pitfalls
- Never fabricate citations or page/paragraph numbers.
- Do not paraphrase holdings without quoting the source language.
- If a question requires jurisdiction-specific rules not in scope,
  state the limitation clearly.
- Distinguish between binding and persuasive authority explicitly.
