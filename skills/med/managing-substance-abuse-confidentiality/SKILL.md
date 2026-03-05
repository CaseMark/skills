---
name: managing-substance-abuse-confidentiality
description: Applies 42 CFR Part 2 substance abuse confidentiality requirements with consent and disclosure protocols. Use when managing SUD records, applying Part 2 requirements, or handling substance abuse confidentiality.
tags:
  - management
  - healthcare-compliance
metadata:
  author: casemark
  practice_areas:
    - Healthcare Compliance
    - HIPAA
    - Healthcare Regulation
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---

# Managing Substance Abuse Confidentiality

A structured framework for applying the federal confidentiality requirements of 42 CFR Part 2 to substance use disorder (SUD) patient records, including consent management, permitted disclosures, and the interaction between Part 2 and HIPAA following the 2024 Final Rule amendments.

## Why This Skill Exists

42 CFR Part 2 imposes confidentiality protections for SUD treatment records that are significantly stricter than HIPAA. Part 2 was enacted to address the stigma of substance use disorders and the concern that fear of disclosure would deter individuals from seeking treatment. Unlike HIPAA, Part 2 generally requires patient consent for any disclosure of SUD records—including for treatment, payment, and healthcare operations (activities that HIPAA permits without consent). Violations carry criminal penalties (up to $500 for first offense, up to $5,000 for subsequent offenses under 42 U.S.C. § 290dd-2(f)). The 2024 Final Rule (effective February 2024) aligned Part 2 more closely with HIPAA by permitting disclosure for treatment, payment, and healthcare operations with a single prior written consent, but significant differences remain—particularly regarding use of Part 2 records in criminal investigations. Organizations that treat SUD patients or receive SUD records must navigate the intersection of Part 2 and HIPAA with precision to avoid both improper disclosure (Part 2 violation) and improper restriction of information needed for patient care (patient safety risk).

---

## Checkpoint A — Program and Applicability Assessment

### Intake Questions

1. Is the organization a Part 2 "program"—a federally assisted entity that holds itself out as providing substance use disorder diagnosis, treatment, or referral for treatment? (Includes any program receiving federal funding, tax-exempt status, or authorization under controlled substance registration.)
2. Does the organization receive SUD records from Part 2 programs (making it a "lawful holder" subject to redisclosure restrictions)?
3. What types of SUD services are provided—detoxification, medication-assisted treatment (MAT), counseling, residential treatment, outpatient treatment, screening and brief intervention?
4. How does the organization identify and segment Part 2-protected records in its EHR system?
5. Has the organization implemented the 2024 Final Rule amendments that align Part 2 consent with HIPAA's TPO framework?
6. Does the organization participate in health information exchanges (HIEs) that transmit SUD data?
7. Does the organization have patients who are court-ordered to treatment?
8. Are there research activities involving Part 2-protected patient data?
9. Does the organization's breach notification process address Part 2 records specifically?
10. How does the organization handle law enforcement requests for SUD records?

### Required Documents

- 42 CFR Part 2 policies and procedures
- Part 2 consent forms (current and prior to 2024 amendments)
- EHR configuration documentation showing Part 2 record segmentation
- Staff training records on Part 2 requirements
- Patient notice of Part 2 rights
- Qualified Service Organization Agreements (QSOAs)
- Court order documentation for any court-ordered disclosures
- HIE participation agreements addressing Part 2 data
- Breach notification procedures specific to Part 2 records
- Research data use agreements for Part 2-protected data

---

## Step 1 — Applicability Determination

Determine what records and entities are subject to Part 2:

- **Part 2 Program Definition**: A "program" is any individual, entity, or identifiable unit within a general medical facility that holds itself out as providing and actually provides SUD diagnosis, treatment, or referral for treatment. "Federally assisted" includes entities receiving any federal funding, having tax-exempt status, being authorized by government entity to provide SUD treatment, or being registered under the Controlled Substances Act to dispense or prescribe substances for SUD treatment (e.g., buprenorphine prescribers under DATA 2000/MAT Act).
- **Protected Information**: Part 2 protects "patient identifying information"—any information that identifies a person as having or having had a substance use disorder, or as having received SUD diagnosis, treatment, or referral, whether directly or by inference.
- **General Medical Setting**: When SUD treatment occurs within a general medical facility (hospital, primary care), Part 2 applies only to records created by the identifiable SUD treatment unit. However, if SUD information is integrated into the general medical record without segmentation, the entire record may be subject to Part 2 protections.
- **Lawful Holder Obligations**: Any entity that receives Part 2-protected information with proper consent becomes a "lawful holder" and must comply with redisclosure restrictions—including the notice that accompanies every disclosure stating the information may not be further disclosed without consent.

