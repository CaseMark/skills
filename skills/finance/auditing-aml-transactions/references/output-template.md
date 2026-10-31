# Output Template

Produce the header and the parts below in this order. Tables for detail, short sentences for conclusions. Every computed date shows its weekday; every figure carries a source locator (file, tab, row, case ID) or `[UNVERIFIED]`; every rule carries its citation from `references/primary-sources.md` or `[VERIFY]`.

## Contents

1. Header and source-review register
2. Part 1. Status, declined parts and summary
3. Part 2. Scope, population and rule map
4. Part 3. Test results (alerts and cases, SAR timeliness, thresholds, lookback, CTR and structuring, 314(a))
5. Part 4. Windows open on the review date
6. Part 5. Findings and judgment calls
7. Part 6. SAR narrative draft (when requested)
8. Part 7. Reconciliation table
9. Part 8. Hand-offs, open items and `[VERIFY]` list
10. Label tests

## Header

- Institution name, institution type for each entity whose activity is in scope, regulator, review date, requester and role, engagement type (alert or case QA, SAR QA, threshold or tuning test, lookback, CTR or structuring test, narrative), and: "Draft for review by the BSA/AML officer."
- Source-review register:

| File or excerpt | Type (case export, transaction extract, tuning file, order, KYC profile, policy, engagement letter, email) | Date and issuer | Rank | Status (Reviewed / Not relevant / Unreadable after attempt / Still needed) | Records, tabs or pages read | Note |
|---|---|---|---|---|---|---|

## Part 1. Status, declined parts and summary

Status, one label used exactly (tests in section 10):

- **Ready for BSA officer review**
- **Ready subject to listed confirmations**
- **Not ready: blocking issues**
- **Declined: hard stop** (the whole request)

Partial decline: when a hard stop applies to some items only, list each declined item on its own line as "Item [n]: Declined: hard stop (part). Reason: [hard stop number and rule]. Compliant alternative: [what is produced instead]." Then give the status label for the remainder on a separate line.

Then one paragraph: what was tested, the population and period, the main findings with severity, and the next action.

## Part 2. Scope, population and rule map

| Entity | Institution type | SAR rule, threshold, clock | CTR and exemption rules | Other (314(a), state rule) |
|---|---|---|---|---|

| Dimension | Required by (document, locator) | Tested | Difference | Label |
|---|---|---|---|---|
| Customers or accounts | | | | |
| Period | | | | |
| Products and channels | | | | |
| Entities and branches | | | | |
| Extract tie-out to core or GL | | | | |

Sampling plan: population, strata, method (statistical or judgmental), confidence, tolerable rate, expected exceptions, size and selection method, with the gap class "policy election" for parameters the institution did not set.

## Part 3. Test results

**Alerts and cases**

| Case or alert ID | Alert date (weekday) | Determination date and evidence | Closure date | Disposition taken | Tests failed (section 1 of the methods file) | Decision label |
|---|---|---|---|---|---|---|

**SAR timeliness**

| SAR | Institution type and rule | Determination date (weekday) | Suspect identified? | Due date (weekday) | Filed (weekday) | Days early or late | Timeliness label |
|---|---|---|---|---|---|---|---|

**Thresholds and tuning**

| Scenario | Old and new parameters | Period | Alerts and SARs at each setting | SARs in dropped band (% of total) | Below-the-line sample (size, parameters, results) | Threshold label |
|---|---|---|---|---|---|---|

**Lookback**: the Part 2 scope table with Scope labels, the sampling result with the upper bound, and a Sample conclusion label.

**CTR and structuring**

| Person | Business day (weekday) | Transactions (branch, account, channel, amount) | Daily cash in | CTR required? | CTR filed? | CTR due (weekday) | Structuring indicators |
|---|---|---|---|---|---|---|---|

**314(a)**: request posting date, time frame, match, report date, referral to investigations (yes or no, date).

**Independence**: each reviewer, tester or vendor, the work under test, the relationship, the independence label.

## Part 4. Windows open on the review date

| Element | Trigger event and date (weekday) | Period and rule | Due date (weekday) | Weekend or holiday effect | Status (open, past due, not applicable, not elected) |
|---|---|---|---|---|---|

List every element in the clocks table of `references/aml-reporting-rules.md` that the facts make relevant, including those not elected or not applicable, with the reason.

## Part 5. Findings and judgment calls

| # | Severity | Finding | Evidence (locators) | Rule or standard | Effect | Recommendation | Owner |
|---|---|---|---|---|---|---|---|

Judgment calls (sampling parameters, continuing-activity cadence, documenting no-file decisions, aggregation of commonly owned businesses) list the options, the recommendation and what changes under each.

## Part 6. SAR narrative draft

Only when requested and when the decision maker's determination is recorded or the draft is marked for decision. Order: subject information; summary of the activity; chronology with dates, branches, accounts, amounts; totals and counts; why unusual against the customer profile; how detected and investigated; supporting documents. Factual; no statement that a crime was committed; no reference to the customer being told.

## Part 7. Reconciliation table

