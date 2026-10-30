# SAR, CTR, Confidentiality and Sanctions Rules

## Contents

1. Clocks table, one trigger per element
2. SAR decision procedure design
3. Continuing activity
4. CTRs, aggregation, exemptions and structuring
5. SAR confidentiality and safe harbor
6. Requests the skill declines, and compliant alternatives
7. Record retention schedule
8. OFAC sanctions compliance as a separate regime

Citations are to 31 C.F.R. unless stated; each was read on 2026-10-30 (see `references/primary-sources.md`).

## 1. Clocks table, one trigger per element

Every timed element has its own trigger. Never carry one anchor across rows.

| Element | Trigger event | Period | Rule |
|---|---|---|---|
| SAR, bank, broker-dealer, mutual fund, insurer, FCM/IB, loan or finance company | Initial detection of facts that may constitute a basis for filing: the date a review determines, or the institution otherwise knows or has reason to suspect, that the activity meets a SAR definition | 30 calendar days | 1020.320(b)(3) and analogs; FFIEC manual (an alert or system flag is not initial detection) |
| Same, when no suspect is identified on the detection date | Same detection date | Up to 30 more days to identify a suspect; never more than 60 calendar days from detection | Same |
| SAR, MSB | Initial detection of facts | 30 calendar days; no extension | 1022.320(b)(3) |
| Immediate telephone notice to law enforcement | A violation requiring immediate attention (ongoing money laundering scheme; terrorist financing) | Immediately, in addition to the timely SAR | 1020.320(b)(3); 1022.320(b)(3); 1023.320(b)(3) |
| Continuing activity SAR (elective guidance) | Filing date of the previous related SAR | Review window 90 days after that filing; file by day 120 after the previous filing | Interagency SAR FAQs Q2-Q3 (Oct. 9, 2025): not required; an institution may instead file as appropriate within the regular timelines |
| Alert review | Alert generation | No regulatory period; complete in a reasonable time, set by policy and measured | FFIEC manual |
| CTR | Business day of the reportable transaction | File within 15 days following that day | 1010.306(a)(1) |
| CTR exemption designation (FinCEN Form 110 where required) | First reportable transaction to be exempted | Designate by the close of the 30-calendar-day period beginning after that day | 1020.315(c) |
| CTR exemption eligibility review | Prior review | At least once each year | 1020.315(d) |
| OFAC blocked property report | Date property becomes blocked | 10 business days | 31 C.F.R. 501.603(b)(1)(i) |
| OFAC annual blocked property report | Blocked property held as of June 30 | By September 30 | 501.603(b)(2) |
| OFAC rejected transaction report | Date of rejection | 10 business days | 501.604(c) |
| MSB program establishment | Date the business is established | Program within 90 days (or by July 24, 2002) | 1022.210(e) |

Clocks are calendar days except the OFAC clocks, which are business days. Show each computed date with its weekday. Where a SAR due date falls on a weekend or holiday, file earlier; a policy that relies on a roll-forward to the next business day is `[VERIFY]`.

Worked pattern for a policy example: determination that activity is suspicious on Monday, September 14, 2026, subject identified: due Wednesday, October 14, 2026. If no subject identified: up to Friday, November 13, 2026. A policy that starts the clock at case closure (say September 30) and adds 60 days produces Sunday, November 29, 2026, 76 days after detection, which is late.

## 2. SAR decision procedure design

- Dollar thresholds by type: $5,000 for banks, broker-dealers, mutual funds, insurers, FCMs/IBs, loan or finance companies and (from 2028) investment advisers; $2,000 for MSBs, with $5,000 for money order and traveler's check issuers reviewing clearance records. Voluntary SARs below thresholds are permitted.
- Definitions to quote in the policy: funds from illegal activity or disguising them; designed to evade BSA requirements, including structuring; no business or apparent lawful purpose after examining available facts; for MSBs, broker-dealers and others, use to facilitate criminal activity.
- Separate the steps and owners: alert generation, alert review (with a time standard), case investigation, SAR decision by a person or committee with authority, filing, board notification. The FFIEC manual expects dual control: those who prepare SARs generally should not also make the filing decision.
- Documentation of a decision not to file is not required (SAR FAQs Q4, Oct. 2025); an institution may require a short statement as a policy election.
- Near-threshold cash activity alone does not require a SAR absent knowledge, suspicion or reason to suspect evasion (SAR FAQs Q1). Monitoring parameters are risk-based. This is a reason to tune alerts, never a reason to exempt any customer class from SAR decisioning.
- When the subject is a director, officer or board member, the usual board notification step is bypassed and the deviation documented with uninvolved senior management (FFIEC manual).
- Supporting documentation is identified and kept as filed with the SAR (1020.320(d)).

## 3. Continuing activity

The October 9, 2025 interagency FAQs state that no separate post-SAR review of a customer or account is required; risk-based monitoring may be relied on. If the institution elects the guidance cadence, the timeline is: day 0 detection, day 30 initial SAR, day 120 end of the 90-day period, day 150 continuing SAR (with no suspect: day 60, 150, 180). Anchor each continuing filing to the prior SAR's filing date, not to detection. Example: initial SAR filed Tuesday, October 13, 2026; 90-day window October 14, 2026 to January 11, 2027; continuing SAR by Wednesday, February 10, 2027. A policy may keep a scheduled review as an election; it may not describe it as a regulatory requirement.

## 4. CTRs, aggregation, exemptions and structuring

