---
name: deposition-document-assembly
description: Assembles and organizes documents for deposition preparation by identifying deponent-connected materials, categorizing by use (authentication, impeachment, key fact, background), generating an exhibit candidate list, and flagging document gaps. Produces a complete document inventory, exhibit list, impeachment index, gap analysis, and pre-deposition preparation checklist. Use before building a deposition outline — for fact witnesses, party deponents, corporate representatives (30(b)(6)), or expert witnesses in US federal and state litigation.
tags:
  - analysis
  - checklist
  - litigation
---

# Deposition Document Assembly

Systematically identifies, categorizes, and inventories documents for deposition preparation, then outputs an exhibit list, gap analysis, and impeachment index.

## Prerequisites

1. **Deponent identity and role** — name, employer, party/non-party status
2. **Deposition topics** — subject matter, 30(b)(6) notice topics if applicable
3. **Case materials** — produced documents, pleadings, prior testimony (provide what's available)
4. **Deponent type** — fact witness, party, corporate rep, or expert

If materials are unavailable, the skill will prompt for information needed to guide document identification.

## Output Structure / Process

### Phase 1: Document Identification

**A. By Connection to Deponent**

| Category | What to Find |
|----------|-------------|
| Authored | Documents the deponent wrote, signed, or created |
| Received | Documents addressed to or received by the deponent |
| CC'd/BCC'd | Documents where deponent was copied |
| Mentioned | Documents referencing the deponent by name |
| Custodial | Documents from deponent's files or email account |

**B. By Topic**

| Category | What to Find |
|----------|-------------|
| Key Events | Documents about events deponent will testify about |
| Decisions | Documents about decisions deponent made or participated in |
| Communications | Correspondence involving the deponent |
| Policies | Policies deponent was subject to or responsible for |
| Records | Business records deponent maintained or used |

**C. Prior Statements**

| Type | Examples |
|------|----------|
| Prior testimony | Depositions in this or other cases |
| Sworn statements | Affidavits, declarations |
| Discovery responses | Interrogatory answers, RFA responses where deponent is identified |
| Other | Written or recorded statements |

---

### Phase 2: Document Inventory

| Doc ID | Description | Date | Bates | Connection | Category | Key Pages | Notes |
|--------|-------------|------|-------|------------|----------|-----------|-------|
| | | | | | | | |

**Connection types:** Authored · Received · CC'd · Mentioned · Custodial · Topic-related  
**Categories:** Authentication · Impeachment · Key Fact · Background · Pleading/Discovery

---

### Phase 3: Exhibit Candidate List

| Exhibit # | Document | Bates/ID | Topic | Purpose | Priority |
|-----------|----------|----------|-------|---------|----------|
| | | | | | Essential / Likely / Backup |

**Organization:** Chronological (narrative depositions) · Topical (issue-focused) · Strategic (examination sequence)

---

### Phase 4: Gap Analysis

**Standard checklist by deponent type:**

| Deponent Type | Documents to Verify |
|---------------|---------------------|
| Any deponent | Resume/CV, org chart, job description, prior testimony in this case |
| Party | Complaint/Answer, interrogatory responses, RFA responses, produced documents |
| Employee | Personnel file (if relevant), training/disciplinary records, email samples |
| 30(b)(6) rep | Corporate org docs, policies/procedures by notice topic, prior 30(b)(6) testimony |
| Expert | Expert report, CV, publications, fee agreement, prior testimony list, materials considered |

**Gap Analysis Output:**

| Missing Document | Why It Matters | Potential Source | Action Required |
|-----------------|----------------|-----------------|-----------------|
| | | | |

---

### Phase 5: Impeachment Index

| Document | Bates/ID | Document Says | Expected Testimony | Inconsistency | Approach |
|----------|----------|---------------|-------------------|---------------|----------|
| | | "[Quote]" | | | |

For each entry, note: (1) exact page/paragraph of the statement, (2) questions to commit the witness before confrontation, (3) follow-up after introduction.

---

### Phase 6: Final Output Package

```
DEPOSITION DOCUMENT ASSEMBLY
=============================
Deponent:          [Name / Role]
Deposition Date:   [Date]

DOCUMENT SUMMARY
----------------
Total Documents:   [#]
  Authentication:  [#]
  Impeachment:     [#]
  Key Fact:        [#]
  Background:      [#]
  Pleadings/Disc:  [#]

GAPS IDENTIFIED
---------------
1. [Missing document] — Action: [Step]
2. [Missing document] — Action: [Step]

PREPARATION TASKS
-----------------
[ ] Obtain missing documents (see Gap Analysis)
[ ] Prepare clean exhibit copies
[ ] Number/tab exhibits; prepare witness, opposing counsel, reporter, and working sets
[ ] For digital depositions: load documents in presentation software, test screen sharing
[ ] Review impeachment documents; integrate into deposition outline
```

## Guidelines

- **Impeachment documents:** Do not pre-disclose impeachment exhibits if jurisdiction permits surprise; keep separate from main exhibit binder
- **30(b)(6):** Exhibits must align with designated notice topics — flag documents outside the notice scope
- **Authentication foundation:** Identify which deponent can authenticate each exhibit before trial; note in inventory
- **FRCP 30(f):** Original exhibits must be annexed to the deposition record unless parties stipulate otherwise [VERIFY local rules]
- **FRE 901-902:** Plan authentication method (witness testimony, self-authentication, stipulation) for each proposed exhibit
- **FRE 408:** Label any settlement-adjacent communications if used for a non-settlement purpose
- Cross-reference with `deposition-preparation` (outline), `deposition-questioning-techniques` (document use during exam), and `deposition-30b6-corporate-rep` (corporate rep specifics)
