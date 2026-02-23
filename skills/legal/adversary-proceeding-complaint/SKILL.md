---
name: adversary-proceeding-complaint
description: Drafts adversary proceeding complaints for filing in U.S. Bankruptcy Court under FRBP Rule 7001, covering dischargeability disputes, fraudulent transfers, preference actions, and automatic stay violations. Produces a filing-ready pleading with caption, jurisdictional basis, numbered factual allegations, count structure, and prayer for relief. Use when a trustee, creditor, or party in interest needs to initiate litigation within an existing bankruptcy case.
tags:
  - drafting
  - litigation
  - pleading
---

# Adversary Proceeding Complaint

Drafts a filing-ready complaint initiating an adversary proceeding in U.S. Bankruptcy Court under FRBP Rule 7001.

## Prerequisites

1. **Bankruptcy case information** — court, district/division, case number, chapter, debtor name as filed
2. **Party details** — plaintiff name/capacity (trustee, creditor, etc.), defendant name/address/relationship to estate
3. **Factual basis** — chronology of events, transactions, transfers, dates, amounts, documentary evidence
4. **Claim type(s)** — which Rule 7001 category and substantive statutory basis applies
5. **Relief sought** — specific dollar amounts, determinations, or remedies requested

## Output Structure

### 1. Caption

| Element | Format |
|---------|--------|
| Court | UNITED STATES BANKRUPTCY COURT, [DISTRICT], [DIVISION] |
| In re: | Debtor name exactly as in main case |
| Case No. | Main bankruptcy case number |
| Adversary No. | Include if assigned; otherwise leave blank for clerk |
| Parties | Plaintiff v. Defendant with capacity designations |

### 2. Introductory Paragraph

- State complaint is filed pursuant to FRBP 7001
- Identify applicable Rule 7001 subsection
- One-sentence summary of dispute and primary relief

### 3. Jurisdiction & Venue

State each basis with statutory citation:

- **Subject matter**: 28 U.S.C. § 1334 (original jurisdiction)
- **Reference**: 28 U.S.C. § 157 (reference to bankruptcy court)
- **Core/non-core**: 28 U.S.C. § 157(b)(2) — identify specific subsection if core
- **Personal jurisdiction**: basis over defendant
- **Venue**: basis in this district

### 4. Parties

Numbered paragraphs for each party:
- **Plaintiff**: relationship to estate, standing basis
- **Defendant**: identifying information, address, relationship to debtor/estate

### 5. Factual Background

Numbered paragraphs, chronological order:
- Bankruptcy filing date, chapter, procedural history
- Party relationship, contractual/business dealings
- Each distinct factual allegation in its own paragraph
- Specific dates, dollar amounts, document references

### 6. Claim-Specific Factual Allegations

Tailor to claim type:

| Claim Type | Statute | Key Allegations |
|------------|---------|-----------------|
| Dischargeability | 11 U.S.C. § 523(a)(2), (4), or (6) | Specific transactions, representations, fraudulent conduct, willful/malicious injury |
| Preference | 11 U.S.C. § 547 | Each transfer: date, amount, antecedent debt, timing relative to petition date |
| Fraudulent transfer | 11 U.S.C. § 548 / state law | Transfer details, consideration received, actual or constructive fraud badges |
| Stay violation | 11 U.S.C. § 362 | Acts taken post-petition, knowledge of filing, damages caused |

### 7. Counts

Each count as a separate section:

```
COUNT [N] — [TITLE, e.g., "Nondischargeability Under 11 U.S.C. § 523(a)(2)(A)"]

[X]. Plaintiff incorporates paragraphs 1 through [Y] as if fully set forth herein.
[X+1]. [Element 1 with supporting factual allegations]
[X+2]. [Element 2 with supporting factual allegations]
...
```

Address every statutory element for each count.

### 8. Prayer for Relief

- Specific judgment on each count (e.g., "determining the debt in the amount of $_____ nondischargeable")
- Avoidance and recovery of specific transfers with values
- Damages for stay violations (actual, punitive if applicable)
- Costs and attorneys' fees where statutorily authorized
- "Such other and further relief as the Court deems just and proper"

### 9. Signature Block & Verification

- Attorney signature block with bar number, firm, address, phone, email
- Certificate of service

## Guidelines

- Use numbered paragraphs for all factual allegations
- Plead facts, not legal conclusions — each element must be supported by specific factual allegations meeting *Twombly*/*Iqbal* plausibility standard
- Maintain consistent defined terms and party designations throughout
- Cite statutes in standard Bluebook format
- Check local bankruptcy court rules for formatting requirements (margins, font, ECF conventions)
- For § 523 claims, plaintiff bears burden of proof by preponderance (or clear and convincing for § 523(a)(2)) — plead accordingly
- For § 547 preferences, confirm the look-back period: 90 days general, 1 year for insiders
- For § 548 fraudulent transfers, confirm 2-year reach-back from petition date; state law may extend further
- Do not include argumentative language or rhetoric — maintain neutral pleading tone
- Flag any assumed facts with `[CONFIRM WITH CLIENT]`
