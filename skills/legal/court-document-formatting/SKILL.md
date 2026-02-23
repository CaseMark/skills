---
name: court-document-formatting
description: >-
  Builds a filing-ready formatting blueprint for U.S. litigation pleadings,
  motions, and briefs. It applies mandatory caption, spacing, pagination,
  certificate, and e-filing formatting requirements while surfacing
  court-by-court/local-rule overrides. Use when preparing court documents,
  checking filing compliance, generating exhibit packages, or converting
  drafts for e-filing. Trigger keywords: court filing format, caption, page
  limits, line numbers, service certificate, PDF/A, local rules, judge
  instructions.
tags:
  - brief
  - drafting
  - litigation
  - motion
  - pleading
---

# Court Document Formatting

Creates a structured court-compliance format map before filing a litigation filing draft.

## Prerequisites

1. Identify filing court: court name, division, district/state, judge (if assigned), and case number format.
2. Confirm governing rules:
   1. FRCP/FRCP-related local counterpart rules, and
   2. The exact local rules package version in effect.
3. Confirm document class: pleading, motion, brief, reply, notice, or order response.
4. Confirm filing channel: paper filing, CM/ECF, CM/ECF equivalent, or vendor portal.
5. Gather required ancillary items: certificate of service format, exhibit numbering method, and word/length limits.

## Output Structure / Process

### 1) Rules Stack

| Layer | Rule source | Must match before draft finalized |
|---|---|---|
| 1 | Federal/parent court baseline | Paper/margins/spacing/font/heading |
| 2 | Division/court local rules | Added/overriding formatting constraints |
| 3 | Judge standing orders | Typography, fonts, binders, appendices |
| 4 | Case-specific order | Court or chamber-specific directives |

### 2) Base Federal Requirements (minimum baseline)

| Element | Requirement |
|---|---|
| Paper | 8.5 x 11 |
| Margins | 1 inch all sides |
| Font | 12 pt serif (Times New Roman/Times/Cambria-equivalent) unless court requires otherwise |
| Line spacing | Double-spaced body text |
| Page numbering | Consecutive pages in footer |
| Line numbering | If required by local rules: restart each page or continuous, per local rule |
| Signature block | Include counsel signature block and firm info as required |

### 3) Court Header / Caption Template

```text
[COURT NAME]
[COURT ADDRESS OR DISTRICT/COUNTY IDENTIFIER]

[PLAINTIFF],
    Plaintiff,
v.
[DEFENDANT],
    Defendant.

Case No. [COURT-SPECIFIC FORMAT]
[DOCUMENT TITLE] (e.g., MOTION FOR ... / RESPONSE / BRIEF IN SUPPORT)
```

### 4) Local Variation Matrix

| Topic | What to verify |
|---|---|
| Page limits | Word/page limits by motion type, filing tier, reply, and appendix |
| Fonts/spacing exceptions | Court may require alternate font or spacing |
| Electronic filing specs | Acceptable file size, bookmark requirements, OCR settings, attachment format |
| Certificate of service | Exact title, recipient list, method, and proof language |
| Exhibits | Labeling convention, tabbing, exhibits in sequence, exhibit indexing rules |

### 5) Filing Preparation Checklist

- Confirm caption data exactly matches case title.
- Verify docket number style and party designations.
- Run numbering checks on paragraphs, pages, and exhibits.
- Validate footnote/font/wording consistency.
- Confirm length compliance (brief, motion, declaration, or appendix).
- Generate a filing-specific pre-check summary:
  - Baseline rules applied
  - Local overrides applied
  - Items pending verification
- Export final PDF (PDF/A or format required by court portal).
- For image-heavy exhibits, run OCR and ensure searchable text layer when required.

## Guidelines

- Use local rules as controlling law over federal defaults.
- If any required local rule is unavailable, stop and request verification before final formatting.
- Never assume judge-level preferences; pull them from current standing orders.
- Do not omit filing deadlines or certificate of service requirements during final conversion.
- Keep style changes confined to the governing layer currently active (base, local, or judge-level override).
- For scanned documents, require OCR before e-filing if the court requires text-searchable filings.
- If rules conflict, prioritize the most specific source: judge order > local rule > general court rule > federal baseline.
