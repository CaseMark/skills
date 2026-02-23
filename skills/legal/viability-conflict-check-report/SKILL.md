---
name: viability-conflict-check-report
description: Drafts a pre-filing US litigation intake memo that combines conflict screening, legal/procedural viability analysis, and economic triage to support an accept-versus-decline decision. Use when the request is for matter acceptance review, conflict-check review, pre-suit intake triage, referral screening, or conflict-waiver recommendations, using trigger phrases such as “new matter evaluation,” “decline/accept decision,” “conflict check,” and “pre-filing assessment.”
tags:
  - analysis
  - litigation
  - memo
---

# Case Viability & Conflict Check Report

Produces a litigation-internal memorandum for partner-level approval before firm engagement.

## Prerequisites

1. Intake summary with alleged facts, date(s), parties, claims, and claimed damages.
2. Signed/authorized access to conflict database and firm client/matter records.
3. Document set (complaint drafts, police reports, correspondence, medical records, contracts, estimates, etc.).
4. Proposed jurisdiction and forum information.
5. Fee model being contemplated (contingency/hourly/flat/hybrid).
6. Internal policy thresholds for minimum merit, minimum projected value, and conflict tolerance.
7. Available research access for jurisdiction-specific statutes, procedural rules, and recent adverse precedent.

## Output Structure / Process

### 1) Required Evidence Intake
| Field | Required extraction | Verification rule |
|---|---|---|
| Matter identity | Client name/aliases, adverse parties, incident date, filing target date | At least one source document each |
| Liability facts | Key elements tied to alleged claims | Flag unsupported or self-serving allegations |
| Exposure facts | Medical/economic loss, property loss, lost income, pain scales | Distinguish disclosed from inferred amounts |
| Timeline risks | Accrual date, notice period, SOL clock | Compute deadline with uncertainty notes |
| Internal touchpoints | Prior or current relationships with parties/matter/subject matter | Confirm via conflict database scope/date |

### 2) Conflict Analysis
- Run full conflict query across current clients, former clients, pending matters, and anticipated adverse interests.
- Classify by bucket:
  - Direct current-client conflict
  - Former-client duty conflict
  - Positional inconsistency
  - Imputed conflict
  - Prospective-client issue
- Assess each bucket as:
  - Non-waivable barrier
  - Waivable only with informed written consent
  - No impediment
- Use Rules 1.7, 1.9, 1.10, 1.18 as baseline ethical framework; note local equivalents and modifications in the governing jurisdiction. [VERIFY]

### 3) Legal/Procedural Viability Matrix
| Issue | Strengths | Weaknesses | Counterparty defenses | Evidence needed |
|---|---|---|---|---|
| Elements for each cause | Facts matching element + citations | Missing or contradictory facts | Most likely threshold and merits defenses | What is required to cure each gap |

- Validate standing, real party in interest, and any assignment/subrogation ownership constraints.
- Check procedural gatekeepers:
  - Statute of limitations (start date, tolling, deadline)
  - Jurisdiction, venue, personal jurisdiction
  - Administrative prerequisites (pre-suit notice, exhaustion, ADR preconditions)
  - Mandatory mediation/arbitration and enforceability questions
- Include statute references only when verified; otherwise mark as `[VERIFY]`.
- Cite any adverse controlling decisions likely to defeat core claim theories.

### 4) Economic and Resource Review
| Cost/effort bucket | Range estimate | Risk multiplier | Decision impact |
|---|---|---|---|
| Investigation & pleadings | hours + cost | 1x | Low / medium / high |
| Discovery & motions | hours + costs | 1–2x | |
| Experts/evidence | budget + dependencies | 1–3x | |
| Trial/posture prep | hours + budget | 1–4x | |
| Collection risk | low / medium / low certainty | value-adjusted recovery | |

- Quantify expected recovery bands (best/base/worst) and estimate collectability.
- Compare projected investment against expected upside and downside.
- Include staffing need, conflicts-screen burden, and co-counsel or specialist dependency.

### 5) Recommendation Logic
- Require explicit recommendation: `ACCEPT` or `DECLINE` (no soft close).
- If `ACCEPT`, list pre-engagement conditions:
  - Conflict waivers
  - Retainer/cost structure
  - Retention letter scope limits
  - Clarifying call and evidence supplement list
- If `DECLINE`, provide:
  - Legal reason(s)
  - Economics reason(s)
  - Resource/risk reason(s)
  - Referral destination(s), including courtesy constraints

### 6) Report Template
```text
Case Viability & Conflict Check Report
Date:
Preparer:
Matter ID:
Jurisdiction / Court venue:
Matter phase: Pre-filing

1) Intake Fact Snapshot
- Client:
- Adverse parties:
- Date(s) of accrual:
- Alleged losses:
- Current procedural posture:

2) Conflict Check Record
- Databases searched:
- Date range covered:
- Conflict findings:
- Waiver strategy/consent feasibility:
- Final conflict posture:

3) Legal Viability Assessment
- Claims and element analysis:
- Procedural blockers:
- Exposure ceiling + collectability:
- Adverse authority/defense profile:

4) Economic Viability
- Estimated cost by phase:
- Fee model assumptions:
- ROI and risk-adjusted upside:
- Capacity/utilization impact:

5) Recommendation
- Decision:
- Conditions precedent:
- Red flags:
- Action memo:

6) Sources / Limits
- Legal authorities:
- Internal records reviewed:
- Analysis limitations / missing facts:
```

## Guidelines

1. Use conservative assumptions when material facts are missing; treat gaps as risk unless corroborated.
2. Distinguish confirmed facts from inferred facts and unsupported inferences.
3. Do not provide client-directed legal advice in this memo; keep language leadership-internal.
4. Never normalize conflicts; document waiver path and failure mode before acceptance.
5. Require explicit decision authority and date stamp in final section.
6. Treat any jurisdiction-specific rule, statute, or procedural nuance as needing independent verification where unfamiliar. [VERIFY]
7. Preserve privilege posture by routing as attorney work product/internal analysis; exclude from client-facing files without cleanup.
