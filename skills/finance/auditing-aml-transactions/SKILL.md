---
name: auditing-aml-transactions
language: en
description: Screens transaction data for suspicious patterns using red flag typologies and structures SAR narrative elements. Use when reviewing transactions for AML, identifying suspicious activity, or drafting SAR narratives.
tags:
  - compliance
  - financial-compliance
  - aml
metadata:
  author: casemark
  practice_areas:
    - Regulatory Compliance
    - Financial Regulation
    - Compliance
  document_types:
    - Compliance Report
  skill_modes:
    - Audit
    - Review
---
# Auditing AML Transactions

Screens transaction data for suspicious patterns using red flag typologies and structures SAR narrative elements for BSA/AML compliance.

## When To Use

- Transaction monitoring system generates an alert requiring human review
- BSA officer receives a referral (internal, law enforcement, or examiner finding)
- Periodic look-back or enhanced due diligence review of high-risk accounts
- Continuation SAR is due on the 90-day cycle
- Independent audit requires sample transaction review
- 314(b) information-sharing request received from another institution

## Inputs To Gather

Collect all items below before starting review. If transaction records are unavailable, STOP — document the gap and escalate.

### Institution & Scope

- Institution type (bank, MSB, broker-dealer, credit union, insurance, casino, other) [VERIFY]
- Charter/license jurisdiction and primary regulator [VERIFY]
- BSA/AML program status (established / recently remediated / under consent order)
- Review period (start and end dates)
- Alert source and alert/case ID

### Subject Information

- Subject name(s) — individuals and/or entities
- Account number(s), account type(s), and open date
- Customer risk rating (Low / Medium / High / Unrated)
- KYC profile: stated occupation, income, expected activity, source of funds
- Prior SAR history on this subject

### Data Sources

Confirm availability of each: transaction records (debits/credits), wire transfer details (originator/beneficiary), cash activity and CTR history, check images and deposit slips, account statements, CDD/EDD documentation, OFAC/sanctions screening results, negative news and adverse media, law enforcement subpoenas or 314(b) requests.

## Workflow

### Step 1 — Transaction Profiling

Summarize account activity for the review period:

| Metric | Value |
|---|---|
| Total credits (count / dollar) | |
| Total debits (count / dollar) | |
| Cash-in / Cash-out (count / dollar) | |
| Wire-in / Wire-out (count / dollar) | |
| ACH/EFT and check activity (count / dollar) | |
| Average and largest single transaction | |
| CTRs filed during period | |
| Jurisdictions involved | |

Compare observed activity against three baselines:
- **KYC expected activity** — Does volume/type match customer declarations?
- **Peer group** — Consistent with similarly situated customers?
- **Historical baseline** — Has pattern shifted from prior periods?

Flag material deviations with `[DEVIATION]` and quantify the variance.

### Step 2 — Red Flag Identification

Screen activity against recognized typologies. For each red flag identified, document:

- **Red flag typology** — Name from reference taxonomy
- **Category** — Structuring / Rapid Movement / Geographic / Shell-Layering / Trade-Based / Behavioral / Other
- **Transactions implicated** — Date, amount, type, counterparty
- **Severity** — High / Medium / Low
- **Explanation** — Why this pattern is suspicious in context

Key thresholds:
- **CTR**: $10,000 cash (single or aggregate same-business-day). Transactions just below are a structuring indicator. [VERIFY current threshold]
- **SAR dollar minimum**: $5,000+ with known suspect; $25,000+ with no identified suspect (banks). No dollar minimum for MSBs. [VERIFY by institution type]
- **Rapid movement**: Funds deposited and withdrawn/transferred within 48 hours with no apparent business purpose.
- **Round-dollar transfers**: Unusual frequency of round-amount wires inconsistent with commercial invoicing.

### Step 3 — OFAC & Sanctions Screening

Confirm whether any party to flagged transactions appears on:
- OFAC SDN List and Consolidated Sanctions List
- FinCEN 311 Special Measures (jurisdictions/institutions)
- EU/UN sanctions lists (if applicable) [VERIFY applicability]
- FATF High-Risk and Non-Cooperative Jurisdictions list

