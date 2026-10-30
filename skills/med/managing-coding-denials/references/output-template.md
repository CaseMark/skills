# Output Template

Produce the header and sections in order. Every date shows its trigger and source; every clinical value shows its source, date, time and author role. Keep the narrative short and put detail in tables.

## Contents

1. Header
2. Section 1. Determination summary
3. Section 2. Denial register and clock table
4. Section 3. Source register and record-integrity check
5. Section 4. Classification and argument map
6. Section 5. Route election
7. Section 6. Appeal letter draft
8. Section 7. Peer-to-peer and discussion log
9. Section 8. Reconciliation table
10. Section 9. Gaps
11. Section 10. Hand-offs
12. Section 11. Open items, declined requests and `[VERIFY]` list

## Header

- Claim identifier (de-identified unless the environment requires otherwise), dates of service ("From" and "Through"), bill type, payer and product (Medicare FFS, Medicare Advantage HMO or PPO, commercial, ERISA plan), contract status (contracted or non-contracted), current appeal level.
- Today's date and the date of every notice relied on.
- Preparer note: "Draft for coder, CDI, denials and compliance review. Not legal advice."

## 1. Determination summary

| Denied item | Denial type | Recommendation | Next deadline (received by) | Deadline status | Blocking open items |
|---|---|---|---|---|---|
| | Coding validation / Clinical validation / Medical necessity or status / Technical | Appeal / Correct and rebill / Request reopening / Accept denial / Hold: <fact> | | Open / Urgent (10 days or fewer) / Expired: good cause only | |

## 2. Denial register and clock table

Denial register: notice type (ERA, demand letter, review results letter, organization determination, audit letter), issuer (MAC, RAC, UPIC, QIC, MA plan, commercial payer), notice date, CARC/RARC or reason text, amount, codes or status changed.

Clock table, one row per timed element, each with its own trigger:

| Element | Trigger event and date | Rule | Arithmetic | Must be received by | Received by whom |
|---|---|---|---|---|---|
| Redetermination | Notice date + 5 days presumed receipt | 405.942 | notice + 5 + 120 | | MAC |
| Recoupment stop | Demand letter date | 405.379(d) | day 41 | | MAC |
| Part B inpatient window | Through date | 414.5(c); 424.44 | through date + 1 calendar year | | MAC |
| MA reconsideration | Organization determination notice date + 5 | 422.582(b) | notice + 5 + 60 | | Plan or named delegate |
| Commercial appeal | Trigger named in the contract | Contract section | | | Payer address in contract |

Say which threshold year applies to any ALJ or court request and show the amount-in-controversy computation.

## 3. Source register and record-integrity check

| Document | Author role | Created (date, time) | Created before claim? | Created after denial? | Status | Use |
|---|---|---|---|---|---|---|
| | | | Yes / No | Yes / No | Reviewed / Unreadable after attempt / Still needed | Original evidence / Late entry, disclosed / Not used |

## 4. Classification and argument map

| Denial issue | Type | Reviewer's standard | Controlling standard | Record evidence (locator) | Argument | Weakness and response |
|---|---|---|---|---|---|---|

For clinical validation rows, add the definition applied (with contract section or `[VERIFY]`) and a criterion-by-criterion table: criterion, value, date and time, source, met or not met.

## 5. Route election

| Route | Deadline and trigger | What it can recover | What it forecloses or risks | Owner decision needed |
|---|---|---|---|---|
| Appeal at <level> | | | | |
| Corrected claim, reopening or DRG review request | | | | |
| Part B inpatient claim | | | | |
| Accept denial | | | | |

## 6. Appeal letter draft

Letter skeleton (fill only the sections the denial type needs):

1. Identification: claim, dates of service, notice date and reference, level requested, deadline and how it was computed.
2. Issue statement in the reviewer's own words, and the denial type.
3. Scope or authority objection, if any (for example, RAC clinical validation; MA criteria not publicly posted; prior approval under 422.138(c)).
4. Coding validation section: provider documentation quoted with locators; guideline section.
5. Clinical validation section: the definition that applies and why; criterion table with sourced values.
6. Medical necessity or status section: 412.3 expectation at the order; complex medical factors; time counted.
7. Requested action and enclosures list (each enclosure dated; late entries labeled as late entries with their dates).

No denial-mitigation or payment language belongs in any provider query; it may appear in the appeal letter only as the requested action.

## 7. Peer-to-peer and discussion log

| Date and time | Payer reference | Participants and credentials | Issue | Outcome stated | Written confirmation received? | Effect on deadline |
|---|---|---|---|---|---|---|

## 8. Reconciliation table

| # | Fact | Source A says | Source B says | Controlling source and why | Effect |
|---|---|---|---|---|---|

Typical rows: denial letter's summary of the record against the record itself; ERA date against letter date; abstract codes against the provider's final diagnostic statement; mailroom receipt against the date the team saw the letter.

## 9. Gaps

| Gap | Affects | Gap class (unknown fact / source conflict / unverified external lookup / policy election) | Who can resolve | Next step |
|---|---|---|---|---|

## 10. Hand-offs

| To skill | Why | What is passed | What this review did not do |
|---|---|---|---|
| managing-drg-optimization | DRG assignment behind a downgrade | Codes, documentation, denial rationale | Did not regroup the claim |
| managing-cdi-programs | Compliant query where documentation conflicts | Indicators and locators | Did not draft the query |
| conducting-false-claims-analysis | Altered records, overpayment, pattern of unsupported codes | Findings and dates | Did not assess FCA exposure |
| managing-observation-stays | Status determination under 412.3 | Timeline and orders | Did not decide status |

## 11. Open items, declined requests and `[VERIFY]` list

| # | Item | Depends on | Owner | Next action | Changes the recommendation? |
|---|---|---|---|---|---|

Declined requests: each request declined, the rule behind it, and what was done instead.

Close with: "Draft for coder, CDI, denials and compliance review. Appeal outcome depends on payer adjudication and the record as billed."
