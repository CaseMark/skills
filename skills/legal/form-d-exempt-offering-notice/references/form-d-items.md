# Form D Items 1-16 and Signature

Use the form's own item numbers and field labels. For each item, populate from the highest-ranked source (see `source-reconciliation.md`), cite it, and record confidence as High (read directly from an executed or governing document), Medium (read from a lower-ranked source and consistent), or Low (inferred, conflicting or missing).

**Clarification of Response** fields exist only on Item 3 (one per related person), Item 10, Item 13, Item 15 and Item 16. Each is limited to 255 characters and is public. Items 1, 2, 4-9, 11, 12, 14 and the signature block have no clarification field; record judgment calls on those items in the memo, not in the filing.

## Item 1. Issuer's Identity

Fields: Name of Issuer; Jurisdiction of Incorporation/Organization; Year of Incorporation/Organization; Previous Name(s) (or None); Entity Type; CIK.

- Name: the exact legal name in the formation document (certificate of limited partnership, certificate of formation, certificate of registration), not the marketing name.
- Year of Incorporation/Organization: one of Over Five Years Ago; Within Last Five Years (specify year); Yet to Be Formed.
- Entity Type: Corporation; Limited Partnership; Limited Liability Company; General Partnership; Business Trust; Other (specify). A non-U.S. vehicle may not map cleanly (for example, a Cayman exempted limited partnership); choose the closest type, or Other (specify), and record the choice as a judgment call in the memo. `[VERIFY]` which EDGAR accepts for the specific vehicle.
- CIK: retrieve from EDGAR. If the issuer has none, mark MISSING and route to the Form ID path (`edgar-access.md`). If a CIK supplied by the client returns no result or a different entity on EDGAR, say so and do not use it.
- Multiple issuers: when more than one issuer sold securities in the same offering, they may be identified on one filing. Check the multiple-issuer box, identify a primary issuer (the most important issuer in the offering) in the first fields, and add each other issuer on Items 1 and 2 continuation pages. Some states require a separate filing for each issuer. Whether to use one filing or several is a judgment call (see `fund-structures.md`).

## Item 2. Principal Place of Business and Contact Information

Fields: Street Address 1 and 2; City; State/Province/Country; ZIP/Postal Code; Phone No. For a fund, use the address in the offering or governing documents for the issuer's principal place of business, which is often the general partner's or manager's office and not the registered office. If they differ, say which you used.

## Item 3. Related Persons

Fields per person: Last, First, Middle Name; Street Address; Relationship(s) (Executive Officer, Director, Promoter); Clarification of Response (if necessary).

