# Schedule Drafting Rules

## Contents

1. Mapping the agreement to the schedules
2. General terms (preamble) provisions and each side's position
3. The description standard
4. Cross-references and the "reasonably apparent" clause
5. Knowledge, materiality and threshold qualifiers
6. Admissions, privilege and confidentiality
7. Public company targets: SEC reports carve-out and filing
8. Consistency checks across the deal documents

Authorities named here are listed, with what was read and when, in `references/primary-sources.md`. A case named below supports only the point stated; the agreement in front of you controls.

## 1. Mapping the agreement to the schedules

Build the map from the newest draft of the agreement, never from the schedule draft or a checklist.

| Check | What to record | Why it matters |
|---|---|---|
| Draft and date | Draft number, date, who circulated it | Numbering moves between drafts; a schedule keyed to draft 4 qualifies the wrong reps under draft 5 |
| Article lead-in | Whether the article opens with "Except as set forth in the Disclosure Schedule" (or the corresponding section of it) | An article-level lead-in can make every schedule an exception to every rep in that article (BBP Holdco); without one, only reps with their own lead-in can be qualified |
| Section lead-in | "Except as set forth on Schedule 3.10" or similar, per section and subsection | A rep with no lead-in, under an article with no lead-in, cannot be qualified by any schedule; the fix is an agreement change |
| Rep type | List rep ("Schedule 3.13(a) lists each Material Contract"), exception rep ("except as set forth on Schedule 3.10, no Action is pending"), or both | A list rep is breached by an omission; an exception rep is breached by an undisclosed fact |
| Defined terms | Material Contract thresholds, lookback dates, Knowledge persons, "Company" (with or without Subsidiaries), Material Customer | The population of items to list comes from these definitions, not from the data room |
| Entity scope | Which entity makes the rep and which entities it covers | A contract signed by the seller's parent is not a contract "to which the Company is a party"; it goes on a shared-contracts or transition list if the agreement has one, and is flagged if it does not |
| Covenant schedules | Interim operating covenant exceptions placed in the disclosure letter | Exceptions moved from a covenant into a schedule apply to that covenant only unless the agreement says otherwise (Williams) |

Annualize every amount the same way the definition does ("in any twelve-month period", "in the last fiscal year") and show the arithmetic in the map. Monthly and quarterly fees are multiplied out; do not compare a monthly figure with an annual threshold.

## 2. General terms (preamble) provisions and each side's position

| Provision | Seller's usual position | Buyer's usual position | Drafting note |
|---|---|---|---|
| Cross-reference clause | Any disclosure qualifies every rep to which its relevance is reasonably apparent | Disclosure qualifies only the numbered section, plus sections expressly cross-referenced | Whatever the clause says, add express cross-references (section 4) |
| No admission | Inclusion is not an admission of liability, of breach, or that the item is material or outside the ordinary course | Usually accepted | Does not undo a factual admission written into the description (section 6) |
| No expansion | Schedules do not expand the reps | Accepted | Keep reps in the agreement, not in the schedule |
| Summaries | Descriptions are qualified by the documents themselves | Accept only for documents actually delivered and identified | Identify the document precisely so the qualification has something to attach to |
| Data room incorporation | Everything in the data room is deemed disclosed | Reject; information outside the schedules does not qualify the reps | Delaware has refused to let data room contents or a diligence call qualify a rep the schedule did not cover (Dura Medic); do not draft general incorporation unless the agreement itself provides for it, and then flag it |
| Headings | Headings are for convenience | Accepted | Headings do not substitute for the numbered reference |
| Updates | Seller may supplement; supplements cure | Supplements are for information only and cure nothing | Governed by the agreement; see `references/updates-and-sandbagging.md` |

The preamble cannot change the agreement. If the agreement and the preamble conflict, the agreement controls, and the conflict is a blocking issue to resolve in the agreement.

## 3. The description standard

A disclosure qualifies a rep only to the extent it states the fact that would otherwise make the rep untrue. For each item:

1. Identify the document or matter: title, parties, date, amendments, court or agency, docket or charge number.
2. State the exception itself: the consent right, the termination right, the default, the audit, the allegation, the amount, the date of notice.
3. State status as of the schedule date: pending, threatened in writing, settled, closed.
4. Give amounts with their source; give dates with their source.
5. Use the defined terms of the agreement.

| Weak | Adequate |
|---|---|
| "Master Supply Agreement with Halvorsen Foods, Inc." against a change-of-control rep | "Master Supply Agreement dated March 3, 2021 between the Company and Halvorsen Foods, Inc. Under Section 14.2, Halvorsen may terminate on 30 days' written notice following a change of control of the Company." |
| "Certain regulatory audits" | Each audit by agency, notice date, period covered, status |
| "See Data Room folder 7.3" | The specific documents in folder 7.3 that create exceptions, each described as above |
| "Employment matters" | Charge, filing date, claimant's role, the allegations as stated in the charge, status |

What courts have done with descriptions (each read in full; see `references/primary-sources.md`):

