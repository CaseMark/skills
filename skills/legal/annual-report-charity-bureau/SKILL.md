---
name: annual-report-charity-bureau
description: >
  Generates a U.S. nonprofit annual filing package for state charity-bureau
  registration requirements. Produces a Full Compliance Package, Form-Field Mode,
  or Executive Briefing with source-citation matrix, required-disclosure
  cross-checks, and filing-instruction controls. Use when drafting annual report
  submissions, renewal packets, penalty-of-perjury certifications, or state
  charity bureau filings for charitable solicitation compliance. Also trigger when
  the user mentions Form RRF-1, CHAR500, BCO-10, nonprofit annual report, charity
  registration renewal, or fundraiser disclosure attachments.
tags:
  - corporate
  - drafting
  - regulatory
  - research
  - summary
---

# Annual Report for State Charity Bureau

## Why This Skill Exists

State charity bureau annual filings carry penalty-of-perjury certifications and strict deadlines that vary by jurisdiction, fiscal year end, and revenue level. Missing a deadline can trigger late fees, solicitation suspensions, or loss of registration — and the requirements differ significantly across states (audit thresholds, oath language, required attachments, fee schedules). Organizations that treat these filings as a simple form-fill risk inconsistencies between the 990, financial statements, and state disclosures — inconsistencies that charity bureaus flag for investigation. This skill produces a cross-referenced, source-documented filing package that ensures internal consistency and jurisdiction-specific compliance.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft." Gather:

1. **Filing state/jurisdiction and filing year**
2. **Reporting period** (start/end dates, fiscal year end)
3. **Total revenue for the period** (for thresholding audit/review rules)
4. **Whether professional fundraisers/solicitors/co-venturers were used**
5. **Target output mode**: `full-compliance`, `form-field`, or `executive-briefing`

### Documents to Request

- Articles/charter, bylaws, board minutes/resolutions
- IRS Form 990 or equivalent + schedules
- Financial statements (audited/reviewed/compiled or GL summary)
- Contracts, policy docs, fundraising records, registration correspondence

**If the user doesn't respond**, apply and clearly label these defaults: filing is annual renewal/financial solicitation report (not secretary-of-state corporate report); reporting period is last completed 12 months; audit/review/compilation threshold to be researched per state rule; no professional fundraisers unless documents indicate usage. Mark all defaults as `[ASSUMED]`.

---

## Step 1: Intake Normalization

Build the intake normalization table and open-items tracker:

| Field | Value | Source | Conflict / Note |
|---|---|---|---|
| Legal name | | | |
| EIN | | | |
| State charity registration number | | | |
| Fiscal year end | | | |
| Reporting period | | | |
| State of filing | | | |
| Revenue basis used | | | |
| Fundraiser use | | | |

Flag any conflicts between sources (e.g., 990 revenue vs. audited financials) with `[CONFLICT — VERIFY WITH COUNSEL]`.

---

## Step 2: State-Requirements Research

Research requirements from official sources only: agency page, statute, admin code, filing instructions, fee schedule, portal guidance.

Record for each source: URL + publish/update date. Mark unverified details as `[TO BE CONFIRMED]`.

### Required Deliverable: Requirements Matrix

| Topic | Requirement | Source | Applies? | Status |
|---|---|---|---|---|
| Filing form/portal | | | | |
| Deadline | | | | |
| Fees and payment method | | | | |
| Audit/review/compilation thresholds | [VERIFY] | | | |
| Mandatory attachments | | | | |
| Required signatories | | | | |
| Oath language required | | | | |
| Notarization / signature method | | | | |
| Fundraiser disclosure fields | | | | |

---

## Step 3: Draft Report Sections

Draft in this order unless the state form dictates another:

1. **Organizational Identity** — legal name, DBA, EIN, registration number, addresses, solicitation channels, reporting period, material changes
2. **Governance and Leadership** — board roster with roles, terms, compensation, relationship disclosures
3. **Financial Position** — comparative financial summary with variance analysis, financial ratios
4. **Charitable Programs and Impact** — program descriptions, geography, beneficiaries, outputs, outcomes, expenses
5. **Fundraising and Compliance** — fundraising disclosures by method, professional fundraiser schedule (if applicable)
6. **Attachments and Filing Execution** — exhibits index, certification/signature block, filing instructions

### Core Output Templates

**Organizational Identity Block**

| Field | Response |
|---|---|
| Legal name | |
| DBA/assumed names | |
| EIN | |
| State registration number | |
| Principal address | |
| Mailing address | |
| Solicitation channels | |
| Reporting period | |
| Material changes during period | |

**Governance Roster**

| Name | Role/title | Address (if required) | Term start | Term end | Compensation | Relationship/disclosure notes |
|---|---|---|---|---|---|---|

**Financial Summary (comparative)**

