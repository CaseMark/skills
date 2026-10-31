# Claim Construction and Infringement Rules

Rules for construing claims and charting infringement of U.S. utility patents. Every rule carries the authority checked in the primary-sources register. A rule marked `[VERIFY]` is not settled by a source read for this skill; analyze both readings where it matters.

## Contents

1. Order of analysis
2. Claim construction (Phillips)
3. Means-plus-function and nonce terms (112(f), Williamson)
4. Literal infringement and the all-elements rule
5. Doctrine of equivalents and its limits
6. Who infringes: direct infringement, method claims and divided performance
7. Indirect infringement: inducement and contributory infringement
8. Where the act happens: territorial limits, 271(f) and 271(g)
9. Defenses that turn on the accused product's chain of title or its use
10. Evidence standards for the accused product

## 1. Order of analysis

1. Confirm the claim text in force (status file, original or certificate text).
2. Construe each disputed term from the intrinsic record before looking at the accused product. Construction is done once, for infringement and validity alike; never construe a term one way to read on the product and another way to avoid prior art.
3. Chart each limitation of each asserted claim against the accused product, literal first.
4. For any limitation not literally met, test equivalents only after checking every bar in section 5.
5. Identify the actor and place of each act (sections 6 to 8).
6. For indirect theories, prove a direct infringer first, then knowledge and intent.

A dependent claim includes every limitation of the claim it depends on. If the independent claim is not infringed, no claim depending on it is infringed.

## 2. Claim construction (Phillips)

Source: Phillips v. AWH Corp., 415 F.3d 1303 (Fed. Cir. 2005) (en banc); Thorner v. Sony, 669 F.3d 1362 (Fed. Cir. 2012).

- Words of a claim take their ordinary and customary meaning to a person of ordinary skill in the art at the time of the invention (the effective filing date), read in the context of the whole patent (Phillips, 415 F.3d at 1312-13).
- The claims are read in view of the specification, which is "the single best guide to the meaning of a disputed term" (Phillips, quoting Vitronics). The prosecution history is also intrinsic evidence.
- Do not confine claims to the embodiments. Phillips expressly rejects limiting claims to a single disclosed embodiment merely because it is the only one described (415 F.3d at 1323). The line between reading a claim in light of the specification and importing a limitation from it is drawn by asking how a skilled artisan would read the term.
- Only two exceptions displace plain meaning: the patentee acts as its own lexicographer by clearly setting out a different definition, or the patentee clearly disavows claim scope in the specification or during prosecution (Thorner). Words such as "preferred," "exemplary," or "in one embodiment," and statements that other means may be substituted, cut against disavowal.
- Statements by the patent owner in an inter partes review, before or after institution, can support prosecution disclaimer (Aylus Networks v. Apple, 856 F.3d 1353 (Fed. Cir. 2017)). Read the patent owner preliminary response, the response, and any reexamination or reissue arguments for every term in dispute.
- Extrinsic evidence (expert testimony, dictionaries, treatises) is less significant than the intrinsic record and cannot contradict it (Phillips).
- Claim differentiation: a limitation in a dependent claim suggests the independent claim lacks it. It is a guide, not a rule.

Record each construction in the construction table with the intrinsic support (column and line, prosecution paper and page) and the alternative construction the other side will urge. If the outcome on a limitation changes under the alternative, chart both.

## 3. Means-plus-function and nonce terms (112(f), Williamson)

Source: 35 U.S.C. 112(f); Williamson v. Citrix Online, 792 F.3d 1339 (Fed. Cir. 2015) (en banc in relevant part).

- An element "expressed as a means or step for performing a specified function without the recital of structure, material, or acts" covers only "the corresponding structure, material, or acts described in the specification and equivalents thereof" (112(f)).
- Absence of the word "means" creates a rebuttable presumption that 112(f) does not apply. Williamson overruled the characterization of that presumption as "strong." The test is whether the words of the claim are understood by persons of ordinary skill in the art to have a sufficiently definite meaning as the name for structure.
- Generic terms such as "module," "unit," "mechanism," "element," or "device" coupled with a function may be nonce words that operate like "means" ("distributed learning control module" in Williamson).
- When 112(f) applies: identify the claimed function; find the corresponding structure the specification clearly links to that function (for a computer-implemented function, the algorithm); then compare the accused structure for identity or equivalence. If no corresponding structure is disclosed, flag possible indefiniteness and hand validity to answer-with-invalidity-contentions; do not chart against an undefined function.
- Statutory equivalents under 112(f) are part of literal infringement and are narrower than the doctrine of equivalents. Keep the two analyses separate.

## 4. Literal infringement and the all-elements rule

Source: 35 U.S.C. 271(a); Warner-Jenkinson Co. v. Hilton Davis Chem. Co., 520 U.S. 17 (1997).

