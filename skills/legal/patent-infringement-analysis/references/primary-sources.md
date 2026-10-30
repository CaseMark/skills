# Primary Sources and Verification Register

## Contents

1. How these sources were checked
2. Statutes and regulations
3. Supreme Court cases
4. Federal Circuit cases
5. `[VERIFY]` list

## How these sources were checked

All checks were made on 2026-10-30 through the case.dev research API. "Full text via case.dev" means the page named in the URL column was retrieved through the case.dev contents or legal full-text endpoint and the statement was compared with the passage read, not a search snippet. Where the retrieval returned only the first 50,000 characters of a long opinion, the method says so and the statement rests on a passage inside that portion or in the returned highlights. Every case citation was also run through the case.dev citation verifier (`/legal/v1/verify`), which matched it to a CourtListener record. Statutes change; re-read the current text of each section relied on before the analysis goes to counsel (Ground Rule 4 in SKILL.md).

## Statutes and regulations

| Authority | URL read | Method | What it supports | Checked |
|---|---|---|---|---|
| 35 U.S.C. 271 | law.cornell.edu/uscode/text/35/271 | Full text via case.dev | (a) make, use, offer, sell within the U.S. or import during the term; (b) active inducement; (c) contributory infringement, material component, especially made or adapted, not a staple article; (f)(1) supply of all or a substantial portion of components to induce combination abroad; (f)(2) especially adapted component with knowledge and intent; (e)(1) safe harbor for uses reasonably related to submitting information under federal drug law; (g) import or sale of product made by a patented process, materially changed and trivial-component exceptions; (i) offer to sell by non-patentee means sale before expiration | 2026-10-30 |
| 35 U.S.C. 112(f) | law.cornell.edu/uscode/text/35/112 | Full text via case.dev | Means or step plus function construed to cover corresponding structure, material or acts in the specification and equivalents | 2026-10-30 |
| 35 U.S.C. 154(a)(2)-(3), (b), (d) | law.cornell.edu/uscode/text/35/154 | Full text via case.dev | Term ends 20 years from U.S. filing date or earliest application referenced under 120, 121, 365(c), 386(c); foreign and 119 priority not counted; term adjustment, and (b)(2)(B) no adjustment past a disclaimed date; (d) provisional-rights royalty from publication to issue with actual notice, substantially identical claims, suit within 6 years of issue | 2026-10-30 |
| 35 U.S.C. 41(b)-(c) | law.cornell.edu/uscode/text/35/41 | Full text via case.dev | Maintenance fees at 3.5, 7.5, 11.5 years after grant; expiration at the end of the 6-month grace period if unpaid; delayed fee accepted as unintentional treats the patent as not expired, with intervening rights for acts after the grace period and before acceptance | 2026-10-30 |
| 35 U.S.C. 252 | law.cornell.edu/uscode/text/35/252 | Full text via case.dev | Effect of reissue; substantially identical claims continue; intervening rights | 2026-10-30 |
| 35 U.S.C. 253 | law.cornell.edu/uscode/text/35/253 | Full text via case.dev | (a) disclaimer of a complete claim, considered part of the original patent; (b) disclaimer or dedication of a terminal part of the term | 2026-10-30 |
| 37 C.F.R. 1.321 | ecfr.gov (title 37, part 1, section 1.321) | Full text via case.dev | (c)(3) terminal disclaimer to obviate double patenting must state the patent is enforceable only while commonly owned with the reference | 2026-10-30 |
| MPEP 1490 (Disclaimers) | uspto.gov/web/offices/pac/mpep/s1490.html | Full text via case.dev | Terminal disclaimer cuts term beyond the full statutory term of the reference patent, as shortened by any terminal disclaimer; exculpatory language in the standard forms is permissible; common ownership required at the time of enforcement; 154(b)(2)(B) limits adjustment | 2026-10-30 |
| USPTO form PTO/AIA/26 | uspto.gov/sites/default/files/documents/aia0026.pdf | Full text via case.dev | Standard double-patenting disclaimer text: disclaims beyond the reference patent's full statutory term; does not disclaim up to that term if the reference patent later lapses for fees, is held unenforceable or invalid, is disclaimed, has all claims canceled by reexamination, is reissued, or is otherwise terminated early; common-ownership enforcement provision | 2026-10-30 |
| 35 U.S.C. 284 | law.cornell.edu/uscode/text/35/284 | Full text via case.dev | Damages adequate to compensate, not less than a reasonable royalty; increase up to three times; expert testimony | 2026-10-30 |
| 35 U.S.C. 286 | law.cornell.edu/uscode/text/35/286 | Full text via case.dev | No recovery for infringement more than six years before filing the complaint or counterclaim | 2026-10-30 |
| 35 U.S.C. 287(a) | law.cornell.edu/uscode/text/35/287 | Full text via case.dev | Marking with number or internet address; without marking, damages only after notice of infringement; filing suit is notice | 2026-10-30 |
| 35 U.S.C. 298 | law.cornell.edu/uscode/text/35/298 | Full text via case.dev | Failure to obtain or present advice of counsel may not prove willfulness or intent to induce; applies to civil actions commenced on or after January 14, 2013 (Pub. L. 112-274 note) | 2026-10-30 |
| 35 U.S.C. 307 | law.cornell.edu/uscode/text/35/307 | Full text via case.dev | Reexamination certificate cancels, confirms or incorporates claims; intervening rights for amended or new claims | 2026-10-30 |
| 35 U.S.C. 315 | law.cornell.edu/uscode/text/35/315 | Full text via case.dev | (a) civil action bars and stays; (b) one-year bar after service of an infringement complaint; (e)(1)-(2) estoppel for grounds raised or reasonably could have raised after a final written decision | 2026-10-30 |
| 35 U.S.C. 318 | law.cornell.edu/uscode/text/35/318 | Full text via case.dev | (a) final written decision; (b) certificate canceling, confirming and incorporating claims; (c) intervening rights | 2026-10-30 |
| 35 U.S.C. 273 | law.cornell.edu/uscode/text/35/273 | Full text via case.dev | (a) good-faith commercial use in the U.S. at least 1 year before the earlier of the effective filing date or a 102(b) public disclosure; (b) clear and convincing burden; (c) regulatory review and nonprofit uses | 2026-10-30 |
| 35 U.S.C. 254, 255 | law.cornell.edu/uscode/text/35/254 and /255 | Full text via case.dev | Corrected patent has effect for causes of action arising after the certificate | 2026-10-30 |
| 35 U.S.C. 156(a)-(b) | law.cornell.edu/uscode/text/35/156 | Full text via case.dev | Term extension from the original expiration including 154(b) adjustment for products subject to regulatory review; rights during extension limited to approved uses | 2026-10-30 |

