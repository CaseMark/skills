# Output Template

Produce the header and the six sections in this order. Keep sentences plain; put detail in tables. Every date shows its weekday.

## Contents

1. Header (including the source-review register)
2. Section 1. Filing determination (including the identifier lookup register)
3. Section 2. Blocking issues and client questions
4. Section 3. Evidence-to-field worksheet and item-by-item draft
5. Section 4. Judgment calls
6. Section 5. Hand-offs (complete)
7. Section 6. Assumptions, open items and `[VERIFY]` list
8. Filing package (only when requested)

## Header

- Matter or offering name, issuer(s), date prepared, preparer note: "Draft for attorney review."
- Today's date used for deadline comparison.
- One paragraph classifying the structure (issuers, vehicles, exemption and exclusion, existing or new offering).
- **Source-review register**, the output of the gate in `source-reconciliation.md`. One row per inventoried file, including files with uninformative names and every workbook sheet:

| File | Type | Date | Rank | Status | Pages or sheets read | Note |
|---|---|---|---|---|---|---|
| name as inventoried | subscription, questionnaire, LPA, PPM, ledger, closing memo, prior filing, agent agreement, email, other | | 1-4 | Reviewed / Not relevant / Unreadable after attempt / Still needed | | reason for Not relevant; method tried and dependent conclusions for Unreadable; who supplies it for Still needed |

Where the client's description of the document set differs from the register (a document described as outstanding that is in the matter, or described as sent that is not), say so under the table.

Put the EDGAR access plan (CIK status for each issuer, Form ID needs, delegation to the firm) in Section 1 beside the Form ID rows.

## 1. Filing determination

A table with one row per required filing.

| Filing | Issuer | Trigger | Date of first sale (basis) | Due date | Status |
|---|---|---|---|---|---|
| New notice / Amendment / Form ID | name | what requires it | date and the contract clause relied on | date | on time / due in N days / past due |

Under the table, for each new notice, the fixed computation:

```
Date of first sale: <date> (<weekday>)
Raw day 15:         <date> (<weekday>)
Due date:           <date> (<weekday>)   [rolled because <reason> | not rolled]
```

For each amendment, state which trigger applies (error, change, annual), the figures and percentages behind any 10 percent test, the annual anniversary date, and the reset date if a change-driven amendment is filed first. State which issuers need a Form ID. Where a prior notice is unconfirmed, show both filing paths (amendment if it exists; late new notice from the original date of first sale if it does not) with the due date and consequence of each.

**Identifier lookup register**, one row per identifier, in the vocabulary of `edgar-access.md`:

| Identifier | Issuer or person | Value in documents (source) | Route | Date and time | Outcome | Evidence returned | Consequence |
|---|---|---|---|---|---|---|---|
| CIK / accession / file no. / CRD | | | EDGAR company search, submissions data, filing index, BrokerCheck, IAPD | | Confirmed match / Affirmative no-match / Different entity returned / Lookup blocked or failed / Not checked | the name, error or empty result as returned | |

## 2. Blocking issues and client questions

Ranked by severity, most severe first. A table:

| # | Severity | Issue | Why it blocks | Source citation | Recommendation and alternatives | Who can resolve |
|---|---|---|---|---|---|---|

