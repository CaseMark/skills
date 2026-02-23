---
name: coi-compliance-review
description: Conducts a contract-driven compliance review of CRE insurance certificates (ACORD 25) and endorsements against Access Agreement insurance requirements. Verifies coverage limits, Additional Insured status, primary/non-contributory language, waiver of subrogation, umbrella alignment, and carrier qualifications. Produces a pass/fail compliance determination with broker-ready deficiency instructions and escalation guidance. Use when reviewing certificates of insurance, COIs, ACORD forms, vendor insurance, contractor insurance, site access insurance, or Additional Insured endorsements in commercial real estate transactions.
tags:
  - analysis
  - summary
  - transactional
---

# CRE Insurance Certificate Compliance Review

Reviews ACORD 25 certificates and endorsements against a CRE Access Agreement's insurance requirements, producing a defensible compliance determination with deficiency instructions.

## Prerequisites

1. **Access Agreement** — executed or signature-ready, including all exhibits, insurance schedules, and any incorporated riders or property rules
2. **All COIs** — ACORD 25 (CGL); separate forms for auto, WC/EL, umbrella/excess, professional, pollution, builder's risk as required
3. **Endorsements** — Additional Insured (e.g., ISO CG 20 10, CG 20 37), primary/non-contributory, waiver of subrogation
4. **Recipient details** — insurer and broker contact info; exact legal name of accessing party and all required Indemnitees (owner, manager, lender, affiliates)
5. **Project scope** — work description, access dates, locations, and any heightened-risk activities (hot work, roofing, structural, environmental, confined space)

**If endorsements are required but not provided:** Pause and request before issuing a final determination. If user insists on proceeding, issue a **preliminary conditional review** with all unverified conclusions clearly labeled.

---

## Output Structure

### Step 1 — Build Verification Matrix from the Insurance Clause

Extract and normalize all requirements into testable items before reviewing any COI:

| Requirement | Contractual Standard | Evidence Required |
|---|---|---|
| CGL form | Occurrence (not claims-made) | COI policy type field |
| CGL per-occurrence | $[X] | COI limits box |
| CGL general aggregate | $[X] | COI limits box |
| Products/Completed Ops agg | $[X] | COI limits box |
| Aggregate basis | Per project / Per location / Policy | COI "Limits Apply Per" field |
| Auto CSL | $[X] / "Any Auto" | COI auto section |
| WC | Statutory | COI WC section |
| EL – Each Accident / Disease | $[X] / $[X] | COI EL limits |
| Umbrella/Excess | $[X] over scheduled underlying | Umbrella COI + declarations |
| Additional Insured – ongoing | [Exact entity names] | CG 20 10 or equivalent |
| Additional Insured – completed ops | [Exact entity names] | CG 20 37 or equivalent |
| Primary & Non-Contributory | When required by contract | PNC endorsement |
| Waiver of Subrogation | CGL / WC / Auto | Per-line endorsements |
| Carrier rating | AM Best A- VII or better | Broker attestation |
| Cancellation notice | [X] days | Endorsement or covenant |
| Deductible / SIR cap | $[X] max | Declarations or broker letter |

**Flag ambiguous clause language** (e.g., "as acceptable to Owner") for client confirmation before issuing a determination.

---

### Step 2 — ACORD 25 Internal Review Checklist

- [ ] Named Insured matches Recipient's exact legal name and entity suffix in the Agreement
- [ ] Producer contact information present and usable
- [ ] Policy effective/expiration dates cover entire access period (+ completed ops tail if required)
- [ ] CGL form type: **Occurrence** (claims-made = non-compliant absent contract exception)
- [ ] CGL per-occurrence, general aggregate, and products/completed ops aggregate meet minimums
- [ ] "Limits Apply Per" field matches contract (Policy vs. Per Project vs. Per Location)
- [ ] Auto: "Any Auto" or required symbols; CSL meets minimum
- [ ] WC: Statutory box checked; EL limits meet minimums; proprietor/officer exclusions noted
- [ ] Umbrella/Excess: present, limits confirmed, form type (umbrella vs. excess)
- [ ] Description of Operations: no suspicious exclusions (e.g., "Excluding Residential Work," geographic carve-outs, Labor Law exclusions)
- [ ] "Certificate Holder" ≠ "Additional Insured" — confirm not treated as equivalent

> **COI is an informational snapshot only.** It does not amend, extend, or alter policy coverage. All compliance conclusions depend on underlying endorsements.

---

### Step 3 — Additional Insured Verification

**Required evidence:** Actual endorsement (blanket or scheduled), not COI checkbox or Description of Operations narrative alone.

| Check | Standard |
|---|---|
| Endorsement type | Blanket ("when required by written contract") or scheduled with exact entity names |
| Ongoing operations | ISO CG 20 10 04 13 or equivalent |
| Completed operations | ISO CG 20 37 04 13 or equivalent — **required if contract demands it** |
| AI scope | "Caused in whole or in part by named insured's acts or omissions" vs. vicarious-only — quote operative language |
| Entity name match | Exact match including entity suffix (LLC, LP, Inc.) and any affiliate/lender extension |
| Umbrella AI | Confirm umbrella also extends AI; if not, client's AI coverage is capped at CGL limits |

