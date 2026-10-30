---
name: patent-infringement-analysis
language: en
description: >
  Drafts patent infringement and non-infringement analyses with element-by-element claim
  charts for U.S. utility patents, for the patent owner or accused party. Confirms the
  claim text in force after reexamination, IPR or reissue, patent term, terminal disclaimer
  and maintenance status; construes claims under Phillips from the claim language,
  specification and file history; tests 112(f) means-plus-function and nonce terms
  under Williamson; applies the all-elements rule; tests equivalents against vitiation,
  Festo prosecution history estoppel and dedication; charts method claims and
  divided infringement under Akamai; tests inducement and contributory infringement for
  knowledge under Global-Tech and Commil; checks 271(f) and (g) extraterritorial acts,
  the 286 six-year window, 287 marking, IPR estoppel and willfulness facts. Use for claim
  chart, infringement analysis, non-infringement position, design-around review or notice
  letter response. Not an opinion of counsel; routes damages to expert-report-on-damages.
tags:
  - litigation
  - analysis
  - memo
  - research
---

# Patent Infringement Analysis

Prepares a draft infringement or non-infringement analysis of asserted claims of a U.S. utility patent against an accused product or process: the claim text in force and the patent's term, claim constructions from the intrinsic record, a claim chart for each claim and accused version with a label for every limitation, the infringement theories with their actor, place and knowledge dates, the window in which infringement and damages can exist, and hand-offs. It works for the patent owner or the accused party and states adverse results plainly. Every output is a draft prepared at the direction of counsel for review by a registered patent practitioner or litigation attorney; it is never an opinion of counsel.

## Why This Skill Exists

Infringement analyses fail in predictable places. The analyst charts the claim printed on the patent when an IPR certificate canceled it, reads "fastener" as "screw" because the only drawing shows a screw, offers an equivalent the applicant gave up by amendment, charts a method claim against a company that performs only three of four steps, pleads inducement for years before the accused party knew of the patent, or marks a limitation met from a product brochure. Each error produces a position that collapses at claim construction, summary judgment or deposition, and some create willfulness and privilege exposure for the client. The work also carries consequences beyond the merits: a written analysis relied on as advice of counsel can open the client's privileged communications on the same subject, so this skill produces drafts for counsel and never a formal opinion.

## Where Mistakes Hide

| Input / Document | What It Is Used For | Where the Error Hides |
|---|---|---|
| Issued patent, reexamination and IPR certificates, reissue, certificates of correction | The claim text actually in force | Claim printed on the original patent charted after an IPR certificate canceled it or a reexamination certificate amended it; dependent claim charted without its parent's limitations; intervening rights for amended claims ignored |
| Filing history on the patent face, term adjustment, terminal disclaimers, maintenance fee record | Whether and when the patent is in force | Term counted from the continuation's own filing date instead of the earliest U.S. application it references; terminal disclaimer or lapsed maintenance fee not checked; infringement and injunctive relief analyzed for acts after expiration |
| Specification and drawings | Context for construing claim terms | Claim term limited to the preferred or only embodiment without lexicography or disavowal (Phillips; Thorner); "module" or "unit" claimed by function treated as structure without a Williamson test |
| Prosecution history, reexamination and IPR record | Disclaimer and estoppel | Narrowing amendment ignored when an equivalents theory recaptures the surrendered range (Festo); patent owner's IPR arguments ignored in construction (Aylus); disclosed but unclaimed alternative argued as an equivalent (Johnson & Johnston) |
| Claim chart rows | Element-by-element comparison | Two limitations merged into one row; a limitation skipped; equivalents stretched until the limitation is gone (Warner-Jenkinson vitiation); conclusion with no evidence citation |
| Accused-product evidence: source code, schematics, teardown, data sheets versus marketing | Proof of what the product does, by version | Limitation marked met from a brochure or website; versions or configurations merged; marketing claims contradicting the technical record not reconciled |
| Method claims and who performs each step | Identifying a direct infringer | Steps performed by customers or partners attributed to the accused party without an Akamai basis; inducement pleaded with no direct infringer (Limelight); "use" of a system assigned to a party that does not put it into service (Centillion) |
| Notice letters, prior dealings, citations in prosecution, internal emails | Knowledge for inducement, contributory infringement and willfulness | Indirect liability counted from first sale instead of the date of knowledge of the patent and of infringement (Global-Tech; Commil); belief in invalidity treated as a defense to inducement |
| Place of manufacture, sale, server location, export shipments | Territorial reach of 271 | Foreign manufacture or sale charted as 271(a) infringement; single exported component treated as a "substantial portion" under 271(f)(1) (Life Technologies) |
| Engagement, requester's side, assignment and license records, purpose of the written analysis | Who the client is, who owns and may enforce the patent, and what the document will be used for | Draft presented or requested as a formal opinion of counsel; request to reach a set conclusion or omit adverse facts; analysis run for a patent the client does not own or for products already licensed or exhausted (Impression Products) |

