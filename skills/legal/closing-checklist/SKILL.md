---
name: closing-checklist
description: Drafts comprehensive M&A closing checklists that function as project management and risk mitigation instruments for corporate acquisitions. Covers corporate authorizations, transaction documents, third-party consents, regulatory filings, funds flow, and post-closing obligations. Use when coordinating closings for mergers, acquisitions, stock purchases, asset deals, or any corporate transaction requiring multi-party document tracking.
tags:
  - checklist
  - corporate
  - drafting
  - transactional
---

# M&A Closing Checklist

Generates a transaction-specific closing checklist that tracks every document, approval, consent, and action item from deal signing through post-closing compliance.

## Prerequisites

1. **Definitive transaction agreement** — purchase agreement, merger agreement, or equivalent governing document with all schedules
2. **Transaction structure** — stock purchase, asset purchase, merger, or other arrangement
3. **Party information** — full legal names of buyer, seller, target (if distinct), escrow agent, and other parties
4. **Closing logistics** — anticipated date, time (with timezone), location or virtual platform
5. **Material contracts list** — contracts with change-of-control or consent provisions

## Output Structure

### Document Header

```
CLOSING CHECKLIST
Acquisition of [Target] by [Buyer]
Closing Date: [Date] | Time: [Time + TZ]
Closing Method: [In-person at ___] / [Virtual via ___]
```

### Party Legend

| Abbrev. | Party |
|---------|-------|
| BC | Buyer's Counsel |
| SC | Seller's Counsel |
| B | Buyer |
| S | Seller |
| Co | Company (if distinct from Seller) |
| EA | Escrow Agent |

Expand as needed for lenders, accountants, regulatory bodies, landlords.

### Checklist Matrix Format

Every item uses this structure:

| # | Description | Responsible | Cross-Ref (§) | Status |
|---|-------------|-------------|----------------|--------|

Status stages: `Draft → Review → Negotiation → Execution → Delivered`

### Section I — Corporate Authorization & Organizational Documents

- [ ] Certificates of good standing / existence (buyer + seller jurisdictions, dated ≤30 days pre-closing)
- [ ] Board resolutions authorizing transaction (both parties)
- [ ] Shareholder / member approval (if required by governing docs, state law, or securities terms)
- [ ] Certified copies of organizational documents (articles/certificate of incorporation, bylaws/operating agreement)
- [ ] Evidence of any required preferred shareholder, option holder, or warrant holder consent
- [ ] Secretary's certificates attaching and authenticating all organizational documents and resolutions

### Section II — Principal Transaction Documents

**All structures:**
- [ ] Definitive purchase/merger agreement (fully executed with all disclosure schedules)
- [ ] Escrow agreement (if applicable — confirm amount, duration, release conditions, claims procedures)

**Asset purchases — add:**
- [ ] Bill of sale (tangible personal property)
- [ ] Assignment and assumption agreement (contracts, IP licenses, permits, assumed liabilities)
- [ ] Real property deeds / transfer documents
- [ ] IP assignment agreements (patents, trademarks, copyrights, domains — with registration formalities)

**Stock purchases — add:**
- [ ] Stock certificates with legends (or book-entry transfer documentation)
- [ ] Stock power / transfer instruments
- [ ] Resignations of outgoing directors/officers; appointments of replacements

**Mergers — add:**
- [ ] Certificate/articles of merger (ready for filing with secretary of state)
- [ ] Director/officer resignations and appointments

### Section III — Ancillary Agreements

- [ ] Legal opinions (seller's counsel + buyer's counsel) — covering existence, authority, enforceability, no conflicts
- [ ] Payoff letters + lien releases for all outstanding indebtedness (bank loans, equipment financing, shareholder loans)
  - Each must specify: exact payoff amount, wire instructions, commitment to deliver UCC-3 terminations / mortgage releases
- [ ] Employment agreements / offer letters for continuing key employees
- [ ] Non-competition / non-solicitation agreements (per scope, duration, geography in purchase agreement; comply with applicable state enforceability law)
- [ ] Transition services agreement (if applicable — scope, duration, fees, SLAs, termination rights)
- [ ] Other commercial agreements (supply, distribution, licensing)

### Section IV — Consents, Approvals & Regulatory

- [ ] Third-party contract consents (identify all change-of-control / assignment restrictions from material contracts)
- [ ] HSR Act filing (if thresholds met) — track: filing date, additional information requests, waiting period expiration
- [ ] State antitrust / competition filings
- [ ] Industry-specific regulatory approvals (healthcare, financial services, telecom, etc.)
- [ ] Foreign investment review (CFIUS or equivalent, if applicable)
- [ ] Landlord consents for lease assignments (submit early — landlords require extended review)
- [ ] Franchisor / licensor approvals

### Section V — Closing Certificates & Officer Deliverables

- [ ] Seller's officer certificate — rep/warranty bring-down, covenant compliance, condition satisfaction
- [ ] Buyer's officer certificate — parallel certifications
- [ ] Secretary's certificates (both parties) — authenticating org docs, resolutions, incumbency
- [ ] Bring-down / MAC certificate — no material adverse change since signing
- [ ] Tax certificates:
  - IRS Form W-9 (domestic seller)
  - FIRPTA certificate under IRC § 1445 (if seller is foreign person)
  - State withholding certificates as applicable

### Section VI — Funds Flow & Financial Settlement

Prepare a **funds flow memorandum** covering:

| Line Item | Amount | Payee | Wire Instructions |
|-----------|--------|-------|-------------------|
| Base purchase price | | | |
| Working capital adjustment (estimated) | | | |
| Escrow deposit (indemnification) | | | |
| Escrow deposit (earnout/holdback) | | | |
| Creditor payoffs (itemize each) | | | |
| Seller transaction expenses | | | |
| Buyer transaction expenses | | | |
| Transfer taxes / recording fees | | | |
| **Net proceeds to Seller** | | | |

- [ ] Wire transfer instructions verified (implement verbal callback confirmation — fraud prevention)
- [ ] Closing statement / settlement statement for tax reporting

### Section VII — Post-Closing Obligations

- [ ] File certificate/articles of merger (if merger — coordinate timing for effective time control)
- [ ] Press release / public announcement (reviewed and approved by both parties; securities law compliance if public company)
- [ ] Counterparty notices (customers, suppliers, landlords, lenders) — prepare templates by recipient category
- [ ] Governmental filings:
  - HSR final notifications
  - Transfer tax returns and payments
  - Bulk sale compliance (if applicable under state law)
  - Business license/permit updates
  - Tax authority notifications (sales tax, employment tax)
- [ ] Corporate record updates (stock ledger / membership records, minute books)
- [ ] Asset recording on buyer's books; assumed liability entries

## Guidelines

1. **Cross-reference every item** to the specific purchase agreement section creating the obligation
2. **Map dependencies** — funds flow requires all payoff letters; closing certificates require covenant completion; identify and sequence accordingly
3. **Build lead time** for items requiring third-party cooperation (landlord consents, regulatory approvals, lien releases)
4. **Version control** — date/time stamp each circulation; designate one party to maintain the master checklist
5. **Jurisdiction-specific requirements** — research state-level variations for transfer taxes, bulk sale laws, corporate formalities based on where parties are organized, where assets are located, and where business operates
6. **Status update protocol** — establish frequency of checklist circulation and escalation procedures for items falling behind
7. **Wire fraud prevention** — require verbal verification of any changes to wire instructions; confirm receipt of all fund transfers
8. **Adapt sections** based on transaction structure — omit inapplicable sections rather than including placeholder content
