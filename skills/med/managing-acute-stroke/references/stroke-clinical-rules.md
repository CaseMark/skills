# Stroke Clinical Rules (Guideline Layer)

Guideline content for comparing what happened in an encounter with what the guidelines recommend. Every value carries its source and year. Nothing here is an order for a patient; the review reports what the guideline says and what the record shows, and a clinician decides. Checked October 30, 2026; locators and the `[VERIFY]` items are in `references/primary-sources.md`.

## Contents

1. Authority map and versions
2. Clock anchors and windows (each with its own trigger)
3. IV thrombolysis: eligibility frame, agents and doses
4. Contraindications: 2026 gradient of risk, 2019 list, FDA labels
5. Blood pressure by time point
6. Endovascular thrombectomy and imaging selection
7. Systems of care and transfer
8. Early in-hospital care
9. Hemorrhagic stroke: ICH blood pressure and anticoagulant reversal

## 1. Authority map and versions

| Authority | Status on 2026-10-30 | Use it for |
|---|---|---|
| AHA/ASA 2026 Guideline for the Early Management of Patients With AIS (Prabhakaran et al., Stroke, published online Jan. 26, 2026, doi 10.1161/STR.0000000000000513) | Current. Section 1.4 states it replaces the 2018 guideline and its 2019 update | Every ischemic stroke recommendation below, cited "AIS 2026 §x, rec n (COR, LOE)" |
| AHA/ASA 2018 guideline with 2019 update (Powers et al., Stroke 2019;50:e344-e418) | Superseded for care after Jan. 26, 2026 | Only for care delivered before that date, or to explain an older order set |
| AHA/ASA 2022 Guideline for Spontaneous ICH (Greenberg et al., Stroke 2022;53:e282-e361) | No AHA/ASA replacement found `[VERIFY]` | ICH blood pressure and anticoagulant reversal |
| Neurocritical Care Society and Society of Critical Care Medicine (NCS/SCCM), Treatment of Antithrombotic-Associated Intracranial Hemorrhage in Adults: A Focused Guideline Update (Neurocrit Care, published Sept. 24, 2026, doi 10.1007/s12028-026-02601-4) | Current; non-AHA; updates the 2016 NCS/SCCM guideline on five questions | Reversal-agent choice for factor Xa inhibitors, platelet transfusion, desmopressin, small IPH; shown as its own row, never merged with AHA/ASA 2022 |
| FDA labels (TNKase, revised 2/2025; Activase) | Current labels; narrower than the guideline in places | Label-versus-guideline conflicts; never silently merged with the guideline |
| Facility stroke protocol and order sets | Policy election | Local thresholds and agent choice; a conflict with the guideline is named, not resolved |

Care date decides which guideline applies. For care before Jan. 26, 2026, compare against the 2019 update and say so; for later care, compare against AIS 2026 and list any order-set language still drawn from 2019.

## 2. Clock anchors and windows (each with its own trigger)

Anchor definitions:
- Last known well (LKW): the last time the patient was witnessed or reported to be at baseline before the current symptoms. For a witnessed onset it equals symptom onset. For a wake-up stroke it is the time the patient was last seen or reported normal before sleep (or during a documented normal awakening), never the time the symptoms were found.
- Symptom discovery (recognition): when the deficit was first noticed. It starts only the DWI-FLAIR extended-window clock.
- Arrival: earliest documented arrival at this hospital (measure definition in `references/measure-abstraction-rules.md`).
- IVT start: alteplase bolus time or tenecteplase push time.

