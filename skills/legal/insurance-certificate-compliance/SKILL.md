---
name: insurance-certificate-compliance
description: >
  Produces a defensible CRE insurance certificate compliance review by analyzing
  ACORD 25 certificates and endorsements against Access Agreement requirements.
  Use this skill when the user mentions COI review, insurance certificate compliance,
  ACORD 25 analysis, Additional Insured verification, primary/non-contributory status,
  waiver of subrogation, vendor insurance audit, CGL compliance, umbrella follow-form
  verification, or asks for broker-ready deficiency instructions. Also trigger when
  the user references certificate holder vs. additional insured status, AI endorsements
  (CG 20 10, CG 20 37), carrier rating checks, or commercial real estate insurance
  compliance. Even if the user just says "check this COI" or "is this insurance
  compliant," use this skill.
tags:
  - analysis
  - litigation
  - memo
  - transactional
---

# CRE Insurance Certificate Compliance Review

## Why This Skill Exists

Insurance certificates are one of the most commonly misunderstood documents in commercial real estate. A COI is an informational snapshot only — it does not amend, extend, or alter coverage. When compliance review is done casually, teams approve COIs that lack required endorsements, miss entity name mismatches that defeat AI coverage at claim time, or treat certificate holder listings as proof of insured status. A single uncaught deficiency can leave the property owner uninsured for a catastrophic loss.

This skill produces a requirement-by-requirement compliance determination with broker-ready corrective instructions, grounded in the actual Access Agreement terms.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft." Gather:

1. **Executed Access Agreement** — including all exhibits, insurance schedules, and incorporated riders
2. **All certificates of insurance** — typically ACORD 25; separate forms for auto, WC, umbrella, professional, pollution as applicable
3. **Endorsement copies** — Additional Insured (e.g., ISO CG 20 10, CG 20 37), primary/non-contributory, waiver of subrogation
4. **Recipient's broker contact details**
5. **Project/work description** — scope, dates, locations, hazard level

**If the user doesn't respond**, apply and clearly label these defaults: review against standard CGL/auto/WC/umbrella requirements; flag all missing endorsements as non-compliant; produce deficiency instructions for any gap.

### Documents to Request

If endorsements or required COIs are missing, pause and request them. If user insists on proceeding without, produce a **preliminary review** clearly labeling all conclusions as conditional.

---

## Step 1: Build Verification Matrix from Agreement

Extract and normalize the insurance clause into testable requirements:

| Requirement Category | Extract |
|---|---|
| Lines of coverage | CGL, auto, WC/EL, umbrella/excess, professional, pollution, cyber |
| Limits | Per-occurrence, general aggregate, products/completed-ops aggregate, CSL for auto, EL amounts |
| Aggregate structure | Per-project, per-location, or policy-level |
| Additional Insured entities | Exact legal names with entity suffixes for owner, manager, lender, affiliates |
| AI scope | Ongoing operations only, or ongoing + completed operations |
| Required endorsement forms | Specific ISO form numbers or "or equivalent" |
| Primary & non-contributory | Required on which lines |
| Waiver of subrogation | Required on which lines (CGL, WC, auto, property) |
| Carrier rating | AM Best minimum (typically A- VII) |
| Cancellation notice | Days' notice, to whom |
| Deductible/SIR caps | Maximum amounts |
| Occurrence vs. claims-made | Which lines must be occurrence form |

**Key pitfalls**: Missing completed-operations AI requirement; entity name mismatches (e.g., "ABC Management" vs. "ABC Management, LLC"); assuming umbrella follows form without proof.

---

## Step 2: Review ACORD 25 for Baseline Sufficiency

Check each field systematically:

| Check | What to verify |
|---|---|
| Named Insured | Matches Recipient entity in Agreement (exact legal name + suffix) |
| Policy dates | Coverage spans entire access period |
| CGL form type | "Occurrence" checked if contract requires it |
| CGL limits | Per-occurrence, general aggregate, products/completed-ops aggregate |
| Aggregate applies per | Project/location if contract requires (not just "Policy") |
| Auto coverage | "Any Auto" or required symbols; CSL meets minimum |
| WC/EL | Statutory WC; EL limits meet contract; no excluded officers performing work |
| Umbrella/Excess | Exists if required; limits stack to meet contract total; follows form to required lines |
| Certificate Holder vs. AI | Being listed as Certificate Holder does NOT grant insured status |

**Critical rule**: A COI is an informational snapshot only — it does not amend, extend, or alter coverage. Never treat it as proof of coverage.

---

## Step 3: Verify Additional Insured Status

1. Confirm **exact entities** required as AI (including affiliates language)
2. Determine endorsement type:
   - **Blanket** ("when required by written contract") — requires executed contract + endorsement copy
   - **Scheduled** (named entities) — confirm schedule lists correct names
3. Verify **scope** matches contract:
   - Ongoing operations only (CG 20 10) vs. ongoing + completed operations (CG 20 10 + CG 20 37)
   - "Caused in whole or in part" vs. vicarious liability only — varies by endorsement edition
4. If only COI is provided (no endorsement copies): **non-compliant** — issue deficiency notice

> Deficiency template: "The COI indicates Additional Insured status; however, please provide copies of AI endorsement(s) (e.g., ISO CG 20 10 and CG 20 37, or equivalents) confirming AI for both ongoing and completed operations for the entities listed in Section [__] of the Access Agreement. A certificate alone is not sufficient."

