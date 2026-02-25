---
name: ca-privilege-log
description: >
  Generates California-compliant privilege logs for withheld or redacted discovery
  materials under CCP 2031.240. Use this skill when the user mentions privilege
  log drafting, California privilege log, CCP 2031.240, attorney-client privilege
  logging, work product designation, Evid. Code 952/954, CCP 2018.030, redaction
  logging, meet-and-confer privilege disputes, or privilege log review. Also
  trigger when the user references Hernandez v. Superior Court, Costco Wholesale,
  Wellpoint, waiver analysis, common interest doctrine, or asks for help
  documenting withheld documents. Even if the user just says "I need a privilege
  log" or "help me log these withheld docs," use this skill.
tags:
  - analysis
  - checklist
  - drafting
  - litigation
---

# California Privilege Log

## Why This Skill Exists

Privilege logs are the first line of defense when an opponent challenges withholding — and the first thing a judge scrutinizes on a motion to compel. An inadequately described privilege log entry is functionally equivalent to no privilege assertion at all, because the court cannot evaluate the claim without understanding who communicated what to whom and why. California courts following *Hernandez v. Superior Court* (2003) 112 Cal.App.4th 285 [VERIFY] require descriptions specific enough to assess the privilege without revealing privileged substance — a narrow target that most logs miss.

This skill produces a defensible California privilege log that enables assessment without revealing privileged substance, with consistent formatting, proper authority citations, and attorney-review flags for waiver risks.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft." Gather:

1. **Discovery context** — RFP set, request text, objections, and any ESI protocol, CMO, or stipulation on logging format
2. **Document population** — withheld and redacted items with stable IDs/Bates, family links, and production status
3. **Metadata** — date, author, recipients (TO/CC/BCC), document type, subject/file name, custodian, location
4. **Roles list** — name-to-role map for all participants (client, in-house, outside counsel, consultants, third parties)
5. **Privilege basis** — ACP, WPD absolute, WPD qualified, common interest/joint defense (with proof)
6. **Litigation timeline** — trigger facts for "anticipation of litigation" for work product
7. **Waiver risks** — known third-party dissemination, mixed business/legal communications, forwarded chains

**If the user doesn't respond**, apply and clearly label these defaults: California state court; attorney-client privilege basis; withheld (not redacted); standard column format.

---

## Step 1: Confirm Forum and Governing Standard

California state court vs. federal — adapt mechanics only if an order or stipulation controls. Identify any court-specific or CMO-mandated logging format requirements.

---

## Step 2: Normalize Metadata

Ensure consistent names, roles, dates, and family relationships across all entries. Split attachments as separate entries unless the protocol allows categorical treatment.

---

## Step 3: Classify Privilege Basis Per Item

| Label | Use When | Authority |
|---|---|---|
| Attorney-Client Privilege | Confidential client-lawyer communication for legal advice | Evid. Code §§ 952, 954 |
| Work Product – Absolute | Attorney impressions, opinions, legal research, theories | CCP § 2018.030(a) |
| Work Product – Qualified | Other attorney work product | CCP § 2018.030(b) |
| Joint Defense / Common Interest | Shared legal strategy with aligned parties | Require agreement [VERIFY] |

Do not over-assert both ACP and WPD without factual support for each.

---

## Step 4: Draft Log Entries

### Standard Log Columns

| Column | Required | Notes |
|---|---|---|
| Entry ID / Bates | Yes | Unique per document or family item |
| Date | Yes | "Undated" if unknown |
| Document Type | Yes | Email, memo, draft, notes, etc. |
| Author (Name + Role) | Yes | Use role mapping |
| Recipients TO (Name + Role) | Yes | Separate TO/CC/BCC |
| Recipients CC/BCC | If any | Include third parties explicitly |
| Description | Yes | Functional, non-substantive |
| Privilege Basis | Yes | ACP, WPD-Abs, WPD-Qual, or both |
| Legal Authority | Yes | Cite relevant statutes |
| Production Status | Yes | Withheld or Redacted |
| RFP / Request No. | If tracked | Link to request |
| Notes | Optional | Family/attachment links, redaction note |

