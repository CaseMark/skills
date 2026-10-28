# Filing Package: Draft XML, Online Forms Keying Sheet and Pre-Submission Checklist

The filing package turns a reviewed memo into what the person who holds the EDGAR credentials needs: a draft submission XML built to the SEC's Form D XML Technical Specification, a screen-by-screen keying sheet for anyone filing through the EDGAR Online Forms application instead, and a checklist that runs from attorney sign-off through the live filing. It is produced only on request, it is built from the Section 3 worksheet and never from the documents directly, and it is never described as accepted, validated or ready for a live filing. This skill does not transmit anything.

Sources: EDGAR Form D XML Technical Specification (file headed Version 13, March 2025; schema files `formDSubmission.xsd.xml`, `formDStateCodes.xsd.xml`, `statesOfSolicitationCodes.xsd.xml`), downloaded as the "full specs" zip from https://www.sec.gov/submit-filings/technical-specifications; EDGAR Filer Manual Volume II, Version 78 (September 14, 2026), chapter 8 (sections 8.1.7 to 8.1.9, the online Form D screens) and chapter 9 (filer-constructed XML and test transmission). Re-download both before relying on an element name or a screen title; the SEC revises them.

## Contents

1. Trigger and preconditions
2. Part 0. Provenance table and placeholders
3. Part 1. Draft submission XML
4. Part 2. Online Forms keying sheet
5. Part 3. Pre-submission checklist
6. Local validation and the EDGAR test submission
7. Labels

## Trigger and preconditions

Produce the package when the user asks for the filing package, the XML, the keying sheet or the pre-submission checklist, or when the request for the memo says to include it, or when the user says the attorney has confirmed the memo and asks to prepare for filing. Without such a request, Steps 1 to 8 end with the memo.

The package depends on a completed memo (header and Sections 1 to 6) for the same matter: either produced in the same run or supplied by the user. Every value in the package is copied from a Section 3 worksheet row. If no memo exists, run Steps 1 to 8 first. If the memo is supplied, do not re-derive its values; where a worksheet row is absent for a field the XML needs, add the row to the memo, not a value to the XML.

One package per matter; within it, one XML file and one keying sheet per filing (co-issuers on one filing share one file), and one checklist that covers every filing.

## Part 0. Provenance table and placeholders

Open the package with one provenance table per filing: one row per XML element that carries a value (and so per keying-sheet field).

| XML element (path under edgarSubmission) | Keying-sheet screen and field | Value placed | Worksheet row (item, field) | Row status | Basis |
|---|---|---|---|---|---|
| | | | | Settled / Unknown fact / Issuer election / Not applicable / Unverified external lookup / Source conflict | Settled value / Recommended choice, confirm before live / Placeholder, filer supplies / Placeholder, blocked until the row is settled |

The basis column follows from the row status:

- **Settled**: the value is placed.
- **Issuer election**, or a Section 4 judgment call: the recommended value is placed and the basis says "Recommended choice, confirm before live"; the checklist carries the confirmation.
- **Unknown fact**, **Unverified external lookup**, **Source conflict**: a placeholder is placed, never the provisional value, and the row is listed under "XML blocked until" at the foot of the table with the owner and next action from Section 6.
- **Not applicable**: the element is omitted or left empty as the specification allows (an empty `salesCompensationList` when Item 12 is Not applicable).
- **Credentials and signature**: the CIK confirmation code (CCC), the submission contact, notification addresses, the typed signature and the signature date are always placeholders. The CCC is a credential and never appears in any output. The signature is the signer's act on the day of filing; EDGAR suspends a future signature date.

Placeholders take one form, `[[WHAT: for whom]]`, for example `[[CIK: Larkspur Growth Partners III, L.P.]]`, `[[CCC]]`, `[[SIGNATURE DATE]]`. The form is deliberate: any file still containing `[[` fails schema validation and cannot be transmitted by accident. The provenance table ends with the list of every placeholder in the file and who replaces it.

## Part 1. Draft submission XML

