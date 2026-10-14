---
name: form-d-exempt-offering-notice
language: en
description: >
  Drafts SEC Form D notices of exempt offering and Form D/A amendments for operating
  companies and pooled investment funds, mapped one-to-one to the form's 16 items.
  Reconciles subscription documents, governing documents and administrator ledgers
  before drafting, determines the date of first sale and the filing deadline, identifies
  amendment triggers, and plans EDGAR access (Form ID, EDGAR Next) for new issuers.
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

Prepares Form D notices and Form D/A amendments for offerings made under Rule 504, Rule 506(b), Rule 506(c) or Section 4(a)(5), for operating companies and pooled investment funds. The deliverable is a filing determination, ranked blocking issues, an item-by-item draft keyed to the form's own numbering, judgment calls, and hand-offs to related skills. It is a draft for attorney review. It is never a filing-ready package.

## Why This Skill Exists

Form D looks like data entry and is not. Filings go wrong in three predictable ways: the 15-day clock is started from the wrong date, the draft is built from a client summary or an administrator ledger instead of the executed documents, and fund structures (parallel funds, feeders, offshore vehicles, multi-vehicle caps) get forced into operating-company assumptions. Form D is public, there is no confidential treatment, and a new issuer cannot file at all until it has a CIK and delegated filing access. This skill front-loads those problems so the attorney sees them before the deadline, not after.

## Ground Rules

1. **Draft only.** Never state or imply that a filing is ready to submit. Every output is a draft for attorney review.
2. **Never guess identifiers.** CIKs, CRD numbers, file numbers and accession numbers come from EDGAR, BrokerCheck or a source document, or they are marked MISSING. If an EDGAR lookup returns nothing, or returns a different entity than the one named in the documents, say so plainly and do not substitute a near match.
3. **Cite every populated field.** Each value names the document and the section or page it came from.
4. **Name conflicts, do not resolve them silently.** When two sources disagree, show both, say which controls under the hierarchy in `references/source-reconciliation.md`, and use the controlling value.
5. **Only fields that exist on Form D.** Draft Items 1 through 16 and the signature block, using the form's own item numbers and field labels. The form has no field for SIC code, website, price per unit, best-efforts or firm-commitment structure, escrow, a financial-condition checklist or general use-of-proceeds categories. If client materials supply those facts, leave them out of the draft: do not list them in any table, not even as "N/A", and do not add a note about their absence.
6. **Clarification of Response exists on five items only:** Items 3, 10, 13, 15 and 16. Use it there for every judgment call that affects what a reader of the public filing would understand. For every other item there is no such field, so record the judgment call in the memo (Section 4 of the output), not in the filing.
7. **Form D is public.** Clarification text, names and amounts are disseminated on EDGAR and cannot be kept confidential. Flag any proposed clarification or value that would expose deal terms, investor identity or strategy. Clarification text is limited to 255 characters.
8. **Mark what you cannot confirm with `[VERIFY]`.** Do not invent citations, interpretive-guidance numbers or thresholds. The rules below were checked against primary sources; rules marked `[VERIFY]` were not found in primary text and are practice or inference.
9. **Today's date matters.** Establish the current date at intake. If any computed deadline has passed or falls within five business days, say so at the top of Section 1 and in Section 2.
10. **Prior filings are evidence, not authority.** Follow a prior filing's approach where the form permits more than one reading (for example, how a shared offering cap is presented). Where the prior filing conflicts with the form's instructions (for example, the wrong Item 5 range for the fund type), treat it as an error to correct by amendment and say so. If the prior notice's CIK or accession number cannot be confirmed on EDGAR, treat the prior notice as unconfirmed; do not assume an amendment is possible (see `references/edgar-access.md`).

## Workflow

Run the steps in order. Read the named reference file before each step that cites one.

### Step 1: Intake and inventory

Ask for anything missing, but do not stall: proceed with what was provided and list the gaps.

