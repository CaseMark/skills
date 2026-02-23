---
name: insurance-certificate-compliance
description: Reviews CRE insurance certificates (ACORD 25) against Access Agreement requirements, verifying coverage limits, Additional Insured endorsements, primary/non-contributory status, and waiver of subrogation compliance. Produces a defensible compliance determination with broker-ready deficiency instructions. Use when reviewing COIs, checking insurance compliance, verifying additional insured status, or auditing vendor insurance certificates for commercial real estate.
tags:
  - analysis
  - litigation
  - memo
  - transactional
---

# CRE Insurance Certificate Compliance Review

Reviews insurance certificates and endorsements against Access Agreement requirements to produce a defensible compliance determination with broker-ready corrective instructions.

## Prerequisites

1. **Executed Access Agreement** — including all exhibits, insurance schedules, and incorporated riders
2. **All certificates of insurance** — typically ACORD 25; separate forms for auto, WC, umbrella, professional, pollution as applicable
3. **Endorsement copies** — Additional Insured (e.g., ISO CG 20 10, CG 20 37), primary/non-contributory, waiver of subrogation
4. **Recipient's broker contact details**
5. **Project/work description** — scope, dates, locations, hazard level

If endorsements or required COIs are missing, pause and request them. If user insists on proceeding without, produce a **preliminary review** clearly labeling all conclusions as conditional.

## Process

### Step 1: Build Verification Matrix from Agreement

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

### Step 2: Review ACORD 25 for Baseline Sufficiency

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

### Step 3: Verify Additional Insured Status

1. Confirm **exact entities** required as AI (including affiliates language)
2. Determine endorsement type:
   - **Blanket** ("when required by written contract") — requires executed contract + endorsement copy
   - **Scheduled** (named entities) — confirm schedule lists correct names
3. Verify **scope** matches contract:
   - Ongoing operations only (CG 20 10) vs. ongoing + completed operations (CG 20 10 + CG 20 37)
   - "Caused in whole or in part" vs. vicarious liability only — varies by endorsement edition
4. If only COI is provided (no endorsement copies): **non-compliant** — issue deficiency notice

> Deficiency template: "The COI indicates Additional Insured status; however, please provide copies of AI endorsement(s) (e.g., ISO CG 20 10 and CG 20 37, or equivalents) confirming AI for both ongoing and completed operations for the entities listed in Section [__] of the Access Agreement. A certificate alone is not sufficient."

### Step 4: Verify Primary and Non-Contributory

- Separate requirement from AI status — AI does not automatically mean primary
- COI narrative alone is insufficient; require **endorsement or policy provision**
- Verify endorsement is:
  - Conditioned on written contract (satisfied by the Agreement)
  - Applicable to ongoing and completed operations (not just one)
  - Not overridden by umbrella "other insurance" clause
- Check whether umbrella is also primary or only excess over primary CGL

### Step 5: Verify Remaining Requirements

| Requirement | Verification method |
|---|---|
| **Waiver of subrogation** | Endorsement on each required line (CGL, WC, auto, property) — COI checkbox alone insufficient |
| **Umbrella AI coverage** | Confirm umbrella recognizes AI status; request declarations + AI endorsement for umbrella |
| **Carrier rating** | AM Best confirmation or broker attestation; note ratings can change at renewal |
| **Cancellation notice** | ACORD 25 standard language confers no notice rights; require contractual covenant + notice endorsement if available |
| **Deductible/SIR** | COI rarely shows these; request declarations or broker letter. Flag credit risk for large SIRs |
| **Description of Operations** | Check for exclusionary language ("Excluding Residential," geographic limits) that could invalidate coverage |

### Step 6: Produce Compliance Determination

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

DISCLAIMER: This is a draft risk-control assessment requiring review
by a licensed attorney. It does not constitute a coverage opinion.
All determinations should be confirmed with the client's insurance
broker or risk management department.
```

**Drafting rules for the written record**:
- Use "unable to verify" rather than "coverage will be denied"
- Avoid speculative coverage statements — stick to contract requirements vs. documentary evidence
- Distinguish: "confirmed" / "indicated but not verified" / "not shown — non-compliant"

## Jurisdiction-Specific Flags

| Jurisdiction | Key Issue | Action |
|---|---|---|
| **New York** | Labor Law §§240/241 strict liability for gravity injuries on construction sites | Check for "Labor Law," "Heights," or "Action Over" exclusions in policy materials. Escalate to coverage counsel. See also NY Insurance Law §3426 (cancellation/non-renewal) [VERIFY] |
| **Texas** | Anti-Indemnity Act (Insurance Code Ch. 151) restricts AI for indemnitee's own negligence in construction contracts | Flag if access involves "construction, alteration, or repair" |
| **California** | Civil Code §2782 limits risk-shifting for owner's "active negligence" in construction | Confirm indemnity + AI requirements are consistent |
| **Florida** | Fla. Stat. §627.4137 claimant rights to policy information | Note if potential claim is identified |

For all jurisdictions: do not assert universal rules about certificate legal effect or anti-indemnity scope. Treat the Agreement as the commercial benchmark and flag state-law issues for local counsel confirmation.

## Guidelines

- **COI ≠ coverage**: Never approve compliance based solely on a certificate without required endorsements
- **Entity names must match exactly** — including LLC, Inc., LP suffixes; mismatches defeat AI coverage at claim time
- **Conditional access is risky** — if business team overrides, document the exception and require mitigations
- **Privilege**: Confirm with supervising attorney whether output should be labeled privileged; sharing to third-party property managers may waive privilege
- **Ethics**: Model Rule 1.1 (competence) requires understanding COI limitations; Rule 4.1 (truthfulness) governs communications with Recipient's broker
- **No coverage opinions**: This review compares contract requirements to documentary evidence — it does not opine on whether coverage will respond to a specific claim
- **Attorney review required**: Every deliverable must include the disclaimer that it requires licensed attorney review before reliance
