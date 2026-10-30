# Stroke Measure Abstraction Rules (Measure Layer)

Performance-measure rules for one encounter. These are abstraction rules, not clinical recommendations: a case can meet a guideline and fail a measure, or the reverse. Report each on its own row. Checked October 30, 2026 against the Specifications Manual for Joint Commission National Quality Measures; locators are in `references/primary-sources.md`.

## Contents

1. Version lock and program scope
2. Populations and who counts the case
3. Timestamp data elements (LKW, arrival, thrombolytic)
4. STK measures
5. CSTK, STK-OP and ASR measures used most in stroke reviews
6. Target: Stroke and Get With The Guidelines time goals
7. What is not a Joint Commission STK measure

## 1. Version lock and program scope

| Manual version | Discharges covered |
|---|---|
| v2026A (and addendum A1) | 01-01-2026 through 06-30-2026 |
| v2026B | 07-01-2026 through 12-31-2026 |
| v2026B1 (posted 9/14/2026) | 10-01-2026 through 12-31-2026 (4Q26) |

Select the version by discharge date and name it in the header. For a 4Q26 discharge use v2026B1; for 3Q26 use v2026B `[VERIFY]` whether B1 changes any element you rely on for 3Q26.

Program scope (Joint Commission stroke measures page, read 2026-10-30):
- Chart-abstracted STK, CSTK, STK-OP, ASR-IP, ASR-OP and STK-VOL measures are used for stroke certification (Acute Stroke Ready, Primary, Thrombectomy-Capable, Comprehensive), each program using its own subset.
- eSTK-2, eSTK-3, eSTK-5 and eSTK-6 are eCQMs used for accreditation. CMS reporting of the stroke eCQMs in 2026 `[VERIFY]` (the Joint Commission 2026 eCQM webinar cites CMS national averages for STK-2, STK-3 and STK-5).
- Ask which certification level the hospital holds before applying a CSTK measure; CSTK measures apply to comprehensive stroke centers.

## 2. Populations and who counts the case

- STK Initial Patient Population: age 18 or older, length of stay 120 days or less, ICD-10-CM principal diagnosis on Table 8.1 (ischemic) or Table 8.2 (hemorrhagic); the two subpopulations are sampled separately.
- STK-OP: ED encounters with an E/M code on Table 1.0, an ischemic or hemorrhagic principal diagnosis and age 18 or older; the patient is transferred to another hospital.
- Thrombolytic counted "at this hospital" only. IV Alteplase Initiation is "No" if the drug was given at another hospital before transfer or the patient arrived with the infusion running.
- Transfers within one system with one medical record use the first facility's arrival, except for CSTK, STK, STK-OP and ASR measures, which use arrival at the stroke center (Arrival Time element).
- Common exclusions: comfort measures only (timing varies by measure), clinical trial, elective carotid intervention. Check each in the measure's own form.

## 3. Timestamp data elements (LKW, arrival, thrombolytic)

Time Last Known Well (v2026B1, collected for STK-4, ASR-IP-1, ASR-OP-1):
- Definition: the time before hospital arrival at which the patient was last known to be without signs and symptoms of the current stroke or at baseline. It must precede Arrival Time.
- A specific time entered as LKW on a Code Stroke form or stroke template is used over other times, unless any physician, APN or PA documents that LKW or onset is unknown.
- If both LKW and symptom onset are documented, use LKW. Example in the manual: normal at 22:00, awoke at 02:00 with headache and returned to sleep, normal at 07:00, symptoms at 08:00: LKW is 07:00.
- If only a symptom onset time is documented, use it as LKW.
- "N hours ago": subtract from ED arrival; a range: use the maximum; "less than N hours": use N.
- Multiple LKW times without a Code Stroke form: physician documentation first; among physicians, the earliest.
- Resolved prior episodes: use the most recent episode before arrival.
- "Symptoms started just prior to ED arrival" with no other time: use Arrival Time.

Last Known Well (Y/N): "No" if any physician, APN or PA documents LKW unknown (with listed exceptions); "No" for "patient OK last night" with no time when LKW is clearly over 2 hours before arrival; "No" for an in-house stroke. Do not infer "unknown" from the words "wake-up".

