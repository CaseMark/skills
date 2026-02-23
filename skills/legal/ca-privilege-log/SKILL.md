---
name: ca-privilege-log
description: Generates California-compliant privilege logs for withheld or redacted discovery materials under CCP 2031.240, applying Evid. Code 952/954 attorney-client privilege and CCP 2018.030 work product distinctions. Use for California civil discovery responses, privilege log drafting, redaction logging, meet-and-confer prep, or when asked for “privilege log,” “withhold,” “work product,” “Hernandez,” “Costco,” or “Wellpoint.”
tags:
  - analysis
  - checklist
  - drafting
  - litigation
---

# California Privilege Log

Produce a defensible California privilege log that enables assessment without revealing privileged substance.

## Prerequisites

1. **Discovery context** — RFP set, request text, objections, and any ESI protocol, CMO, or stipulation on logging format.
2. **Document population** — withheld and redacted items with stable IDs/Bates, family links, and production status.
3. **Metadata** — date, author, recipients (TO/CC/BCC), document type, subject/file name, custodian, location.
4. **Roles list** — name-to-role map for all participants (client, in-house, outside counsel, consultants, third parties).
5. **Privilege basis** — ACP, WPD absolute, WPD qualified, common interest/joint defense (with proof).
6. **Litigation timeline** — trigger facts for “anticipation of litigation” for work product.
7. **Waiver risks** — known third-party dissemination, mixed business/legal communications, forwarded chains.

## Output Structure / Process

1. Confirm forum and governing standard: California state court vs. federal; adapt mechanics only if an order or stipulation controls.
2. Normalize metadata: consistent names, roles, dates, and family relationships; split attachments unless the protocol allows categorical treatment.
3. Classify basis per item: ACP (Evid. Code §§ 952, 954), WPD absolute/qualified (CCP § 2018.030(a)/(b)), or both.
4. Draft descriptions that are sufficiently specific under Hernandez v. Superior Court (2003) 112 Cal.App.4th 285 [VERIFY].
5. Flag waiver and mixed-purpose risks (Evid. Code § 912; Costco Wholesale Corp. v. Superior Court (2009) 47 Cal.4th 725 [VERIFY]).
6. Assemble the production log and separate attorney-only review flags.

**Standard Log Columns**

| Column | Required | Notes |
| --- | --- | --- |
| Entry ID / Bates | Yes | Unique per document or family item |
| Date | Yes | “Undated” if unknown |
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

**CSV Header Template**

```csv
EntryID,Bates,Date,DocType,Author,RecipientsTO,RecipientsCC,RecipientsBCC,Description,PrivilegeBasis,LegalAuthority,ProductionStatus,RequestNo,Notes
```

**Privilege Basis Labels**

| Label | Use When | Authority |
| --- | --- | --- |
| Attorney-Client Privilege | Confidential client-lawyer communication for legal advice | Evid. Code §§ 952, 954 |
| Work Product – Absolute | Attorney impressions, opinions, legal research, theories | CCP § 2018.030(a) |
| Work Product – Qualified | Other attorney work product | CCP § 2018.030(b) |
| Joint Defense / Common Interest | Shared legal strategy with aligned parties | Require agreement [VERIFY] |

**Description Checklist**

- [ ] Identify document type and general purpose.
- [ ] Identify roles of participants (client, in-house, outside counsel).
- [ ] State legal purpose at a high level (request/provision of legal advice; prepared for litigation).
- [ ] Avoid quoting privileged subject lines or legal theories.
- [ ] Specify redacted vs. withheld.
- [ ] Avoid over-asserting both ACP and WPD without support.

**Safe Description Templates**

```text
Confidential email between [Client Role] and [Counsel Role] requesting or providing legal advice regarding [high-level issue]; withheld under attorney-client privilege (Evid. Code §§ 952, 954).

Internal memorandum prepared by [Counsel Role] at counsel’s direction in anticipation of litigation regarding [high-level issue], reflecting counsel’s impressions and legal theories; withheld as work product—absolute (CCP § 2018.030(a)).

Draft [document type] prepared for attorney review and legal advice concerning [high-level issue]; produced with redactions for privileged portions; redactions based on attorney-client privilege (Evid. Code §§ 952, 954).
```

**Attorney Review Flags (Separate, Non-Produced)**

- Third-party recipient present; confirm necessity under Evid. Code § 952.
- Forwarded to non-legal distribution list; assess waiver under Evid. Code § 912.
- Mixed business/legal purpose; confirm dominant purpose analysis (Costco Wholesale [VERIFY]).
- Work product claimed before litigation trigger; confirm timeline.
- Expert involvement; confirm designation and potential waiver.

## Guidelines

- Do not invent metadata, roles, or bases; stop and request missing inputs.
- Do not expose privileged substance, legal strategy, or settlement positions.
- Treat attachments as separate entries unless protocol allows grouping.
- Prefer redactions over complete withholding when only part is privileged.
- Use consistent naming and formatting across entries; inconsistency signals weakness.
- Apply the burden framework from Wellpoint Health Networks v. Superior Court (1997) 59 Cal.App.4th 110 [VERIFY].
- If federal court applies, adapt mechanics to FRCP 26(b)(5)(A) while keeping California privilege elements.
- Require attorney review before service; comply with Cal. Rules of Prof. Conduct 1.1, 1.6, 3.3 [VERIFY].
