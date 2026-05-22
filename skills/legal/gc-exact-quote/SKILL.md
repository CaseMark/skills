---
name: GC Exact Quote Legal
description: Verifiable legal citation extraction with character-level precision and source tracing
tags:
  practice_area: [litigation, regulatory, corporate]
  document_type: [brief, memo, pleading]
  skill_mode: [analysis, research]
---

# GC Exact Quote Legal

Extract verifiable, character-precise legal citations from case law, statutes, regulations, and contractual provisions with full source traceability.

## Prerequisites

- Primary legal authority database access (Westlaw, Lexis, PACER, government gazettes)
- Document OCR or structured text for uploaded materials
- SOC 2 Type II data isolation for confidential documents

## Workflow

1. **Query parsing**: Identify the specific legal proposition or quote being sought from natural language input
2. **Source search**: Retrieve relevant primary authority using exact-quote search across case databases, statutes, and regulations
3. **Character-level extraction**: Extract the precise verbatim text including punctuation, parentheticals, and footnote references
4. **Citation verification**: Cross-check extracted text against original source to confirm character-level accuracy
5. **Structured output**: Return verified quote with full citation (volume, reporter, page, pinpoint), source URL, and clickable reference link

## Pitfalls

- Never trust auto-generated quotes without character-level verification — LLMs frequently paraphrase
- Pinpoint citations must reference the exact page where the quote appears, not just the case start page
- When a quote spans multiple paragraphs or includes footnotes, extract and include the complete context
- Ethical obligation: attorneys must verify all citations before filing — the tool assists but does not replace verification
