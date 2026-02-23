---
name: pfs-analyzer
description: Extracts and reconciles medical provider, employment/wage-loss, and insurance/lien data from personal injury plaintiff fact sheets, initial disclosures, and discovery materials against draft builder responses. Flags inconsistencies, supplementation needs, and impeachment risks. Produces builder-ready structured output with source traceability and a lawyer-facing issues memo. Use when analyzing plaintiff fact sheets, reconciling PI discovery responses, extracting medical provider lists, auditing wage loss documentation, or checking disclosure completeness.
tags:
  - analysis
  - litigation
  - pleading
  - summarization
  - summary
---

# Personal Injury Plaintiff Fact Sheet Analyzer

Extracts structured data from PI plaintiff disclosures, reconciles against draft builder responses, and produces a defensible issues memo with variance flags.

## Prerequisites

1. **Plaintiff Fact Sheet or Initial Disclosures** — executed PFS, FRCP 26(a)(1) packet, or MDL CMO-mandated form with attachments
2. **Medical provider list** — specials spreadsheet, treatment chronology, or HIPAA authorization list
3. **Wage loss package** — employer verification, disability notes, pay stubs, W-2s, tax returns
4. **Insurance/benefits disclosures** — health insurance cards, EOBs, PIP/MedPay declarations, lien letters, subrogation notices, Medicare/Medicaid status letters, declaration pages
5. **Client intake notes** — internal questionnaires with raw details potentially omitted from formal PFS
6. **Current draft builder responses** — the discovery responses to validate against

If any item is missing, label output as **"Partial"** and identify exactly what is absent and how it limits confidence.

### Required Context from Attorney

- Governing forum and jurisdiction (federal vs. specific state court)
- Incident date(s) and any disclosed prior injury history
- Date range disclosures cover
- Cash-pay, letter-of-protection, or workers' comp treatment
- Complete pharmacy list for relevant period
- Employment gaps exceeding six months
- Any known but intentionally undisclosed providers (attorney must decide strategy)
- No-fault/PIP vs. fault-based regime
- If MDL: specific CMO number and PFS format requirements

## Process

### Step 1: Build Traceable Extraction Map

Treat the disclosure packet as the controlling source of truth. For every extracted data point, record:

| Field | Format |
|---|---|
| Source document | "Doc 1, p. 4" or "Provider List §2" or Bates range |
| Verbatim text | Exact wording from source |
| Confidence | **High** = explicitly listed with address + dates; **Medium** = entity listed, missing dates or address; **Low** = inferred from context, requires verification |

**Rules:**
- Every fact must trace to specific source text — if untraceable, do not present as extracted data
- Preserve spelling exactly in `verbatim_name`; create separate `normalized_name` for dedup
- Never silently correct spelling or expand abbreviations
- Never merge duplicate-looking entities without confirmation (e.g., "ABC Imaging" vs. "ABC Radiology LLC")
- Distinguish "treatment facility" from "billing entity"
- Normalize document references consistently (page numbers, Bates ranges, or heading/paragraph)

### Step 2: Extract Medical Provider Data

For each provider entity, capture:

| Field | Notes |
|---|---|
| Full facility/provider name | Verbatim + normalized |
| Provider type | Hospital, clinic, physician, PT, imaging, pharmacy, lab, ambulance |
| Address, phone, fax | As disclosed |
| Dates of service | Range or single; preserve vagueness if source is vague |
| NPI | If available |
| Records/bills status | Disclosed, identified-only, or production pending |
| Category | **Injury-related** / **Pre-existing/Prior** / **Billing/Lien entity** |
| Source citation | Document, page, Bates |

**Categorization rules:**
- Treatment before DOI → mark "Prior/Pre-existing" (do not omit)
- Separate radiology reads, pathology, facility fees as distinct billing entities
- Do not treat referrals as treatment encounters
- Do not collapse multiple locations of a provider network
- Flag providers who may later be designated as non-retained treating experts (triggers separate deadlines under FRCP 26(a)(2) or state rules)

**Completeness check:** Ensure extraction includes pharmacies, PTs, diagnostic imaging, and labs — not only physicians.

### Step 3: Extract Employment & Wage Loss Data

For each employer:

| Field | Notes |
|---|---|
| Legal employer name | Verbatim; note any DBA |
| Address, supervisor/HR contact | As disclosed |
| Job title, schedule, pay rate | Preserve exact phrasing (hourly vs. salary) |
| Start/end dates | Flag gaps; do not fabricate precision from estimates |
| Wage documentation | Pay stubs, W-2s, tax returns, employer letters |
| Injury impact | First missed date, total days missed, PTO used, return status (full/light duty) |
| Benefits applied for | STD, LTD, SSDI, workers' comp |

**Rules:**
- Preserve vague time references as "reported estimate per disclosure" — never convert to false-specific dates
- Distinguish employer from worksite (staffing agency situations)
- Capture self-employment details separately
- Flag mitigation issues (job search, return to work)
- Flag employment gaps for defense scrutiny

### Step 4: Extract Insurance, Benefits, Liens & Prior Claims

For each insurance/benefit/lien:

| Field | Notes |
|---|---|
| Insurer/lienholder name | Verbatim |
| Plan type | Health, auto (PIP/MedPay/UIM), workers' comp, disability, Medicare/Medicaid |
| Member ID, group #, claim #, policy # | Distinguish these; do not conflate |
| Named insured | If stated |
| Contact info | Adjuster, claims dept |
| Lien status | Asserted / Pending / Final; amount if stated |
| Source citation | Document, page |

**Critical rules:**
- Extract only what documents contain — never guess policy limits, coverage, or lien validity
- Do not treat a letter of protection as an insurance lien
- If silent on Medicare status → flag: "Confirm Medicare beneficiary status and SSDI application; may trigger MSP reporting"
- Capture prior accidents, prior claims, prior settlements and flag for builder consistency
- Tailor required subfields based on no-fault/PIP vs. fault-based regime

### Step 5: Reconcile Against Builder Draft

Perform a three-dimension diff:

| Dimension | Check | Flag Format |
|---|---|---|
| **Completeness** | Entity-by-entity comparison of providers, employers, insurers | "Missing in builder" / "New — not in disclosures, confirm supplementation" |
| **Consistency** | Names, dates, amounts, addresses | "Spelling mismatch" / "Date range conflict" / "Amount discrepancy" |
| **Characterization** | Builder vs. disclosure support | "Builder overstates" / "Builder understates" |

**Priority flags:**

- **RED ALERT** — Contradiction between documents (e.g., PFS says not working; medical record references work activity). Requires immediate attorney intervention before service.
- **HIGH** — Undisclosed prior accidents, missing providers, inconsistent injury mechanism
- **MEDIUM** — Spelling variations, missing addresses, incomplete date ranges
- **LOW** — Formatting inconsistencies, optional fields unpopulated

**Rules:**
- Never silently overwrite builder data — always show the variance
- Distinguish "disclosed but not produced" from "entirely undisclosed"
- Do not override intentional attorney narrowing of scope — flag and defer to counsel
- Include supplementation timing sensitivity (FRCP 26(e): timely manner if materially incomplete; note state analogs may impose stricter deadlines)

### Step 6: Produce Output

Deliver two documents:

#### A. Builder-Ready Structured Output

- Separate `verbatim_name` and `normalized_name` fields
- Include `source_citation` and `confidence` for every record
- Match builder's exact schema and field constraints (facility vs. provider, one entry per employer, etc.)
- Include standard reservation language where appropriate: *"Plaintiff continues to treat and reserves the right to supplement."*

#### B. Lawyer-Facing Issues Memo

Label: **DRAFT — Attorney Work Product / For Counsel Review Only**

Contents:
1. **Follow-up questions** for client (missing dates, unknown insurance, pharmacy history)
2. **Supplementation needs** with timing sensitivity
3. **Defense focus areas** and impeachment vectors (treatment gaps, employment gaps, prior claims)
4. **Red flags** with recommended action
5. **Entity verification results** (NPI registry checks; flag unverifiable entities)
6. **Privilege flags** — if attorney-client communications found in intake notes, exclude from extraction and flag

## Guidelines

### Quality Control Checklist

- [ ] Every builder field has source citation or is labeled "client to confirm"
- [ ] Governing law references match actual forum (federal vs. state — do not assume FRCP for state cases)
- [ ] Provider names verified against CMS NPI Registry where possible; unverifiable names flagged
- [ ] Treatment dates consistent with DOI; pre-DOI treatment marked "Prior"
- [ ] Date formats consistent throughout; no false-specific conversions from estimates
- [ ] Identifiers (policy #, claim #) transcribed accurately; image-source identifiers flagged for OCR error check
- [ ] Extraction includes pharmacies, PTs, imaging, labs — not only physicians
- [ ] Adversarial review: no omission or discrepancy could be construed as concealment
- [ ] Builder output matches builder schema constraints exactly

### Jurisdiction Adaptation

- **Federal MDL**: Follow CMO-mandated PFS headers exactly; non-compliance risks administrative dismissal
- **California**: CCP governs; plaintiff verification form required alongside data extract
- **Florida**: Align extraction with Form 1.977 standard interrogatories (10-year provider history) [VERIFY]
- **Texas**: Map extraction to Rule 194 Required Disclosure categories [VERIFY]
- **State-specific authorization forms**: Flag "state-specific medical authorization requirements — attorney to confirm"; do not recommend provider contact

### Compliance

- **ABA Model Rules 1.1/1.3**: Attorney must verify all extracted data; LLM extraction does not satisfy competence/diligence duty
- **Model Rule 1.6**: Mask sensitive identifiers in issues memo (last four digits); full values only in secure builder fields
- **Model Rules 3.3/3.4/4.1**: Distinguish "documented facts" from "reported estimates"; never state completeness where record is incomplete
- **FRCP 37 / state sanctions**: Incomplete provider lists are common sanctions targets
- **HIPAA**: All extracted data is PHI; handle per firm data privacy protocols
- **Conflicts**: If documents indicate multiple potential claimants, flag for Model Rule 1.7 conflict screening
- All legal citations must be verified via available search tools or flagged as unverified
- All output requires attorney review before service or filing