| Element | Trigger (clock starts at) | Window or threshold | Source |
|---|---|---|---|
| Standard-window IVT (alteplase or tenecteplase) | LKW or witnessed symptom onset | Within 4.5 hours | AIS 2026 §4.6.2 rec 1 (COR 1, LOE A) |
| Extended IVT, unknown onset, MRI selection | Symptom recognition | Within 4.5 hours of recognition; MRI DWI lesion smaller than one-third of the MCA territory and no marked FLAIR signal change | AIS 2026 §4.6.3 rec 1 (2a, B-R); §3.2 rec 6 |
| Extended IVT, wake-up, perfusion selection | Midpoint of sleep (halfway between LKW and waking) | Within 9 hours of the midpoint; salvageable penumbra on automated perfusion imaging | AIS 2026 §4.6.3 rec 2(a) (2a, B-R) |
| Extended IVT, known LKW, perfusion selection | LKW | 4.5 to 9 hours; salvageable penumbra on automated perfusion imaging | AIS 2026 §4.6.3 rec 2(b) (2a, B-R) |
| IVT for LVO when EVT not possible | LKW or onset | 4.5 to 24 hours; salvageable penumbra; directed by experienced clinicians | AIS 2026 §4.6.3 rec 3 (2b, B-R) |
| Brain imaging | Hospital arrival `[VERIFY]` (the recommendation names no anchor) | As rapidly as possible, for example within 25 minutes | AIS 2026 §3.2 rec 2 (1, B-NR) |
| Pre-IVT blood pressure | Before IVT start | SBP below 185 and DBP below 110 | AIS 2026 §4.3 rec 5 (1, B-NR) |
| Post-IVT blood pressure | IVT start | Below 180/105 for at least the first 24 hours | AIS 2026 §4.3 rec 7 (1, B-R) |
| Post-IVT BP and neuro checks | IVT start | Every 15 min for 2 h, every 30 min for 6 h, hourly until 24 h | AIS 2026 Table 7 |
| Antiplatelet or anticoagulant after IVT | IVT start | Follow-up CT or MRI at 24 h before starting | AIS 2026 Table 7 |
| IV aspirin with IVT | IVT start | Not concurrently or within 90 minutes after the start | AIS 2026 §4.8 rec 17 (3: Harm, B-R) |
| Aspirin, general | Stroke onset | Within 48 hours | AIS 2026 §4.8 rec 1 (1, A) |
| DAPT, minor non-cardioembolic AIS (NIHSS 3 or less) or high-risk TIA, no IVT | Symptom onset | Start within 24 hours; 21 days, then single agent | AIS 2026 §4.8 rec 12 (1, A) |
| Anterior EVT, early window | Symptom onset (LKW) | Within 6 hours | AIS 2026 §4.7.2 recs 1, 4-7 |
| Anterior EVT, late window | Symptom onset (LKW) | 6 to 24 hours | AIS 2026 §4.7.2 recs 2-3 |
| Basilar EVT | Symptom onset (LKW) | Within 24 hours | AIS 2026 §4.7.3 rec 1 (1, A) |
| Bedside swallow screen | First oral intake of any kind, including oral medicines | Before it | AIS 2026 §5.2 rec 1 (1, C-EO) |
| ICH blood pressure lowering | ICH onset; target clock from treatment start | Start within 2 hours of onset; reach target within 1 hour | ICH 2022 §5.1 rec 2 (2a, C-LD) |
| ICH anticoagulant reversal | ICH diagnosis on imaging | As soon as possible; do not wait for coagulation results | ICH 2022 §5.2.1 rec 1 (1, C-LD) and supportive text |

## 3. IV thrombolysis: eligibility frame, agents and doses

