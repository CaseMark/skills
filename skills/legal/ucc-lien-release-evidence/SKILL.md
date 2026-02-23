---
name: ucc-lien-release-evidence
description: >-
  Drafts an Evidence of UCC Lien Release (certificate or letter evidencing
  termination of a UCC-1 financing statement) for U.S. transactional matters.
  Use when documenting UCC-3 termination, secured party release, payoff, or
  clear title in asset purchases, financings, or closing deliverables. Trigger
  keywords: "UCC-1", "UCC-3 termination", "lien release", "secured party
  release", "clear title", "payoff letter", "closing binder".
tags:
  - agreement
  - drafting
  - transactional
---

# Evidence of UCC Lien Release

Produce a formal Evidence of UCC Lien Release suitable for closing and due diligence.

## Prerequisites

1. Original UCC-1 financing statement details (file number, filing date, filing office, jurisdiction)
2. Debtor and secured party legal names and addresses as filed
3. Collateral description from the UCC-1 (and any amendments)
4. Security agreement date and governing documents
5. Evidence of satisfaction (payoff statement, wire confirmation, release letter, settlement, or order)
6. UCC-3 termination statement details if filed (file number, date, stamped copy)
7. Scope of release (full or partial) and effective date
8. Any continuation, assignment, or amendment filings tied to the same collateral

## Output Structure / Process

1. Build the source data table and resolve inconsistencies before drafting.
2. Create a UCC filing chronology table when multiple filings exist.
3. Draft the document using the section checklist and template.
4. Assemble exhibits and verify cross-references.

**Source Data Table**

| Field | Required | Source | Notes |
| --- | --- | --- | --- |
| Debtor legal name | Yes | UCC-1 | Use exact spelling, punctuation, entity suffix |
| Secured party legal name | Yes | UCC-1 | Use exact spelling, punctuation, entity suffix |
| Filing office + jurisdiction | Yes | UCC-1 | Secretary of State or equivalent |
| UCC-1 file number | Yes | UCC-1 | Include filing date |
| Collateral description | Yes | UCC-1 | Mirror language verbatim where possible |
| Security agreement date | Yes | Security agreement | Identify governing document |
| Release scope | Yes | Instructions | Full vs partial; list retained collateral |
| Effective date | Yes | Instructions | Execution date or payoff date |
| UCC-3 termination file number | If filed | UCC-3 | Include date and stamped copy |
| Satisfaction evidence | Yes | Payoff/letters | Cite exhibit numbers |

**UCC Filing Chronology (use when more than one filing exists)**

| Filing No. | Type | Filing Office | Filing Date | Purpose |
| --- | --- | --- | --- | --- |
|  | UCC-1 |  |  | Original financing statement |
|  | UCC-3 |  |  | Amendment/continuation/assignment/termination |

**Section Checklist**

| Section | Required Content | Notes |
| --- | --- | --- |
| Title + Date | Evidence of UCC Lien Release; date of document | Use exact title |
| Parties | Debtor and secured party details | Match UCC-1 |
| Filing Identification | UCC-1 file number, filing office, filing date | Add all jurisdictions |
| Secured Transaction Summary | Security agreement date; obligation summary; collateral categories | Track UCC-1 text |
| Release Statement | Full/partial release; satisfaction; no further claims | Unambiguous |
| Termination Status | UCC-3 filing details or intent to file | Do not imply filed if not filed |
| Effective Date | Specific date | Tie to payoff or execution |
| Exhibits | List supporting documents | Provide exhibit labels |
| Execution | Authorized signatory + title | Add notarization if required |

**Template**

```text
EVIDENCE OF UCC LIEN RELEASE

Date: {Document Date}

1. Parties
Secured Party: {Legal Name}, {Entity Type}, {Jurisdiction of Organization}
Address: {Address}
Debtor: {Legal Name}, {Entity Type}, {Jurisdiction of Organization}
Address: {Address}

2. Financing Statement Identification
UCC-1 File Number: {File Number}
Filing Office/Jurisdiction: {Filing Office, State}
Filing Date: {Filing Date}
Additional Filings (if any): {List UCC-3 amendments/continuations/assignments}

3. Secured Transaction Summary
Security Agreement Date: {Date}
Obligation: {Brief description of secured obligations}
Collateral: {Collateral description mirroring UCC-1}

4. Release and Termination
The Secured Party hereby releases, terminates, and fully discharges all security interests,
liens, and claims in the collateral described above arising under the UCC-1 financing
statement identified in Section 2. All secured obligations have been satisfied in full, and
the Secured Party asserts no further interest in the collateral or proceeds.

5. Termination Filing
{If filed} A UCC-3 Termination Statement has been filed under File No. {UCC-3 No.} on {Date}.
{If not filed} The Secured Party will file a UCC-3 Termination Statement with the filing office
identified above.

6. Effective Date
This release is effective as of {Effective Date}.

7. Exhibits
Exhibit A: UCC-1 Financing Statement
Exhibit B: UCC-3 Termination Statement (file-stamped, if available)
Exhibit C: Payoff/Release Evidence {wire confirmation / payoff letter / order}

Secured Party:

By: ___________________________
Name: {Signatory Name}
Title: {Title}
Date: {Signature Date}

{Optional Notary Acknowledgment}
```

**Exhibits Checklist**

- [ ] UCC-1 financing statement (file-stamped)
- [ ] UCC-3 termination (file-stamped if available)
- [ ] Payoff letter or satisfaction evidence
- [ ] Security agreement (if cited)
- [ ] Order/settlement (if release arises from legal proceeding)

## Guidelines

- Match debtor and secured party names exactly to the UCC-1; flag discrepancies for confirmation.
- Mirror the collateral description; avoid paraphrasing that could narrow or expand scope.
- If the release is partial, list released collateral and expressly preserve any remaining liens.
- Do not state a UCC-3 was filed unless you have the file number and date.
- Use consistent filing office terminology (e.g., “Secretary of State, {State}”).
- Add notarization only if required by jurisdiction or requested by the client.
- Mark any uncertain statutory citations with `[VERIFY]`.
- Keep the document neutral and evidentiary; avoid advocacy or legal conclusions.
