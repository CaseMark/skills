---
name: form-d
description: Drafts SEC Form D Notice of Exempt Offering for EDGAR filing under Regulation D. Captures issuer details, related persons, offering structure, exemption basis (Rule 504, 506(b), 506(c)), sales compensation, and use of proceeds. Use when filing Form D, exempt offering notice, Regulation D compliance, unregistered securities offering, or EDGAR notice filing.
tags:
  - corporate
  - drafting
  - regulatory
---

# Form D Notice of Exempt Offering

Drafts a complete SEC Form D for electronic EDGAR filing within 15 days of the first sale of securities in an exempt offering under Regulation D.

## Prerequisites

1. **Issuer organizational documents** — articles/certificate of incorporation or formation, operating agreement
2. **CIK number** — if previously assigned by SEC
3. **Offering materials** — PPM, subscription agreements, term sheets
4. **Related persons list** — all executive officers, directors, and promoters with business addresses
5. **Compensation arrangements** — broker-dealer agreements, finder's fee arrangements, CRD numbers
6. **Prior Form D filings** — if this is an amendment

## Output Structure

### Item 1: Filing Information

| Field | Notes |
|-------|-------|
| CIK Number | From prior EDGAR filings; leave blank if first filing |
| Filing Type | New Notice or Amendment (specify amendment number) |
| Date of First Sale | Exact date or "Yet to occur" |

### Item 2: Issuer Information

| Field | Notes |
|-------|-------|
| Legal Name | Exactly as in organizational documents |
| Principal Business Address | Street address required (no P.O. boxes) |
| Jurisdiction of Inc./Org. | State or foreign jurisdiction |
| Entity Type | Corporation, LP, LLC, GP, trust, other |
| Year of Inc./Org. | Four-digit year |
| SIC Code | Primary Standard Industrial Classification code |
| Phone / Website | Issuer contact |

Flag any recent name changes, redomiciliation, or structural changes with effective dates.

### Item 3: Related Persons

For each executive officer, director, and promoter:

| Field | Required |
|-------|----------|
| Full Legal Name | Yes |
| Business Street Address | Yes |
| Relationship(s) | Executive Officer / Director / Promoter (check all that apply) |

**Promoter definition**: Any person who, alone or with others, takes initiative in founding/organizing the business, or receives compensation/securities in connection with the offering and meets the regulatory definition.

### Item 4: Securities Offered

| Field | Detail |
|-------|--------|
| Type(s) | Equity, debt, option/warrant, security to be acquired upon exercise, pooled investment fund interests, tenant-in-common, mineral property securities, other |
| Total Offering Amount | Aggregate maximum |
| Total Amount Sold | As of filing date |
| Price Per Unit | Or state "variable pricing" |
| Minimum Investment | Per investor, if applicable |

If multiple classes/series, describe each separately with distinct rights and preferences.

### Item 5: Exemption(s) Claimed

| Exemption | Key Conditions |
|-----------|---------------|
| Rule 504 | Aggregate offering ≤ $10M in 12-month period [VERIFY current threshold] |
| Rule 506(b) | No general solicitation; unlimited accredited investors + up to 35 sophisticated non-accredited |
| Rule 506(c) | General solicitation permitted; issuer must take reasonable steps to verify all purchasers are accredited |
| Section 4(a)(2) | If claimed alongside Reg D, state separate basis |

Confirm factual alignment between the actual offering conduct and claimed exemption requirements.

### Item 6: Offering Structure & Sales Compensation

| Field | Detail |
|-------|--------|
| Duration | Date of first sale → expected termination |
| Offering Basis | Best efforts or firm commitment |
| Minimum Offering Amount | If applicable; describe escrow arrangements and escrow agent |
| Use of Proceeds | Specific categories: working capital, asset acquisition, debt repayment, etc. |

**Sales Compensation Disclosure:**

For each broker-dealer, finder, or intermediary:

| Field | Required |
|-------|----------|
| Name | Yes |
| CRD Number | If registered |
| Associated Broker-Dealer | If applicable |
| Compensation Type | Cash commission, finder's fee, securities, other |
| Compensation Amount/Terms | Dollar amount or formula |
| State(s) of Solicitation | Where solicitation will occur |

### Item 7: Issuer Financial Condition

Note if applicable:
- [ ] Development-stage company
- [ ] Limited operating history
- [ ] Recent material losses
- [ ] Audited financials provided to investors (may be required depending on exemption and investor sophistication)

### Item 8: Signature

| Field | Required |
|-------|----------|
| Signatory Name | Printed full name |
| Title | Must be authorized (executive officer, director, or general partner) |
| Date | Date of execution |

Include certification: signatory has reviewed the filing and information is true and correct in all material respects. Electronic signatures acceptable per SEC EDGAR authentication requirements.

## Guidelines

- **15-day deadline**: File no later than 15 days after first sale of securities
- **Amendments required**: File amendment for any material change in offering terms, new sales in states not previously reported, or annually for ongoing offerings
- **Accuracy is critical**: Inaccuracies can result in loss of exemption, enforcement action, and investor liability
- **Cross-reference**: Verify all Form D information against organizational documents, offering materials, and actual offering conduct
- **Public record**: Form D is publicly available on EDGAR — ensure no inadvertent disclosure of confidential terms beyond what is required
- **State blue sky**: Form D federal filing does not satisfy state notice filing requirements; flag need for separate state filings
- **Do not provide legal opinions** on whether the offering qualifies for a claimed exemption — flag uncertainties for attorney review
