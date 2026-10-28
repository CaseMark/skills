# Form D Items 1-16 and Signature

Use the form's own item numbers and field labels. For each item, populate from the highest-ranked source (see `source-reconciliation.md`), cite it, and record confidence as High (read directly from an executed or governing document), Medium (read from a lower-ranked source and consistent), or Low (inferred, conflicting or unknown).

**Clarification of Response** fields exist only on Item 3 (one per related person), Item 10, Item 13, Item 15 and Item 16. Each is limited to 255 characters and is public. Items 1, 2, 4-9, 11, 12, 14 and the signature block have no clarification field; record judgment calls on those items in the memo, not in the filing.

## Contents

1. Evidence-to-field worksheet
2. Item 1. Issuer's Identity
3. Item 2. Principal Place of Business and Contact Information
4. Item 3. Related Persons
5. Item 4. Industry Group
6. Item 5. Issuer Size
7. Item 6. Federal Exemptions and Exclusions Claimed
8. Item 7. Type of Filing
9. Item 8. Duration of Offering
10. Item 9. Type(s) of Securities Offered
11. Item 10. Business Combination Transaction
12. Item 11. Minimum Investment (decision framework)
13. Item 12. Sales Compensation
14. Item 13. Offering and Sales Amounts
15. Item 14. Investors
16. Item 15. Sales Commissions and Finders' Fees Expenses
17. Item 16. Use of Proceeds
18. Signature and Submission

## Evidence-to-field worksheet

Before drafting, build one worksheet row for every field of Items 1 through 16 and the signature block, including repeating entries (each related person, each compensation recipient, each co-issuer). The worksheet is Section 3 of the output (`output-template.md`); nothing is drafted that does not have a row. Each row records:

1. **Proposed value, or the Form D choices still open** when no value is settled. Every item offers a defined set of answers (checkboxes, ranges, Indefinite, Not Applicable, a number, or nothing). List the choices that remain open and the one recommended.
2. **Source(s)**, cited as in `source-reconciliation.md`.
3. **Conflict and controlling source**, if any source disagrees.
4. **Confidence**: High, Medium or Low as defined above.
5. **Confirmation needed**: none, issuer or counsel, with the question to ask.
6. **Consequence if the value or assumption changes**: the field, count, deadline, exemption or hand-off that moves, and how.
7. **Status**: Settled, or one of the five below.

**MISSING is not a status.** A blank value with the word MISSING tells the attorney nothing. Classify instead:

| Status | Use when | The row must still show |
|---|---|---|
| Unknown fact | The fact exists but no source in the matter states it, or the only source is unreadable | The choices the form offers, the document or person that supplies the fact, and the interim recommendation if the form allows one |
| Issuer election | The form lets the issuer choose and the documents do not decide it (Item 5 Decline to Disclose; Item 13 Indefinite; one filing or several; Regulation S treatment; Item 16 presentation) | Each choice, the recommended one with reasons, and "confirm with issuer" |
| Not applicable | The form's own instruction makes the field inapplicable (Item 12 when there is no compensation; Item 5 Not Applicable where the business is not intended to produce revenue) | The instruction relied on |
| Unverified external lookup | A document supplies the value but the external confirmation (EDGAR, BrokerCheck) returned something other than a confirmed match | The document value, the lookup outcome in the vocabulary of `edgar-access.md`, and the filing consequence |
| Source conflict | Two sources disagree | Both values, the controlling source, the value used, the alternative and what changes under it, and whether a client question is needed |

A row may carry no proposed value only when the form offers no choice that the record supports. Then the row says which single fact or confirmation would settle it, and who owns it.

## Item 1. Issuer's Identity

Fields: Name of Issuer; Jurisdiction of Incorporation/Organization; Year of Incorporation/Organization; Previous Name(s) (or None); Entity Type; CIK.

- Name: the exact legal name in the formation document (certificate of limited partnership, certificate of formation, certificate of registration), not the marketing name.
- Year of Incorporation/Organization: one of Over Five Years Ago; Within Last Five Years (specify year); Yet to Be Formed.
- Entity Type: Corporation; Limited Partnership; Limited Liability Company; General Partnership; Business Trust; Other (specify). For a non-U.S. vehicle (a Cayman exempted limited partnership, say) choose the closest type or Other (specify) and record it as a judgment call `[VERIFY]`.
- CIK: look it up as set out in `edgar-access.md` and record the outcome in that vocabulary. An issuer with no CIK is an Unknown fact row routed to the Form ID path. A CIK supplied by the client or a prior filing whose lookup outcome is anything other than Confirmed match is an Unverified external lookup row; a Different entity or Affirmative no-match outcome means the CIK is not used and the consequence in `edgar-access.md` applies.
- Multiple issuers: when more than one issuer sold securities in the same offering, they may be identified on one filing. Check the multiple-issuer box, identify a primary issuer (the most important issuer in the offering) in the first fields, and add each other issuer on Items 1 and 2 continuation pages. Some states require a separate filing for each issuer. Whether to use one filing or several is a judgment call (see `fund-structures.md`).