- Decision frame (AIS 2026 §4.6.1): treat eligible adults with disabling deficits regardless of NIHSS score (rec 1, COR 1 A); do not delay for CTA or perfusion imaging inside 4.5 hours (rec 2); check glucose before IVT (rec 5). Severe hypoglycemia and hyperglycemia are typically below 50 and above 400 mg/dL; reassess deficits after correction (supportive text 5-6).
- "Disabling" follows Table 4 (PRISMS-based) for NIHSS 0-5: complete hemianopia, severe aphasia, severe extinction, or any weakness limiting sustained effort against gravity are typically disabling; isolated mild aphasia, facial droop, mild hemisensory loss usually are not. Non-disabling deficits within 4.5 hours: IVT not recommended; DAPT preferred (AHA "Top Things to Know", item 4).
- Consent: when a patient cannot consent and no representative is immediately available, proceeding is justified for an otherwise eligible adult with disabling deficits (§4.6.1 supportive text 4). The review records how consent or its waiver was documented.
- Labs: without suspected coagulopathy or recent anticoagulant or heparin use, IVT need not wait for platelet or coagulation results (§4.6.1 supportive text 10).
- Microbleeds: do not delay IVT for MRI to count microbleeds (§4.6.1 rec 11, COR 1).
- Agents (AIS 2026 §4.6.2 rec 1, COR 1 A): tenecteplase 0.25 mg/kg, maximum 25 mg, single bolus; or alteplase 0.9 mg/kg, maximum 90 mg, 10 percent as a 1-minute bolus and the rest over 60 minutes (Table 7). Tenecteplase 0.4 mg/kg is not recommended (rec 2, 3: No Benefit, A).
- Tenecteplase weight bands (Table 7 and the 2025 TNKase label): under 60 kg 15 mg; 60 to under 70 kg 17.5 mg; 70 to under 80 kg 20 mg; 80 to under 90 kg 22.5 mg; 90 kg or more 25 mg. The STEMI dose on the same label goes up to 50 mg; a stroke dose above 25 mg is a dosing error to flag, not a judgment call.
- Bridging: when a patient is eligible for both IVT and EVT, give IVT without waiting to observe a response (AIS 2026 §4.7.1 recs 1-2, COR 1 A).

## 4. Contraindications: 2026 gradient of risk, 2019 list, FDA labels

AIS 2026 replaced the 2019 checklist with Table 8, "Other Situations Wherein Thrombolysis is Deemed to Be Considered", a colour-graded risk table (§4.6.5 knowledge gaps text). The table body did not extract from the guideline PDF; the rows below come from the Guideline Central pocket edition of the 2026 guideline (its Table 6) `[VERIFY]` against the published Table 8.

| Tier | Rows read (Guideline Central pocket edition) |
|---|---|
| Absolute | Acute spinal cord injury within 3 months; intra-axial neoplasm; infective endocarditis; severe coagulopathy or thrombocytopenia (platelets under 100,000/mm3, INR over 1.7, aPTT over 40 s or PT over 15 s); aortic arch dissection; ARIA or amyloid immunotherapy; CT with extensive clear hypodensity; CT with hemorrhage; moderate to severe TBI within 14 days; intracranial or spinal surgery within 14 days |
| Relative | Pre-existing disability; DOAC exposure within 48 hours (individual decision: last dose time, renal function, severity, EVT access, reversal agents and assays; document all of it); ischemic stroke within 3 months; prior ICH; major non-CNS trauma 14 days to 3 months; major non-CNS surgery within 10 days; GI or GU bleeding within 21 days; intracranial arterial dissection; intracranial vascular malformation; STEMI within 3 months; acute pericarditis; left atrial or ventricular thrombus; systemic active malignancy; pregnancy and post-partum; dural puncture within 7 days; arterial puncture of a noncompressible vessel within 7 days; TBI or neurosurgery 14 days to 3 months |
| Low concern | Per a secondary summary only: remote GI bleeding, history of MI, possible stroke mimic, unruptured intracranial aneurysm `[VERIFY]` |

