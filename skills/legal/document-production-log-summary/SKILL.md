---
name: document-production-log-summary
description: Generates a structured log and strategic summary of documents produced by the opposing party in U.S. litigation discovery. Categorizes materials by type (emails, contracts, financials, memos), date range, custodian, and case relevance; flags "hot documents"; tracks privilege assertions per FRCP 26(b)(5); and identifies production gaps. Use during discovery review to organize voluminous productions, surface critical evidence, assess completeness, and support meet-and-confer or motion to compel decisions.
tags:
  - analysis
  - litigation
  - summarization
  - summary
---

# Document Production Log & Summary

Transforms raw discovery productions into an organized inventory with strategic analysis — hot document flags, privilege tracking, and gap identification.

## Prerequisites

1. **Production materials** — all produced documents with Bates numbers assigned
2. **Discovery requests** — the RFPs or subpoenas the production purports to answer
3. **Case caption & case management orders** — any CMO provisions governing discovery format or tracking
4. **Producing party's written response** — including blanket objections and privilege assertions

## Output Structure

### 1. Production Header

| Field | Detail |
|---|---|
| Case caption | Full parties + designations |
| Case number / Court | Docket no., jurisdiction |
| Producing party | Name + counsel contact |
| Discovery request answered | RFP Nos. / subpoena date |
| Date received | MM/DD/YYYY |
| Production format | Native / TIFF / PDF; metadata preserved? |
| Bates range | e.g., DEF000001–DEF004872 |
| Total docs / pages / GB | Aggregate counts |
| Blanket objections | Summarize from written response |

---

### 2. Document Inventory

For each document or document family:

| Bates No. | Date | Type | Author | Recipient(s) | Custodian | Brief Description | Relevance Category | Priority |
|---|---|---|---|---|---|---|---|---|
| DEF000001 | | Email | | | | | | High/Med/Low |

**Document types to categorize:**
- Emails & correspondence
- Contracts & agreements
- Financial records
- Internal memoranda
- Reports & analyses
- Meeting minutes
- Text messages / chat logs
- Photographs / multimedia

**Relevance categories** (map to contested issues, e.g.):
- Breach / performance
- Notice / knowledge
- Damages / valuation
- Causation
- Credibility / impeachment
- Affirmative defenses

---

### 3. Hot Documents

For each flagged document, provide:

```
Bates No.: _______
Date: _______
Document: [Type — Author to Recipient]
Why Critical: [Contradicts position X / Establishes knowledge of Y / Corroborates claim Z / Impeaches witness W]
Recommended Action: [Designate as exhibit / Depose custodian / Use in MSJ]
```

Flag criteria:
- Contradicts opposing party's stated position
- Establishes knowledge, intent, or notice
- Corroborates liability or damages theory
- Undermines witness credibility
- Creates or breaks key timeline elements

---

### 4. Privilege Log (FRCP 26(b)(5))

For each withheld or redacted document:

| Log No. | Date | Type | Author | All Recipients | Subject Matter | Privilege Claimed | Basis |
|---|---|---|---|---|---|---|---|
| | | | | | | AC / WP / CI | |

**Also note:**
- Any privilege claims lacking adequate justification (potential motion to compel grounds)
- Any apparent inadvertent disclosures or subject-matter waiver situations
- Deficient entries that fail FRCP 26(b)(5) specificity requirements

---

### 5. Production Completeness Assessment

**Coverage Analysis:**

| Category | Expected | Produced | Gap? |
|---|---|---|---|
| Date range | [case-relevant span] | [actual span] | |
| Key custodians | [list] | [list] | |
| Document types | [per RFPs] | [actual] | |

**Flag for follow-up:**
- Missing custodians who logically possess responsive materials
- Truncated or orphaned email threads
- Time periods underrepresented vs. case chronology
- Corrupted files, password-protected docs, unsearchable formats
- Categories of requested documents entirely absent

---

### 6. Executive Summary

Provide a 1–2 page narrative covering:
1. Overall production statistics
2. Top 5–10 hot documents with significance
3. Key evidentiary strengths surfaced
4. Key gaps and recommended next steps (supplemental demand, meet-and-confer, motion to compel)
5. Open privilege disputes requiring resolution

## Guidelines

- **FRCP Rule 34** governs production format obligations; note any non-compliance (e.g., failure to produce ESI in requested format)
- **FRCP Rule 26(b)(5)** requires privilege logs to enable the requesting party to assess the claim — flag any entries that fall short
- **Waiver risk**: Note inadvertent productions immediately; clawback procedures under FRCP 26(b)(5)(B) and FRE 502 may apply [VERIFY jurisdiction-specific orders]
- Do not reproduce potentially privileged content in the log — use subject-matter descriptions only
- Custodian gaps are often more strategically significant than document gaps — prioritize custodian completeness review
- Production log should be delivered in two formats: spreadsheet (filterable) + narrative summary report