## Item 2. Principal Place of Business and Contact Information

Fields: Street Address 1 and 2; City; State/Province/Country; ZIP/Postal Code; Phone No. For a fund, use the address in the offering or governing documents for the issuer's principal place of business, which is often the general partner's or manager's office and not the registered office. If they differ, say which you used.

## Item 3. Related Persons

Fields per person: Last, First, Middle Name; Street Address; Relationship(s) (Executive Officer, Director, Promoter); Clarification of Response (if necessary).

List each executive officer and director of the issuer, each person performing similar functions (title alone is not determinative; the form's examples are general and managing partners of partnerships and managing members of limited liability companies), and each person who has functioned directly or indirectly as a promoter within the past five years of the later of the first sale or the date the filing was required. Ten percent owners are not required.

For a fund, take the list from the governing documents in effect on the filing date (`fund-structures.md`). One row per person with the applicable checkbox; use the clarification field where the checkbox alone would mislead (an entity general partner; a managing member of the general partner). If an amendment that may add or remove a person is unreadable or still needed, each affected row is an Unknown fact with the consequence stated (a new related person is an amendment trigger and a covered person).

Adding a related person after a filing requires an amendment. A change only in the address or relationship of a person already listed does not.

## Item 4. Industry Group

Select one. Funds select Pooled Investment Fund (under Banking & Financial Services), then one fund type: Hedge Fund, Private Equity Fund, Venture Capital Fund or Other Investment Fund, and answer whether the issuer is registered as an investment company under the Investment Company Act of 1940 (a fund relying on Section 3(c)(1) or 3(c)(7) answers No). Operating companies select the industry group that fits the business. The fund type drives Item 5, so choose it from the offering documents' description of the strategy and record the basis.

## Item 5. Issuer Size

Select one range.

- Operating companies, Private Equity Funds and Venture Capital Funds: the Revenue Range (No Revenues; $1-$1,000,000; $1,000,001-$5,000,000; $5,000,001-$25,000,000; $25,000,001-$100,000,000; Over $100,000,000; Decline to Disclose; Not Applicable) for the most recently completed fiscal year, or the range to date if no full fiscal year exists. If the business is not intended to produce revenue, the form says to enter Not Applicable.
- Hedge Funds and Other Investment Funds: the Aggregate Net Asset Value Range (No Aggregate Net Asset Value; $1-$5,000,000; $5,000,001-$25,000,000; $25,000,001-$50,000,000; $50,000,001-$100,000,000; Over $100,000,000; Decline to Disclose; Not Applicable) as of the most recent practicable date.

Do not apply the NAV range to a private equity or venture capital fund. Foreign issuers state revenue in U.S. dollars. Declining to disclose is an Issuer election: present it beside the range the record supports, recommend one, and do not select it without client instruction. A newly formed fund with no completed fiscal year is not an Unknown fact; the form's choices (the range to date, Not Applicable where the form's condition is met, or Decline to Disclose) are all open, so list them and recommend.

## Item 6. Federal Exemptions and Exclusions Claimed

Select all that apply: Rule 504(b)(1) (not (i), (ii) or (iii)), 504(b)(1)(i), 504(b)(1)(ii), 504(b)(1)(iii); Rule 506(b); Rule 506(c); Securities Act Section 4(a)(5); and Investment Company Act Section 3(c) with the specific paragraph. The form lists paragraphs (1), (2), (3), (4), (5), (6), (7), (9), (10), (11), (12), (13) and (14) (there is no 3(c)(8) box).

- A single submission cannot claim both Rule 506(b) and Rule 506(c). If co-issuers rely on different rules, file separately.
- Choose the Section 3(c) paragraph from the offering and governing documents, and test it against the investor qualification evidence (Step 5 of the workflow). A fund that claims 3(c)(7) is represented to be owned exclusively by qualified purchasers, subject to the statutory and rule carve-outs. If a qualification conflict is open, the row is a Source conflict showing the selection under each outcome (`fund-structures.md`, Qualification conflicts).
- If co-issuers rely on different 3(c) paragraphs, the form cannot attribute a paragraph to a particular issuer on one filing. Treat this as a judgment call favoring separate filings.

## Item 7. Type of Filing

New Notice or Amendment; and either the Date of First Sale in this Offering or First Sale Yet to Occur. Determine the date as set out in `amendments-and-deadlines.md`. A notice may be filed early, before any sale, with First Sale Yet to Occur. A later sale does not by itself require an amendment, but any amendment filed afterward must give the actual date of first sale and current information in every item. If the prior notice is unconfirmed on EDGAR (`edgar-access.md`), the New Notice or Amendment choice is a Source conflict row showing both paths and their deadlines.

