# Overpayment Clock, Quantification and Disclosure Paths

Rules for the report-and-return obligation (42 U.S.C. 1320a-7k(d)), its regulations, overpayment quantification, and the three ways to resolve an identified overpayment. Read in full text on 2026-10-30 unless marked `[VERIFY]`.

## Contents

1. Which rule applies to whom
2. Identification, deadline and suspension (Parts A and B)
3. Clock table: one trigger per timed element
4. Lookback and reopening
5. Quantification: full review or statistically valid sample
6. Disclosure paths
7. Settlement modeling
8. Positions this skill will not take

## 1. Which rule applies to whom

| Person | Rule | Identification | 180-day suspension | Lookback |
|---|---|---|---|---|
| Provider or supplier, Medicare Parts A and B | 42 C.F.R. 401.305 | Knowingly receives or retains (401.305(a)(2)) | Yes, 401.305(b)(3) | 6 years from receipt (401.305(f)) |
| Medicare Advantage organization | 42 C.F.R. 422.326 | Knowingly receives or retains (422.326(c)); an overpayment exists only "after applicable reconciliation," the annual final risk adjustment data submission deadline under 422.310(g) (422.326(a)) | Not in the regulation; 60 days "unless otherwise directed by CMS for purposes of § 422.311" (RADV) (422.326(d)) | 6 most recent completed payment years (422.326(f)) |
| Part D sponsor | 42 C.F.R. 423.360 | Knowingly standard `[VERIFY]` text not read | `[VERIFY]` | 6 years `[VERIFY]` |
| Medicaid overpayment to a provider | Statute (1320a-7k(d) covers title XIX); no CMS Medicaid regulation located; state rules `[VERIFY]` | Statutory "knowing" | Not in the statute | State rule `[VERIFY]` |
| Provider paid by an MA plan or Medicaid managed care plan | Plan contract and state law; whether 1320a-7k(d) reaches the provider is `[VERIFY]` | | | |

A beneficiary is never a "person" under the statute (1320a-7k(d)(4)(C)(ii)). Name the entity that received the payment (billing NPI and TIN), not the parent or the department where the error arose.

## 2. Identification, deadline and suspension (Parts A and B)

- **Identified** when the person knowingly receives or retains an overpayment; "knowingly" has the FCA meaning (actual knowledge, deliberate ignorance, reckless disregard). This replaced, effective January 1, 2025, the 2016 standard ("determined, or should have determined through the exercise of reasonable diligence ... and quantified") (89 FR 97710, 98553, Dec. 9, 2024).
- **When the 60 days start** (89 FR 98336-98337): with an investigation under way, on actual knowledge of the overpayment; with deliberate ignorance or reckless disregard, on the date the person so acted. Quantification is not a precondition: the 60 days run even if the amount is not yet calculated, so as a practical matter the amount must be calculated inside the period.
- **Deadline** (401.305(b)(1)): the later of 60 days after identification or "the date any corresponding cost report is due, if applicable." Filing cost reports does not by itself make an overpayment "corresponding"; ask whether this overpayment is one the cost report reconciles, record the answer and its source, and compare both dates. Which overpayments correspond is `[VERIFY]` beyond the regulation text (the 2016 preamble was not read).
- **Suspension for investigation** (401.305(b)(3)): when a person has identified an overpayment and conducts a timely, good-faith investigation for related overpayments from the same or similar cause, the deadline for the initial and related overpayments is suspended until the earlier of (A) the investigation concluding and the aggregate amount being calculated, or (B) 180 days after the initial overpayment was identified. The suspension starts when the investigation starts. After it ends, only the unused part of the 60 days remains: the regulation text does not say this; it comes from the preamble's example (investigation started on day 20, so 40 days remain; 89 FR 98338). No investigation, or one that is not timely or not in good faith: no suspension.
- **Other suspensions** (401.305(b)(2)): OIG acknowledges an SDP submission (the 2026 SDP, section 1, says the suspension applies "as long as the submission is timely made", so submit before the deadline); CMS acknowledges an SRDP submission; an extended repayment schedule request under 401.603. Each ends on settlement, withdrawal, removal, or rejection or default.
- **Consequence** (401.305(e); 1320a-7k(d)(3)): an overpayment retained after the deadline is an FCA "obligation." The Civil Monetary Penalties Law also applies (OIG SDP 2026, section 1.B).
- **Reporting** (401.305(d)): through the contractor's claims adjustment, credit balance, self-reported refund or other process; a report based on sampling must describe the statistically valid sampling and extrapolation methodology. An SDP or SRDP disclosure that ends in settlement satisfies reporting.

## 3. Clock table: one trigger per timed element

| Element | Trigger event | Period | Source |
|---|---|---|---|
| Report and return (Parts A and B) | Identification of the initial overpayment | 60 days | 401.305(b)(1)(i) |
| Corresponding cost report | Due date of a cost report that corresponds to this overpayment, if any | Replaces the 60-day date if later | 401.305(b)(1)(ii) |
| Investigation suspension start | Start of a timely, good-faith investigation of related overpayments | Runs until the earlier end event | 401.305(b)(3)(i) |
| Investigation suspension end | Investigation concluded and aggregate calculated, or day 180 after initial identification | Then the unused days of the 60 | 401.305(b)(3)(ii); 89 FR 98338 |
| Protocol suspension | OIG or CMS acknowledgment of receipt of a timely submission | Until settlement, withdrawal or removal | 401.305(b)(2); OIG SDP 2026, section 1 |
| MA applicable reconciliation | Final risk adjustment data submission deadline for the payment year, announced by CMS (422.310(g)) | Before it, unsupported codes are corrected through data submission; after it, an overpayment exists | 422.326(a) |
| MA report and return | Identification by the MA organization | 60 days, no investigation suspension | 422.326(d) |
| MA RADV direction | A CMS direction for purposes of 422.311 | Follows the direction instead of the 60 days | 422.326(d) |
| MA lookback | End of each payment year | 6 most recent completed payment years | 422.326(f) |
| Lookback (Parts A and B) | Date the overpayment was received | Identified within 6 years | 401.305(f) |
| SDP internal investigation | Date of the initial SDP submission | 90 days to complete and report | OIG SDP 2026, section 3.A |
| SDP kickback arrangement end | Date of SDP submission | Terminated within 90 days | OIG SDP 2026, section 2.E |
| FCA limitations | Violation; or official's knowledge | 6 years; 3 years (10-year outer limit) | 31 U.S.C. 3731(b) |
| Retaliation claim | Date of the retaliation | 3 years | 31 U.S.C. 3730(h)(3) |

