---
name: appellate-formatting
description: Generates appellate-filing-ready Tables of Contents, Tables of Authorities, and Certificates of Compliance under FRAP 32(g) and related rules. Provides defensible word-count methodology with transparent exclusion calculations, strict anti-hallucination guardrails for pagination and citations, and cross-verification checklists. Covers federal circuits, state appellate courts, and U.S. Supreme Court formatting variations. Use when building TOC, TOA, compliance certificates, or assembling final appellate brief components for filing.
tags:
  - analysis
  - brief
  - checklist
  - drafting
  - litigation
---

# Appellate Document Formatting and Certification

Produces Tables of Contents, Tables of Authorities, and Certificates of Compliance for appellate briefs with absolute accuracy against the filed document.

## Prerequisites

1. **Final or near-final brief text** — TOC/TOA integrity depends on stable headings and pagination; if still revising, label all output "DRAFT"
2. **Forum and case metadata** — court, circuit/state, case number, short caption, brief type (opening, response, reply, amicus, cross-appeal, rehearing)
3. **Formatting details** — proportional vs. monospaced font, font name/size, line spacing, margins
4. **Filing method** — CM/ECF PDF, paper, or both; whether court requires separate or combined word-count certificate
5. **Any court order** granting different length limits
6. **Local rule requirements** — TOA format, hyperlinking, bookmarks, addendum rules
7. **Word count source** — final count from drafting platform (Word, WordPerfect, Google Docs) and user's list of believed exclusions

If forum, brief type, or formatting details are missing, **stop and ask** — certificate language, limits, and exclusions all depend on these.

## Process

### Step 1: Identify Governing Authority

| Forum | Primary Rules | Certificate Rule | Notes |
|-------|--------------|-----------------|-------|
| Federal (FRAP) | FRAP 28, 32 | FRAP 32(g) | Verify current word limits via search |
| U.S. Supreme Court | Rules 33, 34 | Rule 33.1(g) (booklet) / 33.2 (letter) | Booklet vs. 8.5×11 have different limit types |
| State appellate | Varies | Varies | Do NOT assume state rules mirror FRAP |

**FRAP type-volume limits** (verify current figures):

| Document Type | Word Limit |
|--------------|------------|
| Principal brief (opening/response) | 13,000 |
| Reply brief | 6,500 |
| Amicus brief (FRAP 29) | Verify per rule |

- Search for circuit local rules: `"[Circuit] local rule table of authorities"` and `"[Circuit] certificate of compliance FRAP 32(g)"`
- If search unavailable, flag local-rule dependence and request user provide rule text

### Step 2: Normalize Brief Structure

1. Confirm sections match FRAP 28 required components (if federal):
   - Corporate Disclosure Statement, Jurisdictional Statement, Statement of Issues, Statement of the Case, Summary of Argument, Argument, Conclusion, Certificates
2. Build a **heading map** preserving exact wording, capitalization, and numbering (Roman numerals, letters)
3. **Never rewrite headings** for the TOC — must match brief verbatim
4. Default TOC depth: major headings + two levels of subheadings; follow local rule if specified
5. Flag divergences from conventional section order — ask if intentional

### Step 3: Generate Table of Contents

- If paginated PDF provided → extract page numbers directly
- If unpaginated text → use `[__]` placeholders and label: `"DRAFT—PAGE NUMBERS TO BE UPDATED AFTER PAGINATION"`
- **Never fabricate page numbers**

**Pagination convention:**
- Front matter: lowercase Roman numerals (i, ii, iii)
- Body: Arabic numerals (1, 2, 3)

**TOC template:**

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

**Verification checklist:**
- [ ] Every TOC entry matches a body heading verbatim
- [ ] No phantom headings from deleted sections
- [ ] Indentation reflects heading hierarchy
- [ ] All required sections included

### Step 4: Build Table of Authorities

**Parse all citations from brief text, then validate each one actually appears on listed pages.**

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
- Sub-categorize (e.g., Supreme Court vs. Circuit) only if local rules require

**TOA template:**

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

### Step 5: Compute Word Count

**Bifurcated count method:**

```
Total Words (entire document):        [X]
− Excluded sections per FRAP 32(f):   [Y]
  - Cover page
  - Disclosure statement
  - Table of Contents
  - Table of Authorities
  - Appearance of counsel
  - Signature block
  - Certificate of Compliance
  - Certificate of Service
  - Addendum (statutes/rules/regulations)
─────────────────────────────────────────
= Net Words for Compliance:           [Z]
```

**Critical rules:**
- Verify current FRAP 32(f) exclusion categories — do not rely on memorized list
- Count from source document (Word/WordPerfect), NOT from PDF OCR
- If within 2% of limit → flag explicitly and recommend trimming
- If user asks to exclude non-exempt sections → **refuse** and explain options: edit brief or seek leave for overlength filing
- Always state: *"Word count is an estimate based on supplied text. Attorney must perform final count using filing software."*

### Step 6: Draft Certificate of Compliance

**FRAP 32(g) template:**

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

- Insert bracketed placeholders for any unconfirmed detail — never guess
- If local rules prescribe specific certificate language, use that instead
- If user references "Rule 37 certificate," clarify — FRAP 37 governs interest/mandates, not formatting; ask for the specific court instruction

### Step 7: Final Assembly Cross-Verification

**Pre-filing checklist:**

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

## Jurisdiction-Specific Notes

| Jurisdiction | Key Variation |
|-------------|--------------|
| 5th & 11th Circuits | Certificate of Interested Persons (CIP) required before TOC |
| 9th Circuit | Statement of Related Cases often excluded from word count |
| California (Rule 8.204) | 14,000-word limit for principal brief; different attachment rules [VERIFY] |
| U.S. Supreme Court | Booklet format (Rule 33.1) vs. letter format (Rule 33.2) — different limit types |
| State courts generally | May use page limits, different fonts/margins, separate word-count affidavits |

For any court not listed: search for governing rules and cite with URLs. If search unavailable, provide template with placeholders and instruct attorney to consult applicable rules.

## Guidelines

- **Never fabricate** page numbers, word counts, citations, or rule references
- **Never "improve" citations** by adding information not in the brief without attorney confirmation
- If information cannot be verified, use `[VERIFY]` or bracketed placeholders
- All outputs require licensed attorney review before filing
- Certificates are formal representations to the court — Model Rule 3.3 (Candor) applies
- Do not disclose sealed or confidential material in public-facing components
- If user requests a certificate citing wrong authority or wrong limits, refuse and explain the correct rule
