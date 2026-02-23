---
name: case-summary
description: Generates comprehensive case evaluation summaries from uploaded legal case files. Performs document triage, medical chronology extraction, damages compilation, liability analysis, red flag identification, and case valuation. Use when the user uploads case documents and needs a case summary, case evaluation, litigation package, or PI case analysis.
tags:
  - analysis
  - drafting
  - litigation
  - summarization
  - summary
---

# Case Summary

Transforms a collection of legal case documents into a structured, attorney-ready case evaluation summary. Follows a five-phase workflow from document triage through valuation.

## Workflow

```
Phase 1: Triage & Classification
Phase 2: Document Deep-Dive
Phase 3: Analysis & Synthesis
Phase 4: Red Flag Identification
Phase 5: Valuation & Recommendations
```

## Phase 1: Triage & Classification

Classify each document into: Medical Records, Legal Filings, Correspondence, Financial/Billing, Investigation/Reports, Witness Statements, Photographs/Evidence.

For each document, extract: Bates numbers (if present), document type, date, author/source, key parties referenced.

Flag duplicates by comparing document hashes, dates, and content overlap.

## Phase 2: Document Deep-Dive

Analyze by category:

- **Incident**: Date, location, parties, mechanism, contributing factors, witness accounts, official reports
- **Medical Chronology**: Provider, date, chief complaint, diagnosis (ICD codes if available), treatment, prognosis, referrals
- **Diagnostic Imaging**: Modality, body part, findings, radiologist impression
- **Billing**: Provider, service dates, CPT codes, billed/paid/adjusted amounts, balance, payer
- **Depositions**: Deponent, date, key admissions, contradictions, credibility observations

## Phase 3: Analysis & Synthesis

1. **Medical Chronology**: Compile all treatment into a unified timeline
2. **Treatment Gap Analysis**: Identify gaps >30 days, document reasons if stated
3. **Damages Compilation**: Total economic damages (medical specials, lost wages, future costs) and assess non-economic damages
4. **Liability Analysis**: Map evidence to elements of each theory of liability; assess strength of each theory

## Phase 4: Red Flag Identification

Flag issues in these categories:
- **Medical**: Pre-existing conditions, gaps in treatment, inconsistent complaints, non-compliance
- **Liability**: Comparative fault evidence, conflicting witness accounts, spoliation concerns
- **Damages**: Inflated claims, unrelated treatment, lien complications
- **Credibility**: Social media contradictions, inconsistent statements, surveillance footage

## Phase 5: Valuation & Recommendations

Provide settlement range (low/mid/high), verdict potential, and net-to-client estimate after liens and fees.

Recommend: immediate actions, case strategy, additional discovery needed, experts to retain.

## Citation Standards

Use Bates numbers when available: `[SMITH_0045-0048]`

Fallback: `[Document_Name.pdf, pp. 1-4]`

See [references/OUTPUT-TEMPLATE.md](references/OUTPUT-TEMPLATE.md) for the full output format.

## Quality Checklist

- [ ] All documents classified and accounted for
- [ ] Medical chronology is continuous (gaps flagged)
- [ ] Damages totals reconcile with supporting documents
- [ ] Liability analysis maps to specific evidence
- [ ] Red flags identified and documented
- [ ] Citations traceable to source documents
