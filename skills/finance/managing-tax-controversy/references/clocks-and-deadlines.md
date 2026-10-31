# Clocks and Deadlines

Every clock below has its own trigger event. Never borrow one clock's trigger for another: the petition period runs from the notice's mailing date, the CDP levy window from the date of the CDP notice, the lien window from the end of a five-business-day period after the lien filing, the BBA modification window from the NOPPA mailing date, and the push-out window from the FPA. All rules were read on 2026-10-30; citations and URLs are in `references/primary-sources.md`.

## Contents

1. Counting conventions and the IRC 7503 roll
2. Computation script and output format
3. Assessment clocks (IRC 6501) and consents
4. Refund clocks (IRC 6511, 6513, 6532)
5. Deficiency petition clock (IRC 6213(a)) and its circuit status
6. Appeals intake clocks
7. Collection due process clocks (IRC 6320, 6330)
8. BBA partnership clocks (IRC 6225, 6226, 6231, 6234, 6235)
8A. Third-party summons and innocent spouse clocks (IRC 7609, 6015)
9. Competent authority (MAP) and APA clocks (Rev. Proc. 2015-40, 2015-41)

## 1. Counting conventions and the IRC 7503 roll

- "Within N days after" an event: the event date is day 0; the raw last day is the event date plus N days.
- "N-day period beginning on" an event date: the event date is day 1; the raw last day is the event date plus N minus 1 days.
- "N-day period commencing the day after" an event: the raw last day is the event date plus N days.
- Years: the same calendar date N years later (a February 29 trigger maps to February 28).
- IRC 7503: when the last day for an act falls on a Saturday, Sunday or legal holiday, the act is timely on the next day that is none of those. "Legal holiday" means a District of Columbia legal holiday (and, for an act at an IRS office outside D.C., a statewide holiday in that office's state). IRC 6213(a) repeats the rule for the petition period.
- D.C. legal holidays (D.C. Code 28-2701; list repeated in IRM 25.6.1): January 1; third Monday in January; January 20 every fourth year (Inauguration Day, next in 2029; Monday if January 20 is a Sunday); third Monday in February; April 16 (D.C. Emancipation Day); last Monday in May; June 19; July 4; first Monday in September; second Monday in October; November 11; fourth Thursday in November; December 25. A holiday falling on Saturday is observed the preceding Friday; on Sunday, the following Monday. A January 1 falling on Saturday makes the preceding December 31 a holiday.
- Ad hoc closures (a day of mourning, an executive-order closure) are not on the statutory list. IRM 25.6.1 treats a presidential-death closure as extending the ASED and RSED to the next business day; treat any other closure as [VERIFY] and plan to the unrolled date.
- Timely mailing: IRC 7502 deems a document delivered by U.S. mail or a designated private delivery service to be filed on the postmark date if the postmark falls within the period. An e-filed Tax Court petition is timed by the court's own filing platform; [VERIFY] the court's current electronic-filing cutoff before relying on a same-day filing.
- Early return: a return filed before its due date is deemed filed on the due date for IRC 6501 (6501(b)(1)) and 6511 (6513(a)). IRC 7503 does not move the deemed filing date (IRM 25.6.1, citing Rev. Rul. 81-269).

## 2. Computation script and output format

Recompute every date with a script; never count on a calendar by hand. A minimal implementation:

```python
from datetime import date, timedelta
def nth(y, m, wd, n):                      # nth weekday (Mon=0) of month
    d = date(y, m, 1); d += timedelta((wd - d.weekday()) % 7)
    return d + timedelta(7 * (n - 1))
def last_monday(y, m):
    d = (date(y, m + 1, 1) if m < 12 else date(y + 1, 1, 1)) - timedelta(1)
    return d - timedelta(d.weekday())
def observed(d):
    return d - timedelta(1) if d.weekday() == 5 else d + timedelta(1) if d.weekday() == 6 else d
def dc_holidays(y):
    h = {observed(date(y, m, d)) for m, d in [(1, 1), (4, 16), (6, 19), (7, 4), (11, 11), (12, 25)]}
    h |= {observed(date(y + 1, 1, 1))}
    h |= {nth(y, 1, 0, 3), nth(y, 2, 0, 3), last_monday(y, 5), nth(y, 9, 0, 1), nth(y, 10, 0, 2), nth(y, 11, 3, 4)}
    if (y - 2029) % 4 == 0:
        i = date(y, 1, 20); h.add(i + timedelta(1) if i.weekday() == 6 else i)
    return h
def roll_7503(d):
    while d.weekday() >= 5 or d in dc_holidays(d.year):
        d += timedelta(1)
    return d
```

Report each clock in this fixed format, one block per clock:

```
Clock:          <name>                         Authority: <IRC section, regulation>
Trigger:        <event> on <date> (<weekday>)  Source: <document and locator>
Counting rule:  <e.g., within 90 days after mailing; mailing date is day 0>
Raw last day:   <date> (<weekday>)
7503 roll:      <rolled to <date> because <holiday or weekend> | not rolled>
Due date:       <date> (<weekday>)
Other reading:  <date> - <why> | none.  Plan to the earlier date.
```

## 3. Assessment clocks (IRC 6501) and consents

| Clock | Trigger | Period | Notes |
|---|---|---|---|
| General ASED | Return filed (early return deemed filed on due date) | 3 years after (6501(a)) | Do not apply a 7503 roll to the IRS's assessment date for planning; IRM 25.6.1 tables apply the roll to some return types [VERIFY for the return at issue] |
| Substantial omission | Return filed | 6 years (6501(e)(1)(A)) | Omitted gross income over 25 percent of gross income stated; for a trade or business, gross income is gross receipts before cost of sales; an overstatement of basis counts as an omission; amounts adequately disclosed do not count. Also 6 years for an omission over $5,000 attributable to a 6038D foreign financial asset, and for 951(a) inclusions (6501(e)(1)(C)) |
| Unlimited | False or fraudulent return with intent to evade; willful attempt to evade (non-income taxes); no return filed | Any time (6501(c)(1)-(3)) | A fraud allegation triggers the Checkpoint A criminal-exposure hard stop |
| Foreign information returns | Date the information required under 6038, 6038A, 6038B, 6038D, 6046, 6046A, 6048 (and certain PFIC elections) is furnished | Not before 3 years after (6501(c)(8)); limited to related items if failure was due to reasonable cause | The whole return can stay open |
| Listed transactions | Earlier of disclosure or material-advisor list response | Not before 1 year after (6501(c)(10)) | |
| Late-period amended return | IRS receives a signed document showing additional tax within 60 days before the ASED | ASED for that amount extended to 60 days after receipt (6501(c)(7)) | |
| Form 872 (fixed date) | Signed by both parties before the ASED | To the stated date; further extensions only before that date expires (6501(c)(4)(A)) | A consent signed after expiry does not revive the period |
| Form 872-A (open-ended) | Signed before the ASED | Ends 90 days after the IRS receives Form 872-T from the taxpayer, 90 days after the IRS mails Form 872-T, or 90 days after a notice of deficiency plus 60 days after the restricted period; or on assessment reflecting a final determination and Appeals consideration (IRM 25.6.22.7.1) | Partial agreements, jeopardy and math-error assessments and amended-return assessments do not end it |
| Restricted consent | Negotiated language prepared by the IRS and approved by IRS Counsel | Fixed or open-ended, limited to named issues (Pub. 1035) | IRS grants only when issues outside the restriction are agreed and the scope can be described |

The IRS must tell the taxpayer, each time it asks for a consent, of the right to refuse or to limit the extension to particular issues or periods (6501(c)(4)(B)). Pub. 1035 lists three options: sign an unconditional consent, negotiate terms (period, issues, form), or refuse (the IRS then issues a notice of deficiency, and no penalty attaches to refusing). A consent extends the refund-claim period too (6511(c), Section 4).

## 4. Refund clocks (IRC 6511, 6513, 6532)

| Clock | Trigger | Period | Look-back limit on amount |
|---|---|---|---|
| Claim, return filed | Return filed (early return deemed filed on due date, 6513(a)) | 3 years after filing or 2 years after payment, whichever ends later (6511(a)) | Claim within the 3-year period: tax paid within 3 years plus any filing extension before the claim (6511(b)(2)(A)). Otherwise: tax paid within 2 years before the claim (6511(b)(2)(B)) |
| Claim, no return filed | Each payment | 2 years after that payment | Tax paid within 2 years before the claim |
| Consent in place | Consent signed within the claim period | Not before 6 months after the extended assessment period ends (6511(c)(1)) | Tax paid after the consent plus the amount allowable had the claim been filed when the consent was signed (6511(c)(2)) |
| Financial disability | Individual unable to manage financial affairs (physician statement required; not while a spouse or other person is authorized to act) | Periods suspended (6511(h)) | Same suspension |
| Refund suit | Claim filed; notice of disallowance mailed | Not before 6 months after the claim unless decided; not after 2 years from mailing of the disallowance (6532(a)(1)); extendable by written agreement (Form 907); a filed waiver (Form 2297) starts the 2 years | A claim is a prerequisite to suit (7422(a)) |

Informal claim: a timely written submission that fairly advises the IRS of the nature of the claim can stop the 6511 clock even if it is defective in form, when the defects are remedied by a later amendment and the IRS was not misled (United States v. Kales, 314 U.S. 186 (1941)). Treat it as a rescue argument only: plan to a formal claim on the correct form before the 6511 date, and record the date and content of any earlier letter that might qualify.

Deemed payment dates (6513): early payments on the return due date; withholding on the 15th day of the fourth month after the year ends; estimated tax on the return due date without extensions. Rev. Rul. 2003-41: IRC 7503 adds a filing-extension day to the 3-year look-back only if the return was in fact filed on the rolled day. A return's processing or posting date is not its filing date; use the received date on the transcript or the postmark.

## 5. Deficiency petition clock (IRC 6213(a)) and its circuit status

- Period: within 90 days after the notice is mailed, or 150 days if the notice is addressed to a person outside the United States. The mailing date controls, not receipt. A Saturday, Sunday or D.C. holiday is not counted as the last day.
- Date on the notice: a petition filed on or before the last date the IRS specifies in the notice is treated as timely (6213(a), last sentence). When the notice states a later date than the statute, it is a safe harbor to the stated date; when it states an earlier date, the statutory date still governs. Compute both and plan to the earlier.
- Address: a notice mailed to the last known address is sufficient even if not received (6212(b)(1)).
- Status (checked 2026-10-30): The Tax Court holds the deadline jurisdictional (Hallmark Research Collective, 159 T.C. 126 (2022); Sanders, 161 T.C. No. 8 (2023)) and follows the precedent of the circuit to which the case is appealable (Golsen, 54 T.C. 742 (1970); venue under 7482(b): individual's legal residence, corporation's principal place of business, partnership's principal place of business for 6234 petitions).

| Circuit | Holding | Tolling |
|---|---|---|
| 2d | Buller, No. 24-1557 (Aug. 14, 2025, amended Nov. 26, 2025; cited as 160 F.4th 266 in Kyick and Maniktala [VERIFY reporter citation]): nonjurisdictional | Available; remanded |
| 3d | Culp, 75 F.4th 196 (2023): nonjurisdictional | Presumptively available; remanded |
| 6th | Oquendo, 148 F.4th 820 (2025): nonjurisdictional | Available; case by case; remanded |
| 8th | Maniktala, No. 25-1366 (Aug. 11, 2026): nonjurisdictional | Available; remanded |
| 1st | Kyick Holdings, No. 25-1429 (Aug. 17, 2026): nonjurisdictional but mandatory | Not available |
| 9th | Organic Cannabis, 962 F.3d 1082 (2020) (pre-Boechler, noting a long jurisdictional reading); Atighi (unpublished, 2022): jurisdictional | Pending appeals reported [VERIFY] |
| 4th, 5th, 7th, 10th, 11th, D.C. | No post-Boechler published holding located; older or unpublished decisions treat it as jurisdictional; appeals pending in several [VERIFY] | Treat as unavailable |

Planning rule in every circuit: file by the earlier of the statutory due date and the date on the notice. Equitable tolling is a remedy argument after a miss (diligence plus an extraordinary circumstance, decided case by case), never a planning date. Legislation to make the deadline tollable (H.R. 5349, passed by the Senate with an amendment on September 30, 2026) was not law on 2026-10-30.

## 6. Appeals intake clocks

- Non-docketed case: Appeals will not accept a proposed deficiency case with fewer than 365 days left on the ASED (270 for estate tax) (IRM 8.21.3.2.1). If a protest is planned and fewer than 365 days remain when the case would reach Appeals, a consent is needed or the case goes to Appeals only after a Tax Court petition.
- New information at Appeals: Appeals may return the case to the examiner if at least 210 days remain, and needs 180 days on return (IRM 8.21.3.2.1).
- 30-day letter: the response date is the one printed in the letter; there is no statutory roll. Ask in writing for more time before it passes.
- Case file access: a "specified taxpayer" (individual with AGI of $400,000 or less, or other taxpayer with gross receipts of $5 million or less for the year in dispute) gets the nonprivileged case file no later than 10 days before the Appeals conference (7803(e)(7)).

## 7. Collection due process clocks (IRC 6320, 6330)

| Clock | Trigger | Period | Consequence of missing it |
|---|---|---|---|
| Levy CDP request (6330) | Date of the CDP notice (sent at least 30 days before the first levy) | 30-day period commencing the day after the notice date (Treas. Reg. 301.6330-1, A-C3) | Equivalent hearing only: request within one year commencing the day after the notice date (A-I7); no Tax Court review of the decision except some 6015 relief (A-I6); collection is not automatically suspended |
| Lien CDP request (6320) | End of the 5-business-day period after the NFTL is filed | 30-day period beginning the day after that 5-day period (301.6320-1) | Equivalent hearing within one year after the end of the 5-business-day period |
| Tax Court petition from a notice of determination | Date of the determination | Within 30 days (6330(d)(1)) | Nonjurisdictional and subject to equitable tolling (Boechler, 596 U.S. 199 (2022)); still plan to the 30th day |

A timely CDP request suspends levy and the collection, criminal and suit limitation periods while the hearing and appeals are pending, and not less than 90 days after a final determination (6330(e)(1)). The underlying liability can be contested only if no notice of deficiency was received and no other opportunity to dispute existed (6330(c)(2)(B)). One hearing per tax period (6330(b)(2)).

## 8. BBA partnership clocks (IRC 6225, 6226, 6231, 6234, 6235)

| Clock | Trigger | Period | Notes |
|---|---|---|---|
| Modification submissions | NOPPA mailed | Statute: the 270-day period beginning on the mailing date (6225(c)(7)), so mailing date plus 269 days. Regulation: on or before 270 days after the mailing date (301.6225-2(c)(3)(i)), so plus 270 days | Name the conflict; plan to the earlier date. Extensions only with IRS consent, requested before the period ends |
| FPA earliest mailing | NOPPA mailed | Not earlier than 270 days after, unless the partnership waives (6231(b)(2)(A)) | |
| Push-out election | FPA date | Not later than 45 days after (6226(a)(1)); cannot be extended (301.6226-1(c)(2)) | Revocable only with IRS consent; partner statements must be furnished |
| Readjustment petition | FPA mailed | Within 90 days (6234(a)) to Tax Court, district court or Court of Federal Claims | District court and Claims Court require a deposit of the imputed underpayment, penalties and additions first (6234(b)) |
| Adjustment period | Later of return filed, return due date, or AAR filed | 3 years (6235(a)(1)); or 270 days (plus extensions) after all modification materials are submitted; or 330 days (plus extensions) after the NOPPA | Extendable by agreement before expiry (6235(b)) |

## 8A. Third-party summons and innocent spouse clocks (IRC 7609, 6015)

| Clock | Trigger | Period | Notes |
|---|---|---|---|
| Notice of third-party summons | Service of the summons on the third party | IRS must give notice within 3 days after service and no later than the 23rd day before the examination date (7609(a)(1)); mailing to the last known address is sufficient (7609(a)(2)) | Record the mailing date on the notice; it starts the next clock |
| Petition to quash a third-party summons | Day the notice is given (mailed or served) | Not later than the 20th day after (7609(b)(2)(A)); by the same 20th day, mail a copy of the petition by registered or certified mail to the summoned person and the IRS office named in the notice (7609(b)(2)(B)) | Filed in district court; whether 7503 rolls this court deadline is [VERIFY], so plan to the unrolled day. A taxpayer's petition suspends the 6501 and 6531 periods while pending (7609(e)(1)) |
| Innocent spouse election under 6015(b) or (c) | IRS begins collection activities against the requesting spouse | Any time after a deficiency is asserted and not later than 2 years after collection activities begin (6015(c)(3)(B); 6015(b)(1)(E)) | (c) requires divorce, legal separation, or not living in the same household for 12 months |
| Equitable relief request under 6015(f) | Unpaid liability: the collection period under 6502; paid liability: the refund period under 6511 | Before that period expires (6015(f)(2)) | Each liability portion has its own trigger |
| Tax Court petition for 6015 relief | IRS mails its final determination, or 6 months pass after the election or request with no determination | Any time after the earlier event and not later than the 90th day after the final determination is mailed (6015(e)(1)(A)) | Review is de novo on the administrative record plus newly discovered evidence (6015(e)(7)) |

## 9. Competent authority (MAP) and APA clocks (Rev. Proc. 2015-40, 2015-41)

Both revenue procedures roll their own deadlines to the next day that is not a Saturday, Sunday or D.C. legal holiday (section 1.03 of each). A treaty's own time limit overrides the revenue procedure (Rev. Proc. 2015-40, sec. 3). Neither procedure had been superseded on 2026-10-30; APA user fees were raised for requests filed after January 1, 2024 (IRS user fee page), and remote signatures and electronic filing were allowed from 2020 (IRS release of May 11, 2020).

| Clock | Trigger | Period | Source and notes |
|---|---|---|---|
| Earliest MAP request (U.S.-initiated adjustment) | IRS communicates the proposed adjustment amount in writing (Form 5701 NOPA or Form 4549) | Not accepted before that date | Rev. Proc. 2015-40, sec. 3.04 |
| MAP request for an issue already protested to Appeals | Opening conference with Appeals | No later than 60 days after; issue severed from the protest; no Appeals ADR invoked and no Form 870-AD or closing agreement on it | Rev. Proc. 2015-40, sec. 6.04(3) |
| Treaty notification (foreign-initiated or one-country request) | Event the treaty names (for example, the foreign notice of adjustment) | The number of years the treaty specifies | Rev. Proc. 2015-40, sec. 12; treaty-specific [VERIFY the treaty article for the matter] |
| Protective claim for the U.S. refund side | Reason to believe a tax authority action has resulted or is likely to result in a competent authority issue | Must be a valid IRC 6402 claim; file within the IRC 6511 period for the competent authority year (Section 4) to keep the refund available | Rev. Proc. 2015-40, sec. 11.02; the 6511 timing is an inference from the claim requirement, confirm for the year |
| Annual notification of protective claim | Close of each taxable year after the year the protective claim was filed, until the MAP request is filed | No later than the timely filing date of the return for that later year | Rev. Proc. 2015-40, sec. 11.05(1) |
| Statute extension during MAP | IRS request to extend the assessment period for years covered by the request (including ACAP years) | Before the ASED for each year | Refusing is a ground to deny or end assistance (Rev. Proc. 2015-40, sec. 7.02(2)(c)); a consent also extends the refund period (6511(c)) |
| APA request, prospective year | Applicable return date for the year: the later of the actual filing date (if timely) and the statutory due date without extensions | Complete request filed by that date, or the year becomes a rollback year | Rev. Proc. 2015-41, sec. 3.03(2)(a) |
| APA "dollar file" | Correct user fee paid (7502 timely payment applies) | Complete request within 120 days after; APMA may extend 30 days for good cause if asked before day 120 | Rev. Proc. 2015-41, sec. 3.03(3)(b) |
| Bilateral or multilateral APA | Substantive corresponding request filed with the foreign competent authority | Complete U.S. request no later than 60 days after | Rev. Proc. 2015-41, sec. 3.03(2)(b) |
| APA term consents | Each year of the proposed APA term | Consent to extend the assessment period (general or APMA-standard restricted) when instructed | Rev. Proc. 2015-41, sec. 2.03(3) as summarized in its sec. 1 |
| APA primary adjustment for an APA year | APA effective date | Amended return within 120 days, permitted only if the original return was timely filed no later than 60 days after the effective date | Rev. Proc. 2015-41, sec. 7 (administering the APA) |
| APMA prefiling memorandum review (IRS target, not a taxpayer deadline) | Later of the prefiling memorandum date and the date APMA's requested information is submitted | Review generally completed and an oral recommendation given within four weeks | IRM 4.60.3.3.3 (09-08-2025), from LB&I-04-0423-0006 |
| APMA review and acceptance of an APA request (IRS target) | Filing date of the completed APA request | Review generally completed within eight weeks; a decline needs the APMA director's concurrence and is followed by a decision letter | IRM 4.60.3.3.4 (09-08-2025) |

