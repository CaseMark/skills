---
name: form-8k
description: >-
  Drafts U.S. Form 8-K current reports for SEC EDGAR filing with item-accurate
  narratives, exhibit indexing, and signature blocks. Use when a public
  company has a reportable event, needs Item 1.01/2.01/2.02/5.02/7.01/8.01
  coverage, or must file a current report within four business days. Trigger
  keywords: "Form 8-K", "current report", "SEC filing", "EDGAR", "Item 1.01",
  "Item 2.01", "Item 5.02", "Item 9.01", "Reg FD".
tags:
  - corporate
  - drafting
  - memo
  - regulatory
---

# Form 8-K Current Report

Draft a Form 8-K current report ready for EDGAR conversion based on verified source documents.

## Prerequisites

1. Triggering event facts with dates for event, board approval, and effectiveness.
2. Source documents: definitive agreements, amendments, resolutions, press release, investor deck, employment or separation docs.
3. Registrant identifiers from the latest 10-K/10-Q: exact legal name, Commission File No., CIK, IRS EIN, state of incorporation, fiscal year end, principal executive office address, phone.
4. Item selection list with rationale for each triggered item.
5. Financial statement inputs and significance test data for Item 2.01, if applicable.

## Output Structure / Process

**Cover Page (EDGAR-Ready Fields)**

| Field | Source / Rule |
|---|---|
| Registrant exact legal name | Latest 10-K/10-Q cover |
| Commission File No. and CIK | Latest 10-K/10-Q cover |
| IRS EIN | Latest 10-K/10-Q cover |
| State of incorporation | Charter or 10-K/10-Q |
| Fiscal year end | Latest 10-K/10-Q cover |
| Principal executive offices address and phone | Latest 10-K/10-Q cover |
| Trading symbol(s) and exchange(s) | Latest 10-K/10-Q cover [VERIFY] |
| Checkboxes for reporting items | Form 8-K cover |
| Checkboxes for Rule 425/14a-12/14d-2/13e-4 communications | Form 8-K cover [VERIFY] |
| Indicate amendment, if 8-K/A | Form 8-K cover |

**Item Selection Matrix**

| Item | Trigger | Required Narrative Elements | Typical Exhibits |
|---|---|---|---|
| 1.01 | Entry into material definitive agreement | Date, parties, purpose, key terms, duration, termination, material conditions | Agreement (10.x) |
| 1.02 | Termination of material definitive agreement | Date, parties, reason, termination fees or obligations | Termination notice (10.x) |
| 2.01 | Completion of acquisition/disposition | Date, assets/business, consideration, structure, significance | Purchase agreement (10.x), pro forma (99.x) |
| 2.02 | Results of operations/financial condition | Reference to press release or presentation, caution on furnished status | Press release (99.x) |
| 2.03 | Creation of direct financial obligation or off-balance sheet obligation | Date, amount, terms, maturity, covenants, events of default | Credit agreement (10.x) |
| 2.05 | Costs associated with exit/disposal | Nature of plan, expected charges, timing | Board materials (99.x) |
| 2.06 | Material impairment charges | Nature of impairment, amount, timing | Press release (99.x) |
| 3.02 | Unregistered sales of equity | Date, securities, exemption relied upon, consideration | Subscription/SPA (10.x) |
| 5.02 | Director/officer appointment or departure, compensation | Name, title, effective date, background, compensation arrangements | Offer or separation letter (10.x) |
| 5.03 | Amendments to charter/bylaws, fiscal year change | Description of amendment, effective date | Charter/bylaws (3.1/3.2) |
| 7.01 | Regulation FD disclosure | Description of information furnished | Presentation (99.x) |
| 8.01 | Other events | Factual description, materiality context | Press release (99.x) |
| 9.01 | Financial statements and exhibits | Identify included or to-be-filed financials, list exhibits | FS/pro forma (99.x), agreements (10.x) |

**Narrative Drafting Rules**

- Use objective, non-promotional language and cite only verifiable facts.
- State the event date and any different effective date.
- Use exact legal names for parties and titles for individuals.
- Quantify all material dollar amounts and consideration structure.
- Align narratives with press releases and exhibits to avoid inconsistencies.

**Material Definitive Agreement Summary Template**

```text
On [Date], [Registrant] entered into [Agreement Title] with [Counterparty].
The agreement relates to [Purpose/Transaction].
Material terms include: [Consideration], [Duration], [Termination Rights], [Key Conditions], [Material Covenants].
The agreement becomes effective on [Effective Date] and may be terminated upon [Conditions].
```

**Item 5.02 Personnel Change Template**

```text
Effective [Date], [Name] was [appointed/resigned/terminated] as [Title].
Background: [Prior roles, relevant experience].
Compensation: [Base salary], [Bonus], [Equity], [Severance], [Other material terms].
There are no family relationships or related-party transactions with directors or executive officers, except [if any].
```

**Item 2.01 and Item 9.01 Financials**

- Apply significance tests under Regulation S-X Rule 3-05 and Article 11 (Rule 11-01) [VERIFY].
- Determine whether audited target financials and pro forma financials are required.
- If financials are not available, state that they will be filed by amendment within the Item 9.01 safe harbor period (71 calendar days after the Form 8-K due date) [VERIFY].
- Identify whether any financials are filed with the initial 8-K.

**Exhibit Index (Item 9.01(d))**

| Exhibit No. | Description | Status |
|---|---|---|
| 2.1 | Purchase agreement for [Transaction] | Filed |
| 3.1 | Amended and Restated Certificate of Incorporation | Filed |
| 10.1 | Material definitive agreement | Filed |
| 99.1 | Press release dated [Date] | Furnished |
| 99.2 | Investor presentation dated [Date] | Furnished |

**Signature Block**

```text
Pursuant to the requirements of the Securities Exchange Act of 1934, the registrant has duly caused this report to be signed on its behalf by the undersigned hereunto duly authorized.

Date: [Filing Date]

[Registrant Name]

By: __________________________
Name: [Officer Name]
Title: [Officer Title]
```

**Quality Control Checklist**

- Confirm all dates, names, and amounts match source documents.
- Ensure item numbers match the described event.
- Confirm exhibits referenced are attached and correctly numbered.
- Verify furnished vs filed treatment for Items 2.02 and 7.01.
- Ensure consistency between narrative and press release content.
- Confirm signature authority is documented or customary.

## Guidelines

- Do not include projections or opinions unless required by the item or included in furnished materials.
- Use 8-K/A for material corrections or to file delayed financials under Item 9.01.
- If requesting confidential treatment or redactions, flag Rule 24b-2 and prepare a separate application [VERIFY].
- If the disclosure includes forward-looking statements in an exhibit, include or reference appropriate cautionary language in that exhibit.
- Maintain EDGAR-compatible formatting and avoid typographical or formatting inconsistencies.
- Confirm filing deadline based on the triggering event date and Form 8-K instructions.