---

## Step 4: Verify Primary/Non-Contributory and Remaining Requirements

**Primary and Non-Contributory:**
- Separate requirement from AI status — AI does not automatically mean primary
- COI narrative alone is insufficient; require endorsement or policy provision
- Verify endorsement is conditioned on written contract, applicable to ongoing and completed operations, and not overridden by umbrella "other insurance" clause

**Remaining Requirements:**

| Requirement | Verification method |
|---|---|
| Waiver of subrogation | Endorsement on each required line — COI checkbox alone insufficient |
| Umbrella AI coverage | Confirm umbrella recognizes AI status; request declarations + AI endorsement |
| Carrier rating | AM Best confirmation or broker attestation; note ratings can change at renewal |
| Cancellation notice | ACORD 25 standard language confers no notice rights; require contractual covenant + notice endorsement |
| Deductible/SIR | COI rarely shows these; request declarations or broker letter. Flag credit risk for large SIRs |
| Description of Operations | Check for exclusionary language ("Excluding Residential," geographic limits) |

---

## Step 5: Produce Compliance Determination

Structure the output as:

```
INSURANCE COMPLIANCE REVIEW
[Privileged and Confidential — Attorney-Client Communication]

Project: [Name/Address]
Recipient: [Entity]
Agreement Date: [Date]
Review Date: [Date]

DETERMINATION: [Compliant / Non-Compliant / Conditionally Compliant]

REQUIREMENT-BY-REQUIREMENT ANALYSIS:
| # | Requirement | Contract Reference | Status | Evidence | Deficiency |
|---|---|---|---|---|---|
| 1 | CGL $1M occ / $2M agg | §[X] | Compliant | COI shows matching limits | — |
| 2 | AI - ongoing + completed ops | §[X] | Non-Compliant | No endorsement provided | Provide CG 20 10 + CG 20 37 |
...

BROKER INSTRUCTIONS:
[Numbered list of specific corrective actions with exact document requests]

ESCALATION ITEMS:
[Issues requiring attorney or coverage counsel review]
```

### Mandatory Front Matter

Include at top: **Assumptions Used** and **Open Items / Needed Inputs**. This tells the attorney exactly what was assumed and what must be verified.

**Drafting rules**: Use "unable to verify" rather than "coverage will be denied." Avoid speculative coverage statements. Distinguish: "confirmed" / "indicated but not verified" / "not shown — non-compliant."

---

## Jurisdiction-Specific Flags

| Jurisdiction | Key Issue | Action |
|---|---|---|
| **New York** | Labor Law §§240/241 strict liability for gravity injuries on construction sites | Check for "Labor Law," "Heights," or "Action Over" exclusions. Escalate to coverage counsel. See also NY Insurance Law §3426 [VERIFY] |
| **Texas** | Anti-Indemnity Act (Insurance Code Ch. 151) restricts AI for indemnitee's own negligence in construction | Flag if access involves "construction, alteration, or repair" |
| **California** | Civil Code §2782 limits risk-shifting for owner's "active negligence" in construction | Confirm indemnity + AI requirements are consistent |
| **Florida** | Fla. Stat. §627.4137 claimant rights to policy information | Note if potential claim is identified |

For all jurisdictions: do not assert universal rules about certificate legal effect or anti-indemnity scope. Treat the Agreement as the commercial benchmark and flag state-law issues for local counsel confirmation.

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the initial review, ask:

1. Does the determination match your understanding of the coverage posture?
2. Are there additional entities that should be verified as Additional Insureds?
3. Should any deficiency items be escalated to coverage counsel rather than handled via broker instructions?
4. Is a follow-up compliance check needed after broker cures the deficiencies?

---

## Quality Audit

Before finalizing, verify:

- Every Agreement requirement mapped to a testable check
- Requirement-by-requirement table complete with status for each line
- Entity names compared character-by-character (including LLC, Inc., LP suffixes)
- No compliance finding based solely on COI without endorsement verification
- Broker instructions are specific and actionable (not generic "provide adequate coverage")
- Jurisdiction-specific flags included where applicable
- Assumptions and open items listed prominently
- Privilege designation confirmed with supervising attorney
- Every factual assertion traceable to a document or labeled as assumption
- Disclaimer included stating this is not a coverage opinion

---

## Guidelines

- **COI ≠ coverage**: Never approve compliance based solely on a certificate without required endorsements
- **Entity names must match exactly** — including LLC, Inc., LP suffixes; mismatches defeat AI coverage at claim time
- **No coverage opinions**: This review compares contract requirements to documentary evidence — it does not opine on whether coverage will respond to a specific claim
- **Privilege**: Confirm with supervising attorney whether output should be labeled privileged; sharing to third-party property managers may waive privilege
- **Ethics**: Model Rule 1.1 (competence) requires understanding COI limitations; Rule 4.1 (truthfulness) governs communications with Recipient's broker
- **Anti-hallucination**: Do not invent policy terms, endorsement form numbers, or coverage conclusions not supported by the documents reviewed. Use `[VERIFY]` for any unconfirmed detail
- **Attorney review required**: Every deliverable must include the disclaimer that it requires licensed attorney review before reliance
