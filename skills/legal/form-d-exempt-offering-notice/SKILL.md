---
name: form-d-exempt-offering-notice
language: en
description: >
  Drafts SEC Form D notices of exempt offering and Form D/A amendments for operating
  companies and pooled investment funds, mapped one-to-one to the form's 16 items.
  Runs a source-review gate over the matter inventory, builds an evidence-to-field
  worksheet for every item, reconciles subscription documents, governing documents and
  administrator ledgers issuer by issuer, determines the date of first sale and the
  filing deadline, identifies amendment triggers, records EDGAR and BrokerCheck lookup
  outcomes precisely, and plans EDGAR access (Form ID, EDGAR Next) for new issuers.
  Use for Form D, Form D/A, Reg D notice, notice of exempt offering, fund closing
  filings, parallel fund, feeder fund, or EDGAR filing for a private placement.
tags:
  - corporate
  - drafting
  - memo
  - regulatory
  - funds
  - edgar
---

# Form D Notice of Exempt Offering (Regulation D)

Prepares Form D notices and Form D/A amendments for offerings made under Rule 504, Rule 506(b), Rule 506(c) or Section 4(a)(5), for operating companies and pooled investment funds. The deliverable is a filing determination, ranked blocking issues, an evidence-to-field worksheet and item-by-item draft keyed to the form's own numbering, judgment calls, and complete hand-offs to related skills. It is a draft for attorney review. It is never a filing-ready package.

## Why This Skill Exists

Form D looks like data entry and is not. Filings go wrong in predictable ways, listed in the table below, and most of them trace to drafting from a summary instead of the executed documents. Form D is public, and a new issuer cannot file until it has a CIK and delegated filing access. This skill front-loads those problems so the attorney sees them before the deadline.

## Where mistakes hide

Read each document type with this suspicion before drafting from it.

| Document | What it is used for | Where the error hides |
|---|---|---|
| Administrator ledger or register | Cross-check only | Stale commitment amounts after an executed amendment; scheduled closing dates in place of acceptance dates; summary-tab totals that double count a feeder; status flags that disagree with the executed questionnaire |
| Closing memo | Cross-check; closing mechanics | A "first sale" date that is the closing date; pre-amendment totals |
| Client email or cover note | Context and instructions | An instruction to use a lower-ranked source ("use the register as of Wednesday", "use the org chart"), which carries that source's errors into the filing; a description of the document set that differs from the inventory |
| Org chart and prior Form D | Secondary evidence of related persons; baseline for 10 percent tests | Stale related persons; a prior error copied forward; an unconfirmed CIK or accession number |
| Executed subscriptions and amendments | Commitment amounts, acceptance dates (controlling) | The one file that was spot-checked rather than read; an amendment that changes an amount after the register was cut |
| Investor questionnaires | Status, residence, non-U.S. person representations | A non-qualifying answer the ledger flagged otherwise; a handwritten note; an unsigned page |
| Placement agreement exhibits | Covered investors, fee rate, registered states, associated persons | An investor's state missing from the registered-states exhibit; a fee base that includes a direct investor or a stale amount |
| Bad actor questionnaires and certifications | Covered-person review | A "Yes" with no attached order; a certification dated before the sale it covers |
| Oddly named scans | Often the "outstanding" document | Called missing because a text search did not surface it |

## Ground Rules

