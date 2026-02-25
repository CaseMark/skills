---
name: fundraiser-contract-compliance
description: >
  Audits professional solicitor, fundraising counsel, and commercial co-venturer
  contracts for state charitable solicitation compliance. Classifies fundraising
  relationships, verifies vendor registration, extracts compensation and
  custody-of-funds terms, checks state-mandated contract clauses, and produces
  disclosure-ready narratives, gap logs, and audit evidence packages for annual
  charity reports. Use when reviewing fundraiser agreements, preparing state
  charity filings, onboarding fundraising vendors, auditing charitable
  solicitation compliance, or when a user mentions professional solicitor
  contracts, co-venturer filings, CHAR007, CT-2CF, or Schedule G disclosures.
tags:
  - analysis
  - corporate
  - drafting
  - regulatory
---

# Professional Fundraiser Contract Compliance Check

## Why This Skill Exists

Charitable solicitation regulation is entirely state-based, with each state drawing different lines between professional solicitors, fundraising counsel, and commercial co-venturers — and attaching materially different registration, contract-filing, and disclosure obligations to each classification. Misclassifying a relationship (treating a solicitor as mere counsel when the vendor actually solicits and handles funds) is one of the most common compliance failures, and it cascades: wrong registration, missing contract filings, incorrect annual report disclosures, and potential solicitation suspensions. This skill produces a structured audit that correctly classifies each relationship, verifies registrations, extracts disclosure data, and maps every contract clause against state-mandated requirements.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft." Gather:

1. **States in scope** — where the charity is registered and/or solicits
2. **Contract documents** — executed agreements, amendments, SOWs, exhibits, fee schedules
3. **Filing target(s)** — annual report/renewal, campaign notice, co-venturer filing, etc.
4. **Operational artifacts** — donation flow diagrams, processor agreements, bank deposit controls (if available)
5. **Registration IDs** — fundraiser/solicitor/co-venturer and charity registration numbers per state (if known)
6. **Solicitation start date** — needed for Notice of Intent / contract filing deadlines

**If the user doesn't respond**, apply and clearly label these defaults: all states where charity is registered; annual report/renewal filing target; highest-risk classification until clarified; no operational artifacts available. Mark missing items in "Open Items / Needed Inputs."

---

## Step 1: Classify Relationship and Verify Registration

### Relationship Classification

| Type | Key Markers | Regulatory Burden |
|---|---|---|
| **Professional Solicitor** | Directly solicits donations on behalf of charity; may handle funds, donor data, scripts; paid fee/percent/retainer | Highest — registration, contract filing, campaign financial reporting, point-of-solicitation disclosures |
| **Fundraising Counsel** | Advises, plans, manages campaigns; does NOT directly solicit or take custody of funds | Moderate — if counsel solicits or takes custody, most states reclassify as solicitor |
| **Commercial Co-Venturer** | For-profit ties purchase/use of its goods to charitable benefit ("$1 per sale goes to X") | Focused on advertising disclosures (benefit amount, duration, charity ID) and accounting to charity |
| **Platform / Processor / Vendor** | Donation platform, payment processor, influencer/affiliate | May become solicitor or co-venturer depending on marketing claims and solicitation control |

> **If classification is ambiguous or mixed, treat as highest-risk category until clarified by counsel.**

### Registration Verification Matrix

| Data Point | Contract Ref | Extracted Value | Verification Source | Status |
|---|---|---|---|---|
| Legal name | Preamble | | State registry | Confirmed / Mismatch |
| DBA / trade name | | | | |
| Principal business address | | | | |
| State of formation / entity type | | | Secretary of State DB | |
| Registration No. (per state) | | | State DB (e.g., NY FR-No, CA CT-No) | Current / Expired |
| Bond posted (if required) | | | State bond registry | Y / N / N/A |
| Charity's own registration | | | State DB | Current / Expired |

---

## Step 2: Extract Contract Data

### Disclosure Data Extraction Table

Complete one row per **vendor × campaign × contract/SOW**:

