---
name: insurance-certificate-compliance-check
description: >-
  Performs a contract-driven legal review of insurance certificates and
  endorsements for CRE/site-access and vendor contracts. Use for COI packet
  intake and risk-control outputs that must determine compliance with
  insured-coverage requirements, required limits, additional insured naming,
  completed-operations extension, primary and non-contributory language,
  waiver of subrogation, and notice/qualification terms. Best used when user
  supplies Access Agreement terms plus ACORD forms and asks for a
  pass/fail/conditional result, deficit list, broker-ready remediation, or
  escalation guidance. Trigger keywords: COI, ACORD 25, additional insured,
  primary and non-contributory, completion operations, umbrella, waiver of
  subrogation, insurer rating, certificate holder, cancellation notice.
tags:
  - analysis
  - drafting
  - litigation
  - memo
  - regulatory
  - transactional
---

# Insurance Certificate Compliance Check

Generates a defensible compliance determination comparing agreement requirements to COI and endorsement evidence.

## Prerequisites

1. Access Agreement (final version) with insurance clause, exhibits, schedules, and amendments.
2. COIs for every required coverage line: CGL, auto, workers’ compensation/EL, umbrella, and any expressly required specialty lines.
3. Endorsement and schedule copies for AI, completed operations AI, primary/non-contributory, waiver of subrogation, and umbrella terms.
4. Recipient legal name(s), required AI entities, and exact work/product/project scope.
5. Access dates and project locations, including any post-completion coverage carry-forward period.
6. Governing-law/jurisdiction stated in agreement.
7. Delivery recipients for the output and privilege instructions.

## Output Structure / Process

### 1) Normalize agreement requirements into a matrix

| Category | Required extraction | Normalized output |
|---|---|---|
| Coverage types | CGL, auto, WC/EL, umbrella, etc. | `[line]: [required form/limits/scope]` |
| Limits | Occurrence, agg, products-completed aggregate, per location/project | Numeric minimums + frequency |
| AI scope | named entities and affiliates | Exact legal names + whether ongoing/completed |
| Priority terms | Primary/non-contributory | Required for which policies/lines |
| Waiver of subrogation | Which lines must include waiver | CGL/WC/auto/property |
| Notice/ratings | cancellation notice, AM Best, insurer status | Required evidence/source |
| Special clauses | exclusions, endorsements by form number | Must be provided and checked for fit |

If any clause is vague (`acceptable`, `sufficient`, `as required by owner`) flag as **Attorney Clarification Required**.

### 2) COI baseline checks (information-only)

1. Named insured must match Recipient entity exactly (name + suffix + related entity logic).
2. Policy period covers required access window.
3. Required coverages and stated limits appear in requested fields.
4. Occurrence vs claims-made requirement confirmed where applicable.
5. `Limits Apply` and aggregate designations align with contract (`per occurrence`, `per location`, `per project`).
6. Confirm producer/broker contact exists.
7. Capture red flags: expired/soon-expiring policies, wrong entity, missing policy numbers, suspicious operations descriptions.

If COI evidence is incomplete, set status to `conditionally compliant` and list missing documents before final conclusion.

### 3) Endorsement-level mandatory verification

For every core element below, COI text alone is non-binding.

| Element | Required confirmation | Typical failure mode |
|---|---|---|
| Additional insured | Endorsement or policy language identifies exact required entities | Blanket AI exists but entity mismatch |
| Completed operations AI | Separate language/endorsement for completed ops if required | Only ongoing AI provided |
| Primary/non-contributory | Separate PNC clause/endorsement for AI | AI marked on COI only |
| Umbrella alignment | Underlying + umbrella include required AI/PNC and intended lines | No schedule showing AI/PNC extension |
| Waiver of subrogation | Endorsement showing waiver on required lines | Narrative in COI only |
| Cancellation/no-renewal notice | enforceable mechanism documented | Reliance on ACORD limitations only |

### 4) Risk and coverage-structure checks

1. Confirm required minimum limits versus exposed values at each line and project.
2. Compute combined available limits where umbrella is intended to augment GL/auto/EL.
3. Validate no contractual coverage-on-paper conflict with access-specific exclusions or geographic/type-of-work exclusions.
4. Verify deductibles/SIR and exclusions if high risk or large retention exists (if provided by declarations/broker attestation).
5. Confirm insurer rating requirements with explicit evidence (broker attestation, rating confirmation).

### 5) Jurisdiction adaptation (mark uncertainties)

- New York: construction/gravity-risk clauses and labor-law exclusionary terms need focused review `[VERIFY]`.
- Texas: anti-indemnity construction impact on AI/enforcement pathways `[VERIFY]`.
- California: active-negligence/AI enforceability constraints `[VERIFY]`.
- Florida: policy/document disclosure and insurer-info rights if claim posture exists `[VERIFY]`.

If governing law is uncertain or outside provided data, mark all jurisdictional conclusions as **requires legal verification**.

### 6) Output format

```text
Result: [Compliant | Conditionally Compliant | Non-Compliant]
Jurisdiction: [state]
Coverage period tested: [start] to [end]
Review confidence: [High | Medium | Low]

Requirements Matrix:
- Requirement | Evidence reviewed | Status | Finding | Deficiency
- ...

Escalation: [In-house counsel / Risk manager / Coverage counsel]
Access decision: [Recommend allow / conditional / deny pending docs]
```

Use entity-name exactness and numeric precision (`$1,000,000 each occurrence`, `requires PG-20/CG 20 37`, etc.).

## Guidelines

- Treat every COI statement as documentary indication, not contractual proof.
- Never state “fully covered” without endorsement/policy support.
- Do not conflate `certificate holder` with `additional insured`.
- Never infer AI scope from checkbox or `Description of Operations` only.
- For each missing item, provide a precise broker instruction: exact document, exact endorsement form/edition, and deadline.
- Keep a running list of `confirmed`, `indicated-not-verified`, and `not shown`.
- Never provide coverage legal opinions; flag as **risk-control assessment**.
- Include explicit attorney review requirement before operational reliance.
- If unresolved deficiencies remain and access is allowed, document a written exception and mitigation controls.
- If potential anti-indemnity/statutory effects drive outcome, escalate immediately.
- Use `[VERIFY]` on all uncited or uncertain citations/authority claims.
