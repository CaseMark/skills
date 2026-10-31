# FCA Liability, Damages and Qui Tam Rules

Working rules for the civil False Claims Act (31 U.S.C. 3729-3733) as applied to claims paid by Medicare, Medicaid and other federal health care programs. Read in full text on 2026-10-30 unless marked `[VERIFY]`. Statute and case citations are in `references/primary-sources.md`.

## Contents

1. Liability theories
2. The four elements, tested separately
3. Scienter after SuperValu
4. Materiality after Escobar
5. Causation for AKS-tainted and Stark-tainted claims
6. Statute of limitations
7. Damages base and multiplier
8. Civil penalties by assessment date
9. Qui tam mechanics and the Zafirov challenge
10. Retaliation (3730(h))
11. Record alteration and selective-review scienter

## 1. Liability theories

| Theory | Provision | Health care pattern |
|---|---|---|
| Presentment | 3729(a)(1)(A): knowingly presents or causes to be presented a false or fraudulent claim | Services not rendered, unsupported codes, medically unnecessary services, services by excluded persons |
| False record | 3729(a)(1)(B): false record or statement material to a false claim | Altered documentation, false certifications, false attestations supporting claims |
| Conspiracy | 3729(a)(1)(C) | Agreement to commit (A), (B) or (G) |
| Reverse false claim | 3729(a)(1)(G): knowingly conceals or knowingly and improperly avoids or decreases an obligation to pay | Identified overpayment kept past the 1320a-7k(d) deadline; "obligation" includes "the retention of any overpayment" (3729(b)(3)) |
| Implied false certification | Escobar | Claim makes specific representations about the service and omits a violation that makes them misleading |
| AKS per se falsity | 42 U.S.C. 1320a-7b(g) | Claim includes items or services "resulting from" an AKS violation |

The reverse false claim theory is the one this skill sees most: an overpayment that was not false when billed becomes an FCA obligation once the report-and-return deadline passes (1320a-7k(d)(3); 42 C.F.R. 401.305(e)).

## 2. The four elements, tested separately

Give each element its own label: Supported, Contested, Not supported, or Undetermined, with the evidence for and against.

- **Falsity**: what representation the claim made and why it was untrue (express, implied certification, or per se under 1320a-7b(g)).
- **Scienter**: "knowingly" means actual knowledge, deliberate ignorance or reckless disregard, with no proof of specific intent to defraud (3729(b)(1)).
- **Materiality**: "a natural tendency to influence, or be capable of influencing, the payment or receipt of money" (3729(b)(4)), applied under Escobar (section 4).
- **Causation and damages**: which claims, and how much the government paid because of the false statement (sections 5 and 7).

An error with no scienter is an overpayment, not FCA liability, until the 60-day deadline passes.

## 3. Scienter after SuperValu

- The test is subjective: what the defendant actually knew and believed when it submitted the claim, not what an objectively reasonable person could have believed (Schutte v. SuperValu, 2023).
- A legally plausible reading of an ambiguous rule, adopted after the fact, is not a defense if the entity believed its claims were inaccurate when it submitted them. "Post hoc interpretations" do not control; the focus is "what the defendant knew when presenting the claim."
- Deliberate ignorance: aware of a substantial risk of falsity and intentionally avoiding steps to confirm. Reckless disregard: conscious of a substantial and unjustifiable risk and submitting anyway. Both are defined by the defendant's own awareness.
- Evidence to collect: emails, audit reports and who received them, hotline logs, contractor education letters, prior denials, coding guidance requested and not followed, decisions to stop or narrow a review.
- Corporate knowledge: whose knowledge is attributed to the entity is circuit-variable `[VERIFY]`; list each person who knew and when.

## 4. Materiality after Escobar

Materiality is "demanding." The FCA is not a vehicle for "garden-variety breaches of contract or regulatory violations."

- A requirement labeled a condition of payment is relevant but "not automatically dispositive."
- The government's option to refuse payment if it had known is not sufficient.
- Noncompliance that is "minor or insubstantial" is not material.
- If the government paid a particular claim in full with actual knowledge of the violation, that is "very strong evidence" the requirement is not material; if it regularly pays that type of claim with actual knowledge and has signaled no change, that is "strong evidence" it is not material.
- Evidence of materiality: the requirement goes to the essence of the bargain; the government consistently refuses payment, recoups, or excludes when it learns of this violation.

