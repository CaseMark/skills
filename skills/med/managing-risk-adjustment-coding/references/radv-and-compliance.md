# RADV, Two-Way Review and Compliance

Rules for retrospective review design, chart review records and addenda, RADV readiness, recapture and query programs, and the facts that send a matter to fraud and overpayment analysis. Full citations and dates checked are in the primary sources file.

## Contents

1. Two-way review is the standard
2. Chart review records, linking and addenda
3. RADV audit methodology (CMS-HCC)
4. Recapture, suspect lists and queries
5. False Claims Act exposure and routing
6. Settlements and pending cases (verified facts only)

## 1. Two-way review is the standard

- Plan sponsors must "ensure the accuracy and integrity of risk adjustment data", and when an internal review finds submitted codes that do not meet the submission requirements, the sponsor "is responsible for deleting the submitted diagnosis codes as soon as possible" (MMCM ch. 7, §40).
- As a condition of each monthly payment, the CEO, CFO or a delegate reporting directly to one of them certifies, on best knowledge, information and belief, the accuracy, completeness and truthfulness of data CMS requests (42 CFR 422.504(l)).
- An MA organization must report and return an overpayment within 60 days after it has identified it; "identified" means it knowingly receives or retains the overpayment, with "knowingly" as defined in the False Claims Act; the look-back is the 6 most recent completed payment years; a retained overpayment is an obligation under 31 U.S.C. 3729(b)(3) (42 CFR 422.326, as amended Dec. 9, 2024).
- Exception during RADV: for a contract selected for audit, CMS instructs the plan to suspend overpayment reporting and data corrections for that payment year for enrollees in the audit's sampling frame until further notice; all other plan-identified overpayments still follow 422.326 (PY 2024 RADV methods, §11; 422.326(d)).

Design consequence: a retrospective chart review reads the same records for every submitted diagnosis and every candidate diagnosis. Its output has adds, deletes and query candidates. A review scoped to additions only, or one that records unsupported submitted codes without a deletion step, is the practice alleged in United States v. Anthem (Section 6) and is not a design this skill drafts.

## 2. Chart review records, linking and addenda

- A chart review record (CRR) reports diagnoses found in a medical record review. A linked CRR points to the encounter data record for the visit it reviewed; an unlinked CRR does not. From the CY 2027 midyear run, diagnoses from unlinked CRRs with 2026 dates of service no longer count for non-PACE organizations, except for members who switched to a contract in a different parent organization (CY 2027 Rate Announcement; HPMS memo July 9, 2026).
- CMS found about 85% of the 88.8 million unlinked CRRs submitted in 2023 for 2024 payment could not be matched to any submitted encounter on beneficiary, billing provider and dates of service within three days (CY 2027 Rate Announcement). A commenter warned that plans could convert unlinked CRRs into linked ones. Link a CRR only to the encounter whose record actually contains the support; linking to an unrelated encounter to keep a diagnosis is a false record.
- Addenda: a late entry follows the facility's amendment policy, is dated when written, identifies its author, and documents what happened at the visit. An addendum written months later to add a diagnosis the provider did not consider or address at the visit does not create support (this is the conduct alleged and settled in the Kaiser matter, Section 6). Route amendment-policy questions to managing-medical-records-compliance.

## 3. RADV audit methodology (CMS-HCC)

| Element | Current position (checked 2026-10-30) | Source |
|---|---|---|
| Authority | MA organizations and providers must submit a sample of medical records for validation; CMS "may extrapolate" contract-level findings for PY 2018 onward | 42 CFR 422.310(e), 422.311(a) (eCFR text) |
| 2023 RADV final rule | Extrapolation from PY 2018; no FFS Adjuster; effective April 3, 2023 | 88 FR 6643 (Feb. 1, 2023) |
| Status of that rule | Vacated and remanded Sept. 25, 2025 as not a logical outgrowth of the proposal (Humana Inc. v. Becerra, No. 4:23-cv-00909-O, N.D. Tex.); appeal No. 25-11293 (5th Cir.), argued Oct. 5, 2026; no appellate ruling found as of Oct. 6, 2026 `[VERIFY]` | Opinion; PY 2024 RADV methods fn. 6; Georgetown litigation tracker |
| Extrapolation in current audits | CMS designed PY 2020 and PY 2024 audits to calculate extrapolated overpayments but has not decided whether to collect extrapolated amounts or only sampled-enrollee overpayments | PY 2020 methods (Mar. 20, 2026); PY 2024 methods (Aug. 28, 2026) |
| 2025 expansion | May 21, 2025: audit all eligible MA contracts each payment year in newly initiated audits (about 550), 35 to 200 records per contract, coders from 40 to about 2,000, finish PY 2018-2024 audits | CMS press release |
| Sampling | Enrollees drawn from those CMS's predictive models rank most likely to lose risk score on audit (top quartile from PY 2020); 35, 50, 100 or 200 per contract by frame size | PY 2020 and PY 2024 methods |
| Record limits | At least one valid record per audited HCC; at most twice the number of audited HCCs per enrollee | PY 2024 methods, §6 |
| Coding standard | ICD-10-CM Official Guidelines and AHA Coding Clinic; up to three independent certified-coder reviews | PY 2024 methods, §8 |
| Discrepancy | An HCC used for payment that is not validated by the abstracted codes | PY 2024 methods, §9 |
| Appeals | Reconsideration and further levels under 42 CFR 422.311(c) | PY 2024 methods, fn. 7 |
| Record retention | 10 years | 42 CFR 422.504(d), cited in PY 2024 methods, App. B |
| PY 2024 dates | Enrollee list Sept. 11, 2026; window opens Sept. 18, 2026; records due Feb. 5, 2027, 11:59 pm ET; hardship requests Feb. 19, 2027 | PY 2024 methods, §3 |

