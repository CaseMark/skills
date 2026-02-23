---
name: joint-operating-agreement
description: >-
  Drafts U.S. Joint Operating Agreements (JOA) for oil and gas exploration,
  development, and production. Use for pre-signature drafting, negotiation
  edits, redline cleanup, and execution-ready finalization of party structure,
  operator authority, AFE workflow, cost allocation, billing and audit rights,
  title and lien protections, default remedies, and governing-law mechanisms.
  Trigger keywords: JOA, joint operating agreement, operator, non-operator,
  joint account, participating interest, revenue interest, AFE, non-consent,
  default, foreclosure, lien rights, title opinion, area add/drop, memorandum
  of agreement.
tags:
  - agreement
  - drafting
  - regulatory
---

# Joint Operating Agreement (JOA) Drafting Protocol

Create a structured, clause-complete JOA draft that is operationally usable and litigation-ready, with all critical economics, authority limits, title protections, and enforcement rights in enforceable U.S. oil-and-gas transaction language.

## Prerequisites

1. Full party identities from formation filings: exact legal name, entity type, state of formation, authority proof, registered agent and address, signatory authority.
2. Contract Area package: lease and mineral title chain, legal descriptions/metes-and-bounds or section data, gross/net acreage, term/extension history.
3. Initial economics inputs: participating interest, revenue interest, burdens (overriding royalties, net profits interests, production payments), and non-cash considerations.
4. Operator and non-operator role map: who is Operator, compensation assumptions, overhead model, voting thresholds, approval workflow.
5. Regulatory baseline: jurisdiction state, federal land status, unitization/pooling framework, any foreign ownership or environmental constraints.
6. Operational governance inputs: AFE cadence, routine vs non-routine definitions, non-consent mechanics, force-majeure emergency operations approach.
7. Finance and tax assumptions: billing cycle, interest on late payments, audit tolerance, overhead markup/fixed-charge model, dispute escalation path.
8. Closing and execution details: number of execution parties, intended governing law/state forum, dispute mechanism preference, recording jurisdiction(s), title standards.

## Output Structure / Process

1. Normalize inputs
   - Build an assumptions block with missing items explicitly marked: `[CLIENT TO PROVIDE: ...]`.
   - Verify that participation percentages and burdens reconcile internally.

2. Draft core agreement architecture
   - Cover page with title/effective date/signature placeholders.
   - Table of Contents with article/section numbering.
   - Definitions section with controlled capitalization.
   - Full articles:
     - I. Parties and Contract Area
     - II. Organization, Operator Duties, and Authority
     - III. Operations and AFE Governance
     - IV. Financial Management and Accounting
     - V. Title and Interests
     - VI. Product Handling and Marketing
     - VII. Defaults, Remedies, and Survival
     - VIII. Execution, Assignment, and Governing Law

3. Insert mandatory precision tables
   - Use for party information, interests, and fee/royalty burdens.
   - Use for AFEs, expenditure thresholds, and consent mechanics.
   - Use for interest allocation, imbalances, and default/liens.

4. Generate operating mechanics
   - Define required Operator authority limits and prohibited actions.
   - Include approval thresholds for routine/non-routine work.
   - Include non-consent consequences and buy-in rights.

5. Build financial engine
   - Define cost categories and allocation rules (capital/opex/direct/indirect).
   - Insert billing schedule, audit rights, disputes, and payment default treatment.

6. Build title and lien stack
   - Specify title standard(s), title opinion process, curative rights, and failure consequences.
   - Define contractual lien attachment, priority mechanics, enforcement, and foreclosure workflow.

7. Build protective provisions
   - Default definitions, cure periods, remedies (advance/lien/foreclosure/offset), and succession.
   - Integration, amendment, and dispute resolution with mediation/arbitration options if requested.
   - Severability and recordation language.

8. Final legal hygiene pass
   - Cross-references validated.
   - Defined terms map and consistency check.
   - Missing data placeholders unresolved by explicit bracketed tasks.
   - Add comments for jurisdiction-sensitive options (state defaults, election clauses).

## Core Templates

### Party and Interest Schedule

```text
| Party | Legal Name | Entity Type/Jurisdiction | Address | Authority Signatory | Participating Interest | Revenue Interest | Burdens (ORR/NPI/etc.) | Non-Operator/Operator |
|------|-----------|--------------------------|--------|-------------------|-----------------------|------------------|-------------------------|----------------------|
| 1    |           |                          |        |                   |                       |                  |                         |                      |
| 2    |           |                          |        |                   |                       |                  |                         |                      |
```

### AFE Approval Matrix

```text
| AFE Type | Notable Capex/Opex Items | Estimated Cost | AFE Trigger | Review Period | Approval Rule | Non-Consent Penalty |
|----------|--------------------------|----------------|-------------|---------------|--------------|---------------------|
| Routine  |                          |                |             |               |              |                     |
| Non-Routine |                        |                |             |               |              |                     |
```

### Product and Imbalance Log

```text
| Well | Delivery Point | Revenue Interest Basis | Net Sales Volume | In-Kind Volume Taken | Over/Under Amount | Settlement/Carryforward Method |
|------|----------------|-----------------------|------------------|----------------------|------------------|-------------------------------|
```

### Default and Lien Checklist

```text
- Monetary default notice date:
- Cure period:
- Accrual interest rate:
- Default remedy stack order:
  1) advance + lien
  2) suspension of rights
  3) foreclosure or interest adjustment
- Distribution of foreclosure proceeds order:
```

### Jurisdiction and compliance callouts

- Include state-specific law stack explicitly: `[VERIFY]`
- If federal lands implicated, tie obligations to federal royalty/confidentiality/reporting rules: `[VERIFY]`
- Foreign entity language references FIRPTA/CBRE approvals only after jurisdiction confirmation: `[VERIFY]`
- ESIGN/UETA form of execution language conditioned on applicable state adoption: `[VERIFY]`
- Lien/perfection/enforcement mechanics must align with chosen state mortgage/security law: `[VERIFY]`

## Guidelines

- Do not draft without a title/interest schedule and party authority appendix.
- Do not mix participating interest and revenue interest unless tables show both and mathematically reconcile totals.
- Require mathematical checks: participating interests sum = 100%; revenue interests net of burdens reconcile to 100%.
- Use capitalized defined terms consistently and define all capitalized terms at first use.
- If a fact is unknown, insert `[CLIENT TO PROVIDE: ...]` rather than guessing.
- Keep AFE and billing language operational, not aspirational; include triggers, timelines, and remedies.
- Place all optional clauses (arbitration vs mediation, election carveouts, non-judicial foreclosure, tax language) as explicit alternative blocks with selection notes.
- Prefer contractually enforceable mechanics over soft language (“best efforts” only where necessary and narrowed by measurable actions).
- For each major duty/remedy, align to a specific section number to aid cross-reference.
- Add exhibits for: legal description, accounting procedures, assignment/joinder format, and any non-consent or expansion workflow.