---

## Step 2 — Consent Framework (Post-2024 Final Rule)

Apply the updated consent requirements:

**Single Consent for TPO (New Under 2024 Rule)**:
- Patients may now sign a single consent that permits disclosure for treatment, payment, and healthcare operations—aligning with HIPAA's TPO concept.
- The consent must be written and include: patient name, purpose of disclosure (TPO), entities/persons permitted to receive (or class of entities, e.g., "my treating providers"), right to revoke, expiration date or event, and signature/date.
- Unlike prior law, a single consent can authorize ongoing disclosures for TPO without naming each specific recipient.

**Consent for Other Purposes**:
- Disclosures for purposes other than TPO (e.g., legal proceedings, employment, insurance eligibility) still require specific consent that identifies the particular recipient and purpose.
- Consent for legal proceedings requires additional protections and may require court order in some circumstances.

**Revocation of Consent**:
- Patients may revoke consent at any time. Revocation applies prospectively—disclosures made before revocation are not affected.
- Document revocation in the patient record and notify entities previously authorized to receive information.

**Consent Exceptions (No Consent Required)**:
- Medical emergency (bona fide medical emergency threatening life, with documentation)
- Audit and evaluation by government agencies or qualified personnel
- Research with IRB or Privacy Board approval and data use agreement
- Court order meeting specific Part 2 requirements (not a standard subpoena)
- Reports of suspected child abuse or neglect per state mandatory reporting laws
- Qualified Service Organization activities (under a QSOA)
- Communication within a program or between a program and an entity with direct administrative control

---

## Step 3 — Criminal Justice and Legal Proceedings

Address the heightened protections for legal proceedings:

- **Prohibition on Use in Criminal Proceedings**: Under the 2024 amendments, Part 2 records disclosed with consent for TPO cannot be used in any criminal investigation or prosecution of the patient—this is a fundamental difference from HIPAA. The prohibition applies to law enforcement, prosecutors, and courts.
- **Court Orders**: Part 2 records may be disclosed pursuant to a court order, but the court order must meet specific Part 2 requirements (42 CFR § 2.64–2.67), which are more restrictive than a general subpoena. The court must find "good cause" by determining that disclosure is more important than potential injury to the patient, the physician-patient relationship, and treatment services.
- **Subpoenas**: A standard subpoena is not sufficient to compel Part 2 records. The program must assert the Part 2 confidentiality protection and require a qualifying court order.
- **Law Enforcement Requests**: Absent a qualifying court order, Part 2 programs must not disclose patient identifying information in response to law enforcement requests, search warrants (unless accompanied by a qualifying court order), or grand jury subpoenas.
- **Child Abuse Reporting**: Part 2 permits (but does not require) reporting suspected child abuse or neglect under state mandatory reporting laws. The report may not include information identifying the patient as having an SUD beyond what is needed for the report.

---

## Step 4 — EHR Segmentation and Technical Implementation

- **Record Segmentation**: Evaluate whether the organization's EHR supports segmenting Part 2-protected records so they are not disclosed in general record releases or HIE transmissions without appropriate consent.
- **Segmentation Approaches**: Common approaches include: separate encounter types with restricted access, Part 2 sensitivity flags on records, separate SUD treatment modules, and consent-based access controls. No approach is perfect—assess tradeoffs between patient safety (provider access to SUD information for treatment) and confidentiality.
- **HIE Participation**: If the organization participates in an HIE, verify that Part 2 records are handled according to the patient's consent status. HIE systems must be configured to suppress Part 2 data when consent has not been obtained.
- **Redisclosure Notice**: Every disclosure of Part 2 information must be accompanied by the Part 2 redisclosure prohibition notice: "This information has been disclosed to you from records protected by federal confidentiality rules (42 CFR Part 2). The federal rules prohibit you from making any further disclosure of information in this record that identifies a patient as having or having had a substance use disorder either directly, by reference to publicly available information, or through verification of such identification by another person unless further disclosure is expressly permitted by the written consent of the individual whose information is being disclosed or as otherwise permitted by 42 CFR Part 2."
- **Breach Response**: Part 2 now aligns breach notification with HIPAA requirements under the 2024 amendments. Verify the organization's breach response process includes Part 2-specific considerations.

