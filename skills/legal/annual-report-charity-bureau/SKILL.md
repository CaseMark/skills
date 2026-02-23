---
name: annual-report-charity-bureau
description: Generates a U.S. nonprofit annual filing package for state charity-bureau/charity registration requirements. Use when drafting annual report submissions, renewal packets, and penalty-of-perjury certifications for charitable solicitation compliance. Triggers on state charity bureau annual report, annual filing, nonprofit report, Form-Field Mode, fundraiser disclosure, attachment index, and board-signoff packet requests. Produces a Full Compliance Package, Form-Field Mode, or Executive Briefing with source-citation matrix, required-disclosure cross-checks, and filing-instruction controls.
tags:
  - corporate
  - drafting
  - regulatory
  - research
  - summary
---

# Annual Report for State Charity Bureau

Creates a defensible annual filing document package for state charity bureau review, aligned to jurisdiction-specific solicitation rules, signatures, and exhibits.

## Prerequisites

1. Confirm before drafting:
   - Filing state/jurisdiction and filing year
   - Reporting period (start/end dates, fiscal year end)
   - Total revenue for the period (for thresholding audit/review rules)
   - Whether professional fundraisers/solicitors/co-venturers were used
   - Target output mode: `full-compliance`, `form-field`, or `executive-briefing`
2. Upload source corpus:
   - Articles/charter, bylaws, board minutes/resolutions
   - IRS Form 990 or equivalent + schedules
   - Financial statements (audited/reviewed/compiled or GL summary)
   - Contracts, policy docs, fundraising records, registration correspondence
3. If any item missing, continue with explicit `[ASSUMED]` marks and add `[TO BE CONFIRMED]` items.

## Output Structure / Process

1. Intake and defaults
   - Resolve required inputs; otherwise apply defaults below and label as `[ASSUMED]`:
     - Filing is annual renewal/financial solicitation report, not secretary-of-state corporate report
     - Reporting period is last completed 12 months unless source indicates short year
     - Audit/review/compilation to be researched and applied per state rule
     - No professional fundraisers unless documents indicate usage
2. Build intake normalization table and open-items tracker

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

3. State-Requirements Research (official sources only)
   - Official agency page, statute, admin code, filing instructions, fee schedule, portal guidance
   - Record: source URL + publish/update date
   - Conflicts -> cite both + `[CONFLICT — VERIFY WITH COUNSEL]`
   - Unverified details -> `[TO BE CONFIRMED]`
4. Requirements matrix

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

5. Draft report sections in this order unless state form dictates another order:
   - Organizational identity
   - Governance and leadership
   - Financial position
   - Charitable programs and impact
   - Fundraising and compliance
   - Attachments and filing execution

6. Assemble filing package
   - Certification and signature block
   - Filing instruction sheet
   - Optional transmittal cover letter for executive review

## Core Output Templates

### Organizational Identity Block

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

### Governance Roster

| Name | Role/title | Address (if required) | Term start | Term end | Compensation | Relationship/disclosure notes |
|---|---|---|---|---|---|---|
| | | | | | | |

### Financial Summary (comparative)

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

### Financial Ratios

| Metric | Formula | Output | Audit note |
|---|---|---|---|
| Program expense ratio | Program expenses / total expenses | | |
| Fundraising efficiency | Fundraising expenses / total contributions | | |
| Operating reserves (months) | Unrestricted net assets / (total expenses / 12) | | |

### Programs and Impact Table

| Program | Purpose | Geography | Beneficiaries | Outputs | Outcomes | Program expenses | Volunteer hours |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

### Fundraising Disclosures

| Method | Gross raised | Direct costs | Net proceeds | State-required notes |
|---|---:|---:|---:|---|
| Online | | | | |
| Direct mail | | | | |
| Events | | | | |
| Major gifts | | | | |
| Other | | | | |
| Total | | | | |

### Professional Fundraiser Schedule (if applicable)

| Entity | Role | Contract dates | Amount paid | Amount raised | Registration ID | Attached? |
|---|---|---|---|---|---|---|
| | | | | | | |

### Attachments Index

| Exhibit | Description | Required by state | Included | Citation/reference |
|---|---|---|---|---|
| A | Form 990 + schedules | | | |
| B | Audit/review/compilation report | | | |
| C | Fundraiser or solicitor contracts | | | |
| D | Board resolution | | | |
| E | Other state-required docs | | | |

### Certification and Signatures

Use exact statutory language when available; otherwise flag `[VERIFY]` or `[TO BE CONFIRMED]`.

**Default penalty statement:**
"I declare under penalty of perjury under the laws of [STATE] that I have examined this report and attachments and believe them true, correct, and complete under penalty of perjury."

| Role | Name | Title | Signature | Date |
|---|---|---|---|---|
| | | | | |

### Filing Instructions

| Item | Detail |
|---|---|
| Filing method | |
| Deadline | |
| Fee | |
| Extension process | |
| Number of originals/copies | |
| Notarization requirement | |

## Mode Packs

- **Full Compliance Package**: narrative + all tables + exhibits index + signature and filing instructions.
- **Form-Field Mode**: field-by-field responses matching state form/portal, with linked source evidence.
- **Executive Briefing**: concise leadership summary of filing posture, risks, and open issues.

## Guidelines

1. Use official state/legal sources only for statutory and form requirements; do not infer legal obligations.
2. Keep values consistent across tables and narrative; if inconsistent, reconcile or flag conflict.
3. Every missing item must be marked `[OPEN]`, `[ASSUMED]`, or `[TO BE CONFIRMED]`.
4. Never fabricate filing rules, deadlines, fee tiers, or audit requirements.
5. Ensure final package is internally cross-referenced by exhibit and requirement topic.
6. Always include jurisdiction caveat if state rules vary by year or filing type.
7. Preserve board/officer identities and compensation disclosures exactly as source documents state.
8. Mark uncertain legal statements with `[VERIFY]` before final delivery.