1. Issuer(s): legal names, entity types, jurisdictions, formation dates, any CIK already assigned.
2. Offering: operating company or pooled investment fund; exemption claimed (504, 506(b), 506(c), 4(a)(5)); Investment Company Act exclusion (3(c)(1) or 3(c)(7)) for funds.
3. Which closings or events have occurred, and whether any Form D has already been filed for this offering (obtain the prior filing).
4. The document set. Build an inventory table: each document, its type, its date, and where it ranks in the source hierarchy.
5. The persons who will sign and who will do the EDGAR filing.

### Step 2: Classify the structure

Decide and state: single issuer or multiple issuers; new offering or existing offering; operating company or pooled fund. For funds, identify each vehicle's role (main fund, parallel fund, feeder, offshore feeder, alternative investment vehicle) and which vehicles are separate issuers. Read `references/fund-structures.md` for any pooled fund.

### Step 3: Reconcile the sources

Read `references/source-reconciliation.md` and run every reconciliation it lists before drafting any item. In short, rank sources as:

1. Executed and accepted subscription documents, then governing documents.
2. Offering documents and supplements.
3. Administrator ledgers and closing memos.
4. Client emails and org charts.

Where a client instruction conflicts with a higher-ranked document, the document controls; raise the conflict as a client question.

### Step 4: Determine the filings, the date of first sale and the deadline

Read `references/amendments-and-deadlines.md`. For each issuer, decide whether the filing is a new notice, an amendment, or both, and state the trigger. Then apply the rules below.

**Date of first sale.** Quote the form's definition: the date on which the first investor is irrevocably contractually committed to invest, which, depending on the terms and conditions of the contract, could be the date on which the issuer receives the investor's subscription agreement or check. Do not use the scheduled closing date, the date capital is called or paid, or the date shown in a closing memo or ledger. For each vehicle, find the earliest subscription and read its acceptance and revocability provisions to decide when that investor became irrevocably bound:

- If the investor's signed subscription is irrevocable on delivery, the date of first sale can be the date the issuer received it.
- If the investor may withdraw until the issuer countersigns or accepts, the date of first sale is the acceptance date.
- If the agreement is silent or ambiguous, choose the earlier defensible date for the deadline, record the other candidate date, and list it as a judgment call.

Capital for a fund is called later, so payment is never the test. A mandatory capital call is made under the original offering and does not start a new clock.

**Deadline.** A new notice is due no later than 15 calendar days after the date of first sale. Count the first sale date as day 0. If day 15 falls on a Saturday, Sunday or federal holiday, the due date is the first business day after. A Saturday or Sunday first-sale date does not toll or shift the clock; only the due date rolls. Show this computation every time, in exactly this form:

```
Date of first sale: <date> (<weekday>)
Raw day 15:         <date> (<weekday>)
Due date:           <date> (<weekday>)   [rolled because <reason> | not rolled]
```

The rule text does not define "holiday". Treat federal legal holidays as holidays and state that assumption `[VERIFY]`. Also advise filing well before 5:30 p.m. Eastern on the due date: a submission after that time is deemed filed the next business day, and Form D is not among the filing types dated same-day after 5:30 p.m. `[VERIFY]`.

**Amendments under Rule 503.** An amendment is required (a) to correct a material mistake of fact or error, as soon as practicable after discovery; (b) to reflect a change in the information provided, as soon as practicable after the change, except for the listed exceptions; and (c) annually, on or before the first anniversary of the most recent filing, while the offering is continuing. A filed amendment resets the annual anniversary. The change-driven trigger runs from the change, not from the annual date, so do not defer a change-driven amendment to the annual date. Apply the exception list in `references/amendments-and-deadlines.md` item by item, including the direction of each change, the 10 percent tests measured cumulatively since the previously filed notice, and the rule that an exception applies only when the change occurs solely in excepted information. Adding a new related person or a new sales compensation recipient is never excepted.

**Late filing.** Filing Form D is not a condition of the Rule 506 exemption, and a late filing does not by itself forfeit covered-security status. A late filing is nonetheless a failure to comply with Rule 503, with consequences under Rule 507 if an injunction is entered, and with state notice consequences. If any deadline has passed, escalate to the supervising attorney, recommend filing as soon as practicable, and route the state notice question to `blue-sky-filings`.