- CTR for each deposit, withdrawal, exchange or other payment or transfer in currency of more than $10,000 (1010.311). Multiple currency transactions are one transaction when the institution knows they are by or on behalf of any person and total more than $10,000 cash in or cash out in one business day; all domestic branches count (1010.313). Night and weekend deposits count on the next business day.
- Monetary instruments: a bank check or draft, cashier's check, money order or traveler's check sold for currency of $3,000 to $10,000 inclusive requires the purchaser records in 1010.415; cash over $10,000 is a CTR transaction.
- Exemptions (1020.315) are for banks only, require FinCEN Form 110 designation where applicable and an annual eligibility review; there is no biennial renewal in the current text.
- Structuring: no person may structure, assist in structuring, or attempt either, to evade CTR requirements, or cause a failure to file or a false CTR (31 U.S.C. 5324(a); 1010.314). The definition covers any amount, one or more institutions, one or more days (1010.100(xx), quoted in SAR FAQ Q1). Staff who advise customers how to stay under the threshold are assisting structuring.

## 5. SAR confidentiality and safe harbor

- A SAR, and any information that would reveal its existence, is confidential (1020.320(e) and analogs). No current or former director, officer, employee, agent or contractor may notify any person involved in the transaction that it was reported (31 U.S.C. 5318(g)(2)(A)).
- Subpoena or request for a SAR: decline to produce it, cite 1020.320(e) and 31 U.S.C. 5318(g)(2)(A)(i), and notify FinCEN of the request and the response (1020.320(e)(1)(i)).
- Permitted: disclosure to FinCEN, law enforcement and the BSA examining regulators; sharing the underlying facts and documents (not the SAR) with another institution for a joint SAR; sharing within the corporate organizational structure as regulation or guidance permits; employment references under 31 U.S.C. 5318(g)(2)(B) without revealing that a SAR was filed.
- Safe harbor from liability to any person for the disclosure and for not notifying the subject (31 U.S.C. 5318(g)(3); 1020.320(f)). It does not protect against government enforcement.
- Account closure and exit letters state a business reason or none; they never reference a SAR, an investigation by the institution's BSA function, or "a report to the government" about the customer.

## 6. Requests the skill declines, and compliant alternatives

| Request | Response | Compliant alternative to offer |
|---|---|---|
| Script telling customers to keep cash deposits at or under $10,000 or split them across days or branches | Declined: hard stop (assisting structuring) | Script explaining that the bank files a CTR for cash over $10,000, that it is routine, and that staff cannot advise on how to avoid it |
| Procedure exempting valued or large customers from SAR decisioning, or instructing analysts to close alerts without review | Declined: hard stop | Risk-based alert tuning with documented rationale and validation; the same decision standard for every customer |
| Thresholds or rules set so that structuring or other reportable patterns cannot generate alerts | Declined: hard stop | Threshold calibration tied to the risk assessment, tested by below-the-line sampling |
| Relationship manager call or letter telling a customer a SAR was filed, or hinting at it | Declined: hard stop | Exit or closure letter without SAR reference; internal escalation to the BSA officer |
| Producing SARs in civil discovery | Declined: hard stop for production | Decline-and-notify-FinCEN procedure; produce underlying business records as counsel advises |
| Splitting a customer's wires or names to avoid sanctions screening hits | Declined: hard stop | Escalation and OFAC licensing review |

## 7. Record retention schedule

| Record | Period | Starts | Rule |
|---|---|---|---|
| SAR and supporting documentation | 5 years | Date of filing | 1020.320(d); 1022.320(c) |
| CTR copy | 5 years | Date of the report | 1010.306(a)(2) |
| Beneficial ownership identification (certification) | 5 years | Account closed | 1010.230(i)(2) |
| Beneficial ownership verification records | 5 years | Record made | 1010.230(i)(2) |
| Other Chapter X records | 5 years | As the rule states | 1010.430(d) |
| OFAC transaction records | 10 years | Date of transaction | 501.601 (amended 89 FR 74834, Sept. 13, 2024) |
| OFAC blocked property records | Period blocked plus 10 years | Date unblocked | 501.601 |

The FFIEC manual's OFAC page still states five years; the regulation controls. Name this conflict in the reconciliation table when a source quotes five years for OFAC records.

## 8. OFAC sanctions compliance as a separate regime

- OFAC administers sanctions under IEEPA, TWEA and program statutes, with regulations in 31 C.F.R. Chapter V. It is not part of the BSA and not a Chapter X requirement. Unlike the BSA, OFAC regulations reach U.S. banks' foreign branches and often overseas offices (FFIEC manual).
- Civil liability is strict: a person may be liable without knowing or having reason to know the transaction was prohibited (Commerce, Treasury and Justice Tri-Seal Compliance Note, March 2024). Risk-based screening design does not convert a sanctions prohibition into a risk tolerance.
- OFAC's Framework for Compliance Commitments (2019) names five components: management commitment, risk assessment, internal controls, testing and auditing, training. OFAC may consider an effective program in deciding penalties.
- Program content: sanctions risk assessment; screening of customers, beneficial owners, counterparties and transactions with list update timing; blocking into a labeled interest-bearing blocked account where the regulations require; rejection; reporting within 10 business days; annual report by September 30; licensing; voluntary self-disclosure decisions (Economic Sanctions Enforcement Guidelines, 31 C.F.R. Part 501, App. A); 10-year records.
- Present it as a separate sanctions compliance program, or as a clearly separate chapter with its own authority, owner, testing scope and retention. It may share people and systems with the BSA program.
- Detailed screening design, match investigation and escalation go to managing-sanctions-screening.
