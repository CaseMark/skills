# Patent Status, Remedy Windows, Willfulness and Privilege

Rules for confirming that the claims charted are the claims in force, for fixing the period in which infringing acts and damages can exist, and for handling willfulness and privilege. Each timed element has its own trigger; never compute one date from another element's trigger.

## Contents

1. Claim version: certificates of correction, reissue, reexamination and IPR
2. Patent term and expiration
3. Clocks table
4. Damages window: 286 and 287
5. IPR record and estoppel
6. Willfulness, enhanced damages and advice of counsel
7. Privilege and the written analysis
8. Damages hand-off

## 1. Claim version

Pull the full file wrapper and every post-grant certificate before charting. The claim in force is the last certificate's text, not the claim printed on the face of the original patent.

| Event | Effect on the claims | Source |
|---|---|---|
| Inter partes review final written decision, then certificate | Certificate cancels claims finally determined unpatentable, confirms those found patentable, and incorporates new or amended claims | 35 U.S.C. 318(a)-(b) |
| Ex parte reexamination certificate | Cancels, confirms or incorporates amended or new claims | 35 U.S.C. 307(a) |
| Amended or new claim after IPR or reexamination | Intervening rights as for reissue under 252 for anyone who made, purchased, used or imported, or made substantial preparation, before the certificate issued | 35 U.S.C. 318(c), 307(b) |
| Reissue | Original surrendered; claims substantially identical to the original continue from the original date; others carry intervening rights | 35 U.S.C. 252 |
| Claims canceled while an infringement suit is still pending | Patentee no longer has a cause of action on those claims if the case is not yet final | Fresenius USA v. Baxter Int'l, 721 F.3d 1330 (Fed. Cir. 2013) |
| Statutory disclaimer of a complete claim | The recorded disclaimer is thereafter considered part of the original patent; effect on pending suits and past damages `[VERIFY]` | 35 U.S.C. 253(a) |
| Certificate of correction (Office mistake or applicant's clerical mistake) | The corrected patent has effect only for causes of action arising after the certificate; chart pre-certificate acts against the uncorrected text | 35 U.S.C. 254, 255 |

Record in the claim status table, for each asserted claim: original text, each certificate and date, text in force, and one status label from the output template. A canceled claim is never charted as asserted. A dependent claim whose parent was canceled survives only if itself confirmed or not challenged, and it still includes the parent's limitations.

## 2. Patent term and expiration

- Term begins on issue and ends 20 years from the U.S. filing date of the application, or, if the application specifically references an earlier application under 35 U.S.C. 120, 121, 365(c) or 386(c), from the filing date of the earliest such application (35 U.S.C. 154(a)(2)). A continuation or divisional therefore expires 20 years from the earliest U.S. nonprovisional parent it claims, not from its own filing date.
- Foreign priority and provisional applications claimed under 119, 365(a), 365(b), 386(a) or 386(b) do not count toward term (154(a)(3)).
- Patent term adjustment under 154(b) adds the days printed on the patent and any later USPTO redetermination. Patent term extension under 35 U.S.C. 156 runs from the original expiration (including 154(b) adjustment) for a patent claiming a product subject to regulatory review, and during the extension the rights are limited to approved uses of the product (156(a), (b)); the length of any extension comes from the USPTO record.
- Terminal disclaimer: the patentee may disclaim any terminal part of the term (35 U.S.C. 253(b)). A terminal disclaimer filed to obviate nonstatutory double patenting ends the term at the reference patent's full statutory term as the disclaimer defines it (on the standard form, as that term is shortened by any terminal disclaimer of the reference patent) (MPEP 1490; PTO/AIA/26). An early lapse of the reference patent does not shorten it unless the disclaimer says otherwise: the standard forms state that the disclaimer does not reach the term up to the reference patent's full statutory term if the reference patent later expires for failure to pay a maintenance fee, is held unenforceable or invalid, is disclaimed, has all claims canceled by a reexamination certificate, is reissued, or is otherwise terminated early. Enforceability still ends when common ownership with the reference patent ends (37 C.F.R. 1.321(c)(3)). Term adjustment under 154(b) cannot carry the patent past the date specified in the disclaimer (154(b)(2)(B)). Read the disclaimer itself; check the reference patent's full statutory term and the ownership of both patents. Whether the reference patent's own term adjustment counts toward its "full statutory term" `[VERIFY]`.
- Maintenance fees for utility patents fall due 3.5, 7.5 and 11.5 years after grant; if not paid by the due date or within the 6-month grace period, the patent expires at the end of the grace period (35 U.S.C. 41(b)). If the Director later accepts a delayed fee as unintentional, the patent is considered not to have expired, but anyone who made, bought, sold, used or imported the invention after the grace period and before acceptance has intervening rights (41(c)).
- Provisional rights: separately from infringement, a patent carries a right to a reasonable royalty from anyone who, between publication of the application under 122(b) and issue, made, used, offered, sold or imported the invention as claimed in the published application and had actual notice of the published application; only if the issued claim is substantially identical to the published claim, and only in an action brought within 6 years after issue (35 U.S.C. 154(d)). No publication (for example, a nonpublication request) means no provisional rights.
- Infringement under 271(a) requires the act during the term. Acts after expiration are not infringing; an "offer to sell" by someone other than the patentee is one where the sale will occur before expiration (271(i)).

## 3. Clocks table

| Element | Trigger event | Period or rule | Source |
|---|---|---|---|
| Statutory term | Filing date of the earliest U.S. application specifically referenced under 120, 121, 365(c) or 386(c), or the application's own U.S. filing date | 20 years, plus 154(b) adjustment | 35 U.S.C. 154(a)(2), (b) |
| Terminal-disclaimed term | End of the reference patent's full statutory term as the disclaimer defines it (not an early lapse, invalidity or cancellation of the reference patent unless the disclaimer says otherwise) | Ends then, even if 154 and 154(b) would run longer | 35 U.S.C. 253(b), 154(b)(2)(B); 37 C.F.R. 1.321; MPEP 1490; PTO/AIA/26 |
| Enforceability under a double-patenting terminal disclaimer | Any date common ownership with the reference patent ends | Unenforceable while not commonly owned, whatever the term | 37 C.F.R. 1.321(c)(3) |
| Maintenance fee lapse | Grant date | Due 3.5, 7.5, 11.5 years; 6-month grace; expires at end of grace | 35 U.S.C. 41(b) |
| Intervening rights after delayed fee acceptance | End of the 6-month grace period, then the date the delayed fee is accepted | Acts between the two dates protected | 35 U.S.C. 41(c)(2) |
| Certificate of correction | Issue date of the certificate | Corrected text governs causes arising after it | 35 U.S.C. 254, 255 |
| Provisional-rights royalty period | Publication of the application under 122(b), with actual notice of it, until issue | Royalty only; claims substantially identical; suit within 6 years after issue | 35 U.S.C. 154(d) |
| Damages lookback | Filing of the complaint or counterclaim for infringement | No recovery for infringement more than 6 years before filing | 35 U.S.C. 286 |
| Pre-notice damages for unmarked patented articles | Date of actual notice of infringement to the infringer, or filing of the action | Damages only after notice if patented articles were not marked | 35 U.S.C. 287(a) |
| Knowledge for inducement and contributory infringement | Date the accused party learned of the patent and of the infringement (or became willfully blind) | Indirect liability only from that date | Global-Tech; Commil; Aro |
| IPR petition bar | Service on the petitioner, its real party in interest or privy of a complaint alleging infringement of the patent | Petition more than 1 year later cannot be instituted (joinder excepted) | 35 U.S.C. 315(b) |
| Intervening rights for amended or new claims | Issue date of the IPR or reexamination certificate | Protects acts and substantial preparation before that date | 35 U.S.C. 318(c), 307(b) |
| 298 applicability | Commencement of the civil action | Applies to actions commenced on or after January 14, 2013 | Pub. L. 112-274, note to 35 U.S.C. 298 |

Show every computed date with its weekday, the trigger date's evidence, and the arithmetic.

## 4. Damages window: 286 and 287

- Section 286 is a limit on recovery measured back from the filing of the complaint or counterclaim, not a bar on filing. Laches cannot defeat damages for infringement within the 286 period (SCA Hygiene Prods. v. First Quality Baby Prods., 580 U.S. 328 (2017)).
- Marking: a patentee or licensee that makes, offers, sells or imports a patented article may mark it with "patent" or "pat." and the number, or with an internet address associating the article with the number. Without marking, damages run only from proof that the infringer was notified of the infringement and continued; filing suit is notice (287(a)).
- The patentee bears the burden of pleading and proving compliance with 287(a). The accused infringer bears only an initial burden of production to identify unmarked products it believes practice the patent (Arctic Cat v. Bombardier Recreational Prods., 876 F.3d 1350 (Fed. Cir. 2017)).
- Actual notice requires the affirmative communication of a specific charge of infringement by a specific accused product or device; the infringer's own knowledge does not count (Amsted Indus. v. Buckeye Steel Castings, 24 F.3d 178 (Fed. Cir. 1994)).
- The marking requirement does not apply when only method claims are asserted (Crown Packaging Tech. v. Rexam Beverage Can, 559 F.3d 1308 (Fed. Cir. 2009)). When both apparatus and method claims are asserted from a patent whose articles were sold unmarked, analyze each claim type separately `[VERIFY]`.
- This skill reports the damages window and the notice dates only. Amounts go to the damages expert.

## 5. IPR record and estoppel

- Read the petition, institution decision, patent owner response, any motion to amend, the final written decision and the certificate. Patent owner statements in the IPR can create prosecution disclaimer for construction (Aylus).
- Estoppel in court: after a final written decision, the petitioner, its real party in interest or privy may not assert that a claim is invalid on any ground it raised or reasonably could have raised in the IPR (35 U.S.C. 315(e)(2)). IPR grounds are limited to patents and printed publications, so estoppel does not bar a public-use, on-sale or known-or-used ground based on a physical system, even when patents and printed publications describing it are used as evidence (Ingenico Inc. v. IOENGINE, LLC, 136 F.4th 1354 (Fed. Cir. 2025)).
- Estoppel is a validity question. This skill records it in the IPR register and hands validity to answer-with-invalidity-contentions or notice-of-prior-art; it does not decide invalidity.

## 6. Willfulness, enhanced damages and advice of counsel

- The court may increase damages up to three times the amount found (35 U.S.C. 284). Enhancement is discretionary and reserved for egregious infringement behavior; subjective willfulness, intentional or knowing, may warrant it without a separate objective-recklessness showing; culpability is measured against the actor's knowledge at the time of the conduct; the standard of proof is a preponderance (Halo Elecs. v. Pulse Elecs., 579 U.S. 93 (2016)).
- Failure to obtain advice of counsel, or to present it, may not be used to prove willful infringement or intent to induce (35 U.S.C. 298).
- No adverse inference that an opinion was or would have been unfavorable arises from invoking privilege or from not obtaining an opinion (Knorr-Bremse v. Dana Corp., 383 F.3d 1337 (Fed. Cir. 2004) (en banc)).
- Record evidence bearing on willfulness neutrally: when the accused party learned of the patent, notice letters, copying evidence, design-around efforts, and good-faith non-infringement or invalidity positions. Adverse facts such as internal copying statements are stated, not omitted.

## 7. Privilege and the written analysis

- A party that relies on advice of counsel to answer a willfulness charge waives attorney-client privilege and work-product protection for communications on the same subject matter; an in-house infringement analysis conveyed to decision makers was treated as a legal opinion, and the waiver reached communications before and after the complaint (In re EchoStar Commc'ns Corp., 448 F.3d 1294 (Fed. Cir. 2006)). Scope of waiver as to trial counsel `[VERIFY]` (In re Seagate not read).
- Consequences for this skill:
  - Every output is a draft prepared at the direction of counsel for attorney review. Do not call it an opinion of counsel, do not put it on letterhead for signature, and do not address it to a business recipient for reliance.
  - Whether a formal opinion of counsel is obtained, who writes it, and whether it is relied on are counsel's decisions. Note that a formal opinion relied on later may be produced with related communications on the same subject.
  - Keep technical findings, evidence citations and adverse facts in the draft. A draft that omits known adverse facts cannot support any later good-faith position and misleads the reviewer.
  - Privilege and work-product labeling and distribution follow counsel's instructions; whether work-product protection attaches depends on anticipation of litigation and forum law `[VERIFY]`.

## 8. Damages hand-off

- Section 284 provides damages adequate to compensate, and no less than a reasonable royalty. The en banc Federal Circuit applied Rule 702 to exclude a royalty expert's per-unit rate drawn from licenses that did not support it, and ordered a new damages trial (EcoFactor, Inc. v. Google LLC, 137 F.4th 1333 (Fed. Cir. 2025) (en banc)).
- Pass to the damages expert: the claims with an infringement position supported, the accused products and versions, the damages window and its trigger dates, marking and notice findings, the date of knowledge, the place of each act (domestic, 271(f), 271(g)), any non-infringing alternatives found during the design-around review, and licenses in the record. Do not compute a royalty rate or lost profits here.
