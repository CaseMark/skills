---
name: pfs-analyzer
description: >
  Extracts and reconciles medical provider, employment/wage-loss, and
  insurance/lien data from personal injury plaintiff fact sheets, initial
  disclosures, and discovery materials against draft builder responses. Use this
  skill when the user mentions plaintiff fact sheet analysis, PFS extraction,
  medical provider reconciliation, wage loss audit, insurance lien tracking,
  PI discovery reconciliation, disclosure completeness checking, builder
  response validation, or MDL plaintiff data extraction. Also trigger when the
  user references FRCP 26(a)(1) initial disclosures, treatment chronologies,
  specials spreadsheets, or asks for help organizing plaintiff injury data.
  Even if the user just says "analyze this fact sheet" or "check these PI
  disclosures," use this skill.
tags:
  - analysis
  - litigation
  - pleading
  - summarization
  - summary
---

# Personal Injury Plaintiff Fact Sheet Analyzer

## Why This Skill Exists

Plaintiff fact sheets and initial disclosures are the foundation of every personal injury case, but they are also the most common source of discovery sanctions, supplementation failures, and impeachment at trial. Provider lists are incomplete, wage loss data conflicts with tax returns, insurance information is outdated, and draft builder responses drift from the source documents. When these discrepancies surface during opposing counsel's deposition or at summary judgment, the damage is severe and often irreversible.

This skill extracts structured data from PI plaintiff disclosures, reconciles it against draft builder responses, and produces a defensible issues memo with variance flags — all with source traceability for every data point.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft." Gather:

1. **Plaintiff Fact Sheet or Initial Disclosures** — executed PFS, FRCP 26(a)(1) packet, or MDL CMO-mandated form with attachments
2. **Medical provider list** — specials spreadsheet, treatment chronology, or HIPAA authorization list
3. **Wage loss package** — employer verification, disability notes, pay stubs, W-2s, tax returns
4. **Insurance/benefits disclosures** — health insurance cards, EOBs, PIP/MedPay declarations, lien letters, subrogation notices, Medicare/Medicaid status letters, declaration pages
5. **Client intake notes** — internal questionnaires with raw details potentially omitted from formal PFS
6. **Current draft builder responses** — the discovery responses to validate against
7. **Forum and jurisdiction** — federal vs. specific state court
8. **Key context** — incident date(s), disclosed prior injury history, date range disclosures cover, cash-pay/LOP/workers' comp treatment, complete pharmacy list, employment gaps exceeding six months

**If the user doesn't respond**, apply and clearly label these defaults: federal court; FRCP 26(a)(1) framework; all available documents included; partial output if source materials are incomplete.

> If any item is missing, label output as **"Partial"** and identify exactly what is absent and how it limits confidence.

---

## Step 1: Build Traceable Extraction Map

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
- Never merge duplicate-looking entities without confirmation
- Distinguish "treatment facility" from "billing entity"

---

## Step 2: Extract Medical Provider Data

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
- Flag providers who may later be designated as non-retained treating experts
- Ensure extraction includes pharmacies, PTs, imaging, and labs — not only physicians

---

## Step 3: Extract Employment and Wage Loss Data

For each employer:

| Field | Notes |
|---|---|
| Legal employer name | Verbatim; note any DBA |
| Address, supervisor/HR contact | As disclosed |
| Job title, schedule, pay rate | Preserve exact phrasing (hourly vs. salary) |
| Start/end dates | Flag gaps; do not fabricate precision from estimates |
| Wage documentation | Pay stubs, W-2s, tax returns, employer letters |
| Injury impact | First missed date, total days missed, PTO used, return status |
| Benefits applied for | STD, LTD, SSDI, workers' comp |

**Rules:**
- Preserve vague time references as "reported estimate per disclosure"
- Distinguish employer from worksite (staffing agency situations)
- Capture self-employment details separately
- Flag mitigation issues (job search, return to work)
- Flag employment gaps for defense scrutiny

---

