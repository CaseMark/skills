---
name: psychiatric-advance-directive
description: Drafts Psychiatric Advance Directives (PADs) / Mental Health Advance Directives — jurisdiction-specific legal instruments capturing a principal's psychiatric treatment instructions and agent authority for use during future incapacity crises. Covers capacity attestation, mental health agent appointment with HIPAA authorization, psychotropic medication preferences (preferred/conditional/refused), ECT consent, Ulysses Clause, crisis activation, and involuntary treatment acknowledgment. Embeds Model Rule 1.14 guardrails and anti-hallucination constraints on statutory citations. Use when drafting PADs, mental health powers of attorney, mental health treatment declarations, or psychiatric crisis planning documents.
tags:
  - agreement
  - drafting
  - regulatory
  - transactional
---

# Psychiatric Advance Directive (PAD)

Drafts a clinically actionable, legally durable Psychiatric Advance Directive translating the principal's psychiatric history and values into instructions for mental health treatment during future incapacity.

## Prerequisites

1. **Jurisdiction** — required before drafting; enforceability, execution formalities, and Ulysses Clause availability are jurisdiction-specific. For multi-jurisdiction use, flag portability limits.
2. **Clinical history** — diagnoses (if client consents to include), prior hospitalizations (facilities, dates, involuntary holds), current medications, known allergies/adverse reactions (e.g., dystonia, NMS, metabolic effects), prior effective medications.
3. **Agent designation** — full legal name, address, phone, email, relationship, and willingness to serve for primary agent and at least one alternate. Identify any statutory default surrogates whose priority may conflict with the chosen agent.
4. **Individuals to exclude** — any person to be blocked from agent role or information access (protective orders, no-contact orders, restraining orders).
5. **Treatment preferences** — stance on ECT, seclusion/restraint, specific psychotropic drug classes, preferred de-escalation techniques, voluntary vs. involuntary admission, peer respite, law enforcement involvement.
6. **Crisis activation details** — early warning signs, sensory/trauma triggers, preferred first contacts.
7. **Existing documents** — general AHCD, health care proxy, guardianship/conservatorship orders, or prior PAD to coordinate or supersede.
8. **Execution logistics** — notary access, witness availability, statutory disinterest requirements, agent acceptance signature requirement.

If jurisdiction, agent identity, or treatment preferences are missing, pause and request before generating a final draft. Alternatively, produce a draft marked **NOT EXECUTION-READY — REQUIRES JURISDICTIONAL FORMALITIES REVIEW**.

## Output Structure

### Document Architecture

| Section | Content |
|---|---|
| Title & Purpose | "Psychiatric Advance Directive and Appointment of Mental Health Agent"; plain-language purpose for clinicians; conflict-of-directives priority clause |
| Capacity Affirmation | Principal's contemporaneous statement of understanding and voluntariness; optional clinician attestation block (recommended when client has frequent crises) |
| Agent Appointment | Primary + alternate agents with 24/7 contact info; authority clause tied to statutory incapacity standard; priority statement over default surrogates; HIPAA authorization |
| Exclusions | Named individuals prohibited from agent role or information access |
| Treatment Preferences | Medications, ECT, hospitalization, de-escalation (see detail below) |
| Ulysses Clause | If jurisdiction allows: non-revocation during incapacity (verify before including) |
| Revocation & Updates | Standard revocation rights; annual review request; supersession of prior PADs with date |
| Crisis Activation | Early warning signs; contact ladder (≤2 contacts for emergency realism); what helps client accept care |
| Override Protocol | What facility must do if it cannot follow the PAD |
| Execution Blocks | Principal, witnesses (×2), notary (if required), agent acceptance (if required) |
| Distribution Log | Agent, alternates, treating providers, hospital systems, patient portals, state advance directive registry |

### First-Page Summary ("If You Only Read One Page")

Place at top of document — intake staff must locate key info in under 2 minutes:
- Agent name + 24/7 phone number
- Top 3 crisis triggers / early warning signs
- Top 3 treatment preferences (including any critical refusals)

### Treatment Preferences — Medication Structure

Draft in three labeled categories:

```
PREFERRED (first-line, if clinically appropriate):
  [Drug name] — reason: [prior efficacy, tolerability, titration notes]

CONDITIONAL (only under stated circumstances):
  [Drug name] — when: [e.g., short-term PRN for agitation; last resort only]

REFUSED (with reasons):
  [Drug name] — reason: [e.g., prior kidney toxicity; severe extrapyramidal symptoms on ~[date]]
  Acceptable alternative: [Drug name]
```

*Rationale for refusals reduces best-interests override risk. Always pair each refusal with an acceptable alternative.*

### ECT Language Template

```
Electroconvulsive Therapy (ECT):
☐ I consent
☐ I do not consent
☐ I consent only if: [conditions, e.g., max treatments, specific facility]

I understand legal requirements for ECT may vary by jurisdiction. I request my
Agent and treating psychiatrist review applicable law and clinical indications
at the time of any proposed ECT.
```

### De-escalation & Environment Template

```
I calm more quickly when staff: [specific behaviors, e.g., speak slowly, explain
each step before touching, allow quiet space].

If I am [specific behavior], please offer [specific accommodation] before
considering restraint. If restraint is required, please attempt [alternatives]
first unless there is immediate danger to myself or others.

Trauma considerations: [specific triggers, e.g., male staff for certain holds;
specific sensory stimuli].
```