## Item 8. Duration of Offering

Answer whether the issuer intends the offering to last more than one year. For funds, use the offering period and final-closing window in the offering documents; an initial closing followed by subsequent closings over a longer window can mean Yes.

## Item 9. Type(s) of Securities Offered

Select all that apply: Equity; Debt; Option, Warrant or Other Right to Acquire Another Security; Security to be Acquired Upon Exercise of Option, Warrant or Other Right to Acquire Security; Pooled Investment Fund Interests; Tenant-in-Common Securities; Mineral Property Securities; Other (describe). Fund interests are Pooled Investment Fund Interests.

## Item 10. Business Combination Transaction

Yes or No: whether the offering is made in connection with a business combination such as a merger, acquisition or exchange offer, with a Clarification of Response. Ordinary fund offerings answer No; confirm from the offering documents.

## Item 11. Minimum Investment (decision framework)

Field: minimum investment accepted from any outside investor. The form's instruction: if the offering has a minimum that can be waived, give the lowest amount below which a waiver will not be granted; if there is no minimum, enter 0. Staff interpretation (Securities Act Forms C&DI 130.03): where the issuer may waive any required minimum, the answer is 0 because there is effectively no minimum. `[VERIFY]` the wording of both before quoting them in a client memo. There is no clarification field, so the reasoning goes in Section 4, every time.

Do not jump from "the general partner may waive the minimum" to 0, and do not report the stated minimum when it has been waived. Answer four questions and record each answer with its source:

1. **Stated minimum.** The amount in the offering document and in the governing document, and whether they agree.
2. **Waiver authority.** Who may accept less, on what conditions (sole discretion; a stated class of investors; advisory committee consent), and whether the authority can itself be changed without investor consent.
3. **Non-waivable floor.** Any amount below which the governing document, the offering document, a side letter, or a written issuer policy says no commitment will be accepted from an outside investor. A floor in the governing or offering document binds. A floor in an internal policy counts only if the issuer confirms it is the amount below which it will not grant a waiver.
4. **Accepted below-minimum subscriptions.** Each accepted commitment below the stated minimum: the amount, whether the investor is an outside investor (defined below), and the authority used. A low accepted amount is evidence of practice; it does not by itself set the floor.

Then present, in Section 4, each reading the record supports, a recommendation, and the confirmation required:

- A documented floor, not breached for any outside investor: recommend the floor; confirm that no outside investor below it has been or will be accepted.
- Unrestricted discretion with no floor anywhere, or a practice of waiving to any amount: recommend 0 under C&DI 130.03. Alternative: a policy floor, if the issuer confirms one.
- Unrestricted discretion on paper but a written policy floor the issuer applies: recommend the policy floor if the issuer confirms it will not waive below it; otherwise present the floor and 0 and ask.
- A documented floor breached for an outside investor: present the lowest accepted outside amount and 0, and ask whether the floor was changed or waived case by case.
- No waiver authority and no below-minimum acceptance: recommend the stated minimum.

State the recommended value, each alternative with its reading, what the issuer must confirm, and the consequence of each (for an amendment, a cumulative decrease of more than 10 percent requires a Form D/A; `amendments-and-deadlines.md`).

Outside investors exclude employees, officers, directors, general partners, trustees, consultants, advisors or vendors of the issuer, its parents and majority-owned subsidiaries, and (per staff interpretation) their immediate family members and controlled entities. A below-minimum commitment from such a person does not set the Item 11 figure; say so.

## Item 12. Sales Compensation

Fields per recipient: Recipient; Recipient CRD Number (or No CRD Number); (Associated) Broker or Dealer; its CRD Number (or No CRD Number); address; States of Solicitation (All States, Foreign/Non-US, or individual states).

List every person paid, directly or indirectly, any commission or similar compensation in connection with sales in the offering, including finders. A recipient need not have a CRD number to be listed. If more than five persons to be listed are associated with the same broker-dealer, enter only the broker-dealer. If there is no compensation, enter nothing in Item 12 and record the row as Not applicable with the agreement or confirmation relied on.

Take CRD numbers from BrokerCheck or the placement agreement, never from memory, and confirm each on BrokerCheck or IAPD with the lookup outcome recorded as in `edgar-access.md`; a number from the agreement that could not be confirmed is an Unverified external lookup row. For each recipient, complete the placement agent cross-check matrix in `output-template.md` Section 5 for every investor; a gap exists only where the recipient introduced the investor and the investor's state is outside the registered-states exhibit. States of Solicitation are the states where the recipient actually solicited or introduced investors (from the matrix) plus any it intends to solicit; a state where it solicited without registration is still listed here, with the gap routed, because the registered-states exhibit is not the answer to this field. Adding a new recipient requires an amendment; a change in an Item 12 address or in the states of solicitation does not.