### CSV Header Template

```csv
EntryID,Bates,Date,DocType,Author,RecipientsTO,RecipientsCC,RecipientsBCC,Description,PrivilegeBasis,LegalAuthority,ProductionStatus,RequestNo,Notes
```

### Safe Description Templates

```text
Confidential email between [Client Role] and [Counsel Role] requesting or providing legal advice regarding [high-level issue]; withheld under attorney-client privilege (Evid. Code §§ 952, 954).

Internal memorandum prepared by [Counsel Role] at counsel's direction in anticipation of litigation regarding [high-level issue], reflecting counsel's impressions and legal theories; withheld as work product—absolute (CCP § 2018.030(a)).

Draft [document type] prepared for attorney review and legal advice concerning [high-level issue]; produced with redactions for privileged portions; redactions based on attorney-client privilege (Evid. Code §§ 952, 954).
```

### Description Checklist

- [ ] Identify document type and general purpose
- [ ] Identify roles of participants (client, in-house, outside counsel)
- [ ] State legal purpose at a high level (request/provision of legal advice; prepared for litigation)
- [ ] Avoid quoting privileged subject lines or legal theories
- [ ] Specify redacted vs. withheld
- [ ] Avoid over-asserting both ACP and WPD without support

---

## Step 5: Flag Waiver and Risk Issues

Generate a separate attorney-only review section (non-produced):

- Third-party recipient present; confirm necessity under Evid. Code § 952
- Forwarded to non-legal distribution list; assess waiver under Evid. Code § 912
- Mixed business/legal purpose; confirm dominant purpose analysis (*Costco Wholesale Corp. v. Superior Court* (2009) 47 Cal.4th 725 [VERIFY])
- Work product claimed before litigation trigger; confirm timeline
- Expert involvement; confirm designation and potential waiver

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the initial privilege log, ask:

1. Are the role assignments (client, in-house, outside counsel, third party) accurate for all participants?
2. Are there any entries where the privilege basis needs reconsideration (e.g., mixed business/legal purpose)?
3. Should any withheld documents be produced with redactions instead of full withholding?
4. Does the log format match any court order or stipulation requirements?

If the user doesn't answer, recommend reviewing the waiver-risk flags first and proceed if authorized.

---

## Quality Audit

Before finalizing, verify:

- Every entry has a unique ID/Bates number
- All participants mapped to roles consistently across entries
- Descriptions are sufficiently specific under *Hernandez* [VERIFY] without revealing privileged substance
- Privilege basis supported by facts (not just boilerplate assertion)
- Redacted vs. withheld correctly designated for each entry
- Attachments treated as separate entries (unless protocol allows grouping)
- No privileged subject lines, legal theories, or settlement positions exposed
- Waiver risks flagged in attorney-only section
- Consistent naming and formatting across all entries
- All statutory citations verified or marked `[VERIFY]`
- CSV/table format matches any applicable court order or ESI protocol

---

## Guidelines

- Do not invent metadata, roles, or bases; stop and request missing inputs
- Do not expose privileged substance, legal strategy, or settlement positions
- Treat attachments as separate entries unless protocol allows grouping
- Prefer redactions over complete withholding when only part is privileged
- Use consistent naming and formatting across entries; inconsistency signals weakness
- Apply the burden framework from *Wellpoint Health Networks v. Superior Court* (1997) 59 Cal.App.4th 110 [VERIFY]
- If federal court applies, adapt mechanics to FRCP 26(b)(5)(A) while keeping California privilege elements
- **Anti-hallucination** — all case citations must be verified or flagged `[VERIFY]`; never generate unverified case law
- **Attorney review required** — all output must be reviewed by supervising counsel before service; comply with Cal. Rules of Prof. Conduct 1.1, 1.6, 3.3 [VERIFY]
