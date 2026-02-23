---
name: employee-complaint-summaries
description: Generates structured summaries of employee complaints in employment litigation by extracting key parties, chronological timelines, allegations, legal claims, evidence inventory, employer defenses, and risk flags from complaint files, investigation reports, personnel files, and correspondence. Covers Title VII, ADA, ADEA, FMLA, FLSA, and state/local analogs. Use when reviewing initial complaints, internal investigation reports, or personnel files to assess case risk, identify inconsistencies, and develop litigation or response strategy.
tags:
  - analysis
  - litigation
  - summarization
  - summary
---

# Employee Complaint Summary

Produces a structured attorney-review memo distilling an employee complaint into parties, timeline, claims, evidence, defenses, and risk assessment.

## Prerequisites

1. **Complaint materials** — formal complaint letter, EEOC charge, or internal grievance filing
2. **Investigation file** — HR investigation report, witness statements, interview notes
3. **Personnel records** — performance reviews, disciplinary records, employment agreements
4. **Correspondence** — emails, texts, or other communications referenced in the complaint
5. **Policy documents** — employee handbook, anti-harassment/discrimination policies (if available)

## Output Structure

### 1. Key Parties

| Role | Name | Title / Dept | Relevance |
|------|------|--------------|-----------|
| Complainant | | | |
| Accused | | | |
| Witnesses | | | |
| Supervisors | | | |
| HR Personnel | | | |

### 2. Chronological Timeline

| Date | Event | Parties Involved | Source |
|------|-------|-----------------|--------|
| | | | |

Flag approximate dates as `[est.]`. Note gaps in the record explicitly.

### 3. Allegations & Legal Claims

For each claim:
- **Claim type** (discrimination / harassment / retaliation / wage-hour / wrongful termination / breach of contract / other)
- **Protected basis** if applicable (race, sex, age, disability, national origin, religion, FMLA leave, etc.)
- **Key quoted language** from the complaint with document/page citation
- **Alleged harm** (termination, demotion, hostile work environment, lost wages, etc.)

### 4. Evidence Inventory

| Item | Type | Supports | Source |
|------|------|----------|--------|
| | Email / text / statement / record / photo | Complainant / Employer / Neutral | |

### 5. Employer Responses & Defenses

- Known employer explanations for adverse actions (legitimate nondiscriminatory reason, performance basis, RIF, policy violation)
- Contrary witness statements or documentation
- Evidence of progressive discipline, prior warnings, or documented performance issues
- Any internal investigation findings and conclusions

### 6. Legal Framework & Procedural Checklist

- [ ] **Title VII** (42 U.S.C. § 2000e) — discrimination/harassment/retaliation; EEOC charge required; 180/300-day filing deadline
- [ ] **ADA** (42 U.S.C. § 12101) — disability discrimination; same EEOC exhaustion
- [ ] **ADEA** (29 U.S.C. § 621) — age 40+; EEOC charge required
- [ ] **FMLA** (29 U.S.C. § 2601) — interference or retaliation; 2/3-year SOL
- [ ] **FLSA** (29 U.S.C. § 201) — wage/hour; 2/3-year SOL; no EEOC exhaustion required
- [ ] **State/local analogs** — identify applicable state FEP statute and any broader protections [VERIFY jurisdiction]
- [ ] **Contractual grievance procedures** — arbitration clauses, notice requirements, internal appeal steps

### 7. Risk Assessment

| Factor | Assessment |
|--------|-----------|
| Claim strength (evidence quality) | Strong / Mixed / Weak |
| Key factual disputes | |
| Credibility issues | |
| Punitive damages exposure | Yes / No / Possible |
| Pattern-or-practice risk | Yes / No |
| Systemic/class scope potential | Yes / No |
| Gaps requiring further investigation | |

### 8. Investigation & Discovery Priorities

List outstanding information needs: missing documents, uninterviewed witnesses, ESI to preserve, third-party records to obtain.

## Guidelines

- Cite source document and page/section for every factual assertion
- Maintain neutral framing; represent each party's position accurately
- Flag `[GAP]` where the record is incomplete and additional investigation is needed
- Flag `[VERIFY]` on any statutory citation where jurisdiction-specific variation may apply
- Do not apply legal conclusions to facts — flag issues for attorney analysis
- Note EEOC/agency deadlines if charge has been filed or adverse action date is known
