# Output Template

Produce the header and the sections below in order. Use only the sections the scope needs (an encounter review skips Section 6 unless asked; a program review skips Sections 3 and 5), and say which were skipped. Every time shows date and 24-hour clock and names its source.

## Contents

1. Header
2. Section 1. Determination summary
3. Section 2. Source register
4. Section 3. Encounter timeline
5. Section 4. Trigger, location and party analysis
6. Section 5. Encounter element scorecard
7. Section 6. Program and administrative checklist
8. Section 7. Reconciliation table
9. Section 8. Gaps, corrective actions and declined requests
10. Section 9. Exposure context
11. Section 10. Hand-offs
12. Section 11. Open items and `[VERIFY]` list

## Header

- Hospital name and type (hospital, CAH, REH), the role it played (sending, receiving, both), and the department where the individual presented.
- Encounter identifier (de-identified unless the user's environment requires otherwise), encounter date, and today's date.
- Purpose: complaint response, internal audit, recipient-report decision, survey readiness, or plan-of-correction support.
- Authorities applied, each dated: "42 U.S.C. 1395dd; 42 C.F.R. 489.24 and 489.20(l), (m), (q), (r); SOM Appendix V Rev. 191 (07-19-19); SOM Chapter 5 Rev. 243 (06-12-26); 45 C.F.R. 102.3 (2025 amounts, no 2026 adjustment), checked <date>."
- Preparer note: "Draft for compliance officer and counsel review. Not a survey determination or legal opinion."

## 1. Determination summary

| Requirement | Result | Basis in one line | Tag | Blocking open items |
|---|---|---|---|---|
| MSE by a designated QMP without delay | Potential deficiency / No deficiency identified / Documentation gap / Cannot determine | | A-2406 | |

Program rows use Meets / Partially meets / Does not meet / Cannot determine. "Cannot determine" names the missing fact and who can supply it.

## 2. Source register

| Source | Type | Date range | Status | Note |
|---|---|---|---|---|
| | Central log, triage note, MSE note, registration audit trail, on-call list, call log, transfer form, acceptance log, transport record, admission order, bylaws or rules (approval date), policy, signage photo, campus map | | Reviewed / Not relevant / Unreadable after attempt / Still needed | |

## 3. Encounter timeline

One row per event, sorted by time. Each timed element keeps its own trigger.

| Date time | Event | Actor (name, credential, QMP designation source) | Source and locator | Time type (arrival, entry, signed, ordered, departed, received) | Used for |
|---|---|---|---|---|---|

Required events where they exist: arrival and request; registration and any payment or insurance contact; triage; MSE start and finish; EMC determination; on-call request and arrival; admission decision and signed order; certification or written request; acceptance (name, title, time); records sent; departure; arrival at recipient; recipient's reason-to-believe time; report sent.

## 4. Trigger, location and party analysis

```
Hospital and role:                <name>; sending | receiving | both
Department of presentation:       <name>; DED test met: licensed | held out | one-third | none | not established
On hospital property?             <yes | no | not established> (campus map, 250-yard rule, excluded structures)
"Comes to the ED" route:          DED request | elsewhere on property | hospital-owned ambulance | non-hospital ambulance on property
Status on arrival:                not a patient | scheduled outpatient | inpatient
Duty ended by:                    no EMC | stabilized | good-faith inpatient admission (order time) | appropriate transfer | LWBS or AMA of own free will | still open
Obligated parties:                hospital; screening QMP; on-call physician; transferring physician; recipient hospital
```

## 5. Encounter element scorecard

| Element | Rule | Evidence and time | Source | Result | Note |
|---|---|---|---|---|---|

Rows: trigger; QMP designation of the screener; MSE content against presentation (not triage alone); delay or discouragement for payment or insurance; EMC determination; labor and false-labor certification (if pregnant with contractions); stabilizing treatment within capability; on-call response; admission (good faith, order time); transfer basis (request or certification with risk-benefit summary, timed at transfer); treatment before transfer; receiving acceptance (name, title, time); records sent; transport; refusal documentation; recipient report (if receiving). Use Not applicable with a reason where an element does not arise.

## 6. Program and administrative checklist

| Item | Regulation and tag | Evidence | Result | Corrective action |
|---|---|---|---|---|
| Signage (rights, labor, Medicaid; languages of population served; every DED entrance and waiting area) | 489.20(q), A-2402 | | | |
| Central log (all DEDs linked; dispositions; LWBS entries) | 489.20(r)(3), A-2405 | | | |
| On-call list (individual names, current privileges, backup, response minutes) | 489.20(r)(2), 489.24(j), A-2404 | | | |
| Transfer records kept 5 years from transfer | 489.20(r)(1), A-2403 | | | |
| Recipient reporting procedure | 489.20(m), A-2401 | | | |
| QMP designation approved by governing body | 489.24(a)(1)(i), A-2406 | | | |
| Off-campus DED inventory | 413.65(g)(1); 489.24(b) | | | |

## 7. Reconciliation table

| # | Fact | Source A says | Source B says | Controlling source and why | Effect on result |
|---|---|---|---|---|---|

Typical rows: "stable for transfer" note against an unresolved EMC; triage time against MSE time; log disposition against the chart; acceptance per transfer center against the receiving physician's note; bylaws QMP list against a department memo.

## 8. Gaps, corrective actions and declined requests

| Gap | Element | Gap class (unknown fact / source conflict / unverified external lookup / policy election) | Owner | Corrective action (prospective only) |
|---|---|---|---|---|

Corrective actions change policies, forms, training, staffing, logs going forward and audits; they never change a past entry. A late entry is made only under facility policy, bears its actual date and time, and is labeled as late.

If any request was declined, add:

```
Declined: <the requested alteration, backdating, recharacterization, deletion, or non-reporting>
Reason: Ground Rule 8 or 9; App. V A-2409 ("Certifications may not be backdated") where it applies
Compliant path: <dated late entry under policy | report now | counsel review>
```

## 9. Exposure context

Label as context, not a determination: Appendix V tags implicated; CMP tier by bed count with the dated figure; whether the facts suggest immediate jeopardy (a CMS judgment); mitigating and aggravating factors under 42 C.F.R. 1003.520; termination track if cited.

## 10. Hand-offs

| To skill | Why | What is passed | What this review did not do |
|---|---|---|---|
| coordinating-emergency-transfers | Fix the transfer process and form | Element results for the transfer | Did not redesign the form |
| managing-medical-records-compliance | Late-entry or amendment handling | The gap and the policy question | Did not draft any entry |
| legal-research | Circuit or State law questions | The question and facts | Did not resolve preemption or private-action law |

## 11. Open items and `[VERIFY]` list

| # | Open item | Depends on | Owner | Next action | Changes a result? |
|---|---|---|---|---|---|

Then each `[VERIFY]` statement relied on, with what would settle it.

Close with: "Draft for compliance officer and counsel review. Not a survey determination, legal opinion or clinical order."
