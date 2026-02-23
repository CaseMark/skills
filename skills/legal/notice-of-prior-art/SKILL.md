---
name: notice-of-prior-art
description: Drafts a Notice of Prior Art for patent litigation, USPTO prosecution submissions, or PTAB proceedings. Identifies and analyzes prior art references with element-by-element claim mapping, ensures compliance with 37 CFR 1.56 duty of disclosure, local patent rules, and IPR petition requirements. Use when preparing invalidity contentions, duty-of-disclosure filings, inter partes review petitions, or pre-litigation prior art disclosures.
tags:
  - drafting
  - litigation
  - pleading
---

# Notice of Prior Art

Drafts a litigation-ready Notice of Prior Art that discloses references material to patentability under 35 U.S.C. §§ 102 and 103, with element-by-element claim mapping and procedural compliance.

## Prerequisites

1. **Patent-at-issue** — patent/application number, filing date, issue date, named inventors, claims (independent + dependent)
2. **Prosecution history** — IDS filings, office actions, amendments narrowing claim scope
3. **Prior art references** — patents, publications, products, public uses with dates and bibliographic data
4. **Procedural context** — filing forum (USPTO under 37 CFR 1.56 | district court under local patent rules | PTAB under 35 U.S.C. § 311 | informal disclosure)
5. **Claim chart or mapping** — identification of which claims are challenged and which limitations each reference addresses

## Output Structure

### 1. Header & Caption

| Forum | Required Elements |
|-------|-------------------|
| **USPTO** | Application/patent number, art unit, examiner, confirmation number, customer number |
| **District Court** | Full case caption, civil action number, court/division, assigned judge |
| **PTAB** | Proceeding number (IPR/PGR), patent number, petitioner/patent owner |

### 2. Introduction

- Statutory basis: 35 U.S.C. §§ 102, 103
- Patent identification: full number, issue date, application number, filing date, inventors (patent order), title
- Legal framework statement referencing the specific procedural authority:
  - USPTO → 37 CFR 1.56 duty of candor
  - District court → applicable local patent rules (e.g., N.D. Cal. Patent L.R., E.D. Tex.)
  - PTAB → 35 U.S.C. § 311

### 3. Prior Art Reference Disclosures

For each reference, present:

**Patent references:**
- Full number with country code (e.g., US 5,123,456 A)
- All inventors, issue/publication date, title, assignee, CPC classification
- For foreign patents: original-language title + English translation; patent family info

**Non-patent literature:**
- Full bibliographic citation (Bluebook or MPEP convention per forum)
- Authors, title, journal/publication, volume/issue, date, pages, DOI/URL
- For standards/conference proceedings: sponsoring org, date, location, document ID

**Public use / on-sale bar (§ 102(a)/(b)):**
- Specific dates of offer for sale, public demonstration, or third-party access
- Corroborating evidence: sales records, invoices, marketing materials, communications
- Analysis of why disclosure was sufficiently public (address any confidentiality issues)

### 4. Claim-by-Claim Analysis

#### Anticipation (§ 102)

For each challenged claim, create an element-by-element claim chart:

```
| Claim Element | Prior Art Disclosure | Citation (col:line / page:para) |
|---------------|---------------------|---------------------------------|
| [Limitation]  | [Corresponding disclosure] | [Precise location] |
```

- Show every limitation disclosed expressly or inherently in a single reference
- Address enablement: reference must enable practice without undue experimentation (*In re Wands*, 858 F.2d 731 (Fed. Cir. 1988)) [VERIFY]
- For inherent disclosures: cite *Schering Corp. v. Geneva Pharms.*, 339 F.3d 1373 (Fed. Cir. 2003) [VERIFY] and explain why the limitation necessarily results from express disclosures

#### Obviousness (§ 103)

Apply the *Graham v. John Deere Co.*, 383 U.S. 1 (1966) framework:

| Graham Factor | Analysis Required |
|---------------|-------------------|
| **Scope/content of prior art** | Technical field, problems addressed, solutions disclosed |
| **Level of ordinary skill** | Education, experience, technology sophistication (cite spec, prosecution history, or expert testimony) |
| **Differences from prior art** | Map which references cover which limitations; identify the alleged inventive step |
| **Motivation to combine** | Articulate reasoning per *KSR Int'l Co. v. Teleflex Inc.*, 550 U.S. 398 (2007) — from references themselves, skilled-artisan knowledge, or nature of problem |
| **Reasonable expectation of success** | Why a skilled artisan would predict the combination works |

Address secondary considerations if applicable:

- [ ] Commercial success
- [ ] Long-felt unresolved need
- [ ] Failure of others
- [ ] Copying by competitors
- [ ] Unexpected results
- [ ] Industry praise / expert skepticism

(*Stratoflex, Inc. v. Aeroquip Corp.*, 713 F.2d 1530 (Fed. Cir. 1983)) [VERIFY]

### 5. Exhibit List

| Exhibit | Description | Date | Source | Relevance |
|---------|-------------|------|--------|-----------|
| A | [Doc type & title] | [Date] | [Author/source] | [Claim/limitation addressed] |

- Every cited reference must appear as an exhibit or have a verifiable public source (DOI, stable URL, database accession number)
- Foreign-language references: note translation status; include certification if required
- Citation format: MPEP conventions for USPTO; Bluebook for court filings

### 6. Conclusion & Certification

- Summarize: state whether prior art anticipates (§ 102), renders obvious (§ 103), or raises substantial patentability questions
- In litigation: note clear-and-convincing-evidence standard for invalidity (35 U.S.C. § 282)

**Certification language by forum:**

| Forum | Required Certification |
|-------|----------------------|
| **USPTO (37 CFR 1.56)** | Each item is material to patentability; submitted in compliance with duty of candor and good faith |
| **USPTO declaration** | 37 CFR 1.68 language (domestic) or 28 U.S.C. § 1746 (foreign declarants) |
| **District court** | Per local rules and FRCP requirements |
| **PTAB** | Per 37 CFR 42 requirements |

**Signature block:** typed name, designation (patent attorney/agent), USPTO registration number, firm, address, phone, email, date. Comply with e-filing requirements (Patent Center / CM/ECF).

## Guidelines

- **Pre-AIA vs. AIA**: Determine which § 102 framework applies based on the patent's effective filing date (before or after March 16, 2013)
- **Claim construction**: Use consistent terminology matching the patent claims and specification
- **No conclusory statements**: Every legal assertion must have factual and analytical support
- **Preservation of rights**: Include reservation language if additional prior art may be identified through ongoing discovery
- **Duty of disclosure is ongoing**: For USPTO filings, note that the obligation continues throughout prosecution
- **Privilege**: Do not disclose work-product analysis beyond what is required by the applicable disclosure obligation
- **Verify all citations**: Confirm patent numbers, dates, and case citations against primary sources before filing