Arrival Time (v2026B): the earliest documented time the patient arrived, from the measure's Only Acceptable Sources (ED face sheet, registration, triage, ED ECG, ED labs, ED imaging and other ED record entries). EMS records are disregarded. An earlier time in an acceptable source is used unless it is an obvious error.

IV Alteplase Initiation (v2026B1): "Yes" when a hang or infusion time is documented at this hospital. The inclusion list names tenecteplase (TNK, TNKase) as well as alteplase; intra-arterial t-PA and other thrombolytics are excluded.

## 4. STK measures

Only the STK-4 measure information form was read in full. The other rows come from the v2026B1 set listing, its data-element list and the GWTG-Stroke measure summaries: `[VERIFY]` each against its own measure information form before scoring it.

| Measure | Rule that decides most disputes | Clock (trigger to event) |
|---|---|---|
| STK-1 VTE prophylaxis | Prophylaxis the day of or day after hospital admission, or a documented reason for none | Admission date to prophylaxis date |
| STK-2 Discharged on antithrombotic | Ischemic stroke; prescribed at discharge or documented reason | Discharge |
| STK-3 Anticoagulation for AF/flutter | Ischemic stroke with AF/flutter; prescribed at discharge or reason | Discharge |
| STK-4 Thrombolytic therapy | Denominator: ED patients (ED Patient = Y) with ischemic stroke whose arrival is within 120 minutes of LKW, less cases with a documented Reason for Not Initiating IV thrombolytic; numerator: thrombolytic initiated at this hospital within 180 minutes of LKW | LKW to arrival (Timing I); LKW to initiation (Timing II) |
| STK-5 Antithrombotic by end of hospital day 2 | Day of arrival is day 1; thrombolytic given changes the logic (element "IV OR IA Alteplase Administered at This Hospital or Within 24 Hours Prior to Arrival") | Arrival date to end of day 2 |
| STK-6 Discharged on statin | Ischemic stroke; prescribed at discharge or reason | Discharge |
| STK-8 Stroke education | Listed in the v2026B1 set table | Discharge |
| STK-10 Assessed for rehabilitation | Ischemic or hemorrhagic stroke | During stay |

STK-4 detail (v2026B1 algorithm):
- Step 3: ED Patient = N: not in the measure population (category B); missing: rejected. Clinical Trial = Y and Elective Carotid Intervention = Y also leave the population (steps 4-5).
- Timing I = arrival minus LKW. Over 120 minutes: not in the measure population (category B). Below 0: rejected.
- Steps 13-14: IV thrombolytic not initiated: a documented Reason for Not Initiating = Y takes the case out of the population (category B); = N keeps it in the population and out of the numerator (category D). A no-thrombolytic case is never a failure until this element is checked.
- Timing II = initiation minus LKW. 180 minutes or less: numerator. Over 180 and up to 270 minutes: excluded only with a documented Reason for Extending the Initiation (for example treatment to lower BP before IVT, a recanted refusal, arrest or intubation in the ED, or another reason documented by a physician, APN, PA or pharmacist on the day of or after arrival; system reasons such as CT or pharmacy delays do not count). Over 270 minutes: in the population, not in the numerator.
- STK-4 is anchored on LKW, not on the door. A door-to-needle figure never decides STK-4.
- The STK-4 form still names alteplase and cites the 2019 guideline; its 180-minute numerator is narrower than the 2026 guideline's 4.5-hour window. Report both; do not call care that met the guideline a measure pass, or the reverse.

## 5. CSTK, STK-OP and ASR measures used most in stroke reviews