## Step 4: Extract Insurance, Benefits, Liens, and Prior Claims

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

---

## Step 5: Reconcile Against Builder Draft

Perform a three-dimension diff:

| Dimension | Check | Flag Format |
|---|---|---|
| **Completeness** | Entity-by-entity comparison | "Missing in builder" / "New — not in disclosures, confirm supplementation" |
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
- Include supplementation timing sensitivity (FRCP 26(e); note state analogs may impose stricter deadlines)

---

## Step 6: Produce Deliverables

### A. Builder-Ready Structured Output
- Separate `verbatim_name` and `normalized_name` fields
- Include `source_citation` and `confidence` for every record
- Match builder's exact schema and field constraints
- Include standard reservation language: *"Plaintiff continues to treat and reserves the right to supplement."*

### B. Lawyer-Facing Issues Memo
Label: **DRAFT — Attorney Work Product / For Counsel Review Only**

1. **Follow-up questions** for client (missing dates, unknown insurance, pharmacy history)
2. **Supplementation needs** with timing sensitivity
3. **Defense focus areas** and impeachment vectors (treatment gaps, employment gaps, prior claims)
4. **Red flags** with recommended action
5. **Entity verification results** (NPI registry checks; flag unverifiable entities)
6. **Privilege flags** — if attorney-client communications found in intake notes, exclude from extraction and flag

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the initial extraction and reconciliation, ask:

1. Are the RED ALERT and HIGH-priority flags accurate — any known explanations I should incorporate?
2. Are there providers or employers the client mentioned but that don't appear in the disclosure documents?
3. Should I generate a supplementation timeline based on the gaps identified?
4. Does the builder-ready output match your builder's schema requirements?

If the user doesn't answer, recommend addressing RED ALERT items first and proceed if authorized.

---

## Quality Audit

Before finalizing, verify:

- Every builder field has source citation or is labeled "client to confirm"
- Governing law references match actual forum (federal vs. state)
- Provider names verified against CMS NPI Registry where possible; unverifiable names flagged
- Treatment dates consistent with DOI; pre-DOI treatment marked "Prior"
- Date formats consistent throughout; no false-specific conversions from estimates
- Identifiers (policy #, claim #) transcribed accurately; image-source identifiers flagged for OCR error check
- Extraction includes pharmacies, PTs, imaging, labs — not only physicians
- Adversarial review: no omission or discrepancy could be construed as concealment
- Builder output matches builder schema constraints exactly
- Reconciliation shows all variances — nothing silently overwritten

---

## Guidelines

### Jurisdiction Adaptation
- **Federal MDL**: Follow CMO-mandated PFS headers exactly; non-compliance risks administrative dismissal
- **California**: CCP governs; plaintiff verification form required alongside data extract
- **Florida**: Align extraction with Form 1.977 standard interrogatories (10-year provider history) [VERIFY]
- **Texas**: Map extraction to Rule 194 Required Disclosure categories [VERIFY]
- **State-specific authorization forms**: Flag "state-specific medical authorization requirements — attorney to confirm"; do not recommend provider contact

### Compliance and Ethics
- **ABA Model Rules 1.1/1.3**: Attorney must verify all extracted data; LLM extraction does not satisfy competence/diligence duty
- **Model Rule 1.6**: Mask sensitive identifiers in issues memo (last four digits); full values only in secure builder fields
- **Model Rules 3.3/3.4/4.1**: Distinguish "documented facts" from "reported estimates"; never state completeness where record is incomplete
- **FRCP 37 / state sanctions**: Incomplete provider lists are common sanctions targets
- **HIPAA**: All extracted data is PHI; handle per firm data privacy protocols
- **Conflicts**: If documents indicate multiple potential claimants, flag for Model Rule 1.7 conflict screening

### Anti-Hallucination
- All legal citations must be verified via available search tools or flagged as unverified
- Never invent provider names, dates, identifiers, or policy details
- Every data point must trace to a specific source document

### Attorney Review Required
- All output requires attorney review before service or filing
