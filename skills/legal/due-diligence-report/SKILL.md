---
name: due-diligence-report
language: en
description: >-
  Drafts legal due diligence reports for M&A and financing transactions, in
  red-flag and full-form versions, from a virtual data room: source-review
  register, findings matrix rated Critical, Significant, Moderate or Minor,
  consents table, and reconciliation of seller summaries to executed contracts
  and amendments. Checks the data room index and Q&A log before calling a
  document missing; tests change-of-control and anti-assignment clauses
  against the deal structure (stock purchase, reverse triangular merger,
  asset purchase); flags exclusivity, MFN and non-compete clauses binding the
  buyer's affiliates; reviews IP chain of title and open source, WARN Act
  aggregation, misclassification, litigation and regulatory exposure, UCC
  lien searches against the debt schedule, aggregated sub-threshold risk, and
  privilege and clean teams. Use for diligence report, red flag memo, legal
  due diligence, target review or data room review. Routes gun-jumping to
  hsr-filing and findings to disclosure-schedules and merger-agreement.
tags:
  - transactional
  - corporate
  - analysis
  - memo
---

# Legal Due Diligence Report

Prepares a legal due diligence report on a target business for an acquisition, investment or financing: a red-flag report limited to Critical and Significant findings, or a full-form report covering every area in scope. The deliverable is a determination label, a source-review register, a rated findings matrix, area analyses, a consents and closing-deliverables table, a reconciliation of summaries to executed documents, open items, and hand-offs to the drafting workflows. Every finding traces to a document in the data room or is marked as open. Everything it produces is a draft for review by a qualified attorney.

## Why This Skill Exists

A diligence report is relied on to price the deal, write the disclosure schedules and decide which consents, indemnities and closing conditions the agreement needs. Its errors are rarely about law the reviewer did not know. They come from the review process: a contract called missing that sat in a misnamed folder, a seller summary trusted over the signed amendment, a consent analysis done for a merger when the deal became an asset purchase, a non-compete that will bind the buyer's other companies, a layoff plan split into rounds that each fall under 50, or a lien search run in the headquarters state instead of the state of organization. This skill builds the checks for those failures into the workflow.

## Where Mistakes Hide

| Input / Document | What It Is Used For | Where the Error Hides |
|---|---|---|
| Data room index, Q&A log, late-upload and miscellaneous folders | Locating each document before any gap finding | Document reported missing without searching the whole index by counterparty name or reading the Q&A answer; scanned file under a generic name never opened; image-only PDF never run through OCR; partly unreadable file called missing instead of "Unreadable after attempt" |
| Seller contract summary, CIM, index descriptions, draft disclosure schedules | A map of what to read, never the finding itself | Summary's "no change of control" repeated in the report while an executed amendment added a termination right; unsigned draft or form read as the executed contract; side letters and SOWs that change the master terms not requested |
| Assignment, change-of-control and consent clauses, with the deal structure | The consents table and closing conditions | Merger reasoning applied to an asset deal or the reverse; "by operation of law" read without the governing law (Meso Scale under Delaware law, SQL Solutions under California law `[VERIFY]`); express change-of-control clause missed because the deal "assigns nothing"; federal contract transferred without novation; in-licensed patent treated as freely transferable |
| Entity chart, signing entity on each contract, record owner of IP and permits | Defining the perimeter of what the buyer receives | Key contract, lease or license signed by a parent, sister company or founder outside the perimeter and assumed to come with the target; registrations held in a founder's name; subsidiaries left out of the review |
| Exclusivity, non-compete, non-solicit and MFN clauses binding "Affiliates" | Post-closing restrictions on the buyer group | Covenant read only for the target, while the control-based Affiliate definition will reach the buyer and, for a fund buyer, every portfolio company under common control; MFN that will compare the buyer group's pricing |
| Scope letter materiality threshold | Deciding which contracts get a full read | Per-contract revenue threshold applied to skip contracts that share the same change-of-control termination right and together exceed it, or to skip a covenant whose exposure is the buyer group's revenue, not the contract's |
| Invention assignment agreements, contractor agreements, code contributor lists, open-source scan | IP chain of title | "Agree to assign" language treated as a present assignment; contractor-written software treated as work made for hire without a signed assignment; patent assignments not recorded; AGPL or GPL components in distributed or network-served products unreported |
| Employee census by site with hours and hire dates, buyer's integration plan | WARN Act screen and employee liabilities | Each reduction round tested alone though rounds within 90 days aggregate; part-time employees counted in the 33 percent denominator; seller-versus-buyer notice duty at closing ignored; notice date taken from closing instead of each group's first termination |
| Contractor roster, 1099 list, staffing agency agreements | Misclassification exposure | Long-term, full-time contractors doing core work accepted as contractors without the governing classification test; the same people's IP assignments not checked |
| Seller litigation list, docket searches, demand letters, regulator correspondence, consent orders | Litigation and regulatory exposure | Only filed suits reported; threatened claims in correspondence and open regulatory inquiries missed; continuing obligations under consent orders or settlements not carried forward; exposure figures invented instead of quoted |
| UCC, judgment and tax lien search reports, debt schedule, payoff letters | Indebtedness, liens and closing deliverables | Search run in the headquarters state rather than the state of organization; filings not reconciled to the debt schedule (merchant cash advance, equipment finance); lapsed filing reported as either a live lien or proof of repayment |
| Permits, licenses and regulatory authorizations; buyer's foreign ownership | Regulatory approvals and closing conditions | License treated as staying with the target in a stock deal though the regulator must approve a transfer of control (FCC licenses, 47 U.S.C. 310(d)); state license approvals not listed; foreign-person buyer of a TID U.S. business not screened for a mandatory CFIUS declaration (31 C.F.R. 800.401) |
| Privileged legal memos and customer-level pricing in the data room | Privilege preservation and antitrust compliance | Privileged memos produced without a common-interest basis; no privilege carve-out flagged for a merger; competitively sensitive data sent to buyer personnel outside the clean team, a gun-jumping risk routed nowhere |