Where the older sources differ:
- The 2019 update and many order sets list prior ICH and ischemic stroke within 3 months as exclusions; the 2026 table grades both as relative. Report which list the order set used and the care date.
- The ECASS III extra exclusions for 3-4.5 hours (age over 80, NIHSS over 25, diabetes with prior stroke, any oral anticoagulant) are not part of the 2026 table `[VERIFY]` that no 2026 row restores them.
- TNKase label (revised 2/2025): start "within 3 hours after the onset of stroke symptoms"; contraindicated for AIS with active internal bleeding, intracranial or intraspinal surgery or trauma within 2 months, known bleeding diathesis, current severe uncontrolled hypertension, intracranial neoplasm, AVM or aneurysm, and active intracranial hemorrhage. History of ICH and ischemic stroke within 3 months are label contraindications for STEMI only. The label's 3-hour window and the guideline's 4.5 hours conflict; name the conflict and the facility's election.
- Activase label window and contraindication list: not read in this pass `[VERIFY]`.

## 5. Blood pressure by time point

| Time point | Threshold | Source |
|---|---|---|
| Before IVT starts | Below 185/110 | AIS 2026 §4.3 rec 5 (1, B-NR) |
| From IVT start, at least 24 h | Below 180/105; measure more often if SBP over 180 or DBP over 105 | §4.3 rec 7 (1, B-R); Table 7 |
| After IVT, intensive target | SBP below 140 not recommended | §4.3 rec 8 (3: No Benefit, B-R) |
| Before EVT without IVT | 185/110 or lower is reasonable | §4.3 rec 6 (2a, B-NR) |
| During EVT and 24 h after | 180/105 or lower is reasonable | §4.3 rec 9 (2a, B-NR) |
| After successful EVT reperfusion (mTICI 2b-3), 72 h | SBP below 140 is harmful | §4.3 rec 10 (3: Harm, A) |
| Spontaneous ICH, mild to moderate, SBP 150-220 | Target 140, keep 130-150 | ICH 2022 §5.1 rec 3 (2b, B-R) |
| Spontaneous ICH, mild to moderate | Lowering below 130 potentially harmful | ICH 2022 §5.1 rec 5 (3: Harm, B-R) |

Inequality note: rec 7 reads "below 180/105" while Table 7 reads "at or below". A reading of exactly 180 or 105 is a boundary case; show it and do not score it either way without the facility protocol.

## 6. Endovascular thrombectomy and imaging selection

AIS 2026 §4.7.2 (anterior circulation proximal LVO of the ICA or M1 unless stated):
- 0-6 h, NIHSS 6 or more, prestroke mRS 0-1, ASPECTS 3-10: recommended (1, A).
- 6-24 h, NIHSS 6 or more, mRS 0-1, ASPECTS 6 or more: recommended (1, A).
- 6-24 h, selected patients under 80, NIHSS 6 or more, mRS 0-1, ASPECTS 3-5, no significant mass effect: recommended (1, A). Large-core trials underrepresented people over 80, renal failure, refractory hypertension and short life expectancy; SELECT2 exploratory data suggest no benefit with 26 mL or more of severe hypodensity.
- 0-6 h, ASPECTS 0-2, under 80, mRS 0-1, no significant mass effect: reasonable (2a, B-R).
- 0-6 h, prestroke mRS 2: reasonable (2a, B-NR); mRS 3-4: might be reasonable (2b, B-NR).
- Dominant proximal M2, 0-6 h, mRS 0-1, NIHSS 6 or more, ASPECTS 6 or more: reasonable (2a, B-NR). Nondominant or codominant M2, distal MCA, ACA, PCA: not recommended (3: No Benefit, A).
- Basilar (§4.7.3): mRS 0-1, NIHSS 10 or more, PC-ASPECTS 6 or more, within 24 h: recommended (1, A); NIHSS 6-9: not well established (2b, B-R).
- Imaging (§3.2): CT/CTA or MRI/MRA as rapidly as possible within 24 h of LKW (rec 8); adjunctive CTP, DWI-FLAIR or DWI-PWI in the 6-24 h window can be useful if immediately available (rec 9). Late-window EVT no longer requires perfusion imaging when ASPECTS criteria are met; a note saying "no CTP, so not a candidate" is a finding to examine.
- Repeat imaging at the thrombectomy center: direct triage to the angiography suite without repeat imaging may be considered unless there is clinical change or transfer delay (§3.2, 2b).

