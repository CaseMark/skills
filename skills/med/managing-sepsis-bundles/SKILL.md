---
name: managing-sepsis-bundles
language: en
description: >
  Tracks and abstracts sepsis bundle compliance for one encounter against CMS SEP-1 (Severe Sepsis
  and Septic Shock Management Bundle) and, on request, the Surviving Sepsis Campaign hour-1 bundle
  and SSC 2026 guidelines, keeping each framework separate. Builds a timestamp ledger from the
  MAR, labs, flowsheets and provider notes; computes time zero (severe sepsis presentation time
  and septic shock presentation time) instead of copying sepsis alert or triage times; scores
  initial and repeat lactate, blood cultures before antibiotics, antibiotic timing, 30 mL/kg
  crystalloid for hypotension or lactate of 4 or more, vasopressors for persistent hypotension,
  and reassessment documentation; screens SEP-1 exclusions by manual version and discharge date;
  separates SIRS-based SEP-1 criteria from Sepsis-3, SOFA and qSOFA. Use for SEP-1 abstraction,
  sepsis core measure review, sepsis bundle audit, time zero disputes, or sepsis documentation
  gaps. Drafts for clinician and quality-abstractor review; no patient orders.
tags:
  - management
  - emergency-medicine
  - compliance
metadata:
  author: casemark
  practice_areas:
    - Emergency Medicine
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---

# Managing Sepsis Bundles

Builds a sepsis bundle compliance review for one encounter: a timestamp ledger from the source record, a computed time zero, a SEP-1 element scorecard scored against the specifications manual version for the discharge date, and, only when asked, a separate comparison against Surviving Sepsis Campaign (SSC) recommendations. It also lists documentation gaps, compliant query candidates and hand-offs. Everything it produces is a draft for review by a clinician and a trained quality abstractor; it is not a final abstraction, a coding decision or a clinical order.

## Why This Skill Exists

Sepsis is common and lethal: CDC estimates about 1.7 million U.S. adults develop it each year and at least 350,000 of them die in the hospital or are discharged to hospice. CMS SEP-1 has been reported in the Hospital Inpatient Quality Reporting Program since FY 2017 and has been scored in the Hospital Value-Based Purchasing Safety domain since the FY 2026 program year, so a single abstraction error moves a public rate and payment. SEP-1 is all-or-none, and most disputed cases turn on definitions and clocks rather than care: which framework applies, when time zero is, and which timestamp counts. Three frameworks use the same words for different things. SEP-1 is a SIRS-based abstraction measure with 3-hour and 6-hour windows; the SSC Hour-1 Bundle and the SSC 2026 guidelines are clinical recommendations with their own clocks; Sepsis-3 is a SOFA-based definition with no clock at all. This skill keeps them apart.

## Where Mistakes Hide

| Input / Document | What It Is Used For | Where the Error Hides |
|---|---|---|
| The request, protocol or dashboard naming "the bundle" | Choosing the framework to score against | SSC hour-1 targets applied to SEP-1 (an antibiotic at 2 hours called a SEP-1 failure), or SEP-1's 3 hours called guideline-concordant care for septic shock |
| Sepsis alert log, triage record, navigator worksheet | Candidate times for time zero | Alert fire time, triage time, order-set time or navigator "recognition" time copied as severe sepsis presentation time instead of the time the last of the three criteria was met within 6 hours |
| Provider notes using "sepsis", "Sepsis-3", "SOFA" or "qSOFA" | Deciding whether severe sepsis or septic shock is present under SEP-1 | A SOFA score of 2 or more, qSOFA, or the word "sepsis" treated as SEP-1 severe sepsis; Sepsis-3 shock (lactate over 2 on pressors) treated as SEP-1 shock (lactate 4 or more or persistent hypotension); SOFA and SOFA-2 not distinguished |
| Lab reports for initial and repeat lactate | Initial lactate, repeat-lactate trigger, septic shock trigger | Order or result time used where collection time governs; repeat clock run from the initial lactate instead of presentation time; a lactate of exactly 2.0 treated as over 2 |
| Crystalloid orders, weights and the MAR | 30 mL/kg element | Actual weight used where a provider documented obesity and directed ideal weight, or the reverse; the 10 percent allowance applied to the volume infused; 30 mL/kg demanded for a lactate of 2 to 3.9 without hypotension; non-crystalloid volume counted |
| Vital sign flowsheet after fluids | Persistent hypotension and the vasopressor element | One low reading in the hour after the infusion treated as persistent hypotension; readings outside that hour counted |
| Reassessment notes and attestations | Repeat volume status and tissue perfusion assessment | A templated note signed before crystalloid completion, outside 6 hours of septic shock presentation, or by a role the manual does not accept |
| Medication administration record and order log | Antibiotic and blood culture elements | Order or verification time used for administration; cultures drawn after the first antibiotic dose; a dose more than 24 hours before presentation not tested against the exclusion |
| Transfer records, code-status orders, coding abstract | Population and exclusions | A DNR read as comfort measures only; a transfer from a clinic read as an acute transfer; a stale checklist excluding COVID-19 cases for a 2026 discharge; the wrong manual version for the discharge date |

