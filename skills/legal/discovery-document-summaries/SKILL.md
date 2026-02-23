---
name: discovery-document-summaries
description: Generates strategically focused summaries of discovery documents — depositions, emails, contracts, interrogatory responses, medical records, financial statements — with Bates citations, impeachment flags, timeline extraction, and privilege alerts. Produces an executive overview plus per-document entries organized by document type, chronology, or legal issue. Use during discovery and pre-trial phases of U.S. commercial litigation to compress voluminous document sets into actionable case preparation materials.
tags:
  - analysis
  - litigation
  - summarization
  - summary
---

# Discovery Document Summaries

Distills voluminous discovery productions into strategically focused summaries with Bates citations, impeachment opportunities, timeline anchors, and privilege alerts.

## Prerequisites

1. **Discovery documents** — depositions, emails, contracts, interrogatory responses, medical records, financial records, or other produced materials
2. **Case context** — operative claims, defenses, and key disputed issues to focus analysis
3. **Production identifiers** — Bates ranges or document control numbers for citation
4. (Optional) **Protective order designations** — to flag confidentiality tiers correctly

## Output Structure

### 1. Executive Overview

| Field | Content |
|---|---|
| Volume reviewed | Total pages / document count |
| Date range | Earliest to latest document date |
| Document categories | Depositions, emails, contracts, records, etc. |
| Key findings | Top 3–5 most significant evidentiary items |

### 2. Per-Document Entry Format

```
Document ID:     [Bates No. / production identifier]
Date:            [Document date]
Author/Parties:  [Author → Recipient, or contracting parties]
Type:            [Email / Deposition / Contract / Record / etc.]
Summary:         [2–4 sentence description of content]
Key Excerpts:    "[Verbatim quote]" (Bates XXXXX, p. X)
Legal Relevance: [Specific claim/defense element addressed]
Flags:           [⚑ Impeachment | ⚐ Privilege concern | ★ Exhibit candidate | ↔ Inconsistency]
```

### 3. Deposition-Specific Fields

In addition to the standard entry, capture:

- **Inconsistencies** — prior testimony, sworn statements, or documents that contradict this testimony (cite both sources)
- **Evasions** — questions avoided or answered unclearly; note verbatim Q&A with page/line cite
- **Credibility observations** — strong or weak moments affecting witness reliability, with page/line reference

### 4. Closing Section: Gaps & Follow-Up

- **Evidentiary gaps** — documents implied by references in produced materials but not produced
- **Additional discovery needed** — suggested RFPs, interrogatories, or deposition topics
- **Privilege log entries** — entries worth challenging or monitoring for future production

## Extraction Priorities

When reviewing documents, extract in this order:

| Priority | Target |
|---|---|
| 1 | Admissions and denials on disputed facts |
| 2 | Intent/knowledge evidence — awareness of risk, obligation, or wrongdoing |
| 3 | Timeline anchors — dates establishing sequence of events or notice |
| 4 | Chain of custody / authentication foundation facts |
| 5 | Contradiction material — conflicts between documents or witness statements |
| 6 | Damages evidence — monetary amounts, loss calculations, financial impact |

## Organization Options

| Method | Best For |
|---|---|
| By document type | Large mixed productions |
| Chronological | Fraud, breach, or narrative-heavy cases |
| By legal issue / claim element | Complex multi-count complaints |
| By witness | Deposition-heavy phases |

## Guidelines

- **Cite everything** — every extracted fact must reference a Bates number or production ID; never assert unattributed facts
- **Quote verbatim for key excerpts** — paraphrase for context only; use quotation marks and page/line for all direct quotes
- **Flag privilege concerns** — mark any document that appears inadvertently produced or bears privilege indicators; do not summarize privileged content, flag for attorney review
- **Flag confidentiality designations** — note CONFIDENTIAL or AEO tiers per protective order on every affected entry
- **Note ambiguity explicitly** — if a document is internally unclear or contradictory, say so; do not resolve ambiguity by assumption
- **Cross-reference** — link related documents (e.g., email chain → contract provision → deposition testimony) to surface evidentiary connections
- **Jurisdiction** — U.S. federal and state civil litigation rules assumed; flag if materials suggest foreign jurisdiction or forum
