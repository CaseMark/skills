---
name: form-d-notice
language: en
description: Drafts U.S. SEC Form D notice data sets for Regulation D exempt offerings (Rule 504, 506(b), 506(c)), ready for EDGAR submission. Use when preparing a Form D filing, notice of exempt offering, Reg D compliance, or unregistered securities offering notice.
tags:
  - corporate
  - drafting
  - memo
  - regulatory
---

# Form D Notice of Exempt Offering

Produces a complete Form D data set for EDGAR submission. Filing deadline: within 15 days of first sale (Rule 503) [VERIFY].

## Prerequisites

Collect before drafting:

- **Filing status**: initial or amendment; date of first sale
- **Issuer identifiers**: legal name, CIK, EIN, org form, jurisdiction, year formed, SIC code, principal address, phone, website
- **Related persons**: all executive officers, directors, and promoters with business addresses
- **Offering terms**: security type(s), amount offered/sold, price or valuation method, minimum investment
- **Exemption basis**: Rule 504 / 506(b) / 506(c); solicitation and verification approach
- **Sales compensation**: broker-dealers/finders, CRD numbers, compensation structure
- **Use of proceeds**: primary uses, escrow arrangements if any
- **Signatory**: name, title, confirmation of authority
- **Prior Form D** data (amendments only)

Flag any missing items explicitly — never guess.

## Quick Start

1. Confirm filing type (initial/amendment) and first sale date
2. Populate issuer information from charter documents
3. List all related persons (officers, directors, **and promoters**)
4. Detail offering terms per class/series
5. State exemption claimed with matching eligibility facts
6. Document sales compensation and use of proceeds
7. Prepare signature block
8. Run validation checklist

## Core Workflow

### 1. Filing Header

- Filing type: Initial or Amendment
- Date of first sale
- CIK (if assigned)

### 2. Issuer Information

| Field | Req | Notes |
|---|---|---|
| Legal name | Yes | Must match charter documents |
| Jurisdiction | Yes | State/country of organization |
| Org form | Yes | Corp / LLC / LP / etc. |
| Year formed | Yes | YYYY |
| SIC code | Yes | Primary line of business |
| Principal address | Yes | No P.O. boxes |
| Phone | Yes | |
| Website | No | If maintained |

### 3. Related Persons

List every executive officer, director, and promoter:

| Name | Role(s) | Business Address |
|---|---|---|

Role definitions:
- **Executive officer** — any policy-making officer
- **Director** — board member
- **Promoter** — person taking initiative in founding/organizing the issuer

### 4. Offering Details

Provide per class/series if multiple securities:

- Type of security
- Total amount offered
- Amount sold to date
- Price per unit or valuation method
- Minimum investment
- Anticipated offering duration

### 5. Exemption Claimed

| Exemption | Eligibility | Solicitation | Investor Limits |
|---|---|---|---|
| Rule 504 | State qualification/limits apply | No general solicitation unless state law permits | As applicable |
| Rule 506(b) | Accredited + up to 35 sophisticated | No general solicitation | Investor sophistication required |
| Rule 506(c) | Accredited only | General solicitation permitted | Verification steps required |

If also relying on Section 4(a)(2), note basis and Reg D alignment.

### 6. Sales Compensation

- Brokers/finders used: Yes / No
- Names and CRD numbers (if registered)
- Cash commissions
- Non-cash compensation (securities, warrants, etc.)

### 7. Use of Proceeds / Escrow

- Primary use(s) of proceeds
- Material debt repayment (identify)
- Escrow details: agent, conditions
- Minimum offering amount and close conditions

### 8. Signature Block

```
By: [Name]
Title: [Title]
Date: [YYYY-MM-DD]
Authority: Duly authorized to sign on behalf of issuer; information is true and correct to the best of knowledge.
```

## Amendment Triggers

File an amendment when:
- Material change to offering terms or issuer information
- Correction of a material error
- Ongoing offering requires periodic update [VERIFY]

## Validation Checklist

```
- [ ] EDGAR deadline met (≤15 days from first sale)
- [ ] No conflicts with charter, PPM, SAFEs, or notes
- [ ] Exemption conditions match actual offering conduct
- [ ] All addresses complete and consistent
- [ ] Amounts and dates reconcile across materials
- [ ] State "blue sky" filings noted separately
```

## Pitfalls

- **506(b)**: must confirm no general solicitation and ≤35 non-accredited investor limit
- **506(c)**: must document accredited investor verification steps
- **Promoters omitted**: related persons list must include promoters, not just officers/directors
- **Consistency**: Form D must align with subscription docs, PPM, and actual sales practices
- Mark uncertain legal citations with `[VERIFY]`