Severity levels: Critical (deadline, CIK, exemption or exclusion in doubt, qualification conflict, potentially disqualifying bad actor event, unconfirmed prior notice); High (value conflict that changes a filing outcome; an unreadable or still-needed document a filing outcome depends on; a client instruction that would carry a lower-ranked source's error into the filing); Medium (value conflict with a clear controlling source); Low (clean-up). A missing or unconfirmed CIK for any issuer is Critical. A bad actor "Yes" is Critical only when characterized as potentially disqualifying on the primary document; one characterized as unresolved, disclosure-only or outside the criteria on its face is High, not Critical, and is routed for counsel confirmation rather than concluded here. Every row ends in a recommendation and what changes under the alternative; a row that only names a problem is incomplete.

## 3. Evidence-to-field worksheet and item-by-item draft

Start with the **investor reconciliation table** for each issuer (every investor; executed amount, ledger amount, delta; `fund-structures.md`), then for a multi-issuer program the **issuer calculation schedules** (one per issuer) and the **program schedule**, with the arithmetic check for each issuer shown as a line: "(a) $X minus (b) $Y equals (c) $Z" or the stated treatment that explains the difference. Where any Regulation S sale exists, 13(b) and 14 appear in both variants. Items 13 to 15 are not drafted until the table is complete and every unexplained delta is in Section 2.

Then one worksheet table per filing, using the form's item numbers and field labels. The worksheet columns are defined in `form-d-items.md` (Evidence-to-field worksheet).

| Item | Proposed value or open choices | Source | Conflict and controlling source | Confidence | Confirmation needed | Consequence if changed | Status | Flag or clarification text |
|---|---|---|---|---|---|---|---|---|
| 1. Issuer's Identity: Name of Issuer | | document, section | | High / Medium / Low | none / issuer: question / counsel: question | | Settled / Unknown fact / Issuer election / Not applicable / Unverified external lookup / Source conflict | |

Use one row per field or per repeating entry (each related person, each compensation recipient, each co-issuer). Show clarification text only where the form has a clarification field (Items 3, 10, 13, 15, 16), and show its character count. No row is blank or "MISSING": an unsettled row lists the choices still open, the recommended one, and what settles it. Include the signature block row with the signer, capacity and authority.

## 4. Judgment calls

For each: the question, the options, the recommended choice, what changes under each alternative, and the reason. Include every judgment call on an item that has no clarification field. Always include Item 11, laid out as the four questions and readings in `form-d-items.md` with the recommended value, alternatives and issuer confirmation. Other typical entries: an ambiguous date of first sale; one filing or several; Regulation S reporting; Item 13 cap presentation; Item 15 payer; entity type for a non-U.S. vehicle; related persons beyond the form's examples; Item 5 for a new fund.

## 5. Hand-offs

A hand-off is complete only when the receiving workflow could start without re-reading the matter. A referral by skill name with "see above" is not a hand-off. Each hand-off also states, in one sentence, what this skill did not do and what remains for the related workflow.

**`blue-sky-filings`.** This skill does not perform the state-by-state analysis. First the **placement agent cross-check matrix**, one row per investor of every issuer, no sampling:

| Investor | Issuer | State or non-U.S. | Introduced by (agent name or Direct) | Agent registered in that state? (registered-states exhibit, page) | Gap? |
|---|---|---|---|---|---|

Mark Gap only where Introduced by is an agent and the state is outside that agent's list. A Direct-introduced investor creates no agent registration gap in any state; its state still appears in the state table below for the notice-filing question. Then pass:

| Issuer | State | Investors there (name, commitment, residence or solicitation basis, source) | Date of first sale to a resident of that state (basis) | Placement agent or finder involved and its registration status in that state (source: registered-states exhibit) | Triggering fact | Deadline or timing question | Missing confirmation |
|---|---|---|---|---|---|---|---|

Plus: whether any federal deadline has passed (late-notice consequences), whether the filing is one notice or several (some states require one per issuer), and the related-person and agent facts a state form may ask for.

**`bad-actor-disqualification-review`.** This skill reads the questionnaires and certifications; the diligence record and disqualification analysis belong to the receiving workflow. Pass:

| Person or entity | Covered-person category and basis | Questionnaire or certification: date, executed, stale? | Each "Yes": question, disclosed event, event date, source page, primary document reviewed? | Characterization after applying Rule 506(d) (potentially disqualifying / disclosure-only / outside the criteria on its face / unresolved) | Counsel decision needed | Follow-up, owner, and timing relative to the Form D signature |
|---|---|---|---|---|---|---|

Include every newly identified related person or covered person with no questionnaire, every unsigned or undated questionnaire, every stale or expired agent certification, and every order or judgment still needed. State the sale dates the lookbacks run from.

## 6. Assumptions, open items and `[VERIFY]` list

- Assumptions made and what changes if each is wrong.
- **Open items**, as a table; every row has an owner and a next action:

| # | Open item | Depends on (document, lookup, confirmation) | Owner | Next action | Blocks filing? |
|---|---|---|---|---|---|

- Documents still needed (the Still needed rows of the source-review register) and unreadable documents with their dependent conclusions.
- Each `[VERIFY]` statement with what would settle it.

Close with: "Draft for attorney review. This is not a filing-ready submission."

When a filing package was requested, it follows Section 6 as a seventh part, laid out in `filing-package.md` (provenance table, draft XML, keying sheet, checklist), and the memo's closing line is repeated after it.

Before closing, run the quality-control gate in `SKILL.md`.