1. **Draft only.** Never state or imply that a filing is ready to submit. Every output is a draft for attorney review.
2. **Never guess identifiers.** CIKs, CRD numbers, file numbers and accession numbers come from EDGAR, BrokerCheck or a source document. Every identifier gets a primary lookup and a recorded outcome in the five-outcome vocabulary of `references/edgar-access.md` (confirmed match, affirmative no-match, different entity returned, lookup blocked or failed, not checked). A failed lookup is not a no-match; a no-match is not "unverified". Never substitute a near match or a real entity for a fictional one.
3. **Cite every populated field.** Each value names the document and the section or page it came from.
4. **Name conflicts, do not resolve them silently.** When two sources disagree, show both, say which controls under the hierarchy in `references/source-reconciliation.md`, and use the controlling value. A ledger flag never controls over an executed document. A client instruction to use a lower-ranked source is a conflict to reconcile, not an instruction to follow.
5. **Only fields that exist on Form D.** Draft Items 1 through 16 and the signature block, using the form's own item numbers and field labels. The form has no field for SIC code, website, price per unit, offering structure, escrow, financial condition or general use-of-proceeds categories. If client materials supply those facts, leave them out entirely: no table row, no "N/A", no note about their absence.
6. **Clarification of Response exists on five items only:** Items 3, 10, 13, 15 and 16. Use it there for every judgment call that affects what a reader of the public filing would understand. For every other item there is no such field, so record the judgment call in the memo (Section 4 of the output), not in the filing.
7. **Form D is public.** Clarification text, names and amounts are disseminated on EDGAR and cannot be kept confidential. Flag any proposed clarification or value that would expose deal terms, investor identity or strategy. Clarification text is limited to 255 characters.
8. **Mark what you cannot confirm with `[VERIFY]`.** Do not invent citations, interpretive-guidance numbers or thresholds. The rules below were checked against primary sources; rules marked `[VERIFY]` were not found in primary text and are practice or inference.
9. **Today's date matters.** Establish the current date at intake. If any computed deadline has passed or falls within five business days, say so at the top of Section 1 and in Section 2.
10. **Prior filings are evidence, not authority.** Follow a prior filing's approach where the form permits more than one reading. Where the prior filing conflicts with the form's instructions, treat it as an error to correct by amendment and say so. If the prior notice's CIK or accession number cannot be confirmed on EDGAR, treat the prior notice as unconfirmed; do not assume an amendment is possible (see `references/edgar-access.md`).
11. **A document is "still needed" only after an inventory check and a retrieval attempt.** Before any document is described as missing or unavailable, check the matter inventory, open the file, and attempt extraction or OCR, under the source-review completion gate in `references/source-reconciliation.md`. If a file stays unreadable, say exactly what could not be read and which conclusions depend on it.
12. **"MISSING" is not an answer.** Every field of Items 1 through 16 and the signature block gets an evidence-to-field worksheet row (`references/form-d-items.md`). A value that is not settled is classified as an unknown fact, an issuer election, not applicable, an unverified external lookup, or a source conflict, with the Form D choices still open and what settles it.
13. **Issuer first, program second.** Items 13, 14 and 15 are computed for each issuer from its own executed documents, investor by investor, before any program-wide figure is presented (`references/fund-structures.md`, Issuer-specific reconciliation). A total is never copied from a ledger, closing memo or email. A program total goes into an issuer-specific field only under the conditions stated there.
14. **A flag is not a deliverable.** Every conflict, qualification question, bad actor "Yes" and lookup failure ends in a recommendation, the alternatives and what changes under each, an owner, and a next action.

## Workflow

Run the steps in order. Read the named reference file before each step that cites one.

### Step 1: Intake and inventory

Ask for anything missing, but do not stall: proceed with what was provided and list the gaps.

1. Issuer(s): legal names, entity types, jurisdictions, formation dates, any CIK already assigned.
2. Offering: operating company or pooled investment fund; exemption claimed (504, 506(b), 506(c), 4(a)(5)); Investment Company Act exclusion (3(c)(1) or 3(c)(7)) for funds.
3. Which closings or events have occurred, and whether any Form D has already been filed for this offering (obtain the prior filing).
4. The document set. Build the matter inventory from the files actually present (folder listing, data room export, attachments), not from the client's description: each file, its type, its date, its pages or sheets, and its rank in the source hierarchy. Where the description and the inventory differ, note it as a client question.
5. The persons who will sign and who will do the EDGAR filing.

### Step 2: Classify the structure

Decide and state: single issuer or multiple issuers; new offering or existing offering; operating company or pooled fund. For funds, identify each vehicle's role (main fund, parallel fund, feeder, offshore feeder, alternative investment vehicle) and which vehicles are separate issuers. Read `references/fund-structures.md` for any pooled fund.

### Step 3: Complete the source-review gate, then reconcile the sources

