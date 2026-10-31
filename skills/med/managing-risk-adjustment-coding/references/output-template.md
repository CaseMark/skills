# Output Template

Produce the header and the sections below in order. Every diagnosis row names its encounter, date of service, provider and credential, and the page or line that supports it. Put detail in tables; keep narrative short.

## Contents

1. Header
2. Section 1. Determination summary
3. Section 2. Declined parts
4. Section 3. Source register and encounter ledger
5. Section 4. Encounter eligibility screen
6. Section 5. Diagnosis validation table
7. Section 6. HCC and RAF impact
8. Section 7. Two-way reconciliation
9. Section 8. RADV support packet (when asked)
10. Section 9. Reconciliation table (conflicts)
11. Section 10. Gaps and query candidates
12. Section 11. Hand-offs
13. Section 12. Open items and `[VERIFY]` list

## Header

- Member identifier (de-identified), program (MA non-PACE, PACE, ACA individual or small group), plan or contract if given.
- Payment year or benefit year; dates of service in scope; model, for example "2024 CMS-HCC model (V28), 100% for PY 2027; diagnoses from 2026 dates of service".
- Review type: prospective (pre-visit), concurrent (pre-submission), retrospective two-way chart review, RADV preparation, or program design.
- ICD-10-CM guideline year applied to each date of service.
- Preparer note: "Draft for certified coder, CDI and compliance review."

## 1. Determination summary

| Diagnosis or HCC | Result | Action | Basis in one line | Blocking open item |
|---|---|---|---|---|
| | Supported / Supported at a different code / Not supported / Ineligible source / Outside period for PY <year> / Cannot determine | Submit / Retain / Delete / Query candidate / No action | | |

Counts: submitted codes reviewed, retained, to delete; candidate codes reviewed, to submit, to query. A summary with additions and no deletion line is incomplete.

## 2. Declined parts

Use only these labels, one row per declined part, before any analysis. Write "None" when nothing was declined.

| Label | Use when the request asks to | What the output does instead |
|---|---|---|
| Declined: add-only scope (restated as two-way review) | Review or submit additions only, or leave unsupported submitted codes in place | Runs the two-way review of the same records |
| Declined: retain or not report unsupported code (routed) | Keep, defend or not report a known unsupported paid code, or endorse a go-forward-only fix | States Delete and the 42 CFR 422.326 duty; routes to conducting-false-claims-analysis |
| Declined: leading prompt or pre-filled diagnosis | Build a confirm checkbox, a pre-filled assessment or a default code | Supplies non-leading evaluation prompts |
| Declined: capture-count incentive (routed) | Draft pay, bonuses, quotas or talking points tied to HCCs or gaps captured | Routes the design to conducting-false-claims-analysis |
| Declined: documentation change | Add an addendum for a diagnosis not addressed at the visit, backdate, have someone else sign or attest, or re-link a chart review record | Names the late-entry policy route or a non-leading query candidate |

| Label | Requested item, quoted | Where it is handled |
|---|---|---|

## 3. Source register and encounter ledger

| Source | Type | Date of service | Provider and credential | Signed? | Status |
|---|---|---|---|---|---|
| | Office note, hospital outpatient, inpatient record, HRA, telehealth note, radiology report, lab, problem list, superbill, vendor file, suspect list | | | Yes (method) / No / n/a | Reviewed / Not relevant / Unreadable after attempt / Still needed |

## 4. Encounter eligibility screen

| Encounter | Face-to-face or audio-video? | Acceptable source? | Acceptable provider type for the payment year? | Signature and credential | Date inside period? | Result |
|---|---|---|---|---|---|---|
| | | | | | | Eligible / Ineligible source (name the test) / Outside period for PY <year> (name each open run that holds the date) / Cannot determine |

## 5. Diagnosis validation table

| # | Condition as written | Encounter | Supporting text (quote, page or line) | Guideline applied | Code | Result | Action |
|---|---|---|---|---|---|---|---|

Rules: quote the assessment or plan text, not the problem list; for a "history of" condition show the test applied (I.C.2.m malignancy, Z86.73 stroke); for an uncertain term cite IV.H and code the sign or symptom; for a specificity change show both codes.

## 6. HCC and RAF impact

| Code | HCC (model version) | Hierarchy result | Relative factor (segment, table) | Counted? |
|---|---|---|---|---|

Then: the sum of counted HCC factors, before and after the review, with the components included and excluded named (demographic, interaction, payment-HCC count, normalization, MA coding pattern adjustment). Show the script or the arithmetic. Dollar figures only with their inputs, labeled illustrative.

## 7. Two-way reconciliation

| Direction | Code | HCC | Source record | Reason | Owner | Next step |
|---|---|---|---|---|---|---|
| Delete | | | | Not supported / Ineligible source | | Deletion through the plan's correction process; overpayment question routed |
| Submit | | | | Supported on an eligible encounter | | Linked CRR or encounter correction to that encounter |
| Query | | | | Clinical indicator without a documented diagnosis | | Non-leading query under the query policy |

## 8. RADV support packet (when asked)

| Audited HCC (with model version, e.g., V24HCC19) | Best record (type, date, provider, credential) | Support location | Code abstracted | Fallback record | Risk note |
|---|---|---|---|---|---|

## 9. Reconciliation table (conflicts)

| # | Fact | Source A says | Source B says | Controlling source and why | Effect on result |
|---|---|---|---|---|---|

Typical rows: vendor code list against the encounter note; problem list against assessment; claim date against note date; credential on the claim against the signature block; CMS-HCC against HHS-HCC numbering.

## 10. Gaps and query candidates

| Gap | Diagnosis affected | Gap class (unknown fact / source conflict / unverified external lookup / policy election) | Who can resolve | Compliant next step |
|---|---|---|---|---|

A query candidate states the clinical indicator and asks the provider to evaluate; it never proposes the answer and never asks for an entry dated back to a past visit.

## 11. Hand-offs

| To skill | Why | What is passed | What this review did not do |
|---|---|---|---|
| conducting-false-claims-analysis | MA risk adjustment overpayments under 42 CFR 422.326, one-sided or add-only chart reviews, raise-only query policies, capture-count incentives | The finding, years, codes, records | Did not assess knowledge, materiality, damages or disclosure |
| managing-cdi-programs | Query wording | Clinical indicators and encounter | Did not draft the query |
| managing-compliance-audits | Program-level sample design | Error findings by category | Did not design the sample |
| legal-research | RADV appeal or litigation status (no dedicated skill) | Audit report and dates | Did not advise on appeal rights |

## 12. Open items and `[VERIFY]` list

| # | Open item | Depends on | Owner | Next action | Changes a result? |
|---|---|---|---|---|---|

Then each `[VERIFY]` statement relied on, with the document that would settle it.

Close with: "Draft for certified coder, CDI and compliance review. Not a submission, deletion or attestation, and not legal advice."
