---
name: advance-health-care-directive
description: Drafts U.S. state-compliant Advance Health Care Directives (health care proxy, living will, and related execution package) into attorney-review-ready, clinically actionable documents. Use when a user requests a health care directive, healthcare agent appointment, capacity trigger planning, HIPAA authorization bridge, organ donation/disposition preference, or execution checklist before signing and distribution.
tags:
  - agreement
  - drafting
  - transactional
---

# Advance Health Care Directive

Drafts a jurisdiction-specific directive package that appoints a health care decision-maker, sets treatment preferences, addresses record-access and portability issues, and enforces execution formalities.

## Prerequisites

1. **Jurisdiction locked**: client principal state plus expected care states identified; determine whether out-of-state portability is needed.
2. **Draft scope confirmed**: directive + health care agent + living wishes + revocation + execution clauses; attorney review required before finalization.
3. **Capacity context collected**: no contested capacity assumptions; if concern exists, flag for contemporaneous capacity memo.
4. **Client identity/case data captured**: legal name, DOB, aliases, contact data, diagnosis context relevant to decision-making.
5. **Agent architecture collected**: primary agent and alternates with full contact details, availability, conflicts, and consent to serve.
6. **Treatment preference inputs captured**: CPR, ventilation, feeding/hydration, hospitalization goals, comfort care, palliative sedation position, religious/cultural restrictions.
7. **Existing documents reviewed**: prior directives, POLST/MOLST, donor registry status, powers of attorney, guardianship/adult protective orders.
8. **Execution logistics captured**: where signing occurs, notary availability, witness constraints, facility-specific rules, spouse/relative limitations.
9. **Conflict and influence screening**: family tensions, beneficiary pressure, undue influence indicators flagged to attorney.
10. **Stop-conditions**: if required legal inputs are missing, pause and request follow-up instead of drafting assumptions.

## Output Structure / Process

### 1) Intake and validation
| Data Block | Required Fields | Verification |
|---|---|---|
| Client profile | Name, DOB, aliases, state residence, contact | Confirm spelling consistency across all blocks |
| Jurisdiction | Primary state, secondary care state(s), portability strategy | [VERIFY] all execution/effectiveness rules per state statute |
| Capacity posture | Capacity red flags, physician assessment request, memory of recent delirium episodes | Counsel for contemporaneous memo when risk is present |
| Agent chain | Primary + up to two alternates, relationships, contact, disqualifications | Confirm no disqualified classes under local statute |
| Treatment values | Scenario-based preferences, values hierarchy, palliative care directives | Ensure no contradictory instructions |
| Legal/medical interfaces | POLST/MOLST status, donor registry status, prior directives | Reconcile conflicts and provide harmonized set |
| Execution logistics | Witness sources, notary method, facility constraints | Include jurisdiction-specific affidavit/attestation language |
| Delivery plan | Copy recipients (agent, PCP, facilities, portal) | Include immediate distribution checklist |

### 2) State-law scaffold (must be completed before drafting final text)
| Topic | Required confirmation |
|---|---|
| Governing statute/framework | Identify controlling statute and official form/official guidance URL |
| Formalities | Witness vs. notary options, number, disqualifications, facility-specific add-ons |
| Trigger mechanics | Springing vs immediate authority; incapacity standard and certifying clinician count |
| Substantive scope | Definitions (terminal, incurable, persistent unconsciousness, etc.) if used in instructions |
| Limitations | Pregnancy restrictions, mental health treatment authority, substance/mental-health/HIV record limits |
| Revocation | Permitted methods and effective timing |
| Provider protection | Reliance rights for copies/electronic versions and good-faith immunity |
| Criminal/self-harm-adjacent language | Palliative medication and comfort care phrasing review |

### 3) Draft section order (fixed)
1. Purpose statement and chosen effective date.
2. Health care agent appointment (clear trigger and scope).
3. Successor agent ladder with strict availability/unavailability conditions.
4. Written values statement and decision-making hierarchy.
5. Treatment instruction matrix.
6. HIPAA authorization bridge (effective immediately unless state otherwise requires).
7. Organ donation/disposition-of-remains notes.
8. Revocation, supersession, and severability.
9. Provider reliance and transfer obligations (if conscience objection possible).
10. Execution block (signature/witness/notary/acceptance).

### 4) Section templates

```text
[CLIENT NAME], [CLIENT ADDRESS]
I appoint [PRIMARY AGENT NAME], [RELATIONSHIP], as my Health Care Agent.
Contact: [ADDRESS] | [PHONE] | [EMAIL]
Authority starts when [trigger condition], as determined by [clinician criteria per state law].
Agent authority includes: treatment consent/denial, admission/discharge, care-site transfer, treatment preferences execution, and record-access coordination.
If written instruction conflicts with discretionary choice, written instruction controls.
If unspecified, Agent applies my stated values and substituted-judgment standard.
```

```text
If my Primary Agent is unavailable/unwilling/disqualified, I appoint:
First Alternate: [NAME/CONTACT]
Second Alternate: [NAME/CONTACT]
Each assumes authority only if all prior agents are unavailable per state rules.
```

```text
I authorize my Health Care Agent and alternates to access and exchange all medical records and protected health information now, regardless of trigger status, for purposes of determining incapacity and coordinating care.
Effective date: immediate upon execution.
Scope includes records from all treating providers, facilities, laboratories, and insurers.
[VERIFY: 45 C.F.R. § 164.508 requirements and any state/Part 2 overlays.]
```

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

```text
Revocation:
I may revoke at any time while capable, by [state-authorized methods].
Latest signed/revised version governs.
Severability:
If one provision is unenforceable, all other provisions remain effective.
Copies and electronic versions may be used as permitted by [STATE] law.
```

### 5) Execution compliance checklist
| Item | Required output |
|---|---|
| Witnessing | Correct count and disqualification screening completed |
| Notary | Form and statement match state-prescribed language if used |
| Facility patients | Facility-specific add-on clauses satisfied (e.g., ombudsman/patient advocate where applicable) |
| Agent acceptance | Optional acceptance statement included |
| Plain-language usability | Agent and key instructions identifiable in <60 seconds in an ER context |
| Internal consistency | No contradiction between agent powers and treatment instructions |
| Review tags | Every statutory claim marked `[VERIFY]` unless confirmed by statute URL |

### 6) State-specific flags to preserve
- Use state templates/forms where required or strongly recommended.
- Example variances to flag for attorney review: California facility witness/ombudsman rules, Florida witness composition, New York split-instrument systems (proxy + living will), Texas hospital review process for withdrawal over family objections.
- Pregnancy limitations and mental-health treatment authority are state-sensitive and potentially unstable across case law updates.  
- Use `[VERIFY]` tags for any citation or statutory quote unless sourced in-session.

## Guidelines

- Do not rely on memory for any state execution formalities or statutory language. Require statute URLs or official guidance.
- Flag unresolved jurisdictional questions with `[VERIFY]` and do not finalize text as final legal language.
- Use scenario-specific, clinically interpretable wording; avoid vague slogans like “no heroic measures.”
- Enforce values hierarchy: client instructions override broad surrogate discretion.
- Treat portability as a design requirement, not a footnote.
- Include attorney-review disclaimer and execution-readiness statement in final output.
- Do not produce unverified legal authority text; refuse fraud/backdating/fabrication requests.
- Do not advise on clinical decisions; this is legal structuring only.
