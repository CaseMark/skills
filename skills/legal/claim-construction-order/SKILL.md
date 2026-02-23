---
name: claim-construction-order
description: Drafts a U.S. federal court Claim Construction Order (Markman order) following patent claim construction briefing or hearing. Applies Phillips v. AWH Corp. intrinsic/extrinsic evidence hierarchy to construe disputed claim terms and produce binding judicial interpretations that govern infringement and validity analyses. Use when drafting Markman orders, claim construction memoranda, or disputed-term rulings in U.S. patent litigation.
tags:
  - brief
  - drafting
  - litigation
---

# Claim Construction Order

Drafts a binding federal court order construing disputed patent claim terms following Markman v. Westview Instruments, Inc., 517 U.S. 370 (1996).

## Prerequisites

1. **Patent(s) at issue** — full text including claims and specification (with column/line numbers)
2. **Prosecution history** — file wrapper documents with paper numbers and pages
3. **Parties' proposed constructions** — joint claim construction chart or equivalent
4. **Markman record** — hearing transcript, expert declarations, tutorial submissions, briefing
5. **Case caption** — court, division, case number, full party names

## Output Structure

### 1. Caption & Title
Standard federal court caption. Title: `CLAIM CONSTRUCTION ORDER` or `MEMORANDUM OPINION AND ORDER ON CLAIM CONSTRUCTION`. Comply with district local rules.

### 2. Introduction
- Patent(s) at issue (number, title)
- Procedural posture (post-hearing, post-briefing, or stipulated record)
- Number of disputed terms being construed
- Cite: *Markman*, 517 U.S. 370; 35 U.S.C. § 112

### 3. Background
- Plain-language description of patented technology and its field
- Accused products/processes and infringement allegations (neutral summary)
- Relevant procedural history (complaint, answer, scheduling order, Markman date)

### 4. Legal Standard

| Principle | Rule |
|-----------|------|
| Governing standard | *Phillips v. AWH Corp.*, 415 F.3d 1303 (Fed. Cir. 2005) (en banc) — ordinary meaning to POSITA at time of invention |
| Primary source | Claim language, read in light of specification and prosecution history |
| Specification | "Single best guide" to claim meaning; may supply explicit lexicography |
| Prosecution history | Binding disclaimers and narrowing amendments limit scope |
| Extrinsic evidence | Dictionaries, expert testimony, treatises — secondary; cannot contradict intrinsic record |
| Appellate standard | Claim construction is a question of law (de novo); subsidiary factual findings reviewed for clear error — *Teva Pharms. USA, Inc. v. Sandoz, Inc.*, 574 U.S. 318 (2015) |
| Subsidiary precedent | *Vitronics Corp. v. Conceptronic, Inc.*, 90 F.3d 1576 (Fed. Cir. 1996) |

### 5. Construction of Disputed Terms

For **each** disputed term, use this structure:

```
Term: "[exact claim language]" (Claim [X] of U.S. Patent No. [X])

Plaintiff's Construction: ...
Defendant's Construction: ...

Analysis:
  Intrinsic Evidence
  - Claim language: how term appears in asserted and related claims
  - Specification: col. [X], ll. [X]–[X] — [quote/paraphrase]
  - Prosecution history: Paper No. [X], p. [X] — [disclaimer/amendment if any]

  Extrinsic Evidence (if intrinsic record is ambiguous)
  - [Dictionary definition / expert testimony / treatise — source, edition, page]

Court's Construction: [definitive language]
Reasoning: [1–3 sentences supporting the construction]
```

**Special cases:**
- **Plain meaning**: If no construction beyond plain and ordinary meaning is warranted, state that explicitly with brief reasoning.
- **Means-plus-function** (35 U.S.C. § 112(f)): Identify claimed function; identify corresponding structure disclosed in specification (col./ll.).
- **Indefiniteness**: Flag any term that may be indefinite under *Nautilus, Inc. v. Biosig Instruments, Inc.* [VERIFY citation]; note without resolving unless record is sufficient.

### 6. Conclusion
- Tabular summary of all construed terms and their final constructions
- Note which constructions may bear on infringement or validity without prejudging summary judgment
- Confirm constructions are binding for all litigation purposes (expert reports, jury instructions, motions)

### 7. Formal Order Block

```
IT IS HEREBY ORDERED that the disputed claim terms of [Patent No(s).] are
construed as set forth above. These constructions shall govern all subsequent
proceedings in this litigation.

[Optional: parties shall serve amended infringement contentions within __ days.]

SO ORDERED this ___ day of __________, 20___.

_________________________________
[Judge Name]
United States District Judge
```

## Guidelines

- **Judicial tone**: Authoritative, neutral, analytical. No advocacy; no party-favoring language.
- **Spec citations**: Always include column and line numbers (e.g., col. 4, ll. 12–18).
- **Prosecution history citations**: Include paper number and page from file wrapper.
- **Case law**: Bluebook format with pinpoint citations.
- **Consistency check**: Verify constructions are internally consistent across related terms; ensure no construction renders claims invalid or reads out a disclosed embodiment.
- **Avoid**: Importing limitations from preferred embodiments; constructions that merely restate the term; overbroad constructions that lack support.
- **Jurisdiction**: U.S. federal patent litigation only. Local rules vary by district — verify caption format, page limits, and required exhibits.
- **[VERIFY]**: All case citations should be verified against current Federal Circuit and Supreme Court precedent before filing.
