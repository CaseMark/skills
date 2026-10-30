# Output Template

Produce the header and the sections below in order. Every date shows its weekday. Every dollar figure names its source (claims extract, remittance, sample workpaper) and whether it is a paid amount, a billed charge, or an estimate. Put detail in tables; keep the narrative short.

## Contents

1. Header and source register
2. Section 1. Status and labels
3. Section 2. Issue matrix
4. Section 3. Element analysis
5. Section 4. Overpayment clock
6. Section 5. Quantification
7. Section 6. Exposure and settlement model
8. Section 7. Qui tam and retaliation risk
9. Section 8. Reconciliation table
10. Section 9. Hand-offs
11. Section 10. Open items and `[VERIFY]` list

## Header

- Entity that received payment (legal name, billing NPIs, TINs), programs affected, review period, today's date.
- Requester and role; whether the work is at counsel's direction (privilege is counsel's call, not this draft's).
- Trigger: internal audit, hotline report, contractor audit, counsel's Stark or AKS finding, subpoena, CID, unsealed qui tam.
- Inbound hand-off, if any: the stark-law-aks-compliance labels as received, the noncompliant periods, the affected DHS claims or the data needed to identify them, and the disclosure path label.
- Preparer note: "Draft for compliance officer and counsel review."

Source register, one row per file:

| File | Type | Date range | Status | Note |
|---|---|---|---|---|
| | claims extract, remittance, audit report, sample workpaper, hotline log, email, policy, contractor letter, counsel memo, subpoena or CID | | Reviewed / Not relevant / Unreadable after attempt / Still needed | |

## 1. Status and labels

**Report status**, one used exactly: **Ready for compliance and counsel review**; **Not ready: blocking issues** (name them). A request blocked by a hard stop is labeled **Declined: hard stop** where it is answered, with the reason and what is produced instead; the rest of the report continues.

Per issue, one of each:

- **FCA exposure**: not indicated / overpayment only / potential / undetermined.
- **Clock**: not started / running / suspended / expired / undetermined (with the deadline date).
- **Quantification**: known-claim amount / extrapolated estimate (valid design) / estimate not reportable: invalid sample / not yet quantified.
- **Disclosure path**: none indicated / CMS SRDP / OIG SDP / contractor refund / counsel decision required.

## 2. Issue matrix

| # | Issue | Program and payer | Billing entity (NPI, TIN) | Period (payment dates) | Claims affected | Paid amount | Theory | Source |
|---|---|---|---|---|---|---|---|---|

## 3. Element analysis

| Issue | Falsity | Scienter | Materiality | Causation | Evidence for | Evidence against | Authority |
|---|---|---|---|---|---|---|---|
| | Supported / Contested / Not supported / Undetermined | | | | | | |

Materiality rows always state what the payer knew and what it did after knowing. Causation rows for AKS-based claims state the governing circuit and its standard, or both readings.

## 4. Overpayment clock

| Element | Trigger event and date (weekday) | Source of the date | Period | Ends (weekday) | Status |
|---|---|---|---|---|---|
| Initial identification | | | | | |
| Investigation start | | | | | |
| Suspension end (earlier of completion or day 180) | | | | | |
| Report-and-return deadline | | | Unused days of the 60 | | |
| Cost report due date, if any | | | | | |
| Protocol acknowledgment, if any | | | | | |
| Lookback start (receipt date 6 years back) | | | | | |

Rejected candidate dates (quantification complete, board meeting, consultant report, refund approval), each with the reason it does not control.

## 5. Quantification

- Method: full review, or sample. For a sample: objective, population, frame (and how it differs from the population), sampling unit, size, random-number source, design, review criteria, estimator, point estimate, and the confidence interval if a contractor convention is shown.
- Known-claim amount: confirmed overpaid claims with claim numbers and paid amounts.
- Underpayments: listed, never netted for SDP purposes.

## 6. Exposure and settlement model

| Path | Base (paid amount) | Multiplier | Penalties (count x min; count x max) | Credits | Range | Assumptions |
|---|---|---|---|---|---|---|
| Contractor refund | | 1 | none | | | |
| OIG SDP | | at least 1.5 (false billing) or remuneration-based (kickback) | none; $20,000 or $100,000 minimum | | | |
| CMS SRDP | | `[VERIFY]` | | | | |
| Litigated FCA | | 3 (2 if 3729(a)(2) applies) | $14,308 to $28,619 per claim (assessed after July 3, 2025; no 2026 change) | | | |

## 7. Qui tam and retaliation risk

Who knows the facts and how; internal reports and responses; public disclosures; pending adverse actions against reporters (each routed to employment counsel); status of any sealed or unsealed action; the Zafirov status line from `references/fca-liability-and-damages.md`, section 9.

## 8. Reconciliation table

| # | Fact | Source A says | Source B says | Controlling source and why | Effect |
|---|---|---|---|---|---|

Typical rows: audit report date against the date the compliance officer received it; dashboard paid amount against remittance; counsel's noncompliant period against the claims extract period; sample frame against population.

## 9. Hand-offs

| To skill | When | What is passed | What this draft did not do |
|---|---|---|---|
| stark-law-aks-compliance | Counsel's legal analysis and opinion on Stark or AKS compliance, the 1320a-7b(g) reading for the forum, and the final disclosure path | Claim sets under each reading, clock status, settlement model | Did not decide Stark or AKS compliance |
| conducting-stark-law-analysis | Provider-side operational review of the arrangement against Stark exceptions | The arrangement facts and periods | Did not test exception elements |
| conducting-anti-kickback-analysis | Provider-side safe harbor documentation for a payment arrangement | The arrangement facts | Did not test safe harbor elements |
| managing-compliance-audits | Designing the audit sample and corrective action plan | Population, frame, error definition | Did not draw the sample |
| auditing-coding-accuracy | Claim-level coding review of sampled claims | Sample list, review criteria | Did not code the claims |
| managing-risk-adjustment-coding | MA diagnosis support and RADV issues behind an MA overpayment | Unsupported diagnoses, payment years | Did not validate diagnoses |
| managing-compliance-programs | Program-wide fixes after the finding | Root causes | Did not design the program |
| whistleblower-protection-policy | Anti-retaliation policy drafting | The retaliation risks found | Did not draft the policy |
| legal-research | 3730(h) case law, circuit rules marked `[VERIFY]`, state Medicaid overpayment rules; no dedicated skill exists | The question and forum | Did not research the rule |

## 10. Open items and `[VERIFY]` list

| # | Open item | Gap class (unknown fact / source conflict / unverified external lookup / policy election) | Owner | Next action | Changes a deadline or a label? |
|---|---|---|---|---|---|

Close with: "Draft for compliance officer and counsel review. Not legal advice, not a disclosure, and not a refund."
