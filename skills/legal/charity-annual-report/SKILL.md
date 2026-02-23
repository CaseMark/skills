---
name: charity-annual-report
description: Drafts comprehensive Annual Reports for submission to State Charity Bureaus, ensuring compliance with state-specific charitable solicitation laws and regulatory requirements for nonprofit organizations. Extracts organizational identity, governance, financial, and programmatic data from uploaded documents, researches state-specific filing requirements, and produces a penalty-of-perjury-certified report with required attachments. Use when drafting charity bureau annual reports, nonprofit compliance filings, charitable solicitation renewals, or state charity registration renewals.
tags:
  - corporate
  - drafting
  - regulatory
  - research
  - summary
---

# Annual Report for State Charity Bureau

Drafts a filing-ready Annual Report for a State Charity Bureau with certified financials, governance disclosures, and all required attachments.

## Prerequisites

1. **Governing documents** — articles of incorporation, bylaws, board resolutions, meeting minutes
2. **Prior charity filings** — previous annual reports, charity bureau correspondence, registration certificates
3. **Financial records** — IRS Form 990 (all schedules), audited/reviewed/compiled financial statements, general ledger summary
4. **Fundraising records** — gross/net by method, donor platform exports, professional fundraiser/solicitor/co-venturer contracts
5. **Governance policies** — conflicts of interest, whistleblower, document retention

## Output Modes

| Mode | Description |
|---|---|
| **Full Compliance Package** (default) | Filing-ready narrative report with tables, attachments index, signature blocks, certification, filing instructions |
| **Form-Field Mode** | Field-by-field answers keyed to state form/portal, with source citations and optional narrative addendum |
| **Executive Briefing** | 2–3 page summary of filing status, key financials, compliance issues, and open items for board review |

## Process

### Phase 0: Pre-Draft Intake

Confirm or apply defaults (mark unconfirmed values `[ASSUMED]`):

| Item | Default if unconfirmed |
|---|---|
| Filing state | State from uploaded registration docs |
| Reporting period | Most recent completed 12-month fiscal year |
| Mandatory form/portal | Narrative format unless state form identified in research |
| Total revenue | Needed for audit/review tier — flag `[TO BE CONFIRMED]` |
| Professional fundraisers used | None unless contracts found in uploads |
| Output mode | Full Compliance Package |

Maintain an **Open Items** tracker throughout; resolve or flag each before finalizing.

### Phase 1: Source Extraction

Build an **Intake Normalization Table** reconciling data across all source documents:

| Field | Value | Source | Conflicts/Notes |
|---|---|---|---|
| Legal name / DBA(s) | | | |
| EIN / State charity reg # | | | |
| Principal & mailing address | | | |
| FYE / Reporting period | | | |
| Date of incorporation | | | |
| Tax-exempt status (501(c) type) | | | |
| Current & prior year revenue | | | |

**Edge cases to check:** short fiscal year, mid-year name/address changes, merged/successor entities.

### Phase 2: State Requirements Research

Research current rules from **official sources only** (charity bureau/AG website, statutes, admin code, filing instructions). Record source URL and publication date for every requirement.

Build a **Requirements Matrix** covering:

- Filing form number, deadline, extension availability, method (portal/mail), fee
- Audit/review/compilation revenue thresholds
- Required attachments (990, audit report, contracts, etc.)
- Professional fundraiser disclosure fields
- Certification/oath language (verbatim if prescribed), required signatories, notarization
- Governance policy attestation requirements
- Special disclosures (related-party transactions, name changes, litigation)
- Multi-state notes (URS accepted?)

Mark unconfirmed requirements `[TO BE CONFIRMED]`; conflicting sources `[CONFLICT — VERIFY WITH COUNSEL]`.

### Phase 3: Draft Core Sections

**Section 1 — Organizational Identity:** Legal name, DBA(s), EIN, registration #, addresses, website/solicitation channels, reporting period, material mid-year changes, affiliated entities.

**Section 2 — Governance:** Board/officer roster (name, title, address if required, term dates, compensation, independence status). Confirm compliance with state minimums and bylaws. Note mid-year changes, bylaw amendments, policy adoptions.