| Category | Fields to Extract |
|---|---|
| **Parties** | Legal names, addresses, entity types |
| **Classification** | Solicitor / counsel / co-venturer / other |
| **Campaign** | Name/ID, dates, services, whether "solicitation" occurs |
| **Compensation** | Type (%, flat, retainer, per-call, CPM); exact percentage + base (gross vs. net); minimums/guarantees; expense allocations |
| **Custody of Funds** | Who receives funds first; deposit method (lockbox/joint/vendor account); deposit timing; remittance timing; segregation; deductions before remittance |
| **Other Terms** | Charity name/logo use; donor data ownership; records/inspection rights; script/materials approval; governmental filing responsibilities; cancellation rights; subcontractors; insurance/indemnity |

### Funds Flow Map

Document for each arrangement:

1. Donor payment methods
2. Donation intake entity (vendor / platform / charity)
3. Processor merchant of record
4. Deposit account owner + bank + account type (operating / trust / segregated)
5. Timing: deposit within ___ days; remittance within ___ days
6. Deductions before remittance
7. Reconciliation controls

**Red flags:**
- Vendor receives checks payable to vendor (not charity)
- Commingled accounts
- Remittance timing unstated
- Charity lacks bank-view or reconciliation rights
- No segregation of charitable funds

---

## Step 3: Mandated-Clause Compliance Audit

Check each contract against this baseline. **Verify exact requirements per state statute.**

**A. Parties, Scope & Campaign**
- [ ] Charity and vendor clearly identified (legal names, addresses)
- [ ] Services defined; whether vendor will solicit contributions
- [ ] Campaign(s) and geographic scope specified

**B. Compensation**
- [ ] Compensation stated clearly (%, fees, calculation base)
- [ ] "Gross receipts" vs. "net proceeds" defined
- [ ] Expenses and cost allocations defined
- [ ] Possible to compute % of gross contributions charity retains

**C. Custody of Funds (High Priority)**
- [ ] Who has custody/control at each step
- [ ] If vendor receives funds: segregation required, deposit/remittance timing stated
- [ ] Cash/check handling, endorsements, payable-to instructions addressed
- [ ] Refunds/chargebacks and processor fees addressed

**D. Term & Cancellation**
- [ ] Term and renewal provisions clear
- [ ] Charity termination rights included
- [ ] Statutorily required cancellation right present (commonly 10–15 days; CA/NY require specific windows) [VERIFY per state]

**E. Recordkeeping & Audit**
- [ ] Vendor must maintain campaign records (commonly 3–7 years)
- [ ] Charity access/inspection rights included
- [ ] Periodic accountings required (frequency and content defined)
- [ ] Written financial report required after campaign end (commonly 90 days) [VERIFY per state]

**F. Solicitation Materials & Disclosures**
- [ ] Charity approval of scripts/materials required before use
- [ ] Point-of-solicitation disclosures addressed (solicitor name, charity name, % retained)
- [ ] Co-venture ads include: benefit amount/%, campaign duration, charity identity [VERIFY per state]

**G. Registration & Filings**
- [ ] Vendor represents current registration/licensing
- [ ] Registration numbers and renewal evidence required
- [ ] Responsibility for state filings/notices allocated
- [ ] Pre-solicitation filing deadlines referenced (commonly 10–20 days before start)

**H. Subcontractors**
- [ ] Subcontracting requires charity consent
- [ ] Subs must meet same registration/recordkeeping requirements

**I. Data & Privacy**
- [ ] Donor data ownership and permitted use addressed
- [ ] Unauthorized sale/rental of donor lists prohibited
- [ ] Security measures and breach notification included

### State-Specific Clause Matrix

| State | Relationship Type | Statute | Required Clauses | Cancellation Right | Financial Report Deadline | Required Filings |
|---|---|---|---|---|---|---|
| CA | | Bus. & Prof. Code §§ 17510+ [VERIFY] | | | | CT-1/CT-2 series |
| NY | | Exec. Law Art. 7-A; 13 NYCRR Part 91 [VERIFY] | | | | CHAR007 |
| FL | | Ch. 496, Fla. Stat. [VERIFY] | | | | |
| IL | | 225 ILCS 460/ [VERIFY] | | | | |

---

## Step 4: Produce Outputs

### Gap / Issue Log

| Issue ID | Contract / Vendor | Type | Finding | Risk | Recommended Fix | Owner | Deadline |
|---|---|---|---|---|---|---|---|

