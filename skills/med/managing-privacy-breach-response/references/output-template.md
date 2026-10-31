# Output Template

Produce the header and the sections below in order. Dates are ISO (YYYY-MM-DD) with the weekday and whether the date rolls (federal clocks never roll); every fact names its source. Keep PHI out of the draft: use counts, data-element names and de-identified case labels.

## Contents

1. Header
2. Section 1. Determination summary
3. Section 2. Source register and incident timeline
4. Section 3. Discovery block
5. Section 4. Threshold and exception analysis
6. Section 5. Four-factor risk assessment
7. Section 6. Affected population and thresholds
8. Section 7. Clocks table
9. Section 8. Notice content and recipients
10. Section 9. Reconciliation table
11. Section 10. Gaps and declined requests
12. Section 11. Hand-offs
13. Section 12. Open items, `[VERIFY]` list and documentation file

## Header

- Incident label, entity name and role (covered entity, business associate, Part 2 program, PHR vendor, other), today's date.
- Regimes run, each named with its citation: for example "HIPAA Breach Notification Rule, 45 C.F.R. 164.400-414"; "42 C.F.R. 2.16(b) (Part 2 records, compliance date 2026-02-16)"; "16 C.F.R. Part 318"; each state statute by section.
- Preparer note: "Draft for privacy officer and counsel review. Not legal advice; no notice has been sent."

## 1. Determination summary

| Regime | Outcome (verbatim label) | Basis in one line | Earliest open deadline | Blocking open items |
|---|---|---|---|---|
| HIPAA | Presumed breach: notification required / Not a breach: ... / Cannot determine | | | |

One row per regime and per state. Never merge rows. Put any deadline that has passed or falls within 5 days of today at the top in bold.

## 2. Source register and incident timeline

| Source | Type (log, ticket, forensic report, email, BAA, policy, interview note, address file) | Date | Status (Reviewed / Not relevant / Unreadable after attempt / Still needed) | Note |
|---|---|---|---|---|

| Date and time | Event | Who knew (role, entity) | Source and locator |
|---|---|---|---|

## 3. Discovery block

```
Incident occurred:                 <date or range>            (<source>)
First known to workforce or agent: <date> by <role>           (<source>)
Would have been known with
  reasonable diligence:            <date | not earlier>       (<basis>)
Business associate discovery:      <date | n/a>               agent? <yes | no | unclear>
Covered entity discovery used:     <date>   basis: <first knowledge | imputed BA discovery | BA notice>
Rejected candidate dates:          <investigation closed, privacy officer told, committee met>, each with the reason
```

## 4. Threshold and exception analysis

| Question | Finding | Evidence | Result |
|---|---|---|---|
| PHI / Part 2 record / PHR identifiable health information / state data element | | | |
| Use or disclosure not permitted (Privacy Rule; Part 2 if Part 2 records) | | | |
| Secured under HHS guidance (standard, key custody, device state, every copy) | | | Secured / Not secured / Not shown |
| Exception (i), (ii), (iii), each condition tested | | | Applies / Does not apply |

## 5. Four-factor risk assessment

| Factor | Facts and evidence | Points toward | Gaps |
|---|---|---|---|
| 1. Nature and extent of PHI | | | |
| 2. Unauthorized person | | | |
| 3. Actually acquired or viewed | | | |
| 4. Mitigation | | | |
| Combined conclusion | Demonstrates low probability / Does not demonstrate low probability | | |

Every row is filled before the conclusion is written. If any factor lacks evidence, say so; a missing factor cannot support low probability.

## 6. Affected population and thresholds

| Group | Count | Source | Notes (deduplicated, deceased, bad addresses) |
|---|---|---|---|
| Total unique individuals | | | |
| Residents of each state or jurisdiction (one row each) | | | |
| Unknown residence | | | |
| Part 2 patients (subset) | | | |

Threshold results: HHS (500 or more); media per state (more than 500; FTC 500 or more); each state AG threshold.

## 7. Clocks table

| # | Notice | Regime | Trigger event | Trigger date (source) | Rule | Computed deadline (with weekday) | Rolls if weekend or holiday? | Days left from today | Status |
|---|---|---|---|---|---|---|---|---|---|

One row per notice per regime per state, each with its own trigger. Paste the script inputs and outputs under the table. Mark outer limits as "outer limit; without unreasonable delay governs".

## 8. Notice content and recipients

Checklist against 164.404(c)(1)(A)-(E) and each state's elements; recipients (individuals, next of kin, HHS portal, media outlets by state, attorneys general, CDPH, consumer reporting agencies where a state requires). Drafting goes to data-breach-consumer-notice.

## 9. Reconciliation table

| # | Fact | Source A says | Source B says | Controlling source and why | Effect |
|---|---|---|---|---|---|

Typical rows: incident ticket date against the investigation memo's "discovery" date; vendor letter against the BAA; IT "encrypted" statement against the device management log; address file count against the forensic count.

## 10. Gaps and declined requests

| Gap or request | Class (unknown fact / source conflict / unverified external lookup / policy election / declined) | Effect | Who resolves | Next step |
|---|---|---|---|---|

A declined request is recorded with one of these labels, verbatim, then the reason and the honest alternative: "Declined: shifted discovery date" (a later, earlier or otherwise unsupported discovery date) or "Declined: fixed conclusion" (a result set in advance, or adverse facts left out).

## 11. Hand-offs

| To skill | Why | What is passed | What this draft did not do |
|---|---|---|---|
| data-breach-consumer-notice | Individual and substitute notice letters | Content checklist, data elements, contact plan | Did not draft letters |
| hipaa-baa | BAA notice terms to amend | BAA clause, gap found | Did not redraft the BAA |
| managing-cybersecurity-healthcare | Containment, forensics, recovery | Timeline, systems, open forensic questions | Did not direct technical response |
| managing-substance-abuse-confidentiality | Part 2 consent and redisclosure questions | Part 2 record subset | Did not decide consent questions |
| legal-research | State statutes not checked here | State list and counts | Did not confirm those states' rules |

## 12. Open items, `[VERIFY]` list and documentation file

| # | Open item | Depends on | Owner | Next action | Changes an outcome or deadline? |
|---|---|---|---|---|---|

Then each `[VERIFY]` relied on. Then the documentation file to retain for six years (164.530(j)): timeline, discovery block, threshold analysis, risk assessment, counts, clocks, copies of notices and proof of delivery, HHS submission receipt, law enforcement statements, BA correspondence.

Close with: "Draft for privacy officer and counsel review. Not legal advice; no notice has been sent."