- Every limitation of the claim, as construed, must be found in the accused product or process. One missing limitation defeats literal infringement of that claim.
- Each element is material to defining the scope of the invention (Warner-Jenkinson, 520 U.S. at 28-30). Never chart the invention "as a whole," never merge two limitations into one row, and never skip a preamble or a "wherein" clause without deciding whether it limits.
- Chart each limitation in its own row with the specific evidence (document, page, figure, code file and line, test result) and an explanation of why the evidence meets the limitation. A conclusion without evidence is "Not determinable on current evidence."
- Chart each accused version or configuration separately when the evidence differs.

## 5. Doctrine of equivalents and its limits

Sources: Warner-Jenkinson, 520 U.S. 17; Festo Corp. v. Shoketsu Kinzoku Kogyo Kabushiki Co., 535 U.S. 722 (2002); Johnson & Johnston Assocs. v. R.E. Serv. Co., 285 F.3d 1046 (Fed. Cir. 2002) (en banc).

Test: the accused element must be equivalent to the claimed element, limitation by limitation. Function-way-result and insubstantial differences are both acceptable frameworks; the question is whether the accused product contains elements identical or equivalent to each claimed element. Equivalence and known interchangeability are judged at the time of infringement (Warner-Jenkinson).

Bars, checked in this order before any equivalents theory is offered:

| Bar | Rule | Source |
|---|---|---|
| Vitiation | Equivalents may not be applied so broadly as to eliminate an element in its entirety. If the theory reads the limitation out of the claim (for example, "non-metallic" met by metal), equivalents fail | Warner-Jenkinson, 520 U.S. at 28-30 |
| Amendment-based estoppel | A narrowing amendment made to satisfy any requirement of the Patent Act may give rise to estoppel. If the record does not explain the amendment, a patentability reason is presumed. The narrowing amendment is presumed to surrender the territory between the original and the amended claim | Warner-Jenkinson, 520 U.S. at 33 (presumption where the record is silent); Festo, 535 U.S. at 736, 740 |
| Rebuttal of the Festo presumption | Patentee bears the burden to show the equivalent was unforeseeable at the time of the amendment, the rationale of the amendment bears no more than a tangential relation to the equivalent, or some other reason the patentee could not reasonably have described it | Festo, 535 U.S. at 740-41 |
| Argument-based estoppel | Arguments made to the examiner surrender equivalents only where the prosecution history shows a clear and unmistakable surrender of subject matter; arguments are not presumed to surrender a whole range the way amendments are | Conoco, Inc. v. Energy & Envtl. Int'l, 460 F.3d 1349 (Fed. Cir. 2006) |
| Dedication-disclosure | Subject matter disclosed in the specification but not claimed is dedicated to the public and cannot be recaptured through equivalents | Johnson & Johnston (en banc) |
| Ensnarement | An equivalents range may not ensnare the prior art. Construct a hypothetical claim that literally covers the accused product and ask whether it would have been patentable over the prior art; a legal limit decided by the court, with the patentee bearing the burden of persuasion | DePuy Spine v. Medtronic Sofamor Danek, 567 F.3d 1314 (Fed. Cir. 2009), following Wilson Sporting Goods v. David Geoffrey & Assocs., 904 F.2d 677 (Fed. Cir. 1990) |

An equivalents position that clears every bar is stated as "Met under DOE only," never as literal infringement, and the per-claim label reflects the weaker footing.

## 6. Who infringes: direct infringement, method claims and divided performance

Sources: 35 U.S.C. 271(a); Akamai Techs. v. Limelight Networks, 797 F.3d 1020 (Fed. Cir. 2015) (en banc); Limelight Networks v. Akamai Techs., 572 U.S. 915 (2014); Centillion Data Sys. v. Qwest Commc'ns Int'l, 631 F.3d 1279 (Fed. Cir. 2011).

- Direct infringement of a method claim occurs only where all steps are performed by or attributable to a single entity (Akamai).
- Another party's performance is attributed to the accused entity in two situations: (1) the entity directs or controls the others' performance, including through an agent or by contract; or (2) the actors form a joint enterprise. Direction or control also exists when the entity conditions participation in an activity or receipt of a benefit on performance of a step and establishes the manner or timing of that performance (Akamai).
- A method claim is infringed by performing the steps, not by selling a product capable of performing them. Chart who performs each step and where.
- To "use" a claimed system under 271(a), a party must put the invention into service: control the system as a whole and obtain benefit from it. Physical control of every element is not required (Centillion).
- Build a step-by-actor table for every method claim and every system claim whose components are owned by different parties.

## 7. Indirect infringement: inducement and contributory infringement

Sources: 35 U.S.C. 271(b), (c); Global-Tech Appliances v. SEB S.A., 563 U.S. 754 (2011); Commil USA v. Cisco Sys., 575 U.S. 632 (2015); Aro Mfg. Co. v. Convertible Top Replacement Co., 377 U.S. 476 (1964); Limelight, 572 U.S. 915.