## Ground Rules

1. **Draft only.** The report is a draft for attorney review. It is not sent to the client, a lender, an insurer or the other side by this skill, and it never states that diligence is complete without that review.
2. **Source-review gate.** Never call a document missing until the index has been searched by counterparty name, the Q&A log read, the candidate file opened, and OCR or extraction tried. Classify every open item as one of four gap classes: *unknown fact* (headcount at a site on the snapshot date), *source conflict* (summary versus executed amendment), *unverified external lookup* (a docket, lien or registry search not yet run), or *policy election* (a choice for the client, such as the materiality threshold or whether to seek a consent).
3. **Hierarchy of authority.** For facts: executed agreements and their executed amendments, then official records (filing office searches, dockets, registries), then seller certificates and Q&A answers, then summaries, indexes, the CIM and management statements. For law: current statute and regulation text, then controlling cases, then agency guidance and commentary. Name every conflict in the reconciliation table and state which source controls; never resolve one silently.
4. **Citation discipline.** Every finding carries a source locator (index number, document, section, page, date) or is marked `[UNVERIFIED]`. Every legal statement carries a citation from `references/primary-sources.md` or is marked `[VERIFY]`. Never invent a document, clause, case, statute or exposure figure.
5. **Client, side and perimeter first.** Identify the client, its side (buyer, seller, investor, lender) and the entities being acquired. Test every contract, permit, IP registration and lease against the perimeter; anything held outside it is labeled "Outside the deal perimeter", not assumed to transfer.
6. **Consents follow the structure.** Analyze each consent clause against the deal structure and the contract's governing law, using the outcome labels in `references/contract-and-ip-review.md`, section 4, and state what changes if the structure changes. "It is a merger, so nothing is assigned" is never a complete answer.
7. **Read covenants for whom they bind after closing.** Every exclusivity, non-compete, non-solicit and MFN clause is tested against the buyer group under the contract's Affiliate definition. Where the reach of "Affiliates" is unsettled, present both readings.
8. **Thresholds are policy elections, not blind spots.** Apply the client's materiality threshold, aggregate contracts that share a risk term, and do not use a revenue threshold to screen out covenants binding the buyer group or statutory triggers. Report a hidden aggregate as a finding.
9. **Statutory screens run on their own terms.** WARN headcounts and similar statutory tests are computed with the statute's own definitions and windows, with the arithmetic shown; they are never filtered by the deal's materiality threshold. HSR thresholds and waiting periods are hsr-filing's to compute.
10. **Liens are reconciled, not assumed.** Search where the law locates the debtor, reconcile every filing to the debt schedule, and treat lapse as loss of perfection, not proof of payment.
11. **Privilege and clean teams.** Flag privileged material in the data room and the privilege position after closing. Never route competitively sensitive information to people outside the clean team; route any gun-jumping or information-exchange concern to hsr-filing.
12. **Report what the documents show.** Never omit, soften, re-rate or move a finding so that a lender, R&W insurer, buyer, regulator or court will not see it, and never describe a document as reviewed when it was not. State exposure only as the source states it; no invented probabilities or dollar ranges.

