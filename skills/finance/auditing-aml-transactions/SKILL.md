---
name: auditing-aml-transactions
language: en
description: >-
  Performs and reviews transaction-level BSA/AML testing for U.S. banks, credit
  unions, money services businesses and broker-dealers: alert and case review
  and QA sampling, lookbacks, transaction-level testing of monitoring
  thresholds and below-the-line sampling, structuring and CTR aggregation
  across branches and linked accounts, 314(a) match follow-up, SAR decisioning
  support, SAR timeliness, SAR narrative drafting and SAR QA sampling, and
  reviewer independence. Applies the SAR threshold and clock for the actual
  institution type (31 C.F.R. 1020.320; 1022.320 with $2,000 and no extension
  for MSBs), starts the clock at determination, not the alert, treats
  continuing-activity review and no-SAR documentation as elections under the
  October 2025 SAR FAQs, and sizes samples to the conclusion drawn. Declines to
  suppress, reclassify or close alerts to avoid filing, or to tip off a
  customer. Routes AML program and policy design to aml-compliance-program.
  Drafts for BSA/AML officer review.
tags:
  - compliance
  - financial-compliance
  - aml
metadata:
  author: casemark
  practice_areas:
    - Regulatory Compliance
    - Financial Regulation
    - Compliance
  document_types:
    - Compliance Report
  skill_modes:
    - Audit
    - Review
---
# Auditing AML Transactions

Tests an institution's actual transactions, alerts, cases and filings against the Bank Secrecy Act rules for its type: alert and case QA, SAR timeliness and decision testing, threshold and below-the-line testing, lookbacks, CTR aggregation and structuring tests, 314(a) follow-up, and SAR narrative drafts. The aim is to find reportable activity that was missed and controls that do not work, so the institution can file what it owes and fix its monitoring; reducing alert volume is a legitimate aim only when the evidence shows nothing reportable is lost. The deliverable follows `references/output-template.md`: status, scope and population, test results, open windows, ranked findings, reconciliation, hand-offs and open items. Everything is a draft for review by the BSA/AML officer; it is not a SAR filing decision, an examination conclusion or legal advice.

## Why This Skill Exists

Transaction testing fails on anchors and populations, not on typologies. A QA team counts SAR days from case closure, so every late filing passes. A money transmitter borrows a bank's $5,000 threshold and 60-day extension and closes $3,000 structuring cases as "below threshold". A structuring scenario's threshold is raised to cut alerts, the SAR-per-alert ratio improves, and nobody looks at what stopped alerting. A lookback is run on accounts open on the extract date, so every account closed during the period, which is where the worst activity often sits, is never reviewed; then 25 clean files become "no unreported activity at 95% confidence". A customer deposits $9,500 at one branch and $4,000 at another the same day, and the CTR system, aggregating per account, files nothing. And in 2025 and 2026 the rules moved: continuing-activity reviews and no-file write-ups became elections, and SR 11-7 was superseded. This skill makes each anchor, population and parameter explicit and tests it against the record.

## Where Mistakes Hide