Show every date with its weekday and state "no roll": neither 401.305 nor 422.326 has a weekend or holiday rule, so do not add one. Where identification is before an MA payment year's applicable reconciliation, whether the 60 days run from identification or from reconciliation is `[VERIFY]`; show both.

## 4. Lookback and reopening

- Report and return any overpayment identified within 6 years of the date it was received (401.305(f)). Do not shorten the review to a contractor reopening period: contractor reopening on its own motion is 1 year for any reason, 4 years for good cause, any time for fraud or similar fault (42 C.F.R. 405.980(b)), and a party may ask a contractor to reopen to report and return an overpayment under 401.305 (405.980(c)(4)).
- Measure the lookback from the payment date, not the date of service.

## 5. Quantification: full review or statistically valid sample

- Either review every affected claim, or use a statistically valid random sample projected to a defined population (OIG SDP 2026, section 3.B; 401.305(d)(1)).
- A probe, judgmental, highest-dollar, convenience or "worst cases" sample cannot be extrapolated. Its confirmed errors are known overpayments; report those and design a valid sample for the rest.
- OIG SDP requirements for a sample: at least 100 items; random selection with the source of random numbers shown (RAT-STATS recommended); simple random sampling unless stratified or multistage design is justified; variables sampling with the difference estimator; mean point estimate (no minimum precision); missing items treated as errors; no netting of underpayments; full written sampling plan (objective, population, frame, sampling unit, data sources, review criteria). A probe sample may be folded into the 100 only "if statistically appropriate."
- Medicare contractors extrapolating against a provider generally demand the lower limit of a one-sided 90 percent confidence interval (Program Integrity Manual, ch. 8, 8.4.5); that convention is not the SDP's. State which convention the chosen path uses.
- Population: every claim with the error characteristic in the lookback, all billing NPIs and TINs of the entity that received payment, every federal program affected, each listed separately.

## 6. Disclosure paths

Use the disclosure path labels of stark-law-aks-compliance exactly: Disclosure path: none indicated; Disclosure path: CMS SRDP; Disclosure path: OIG SDP; Disclosure path: contractor refund; Disclosure path: counsel decision required.

| Conduct | Path | Source |
|---|---|---|
| Overpayment or error only, no potential violation of a federal law with CMP authority | Contractor refund (MAC voluntary refund, claim adjustment, credit balance) | 401.305(d)(1); OIG SDP 2026, section 2.C |
| Potential fraud with CMP authority (false billing, excluded persons) | OIG SDP; the submission must acknowledge a potential violation and name the laws | OIG SDP 2026, sections 2.B, 3 |
| Potential AKS violation, alone or with Stark | OIG SDP | OIG SDP 2026, sections 2.C, 7 |
| Stark only, no potential AKS liability for the same arrangement | CMS SRDP, current OMB-approved CMS-10328 forms | OIG SDP 2026, section 7; CMS SRDP page |
| Federal crime | DOJ, not the SDP | OIG SDP 2026, section 2.C |
| Never | Both SDP and SRDP for the same arrangement | OIG SDP 2026, section 7 |

The Stark and AKS characterization that decides the path is counsel's. When counsel has not analyzed the conduct, the label is "Disclosure path: counsel decision required." The SDP is not a way to ask OIG for an opinion.

## 7. Settlement modeling

| Path | Model | Source |
|---|---|---|
| OIG SDP, false billing | Minimum multiplier 1.5 times single damages, applied to the amount paid, not claimed; minimum settlement $20,000 | OIG SDP 2026, section 8 |
| OIG SDP, kickback-related | Generally a multiplier of the remuneration conferred on the referral source; total remuneration disclosed regardless of any lawful purpose; claims-based estimate also required; minimum settlement $100,000 | OIG SDP 2026, sections 3.D, 8 |
| CMS SRDP | CMS may reduce amounts owed (ACA 6409); no fixed multiplier stated in the sources read `[VERIFY]` | CMS SRDP page |
| Contractor refund | Single overpayment amount | 401.305(d)(1) |
| Litigated or government-initiated FCA | Treble damages plus per-claim penalties; reduction to double only under 3729(a)(2) | 31 U.S.C. 3729(a) |

- The SDP credits refunds made before resolution but is not bound by them and may require the review to be redone (section 10). SDP disclosers waive limitations defenses for the CMP 6-year period (section 2.D).
- Present each path as a range with its assumptions. A settlement figure is a model for counsel, never a predicted outcome.

## 8. Positions this skill will not take

- That identification waits for quantification, board approval, a consultant's final report, or the end of an investigation that has not been shown to be timely and in good faith.
- That a review can be stopped, narrowed, left unwritten or kept "under review" so that the entity never knowingly retains an overpayment.
- That one cause can be split into separate investigations to restart the 180 days, or that the 180 days apply where the regulation does not provide them.
- That a year inside the 6-year lookback can be dropped because the contractor can no longer reopen it.