| Element | Inducement, 271(b) | Contributory, 271(c) |
|---|---|---|
| Direct infringement by someone | Required. No inducement liability where no one has directly infringed under 271(a) (Limelight) | Required |
| Knowledge | Knowledge of the patent and knowledge that the induced acts constitute patent infringement (Global-Tech; Commil) | Knowledge that the combination for which the component was especially designed was both patented and infringing (Aro, 377 U.S. at 488-93) |
| Willful blindness | Satisfies knowledge: the defendant subjectively believes there is a high probability a fact exists and takes deliberate actions to avoid learning it. Recklessness and negligence do not (Global-Tech) | Same knowledge standard (Global-Tech treats 271(b) and (c) alike) |
| Intent and conduct | Active inducement: intent to bring about the infringing acts | Sale, offer or import of a material component especially made or adapted for infringing use and not a staple article suitable for substantial noninfringing use |
| Not a defense | A good-faith belief that the patent is invalid (Commil) | Same reasoning applies `[VERIFY]` for 271(c) |

- Date the knowledge. Inducement and contributory exposure run only from the date knowledge is shown by evidence (notice letter, citation in prosecution, prior licensing talks, marking seen by the accused, or the complaint itself). Whether service of the complaint alone supplies knowledge for post-filing inducement is decided differently by district courts `[VERIFY]`; state both readings.
- Under 35 U.S.C. 298, failure to obtain or present advice of counsel may not be used to prove intent to induce.

## 8. Where the act happens: territorial limits, 271(f) and 271(g)

Sources: 35 U.S.C. 271(a), (f), (g); Microsoft Corp. v. AT&T Corp., 550 U.S. 437 (2007); Life Techs. Corp. v. Promega Corp., 580 U.S. 140 (2017); WesternGeco LLC v. ION Geophysical Corp., 585 U.S. 407 (2018).

- 271(a) reaches making, using, offering to sell or selling within the United States, or importing into the United States, during the term. Foreign manufacture and foreign sales are not 271(a) acts. Record the place of each act in the chart.
- 271(f)(1): supplying from the United States all or a substantial portion of the components of a patented invention, uncombined, in a manner that actively induces combination abroad. A single component of a multicomponent invention is not a "substantial portion" (Life Technologies).
- 271(f)(2): supplying from the United States a component especially made or adapted and not a staple article, knowing it is so made and intending combination abroad.
- Software: master software sent abroad from which foreign copies are made is not a supplied "component" for those copies (Microsoft v. AT&T). The presumption against extraterritoriality applies.
- 271(g): importing, or selling, offering or using in the United States, a product made abroad by a process patented in the United States, during the term. No 271(g) liability once the product is materially changed by later processes or becomes a trivial and nonessential component of another product.
- Where a 271(f) theory succeeds, foreign lost profits are a damages question for the damages expert (WesternGeco); hand off.
- Method claims practiced partly abroad and systems with servers abroad raise unsettled situs questions `[VERIFY]`; analyze each step's location.

## 9. Defenses that turn on the accused product's chain of title or its use

- Regulatory safe harbor: making, using, offering, selling or importing a patented invention solely for uses reasonably related to the development and submission of information under a federal law regulating drugs or veterinary biological products is not infringement (35 U.S.C. 271(e)(1)). Chart regulatory testing activity separately from commercial activity and flag it for counsel.

- Exhaustion: an authorized sale by the patentee or licensee exhausts patent rights in that item, regardless of post-sale restrictions, including authorized sales abroad (Impression Prods. v. Lexmark Int'l, 581 U.S. 360 (2017)). Ask where the accused components came from and whether any supplier is licensed.
- License and covenant scope: read any license, covenant not to sue, or settlement affecting the patent family before charting.
- Prior commercial use (35 U.S.C. 273): a defense for a process, or a machine, manufacture or composition used in a manufacturing or other commercial process, when the accused party in good faith commercially used the subject matter in the United States at least 1 year before the earlier of the effective filing date or a public disclosure qualifying under 102(b); proved by clear and convincing evidence (273(a)-(b)). Flag it for counsel; the limits and exceptions in 273(e) `[VERIFY]` were not analyzed.

## 10. Evidence standards for the accused product

Rank the accused-product evidence and record its rank in the evidence register:

1. Source code, schematics, engineering drawings, bills of materials, and the product itself (inspection, teardown, testing) for the version and date charted.
2. Technical documentation from the maker: data sheets, API references, service manuals, regulatory filings.
3. Admissions in pleadings, discovery responses, or deposition testimony.
4. Third-party technical reviews and teardowns (identify author and method).
5. Marketing material, websites, press releases and sales decks.

Marketing material alone is not enough to mark a limitation "Met literally." It can show what is sold and offered, and it can corroborate. When a limitation rests only on rank 5 evidence, label it "Not determinable on current evidence" and list the technical evidence that would decide it. When marketing and technical evidence conflict, the technical evidence for the charted version controls and the conflict goes in the reconciliation table.
