# EDGAR Access, Identifier Lookups, Filing Mechanics and Retention

A Form D cannot be filed for an issuer that has no CIK, and since the EDGAR Next transition no one can file without an individual Login.gov credential and a role on the filer's account. For a new issuer this is on the critical path against the 15-day deadline.

## Step 1: Look up every external identifier and record the outcome

This step covers every external identifier the draft relies on: each issuer's CIK, the accession number and file number of any prior notice, and the CRD number of each sales compensation recipient and its associated broker-dealer. Run the appropriate primary lookup for each and record the outcome in the vocabulary below. The register goes in Section 1 of the output (`output-template.md`).

**Primary lookups.** CIK and entity name: EDGAR company search, or the SEC's submissions data by CIK (which returns the entity's filing history, or an affirmative error for a CIK that does not exist). Prior notice: the filing index for the accession number, or the issuer's filing list on EDGAR. CRD: FINRA BrokerCheck for broker-dealers and their associated persons, the SEC's IAPD for advisers. EDGAR full-text search is a secondary route; its silence is not a no-match. A law firm's own CIK is not the issuer's CIK. The SEC asks automated clients to identify themselves in the User-Agent header and to stay within its rate limits; some pages reject anonymous clients. Use your organization's identification, not an individual's personal details.

**Outcomes.** Record exactly one per identifier, with the route used, the date and time, and what the system returned:

| Outcome | Meaning | Evidence required | Consequence |
|---|---|---|---|
| Confirmed match | The identifier resolves to the named issuer or person | The returned name and identifier beside the document's | Use it |
| Affirmative no-match | The system answered and reported that the identifier or name does not exist | The error or empty result as returned (a 404 or "no such key" from the submissions data; "No matching CIK" or an empty result from company search; "no results" from BrokerCheck) | Do not use the identifier. Treat the issuer as having no confirmed CIK (Form ID path). Treat a prior notice whose accession number or CIK returns no-match as unconfirmed; the filing cannot be drafted as an amendment until it is |
| Different entity returned | The identifier resolves, but to an entity other than the one in the documents | The returned name beside the document's name | Do not use the identifier; raise a client question; never adopt the returned entity |
| Lookup blocked or failed | No answer: the request was blocked, rate-limited, timed out, or this environment has no network access | The error as returned, and each alternative route tried | Status UNVERIFIED; open item with an owner; the draft presents both consequences (identifier exists; identifier does not exist) |
| Not checked | No lookup was attempted | The reason | Status UNVERIFIED; must be checked before filing |

Two rules follow. A failed lookup is never reported as "not found"; it is reported as failed, with the routes tried, and another route is attempted before it is recorded. An affirmative no-match is never softened into "unverified" or "could not be confirmed"; it is reported as a no-match with the evidence, because it changes the filing determination.

**Synthetic, training or fictional identifiers.** If the matter appears to use fictional identifiers (a CIK outside the range EDGAR has issued, an issuer name that returns nothing on any route, placeholder numbers, or a matter labelled as training or synthetic), still run the lookups and report the result as it came back. Then explain the filing consequence on those facts: no confirmed CIK means the Form ID path; an unconfirmed prior notice means the filing cannot be drafted as an amendment. Never substitute a real entity with a similar name, and never present a real entity's identifier as the issuer's.

**The prior notice's own CIK or accession number cannot be confirmed.** If the CIK or accession number on a prior Form D returns an affirmative no-match, treat the prior notice as unconfirmed. Ask the client for the EDGAR acceptance email or the filing index. If no prior notice exists on EDGAR, the filing is not an amendment: the issuer may have no CIK and need a Form ID, and the notice is a late new notice measured from the original date of first sale. Present both possibilities with the deadline and consequences of each, make it a Critical blocking issue, and do not draft the amendment as final until it is resolved. If the lookup failed rather than returned a no-match, present the same two possibilities, mark the identifier UNVERIFIED, and name the route that will settle it.

## Step 2: New issuers apply through Form ID

An issuer with no CIK applies on the EDGAR Filer Management dashboard through the amended Form ID. Paper applications are not accepted. Points to put in front of the attorney:

- **Account administrators.** The applicant must authorize and maintain at least two account administrators, except that an individual or single-member company must maintain at least one. Each administrator uses an individual Login.gov account with multifactor authentication. An account administrator cannot also be a user.
- **Notarized authenticating document.** Form ID requires a signed authenticating document, signed by an authorized individual of the applicant and notarized (manual, electronic or remote online notarization). A notarized power of attorney is needed when an account administrator is not employed by the applicant or its affiliates (a law firm or filing agent, for example) or when an individual or single-member company authorizes another person.
- **Login.gov is not entity access.** An individual's Login.gov account does not give filing access for an entity. The individual must also hold a role for that filer, assigned by an account administrator on the dashboard.
- **Timing.** SEC staff review each Form ID. The SEC's published average review time is four business days (excluding federal holidays), and approval is not assured. Submission is available 6:00 a.m. to 10:00 p.m. Eastern on business days. Do not promise a CIK date. If the due date is within about five business days and an issuer has no CIK, state that the deadline is at risk, escalate, and recommend starting immediately.

## Step 3: Recommend delegation to the law firm

Recommend that the issuer delegate filing authority to the law firm's EDGAR account. Delegation lets a filer authorize its law firm, filing agent, broker-dealer or related entity to file on its behalf. The issuer's account administrator delegates on the dashboard, the firm's administrator accepts, and the issuer may cancel at any time. The issuer must have its own CIK and account before it can delegate, and it still has to maintain its own account administrators. Ask who at the firm will be the delegated administrator and who at the issuer will be the account administrators.

## Step 4: Filing mechanics

- Form D is filed through the EDGAR Online Forms application, or as XML conforming to the SEC's Form D XML Technical Specification. Submission types are D and D/A. There is no federal filing fee and no paper filing.
- The filer needs the CIK and the CIK confirmation code (CCC) for the primary issuer and for each additional issuer. A session expires one hour after the last keystroke, so assemble every value before starting.
- On submission EDGAR sends notification emails with the accession number. Record the accession number; never predict it.
- State notice filings run through each state's process, commonly the NASAA Electronic Filing Depository. Timing and fees vary by state and are not set by federal rule `[VERIFY]`; route them to `blue-sky-filings` with the hand-off contents in `output-template.md`.

## XML on request

If the user asks for XML, produce it against the current Form D XML Technical Specification and its schema, and take every element name and allowed value from the specification and schema, never from memory. The SEC's technical specifications page lists a version dated September 20, 2021, while the specification file linked from that page is headed with a March 2025 version number; cite both and use the newer file `[VERIFY]`. Label any XML you produce: "Requires validation in the EDGAR test environment before live submission." XML can be submitted as a TEST submission by setting the test indicator; the online Form D application has no documented test selector `[VERIFY]`. Never present XML as ready for a live filing.

## Signature, authority and retention

Every notice must be signed by a person duly authorized by the issuer. The signer's capacity goes in the Title field, and the authority relied on (resolution, partnership agreement authorization, incumbency certificate) should be cited in the draft. Each issuer must retain the manually signed authentication document for five years. The signer certifies the issuer is not disqualified under Rule 504(b)(3) or Rule 506(d), so bad actor diligence must be complete first.

## Public and permanent

Form D, including clarification text, is publicly available on EDGAR and generally cannot be withdrawn. No confidential treatment is available for any information the form requires.
