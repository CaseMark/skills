---
name: conducting-stark-law-analysis
language: en
description: >
  Conducts the provider-side operational review or documentation workflow across an arrangement
  portfolio: a compliance department's review of physician financial arrangements against Stark
  Law exceptions, as distinct from counsel's opinion. Builds the arrangement inventory and
  reconciles the master contract list to AP, payroll, rent rolls and gift logs to find leases,
  medical directorships, call coverage, free space, staff or services and immediate family
  arrangements; tracks expirations and holdovers; checks signatures and the 90-day writing and
  signature rule; confirms FMV documentation on file; compares compensation as written, paid and
  performed using duty logs, timesheets, call logs and lease space and equipment use; tracks 2026
  nonmonetary compensation, incidental benefit and limited remuneration limits by calendar year;
  reviews group practice productivity bonuses and referral-tracking dashboards; assembles
  escalation to counsel and CMS SRDP facts. Declines backdating. Draft for compliance review.
tags:
  - process
  - healthcare-compliance
  - compliance
metadata:
  author: casemark
  practice_areas:
    - Healthcare Compliance
    - HIPAA
    - Healthcare Regulation
  document_types:
    - Process Documentation
  skill_modes:
    - Process Management
---

# Conducting Stark Law Analysis

Produces a compliance department's operational review of a provider's physician financial arrangements under the physician self-referral law (42 U.S.C. 1395nn; 42 C.F.R. 411.350-411.389): an arrangement inventory reconciled to independent records, a document test and a performance test for each arrangement, a calendar-year limits tracker, a review of group practice compensation and referral-tracking controls, a clock table, and an escalation package for counsel. This is the provider-side operational review of arrangements against Stark exceptions for a compliance department; counsel's legal analysis and opinion stay with stark-law-aks-compliance. The aim is to keep arrangements accurately documented, paid as written and corrected through the mechanisms the regulations allow, and to send potential noncompliance to counsel early. Every output is a draft for review by the compliance officer and health care regulatory counsel; it is not a legal opinion or a disclosure decision.

## Why This Skill Exists

Stark payment denial needs no intent and reaches every DHS claim a physician referred while an arrangement was out of compliance, so most enforcement turns on operational facts: a lease nobody logged, a directorship paid after it expired, a stipend paid without hours, a rate changed by email, a gift card at the holidays. The regulations give compliance departments several ways to catch and fix these problems, but each has a narrow trigger and limit: holdovers on the same terms, the 90-day writing and signature rule, correction of unintended payment errors during the term, reconciliation within 90 days of expiration, and the nonmonetary return rule. OIG's General Compliance Program Guidance (Nov. 2023, section V.D) expects a centralized arrangements tracking process that checks logs, lease use and FMV support against contract terms. This skill runs that review and stops where counsel's legal analysis begins.

## Where Mistakes Hide

