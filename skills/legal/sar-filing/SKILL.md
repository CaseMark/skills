---
name: sar-filing
description: Drafts comprehensive Suspicious Activity Reports (SARs) for FinCEN submission under BSA/AML regulations. Compiles chronological timelines, red flags, subject identification, account details, and activity classifications aligned to FinCEN Form 111. Use when financial institutions detect suspicious transactions requiring mandatory regulatory reporting, BSA compliance filing, or continuing activity reports.
tags:
  - drafting
  - memo
  - regulatory
---

# Suspicious Activity Report (SAR) Filing

Drafts a FinCEN-ready SAR (Form 111) from institutional records, transaction data, and investigation files.

## Prerequisites

1. **Transaction records** — deposits, withdrawals, wires, monetary instruments with exact amounts, dates, account numbers
2. **Customer identification / CIP documentation** — government IDs, SSN/TIN, beneficial ownership certifications, business formation docs
3. **Investigation file** — monitoring alerts, internal notes, correspondence, employee observations
4. **Institutional filer details** — legal name, EIN, LEI, primary federal regulator, SAR contact person
5. **Prior SAR history** (if continuing filing) — BSA Identifier numbers, filing dates

## Output Structure

### 1. Filing Header

| Field | Detail |
|---|---|
| Filing type | Initial / Continuing / Corrective |
| Institution legal name | As registered with FinCEN |
| EIN / LEI | |
| Primary regulator | OCC / Fed / FDIC / NCUA / State |
| SAR contact | Name, title, phone, secure email |
| Detection date | Date suspicious activity first identified |
| Filing deadline | 30 days from detection (60 if no subject identified) |
| Prior BSA ID (if continuing) | Reference number + what new activity/info triggered re-filing |

### 2. Subject & Party Identification

For **each** individual or entity, classify role per FinCEN categories: Subject, Purchaser/Sender, Payee/Receiver, Other.

**Individuals:**
- Full legal name + aliases
- DOB, SSN/ITIN, address (current + historical)
- Government ID type, number, issuing jurisdiction, expiration
- Foreign nationals: passport, citizenship, visa status, high-risk jurisdiction nexus

**Entities:**
- Legal name + DBAs
- EIN, state/date of formation, nature of business
- Beneficial owners (≥25% ownership or substantial control)

**Relationships between parties:** Articulate familial, business, signatory, nominee, or intermediary connections.

### 3. Account & Relationship Detail

For each account involved:

| Field | Detail |
|---|---|
| Account number | |
| Account type | Checking / Savings / Wire / CD / Loan / Credit / Safe deposit / Other |
| Open date / Status | Active / Closed / Restricted / Frozen |
| Holders & signers | Names + relationships |
| Stated purpose | As documented at opening |
| Baseline profile | Typical volume, balances, transaction types |
| Deviations | Specific changes in patterns triggering concern |

Include:
- Branch/department contacts and employee names involved
- Prior compliance concerns or enhanced monitoring
- Correspondent banking / MSB / third-party processor relationships with fund-flow tracing
- CIP/CDD/EDD procedures performed
- Account closure details if applicable (date, notice given, reason)

### 4. Activity Classification & Thresholds

Select from FinCEN standardized categories:

| Category | Examples |
|---|---|
| Structuring | Transactions below CTR thresholds |
| Money laundering | Layering, integration, funnel accounts |
| Terrorist financing | OFAC/SDN nexus |
| Fraud | Check kiting, wire fraud, mortgage fraud, elder exploitation |
| Identity crimes | Synthetic ID, stolen credentials |
| Cyber | Account takeover, intrusion-related transfers |
| Sanctions evasion | Transactions involving sanctioned jurisdictions/persons |
| Other | Unlicensed MSB, trade-based ML, human trafficking |

**Threshold verification:**
- ≥ $5,000 if subject identified
- ≥ $25,000 if no subject identified
- Blocked/attempted transactions: note they were prevented and explain why filing is still warranted
- Confirm no exemption or safe harbor applies
- Confirm not duplicative of another institution's filing (unless unique information exists)

**State:** Total dollar amount, currency, complete time period.

### 5. Narrative

Structure the narrative chronologically addressing the **six critical questions**: Who, What, When, Where, Why, How.

```
NARRATIVE TEMPLATE

1. DETECTION
   - How activity was identified (monitoring alert, employee referral, LE inquiry, audit)
   - Specific rule/threshold triggered; why not dispositioned as false positive

2. CHRONOLOGICAL TIMELINE
   For each significant transaction:
   - Date/time, type (cash/wire/ACH/check/MI), amount, currency
   - Source → destination of funds
   - Customer's stated purpose
   - Unusual characteristics

3. RED FLAG ANALYSIS
   Map observed facts to recognized indicators:
   - Reluctance to provide information
   - Concern about reporting/recordkeeping
   - No economic purpose / business justification
   - Rapid in/out movement with minimal balance retention
   - Structuring patterns
   - Shell company involvement
   - High-risk jurisdiction connections
   - Inconsistency between stated profile and actual activity
   - Known typology matches (cite FFIEC BSA/AML Manual or FinCEN advisories)

4. INVESTIGATION STEPS
   - Customer contact attempts + responses/explanations
   - Why explanations were insufficient
   - Open-source / public records research conducted
   - Prior SARs on same subject (BSA IDs + dates)

5. CONCLUSION
   - Factual basis for determination that activity warrants filing
   - Objective tone — no conclusory statements about criminal intent
```

### 6. Supporting Documentation Index

Organize attachments chronologically or by category:

- Transaction records (statements, slips, wire confirmations, check images)
- Customer ID documents (CIP records, beneficial ownership certs)
- Correspondence (emails, letters, call notes)
- Monitoring system output (alert screenshots, case notes)
- Internal investigation memos
- Communications with other financial institutions

Label each document with title and relevance to narrative.

### 7. Compliance Verification Checklist

- [ ] Filed within 30-day deadline (or 60-day if no subject)
- [ ] All mandatory FinCEN Form 111 fields completed
- [ ] Narrative addresses Who/What/When/Where/Why/How
- [ ] Dollar amounts accurate and aggregated
- [ ] All dates, account numbers, IDs verified
- [ ] Senior management / board notified per institutional policy
- [ ] Legal counsel consulted if civil liability or non-BSA regulatory issues
- [ ] Reviewing/approving officers documented (names, titles)
- [ ] SAR filed via BSA E-Filing System; confirmation + BSA ID retained
- [ ] SAR file stored separately, access restricted to need-to-know personnel
- [ ] 5-year retention period initiated from filing date
- [ ] **No disclosure** made to any subject per 31 U.S.C. § 5318(g)(2)
- [ ] No inadvertent tipping via closure letters or customer communications
- [ ] Immediate LE notification assessed (and made if warranted)

## Guidelines

- **Confidentiality is absolute.** Violation of SAR disclosure prohibition (31 U.S.C. § 5318(g)(2)) carries criminal penalties. Never reference SAR existence in customer-facing communications.
- **Objectivity only.** Present facts and documented observations. Do not state conclusions about criminal guilt or legal violations.
- **Err toward over-inclusion.** FinCEN prefers detailed narratives. Include more rather than less.
- **Standalone document.** The SAR must be comprehensible to LE/FinCEN analysts without access to underlying bank records.
- **Continuing filings** must reference prior BSA IDs and clearly identify what is new.
- **Safe harbor protection** under 31 U.S.C. § 5318(g)(3) applies to good-faith filings — document the institution's investigative process thoroughly to support this.