## Ground Rules

1. **Draft only.** Nothing is sent to the other side, filed, or given to a business recipient for reliance. Every output is a draft prepared at the direction of counsel for attorney review, and it is never called final or an opinion of counsel.
2. **Source-review gate.** Never call a document missing until the matter inventory has been checked and the file opened, with OCR or extraction tried. Classify every open item as one of four gap classes: *unknown fact* (the date the accused party learned of the patent), *source conflict* (the brochure and the schematic describe different seals), *unverified external lookup* (maintenance fee status not yet confirmed on Patent Center, or a rule not in `references/primary-sources.md`), or *policy election* (whether to assert equivalents, whether to seek an opinion of counsel).
3. **Hierarchy of authority.** For claim text: the latest certificate, then the issued patent, then the published application. For construction: claim language, then specification, then prosecution, reexamination and IPR record, then extrinsic evidence. For the accused product: the ranked evidence in `references/claim-construction-and-infringement-rules.md`, section 10, with source code, schematics and inspection first and marketing last. For law: statute and Supreme Court, then en banc and panel Federal Circuit decisions, then district decisions, then commentary. Name every conflict in the reconciliation table and state which source controls; never resolve one silently.
4. **Citation discipline.** Every claim quotation carries its locator (column and line, or certificate page); every fact about the accused product carries an evidence locator and rank, or `[UNVERIFIED]`. Every legal statement carries a citation from `references/primary-sources.md` or `[VERIFY]`. Re-read the current text of each statute relied on. Never invent a case, pin cite, claim text, patent number or document.
5. **Know the client and the purpose first.** Record whose side the client is on, who asked, and what the analysis is for. Do not draft, sign, or format the analysis as a formal opinion of counsel, and do not address it for reliance by business people; that is counsel's own work and decision. Treat privilege and distribution as counsel directs.
6. **Objective analysis, not a set conclusion.** State the evidence and authority on both sides, including what is adverse to the client. Decline a request to reach a stated conclusion regardless of the analysis or to omit known material facts (such as internal copying statements) or controlling authority; offer the complete draft instead.
7. **Claim text in force, during the term.** Confirm each asserted claim's status and the patent's term before charting. Never chart a canceled claim as asserted or count acts after expiration as infringement.
8. **Construction from the intrinsic record.** Construe from the claim language read in light of the specification and prosecution history. An embodiment, even the only one, does not limit a claim without clear lexicography or disavowal. Use one construction for infringement and validity.
9. **All elements, one row each.** Every limitation gets its own row, its own evidence and one label. One "Not met" limitation defeats literal infringement of that claim and of every claim depending on it.
10. **Equivalents only after the bars.** Before offering "Met under DOE only," check vitiation, amendment-based estoppel and its rebuttal, argument-based estoppel and dedication-disclosure, and show the check.
11. **A direct infringer, a place and a date.** Every theory names the direct infringer and the basis for attributing each step; every act has a place; every indirect theory has a dated knowledge showing.
12. **Damages stay with the damages expert.** Report the damages window, notice and marking facts only; route amounts, royalty rates and lost profits to expert-report-on-damages.

## Checkpoint A: Pre-Draft Intake (Mandatory)

Collect, from documents where possible:

1. Today's date; the client, its side, the requester's role and the purpose of the analysis.
2. The patent(s), asserted claims (independent and dependent), and the full claim text.
3. The file history, every reexamination, IPR, reissue and correction certificate, and any IPR papers.
4. Term data: filing dates and continuity data on the face of the patent, term adjustment, terminal disclaimers with their reference patents, maintenance fee status, and ownership (assignment records).
5. The accused products or processes, each version and configuration, and dates of first U.S. sale, import or use.
6. Accused-product evidence by rank: source code, schematics, teardown or inspection results, technical documents, admissions, marketing.
7. Who performs each step of each method claim and where; where products are made, sold, shipped and serviced; any servers abroad.
8. Knowledge evidence: notice letters (date, patent and products named), prior dealings, citations of the patent, internal communications.
9. Licenses, covenants, settlements and supplier relationships affecting the accused products; the patentee's and licensees' marking practice.
10. Any pending or planned litigation, its filing date, and service dates on the accused party.