| Item | Value used | Source 1 (locator) | Source 2 (locator) | Conflict? | Value used and why |
|---|---|---|---|---|---|
| Institution type | | license or charter | policy header | | |
| SAR threshold and clock | | rule | procedure | | |
| Determination date per case | | case notes | case management timestamp | | |
| Population count | | scope document or risk-rating history | extract | | |
| Transaction totals | | core extract | analyst summary | | |
| No-file documentation | | SAR FAQ Q4 | FFIEC manual or procedure | | |
| Model risk guidance | | SR 26-2 (Apr. 17, 2026) | any SR 11-7 or OCC 2011-12 citation | | |

## Part 8. Hand-offs, open items and `[VERIFY]` list

| To | When | Facts passed |
|---|---|---|
| aml-compliance-program | Its description: "Use for an AML policy, BSA program, gap analysis or board approval package". A finding requires a change to the BSA/AML program, policy or procedure (SAR clock procedure, threshold-setting policy, QA procedure, no-file documentation election) | Finding, rule, current procedure text, recommended change |
| managing-sanctions-screening | Its description: "investigating potential matches". A potential OFAC or other sanctions match appears in the data | Party, list, transaction, date; this skill does not disposition the match |
| reviewing-kyc-documentation | Its description: "reviewing KYC files". A customer file is stale or contradicts the activity and needs CIP, CDD or EDD review | Customer, profile date, activity that contradicts it |
| managing-model-risk | Its description: "validating risk models". A statistical or machine-learning scoring layer in the monitoring system needs validation | Model description, outcomes data, below-the-line results |
| bsa-risk-assessment | Its description: "when business changes trigger reassessment". Testing shows a product, channel or customer type the risk assessment omits or under-rates | Volumes, alerts, SARs by segment |
| managing-fraud-operations-banking | Its description: "managing fraud cases". The activity is a fraud loss case (account takeover, check fraud) needing investigation and recovery; SAR-decision testing stays here | Accounts, losses, dates |
| legal-research | Its description: "planning or auditing legal research". A rule outside this skill's register (state law such as NYDFS Part 504 for a non-New York question, casino rules, foreign law); no dedicated skill exists | Jurisdiction, institution type, question |

Open items: | # | Item | Gap class (unknown fact / source conflict / unverified external lookup / policy election) | Owner | Next action | Blocks conclusion? |

`[VERIFY]` list: statement, why unconfirmed, what settles it.

Close with: "Draft for review by the BSA/AML officer. Not a SAR filing decision, not an examination conclusion, and not legal advice."

## 10. Label tests

| Label | Test | Neighbour it is separated from |
|---|---|---|
| Ready for BSA officer review | No open finding above Low; no hard stop applied | Ready subject to listed confirmations |
| Ready subject to listed confirmations | Open findings are High or lower and each has an owner | Not ready: blocking issues (any Critical open) |
| Not ready: blocking issues | At least one Critical finding open | Declined: hard stop (nothing is declined; work is delivered) |
| Declined: hard stop / Declined: hard stop (part) | A Checkpoint A hard stop applies to the whole request / to listed items | Not ready (a finding, not a refusal) |
| Timely | Filed on or before 30 days after the evidenced determination date (60 for a non-MSB with no suspect identified, within the 60-day cap) | Late |
| Late | Filed after that due date, or not filed and the due date has passed | Not determinable |
| Not determinable | No determination date evidenced in the record | Timely or Late (never inferred from the alert or closure date) |
| Decision supported | The disposition follows from the evidence under every test in methods section 1 | Decision not supported |
| Decision not supported | The evidence shows a reportable SAR or CTR not filed, or a test failed that changes the outcome | Insufficient record (record exists but contradicts the decision) |
| Insufficient record | The file lacks what is needed to test the decision | Decision not supported |
| Supported (threshold) | Back-test and a below-the-line sample sized under methods section 5 show no reportable activity lost above the stated tolerable rate | Untested |
| Not supported (threshold) | Back-test or below-the-line evidence shows reportable activity the new setting would not alert | Untested (no evidence either way) |
| Untested (threshold) | No back-test of the dropped band and no below-the-line sample | Supported |
| Scope complete / Scope gap | Every dimension in the scope table ties to the governing document / any dimension excluded without written exclusion | |
| Conclusion supported by sample / Conclusion exceeds sample | The stated conclusion is no stronger than the upper bound at the stated confidence for the population tested / it claims more (zero exceptions, untested segments) | |
| Independent / Independence impaired / Not determinable | No role in the work under test and reporting line outside it / a role in the work or a reporting line to it / facts missing | |

Finding severity:
- **Critical**: a required SAR or CTR not filed or filed late; a clock anchored to the wrong trigger in procedure; a lookback or test scope gap against the governing document; a threshold change Not supported; a sample conclusion that exceeds the sample in a report going to a regulator; alerts closed or suppressed without review; any SAR or 314(a) disclosure.
- **High**: decisions not supported on stale KYC; Untested thresholds; independence impaired; 314(a) match not referred for review; missing alert-review time standard.
- **Medium**: documentation gaps that do not change an outcome.
- **Low**: clean-up.
