---
name: appellate-formatting
description: >
  Generates appellate-filing-ready Tables of Contents, Tables of Authorities,
  and Certificates of Compliance under FRAP 32(g) and related rules. Provides
  defensible word-count methodology with transparent exclusion calculations,
  strict anti-hallucination guardrails for pagination and citations, and
  cross-verification checklists. Covers federal circuits, state appellate courts,
  and U.S. Supreme Court formatting variations. Use this skill when building
  TOC, TOA, compliance certificates, or assembling final appellate brief
  components for filing. Also trigger when the user mentions word count
  calculation, FRAP 32 compliance, appellate brief assembly, page numbering,
  or asks for help formatting a brief for filing. Even if the user just says
  "I need a TOC and TOA" or "format this brief for filing," use this skill.
tags:
  - analysis
  - brief
  - checklist
  - drafting
  - litigation
---

# Appellate Document Formatting and Certification

## Why This Skill Exists

Appellate briefs are rejected at filing for formatting deficiencies more often than attorneys admit. A mismatched TOC heading, a fabricated page number, an incorrect word count, or a certificate citing the wrong rule subsection can delay filing past a jurisdictional deadline. These are mechanical errors with catastrophic consequences. The particular danger with AI-assisted formatting is hallucinated page numbers and citations that don't match the actual document.

This skill produces TOCs, TOAs, and Certificates of Compliance with absolute accuracy guarantees and transparent placeholders where verification is required.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft." Gather:

1. **Final or near-final brief text** — TOC/TOA integrity depends on stable headings and pagination; if still revising, label all output "DRAFT"
2. **Forum and case metadata** — court, circuit/state, case number, short caption, brief type (opening, response, reply, amicus, cross-appeal, rehearing)
3. **Formatting details** — proportional vs. monospaced font, font name/size, line spacing, margins
4. **Filing method** — CM/ECF PDF, paper, or both; whether court requires separate or combined word-count certificate
5. **Any court order** granting different length limits
6. **Local rule requirements** — TOA format, hyperlinking, bookmarks, addendum rules
7. **Word count source** — final count from drafting platform and user's list of believed exclusions

**If the user doesn't respond**, apply and clearly label these defaults: FRAP 32 federal circuit rules; proportional 14-point font; all page numbers as `[__]` placeholders; word count marked as estimate.

If forum, brief type, or formatting details are missing, **stop and ask** — certificate language, limits, and exclusions all depend on these.

---

## Step 1: Identify Governing Authority

| Forum | Primary Rules | Certificate Rule | Notes |
|-------|--------------|-----------------|-------|
| Federal (FRAP) | FRAP 28, 32 | FRAP 32(g) | Verify current word limits |
| U.S. Supreme Court | Rules 33, 34 | Rule 33.1(g) (booklet) / 33.2 (letter) | Booklet vs. 8.5×11 have different limit types |
| State appellate | Varies | Varies | Do NOT assume state rules mirror FRAP |

**FRAP type-volume limits** (verify current figures):

| Document Type | Word Limit |
|--------------|------------|
| Principal brief (opening/response) | 13,000 |
| Reply brief | 6,500 |
| Amicus brief (FRAP 29) | Verify per rule |

---

## Step 2: Normalize Brief Structure and Generate TOC

1. Confirm sections match FRAP 28 required components (if federal)
2. Build a heading map preserving exact wording, capitalization, and numbering
3. **Never rewrite headings** for the TOC — must match brief verbatim
4. Default TOC depth: major headings + two levels of subheadings; follow local rule if specified

**Pagination rules:**
- If paginated PDF provided → extract page numbers directly
- If unpaginated text → use `[__]` placeholders and label: `"DRAFT—PAGE NUMBERS TO BE UPDATED AFTER PAGINATION"`
- **Never fabricate page numbers**
- Front matter: lowercase Roman numerals (i, ii, iii)
- Body: Arabic numerals (1, 2, 3)

### TOC Template

```
TABLE OF CONTENTS

CORPORATE DISCLOSURE STATEMENT ................. i
TABLE OF AUTHORITIES ........................... ii
STATEMENT OF JURISDICTION ...................... 1
STATEMENT OF ISSUES ............................ 2
STATEMENT OF THE CASE .......................... 3
SUMMARY OF ARGUMENT ............................ 10
ARGUMENT ....................................... 12
  I.  [Point Heading Verbatim from Brief] ....... 12
      A. [Subheading Verbatim] .................. 12
      B. [Subheading Verbatim] .................. 14
  II. [Point Heading Verbatim from Brief] ....... 18
CONCLUSION ..................................... 30
CERTIFICATE OF COMPLIANCE ...................... 31
CERTIFICATE OF SERVICE ......................... 32
```

---

## Step 3: Build Table of Authorities

Parse all citations from brief text, then validate each one actually appears on listed pages.

**Required categories (in order):**

| Category | Sort Order |
|----------|-----------|
| Cases | Alphabetical by first party name |
| Constitutional Provisions | By article/amendment |
| Statutes | By code and section number |
| Rules | By rule number |
| Other Authorities | Alphabetical by author/title |

**Rules:**
- Copy citations exactly from brief — do NOT add reporter cites, volume numbers, or years not in the text
- If citation is incomplete, include as-is and flag: `"[Citation appears incomplete; verify reporter and year]"`
- Use "passim" only when authority cited 5+ times and jurisdiction permits
- Capture footnote citations
- Handle "In re" and "Ex parte" sorting correctly

