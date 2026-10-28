# Source Hierarchy, Review Gate and Reconciliation

The value of the draft depends on reviewing the whole matter and reconciling the document set before any field is populated. Run these sections in order.

## Contents

1. Source hierarchy
2. Source-review completion gate
3. Client instructions that point at a lower-ranked source
4. Reconciliations to run before drafting
5. Bad actor questionnaire review
6. Conflict write-up
7. Citations
8. Public-disclosure check

## Source hierarchy

Rank sources from most to least authoritative:

1. **Executed and accepted subscription documents**, then **governing documents** (partnership agreement and amendments, formation documents, general partner constituent documents, incumbency certificates).
2. **Offering documents and supplements** (the private placement memorandum and its supplements, side letters where they bear on the filing).
3. **Administrator ledgers and closing memos.**
4. **Client emails and org charts.**

Use the hierarchy by question:

- Investor-level facts (commitment, signature and acceptance dates, status representations, residence): the executed subscription and questionnaire control.
- Structure and people (issuer identity, general partners, managing members, entity type, formation date, program cap, exemption): the governing documents control; for the cap, the latest offering document or supplement controls over the prior filing.
- A prior Form D records what was reported, not what is true. A later executed amendment or supplement supersedes an earlier version; cite both.
- Unsigned, undated or draft documents rank below executed ones; an executed document that is not countersigned is not "accepted".
- A client email describing the document set is a description, not the inventory. The inventory is what is actually in the matter.

## Source-review completion gate

Complete this gate before drafting any item. Its output is the source-review register in the output header (`output-template.md`).

**Build the inventory from the matter, not from the description of the matter.** List every file in the matter folder, data room export or attachment set: file name, document type, date, source rank, and pages or sheets. Include files with uninformative names ("Scan_20260917.pdf", "Document (3).pdf"), attachments inside emails, and every sheet of every workbook. When the client's description and the inventory differ, the inventory wins and the difference is a client question.

**Open every file.** A search that does not surface a document's contents is not evidence that the document is absent or unreadable. Search tools index text layers and miss scans, oddly named files, email attachments and secondary sheets. Before any document is described as missing or unavailable: (1) check the inventory by name, type and date; (2) retrieve and open the file directly; (3) extract its text layer, OCR image-only pages, and for spreadsheets read every sheet, formula, note and hidden row or column; (4) only then assign a status. An Unreadable after attempt row requests a native or re-scanned copy, and the request goes in Section 2 when a filing outcome depends on it.

**Give every row one status.**

| Status | Meaning | The row must also show |
|---|---|---|
| Reviewed | Opened and read in full (for a subscription: signature page, acceptance block and questionnaire, not a sample) | Pages or sheets read |
| Not relevant | Opened; bears on no Form D item and no hand-off | A one-line reason |
| Unreadable after attempt | Retrieved, but text could not be extracted after a direct read, text-layer extraction and OCR | The method tried, the pages affected, what the file is believed to be, and each conclusion that depends on it |
| Still needed | Not in the matter at all, and required | Who supplies it, and the fields and conclusions waiting on it |

"Missing" and "unavailable" are not statuses. A document is Still needed only when the inventory check and the retrieval attempt both came up empty.

**Must-review categories.** When present in the inventory, these are reviewed in full and are never Not relevant:

- executed investor subscription agreements, their amendments, and investor questionnaires;
- bad actor questionnaires and placement agent certifications;
- governing documents: partnership or operating agreement and amendments, formation certificates, general partner constituent documents, incumbency certificates;
- offering documents and supplements;
- administrator ledgers and investor registers;
- closing memos, closing checklists and acceptance notices;
- prior Form D filings and EDGAR acceptance messages;
- placement agent or finder agreements and registered-states exhibits.

**Gate.** Drafting starts when every row has a status. Still needed rows go to Section 2 (when a filing outcome depends on them) and Section 6. Unreadable rows carry their dependency list into the evidence-to-field worksheet (`form-d-items.md`) as "Unknown fact (unreadable source)". Nothing is filled from memory or from the likeliest value.

## Client instructions that point at a lower-ranked source

Before reconciling, re-read the client email, cover note and closing memo for any instruction to take a value from a ledger, register, org chart, closing memo or prior filing ("use the administrator's register as of Wednesday"; "the January org chart has the related persons"; "carry the figures from the last Form D"). Each is a red flag, not a shortcut: the named source ranks below the executed and governing documents, and the instruction is usually given because the client has not noticed that they differ. For each: record the instruction and its source; reconcile that source against the controlling documents; if they agree, use the value and cite both; if they differ, use the controlling value, name the conflict in Section 2 with the correct value and the client question, and never comply silently.

**Worked example (synthetic).** The email says "use the register for the amounts; Sorrel Point upsized to $15 million." The register shows $15,000,000; the only executed amendment raises the commitment to $12,000,000. The output uses $12,000,000, records the register and the email as a Source conflict with the amendment controlling, asks whether a further executed amendment exists, and states the Item 13 and 15 consequences if one is produced. "Use the org chart" is handled the same way: the governing documents supply the related persons, and a person they add is an amendment trigger and a covered person whatever the chart shows.

## Reconciliations to run before drafting

Run each one and record the result, even when the sources agree.

