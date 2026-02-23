---
name: ss4-ein-application
description: Drafts IRS Form SS-4 (Application for Employer Identification Number) by extracting entity details from formation documents such as articles of incorporation, operating agreements, and bylaws. Ensures precise legal name matching, correct entity classification, responsible party identification, and NAICS code selection. Use when forming a new business entity, applying for a federal tax ID, or preparing EIN applications for corporations, LLCs, partnerships, or sole proprietorships.
tags:
  - corporate
  - drafting
  - letter
---

# IRS Form SS-4 — EIN Application

Prepares a complete, filing-ready IRS Form SS-4 by extracting verified data from entity formation documents.

## Prerequisites

1. **Formation documents** — Articles of incorporation/organization, certificate of formation, or partnership agreement (filed and stamped)
2. **Governing documents** — Operating agreement, bylaws, shareholder agreements
3. **Responsible party info** — SSN/ITIN, full legal name, title, phone number
4. **Business details** — Principal office address (physical, not P.O. Box), mailing address, planned activities, employee projections

## Document Review

Search all uploaded documents for:

| Source Document | Extract |
|---|---|
| Articles of incorporation/organization | Legal name (exact), formation date, entity type, registered agent |
| Operating agreement / bylaws | Management structure (member-managed vs. manager-managed), ownership %, officer titles, fiscal year, signing authority |
| Partnership agreement | General partner(s), management authority, ownership interests |
| DBA/assumed name filings | Trade names for Line 2 |
| Board resolutions | S corp election (Form 2553), signing authority |
| Business plan / org chart | Employee projections, NAICS code, business activity description |
| Lease agreements | Physical location address |

Cross-reference the legal name across all documents. Flag any discrepancies before proceeding.

## Output Structure

Complete each line group using verified source data:

### Entity Identification (Lines 1–3)

| Line | Field | Instructions |
|---|---|---|
| 1 | Legal name | **Character-for-character** match to formation docs. Include exact suffix: "Inc." / "Incorporated" / "LLC" / "L.L.C." etc. as filed |
| 2 | Trade name / DBA | Only if registered with state/local authority; otherwise leave blank |
| 3 | Mailing address | Street/P.O. Box, suite, city, state, ZIP, county |

### Location & Responsible Party (Lines 4–7b)

| Line | Field | Instructions |
|---|---|---|
| 4a–4b | Physical location | Must be street address (no P.O. Box). Use lease or formation docs |
| 5a–5b | Responsible party name | Individual who owns/controls entity — see table below |
| 6 | SSN or ITIN | Of responsible party. Note if foreign individual without U.S. TIN |
| 7a–7b | Phone / Fax | Business telephone of responsible party |

**Responsible party by entity type:**

| Entity Type | Responsible Party |
|---|---|
| Sole proprietorship | Owner |
| Corporation | Principal officer (president, CEO, CFO, treasurer) per bylaws |
| Partnership | General partner with management authority |
| LLC (member-managed) | Controlling member by ownership % |
| LLC (manager-managed) | Managing member or manager per operating agreement |

### Entity Classification (Lines 8–9a)

- **Line 8a** — Select one checkbox matching formation docs:
  - Sole proprietor / single-member LLC
  - Partnership
  - Corporation (C corp default)
  - Personal service corporation
  - Nonprofit (church, other nonprofit, etc.)
  - Other (specify: e.g., "professional LLC," "LLP")
- **Line 8b** — Check if Form 2553 filed/will be filed for S corp election. Search for board resolutions and shareholder consents.
- **Line 8c** — Check if Form 1023/1023-EZ/1024 filed for tax-exempt status (nonprofits only)
- **Line 9a** — Formation/acquisition date from state-stamped filing. Must match exactly.

### Application Purpose & Operations (Lines 9b–16)

| Line | Field | Instructions |
|---|---|---|
| 9b | Reason for applying | Select primary: started new business, hired employees, banking, changed org type, purchased business, trust, pension plan, other |
| 10 | First wage date | Date wages first paid/will be paid; "N/A" if no employees |
| 11 | Fiscal year close | Month from governing docs or accountant records; default December |
| 12 | Employee projections (12 mo.) | Agricultural vs. non-agricultural; use business plan figures |
| 13 | Agricultural employees? | Yes/No based on business activities |
| 14 | Principal activity | Specific description, not generic (e.g., "retail sale of organic groceries" not "retail") |
| 15 | Products/services | Detailed list of revenue-generating offerings |
| 16 | NAICS code | 6-digit code matching principal activity. Verify against current NAICS manual. |

### Authorization & Signature (Lines 17–18)

- **Third-party designee** — Complete if attorney/CPA authorized to discuss application with IRS. Include: name, phone, 5-digit PIN.
- **Signature block** — Must be signed by individual with authority per governing documents:

| Entity Type | Authorized Signer |
|---|---|
| Sole proprietorship | Owner |
| Partnership | General partner |
| Corporation | Officer authorized by bylaws |
| LLC | Member or manager per operating agreement |

Include: printed name, title, signature line, date, phone number.

## Internal Consistency Checks

Before finalizing, verify:

- [ ] Line 1 legal name matches formation documents character-for-character
- [ ] Entity type (Line 8a) aligns with actual formation structure
- [ ] If corporation → Line 8b addresses S corp election status
- [ ] If "hired employees" (Line 9b) → Line 10 has a specific date (not N/A)
- [ ] If nonprofit → Line 8c addresses exempt status filing
- [ ] Responsible party title matches governing document role
- [ ] Fiscal year (Line 11) matches any fiscal year in governing docs
- [ ] NAICS code corresponds to Lines 14–15 activity description
- [ ] All addresses verified against source documents
- [ ] SSN/ITIN provided for responsible party

## Deliverables

1. **Completed Form SS-4** — All lines filled or marked N/A, formatted to match official IRS layout
2. **Transmittal memo** — Entity name, responsible party, submission method, special circumstances
3. **Preparation notes** — Sources used per section, assumptions made, discrepancies found and resolved, recommended follow-up actions

## Guidelines

- Extract data only from verified source documents; do not fabricate or assume entity details
- Flag any conflicts between formation documents (e.g., different entity names across filings) and request resolution before completing
- If S corp election status is unclear, flag for client confirmation
- NAICS codes change periodically — verify against the current classification manual [VERIFY]
- Form revision date and OMB number must reflect the most recent official IRS version
- The completed form constitutes a certification under penalties of perjury — all information must be verifiable