| Input / Document | What It Is Used For | Where the Error Hides |
|---|---|---|
| Institution charter, license and FinCEN registration | SAR threshold, clock and CTR exemption rules for the entity tested | Bank $5,000 and 60-day extension applied to an MSB (1022.320 sets $2,000 and no extension); "no minimum for MSBs"; the $25,000 no-suspect tier cited to 1020.320 instead of the bank agencies' rules; a check casher treated as a mandatory SAR filer; affiliates in the population tested under the parent's rule |
| Alert logs, case timestamps and SAR filing records | SAR timeliness and decision testing | Clock counted from case closure or SAR drafting, so late SARs pass; or from the alert, so timely SARs fail; continuing SAR anchored to detection or called mandatory; review delay never measured |
| Monitoring scenario thresholds, tuning file and model documentation | Whether thresholds still detect reportable activity | Threshold raised on above-the-line productivity alone with no back-test of the dropped band and no below-the-line sample; SR 11-7 or SR 21-8 cited as current after April 17, 2026; a deterministic rule declared exempt from all testing |
| Lookback order, scope letter and population extract | Who and what is in the population | Closed accounts, a migrated period, a product or channel, or an affiliate left out of the extract; extract not tied to the core; conclusion stated for the whole population |
| Sampling plan and test results | Strength of the conclusion | 25 clean items reported as "no exceptions at 95% confidence"; judgmental samples projected; strata with different risk pooled; exceptions not projected or followed by expanded testing |
| KYC profile used to close an alert | The "expected activity" baseline | Closure on a profile years past its refresh cycle, or on an occupation the activity contradicts; linked accounts and conductors not checked |
| Cash transaction data and CTR records | CTR completeness and structuring detection | Aggregation per account or per branch instead of per person per business day; ATM and night deposits left out; single-transaction rules that cannot see deposits just under $10,000 over several days; CTR-exempt customers dropped from monitoring |
| 314(a) match log | Follow-up on FinCEN requests | Match confirmed to FinCEN but never referred for activity review; SAR filed solely on the match; the request disclosed to a relationship manager or the customer |
| QA roster, testing engagement letter and org chart | Reviewer and tester independence | QA reviewer checks own team's alerts; lookback vendor tested scenarios it designed; tester reports to the BSA function it tests |
| The request itself: who asks, for what, and to what end | Scope of what this skill will produce | Bulk closure, reclassification or threshold changes meant to avoid SARs, exemptions for valued customers, or a letter telling a customer about a SAR, accepted as ordinary backlog or customer-service work |

## Ground Rules

