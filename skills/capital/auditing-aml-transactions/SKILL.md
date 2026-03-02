---
name: auditing-aml-transactions
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

---

## Why This Skill Exists

The Bank Secrecy Act (BSA) and USA PATRIOT Act impose affirmative obligations on financial institutions to detect and report suspicious activity. Failure to maintain an adequate AML program or to file Suspicious Activity Reports (SARs) when required carries severe consequences:

- **Civil money penalties** — FinCEN has assessed penalties exceeding $100M against individual institutions for BSA violations.
- **Criminal liability** — Willful violations can result in imprisonment for compliance officers and executives.
- **Regulatory action** — Consent orders, cease-and-desist orders, and charter revocation.
- **Reputational damage** — Public enforcement actions destroy customer and counterparty trust.

Every U.S. financial institution must maintain the **five pillars** of a BSA/AML program:

1. Internal policies, procedures, and controls
2. Designated BSA/AML compliance officer
3. Ongoing employee training
4. Independent testing (audit)
5. Risk-based Customer Due Diligence (CDD) and beneficial ownership procedures

This skill supports pillars 1, 4, and 5 by systematizing the transaction review process, ensuring red flag identification is consistent, and producing SAR narratives that meet FinCEN's content requirements.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Before beginning any AML transaction review, collect and confirm the following. Do NOT proceed until each item is resolved or explicitly marked as unavailable.

### Institution & Scope

| Item | Detail Required | Status |
|---|---|---|
| Institution type | Bank, MSB, broker-dealer, credit union, insurance, casino, other | [ ] |
| Charter/license jurisdiction | State/federal regulator | [ ] |
| BSA/AML program maturity | Established / Recently remediated / Under consent order | [ ] |
| Review period | Start and end dates | [ ] |
| Alert source | Transaction monitoring system, referral, law enforcement request, examiner finding, other | [ ] |
| Alert/case ID | Internal reference number | [ ] |

### Subject Information

| Item | Detail Required | Status |
|---|---|---|
| Subject name(s) | Individual(s) and/or entity(ies) | [ ] |
| Account number(s) | All accounts under review | [ ] |
| Account type(s) | Personal, business, trust, correspondent, etc. | [ ] |
| Account open date | When relationship began | [ ] |
| Customer risk rating | Low / Medium / High / Unrated | [ ] |
| KYC profile summary | Stated occupation, income, expected activity, source of funds | [ ] |
| Prior SAR history | Any previous SARs filed on this subject | [ ] |

### Data Availability

| Data Source | Available? | Format | Notes |
|---|---|---|---|
| Transaction records (debits/credits) | [ ] | | |
| Wire transfer details (originator/beneficiary) | [ ] | | |
| Cash activity / CTR history | [ ] | | |
| Check images / deposit slips | [ ] | | |
| Account statements | [ ] | | |
| CDD / EDD documentation | [ ] | | |
| OFAC/sanctions screening results | [ ] | | |
| Negative news / adverse media | [ ] | | |
| Law enforcement subpoenas / 314(b) requests | [ ] | | |

**Gate rule:** If transaction records are unavailable, STOP. Document the gap and escalate. You cannot conduct an AML review without underlying transaction data.

---

## Step 1: Transaction Profiling

Summarize the account activity within the review period. Produce the following deliverable:

### Transaction Summary Table

| Metric | Value |
|---|---|
| Total credits (count / dollar) | |
| Total debits (count / dollar) | |
| Cash-in (count / dollar) | |
| Cash-out (count / dollar) | |
| Wire-in (count / dollar) | |
| Wire-out (count / dollar) | |
| ACH / EFT activity (count / dollar) | |
| Check activity (count / dollar) | |
| Average transaction size | |
| Largest single transaction | |
| CTRs filed during period | |
| Jurisdictions involved | |

### Profile Comparison

Compare observed activity against:
- **KYC expected activity** — Does the volume/type match what the customer declared?
- **Peer group** — Is this consistent with similarly situated customers?
- **Historical baseline** — Has the pattern shifted from prior periods?

Flag any material deviation with `[DEVIATION]` and quantify the variance.

---

## Step 2: Red Flag Identification

Systematically screen activity against recognized typologies. Reference `references/AML-RED-FLAGS.md` for the full categorized list.

For EACH red flag identified, document:

| Field | Content |
|---|---|
| Red flag typology | Name from reference taxonomy |
| Category | Structuring / Rapid Movement / Geographic / Shell/Layering / Trade-Based / Behavioral / Other |
| Transactions implicated | Date, amount, type, counterparty |
| Severity | High / Medium / Low |
| Explanation | Why this pattern is suspicious in context |

### Critical Thresholds

- **CTR threshold**: $10,000 in cash (single or aggregate same-business-day). Transactions just below this threshold are a structuring indicator.
- **SAR dollar threshold**: $5,000+ involving a known suspect; $25,000+ with no identified suspect (for banks). Note: No dollar minimum for MSBs.
- **Rapid movement**: Funds deposited and withdrawn/transferred within 48 hours with no apparent business purpose.
- **Round-dollar transfers**: Unusual frequency of round-amount wires or transfers inconsistent with commercial invoicing.

---

## Step 3: OFAC & Sanctions Intersection

Confirm whether any party to flagged transactions appears on:

- OFAC SDN (Specially Designated Nationals) List
- OFAC Consolidated Sanctions List
- FinCEN 311 Special Measures (jurisdictions/institutions)
- EU/UN sanctions lists (if applicable)
- FATF High-Risk and Non-Cooperative Jurisdictions list

| Counterparty / Jurisdiction | Screening Result | List Checked | Date Screened |
|---|---|---|---|
| | | | |