## 7. Systems of care and transfer

- Hospitals without 24/7 thrombectomy should have transfer protocols for fast, safe transfer of patients potentially eligible for EVT (AIS 2026 §2.9 rec 2, COR 1, C-EO) and primary stroke centers should rapidly perform and read CTA or MRA (rec 3, COR 1).
- EVT-capable hospitals should track door-to-puncture, reperfusion and long-term outcomes (rec 5, COR 1).
- Prehospital destination: direct transport to the closest EVT-capable hospital may be considered where rapid interhospital transfer is not well functioning (AIS 2026 Top Things to Know, item 2).
- Door-in-door-out has no numeric guideline target in AIS 2026 `[VERIFY]`; the measure is STK-OP-1 (median minutes), described in `references/measure-abstraction-rules.md`.

## 8. Early in-hospital care

- Dysphagia: bedside swallow screen before liquid or food intake (§5.2 rec 1, COR 1, C-EO); trained professionals (rec 2, 2a). Oral medicines count as oral intake for the review.
- NIHSS: a severity scale, preferably the NIHSS, at baseline and after reperfusion therapy (§3.1 rec 1, COR 1, B-NR).
- VTE: intermittent pneumatic compression for impaired mobility (§5.4 rec 1, COR 1, B-R); prophylactic heparin reasonable (rec 2, 2a); elastic stockings harmful (rec 5).
- Glucose: treat below 60 mg/dL (§4.5 rec 1); 140-180 mg/dL reasonable for persistent hyperglycemia (rec 2, 2a); 80-130 mg/dL with IV insulin not recommended (rec 3).

## 9. Hemorrhagic stroke: ICH blood pressure and anticoagulant reversal

- Stop the anticoagulant and reverse as soon as possible after diagnosis, regardless of whether the INR is back (ICH 2022 §5.2.1 rec 1 and supportive text: time of last dose and renal function guide therapy; coagulation assays should not delay reversal).
- VKA with INR 2.0 or more: 4F-PCC in preference to FFP (rec 2, COR 1, B-R), followed by IV vitamin K (rec 3, COR 1). VKA with INR 1.3-1.9: PCC may be reasonable (rec 4, 2b). These INR thresholds apply to warfarin, not to factor Xa inhibitors.
- Factor Xa inhibitor: andexanet alfa reasonable (rec 5, 2a, B-NR); 4F-PCC or aPCC when a specific agent is unavailable (synopsis).
- NCS/SCCM focused update (Sept. 24, 2026), a separate issuer: Recommendation 1-1 suggests 4F-PCC rather than andexanet alfa for factor Xa inhibitor-associated spontaneous ICH (conditional, moderate certainty); 1-2 the same for traumatic ICH (conditional, very low certainty); 2-1 suggests against platelet transfusion for spontaneous IPH on antiplatelets without neurosurgery; 2-2 suggests transfusion for spontaneous IPH on aspirin needing neurosurgery; 4-1 makes no recommendation on treating anticoagulant effects in small IPH (generally under 5-10 mL). Report it beside the AHA/ASA 2022 row with its own name and strength. Dabigatran: idarucizumab reasonable (rec 6, 2a). Heparin: protamine (synopsis).
- Andexanet alfa (Andexxa) US status: FDA safety communication, AstraZeneca ended US sales on Dec. 22, 2025 and requested withdrawal of the BLA; FDA considers its risks to outweigh benefits. An order set or note that names andexanet as first line for US care after that date is out of date; the AHA/ASA 2022 guideline text has not been revised `[VERIFY]`, while the NCS/SCCM 2026 update already favours 4F-PCC.
- Aneurysmal SAH (nimodipine, CSTK-06) is outside this file; use the current AHA/ASA aneurysmal SAH guideline `[VERIFY]` version.
