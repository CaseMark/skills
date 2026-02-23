---
name: appellate-formatting-certification
description: Generates appellate-brief Tables of Contents and Authorities plus a rule-accurate Certificate of Compliance with defensible word-count methodology. Use for appellate brief formatting, TOC/TOA rebuilds, certificate of compliance drafting, FRAP 32(g) citations, word-count certifications, and final PDF cross-checks before filing.
tags:
  - analysis
  - brief
  - drafting
  - litigation
---

# Appellate TOC/TOA and Compliance Certificate

Produce filing-ready TOC, TOA, and certificate language tied to the final paginated brief and the governing rules.

## Prerequisites

1. Final or near-final brief text with stable headings and citations.
2. Forum and brief type (court, circuit/state, document type).
3. Formatting specs (font, size, spacing, margins).
4. Pagination source (final PDF or instruction to leave placeholders).
5. Word-count source (word processor count) and list of excluded sections.
6. Local rules, standing orders, or court order modifying format or limits.

## Output Structure / Process

Required inputs table:

| Input | Required | If missing |
| --- | --- | --- |
| Court and brief type | Yes | Ask targeted questions before drafting |
| Final paginated PDF | Preferred | Use placeholders; label as DRAFT |
| Word processor word count | Yes | Insert placeholder; require attorney count |
| Excluded sections list | Yes | Require rule text; do not assume |
| Local rules | Yes | Request rule text or cite [VERIFY] |

Rule anchors to verify against current rules:

| Forum | Core rule anchors |
| --- | --- |
| Federal courts of appeals | FRAP 28, FRAP 32(a)(5)-(7), FRAP 32(f), FRAP 32(g) [VERIFY] |
| State appellate courts | State rule text only [VERIFY] |
| U.S. Supreme Court | Sup. Ct. R. 33, 34, 33.1(g), 33.2 [VERIFY] |

Process checklist:

1. Confirm governing rules and any court order modifying limits.
2. Normalize heading map from the final brief; preserve exact text.
3. Generate TOC from the final pagination.
4. Generate TOA from the citations in the final brief.
5. Compute word count with explicit exclusions and method.
6. Draft certificate language tied to the confirmed rules.
7. Run final QC against the final PDF.

TOC rules:

- Never fabricate page numbers.
- If unpaginated, use placeholders like `[__]` and label `DRAFT - PAGE NUMBERS TBD`.
- Preserve exact heading text, capitalization, and numbering.
- Use Roman numerals for front matter and Arabic for body only if the forum does so.
- Include all required sections for the forum, including certificates if required.

TOC template:

```text
TABLE OF CONTENTS

[FRONT MATTER ITEM] ........................................ [__]
TABLE OF AUTHORITIES ....................................... [__]
[REQUIRED STATEMENTS] ...................................... [__]
ARGUMENT ................................................... [__]
  I. [Heading] ............................................. [__]
     A. [Subheading] ....................................... [__]
CONCLUSION ................................................. [__]
CERTIFICATE OF COMPLIANCE .................................. [__]
CERTIFICATE OF SERVICE ..................................... [__]
```

TOA categories and sorting:

| Category | Include | Sorting rule |
| --- | --- | --- |
| Cases | All cases cited in the brief | Alphabetical by first party name |
| Constitutional Provisions | Federal or state provisions cited | Jurisdiction then provision |
| Statutes | All statutes cited | Code then section |
| Rules | FRAP, local rules, state rules cited | Rule number |
| Other Authorities | Treatises, articles, manuals | Alphabetical by author/title |

TOA rules:

- Do not add or fix citations not present in the brief.
- If a citation is incomplete, flag it for attorney review.
- Avoid "passim" unless the forum permits it.
- Ensure each authority listed appears in the brief, including footnotes.

Word-count calculation table:

| Step | Value |
| --- | --- |
| Total words (source document) | [____] |
| Excluded sections (by rule) | [list with rule cite] |
| Excluded words | [____] |
| Net words for compliance | [____] |

Certificate template (adapt to forum rules):

```text
CERTIFICATE OF COMPLIANCE

Pursuant to [Rule cite] [VERIFY], I certify that this brief complies with the type-volume limitation of [Rule cite] [VERIFY] because it contains [____] words, excluding the parts of the brief exempted by [Rule cite] [VERIFY].

This brief complies with the typeface and type-style requirements of [Rule cite] [VERIFY] because it has been prepared in a proportionally spaced typeface using [Software] in [Font Size]-point [Font Name].
```

Final QC checklist:

- TOC headings match the brief verbatim.
- TOC page numbers match the final PDF.
- TOA entries match citations in the brief and page references are correct.
- Word count matches the source document used to generate the PDF.
- Certificate cites the correct rule and states the actual method and software.
- If within 2% of the limit, flag for trimming or motion for leave.

## Guidelines

- Do not invent page numbers, word counts, or citations.
- Do not certify compliance without a confirmed count and formatting specs.
- If the user requests a "Rule 37 certificate," ask for the exact order or rule basis; FRAP 37 is substantive interest relief, not a generic formatting certificate [VERIFY].
- For state or Supreme Court filings, require the exact rule text or insert placeholders with [VERIFY].
- Always require attorney review before filing and note that all counts and citations must be independently verified.
- Protect confidentiality; exclude sealed or sensitive data unless explicitly authorized.