Record for every requirement relied on: the text and whether it is labeled a condition of payment; what the payer (CMS, the MAC, a state agency) knew and when; what it did after it knew (denied, recouped, educated only, kept paying); and the label. Never mark materiality Supported from the regulation's text alone.

Label rule: Supported needs evidence beyond the text, such as consistent refusal or recoupment once the payer learns of the violation. Where the payer paid with actual knowledge of the same violation, the label is Contested, and the weighing is left to counsel; this skill does not mark materiality Not supported on payer behavior alone, because Escobar treats materiality as a holistic judgment.

## 5. Causation for AKS-tainted and Stark-tainted claims

- **AKS (1320a-7b(g))**: "resulting from" is circuit-variable. But-for causation: First Circuit (Regeneron, 2025), Sixth Circuit (Martin v. Hathaway, 2023), Eighth Circuit (Cairns, 2022). Third Circuit: a "link" between the kickback and at least one claim, less than but-for; temporal proximity alone is not enough (Greenfield, 2018). Other circuits: `[VERIFY]`; model both readings.
- **Stark**: payment for DHS furnished on a prohibited referral is barred without intent (42 U.S.C. 1395nn(g)(1)); the claim set is every Medicare DHS claim on the physician's referrals during the noncompliant period. FCA liability still needs scienter and materiality.
- Forum: an FCA action may be brought in any district where any defendant "can be found, resides, transacts business," or where any proscribed act occurred (31 U.S.C. 3732(a)). The circuit where the entity sits is a default, not a certainty; where venue could lie elsewhere, model each plausible circuit's causation rule.
- The Stark/AKS legal conclusions come from counsel (stark-law-aks-compliance). This skill takes the labels as given, sizes the claim set under each reading, and returns any disagreement to counsel.

## 6. Statute of limitations (31 U.S.C. 3731(b))

| Limit | Trigger event | Note |
|---|---|---|
| 6 years | Date the violation is committed | Presentment: claim submission. Reverse false claim on a retained overpayment: when the violation is committed is for counsel; a reading that it occurs at the 1320a-7k(d) deadline is `[VERIFY]` |
| 3 years | Date material facts are known or reasonably should have been known by the responsible U.S. official | Whichever of the 6-year and 3-year periods ends last; also available in relator suits the government declined (Cochise, 2019) |
| 10 years | Date the violation is committed | Outer limit on the 3-year rule |
| Relation back | Government complaint in intervention relates back to the relator's filing date (3731(c)) | |

The 6-year overpayment lookback (section 2 of the overpayment reference) and the FCA limitations period are different rules with different triggers; compute both.

## 7. Damages base and multiplier

- Treble damages: 3 times "the amount of damages which the Government sustains" (3729(a)(1)). Reduced to not less than double for a qualifying self-report within 30 days, with full cooperation and no pending action or known investigation (3729(a)(2)).
- The base is what the program paid, never billed charges. Exclude beneficiary deductibles and coinsurance unless a program paid them.
- Match the base to the theory: services not rendered or worthless, or claims per se false under 1320a-7b(g) or Stark, use the program payment for the affected claims; an upcoded claim uses the difference between what was paid and what the supported code would have paid `[VERIFY]` (courts measure damages differently by theory and circuit; show the measure chosen and the alternative).
- Credits: Bornstein (1976) held that the Government's actual damages are multiplied before any subtraction for compensatory payments; it construed the earlier double-damages provision, and its application to the current treble provision in the governing circuit is `[VERIFY]`. Show refunds as a separate line and state the order used.
- Medicaid: the federal share and the state share may be pursued under different statutes `[VERIFY]` by state.

## 8. Civil penalties by assessment date (28 C.F.R. 85.5)

Penalties are per false claim, set by the date the penalty is assessed, for violations after November 2, 2015.

| Penalty assessed | Minimum | Maximum | Source |
|---|---|---|---|
| After Feb. 12, 2024 through July 3, 2025 | $13,946 | $27,894 | 28 C.F.R. 85.5, table 1, fourth column |
| After July 3, 2025 | $14,308 | $28,619 | 28 C.F.R. 85.5, table 1, fifth column (90 FR 29445, July 3, 2025) |
| Calendar year 2026 | No change: DOJ made no 2026 adjustment because October 2025 CPI-U data were not produced; it continues the 2025 levels | | 91 FR 43405 (July 15, 2026); OMB M-26-11 |