## Checkpoint A: Pre-Draft Intake (Mandatory)

Collect, from documents where possible:

1. Today's date, the data room cut-off date, and the report type (red-flag or full-form).
2. The client, its side, and any other recipients the report will reach (lender, R&W insurer).
3. Transaction structure (stock purchase, reverse triangular merger, forward merger, asset purchase, minority investment, financing), the latest LOI or term sheet, and target entities in the perimeter.
4. Data room access and the full index; the Q&A log; any seller summaries.
5. Scope letter: areas in scope, materiality threshold, key customers and suppliers, regulatory approvals expected.
6. Buyer's post-closing plans that create legal triggers: site closures, reductions, integration of sales teams, rebranding.
7. Buyer group information needed for covenant review: parent, funds, and portfolio companies in the target's field.
8. Clean-team agreement, confidentiality agreement, and any common-interest agreement.
9. Search reports already ordered (UCC, judgment, tax lien, litigation, IP registries) with jurisdictions and dates.

**Defaults if not supplied:** red-flag report; materiality threshold of contracts with annual value of at least 1 percent of target revenue, plus every contract containing a change-of-control, assignment, exclusivity, non-compete, MFN or uncapped indemnity term regardless of value (statutory triggers such as WARN and HSR apply on their own terms and override any threshold); structure unknown means the consents table analyzes both a reverse triangular merger and an asset purchase; general report version without customer-level or price-level detail.

**Hard stops (label the determination "Declined: hard stop" and produce only what each one names):**
- The client or its side is unknown: produce the intake questions only.
- No index, no documents and no access to the data room: produce a supplemental request list (hand to due-diligence-checklist), not a report.
- A request to omit, soften, re-rate or relocate a known adverse finding so that a lender, R&W insurer, buyer, regulator or court will not see it, or to describe unreviewed documents as reviewed: decline that version and offer the accurate report.
- A request to send competitively sensitive information (customer-level pricing, costs, strategic plans) to buyer personnel outside the clean team, or to coordinate operations before closing: decline that distribution, produce the general version, and route the issue to hsr-filing.

**Not hard stops:** a partial data room (use "Scope-limited: index or summary review only" or "Issued subject to listed open items"); unknown structure (analyze both); a missing threshold (use the default); unreadable files (classify and request clean copies).

## Step 1: Fix Scope, Perimeter and Structure

Read `references/output-template.md`, Header. Record the client and side, structure, perimeter entities, report type, threshold and who set it, and the report version. List every target entity and its state of organization; these drive the lien searches in Step 8.

## Step 2: Build the Source-Review Register

Read `references/contract-and-ip-review.md`, sections 1 and 2. Register each in-scope document with its status label. Before any document is reported missing, run the five-check protocol and record the searches. Mark every seller summary "Reviewed: summary only (not relied on)" and use it as a map only.

## Step 3: Corporate and Capitalization

Review charter, bylaws, minutes, equity ledger, option plan and grants, stockholder agreements, and subsidiary documents. Reconcile the cap table to issuance approvals. Note drag-along, preemptive and consent rights that affect the deal mechanics, and any approval the structure requires.

## Step 4: Material Contracts, Consents and Covenants

Read `references/contract-and-ip-review.md`, sections 3 to 6, before reading the contracts. For each in-scope contract and each executed amendment: record the signing entity, the governing law, assignment and change-of-control terms, term and termination, exclusivity, MFN, non-compete and non-solicit terms, and pricing commitments. Fill the consents table with one outcome label per contract. Test each covenant against the buyer group. Aggregate sub-threshold contracts that share a risk term.