Readiness packet per HCC: the one best record (valid source, eligible provider, signed with credentials, complete date inside the period), the page and line that supports the code, the code and its HCC with model version, and a fallback record. A record that supports the HCC only by inference is not "best".

## 4. Recapture, suspect lists and queries

- HCCs do not carry forward. Each payment year needs a supported diagnosis from that year's dates of service, so a chronic condition is "recaptured" only when the provider evaluates it at an eligible visit and documents it.
- A suspect or pre-visit list may tell a provider which conditions to evaluate. It may not supply a diagnosis for the provider to accept: no "confirm" checkbox, no pre-filled assessment text, no default code. The prompt names the clinical indicator and asks the provider to evaluate and document whatever the provider finds, including "resolved" or "not present".
- Queries follow the facility's compliant query policy (non-leading, multiple choice with "other" and "unable to determine", clinical indicators cited). Draft wording goes to managing-cdi-programs.
- Incentives, quotas or scorecards tied to the number of diagnoses or HCCs captured, rather than to documentation accuracy, are a compliance risk flag (the Kaiser allegations included physician goals and bonuses tied to risk adjustment diagnoses). Route the incentive design to conducting-false-claims-analysis; do not draft it.
- Report capture metrics with their counterpart: deletion rate, query "not present" rate and RADV-style validation rate.

## 5. False Claims Act exposure and routing

Elements to flag, not decide: liability attaches to a person who knowingly presents a false claim, knowingly makes or uses a false record material to a false claim, or knowingly conceals or improperly avoids an obligation to pay money to the Government (31 U.S.C. 3729(a)(1)(A), (B), (G)). "Knowingly" includes deliberate ignorance and reckless disregard and requires no specific intent to defraud (3729(b)(1)).

Facts that trigger routing to conducting-false-claims-analysis (state the fact, cite the record, stop the analysis there): a known unsupported diagnosis that was submitted and paid and is not being deleted; a review design that only adds; a request to keep, link or "fix" a code without support; a pattern finding (for example a high error rate in an OIG high-risk group) affecting prior payment years; incentives tied to capture counts; a pending RADV audit with known unsupported HCCs. This skill does not opine on scienter, materiality, damages or disclosure strategy.

## 6. Settlements and pending cases (verified facts only)

| Matter | Date | Amount | Allegation as stated by DOJ or OIG | Status |
|---|---|---|---|---|
| Kaiser Permanente affiliates (complaint filed N.D. Cal., Oct. 2021) | Jan. 14, 2026 | $556 million | 2009-2018: mined past history, sent queries urging physicians to add diagnoses by addenda months or over a year after visits, diagnoses often unrelated to the visit; physician and facility goals and bonuses tied to adding diagnoses | Settled; allegations only |
| Independent Health | Dec. 20, 2024 | Up to $98 million | Knowingly submitting or causing invalid diagnosis codes for MA enrollees | Settled |
| The Cigna Group | Sept. 30, 2023 | $172,294,350 | Submitting and failing to withdraw inaccurate and untruthful diagnosis codes | Settled |
| Martin's Point Health Care | July 31, 2023 | $22,485,000 | Submitting inaccurate diagnosis codes for MA enrollees | Settled |
| United States v. Anthem, No. 1:20-cv-02593 (S.D.N.Y.) | Complaint Mar. 2020 | n/a | Chart review program run solely to add codes, ignoring the duty to delete inaccurate diagnoses ("one-sided" chart review), early 2014 to early 2018 | Pending as of Oct. 28, 2026; allegations, not findings |

Name a matter only with the facts in this table. Settlements resolve allegations without findings of liability unless the release says otherwise; say so when citing one.