**Defaults if not supplied** (a statute or certificate overrides any default it addresses): claim status "Status unconfirmed" and a USPTO check listed as an unverified external lookup; terms given ordinary meaning with the alternative construction charted where a dispute is foreseeable; accused-product facts from marketing alone labeled "Not determinable on current evidence"; knowledge date for indirect theories set at the earliest documented notice naming the patent, not the first sale; planned filing date assumed to be today for the 286 window, labeled as an assumption; analysis status no better than "Ready subject to listed confirmations."

**Hard stops (label the analysis status "Declined: hard stop"; produce the request, routing or alternative, not the requested analysis):**
- No claim language for any asserted claim (only a patent number, title or summary) and no way to obtain the patent text: produce the document request.
- No information about the accused product or process beyond its name: produce the evidence request and the list of limitations to investigate.
- A request to issue, sign or format the analysis as a formal opinion of counsel, to reach a fixed conclusion regardless of the analysis, or to omit known material adverse facts or controlling authority: decline that version, explain why, and offer the complete draft analysis for counsel.
- The patent is a design patent, plant patent or non-U.S. patent: route to legal-research, which handles it as a research question; no dedicated skill exists.

**Not hard stops:** missing file history (Critical item; constructions marked provisional); marketing-only evidence (limitations "Not determinable on current evidence"); expired patent (analyze the past window only); damages questions (hand off).

## Step 1: Client, Purpose and Privilege Posture

Record the client, side, requester and purpose in the header of `references/output-template.md`. Read `references/patent-status-remedies-and-privilege.md`, sections 6 and 7, before writing anything about willfulness or advice of counsel. Apply the hard stops. Note any licensed or exhausted supply chain under `references/claim-construction-and-infringement-rules.md`, section 9.

## Step 2: Claim Text in Force and Patent Term

Read `references/patent-status-remedies-and-privilege.md`, sections 1 to 3. Fill the claim status table and the term computation in Part 2 of `references/output-template.md`, each element from its own trigger. A canceled claim, an expired patent or an unenforceable period is a Critical item and narrows everything that follows.

## Step 3: Assemble the Intrinsic Record

List every specification passage, prosecution paper, reexamination paper and IPR paper bearing on each claim term, with locators. Mark amendments and arguments made to overcome prior art; they feed both construction and the equivalents bars.

## Step 4: Construe the Disputed Terms

Read `references/claim-construction-and-infringement-rules.md`, sections 2 and 3. Fill the construction table in Part 3. Test each functional term for 112(f) under Williamson. Where lexicography or disavowal is claimed, quote it; where it is absent, say so. Chart the alternative construction when the result would change.

## Step 5: Build the Accused-Product Evidence Register

Read `references/claim-construction-and-infringement-rules.md`, section 10. Fill Part 4 by version. Reconcile marketing statements against technical evidence in the reconciliation table.

## Step 6: Chart Literal Infringement

Read `references/claim-construction-and-infringement-rules.md`, section 4. Chart every limitation of every asserted claim for each version in Part 5, with evidence and reasons, and assign one limitation label.

## Step 7: Test Equivalents

Read `references/claim-construction-and-infringement-rules.md`, section 5. For each limitation not met literally, run the bars table first. Offer "Met under DOE only" only when every bar is cleared, and state the weaker footing.

## Step 8: Actor, Place and Knowledge

Read `references/claim-construction-and-infringement-rules.md`, sections 6 to 8. Build the step-by-actor table for method and multi-party system claims, decide attribution, record the place of each act, and date the knowledge for each indirect theory. Fill Part 6.

## Step 9: Remedy Windows, Willfulness Facts and Validity Hand-off

Read `references/patent-status-remedies-and-privilege.md`, sections 3 to 6 and 8. Compute the damages window from its triggers; record marking and notice facts and willfulness facts in Part 7. Record each IPR and reexamination, and any 315(e) estoppel, in the IPR register in Part 2, and hand validity questions to answer-with-invalidity-contentions or notice-of-prior-art.

## Step 10: Positions and Assembly

Assign one claim-position label per claim and version and the analysis status from `references/output-template.md`, Part 1. Rank blocking issues, complete the reconciliation table, hand-offs, open items and the `[VERIFY]` list, and close with the template's closing line.

## Checkpoint B: Post-Draft Alignment

Confirm with the user or list as open items:

1. Are the client's side and the purpose correct, and has counsel decided how the draft will be held and distributed?
2. Has the claim text in force been confirmed against the USPTO record for each asserted claim?
3. Does counsel accept the constructions, including the alternatives charted?
4. Is each limitation marked met supported by evidence of rank 1 to 3 for the version charted?
5. Are the knowledge dates and the planned filing date confirmed?

If the user does not answer, recommend confirming the claim text in force and obtaining technical evidence for every limitation resting on marketing; those are the most common reasons an infringement position fails later.

## Quality Audit

Before responding, confirm each statement. If one fails, fix the draft.

