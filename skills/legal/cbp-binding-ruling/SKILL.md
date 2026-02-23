---
name: cbp-binding-ruling
description: Drafts U.S. Customs and Border Protection binding ruling requests under 19 CFR Part 177 for customs compliance decisions on tariff classification, valuation, origin, and marking before importation. Use in pre-filing Regulatory/International Trade workflows when the user asks for a binding ruling packet, CBP import treatment opinion, HTSUS analysis, transaction-value methodology, or exhibit-backed drafting/review of a formal request. Trigger when input mentions “binding ruling,” “CBP ruling request,” “19 CFR Part 177,” “classification request,” “valuation,” “country of origin,” or “marking for import.”
tags:
  - drafting
  - letter
  - regulatory
  - research
---

# CBP Binding Ruling Request (19 CFR Part 177)

Produces a complete, evidence-backed U.S. Customs and Border Protection binding ruling request package for pre-filing import decisions.

## Prerequisites

1. Confirm the matter concerns a U.S. import treatment determination (classification, valuation, country of origin, or marking) and is appropriate for the binding ruling process under 19 CFR Part 177.
2. Identify the requesting party’s role and authority (importer/prospective importer/foreign manufacturer/authorized representative).
3. Gather transaction evidence: supply chain docs, technical specs, invoices, contracts, prior entries, and prior CBP communications.
4. Confirm whether there are related-party pricing factors, royalty/assist/profit-sharing elements, or prior rulings on similar goods.
5. Secure signatory authority and execution logistics: identity, title, legal signatory, and power-of-attorney scope if acting through counsel/broker.
6. Determine whether confidential business information is included and classify redaction requests.
7. Verify no pending protest/litigation or excluded-request status that conflicts with Part 177 scope.

## Output Structure / Process

1) Scope and jurisdiction screen
- Validate request type against CBP authority limits; do not include requests for hypothetical enforcement/penalty opinions.
- If determination is potentially non-Part 177 in scope, flag and reframe to non-binding inquiry.

| Determination type | Core statute/regulation | Required factual anchor |
|---|---|---|
| Tariff classification | 19 CFR Part 177, HTSUS + GRI 1-6 | Full physical composition, function, process, and alternatives rejected |
| Customs valuation | 19 USC 1401a, 19 CFR Part 152 | Related-party analysis, transfer pricing facts, royalty/assists/proceeds |
| Origin/marking | 19 CFR Part 102 (or relevant agreement appendices) | Manufacturing operations by entity, change in tariff classification, criteria applied |
| Other treatment | Related Part 177 authority + specific Part/reg guidance | Precise issue isolation and requested relief | [VERIFY]

2) Requester and standing section (mandatory)
- Include:
  - Full legal name and principal business address
  - Contact person and method
  - Relationship to merchandise/importation
  - Legal authority basis and POA summary (if applicable)
- Distinguish roles if the requester is not the importer of record.
- Address pre-filing commercial interest if not the final importer.

3) Build the merchandise record
Use this required matrix:

| Field | Required detail |
|---|---|
| Product name | Commercial and technical designation |
| Composition | Material IDs and percentages by weight/volume |
| Process | Step-by-step transformation from origin materials to final state |
| Specs | Weight, dimensions, capacity, tolerances, performance parameters |
| Use | End-user function, market segment, substitutability |
| Standards | ASTM/ISO/FDA/FCC/etc. references, with citation list |
| Samples | Photos/specimens plan and exhibit mapping |

- For proposed classification, state full ten-digit HTSUS and support with GRI sequencing, Explanatory Notes, and exclusionary analysis.

4) Transaction structure and history
- Document full chain:
  - Sourcing → processing → manufacturing → export → shipment → intended U.S. entry
- Provide all parties and relationship mapping:
  - Seller, manufacturer, broker, importer, distributor, end-user
  - Related-party flags under 19 CFR 152.102(g)
- Include pricing structure:
  - Incoterms
  - currency/payment terms
  - royalties, assists, non-monetary consideration
  - proceeds of resale
