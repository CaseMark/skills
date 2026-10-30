# Output Template

Produce the header and the sections below in order. Put detail in tables. Every value carries its date, time and source. Every dose figure in this output is labeled "protocol-expected, for comparison" or "as ordered"; none is written as an instruction to give a dose.

## Contents

1. Header
2. Section 1. Disposition summary
3. Section 2. Source register
4. Section 3. Regimen and version match
5. Section 4. Dosing variables
6. Section 5. Dose comparison table
7. Section 6. Cumulative-dose ledger
8. Section 7. Cycle, interval and clearance-to-treat
9. Section 8. Route and handling safety
10. Section 9. Verification and documentation record
11. Section 10. Reconciliation table
12. Section 11. Hand-offs
13. Section 12. Open items and `[VERIFY]` list

## Header

- Patient identifier (de-identified unless the environment requires otherwise), diagnosis as written in the order, regimen name, order set name, version and effective date, cycle and day as ordered, planned administration date.
- Review type: prospective order verification, pre-administration check, or retrospective protocol-adherence review.
- Standards applied, each with edition: for example "ASCO-ONS Antineoplastic Therapy Administration Safety Standards (2024)"; "ISMP Targeted Medication Safety Best Practices for Hospitals 2026-2027"; "USP <800>"; the product labels read; the institution order set.
- Preparer line: "Draft for pharmacist, oncology nurse and prescriber review. Not an order."

## 1. Disposition summary

| Item | Result | Basis in one line | Blocking open items |
|---|---|---|---|
| Overall order | No discrepancies found / Clarification required before preparation / Critical: escalate now / Cannot complete verification | | |
| Each agent | Consistent / Discrepancy / Not applicable / Cannot verify | | |

For a retrospective review use: Adherent / Deviation with documented rationale / Deviation without documented rationale / Cannot determine. Use these labels exactly.

Declined parts of the request (include only when a part was declined):

| Request | Label | What was provided instead | Routed to |
|---|---|---|---|
| | Declined: dose selection - routed to prescriber / Declined: attestation - record reflects only checks performed / Declined: record alteration | | |

Use the three labels exactly. A declined part never stops the rest of the review. "Cannot verify" and "Cannot determine" always name the missing fact and who can supply it. "No discrepancies found" never means released; release is the pharmacist's act.

## 2. Source register

| Source | Type | Date | Status | Note |
|---|---|---|---|---|
| | Order, order set, published regimen, trial protocol, flowsheet, lab report, outside records, MAR, pharmacy log, specialty pharmacy record | | Reviewed / Not relevant / Unreadable after attempt / Still needed | |

## 3. Regimen and version match

| Element | Order says | Order set (version) says | Published regimen or protocol says | Match? | Note |
|---|---|---|---|---|---|

Rows: drugs, dose per unit, route, rate, days, cycle length, number of cycles, premedication and supportive care, hold parameters. Name any exception order and whether 3.4.1 authorization and 3.4.2 rationale are documented.

## 4. Dosing variables

```
Height:            <cm> measured <date> by <role>; second verifier <role | none>
Weight:            <kg> measured <date> by <role>; type <actual | ideal | adjusted>; prior weight <kg, date>; change <percent>
BSA:               formula <name>; unrounded <value>; rounded <value>; cap applied <none | value, documented reason | none documented>
Serum creatinine:  <mg/dL> collected <date time>; assay <IDMS | unknown>
GFR for Calvert:   method <CG | measured | other>; value <mL/min>; cap per order set <125 | none stated>; value used <mL/min>
Other variables:   <bilirubin, AST/ALT, ANC, platelets with collection times>
```

## 5. Dose comparison table

| Agent | Protocol dose (unit) | Variable used | Protocol-expected dose, for comparison | Dose as ordered | Difference (mg, percent) | Order set tolerance | Result |
|---|---|---|---|---|---|---|---|

## 6. Cumulative-dose ledger

| Agent | Date range | Facility or source | Dose per unit and cycles | Cumulative (mg/m² or units) | Source locator |
|---|---|---|---|---|---|

Close with the total after this dose, the label statement for that agent with label date, LVEF or other monitoring result with date, and whether the record documents a prescriber decision at this total.

## 7. Cycle, interval and clearance-to-treat

| Check | Trigger date | Computed value | Order says | Parameter from order set | Result |
|---|---|---|---|---|---|

Rows: actual Day 1 of the current cycle; day of cycle on the planned date; next Day 1 due; minimum interval; each hold parameter with lab collection time.

## 8. Route and handling safety

| Check | Finding | Source | Result |
|---|---|---|---|

Rows as applicable: vinca alkaloid container and label; intrathecal separation, labeling and delivery; oral prescription in the EHR order with quantity, refills and schedule; hazardous-drug label; CSTD use for administration of NIOSH Table 1 antineoplastics.

## 9. Verification and documentation record

| Verification | Required elements present? | Signers and roles | Independent? | Time | Result |
|---|---|---|---|---|---|

Result labels, used exactly: Documented / Not documented / Independence not shown / Not yet due. "Not documented" covers a check that is absent, lacks a required element, or lacks a signer of the required role or number; "Not yet due" covers a check whose trigger (for example the patient's presence for the fourth verification) has not occurred. Rows: two-person height and weight check (new plan), first, second, third and fourth verification, allergy confirmation, consent. This table reports what the record shows. It is never completed or signed on anyone's behalf.

## 10. Reconciliation table

| # | Fact | Source A says | Source B says | Controlling source and why | Effect on result |
|---|---|---|---|---|---|

Typical rows: order weight against flowsheet weight; tracker total against outside records; treatment calendar against MAR dates; lab eGFR against the order set's GFR method; order set version against the published regimen.

## 11. Hand-offs

| To skill | Why | What is passed | What this review did not do |
|---|---|---|---|
| managing-chemotherapy-toxicity | Toxicity grading and the modification decision | Labs, prior-cycle toxicity notes | Did not grade toxicity or choose a dose level |
| interpreting-echocardiograms | LVEF result behind a cumulative-dose decision | Study dates and reports | Did not interpret the study |
| managing-patient-safety-events | A wrong-route, wrong-dose or wrong-day event or near miss | The facts and timeline | Did not file the report |

## 12. Open items and `[VERIFY]` list

| # | Open item | Gap class (unknown fact / source conflict / unverified external lookup / policy election) | Owner | Next action | Changes the disposition? |
|---|---|---|---|---|---|

Then each `[VERIFY]` statement relied on, with what would settle it.

Close with: "Draft for pharmacist, oncology nurse and prescriber review. Not an order and not a release for preparation or administration."
