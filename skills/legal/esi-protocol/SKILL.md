---
name: esi-protocol
description: Drafts comprehensive ESI protocols governing e-discovery procedures in federal litigation. Establishes frameworks for preservation, identification, collection, processing, review, and production of electronically stored information compliant with FRCP Rules 26, 34, and 37 and Sedona Principles. Use during discovery phase to formalize ESI agreements between parties.
tags:
  - agreement
  - drafting
  - litigation
---

# ESI Protocol

Drafts a stipulated ESI protocol to govern e-discovery procedures, suitable for entry as a court order. Must establish a complete framework for preservation, identification, collection, review, and production of electronic evidence under FRCP Rules 26, 34, and 37.

## Prerequisites

Gather before drafting:

1. **Case information** — parties, caption, court, docket number, nature of claims/defenses
2. **Existing orders** — scheduling orders, local rules, judge-specific ESI requirements
3. **Rule 26(f) conference** — any preliminary agreements or meet-and-confer correspondence
4. **Data landscape** — parties' IT infrastructure, data mapping, retention policies, custodian information
5. **Prior ESI disputes** — any correspondence or orders regarding ESI issues
6. **Vendor information** — e-discovery vendors retained, technical recommendations

## Output Structure

### Preamble and Definitions

- Formal preamble citing FRCP 26(f) and court's authority
- Party identification, temporal scope, proportionality acknowledgment
- **Comprehensive definitions** for:
  - ESI (per Rule 34(a)(1)(A))
  - System metadata vs. application metadata
  - Native format, static image format, load file
  - Reasonably accessible vs. not reasonably accessible (Rule 26(b)(2)(B))
  - Key custodians, data sources
  - Privilege-related terms (privilege log, clawback, quick peek, inadvertent disclosure)

### Preservation Obligations

- Preservation trigger date and scope
- Litigation hold notice requirements (content, recipients, reissue cadence)
- Structured vs. unstructured data preservation
- Third-party preservation obligations (cloud providers, vendors, former employees)
- Proportionality-based limitations (temporal, custodian, source, subject matter)
- Spoliation notification and meet-and-confer requirements

### Identification and Collection

- Custodian identification methodology and exchange timeline (30-45 days)
- Tiered custodian approach (core first, supplemental as needed)
- Collection standards: forensic (write-blocking, hash values, chain of custody) vs. routine
- Source-specific protocols: email, file servers, mobile devices, cloud, collaboration tools, social media
- Departed employee data handling
- Collection filters: date ranges, file types, deduplication

### Search Methodology

- **Keyword search**: development, negotiation, testing, refinement process
- **TAR/Predictive coding**: workflow specification, seed set procedures, validation metrics (precision/recall targets), transparency requirements
- **Analytics**: email threading, near-duplicate detection, concept clustering, foreign language identification
- Dispute resolution specific to search methodology disagreements

### Processing and Review

- Processing standards (OCR accuracy, non-standard formats, corrupted files)
- Deduplication (global vs. custodian-level, preserving distribution metadata)
- Email threading and family relationship preservation
- Filtering protocols for system/non-relevant files
- Review quality control (training, multi-level review, statistical sampling)

### Production Format

- Native format requirements (spreadsheets, databases, structured data)
- Image format specifications (TIFF/PDF, 300 DPI, color rendering, endorsements)
- Extracted text and OCR standards
- **Metadata specification**: Bates numbers, document date, author, recipients, subject, file name, path, extension, size, custodian, MD5 hash, parent-child indicators
- Bates numbering conventions (prefix, digits, family numbering)
- Load file format (Concordance DAT / IPRO LFP)
- Production media and delivery method
- Paper document scanning specifications

### Privilege Protection

- Privilege log requirements per Rule 26(b)(5)(A)
- Categorical vs. document-by-document logging
- Timing for privilege log production
- Redaction procedures and redaction logs
- **FRE 502(d) clawback agreement**: inadvertent disclosure procedures, sequestration obligations, challenge procedures
- Work product treatment (fact vs. opinion)
- Protective order for confidential business information

### Cost Allocation

- Preservation, collection, processing, review, and production cost allocation
- Cost-shifting procedures for not-reasonably-accessible ESI
- TAR and specialized processing cost sharing
- Translation and transcription costs

### Cooperation and Dispute Resolution

- Monthly/quarterly discovery conferences
- Phased discovery provisions
- Multi-tiered dispute resolution (discovery counsel → lead counsel → executives → court)
- Expedited briefing for ESI disputes
- Special master/neutral expert provisions
- Waiver provisions for untimely objections

### Execution and Modification

- Signature blocks for all parties
- Amendment procedures (technical vs. substantive)
- Duration and termination provisions
- Return/destruction of produced ESI at case conclusion
- Severability and integration clauses

## Guidelines

- Draft in precise legal language suitable for court filing
- Balance specificity with flexibility for unforeseen technical challenges
- Ensure provisions are balanced — not unfairly advantaging either party
- Cite FRCP, Sedona Principles, and EDRM standards where appropriate
- Include cooperation and proportionality commitments per 2015 FRCP amendments
