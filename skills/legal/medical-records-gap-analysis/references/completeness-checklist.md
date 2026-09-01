# Records Completeness Audit Checklist

Use this item-level checklist for production integrity, Categories B through E, and representation signals. Apply only the sections within the user's requested scope, but note when an omitted check limits a requested conclusion.

## Contents

1. [Production integrity](#production-integrity)
2. [Source universe and review status](#source-universe-and-review-status)
3. [Implied providers and record sets](#implied-providers-and-record-sets)
4. [Representation timeline](#representation-timeline)
5. [Pre-incident baseline](#pre-incident-baseline)
6. [Cross-references and partial productions](#cross-references-and-partial-productions)
7. [Complaint and diagnosis evolution](#complaint-and-diagnosis-evolution)
8. [Expected records by custodian](#expected-records-by-custodian)

## Production integrity

- [ ] Patient identity is consistent on sampled pages from every Bates prefix; mismatches are production errors, not facts to analyze.
- [ ] Requested date range is compared with received date range for each provider when the request, subpoena, or authorization is available.
- [ ] Bates numbering is checked for discontinuities within each prefix.
- [ ] Page count is compared with any cover letter, index, or custodian certification.
- [ ] Exact duplicates are distinguished from amended notes, corrected reports, and addenda.
- [ ] Records-custodian certification or affidavit is inventoried when expected; legal sufficiency is left to counsel.

## Source universe and review status

- [ ] Every accessible matter object is represented in the Source Accounting Index, including objects excluded from substantive review.
- [ ] Each object has an apparent source, file type, page or Bates coverage, date coverage where available, readability status, and review status.
- [ ] Original source productions are distinguished from billing, claims, insurance, agency, lien, authorization, and other nonclinical sources.
- [ ] Demand packages, chronologies, prior reports, exhibit sets, and other derivative compilations are identified and used only as leads or cross-checks when underlying sources are available.
- [ ] Search results are used for navigation, not as evidence that every source was reviewed.
- [ ] Every readable in-scope source production has been reviewed.
- [ ] Exact duplicates are established by reliable byte-, page-, or content-level comparison before repeat review is omitted.
- [ ] Overlapping but independently produced records retain separate provenance and do not create duplicate encounters.
- [ ] Unreadable, OCR-limited, processing, password-protected, missing, or otherwise inaccessible sources are listed with the reason and required next step.
- [ ] Potentially privileged or unrelated objects are inventoried at a safe metadata level and not opened without authorization.
- [ ] Attorney-directed work product is distinguished from non-privileged derivative or agent-generated analysis; neither is treated as source evidence.
- [ ] The selected audit-status label matches the source coverage: Matter-Wide Audit, Matter-Wide Audit With Identified Review Limitations, or User-Scoped Audit.

## Implied providers and record sets

For every signal, record the source date and citation, implied custodian or specialty, expected date range and record type, and whether the Provider Index resolves it.

- [ ] Referral orders and consult requests.
- [ ] Imaging and diagnostic orders; distinguish order, report, and image files.
- [ ] PT, OT, chiropractic, behavioral-health, and other therapy referrals.
- [ ] Prescriptions; distinguish the prescribing note from pharmacy fill history.
- [ ] Emergency, urgent-care, hospital, and outside visits mentioned retrospectively.
- [ ] Prior treatment listed in intake, new-patient, or history forms.
- [ ] Providers implied by claim lines, EOBs, bills, or lien materials.
- [ ] EMS or other transport suggested by arrival mode or trauma documentation.
- [ ] Reference or send-out laboratory work.
- [ ] IMEs, defense examinations, or record reviews mentioned in correspondence or notes.
- [ ] Prior claims, workers-compensation, or disability records referenced in the production.
- [ ] Attorney-referral, lien, or letter-of-protection references in the produced record, without assuming that related privileged communications are discoverable.

Do not name a provider the source does not identify. If only a specialty or facility type is known, list that unresolved custodian type.

## Representation timeline

Each source-supported item becomes a dated datapoint. Report temporal relationships only; do not imply that representation caused care, referral, or a later complaint.

- [ ] Letters of representation already present in the authorized production.
- [ ] Attorney lien notices and letters of protection.
- [ ] Chart notations that the patient consulted, hired, or was referred by an attorney.
- [ ] Intake forms naming an attorney or law firm as the referral source.
- [ ] Billing entries addressed to or guaranteed by a law firm.
- [ ] User-provided `representation_date`, labeled as uncited unless corroborated.

Do not recommend production of attorney-client communications or work product. Flag privilege, discoverability, and authorization questions for counsel.

## Pre-incident baseline

Evaluate each claimed body system separately:

- [ ] Any pre-incident records are present within the selected lookback window.
- [ ] A primary-care provider is identified and corresponding records are present.
- [ ] Prior injuries, accidents, claims, or treatment to the same body system are mentioned and the referenced records are present.
- [ ] Medications active at the incident date are identified and relevant prescriber records are present.
- [ ] Baseline function, work status, or activity level is documented.

If no baseline records are present, state the absence. Do not infer a clean baseline from silence.

## Cross-references and partial productions

### Cross-references

- [ ] Every billed date of service has a corresponding clinical note, and vice versa, subject to known global or bundled billing arrangements.
- [ ] Codes are normalized before comparing billed procedures or diagnoses with documentation.
- [ ] Written prescriptions are compared with produced pharmacy fill history.
- [ ] Imaging orders are compared separately with reports and image files.
- [ ] Potential duplicate charges are identified without concluding that they are erroneous.
- [ ] Clinical-only and billing-only date ranges are listed for each provider.

### Common partial-production patterns

- [ ] Hospital radiology reports and image files.
- [ ] Nursing flowsheets and medication administration records.
- [ ] Operating-room, anesthesia, catheterization-lab, and procedure records.
- [ ] Outside or send-out laboratory results.
- [ ] EMS run sheets.
- [ ] Therapy daily notes when only evaluations or summaries were produced.
- [ ] Post-operative follow-up beyond a single note when the record indicates more care was planned.
- [ ] Itemized billing when only account summaries or balances were produced.

## Complaint and diagnosis evolution

Establish the early baseline from the disclosed `complaint_baseline_hours` window. If that window is adjusted because records are sparse or the context requires it, record the selected window and reason.

- [ ] First-care modality, date, and time are captured at the precision supported by the source.
- [ ] Early complaints and body parts are listed with citations.
- [ ] Initial mechanism descriptions are preserved as documented.
- [ ] Explicit denials are quoted or accurately paraphrased with citations.
- [ ] Objective findings and studies are separated from reported symptoms.
- [ ] Complaints or diagnoses first documented after a NOTE or SIGNIFICANT gap are identified.
- [ ] Complaints or diagnoses first documented after a representation datapoint are identified without a causal inference.
- [ ] Later complaints that conflict with an explicit early denial include citations to both records.
- [ ] Newly documented complaints, new diagnoses, and changed mechanism descriptions are distinguished.
- [ ] Missing records, provider documentation differences, and condition-specific onset patterns are considered before recommending follow-up.

For every finding, state the elapsed time and intervening gap or representation datapoint. Report the record sequence; do not assess credibility, fabrication, causation, or medical significance.

## Expected records by custodian

Use this inventory as a reasonableness check, not proof that a record exists. Facility practices and the requested scope vary.

| Custodian | Commonly separate record sets |
|-----------|-------------------------------|
| Hospital | Admission and discharge records, H&P, orders, progress notes, nursing documentation, MAR, radiology, laboratory, procedure and anesthesia records, ED record, itemized billing |
| Emergency or urgent care | Triage, clinician note, orders, results, discharge instructions, billing |
| PCP or specialist | Office notes, orders, referrals, correspondence, problem and medication lists, billing |
| PT, OT, chiropractic, or other therapy | Evaluation, daily notes, progress summaries, discharge, attendance, billing |
| Imaging center | Order, report, image files, billing |
| Pharmacy | Fill history identifying medication, fill date, quantity, and prescriber where available |
| IME or record reviewer | Report, materials-reviewed list, correspondence where discoverable |