## Ground Rules

1. **Draft only.** Every output is a draft for a clinician and a quality abstractor. Never state that a case is final, submitted or validated, and never phrase guideline content as an order for this patient (no doses, rates or agents directed at the patient).
2. **Source-review gate.** Do not call any timestamp, note or result missing until every supplied document has been opened and searched, including scanned and oddly named files. Classify each unresolved gap as an unknown fact, a source conflict, an unverified external lookup (for example a manual rule not confirmed in the current version) or a policy election (for example the facility's sepsis protocol choice).
3. **Hierarchy of authority.** For abstraction rules: the CMS manual version for the discharge date (measure information form, algorithm, data dictionary), then CMS Q&A, then facility policy; SSC guidelines never decide a SEP-1 question. For facts: source entries (MAR administration times, specimen collection times, flowsheet vitals, provider notes) govern over dashboards, alert logs, navigator worksheets and abstraction tools. Name every conflict in the reconciliation table; never resolve one silently.
4. **Citation discipline.** Every timestamp, value and quoted note carries a source locator (document, date and time, author role) or `[UNVERIFIED]`. Every rule carries its framework and version or `[VERIFY]`.
5. **Name the framework on every conclusion.** Write "SEP-1 v5.18a: met", "SSC Hour-1 Bundle: not begun within the hour" or "Sepsis-3 criteria documented". Never merge frameworks into one pass or fail.
6. **Lock the version.** Select the SEP-1 manual by discharge date and state it in the header. Manual versions change yearly; v5.18a covers 2026 discharges and a v5.19 is reported for 2027 `[VERIFY]`.
7. **Compute time zero; never copy it.** Show the three criteria, their times, the 6-hour span check and any provider documentation in the fixed block from `references/output-template.md`, and list each rejected candidate time with the reason.
8. **Use the right clock and the right timestamp.** Initial lactate, cultures, antibiotics and repeat lactate run from severe sepsis presentation; crystalloid, vasopressor and reassessment run from septic shock presentation. Use collection and administration times, not order times, unless the data dictionary says otherwise.
9. **No documentation fixes.** Never suggest adding, backdating or editing an entry to change a result. A late entry follows facility policy and is labeled as such; an unclear note becomes a query candidate routed to `managing-cdi-programs`, written without a leading answer.
10. **Outcome vocabulary.** A case is Pass, Fail, Excluded, Not in population, or Cannot determine. An element is Met, Not met, Not required or Cannot determine. "Cannot determine" always names the missing fact and who can supply it.

## Checkpoint A: Pre-Draft Intake (Mandatory)

Collect before Step 1:

1. Purpose: concurrent tracking on an open encounter, retrospective SEP-1 abstraction, quality-improvement case review, or record review for counsel.
2. Arrival, admission and discharge dates (discharge date selects the manual version).
3. Age at admission and admission source, including any transfer from another hospital or its ED.
4. Which frameworks the user wants scored. Default: SEP-1 only; add the SSC overlay only when asked.
5. The record set: ED and inpatient provider notes, triage and nursing flowsheets with vitals, MAR, order log, lab reports with collection and result times, weights and heights, code-status and comfort-care orders, transfer records, the sepsis alert log, and the final ICD-10-CM codes for a retrospective review.
6. Facility sepsis policy and any EHR sepsis screening definition, if the question concerns internal tracking.

Defaults when an input is missing:

- Admission source missing: treat transfer status as an unknown fact and keep the case provisional; never assume "no transfer".
- Open encounter with no discharge date: run concurrent tracking under the version for the current year, labeled provisional.
- Frameworks not stated: score SEP-1 only and offer the SSC overlay.
- Weight missing: list the element as Cannot determine; never estimate a weight.

Hard stops (do not score SEP-1 pass or fail):

- No discharge date or no way to identify the manual version, for a retrospective abstraction.
- Patient under 18 for SEP-1: say the case is outside SEP-1 and route pediatric sepsis questions to `managing-pediatric-emergencies`.
- A request to write orders, doses or treatment for a current patient: decline that part and offer the guideline comparison instead.
- A request to create, backdate or alter documentation so the case passes.
- No timestamped source for the events at issue (only a narrative summary): produce the ledger of what is missing and stop before scoring.

## Step 1: Frame the Question and the Frameworks

Read `references/clinical-criteria-and-ssc.md`, Section 1, before writing anything. Restate the question in one line and name each framework that will be scored and its version. If the user says "the bundle" or "hour-1" while asking about SEP-1 performance, name the mismatch in the first line of the output and score each framework separately.

## Step 2: Build the Source Register and Timestamp Ledger

Open every supplied document and complete the source register in `references/output-template.md`, Section 2. Then build the ledger: every vital sign set, lactate, culture, antibiotic, fluid, vasopressor, provider note on infection or sepsis, code-status order and transfer event, each with its value, time, time type and source. Where two sources give different times for one event, record both and add a reconciliation row.

## Step 3: Screen the Population and Exclusions

Read `references/sep1-abstraction-rules.md`, Sections 1 and 2. Confirm the version, age, qualifying code (retrospective review) and each exclusion in the version's data dictionary. A DNR or DNI order is not comfort measures only. Check any checklist the user supplies against the version: a 2024 or 2025 checklist can carry exclusions the 2026 manual dropped.

## Step 4: Compute Severe Sepsis Presentation Time

Read `references/sep1-abstraction-rules.md`, Section 3. Find documentation of infection, each SIRS criterion and each organ dysfunction criterion with times, using SEP-1 thresholds, not SOFA or qSOFA. Confirm all three fall within 6 hours. Compare with the time of any physician, APN or PA documentation of severe sepsis or septic shock and take the earlier. Write the fixed time-zero block and list each rejected candidate (alert fire, triage, order set, navigator) with why it does not control. If two readings of the record give different times, show both and the elements whose result changes.

## Step 5: Determine Septic Shock

Read `references/sep1-abstraction-rules.md`, Sections 4 and 7. Test the initial lactate (4 or more), persistent hypotension in the hour after the target crystalloid volume, and provider documentation of septic shock. Record septic shock presentation time and the 3-hour and 6-hour windows it opens. Do not import the Sepsis-3 shock definition.

## Step 6: Score Each Element

Read `references/sep1-abstraction-rules.md`, Sections 5 to 8. Fill the element scorecard in `references/output-template.md`, Section 5. For the crystalloid row, show the weight used and why (actual, or ideal with documented obesity), the target, the ordered and infused volumes, and any documented reason for a lower volume. For the vasopressor row, show the readings in the hour after infusion. For the reassessment row, show the note time against crystalloid completion. Then set the case result.

## Step 7: Add the Clinical Guideline Overlay (Only When Asked)

Read `references/clinical-criteria-and-ssc.md`, Sections 5 and 6. Compare the ledger with the Hour-1 Bundle (time zero at triage or earliest annotation) or with SSC 2026 statements, citing each statement's strength. Present it in its own section, labeled as not a SEP-1 result and not an order. Antibiotic choice and duration go to `conducting-antimicrobial-stewardship`.

## Step 8: Reconcile, List Gaps and Hand Off

Complete the reconciliation table, the gaps and query candidates, the hand-offs, and the open items with every `[VERIFY]` relied on (`references/output-template.md`, Sections 7 to 10). Check each rule you relied on against `references/primary-sources.md`; carry its `[VERIFY]` flag into the output if it has one.

## Checkpoint B: Post-Draft Alignment

1. Does the output answer the question asked, for the framework asked, with each framework scored on its own row?
2. Is the version named and correct for the discharge date?
3. Is time zero computed from criteria, with rejected candidates listed, and does every element use the correct clock?
4. Does every result that depends on a `[VERIFY]` rule say so, and would the result flip if the rule reads differently?
5. Is anything phrased as an order or as advice to change documentation? Remove it.
6. Are open items owned, with a next action?

## Quality Audit

1. The header names each framework and the SEP-1 manual version by discharge date.
2. The source register covers every supplied document with a status; nothing is called missing without a search.
3. Every ledger entry has a value, a time, a time type and a source locator.
4. The time-zero block is complete, the 6-hour span is checked, and rejected candidates are listed with reasons.
5. SEP-1 severe sepsis and shock rest on SEP-1 thresholds, not SOFA, qSOFA, the word "sepsis" or the Sepsis-3 shock definition.
6. Initial lactate, cultures, antibiotic and repeat lactate run from severe sepsis presentation; crystalloid, vasopressor and reassessment run from septic shock presentation.
7. Administration and collection times are used, and every order-time substitution is flagged.
8. The crystalloid row shows weight basis, target, ordered and infused volume, and any documented lower-volume reason.
9. Persistent hypotension rests on readings in the hour after the target volume, not on a single reading.
10. Every exclusion applied is tested against the version in force, and DNR is not equated with comfort measures only.
11. SSC content appears only in the overlay, cites strength and year, and contains no patient-directed orders.
12. Every conflict is in the reconciliation table; every gap is classified; no step suggests altering documentation.
13. Every `[VERIFY]` relied on appears in the open-items list with what would settle it.

## Guidelines

- A sepsis alert is a screen. Its fire time starts nothing in SEP-1 and does not establish Sepsis-3 onset.
- SEP-1 antibiotic timing is 3 hours from severe sepsis presentation. SSC 2026 recommends antimicrobials ideally within 1 hour for possible, probable or definite septic shock and suggests up to 3 hours after rapid assessment for possible sepsis without shock. Report both when asked; do not substitute one for the other.
- The 30 mL/kg element is triggered by initial hypotension or an initial lactate of 4 or more, not by any lactate over 2.
- A provider's documented reason for a smaller volume (heart failure, kidney failure) matters to both the clinical record and the measure; check the version's criteria rather than assuming either way.
- Lactate rises for reasons other than hypoperfusion (epinephrine, beta-agonists, liver failure, seizure). The measure still counts the value; clinical interpretation belongs in the overlay.
- Concurrent tracking on an open encounter is provisional: windows still open are "Not yet due", never "Not met".
- Keep protected health information to what the review needs; de-identify case identifiers in shared drafts.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Two plausible time-zero values | Infection documentation is ambiguous or a provider note predates the clinical criteria | Show both computations, the elements whose result changes, and route the note to a CDI query candidate |
| A scanned or image-only flowsheet or MAR | Text search missed it | Open it, attempt OCR, and if still unreadable list it as unreadable with the dependent elements set to Cannot determine |
| Lab report shows only result time | Collection time not exported | Request the collection time; meanwhile mark dependent elements Cannot determine, not Met |
| Dashboard or navigator worksheet disagrees with the chart | Tool logic uses alert or order times | The chart entry controls; add a reconciliation row naming the tool's rule |
| Weight missing or conflicting | Stated, estimated and measured weights differ | List each weight with source and time; apply the version's weight rule; flag if the result changes |
| User supplies an older abstraction checklist | Version drift | Score against the version for the discharge date and list each checklist rule that differs |
| Notes say "septic shock" but no qualifying lactate or readings | Provider documentation route | Test the documentation route in the version, then apply its clocks; flag `[VERIFY]` if the route's wording is unconfirmed |

## Related Skills

- conducting-antimicrobial-stewardship: antibiotic choice, spectrum, de-escalation and duration.
- managing-cdi-programs: compliant queries when sepsis, severe sepsis or septic shock documentation is ambiguous or conflicting.
- managing-clinical-documentation-improvement: program-level documentation metrics behind recurring sepsis gaps.
- abstracting-clinical-documentation: codeable diagnoses and specificity for the sepsis codes that place a case in the population.
- managing-quality-reporting: hospital rates, submission and data validation beyond a single case.
- tracking-clinical-deterioration: early warning scores and escalation that feed sepsis screening.
- managing-pediatric-emergencies: patients under 18, who fall outside SEP-1.
- conducting-mortality-reviews: case review of a sepsis death beyond bundle compliance.
- medical-record-chronology: a litigation chronology when counsel needs the full timeline rather than a measure result.

## Reference Files

- `references/sep1-abstraction-rules.md`: SEP-1 version lock, population, exclusions, time zero, septic shock, element windows, fluid and reassessment rules, timestamp conventions.
- `references/clinical-criteria-and-ssc.md`: framework comparison, Sepsis-3, SOFA and SOFA-2, screening tools, SSC Hour-1 Bundle, SSC 2026 statements.
- `references/output-template.md`: deliverable sections, timestamp ledger, time-zero block, element scorecard, reconciliation table, hand-off table.
- `references/primary-sources.md`: each authority checked with date and what it supports, and the `[VERIFY]` list.