**Section 3 — Financials:** Present on identified accounting basis (accrual/cash).

| Category | Current Year | Prior Year | Variance ($) | Variance (%) |
|---|---|---|---|---|
| Contributions & grants | | | | |
| Program service revenue | | | | |
| Investment income | | | | |
| Special events (net) | | | | |
| Other revenue | | | | |
| **Total Revenue** | | | | |
| Program expenses | | | | |
| Management & general | | | | |
| Fundraising | | | | |
| **Total Expenses** | | | | |
| **Change in Net Assets** | | | | |
| Total assets / liabilities / net assets | | | | |

Include key ratios: program expense ratio (target ≥75%), fundraising efficiency, months of operating reserves.

**Section 4 — Programs & Impact:** For each major program: charitable purpose, populations served, geography, quantifiable outputs/outcomes, program expenses, volunteer hours. Synthesize connection to mission.

**Section 5 — Fundraising & Compliance:**

- Fundraising by method (gross, direct costs, net)
- Professional fundraiser/solicitor/co-venturer table (entity, role, contract dates, amounts paid/raised, state registration ID, contract attached)
- Registration status, multi-state solicitation, audit compliance, governance policy attestation
- Format each requirement as: state the legal requirement → state compliance status

### Phase 4: Attachments Index

| Exhibit | Description | Date | Required? | Included? |
|---|---|---|---|---|
| A | IRS Form 990 (all schedules) | | | |
| B | Audit/review/compilation report | | | |
| C | Professional fundraiser contracts | | | |
| D | Board resolution approving report | | | |
| E | Articles of incorporation/amendments | | | |

Cross-check every exhibit against the Requirements Matrix.

### Phase 5: Execution Package

**Certification language:** Insert verbatim state-prescribed language. If unavailable, use placeholder:

> `[TO BE CONFIRMED]` "I declare under penalty of perjury under the laws of [STATE] that I have examined this Annual Report, including all accompanying schedules, statements, and attachments, and to the best of my knowledge and belief, it is true, correct, and complete."

**Signature blocks:** Per state requirements and bylaws (President/Chair, Treasurer/CFO typical). Include notarization block only if required.

**Filing instructions:** Deadline, extension process, method (portal URL/mailing address), fee and payment method, original/electronic signature requirements, number of copies.

### Phase 6: Refinement Options

Offer the user: convert to Form-Field Mode, strengthen program narrative, adjust financial presentation, expand fundraiser disclosures, add multi-state appendix, produce Executive Briefing, generate cover letter.

## Quality-Control Checklist

- [ ] All unconfirmed values labeled `[ASSUMED]` or `[TO BE CONFIRMED]`
- [ ] Requirements Matrix complete with official citations and verification dates
- [ ] Filing deadline correctly calculated from FYE
- [ ] Audit/review tier correctly applied to organization's revenue
- [ ] Legal name, EIN, and registration # identical across all sections
- [ ] Revenue/expense totals reconcile to financial statements and Form 990
- [ ] Functional expense categories align with 990 Part IX
- [ ] Financial ratios arithmetically verified
- [ ] All required attachments indexed and cross-referenced in narrative
- [ ] Certification language is state-correct (verbatim where required)
- [ ] Correct signatories identified per state law and bylaws
- [ ] Notarization requirement confirmed or ruled out
- [ ] Consistent date format, financial formatting, and professional tone throughout
- [ ] No unmarked placeholder text remains

## Guidelines

- **Accuracy is paramount** — report is certified under penalty of perjury; flag any data gap rather than guess
- **Official sources only** for state requirements — AG/charity bureau websites, statutes, admin code
- **Reconcile across documents** — name, EIN, financials must match between 990, audit, and narrative
- **State-specific variation** — never assume one state's rules apply to another; each state has distinct thresholds, forms, deadlines, and disclosure requirements
- **Professional fundraiser scrutiny** — these disclosures are a primary enforcement focus; verify contract compliance
- **Multi-state awareness** — if evidence suggests solicitation in other states, note registration obligations even if out of scope
