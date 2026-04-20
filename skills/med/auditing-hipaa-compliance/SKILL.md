---
name: auditing-hipaa-compliance
language: en
description: Conducts HIPAA compliance assessments with Privacy Rule, Security Rule, and Breach Notification analysis. Use when auditing HIPAA compliance, assessing privacy practices, or reviewing security controls.
tags:
  - audit
  - healthcare-compliance
  - compliance
metadata:
  author: casemark
  practice_areas:
    - Healthcare Compliance
    - HIPAA
    - Healthcare Regulation
  document_types:
    - Audit Report
  skill_modes:
    - Audit
    - Compliance
---

# Auditing HIPAA Compliance

A structured methodology for conducting compliance assessments across all three HIPAA rules—Privacy (45 CFR §§ 160, 164 Subpart E), Security (45 CFR § 164 Subpart C), and Breach Notification (45 CFR §§ 164.400–414)—for covered entities and business associates.

## Why This Skill Exists

HIPAA enforcement has intensified since the HITECH Act expanded OCR's authority and introduced tiered civil monetary penalties up to $2,067,813 per violation category per year. Resolution agreements routinely exceed $1 million, and corrective action plans impose multi-year monitoring burdens. A rigorous audit methodology identifies gaps before OCR does, reduces breach likelihood, and demonstrates "reasonable diligence" that can mitigate penalty tiers under 45 CFR § 160.404. Healthcare organizations that conduct proactive HIPAA audits reduce average breach-related costs and satisfy downstream obligations to payers, accreditors, and state regulators that layer on top of federal requirements.

---

## Checkpoint A — Intake and Scoping

### Intake Questions

1. Is the entity a covered entity (health plan, clearinghouse, provider with electronic transactions) or a business associate?
2. What HIPAA rules are in scope—Privacy only, Security only, Breach Notification only, or comprehensive?
3. Does the entity participate in an Organized Health Care Arrangement (OHCA) or Affiliated Covered Entity (ACE) designation?
4. What is the entity's current risk analysis date and who performed it?
5. Has the entity been subject to prior OCR investigations, resolution agreements, or corrective action plans?
6. Are there active business associate agreements (BAAs) with subcontractors who access ePHI?
7. Does the entity operate in states with stricter privacy laws (e.g., California CMIA, Texas HB 300, New York SHIELD Act)?
8. What electronic health record (EHR) system is in use, and what version?
9. Has the entity experienced any reportable breaches in the past three years?
10. Does the entity use cloud-hosted infrastructure for ePHI storage or transmission?

### Required Documents

- Current HIPAA policies and procedures manual
- Most recent Security Risk Analysis (SRA) per 45 CFR § 164.308(a)(1)(ii)(A)
- Business Associate Agreement inventory with execution dates
- Notice of Privacy Practices (NPP) currently in effect
- Training records for workforce members (dates, topics, attendance)
- Breach log and any prior 60-day notifications to HHS
- IT asset inventory including devices that create, receive, maintain, or transmit ePHI
- Access control logs and user provisioning/de-provisioning records
- Incident response plan and any prior incident reports
- Physical security documentation (facility access controls, workstation policies)

---

## Step 1 — Privacy Rule Assessment (45 CFR § 164 Subpart E)

Evaluate the entity's compliance with Privacy Rule administrative requirements and individual rights:

- **NPP Content Review**: Confirm the NPP includes all required elements under § 164.520(b)—uses and disclosures, individual rights, entity duties, complaint process, and effective date. Verify the NPP reflects 2013 Omnibus Rule amendments including breach notification language and genetic information nondiscrimination.
- **Minimum Necessary Standard**: Assess whether the entity has identified persons or classes who need PHI access, the categories of PHI needed, and conditions appropriate to access per § 164.514(d). Review role-based access policies against actual system permissions.
- **Individual Rights Implementation**: Test processes for access requests (§ 164.524, 30-day response), amendment requests (§ 164.526), accounting of disclosures (§ 164.528), restriction requests (§ 164.522), and confidential communications (§ 164.522(b)). Verify the entity honors the mandatory restriction for self-pay patients under HITECH § 13405(a).
- **Authorization Forms**: Review authorization forms against the core elements and required statements in § 164.508(c). Confirm separate authorizations for psychotherapy notes, marketing, and sale of PHI.
- **De-identification Methods**: If the entity de-identifies data, verify use of Expert Determination (§ 164.514(b)(1)) or Safe Harbor (§ 164.514(b)(2)) with all 18 identifiers removed or generalized.
- **Research Uses**: If applicable, evaluate compliance with § 164.512(i) including IRB/Privacy Board waivers, preparatory-to-research access, and decedent research provisions.

