# Expectations that apply to every test

Each test's expected-behavior file adds to these. A test passes only when every "Must" line in this file and in its own file is satisfied and no "Must not" line is breached. Grade each line pass or fail; record the evidence (section and quote) for each.

## Must

- Output has the header and Sections 1 through 6 in order, and closes with "Draft for attorney review. This is not a filing-ready submission."
- The header contains a source-review register with one row per file in the test's inventory (every file named in the folder listing, including the email and every workbook sheet), each with a status from: Reviewed, Not relevant, Unreadable after attempt, Still needed.
- Every file in a must-review category (subscriptions, questionnaires, bad actor questionnaires and certifications, LPA and GP agreement, PPM and supplements, register, closing memo, prior filing, placement agreement) is Reviewed, or is Unreadable after attempt with the method tried, or is Still needed with the supplier named.
- Section 1 shows the date-of-first-sale computation in the fixed three-line format with weekdays, based on the General Partner's acceptance (countersignature) date under Subscription Agreement s. 2 and LPA s. 3.3, not the closing memo or register date.
- Section 1 contains an identifier lookup register with one row per identifier (each issuer's CIK, any accession number, each CRD number) and an outcome from: Confirmed match, Affirmative no-match, Different entity returned, Lookup blocked or failed, Not checked, with the route and the evidence returned.
- Section 3 is a worksheet with every field of Items 1 through 16 and the signature block, each with a proposed value or the open choices, source, confidence, confirmation needed, consequence if changed, and a status (Settled, Unknown fact, Issuer election, Not applicable, Unverified external lookup, Source conflict).
- Item 5 for the newly formed fund is presented as open choices with a recommendation (not as an unknown), and Item 11 appears in Section 4 with the four-question analysis, a recommended value, alternatives and the issuer confirmation required.
- Item 15 reports Brightwater's commissions computed from the placement agreement rate and the commissionable base, marked estimate, with the Investment Manager as payer in the clarification; it is not $0.
- Section 5 hand-off to `blue-sky-filings` lists each state with the investors there, the date of first sale to a resident of that state, the placement agent's registration status in that state, and the Arizona gap (Sorrel Point introduced by Brightwater; Arizona absent from Exhibit C) where Sorrel Point is in the matter.
- Section 5 hand-off to `bad-actor-disqualification-review` lists each covered person with questionnaire status and sale dates, and notes whether a closing bring-down certification from Brightwater (Placement Agreement s. 6.1) is in the matter.
- Section 6 has an open-items table in which every row has an owner and a next action.
- Every ledger value used was compared with the executed document and every difference is written up.

## Must not

- Use the word "MISSING" as a field value or status.
- Describe any inventoried file as missing, unavailable or outstanding without an Unreadable after attempt or Still needed row that states the attempt or the supplier.
- Use September 18, 2026 as the date of first sale for Larkspur Growth Partners III, L.P. where Meridian's acceptance is September 16, 2026.
- Include any field that is not on Form D (SIC code, website, price per unit, use-of-proceeds categories, escrow, financial condition).
- Present a provisional or conflicted value as Settled, or state a filing is ready to submit.
- Put clarification text on any item other than 3, 10, 13, 15 and 16, or exceed 255 characters.
- Report a failed or blocked lookup as a no-match, or an affirmative no-match as "unverified".
