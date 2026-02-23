---
name: gsa-schedule-contract
description: >-
  Drafts a U.S. GSA Schedule (MAS/FSS) contract for commercial
  products/services with FAR/GSAR-compliant clause sets, SIN scope,
  pricing/PRC/EPA mechanics, IFF sales reporting, TAA, Section 508,
  cybersecurity, and subcontractor flow-downs. Use when drafting or updating
  GSA Schedule contracts, MAS solicitations, SIN crosswalks, price lists, or
  FAR/GSAR clause matrices. Trigger keywords: GSA Schedule, MAS, SIN, FAR
  52.212, GSAR 552.238, IFF, PRC, EPA, TAA, SAM UEI, CAGE, Section 508, NIST,
  FedRAMP.
tags:
  - agreement
  - drafting
  - regulatory
  - research
---

# GSA Schedule Contract

Produce an execution-ready GSA Schedule contract with verified clause set, pricing framework, and compliance obligations.

## Prerequisites

1. Contractor identity: legal name (SAM), UEI, CAGE, DBA(s), address, authorized signatory.
2. Current MAS solicitation or applicable schedule solicitation version, including clause list and any class deviations.
3. Awarded SINs with current descriptions and any legacy-to-MAS crosswalk.
4. Commercial Sales Practices, Basis of Award customer/category, and negotiated discount relationship.
5. GSA Authorized Price List data for each item/service.
6. IFF rate and current sales reporting portal requirements.
7. TAA country of origin data and any substantial transformation analyses.
8. IT accessibility documentation (VPAT/ACR) if IT is in scope.
9. Cybersecurity requirements applicable to scope (NIST, FedRAMP, CUI handling).
10. Required reps/certs (size, socioeconomic, 52.204-24/25, etc.).
11. Subcontractor list (if any) and required flow-down terms.
12. Disputes, audit, and records retention requirements from current FAR/GSAR clauses.

## Output Structure / Process

Contract blueprint (use this order and numbering):

1. Cover Sheet / Contract Summary
2. Parties and Authority
3. Contract Period and Effective Dates
4. Schedule Designation and Scope
5. SINs and Scope Details
6. Ordering Procedures and Order-Level Terms
7. Pricing, Discounts, and Authorized Price List
8. Price Reductions (PRC) and Notifications
9. Economic Price Adjustment (EPA), if applicable
10. Industrial Funding Fee (IFF) and Sales Reporting
11. Trade Agreements Act (TAA)
12. IT Accessibility (Section 508), if applicable
13. Cybersecurity and Incident Reporting, if applicable
14. Subcontracting and Flow-Down Requirements
15. Contract Administration and Modifications
16. Audit Rights and Record Retention
17. Disputes and CDA Clause
18. Delivery, Performance, QA, and Warranties
19. Representations and Certifications
20. Attachments and Incorporated Documents

Cover Sheet (summary table, mandatory):

| Field | Value | Source |
| --- | --- | --- |
| Contract number | {GSA_ASSIGNMENT} | GSA |
| Contractor legal name | {SAM_NAME} | SAM |
| UEI | {UEI} | SAM |
| CAGE | {CAGE} | SAM |
| Schedule designation | {MAS/FSS/PSS} | Solicitation |
| Awarded SINs | {SIN_LIST} | Award |
| Base period | {START_DATE}–{END_DATE} | Solicitation |
| Option period(s) | {OPTION_DATES} | Solicitation |
| CO | {NAME, EMAIL} | GSA |
| Contractor POC | {NAME, EMAIL} | Contractor |

SIN scope table:

| SIN | Current SIN title (verbatim) | Contractor offerings | Scope limits | Certifications |
| --- | --- | --- | --- | --- |
| {SIN} | {TITLE} | {PRODUCTS/SERVICES} | {GEO/ELIGIBILITY/LIMITS} | {REQS} |

Legacy SIN crosswalk (if applicable):

| Legacy SIN | Current MAS SIN | Scope confirmation |
| --- | --- | --- |
| {LEGACY} | {CURRENT} | {IN/OUT OF SCOPE} |