---

## Step 2 — Security Rule Assessment (45 CFR § 164 Subpart C)

Evaluate all three safeguard categories with attention to required vs. addressable implementation specifications:

- **Administrative Safeguards (§ 164.308)**:
  - Risk Analysis: Verify the SRA is comprehensive (all ePHI repositories), current (updated for system changes), and documents threats, vulnerabilities, likelihood, and impact per NIST SP 800-30 methodology.
  - Risk Management: Confirm a documented risk management plan addresses findings from the SRA with remediation timelines and responsible parties.
  - Workforce Security: Review procedures for authorization, supervision, clearance, and termination per § 164.308(a)(3). Verify access is terminated within 24 hours of workforce departure.
  - Information Access Management: Confirm role-based access aligned with minimum necessary, and review the process for granting, modifying, and revoking access.
  - Security Incident Procedures: Verify documented procedures for identifying, responding to, and mitigating security incidents per § 164.308(a)(6).
  - Contingency Plan: Evaluate data backup plan, disaster recovery plan, emergency mode operation plan, and testing/revision procedures per § 164.308(a)(7).

- **Physical Safeguards (§ 164.310)**:
  - Facility Access Controls: Review policies for facility security plans, access control/validation, maintenance records, and workstation security.
  - Device and Media Controls: Evaluate disposal, media re-use, accountability, and data backup/storage procedures for devices containing ePHI.

- **Technical Safeguards (§ 164.312)**:
  - Access Controls: Verify unique user identification, emergency access procedures, automatic logoff, and encryption/decryption implementations.
  - Audit Controls: Confirm mechanisms to record and examine activity in systems containing ePHI per § 164.312(b).
  - Integrity Controls: Evaluate mechanisms to authenticate ePHI and protect against improper alteration or destruction.
  - Transmission Security: Verify encryption of ePHI in transit. Document rationale if encryption is deemed "not reasonable and appropriate" for addressable specifications.

---

## Step 3 — Breach Notification Rule Assessment (45 CFR §§ 164.400–414)

- **Breach Definition Compliance**: Verify the entity applies the correct definition of breach—acquisition, access, use, or disclosure of unsecured PHI in a manner not permitted that compromises security or privacy, with the four-factor risk assessment per § 164.402.
- **Risk Assessment Methodology**: Confirm the entity's breach risk assessment evaluates: (1) nature and extent of PHI involved, (2) unauthorized person who used/received PHI, (3) whether PHI was actually acquired or viewed, and (4) extent of risk mitigation.
- **Notification Timeliness**: Verify individual notification within 60 days of discovery (§ 164.404), HHS notification annually for sub-500 breaches or within 60 days for 500+ breaches (§ 164.408), and media notification for 500+ breaches in a state/jurisdiction (§ 164.406).
- **Notification Content**: Confirm notifications include: description of breach, PHI types involved, steps individuals should take, entity's investigation/mitigation actions, and contact information per § 164.404(c).
- **Business Associate Obligations**: Verify BAs report breaches to covered entities without unreasonable delay and no later than 60 days after discovery per § 164.410, or shorter timeframes if specified in the BAA.
- **Breach Log Maintenance**: Confirm maintenance of a breach log capturing all incidents including those below the 500-individual threshold.

---

## Step 4 — Business Associate Agreement Review