1. **Per-investor commitments.** For every investor of every issuer, the executed subscription amount as amended by any executed amendment, the acceptance date, the ledger amount and the delta, in the investor reconciliation table (`fund-structures.md`, Issuer-specific reconciliation). Every unexplained delta is a conflict. The issuer's Item 13 and Item 15 figures are sums of this table's executed amounts; a total from a ledger summary tab, closing memo or email is a cross-check only.
2. **Acceptance and commitment dates.** Date each subscription became irrevocable (see `amendments-and-deadlines.md`) versus the dates in the closing memo and ledger. The closing date is not a substitute.
3. **Accredited, qualified purchaser and knowledgeable employee status.** Questionnaire answers versus ledger flags. A ledger flag never overrides a questionnaire. Write up each conflict as required in `fund-structures.md` (Qualification conflicts).
4. **Investor states versus placement agent registration.** Every investor's state and who introduced the investor (agent or direct) versus the agent's registered-states exhibit, in the placement agent cross-check matrix laid out in `output-template.md` Section 5. A gap exists only for an agent-introduced investor in a state outside the list; a direct investor's state is never an agent registration gap.
5. **Related persons.** Governing documents versus the prior Form D, the org chart and client instructions. Flag every difference.
6. **Offering size.** Current offering documents and supplements versus the prior filing's Item 13; compute any cumulative change as a percentage.
7. **Issuer facts.** Legal names, entity types, jurisdictions, formation dates and previous names across the formation documents, the offering documents and the prior filing.
8. **Sales compensation.** The placement or finder agreement versus any fee reported in the prior filing and the ledger or closing memo; compute the fee per issuer from the commissionable base; CRD numbers from BrokerCheck or the agreement, with the lookup outcome recorded (`edgar-access.md`).
9. **Covered persons and bad actor diligence status.** Questionnaires and certifications received, outstanding, stale or answered Yes, versus the related persons list and the agent list. Run the review in the next section; it feeds the hand-off.

## Bad actor questionnaire review

The Form D signer certifies that the issuer is not disqualified under Rule 506(d). The full diligence belongs to `bad-actor-disqualification-review`, but this skill reads every questionnaire and certification in the inventory and records what each says, because the hand-off is only as good as that record.

For each questionnaire or certification, record: who it covers; the covered-person category under Rule 506(d)(1) (the issuer; its directors, executive officers, other officers participating in the offering, general partners and managing members; 20 percent beneficial owners by voting power; promoters; the investment manager of a pooled fund and its general partners, managing members, directors and officers; solicitors paid for the offering and their principals); the date signed; whether it is executed; whether its date is stale relative to the sale it covers; and whether any answer is Yes.

**For every Yes, record:**

| Field | Content |
|---|---|
| Person and role | Name, entity, and the capacity that makes the person a covered person |
| Question | Number and text as answered |
| Disclosed event | What the person disclosed, in the person's own words |
| Date of event | The date of the order, conviction, judgment or suspension; when it took effect; when it expires, if it does |
| Source | Questionnaire file and page; any attachment |
| Primary document | Whether the underlying order, judgment, decree or settlement is in the inventory and was reviewed; if not, who holds it |

**Characterize only after applying the rule's criteria,** never from the questionnaire alone. Walk the event through Rule 506(d)(1): the event category; the lookback measured back from the relevant sale (ten years for convictions, or five for the issuer, its predecessors and affiliated issuers; five years for court injunctions and Commission cease-and-desist orders; "at the time of such sale" for orders, suspensions, expulsions and bars that must be in effect); for final orders of state securities, banking and insurance regulators, federal banking agencies, the CFTC and the NCUA, whether the order bars the person at the time of sale or is a final order based on a violation of a law prohibiting fraudulent, manipulative or deceptive conduct entered within ten years; and whether a Rule 506(d)(2) exception applies (the event occurred or the order was issued before September 23, 2013; a Commission waiver; the court's or regulator's written advice that disqualification should not arise; or the reasonable-care exception, which requires factual inquiry). Then characterize as one of:

- **Potentially disqualifying.** On the primary document, the event fits a Rule 506(d)(1) category within its lookback and no exception is established. The exemption is in doubt. Critical blocking issue.
- **Disclosure-only.** The event would have been disqualifying but occurred before September 23, 2013, so Rule 506(e) requires a written description to each purchaser a reasonable time before sale. Confirm it was furnished.
- **Outside the criteria on its face.** The primary document was reviewed and the event fits no category (for example, a state cease-and-desist order with no bar and no fraud-based finding, or a suspension that had ended before the sale). State the reasoning; counsel confirms.
- **Unresolved.** The primary document was not reviewed, the questionnaire's description is incomplete, or the criteria cannot be applied on the record. Say exactly what is needed.

In every case name the counsel decision (proceed; obtain the order; seek a Commission waiver; obtain the regulator's written advice; remove the person from the covered role before the sale; furnish Rule 506(e) disclosure; document reasonable care) and the follow-up with its owner and timing relative to signature. A Yes with no attached order creates a Still needed row for that order. Carry each Yes, each missing or unsigned questionnaire and each stale certification into Section 5 (`output-template.md`).

## Conflict write-up

For each conflict, write: the field; the two (or more) values; the source of each, with section or page; which source controls under the hierarchy and why; the value used; the recommended resolution and what changes under the alternative; and whether a client question is needed. Never silently pick one value. Put conflicts that change a deadline, an amendment trigger or an exemption conclusion in Section 2 of the output; put the rest in the Section 3 conflict column.

## Citations

Cite each populated field as the document name plus the section, page or Bates range, for example "Subscription Agreement (Investor A), s. 3(b), p. 4". If the document has no section numbers, cite the page. If a value comes from more than one document, cite each.

## Public-disclosure check

Before finalizing clarification text, read it as a stranger would read the public filing. Remove or flag investor names, side-letter terms, fee splits and strategy details that need not be public.
