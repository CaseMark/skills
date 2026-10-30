# Output Template

Produce the header and the sections below in order. Every timestamp shows date and 24-hour time and names its source. Put detail in tables; keep the narrative short.

## Contents

1. Header
2. Section 1. Determination summary
3. Section 2. Source register and timestamp ledger
4. Section 3. Population and exclusion screen
5. Section 4. Time zero computation
6. Section 5. Element scorecard
7. Section 6. Clinical guideline overlay (only when asked)
8. Section 7. Reconciliation table
9. Section 8. Documentation gaps and query candidates
10. Section 9. Hand-offs
11. Section 10. Open items and `[VERIFY]` list

## Header

- Case identifier (de-identified unless the user's environment requires otherwise), arrival date and time, admission date, discharge date.
- Purpose: concurrent tracking, retrospective SEP-1 abstraction, quality-improvement case review, or record review for counsel.
- Frameworks applied, each named with version: for example "CMS SEP-1, Specifications Manual v5.18a (discharges 01/01/2026-12/31/2026)"; "SSC Hour-1 Bundle (2018)"; "SSC adult guidelines 2026"; "Sepsis-3 (2016)".
- Preparer note: "Draft for clinician and quality-abstractor review."

## 1. Determination summary

| Framework | Result | Basis in one line | Blocking open items |
|---|---|---|---|
| SEP-1 | Pass / Fail / Excluded / Not in population / Cannot determine | the failed element or the exclusion | |
| SSC Hour-1 Bundle | Elements begun within the hour: n of 5 | | |

Never merge the rows. "Cannot determine" names the missing fact.

## 2. Source register and timestamp ledger

Source register, one row per document reviewed:

| Source | Type | Date range | Status | Note |
|---|---|---|---|---|
| | ED provider note, nursing flowsheet, MAR, lab report, order log, sepsis alert log, navigator worksheet, transfer record, other | | Reviewed / Not relevant / Unreadable after attempt / Still needed | |

Timestamp ledger, one row per event, sorted by time:

| Date time | Event | Value | Source and locator | Time type (collection, result, administration start, order, entry) | Used for |
|---|---|---|---|---|---|

## 3. Population and exclusion screen

| Test | Finding | Source | Result |
|---|---|---|---|
| Age 18 or older | | | |
| Qualifying ICD-10-CM code | | | |
| Each exclusion in the version's data dictionary | | | Applies / Does not apply / Cannot determine |

## 4. Time zero computation

Show this block every time, in this form:

```
Infection documented:            <date time> (<source>)
SIRS criterion A:                <value> at <date time> (<source>)
SIRS criterion B:                <value> at <date time> (<source>)
Organ dysfunction:               <value> at <date time> (<source>)
Span of the three criteria:      <hh:mm>   within 6 hours? <yes | no>
Provider documentation of severe sepsis or septic shock: <date time | none>
Severe sepsis presentation time: <date time>   basis: <last criterion | provider documentation | ED or floor arrival rule>
Rejected candidates:             <alert fire, triage, order set, navigator time>, each with the reason
Initial hypotension:             <time of qualifying readings | none>  (crystalloid trigger)
Initial lactate 4 or more:       <result time | none>                  (crystalloid trigger)
Crystalloid clock starts:        <earlier trigger | not required>
Septic shock presentation time:  <date time | not present>   basis: <lactate 4 or more | persistent hypotension | provider documentation>
3-hour window ends:              <date time>     6-hour window ends: <date time>
```

## 5. Element scorecard

| Element | Required? (why) | Window (opens, closes) | Qualifying event and time | Source | Result | Note |
|---|---|---|---|---|---|---|
| Initial lactate | | | | | Met / Not met / Not required / Cannot determine | |

Rows: initial lactate, blood cultures before antibiotics, antibiotic (route, earliest start time in the window, and any antibiotic table the version applies, `[VERIFY]` for v5.18a), repeat lactate, crystalloid (with its trigger, the weight used and its source, the target, ordered and infused volumes), vasopressor, reassessment. Vasopressor and reassessment are Not required when septic shock is not present.

## 6. Clinical guideline overlay (only when asked)

A separate table against the SSC Hour-1 Bundle or SSC 2026 statements, each row citing the statement and its strength. Label it "Clinical guideline comparison; not a SEP-1 result and not an order."

## 7. Reconciliation table

| # | Fact | Source A says | Source B says | Controlling source and why | Effect on result |
|---|---|---|---|---|---|

Typical rows: dashboard time zero against computed time zero; order time against MAR administration time; navigator worksheet against the flowsheet; weight in the order against the weight in triage.

## 8. Documentation gaps and query candidates

| Gap | Element affected | Gap class (unknown fact / source conflict / unverified external lookup / policy election) | Who can resolve | Compliant next step |
|---|---|---|---|---|

A query candidate is a question to route under the facility's query policy, never a suggested answer and never a request to add a time after the fact.

## 9. Hand-offs

| To skill | Why | What is passed | What this review did not do |
|---|---|---|---|
| conducting-antimicrobial-stewardship | Antibiotic choice, spectrum, de-escalation | Agents, times, cultures, source | Did not judge appropriateness beyond the manual's antibiotic element |
| managing-cdi-programs | Ambiguous sepsis documentation | The conflicting notes and timestamps | Did not draft the query |
| managing-quality-reporting | Aggregate rates, submission, validation | Case result and version | Did not compute a hospital rate |

## 10. Open items and `[VERIFY]` list

| # | Open item | Depends on | Owner | Next action | Changes the SEP-1 result? |
|---|---|---|---|---|---|

Then each `[VERIFY]` statement relied on, with the manual section or guideline text that would settle it.

Close with: "Draft for clinician and quality-abstractor review. Not a final abstraction and not a clinical order."