## Supreme Court cases

| Case | URL read | Method | What it supports | Checked |
|---|---|---|---|---|
| Warner-Jenkinson Co. v. Hilton Davis Chem. Co., 520 U.S. 17 (1997) | supreme.justia.com/cases/federal/us/520/17/ | Full text via case.dev (first 50,000 characters and highlights) | Each element material; equivalents applied element by element, not to the invention as a whole (at 28-30); no application so broad as to eliminate an element; equivalence judged at the time of infringement; triple identity or insubstantial differences; presumption of a patentability reason where the record does not explain an amendment | 2026-10-30 |
| Festo Corp. v. Shoketsu Kinzoku Kogyo Kabushiki Co., 535 U.S. 722 (2002) | courtlistener.com opinion 118510 | Full text via case.dev legal full-text | Narrowing amendment to satisfy any requirement of the Patent Act may create estoppel (at 736); presumptive surrender of territory between original and amended claim; patentee's burden to rebut: unforeseeable, tangential, or other reason (at 740-41); no complete bar | 2026-10-30 |
| Global-Tech Appliances, Inc. v. SEB S.A., 563 U.S. 754 (2011) | courtlistener.com opinion 217702 | Full text via case.dev legal full-text | Inducement requires knowledge that the induced acts constitute patent infringement; same knowledge for 271(b) and (c); willful blindness: subjective belief of high probability plus deliberate actions to avoid learning; not recklessness or negligence | 2026-10-30 |
| Commil USA, LLC v. Cisco Sys., Inc., 575 U.S. 632 (2015) | law.cornell.edu/supremecourt/text/13-896 | Full text via case.dev | Inducement requires knowledge of the patent and knowledge that the induced acts infringe; belief in invalidity is not a defense | 2026-10-30 |
| Limelight Networks, Inc. v. Akamai Techs., Inc., 572 U.S. 915 (2014) | supreme.justia.com/cases/federal/us/572/12-786/ | Full text via case.dev | No inducement liability under 271(b) when no one has directly infringed under 271(a) | 2026-10-30 |
| Aro Mfg. Co. v. Convertible Top Replacement Co., 377 U.S. 476 (1964) | supreme.justia.com/cases/federal/us/377/476/ | Full text via case.dev | 271(c) requires knowledge that the combination was both patented and infringing (at 488-93) | 2026-10-30 |
| Halo Elecs., Inc. v. Pulse Elecs., Inc., 579 U.S. 93 (2016) | supreme.justia.com/cases/federal/us/579/14-1513/ | Full text via case.dev | Enhanced damages discretionary for egregious conduct; subjective willfulness may suffice; culpability measured at the time of conduct; preponderance standard | 2026-10-30 |
| Microsoft Corp. v. AT&T Corp., 550 U.S. 437 (2007) | supreme.justia.com/cases/federal/us/550/05-1056/ | Full text via case.dev | Foreign-made copies of software are not components supplied from the U.S. under 271(f); presumption against extraterritoriality | 2026-10-30 |
| Life Techs. Corp. v. Promega Corp., 580 U.S. 140 (2017) | law.cornell.edu/supremecourt/text/14-1538 | Full text via case.dev | Supplying a single component of a multicomponent invention is not "all or a substantial portion" under 271(f)(1) | 2026-10-30 |
| WesternGeco LLC v. ION Geophysical Corp., 585 U.S. 407 (2018) | supreme.justia.com/cases/federal/us/585/16-1011/ | Full text via case.dev | Lost foreign profits recoverable for 271(f)(2) infringement as a domestic application of 284 | 2026-10-30 |
| SCA Hygiene Prods. Aktiebolag v. First Quality Baby Prods., LLC, 580 U.S. 328 (2017) | supreme.justia.com/cases/federal/us/580/15-927/ | Full text via case.dev | Laches cannot bar damages for infringement within the 286 period | 2026-10-30 |
| Impression Prods., Inc. v. Lexmark Int'l, Inc., 581 U.S. 360 (2017) | supreme.justia.com/cases/federal/us/581/15-1189/ | Full text via case.dev | Authorized sale exhausts patent rights in the item regardless of restrictions, including sales abroad | 2026-10-30 |

