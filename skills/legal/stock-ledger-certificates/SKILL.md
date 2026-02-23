---
name: stock-ledger-certificates
description: >-
  Drafts a complete stock ledger and stock certificate package for U.S.
  corporations, including a master equity ledger table, formal certificate
  templates, transfer procedures, and officer certification block. Extracts
  capitalization structure, authorized share classes, par value, and
  historical issuances from uploaded formation documents. Use when forming a
  corporation, issuing initial shares, or establishing official equity
  ownership records. Trigger keywords: stock ledger, stock certificates,
  equity records, share issuance, corporate capitalization, certificate of
  stock, corporate formation.
tags:
  - agreement
  - corporate
  - drafting
---

# Stock Ledger and Certificates

Drafts the official equity ownership package for a corporation: master stock ledger, individual certificate templates, and certification block.

## Prerequisites

1. **Articles of Incorporation** — legal name, state of incorporation, authorized share structure, par value, share classes
2. **Bylaws or Organizational Minutes** — authorized officers, any transfer restrictions
3. **Shareholders' Agreement / Buy-Sell Agreement** (if any) — ROFR provisions, transfer restrictions
4. **Existing stock records** (if any) — prior issuances, certificate numbers, historical transactions

## Output Structure

### 1. Document Header

| Field | Content |
|---|---|
| Corporation Name | Full legal name |
| State of Incorporation | [State] |
| Date of Incorporation | [Date] |
| Document Title | Stock Ledger and Stock Certificates |
| Prepared As Of | [Current date] |
| Purpose Statement | Official record of all equity ownership of the corporation |

---

### 2. Authorized Capital Structure

State total authorized shares by class:

| Class | Shares Authorized | Par Value | Authorizing Document |
|---|---|---|---|
| Common | [#] | $[X] / No par value | Articles of Incorporation, §[X] |
| Preferred | [#] | $[X] / No par value | Articles of Incorporation, §[X] |

---

### 3. Stock Ledger Table

| Cert. No. | Date Issued | Shareholder (Full Legal Name) | Shares | Class | Consideration | Transfer / Notes |
|---|---|---|---|---|---|---|
| 001 | [Date] | [Name] | [#] | Common | $[X] cash / [description] | — |
| 002 | [Date] | [Name] | [#] | Common | $[X] cash / [description] | — |

- Number certificates sequentially starting at **001**
- Populate from uploaded documents; flag any gaps or inconsistencies
- Cancelled certificates: mark column "CANCELLED — [date], replaced by Cert. No. [X]"

---

### 4. Stock Certificate Template

Each certificate must include:

- [ ] Unique certificate number (matching ledger)
- [ ] Corporation's full legal name and state of incorporation
- [ ] Shareholder's complete legal name and address
- [ ] Number of shares in **both numerals and written words** (e.g., "100 — One Hundred shares")
- [ ] Class of stock
- [ ] Date of issuance
- [ ] Statement: *"Subject to the Corporation's Bylaws and any applicable Shareholder Agreement"*
- [ ] Corporate seal space or notation "Corporate Seal"
- [ ] Signature lines: **President/CEO** + **Secretary** (printed name and title below each)

---

### 5. Transfer Procedure Summary

Include as a standing instruction block:

> **To transfer shares:** Surrendering shareholder must (1) endorse the original certificate or execute a separate stock power/assignment, (2) deliver endorsed certificate and transfer documentation to the corporation, (3) corporation cancels old certificate, issues new certificate, and updates the ledger. Transfer restrictions in any shareholders' agreement or bylaws must be satisfied prior to recording.

---

### 6. Officer Certification Block

> *"The undersigned officers of [Corporation Name] hereby certify that the foregoing Stock Ledger accurately reflects all issuances and transfers of the corporation's capital stock as of [date]."*

| | |
|---|---|
| _________________________ | _________________________ |
| [Name], President/CEO | [Name], Secretary |
| Date: __________________ | Date: __________________ |

---

## Guidelines

- **Records location**: Ledger must be maintained at the corporation's principal office or registered agent's office per applicable state business corporation act
- **Shareholder inspection**: Shareholders have statutory inspection rights in most U.S. states — do not include confidential side letters in the main ledger
- **Multiple classes**: Clearly distinguish classes in both ledger and certificates; reflect rights/preferences from articles
- **Securities law**: Note on each certificate or as a legend if shares are restricted securities (e.g., Section 4(a)(2) exemption): *"These securities have not been registered under the Securities Act of 1933..."* [VERIFY applicable legend with counsel]
- **State variance**: Certificate content and ledger requirements vary by state — flag if state of incorporation is not evident from documents and prompt user to confirm compliance with applicable Business Corporation Act
- **S-corp**: Flag if entity is S-corp; note that shares may only be held by eligible shareholders and restrictions on number/type of shareholders apply
