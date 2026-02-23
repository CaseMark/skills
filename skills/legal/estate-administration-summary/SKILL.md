---
name: estate-administration-summary
description: Generates structured U.S. estate administration/probate summaries that capture decedent and case identifiers, asset inventory and valuations, creditor claims, distributions, tax compliance, disputes, and next steps with source citations. Use for estate administration summary, probate status report, executor update, estate progress report, inventory and appraisal summary, creditor claims status, or distribution schedule summary.
tags:
  - summarization
  - summary
  - transactional
---

# Estate Administration Summary

Structured snapshot of probate/estate administration status, actions completed, issues, and remaining work.

## Prerequisites

1. Governing instrument(s): will, codicils, trust, or intestacy determination.
2. Probate case data: court, case number, petition, letters of appointment, bond.
3. Asset inventory and appraisals with valuation dates.
4. Creditor notices, claims register, and payment records.
5. Beneficiary roster and distribution records (interim/final).
6. Tax filings and notices: final 1040, fiduciary returns, estate/inheritance tax if applicable.
7. Orders, objections, correspondence, or litigation filings affecting administration.

## Output Structure / Process

Use the sections below in order. Cite sources for all factual statements (document name + date + page/paragraph). If a fact is missing or uncertain, mark `UNKNOWN` and list it in "Open Questions / Missing Docs".

### 1) Matter Header (table)

Field | Value | Source
--- | --- | ---
Decedent (full name) |  |
Date of death |  |
Domicile at death |  |
Jurisdiction / court |  |
Case number |  |
Personal representative / executor |  |
Relationship to decedent |  |
Appointment date |  |
Governing instrument | will / trust / intestacy |
Bond required? | yes/no/unknown |
Status as of | YYYY-MM-DD |

### 2) Estate Snapshot (bullets)

- Gross estate value (as of date):
- Known liabilities (as of date):
- Cash on hand / reserves:
- Distributions to date (total):
- Anticipated remaining duration:

### 3) Assets & Valuation (table)

Asset | Category | Ownership/title | Value (date) | Status (retained/sold) | Beneficiary/plan | Issues | Source
--- | --- | --- | --- | --- | --- | --- | ---
 |  |  |  |  |  |  | 

### 4) Creditor Claims (table)

Claim deadline | Date | Source
--- | --- | ---
Statutory claims deadline |  | 

Creditor | Amount claimed | Priority class | Status (approved/rejected/paid/pending) | Resolution date | Notes | Source
--- | --- | --- | --- | --- | --- | ---
 |  |  |  |  |  | 

### 5) Distributions (table)

Recipient | Relationship | Asset/cash | Value | Date | Authority (order/consent) | Source
--- | --- | --- | --- | --- | --- | ---
 |  |  |  |  |  | 

### 6) Tax Compliance (checklist)

- [ ] Final individual income tax return filed (Form 1040) date:
- [ ] Fiduciary income tax returns filed (Form 1041 or state equivalent) periods:
- [ ] Estate tax return required? (Form 706 / state) basis:
- [ ] Taxes paid / liabilities outstanding:
- [ ] Audits, notices, or disputes:

### 7) Disputes / Litigation / Challenges (table)

Issue | Parties | Procedural status | Next deadline/event | Impact on administration | Source
--- | --- | --- | --- | --- | ---
 |  |  |  |  | 

### 8) Administration Timeline (table)

Date | Event | Source
--- | --- | ---
 |  | 

### 9) Beneficiary Communications & Accountings (bullets)

- Beneficiaries notified (date/method):
- Missing, minor, or incapacitated beneficiaries:
- Accountings delivered or filed (type/date):
- Objections or concerns raised:

### 10) Remaining Tasks & Forecast (table)

Task | Dependency | Target date | Risk/notes | Source
--- | --- | --- | --- | ---
 |  |  |  | 

### 11) Open Questions / Missing Docs (list)

- 
- 

### Template (optional formatting)

```
Estate Administration Summary (As of YYYY-MM-DD)

1. Matter Header
2. Estate Snapshot
3. Assets & Valuation
4. Creditor Claims
5. Distributions
6. Tax Compliance
7. Disputes / Litigation
8. Administration Timeline
9. Beneficiary Communications & Accountings
10. Remaining Tasks & Forecast
11. Open Questions / Missing Docs
```

## Guidelines

- Use neutral, factual language; avoid legal opinions or advice.
- State all amounts and dates with "as of" qualifiers and cite the source.
- Do not infer statutory deadlines or priority rules; if not documented, mark `UNKNOWN` and flag as state-specific.
- Reconcile conflicting data only when a source hierarchy is explicit; otherwise show both and note the conflict.
- Redact or mask sensitive identifiers (SSN, full account numbers).
- If a legal citation is required but not verified, tag it `[VERIFY]`.
- Keep U.S. probate terminology consistent with the governing jurisdiction (court terminology varies by state).
