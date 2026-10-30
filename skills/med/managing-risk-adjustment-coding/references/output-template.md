# Output Template

Produce the header and the sections below in order. Every diagnosis row names its encounter, date of service, provider and credential, and the page or line that supports it. Put detail in tables; keep narrative short.

## Contents

1. Header
2. Section 1. Determination summary
3. Section 2. Source register and encounter ledger
4. Section 3. Encounter eligibility screen
5. Section 4. Diagnosis validation table
6. Section 5. HCC and RAF impact
7. Section 6. Two-way reconciliation
8. Section 7. RADV support packet (when asked)
9. Section 8. Reconciliation table (conflicts)
10. Section 9. Gaps and query candidates
11. Section 10. Hand-offs
12. Section 11. Open items and `[VERIFY]` list

## Header

- Member identifier (de-identified), program (MA non-PACE, PACE, ACA individual or small group), plan or contract if given.
- Payment year or benefit year; dates of service in scope; model, for example "2024 CMS-HCC model (V28), 100% for PY 2027; diagnoses from 2026 dates of service".
- Review type: prospective (pre-visit), concurrent (pre-submission), retrospective two-way chart review, RADV preparation, or program design.
- ICD-10-CM guideline year applied to each date of service.
- Preparer note: "Draft for certified coder, CDI and compliance review."

## 1. Determination summary

| Diagnosis or HCC | Result | Action | Basis in one line | Blocking open item |
|---|---|---|---|---|
| | Supported / Supported at a different code / Not supported / Ineligible source / Cannot determine | Submit / Retain / Delete / Query candidate / No action | | |

Counts: submitted codes reviewed, retained, to delete; candidate codes reviewed, to submit, to query. A summary with additions and no deletion line is incomplete.

## 2. Source register and encounter ledger

| Source | Type | Date of service | Provider and credential | Signed? | Status |
|---|---|---|---|---|---|
| | Office note, hospital outpatient, inpatient record, HRA, telehealth note, radiology report, lab, problem list, superbill, vendor file, suspect list | | | Yes (method) / No / n/a | Reviewed / Not relevant / Unreadable after attempt / Still needed |

## 3. Encounter eligibility screen

| Encounter | Face-to-face or audio-video? | Acceptable source? | Acceptable provider type for the payment year? | Signature and credential | Date inside period? | Result |
|---|---|---|---|---|---|---|
| | | | | | | Eligible / Ineligible source (name the test) / Cannot determine |

## 4. Diagnosis validation table

| # | Condition as written | Encounter | Supporting text (quote, page or line) | Guideline applied | Code | Result | Action |
|---|---|---|---|---|---|---|---|

Rules: quote the assessment or plan text, not the problem list; for a "history of" condition show the test applied (I.C.2.m malignancy, Z86.73 stroke); for an uncertain term cite IV.H and code the sign or symptom; for a specificity change show both codes.

## 5. HCC and RAF impact

| Code | HCC (model version) | Hierarchy result | Relative factor (segment, table) | Counted? |
|---|---|---|---|---|

Then: the sum of counted HCC factors, before and after the review, with the components included and excluded named (demographic, interaction, payment-HCC count, normalization, MA coding pattern adjustment). Show the script or the arithmetic. Dollar figures only with their inputs, labeled illustrative.

## 6. Two-way reconciliation

| Direction | Code | HCC | Source record | Reason | Owner | Next step |
|---|---|---|---|---|---|---|
| Delete | | | | Not supported / Ineligible source | | Deletion through the plan's correction process; overpayment question routed |
| Submit | | | | Supported on an eligible encounter | | Linked CRR or encounter correction to that encounter |
| Query | | | | Clinical indicator without a documented diagnosis | | Non-leading query under the query policy |

## 7. RADV support packet (when asked)

| Audited HCC (with model version, e.g., V24HCC19) | Best record (type, date, provider, credential) | Support location | Code abstracted | Fallback record | Risk note |
|---|---|---|---|---|---|

## 8. Reconciliation table (conflicts)

| # | Fact | Source A says | Source B says | Controlling source and why | Effect on result |
|---|---|---|---|---|---|

Typical rows: vendor code list against the encounter note; problem list against assessment; claim date against note date; credential on the claim against the signature block; CMS-HCC against HHS-HCC numbering.

## 9. Gaps and query candidates

| Gap | Diagnosis affected | Gap class (unknown fact / source conflict / unverified external lookup / policy election) | Who can resolve | Compliant next step |
|---|---|---|---|---|

A query candidate states the clinical indicator and asks the provider to evaluate; it never proposes the answer and never asks for an entry dated back to a past visit.

## 10. Hand-offs

| To skill | Why | What is passed | What this review did not do |
|---|---|---|---|
| conducting-false-claims-analysis | Known unsupported submitted codes, add-only history, incentive design, prior-year patterns | The finding, years, codes, records | Did not assess knowledge, materiality, damages or disclosure |
| managing-cdi-programs | Query wording | Clinical indicators and encounter | Did not draft the query |
| managing-compliance-audits | Program-level sample design | Error findings by category | Did not design the sample |
| legal-research | RADV appeal or litigation status (no dedicated skill) | Audit report and dates | Did not advise on appeal rights |

## 11. Open items and `[VERIFY]` list

| # | Open item | Depends on | Owner | Next action | Changes a result? |
|---|---|---|---|---|---|

Then each `[VERIFY]` statement relied on, with the document that would settle it.

Close with: "Draft for certified coder, CDI and compliance review. Not a submission, deletion or attestation, and not legal advice."
