---
name: investors-rights-agreement
description: >-
  Drafts a U.S. Investors' Rights Agreement for VC/private equity financings,
  aligning registration rights, information/management rights, pro rata
  rights, expenses, and termination terms with the Stock Purchase Agreement
  and charter. Use when drafting an Investors' Rights Agreement, Amended and
  Restated IRA, or VC financing governance package; trigger keywords:
  "investors' rights agreement", "IRA", "registration rights", "piggyback",
  "Form S-3", "information rights", "management rights", "pro rata", "ROFO".
tags:
  - agreement
  - corporate
  - drafting
  - transactional
---

# Investors' Rights Agreement

Produce a market-standard, internally consistent IRA tied to the financing closing.

## Prerequisites

1. **Core transaction docs** — Stock Purchase Agreement, Certificate/Charter, Voting Agreement, ROFR/Co-Sale, cap table, closing schedule.
2. **Party data** — legal names, jurisdictions, notice addresses, signature authority.
3. **Deal economics** — share classes, price, amounts, investor thresholds.
4. **Negotiated terms** — thresholds, timing, delays, cutback priority, termination triggers.
5. **Governing law + forum** — selected state and venue.
6. **Any investor-specific requirements** — ERISA management rights, special observer rights, side letters.

## Output Structure / Process

**1) Build schedules and party section**

Checklist:
- Company legal name + jurisdiction (from charter).
- Investors list for Schedule A:
  - Name
  - Address
  - Series/shares
  - Original purchase price
- Founders list for Schedule B:
  - Name
  - Address
  - Shares / class
- Effective date = closing date (match SPA).

**2) Definitions (align to SPA/Charter)**

Include at minimum:
- `Registrable Securities` with standard exclusions
- `Holder`, `Initiating Holders`
- `Major Investor` threshold
- `New Securities`, `Excluded Securities`
- `Deemed Liquidation Event` (charter)
- `Form S-3`, `Register`, `Registration Statement` (if used)

**3) Registration rights framework**

Table: key levers to fill from deal terms.

| Topic | Default Range | Input |
|---|---|---|
| Demand threshold | 25–40% of Registrable Securities | `{{DemandPct}}` |
| Demand count | 1–2 | `{{DemandCount}}` |
| Demand minimum | $5–10M offering size | `{{DemandMin}}` |
| Delay right | up to 90 days / 12 months | `{{DelayLimit}}` |
| Piggyback notice | 10–20 business days | `{{PiggybackNotice}}` |
| Cutback priority | see waterfall below | `{{CutbackOrder}}` |
| Form S-3 threshold | 10–30% | `{{S3Pct}}` |
| S-3 minimum | $1–5M | `{{S3Min}}` |
| S-3 frequency | 1–2 per 12 months | `{{S3Count}}` |

Cutback priority template:
```text
Cutback order:
1) Non-Company, non-Holder securities
2) Company securities
3) Holder Registrable Securities pro rata
```

Standard exclusions for piggyback:
- Form S-4 (M&A), Form S-8 (employee plans), reorganizations/splits.
- Other agreed exclusions (from SPA).

**4) Registration procedures**

Company obligations checklist:
- Prepare/submit registration statement and amendments.
- Provide filings, prospectus, and updates to Holders.
- Blue sky qualification where required.
- Customary legal opinions and comfort letters.
- Exchange listing.
- Underwriting agreement if applicable.
- Maintain effectiveness for distribution period.

Holder obligations checklist:
- Provide information for filings.
- Comply with prospectus delivery.
- Execute custody/lock-up (<= 180 days typical).
- Execute POA for filings as required.

Indemnification template:
```text
Company indemnifies Holders for misstatements/omissions except for Holder-furnished info.
Holders indemnify Company for Holder-furnished info.
Contribution applies if indemnity unavailable.
```

**5) Expenses allocation**

Registration Expenses (Company pays):
- SEC/blue sky fees, printing, Company counsel, auditors, listing, transfer agent.
- One selling-holder counsel (if agreed).

Selling Expenses (Holders pay pro rata):
- Underwriting discounts, commissions, brokerage, holder-specific counsel, transfer taxes.

**6) Information rights**

Minimum deliverables (if negotiated for Major Investors):
- Annual audited FS within 90–120 days of FY end.
- Quarterly unaudited FS within 45 days of quarter end.
- Annual budget within 30 days of FY start.
- Monthly statements within 30 days of month end.
- Other reasonable info for reporting/regulatory needs.

Confidentiality:
- Use for investment monitoring only.
- Standard exceptions (public, third-party, independently developed, legal compulsion).
- Withholding for competitive sensitivity with notice.

Termination (info rights):
- IPO, loss of Major Investor status, or prior to deemed liquidation event.

**7) Management rights**

Include if needed for ERISA VC operating company qualification.
Standard access:
- Reasonable access to facilities/records with notice.
- Board observer rights if no seat.
- Periodic management meetings.

Limitations:
- Advisory only; no fiduciary duty or control.
- Privilege/conflict carve-outs.

**8) Pro rata (ROFO) rights**

Process:
- Company notice 20–30 days before issuance.
- Investor election 15–20 days after notice.
- Oversubscription rights pro rata.
- Company may sell unsubscribed securities on no-better terms within 90–120 days.

New Securities definition:
- Any equity or equity-linked, including convertibles, warrants, options.

Excluded Securities (align to SPA):
- Equity plan issuances
- M&A/strategic transactions approved by board incl. preferred director
- Public offerings
- Existing conversions/exercises
- Debt/lease financings
- Sponsored research/strategic collaborations
- Any other negotiated exclusions

Termination (pro rata):
- IPO (or agreed post-IPO sunset), loss of threshold, or prior to deemed liquidation event.

**9) Termination matrix**

Table:
| Right | Terminates Upon |
|---|---|
| Registration | IPO + 5–7 years; or Rule 144 free sale; or prior to deemed liquidation |
| Information | IPO; loss of Major Investor status; or prior to deemed liquidation |
| Management | IPO; loss of Major Investor status |
| Pro rata | IPO (or post-IPO sunset); loss of Major Investor status; or prior to deemed liquidation |

Note: If using SEC Rule 144 or Rule 415, confirm accuracy. [VERIFY]

**10) Miscellaneous**

Include:
- Governing law + exclusive forum.
- Jury trial waiver (if selected; make conspicuous).
- Amendments: Company + required % of Registrable Securities; class consent for adverse changes.
- Waivers: in writing only; no implied waivers.
- Assignment: Company restricted; Holders may assign to affiliates/qualified transferees with joinder.
- Notices: methods, deemed receipt timing, update requirement.
- Severability and reformation.
- Counterparts and electronic signatures (E-SIGN compliance).
- Entire agreement clause tied to transaction documents.

## Guidelines

- Match all defined terms to SPA/Charter; do not invent new definitions.
- Keep thresholds, timing windows, and sunset periods consistent across docs.
- Ensure schedules reconcile to cap table and closing schedule totals.
- Use U.S. securities law terminology consistently (Securities Act, registration statement, prospectus).
- Avoid adding arbitration unless expressly required by deal terms.
- Flag any legal citation uncertainty with `[VERIFY]`.
- Confirm any board-approval or preferred-director consent requirements for exclusions.
