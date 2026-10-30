# Contract, Consent and IP Review Rules

## Contents

1. Source-review protocol for a virtual data room
2. Which document controls
3. Consent and notice analysis by deal structure
4. Outcome labels for the consents table
5. Restrictive covenants that reach the buyer after closing
6. Materiality thresholds and aggregation
7. IP chain of title
8. Open-source licenses

Authorities named here are listed, with the date each was read, in `references/primary-sources.md`. Anything not confirmed there is marked `[VERIFY]`.

## 1. Source-review protocol for a virtual data room

Before any document is reported as missing, run all five checks and record each in the source-review register:

1. **Index search.** Search the full data room index by counterparty name, by short name and by contract type, not only the folder where the document should be. Sellers often upload late items to a "Miscellaneous", "Supplemental" or Q&A folder under a scan file name.
2. **Q&A log.** Read every Q&A response that names the counterparty. A response such as "uploaded to 9.7.14" ends the search there.
3. **Open the file.** Confirm what it is from its first page and signature page, not from its file name.
4. **Extraction.** For image-only or scanned files, run OCR or text extraction. Record the pages that remain unreadable.
5. **Version check.** Look for amendments, side letters, statements of work, renewal notices and assignment letters filed separately.

Status after the protocol, used verbatim in the register: **Reviewed**; **Reviewed: summary only (not relied on)**; **Unreadable after attempt** (list pages); **Not located after index and Q&A check**; **Not relevant**; **Withheld: privilege or clean team**. Only the fourth label supports a "missing document" finding, and it names the searches run.

## 2. Which document controls

- The executed agreement and every executed amendment control over a seller's contract summary, a disclosure schedule draft, a data room index description, a management presentation or a CIM.
- A later executed amendment controls over the base agreement for the provisions it changes. Read the amendment clause by clause; amendments often add change-of-control, MFN or exclusivity terms that the base agreement lacked.
- An unsigned draft, a redline or a form agreement is not evidence of the executed terms. Record it as such and request the signed copy.
- Where a summary and the executed document disagree, record a **source conflict**, report the executed term, and tell the client the summary is unreliable for the remaining contracts it covers.

## 3. Consent and notice analysis by deal structure

Read the clause, the definitions it uses ("Change of Control", "Affiliate", "assign", "transfer"), the governing-law clause and the deal structure together.

| Structure | What changes hands | Plain anti-assignment clause | "By operation of law" clause | Express change-of-control clause |
|---|---|---|---|---|
| Stock purchase | Ownership of the target's equity; the contracting party is unchanged | Generally not triggered under Delaware law (Meso Scale, discussing Baxter and Branmar) | Generally not triggered | Triggered as defined |
| Reverse triangular merger (target survives) | Target survives; separate existence of merger sub ends | Delaware: generally not an assignment (Meso Scale, 62 A.3d 62, relying on 8 Del. C. 259(a)); California: SQL Solutions (N.D. Cal. 1991) reached the opposite result `[VERIFY]` | Delaware: not triggered on the Meso Scale facts; other law: judgment call | Triggered as defined |
| Forward or direct merger (target disappears) | Target's contracts vest in the survivor under 8 Del. C. 259(a) | Risk of transfer by operation of law; analyze the clause and governing law | Triggered in most readings | Triggered as defined |
| Asset purchase | Each assigned contract is transferred by the seller | Consent required where the clause requires it | Consent required | Usually also triggered |

Special cases that override the table:

- **Federal government contracts.** 41 U.S.C. 6305(a) bars transfer of a federal contract; a purported transfer annuls it as far as the Government is concerned. FAR 42.1204(a) lets the Government recognize a successor through a novation agreement after an asset transfer, including one incident to a merger; under 42.1204(b), no novation is needed for a stock purchase with no legal change in the contracting party. Confirm FAR numbering on the date of the report `[VERIFY]`.
- **Patent and copyright licenses.** A nonexclusive patent license is personal and nonassignable under federal law absent consent (In re CFLC, 89 F.3d 673 (9th Cir. 1996)). Treat an in-license of core IP in a merger as **Judgment call: governing law unsettled** unless the clause or a consent resolves it, and recommend consent.
- **Contracts held outside the target.** A contract signed by a parent, sister company, founder or affiliate that is not being acquired does not move in a stock deal or merger. It needs an assignment, a new contract or a transition arrangement; label it **Outside the deal perimeter**.
- **Notice-only clauses** and **termination rights on a change of control** are separate from consent. A counterparty that cannot block the deal may still terminate after it.

