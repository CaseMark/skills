# Output Template

Produce the header and the eight parts in this order. Plain sentences; detail in tables. Every computed date shows its weekday. Every rule cited carries its section; every fact carries a source locator or `[UNVERIFIED]`.

## Contents

1. Header and source-review register
2. Part 1. Status and summary
3. Part 2. Institution type and rule map
4. Part 3. Risk assessment linkage matrix
5. Part 4. Program text or element-by-element review
6. Part 5. Clocks and retention
7. Part 6. Gaps and judgment calls
8. Part 7. Reconciliation table
9. Part 8. Hand-offs, open items and `[VERIFY]` list

## Header

- Institution legal name, institution type(s), charter or license, functional regulator and SRO, FinCEN registration (MSBs), assets or volume measure, business lines, today's date, mode (new program, program update, gap review of an existing program, single policy or procedure), preparer note: "Draft for review by counsel and the BSA/AML officer."
- Rule-status line: "Rules checked against eCFR and FinCEN releases on [date]; the April 10, 2026 proposed program rule is not in effect" (update if that has changed).
- **Source-review register**, one row per file supplied:

| File | Type | Date or version | Status | Pages or sections read | Note |
|---|---|---|---|---|---|
| name as received | existing policy, risk assessment, exam report, MRA, audit report, org chart, board minutes, procedures, customer forms, vendor template | | Reviewed / Not relevant / Unreadable after attempt / Still needed | | method tried, or who supplies it |

## Part 1. Status and summary

**Status**, one label used exactly:

- **Ready for counsel review**: no open item above Low.
- **Ready subject to listed confirmations**: open items are High or lower.
- **Not ready: blocking issues**: at least one Critical item is open. The draft is still included unless a hard stop applies; it is not presented to the board until each Critical item is closed.
- **Declined: hard stop**: a hard stop in SKILL.md applies to all or part of the request. State the reason, the part declined, and the compliant alternative produced instead. Where only part of a request is declined, give the status for the remainder on a second line.

One paragraph: what the program or policy does, the three highest risks it answers, the main gaps, and the next action.

## Part 2. Institution type and rule map

| Entity | Type | Program rule | SAR rule, threshold, deadline | CDD and 1010.230 coverage | Approval body | Independent testing standard | Other regimes (OFAC, state law, SRO) |
|---|---|---|---|---|---|---|---|

Add a line for each rule whose status matters (proposed program rule, IA rule effective January 1, 2028, CDD exceptive relief of February 13, 2026), stating "in effect" or "proposed" with the date checked.

## Part 3. Risk assessment linkage matrix

| Risk row (product, service, customer type, geography, channel) | Inherent rating | Source (risk assessment page) | Program section answering it | Control strength | Residual rating | Gap? |
|---|---|---|---|---|---|---|

List separately: sections that answer no risk row (legal minimum with rule cited, or template residue to remove); high-rated rows with no section; National Priorities reviewed and the result.

## Part 4. Program text or element-by-element review

**New program or update**, numbered sections in this order:

