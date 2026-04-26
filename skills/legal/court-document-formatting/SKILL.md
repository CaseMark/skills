---
name: court-document-formatting
language: en
description: >-
  Builds a filing-ready formatting blueprint for U.S. litigation pleadings,
  motions, and briefs by applying caption, spacing, pagination, certificate,
  and e-filing requirements with court-specific local-rule overrides. Use when
  preparing court documents, checking filing compliance, generating exhibit
  packages, or converting drafts for e-filing. Triggers: court filing format,
  caption, page limits, line numbers, service certificate, PDF/A, local rules,
  judge instructions.
---

# Court Document Formatting

Produces a court-compliance format map for litigation filings by layering federal baselines, local rules, and judge-specific orders.

## Quick Start

Gather before drafting:

1. **Court**: name, division, district/state, assigned judge, case number format.
2. **Rules**: FRCP or state counterpart + exact local rules version in effect.
3. **Document class**: pleading, motion, brief, reply, notice, or order response.
4. **Filing channel**: paper, CM/ECF, or vendor portal.
5. **Ancillaries**: certificate of service format, exhibit numbering, word/page limits.

## Core Workflow

### 1. Build the Rules Stack

Apply layers in order; each overrides the one above:

| Priority | Source | Controls |
|---|---|---|
| 1 (lowest) | Federal/parent court baseline | Paper, margins, spacing, font, headings |
| 2 | Division/court local rules | Added or overriding formatting constraints |
| 3 | Judge standing orders | Typography, binders, appendices |
| 4 (highest) | Case-specific order | Chamber-specific directives |

**Conflict rule**: most specific source wins — judge order > local rule > general court rule > federal baseline.

### 2. Apply Base Federal Defaults

| Element | Default |
|---|---|
| Paper | 8.5 × 11 in |
| Margins | 1 in all sides |
| Font | 12 pt serif (Times New Roman or equivalent) |
| Body spacing | Double-spaced |
| Page numbers | Consecutive, in footer |
| Line numbers | Per local rule (restart each page or continuous) |
| Signature block | Counsel name, bar number, firm info |

### 3. Set the Caption

```text
[COURT NAME]
[DISTRICT/COUNTY IDENTIFIER]

[PLAINTIFF],
    Plaintiff,
v.
[DEFENDANT],
    Defendant.

Case No. [COURT-SPECIFIC FORMAT]
[DOCUMENT TITLE]
```

### 4. Verify Local Variations

| Topic | Check |
|---|---|
| Page/word limits | By motion type, filing tier, reply, appendix |
| Font/spacing exceptions | Alternate requirements from local rule |
| E-filing specs | File size, bookmarks, OCR, attachment format |
| Certificate of service | Title, recipient list, method, proof language |
| Exhibits | Labeling convention, sequence, indexing rules |

### 5. Filing Preparation Checklist

```
- [ ] Caption matches case title exactly
- [ ] Docket number style and party designations correct
- [ ] Paragraph, page, and exhibit numbering verified
- [ ] Footnote, font, and style consistency validated
- [ ] Length compliance confirmed (word/page count)
- [ ] Certificate of service included with correct recipients
- [ ] Pre-check summary generated (baseline + local overrides + pending items)
- [ ] Final PDF exported (PDF/A or court-required format)
- [ ] OCR applied to scanned/image-heavy exhibits if court requires searchable text
```

## Pitfalls

- **Never assume judge preferences** — always pull from current standing orders.
- **Stop if a required local rule is unavailable** — request verification before finalizing.
- **Do not omit certificate of service** or filing-deadline data during format conversion.
- **Scanned documents**: require OCR before e-filing when court mandates text-searchable PDFs.
- **Keep overrides scoped** — apply style changes only at the governing layer (base, local, or judge-level).
