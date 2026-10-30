# Output Template

Produce the header and the eight parts in this order. Keep sentences plain; put detail in tables. Every date shows its weekday. Every legal statement carries a citation from `references/primary-sources.md` or `[VERIFY]`; every company fact carries a source locator or `[UNVERIFIED]`.

## Contents

1. Header and source-review register
2. Part 1. Status and elections
3. Part 2. Scope map
4. Part 3. Policy text
5. Part 4. Program gap analysis
6. Part 5. Blocking issues and judgment calls
7. Part 6. Reconciliation table and clocks
8. Part 7. Hand-offs, open items and `[VERIFY]` list
9. Declined output

## Header

- Company, group entities covered, requester and role, deliverable type (new policy, revision, review of existing policy, gap memo), today's date, preparer note: "Draft for counsel review."
- **Source-review register**, one row per item supplied:

| File or input | Type | Date | Status | Note |
|---|---|---|---|---|
| name as received | existing policy, risk assessment, entity chart, SEC filing, third-party list, GL extract, audit report, local-law memo, deal file | | Reviewed / Not relevant / Unreadable after attempt / Still needed | method tried, or who supplies it |

## Part 1. Status and elections

**Policy status**, one label used exactly:

- **Ready for counsel review**: no open item above Low.
- **Ready subject to listed confirmations**: open items are High or lower.
- **Not ready: blocking issues**: at least one Critical item is open. The draft is still produced unless a hard stop applies.
- **Declined: hard stop**: a hard stop in SKILL.md applies. Use the declined output below.

**Facilitation-payment election**, one label used exactly, with the facts relied on:

- **Facilitation payments: prohibited** (with the duress and safety exception)
- **Facilitation payments: permitted only within the FCPA exception** (conditions listed; never where the UK Bribery Act or local law reaches the payer)

**Counterparty classification**, one label per counterparty or class:

- **Foreign official** (basis: factors met)
- **Treat as foreign official pending classification** (missing facts listed)
- **Not a foreign official** (basis stated; used only after the control and function factors are recorded)

Then one paragraph: what the policy does, the main risks it addresses, and the most important open item.

## Part 2. Scope map

| Entity or person class | Status (issuer, domestic concern, other person, UK relevant commercial organisation) | Statutes applied | Accounting provisions apply? | Facts and source |
|---|---|---|---|---|

Enforcement-posture note, dated: the statute and limitation periods are unchanged; the current DOJ guidelines and CEP are stated with the date checked; the policy does not rely on them.

## Part 3. Policy text

Sections, in this order. Omit none; say "Not applicable" with the reason where one does not apply.

1. Purpose, commitment from the board and senior management, and scope (entities, people, third parties).
2. Definitions: foreign official (with instrumentality test and classification procedure), anything of value, intermediary, facilitation payment, duress.
3. Prohibitions: bribery of officials and commercial bribery; indirect payments; the knowing standard; acceptance of bribes; reporting demands and solicitations.
4. Facilitation payments: the election and its conditions.
5. Gifts, travel, hospitality, donations, sponsorships, political contributions, hiring: the purpose test, then approval triggers.
6. Third parties: tiers, diligence, red flags, contract clauses, payment controls, refresh.
7. Books, records and internal controls (issuer version, or company-policy version for a private company).
8. Mergers, acquisitions and joint ventures.
9. Local law and country annexes.
10. Training and communication.
11. Reporting, non-retaliation, investigations.
12. Discipline, incentives, and no indemnity of individual criminal fines.
13. Monitoring, testing, review, and ownership of the policy.
Appendices: approval forms, third-party questionnaire, red-flag card, country annex template.

## Part 4. Program gap analysis

| Element | ECCP question (designed / resourced / works in practice) | MoJ principle | Current state and source | Gap | Recommendation | Owner |
|---|---|---|---|---|---|---|

## Part 5. Blocking issues and judgment calls

| # | Severity | Issue | Why it matters | Source | Recommendation and alternatives | Owner |
|---|---|---|---|---|---|---|

Severity: Critical (issuer status unknown; UK nexus unknown where facilitation payments would be permitted; a known red flag on a live payment; a counterparty classified "Not a foreign official" without factors; a provision conflicting with the statute); High (local-law conflict unresolved; no risk assessment; thresholds without purpose test in the existing policy); Medium (training gaps, missing annex); Low (clean-up).

Judgment calls (facilitation-payment election, threshold amounts, tier triggers, country annexes, escalation of a past payment to counsel) each state the options, the recommended choice and the reason.

## Part 6. Reconciliation table and clocks

| Item | Source 1 (locator) | Source 2 (locator) | Conflict? | Value used and why |
|---|---|---|---|---|
| Issuer status | SEC filing or registration | requester's statement | | |
| UK business presence | entity chart, office list | requester's statement | | |
| Countries and government customers | risk assessment | sales data | | |
| Intermediary compensation | contract | invoices, ledger | | |
| GL description of payments | ledger | invoice and contract | | |
| Threshold amounts | existing policy | proposed policy | | |

**Clocks**, one row per timed element, each from its own trigger:

| Element | Trigger event | Trigger date (weekday) and evidence | Period | Date or days elapsed | Source |
|---|---|---|---|---|---|

## Part 7. Hand-offs, open items and `[VERIFY]` list

**Hand-offs.** A hand-off carries the facts the receiving workflow needs.

| To | When | What to pass |
|---|---|---|
| due-diligence-report | An acquisition target needs anti-corruption diligence findings in a deal report | Target countries, government customers, intermediaries, findings, closing date |
| merger-agreement | Anti-corruption representations, indemnity or closing conditions are needed | Findings, risk rating, remediation plan |
| whistleblower-policy | The company needs a standalone reporting and non-retaliation policy | Channels, non-retaliation terms, investigation owner |
| code-of-conduct-and-ethics | The anti-corruption policy must sit inside a company-wide code | Policy summary and cross-references |
| corporate-compliance-checklist | A program-wide assessment beyond anti-corruption is needed | Gap analysis from Part 4 |
| aml-compliance-program | A financial institution needs BSA/AML program design alongside anti-corruption | Entity, products, risk assessment |
| legal-research | A past payment, internal investigation or self-disclosure decision needs counsel's analysis (no dedicated skill exists), or a foreign anti-corruption law needs research | Facts, dates, amounts, people, documents, clocks from Part 6 |

**Open items**, each with owner and next action:

| # | Open item | Gap class (unknown fact / source conflict / unverified external lookup / policy election) | Owner | Next action | Blocks adoption? |
|---|---|---|---|---|---|

**`[VERIFY]` list:** each statement, why it is unconfirmed, and what would settle it.

Close with: "Draft for counsel review. Not for adoption until counsel confirms the scope map, the facilitation-payment election, and every [VERIFY] item."

## Declined output

When a hard stop applies, produce only:

1. Status line: **Declined: hard stop**, and which hard stop.
2. The reason in two or three sentences, citing the rule (for example 15 U.S.C. 78m(b)(5); ECCP paper-program inquiry).
3. What the skill will do instead: a compliant policy on the same subject, a red-flag escalation note, or a hand-off to legal-research for counsel.
4. No draft of the declined provision, version or record, and no partial text of it.
