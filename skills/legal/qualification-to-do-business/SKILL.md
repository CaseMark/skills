---
name: qualification-to-do-business
description: >-
  Drafts U.S. foreign-corporation qualification filings (Application for
  Certificate of Authority) for registration in a target state. Use when
  setting up a non-domiciliary corporation to transact business, checking
  qualification triggers, confirming name availability, preparing
  officer/director and registered-agent data, assembling good-standing
  support, and producing filing-ready execution and fee-ready package
  artifacts. Trigger keywords: certificate of authority, qualification to do
  business, foreign corporation, register to do business, registered agent
  appointment.
tags:
  - agreement
  - corporate
  - drafting
  - research
---

# State Qualification to Do Business

Produces a state-specific Certificate of Authority packet for a foreign corporation seeking legal authorization to transact business in a U.S. state.

## Prerequisites

1. Corporate formation package: incorporation certificate/articles, bylaws or equivalent governance charter, and current officer/board authorization evidence.
2. Exact legal name as filed in the home jurisdiction, including punctuation and entity designator.
3. Target-state research plan: required form/version, filing method, fee, signature, and authentication requirements.
4. Name-availability result in target state, including any alternatives or assumed-name requirements.
5. Home-jurisdiction certificate of good standing/existence (or equivalent).
6. Current principal officers/directors and intended in-state activities to evaluate filing necessity.

## Output Structure / Process

### 1) State compliance snapshot (mandatory prefill)

| Item | Required output |
|---|---|
| Target state | Exact state and filing office/program |
| Qualification required? | Yes/No with legal basis or exception note |
| Official form available | Yes/No + form title/version |
| Exact filing name | Legal name + any alt/assumed name requirement |
| Registered agent model | Required, available, physical address |
| Consent format | Signature language required by state |
| Notarization/declaration | Required yes/no; text if required |
| Certificate authentication | Apostille/consular rule if applicable |
| Fee | Current filing fee and payment channel |
| Submission channel | Online/mail/in-person + filing ID/portal |

### 2) Core data checklist

| Field | Capture rule |
|---|---|
| Legal name | Match formation document exactly |
| Formation jurisdiction | State or country + exact incorporation date |
| Duration | Perpetual or fixed term |
| Principal office address | Physical address (no PO box if disallowed) |
| Registered office | Physical in target state |
| Registered agent | Full legal name + address + availability statement |
| Officers | Full names, titles, business addresses |
| Directors | Full names + addresses |
| Authorized filer | Title and authority source |
| Filing date | Current date unless state requires specific effective date |

### 3) Drafting process

1. Build application headings and statutory sections: identification, in-state presence, registered office/agent, governance disclosure, certification, and signature block.
2. Populate required identity data and in-state contact information from source records only.
3. Insert authorized filing officer signature block and state-specific attestation or declaration text.
4. Add registered-agent consent block using exact required language or closest compliant equivalent.
5. Append filing checklist and document index with all exhibits and fee instructions.
6. Add transacting-business risk note when applicability is uncertain.

### 4) Deliverable templates

```text
Entity Legal Name:
Formation Jurisdiction:
Formation Date:
Principal Office:
Target State:
Registered Office:
Registered Agent:
Registered Agent Street Address:
Authorized Signatory:
Signatory Title:
Execution Date:
```

```text
Officers:
[Title] | [Full Name] | [Business Address]
Directors:
[Title/Role] | [Full Name] | [Business Address]
```

```text
Filing Package:
- Application (completed form or drafted equivalent)
- Certificate of Good Standing/Existence
- Name Reservation/Assumed Name documents (if required)
- Filing fee authorization/payment item
- Any state-required affidavits or declarations
```

### 5) Validation gates (before final output)

- No placeholders remain.
- Registered agent consent present and complete.
- Good-standing certificate recency checked against target-state tolerance [VERIFY].
- Officer/director rosters current and sourced.
- Notary or declaration block matches state requirement.
- Fee amount and payment instructions verified from latest state guidance.

## Guidelines

- Use home-state and target-state authority directly; do not assume cross-state uniformity.
- Preserve exact legal name capitalization, punctuation, and designator.
- Do not infer missing officer/agent details.
- If foreign-country incorporation is involved, evaluate apostille or authentication chain [VERIFY].
- If activity likely exempt from qualification (e.g., isolated transaction/interstate activity-only scenarios), include an issue flag for legal review [VERIFY].
- If qualification is not yet required, output reasoned denial memo instead of a filing package.