## Federal Circuit cases

| Case | URL read | Method | What it supports | Checked |
|---|---|---|---|---|
| Phillips v. AWH Corp., 415 F.3d 1303 (Fed. Cir. 2005) (en banc) | courtlistener.com opinion 791122 | Full text via case.dev legal full-text (first 50,000 characters and highlights) | Ordinary meaning to a skilled artisan at the effective filing date (at 1312-13); specification the single best guide; prosecution history intrinsic; extrinsic evidence less significant; claims not confined to a single embodiment (at 1323) | 2026-10-30 |
| Conoco, Inc. v. Energy & Envtl. Int'l, L.C., 460 F.3d 1349 (Fed. Cir. 2006) | law.resource.org (460 F.3d 1349) | Full text via case.dev | Argument-based estoppel requires a clear and unmistakable surrender of subject matter in the prosecution history; arguments are not presumed to surrender a range as amendments are | 2026-10-30 |
| DePuy Spine, Inc. v. Medtronic Sofamor Danek, Inc., 567 F.3d 1314 (Fed. Cir. 2009) | law.justia.com (cafc 08-1240) | Full text via case.dev | Ensnarement is a legal limit on equivalents decided by the court; hypothetical claim literally covering the accused device tested against prior art; patentee bears the burden of persuasion; quotes Warner-Jenkinson at 33 for the amendment-reason burden | 2026-10-30 |
| Wilson Sporting Goods Co. v. David Geoffrey & Assocs., 904 F.2d 677 (Fed. Cir. 1990) | Quoted in DePuy Spine | Citation verified; holding as quoted in DePuy Spine | Origin of the hypothetical-claim ensnarement test; patentee's burden | 2026-10-30 |
| Thorner v. Sony Computer Entm't Am. LLC, 669 F.3d 1362 (Fed. Cir. 2012) | law.justia.com (cafc 11-1114) | Full text via case.dev | Only two exceptions to plain meaning: lexicography and disavowal in specification or prosecution | 2026-10-30 |
| Williamson v. Citrix Online, LLC, 792 F.3d 1339 (Fed. Cir. 2015) (en banc in part) | law.justia.com (cafc 13-1130, 2015-06-16) | Full text via case.dev | "Strong" presumption against 112(f) without "means" overruled; test is whether the words have a sufficiently definite meaning as the name for structure; "module" as a nonce word | 2026-10-30 |
| Aylus Networks, Inc. v. Apple Inc., 856 F.3d 1353 (Fed. Cir. 2017) | law.justia.com (cafc 16-1599) | Full text via case.dev | Patent owner statements in IPR, before or after institution, can support prosecution disclaimer | 2026-10-30 |
| Johnson & Johnston Assocs. v. R.E. Serv. Co., 285 F.3d 1046 (Fed. Cir. 2002) (en banc) | law.justia.com (F3/285/1046) | Full text via case.dev | Subject matter disclosed but not claimed is dedicated to the public and cannot be recaptured by equivalents | 2026-10-30 |
| Akamai Techs., Inc. v. Limelight Networks, Inc., 797 F.3d 1020 (Fed. Cir. 2015) (en banc) | law.justia.com (cafc 09-1372, 2015-08-13) | Full text via case.dev | Single-entity rule for method claims; attribution by direction or control or joint enterprise; conditioning participation or a benefit on performance and establishing manner or timing | 2026-10-30 |
| Centillion Data Sys., LLC v. Qwest Commc'ns Int'l, Inc., 631 F.3d 1279 (Fed. Cir. 2011) | law.justia.com (cafc 10-1110-1131) | Full text via case.dev | To "use" a system a party must put it into service, control as a whole and obtain benefit; physical control of each element not required | 2026-10-30 |
| Arctic Cat Inc. v. Bombardier Recreational Prods. Inc., 876 F.3d 1350 (Fed. Cir. 2017) | law.justia.com (cafc 17-1475) | Full text via case.dev | Patentee bears burden of proving marking; accused infringer's low initial burden of production identifying unmarked products | 2026-10-30 |
| Amsted Indus. Inc. v. Buckeye Steel Castings Co., 24 F.3d 178 (Fed. Cir. 1994) | law.justia.com (F3/24/178) | Full text via case.dev | Actual notice requires affirmative communication of a specific charge of infringement by a specific accused product; infringer's knowledge irrelevant | 2026-10-30 |
| Crown Packaging Tech., Inc. v. Rexam Beverage Can Co., 559 F.3d 1308 (Fed. Cir. 2009) | law.justia.com (cafc 08-1284) | Full text via case.dev | Marking requirement does not apply when only method claims are asserted | 2026-10-30 |
| Fresenius USA, Inc. v. Baxter Int'l, Inc., 721 F.3d 1330 (Fed. Cir. 2013) | law.justia.com (cafc 12-1334) | Full text via case.dev | Cancellation of asserted claims in reexamination while the suit is pending eliminates the cause of action | 2026-10-30 |
| Ingenico Inc. v. IOENGINE, LLC, 136 F.4th 1354 (Fed. Cir. 2025) | law.justia.com (cafc 23-1367) | Full text via case.dev | 315(e)(2) "ground" means patents or printed publications; estoppel does not bar public-use or known-or-used grounds based on device art | 2026-10-30 |
| In re EchoStar Commc'ns Corp., 448 F.3d 1294 (Fed. Cir. 2006) | law.justia.com (F3/448/1294) | Full text via case.dev | Relying on advice of counsel waives privilege and work product on the same subject matter; in-house analysis conveyed to executives treated as legal opinion | 2026-10-30 |
| Knorr-Bremse Systeme Fuer Nutzfahrzeuge GmbH v. Dana Corp., 383 F.3d 1337 (Fed. Cir. 2004) (en banc) | law.justia.com (F3/383/1337) | Full text via case.dev | No adverse inference from invoking privilege or failing to obtain an opinion of counsel | 2026-10-30 |
| EcoFactor, Inc. v. Google LLC, 137 F.4th 1333 (Fed. Cir. 2025) (en banc) | cafc.uscourts.gov/opinions-orders/23-1101.OPINION.5-21-2025_2518737.pdf | Full text via case.dev | Rule 702 gatekeeping; per-unit royalty opinion from licenses not based on sufficient facts or data; new damages trial | 2026-10-30 |