- Inventory all vendors, subcontractors, and downstream entities that meet the business associate definition under § 160.103.
- Verify each BAA contains the required provisions of § 164.504(e) including: permitted uses/disclosures, safeguard obligations, breach reporting, subcontractor flow-down, return/destruction of PHI, and termination provisions.
- Confirm BAAs are updated to reflect 2013 Omnibus Rule requirements including direct BA liability.
- Flag any entity accessing PHI without a BAA in place—this constitutes an impermissible disclosure by the covered entity.
- Review conduit exception applicability for entities providing mere transmission (e.g., USPS, ISPs with transient access).

---

## Step 5 — Findings Classification and Corrective Actions

Classify each finding using a consistent severity taxonomy:

| Severity | Definition | Expected Remediation |
|----------|-----------|---------------------|
| Critical | Active or imminent breach risk; direct violation of required standard | Immediate (0–30 days) |
| High | Addressable specification not implemented without documented rationale; systemic gap | 30–60 days |
| Medium | Policy exists but implementation is inconsistent or undocumented | 60–90 days |
| Low | Best practice gap; no regulatory violation but improvement opportunity | 90–180 days |
| Informational | Observation for future consideration | Next audit cycle |

For each finding, document: the specific regulatory citation, factual basis with evidence references, risk implications, and recommended corrective action with responsible party and target date.

---

## Checkpoint B — Report Review and Validation

Before finalizing the audit report:

1. Verify every finding maps to a specific HIPAA regulatory citation (section and paragraph level).
2. Confirm all required vs. addressable specifications are correctly categorized—addressable does not mean optional; it requires documented assessment and either implementation or equivalent alternative measures per § 164.306(d).
3. Cross-check findings against OCR's published enforcement trends and recent resolution agreements for pattern consistency.
4. Validate that corrective action recommendations are operationally feasible within stated timelines.
5. Ensure the report distinguishes between Privacy Rule, Security Rule, and Breach Notification Rule findings for clarity.
6. Review for any state law preemption issues where state law is "more stringent" and therefore not preempted by HIPAA per § 160.203.
7. Confirm the report includes an executive summary, methodology description, scope limitations, and detailed finding appendix.

---

## Quality Audit

- [ ] All three HIPAA rules (Privacy, Security, Breach Notification) addressed in scope
- [ ] Security Risk Analysis evaluation uses NIST SP 800-30 or equivalent recognized framework
- [ ] Every finding includes specific regulatory citation at section/paragraph level
- [ ] Addressable specifications analyzed with documented rationale for implementation decisions
- [ ] Business associate inventory is complete with BAA status for each entity
- [ ] Breach notification timeline compliance verified against 60-day requirement
- [ ] Individual rights processes tested, not just policy-reviewed
- [ ] State law overlay identified for applicable jurisdictions
- [ ] Corrective action plan includes responsible parties, timelines, and verification methods
- [ ] Report clearly labels findings by severity and regulatory category
- [ ] All [VERIFY] tags resolved or escalated before report finalization

---

## Guidelines

- Never conflate "addressable" with "optional"—the Security Rule requires documented assessment of every addressable specification and implementation of an equivalent alternative if the specification itself is not implemented.
- Always distinguish between Privacy Rule violations (impermissible uses/disclosures) and Security Rule violations (safeguard failures) as they carry different penalty structures and corrective action implications.
- Apply the four-factor breach risk assessment before concluding a security incident is not a reportable breach—the presumption is that any impermissible use/disclosure of unsecured PHI is a breach unless the risk assessment demonstrates low probability of compromise.
- OCR investigations increasingly target risk analysis adequacy—a checklist approach without genuine threat/vulnerability analysis will be found deficient.
- Maintain attorney-client privilege protections where the audit is conducted under legal direction; clearly mark privileged materials and limit distribution.
- Document all assumptions, scope exclusions, and limitations of the audit—this protects the auditor and prevents the entity from claiming broader compliance than assessed.
- HIPAA preempts state law only when state law is "less stringent"—always check whether applicable state law provides greater protection and note where state requirements exceed HIPAA.
- This skill produces compliance analysis, not legal advice. All findings should be reviewed by qualified healthcare counsel before enforcement response or voluntary disclosure decisions.