### Step 5: Run the qualification and compliance screens

Before drafting Items 6, 11 and 14, check every investor against the exemption and fund-exclusion relied on. Read the qualification-conflict section of `references/fund-structures.md`. If any investor questionnaire shows a status that conflicts with the exemption or the exclusion, escalate before filing; do not just report the count. Explain the Rule 506(b) consequences (Rule 502(b) information delivery and the sophistication requirement for non-accredited purchasers; 506(c) is unavailable) and the Investment Company Act consequences (a Section 3(c)(7) fund must be owned exclusively by qualified purchasers, subject to the knowledgeable-employee and other carve-outs).

### Step 6: Draft the items

Read `references/form-d-items.md`. Draft each of Items 1 through 16 and the signature block, using the form's own numbering and field names, with a value, source citation, confidence level and any flag or clarification text for each. Respect the single-exemption limit: a submission cannot claim both Rule 506(b) and Rule 506(c).

### Step 7: Plan EDGAR access

Read `references/edgar-access.md`. For every issuer, retrieve or confirm the CIK. A missing CIK is a critical-path item against the deadline and goes at the top of the blocking issues. Recommend that the issuer delegate filing authority to the law firm's EDGAR account.

### Step 8: Hand off

- State notice filings, and any placement agent state registration gap (for example, an investor located in a state that is not on the placement agent's registered-states exhibit): `blue-sky-filings`.
- Rule 506(d) diligence: `bad-actor-disqualification-review`. Include every newly identified covered person or related person, every "Yes" answer on a questionnaire, every missing or unsigned questionnaire, and every stale or expired placement agent certification. The Form D signer certifies on the form that the issuer is not disqualified, so this diligence must be complete before signature.

## Required Output Format

Produce these six sections, in this order. The template and table layouts are in `references/output-template.md`.

1. **Filing determination.** Each required filing (new notice, amendment, Form ID), the trigger, the date of first sale with the contract reasoning, and the due-date computation in the fixed format above.
2. **Blocking issues and client questions.** Everything that must be resolved before filing, ranked by severity, each with its source citation and the person who can resolve it.
3. **Item-by-item draft.** A table per filing with the columns Item, Value, Source, Confidence, Flag or clarification text.
4. **Judgment calls.** Where reasonable practitioners differ: the options, the recommended choice and why. Include every judgment call on an item that has no clarification field.
5. **Hand-offs.** To `blue-sky-filings` and `bad-actor-disqualification-review`, each with the specific facts to pass.
6. **Assumptions, open items and `[VERIFY]` list.** The assumptions made, the documents still needed, and each `[VERIFY]` statement with what would settle it.

Close the output with: "Draft for attorney review. This is not a filing-ready submission."

## Quality Checks Before Responding

- Every date computation is shown in the fixed format, with weekdays.
- Every populated value has a source citation; every MISSING value says what is needed.
- No CIK, CRD, file number or accession number appears that was not read from a document or a lookup.
- No conflict between sources has been resolved without being named.
- No field outside Form D appears anywhere in the draft.
- Clarification text appears only on Items 3, 10, 13, 15 and 16, and nothing in it is confidential.
- Every investor in the document set has been checked against the exemption and exclusion relied on.
- Every unconfirmed statement carries `[VERIFY]`.

## Reference Files

| File | Read it when |
|---|---|
| `references/form-d-items.md` | Drafting Items 1-16 and the signature block |
| `references/amendments-and-deadlines.md` | Determining date of first sale, deadlines and amendment triggers |
| `references/fund-structures.md` | Any pooled investment fund, parallel fund, feeder, or qualification question |
| `references/source-reconciliation.md` | Ranking sources and reconciling the document set |
| `references/edgar-access.md` | Form ID, EDGAR Next, delegation, XML, signing and retention |
| `references/output-template.md` | Laying out the six-section deliverable |
| `references/primary-sources.md` | Citing a rule or form instruction; the source URLs and what was confirmed |
