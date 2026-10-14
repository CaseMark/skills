# EDGAR Access, Filing Mechanics and Retention

A Form D cannot be filed for an issuer that has no CIK, and since the EDGAR Next transition no one can file without an individual Login.gov credential and a role on the filer's account. For a new issuer this is on the critical path against the 15-day deadline.

## Step 1: Establish whether each issuer has a CIK

For every issuer, look up the CIK supplied in the documents or by the client on EDGAR (company search, or the SEC's submissions data by CIK). Confirm the name on EDGAR matches the issuer. Outcomes:

- Match found: record the CIK and the EDGAR name.
- Nothing found for a supplied CIK: report "CIK <number> not found on EDGAR" plainly, treat the issuer as having no confirmed CIK, and do not propose a different entity.
- A different entity: report the mismatch, and do not use the CIK.
- No lookup possible in this environment: mark the CIK UNVERIFIED and list the lookup as an open item.

A law firm's own CIK is not the issuer's CIK.

**A failed lookup is not a "not found".** Report "not found" only when EDGAR returns an affirmative no-match (for example a 404 or "no such key" from the SEC's submissions data, or "No matching CIK" from the company page). If a request is blocked, rate-limited or times out, say the lookup failed, try another route (the SEC's submissions data by CIK, EDGAR full-text or entity search, or a web-fetch tool), and mark the CIK UNVERIFIED if none works. The SEC asks automated clients to identify themselves in the User-Agent header and to stay within its rate limits; some pages reject anonymous clients. Use your organization's identification, not an individual's personal details.

**The prior notice's own CIK cannot be found.** If the CIK or accession number on a prior Form D does not exist on EDGAR, treat the prior notice as unconfirmed. Ask the client for the EDGAR acceptance email or the filing index. If no prior notice exists on EDGAR, the filing is not an amendment: the issuer may have no CIK and need a Form ID, and the notice is a late new notice measured from the original date of first sale. Present both possibilities, make it a Critical blocking issue, and do not draft the amendment as final until it is resolved.

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
- State notice filings run through each state's process, commonly the NASAA Electronic Filing Depository. Timing and fees vary by state and are not set by federal rule `[VERIFY]`; route them to `blue-sky-filings`.

## XML on request

If the user asks for XML, produce it against the current Form D XML Technical Specification and its schema, and take every element name and allowed value from the specification and schema, never from memory. The SEC's technical specifications page lists a version dated September 20, 2021, while the specification file linked from that page is headed with a March 2025 version number; cite both and use the newer file `[VERIFY]`. Label any XML you produce: "Requires validation in the EDGAR test environment before live submission." XML can be submitted as a TEST submission by setting the test indicator; the online Form D application has no documented test selector `[VERIFY]`. Never present XML as ready for a live filing.

## Signature, authority and retention

Every notice must be signed by a person duly authorized by the issuer. The signer's capacity goes in the Title field, and the authority relied on (resolution, partnership agreement authorization, incumbency certificate) should be cited in the draft. Each issuer must retain the manually signed authentication document for five years. The signer certifies the issuer is not disqualified under Rule 504(b)(3) or Rule 506(d), so bad actor diligence must be complete first.

## Public and permanent

Form D, including clarification text, is publicly available on EDGAR and generally cannot be withdrawn. No confidential treatment is available for any information the form requires.