**Sample deficiency language:**
> "The COI indicates AI status; however, the Agreement requires Owner, Manager, and Lender as Additional Insureds for ongoing and completed operations. Provide copies of the AI endorsements (ISO CG 20 10 and CG 20 37 or equivalents) confirming AI status for both phases and for each entity listed in Section __ of the Agreement. A certificate alone is not sufficient."

---

### Step 4 — Primary & Non-Contributory Verification

- [ ] Contract requires P&NC → confirmed in writing?
- [ ] COI Description of Operations contains P&NC narrative? (informational only)
- [ ] **Endorsement provided** confirming P&NC when required by written contract?
- [ ] Endorsement scope: applies to ongoing ops only, or completed ops as well?
- [ ] Umbrella "other insurance" clause does not override P&NC at CGL level?

Without a P&NC endorsement, client's insurer may be forced to contribute — treat as **non-compliant**.

---

### Step 5 — Ancillary Requirements

**Waiver of Subrogation**

| Line | Required | Endorsement Provided |
|---|---|---|
| CGL | Yes/No | ☐ |
| Workers' Compensation | Yes/No | ☐ |
| Auto | Yes/No | ☐ |

WC waiver typically requires a specific form; a COI checkmark is insufficient.

**Limits structure**
- Combined CGL + umbrella limits ≥ contract total minimum
- Umbrella underlying schedule includes CGL, auto, and EL as required
- Products/completed ops aggregate confirmed at required level

**Carrier rating**
- AM Best minimum per contract (typically A- VII)
- COI does not show ratings — require broker attestation or AM Best confirmation
- Flag for re-verification on each renewal

**Cancellation/Notice**
- Modern ACORD 25 does not guarantee insurer-to-certificate-holder notice
- Require Recipient contractual covenant to notify + request insurer notice endorsement where available
- Flag reliance on notice as a soft control only

**Deductibles / SIR**
- COI generally does not show deductibles reliably
- If contract caps SIR, require declarations page or broker letter
- Large SIR = Recipient effectively self-insuring first layer; flag credit/funding risk for AI defense

---

### Step 6 — Compliance Determination Output

Structure as a memo or email-ready report:

```
COMPLIANCE STATUS: [COMPLIANT / NON-COMPLIANT / CONDITIONALLY COMPLIANT]

SUMMARY: [1–2 sentence bottom line]

REQUIREMENT-BY-REQUIREMENT FINDINGS:
[Table or list: Requirement | Status | Evidence | Gap/Action]

DEFICIENCIES (broker-ready):
1. [Specific item — exact entity name, exact limit, exact form needed]
2. ...

ESCALATION RECOMMENDATION: [Yes/No — reason]

ACCESS RECOMMENDATION:
- Compliant: Access may proceed.
- Non-compliant / Conditional: Access not recommended until items above are resolved. If business team grants access notwithstanding, document as exception to policy and identify mitigations (restricted scope, supervision, indemnity hold).

ATTORNEY REVIEW REQUIRED: This is a draft risk-control assessment, not a coverage opinion. Confirm with supervising attorney and client's broker before reliance.
```

**Escalate to coverage counsel when:**
- Recipient cannot produce required endorsements
- Endorsement language materially narrower than contract requirement
- Carrier rating below contractual minimum
- Heightened-risk work (NY construction, hazmat, structural)
- Agreement's insurance terms are internally inconsistent

---

## Guidelines

- **COI ≠ Policy.** Never conclude coverage is confirmed without endorsement-level evidence for AI, P&NC, and waiver of subrogation
- **Entity names:** Exact match required — punctuation, entity suffix, affiliates. Mismatch = AI coverage gap
- **Completed ops:** Separately confirm; many blanket AI endorsements cover only ongoing operations
- **Claims-made CGL:** Flag as non-compliant for CRE access absent explicit contract exception
- **Umbrella:** Verify AI status and underlying schedule; "follows form" is not self-proving
- **Privilege:** Label output "Privileged and Confidential / Attorney-Client Communication" if directed by supervising attorney; confirm privilege posture before broad distribution

**Jurisdiction flags — escalate to local counsel:**

| State | Issue |
|---|---|
| New York | Labor Law §§ 240/241 strict liability; check for "Action Over," "Labor Law," or "Heights" exclusions on all submitted policies; NY Ins. Law § 3426 cancellation rules |
| Texas | Insurance Code Ch. 151 anti-indemnity may limit AI enforceability in construction contracts — confirm whether access involves "construction, alteration, or repair" |
| California | Civil Code § 2782 limits risk-shifting for owner's active negligence in construction contexts |
| Florida | Fla. Stat. § 627.4137 — claimant rights to certified policy copies; flag if potential claim identified |

- For **all jurisdictions:** Do not assert universal rules on COI legal effect, P&NC enforceability, or anti-indemnity statutes. Flag for attorney verification
- **[VERIFY]** any case citations or statutory interpretations not confirmed by contemporaneous research before including in client-facing output
