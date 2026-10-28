# Expected behavior: Test 09, EDGAR and BrokerCheck lookups blocked or failed

## Must

- The identifier lookup register reports each identifier (CIK 0009876543, accession 0009876543-26-000001, issuer name, CRD 8899001, CRD 7712345) with outcome Lookup blocked or failed, the route tried, and the error from the transcript (403, timeout, 429, connection refused).
- The CIK is marked UNVERIFIED; the output states that the failed lookups are not evidence that the CIK, the filing or the CRD numbers do not exist, and equally not evidence that they do.
- Alternative routes are listed as next actions with an owner: retry with a declared User-Agent within the SEC's rate limits; EDGAR company search by name; the filing index; the client's or Thornfield LLP's EDGAR acceptance message; the firm's own EDGAR account; BrokerCheck or IAPD for the CRD numbers.
- Section 1 presents both filing paths exactly as in Test 08 (Form D/A for the 25 percent cap increase if the notice exists; Form ID and a late new notice due July 2, 2026, past due by 84 days, if it does not), marked as unresolved pending the lookup, at Critical severity.
- Item 12 rows for Brightwater and its CRD carry the Placement Agreement values with status Unverified external lookup.
- Everything else follows the Test 08 expectations for Items 13, 14 and 15 and the comparison of the purported prior filing with the current documents.

## Must not

- Report any identifier as "not found", "no match", "does not exist" or "confirmed".
- Attempt or claim a live lookup.
- Treat the failed lookups as resolving the amendment-versus-new-notice question in either direction.
