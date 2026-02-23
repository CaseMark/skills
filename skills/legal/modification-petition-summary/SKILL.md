---
name: modification-petition-summary
description: >-
  Produces structured summaries of U.S. family law modification petitions,
  capturing the existing order, requested changes, alleged material change in
  circumstances, supporting facts, evidence, and procedural posture. Use when
  summarizing petitions to modify custody, visitation, child support, spousal
  support, or other post-judgment orders for quick attorney review. Trigger
  keywords: "modification petition", "change in circumstances", "custody
  modification", "support modification", "visitation modification",
  "post-judgment motion".
tags:
  - litigation
  - summarization
  - summary
---

# Modification Petition Summary

Condense a family law modification petition into a decision-ready, neutral summary.

## Prerequisites

1. The modification petition and all referenced exhibits/attachments
2. The current order/judgment being modified (or its date and terms)
3. Docket metadata (court, case number, filing date)
4. Jurisdiction/state and party roles (petitioner/respondent)
5. Any cited statutes/case law included in the petition

## Output Structure / Process

Use the following structure and fill all fields that are present in the petition. Note missing items explicitly.

**Case Snapshot (table)**

| Field | Details |
| --- | --- |
| Court / County | |
| Case No. | |
| Parties | |
| Petitioner / Respondent | |
| Filing Date | |
| Order at Issue (type/date) | |
| Requested Hearing Date | |
| Emergency/Temporary Relief Sought | Yes/No; details |

**Order Comparison (table)**

| Topic | Current Order | Requested Modification |
| --- | --- | --- |
| Custody (legal/physical) | | |
| Parenting time / visitation | | |
| Child support | | |
| Spousal support | | |
| Other provisions | | |

**Grounds for Modification (checklist)**

- Material change in circumstances alleged: Yes/No
- Nature of change: relocation, income change, child needs, health, safety, cohabitation/remarriage, school issues, other
- Best interests factors invoked: Yes/No; specify
- Statutory standard cited: Yes/No; cite if provided
- Retroactive modification requested: Yes/No; scope

**Factual Allegations (bulleted chronology)**

- Date/period: event/fact alleged
- Link to requested change: how petitioner connects fact to relief
- Any allegations of noncompliance with prior order

**Evidence Inventory (table)**

| Evidence Type | Attached? | Description / Purpose |
| --- | --- | --- |
| Financial declaration | | |
| Party declaration(s) | | |
| Witness declaration(s) | | |
| Expert report(s) | | |
| School records | | |
| Medical records | | |
| Other exhibits | | |

**Legal Framework (short list)**

- Statutes cited
- Case law cited
- Local rules/procedural standards cited

**Procedural Posture (table)**

| Item | Details |
| --- | --- |
| Service/Notice described | |
| Prior modification history mentioned | |
| Related proceedings (contempt, enforcement, DV) | |
| Requested fees/costs | |
| Mediation/ADR requested or required | |

**Relief Requested (list)**

- Primary modification(s)
- Temporary/emergency orders
- Ancillary relief (fees, costs, transportation, exchanges, supervised visits, etc.)

**Gaps / Flags (list)**

- Missing: current order text/date, financial data, parenting plan, jurisdiction facts, service info
- Potential jurisdiction/venue issue: flag if facts suggest multi-state custody or relocation
- Procedural defect: missing verification, missing required forms, untimely filing, lack of notice (if apparent)

## Guidelines

- Keep tone neutral and factual; do not argue merits.
- Mirror petition terminology for accuracy; avoid recharacterizing allegations.
- Distinguish between attached evidence and referenced-but-missing documents.
- Flag any uncertainty or absent data explicitly as “Not provided”.
- Jurisdiction-specific standards vary by state; do not infer standards not stated.
- Use `[VERIFY]` for any legal citation you cannot confirm.
