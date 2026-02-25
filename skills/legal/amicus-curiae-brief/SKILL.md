---
name: amicus-curiae-brief
description: >
  Drafts filing-ready U.S. amicus curiae briefs for appellate courts with
  rule-anchored compliance, additive thesis selection, record-safe fact handling,
  and verified authority control. Use this skill when asked to draft an amicus
  brief, friend of the court brief, FRAP 29 amicus, FRAP 32 amicus, Supreme
  Court Rule 37 amicus, cert-stage or merits-stage amicus, or when preparing
  consent/leave and disclosure language for amici. Also trigger when the user
  mentions amicus interest statement drafting, non-party brief filing, or asks
  about amicus procedural requirements. Even if the user just says "we need to
  file an amicus" or "draft a friend of the court brief," use this skill.
tags:
  - brief
  - drafting
  - litigation
---

# Amicus Curiae Brief

## Why This Skill Exists

Courts grant amici permission to participate because they bring perspectives the parties cannot. When amicus briefs merely restate party arguments or fail procedural requirements, they waste judicial resources, damage the amicus's credibility, and risk sanctions or striking. The most common failures: missing disclosure requirements, introducing new adjudicative facts not in the record, duplicating party arguments without additive value, and missing word limits or formatting rules.

This skill produces a procedurally compliant, substantively additive amicus brief with verified authority control and record-safe fact handling.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft." Gather:

1. **Forum and stage** — court, case caption, docket number, cert vs. merits, panel or en banc
2. **Deadlines** — docket schedule and any amicus-specific order
3. **Party briefs** — at least the supported party's principal brief; ideally all briefs filed
4. **Record anchors** — record citations used by the parties for any adjudicative facts
5. **Amicus profile** — legal entity, mission, constituency, expertise, and relationship to parties
6. **Position** — supports petitioner/respondent or neither; requested disposition
7. **Consent/leave** — written consent status and whether a motion is required
8. **Disclosure facts** — authorship and funding facts for Rule 29/Rule 37 disclosures
9. **Formatting rules** — applicable word/page limits, font, spacing, cover color, copy counts
10. **Source set** — primary sources for any legislative facts or empirical claims

**If the user doesn't respond**, apply and clearly label these defaults: federal circuit FRAP 29 rules; standard word limits for amicus; hybrid expertise/systemic-consequences thesis approach.

---

## Step 1: Build Compliance Map

| Field | Fill-In |
|---|---|
| Rule Set | FRAP 29/32, Supreme Court Rule 37, or state rule text |
| Deadline | Date/time and trigger brief |
| Word/Page Limit | Rule section and limit |
| Required Sections | Interest, disclosures, summary, argument, conclusion |
| Certificates | Compliance, service, corporate disclosure if required |
| Filing Format | ECF/PDF, paper copies, cover color [VERIFY] |
| Local Deviations | Circuit/state rule additions |
| Signature | Admitted counsel requirement; Supreme Court Bar if applicable |

---

## Step 2: Select Additive Thesis

Extract the party's argument chain and identify the gap the amicus can fill. Pick one primary thesis that is not a restatement of party arguments.

Choose one of:
- **Expertise translation** — technical or industry knowledge the parties lack
- **Systemic consequences** — how the ruling affects non-parties and broader systems
- **Doctrinal harmonization** — how the ruling fits with related precedent or statutory schemes
- **Historical/structural framing** — legislative history, original understanding, or institutional design

State the thesis in one sentence suitable for the Summary of Argument.

### Record-Safety Matrix

| Fact Type | Allowed Use | Required Support |
|---|---|---|
| Adjudicative facts | Only as in record | Record cite from briefs or record |
| Legislative facts | Context only | Primary sources, stable citations |
| Predictive claims | Cautious language | Empirical or governmental sources |

---

## Step 3: Draft the Brief

### Brief Template

```text
COVER PAGE
TABLE OF CONTENTS
TABLE OF AUTHORITIES

DISCLOSURE STATEMENT (FRAP 29(a)(4)(E) or Rule 37.6)
STATEMENT OF INTEREST OF AMICUS CURIAE

SUMMARY OF ARGUMENT

ARGUMENT
I. [Conclusion heading with thesis]
   A. [Expertise/empirics/historical framing]
   B. [Application to legal choice before the court]
   C. [Administrability or systemic consequences]
II. [If needed: discrete second point, not duplicative]

CONCLUSION

CERTIFICATE OF COMPLIANCE
CERTIFICATE OF SERVICE
SIGNATURE BLOCK
```

### Argument Build Rules
- Use conclusion-style headings
- Tie each paragraph to a verified source or record cite
- Translate technical content into judge-friendly terms
- Address a predictable counterargument in each major section

---

## Step 4: Draft Certificates

```text
Certificate of Compliance
This brief complies with the type-volume limitation of [rule] because it
contains [X] words, excluding the parts exempted by [rule]. It complies
with typeface and type-style requirements of [rule] because it was prepared
in [software] using [font/size]. [VERIFY rule cites.]

Certificate of Service
I certify that on [date], I served this brief on all parties via
[ECF/other method].
```

Insert bracketed placeholders for any unconfirmed detail — never guess.

---

## Step 5: Produce Deliverables

### Mandatory Front Matter

At the top of every output, include:
1. **Assumptions Used** — forum, posture, consent status, thesis approach, governing rules
2. **Open Items / Needed Inputs** — missing party briefs, unconfirmed rule text, disclosure facts

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the initial brief, ask:

1. Does the thesis deliver a perspective the parties' briefs do not?
2. Are the disclosure facts (authorship, funding) confirmed and accurate?
3. Should additional authorities or empirical sources be incorporated?
4. Is the tone calibrated correctly for this court and this amicus's role?

---

## Quality Audit

Before finalizing, verify:

- Rule text verified against current forum rules
- Consent/leave requirements satisfied
- Disclosure statement matches rule text and confirmed facts
- No duplication of party arguments — thesis is additive
- All adjudicative facts tied to record cites
- All legislative facts sourced and framed as context
- Unverified authorities flagged `[VERIFY]`
- TOC/TOA accurate after pagination
- Word count and formatting compliance confirmed
- Assumptions and open items listed prominently
- Every factual assertion traceable to source or labeled as assumption

---

## Guidelines

- Do not restate party arguments; deliver a distinct thesis
- Do not introduce new legal issues unless the forum permits and counsel directs it
- Use `[VERIFY]` for any unconfirmed citation, rule text, or empirical claim
- Separate record facts from legislative facts and label record-sensitive material
- Keep tone judicial: restrained, analytic, non-partisan
- Confirm state appellate rules; do not assume FRAP applies
- Supreme Court briefs require Rule 37.6 disclosures and Supreme Court Bar signature [VERIFY]
- California Rule of Court 8.200(c) and NY Court of Appeals Rule 500.23 details must be confirmed [VERIFY]
- **Anti-hallucination**: Never fabricate case citations, rule text, or empirical data. Every authority must be verified or flagged
- **Attorney review required**: All output requires attorney review and approval before filing