- Include prior import history if exists:
  - entry numbers, ports, dates, declared HTSUS/values, outcome of reviews/audits
  - prior rulings/internal advice/protests with factual changes explained

5) Legal questions and issue isolation
- One legal question per discrete issue.
- Avoid compound questions and non-determinative hypotheticals.
- Keep each question directly tied to requested ruling outcome.
- Draft sample question forms only; tailor to facts:

```
Whether the subject merchandise is properly classifiable under subheading [______] , HTSUS,
as opposed to [alternative subheading], based on [G.R.I. path + facts].

Whether transaction value under 19 U.S.C. 1401a is acceptable where:
- buyer/seller relationship: [______]
- payment/royalties/assists: [______]
and whether [specific adjustment] is required under 19 U.S.C. 1401a(b)(1)(D).

Whether country of origin for marking purposes is [country], under 19 CFR Part 102, based on
the identified processing and [change in tariff classification / substantial transformation].

```

6) Legal analysis framework
- Include authority stack table in final draft:

| Issue | Controlling authority | Binding/corroborative support | Application to fact pattern |
|---|---|---|---|
| Classification | HTSUS, GRI 1-6 | HQ rulings, NY rulings, ENs | Why heading/subheading is/ is not met |
| Valuation | 19 USC 1401a; 19 CFR Part 152 | CBP rulings, prior determinations | Whether transaction value is acceptable and adjustments required |
| Origin/Marking | 19 CFR Part 102; agreement-specific rules | Rulings + technical evidence | Why chosen origin rule is triggered |
| Procedure | 19 CFR Part 177 | CBP administrative guidance | Routing and documentary sufficiency |

- Prior rulings:
  - prioritize HQ decisions; use NY decisions for factually close products
  - distinguish adverse precedent with material differences
  - flag potential supersession or revocation status before citing.

7) Supporting evidence package
Prepare an exhibit index with evidence type + relevance:

| Exhibit ID | Document type | Relevance |
|---|---|---|
| Ex. 1 | Corporate authorization / POA | Standing and signatory authority |
| Ex. 2 | Technical specs / engineering data | Composition and manufacturing basis |
| Ex. 3 | Samples/photos | Physical characteristics |
| Ex. 4 | Commercial documentation | Value and sale-structure support |
| Ex. 5 | Prior rulings/correspondence | Historical/canonical treatment |
| Ex. 6 | Expert/lab reports | Scientific/compositional support |

- Include certifications for expert reports (identity, qualification, method, date).

8) Certification and confidentiality
- Add sworn certification language with printed name/title/signature/date.
- Confirm signer has authority and fact knowledge or reasonable basis.
- Add explicit 19 CFR 177.2(b)(7)-aligned confidentiality request with:
  - itemized confidential identifiers
  - harm rationale
  - non-confidential publication redaction plan

9) Final assembly and quality gates
- Confirm no unresolved references or unsupported facts.
- Ensure every asserted statement has exhibit support.
- Verify citation currency and any revocation status.
- Confirm routing to proper CBP office is current and accurate [VERIFY].
- Ensure all questions map directly to requested determinations only.

```text
Template order for final output:
1. Header and requester identification
2. Purpose and legal authority
3. Factual background
4. Transaction/merchandise description
5. Issue(s) and question(s) presented
6. Applicable law and analytical discussion
7. Requested determination
8. Attachments and index
9. Certification and signatures
```

## Guidelines

- Use plain, auditable facts: no narrative claims without source documents.
- Separate merits analysis from factual statements.
- Keep legal analysis concise but complete enough for administrative review.
- Use current law only; explicitly mark uncertain authority with [VERIFY] before finalization.
- Never include requests outside CBP binding ruling scope (e.g., unresolved litigation strategy, penalty/reasonable-care advisories, non-customs policy questions).
- For U.S. jurisdiction only; adjust if trade agreement or foreign-law layer exists.