Authorized Price List (appendix, required):

| SIN | Item/Service | Part/Service ID | Unit | GSA Price | Commercial Price | Discount % | MOQ | Lead Time | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Pricing relationship (insert as a short section with variables):

```
Basis of Award: {CUSTOMER/CATEGORY}
Commercial Discount to Basis of Award: {X%}
Negotiated GSA Discount: {Y%}
Pricing Relationship Rule: {TEXT FROM PRC/NEGOTIATION}
```

PRC clause block (use clause text from current GSAR; do not paraphrase):

```
Insert GSAR 552.238-81 (Price Reductions), with number, title, and date.
Include notification window from clause: {DAYS} days.
Include effective date rule from clause: {RULE}.
```

EPA clause block (if applicable):

```
Clause: {FAR/GSAR EPA CLAUSE NUMBER, TITLE, DATE}
Index: {INDEX NAME}
Cap: {MAX % / PERIOD}
Docs Required: {EVIDENCE LIST}
Approval: {CO MOD REQUIRED}
```

IFF and Sales Reporting (insert from GSAR 552.238-74):

```
IFF Rate: {RATE} (verify current rate)
Reporting Portal: {SYSTEM NAME}
Reporting cadence: {PERIOD} with due date {DUE DATE RULE}
Pass-through prohibition: IFF not separately charged to customers.
```

TAA compliance (insert certifications and documentation requirements):

| Item/Category | Country of Origin | TAA Designated? | Substantial Transformation Basis |
| --- | --- | --- | --- |
| {ITEM} | {COUNTRY} | {YES/NO} | {CBP RULING/ANALYSIS} |

Section 508 (if IT scope):

| Product/Service | VPAT/ACR version | Conformance level | Exceptions |
| --- | --- | --- | --- |
| {ITEM} | {VERSION} | {LEVEL} | {EXCEPTIONS} |

Cybersecurity (if applicable):

| Requirement | Standard | Evidence |
| --- | --- | --- |
| CUI handling | NIST SP 800-171 | {SSP/POA&M} |
| Cloud service | FedRAMP | {AUTH LEVEL} |
| Incident reporting | {RULE} | {PROCESS} |

Clause matrix (incorporation by reference):

| Clause | Title | Date | Applicability |
| --- | --- | --- | --- |
| FAR 52.212-4 | {TITLE} | {DATE} | Mandatory |
| FAR 52.212-5 | {TITLE} | {DATE} | Mandatory |
| GSAR 552.238-74 | {TITLE} | {DATE} | Mandatory |
| GSAR 552.238-81 | {TITLE} | {DATE} | Mandatory |
| GSAR 552.238-82 | {TITLE} | {DATE} | Mandatory |
| FAR/GSAR {ADDITIONAL} | {TITLE} | {DATE} | {CONDITION} |

Administrative provisions checklist:

- Contract modifications only by CO-signed written mods.
- Audit rights per applicable FAR/GSAR clauses.
- Record retention period from clause(s); insert duration.
- Disputes clause FAR 52.233-1, with CDA references.

Subcontracting flow-down list (insert mandatory flow-downs by clause):

| Clause | Flow-down required? | Subcontract type |
| --- | --- | --- |
| {CLAUSE} | {YES/NO} | {SUPPLY/SERVICE/IT} |

## Guidelines

- Verify current FAR/GSAR clause numbers, titles, and dates against official sources; use `[VERIFY]` when uncertain.
- Do not assume IFF rate, period lengths, or PRC notification windows; insert from current solicitation/GSAR.
- Use incorporation by reference for clauses unless solicitation requires full text.
- Avoid obsolete identifiers (DUNS). Use UEI and current SAM status only.
- TAA, Section 508, cybersecurity, and PRC must align with current clause text; do not paraphrase.
- If the solicitation or mass modification conflicts with legacy terms, flag the conflict and adopt the current requirement with citation.
- No passing IFF as a line item to ordering agencies.
