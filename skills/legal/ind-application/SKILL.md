---
name: ind-application
description: Drafts FDA Investigational New Drug (IND) applications compliant with 21 CFR Part 312, including Form 1571, Investigator's Brochure, clinical protocols, CMC sections, and nonclinical data packages. Covers all phases of clinical trial authorization. Use when preparing IND submissions, pre-IND packages, IND amendments, or FDA clinical trial authorization documents for pharmaceutical or biotech sponsors.
tags:
  - drafting
  - memo
  - regulatory
---

# Investigational New Drug (IND) Application

Drafts a complete IND application under 21 CFR Part 312 for FDA authorization to initiate human clinical trials.

## Prerequisites

1. **Drug substance/product information** — chemical name, code designation, structural formula, mechanism of action
2. **Nonclinical study reports** — pharmacology, toxicology, PK/PD data packages
3. **CMC data** — manufacturing process, specifications, stability data, certificates of analysis
4. **Clinical protocol(s)** — study design, objectives, endpoints, statistical analysis plan
5. **Investigator information** — CVs, Form FDA 1572, clinical site details
6. **Prior human experience data** (if any) — foreign clinical trials, published literature, compassionate use
7. **IRB documentation** — approval letters or submission plans, informed consent forms

## Output Structure

The IND must follow the section order mandated by 21 CFR 312.23(a):

| Section | Content | Regulatory Reference |
|---------|---------|---------------------|
| 1. Cover Sheet | FDA Form 1571 (current version from fda.gov) | 312.23(a)(1) |
| 2. Table of Contents | Mirror regulatory section numbering exactly | 312.23(a)(2) |
| 3. Introductory Statement | Scientific rationale, therapeutic purpose, medical need, general investigational plan | 312.23(a)(3) |
| 4. Investigator's Brochure | Safety profile, efficacy data, pharmacology, known risks | 312.23(a)(5) |
| 5. Clinical Protocol(s) | Study design, objectives, selection criteria, dosing, safety monitoring, statistical plan | 312.23(a)(6) |
| 6. CMC — Drug Substance | Composition, structure, synthesis/manufacturing, specifications, stability | 312.23(a)(7) |
| 7. CMC — Drug Product | Formulation, manufacture, controls, container/closure, stability | 312.23(a)(7) |
| 8. Pharmacology/Toxicology | Nonclinical studies: PK, acute/chronic tox, repro tox, genotox, carcinogenicity | 312.23(a)(8) |
| 9. Previous Human Experience | Prior clinical data, foreign trials, literature review | 312.23(a)(9) |
| 10. Additional Information | IRB approvals, informed consent, investigator qualifications, lab certifications | 312.23(a)(10) |

### Form 1571 Checklist

- [ ] Sponsor name, address, contact
- [ ] Drug name and all code designations
- [ ] Proposed clinical trial phase (I, II, III)
- [ ] IND number (if amendment) or "Initial" designation
- [ ] Serial number
- [ ] Indication(s) under investigation
- [ ] List of all enclosed sections
- [ ] Authorized signature with date

### Investigator's Brochure Structure

- [ ] Physical/chemical/pharmaceutical properties
- [ ] Nonclinical pharmacology summary
- [ ] Nonclinical PK and metabolism
- [ ] Nonclinical toxicology (tabulate: species, route, duration, NOAEL, key findings)
- [ ] Clinical experience summary (if applicable)
- [ ] Known/anticipated adverse effects and precautions

### Clinical Protocol Required Elements

- [ ] Title, protocol number, version/date
- [ ] Primary and secondary objectives
- [ ] Study design and phase
- [ ] Inclusion/exclusion criteria
- [ ] Dosing regimen with rationale
- [ ] Efficacy and safety endpoints
- [ ] Stopping rules and dose-limiting toxicity definitions
- [ ] Safety monitoring plan (AE reporting, DSMB if applicable)
- [ ] Statistical analysis plan with sample size justification

### CMC — Phase-Appropriate Detail

| Phase | Drug Substance | Drug Product | Stability |
|-------|---------------|-------------|-----------|
| Phase I | Synthetic route, preliminary specs, structure confirmation | Formulation description, basic controls | Abbreviated (sufficient to cover trial duration) |
| Phase II | Refined process, tightened specs, impurity profiles | Process validation initiated, expanded controls | 6+ months accelerated and long-term |
| Phase III | Full process validation, complete characterization | Full cGMP compliance, container/closure validation | ICH-compliant program |

### Nonclinical Data Presentation

For each study, tabulate:

| Field | Content |
|-------|---------|
| Study type | (e.g., 28-day repeat dose toxicity) |
| Test facility | Name, GLP compliance status |
| Species/strain | |
| Route of administration | |
| Dose levels | |
| Duration | |
| NOAEL/NOEL | |
| Key findings | |
| Relevance to clinical dose | |

### Environmental Assessment

- Most INDs qualify for **categorical exclusion** under 21 CFR 25.31(e)
- If claiming exclusion: cite the specific 21 CFR 25 provision and include a brief statement of basis
- If exclusion does not apply: prepare environmental assessment per 21 CFR Part 25 Subpart B

## Guidelines

- **Verify all FDA forms** — retrieve current Form 1571 and Form 1572 versions directly from fda.gov; forms update periodically
- **Phase-appropriate CMC** — do not over-document early-phase INDs or under-document late-phase; follow FDA guidance "INDs for Phase 2 and Phase 3 Studies: CMC Information" [VERIFY]
- **Cross-reference internally** — every protocol reference to nonclinical data must cite the specific section/page of the IND where that data appears
- **GLP compliance** — pivotal nonclinical safety studies must be conducted under 21 CFR Part 58 (GLP); flag any non-GLP studies and justify
- **Prior human experience** — search ClinicalTrials.gov and published literature for any prior exposure data on the compound or close analogs
- **Safety-first framing** — every section must demonstrate adequate basis for protecting human subjects
- **No promotional language** — IND is a scientific/regulatory document; avoid efficacy claims unsupported by data
- **Redact trade secrets** — mark confidential commercial information per 21 CFR 312.130 if sponsor requests
- **eCTD format** — for electronic submissions, organize per FDA eCTD guidance Module 1-5 structure [VERIFY]
- **Pre-IND meeting** — note any FDA feedback from Type B pre-IND meetings and address each comment explicitly