1. The client, side, requester and purpose are stated, and the draft is labeled a draft for attorney review, not an opinion of counsel.
2. Every asserted claim has a status label, and no canceled claim is charted as asserted.
3. The term is computed from the earliest referenced U.S. filing date with adjustment, terminal disclaimer and maintenance status checked, each from its own trigger.
4. Every construction cites intrinsic evidence, and no term is limited to an embodiment without quoted lexicography or disavowal.
5. Every functional term without "means" was tested under Williamson, and every 112(f) term names its corresponding structure.
6. Every limitation has its own row, evidence locator, evidence rank and exactly one limitation label.
7. No limitation is "Met literally" on marketing evidence alone.
8. Every "Met under DOE only" shows the vitiation, estoppel and dedication checks.
9. Every method claim has a step-by-actor table and an attribution basis, and every indirect theory names a direct infringer.
10. Every indirect theory has a dated knowledge showing of the patent and of infringement.
11. The place of each accused act is stated, and no foreign act is charted under 271(a).
12. The damages window uses 286 from the filing date and 287 from notice, and no damages amount appears.
13. Every legal statement cites `references/primary-sources.md` or carries `[VERIFY]`, and adverse facts and authority are included.

## Guidelines

- Write as if the other side and the court will read the draft later. Explain why each limitation is or is not met; a label without reasons is not an analysis.
- Be definite where the evidence and law allow and say what would change the answer where they do not. "Contested: both positions arguable" is a finding when the result turns on a disputed construction.
- Keep infringement and validity separate. A strong invalidity argument does not make a limitation unmet, and belief in invalidity does not negate inducement knowledge.
- Do not tailor a construction to the product. If the client's preferred construction would also read on prior art, say so.
- For design-around reviews, chart the redesigned version as its own version and identify the limitation it avoids; flag equivalents risk on that limitation.
- When an instruction conflicts with a statute or controlling decision (charting a canceled claim, counting inducement from first sale), draft the compliant version and explain the change.

## Troubleshooting

| Problem | Likely cause | What to do |
|---|---|---|
| File history pages unreadable or missing | Image-only download or partial wrapper | Try OCR; list missing papers; mark constructions that depend on them provisional; request the full wrapper |
| Claim text differs between sources | Certificate not in the file, or a database copy of the original claims | Use the latest certificate; record both in the reconciliation table; mark the claim "Status unconfirmed" until the USPTO record is checked |
| Accused product has several versions | Rolling releases or regional variants | Chart each version separately; date each evidence item; request version history |
| Only marketing material available | Pre-suit stage, no product access | Label affected limitations "Not determinable on current evidence"; list inspection, purchase, teardown or code review needed |
| Marketing and technical evidence conflict | Promotional wording, or a different version | Technical evidence for the charted version controls; record the conflict |
| Steps performed by several parties | Customer, partner or cloud provider performs some steps | Build the step-by-actor table; test Akamai attribution; do not plead inducement without a direct infringer |
| Knowledge date unclear | Letter named the patent family but not the patent or product | Use the earliest document naming the patent; record the gap; show the result under each date |

## Related Skills

- expert-report-on-damages: hand off any royalty, lost profits or damages amount; pass the window, notice, marking, knowledge and place-of-act findings.
- claim-construction-chart: hand off when counsel needs a joint claim construction chart for a Markman submission.
- answer-with-invalidity-contentions: hand off validity defenses and invalidity contentions for a defendant's answer.
- notice-of-prior-art: hand off prior art disclosure or an IPR petition, with the 315(b) bar date.
- patent-infringement-complaint: hand off when the patent owner decides to file suit on supported claims.
- preservation-letter: hand off evidence preservation for accused-product versions and knowledge documents.
- ip-infringement-analysis: hand off trademark, copyright and trade secret questions.
- legal-research: hand off design, plant and foreign patents and forum-specific rules; no dedicated skill exists for those.

## Reference Files

- `references/claim-construction-and-infringement-rules.md`: order of analysis, Phillips construction, 112(f) and nonce terms, all-elements rule, equivalents and its bars, divided infringement, indirect infringement knowledge, territorial reach, exhaustion, evidence ranking.
- `references/patent-status-remedies-and-privilege.md`: claim version after certificates, term and terminal disclaimers, clocks table, 286 and 287 window, IPR record and estoppel, willfulness and advice of counsel, privilege, damages hand-off.
- `references/output-template.md`: deliverable layout, status, claim-status, limitation and claim-position labels, construction table, evidence register, claim charts, theories table, reconciliation table, hand-off table.
- `references/primary-sources.md`: every authority checked with its URL, method, what it supports and the date checked, plus the `[VERIFY]` list.
