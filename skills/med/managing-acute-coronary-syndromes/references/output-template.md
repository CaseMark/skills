# Output Template

Produce the header and the sections below in order. Every timestamp shows date and 24-hour time, its facility, and its source document. Put detail in tables; keep narrative short. Sections that do not apply say "Not applicable" with the reason.

## Contents

1. Header
2. Section 1. Summary of findings by framework
3. Section 2. Source register and timestamp ledger
4. Section 3. Clock table
5. Section 4. Measure scorecard
6. Section 5. Diagnostic documentation review (ECG, troponin, MI classification)
7. Section 6. Reperfusion choice and fibrinolysis contraindication review
8. Section 7. Discharge and transition-of-care checklist
9. Section 8. Reconciliation table
10. Section 9. Documentation gaps and query candidates
11. Section 10. Hand-offs
12. Section 11. Open items and `[VERIFY]` list

## Header

- Case identifier (de-identified unless the user's environment requires otherwise), age band, sex as documented, facilities involved (referral and receiving), arrival and discharge dates.
- Purpose: concurrent coordination review, retrospective quality review, registry abstraction support, peer-review packet, or record review for counsel.
- Frameworks applied, each named with version, for example: "2025 ACC/AHA/ACEP/NAEMSP/SCAI ACS guideline (corrected Nov. 10, 2025)"; "CMS996v6 STEMI eCQM, CY 2026 reporting period"; "2017 AHA/ACC STEMI/NSTEMI performance measures PM-10, PM-11, PM-12"; "Fourth UDMI (2018)" and/or "Fifth UDMI (2026)"; "ICD-10-CM FY 2027 guidelines".
- Preparer note: "Draft for clinician and quality review. Not a diagnosis, not a code assignment and not an order."

## 1. Summary of findings by framework

| Framework | Item | Result | Basis in one line | Blocking open items |
|---|---|---|---|---|
| 2025 guideline | Transfer FMC-to-device goal 120 min | Met / Not met / Cannot determine | | |
| CMS996v6 | ED encounter at Hospital A | In numerator / Not in numerator / Excluded / Exception documented / Not in population / Cannot determine | | |
| 2017 PM-12 | CR referral before discharge | Met / Not met / Exception documented / Cannot determine | | |

Never merge rows across frameworks. "Cannot determine" names the missing fact and who can supply it.

## 2. Source register and timestamp ledger

| Source | Facility | Type | Date range | Status | Note |
|---|---|---|---|---|---|
| | | EMS run sheet, ED record, ECG tracing or report, lab report, cath report, MAR, transfer record, discharge summary, dashboard, registry abstract, other | | Reviewed / Not relevant / Unreadable after attempt / Still needed | |

| Date time | Facility | Event | Value | Source and locator | Time type (arrival, registration, triage, acquisition, interpretation, collection, result, administration, departure, procedure start, device) | Used for |
|---|---|---|---|---|---|---|

## 3. Clock table

One row per element. Each row has its own start event; never copy one anchor across rows.

| Element | Framework | Start event and time | Stop event and time | Interval (min) | Target | Result | Alternative anchor and its result |
|---|---|---|---|---|---|---|---|

Under "Alternative anchor", show every other plausible start time (for example arrival, triage or first ECG for a walk-in FMC) and whether the result changes. Open windows on a live encounter are "Not yet due", never "Not met".

## 4. Measure scorecard

| Measure and version | Population test | Exclusions checked (each, with finding) | Exceptions checked | Numerator test | Result |
|---|---|---|---|---|---|

State the facility the measure is attributed to. A transfer case usually generates separate rows for the referral and receiving hospitals.

## 5. Diagnostic documentation review

ECG block:

```
ECG <n>: acquired <time>, interpreted <time> by <role>; findings as documented: <text>
STEMI criteria (2025 Table 3): <met | not met | cannot determine>
Equivalent patterns screened: posterior <leads V7-V9 obtained? yes/no>, LBBB or paced <Sgarbossa documented? yes/no>, de Winter, hyperacute T, aVR, right-sided leads
Clinician conclusion in the record: <quote and locator>
Review note: <consistent | possible missed pattern for physician review>
```

Troponin block, one row per value:

| Collected | Resulted | Assay and generation | Unit | Value | Lab 99th percentile URL (sex-specific if reported) | Pathway and threshold used | Hours from symptom onset | Above URL? |
|---|---|---|---|---|---|---|---|---|

Then: absolute and relative delta with the pathway's own delta threshold, and "acute pattern / chronic pattern / cannot determine".

Classification block:

| Statement in record | Locator | Definition it uses (Fourth UDMI type, Fifth UDMI class, none) | Criteria documented | Code on abstract | Conflict? |
|---|---|---|---|---|---|

## 6. Reperfusion choice and fibrinolysis contraindication review

| Fact | Source | Facility checklist label | 2025 Table 14 category | CMS996v6 exclusion? |
|---|---|---|---|---|

Close with the decision documented by the clinician and its stated reason. Label any concordance question "for physician peer review".

## 7. Discharge and transition-of-care checklist

| Item | Documented status (done, declined, contraindicated with reason, deferred with owner, absent) | Source | Guideline or measure basis | Gap? |
|---|---|---|---|---|

Rows: antiplatelet regimen and planned duration, bleeding-reduction plan if any, PPI where indicated, high-intensity statin and lipid follow-up, beta-blocker, ACEi or ARB where indicated, LVEF, sublingual nitroglycerin, CR referral placed (program named), follow-up appointments, education. The column records documentation only; it never proposes an agent or dose.

## 8. Reconciliation table

| # | Fact | Source A says | Source B says | Controlling source and why | Effect on result |
|---|---|---|---|---|---|

Typical rows: dashboard door-to-balloon against the ledger; registration time against arrival time; procedure start against device time; discharge summary diagnosis against progress notes; facility checklist against Table 14.

## 9. Documentation gaps and query candidates

| Gap | Item affected | Gap class (unknown fact / source conflict / unverified external lookup / policy election) | Who can resolve | Compliant next step |
|---|---|---|---|---|

A query candidate is a question routed under the facility's query policy, never a suggested answer, and never a request to add or move a time.

## 10. Hand-offs

| To skill | Why | What is passed | What this review did not do |
|---|---|---|---|
| interpreting-emergency-ecgs | Possible STEMI-equivalent pattern | Tracings, times, documented reads | Did not issue a final ECG interpretation |
| managing-cdi-programs | Conflicting MI documentation | Conflicting statements with locators | Did not draft the query answer or assign a code |
| coordinating-emergency-transfers | Transfer delay or EMTALA documentation | Transfer timeline | Did not assess EMTALA compliance |
| managing-cardiac-rehabilitation | CR referral and program enrollment | Diagnosis, procedure, referral status | Did not write an exercise prescription |
| managing-quality-reporting | Aggregate rates and submission | Case-level results and versions | Did not compute a hospital rate |

## 11. Open items and `[VERIFY]` list

| # | Open item | Depends on | Owner | Next action | Changes a result? |
|---|---|---|---|---|---|

Then each `[VERIFY]` statement relied on, with the document that would settle it.

Close with: "Draft for clinician and quality review. Not a diagnosis, not a code assignment and not an order."