**Construction rules** (specification sections 3.2, 3.4, 5 and 6; violations suspend the filing):

1. Element names are case-sensitive and appear in the order of the skeleton below, which follows the schema's sequence. Include a container only when it has content, except `salesCompensationList`, which is mandatory and may be empty.
2. Take every element name, allowed value and code from the specification and schema files, never from memory. Codes for `stateOrCountry` are the two-character EDGAR codes in `formDStateCodes.xsd.xml` (U.S. states by postal abbreviation; countries by EDGAR code, for example E9 Cayman Islands, G7 Denmark, U0 Singapore, X0 United Kingdom); codes for `statesOfSolicitationList/state` are the 50 states, DC and PR. Enumerated values (entity type, relationship, industry group, fund type, revenue and net-asset-value ranges, exemption items such as `06b`, `06c`, `04.1`, `4a5`, `3C`, `3C.1`, `3C.7`) are copied exactly as the schema spells them.
3. Elements the specification marks for EDGAR to fill are omitted: `schemaVersion`, `entityName`, `jurisdictionOfInc`, `stateOrCountryDescription`, `edgarPreviousNameList`, and `description` under states of solicitation. EDGAR disseminates the name and jurisdiction on file for the CIK, so the checklist confirms the EDGAR company record before the live filing.
4. Elements typed as true-only (`isEstimate`, each `typesOfSecuritiesOffered` flag, the `yearOfInc` choices, `yetToOccur`, the over-100 flags) are included only when true and never written as `false`. True-or-false elements (`is40Act`, `isAmendment`, `moreThanOneYear`, `isBusinessCombinationTransaction`, `hasNonAccreditedInvestors`, `foreignSolicitation`, `authorizedRepresentative`) are always `true` or `false`.
5. Dollar amounts are whole numbers with digits only: no commas, dollar signs, decimals or spaces. `totalOfferingAmount` and `totalRemaining` may instead be `Indefinite`; otherwise `totalRemaining` equals `totalOfferingAmount` minus `totalAmountSold`. Dates are `YYYY-MM-DD`.
6. Lengths: street 40, city 30, ZIP or postal code 10, phone 20, first and middle name 150, last name 200, recipient and broker-dealer name 200, every clarification 255, `entityTypeOtherDesc` 255, contact name 30, e-mail 80, signature `issuerName` and `nameOfSigner` 150, `signatureName` 30, `signatureTitle` 60. Escape `&`, `<`, `>` and `"` as `&amp;`, `&lt;`, `&gt;`, `&quot;`. EDGAR stores every value except `signatureName` and `contactEmailAddress` in upper case.
7. A start tag, its value and its end tag stay on one line. The file ends in `.xml`, contains no stylesheet reference, and if it has an XML declaration that line is first with version `1.0`.
8. `submissionType` is `D` or `D/A`. A `D/A` sets `isAmendment` to `true` and gives `previousAccessionNumber` as the accession number of an accepted Form D of the same issuer, from the identifier lookup register with outcome Confirmed match; anything else is a placeholder. A `D` omits `previousAccessionNumber`.
9. `testOrLive` is `TEST` in every file this skill produces. The filer changes it to `LIVE` only for the live transmission; the tag, not the website link, decides how EDGAR processes the file.
10. Signatures: one `signature` block per issuer, in any order, each with `issuerName` exactly as EDGAR records the issuer's name (a mismatch suspends the filing); or one block for the primary issuer with `authorizedRepresentative` set to `true` when the signer is the duly authorized representative of every other issuer.
11. `issuerPreviousNameList` holds `<value>None</value>` or up to three `previousName` elements. `entityType` `Other` requires `entityTypeOtherDesc`. `yearOfInc` holds exactly one of `withinFiveYears` (with a four-digit `value`), `overFiveYears` or `yetToBeFormed`. `issuerSize` holds `aggregateNetAssetValueRange` only when the fund type is Hedge Fund or Other Investment Fund, otherwise `revenueRange`. `06b` and `06c` never appear together.
12. Business-rule warnings EDGAR issues even on a valid file, to be resolved in the memo rather than suppressed: a Rule 504 total offering amount above $10 million; more than 35 non-accredited investors under Rule 506(b); `3C` selected without `isPooledInvestmentFundType`; a $0 total offering amount.