## Step 5: IP and Technology

Read `references/contract-and-ip-review.md`, sections 7 and 8. Check the operative assignment words in every employee and contractor agreement, contractor-written code and its assignments, record ownership and recordation of registrations, in-licenses of core technology, and the open-source scan.

## Step 6: Employment, Benefits and WARN

Read `references/employment-liens-and-privilege.md`, sections 1 to 3. If any reduction or closure is planned or occurred in the last 90 days, run the WARN screen by site with the arithmetic shown for each 30-day and 90-day window, identify who gives notice, and compute each group's notice date from its own first termination. Review key employee agreements, change-in-control payments, contractor classification and benefit plans.

## Step 7: Litigation, Regulatory and Other Areas

Read `references/employment-liens-and-privilege.md`, section 5. Compare the seller's litigation list with docket searches and correspondence. Cover permits and licenses (regulator consent to a change of control and CFIUS screening per `references/contract-and-ip-review.md`, section 3), regulatory correspondence and consent orders, privacy and cybersecurity, real estate, environmental and insurance to the extent in scope. Quote exposure as the source states it.

## Step 8: Indebtedness and Liens

Read `references/employment-liens-and-privilege.md`, sections 1 and 4. Confirm each search was run in the state of organization under the exact registered name, plus local searches where needed. Reconcile every filing to the debt schedule; compute each filing's lapse date from its own filing date; list payoff letters, terminations and releases as closing deliverables.

## Step 9: Privilege and Clean-Team Check

Read `references/employment-liens-and-privilege.md`, section 6. Record privileged material in the data room, whether a common-interest basis exists under the governing law, and whether the agreement needs a privilege carve-out. Confirm which findings rely on clean-team material and prepare the version split. Record target overlaps found in diligence (products, services, customers or geographies where the target and the buyer group both compete) and any gun-jumping or information-exchange issue, and hand both to hsr-filing; Item 4(c) and 4(d) document collection, custodians and Item 8 prior acquisitions stay with that skill.

## Step 10: Rate, Reconcile and Assemble

Lay out the report per `references/output-template.md`. Rate each finding, assign a gap class to each open item, complete the reconciliation table, choose the determination label, and complete each hand-off with the facts the receiving workflow needs. List every `[VERIFY]` item with what would settle it, drawing on `references/primary-sources.md`.

## Checkpoint B: Post-Draft Alignment

Confirm with the user or state as open items:

1. Is the structure in the report the structure in the latest draft agreement? If it changed, has the consents table been rerun?
2. Does the client accept the materiality threshold given the aggregated findings?
3. Are the buyer group's businesses in the covenant analysis complete and current?
4. Are the post-closing reduction plans and dates final enough to support the WARN analysis?
5. Who will receive the report, and does that recipient list require a general version or raise privilege concerns?

If the user does not answer, recommend confirming the structure, the recipient list and the buyer group first; those change the most findings.

## Quality Audit

Before responding, confirm each statement. If one fails, fix the report.

1. The determination label is one of the four in `references/output-template.md`, and it matches the open items.
2. No document is called missing unless its register status is "Not located after index and Q&A check" with the searches named.
3. No finding rests on a seller summary, index description or draft; every summary-versus-executed conflict appears in the reconciliation table.
4. Every contract in the consents table has one outcome label, its clause locator, governing law, the structure assumed and what changes if the structure changes.
5. Every contract, lease, license and registration held outside the perimeter is labeled as such.
6. Every restrictive covenant and MFN was tested against the buyer group, with both readings where the Affiliate definition is unsettled.
7. Sub-threshold contracts that share a risk term were aggregated, and the total is stated against the threshold and target revenue.
8. The WARN analysis, where triggered, excludes part-time employees from numerator and denominator, shows every 30-day and 90-day window, names who gives notice, and dates each group's notice from its own first termination.
9. IP findings check operative assignment language, contractor code, recordation and copyleft components.
10. Lien findings rest on a search in the state of organization, every filing is reconciled to the debt schedule, and lapsed filings are described as unperfected rather than paid.
11. Privilege, clean-team and gun-jumping issues are flagged and routed to hsr-filing where they arise.
12. Every finding has a source locator or `[UNVERIFIED]`; every legal statement has a citation from `references/primary-sources.md` or `[VERIFY]`; no exposure figure is invented.
13. No finding was omitted, softened or re-rated for its audience, and the report closes with the draft-for-attorney-review line.