1. Purpose, scope, entities and business lines covered; statutory and regulatory basis.
2. Governance: approval body and approval record; board oversight and reporting cadence; BSA/AML officer designation, authority, independence, resources, reporting line, U.S. location; delegations.
3. Risk assessment: methodology summary, owner, refresh triggers and cadence, link to the matrix in Part 3.
4. Customer identification program (the type's CIP rule, e.g., 1020.220 for banks: identifying information before account opening, risk-based verification within a reasonable time, records, government list comparison, customer notice, reliance) and customer due diligence: risk profiles, risk tiers, periodic review cycles by tier, EDD triggers.
5. Beneficial ownership (covered institutions only; for others label it a policy election): ownership prong at 25 percent or more with look-through, one control person, trust rule, exclusions, timing under FIN-2026-R001, verification, records.
6. Monitoring and investigations: alert sources, review time standards, escalation, dual control.
7. SAR: definitions, threshold, clocks from Part 5, decision authority, filing, board notification, confidentiality, law enforcement requests and subpoenas, 314(a) requests (1010.520) and any 314(b) sharing (1010.540).
8. CTR, aggregation, exemptions (banks), structuring detection, monetary instrument records (1010.415), funds-transfer records and transmittal-order information for $3,000 or more (1020.410(a) for banks; 1010.410(e)-(f)).
8a. MSBs only: FinCEN registration, renewal, agent list and re-registration under 1022.380, with the clocks from Part 5.
9. Training: audiences, content by role, frequency, records.
10. Independent testing: who, independence test, scope, frequency, reporting line, remediation tracking.
11. Recordkeeping: schedule from Part 5.
12. Program maintenance: change triggers, rule-change watch, approval of amendments, version history.

Sanctions: a separate OFAC sanctions compliance program document, or a separate chapter with its own owner, authority (31 C.F.R. Chapter V), testing scope and 10-year records. Never numbered as a BSA element.

**Gap review of an existing program**, one row per element:

| Element | Rule | Existing text (section, page) | Finding | Severity | Fix |
|---|---|---|---|---|---|

Finding labels, used exactly: **Meets rule**; **Gap**; **Not applicable to this institution type**; **Policy election** (lawful choice the institution makes, stated as such).

## Part 5. Clocks and retention

| Element | Trigger event | Trigger date (weekday) and evidence | Period | Deadline (weekday) | Status | Rule |
|---|---|---|---|---|---|---|

One row per timed element, each from its own trigger. Retention table: record, period, start event, rule.

## Part 6. Gaps and judgment calls

| # | Severity | Issue | Why it matters | Source | Recommendation and alternatives | Owner |
|---|---|---|---|---|---|---|

Severity:
- **Critical**: rule for the wrong institution type applied; no current risk assessment, or a high-rated risk with no control; BSA/AML officer without authority, independence or resources; independent tester not independent under the governing rule; a SAR or CTR clock anchored to the wrong trigger; a procedure that would reveal a SAR or assist structuring; beneficial ownership definition narrower than 1010.230(d); OFAC records set below 10 years; a proposed rule presented as in force.
- **High**: approval by the wrong body; review cycles not risk-tiered; training not role-based; missing law enforcement request procedure; state law not checked.
- **Medium**: documentation and formatting gaps that do not change a control.
- **Low**: clean-up.

Judgment calls (adopting proposed-rule elements early, per-account re-certification of beneficial owners, documenting no-SAR decisions, continuing activity cadence, testing frequency) each state the options, the recommendation and the reason.

## Part 7. Reconciliation table

| Item | Value used | Source 1 (locator) | Source 2 (locator) | Conflict? | Value used and why |
|---|---|---|---|---|---|
| Institution type and regulator | | charter or license | policy header | | |
| Approval body and date | | board minutes | policy cover | | |
| BSA/AML officer and reporting line | | org chart | job description | | |
| Highest-rated risks | | risk assessment | policy scope | | |
| SAR threshold and deadline | | rule | existing policy | | |
| Independent tester and reporting line | | engagement letter | org chart | | |
| Beneficial ownership threshold and timing | | rule and FIN-2026-R001 | onboarding form | | |
| OFAC record retention | | 501.601 | policy or FFIEC manual | | |

## Part 8. Hand-offs, open items and `[VERIFY]` list

**Hand-offs.** A hand-off carries the facts the receiving workflow needs.

| To | When | What to pass |
|---|---|---|
| auditing-aml-transactions | Transaction-level testing, red-flag screening of actual transactions, lookbacks, or SAR narrative drafting | Program thresholds, risk tiers, typologies from the risk assessment, period and data set |
| bsa-risk-assessment | The risk assessment is missing, stale, or does not cover a product, channel or acquisition | Products, customer counts by segment, geographies, volumes, prior findings |
| cip-policy | A standalone CIP policy is needed | Institution type, account types, channels, verification methods |
| reviewing-kyc-documentation | Individual customer files need review against CIP, CDD or EDD standards | The procedures adopted here and the file set |
| managing-sanctions-screening | Screening design, match investigation or escalation detail for the sanctions program | Sanctions risk assessment, lists, systems, blocking and reporting procedures |
| legal-research | A rule outside this skill's register: state MSB licensing, foreign AML law, payment stablecoin issuer rules, casino rules; no dedicated skill exists | Jurisdiction, institution type, question |

**Open items**, each with owner and next action:

| # | Open item | Gap class (unknown fact / source conflict / unverified external lookup / policy election) | Owner | Next action | Blocks board approval? |
|---|---|---|---|---|---|

**`[VERIFY]` list:** each statement, why unconfirmed, what settles it.

Close with: "Draft for review by counsel and the BSA/AML officer. Not for board approval until the rule status, the institution-type rules and every Critical item are confirmed."