If a potential OFAC match is identified, **escalate immediately** — OFAC obligations are strict liability and operate on a separate, shorter timeline than SAR filing.

---

## Step 4: Investigation Disposition

Based on Steps 1-3, reach one of the following dispositions:

| Disposition | Criteria | Action Required |
|---|---|---|
| **File SAR** | Activity is suspicious, cannot be reasonably explained, and meets dollar thresholds | Proceed to Step 5 |
| **Close — Suspicious Below Threshold** | Activity raises concerns but does not meet SAR dollar thresholds | Document rationale; retain for 5 years; consider enhanced monitoring |
| **Close — Activity Explained** | Legitimate business purpose confirmed with supporting documentation | Document rationale and evidence; retain for 5 years |
| **Escalate** | Potential OFAC match, law enforcement nexus, or insider involvement | Immediate escalation per institution policy |

**Document the rationale for every disposition.** Examiners review closed cases as closely as filed SARs.

---

## Step 5: SAR Narrative Drafting

If disposition is "File SAR," draft the narrative using the structure below. The narrative must answer **who, what, when, where, why, and how**.

### SAR Narrative Template

```
SUBJECT INFORMATION
- Full legal name(s), DOB, SSN/TIN (if available), address
- Relationship to institution: account type(s), open date, branch
- Customer risk rating and basis

SUSPICIOUS ACTIVITY DESCRIPTION
- Nature of suspicious activity (use FinCEN characterization codes where applicable)
- [WHO] Identify all subjects and their roles
- [WHAT] Describe the specific transactions and patterns
- [WHEN] Provide the date range of suspicious activity
- [WHERE] Identify branches, jurisdictions, geographic nexus
- [WHY] Explain why the activity is suspicious (deviation from expected, red flags triggered)
- [HOW] Describe the method/mechanism used

TRANSACTION DETAIL
- Chronological summary of key transactions
- Total dollar amount of suspicious activity
- Instruments/channels used (cash, wire, ACH, check, crypto)

INVESTIGATION SUMMARY
- How the activity was detected (monitoring system, referral, etc.)
- Steps taken during investigation
- CDD/EDD reviewed
- Third-party information obtained (314(b), public records, adverse media)

SUPPORTING DOCUMENTATION
- List of exhibits and attachments
- Reference to prior SARs if continuation filing
```

### Narrative Quality Rules

1. **Factual, not conclusory** — State what happened; do not assert that the subject committed a crime.
2. **Chronological** — Present events in time sequence.
3. **Specific** — Include dates, amounts, account numbers, counterparty names.
4. **Complete** — A reader with no prior knowledge should understand the case from the narrative alone.
5. **No jargon without definition** — Spell out acronyms on first use.
6. **Quantified** — Total suspicious amounts; count of transactions.
7. **No customer notification** — Never include language suggesting the customer was or will be informed of the SAR. SAR confidentiality (31 USC 5318(g)(2)) is absolute.

### Filing Deadlines

| Scenario | Deadline |
|---|---|
| Standard SAR | 30 calendar days from initial detection |
| No suspect identified | 30 days; may extend to 60 days to identify suspect |
| Ongoing activity | Continuing SARs filed every 90 days |
| Criminal referral needed | Immediately notify law enforcement; SAR still required within 30 days |

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

Before finalizing, verify each item:

| Verification Item | Confirmed? |
|---|---|
| All flagged transactions are supported by underlying records | [ ] |
| Red flags are mapped to recognized typologies (not invented) | [ ] |
| SAR narrative answers all six questions (who/what/when/where/why/how) | [ ] |
| Dollar amounts are accurate and reconciled to source data | [ ] |
| Dates are verified against transaction records | [ ] |
| No SAR-tipping language present (no indication customer was notified) | [ ] |
| Disposition rationale is documented even for closed cases | [ ] |
| OFAC screening is current (within 24 hours for escalated cases) | [ ] |
| Filing deadline calculated and recorded | [ ] |
| All assumptions marked with `[VERIFY]` | [ ] |

---

## Quality Audit

### Completeness

- [ ] Pre-draft intake fully populated or gaps explicitly documented
- [ ] Transaction profiling covers all activity types in the review period
- [ ] Every identified red flag has a severity rating and supporting transactions
- [ ] Disposition is one of the four defined outcomes with written rationale

### Accuracy

- [ ] Dollar amounts cross-referenced to source transaction data
- [ ] Dates confirmed against bank records (not estimated)
- [ ] Counterparty names verified against wire details / account records
- [ ] OFAC screening results are from the current list version

### Regulatory Compliance

- [ ] SAR narrative meets FinCEN content requirements
- [ ] No SAR-tipping or customer-notification language anywhere in output
- [ ] Filing deadline documented and within regulatory window
- [ ] CTR analysis included for cash-intensive accounts
- [ ] 5-year record retention requirement noted

### Professional Standards

- [ ] Findings distinguish between confirmed facts and inferences
- [ ] All inferences and assumptions marked with `[VERIFY]`
- [ ] Terminology is consistent throughout
- [ ] Output is actionable for BSA officer / compliance committee
- [ ] Escalation triggers clearly identified

---

## Reference Files

| File | Purpose |
|---|---|
| `references/AML-RED-FLAGS.md` | Categorized red flag typologies for transaction screening |

### External References (Do Not Reproduce — Cite Only)

- FinCEN SAR Filing Instructions (FinCEN Report 111 / 111-B)
- FFIEC BSA/AML Examination Manual
- FinCEN Advisories and Guidance (FIN-2021-A003, etc.)
- FATF 40 Recommendations and Mutual Evaluation Reports
- OFAC SDN List and Consolidated Sanctions List
- USA PATRIOT Act, Title III
- 31 CFR Chapter X (BSA Regulations)
