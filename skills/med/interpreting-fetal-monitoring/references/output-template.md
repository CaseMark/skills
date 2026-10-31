# Output Template

Produce the header and sections in order. Every tracing feature carries a strip locator: date, clock time range, archive page or panel, and monitoring mode. Keep narrative short; put detail in tables.

## Contents

1. Header
2. Section 1. Summary by segment
3. Section 2. Source register, monitoring modes and clock offset
4. Section 3. Clinical timeline
5. Section 4. Segment interpretation worksheet
6. Section 5. Deceleration and contraction log
7. Section 6. Charted interpretation against the tracing (retrospective)
8. Section 7. Responses on the timeline (retrospective)
9. Section 8. Reconciliation table
10. Section 9. Gaps and hand-offs
11. Section 10. Open items and `[VERIFY]` list

## Header

- Case identifier (de-identified unless the user's environment requires otherwise), date or dates of care, gestational age on each date with its dating source.
- Purpose: concurrent documentation support, quality or peer review, or medical-legal record review.
- Nomenclature: "NICHD 2008 definitions and three-tier categories". Guidance in force on the date of care: for example "ACOG CPG No. 10 (Oct. 2025)" or "ACOG PB 106 (2009) and PB 116 (2010)"; facility policies and their versions.
- Outcome status for retrospective work: "Outcome-blind pass completed before outcome data were opened: yes or no".
- Preparer note: "Draft for clinician review."

## 1. Summary by segment

| Segment (clock time) | Mode | Category | Category II features (higher-risk; protective) | Key basis | Open items |
|---|---|---|---|---|---|
| | External or FSE; toco or IUPC | Category I / Category II / Category III / Not categorized (reason) | | | |

Never give one category for the whole labor.

## 2. Source register, monitoring modes and clock offset

| Source | Type | Clock range | Paper speed and vertical scale (paper) or export settings (digital) | Status |
|---|---|---|---|---|
| | EFM archive export, paper strip, flowsheet, MAR, provider note, annotation log | | | Reviewed / Unreadable after attempt / Still needed |

Clock offset statement: "EFM clock runs <n> minutes <ahead or behind> the EHR, anchored on <event> at <times>", or "No anchor event found; times not aligned".

## 3. Clinical timeline

| Clock time | Event | Value or detail | Source and locator | Entry time if different |
|---|---|---|---|---|

Include stage of labor, exams, membrane status, mode changes, medications with rates, maternal pulse, BP, temperature and SpO2, position changes, notifications, decision and delivery.

## 4. Segment interpretation worksheet

One block per segment:

```
Segment:              <start>-<end>   mode: <external | FSE>, <toco | IUPC>
Signal check:         maternal pulse <value at time> vs recorded rate <value>; MHR indicators: <none | list>
Uterine activity:     blocks <a>, <b>, <c> per 10 min; 30-min average <x.x>; tachysystole <yes | no>, <with | without> FHR decelerations
Baseline:             <n> bpm from <minutes> of identifiable baseline in <window>; or indeterminate
Variability:          amplitude <low>-<high> bpm -> <absent | minimal | moderate | marked>
Accelerations:        GA <weeks+days> -> threshold <15x15 | 10x10>; <list with peak and duration>
Decelerations:        see log; recurrence <k> of <n> contractions in <20-min window> = <percent>
Sinusoidal:           <absent | present from to>
Category:             <label>; basis: <criteria>
CPG 10 Box 3:         higher-risk <list | none>; protective <list | none>
```

## 5. Deceleration and contraction log

| # | Contraction onset, peak, end | Decel onset | Nadir time and rate | Return | Onset to nadir (s) | Nadir minus peak (s) | Depth (bpm) | Duration | Type |
|---|---|---|---|---|---|---|---|---|---|

Type is early, late, variable, prolonged, or unclassified (with reason).

## 6. Charted interpretation against the tracing (retrospective)

| Charted time and author role | Charted wording (quoted) | Tracing for the same window | Agreement or mismatch | Policy in force |
|---|---|---|---|---|

## 7. Responses on the timeline (retrospective)

| Finding and time | First charted recognition | Notification | Action and time | Tracing after action | Guidance in force on that date |
|---|---|---|---|---|---|

Each interval runs from its own event. Describe; do not grade compliance with the standard of care.

## 8. Reconciliation table

| # | Fact | Source A says | Source B says | Controlling source and why | Effect on interpretation |
|---|---|---|---|---|---|

Typical rows: charted category against tracing; EFM clock against EHR clock; nurse's "accelerations" against maternal pulse; outcome-blind reading against post-outcome reading; NICHD 2008 against CPG 10 wording.

## 9. Gaps and hand-offs

| Gap | Affects | Gap class (unknown fact / source conflict / unverified external lookup / policy election) | Who can resolve | Next step |
|---|---|---|---|---|

| To skill | Why | What is passed | What this draft did not do |
|---|---|---|---|
| medical-record-chronology | Full litigation chronology | Timeline and segment summary | No Bates-level chronology |
| managing-newborn-assessments | Neonatal condition at birth | Delivery time, final segment | No neonatal assessment or cord gas opinion |
| managing-patient-safety-events | Event reporting and root cause | Reconciliation and response tables | No causal analysis |

## 10. Open items and `[VERIFY]` list

| # | Open item | Depends on | Owner | Next action | Could change a category? |
|---|---|---|---|---|---|

Close with: "Draft for clinician review. Not a clinical order, not a standard-of-care opinion and not a causation opinion."
