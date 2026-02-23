---
name: bail-hearing-summary
description: Generates structured bail hearing summaries for criminal defense matters, extracting charges, prosecution/defense arguments, bail conditions, risk factors, and court rulings from transcripts and case documents. Use when summarizing bail hearings, pretrial detention decisions, bond hearings, or release condition orders.
tags:
  - litigation
  - summarization
  - summary
---

# Bail Hearing Summary

Produces a structured summary of a bail hearing from transcripts and case documents for quick attorney reference.

## Prerequisites

1. **Charging documents** — complaint, indictment, or information with statute citations
2. **Hearing transcript or recording** — the bail/bond hearing itself
3. **Defendant background** — criminal history, FTA history if available
4. **Party submissions** — prosecution and defense bail memoranda, if filed

## Output Structure

### Header Block

| Field | Content |
|-------|---------|
| Case Name | *People/State/United States v. [Defendant]* |
| Case Number | |
| Court / Jurisdiction | |
| Hearing Date | |
| Presiding Judge | |
| Prosecution Counsel | |
| Defense Counsel | |

### Section 1: Charges

Table format:

| Count | Statute | Offense | Classification | Degree |
|-------|---------|---------|---------------|--------|
| 1 | | | Felony/Misdemeanor | |

### Section 2: Prosecution Arguments

Extract and organize under these categories:
- **Flight risk factors** — prior FTAs, out-of-jurisdiction ties, passport/travel access, financial resources
- **Danger to community** — nature of charges, prior violent history, threats, weapons
- **Strength of evidence** — key evidence cited by prosecution
- **Bail request** — specific amount, conditions sought (detention, high bail, monitoring, no-contact, passport surrender, geographic restrictions)

### Section 3: Defense Arguments

Extract and organize under these categories:
- **Community ties** — residence stability, employment, family responsibilities
- **Mitigating factors** — no/limited criminal history, cooperation, health conditions
- **Proposed conditions** — ROR, reduced bail amount, supervision alternatives
- **Bail request** — specific amount or release type requested

### Section 4: Court Ruling

| Element | Detail |
|---------|--------|
| Bail granted/denied | |
| Amount (if set) | |
| Acceptable form | Cash / Surety / Property / Percentage |
| Court's stated reasoning | |

**Conditions imposed** — numbered list of all conditions:
- [ ] Reporting requirements
- [ ] Travel restrictions
- [ ] Electronic monitoring
- [ ] No-contact orders
- [ ] Substance abuse testing
- [ ] Mental health treatment
- [ ] Other special conditions

If bail denied: note remand to custody and court's reasoning.

### Section 5: Upcoming Dates & Procedural Notes

- Next court date and purpose
- Filing deadlines
- Pending motions (reconsideration, appeal of bail decision)

## Guidelines

- **Objectivity** — present facts and arguments as stated; no advocacy or legal conclusions
- **Quote key statements** — use direct quotes from transcript for significant judicial findings or counsel statements
- **Attribute all facts** — tie assertions to source documents
- **Length** — target 2–4 pages depending on hearing complexity
- **Format** — use headings, tables, and bullet lists for scannability
- **Jurisdiction awareness** — note which bail statute or standard the court applied (e.g., federal Bail Reform Act 18 U.S.C. § 3142, state equivalent) without assuming a specific jurisdiction unless documents indicate one
