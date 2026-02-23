---
name: hipaa-baa
description: >-
  Drafts HIPAA/HITECH-compliant Business Associate Agreements (BAAs) for
  covered entities and business associates handling PHI/ePHI, aligning Privacy
  Rule and Security Rule duties, breach notification, subcontractor
  flow-downs, and individual-rights support with state-law overlays. Use when
  drafting or updating a BAA, negotiating vendor PHI access, or attaching
  HIPAA terms to a services agreement. Trigger keywords: BAA, business
  associate agreement, HIPAA contract, PHI vendor agreement, HITECH breach
  notice.
tags:
  - agreement
  - drafting
  - regulatory
---

# HIPAA Business Associate Agreement (BAA)

Produce a HIPAA/HITECH-compliant BAA tailored to the services, PHI flow, and risk profile.

## Prerequisites

1. Party identities, entity types, jurisdictions, and notice addresses.
2. Underlying services agreement/SOW and a plain-language description of services.
3. PHI data map: categories of PHI, ePHI vs paper, systems, storage locations, data flows.
4. Known regulatory overlays (state privacy, breach laws, 42 CFR Part 2, VA/military records).
5. Security posture snapshot: safeguards, risk assessment cadence, incident contacts.
6. Negotiated risk allocation: indemnity, insurance limits, liability caps (if any).
7. Preferred timelines: breach notice, cure periods, termination notice.

## Output Structure / Process

Use this section order and fill placeholders with matter facts.

```text
1. Parties, Effective Date, Recitals (basis for BA relationship)
2. Definitions (HIPAA terms + agreement-specific)
3. Permitted Uses/Disclosures; Prohibited Uses
4. Safeguards (Privacy + Security Rule)
5. Breach/Incident Notification
6. Subcontractors/Downstream Flow-Downs
7. Individual Rights Support
8. Government Access/Compliance Cooperation
9. Term/Termination; Return/Destruction of PHI
10. Indemnity/Insurance; Liability Allocation
11. Miscellaneous (amendment, governing law, notices, assignment, severability, survival)
12. Signatures; Exhibits (implementation checklist)
```

**Definitions checklist (include all that apply)**

| Term | Source/Notes |
| --- | --- |
| Protected Health Information (PHI) | 45 CFR 160.103 [VERIFY] |
| Electronic PHI (ePHI) | 45 CFR 160.103 [VERIFY] |
| Breach | 45 CFR 164.402 [VERIFY] |
| Security Incident | 45 CFR 164.304 [VERIFY] |
| Unsecured PHI | HHS Guidance/NIST references [VERIFY] |
| Designated Record Set | 45 CFR 164.501 [VERIFY] |
| Required by Law, Individual, Secretary, Subcontractor, Use, Disclosure | HIPAA definitions [VERIFY] |

**Required BAA clauses (minimums)**

- [ ] Permit/limit uses and disclosures to services + required by law.
- [ ] Prohibit uses/disclosures that would violate Privacy Rule if done by covered entity.
- [ ] Require safeguards: Privacy Rule + Security Rule (45 CFR 164.308/310/312) [VERIFY].
- [ ] Require breach notification and security incident reporting.
- [ ] Flow-down to subcontractors (same restrictions/conditions).
- [ ] Make PHI available for access/amendment/accounting support.
- [ ] Make records available to HHS Secretary for compliance review.
- [ ] Provide return/destruction or extension of protections if infeasible.
- [ ] Termination for material breach.

**Permitted/Prohibited Uses table**

| Topic | Required Drafting |
| --- | --- |
| Core permitted uses | Tie each to a service obligation; include data aggregation if applicable. |
| Management/admin uses | Allow only if required by law or recipient assurances (confidentiality, limited use). |
| Required by law | Permit with notice to covered entity where allowed. |
| Minimum necessary | Require policies; define exceptions (treatment, disclosures to covered entity). |
| Prohibited uses | No sale of PHI; no marketing without authorization; no psychotherapy notes unless authorized. |

**Safeguards checklist**

- [ ] Admin: security official, access management, workforce training, incident response, contingency plan.
- [ ] Physical: facility access controls, workstation use/security, device/media disposal.
- [ ] Technical: unique IDs, emergency access, auto-logoff, encryption, audit controls, integrity controls, authentication, transmission security.
- [ ] Risk analysis documented and updated; remediation tracked.

**Breach/Incident notice (choose timelines and content)**

| Element | Include |
| --- | --- |
| Deadline | “Without unreasonable delay,” cap in days (e.g., 10 business days). |
| Discovery standard | Knowledge or would have known with reasonable diligence. |
| Content | Dates, description, PHI types, affected individuals count, mitigation steps, contact info. |
| Supplemental updates | Required as new facts emerge. |
| Incident logs | Maintain and provide periodic summaries of non-breach incidents. |

**Individual rights support**

| Right | Business Associate обязанность |
| --- | --- |
| Access | Provide DRS data within X days for 45 CFR 164.524 [VERIFY]. |
| Amendment | Implement amendments within X days; flow-down to subcontractors. |
| Accounting | Maintain disclosure logs for 45 CFR 164.528 [VERIFY]. |
| Restrictions/confidential comms | Implement covered entity instructions. |

**Subcontractors**

- [ ] Prior written approval required (if negotiated).
- [ ] Written BAA-equivalent flow-down with same restrictions.
- [ ] Ongoing monitoring/audit rights and prompt notice of issues.

**Termination / PHI disposition**

- [ ] Term tied to services but survives until PHI returned/destroyed.
- [ ] Cure period and immediate termination triggers for material breach.
- [ ] Return/destroy within X days; certification of destruction.
- [ ] If infeasible: extend protections, limit uses/disclosures.

**Exhibit: Implementation checklist**

- [ ] Contact points and escalation path.
- [ ] Security program baseline and audit cadence.
- [ ] Subcontractor list and approvals.
- [ ] Incident response tabletop schedule.

## Guidelines

- Match obligations to actual operational capability; do not promise controls the BA cannot meet.
- Align with underlying services agreement; reconcile conflicting terms.
- Add state-law and special-category overlays when applicable; use the most protective rule.
- Use defined terms consistently; avoid ambiguity in permitted uses.
- Mark any uncertain legal citations with `[VERIFY]`.
- If HIPAA rules change post-execution, include amendment mechanism and timeline.
