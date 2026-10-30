# Output Template

Produce the header and the sections below in order. Every timestamp shows date and 24-hour time and names its source and time type. Put detail in tables; keep narrative short.

## Contents

1. Header
2. Section 1. Determination summary
3. Section 2. Source register and timestamp ledger
4. Section 3. Clock block
5. Section 4. Guideline comparison
6. Section 5. Measure scorecard
7. Section 6. Reconciliation table
8. Section 7. Documentation gaps and query candidates
9. Section 8. Hand-offs
10. Section 9. Open items and `[VERIFY]` list

## Header

- Case identifier (de-identified unless the user's environment requires otherwise), arrival date and time, discharge date (or "open encounter").
- Purpose: concurrent stroke coordination, retrospective measure abstraction, quality or peer-review case review, transfer review, or record review for counsel.
- Stroke type as documented on imaging: ischemic, ICH, SAH, TIA, or not established.
- Hospital role in this case: certification level (ASR, PSC, TSC, CSC or none) and whether it is the sending or the receiving hospital.
- Frameworks applied, each with version: for example "AHA/ASA AIS guideline 2026"; "AHA/ASA spontaneous ICH guideline 2022"; "Joint Commission Specifications Manual v2026B1 (discharges 10-01-2026 to 12-31-2026)"; "AHA Target: Stroke Phase III"; "facility stroke protocol, revision date".
- Preparer note: "Draft for clinician and stroke-coordinator review."

## 1. Determination summary

| Framework | Result | Basis in one line | Blocking open items |
|---|---|---|---|
| AIS 2026 guideline comparison | Consistent / Not consistent / Not applicable / Cannot determine, per element | | |
| STK-4 (or other measure) | Numerator / Not in numerator / Excluded / Not in population / Cannot determine | | |
| Target: Stroke time goals | DTN in minutes, and which goal bands it falls within | | |

Never merge rows. "Cannot determine" names the missing fact and who can supply it.

## 2. Source register and timestamp ledger

Source register, one row per document reviewed:

| Source | Type | Date range | Status | Note |
|---|---|---|---|---|
| | EMS run sheet, code stroke form, ED triage, ED provider note, neurology or telestroke note, nursing flowsheet, MAR, imaging reports, transfer record, order set, dashboard extract | | Reviewed / Not relevant / Unreadable after attempt / Still needed | |

Timestamp ledger, one row per event, sorted by time:

| Date time | Event | Value | Source and locator | Time type (witnessed, reported, documented, administration start, order, entry) | Used for |
|---|---|---|---|---|---|

Minimum events: LKW (each documented version), symptom discovery, EMS contact, arrival (each candidate), stroke alert, physician and stroke-team arrival, glucose, imaging start and read, NIHSS (each total with its time), BP readings around IVT, consent, thrombolytic start, CTA and perfusion, transfer request and departure, receiving arrival, skin puncture, reperfusion, swallow screen, first oral intake, first antithrombotic, reversal agent start.

## 3. Clock block

Show this block every time, in this form:

```
LKW:                       <date time> (<source>)   basis: <witnessed onset | last seen normal | code stroke form | measure rule>
Rejected LKW candidates:   <time and source, with the reason each was not used>
Symptom discovery:         <date time | not applicable>
Arrival (this hospital):   <date time> (<source>)   rejected candidates: <triage, registration, alert, CT>
IVT start:                 <date time | none>   agent: <alteplase | tenecteplase>
LKW to arrival:            <minutes>       LKW to IVT start: <minutes>
Door to needle:            <minutes, from arrival>
Standard IVT window ends:  <LKW + 4.5 h>
Extended IVT clocks:       DWI-FLAIR <recognition + 4.5 h>; wake-up perfusion <midpoint of sleep + 9 h>; LKW perfusion <LKW + 4.5 h to LKW + 9 h>
EVT window:                <LKW + 6 h> / <LKW + 24 h>   puncture: <date time | none>
Post-IVT BP and neuro-check schedule: q15 min to <IVT + 2 h>; q30 min to <IVT + 8 h>; hourly to <IVT + 24 h>
Transfer:                  door-in <time>; door-out <time>; DIDO <minutes>
```

## 4. Guideline comparison

| Element | Guideline statement (source, COR, LOE) | Record shows (time, source) | Result | Note |
|---|---|---|---|---|

Label the section "Guideline comparison; not a measure result and not an order." Every result names the guideline and year. Where the facility protocol differs, add the protocol text and mark the row "policy election".

## 5. Measure scorecard

| Measure | Population test (each step with value) | Numerator test | Exclusion or reason documented | Result | Version |
|---|---|---|---|---|---|

Show STK-4 Timing I and Timing II in minutes. For STK-OP-1 report the case's minutes and stratum; no pass or fail.

## 6. Reconciliation table

| # | Fact | Source A says | Source B says | Controlling source and why | Effect on result |
|---|---|---|---|---|---|

Typical rows: code stroke form LKW against triage onset; dashboard door time against earliest arrival; order set contraindication list against AIS 2026 Table 8; FDA label window against the guideline; flowsheet NIHSS components against a later total.

## 7. Documentation gaps and query candidates

| Gap | Element affected | Gap class (unknown fact / source conflict / unverified external lookup / policy election) | Who can resolve | Compliant next step |
|---|---|---|---|---|

A query candidate is a neutral question routed under the facility's query policy, never a suggested answer and never a request to add or change an entry after the fact.

## 8. Hand-offs

| To skill | Why | What is passed | What this review did not do |
|---|---|---|---|
| interpreting-neuroradiology | ASPECTS, core volume, perfusion mismatch disputed | Imaging reports and times | Did not read images |
| managing-anticoagulation-therapy | Anticoagulant timing, reversal agent choice, restart after ICH | Agent, last dose, labs, times | Did not choose an agent or dose |
| coordinating-emergency-transfers | Transfer delay or DIDO review | Transfer timestamps | Did not judge the receiving hospital's acceptance process |
| managing-quality-reporting | Rates, submission, sampling | Case results and version | Did not compute a hospital rate |
| managing-cdi-programs | Ambiguous LKW, stroke type or NIHSS documentation | Conflicting entries | Did not draft the query text |

## 9. Open items and `[VERIFY]` list

| # | Open item | Depends on | Owner | Next action | Changes a result? |
|---|---|---|---|---|---|

Then each `[VERIFY]` statement relied on, with what would settle it.

Close with: "Draft for clinician and stroke-coordinator review. Not a final abstraction, not a peer-review determination and not a clinical order."
