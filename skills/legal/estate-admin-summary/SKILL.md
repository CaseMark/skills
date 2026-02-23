---
name: estate-admin-summary
description: Generates structured summaries of estate administration proceedings from probate documents, wills, asset inventories, creditor claims, and distribution records. Covers decedent info, asset catalog, creditor status, tax compliance, beneficiary communications, legal hurdles, and remaining tasks. Use when summarizing estate progress, preparing status reports, onboarding to a probate matter, or briefing executors and beneficiaries.
tags:
  - summarization
  - summary
  - transactional
---

# Estate Administration Summary

Produces a comprehensive snapshot of an estate administration's current status, completed actions, and outstanding matters from available probate documents.

## Prerequisites

1. **Governing instrument** — will, trust, or intestacy determination
2. **Probate filings** — petition, letters testamentary/administration, court orders
3. **Asset inventory** — appraisals, account statements, real property records
4. **Creditor claims file** — filed claims, approvals, rejections, payment records
5. **Tax records** — estate tax returns, final individual returns, fiduciary returns
6. **Distribution records** — interim/partial distributions, receipts
7. **Correspondence** — beneficiary notices, creditor communications, court accountings

## Output Structure

### 1. Estate Identification

| Field | Detail |
|---|---|
| Decedent | Name, date of death |
| Jurisdiction | State/county of administration |
| Case/Matter No. | If applicable |
| Personal Representative | Name, relationship, date appointed |
| Governing Instrument | Will / Trust / Intestacy |
| Date Administration Opened | — |

### 2. Asset Inventory

Organize by category. For each significant asset:

| Category | Asset Description | Appraised/Est. Value | Status | Intended Beneficiary |
|---|---|---|---|---|
| Real Property | | | Held / Sold / Transferred | |
| Financial Accounts | | | Liquidated / Open | |
| Personal Property | | | Distributed / Held | |
| Business Interests | | | Valued / Pending | |

- Flag assets with valuation challenges, special handling requirements, or disputes
- For distributed assets: note date, recipient, value transferred

### 3. Creditor Claims

| Creditor | Amount Claimed | Status | Notes |
|---|---|---|---|
| | | Approved / Rejected / Paid / Pending | |

Include:
- Claims filing deadline and whether expired
- Priority debts: funeral expenses → administration costs → taxes → secured obligations
- Disputed claims: basis for dispute, negotiation/litigation status

### 4. Tax Compliance

| Return | Required? | Filed? | Status |
|---|---|---|---|
| Federal estate tax (Form 706) | | | |
| State estate/inheritance tax | | | |
| Decedent's final income tax | | | |
| Fiduciary income tax (Form 1041) | | | |

- Note outstanding liabilities, pending audits, or anticipated issues

### 5. Legal Hurdles & Challenges

For each issue document:
- **Nature** — will contest, beneficiary dispute, omitted heir claim, estate litigation, tax controversy, regulatory issue
- **Parties involved**
- **Procedural status**
- **Potential impact** on administration timeline and distributions

### 6. Administration Timeline

Chronological milestones:

- [ ] Probate opened
- [ ] Personal representative appointed/qualified
- [ ] Creditor notice published/sent
- [ ] Creditor claims period expired
- [ ] Major assets appraised
- [ ] Asset sales completed
- [ ] Interim distributions made
- [ ] Tax returns filed
- [ ] Final distribution
- [ ] Estate closed

Mark completed items with dates; note delays or inactivity gaps.

### 7. Beneficiary Status

- All beneficiaries identified and located?
- Minors or incapacitated persons requiring guardianship/conservatorship procedures?
- Objections or concerns raised?
- Accountings provided — formal (court-filed) or informal, with dates

### 8. Remaining Tasks & Projected Timeline

- List each outstanding task required before closure
- Identify blocking dependencies (e.g., pending litigation, tax clearance)
- Estimate realistic completion timeline with acceleration/delay factors

## Guidelines

- Cite specific source documents for all factual assertions
- Acknowledge uncertainties in valuations, claim amounts, or legal outcomes — do not speculate
- Flag areas needing additional investigation or documentation
- Format all monetary amounts, dates, and legal citations consistently
- State-specific creditor claims periods and notice requirements vary — identify the applicable statute
- Use neutral, objective tone suitable for court filings, client communications, or case management systems
- If governing instrument is ambiguous on distribution, note the interpretive issue without resolving it