## Guidelines

- Separate facts (what the document says) from analysis (what it means for the deal) from recommendations (what to do about it).
- Keep a neutral tone. The report is read later by people deciding whether the buyer knew of a problem.
- Quote only the operative words of a clause; cite it so a reader can find it in seconds.
- Assume a U.S. transaction unless told otherwise and call out any non-U.S. entity, contract or law.
- Do not confirm regulatory approvals, consents or searches without the document that shows them.
- A finding that would change the price, structure or signing timeline goes in the executive summary, whatever its area.

## Troubleshooting

| Problem | Likely cause | What to do |
|---|---|---|
| Document listed in the summary but not where expected | Late upload under a generic file name, or a Q&A answer pointing elsewhere | Run the five-check protocol; if still not found, label it "Not located after index and Q&A check" and request it with the searches named |
| Scanned contract partly unreadable after OCR | Image-only or low-quality scan | Report the readable pages; label the file "Unreadable after attempt" with the page range; request a clean copy; do not rate terms that sit only on unreadable pages |
| Summary and executed contract disagree | Summary outdated or prepared from the base agreement only | Executed document and latest executed amendment control; record the conflict; flag the summary as unreliable for the rest of the set |
| Structure changes mid-diligence | Tax, consent or liability considerations | Rerun the consents table for the new structure; note which outcome labels changed |
| Contract governed by non-Delaware law with a "by operation of law" clause | Unsettled treatment of mergers under that law | Label "Judgment call: governing law unsettled", recommend consent for key contracts, and add a `[VERIFY]` item |
| Lien search came back clean in the headquarters state | Search run in the wrong jurisdiction for a registered organization | Order the search in the state of organization under the exact registered name before reporting no liens |
| Seller refuses to produce customer-level pricing | Antitrust caution or competitive concern | Propose clean-team access or aggregated data; route to hsr-filing; record as an open item, not a missing document |
| Headcount data lacks hours or hire dates | Census prepared for payroll, not WARN | Request average hours and hire dates by site; mark the WARN analysis open with the gap class unknown fact |

## Related Skills

- due-diligence-checklist: preparing the request list before review or a supplemental request list for gaps.
- due-diligence-summary: a short decision-ready summary rated High, Medium or Low, when the user wants a summary for a board or committee rather than this skill's full red-flag or full-form report with source-review register, consents table and reconciliation.
- disclosure-schedules: turning findings into exceptions to the representations, with source locators.
- merger-agreement: drafting special indemnities, escrows, closing conditions, definitions (Indebtedness, Permitted Liens, Affiliate) and a privilege carve-out from the findings.
- hsr-filing: target overlaps and gun-jumping or information-exchange issues found in diligence are handed there; premerger notification, thresholds, Item 4(c) and 4(d) custodian collection and Item 8 stay with that skill.
- analyzing-m-and-a-tax-implications: tax audits and open tax matters found in diligence, and structure changes that alter tax treatment.
- legal-research: payroll-tax and classification exposure from misclassified workers; no dedicated skill exists for it.
- consent-letter: drafting the consent and notice requests for contracts labeled Consent required or Notice only.
- contract-abstracts: abstracting individual contracts in detail when the report needs more than the finding.
- ip-assignment: confirmatory assignments to close chain-of-title gaps.

## Reference Files

- `references/contract-and-ip-review.md`: data room source-review protocol, document hierarchy, consent analysis by deal structure, permits and CFIUS, outcome labels, restrictive covenants and Affiliates, materiality aggregation, IP chain of title, open source.
- `references/employment-liens-and-privilege.md`: timed elements and triggers, WARN screen, worker classification and benefits, UCC and lien searches, litigation and regulatory review, privilege, common interest and clean teams.
- `references/output-template.md`: report layout, determination labels, source-review register, findings matrix, consents table, reconciliation table, open items, hand-offs and deal protection mapping.
- `references/primary-sources.md`: every authority checked with its source, what it supports and the date checked, plus the `[VERIFY]` list.
