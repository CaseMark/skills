---
name: advance-health-care-directive
description: >
  Drafts jurisdiction-specific Advance Health Care Directive packages including
  health care agent appointment, living will instructions, HIPAA authorization
  bridge, organ donation preferences, and execution compliance checklists. Use
  this skill when the user mentions advance directive, health care directive,
  healthcare proxy, living will, health care agent appointment, HIPAA
  authorization, capacity trigger planning, medical power of attorney, end-of-life
  planning, or execution formalities for healthcare documents. Also trigger when
  the user references state-specific directive forms, witness or notary
  requirements for healthcare documents, or asks about portability of directives
  across states.
tags:
  - agreement
  - drafting
  - transactional
---

# Advance Health Care Directive

## Why This Skill Exists

Advance Health Care Directives fail in practice for two reasons: they don't comply with state-specific execution formalities (making them unenforceable when it matters most), or they use vague language that leaves clinicians and agents unable to act in an emergency. A directive that says "no heroic measures" is clinically useless. A directive signed with one witness in a state requiring two is legally void.

This skill produces a jurisdiction-aware, clinically actionable directive package — agent appointment, treatment instructions, HIPAA bridge, execution checklist — that an ER team can parse in under 60 seconds and that survives legal challenge. The primary grounding is state probate/health codes governing advance directives, with HIPAA (45 C.F.R. § 164.508) overlay for authorization language.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft." Gather:

1. **Jurisdiction** — client's primary state of residence plus expected care states; whether out-of-state portability is needed
2. **Draft scope** — directive + health care agent + living wishes + revocation + execution clauses; confirm attorney review required before finalization
3. **Capacity context** — any contested capacity concerns; if present, flag for contemporaneous capacity memo
4. **Client identity** — legal name, DOB, aliases, contact data, diagnosis context relevant to decision-making
5. **Agent architecture** — primary agent and alternates with full contact details, availability, conflicts, and consent to serve
6. **Treatment preferences** — CPR, ventilation, feeding/hydration, hospitalization goals, comfort care, palliative sedation position, religious/cultural restrictions
7. **Existing documents** — prior directives, POLST/MOLST, donor registry status, powers of attorney, guardianship/adult protective orders
8. **Execution logistics** — signing location, notary availability, witness constraints, facility-specific rules, spouse/relative witness limitations
9. **Conflict screening** — family tensions, beneficiary pressure, undue influence indicators flagged to attorney

**If the user doesn't respond**, apply and clearly label these defaults: immediate-authority directive; primary agent with one alternate; comfort-focused treatment preferences; forum-neutral directive template with state-specific execution formalities and statutory form references marked `[VERIFY JURISDICTION]`; standard HIPAA authorization bridge.

### Documents to Request

Request these materials — they substantially improve quality:

- Prior advance directives, living wills, or health care proxies
- POLST/MOLST forms (if any)
- Powers of attorney (financial and healthcare)
- Guardianship or conservatorship orders
- Organ donation registrations
- Relevant medical records establishing diagnosis context

If materials are missing, flag them explicitly. Proceed with labeled assumptions rather than stalling, but list "Open Items / Needed Inputs" for attorney follow-up.

---

## Step 1: Validate Intake and Map State Law

Before drafting any text, build the jurisdictional scaffold.

### Required Deliverable: Intake Validation Table

| Data Block | Required Fields | Verification |
|---|---|---|
| Client profile | Name, DOB, aliases, state residence, contact | Confirm spelling consistency across all blocks |
| Jurisdiction | Primary state, secondary care state(s), portability strategy | `[VERIFY]` all execution/effectiveness rules per state statute |
| Capacity posture | Capacity red flags, physician assessment needs | Flag for contemporaneous memo when risk is present |
| Agent chain | Primary + up to two alternates, relationships, contact, disqualifications | Confirm no disqualified classes under local statute |
| Treatment values | Scenario-based preferences, values hierarchy, palliative care directives | Ensure no contradictory instructions |
| Legal/medical interfaces | POLST/MOLST status, donor registry, prior directives | Reconcile conflicts and provide harmonized set |
| Execution logistics | Witness sources, notary method, facility constraints | Include jurisdiction-specific affidavit/attestation language |
| Delivery plan | Copy recipients (agent, PCP, facilities, portal) | Include immediate distribution checklist |

### Required Deliverable: State-Law Scaffold

| Topic | Required Confirmation |
|---|---|
| Governing statute/framework | Controlling statute and official form/guidance URL |
| Formalities | Witness vs. notary options, number, disqualifications, facility-specific add-ons |
| Trigger mechanics | Springing vs. immediate authority; incapacity standard and certifying clinician count |
| Substantive scope | Definitions (terminal, incurable, persistent unconsciousness) if used |
| Limitations | Pregnancy restrictions, mental health treatment authority, substance/HIV record limits |
| Revocation | Permitted methods and effective timing |
| Provider protection | Reliance rights for copies/electronic versions and good-faith immunity |

---

## Step 2: Draft the Directive Sections

Use a fixed section order. Each section must use clinically interpretable language — no vague slogans.

### Fixed Section Order

1. **Purpose statement** and chosen effective date
2. **Health care agent appointment** — clear trigger and scope
3. **Successor agent ladder** — strict availability/unavailability conditions
4. **Written values statement** and decision-making hierarchy
5. **Treatment instruction matrix** — scenario-based, not abstract
6. **HIPAA authorization bridge** — effective immediately unless state requires otherwise
7. **Organ donation / disposition-of-remains** notes
8. **Revocation, supersession, and severability**
9. **Provider reliance and transfer obligations** (if conscience objection possible)
10. **Execution block** — signature/witness/notary/acceptance

### Section Templates

