---
name: hipaa-release-authorization
description: >-
  Drafts U.S. HIPAA-compliant PHI release authorizations for estate-planning
  workflows, enabling designated healthcare agents or representatives to
  access a patient’s medical information. Use for drafting release forms,
  healthcare POA support documents, and record-access instruments. Trigger
  keywords: HIPAA release, PHI authorization, estate planning, healthcare
  agent, healthcare power of attorney, advance directive support. Enforces 45
  CFR §164.508 core authorization elements, scope of disclosure controls,
  revocation statement, notice language, and execution requirements.
tags:
  - agreement
  - drafting
  - regulatory
  - transactional
---

# HIPAA Release Authorization Form

Drafts an estate-planning-oriented HIPAA authorization form that permits selected recipients to access specified protected health information from covered entities.

## Prerequisites

1. Jurisdiction (state) identified for signature/agent-execution formalities.
2. Patient/authorizing individual data: legal name, DOB, and contact details.
3. Defined recipients: healthcare agent, successor agent(s), and any additional representatives.
4. Defined disclosing parties: providers, hospitals, labs, pharmacies, health plans, and entities likely to possess PHI.
5. PHI scope decision: all records vs. limited categories.
6. Disclosure purpose and duration (expiration date/event) confirmed.
7. Representative authority verification when client lacks capacity (POA, guardian order, court appointment docs).
8. Prior estate-planning documents uploaded for consistency (e.g., healthcare proxy, advance directive language references).

## Output Structure / Process

### Required sections checklist

| Section | Inputs required | Compliance target |
|---|---|---|
| Title + declaration | Form purpose and legal basis | Clear, single-purpose authorization |
| Patient authorization statement | Identity + capacity check | Voluntary, specific written consent |
| Authorized recipients | Agent names, roles, relationships | Precise, no ambiguous recipients |
| Disclosing entities | Covered entities/record holders | Broad only when intended |
| PHI scope | Records/categories requested | Include exclusions if any |
| Purpose | Decision-making function and use case | Specific estate-planning healthcare purpose |
| Expiration/termination | End date, event, or condition | Must be explicit |
| HIPAA disclosures/limits | Re-disclosure, treatment non-conditioning | Required notices |
| Revocation | How/where written revocation is sent | Clear patient rights statement |
| Execution block | Signatures, printed names, dates | Patient-first, then representative if needed |
| Optional witness/notary block | State-law requirements | Add only where applicable [VERIFY] |
| Footer counsel note | Review/disclaimer | Optional but recommended |

### Draft template

```markdown
AUTHORIZATION FOR RELEASE OF PROTECTED HEALTH INFORMATION
Pursuant to 45 CFR §164.508

1) Authorizing Individual (Patient)
- Name:
- Date of Birth:
- Address:
- Phone/Email:

2) Authorization
I authorize the use and disclosure of my protected health information (PHI) as described below.

3) Person(s) authorized to disclose PHI (Disclosers)
- [Covered entity or healthcare facility 1]
- [Covered entity or healthcare facility 2]

4) Person(s) authorized to receive PHI (Recipients)
- [Agent Name], designated Healthcare Agent
- [Successor Agent Name], designated Successor Healthcare Agent
- [Other Representative/Attorney/Family Member, if any]

5) PHI to be disclosed
- [ ] All PHI
- [ ] Limited to: [Specify medical record categories]
- [ ] Sensitive categories if included: [substance use, mental health, genetic, HIV/AIDS, etc.] [VERIFY]

6) Purpose of disclosure
To permit recipients to obtain, discuss, review, and rely on my PHI for healthcare decision-making under my healthcare directives and/or healthcare power of attorney.

7) Duration
This authorization is effective upon execution and remains effective until:  
- [ ] A stated date: [__] or  
- [ ] Revocation by me in writing, or  
- [ ] Death, whichever occurs first.

8) Patient rights / required statements
- I may revoke this authorization at any time with written notice to the entity that possesses the records.
- Revocation applies prospectively to future uses/disclosures by covered entities after notice.
- PHI disclosed under this authorization may be re-disclosed and may lose some HIPAA protection.
- I understand I may refuse to sign this authorization and this refusal cannot be used against me.
- Treatment or services will not be conditioned on signing unless required by law.
- I have the right to receive a signed copy.

9) Execution
Patient Signature: ____________________  Date: _______
Printed Name: ________________________

If signed by representative:
Representative Name: ______________  Signature: __________  Date: _______
Authority/Relationship: _______________  Document: _______________

Witness/Notary (if required by state law): ____________________________________________________ [VERIFY]
```

### Final generation rules

1. Always render all bracketed placeholders visibly.
2. Prefer complete clauses over undefined references.
3. Keep medical categories explicit; do not mix “all records” and narrow categories.
4. Validate for internal consistency (recipient appears in same section, same spelling throughout).
5. Add state-specific addendum blocks only when confirmed for target jurisdiction.

## Guidelines

- Do not authorize disclosures broader than needed unless client requests full-record access.
- Do not omit the identity of recipients or disclosers.
- Do not include blank signature authority fields for representative execution.
- Include written revocation mechanism and contact target in the revocation paragraph.
- Never represent federal law as exclusive when state mandates may override form requirements [VERIFY].
- Include attorney review language in cover memo if template will be client-facing.
- Estate planning variants should align with the governing healthcare POA terminology and naming in the core delegation document [VERIFY].
