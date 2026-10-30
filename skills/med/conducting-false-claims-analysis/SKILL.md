---
name: conducting-false-claims-analysis
language: en
description: >
  Evaluates provider-side False Claims Act (31 U.S.C. 3729-3733) and Medicare and Medicaid
  overpayment exposure. Tests falsity, scienter, Escobar materiality and causation; computes
  the 60-day deadline under 42 C.F.R. 401.305 (180-day suspension, 6-year lookback);
  quantifies from claims or a valid sample; models treble damages, penalties, OIG SDP, CMS
  SRDP and refunds. Covers FCA exposure, qui tam risk, overpayment
  quantification and settlement modeling once stark-law-aks-compliance finds noncompliance
  (1320a-7b(g) causation, Stark-tainted DHS claims); exposure and overpayment quantification
  for arrangements escalated by conducting-stark-law-analysis; MA risk-adjustment overpayments
  under 422.326; one-sided or add-only chart reviews, raise-only CDI query policies and
  capture-count incentives; altered or backdated records in appeals and overpayments found
  during appeal review; subpoena, CID or unsealed qui tam response; 3730(h) retaliation.
  Counsel's Stark and AKS opinion stays in stark-law-aks-compliance.
tags:
  - process
  - healthcare-compliance
  - compliance
  - risk
metadata:
  author: casemark
  practice_areas:
    - Healthcare Compliance
    - HIPAA
    - Healthcare Regulation
  document_types:
    - Process Documentation
  skill_modes:
    - Process Management
---

# Conducting False Claims Analysis

Prepares a provider-side False Claims Act and overpayment analysis for one issue or one set of related issues: an issue matrix, a four-element liability analysis, the 60-day report-and-return clock with each trigger shown, an overpayment quantification, an exposure and settlement model by disclosure path, qui tam and retaliation risk, and hand-offs, in the format of `references/output-template.md`. Its aim is to find, quantify and return what is owed on time and to size exposure accurately so counsel can choose a lawful resolution. Every output is a draft for review by the compliance officer and health care counsel; it is not legal advice, a disclosure or a refund.

## Why This Skill Exists

The FCA remains the government's main civil health care fraud tool: in fiscal year 2025, DOJ reported more than $6.8 billion in FCA settlements and judgments, over $5.7 billion of it from health care matters, and a record 1,297 qui tam suits. For a provider, most exposure now arrives through a door it controls: an overpayment that was an honest error when billed becomes an FCA "obligation" once the report-and-return deadline passes. Since January 1, 2025 that deadline runs from the date the provider knowingly receives or retains the overpayment, not from the date it finishes counting, with a suspension of up to 180 days only for a timely, good-faith investigation of related claims. Analyses go wrong on dates, on the damages base, on stale penalty tables, on samples that cannot be extrapolated, and on treating a regulation's text as proof that a violation mattered to the payer. This skill keeps each of those separate and sourced.

## Where Mistakes Hide