**Agent Appointment:**
```text
[CLIENT NAME], [CLIENT ADDRESS]
I appoint [PRIMARY AGENT NAME], [RELATIONSHIP], as my Health Care Agent.
Contact: [ADDRESS] | [PHONE] | [EMAIL]
Authority starts when [trigger condition], as determined by [clinician criteria per state law].
Agent authority includes: treatment consent/denial, admission/discharge, care-site transfer,
treatment preferences execution, and record-access coordination.
If written instruction conflicts with discretionary choice, written instruction controls.
If unspecified, Agent applies my stated values and substituted-judgment standard.
```

**Successor Agents:**
```text
If my Primary Agent is unavailable/unwilling/disqualified, I appoint:
First Alternate: [NAME/CONTACT]
Second Alternate: [NAME/CONTACT]
Each assumes authority only if all prior agents are unavailable per state rules.
```

**HIPAA Authorization Bridge:**
```text
I authorize my Health Care Agent and alternates to access and exchange all medical records
and protected health information now, regardless of trigger status, for purposes of
determining incapacity and coordinating care.
Effective date: immediate upon execution.
Scope includes records from all treating providers, facilities, laboratories, and insurers.
[VERIFY: 45 C.F.R. § 164.508 requirements and any state/Part 2 overlays.]
```

**Treatment Preferences:**
```text
My goals:
1) Comfort and pain control.
2) Maintain communication/contact with loved ones when feasible.
3) Avoid prolonged treatment with no reasonable benefit.
Treatment preferences:
- CPR: [Yes/No; include context]
- Ventilation: [Yes/No; include limits]
- Artificial nutrition/hydration: [Yes/No; include context]
- Hospitalization: [Preference]
- Comfort care: [Include explicit palliative care and symptom-control direction]
If not specified, apply my values and best judgment as if I could decide for myself.
```

**Revocation and Severability:**
```text
I may revoke at any time while capable, by [state-authorized methods].
Latest signed/revised version governs.
If one provision is unenforceable, all other provisions remain effective.
Copies and electronic versions may be used as permitted by [STATE] law.
```

---

## Step 3: Execute Compliance Verification

### Required Deliverable: Execution Compliance Checklist

| Item | Required Output |
|---|---|
| Witnessing | Correct count and disqualification screening completed |
| Notary | Form and statement match state-prescribed language if used |
| Facility patients | Facility-specific add-on clauses satisfied (e.g., ombudsman/patient advocate) |
| Agent acceptance | Optional acceptance statement included |
| Plain-language usability | Agent and key instructions identifiable in <60 seconds in an ER context |
| Internal consistency | No contradiction between agent powers and treatment instructions |
| Review tags | Every statutory claim marked `[VERIFY]` unless confirmed by statute URL |

### State-Specific Flags

- Use state templates/forms where required or strongly recommended
- Example variances to flag for attorney review: California facility witness/ombudsman rules, Florida witness composition, New York split-instrument systems (proxy + living will), Texas hospital review process for withdrawal over family objections
- Pregnancy limitations and mental-health treatment authority are state-sensitive and potentially unstable across case law updates
- Use `[VERIFY]` tags for any citation or statutory quote unless sourced in-session

---

## Step 4: Produce Final Package

Output the complete directive with mandatory front matter.

### Mandatory Front Matter

At the very top of every output, before any substantive content, include:

1. **Assumptions Used** — jurisdiction, trigger type, agent chain, treatment posture, key facts relied on
2. **Open Items / Needed Inputs** — missing documents, unresolved jurisdictional questions, unverified citations

### Deliverable Package

1. Complete advance health care directive document
2. Execution compliance checklist (filled)
3. Distribution plan with recipient list
4. State-specific notes and `[VERIFY]` items for attorney review

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the initial package, ask:

1. Does the agent chain and trigger mechanism match the client's intent?
2. Are the treatment preferences correctly stated — especially CPR, ventilation, and feeding/hydration positions?
3. Are there any family members or situations that need special handling in the values statement?
4. Should the directive be harmonized with an existing or new POLST/MOLST?

If the user doesn't answer, recommend the next best refinement based on stated objectives and proceed if authorized.

---

## Quality Audit

Before finalizing, verify:

- [ ] Jurisdiction identified and state-law scaffold completed
- [ ] Agent chain includes primary + at least one alternate with full contact info
- [ ] Treatment preferences are scenario-specific, not abstract ("no heroic measures" eliminated)
- [ ] HIPAA authorization bridge included and effective date confirmed
- [ ] No contradiction between agent powers and treatment instructions
- [ ] Execution formalities match state requirements (witness count, disqualifications, notary)
- [ ] Portability addressed if client receives care in multiple states
- [ ] Every statutory citation verified or marked `[VERIFY]`
- [ ] Assumptions and open items listed prominently in front matter
- [ ] Plain-language usability: key instructions locatable in <60 seconds
- [ ] No invented facts, diagnoses, relationships, or statutory language

---

## Guidelines

- Do not rely on memory for any state execution formalities or statutory language — require statute URLs or official guidance
- Flag unresolved jurisdictional questions with `[VERIFY]` and do not finalize text as final legal language
- Use scenario-specific, clinically interpretable wording; avoid vague slogans like "no heroic measures"
- Enforce values hierarchy: client instructions override broad surrogate discretion
- Treat portability as a design requirement, not a footnote
- Do not advise on clinical decisions — this is legal structuring only
- Do not produce unverified legal authority text; refuse fraud/backdating/fabrication requests
- **Attorney review required** — include disclaimer and execution-readiness statement in final output
- **Ethics**: Model Rules 1.1 (competence), 1.14 (diminished capacity), 1.6 (confidentiality)