List each executive officer and director of the issuer, each person performing similar functions (title alone is not determinative; the form's examples are general and managing partners of partnerships and managing members of limited liability companies), and each person who has functioned directly or indirectly as a promoter within the past five years of the later of the first sale or the date the filing was required. Ten percent owners are not required.

For a fund, take the list from the governing documents in effect on the filing date. See `fund-structures.md` for the fund-specific rules and the source priority. Each person gets one row with the relationship checkbox that applies. Use the clarification field to explain capacity where the checkbox alone would mislead (for example, an entity general partner entered in the name fields, or an individual who is a managing member of the general partner).

Adding a related person after a filing requires an amendment. A change only in the address or relationship of a person already listed does not.

## Item 4. Industry Group

Select one. Funds select Pooled Investment Fund (under Banking & Financial Services), then one fund type: Hedge Fund, Private Equity Fund, Venture Capital Fund or Other Investment Fund, and answer whether the issuer is registered as an investment company under the Investment Company Act of 1940 (a fund relying on Section 3(c)(1) or 3(c)(7) answers No). Operating companies select the industry group that fits the business. The fund type drives Item 5, so choose it from the offering documents' description of the strategy and record the basis.

## Item 5. Issuer Size

Select one range.

- Operating companies, Private Equity Funds and Venture Capital Funds: the Revenue Range (No Revenues; $1-$1,000,000; $1,000,001-$5,000,000; $5,000,001-$25,000,000; $25,000,001-$100,000,000; Over $100,000,000; Decline to Disclose; Not Applicable) for the most recently completed fiscal year, or the range to date if no full fiscal year exists. If the business is not intended to produce revenue, the form says to enter Not Applicable.
- Hedge Funds and Other Investment Funds: the Aggregate Net Asset Value Range (No Aggregate Net Asset Value; $1-$5,000,000; $5,000,001-$25,000,000; $25,000,001-$50,000,000; $50,000,001-$100,000,000; Over $100,000,000; Decline to Disclose; Not Applicable) as of the most recent practicable date.

Do not apply the NAV range to a private equity or venture capital fund. Foreign issuers state revenue in U.S. dollars. Declining to disclose is the issuer's choice; do not select it without client instruction.

## Item 6. Federal Exemptions and Exclusions Claimed

Select all that apply: Rule 504(b)(1) (not (i), (ii) or (iii)), 504(b)(1)(i), 504(b)(1)(ii), 504(b)(1)(iii); Rule 506(b); Rule 506(c); Securities Act Section 4(a)(5); and Investment Company Act Section 3(c) with the specific paragraph. The form lists paragraphs (1), (2), (3), (4), (5), (6), (7), (9), (10), (11), (12), (13) and (14) (there is no 3(c)(8) box).

- A single submission cannot claim both Rule 506(b) and Rule 506(c). If co-issuers rely on different rules, file separately.
- Choose the Section 3(c) paragraph from the offering and governing documents, and test it against the investor qualification evidence (Step 5 of the workflow). A fund that claims 3(c)(7) is represented to be owned exclusively by qualified purchasers, subject to the statutory and rule carve-outs.
- If co-issuers rely on different 3(c) paragraphs, the form cannot attribute a paragraph to a particular issuer on one filing. Treat this as a judgment call favoring separate filings.

## Item 7. Type of Filing

New Notice or Amendment; and either the Date of First Sale in this Offering or First Sale Yet to Occur. Determine the date as set out in `amendments-and-deadlines.md`. A notice may be filed early, before any sale, with First Sale Yet to Occur. A later sale does not by itself require an amendment, but any amendment filed afterward must give the actual date of first sale and current information in every item.

## Item 8. Duration of Offering

Answer whether the issuer intends the offering to last more than one year. For funds, use the offering period and final-closing window in the offering documents; an initial closing followed by subsequent closings over a longer window can mean Yes.

## Item 9. Type(s) of Securities Offered

Select all that apply: Equity; Debt; Option, Warrant or Other Right to Acquire Another Security; Security to be Acquired Upon Exercise of Option, Warrant or Other Right to Acquire Security; Pooled Investment Fund Interests; Tenant-in-Common Securities; Mineral Property Securities; Other (describe). Fund interests are Pooled Investment Fund Interests.

## Item 10. Business Combination Transaction

Yes or No: whether the offering is made in connection with a business combination such as a merger, acquisition or exchange offer, with a Clarification of Response. Ordinary fund offerings answer No; confirm from the offering documents.

## Item 11. Minimum Investment

Field: minimum investment accepted from any outside investor. If the offering has a minimum that can be waived, the form's instruction says to give the lowest amount below which a waiver will not be granted. If there is no minimum, enter 0. A staff interpretation says that where an issuer may waive any required minimum, the answer is zero because there is effectively no minimum. These are reconcilable: use the stated floor if the documents set one, and 0 if the GP's waiver discretion has no floor. `[VERIFY]` the wording of the instruction and the staff interpretation before citing either in a client memo.

Outside investors exclude employees, officers, directors, general partners, trustees, consultants, advisors or vendors of the issuer, its parents and majority-owned subsidiaries, and (per staff interpretation) their immediate family members and controlled entities. If the GP accepted a commitment below the stated minimum from an outside investor, flag the Item 11 judgment call in the memo. There is no clarification field here.

## Item 12. Sales Compensation

Fields per recipient: Recipient; Recipient CRD Number (or No CRD Number); (Associated) Broker or Dealer; its CRD Number (or No CRD Number); address; States of Solicitation (All States, Foreign/Non-US, or individual states).

List every person paid, directly or indirectly, any commission or similar compensation in connection with sales in the offering, including finders. A recipient need not have a CRD number to be listed. If more than five persons to be listed are associated with the same broker-dealer, enter only the broker-dealer. If there is no compensation, enter nothing in Item 12.

Take CRD numbers from BrokerCheck or the placement agreement; never guess. For each recipient, compare the states where it solicited or introduced investors against the states in which it is registered, using the investor list and the placement agent's registered-states exhibit. A mismatch goes to `blue-sky-filings`. Adding a new recipient requires an amendment; a change in an Item 12 address or in the states of solicitation does not.

## Item 13. Offering and Sales Amounts

Fields: (a) Total Offering Amount or Indefinite; (b) Total Amount Sold; (c) Total Remaining to be Sold or Indefinite; Clarification of Response.

- Amounts include all consideration, including cash to be paid in the future under mandatory capital commitments. For a fund, Total Amount Sold is the aggregate of commitments from accepted subscriptions, not capital called or paid.
- Amounts are aggregate historic amounts since the start of the offering.
- Select Indefinite only if the amount cannot be determined or calculated now. If an amount is definite but hard to calculate, give a good-faith estimate. Total Offering Amount must be greater than zero.
- For a multi-vehicle program, report the program cap with a clarification, a per-vehicle allocation, or Indefinite. Follow the issuer's prior-filing approach unless there is a reason to change, and explain any change.
- Offshore and Regulation S sales: report either Regulation D sales only or all sales, with a clarification, and be consistent with prior filings. See `fund-structures.md`.

## Item 14. Investors

Fields: whether securities have been or may be sold to persons who are not accredited investors, and the number of non-accredited investors who have already invested; and the total number of investors who have already invested.

The numbers are historic totals regardless of whether investors still hold. A feeder fund that invests into a main fund is one investor in the main fund; do not count the feeder's own investors at the program level. There is no clarification field here, so record the counting approach in the memo, and put any cross-reference the reader needs in the Item 13 clarification. If any investor is non-accredited, stop and follow the escalation in `fund-structures.md`.

## Item 15. Sales Commissions and Finders' Fees Expenses

Fields: Sales Commissions $ (with Estimate box); Finders' Fees $ (with Estimate box); Clarification of Response. Give amounts separately; check Estimate when the amount is not known. The amounts may be given as subject to future contingencies. Report commissions and finder's fees associated with sales in the offering even when the adviser or another party pays them: Item 15 is not limited to payments from offering proceeds (SEC Securities Act Forms C&DI 130.08). Explain the payer and basis in the clarification. Do not report $0 solely because the issuer pays nothing, or copy a prior filing's $0 when the current documents show fees. Escalate the discrepancy, and assess whether the prior notice requires correction under Rule 503.


## Item 16. Use of Proceeds

Field: the amount of gross proceeds that has been or is proposed to be used for payments to any person required to be named as an executive officer, director or promoter in Item 3, with an Estimate box and a Clarification of Response. This is the only use-of-proceeds disclosure on the form. Whether and how to report fund management fees or carried interest paid to a related-person general partner is not addressed in the form's instructions `[VERIFY]`; follow the issuer's prior approach and explain it in the clarification.

## Signature and Submission

Fields: Issuer(s); Name of Signer; Signature; Title; Date; number of continuation pages attached. For each issuer, identify the person signing, the capacity (in Title), and the authority the signer relies on (a board or manager resolution, the partnership agreement's authorization of the general partner and its signatories, an incumbency certificate). If one person signs for several co-issuers, the online form includes a statement that the signer is a duly authorized representative of the other issuers; confirm the signer holds that authority for each.

The form's terms of submission include certifications that the issuer is not disqualified under Rule 504(b)(3) or Rule 506(d) and a consent to service of process. The signer therefore certifies the bad actor position; do not present the form as ready for signature until `bad-actor-disqualification-review` has run. A manually signed authentication document for each issuer must be retained for five years.