| Input / Document | What It Is Used For | Where the Error Hides |
|---|---|---|
| Audit report, hotline log, email chain showing who learned what and when | Identification date and the start of the 60-day clock | Clock started at quantification, board approval or the consultant's final report instead of the date the entity knowingly received or retained the overpayment; the 180-day suspension claimed for an investigation never begun or not pursued in good faith; suspension counted from the investigation start instead of day 180 after initial identification; the full 60 days restored after the suspension instead of only the unused days |
| Sample workpapers and extrapolation | Overpayment amount to report, refund or disclose | A probe, judgmental or highest-dollar sample extrapolated to the universe; fewer than 100 items or a lower-bound estimate for an OIG SDP submission; underpayments netted; missing items not counted as errors; frame narrower than the population; no methodology description for a contractor report (401.305(d)(1)) |
| Claims extract and remittance data for the review period | Lookback window and the claims population | Review cut to the 1-year or 4-year contractor reopening period instead of the 6-year lookback from receipt (401.305(f)); lookback measured from date of service; FCA limitations (3731(b): 6 years, or 3 years from the official's knowledge up to 10) confused with the overpayment lookback |
| Paid amounts, billed charges, refunds already made | Single damages and the treble base | Treble applied to billed charges or beneficiary cost-sharing instead of program payments; full payment trebled where the theory supports only a differential, or the reverse; prior refunds netted before multiplying with no order stated |
| Penalty table in a prior memo or template | Per-claim civil penalty range | 2024 amounts ($13,946-$27,894) used for a penalty assessed today; the 2026 "adjustment" assumed although DOJ made none, so the after-July 3, 2025 amounts ($14,308-$28,619) still apply |
| Regulation, LCD, manual or condition of participation cited as the requirement | Materiality | Materiality concluded from the words "condition of payment" alone; the MAC's or CMS's payment with actual knowledge of the same violation ignored (Escobar) |
| Emails and policies on how the billing rule was read | Scienter | An objectively reasonable reading adopted after the fact treated as a defense, when SuperValu looks at what the entity actually believed when it billed |
| Counsel's Stark and AKS conclusions and arrangement facts | Claim set and causation for arrangement-based exposure | AKS-tainted claims counted without the forum's 1320a-7b(g) causation standard (but-for in the First, Sixth and Eighth Circuits; a link in the Third); Stark-tainted DHS claims limited to a causal subset; Stark-only conduct sent to the OIG SDP, or AKS conduct to the CMS SRDP or a MAC refund |
| Entity, program and payer identifiers (NPI, TIN, MA or Medicaid plan) | Who owes, under which rule, to whom | 401.305 and its 180-day suspension applied to an MA organization (422.326 has none) or to Medicaid; affiliated billing NPIs left out of the population; the parent named as the "person" instead of the entity paid |
| HR file, hotline report, restructuring list | Retaliation exposure (3730(h)) | Adverse action against an internal reporter during the review; relator identity pursued; reporter protection limited to employees though contractors and agents are covered |
| News of Zafirov and similar challenges | Qui tam risk weighting | Relator suits discounted as unconstitutional although the Eleventh Circuit vacated that ruling on September 1, 2026 and every circuit to decide has upheld the Appointments Clause question |

## Ground Rules

1. **Draft only.** Nothing is filed, refunded, disclosed or sent to a government agency or contractor by this skill. Every output is labeled a draft for the compliance officer and counsel.
2. **Source-review gate.** Do not call a claim, date or document missing until every supplied file has been opened and searched, with OCR or extraction tried. Classify each gap as an *unknown fact* (when the compliance officer read the audit), a *source conflict* (remittance and dashboard paid amounts differ), an *unverified external lookup* (a state Medicaid rule not in `references/primary-sources.md`) or a *policy election* (which disclosure path to use).
3. **Hierarchy of authority.** Law: statute, current regulation, preamble, agency protocols, the governing circuit's decisions, other decisions, commentary. Facts: remittance and claims data, then the medical record and audit worksheets, then audit reports, then dashboards, emails and summaries. Counsel's Stark and AKS labels govern the legal characterization of an arrangement. Name every conflict in the reconciliation table and state which source controls; never resolve one silently.
4. **Citation discipline.** Every date, claim count and dollar figure carries a source locator or `[UNVERIFIED]`; every legal statement carries a citation from `references/primary-sources.md` or `[VERIFY]`. A circuit's rule is named only if it is in the register; otherwise model both readings.
5. **Identification follows the facts.** Decline to structure, date, word, split or limit findings so as to delay or avoid the 60-day obligation or to keep the entity from "knowing": no stopping or narrowing a review to avoid knowledge, no later identification date than the record shows, no indefinite "under review" status for confirmed errors, no splitting one cause to restart the 180 days, no dropping years inside the lookback. Produce the accurate clock instead.
6. **Every clock has its own trigger.** Fill the clock table in `references/overpayment-clock-and-disclosure.md`, section 3, with the trigger event and date for each element, weekday included, and list each rejected candidate date with the reason.
7. **Four elements, four labels.** Falsity, scienter, materiality and causation each get Supported, Contested, Not supported or Undetermined, with evidence. An error without scienter is an overpayment, not FCA liability, until the deadline passes.
8. **Penalties by assessment date; damages on paid amounts.** Use the 28 C.F.R. 85.5 column for a penalty assessed now and state the column. The damages base is what the program paid, matched to the liability theory.
9. **No extrapolation without a valid design.** A figure projected from a non-random or undocumented sample is labeled "estimate not reportable: invalid sample"; confirmed errors are reported as the known-claim amount.
10. **Route follows conduct and counsel.** Use the disclosure path labels exactly. Stark only goes to the CMS SRDP; AKS alone or with Stark to the OIG SDP; error-only overpayments to contractor refund; never both protocols for one arrangement. Where counsel has not characterized the conduct, the label is "Disclosure path: counsel decision required."
11. **Protect reporters.** Decline to identify a suspected relator or reporter, or to plan or justify adverse action because of a report. Flag every pending adverse action against a reporter for employment counsel.

## Checkpoint A: Pre-Draft Intake (Mandatory)

Collect, from documents where possible:

1. Today's date, the requester and role, and whether the work is at counsel's direction.
2. The entity that received payment: legal name, billing NPIs and TINs, and any affiliates in the claims data.
3. Programs and payers: Medicare Parts A and B, MA plan or MA organization, Part D, Medicaid (state; fee-for-service or managed care), TRICARE, other.
4. The issue and its trigger: internal audit, hotline report, contractor or OIG audit, counsel's Stark or AKS finding, an arrangement escalated by conducting-stark-law-analysis, MA risk-adjustment overpayments under 42 C.F.R. 422.326 (one-sided or add-only chart reviews, capture-count incentives), raise-only CDI query policies, altered or backdated records or overpayments found during appeal review (managing-coding-denials), subpoena, CID, unsealed qui tam.
5. Claims data: claim count, payment dates, paid amounts, billed charges, refunds already made, and cost report due dates if any.
6. The knowledge timeline: when each person learned of the issue, what they received, and when any investigation of related claims began and ended.
7. Sample documentation: objective, population, frame, selection method and random-number source, size, review criteria and results.
8. For arrangement-based issues, the stark-law-aks-compliance hand-off (its Stark, AKS and disclosure path labels, the noncompliant periods, the affected DHS claims or the data needed to identify them, and the federal circuit) or the conducting-stark-law-analysis escalation (the arrangement's operational facts and periods). For coding-driven issues, the sibling's record-level findings, without its conclusions on knowledge or damages.
9. Evidence bearing on scienter and materiality: emails, policies, education letters, prior denials, payer audits and what the payer did afterwards.
10. Reporter facts: hotline reports, who raised the issue, and any pending employment action.

**Defaults if not supplied** (a statute or regulation overrides any default it addresses): program is Medicare Parts A and B, marked `[UNVERIFIED]`; no cost report applies unless the entity files one; the governing circuit is the one where the entity is located; the penalty column is the one for penalties assessed after July 3, 2025, since DOJ made no 2026 adjustment; disclosure path "counsel decision required" until counsel characterizes the conduct.

**Hard stops (a partial decline: label only the affected request with the fixed line from `references/output-template.md`, section 1, "Declined: hard stop (<stop name>)", produce what the stop calls for instead, and continue the rest of the analysis):**
- **Identification structuring**: a request to structure, date, word or limit findings so as to delay or avoid the 60-day obligation, or to minimize or postpone identification (Ground Rule 5): decline that part; produce the accurate clock and the lawful options.
- **Reporter protection**: a request to identify, unmask or take adverse action against a suspected relator or internal reporter, or to frame discipline around a report: decline that part; flag 3730(h) and route to employment counsel.
- **No claims data**: no claims data at all (no claim count, payment dates or paid amounts): produce the data request; no exposure figure. A stark-law-aks-compliance hand-off that lists only the data needed is accepted on this basis: build the data request and the clock analysis from it.
- **Invalid extrapolation**: a request to present an extrapolated figure as the reportable, refundable or disclosable amount when the sample is not a documented random selection from a defined frame: produce the known-claim amount and a sampling plan request instead of the extrapolated figure.

**Not hard stops:** an unknown identification date (show each candidate date and the deadline it produces); an unknown circuit rule (`[VERIFY]` and both readings); no counsel analysis of an arrangement (label the path "counsel decision required" and continue); a pending sealed qui tam rumor (note it; do not investigate the relator).

## Step 1: Frame the Issue, Entity and Program

Read `references/overpayment-clock-and-disclosure.md`, section 1. Record the header and source register from `references/output-template.md`. Name the entity paid, each program and the rule that governs it (401.305, 422.326, statute only for Medicaid). Build the issue matrix, one row per issue and program.

## Step 2: Fix the Knowledge Timeline and the Clock

Read `references/overpayment-clock-and-disclosure.md`, sections 2 and 3. From the record, find the date the entity knowingly received or retained the first overpayment. Test whether an investigation of related overpayments began, when, and whether it was timely and in good faith. Compute the suspension end as the earlier of completion or day 180 after initial identification, then add only the unused days of the 60. Compare with any cost report due date. Assign the clock label and list rejected candidate dates.

## Step 3: Set the Lookback and the Population

Read `references/overpayment-clock-and-disclosure.md`, section 4. Set the 6-year lookback from payment dates. Define the population across every billing NPI, TIN and program. Note the separate FCA limitations dates from `references/fca-liability-and-damages.md`, section 6.

## Step 4: Quantify

Read `references/overpayment-clock-and-disclosure.md`, section 5. Use a full review where feasible. For a sample, check each design element against the path's convention. Report the known-claim amount separately from any estimate; label an estimate from an invalid design "estimate not reportable: invalid sample" and draft the sampling plan request for managing-compliance-audits.

## Step 5: Test the Four Elements

Read `references/fca-liability-and-damages.md`, sections 1 to 5. For each issue, label falsity, scienter (what the entity actually believed when it billed), materiality (the requirement's text, what the payer knew, and what the payer did after knowing; payment with actual knowledge makes the label Contested at most) and causation. For arrangement-based issues, take counsel's labels as given, size the claim set under Stark and under the forum's 1320a-7b(g) standard, and send any disagreement back to stark-law-aks-compliance.

## Step 6: Model Exposure and Settlement

Read `references/fca-liability-and-damages.md`, sections 7 and 8, and `references/overpayment-clock-and-disclosure.md`, sections 6 and 7. Build the exposure table on paid amounts: contractor refund, OIG SDP or CMS SRDP as applicable, and litigated FCA with treble damages and the current penalty range. Show credits on their own line and state the order used. Assign the disclosure path label from the conduct and counsel's characterization.

## Step 7: Assess Qui Tam and Retaliation Risk

Read `references/fca-liability-and-damages.md`, sections 9 and 10. Record who knows the facts, internal reports and responses, public disclosures, any subpoena, CID or unsealed complaint, and every pending adverse action against a reporter. State the Zafirov status as of the review date.

## Step 8: Reconcile, Hand Off and List Open Items

Complete the reconciliation table, hand-offs and open items in `references/output-template.md`, sections 8 to 10. Check each rule relied on against `references/primary-sources.md` and carry its `[VERIFY]` flag into the output.

## Checkpoint B: Post-Draft Alignment

1. Does the draft answer the question asked, for the entity and programs actually paid?
2. Is the identification date taken from the record, with every rejected candidate listed, and does the deadline use only the unused days after any suspension?
3. Does any estimate rest on a valid design, and is the known-claim amount stated separately?
4. Is every disclosure path label consistent with counsel's Stark and AKS labels, and are disagreements routed back to counsel?
5. Has any requested wording, date or scope change been checked against Ground Rule 5 and declined where it would delay or avoid the obligation?
6. Are open items owned, with the next action and whether they change a deadline?

## Quality Audit

1. The header names the entity paid (NPIs, TINs), each program, the rule governing each, and the trigger.
2. Every supplied file appears in the source register with a status; nothing is called missing without a search.
3. The identification date is sourced to the record, and rejected candidate dates are listed with reasons.
4. The clock table gives each element its own trigger and date with weekday, and the suspension ends at the earlier of completion or day 180 after initial identification, with only the unused days added.
5. The lookback is 6 years from receipt (or the rule for that program), not a reopening period.
6. Any sample is checked element by element against the path's convention, and no invalid estimate is reported.
7. Falsity, scienter, materiality and causation each carry a label and evidence; materiality states what the payer knew and did.
8. Scienter rests on what the entity believed when it billed, not on a later reasonable reading.
9. The damages base is program payments matched to the theory, never billed charges, and credits are shown separately.
10. The per-claim penalty range uses $14,308-$28,619 for penalties assessed after July 3, 2025, with the 2026 no-adjustment notice cited.
11. The disclosure path label follows the conduct and counsel's characterization, and no arrangement goes to both protocols.
12. No output delays or avoids identification, and no output targets a reporter.
13. Every `[VERIFY]` relied on appears in the open items with what would settle it, and the draft closes with the review line.

## Guidelines

- Write as if the government, a relator and a court will read the draft. Adverse dates and emails belong in it.
- Be exact about what is known and what is estimated. A known overpayment can be returned on time while the estimate for related claims is still being built.
- Keep prospective fixes (edits, education, policy) separate from look-back obligations (report, return, disclose).
- A settlement range is a model for counsel's decision, never a prediction or a negotiating position.
- When an instruction conflicts with a rule (report later, narrow the review, use the SRDP for AKS conduct), draft the compliant version and explain the change.
- Limit protected health information to what the analysis needs; use claim numbers rather than patient names.

## Troubleshooting

| Problem | Likely cause | What to do |
|---|---|---|
| Two plausible identification dates | Audit report dated before the compliance officer received it, or an email suggests earlier awareness | Compute the deadline from each, show both, flag the earlier as controlling until counsel decides |
| Claims extract and remittance disagree on paid amounts | Adjustments, recoupments or crossover payments | Use remittance; add a reconciliation row; recompute the base |
| Sample workpaper lacks the random-number source or frame | Undocumented or judgmental selection | Treat confirmed errors as known overpayments; label any projection not reportable; request the plan |
| Scanned audit report or medical records unreadable | Image-only files | Attempt OCR; list unreadable pages and the claims whose status depends on them as Undetermined |
| Counsel's labels conflict with the facts supplied here | Different periods or arrangement terms | Record both in the reconciliation table; return the conflict to stark-law-aks-compliance |
| Program unknown for some claims | Payer field missing or MA plan claims mixed with Medicare fee-for-service | Split by payer ID; apply each program's rule; mark unknowns `[UNVERIFIED]` |
| Subpoena, CID or unsealed complaint arrives mid-review | Government or relator action | Note it, preserve documents, keep the clock running, and route response strategy to litigation counsel |

## Related Skills

- stark-law-aks-compliance: counsel's legal analysis and opinion on Stark and AKS compliance, the forum's 1320a-7b(g) reading, and the final disclosure path; this skill sizes the FCA exposure that follows.
- conducting-stark-law-analysis: the operational facts of an escalated arrangement (terms as written and as paid, periods, exception elements) when exposure sizing needs them; it escalates to this skill for exposure and overpayment quantification.
- conducting-anti-kickback-analysis: provider-side safe harbor documentation for a payment arrangement.
- managing-compliance-audits: designing the audit sample and corrective action plan when a valid sample is needed.
- auditing-coding-accuracy: claim-level coding review of the sampled or affected claims.
- managing-risk-adjustment-coding: MA diagnosis support and RADV issues behind an MA risk-adjustment overpayment under 422.326, including two-way review of one-sided or add-only chart reviews.
- managing-drg-optimization: inpatient DRG documentation support when unsupported codes or one-way (raise-only) query policies drive the overpayment.
- managing-coding-denials: the appeal itself; it routes altered or backdated records and overpayments found during appeal review here.
- managing-compliance-programs: program-wide remediation after the finding.
- whistleblower-protection-policy: drafting an anti-retaliation policy after a reporter issue surfaces.
- legal-research: 3730(h) case law, circuit rules marked `[VERIFY]`, and state Medicaid overpayment rules; no dedicated skill exists.

## Reference Files

- `references/fca-liability-and-damages.md`: liability theories, the four elements, SuperValu scienter, Escobar materiality, AKS and Stark causation, limitations, damages base, penalty table by assessment date, qui tam and Zafirov, retaliation.
- `references/overpayment-clock-and-disclosure.md`: which rule applies to whom, identification and suspension, the clock table, lookback and reopening, sampling rules, disclosure paths, settlement models, positions declined.
- `references/output-template.md`: deliverable sections, labels, issue matrix, element and clock tables, exposure model, reconciliation table, hand-off table.
- `references/primary-sources.md`: each authority checked with URL, method, what it supports and the date, corrections to the earlier version, and the `[VERIFY]` list.
