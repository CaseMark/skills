# Query Compliance and Improper Requests

Rules for drafting query candidates and for answering requests that would push a DRG beyond the documentation. Source: ACDIS/AHIMA Guidelines for Achieving a Compliant Query Practice, 2026 Update (August 2026; supersedes the 2022 version), read in full, plus the ICD-10-CM Official Guidelines FY 2027. Section numbers refer to the 2026 brief unless stated.

## Contents

1. What makes a query compliant
2. Formats: multiple choice, yes/no, verbal
3. When to query, and in which direction
4. Requests the skill declines
5. Query candidate template

## 1. What makes a query compliant

- Core requirements (Introduction; Section V): nonleading; clinically relevant indicators with their source; no reference to reimbursement or quality outcomes; the provider exercises independent clinical judgment.
- V.I.A: titles and tracking numbers visible to the provider carry no direction. "CDI provider query - respiratory status" is compliant; "Query for acute hypoxic respiratory failure" is not.
- V.I.B: never mention reimbursement impact, quality measures, denial mitigation or other reporting initiatives. No DRG numbers, weights, "MCC", "CC" or dollar figures in a query.
- V.I.C: include the clinical indicators that justify the query, each with its location in the record. Indicators may come from ED, laboratory, imaging, provider notes, ancillary professionals (nurses, dietitians, wound care, therapists), operative notes and social services, and from a prior encounter when relevant.
- V.I.C.2: no subjective interpretation. Report "heart rate 120", not "tachycardia"; "hemoglobin 10 g/dL", not "anemia". Quoting a provider or nursing note verbatim, with its source, is compliant.
- V.I.C.3: no added emphasis (bold, highlight, arrows), and never in answer options.
- V.I.D: uncertain-diagnosis options are used sparingly and only when supported by indicators.
- V.I.F: published criteria (for example ASPEN, KDIGO) may be attached with a citation, without marking a preferred answer.
- Technology prompts (EHR alerts, AI suggestions) that offer a diagnosis for a specific encounter are queries and must meet the same rules.

## 2. Formats: multiple choice, yes/no, verbal

- Multiple choice (V.II.A): usable in any circumstance. Options must be clinically relevant and supported by the indicators; irrelevant options are excluded; options may be in any order; an "Other, please specify" (or similar) option is required; there is no minimum number of options, but at least one clinically valid option plus an open-ended choice. Options must be reportable under UHDDS and Section III. "Unable to determine", "not clinically significant", "integral to" and similar are allowed when suitable; templates should include "unable to determine" when the scenario calls for it.
- "Unable to determine" means the provider cannot reach a conclusion on the evidence; it is not "unable to rule out" and not an uncertain diagnosis.
- Yes/no (Definitions; V.II): only to clarify an already documented diagnosis or relationship (POA status, cause and effect, substantiating a pathologist's or radiologist's finding). It may not introduce a new diagnosis. A yes/no query based solely on documentation by a clinician not authorized to diagnose (a dietitian's malnutrition note, a wound nurse's etiology) is inappropriate; use multiple choice with that note as an indicator. A POA yes/no query must offer "unable to determine".
- Clinical validation queries are best in multiple-choice form, with options such as "the diagnosis has been ruled out", "after further study the diagnosis is no longer valid", "the diagnosis is present (please provide supporting evidence)", plus "Other".
- Verbal queries are recorded with date and time, participants, indicators and sources, the nonleading statement, options and the response; the response must reach the permanent record.
- The query and response must be part of the health record, or the provider documents the answer in a note or addendum, before a code is assigned from it.

## 3. When to query, and in which direction

- Section VI lists, among others: a condition supported by indicators and reportable under Section III; unclear, incomplete or conflicting documentation; a documented diagnosis that the indicators do not appear to support (clinical validation); a condition documented by someone who is not a qualified provider; relationships, acuity or specificity; "history of" versus active; POA; ruled-in or ruled-out differentials; procedure intent or extent; complications.
- Queries are not required for every discrepancy (lack of business need, no added clarity), but must rest on the clinical data.
- Skill rule built on those criteria: choose query candidates by clinical indicators, in both directions. A review that queries only when the answer could raise the DRG, and leaves unsupported documented CC/MCCs unexamined, is selective in a way the criteria do not permit, and the pattern is a compliance risk to route to conducting-false-claims-analysis when it reflects policy.
- Query the provider who gave direct care for the issue; the attending resolves conflicts (Section VII). A physician advisor who did not treat the patient cannot answer.

## 4. Requests the skill declines

Decline the part named, say why in one line, and continue the compliant review.

| Request | Response | Authority |
|---|---|---|
| Add a diagnosis no provider documented (from labs, vitals, nursing, dietitian or therapist notes) | Declined request; list the indicators as a query candidate | I.A.19; I.B.14; III.B |
| Choose or resequence the principal diagnosis because the DRG pays more | Declined request; apply Section II and UHDDS | Section II; UHDDS |
| Change a POA indicator without documentation | Declined request; query POA if unclear | Appendix I |
| Draft a query that names the wanted diagnosis in the title, mentions DRG or payment, uses yes/no to introduce a diagnosis, or omits "Other" | Declined request; redraft compliantly | 2026 brief V.I.A, V.I.B, V.II |
| Send or ask a provider to document a condition "to capture the MCC" | Declined request | 2026 brief, core requirements |
| Drop a documented diagnosis because a payer uses different clinical criteria | Declined request; clinical validation query and denial-risk note | I.A.19; 2026 brief Section VI |
| Query only when the DRG would rise | Declined request; select on clinical grounds both ways | Section VI criteria; skill rule above |

## 5. Query candidate template

```
Title (neutral): CDI provider query - <body system or topic, no diagnosis>
To: <treating provider for this issue>        Encounter: <de-identified id>
Clinical indicators (verbatim or numeric, each with source):
  - <value or quote> (<document>, <date time>, <author role>)
Question (nonleading): Based on your clinical judgment, can the condition
  being evaluated or treated be further specified?
Options (no emphasis, any order, each supported by the indicators):
  [ ] <clinically supported option 1>
  [ ] <clinically supported option 2>
  [ ] Other (please specify): ________
  [ ] Unable to determine
Note to preparer (not sent): direction of DRG effect is not a reason to send
  or withhold this query.
```

Clinical validation variant: list the indicators found and those not found for the documented diagnosis, then offer "present (please document supporting evidence)", "ruled out", "no longer valid after further study", "Other".
