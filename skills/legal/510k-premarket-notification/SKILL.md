---
name: 510k-premarket-notification
description: Drafts FDA 510(k) Premarket Notification submissions for medical device clearance, including cover letters, FDA Form 3514, device descriptions, substantial equivalence comparisons, performance data sections, labeling, and required statements under 21 CFR Part 807. Supports Traditional, Special, and Abbreviated 510(k) pathways. Use when preparing Class II medical device regulatory filings, FDA premarket submissions, or substantial equivalence analyses.
tags:
  - drafting
  - letter
  - regulatory
---

# FDA 510(k) Premarket Notification

Drafts a complete 510(k) submission package demonstrating substantial equivalence to a predicate device under 21 CFR Part 807, Subpart E.

## Prerequisites

1. **510(k) type determination** — Traditional, Special, or Abbreviated
2. **Predicate device identified** — trade name, manufacturer, K-number, clearance date
3. **Device classification info** — product code, regulation number, panel, class designation
4. **Establishment registration** — FDA registration number, U.S. agent info (if foreign)
5. **Technical file** — engineering drawings, materials list, software architecture (if applicable)
6. **Performance data** — bench testing, biocompatibility (ISO 10993), clinical/literature evidence
7. **Proposed labeling** — IFU, package insert, patient materials, packaging artwork

## Output Structure

### 1. Cover Letter

Address to the appropriate CDRH division. Include:

| Element | Detail |
|---|---|
| Device identification | Trade name + common/usual name |
| 510(k) type | Traditional / Special / Abbreviated |
| Predicate device | Trade name, manufacturer, K-number |
| Regulatory pathway justification | Why 510(k) vs. PMA |
| Submitter contact | Company, regulatory contact, establishment registration |
| U.S. agent | Required if foreign manufacturer |

Tone: professional, collaborative, concise.

### 2. FDA Form 3514

Complete all fields:

- **Applicant**: legal name, FDA establishment registration number, manufacturing address
- **Device names**: trade name (proprietary) + common/usual name (generic)
- **Classification**: product code (3-letter), regulation number (21 CFR §___), panel, class
- **Submission type**: original or resubmission (if resubmission, prior K-number)
- **510(k) type**: Traditional / Special / Abbreviated
- **Disclosure election**: 510(k) Summary (public) or Statement (on-request)
- **Contact info**: phone, email, official correspondent name/title
- **Signature block**: authorized representative with binding authority

### 3. Device Description

Draft a technical description enabling reviewer comprehension without physical examination:

- Physical/dimensional characteristics (size, weight, configuration)
- Materials of construction — flag all patient-contacting materials with ISO 10993 status
- Operating principles and mechanism of action
- Software/firmware architecture, cybersecurity features, AI/ML components (if applicable)
- Energy source type and safety controls (if applicable)
- Sterility method and SAL (if sterile)
- Novel features — each must be addressed in SE comparison

Include references to engineering drawings, cross-sections, annotated photos.

### 4. Intended Use & Indications for Use

| Component | Requirements |
|---|---|
| Intended use | General purpose, broad clinical condition |
| Indications for use | Patient population (age, condition), specific clinical conditions, anatomical site, selection criteria |
| Contraindications | Patients/conditions where device should not be used |
| Consistency check | Must match predicate IU; any divergence requires justification |
| Labeling alignment | Exact same language in labeling, submission, and Form 3514 |

Every indication must be supported by performance data in the submission.

### 5. Substantial Equivalence Comparison

Present as a structured side-by-side table:

| Parameter | Subject Device | Predicate Device (K______) | Analysis |
|---|---|---|---|
| Intended use | | | Same / Different — justify |
| Technology | | | Same fundamental approach? |
| Materials | | | Biocompatibility equivalence |
| Energy source | | | Type, delivery, controls |
| Software | | | Functions, algorithms, I/O |
| Performance specs | | | Accuracy, precision, range |
| Physical characteristics | | | Size, shape, configuration |
| Novel features | | | Why no new safety/effectiveness questions |

**Split predicate strategy**: If using multiple predicates, justify the approach. At least one predicate must share the same intended use.

For every difference: explain why it does not raise new questions of safety or effectiveness, supported by data.

### 6. Performance Data

Organize by study type in this order:

1. **Bench testing** — test method, equipment, conditions, sample size, acceptance criteria (pre-specified), results with statistics, predicate comparison
2. **Biocompatibility** (ISO 10993-1) — contact type/duration, applicable tests, lab identity, acceptance criteria, results; document any unexpected findings with follow-up
3. **Animal studies** (if applicable) — GLP compliance, model justification, sample size with power analysis, endpoints, results including adverse events
4. **Clinical data** — study design, population (inclusion/exclusion), sample size with power analysis, primary/secondary endpoints, statistical analysis, adverse events; OR literature review with citations and relevance synthesis
5. **Standards compliance** — list all applicable consensus standards (ASTM, ISO, IEC, AAMI) with test reports or declarations of conformity
6. **FDA guidance compliance** — cite device-specific guidance documents followed

Each data set must link to a specific SE comparison point or IFU claim.

### 7. Labeling Package

Checklist of required components:

- [ ] Instructions for Use (IFU) — setup, technique, troubleshooting, maintenance
- [ ] Package insert — clinical info, indications, contraindications, warnings
- [ ] Patient labeling (if applicable) — lay language appropriate to population
- [ ] Device/packaging labels — name, manufacturer, lot/serial, sterilization indicators, symbols (ISO 15223-1), storage conditions, expiration
- [ ] Rx statement: "Caution: Federal law restricts this device to sale by or on the order of a physician" (if prescription)
- [ ] Sterilization info (if sterile) — method, SAL, package integrity, sterility maintenance
- [ ] Symbol glossary

Compliance: 21 CFR Part 801. IFU indications must exactly match submission indications.

### 8. Truthful and Accurate Statement

Per 21 CFR 807.87(k):

```
I certify that, in my capacity as [TITLE] of [COMPANY], all information
contained in this 510(k) premarket notification is truthful and accurate,
and no material fact has been omitted. I understand that knowingly making
a false statement constitutes a criminal offense under 18 U.S.C. § 1001.

Printed Name: ___________________________
Title: ___________________________
Signature: ___________________________
Date: ___________________________
```

Signatory must have direct knowledge of submission contents and binding authority.

### 9. 510(k) Summary or Statement

**If Summary** (21 CFR 807.92) — will be public within 30 days of clearance:

- Submitter contact information
- Device names (trade + common), classification (product code, regulation number)
- Concise device description
- Intended use / indications for use (exact language from submission)
- Predicate comparison summary (similarities, differences, resolution)
- Performance data summary (study types, methods, key endpoints, conclusions)
- Overall SE conclusion

**If Statement** (21 CFR 807.93) — greater confidentiality:

- Declaration that full 510(k) will be provided within 30 days of written request
- Contact information and request procedures
- Organization must have fulfillment process in place

## Guidelines

- Cross-reference all sections for consistency in device description, IU language, and performance claims
- Verify predicate device is currently legally marketed and not subject to Class III order
- Consider Pre-Submission (Q-Sub) for novel aspects or pathway uncertainty
- Electronic submissions must comply with 21 CFR Part 11 for signatures
- Flag any proprietary/trade-secret content when choosing Summary vs. Statement
- Mark all uncertain regulatory citations with [VERIFY]
- Do not draft clinical study protocols — flag need for separate clinical planning if data gaps exist