| Line item | Current year | Prior year | Variance $ | Variance % | Source |
|---|---:|---:|---:|---:|---|
| Contributions and grants | | | | | |
| Program service revenue | | | | | |
| Investment income | | | | | |
| Special events net | | | | | |
| Total revenue | | | | | |
| Program expenses | | | | | |
| Management/general | | | | | |
| Fundraising | | | | | |
| Total expenses | | | | | |
| Change in net assets | | | | | |
| Total assets | | | | | |
| Total liabilities | | | | | |
| Net assets | | | | | |

**Financial Ratios**

| Metric | Formula | Output | Audit note |
|---|---|---|---|
| Program expense ratio | Program expenses / total expenses | | |
| Fundraising efficiency | Fundraising expenses / total contributions | | |
| Operating reserves (months) | Unrestricted net assets / (total expenses / 12) | | |

**Programs and Impact Table**

| Program | Purpose | Geography | Beneficiaries | Outputs | Outcomes | Program expenses | Volunteer hours |
|---|---|---|---|---|---|---|---|

**Fundraising Disclosures**

| Method | Gross raised | Direct costs | Net proceeds | State-required notes |
|---|---:|---:|---:|---|
| Online | | | | |
| Direct mail | | | | |
| Events | | | | |
| Major gifts | | | | |
| Other | | | | |
| Total | | | | |

**Professional Fundraiser Schedule** (if applicable)

| Entity | Role | Contract dates | Amount paid | Amount raised | Registration ID | Attached? |
|---|---|---|---|---|---|---|

---

## Step 4: Assemble Filing Package

### Attachments Index

| Exhibit | Description | Required by state | Included | Citation/reference |
|---|---|---|---|---|
| A | Form 990 + schedules | | | |
| B | Audit/review/compilation report | | | |
| C | Fundraiser or solicitor contracts | | | |
| D | Board resolution | | | |
| E | Other state-required docs | | | |

### Certification and Signatures

Use exact statutory language when available; otherwise flag `[VERIFY]`.

**Default penalty statement:**
"I declare under penalty of perjury under the laws of [STATE] that I have examined this report and attachments and believe them true, correct, and complete under penalty of perjury."

| Role | Name | Title | Signature | Date |
|---|---|---|---|---|

### Filing Instructions

| Item | Detail |
|---|---|
| Filing method | |
| Deadline | |
| Fee | |
| Extension process | |
| Number of originals/copies | |
| Notarization requirement | |

---

## Step 5: Mode-Specific Output

| Mode | Description |
|---|---|
| **Full Compliance Package** (default) | Narrative + all tables + exhibits index + signature and filing instructions |
| **Form-Field Mode** | Field-by-field responses matching state form/portal, with linked source evidence |
| **Executive Briefing** | Concise leadership summary of filing posture, risks, and open issues |

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the initial package, ask:

1. Do the financial figures match your records, and are there any discrepancies between the 990 and the financial statements that need resolution?
2. Are all board members and officers current, and should any compensation or relationship disclosures be updated?
3. Should I produce a different output mode (form-field or executive briefing) in addition to what was delivered?
4. Are there any professional fundraiser contracts or amendments not yet provided?

---

## Quality Audit

- Values consistent across all tables and narrative; conflicts flagged with `[CONFLICT — VERIFY WITH COUNSEL]`
- Every missing item marked `[OPEN]`, `[ASSUMED]`, or `[TO BE CONFIRMED]`
- Filing deadline, fee, and extension process verified from official source
- Audit/review/compilation threshold applied correctly for the organization's revenue level
- Oath/certification language matches state statutory requirements or flagged [VERIFY]
- Fundraiser disclosures complete if professional fundraisers were used
- Attachments index cross-referenced against state requirements matrix
- Board roster matches current organizational records
- Financial ratios computed correctly from stated figures
- No fabricated filing rules, deadlines, fee tiers, or audit requirements

---

## Guidelines

- Use official state/legal sources only for statutory and form requirements; do not infer legal obligations
- Keep values consistent across tables and narrative; if inconsistent, reconcile or flag conflict
- Every missing item must be marked `[OPEN]`, `[ASSUMED]`, or `[TO BE CONFIRMED]`
- Never fabricate filing rules, deadlines, fee tiers, or audit requirements
- Ensure final package is internally cross-referenced by exhibit and requirement topic
- Always include jurisdiction caveat if state rules vary by year or filing type
- Preserve board/officer identities and compensation disclosures exactly as source documents state
- Mark uncertain legal statements with `[VERIFY]` before final delivery
- Output requires attorney or compliance officer review before filing

**Required disclaimer on every output:**

> THIS FILING PACKAGE REQUIRES INDEPENDENT VERIFICATION OF ALL DEADLINES, THRESHOLDS, AND LEGAL REQUIREMENTS BY A QUALIFIED ATTORNEY OR CPA BEFORE SUBMISSION, AND DOES NOT CONSTITUTE LEGAL ADVICE.