### Override Protocol Template

```
If providers cannot follow a preference in this PAD due to an emergency, legal
requirement, or unavailability, I request they:
(a) use the least restrictive alternative consistent with safety;
(b) document the reason for deviation from this PAD;
(c) notify my Agent as soon as practicable;
(d) review this PAD again once I am stabilized.
```

### HIPAA Authorization Language

```
I authorize my providers to disclose to my Agent information necessary to carry
out this PAD — including diagnoses, medications, treatment plans, and discharge
planning — to the extent permitted by law. If a separate written authorization
is required, I intend this PAD to serve as that authorization to the maximum
extent allowed, and I authorize completion of any additional forms needed.
```

*Note: Standalone HIPAA-compliant authorization (45 CFR § 164.502 [VERIFY]) may be required — verify by jurisdiction. State mental health confidentiality laws often impose higher protections than federal baseline.*

### Ulysses Clause (verify jurisdiction first)

```
I intend for this PAD to remain in effect even if I attempt to revoke it during
a period of incapacity, to the fullest extent permitted by applicable law.
I have discussed the meaning and effect of this provision with my attorney.
```

⚠️ **Do not include if jurisdiction does not recognize non-revocable PADs.** Including in a non-recognizing jurisdiction risks the document being viewed as coercive or legally defective. If jurisdiction is unclear, flag for attorney verification and omit.

### Jurisdiction-Specific Frameworks [VERIFY all citations before finalizing]

| State | Framework | Key Notes |
|---|---|---|
| North Carolina | N.C. Gen. Stat. § 122C-71 et seq. [VERIFY] | Specific statutory form; significant deviation may cause rejection at state-run facilities |
| Texas | Tex. Civ. Prac. & Rem. Code Ch. 137 [VERIFY] | "Declaration for Mental Health Treatment"; expires 3 years unless different term specified |
| California | Probate Code § 4701 [VERIFY] | General AHCD framework; mental-health-specific provisions commonly appended by practitioners |
| Virginia | Va. Code § 54.1-2981 et seq. [VERIFY] | Robust PAD laws; agent may overrule principal's contemporaneous protest if PAD explicitly authorizes |

For jurisdictions **without explicit PAD statutes**: title as "Mental Health Treatment Preferences and Appointment of Health Care Representative for Psychiatric Decisions"; recommend executing a parallel general durable HCPOA.

For **multi-jurisdiction use**: draft portable preferences and proxy authority; execute state-specific signature pages where needed; warn client that enforceability varies and state-specific forms should be considered where client lives or regularly receives care.

## Guidelines

**Ethics & Professional Responsibility**

| Rule | Application |
|---|---|
| MR 1.14 | If client appears incapacitated at execution, stop — document may not be executable; protective action may be warranted |
| MR 1.1 / 1.4 | Research controlling PAD statute; counsel client that emergency and involuntary treatment statutes may override preferences — do not let the PAD create false expectations |
| MR 1.6 | Discuss whether to omit formal diagnoses in favor of functional descriptions and medication history, given wide distribution to facilities and providers |
| MR 1.7 / 1.8 | Flag conflicts when proposed agent is paid caregiver, estranged spouse, or financially interested; require alternates and safeguards in those cases |
| PSDA | Federal facilities (Medicare/Medicaid) must inform patients of PAD rights — supports recognition infrastructure, but implementation is state-dependent |

**Anti-Hallucination Protocol**

- Every statutory citation, case name, and enforceability claim must be verified via official state code databases before inclusion
- Mark unverified citations `[VERIFY]`; do not fabricate section numbers or case names
- Do not assert "this PAD is legally binding" without jurisdiction-specific verification
- *Sell v. United States*, 539 U.S. 166 (2003) [VERIFY] — establishes constitutional limits on forced medication in criminal competency context; informs liberty interest underlying civil PAD refusals but does not directly govern PAD enforceability

**Execution & Distribution Checklist**

- [ ] Witnesses: typically 2 disinterested adults — verify statutory exclusions (not the agent, not treating facility staff, not financial beneficiaries)
- [ ] Notarization: jurisdiction-specific — verify requirement
- [ ] Agent acceptance signature: jurisdiction-specific — verify requirement
- [ ] Copies provided to: agent, alternates, treating psychiatrist, therapist, case manager, preferred hospital systems, patient portals
- [ ] Check whether jurisdiction maintains an electronic advance directive registry
- [ ] Advise client to carry a wallet crisis card referencing PAD existence and location
- [ ] Date every signature; include supersession clause for all prior PADs
- [ ] Recommend annual reaffirmation or review after any psychiatric hospitalization

**Clinical Usability**

- Replace aspirational language ("treat me with dignity") with concrete operational instructions
- Write override protocol in cooperative, clinically literate tone — defensive institutional interpretation is a real risk
- Keep individual preference rationales to 1–2 sentences
- Do not include demands that are operationally impossible (non-existent facility, unavailable medication, "no security involvement under any circumstances") — convert to preferences with ranked alternatives

**Final Output Must Include**

> *DRAFT FOR ATTORNEY REVIEW ONLY — Not legal advice. Not execution-ready without jurisdiction-specific verification of statutory formalities, citations, and Ulysses Clause availability.*
