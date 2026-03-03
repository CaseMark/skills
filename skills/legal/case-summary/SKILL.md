---
name: case-summary
description: Generates structured case evaluation summaries from uploaded legal documents. Performs document triage, medical chronology, damages compilation, liability analysis, red flag identification, and valuation. Use when a user uploads case files and requests a case summary, case evaluation, litigation package, or PI case analysis.
---

# Case Summary

Produces an attorney-ready case evaluation from a collection of legal documents. Five phases: triage, deep-dive, synthesis, red flags, valuation.

## Quick Start

1. Collect all uploaded case documents.
2. Run phases 1-5 sequentially below.
3. Format output per [references/OUTPUT-TEMPLATE.md](references/OUTPUT-TEMPLATE.md).
4. Verify against the quality checklist before delivering.

## Phase 1: Triage & Classification

Classify each document into: Medical Records, Legal Filings, Correspondence, Financial/Billing, Investigation/Reports, Witness Statements, Photographs/Evidence.

Extract per document: Bates numbers (if present), document type, date, author/source, key parties.

Flag duplicates by comparing hashes, dates, and content overlap.

## Phase 2: Document Deep-Dive

Extract structured data by category:

- **Incident**: date, location, parties, mechanism, contributing factors, witness accounts, official reports
- **Medical**: provider, date, chief complaint, diagnosis (ICD codes if available), treatment, prognosis, referrals
- **Imaging**: modality, body part, findings, radiologist impression
- **Billing**: provider, service dates, CPT codes, billed/paid/adjusted amounts, balance, payer
- **Depositions**: deponent, date, key admissions, contradictions, credibility observations

## Phase 3: Analysis & Synthesis

1. **Medical chronology** — unify all treatment into a single timeline
2. **Treatment gap analysis** — flag gaps >30 days; document stated reasons
3. **Damages compilation** — total economic damages (medical specials, lost wages, future costs); assess non-economic damages
4. **Liability analysis** — map evidence to each liability theory's elements; rate strength

## Phase 4: Red Flag Identification

- **Medical**: pre-existing conditions, treatment gaps, inconsistent complaints, non-compliance
- **Liability**: comparative fault evidence, conflicting witnesses, spoliation concerns
- **Damages**: inflated claims, unrelated treatment, lien complications
- **Credibility**: social media contradictions, inconsistent statements, surveillance footage

## Phase 5: Valuation & Recommendations

Provide settlement range (low/mid/high), verdict potential, and net-to-client estimate after liens and fees.

Recommend: immediate actions, case strategy, additional discovery, experts to retain.

## Citations

Bates numbers when available: `[SMITH_0045-0048]`

Fallback format: `[Document_Name.pdf, pp. 1-4]`

## Quality Checklist

- [ ] All documents classified and accounted for
- [ ] Medical chronology continuous (gaps flagged)
- [ ] Damages totals reconcile with source documents
- [ ] Liability analysis maps to specific evidence
- [ ] Red flags documented
- [ ] Every claim traceable via citation

---

**Key changes:**

- **Removed `tags`** — not part of the Agent Skills spec; discovery relies on `description` keywords
- **Tightened description** — third-person, includes clear trigger phrases, under 1024 chars
- **Added Quick Start** — gives the agent an immediate action sequence before diving into phases
- **Eliminated the workflow code block** — redundant with the phase headings themselves
- **Compressed section headers and prose** — removed filler words, shortened labels (e.g., "Medical Chronology" to "Medical", "Diagnostic Imaging" to "Imaging")
- **Renamed "Citation Standards" to "Citations"** — shorter, same clarity
- **Tightened checklist items** — fewer words per line, same coverage
