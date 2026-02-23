---
name: discovery-and-bill-of-particulars
description: >-
  Drafts U.S. litigation pleadings that combine a discovery demand with a bill
  of particulars to force targeted disclosure, narrow vague theories, and
  build a record for compulsion or sanction relief. Use after initial
  pleadings/return date in criminal defense (primary) or discovery-active
  civil actions when allegations are underspecified, evidence is opaque, or
  trial-preparation notices are unclear. Trigger keywords: discovery demand,
  bill of particulars, motion to compel, FRCP 16, FRCP 26, FRCP 33, FRCP 34,
  FRCP 37, particularity.
tags:
  - drafting
  - litigation
  - pleading
---

# Demand for Discovery and Bill of Particulars

Generate a court-ready pleading that enforces proportional discovery, specifies ambiguous factual/theory allegations, and preserves enforceable compliance leverage.

## Prerequisites

1. Confirm jurisdiction, court, division/department, case number, local rules, and any standing filing or formatting orders.
2. Confirm case posture and whether the matter is criminal, civil, or hybrid procedural posture.
3. Collect charging document/complaint, prior pleadings, motions, stipulations, and existing discovery responses.
4. Identify the ambiguous allegations or information gaps blocking trial preparation.
5. Identify all potential privilege categories and current protective-order constraints.
6. Decide preferred enforcement path: meet-and-confer, motion practice sequence, fee/sanction posture.

## Output Structure / Process

### 1) Regime selection and governing authority block

Output this matrix first:

| Track | Governing rules | Core use | Baseline deadline | Notes |
|---|---|---|---|---|
| Criminal | Fed. R. Crim. P. 16; 7(f) + local criminal practice | Discovery + particulars for notice and defense prep | Local rule/time limit [VERIFY] | For charge specificity and due-process clarity |
| Federal civil | FRCP 26(b)(1), 26(e), 26(g), 33, 34, 36, 37 | Discovery scope + itemized requests | FRCP 33/34 baseline 30 days from service [VERIFY] | Check local deviations |
| State | State procedure + local rules | Adapted template | State statute/rule specific [VERIFY] | Confirm nomenclature and service mechanics |

### 2) Intake-driven issue framing (fill-in schema)

```text
Court: [jurisdiction]
Judge/department: [if required]
Plaintiff/Prosecution: [name]
Defendant: [name]
Case number: [xxxx]
Motion/declaration label: Demand for Discovery and Bill of Particulars
Strategic objective: [e.g., narrow charges, obtain witness/evidence disclosure, prepare defenses]
```

### 3) Draft the authority and need section

- State party status, case stage, and why relief is necessary.
- Criminal: cite FRCP 16 and FRCP 7(f) for disclosure and particularized charge notice.
- Civil: cite FRCP 26(b)(1), 33, 34, 36, 37 for relevance, specificity, and sanctions path.
- Include proportionality statement and statement that requests avoid harassment/fishing.

### 4) Discovery demands (numbered, machine-readable)

Use one numbered list with strict specificity. Required columns:

| Req. | Category | Custodian/source | Time range | Format | Rationale |
|---|---|---|---|---|---|
| 1 | Documents/es | [party + affiliates] | [from/to] | Native + metadata [if ESI] | [defense use] |
| 2 | Communications | [emails/texts/notes] | [from/to] | Native + native index | [defense use] |
| 3 | Witness IDs | [trial/public witnesses] | [if ongoing] | Contact + summary scope | Trial prep/notice |
| 4 | Expert materials | [experts] | [all] | CVs, reports, data, opinions, testing basis | Rebuttal/cross prep |

Template for each item:

```text
[No.] Request for [documents|communications|identity|expert materials]:
Request:
Ground:
Response format:
Privilege carve-out:
```

### 5) Bill of particulars module (civil+criminal branches)

```text
Demand [No.]:
Allegation to specify:
Exact information required:
Reason tied to element/issue:
```

Criminal nodes:
- acts constituting each charged offense
- exact dates/times and locations
- identified participants/co-conspirators/accomplices
- manner and means for each offense
- nexus to venue/elements/defenses

Civil nodes:
- contract/ statutory provisions breached + breach conduct
- itemized damages per category + calculation basis
- each referenced document described with enough specificity for production

### 6) Compliance controls and deadlines

- State response deadline and service method.
- Require complete, verified responses when required by local/operative rules.
- Require supplementation duty as new information becomes known.
- Include fallback sequence: meet-and-confer → motion to compel → sanctions/preclusion/fee recovery.
- Prefer explicit court-ready language for incomplete, evasive, or untimely responses.

### 7) Certification, signature, and service block

```text
I certify under [applicable rule] that this demand is grounded in law, not interposed for delay/harrasment, and not unduly burdensome.
Attorney:
Bar/firm/contact:
/s/ [Attorney]
Date:
Certificate of Service:
Served on [party/counsel] via [CMS/e-service/mail]
Date/time/method:
```

### 8) Final control checks

- Every request mapped to a litigation purpose.
- Privilege and nonparty constraints acknowledged.
- No duplicate/mutually inconsistent requests.
- No invented deadlines; each date/time/citation verified per applicable rules.
- Local captioning/formatting requirements reflected.

## Guidelines

- Keep the document narrowly tailored: each request should be specific, relevant, and discoverable.
- Use parallel phrasing for criminal and civil tracks; never mix standards without indicating governing rule.
- Separate factual requests from relief/remedy requests to reduce objections.
- Build an escalation-ready record: avoid vague terms, include exact relief language.
- Mark jurisdictional assumptions with `[VERIFY]` when local law or state provisions are uncertain.
