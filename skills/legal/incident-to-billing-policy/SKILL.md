---
name: incident-to-billing-policy
description: Drafts a Medicare incident-to billing compliance policy for healthcare practices. Covers eligibility criteria, direct supervision requirements, documentation standards, audit trail systems, and False Claims Act risk mitigation. Grounded in Medicare Benefit Policy Manual Chapter 15 §60.1, 42 CFR 410.26, and 42 U.S.C. §1395x(s)(2)(A). Use when creating or updating incident-to billing policies, responding to OIG scrutiny, or establishing compliance programs for non-physician practitioner billing under physician supervision.
tags:
  - drafting
  - memo
  - regulatory
---

# Incident-To Billing Policy

Drafts a regulatory compliance policy governing Medicare incident-to billing for non-physician practitioner services rendered under physician supervision.

## Prerequisites

1. **Practice profile** — specialties, office locations, states of operation
2. **Provider roster** — physicians (supervising), NPPs (NPs, PAs, CNSs, etc.) with license/credential details
3. **Existing documentation** — current billing policies, EHR workflow descriptions, any prior audit findings
4. **State scope-of-practice summary** — for each state where practice operates (incident-to doesn't preempt stricter state rules)
5. **Payer mix context** — Medicare only, or also Medicaid/commercial (policy scope may expand accordingly)

## Output Structure

### 1. Policy Header & Purpose
| Field | Content |
|---|---|
| Effective Date | [DATE] |
| Review Cycle | Annual minimum; triggered by regulatory changes or audit findings |
| Scope | All clinical and billing staff involved in NPP service billing |
| Authority | Medicare Benefit Policy Manual Ch. 15 §60.1; 42 CFR 410.26; 42 U.S.C. §1395x(s)(2)(A) |

Purpose statement must establish: incident-to is a billing privilege with strict conditions; improper use creates FCA liability, CMPs, and program exclusion risk.

---

### 2. Definitions
| Term | Definition |
|---|---|
| Incident-To Billing | Billing NPP services under the supervising physician's NPI at the physician reimbursement rate |
| Direct Supervision | Physician physically present in the office suite, immediately available — not in the same room, but not reachable only by phone/telemedicine |
| NPP | Non-physician practitioner: NP, PA, CNS, CNM, or other qualified professional per Medicare definition |
| Initial Service | First physician evaluation of a condition establishing the diagnosis and treatment plan |
| Course of Treatment | Ongoing management of a condition for which the physician established the treatment plan |

---

### 3. Eligibility Criteria (All Must Be Met)

- [ ] Physician personally performed the **initial service** for the condition being treated
- [ ] Physician established and documented a **treatment plan**
- [ ] Physician remains **actively involved** in ongoing management
- [ ] Service is a **follow-up** to the established plan — not a new problem, new condition, or new diagnosis
- [ ] Supervising physician is **physically present in the office suite** during the NPP service
- [ ] Physician is **immediately available** (not in surgery, off-site, or otherwise unable to respond)
- [ ] NPP is a **W-2 employee or contractor** of the practice (not independently contracted without supervision structure)
- [ ] Service is of a type **commonly furnished in a physician office** and integral to the physician's professional service
- [ ] State scope-of-practice law **does not impose stricter requirements** that would preclude this arrangement

**Disqualifying scenarios** (must bill under NPP's own NPI):
- First visit for any condition, new or established patient
- Patient presents with a new complaint not covered by existing treatment plan
- Supervising physician is off-site, on call by phone only, or in a procedure room unable to respond
- Service type excluded from incident-to coverage (e.g., certain preventive services, DME)

---

### 4. Operational Procedures

**Scheduling:**
- Flag appointments to determine likely billing path before the visit
- Confirm supervising physician is scheduled and physically present on that date/location
- Use decision flowchart: *Is there a physician-established treatment plan for this condition?* → *Will physician be on-site?* → *Is it a follow-up (not new problem)?*

**Day-of Supervision:**
- Physician signs daily supervision attestation log (name, date, location, hours present)
- Log retained with billing records, not just in medical record

**Clinical Documentation (required in each incident-to encounter note):**
- Reference to physician's original treatment plan (date, diagnosis, plan elements)
- Services rendered are consistent with established plan
- Name of supervising physician on duty
- Confirmation supervising physician was present in suite
- Any consultation or assistance obtained from supervising physician during visit

**Billing Handoff:**
- Billing staff verify supervision log before submitting under physician NPI
- EHR/PM system flags for review: physician not scheduled that day; new diagnosis code; NPP not credentialed for incident-to

---

### 5. Documentation & Retention

| Document | Retention Period | Format |
|---|---|---|
| Physician initial evaluation note | 10 years from service or final payment (whichever later) | EHR/paper |
| NPP follow-up notes | Same | EHR/paper |
| Daily supervision attestation logs | Same | Paper or EHR |
| Provider schedules (location-specific) | Same | HR/scheduling system |
| Billing records and claim data | Same | PM system |
| Training completion records | Duration of employment + 6 years | HR system |

All records must be retrievable within 48 hours of an audit request.

---

### 6. Compliance & Risk Framework

**Governing authorities:**
- 42 U.S.C. §1395x(s)(2)(A) — Medicare statutory basis
- 42 CFR 410.26 — implementing regulations
- Medicare Benefit Policy Manual, Ch. 15, §60.1 — primary operational guidance
- Medicare Claims Processing Manual, Ch. 12 — billing instructions
- False Claims Act, 31 U.S.C. §§3729–3733 — liability for knowingly false claims
- Civil Monetary Penalties Law, 42 U.S.C. §1320a-7a — penalties without specific fraud intent required

**Enforcement exposure:**
- OIG has flagged incident-to billing in multiple Work Plans as a high-risk area
- RAC contractors conduct pre- and post-payment reviews targeting supervision documentation gaps
- Overpayment recovery + interest; CMPs up to $13,000+ per claim [VERIFY current amount]; potential exclusion

**Internal audit program:**
- Quarterly sample review: minimum 10 incident-to claims per NPP per quarter
- Review checklist: supervision documented? treatment plan pre-existed? new problem present? NPP credentialed?
- Compare NPP incident-to billing ratio against specialty benchmarks; investigate outliers

**Error correction:**
- Isolated errors → education, repayment, documentation remediation
- Systemic errors → comprehensive corrective action plan, consider voluntary disclosure
- Voluntary Self-Disclosure Protocol (OIG SDRP) — consult compliance counsel when pattern identified

---

### 7. Training Requirements

| Audience | Initial Training | Refresher |
|---|---|---|
| Physicians | Before supervising incident-to services | Annual + upon policy update |
| NPPs | Before billing incident-to | Annual + upon policy update |
| Clinical staff | Within 30 days of hire | Annual |
| Billing/coding staff | Within 30 days of hire | Annual + upon regulatory changes |

Training must cover: eligibility criteria, direct supervision definition, documentation requirements, consequences of non-compliance.

---

### 8. Governance

| Role | Responsibility |
|---|---|
| Compliance Officer | Policy ownership, audit oversight, regulatory monitoring, voluntary disclosure decisions |
| Medical Director | Clinical guidance on supervision structures, treatment plan standards |
| Billing Director | Claims submission controls, EHR edits, denial tracking |
| Practice Administrator | Staff training coordination, record retention systems |

**Policy updates:** Compliance Officer monitors CMS manual transmittals, Federal Register, and OIG publications. Policy reviewed annually; updated within 30 days of material regulatory change. Version history maintained; prior versions archived.

---

### 9. Appendices to Include in Final Document

- **Appendix A** — Daily Physician Supervision Attestation Log (template)
- **Appendix B** — Incident-To Billing Decision Flowchart
- **Appendix C** — Pre-Submission Billing Checklist
- **Appendix D** — Internal Audit Worksheet
- **Appendix E** — State-Specific Scope-of-Practice Addendum (one page per state)

## Guidelines

- Direct supervision = physical presence in office suite; telephone and telehealth do NOT satisfy this requirement
- Incident-to does not apply in hospital outpatient departments, SNFs, or home settings under most circumstances — scope policy to office/clinic setting or explicitly address each setting
- State law controls if more restrictive than Medicare — always layer state analysis
- Do not use incident-to for new problems even in established patients; bill under NPP's NPI instead
- Mark any statutory or regulatory citations added during drafting with `[VERIFY]` if currency is uncertain
- If practice bills Medicaid or commercial payers, note that incident-to rules vary significantly and this policy covers Medicare only unless explicitly extended