**Skeleton** (a pooled fund, new notice, values from a worksheet; comments mark the alternatives):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<edgarSubmission xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="formDSubmission.xsd.xml">
  <submissionType>D</submissionType>
  <testOrLive>TEST</testOrLive>
  <contactData>
    <contactName>[[CONTACT NAME]]</contactName>
    <contactPhoneNumber>[[CONTACT PHONE]]</contactPhoneNumber>
    <contactEmailAddress>[[CONTACT EMAIL]]</contactEmailAddress>
  </contactData>
  <notificationAddressList>
    <notificationEmailAddress>[[NOTIFICATION EMAIL 1]]</notificationEmailAddress>
  </notificationAddressList>
  <primaryIssuer>
    <cik>[[CIK: issuer legal name]]</cik>
    <ccc>[[CCC]]</ccc>
    <issuerAddress>
      <street1>400 Alder Street</street1>
      <street2>Suite 1200</street2>
      <city>Portland</city>
      <stateOrCountry>OR</stateOrCountry>
      <zipCode>97204</zipCode>
    </issuerAddress>
    <issuerPhoneNumber>(503) 555-0142</issuerPhoneNumber>
    <issuerPreviousNameList><value>None</value></issuerPreviousNameList>
    <entityType>Limited Partnership</entityType>
    <yearOfInc><withinFiveYears>true</withinFiveYears><value>2026</value></yearOfInc>
  </primaryIssuer>
  <!-- co-issuers only: <issuerList><issuer> ...the same children as primaryIssuer... </issuer></issuerList> -->
  <relatedPersonsList>
    <relatedPersonInfo>
      <relatedPersonName><firstName>Dana</firstName><lastName>Whitcombe</lastName></relatedPersonName>
      <relatedPersonAddress><street1>400 Alder Street</street1><street2>Suite 1200</street2><city>Portland</city><stateOrCountry>OR</stateOrCountry><zipCode>97204</zipCode></relatedPersonAddress>
      <relatedPersonRelationshipList><relationship>Executive Officer</relationship><relationship>Director</relationship></relatedPersonRelationshipList>
      <relationshipClarification>Managing Member of Larkspur GP III, LLC, the General Partner</relationshipClarification>
    </relatedPersonInfo>
  </relatedPersonsList>
  <offeringData>
    <industryGroup>
      <industryGroupType>Pooled Investment Fund</industryGroupType>
      <investmentFundInfo><investmentFundType>Private Equity Fund</investmentFundType><is40Act>false</is40Act></investmentFundInfo>
    </industryGroup>
    <issuerSize><revenueRange>Decline to Disclose</revenueRange></issuerSize>
    <federalExemptionsExclusions><item>06b</item><item>3C</item><item>3C.7</item></federalExemptionsExclusions>
    <typeOfFiling>
      <newOrAmendment><isAmendment>false</isAmendment></newOrAmendment>
      <!-- D/A: <isAmendment>true</isAmendment><previousAccessionNumber>0001234567-26-000001</previousAccessionNumber> -->
      <dateOfFirstSale><value>2026-09-16</value></dateOfFirstSale>
      <!-- or <dateOfFirstSale><yetToOccur>true</yetToOccur></dateOfFirstSale> -->
    </typeOfFiling>
    <durationOfOffering><moreThanOneYear>true</moreThanOneYear></durationOfOffering>
    <typesOfSecuritiesOffered><isPooledInvestmentFundType>true</isPooledInvestmentFundType></typesOfSecuritiesOffered>
    <businessCombinationTransaction><isBusinessCombinationTransaction>false</isBusinessCombinationTransaction></businessCombinationTransaction>
    <minimumInvestmentAccepted>0</minimumInvestmentAccepted>
    <salesCompensationList>
      <recipient>
        <recipientName>Brightwater Securities LLC</recipientName>
        <recipientCRDNumber>8899001</recipientCRDNumber>
        <associatedBDName>None</associatedBDName>
        <associatedBDCRDNumber>None</associatedBDCRDNumber>
        <recipientAddress><street1>1 Harbor Plaza</street1><street2>Suite 400</street2><city>Boston</city><stateOrCountry>MA</stateOrCountry><zipCode>02110</zipCode></recipientAddress>
        <statesOfSolicitationList><state>AZ</state><state>TX</state></statesOfSolicitationList>
        <!-- or <statesOfSolicitationList><value>All States</value></statesOfSolicitationList> -->
        <foreignSolicitation>false</foreignSolicitation>
      </recipient>
    </salesCompensationList>
    <offeringSalesAmounts>
      <totalOfferingAmount>250000000</totalOfferingAmount>
      <totalAmountSold>91000000</totalAmountSold>
      <totalRemaining>159000000</totalRemaining>
      <clarificationOfResponse>Clarification from the Item 13 worksheet row, 255 characters at most</clarificationOfResponse>
    </offeringSalesAmounts>
    <investors>
      <hasNonAccreditedInvestors>false</hasNonAccreditedInvestors>
      <!-- when true, add <numberNonAccreditedInvestors>N</numberNonAccreditedInvestors> here -->
      <totalNumberAlreadyInvested>5</totalNumberAlreadyInvested>
    </investors>
    <salesCommissionsFindersFees>
      <salesCommissions><dollarAmount>500000</dollarAmount><isEstimate>true</isEstimate></salesCommissions>
      <findersFees><dollarAmount>0</dollarAmount></findersFees>
      <clarificationOfResponse>Clarification from the Item 15 worksheet row</clarificationOfResponse>
    </salesCommissionsFindersFees>
    <useOfProceeds>
      <grossProceedsUsed><dollarAmount>0</dollarAmount></grossProceedsUsed>
      <clarificationOfResponse>Clarification from the Item 16 worksheet row</clarificationOfResponse>
    </useOfProceeds>
    <signatureBlock>
      <authorizedRepresentative>false</authorizedRepresentative>
      <signature>
        <issuerName>Larkspur Growth Partners III, L.P.</issuerName>
        <signatureName>[[SIGNATURE: typed by the signer]]</signatureName>
        <nameOfSigner>Dana Whitcombe</nameOfSigner>
        <signatureTitle>Managing Member of Larkspur GP III, LLC, General Partner</signatureTitle>
        <signatureDate>[[SIGNATURE DATE]]</signatureDate>
      </signature>
    </signatureBlock>
  </offeringData>