| Input / Document | What It Is Used For | Where the Error Hides |
|---|---|---|
| Master contract list and its scope (entities, physicians, family members) | Defining the population of arrangements to review | Treating the master list as the population; missing arrangements of other system entities, physician-owned LLCs, and immediate family members (a lease paid to a spouse's LLC); omitting the hospital-as-tenant direction; non-physician referral sources reviewed as Stark arrangements |
| AP register, payroll, rent roll, staffing allocations, facilities records | Finding arrangements the list misses | Directorships signed by a department head and paid through AP; free scribes, staff, storage or parking never treated as remuneration; a directorship off the master list that 411.357(d)(1)(ii) relies on when the physician has other services agreements |
| Executed agreement, signature pages, e-signature logs | Writing, signature and term | Database "active" flag accepted without the executed copy; the 90-day rule counted from the request date instead of the noncompliance date, applied to a rate change (411.354(d)(1)(ii)(C)), or applied where set in advance or FMV also fails |
| Expiration dates and payments after expiry | Holdover tracking | Expired agreements paid month to month with no holdover test; a holdover on changed terms, added space or a new rate; a holdover resting on FMV support that no longer covers it; 411.353(h) reconciliation window run from the wrong date |
| Payment register against contract rate and cap | As written versus as paid | A fixed monthly amount accepted because it is under the cap when the contract pays per documented hour; an intended rate change treated as an error; a retroactive "true-up" |
| Duty logs, timesheets, call logs | As performed | Medical directorship stipends paid with logs missing or blank; logs completed in a batch at year end and filed as if contemporaneous; hours below the minimum; duplicate directorships for the same duties |
| Lease, space map, room schedules, badge data, equipment logs | Space and equipment as used | Extra rooms, sessions or equipment used beyond the lease at no charge; lessor use of exclusive space; per-click charges on lessor-referred patients |
| Nonmonetary compensation and gift log | Calendar-year limits | Items counted against the wrong year's limit or a fiscal year; gift cards counted as nonmonetary; appreciation-event gifts left out of the total; the 411.357(k)(3) return used twice in 3 years or for a planned excess |
| Group practice compensation plan and payroll calculations | Productivity bonuses and profit shares | Bonus computed on technical-component or ancillary revenue the physician orders rather than personally performs; DHS profits split by service line in a component under five physicians; plan as written differs from payroll's method |
| Referral reports and leakage dashboards | Referral-tracking controls | Physician-level referral data reaching the compensation committee, renewal or termination decisions, or a capture-rate bonus; the dashboard treated as harmless because Stark's formula test is narrow |

## Ground Rules

1. **Draft only.** Every output is a draft for the compliance officer and health care regulatory counsel. Never call a review final, never state that an arrangement satisfies or fails an exception as a legal conclusion, and never decide disclosure. Use the labels in `references/output-template.md`.
2. **Source-review gate.** Do not call an agreement, signature, log or payment missing until every supplied file has been opened and searched, including scans and e-signature logs, with OCR tried. Classify each open item as an *unknown fact* (whether duty logs exist), a *source conflict* (the payment register differs from the contract rate), an *unverified external lookup* (the CY 2027 limits), or a *policy election* (the organization's FMV refresh interval).
3. **Hierarchy of authority.** For facts: executed agreements and signed amendments, then payment records (AP, payroll, general ledger), then contemporaneous logs and use records, then valuation reports, then the master contract database and contract-management metadata, then dashboards, emails and summaries. For rules: statute, then current eCFR text, then CMS preamble and CMS web guidance, then OIG guidance (compliance program guidance; corporate integrity agreements only as examples), then facility policy. Name every conflict in the reconciliation table and state which source controls; never resolve one silently.
4. **Citation discipline.** Every contract term carries document, section and page; every payment carries a register and line or month; every fact carries a source locator or `[UNVERIFIED]`; every rule carries a citation from `references/primary-sources.md` or `[VERIFY]`.
5. **Inventory before testing.** Reconcile the master list against independent records before testing any arrangement, and record which source revealed each arrangement the list missed.
6. **Three columns for every arrangement.** Compare compensation as written, as paid and as performed for each period. A difference is a finding even when it is below a cap.
7. **Clocks from their own triggers.** Compute each window from the trigger its rule uses, with date and weekday, and say whether it is open or closed as of today (`references/limits-and-clocks.md`, section 3). The 90-day writing and signature rule never covers a mid-term compensation change (411.354(d)(1)(ii)(C), confirmed in stark-law-aks-compliance).
8. **Limits by calendar year of receipt.** Use the CMS limit for the calendar year in which the physician received the item: CY 2026 is $535 for 411.357(k), less than $46 per occurrence for (m), and $6,237 for (z); CY 2025 is $519, less than $45 and $6,055.
9. **No backdating.** Never date a signature, agreement, amendment, log, attestation or approval earlier than the day it is actually signed or created, and never prepare a document meant to look as if it existed earlier. A record prepared late carries its real date and is labeled as prepared after the fact. Gaps are fixed through the rules that allow fixes, prospective agreements signed when signed, and escalation.
10. **Referral data stays out of pay and contract decisions.** Do not design or recommend a bonus, rate, tier, renewal or termination criterion that uses a physician's referrals or capture rate. Review where referral data goes; send intent questions to counsel.
11. **Escalate, do not adjudicate.** Potential noncompliance goes to counsel with the facts assembled. Identification under 42 C.F.R. 401.305, the disclosure path, and AKS intent are counsel's decisions; quantification goes to conducting-false-claims-analysis.

## Checkpoint A: Pre-Draft Intake (Mandatory)

Collect before Step 1:

1. Today's date, the requester and role, the organization's DHS entities in scope, and the review period.
2. Purpose: routine portfolio review, targeted review of named arrangements, expiration and holdover sweep, limits check, or pre-escalation fact assembly.
3. The master contract list export, with its fields (parties, type, dates, rate, status).
4. Independent records: AP payment register for physicians, practices and disclosed entities; payroll for employed physicians and stipends; rent roll and lease roster; staffing and shared-service allocations; nonmonetary compensation and gift logs; conflict-of-interest disclosures.
5. Executed agreements, amendments and signature records for the arrangements in scope.
6. FMV reports and business-need statements, and the organization's FMV refresh policy.
7. Duty logs, timesheets and call logs; room, space and equipment use records.
8. For a physician group: the compensation plan, payroll's calculations, and the basis for group practice status.
9. Referral reports or dashboards, who owns them and who receives them.

Defaults when an input is missing (a statute or regulation overrides any default it addresses):

- Review period not stated: the 12 months ending today, stated in the header.
- Signature date not shown: treat it as an unknown fact; never infer it from the effective date.
- No FMV refresh policy: report "No FMV refresh policy" as a control gap and apply no interval of your own.
- Payment with no matching agreement: add it to the inventory as an unmatched payment, label "Cannot determine", and request the agreement.
- Limits for a year CMS has not posted: `[VERIFY]` and use no estimate.

Hard stops (label the affected part "Declined: hard stop", explain, and continue the rest of the review):

- A request to backdate a signature, agreement, amendment, log or approval, to date any document earlier than it is signed or created, or to prepare a document meant to appear contemporaneous. Offer the lawful options: a writing signed and dated when signed, prospective terms, labeled after-the-fact attestations, and escalation.
- A request to design or draft compensation, bonus, renewal or termination terms that use referral volume, value or capture rate, or to use a referral dashboard to rank physicians for pay or contracting.
- A request to omit, soften or withhold from counsel a known finding of potential noncompliance.

Stop before testing (produce the request list only):

- No arrangement source at all: no master list, no payment records and no agreements.

Route, then continue the operational review: a request for a legal opinion that an exception is met, for AKS intent or state-law analysis, or for a disclosure decision goes to stark-law-aks-compliance.

## Step 1: Scope and Party Map

Read `references/arrangement-review-rules.md`, section 1. List the DHS entities, the physicians, their immediate family members and their entities, and the direction of each payment stream. Record the purpose, period and today's date in the header of `references/output-template.md`.

## Step 2: Build and Reconcile the Inventory

Read `references/arrangement-review-rules.md`, section 2. Open the master list, then each independent record. Add every arrangement the list misses, with the source that revealed it. Fill the source register and inventory in Part 2 of the template. List non-physician referral sources as "Outside this review" with their route.

## Step 3: Document Test

Read `references/arrangement-review-rules.md`, sections 3 and 5, and `references/limits-and-clocks.md`, section 3. For each arrangement, locate the executed copy and record signers, signature dates, term, what is specified, master-list cross-reference, holdover or renewal status, FMV support and business-need statement. For every expired arrangement still paid, test the holdover conditions; for every late signature, compute the 90-day window from the noncompliance date.

## Step 4: Performance Test

Read `references/arrangement-review-rules.md`, section 4. Build the as-written, as-paid and as-performed columns by month. Show the arithmetic of every difference. Check logs for directorships and stipends and use records for space and equipment. Label an ongoing unintended discrepancy "Gap: correct within the rules" only when counsel can confirm it was unintended; otherwise escalate.

## Step 5: Limits Tracker

Read `references/limits-and-clocks.md`, sections 1 and 2. Assign each item to the calendar year of receipt and that year's limit. Exclude cash and cash equivalents from (k) and list them as findings. Include appreciation-event gifts. Compute year-to-date totals and headroom; test any excess against the (k)(3) conditions and deadline.

## Step 6: Group Practice Plans and Referral-Tracking Controls

Read `references/arrangement-review-rules.md`, sections 6 and 7. For each plan component, record whether it rests on services personally performed, incident-to services, or DHS the physician orders, and which 411.352(i) condition applies. For each referral report, record who sees it and whether it reaches pay, renewal or contracting decisions.

## Step 7: Labels, Clocks and Escalation

Read `references/arrangement-review-rules.md`, section 8, and `references/limits-and-clocks.md`, sections 3 to 5. Assign one label per arrangement and period. Fill the clock table. Assemble the escalation memo for counsel with the facts in section 4 of the limits file, and the hand-offs.

## Step 8: Assemble and Check Sources

Complete Parts 1 and 8 to 10 of `references/output-template.md`. Check each rule relied on against `references/primary-sources.md` and carry any `[VERIFY]` flag into the open items.

## Checkpoint B: Post-Draft Alignment

1. Does the inventory include arrangements found only in independent records, and does it say where each was found?
2. Does every arrangement have as-written, as-paid and as-performed columns for each period?
3. Is every clock computed from its own trigger, with weekday and open or closed status as of today?
4. Is every limit tied to the calendar year of receipt and that year's CMS figure?
5. Does any sentence state a legal conclusion, a disclosure path decision or a penalty estimate? Move it to the questions for counsel.
6. Is any document dated, or recommended to be dated, earlier than it is signed or created? Remove it.
7. Are the escalations and open items owned, with next actions?

If the user does not answer, recommend first matching payments to executed agreements and locating signature dates; those facts decide most labels.

## Quality Audit

1. The header states today's date, entities, period, purpose and the draft line.
2. The inventory was reconciled to AP, payroll, rent roll, staffing and gift records, and each added arrangement names its source.
3. Immediate family members and physician-owned entities are in the party map.
4. Each arrangement has an executed-copy check with signature dates, or is "Cannot determine" with the missing document named.
5. Every expired arrangement still paid has a holdover test: term at least 1 year, met at expiry, same terms, continues to meet the exception including FMV.
6. No 90-day writing and signature window is applied to a compensation change, or counted from anything but the noncompliance date.
7. Payments are compared with the written rate per period, with arithmetic shown, and directorship payments are compared with logs.
8. Space and equipment use is compared with what the lease specifies.
9. Limits use the calendar year of receipt, the CMS figure for that year, no cash equivalents, and appreciation-event gifts.
10. Group plan components are tied to personally performed, incident-to or ordered services and to a 411.352(i) condition.
11. Referral data uses are listed, and nothing recommends using referrals in pay or contract decisions.
12. Labels are used exactly as in `references/output-template.md`; no legal conclusion, disclosure choice or penalty estimate appears.
13. No document is backdated or recommended to be; late records carry their real dates.

## Guidelines

- Write for a reader who will check every number: compliance committee, internal audit, counsel, and possibly a government reviewer.
- A finding is not an accusation. "Potential noncompliance: escalate to counsel" moves facts to the people who decide.
- Separate prospective controls (fix the database, stop the fixed AP payment, set renewal alerts well before expiry) from look-back facts (what was paid, when, under what writing).
- Renewal alerts, holdover reports and limit trackers are controls; recommend owners and frequencies, and leave the organization's policy elections to it.
- Keep physician compensation data and referral data to the people who need them for this review.

## Troubleshooting

| Problem | Likely cause | What to do |
|---|---|---|
| Executed agreement cannot be found | Contract database stores drafts; signatures on a separate page | Search email and e-signature logs; treat as unsigned until found; compute the 90-day window from the noncompliance date |
| Signature page undated | Wet signature without a date | Use e-signature or transmittal metadata if any; otherwise an unknown fact; never assign a date |
| Scanned agreement or log unreadable | Image-only file | Try OCR; list unreadable pages and the tests that depend on them as "Cannot determine" |
| Payment register and contract rate differ | Unrecorded amendment, payroll setup error, or retroactive change | Record both; the register shows what was paid; ask who set the rate and when; escalate if the cause is unknown |
| Logs exist only as year-end summaries | Batch completion | Record the creation dates; do not treat them as contemporaneous; escalate if payments depended on them |
| Gift log uses a fiscal year or a single limit | Tool configuration | Re-sort by date of receipt into calendar years and apply each year's limit; record the tool's rule in the reconciliation table |
| Group practice status unknown | No counsel memo | Request it; review the plan under 411.352(i) and mark group status "Cannot determine" |

## Related Skills

- stark-law-aks-compliance: counsel's legal analysis and opinion on whether an exception is met, AKS intent, state law, and the disclosure decision (CMS SRDP or OIG SDP).
- conducting-false-claims-analysis: exposure and overpayment quantification, FCA risk and settlement modeling once potential noncompliance is escalated.
- conducting-anti-kickback-analysis: provider-side safe harbor documentation for arrangements with non-physician referral sources.
- healthcare-services-agreement: drafting a new or renewed directorship or services agreement, signed and dated when actually signed.
- physician-employment-agreement: drafting employment terms once counsel has approved the compensation structure.
- managing-compliance-programs: program-wide policies, training, auditing plans and the arrangements tracking policy itself.
- legal-research: state self-referral or licensure questions not covered by stark-law-aks-compliance; no dedicated med skill exists.

## Reference Files

- `references/arrangement-review-rules.md`: party map, inventory reconciliation, document and performance tests, FMV file, group practice plans, referral-tracking controls, escalation triggers.
- `references/limits-and-clocks.md`: calendar-year limits for 2023-2026, counting rules, clock table with each trigger, facts for counsel's disclosure decision, date arithmetic.
- `references/output-template.md`: review status and finding labels, inventory, document and performance tests, limits tracker, clock table, reconciliation table, escalation package, hand-off table.
- `references/primary-sources.md`: each authority read with URL, method, date and what it supports; corrections to the prior version; the `[VERIFY]` list.
