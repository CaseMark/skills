# Source Hierarchy and Reconciliation

The value of the draft depends on reconciling the document set before any field is populated. Run these steps in order.

## Source hierarchy

Rank sources from most to least authoritative:

1. **Executed and accepted subscription documents**, then **governing documents** (partnership agreement and amendments, formation documents, general partner constituent documents, incumbency certificates).
2. **Offering documents and supplements** (the private placement memorandum and its supplements, side letters where they bear on the filing).
3. **Administrator ledgers and closing memos.**
4. **Client emails and org charts.**

Use the hierarchy by question:

- Investor-level facts (commitment amount, signature date, acceptance, investor representations about status, state of residence): the executed subscription and its questionnaire control.
- Structure and people (who the issuer is, general partners, managing members, entity type, formation date, cap on the program, exemption relied on): the governing documents control, and for the offering cap the most recent offering document or supplement controls over the prior filing.
- A prior Form D is a record of what was reported before, not of what is true. It does not override a later governing or offering document.
- Where a later-dated executed amendment or supplement supersedes an earlier version, use the later one and cite both.
- Unsigned, undated or draft documents rank below executed ones, and an executed document that is not countersigned is not "accepted".

## Reconciliations to run before drafting

Run each one and record the result, even when the sources agree.

1. **Per-investor commitments.** Subscription agreement amount versus ledger amount, for every investor. Differences are conflicts. Totals by vehicle drive Item 13.
2. **Acceptance and commitment dates.** Date each subscription became irrevocable (see `amendments-and-deadlines.md`) versus the dates in the closing memo and ledger. The closing date is not a substitute.
3. **Accredited, qualified purchaser and knowledgeable employee status.** Questionnaire answers versus ledger flags. A ledger flag never overrides a questionnaire.
4. **Investor states versus placement agent registration.** Each investor's state of residence or solicitation versus the placement agent's registered states. Gaps go to `blue-sky-filings`.
5. **Related persons.** Governing documents versus the prior Form D, the org chart and client instructions. Flag every difference.
6. **Offering size.** Current offering documents and supplements versus the prior filing's Item 13; compute any cumulative change as a percentage.
7. **Issuer facts.** Legal names, entity types, jurisdictions, formation dates and previous names across the formation documents, the offering documents and the prior filing.
8. **Sales compensation.** The placement or finder agreement versus any fee reported in the prior filing and the ledger or closing memo; CRD numbers from BrokerCheck or the agreement.
9. **Covered persons and bad actor diligence status.** Questionnaires and certifications received, outstanding, stale or answered Yes, versus the related persons list and the agent list. This feeds the hand-off.

## Conflict write-up

For each conflict, write: the field; the two (or more) values; the source of each, with section or page; which source controls under the hierarchy and why; the value used; and whether a client question is needed. Never silently pick one value. Put conflicts that change a deadline, an amendment trigger or an exemption conclusion in Section 2 of the output; put the rest in the Section 3 flag column.

## Citations

Cite each populated field as the document name plus the section, page or Bates range, for example "Subscription Agreement (Investor A), s. 3(b), p. 4". If the document has no section numbers, cite the page. If a value comes from more than one document, cite each.

## Missing or unreadable documents

If a PDF cannot be rendered directly by your tools, extract its text layer with whatever is available, use OCR for image-only pages, and state the method used and any pages that stayed illegible. For spreadsheets, read every sheet, formula, note and hidden row or column. If a needed document is missing, unreadable or image-only without a usable text layer, mark the dependent fields MISSING or Low confidence, say which document would resolve them, and put the request in Section 2. Do not fill a field from memory or from the likeliest value.

## Public-disclosure check

Before finalizing clarification text, read it as a stranger would read the public filing. Remove or flag investor names, side-letter terms, fee splits and strategy details that need not be public.