## 4. Outcome labels for the consents table

Use exactly one per contract: **Consent required**; **Notice only**; **Termination or other right triggered**; **No consent on these facts**; **Judgment call: governing law unsettled**; **Outside the deal perimeter**. Each row cites the clause and its source locator, the governing law, the deal structure assumed, and what changes if the structure changes (for example, from merger to asset purchase).

## 5. Restrictive covenants that reach the buyer after closing

- Read every exclusivity, non-compete, non-solicit, MFN, right-of-first-refusal and most-favored-pricing clause for whom it binds: "Company", "Company and its Affiliates", "Company and its subsidiaries".
- "Affiliates" defined by control (controls, is controlled by, or is under common control with) can include, after closing, the buyer, its parent and, for a private equity buyer, every portfolio company under common control by the fund. Report whether the covenant would bind them and what they sell in the restricted field.
- Whether "Affiliates" means affiliates at signing or at any time during the term turns on the wording and governing law. Present both readings and the consequence of each; do not choose one silently.
- MFN clauses that compare "the Company or its Affiliates" pricing can import the buyer group's pricing after closing.
- The exposure is measured by the buyer group's affected business, not by the target contract's revenue.

## 6. Materiality thresholds and aggregation

- The client's threshold is a **policy election**. Apply it, and record it at the top of the report.
- Aggregate contracts that share the same risk term (the same change-of-control termination right, the same MFN, the same form) and test the total against the threshold and against target revenue.
- A revenue threshold does not screen out: restrictive covenants that can bind the buyer group; clauses that let a counterparty terminate on a change of control when contracts with that clause together exceed the threshold; uncapped indemnities; guarantees; or statutory triggers such as WARN headcounts and HSR thresholds, which apply on their own terms.
- When the threshold would hide an aggregated risk, report the aggregate as a finding and the threshold issue as a judgment call for the client.

## 7. IP chain of title

- **Inventions.** Rights in an invention belong to the inventor unless effectively assigned (Stanford v. Roche, 563 U.S. 776 (2011)); a patent interest is assignable by an instrument in writing (35 U.S.C. 261). "Agree to assign" was read as a promise to assign in the future, while "do hereby assign" operated on the invention once it existed (583 F.3d 832, 841-42 (Fed. Cir. 2009)). Check the operative words in every employee and contractor agreement.
- **Recording.** An unrecorded patent assignment is void against a later purchaser or mortgagee for value without notice unless recorded within three months from its date or before the later purchase (35 U.S.C. 261). Compare USPTO assignment records with the chain the seller describes.
- **Copyright.** Work by employees within the scope of employment is work made for hire (17 U.S.C. 101). Work by an independent contractor is work made for hire only if it falls within the nine listed categories and a signed writing says so; most custom software does not fit those categories. Otherwise the contractor owns the copyright unless a signed written transfer exists (17 U.S.C. 204(a)). Identify contractor-written code and the written assignment for each contributor.
- **Founder and pre-formation IP.** IP created before incorporation, or held in a founder's name, needs an assignment to the target.
- **Registrations.** Confirm the record owner of every patent, trademark registration and domain is the target entity, not a founder, parent or former subsidiary.

## 8. Open-source licenses

- Obtain a software composition scan or bill of materials, not a management statement.
- GPLv3 section 6 conditions conveying object code on also conveying the Corresponding Source. AGPLv3 section 13 requires a modified version that interacts with users over a network to offer them its Corresponding Source. Identify copyleft components in distributed products and in network services separately.
- Report each copyleft component with: product, how it is used (linked, modified, distributed, network-served), the license, and the remediation (replace, re-architect, comply). The legal effect on a specific architecture is a judgment call for IP counsel.