Read `references/source-reconciliation.md`. First complete the source-review completion gate: open every inventoried file, review every file in the must-review categories in full (every subscription's signature page, acceptance block and questionnaire, not a sample), and give every row a status: reviewed, not relevant, unreadable after attempt, or still needed. The register goes in the output header. No item is drafted until every row has a status.

Then re-read the client email and closing memo for any instruction to use a lower-ranked source, and run every reconciliation the reference lists, including the bad actor questionnaire review. Sources rank: executed and accepted subscription documents, then governing documents; offering documents and supplements; administrator ledgers and closing memos; client emails and org charts. Where a client instruction conflicts with a higher-ranked document, the document controls; raise the conflict as a client question. For multi-issuer programs, build the investor reconciliation and issuer schedules in `references/fund-structures.md` here, before Step 6.

### Step 4: Determine the filings, the date of first sale and the deadline

Read `references/amendments-and-deadlines.md`. For each issuer, decide whether the filing is a new notice, an amendment, or both, and state the trigger.

**Date of first sale.** Quote the form's definition: the date on which the first investor is irrevocably contractually committed to invest. For each vehicle, find the earliest subscription and read its acceptance and revocability provisions to decide when that investor became bound, applying the reference's decision rules (irrevocable on delivery; revocable until acceptance; silent or ambiguous). Do not use the scheduled closing date, the date capital is called or paid, or the date in a closing memo or ledger. A mandatory capital call does not start a new clock.

**Deadline.** A new notice is due no later than 15 calendar days after the date of first sale, counting the first sale date as day 0. If day 15 falls on a Saturday, Sunday or federal holiday, the due date is the first business day after; a weekend first-sale date does not shift the clock. Show the computation every time, in exactly this form:

```
Date of first sale: <date> (<weekday>)
Raw day 15:         <date> (<weekday>)
Due date:           <date> (<weekday>)   [rolled because <reason> | not rolled]
```

Treat federal legal holidays as holidays and state that assumption `[VERIFY]`. Advise filing before 5:30 p.m. Eastern on the due date; a later submission is deemed filed the next business day `[VERIFY]`.

**Amendments under Rule 503.** An amendment is required to correct a material mistake of fact or error, to reflect a change in the information provided (except the listed exceptions), and annually while the offering continues. A filed amendment resets the annual anniversary; a change-driven trigger runs from the change. Apply the exception list in the reference item by item, including the direction of each change and the 10 percent tests measured cumulatively since the previously filed notice. Adding a related person or a sales compensation recipient is never excepted.

**Late filing.** Filing Form D is not a condition of the Rule 506 exemption, but a late filing is a failure to comply with Rule 503, with Rule 507 and state notice consequences. If any deadline has passed, escalate, recommend filing as soon as practicable, and route the state question to `blue-sky-filings`.

### Step 5: Run the qualification and compliance screens

Before drafting Items 6, 11 and 14, check every investor against the exemption and fund-exclusion relied on. If any questionnaire conflicts with the exemption, the exclusion or the ledger, escalate using the six-element write-up in `references/fund-structures.md` (Qualification conflicts), which ends in a recommended next step with an owner and the Form D fields and counts under each outcome. Do not just report the count, and do not let the ledger flag decide.

In the same step, review every bad actor questionnaire and certification as set out in `references/source-reconciliation.md` (Bad actor questionnaire review): for each "Yes", record the person, question, disclosed event, date, source page and whether the primary document was reviewed, then characterize it only after applying the Rule 506(d) criteria. A "Yes" is routed with a counsel decision, never concluded here.

### Step 6: Build the worksheet and draft the items

Read `references/form-d-items.md`. Build the evidence-to-field worksheet for every field of Items 1 through 16 and the signature block, then draft each item using the form's own numbering and field names. Apply the Item 11 decision framework rather than a categorical rule. Where any Regulation S sale exists, present Items 13(b) and 14 in both variants (Regulation D only; all sales). Respect the single-exemption limit: a submission cannot claim both Rule 506(b) and Rule 506(c).

### Step 7: Look up identifiers and plan EDGAR access

Read `references/edgar-access.md`. For every issuer, retrieve or confirm the CIK; for any prior notice, the accession number; for every compensation recipient, the CRD number. Record each lookup's outcome in the identifier lookup register with the route, the evidence returned and the filing consequence. A missing or unconfirmed CIK is a critical-path item against the deadline and goes at the top of the blocking issues. Recommend that the issuer delegate filing authority to the law firm's EDGAR account.

### Step 8: Hand off, completely

Read the Section 5 rules in `references/output-template.md`. A referral by skill name is not a hand-off. Each hand-off carries the specific issuers, persons, states, triggering facts, dates and deadlines, missing confirmations, and what remains for the related workflow.

- State notice filings and placement agent registration gaps: `blue-sky-filings`, with the placement agent cross-check matrix covering every investor (introduced by whom, state, agent registered there). This skill does not perform the state-by-state analysis; it supplies every fact that analysis needs.
- Rule 506(d) diligence: `bad-actor-disqualification-review`, with every covered person, every "Yes" and its review record, every missing or unsigned questionnaire and every stale certification. The Form D signer certifies that the issuer is not disqualified, so this diligence must be complete before signature.

## Required Output Format

Produce the header and these six sections, in this order. The template and table layouts are in `references/output-template.md`.

0. **Header.** Matter, issuers, today's date, structure classification, and the source-review register.
1. **Filing determination.** Each required filing, the trigger, the date of first sale with the contract reasoning, the due-date computation in the fixed format, and the identifier lookup register.
2. **Blocking issues and client questions.** Ranked by severity, each with its source citation, the recommendation and alternatives, and the person who can resolve it.
3. **Evidence-to-field worksheet and item-by-item draft.** The investor reconciliation and issuer schedules first, then one worksheet table per filing.
4. **Judgment calls.** The options, the recommended choice, what changes under each alternative, and why. Include every judgment call on an item that has no clarification field, and always Item 11.
5. **Hand-offs.** To `blue-sky-filings` and `bad-actor-disqualification-review`, each complete as defined in the template.
6. **Assumptions, open items and `[VERIFY]` list.** Every open item with an owner and a next action; the documents still needed; each `[VERIFY]` statement with what would settle it.

Close the output with: "Draft for attorney review. This is not a filing-ready submission."

## Quality-Control Gate Before Responding

Confirm each statement below is true of the draft. If one is not, fix the draft; do not respond with the gate unmet.

- Every inventoried file in a must-review category was reviewed in full, or is recorded as unreadable after a stated attempt or as still needed from a named source. No file is described as missing because a search did not surface it.
- No field is blank or "MISSING". Every unsettled field is classified with the Form D choices still open and what settles it.
- The investor reconciliation table covers every investor of every issuer, with executed amount, ledger amount and delta; an empty or partial table means the draft is incomplete. Items 13 and 15 are sums of its executed amounts, not a figure copied from any single source.
- For each issuer, the arithmetic check (sold plus remaining equals the reported offering amount, or the stated treatment that explains the difference) is shown; program figures appear separately; where any Regulation S sale exists, Items 13(b) and 14 show both variants.
- Every client instruction to use a lower-ranked source was reconciled against the controlling document and, where it would carry an error forward, written up as a conflict with the correct value.
- Every bad actor questionnaire "Yes" was summarized in the review record, characterized only after applying the Rule 506(d) criteria, given the severity the template assigns to that characterization, and routed with a counsel decision and a follow-up.
- Every date of first sale and deadline rests on the governing contractual event in the executed documents, not on a closing label, a closing memo date or a ledger date; every computation is shown in the fixed format with weekdays.
- Every EDGAR and BrokerCheck lookup is described by its actual outcome; no failed lookup is called a no-match, no no-match is called unverified, and no identifier appears that was not read from a document or a lookup.
- The placement agent cross-check matrix covers every investor, flags only agent-introduced investors in states outside the agent's registered list, and flags no direct investor as an agent registration gap.
- Every conflict and qualification question ends in a recommendation with the alternatives and what changes under each. Every unresolved item has an owner and a next action.
- No unresolved or provisional value is presented as settled; confidence and status columns match the narrative.
- No field outside Form D appears anywhere in the draft; clarification text appears only on Items 3, 10, 13, 15 and 16, within 255 characters, and nothing in it is confidential.
- Every investor in the document set has been checked against the exemption and exclusion relied on. Every unconfirmed statement carries `[VERIFY]`.

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| A document the client mentioned "cannot be found" | The search tool indexed text layers and the file is a scan or has an unrelated name | Walk the inventory file by file; open each; OCR scans; then assign a status (`references/source-reconciliation.md`) |
| A field is "MISSING" | The drafter skipped the choice analysis | Fill the worksheet row: open choices, recommendation, what settles it (`references/form-d-items.md`) |
| Item 13 or 15 matches the ledger total exactly but not the subscriptions | The total was copied, not computed | Rebuild from the investor reconciliation table; write up the ledger difference as a conflict |
| An issuer's Item 13 shows the program total | Program figures were carried across issuers | Rebuild from the issuer schedule; apply the program-total conditions (`references/fund-structures.md`) |
| Item 11 is 0 "because the GP can waive" or the stated minimum "because the PPM says so" | A categorical shortcut | Run the four-question framework and present the recommendation and alternatives |
| A direct investor's state is flagged as an agent registration gap, or an agent-introduced investor's state is not | The cross-check was eyeballed | Complete the matrix for every investor (`references/output-template.md`, Section 5) |
| A "Yes" on a questionnaire is listed only in the hand-off, or is Critical without the order being read | The event was not reviewed, or severity was assumed | Complete the review record, characterize under Rule 506(d), apply the template's severity rule |
| "CIK not found" after a 403 or timeout | A failed lookup was treated as a no-match | Re-run by another route; if all fail, report Lookup blocked or failed and present both consequences |
| A 404 from the submissions data reported as "unverified" | A no-match was softened | Report Affirmative no-match, with the evidence, and its filing consequence |

## Reference Files

| File | Read it when |
|---|---|
| `references/form-d-items.md` | Building the evidence-to-field worksheet and drafting Items 1-16 and the signature block; the Item 11 framework |
| `references/amendments-and-deadlines.md` | Determining date of first sale, deadlines and amendment triggers |
| `references/fund-structures.md` | Any pooled investment fund, parallel fund, feeder, the investor reconciliation and issuer schedules, or a qualification conflict |
| `references/source-reconciliation.md` | The source-review gate, ranking sources, client instructions to use a lower-ranked source, reconciling the document set, and the bad actor questionnaire review |
| `references/edgar-access.md` | Identifier lookup outcomes, Form ID, EDGAR Next, delegation, XML, signing and retention |
| `references/output-template.md` | Laying out the header and six-section deliverable, the severity rule, the cross-check matrix and complete hand-offs |
| `references/primary-sources.md` | Citing a rule or form instruction; the source URLs and what was confirmed |