- Violations on or before November 2, 2015: $5,500 to $11,000 (28 C.F.R. 85.3(a)(9)); by 2026 most are past the 10-year outer limit.
- Show the penalty range as count of claims times minimum and maximum. Never use an older column for a penalty that would be assessed today. Re-check 85.5 for a 2027 adjustment before relying on these figures after January 2027.

## 9. Qui tam mechanics and the Zafirov challenge

- Relator files under seal for at least 60 days; the government may seek extensions (3730(b)(2)-(3)). Relator share: 15 to 25 percent if the government intervenes, 25 to 30 percent if it declines (3730(d)). Only the government may intervene in or bring a related action while one is pending (3730(b)(5)).
- Public disclosure bar and original source: 3730(e)(4).
- Zafirov: the Middle District of Florida held the qui tam provisions violate the Appointments Clause (751 F. Supp. 3d 1293 (M.D. Fla. 2024)). The Eleventh Circuit vacated on September 1, 2026 (No. 24-13581), holding relators are not officers of the United States and joining the Fifth, Sixth, Ninth and Tenth Circuits; it remanded the Take Care and Vesting Clause arguments. Mandate issued September 30, 2026. On remand, the district court set a hearing for November 23, 2026. Whether a certiorari petition is filed is `[VERIFY]`. Treat qui tam suits as viable in every circuit; the remaining arguments are a defense for litigation counsel, not a reason to discount relator risk.

## 10. Retaliation (31 U.S.C. 3730(h))

- Protects employees, contractors and agents from discharge, demotion, suspension, threats, harassment or other discrimination because of lawful acts in furtherance of an FCA action "or other efforts to stop 1 or more violations," which reaches internal reports.
- Relief: reinstatement, 2 times back pay, interest, special damages, litigation costs and attorneys' fees. Limitations: 3 years after the retaliation.
- During any review, flag every pending adverse action against a person who reported the issue, and route it to employment counsel before it is taken.

## 11. Record alteration and selective-review scienter

**Altered or backdated records.** A record created or changed after the claim, the denial or the audit request and presented as original (an addendum dated to the visit, a re-signed order, a merged note) is the classic false record of 3729(a)(1)(B): a false record or statement "material to a false or fraudulent claim." Submitted in an appeal, it is offered to obtain or keep payment, so its tendency to influence payment is direct. Submitted to avoid repaying, it can fall under 3729(a)(1)(G).

- Inventory every version: displayed date, creation and modification timestamps from the EHR audit log, author, signer, and where each version was sent (MAC, QIC, ALJ, auditor, payer).
- Label falsity and scienter for the record itself, separately from the underlying claim. A late entry disclosed as late, with its own date and author, is not a false record; one dated to look contemporaneous is.
- The claim behind the record has its own status: if the original record did not support it, it is an overpayment candidate with its own clock.
- Never repair, re-date, re-sign, replace or resubmit a record, and never advise withdrawing or "correcting" a submission without counsel; a second submission can be a second false record. Criminal exposure and contact with the adjudicator are for counsel.

**Selective-review scienter.** These designs do not make a claim false; each claim's falsity rests on its own record. They are evidence on scienter under 3729(b)(1) as SuperValu reads it, and they widen the population to review:

| Design | Why it bears on scienter | Population it widens |
|---|---|---|
| One-sided or add-only chart review (adds supported codes, never deletes unsupported ones) | Unsupported codes seen and left in place are knowingly retained; declining to look for deletions while looking for additions fits deliberate ignorance | Every member and payment year reviewed, both directions; for an MA organization, 422.326 applies to deletions it identifies |
| Raise-only (one-way) CDI query policy (queries only when a higher-weighted diagnosis could be added) | Shows awareness that documentation is incomplete, acted on only when payment rises | Claims whose CC, MCC or HCC rests on a query or post-discharge addendum |
| Capture-count incentives (pay per HCC closed, per gap captured, per query agreed) | Motive and pressure; also a possible AKS or Stark question if the payee is a referral source (route to counsel) | Codes captured under the incentive period |
| Stopping or narrowing a review after errors are found | Deliberate ignorance; the 2024 preamble starts the 60 days on the date the entity acted in deliberate ignorance or reckless disregard (89 FR 98336) | The period the review would have covered |

Record each design with its dates, its owner and its documents, and carry it into the scienter row of the element table.

