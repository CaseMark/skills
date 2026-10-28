# Expected behavior: Test 08, affirmative EDGAR no-match

## Must

- The identifier lookup register reports, for CIK 0009876543, the route (the SEC's submissions data by CIK and/or EDGAR company search), the evidence returned (an HTTP 404 or equivalent no-such-entity response), and the outcome Affirmative no-match. For the issuer name, EDGAR company search returning no filer is reported as Affirmative no-match. For accession number 0009876543-26-000001, the filing index lookup is reported with its outcome.
- CRD numbers 8899001 (Brightwater) and 7712345 (Ortiz) are looked up on BrokerCheck and the outcome reported as returned (Affirmative no-match or Lookup blocked or failed), with the consequence for Item 12 (Unverified external lookup rows carrying the agreement values).
- The output states that the identifiers may be fictional or placeholder values and still reports the lookup results and their filing consequence; it does not propose any real entity as the issuer.
- Section 1 presents both filing paths with deadlines: (A) if the July 2, 2026 notice exists under a CIK the client can evidence (EDGAR acceptance message or filing index from Thornfield LLP), a Form D/A is required as soon as practicable because the cap increase from $200,000,000 to $250,000,000 is a 25 percent increase (over the 10 percent exception), with Item 7 Amendment and the June 17, 2026 date of first sale, and the annual amendment date of July 2, 2027 would reset on filing; (B) if no notice exists, the issuer has no CIK (Form ID required) and the filing is a late new notice: date of first sale June 17, 2026 (Wednesday), raw day 15 July 2, 2026 (Thursday), due July 2, 2026 (Thursday), not rolled, past due by 84 days as of September 24, 2026, with the late-filing escalation and the state-notice consequence routed to `blue-sky-filings`.
- The prior notice is treated as unconfirmed: a Critical blocking issue with the owner (client and Thornfield LLP) and next action (produce the EDGAR acceptance message, or confirm no filing was made); the Item 7 row is a Source conflict showing both paths.
- The purported prior filing's contents are compared with the current documents: Item 12 states of solicitation (MA, NY, OH, TX) versus Exhibit C; Item 15 $0 versus the placement agreement (correct for the June closing with a direct investor, $500,000 now); Item 11 $5,000,000 versus the waiver authority (judgment call); Item 5 Decline to Disclose as the issuer's election.
- Current figures: Item 13 $250,000,000 / $91,000,000 / $159,000,000; Item 14 five investors, zero non-accredited; Item 15 $500,000.

## Must not

- Describe the 404 or empty-search result as "unverified", "could not be confirmed" or "inconclusive".
- Substitute, suggest or look up a different real entity as the issuer, or present any real CIK.
- Draft the filing as an amendment without presenting the late-new-notice path and its deadline.
