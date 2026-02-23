---
name: subpoena-duces-tecum
description: Drafts a Subpoena Duces Tecum compelling production of records without testimony, compliant with Federal Rule 45 or state equivalents. Handles recipient designation, document category scoping, production format specifications, privilege/objection notices, and service certification. Use when drafting subpoenas for records, document production subpoenas, third-party discovery requests, or duces tecum commands during the discovery phase of criminal defense or general litigation matters.
tags:
  - drafting
  - litigation
  - pleading
---

# Subpoena Duces Tecum for Records

Drafts an enforceable subpoena compelling production of documents or records from a party or non-party, without requiring personal appearance.

## Prerequisites

1. **Case identifiers** — party names (as captioned), case number, court name with division/judge designation
2. **Recipient information** — full legal name, title/position, address for service; for entities: custodian of records or registered agent
3. **Target records** — categories of documents needed, relevant date ranges, identifying details (account numbers, transaction dates, names)
4. **Jurisdiction** — federal (Rule 45) or specific state rules; any applicable local rules
5. **Prior discovery** — deposition testimony, interrogatory responses, or correspondence referencing the records sought
6. **Special recipient considerations** — government agency protocols, HIPAA-covered entities, financial institution privacy rules, out-of-state service issues

## Output Structure

### 1. Court Header

| Element | Requirement |
|---------|-------------|
| Court name | Full official name with division |
| Caption | All parties exactly as in operative pleadings |
| Case number | Include judge/division designation |
| Formatting | Comply with local rules (font, margins, spacing) |

### 2. Issuing Attorney Block

- Full name, firm, address, phone, email, bar number
- Citation to authorizing rule (Fed. R. Civ. P. 45 or state equivalent)
- Confirm whether jurisdiction allows attorney-issued subpoenas or requires clerk involvement

### 3. Recipient Designation

- Complete legal name and title/position
- For entities: custodian of records or designated agent, entity's registered name
- Proper service address verified against case documents and public records

### 4. Command Language

Draft command that:
- Compels production **without personal appearance**
- Specifies production method:

| Method | Details to Include |
|--------|--------------------|
| Physical delivery | Address, suite, access instructions |
| Electronic transmission | Secure method, file format (native/PDF/TIFF), metadata preservation requirements |
| On-site inspection | Location, access hours, copying arrangements |

- Requires records organized and labeled by request category (Bates numbering if appropriate)

### 5. Records Description

For each category, specify:

```
Category [N]: [Description]
  - Date range: [start] to [end]
  - Subject matter: [specific description]
  - Identifying details: [account numbers, names, transaction IDs]
  - Format: [paper, ESI, native files, etc.]
```

Checklist for each category:
- [ ] Time-bounded with exact dates
- [ ] Specific enough for recipient to identify responsive records
- [ ] Not so broad as to invite overbreadth objection
- [ ] Covers "possession, custody, or control"
- [ ] ESI addressed explicitly if applicable (emails, texts, databases, deleted files, backups, metadata)

### 6. Compliance Terms

- **Production date**: Must satisfy minimum notice period (14 days under Rule 45; verify state equivalents)
- **Production location/method**: Full address or electronic delivery instructions
- **Contact for questions**: Issuing counsel's phone and email
- **Offer of reasonable accommodation**: Alternative methods or rolling production for voluminous records

### 7. Rights and Obligations Notice

Include statements covering:

| Topic | Content |
|-------|---------|
| Objections | Right to serve written objections; deadline per applicable rule |
| Motion to quash/modify | Procedure and court for filing |
| Privilege assertions | Attorney-client, work product, physician-patient; privilege log requirements; in camera review option |
| Protective orders | Availability for confidential/proprietary information |
| Preservation duty | Obligation to preserve all responsive records upon receipt, regardless of intent to object |
| Non-compliance consequences | Contempt, sanctions, compelled compliance, adverse inferences |

### 8. Execution Block

- Signature line with attorney name, date, bar number, firm, full contact info
- **Certificate of service**: method, date, and recipients of service; must comply with jurisdictional certification requirements
- Verify acceptable service methods (typically personal service by non-party 18+, with notice to all parties)

## Guidelines

- **Scope discipline**: Each records category must be relevant to a specific claim or defense — avoid fishing expeditions
- **Anticipate objections**: Draft descriptions that survive overbreadth, undue burden, and relevance challenges; reference specific case events or transactions where possible
- **Rule 45 compliance** (federal): Verify current rule text for geographic reach limits, notice requirements, and issuing-court requirements [VERIFY exact current amendments]
- **HIPAA/financial records**: Include appropriate authorization forms or statutory basis when subpoenaing medical or financial records
- **Notice to parties**: Most jurisdictions require advance notice to all parties before or concurrent with service on non-party recipient
- **Do not assume testimony**: This subpoena is records-only — exclude any appearance or deposition language
- **Cross-check consistency**: Party names, case numbers, and dates must be identical throughout the document
- **Professional tone**: Command language should be authoritative but not adversarial