- Dura Medic (Del. Ch. 2025): the schedule identified one government audit and not others; the sellers' argument that the buyer learned of another audit on a diligence call or could have found it in the data room did not qualify the rep, and the integration clause barred using that extrinsic evidence to vary the rep.
- Sam I Aggregator (Del. Ch. 2025, dismissing the buyer's counterclaims at the pleading stage): a disclosure letter that defined a former officer's demand as the "allegations" against the company and placed it under the accounting-controls rep qualified that rep; the buyer could not later narrow it to an employment matter.
- BBP Holdco (Del. Super. 2025): a schedule that named the regulator, the directive provision and the notice was adequate disclosure of the written notice; the article-level lead-in made it an exception to the reps in that article.

## 4. Cross-references and the "reasonably apparent" clause

Typical text: information in one section "shall be deemed to apply to and qualify ... each other Section ... to the extent that it is reasonably apparent on its face in light of the context and content of the disclosure that such information is relevant to such other Section."

- Read it narrowly. In Williams v. Energy Transfer (Del. Ch. 2021) the court read the clause to carry an exception to another covenant where that was facially necessary to avoid an inconsistency, and rejected a reading that would let an exception excuse any logically related conduct.
- "On its face" means from the words of the disclosure. If the disclosure does not mention the subject of the other rep (for example, a litigation entry that does not mention the accounting allegations it contains), relevance is not apparent on its face.
- Rule: every disclosure that is meant to qualify more than one rep carries an express cross-reference in each schedule ("See also Schedule 3.6(c)") or is repeated there in full. The clause is a safety net, not a drafting method.

## 5. Knowledge, materiality and threshold qualifiers

| Situation | Rule |
|---|---|
| Rep is knowledge-qualified | Schedule the facts within the defined Knowledge persons' actual or constructive knowledge as defined; do not repeat "to Seller's Knowledge" in the schedule |
| Rep is flat (no knowledge qualifier) | Do not add "to Seller's Knowledge" in the schedule; that is an attempted change to the rep and the buyer will treat it as one. If the seller needs the qualifier, propose it in the agreement |
| Rep is materiality-qualified | Listing an item below the threshold is a seller election; the no-admission clause covers it. Where a materiality scrape applies for indemnity, consider scheduling items the seller would otherwise treat as immaterial; route the scrape analysis to merger-agreement |
| Dollar thresholds and lookbacks | Apply exactly as defined; show the computation; items outside the lookback are not required |
| "Material" undefined | Delaware reads a materiality qualifier in a rep to exclude small, de minimis and nitpicky issues (Akorn, as quoted in Dura Medic); do not rely on that to omit an item the buyer asked about |

## 6. Admissions, privilege and confidentiality

- Facts, not conclusions. A schedule is the seller's own written statement and can be offered against it (Fed. R. Evid. 801(d)(2)(A) treats a party's own statement offered against it as not hearsay; state evidence rules vary). Describe what was alleged, by whom, when, and the status. Do not write "the Company violated", "likely liable", "exposure is approximately", or an intention to settle.
- Do not quote, summarize or characterize counsel's advice, reserve analyses or litigation strategy. Disclosing privileged content to a counterparty may waive the privilege; whether a common-interest doctrine protects deal-related sharing depends on the jurisdiction `[VERIFY]`.
- Third-party confidentiality: a contract may forbid disclosing its terms. Describe the existence of the restriction and the exception without the restricted terms, or obtain consent; flag the conflict.
- Personal data: no Social Security numbers, home addresses, bank account numbers or health details beyond what the rep requires; use employee identifiers for compensation schedules.

## 7. Public company targets: SEC reports carve-out and filing

- Carve-out text usually reads: except as disclosed in the Company SEC Reports filed after a stated date and before signing, excluding risk factors, forward-looking statements and other predictive or cautionary disclosure. Check: the date window, whether exhibits are included, and whether the carve-out applies to the fundamental reps (capitalization, authority) or is excluded from them.
- A filing outside the window, or a risk factor, does not qualify the rep. Schedule the specific matter if it must qualify.
- Filing: under Regulation S-K Item 601(a)(5) schedules to a filed exhibit need not be filed if they do not contain information material to an investment or voting decision not otherwise disclosed; the exhibit must list the omitted schedules and the registrant must furnish them to the Commission on request. Item 601(b)(2)(ii) permits redacting immaterial provisions the registrant customarily treats as confidential, with marking requirements. Item 601(a)(6) permits redacting personal information.
- The SEC's 2005 Titan report states that reps in a publicly disclosed agreement are disclosure to investors and that an issuer must consider whether additional facts are needed so they are not misleading. Draft the schedules assuming they may be requested.
- Antitrust filings may require transaction documents; route filing questions to hsr-filing.

## 8. Consistency checks across the deal documents

| Compare | Against | Common break |
|---|---|---|
| Capitalization schedule | Stock ledger, cap table, option ledger, charter | Option counts or holders differ; a warrant missing |
| Material Contracts list | Data room index, contract database, revenue by customer | A contract in the revenue file missing from the list; a terminated contract still listed |
| Litigation schedule | Litigation files, demand letters, insurer notices, board minutes | A written threat in a demand letter not scheduled |
| Disclosure letter terminology | Agreement defined terms | A schedule uses an undefined or differently defined term |
| Diligence report findings | Schedules | A red flag in the report with no matching disclosure; route the reconciliation to due-diligence-report |
| Tax schedules | Tax returns and tax diligence | Elections and audits omitted; route tax analysis to analyzing-m-and-a-tax-implications |
