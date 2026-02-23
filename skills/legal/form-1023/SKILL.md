---
name: form-1023
description: Drafts IRS Form 1023 Application for Recognition of Exemption under Section 501(c)(3). Analyzes organizational documents, finances, governance, and operations to produce a complete, internally consistent application maximizing likelihood of IRS approval. Use when forming non-profit entities, applying for tax-exempt status, seeking 501(c)(3) recognition, or preparing exemption applications.
tags:
  - corporate
  - drafting
  - regulatory
---

# IRS Form 1023 — Application for Recognition of Exemption

Drafts a complete, submission-ready Form 1023 application for Section 501(c)(3) tax-exempt status, ensuring internal consistency across all sections and compliance with Treasury Regulations.

## Prerequisites

1. **Articles of incorporation / trust instrument** — with purpose and dissolution clauses
2. **Bylaws or operating agreement**
3. **EIN confirmation** (CP 575 or equivalent)
4. **Financial statements** — actuals for up to 3 prior years, or proposed budgets for 2 future years if pre-operational
5. **Board/officer roster** — names, titles, addresses, compensation details
6. **Program descriptions** — for all current and planned activities
7. **Conflict of interest policy** (if adopted)
8. **Related-entity information** — parent, subsidiary, affiliate, or predecessor details

## Output Structure

### Part I — Organizational Identity

Extract and verify against organizing documents:

| Field | Source |
|---|---|
| Legal name (exact match to articles) | Articles of incorporation |
| Mailing address | Client intake |
| EIN | IRS confirmation |
| Accounting period end month | Bylaws / board resolution |
| Contact person + authority | Client intake |
| Entity type (corp / trust / assoc.) | Articles |
| Date of formation | Articles / state filing |

### Part II — Organizing Document Review

**Threshold check — flag failures before proceeding:**

- [ ] Purpose clause limits activities to one or more 501(c)(3) purposes (charitable, religious, educational, scientific, literary, public safety testing, amateur sports, prevention of cruelty)
- [ ] Dissolution clause directs remaining assets to a 501(c)(3) org or government entity for public purposes
- [ ] No express authorization of non-exempt activities

If either clause is deficient, draft amendment language per Rev. Proc. 82-2 [VERIFY] and IRS model provisions before continuing.

### Part III — Activity Narrative

For each significant activity, document:

| Element | Detail Required |
|---|---|
| Description | Specific nature, methods, frequency |
| Beneficiaries | Who is served; charitable class or public |
| Exempt purpose | Which 501(c)(3) category it advances |
| Resources | % of time, budget, staff allocated |
| Revenue | Fees charged, if any; sliding scale / charity care |
| Outcomes | Measurable results or planned metrics |

Order activities by resource allocation (largest first). For pre-operational orgs, include implementation timeline with milestones.

**Private benefit screen for each activity:**
- Selection criteria based on charitable need or exempt criteria (not private relationships)
- Fees set to ensure accessibility; document financial assistance programs
- No commercial-equivalent operations without distinguishing exempt characteristics

### Part IV — Financial Data

**Operational orgs:** Statement of revenues/expenses + balance sheet for current year and 3 preceding years (or each year of existence).

**Pre-operational orgs:** Proposed budgets for current year + 2 succeeding years.

| Revenue Categories | Expense Categories |
|---|---|
| Contributions & grants | Program services |
| Program service revenue | Management & general |
| Investment income | Fundraising |
| Fundraising proceeds | Capital expenditures |
| Other income | Other |

Flag and explain:
- Unrelated business income > 15% of total revenue
- Related-party transactions
- Significant year-over-year changes
- Fundraising costs exceeding 35% of contributions

### Part V — Governance & Compensation

For each officer, director, trustee, key employee, and anyone compensated >$100K:

| Field | Required |
|---|---|
| Name, title, address | Yes |
| Total compensation (all forms) | Yes |
| Hours/week | Yes |
| Related to other listed persons? | Yes |

**Compensation reasonableness documentation:**
- [ ] Comparability data used (similar orgs, independent surveys)
- [ ] Approved by independent board members without conflicts
- [ ] Contemporaneous documentation of deliberation

**Related-party transactions:** For each, state business purpose, fair-market-value basis, and approval process.

### Part VI — Membership & Beneficiary Structure

If membership org: describe categories, voting rights, dues, and how structure serves exempt (not private) purposes.

### Part VII — Organizational Relationships

For each related entity (predecessor, parent, subsidiary, affiliate):

| Field | Detail |
|---|---|
| Name + EIN | — |
| Relationship type | Control, support, shared governance |
| Asset transfers | Date, nature, value |
| Shared resources | Facilities, employees, cost allocation method |

### Part VIII — Specific Activity Compliance

| Activity | Required Disclosure |
|---|---|
| **Political campaign intervention** | Must be zero. Absolute prohibition — any activity = denial. |
| **Lobbying** | Disclose extent (time + expenditure). If material, evaluate §501(h) election for expenditure-test safe harbor. |
| **Grants to individuals** | Selection criteria, application process, monitoring, Schedule H |
| **Grants to organizations** | Verification of recipient exempt status, oversight procedures |
| **Fundraising / gaming** | Frequency, revenue, expenses, state/local law compliance |

### Part IX — Schedule Determination

Complete only applicable schedules:

| Schedule | Trigger |
|---|---|
| A — Churches | Primary purpose is religious worship/assembly |
| B — Schools | Educational institution with enrolled student body |
| C — Hospitals | Medical services or medical research |
| D — Supporting orgs | §509(a)(3) relationship |
| E — Late filers | Filed >27 months after formation; explain delay |
| F — Homes for elderly/handicapped | Residential facility operations |
| G — Successor funds | Community trust or successor fund |
| H — Scholarship orgs | Grants to individuals for education |

### Part X — User Fee & Execution

- Calculate 4-year average gross receipts to determine fee tier
- Include payment proof (check, money order, or Form 8718)
- Signature under penalty of perjury by authorized officer/director/trustee with printed name, title, and date

## Deliverable Format

1. **Complete Form 1023** — organized by IRS form section numbers, all applicable schedules included
2. **Cover memorandum** summarizing:
   - Key application positions
   - Items requiring board action (e.g., document amendments, policy adoptions)
   - Potential IRS inquiry areas with recommended responses
   - Next steps and timeline

## Guidelines

- Present concrete facts, not conclusory legal statements — never write "the organization is operated exclusively for charitable purposes" without supporting specifics
- Ensure absolute internal consistency across narrative, financials, governance, and organizing documents
- Flag any organizing document deficiency as a threshold blocker
- All related-party transactions require affirmative justification
- 27-month filing deadline from formation date controls retroactive exemption eligibility
- If §501(h) lobbying election is advisable, recommend it explicitly with expenditure-limit analysis
- Mark any uncertain statutory or regulatory citations with [VERIFY]
- Do not include political campaign activity under any framing — prohibition is absolute
