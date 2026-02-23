---
name: legal-article-summary
description: Produces structured summaries of legal scholarship (law review articles, journal articles, case notes) capturing thesis, methodology, key authorities, arguments, conclusions, and significance for rapid research triage. Use when drafting legal article summaries, law review summaries, journal note summaries, scholarship reviews, or literature review intake for research, case preparation, or CLE.
tags:
  - analysis
  - corporate
  - summarization
  - summary
---

# Legal Article Summary

Deliver a concise, structured summary that preserves the article’s analytical spine and practical significance.

## Prerequisites

1. Full article text or stable excerpts with page/section markers.
2. Citation data if available: author, title, journal, year, volume/issue, page range, DOI/URL.
3. Reader goal and length target (default 500–800 words unless specified).
4. Jurisdiction or doctrinal focus if not explicit in the article.

## Output Structure / Process

Section checklist (include only what exists in the article):

| Section | Must Include |
| --- | --- |
| Citation | Author, title, journal, year, volume/issue, pages; add DOI/URL if provided |
| Thesis / Question | One sentence statement of the central claim or research question |
| Methodology / Approach | Doctrinal analysis, empirical study, comparative research, theoretical framework, or policy critique |
| Major Arguments | 3–6 key points in the author’s sequence, each 1–3 sentences |
| Key Authorities | Statutes, cases, regulations, or doctrines the author relies on |
| Counterarguments / Limits | Acknowledged limitations, caveats, or addressed counterpoints |
| Conclusions / Recommendations | Findings and any normative proposals, separated clearly |
| Significance / Implications | Contribution to scholarship and practical impact |
| Future Research | Only if the author explicitly flags open questions |

Extraction checklist (do this before writing):

1. Identify the thesis and list the article’s section headings.
2. Capture methodology details, including dataset, sample size, timeframe, and method if empirical.
3. Extract the top authorities cited as foundations, not merely examples.
4. Flag modal language (may/might/could/suggests) and preserve it.
5. Note any explicit limitations or boundary conditions.
6. Record any proposed reforms or practice changes.

Template (edit to fit the article):

```markdown
**Citation:** {Author}, "{Title}," {Journal} {Year}, {Vol}({Issue}) {Pages}. {DOI/URL if provided}

**Thesis / Question:** {One sentence}

**Methodology / Approach:** {Doctrinal/empirical/comparative/theoretical; key details}

**Major Arguments / Findings:**
1. {Point}
2. {Point}
3. {Point}

**Key Authorities:** {Cases/statutes/regulations/doctrines}

**Counterarguments / Limitations:** {If any}

**Conclusions / Recommendations:** {Findings vs. proposals}

**Significance / Implications:** {Why it matters to scholarship and practice}

**Future Research:** {If stated}
```

## Guidelines

- Stay neutral and descriptive; do not add your own critique unless requested.
- Preserve the author’s emphasis and sequencing; do not reorder to improve rhetoric.
- Use plain legal prose; avoid jargon not present in the article.
- Quote sparingly and only if the exact phrasing is decisive; keep quotes short.
- Separate empirical results from normative recommendations.
- If jurisdiction is ambiguous, state it; default to U.S. only when clearly implied.
- If the article is theoretical, specify the framework and assumptions instead of empirical details.
- If the article contains a literature review, summarize the author’s positioning in 1–2 sentences.
- Flag uncertainty about any citation with `[VERIFY]`.