1. **Draft only.** Every test result, finding and narrative is a draft for the BSA/AML officer. Never call a review final, examination-ready or accepted, never file anything, and never sign off a report to a regulator.
2. **Source-review gate.** Never call a record missing until the inventory is checked and each file opened, including every tab of an extract and every case note. Classify each open item as an **unknown fact** (determination date not in the file), a **source conflict** (case timestamp against analyst note), an **unverified external lookup** (current OFAC or FATF list), or a **policy election** (sampling confidence, continuing-activity cadence, no-file write-ups).
3. **Hierarchy of authority.** For law: 31 U.S.C. and 31 C.F.R. Chapter X, then the banking agencies' SAR rules, then an enforcement order's terms for its own scope, then interagency FAQs and FinCEN guidance, then the FFIEC manual, then non-binding model risk guidance, then institution policy and vendor documents. For facts: system-of-record transaction data and core extracts, then case management records and timestamps, then case narratives, then summaries, spreadsheets and emails. Name each conflict in the reconciliation table (the FFIEC manual's no-file documentation passage against FAQ Q4) and state which controls; never resolve one silently.
4. **Citation discipline.** Every figure carries a locator (file, tab, row, case ID) or `[UNVERIFIED]`; every rule carries its citation from `references/primary-sources.md` or `[VERIFY]`. Never invent a threshold, deadline or citation.
5. **Institution type sets the rule.** Determine each tested entity's type before testing; use that type's threshold, clock and exemption rules (`references/aml-reporting-rules.md`, section 1).
6. **Each clock from its own trigger.** The SAR clock runs from determination, never from the alert, case closure or drafting date; each other element uses its own trigger. Dates show weekdays; no weekend roll-forward is assumed.
7. **Elections are labeled.** Continuing-activity reviews, written no-file rationales, alert-review time standards and sampling parameters are institution choices. Test compliance with the institution's choice; never call an election a legal requirement or its absence a violation.
8. **No threshold conclusion without below-the-line evidence.** A tuning or threshold change is never called effective on above-the-line productivity alone.
9. **Conclusions no stronger than the sample and the population.** State confidence, tolerable rate and upper bound; never report "no exceptions in the population" from a sample, and never extend a conclusion to a segment not tested.
10. **Population before testing.** Reconcile customers, period, products, channels and entities to the governing document and the extract to the core before any sample is drawn.
11. **No suppression, no tipping off.** Decline any request to close, reclassify, downgrade, suppress or re-tune alerts or cases, or to exempt customers, in order to avoid a SAR or CTR; and any request to reveal a SAR or a 314(a) request. Meet the legitimate aim in the same request (a backlog, false positives, customer friction) by compliant means.
12. **The SAR decision belongs to the institution.** This skill recommends and drafts; the designated decision maker decides. Narratives state facts and never assert that a crime was committed.
13. **Sanctions stand apart.** A potential OFAC match is escalated to the sanctions process and handed off; it is never dispositioned here.

## Checkpoint A: Pre-Draft Intake (Mandatory)

Collect, from records where possible:

1. Today's date; requester and role; engagement type (alert or case QA, SAR QA, threshold test, lookback, CTR or structuring test, narrative).
2. Each tested entity's legal name and institution type, regulator, and any affiliates or agents whose activity is in the population.
3. The governing document for scope (order, agreement, engagement letter, audit plan) and any report deadline in it.
4. Transaction-level data for the population and period: core extracts, cash and teller logs with branch and conductor, wires, ACH, RDC, card and ATM data, with control totals.
5. Alert and case records: alert, determination, closure and filing dates; notes; decision maker; SAR copies; CTR and Form 110 files.
6. Scenario documentation: parameters before and after changes, effective dates, approvals, back-tests, prior validation reports.
7. KYC profiles with refresh dates and risk ratings; 314(a) request postings, matches and responses.
8. Procedures: SAR, alert review time standard, QA, sampling standard, continuing-activity election, no-file documentation election.
9. QA and tester roster, reporting lines, vendor engagements.

**Defaults if not supplied** (each recorded as a policy election or unknown fact; a governing rule overrides any default it addresses): sampling at 95% confidence and 5% tolerable rate with zero expected exceptions (59 items) unless the order or institution sets otherwise; no continuing-activity cadence unless the institution elects one (FAQ Q2); no-file write-ups not required (FAQ Q4) unless the institution's procedure requires them; alert-review time standard "not set", recorded as a High finding; KYC refresh cycle as the institution's policy states, otherwise "unknown fact".

**Hard stops** (label each declined item "Declined: hard stop (part)" and continue with the rest, or "Declined: hard stop" when the whole request falls):
1. A request, from the requester, a business line, relationship manager, vendor, affiliate or anyone else, to close, reclassify, downgrade, suppress or re-tune alerts or cases, or to exempt named customers, segments or the customers' owners or affiliates from alerting or SAR decisioning, for the purpose of avoiding a SAR or CTR or because of the relationship's value. Produce the compliant alternative.
2. A request to disclose a SAR, information that would reveal one, or a 314(a) request, to the subject, its owners, signers, affiliates or agents, or anyone outside the permitted channels (`references/aml-reporting-rules.md`, sections 7 and 8).
3. No transaction-level data and no case records for the population are supplied as a file, fixture or labeled excerpt, only descriptions: produce the test plan and data request only, and draw no conclusion on whether transactions were reportable, alerts correctly decided or filings timely. Reviewing a scope document, a tuning file or a report's methodology against counts supplied as labeled excerpts is not blocked.
4. The institution type of an entity whose activity is tested cannot be determined from the record or the requester: no SAR threshold or timeliness conclusion for that entity; other tests proceed.

**Not hard stops** (findings, usually Critical or High): stale KYC, untested thresholds, scope gaps, independence problems, late filings, a request to treat a proposed rule as final.

## Step 1: Intake, Institution Type and Request Screen

Build the source-review register in `references/output-template.md`. Fill the rule map for each entity from `references/aml-reporting-rules.md`, section 1. Compare each requested item against the hard stops; label any declined item and draft its compliant alternative before doing anything else.

## Step 2: Scope and Population

Read `references/testing-methods-and-typologies.md`, section 4. Reconcile customers, period, products and channels, entities and extract totals to the governing document. Label each dimension "Scope complete" or "Scope gap", with the count or days missing.

## Step 3: Sampling Plan

Read `references/testing-methods-and-typologies.md`, section 5. Set strata, method, confidence, tolerable rate and size; record parameters as policy elections where the institution set none. For any existing sample, compute the upper bound it supports and compare it with the conclusion stated.

## Step 4: Alert and Case Review

Read `references/testing-methods-and-typologies.md`, sections 1, 8 and 9, and `references/aml-reporting-rules.md`, sections 3 and 4. For each sampled alert or case, test the activity reviewed, the KYC basis and its date, linked accounts and conductors, the rationale against evidence, the decision maker, and confidentiality. Screen against the typologies. Assign Decision supported, Decision not supported or Insufficient record.

## Step 5: SAR Timeliness and Decisioning

Read `references/aml-reporting-rules.md`, sections 1 to 4. For each SAR, take the evidenced determination date, apply the type's clock, and label Timely, Late or Not determinable with dates and weekdays. For each no-file decision, test against the threshold and definitions for the type. For reportable activity not filed, compute the due date and recommend filing without further delay. Test continuing SARs only if the institution elects the cadence, from the prior filing date.

## Step 6: Thresholds and Below-the-Line Testing

Read `references/testing-methods-and-typologies.md`, sections 2 and 3. Compute alerts and SARs at old and new settings over the same period, the SARs in the dropped band and the percent lost; design or evaluate the below-the-line sample; label the threshold Supported, Not supported or Untested. Route statistical or machine-learning model validation to managing-model-risk.

## Step 7: CTR Aggregation, Structuring and 314(a)

Read `references/aml-reporting-rules.md`, sections 5 to 7. Aggregate cash in and cash out per person per business day across branches, accounts and channels; list CTRs required, filed and due. Test multi-day and multi-branch patterns just under $10,000 against single-transaction rules, and look for evidence of intent. Check 314(a) matches for timely reporting, referral for review and nondisclosure.

## Step 8: Independence, Narrative and Assembly

Read `references/testing-methods-and-typologies.md`, sections 6 and 7. Label the independence of each reviewer, tester and vendor. When asked, draft the SAR narrative in the template's order. Fill the windows table for every element relevant on the review date, rank findings by the template's severity tests, complete the reconciliation table, hand-offs, open items and `[VERIFY]` list, and assign the status label.

## Checkpoint B: Post-Draft Alignment

Confirm with the user or list as open items:

1. Is each entity's institution type right, and does any affiliate or agent in the population need its own rule?
2. Is every determination date taken from the record, and does the institution agree with the dates used?
3. Does the institution elect continuing-activity reviews or written no-file rationales?
4. Are the sampling parameters the institution's or the order's, or this draft's elections?
5. Does the population match the governing document, and who will close each scope gap?
6. Does any finding change the program or policy, so that aml-compliance-program should take it?

## Quality Audit

1. Every tested entity's institution type and its SAR rule, threshold and clock are stated, and no bank provision is applied to an MSB.
2. Every SAR timeliness result runs from an evidenced determination date; none runs from an alert, closure or drafting date; each date shows its weekday.
3. Continuing-activity review and no-file documentation are described as elections, and any continuing SAR is anchored to the prior filing date.
4. No threshold is labeled Supported without a back-test and a below-the-line sample; the percent of SARs lost in the dropped band is computed.
5. The population ties to the governing document and the core; every exclusion is a Scope gap or has a written exclusion.
6. Every sample conclusion states confidence, tolerable rate and upper bound and covers only the population tested.
7. CTR tests aggregate per person per business day across branches, accounts and ATM or night deposits; structuring tests span days and branches.
8. Each 314(a) match is checked for report timing, referral for review and nondisclosure.
9. Each closure on KYC states the profile date and whether it was current for the risk tier.
10. Independence is labeled for each reviewer, tester and vendor.
11. No output suppresses or closes alerts to avoid filing, exempts customers, or reveals a SAR or 314(a) request; each declined item carries "Declined: hard stop (part)" or "Declined: hard stop" and a compliant alternative.
12. SR 11-7, SR 21-8, OCC 2011-12 and OCC 2021-19 are not cited as current; the April 10, 2026 FinCEN program proposal is not cited as in force.
13. Labels are used exactly as in `references/output-template.md`, every open window is listed, and the closing draft line is present.

## Guidelines

- Write for the BSA/AML officer and an examiner at once: each finding states the record, the rule, the effect and the fix.
- Recompute every total, count and date from the data; never copy an analyst's figure without tying it.
- Separate what a rule requires from what the institution elected, so a change in election is not read as a violation.
- A backlog is a resourcing and prioritization problem; solve it with risk-based triage, staffing and QA, never with bulk closure.
- Keep customer names and SAR facts inside the work papers; examples and evals use fictional parties.

## Troubleshooting

| Problem | Likely cause | What to do |
|---|---|---|
| Case export lacks a determination date | Tool records only alert and closure | Read the case notes for the investigator's conclusion; if absent, label "Not determinable" and request the record |
| Extract totals do not tie to the core | Filters, migrations or excluded transaction codes | List the difference as a Scope gap; do not sample until resolved or disclosed |
| Case notes and timestamps disagree | Notes written after the fact | Record a source conflict; use the earlier evidenced determination for timeliness |
| Scanned SAR copies unreadable | Image-only PDFs | Try OCR; test the BSA E-Filing acknowledgment fields; mark narrative tests `[UNVERIFIED]` |
| Vendor will not provide scenario logic | Proprietary system | Test outcomes (back-test and below-the-line sample); record the limitation |
| Requester cites "the new FinCEN program rule" | April 10, 2026 proposal | State it is proposed and not in effect; route program changes to aml-compliance-program |
| Potential sanctions hit in the data | Name match in wires | Stop dispositioning that item; hand off to managing-sanctions-screening |

## Related Skills

- aml-compliance-program: hand off program and policy design: drafting or reviewing the BSA/AML program, policies and procedures, gap analysis and board approval packages; this skill covers transaction-level testing, lookbacks and SAR narratives.
- managing-sanctions-screening: hand off potential OFAC or sanctions matches for match investigation and escalation.
- reviewing-kyc-documentation: hand off customer files whose CIP, CDD or EDD documentation is stale or contradicted by the activity.
- managing-model-risk: hand off validation of a statistical or machine-learning monitoring or scoring model.
- bsa-risk-assessment: hand off when testing shows a product, channel or segment the BSA/AML risk assessment omits or under-rates.
- managing-fraud-operations-banking: hand off fraud-loss cases that need fraud investigation and recovery work.
- legal-research: hand off state rules such as NYDFS Part 504 outside a DFS-regulated test, casino rules and foreign AML law; no dedicated skill covers them.

## Reference Files

- `references/aml-reporting-rules.md`: SAR thresholds and clocks by institution type, clocks table, determination, continuing activity and no-file elections, CTR aggregation and exemptions, structuring, 314(a), confidentiality.
- `references/testing-methods-and-typologies.md`: alert and case tests, threshold and below-the-line testing, monitoring validation after April 2026, lookback scope, sampling math, independence, narratives and SAR QA, red flag typologies and severity.
- `references/output-template.md`: deliverable layout, status and partial-decline labels, test tables, windows table, findings severity, reconciliation, hand-offs and label tests.
- `references/primary-sources.md`: authorities checked with URL, method and date, corrections, disposition of the former red-flags reference, and the `[VERIFY]` list.