---

## Step 5 — Training and Operational Compliance

- Train all workforce members who handle SUD records on Part 2 requirements—separate from general HIPAA training, as the rules are materially different.
- Train front desk and registration staff on the prohibition against acknowledging a patient's enrollment in SUD treatment to outside callers.
- Train HIM and release-of-information staff on Part 2 consent requirements, redisclosure restrictions, and the distinction between Part 2 consent and HIPAA authorization.
- Train clinical staff on when Part 2 permits disclosure without consent (medical emergency) and when consent is required even for treatment purposes.
- Implement audit processes to verify that Part 2 records are not disclosed outside the consent authorization—EHR access audits, release-of-information audits, and HIE disclosure audits.

---

## Checkpoint B — Compliance Validation

1. Confirm Part 2 applicability is correctly determined for the organization and its component programs.
2. Verify consent forms meet 2024 Final Rule requirements including the TPO single consent option.
3. Confirm EHR segmentation prevents unauthorized disclosure of Part 2 records in general record releases.
4. Verify the redisclosure prohibition notice accompanies every disclosure of Part 2 information.
5. Confirm law enforcement and legal proceeding protocols correctly apply Part 2's heightened protections.
6. Verify QSOAs are in place for all qualified service organizations accessing Part 2 records.
7. Confirm workforce training addresses Part 2-specific requirements separately from general HIPAA training.
8. Verify breach response procedures include Part 2-specific considerations.

---

## Quality Audit

- [ ] Part 2 program applicability correctly determined
- [ ] 2024 Final Rule amendments implemented in consent processes
- [ ] Single TPO consent form meets all Part 2 requirements
- [ ] Non-TPO disclosures use specific consent with identified recipients
- [ ] EHR segmentation prevents Part 2 record disclosure without consent
- [ ] Redisclosure prohibition notice accompanies every Part 2 disclosure
- [ ] Law enforcement protocols prohibit disclosure absent qualifying court order
- [ ] Court order requirements (good cause finding) enforced for legal proceedings
- [ ] QSOAs executed for all qualified service organizations
- [ ] Workforce training addresses Part 2 separately from HIPAA
- [ ] Breach notification process includes Part 2 considerations
- [ ] HIE participation agreements address Part 2 data handling

---

## Guidelines

- Part 2 is stricter than HIPAA—do not apply HIPAA rules to Part 2 records by default. Part 2 requires consent for disclosures that HIPAA permits without consent, and Part 2 provides protections against use in criminal proceedings that HIPAA does not.
- The 2024 Final Rule significantly aligned Part 2 with HIPAA for TPO disclosures, but critical differences remain—particularly the prohibition on use in criminal investigations and prosecutions. This is the single most important distinction between Part 2 and HIPAA.
- Record segmentation is operationally challenging but necessary. Organizations that integrate SUD records into general medical records without segmentation risk inadvertent disclosure and may subject the entire record to Part 2 protections.
- A standard subpoena does not overcome Part 2 protections. Organizations must assert Part 2 confidentiality and require a qualifying court order with the specific "good cause" finding required by Part 2.
- The medical emergency exception is narrow—it applies only to bona fide medical emergencies threatening life and requires documentation of the emergency and the information disclosed. It does not authorize ongoing disclosure after the emergency is resolved.
- MAT prescribers who are Part 2 programs by virtue of their DEA registration must comply with all Part 2 requirements, including consent, redisclosure restrictions, and recordkeeping.
- This skill produces confidentiality compliance assessment output, not legal advice. Part 2 compliance decisions should involve qualified healthcare privacy counsel, particularly for court-ordered disclosures and law enforcement requests.