### TOA Template

```
TABLE OF AUTHORITIES

Cases                                              Page(s)
Anderson v. Liberty Lobby, Inc.,
  477 U.S. 242 (1986) ............................ 14, 16
Celotex Corp. v. Catrett,
  477 U.S. 317 (1986) ............................ 14

Statutes
28 U.S.C. § 1291 ................................. 1
42 U.S.C. § 1983 ................................. 3, 7, 14

Rules
Fed. R. App. P. 28 ............................... 1
Fed. R. App. P. 32 ............................... 31

Other Authorities
16A Charles Alan Wright et al., Federal Practice
  & Procedure § 3949 (5th ed. 2020) .............. 15
```

---

## Step 4: Compute Word Count and Draft Certificate

### Bifurcated Count Method

```
Total Words (entire document):        [X]
− Excluded sections per FRAP 32(f):   [Y]
  - Cover page, Disclosure statement, TOC, TOA
  - Appearance of counsel, Signature block
  - Certificate of Compliance, Certificate of Service
  - Addendum (statutes/rules/regulations)
─────────────────────────────────────────
= Net Words for Compliance:           [Z]
```

**Critical rules:**
- Verify current FRAP 32(f) exclusion categories
- Count from source document (Word/WordPerfect), NOT from PDF OCR
- If within 2% of limit → flag explicitly and recommend trimming
- If user asks to exclude non-exempt sections → **refuse** and explain options
- Always state: *"Word count is an estimate based on supplied text. Attorney must perform final count using filing software."*

### FRAP 32(g) Certificate Template

```
CERTIFICATE OF COMPLIANCE

Pursuant to Fed. R. App. P. 32(g)(1), I certify that this brief complies
with the type-volume limitation of Fed. R. App. P. 32(a)(7)(B) because
this brief contains [____] words, excluding the parts of the brief
exempted by Fed. R. App. P. 32(f).

This brief also complies with the typeface requirements of Fed. R. App. P.
32(a)(5) and the type-style requirements of Fed. R. App. P. 32(a)(6)
because it has been prepared in a proportionally spaced typeface using
[Software Name] in [Font Size]-point [Font Name].

_____________________________
[Attorney Name]
```

---

## Step 5: Final Assembly Cross-Verification

### Pre-Filing Checklist

- [ ] Every TOC heading matches body heading verbatim
- [ ] Every TOA authority appears on listed pages
- [ ] Certificate word count matches final document count
- [ ] Caption, case number, party names consistent across cover, headers, signature block
- [ ] Font and margins uniform throughout (including footnotes if court requires same size)
- [ ] Front matter: Roman numerals; body: Arabic numerals
- [ ] No orphaned headers at page bottoms
- [ ] PDF is text-searchable with bookmarks (if required by court)
- [ ] TOA page numbers not shifted by TOA insertion itself
- [ ] Certificate cites correct rule subsections for current year

State: *"This document was generated based on [Federal/State] rules for the [Specific Circuit/Court]. All word counts, page numbers, and citations must be independently verified before filing."*

---

## Jurisdiction-Specific Notes

| Jurisdiction | Key Variation |
|-------------|--------------|
| 5th & 11th Circuits | Certificate of Interested Persons (CIP) required before TOC |
| 9th Circuit | Statement of Related Cases often excluded from word count |
| California (Rule 8.204) | 14,000-word limit for principal brief; different attachment rules [VERIFY] |
| U.S. Supreme Court | Booklet format (Rule 33.1) vs. letter format (Rule 33.2) — different limit types |
| State courts generally | May use page limits, different fonts/margins, separate word-count affidavits |

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the initial formatting package, ask:

1. Are all headings finalized, or should TOC entries be marked as draft?
2. Does the word count from your drafting software match the estimate provided?
3. Are there any local rule requirements I should verify for this specific court?
4. Should I generate the addendum (statutes/rules) or is that handled separately?

---

## Quality Audit

Before finalizing, verify:

- Every TOC entry matches a body heading verbatim — no phantom headings
- Every TOA citation copied exactly from brief text — nothing added or improved
- Indentation reflects heading hierarchy correctly
- All required sections included per governing rules
- Page numbers are real (from PDF) or clearly marked as `[__]` placeholders
- Word count methodology is transparent and defensible
- Certificate cites the correct rule subsections for this forum and year
- No fabricated page numbers, word counts, or citations anywhere in output
- Assumptions and open items listed prominently

---

## Guidelines

- **Never fabricate** page numbers, word counts, citations, or rule references
- **Never "improve" citations** by adding information not in the brief without attorney confirmation
- If information cannot be verified, use `[VERIFY]` or bracketed placeholders
- All outputs require licensed attorney review before filing
- Certificates are formal representations to the court — Model Rule 3.3 (Candor) applies
- Do not disclose sealed or confidential material in public-facing components
- If user requests a certificate citing wrong authority or wrong limits, refuse and explain the correct rule
- **Anti-hallucination**: This skill's highest risk is fabricated page numbers and citation page references. Use placeholders aggressively rather than guessing
- **Attorney review required**: Every deliverable must be verified against the final paginated document before filing