Record each counterparty/jurisdiction screened, the result, list version, and date. If a potential OFAC match is identified, **escalate immediately** — OFAC obligations are strict liability with a shorter timeline than SAR filing.

### Step 4 — Disposition

Reach one of four dispositions:

| Disposition | Criteria | Action |
|---|---|---|
| **File SAR** | Suspicious, unexplained, meets dollar thresholds | Proceed to Step 5 |
| **Close — Below Threshold** | Concerning but below SAR dollar minimums | Document rationale; retain 5 years; consider enhanced monitoring |
| **Close — Explained** | Legitimate purpose confirmed with documentation | Document rationale and evidence; retain 5 years |
| **Escalate** | OFAC match, law enforcement nexus, or insider involvement | Immediate escalation per institution policy |

**Document rationale for every disposition.** Examiners review closed cases as closely as filed SARs.

### Step 5 — SAR Narrative Drafting

The narrative must answer **who, what, when, where, why, and how**.

**Structure:**

1. **Subject Information** — Full legal name(s), DOB, SSN/TIN (if available), address, account relationship, risk rating and basis.
2. **Suspicious Activity Description** — Nature of activity (use FinCEN characterization codes), identify all subjects and roles, specific transactions and patterns, date range, branches/jurisdictions, why activity is suspicious, method/mechanism used.
3. **Transaction Detail** — Chronological summary of key transactions, total dollar amount, instruments/channels (cash, wire, ACH, check, crypto).
4. **Investigation Summary** — Detection method, investigation steps, CDD/EDD reviewed, third-party information (314(b), public records, adverse media).
5. **Supporting Documentation** — Exhibit list, reference to prior SARs if continuation filing.

**Narrative rules:**
- Factual, not conclusory — state what happened; never assert a crime was committed
- Chronological presentation
- Specific — dates, amounts, account numbers, counterparty names
- Self-contained — reader with no prior knowledge should understand the case
- Quantified — total suspicious amounts and transaction counts
- **No SAR-tipping language** — never indicate the customer was or will be notified (31 USC 5318(g)(2)) [VERIFY current statutory cite]

**Filing deadlines** [VERIFY current FinCEN guidance]:

| Scenario | Deadline |
|---|---|
| Standard SAR | 30 calendar days from initial detection |
| No suspect identified | 30 days; may extend to 60 days to identify suspect |
| Ongoing activity | Continuing SARs every 90 days |
| Criminal referral | Notify law enforcement immediately; SAR still due within 30 days |

## Output

Deliverables for each review:

1. **Transaction summary table** with profiling metrics and baseline comparisons
2. **Red flag log** — each flag with typology, category, severity, implicated transactions, and explanation
3. **OFAC/sanctions screening record** with list versions and dates
4. **Disposition memo** — selected outcome with written rationale
5. **SAR narrative** (if filing) — structured per the template above, ready for BSA officer review
6. **Filing deadline tracker** — calculated deadline with calendar entry

## Quality Checks

### Completeness
- [ ] Intake items fully populated or gaps explicitly documented
- [ ] Transaction profiling covers all activity types in the review period
- [ ] Every red flag has severity rating and supporting transactions
- [ ] Disposition is one of the four defined outcomes with written rationale

### Accuracy
- [ ] Dollar amounts cross-referenced to source transaction data
- [ ] Dates confirmed against bank records (not estimated)
- [ ] Counterparty names verified against wire details / account records
- [ ] OFAC screening uses current list version

### Regulatory Compliance
- [ ] SAR narrative answers all six questions (who/what/when/where/why/how)
- [ ] No SAR-tipping or customer-notification language anywhere in output
- [ ] Filing deadline documented and within regulatory window [VERIFY]
- [ ] CTR analysis included for cash-intensive accounts
- [ ] 5-year record retention requirement noted

### Professional Standards
- [ ] Findings distinguish confirmed facts from inferences
- [ ] All inferences and assumptions marked with `[VERIFY]`
- [ ] Terminology consistent throughout
- [ ] Output actionable for BSA officer / compliance committee
- [ ] Escalation triggers clearly identified

## Reference Files

| File | Description |
|---|---|
| `references/AML-RED-FLAGS.md` | Categorized AML red flag typologies with indicators and activity patterns for transaction screening |
