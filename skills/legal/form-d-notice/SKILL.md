---
name: form-d-notice
description: Drafts U.S. SEC Form D notices for Regulation D exempt offerings, capturing issuer details, related persons, offering terms, exemption basis, sales compensation, and use of proceeds for EDGAR filing within 15 days of first sale. Use when preparing a Form D, notice of exempt offering, Reg D filing, Rule 506(b)/506(c)/504 offering, or unregistered securities offering compliance.
tags:
  - corporate
  - drafting
  - memo
  - regulatory
---

# Form D Notice of Exempt Offering

Produce a complete Form D data set ready for EDGAR submission.

## Prerequisites

1. **First sale date** and offering status (initial vs amendment)
2. **Issuer identifiers**: legal name, CIK (if any), EIN (if used internally), org form, jurisdiction, year formed, SIC code, principal address, phone, website
3. **Related persons list**: executive officers, directors, promoters with business addresses and roles
4. **Offering terms**: security type(s), amount offered, amount sold to date, price/unit or valuation method, minimum investment
5. **Exemption basis**: Rule 504 / Rule 506(b) / Rule 506(c) and solicitation/verification approach
6. **Sales compensation**: broker-dealers/finders, CRD numbers, compensation structure
7. **Use of proceeds** and escrow arrangements (if any)
8. **Authorized signatory** name/title and confirmation of authority
9. **Prior Form D** data if filing an amendment

## Output Structure / Process

### 1) Filing Header

Checklist:
- `Filing type`: Initial or Amendment
- `Date of first sale`
- `CIK` (if assigned)

### 2) Issuer Information

Use this table format:

| Field | Required | Notes |
| --- | --- | --- |
| Legal name | Yes | Match charter documents |
| Jurisdiction | Yes | State/country of organization |
| Org form | Yes | Corp/LLC/LP/etc. |
| Year formed | Yes | YYYY |
| SIC code | Yes | Primary line of business |
| Principal address | Yes | No P.O. boxes |
| Phone | Yes | |
| Website | No | If maintained |

### 3) Related Persons

Include **all** executive officers, directors, and promoters.

Template:

| Name | Role(s) | Business Address | Notes |
| --- | --- | --- | --- |

Role logic:
- Executive officer: any policy-making officer
- Director: board member
- Promoter: person taking initiative in founding/organizing the issuer

### 4) Offering Details

Provide per class/series if multiple.

Checklist:
- `Type of security`
- `Total amount offered`
- `Amount sold to date`
- `Price per unit` or valuation method
- `Minimum investment`
- `Offering duration` (anticipated)

### 5) Exemption Claimed

Specify exemption and matching facts.

Table:

| Exemption | Eligibility Facts | Solicitation | Investor Limits |
| --- | --- | --- | --- |
| Rule 504 | State qualification/limits apply | No general solicitation unless state law permits | As applicable |
| Rule 506(b) | Accredited + up to 35 sophisticated | No general solicitation | Investor sophistication required |
| Rule 506(c) | Accredited only | General solicitation permitted | Verification steps required |

If relying on Section 4(a)(2) in parallel, note basis and alignment with Reg D.

### 6) Sales Compensation

Checklist:
- `Use of brokers/finders`: Yes/No
- `Broker/agent names`
- `CRD numbers` (if registered)
- `Cash commissions`
- `Non-cash compensation` (securities, warrants, etc.)

### 7) Use of Proceeds / Escrow

Checklist:
- `Primary use(s) of proceeds`
- `Debt repayment` (identify if material)
- `Escrow` details (agent, conditions)
- `Minimum offering amount` and close conditions

### 8) Signature Block

Provide:

- Printed name
- Title
- Date of signature
- Statement of authority and accuracy

Template:

```
By: [Name]
Title: [Title]
Date: [YYYY-MM-DD]
Authority: Duly authorized to sign on behalf of issuer; information is true and correct to the best of knowledge.
```

### 9) Validation Checklist

- EDGAR filing deadline: within 15 days of first sale (Rule 503) [VERIFY]
- No conflicts with charter/PPM/SAFEs/notes
- Exemption conditions match actual offering conduct
- Addresses are complete and consistent
- Amounts and dates reconcile across materials

### 10) Amendment Triggers

File an amendment if:
- Material change to offering terms or issuer information
- Correction of a material error
- Ongoing offering requires periodic updates [VERIFY]

## Guidelines

- Do not guess missing data; flag gaps explicitly.
- If claiming Rule 506(b), confirm no general solicitation and investor limits.
- If claiming Rule 506(c), document accredited investor verification steps.
- Ensure related person list includes promoters, not just officers/directors.
- Keep Form D consistent with subscription docs, PPM, and actual sales practices.
- Note any jurisdictional or state “blue sky” filings separately.
- Mark any uncertain legal citations with `[VERIFY]`.
