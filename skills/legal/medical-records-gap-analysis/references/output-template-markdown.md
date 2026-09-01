# Output Template: Medical Records Gap Analysis

Adapt this structure to the user's requested scope. Omit irrelevant sections and disclose unperformed categories. Every confirmed finding must have a verified source citation; unverified possibilities belong in a separate possible-findings subsection.

## Contents

1. [Records Reviewed](#records-reviewed)
2. [Completeness Scorecard](#completeness-scorecard)
3. [Treatment History Gaps](#a-treatment-history-gaps)
4. [Missing Providers and Record Sets](#b-missing-providers-and-record-sets)
5. [Missing Pre-Incident Baseline](#c-missing-pre-incident-baseline)
6. [Billing, Clinical, and Production Mismatches](#d-billing-clinical-and-production-mismatches)
7. [Complaint and Diagnosis Evolution](#e-complaint-and-diagnosis-evolution)
8. [Possible Findings](#possible-findings--unverified)
9. [Proposed Retrieval Plan](#f-proposed-retrieval-plan)
10. [Methodology and Verification Log](#methodology-and-verification-log)
11. [Limitations](#limitations)

---

# Medical Records Gap Analysis: [Matter Name]

**Prepared:** [date]

**Incident:** [date; time and source citation when reliably available / unavailable]

**Initial care:** [modality; elapsed hours or days at supported precision; citation]

**Perspective:** [neutral / plaintiff / defense]

**Citation scheme:** [Bates / file and page]

## Records Reviewed

| Producing party or custodian | Source range | Pages | Dates covered | Status |
|------------------------------|--------------|-------|---------------|--------|
| [custodian] | [PREFIX00001-PREFIX00450] | [450] | [dates] | [complete / partial / unclear] |

**Parameters:** initial gap [14 days]; interval NOTE [30 days]; interval SIGNIFICANT [60 days]; baseline lookback [5 years]; complaint baseline [96 hours]; injury context [value]; representation date [none / user-provided / source-cited]. These are configurable review heuristics, not legal or clinical standards.

**Scope:** [categories performed, categories omitted, and reason]

## Completeness Scorecard

| Category | Confirmed findings | Possible or unverified | Highest priority |
|----------|--------------------|------------------------|------------------|
| A. Treatment history | [n] | [n] | [summary] |
| B. Missing providers or record sets | [n] | [n] | [summary] |
| C. Pre-incident baseline | [n] | [n] | [summary] |
| D. Billing, clinical, or production mismatches | [n] | [n] | [summary] |
| E. Complaint or diagnosis evolution | [n] | [n] | [summary] |

[Brief overall assessment and the most consequential source-supported findings.]

## A. Treatment History Gaps

### Treatment course

[Short, source-cited sequence of care modalities, escalation or de-escalation, material gaps, and the position of representation datapoints. This is not a full chronology.]

### Representation timeline

| Date | Datapoint | Source | Position in treatment course |
|------|-----------|--------|------------------------------|
| [date] | [letter / lien / LOP / chart notation / user-provided date] | [citation / user-provided, uncited] | [temporal relationship only] |

Do not infer that representation caused treatment, referral, or a later complaint.

### A-0. Initial care interval

- **Incident:** [date/time and supporting source]
- **First documented care:** [provider, modality, date/time, citation]
- **Elapsed time:** [hours or days at supported precision]
- **Flagged:** [yes, exceeds threshold / no, reported as a datapoint]
- **Source-stated context:** [explanation and citation / none located / not applicable]
- **Retrieval action:** [F-n / none]

### A-1. [SIGNIFICANT / NOTE / FUNCTIONAL]: [description]

- **Interval:** [n days; start date to end date]
- **Bracketing encounters:** [provider/date/citation before]; [provider/date/citation after]
- **Source-stated explanation:** [explanation and citation / no explanation located]
- **Related production gap:** [B-n / none identified]
- **Context:** [neutral, source-grounded explanation appropriate to perspective]
- **Representation datapoint:** [date and citation / none]
- **Retrieval action:** [F-n]

## B. Missing Providers and Record Sets

### B-1. [Provider, specialty, or unresolved custodian type]

- **Implying source:** [referral, order, history, bill, or other signal; date; citation]
- **Expected records:** [document type and supportable date range]
- **Retrieval action:** [F-n]

## C. Missing Pre-Incident Baseline

### C-1. [Body system]

- **Finding:** [records present / no records located within selected window]
- **Why records may exist:** [claimed injury, named PCP, prior care, medication, or other source-supported basis with citation]
- **Retrieval action:** [F-n / none]

## D. Billing, Clinical, and Production Mismatches

### D-1. [Mismatch type]

- **Finding:** [both sides of comparison with citations]
- **Interpretation limit:** [what cannot be concluded from the mismatch]
- **Retrieval action:** [F-n / specialist review]

## E. Complaint and Diagnosis Evolution

### Early complaint baseline

- **Window used:** [first 96 hours / adjusted window and reason]
- **First encounter:** [provider, modality, date/time, citation]
- **Complaints and body parts:** [source-cited list]
- **Mechanism:** [as first documented, citation]
- **Explicit denials:** [quoted or accurately paraphrased, citation]
- **Objective findings:** [source-cited list]

### E-1. [Newly documented complaint / new diagnosis / conflict with early denial]

- **Baseline:** [early record or denial, citation]
- **Later record:** [complaint or diagnosis, provider, date, citation]
- **Elapsed time and intervening events:** [duration; gap A-n; representation datapoint if applicable]
- **Context:** [source-stated explanation, documentation limitation, or none located]
- **Interpretation limit:** [no credibility, causation, fabrication, or medical-significance inference]
- **Retrieval action:** [F-n / none]

## Possible Findings — Unverified

- [Possibility, why it could not be page-verified, and `[UNVERIFIED]` label.]

## F. Proposed Retrieval Plan

Counsel review and authorization are required before sending or serving any request.

| # | Priority | Custodian | Date range | Record type | Proposed mechanism | Resolves |
|---|----------|-----------|------------|-------------|--------------------|----------|
| F-1 | [High/Medium/Low] | [specific or unresolved type] | [range] | [specific non-privileged records] | [authorization / supplemental request / subpoena, subject to counsel review] | [A-1, B-2, E-1] |

**Separate custodians or departments:** [clinical / billing / pharmacy / imaging / other]

**Privilege or authorization flags:** [representation, lien, LOP, or other materials requiring counsel review]

## Methodology and Verification Log

- Provider and Encounter Index: [built / reused; source and date]
- Encounters indexed: [n] across [n] providers
- Incident-time source and precision: [citation / unavailable; hours or days]
- Complaint baseline: [window and encounters included]
- Representation timeline: [source-cited items and any uncited user input]
- Audit scope: [checklist sections completed and any sampling]
- Citation preflight: [prefixes, formats, or file-page scheme]
- Verification: [n verified, n unverified, n corrected or removed]
- Limitations: [missing sources, OCR issues, inherited citations, or unperformed checks]

## Limitations

Gap significance is case- and jurisdiction-specific. Duration thresholds are review heuristics, not legal or clinical standards. An apparent treatment gap may reflect an incomplete production rather than absent care, and supplemental records may resolve current findings. Episodic or protocol-driven care can make fixed intervals misleading. Billing mismatches do not establish fraud or error. A newly documented complaint may reflect onset, documentation, or production differences; this report makes no credibility or causation finding. Representation datapoints are temporal facts and support no inference that representation caused treatment or complaint changes. This analysis supports but does not replace attorney judgment.