## `[VERIFY]` list

| Statement | Why unconfirmed | What settles it |
|---|---|---|
| Whether the reference patent's own term adjustment counts in its "full statutory term" for a terminal disclaimer | MPEP 1490 and the form do not answer it directly | Federal Circuit authority and the disclaimer text |
| Scope of the 271(e)(1) safe harbor for research tools and post-approval activity | Statute read; Supreme Court and Federal Circuit decisions not read | Merck KGaA v. Integra and later authority |
| Whether Commil's invalidity-belief rule applies to 271(c) | Commil decided 271(b) | Later Federal Circuit or district authority |
| Whether the complaint alone supplies knowledge for post-filing inducement or willfulness | District courts differ | The forum's decisions |
| Situs of method steps or system use partly abroad | NTP and later situs cases not read | Federal Circuit authority |
| Limits and exceptions to the prior commercial use defense (35 U.S.C. 273(e)) | Subsections (a)-(c) read; (e) not analyzed | Full text of 273(e) and case law |
| Length of any term extension for a given patent (35 U.S.C. 156) | Patent-specific | USPTO extension record |
| Effect of a statutory disclaimer of a claim (253(a)) on pending suits and past damages | Statute read; case law not read | Federal Circuit authority |
| Marking when both method and apparatus claims are asserted | Crown addresses method-only assertions | Federal Circuit authority |
| Scope of advice-of-counsel waiver as to trial counsel | In re Seagate not read | Seagate and forum decisions |
| Whether a draft analysis is protected work product | Depends on anticipation of litigation and forum law | Forum authority and counsel's direction |
| Local patent rules and contention deadlines | Vary by district | The forum's local patent rules |
| Current status of any patent (fees, certificates, ownership) | Changes over time | USPTO Patent Center and assignment records on the date of the analysis |