## Item 13. Offering and Sales Amounts

Fields: (a) Total Offering Amount or Indefinite; (b) Total Amount Sold; (c) Total Remaining to be Sold or Indefinite; Clarification of Response.

- Amounts include all consideration, including cash to be paid in the future under mandatory capital commitments. For a fund, Total Amount Sold is the aggregate of commitments from accepted subscriptions, as amended by executed amendments, not capital called or paid. It is the sum of the investor reconciliation table's executed amounts, computed here; never a single figure copied from a ledger, closing memo or client email. A ledger total that differs from the sum is a Section 2 conflict with the executed documents controlling.
- Amounts are aggregate historic amounts since the start of the offering.
- Select Indefinite only if the amount cannot be determined or calculated now. If an amount is definite but hard to calculate, give a good-faith estimate. Total Offering Amount must be greater than zero.
- Compute (a), (b) and (c) for each issuer first, from that issuer's own executed documents, using the issuer calculation schedule in `fund-structures.md`. Show the arithmetic check (a) minus (b) equals (c) for each issuer, or name the expressly adopted treatment that explains why it does not hold (Indefinite; a shared cap reported in full on each issuer; Regulation S sales excluded from (b)). Any other difference is an error.
- For a multi-vehicle program, report the program cap with a clarification, a per-vehicle allocation, or Indefinite, under the conditions for using a program total in an issuer's field set out in `fund-structures.md`. Follow the issuer's prior-filing approach unless there is a reason to change, and explain any change.
- Offshore and Regulation S sales: an Issuer election between Regulation D sales only and all sales, with a clarification and consistent with prior filings. When any Regulation S sale exists, show 13(b) in both variants with the recommended one marked (`fund-structures.md`).

## Item 14. Investors

Fields: whether securities have been or may be sold to persons who are not accredited investors, and the number of non-accredited investors who have already invested; and the total number of investors who have already invested.

The numbers are historic totals regardless of whether investors still hold. Count per issuer first, by investor name in the worksheet (names stay out of the filing), with the feeder, master and Regulation S treatment in `fund-structures.md`: a feeder fund that invests into a main fund is one investor in the main fund; do not count the feeder's own investors at the program level. There is no clarification field here, so record the counting approach in the memo, and put any cross-reference the reader needs in the Item 13 clarification. When any Regulation S sale exists, show the count in both variants (Regulation D only; all sales). If any investor is non-accredited, or a questionnaire conflicts with the exemption, the exclusion or the ledger, stop and follow the write-up in `fund-structures.md`; show the counts under each outcome.

## Item 15. Sales Commissions and Finders' Fees Expenses

Fields: Sales Commissions $ (with Estimate box); Finders' Fees $ (with Estimate box); Clarification of Response. Give amounts separately; check Estimate when the amount is not known. The amounts may be given as subject to future contingencies. Compute the amount per issuer as the placement agreement's rate times the executed amounts of the agent-introduced investors in that issuer's investor reconciliation table (`fund-structures.md`); a fee figure in a ledger or closing memo is a cross-check, never the source, so an overstated ledger commitment never reaches Item 15. Report commissions and finder's fees associated with sales in the offering even when the adviser or another party pays them: Item 15 is not limited to payments from offering proceeds (SEC Securities Act Forms C&DI 130.08). Explain the payer and basis in the clarification. Do not report $0 solely because the issuer pays nothing, or copy a prior filing's $0 when the current documents show fees. Escalate the discrepancy, and assess whether the prior notice requires correction under Rule 503.

## Item 16. Use of Proceeds

Field: the amount of gross proceeds that has been or is proposed to be used for payments to any person required to be named as an executive officer, director or promoter in Item 3, with an Estimate box and a Clarification of Response. This is the only use-of-proceeds disclosure on the form. Whether and how to report fund management fees or carried interest paid to a related-person general partner is not addressed in the form's instructions `[VERIFY]`; present the choices as an Issuer election, follow the issuer's prior approach where there is one, and explain it in the clarification.

## Signature and Submission

Fields: Issuer(s); Name of Signer; Signature; Title; Date; number of continuation pages attached. For each issuer, identify the person signing, the capacity (in Title), and the authority the signer relies on (a board or manager resolution, the partnership agreement's authorization of the general partner and its signatories, an incumbency certificate). If one person signs for several co-issuers, the online form includes a statement that the signer is a duly authorized representative of the other issuers; confirm the signer holds that authority for each.

The form's terms of submission include certifications that the issuer is not disqualified under Rule 504(b)(3) or Rule 506(d) and a consent to service of process. The signer therefore certifies the bad actor position; do not present the form as ready for signature until `bad-actor-disqualification-review` has run on the complete hand-off. A manually signed authentication document for each issuer must be retained for five years.