- CSTK-01 NIHSS score performed: ischemic stroke patients with an initial NIHSS score performed before any acute recanalization therapy (IV or IA thrombolytic or mechanical thrombectomy), or within 12 hours of arrival for patients without recanalization therapy. Data element Initial NIHSS Score Performed: a documented total is required; component scores without a total are "No"; do not infer a total from components; modified or estimated NIHSS and other scales are excluded. RN, physician, APN, PA and teleneurology totals count.
- CSTK-03 severity measurement for SAH and ICH: initial Hunt and Hess or ICH score with date and time `[VERIFY]` timing rule.
- CSTK-04 procoagulant reversal for ICH: denominator is ICH patients (Table 8.2b principal diagnosis and Table 8.2c admitting diagnosis) with INR 1.4 or more closest to arrival; numerator is a reversal agent from the inclusion list initiated at this hospital. Included agents: PCC (Kcentra), aPCC, FFP, recombinant factor VIIa, idarucizumab, protamine, andexanet alfa. Vitamin K alone is "No". Algorithm order (v2026B1): principal diagnosis on Table 8.2b; Comfort Measures Only = 1 leaves the population; Clinical Trial = Y leaves it; INR 1.4 or more; admitting diagnosis on Table 8.2c; then agent initiated = numerator, and if no agent, a documented Reason for Not Administering a Procoagulant Reversal Agent = Y also places the case in the numerator (step 8), while N leaves it in the population and out of the numerator. The CSTK-04 INR cut-off (1.4) is a measure rule, not the ICH 2022 clinical threshold (INR 2.0 for 4F-PCC in VKA patients).
- CSTK-09 arrival time to skin puncture and CSTK-11/12 rapid effective reperfusion: hospital arrival or skin puncture to TICI 2b-3; data elements include Mode of Arrival and Initial NIHSS Less Than 6 `[VERIFY]` thresholds before scoring.
- STK-OP-1 door to transfer: median minutes from ED arrival to transfer, reported in strata (1b hemorrhagic; 1d-1i ischemic by thrombolytic before transfer, LVO and MER eligibility; 1c retired 7/1/2021). One case contributes minutes to a median; it does not pass or fail. The measure form cites a 2013 Brain Attack Coalition recommendation that transfers occur within 2 hours of arrival.
- ASR-OP-1 thrombolytic therapy: drip and ship, for acute stroke ready hospitals `[VERIFY]` timing rule before scoring.

## 6. Target: Stroke and Get With The Guidelines time goals

AHA Target: Stroke Phase III national goals (brochure; GWTG recognition page read 2026-10-30):
- Primary: door-to-needle within 60 minutes in 85 percent or more of AIS patients treated with IV thrombolytics; door-to-device within 90 minutes (direct arrival) or 60 minutes (transfer) in 50 percent or more of EVT patients.
- Secondary: door-to-needle within 45 minutes in 75 percent or more; within 30 minutes in 50 percent or more.
- Honor Roll levels: 75 percent within 60 (Honor Roll); 85 percent within 60 (Elite); 75 percent within 45 and 50 percent within 30 (Elite Plus); door-to-device goal (Advanced Therapy); minimum 6 patients.
- Suggested intervals for a 60-minute DTN: door to physician 10, stroke team 15, CT start 25, CT read 45 minutes; for 45: 5, 10, 20, 35; for 30: 2.5, 5, 15, 25.
- The goals are hospital percentages. One case is "DTN 50 minutes: within 60, not within 45 or 30", never "Target: Stroke met".
- "Door" is hospital arrival. The GWTG-Stroke coding instructions for the door-to-needle measure (AHASTR13) define Arrival Date/Time as "the earliest documented month, day, year and time the patient arrived at the hospital", the same core rule as the Joint Commission element. Use the earliest documented arrival, not triage, registration, stroke-alert, CT or neurologist-arrival time, and state the source used. Whether GWTG also disregards EMS records, as the Joint Commission Only Acceptable Sources list does, `[VERIFY]`.
- GWTG collects "Eligibility or Medical Reasons IV Thrombolytic was Initiated Greater than 60, 45, or 30 Minutes After Arrival"; record any such documented reason next to the DTN figure without changing the minutes.
- GWTG-Stroke achievement measure: IV thrombolysis "arrive by 3.5 hours, treat by 4.5 hours" from LKW. This is a registry measure, not STK-4; do not mix the two.

## 7. What is not a Joint Commission STK measure

- Dysphagia screening is not in the v2026B1 STK set (STK-1, 2, 3, 4, 5, 6, 8, 10). Treat it as a guideline element (AIS 2026 §5.2) and a facility or registry metric; do not cite "STK-4" or any STK number for it. STK-4 is thrombolytic therapy.
- NIHSS documentation is a measure only through CSTK-01 (comprehensive stroke centers) and through registry fields.
- Door-to-needle time is a Target: Stroke and registry metric, not a Joint Commission STK measure.