### Disclosure Narrative Templates

**Professional Solicitor/Fundraiser:**
> "During [start date] to [end date], the organization engaged **[Vendor name]** ([address]; registration no.: [state: ID]) as a **[professional solicitor / fundraising counsel]** for **[campaign]**. Compensation: **[X% of gross contributions / $X flat fee / description]** plus **[expenses]**. Gross contributions: $[amount]; fees paid: $[amount]; net to organization: $[amount] ([Y]% of gross). Contributions were **[received directly by organization / received by vendor and remitted within [X] days]**."

**Commercial Co-Venturer:**
> "During the reporting period, **[Company name]** conducted a commercial co-venture: **[promotion description]**, [start] to [end]. Benefit to organization: **[$X per sale / X% of sales]**, subject to **[cap/floor]**. Total received: $[amount]. Funds transferred **[timing/method]**. Registration: **[state: ID/filing date]**."

### State Reporting Data Map

| Item | Extracted Data | Form 990 Sch. G | CA CT-2CF | NY CHAR007 |
|---|---|---|---|---|
| Solicitor/CCV name | | Part I, Line 2a | Part II, Line 1 | Part B |
| Compensation % or amount | | Part I, Line 2c | Part II, Line 3 | Part B |
| Gross receipts | | Part I, Line 2b | | Part B |
| Net retained by charity | | | | Part B |
| Custody of funds (Y/N) | | Part I, Line 2b | | |
| Campaign dates | | | | |
| Vendor registration no. | | | | |

### Evidence Binder Checklist

- [ ] Executed contract + amendments/SOWs/exhibits
- [ ] Vendor registration proof per state (with dates)
- [ ] Charity registration proof per state
- [ ] Notice of Intent / contract filing confirmations
- [ ] Campaign materials: scripts, mailers, landing pages, disclosures
- [ ] Funds flow proof: processor statements, bank deposits, remittance confirmations
- [ ] Campaign accounting: gross receipts, expenses, net to charity, refunds
- [ ] Vendor's written financial report of campaign
- [ ] Internal approvals (board/management)
- [ ] Annual report disclosure worksheet tied to source documents
- [ ] Remediation correspondence with vendor

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the initial audit, ask:

1. Does the relationship classification match your understanding of each vendor's actual role and activities?
2. Are there additional contracts, amendments, or SOWs not yet provided?
3. Should I produce disclosure narratives for additional states beyond those covered?
4. Are there funds-flow concerns that need immediate escalation to counsel?

---

## Quality Audit

- Every relationship classification supported by contract language and operational evidence
- Registration status verified or flagged as unverified for each vendor × state
- Compensation base (gross vs. net) clearly identified and consistently applied
- Funds flow documented with red flags surfaced
- All mandated-clause checklist items addressed per state
- Gap/issue log includes risk level, recommended fix, owner, and deadline
- Disclosure narratives match extracted data and are internally consistent
- State reporting data map cross-references Form 990 Schedule G
- Pre-solicitation filing deadlines surfaced
- No fabricated statutes, filing forms, or compliance requirements

---

## Guidelines

- Charitable solicitation regulation is **state-based** — requirements differ significantly by state and by relationship classification
- Always verify current statutes before relying on any checklist item; these laws are frequently amended
- If only a master agreement is available, treat missing SOWs/amendments as compliance risks
- Confirm exact form field names per state (CA RRF-1/CT-2CF, NY CHAR500/CHAR007, Form 990 Schedule G)
- Pre-solicitation filing deadlines (Notices of Intent, contract filings) are commonly 10–20 days before campaign start — check per state
- If classification is unclear or mixed within one campaign, default to highest-risk category
- Mark all uncertain citations or requirements with [VERIFY]
- This workflow supports legal and compliance review — it is not legal advice

**Required disclaimer on every output:**

> THIS COMPLIANCE AUDIT REQUIRES INDEPENDENT ATTORNEY VERIFICATION OF ALL STATUTORY REQUIREMENTS, CLASSIFICATION DETERMINATIONS, AND FILING OBLIGATIONS, AND DOES NOT CONSTITUTE LEGAL ADVICE.