</edgarSubmission>
```

Element-to-item mapping, where it is not obvious from the names: `primaryIssuer` and `issuerList` are Item 1 (CIK, previous names, entity type, year) and Item 2 (address, phone); `relatedPersonsList` is Item 3; `industryGroup` Item 4; `issuerSize` Item 5; `federalExemptionsExclusions` Item 6; `typeOfFiling` Item 7; `durationOfOffering` Item 8; `typesOfSecuritiesOffered` Item 9; `businessCombinationTransaction` Item 10; `minimumInvestmentAccepted` Item 11; `salesCompensationList` Item 12; `offeringSalesAmounts` Item 13; `investors` Item 14; `salesCommissionsFindersFees` Item 15; `useOfProceeds` Item 16; `signatureBlock` the signature page. Where the memo presents two variants (Regulation D only; all sales), the XML carries the recommended variant and the provenance row says so; the other variant is not in the file.

## Part 2. Online Forms keying sheet

For a filer using the EDGAR Online Forms application (no XML). The application has no test mode: the only test path is a filer-constructed XML transmitted as a test (Part 1). The sheet lists the screens in the order the application presents them, with the exact screen titles from Filer Manual Volume II chapter 8, and one row per field:

| # | Screen | Field | Key exactly | Worksheet row | Status | Note |
|---|---|---|---|---|---|---|

Screens, in order, and what each needs from the worksheet:

1. **File Form D**: choose "New Form D Submission", "New Form D Submission (using previous electronically filed Form D data)" (accession number required) or "Amendment to a previous Form D Filing" (accession number required). The accession number comes from the lookup register, Confirmed match only.
2. **Form D Issuer's Information**: primary issuer's CIK and CCC; Submission Contact Information (the person EDGAR contacts about the submission); Notification Information, up to three further e-mail addresses. EDGAR also notifies the login CIK, the contact and the primary issuer.
3. **Issuer's Identity**: Name of Issuer, Jurisdiction of Incorporation/Organization and previous names on file are pre-populated from EDGAR and disabled, so the record is confirmed before this screen, not on it. Key Year of Incorporation/Organization (a four-digit year when within five years), Entity Type (Other requires a description), up to three previous names not on file, and each additional issuer by CIK and CCC (up to 99).
4. **Principal Place of Business and Contact Information**: pre-populated from the business address on file for each CIK; a P.O. Box is rejected; an address keyed here applies to this filing only and does not change the EDGAR record.
5. **Related Persons**: Last, First, Middle; Street Address 1 and 2; City; State/Province/Country; ZIP/Postal Code; Relationship checkboxes; Clarification of Response. One row per Item 3 worksheet row.
6. **Industry Group**: the group; for Pooled Investment Fund, the Investment Fund Type and the Investment Company Act registration question.
7. **Issuer Size**: Revenue Range, or Aggregate Net Asset Value Range when the fund type is Hedge Fund or Other Investment Fund.
8. **Federal Exemption(s) and Exclusion(s) Claimed**: every box from the Item 6 row; Rule 506(b) and Rule 506(c) cannot both be selected; Section 3(c) requires the paragraph.
9. **Type of Filing**: New Notice or Amendment is pre-populated from screen 1; Date of First Sale or First Sale Yet to Occur.
10. **Duration of Offering**: Yes or No.
11. **Type(s) of Securities Offered**: Pooled Investment Fund Interests is pre-checked when Section 3(c) was selected; Other requires a description.
12. **Business Combination Transaction**: Yes or No; clarification up to 255 characters.
13. **Minimum Investment**: whole dollars.
14. **Sales Compensation**: every field but Street Address 2 is required for each recipient; CRD number or None; associated broker-dealer and its CRD number or None; State(s) of Solicitation (states, All States, or foreign); add and remove recipients.
15. **Offering and Sales Amount**: Total Offering Amount or Indefinite; Total Amount Sold; Total Remaining to be Sold is computed and disabled; clarification. The Rule 504 and $0 warnings appear here.
16. **Investors**: the non-accredited checkbox and count; total number of investors. The Rule 506(b) 35-investor warning appears here.
17. **Sales Commissions and Finders' Fee Expenses**: each amount (default $0) with its Estimate box.
18. **Use of Proceeds**: the amount (default $0) with its Estimate box; clarification.
19. **Signature and Submission**: issuer names pre-populated; typed signature, Name of Signer, Title and Date (calendar) for each issuer; the duly authorized representative box when one person signs for the co-issuers; the Terms of Submission; [Submit] validates the whole form and returns to the first screen with an error.
20. **Form D Confirmation/Correction**: [Edit Form D], [View/Print Submission] (the completed form as a PDF, to be compared with the worksheet before transmitting), [Transmit Submission].
21. **Transmit Submission Confirmation**: [Cancel Transmission] or [Transmit Submission].
22. **Transmit Submission Acknowledgment**: shows the accession number. Transmitted is not accepted; acceptance or suspension arrives by e-mail and through the submission query.

The sheet's last block lists the pre-populated fields to verify on screen (name, jurisdiction, previous names, business address) and the placeholders the filer supplies (CIK, CCC, contact, notification addresses, signature, date). A partly keyed form can be saved to the filer's computer and resumed; the session expires an hour after the last keystroke.

## Part 3. Pre-submission checklist

One checklist per matter, for the person who will transmit, each row with evidence of completion and an owner:

| # | Check | Evidence of completion | Owner | Done |
|---|---|---|---|---|

**A. Attorney sign-off on the memo**

1. Every Section 2 Critical and High item is closed or accepted in writing by the attorney.
2. Every worksheet row with status Unknown fact, Source conflict or Unverified external lookup is now Settled, and the provenance table's "XML blocked until" list is empty.
3. Every Issuer election and Section 4 judgment call carried into the file as a recommended choice is confirmed by the attorney (Item 5, Item 11, Item 13 cap and Indefinite presentation, Item 16 presentation, the Regulation S variant, one filing or several, entity type for any non-U.S. vehicle).
4. The `bad-actor-disqualification-review` hand-off has been completed and the signer has been told what the Terms of Submission certify.
5. The `blue-sky-filings` hand-off has an owner and the state deadlines are calendared against the same date of first sale.

**B. EDGAR access**

6. Each issuer's CIK is a Confirmed match in the lookup register (not supplied from memory or a client e-mail), and the EDGAR company record (name, jurisdiction, business address, previous names) matches the matter; any P.O. Box or stale address is corrected through the EDGAR company information function before filing.
7. The CCC for each issuer is in the filer's hands, and the filer holds an active Login.gov credential and a role or delegation for each issuer's account.
8. For a D/A, the previous accession number is that of an accepted Form D of the same issuer.

**C. The file, before the test transmission**

9. Every `[[placeholder]]` has been replaced; the file contains none of `schemaVersion`, `entityName`, `jurisdictionOfInc`, `stateOrCountryDescription`; `testOrLive` reads `TEST`.
10. The file validates locally against the three SEC schema files (next section).
11. Every value in the file matches the provenance table and the worksheet; `totalRemaining` equals the offering amount minus the amount sold, or is Indefinite; every clarification is within 255 characters and discloses nothing confidential.
12. The signature block names the issuer exactly as EDGAR records it, the signer named in the memo and the title the memo settled; the signature date will be the day of transmission.

**D. Test, then live**

13. Transmit as a TEST submission (next section) and read the acceptance or suspense notice. A test acceptance means the file passed the schema and EDGAR's business rules; it does not confirm that any value is correct.
14. Resolve every SUSPENDED message and review every WARNING against the memo; re-test after any change to the file.
15. Before the live transmission: change `testOrLive` to `LIVE`, use the live transmission link (the tag and the link must agree), set the signature date to today, and transmit before 5:30 p.m. Eastern on or before the due date in Section 1.
16. Record the accession number from the acceptance e-mail or the submission query, not from the transmission screen; download the disseminated filing and compare it with the worksheet; calendar the annual amendment date and any change-driven trigger; retain the manually signed authentication document for five years; pass the accession number and filing date to the state notice filings.

## Local validation and the EDGAR test submission

Local schema validation, with the three schema files from the SEC zip in one directory:

```bash
xmllint --noout --schema formDSubmission.xsd.xml <submission>.xml
```

It passes only once every placeholder is replaced. It checks structure, types, lengths and codes; it does not check the CIK and CCC pair, the accession number, the P.O. Box rule, the issuer name in the signature block or the 506(b) and 506(c) conflict, which EDGAR checks at transmission.

Test transmission (Filer Manual Volume II, chapter 9): log in to the EDGAR OnlineForms Management website, choose "Transmit XML Submission", then "Transmit as a Test Submission", select the file and click [Transmit TEST Submission]; or use the "Transmit" link on the EDGAR Filing Website with the same test choice. EDGAR treats the submission as a test, does not disseminate it, and reports acceptance or suspension by e-mail and in the submission query. The `testOrLive` tag inside the file controls processing even when the live link is used.

## Labels

Every XML file and keying sheet in the package carries, at its head, "Draft built from the attorney-review memo dated <date>. Not validated against EDGAR. Requires a TEST submission by the filer and attorney confirmation of every flagged row before any live filing." The package closes with the memo's own closing line.
