---
name: intrastate-offering
description: >
  Produces a structured compliance memo and execution plan for U.S. intrastate
  securities offerings under Securities Act Rule 147 or Rule 147A with state
  registration by qualification. Covers issuer eligibility tests, principal place
  of business, investor residency verification, advertising controls, resale
  restrictions and legends, integration analysis, antifraud alignment, and state
  blue sky registration. Use this skill for intrastate offering compliance, Rule
  147, Rule 147A, registration by qualification, blue sky review, residency
  verification workflows, single-state offerings, or Section 3(a)(11) analysis.
  Also trigger when the user mentions state-only fundraising, in-state investor
  requirements, or resale restriction legends. Even if the user just says
  "we're only raising in one state" or "intrastate exemption," use this skill.
tags:
  - analysis
  - corporate
  - drafting
  - memo
  - regulatory
---

# Intrastate Offering Compliance (Rule 147/147A)

## Why This Skill Exists

Intrastate offerings under Rule 147/147A are conceptually simple — sell only to residents of one state — but operationally demanding. A single out-of-state sale destroys the exemption, potentially retroactively for all investors. The "doing business" tests require documented proof across four metrics. Advertising in the internet age creates constant boundary risks. And unlike Rule 506, there is no NSMIA preemption — the issuer must also comply with full state registration requirements.

This skill builds a defensible compliance memo and execution plan that prevents the exemption-killing mistakes: inadequate residency verification, uncontrolled advertising reach, failed doing-business tests, and integration with concurrent offerings.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft." Gather:

1. **Offering state and issuer entity details** — state of formation, principal office address, org chart
2. **Operations and financials by state** — revenues, assets, employees, locations; most recent financials
3. **Offering terms** — security type, size, pricing, use of proceeds, escrow, commissions
4. **Draft materials** — term sheet, offering document, subscription agreement, marketing copy
5. **Distribution plan and advertising channels** — including internet use
6. **Investor workflow and residency verification process** — online/offline, document retention
7. **Prior and planned offerings** — types, dates, investor pools in last and next 6 months
8. **State blue sky rules** — registration forms, examiner guidance, filing requirements

**If the user doesn't respond**, apply and clearly label these defaults: Rule 147A (permits out-of-state formation and general solicitation with legends); registration by qualification path; standard residency documentation requirements.

---

## Step 1: Select Safe Harbor (Rule 147 vs. 147A)

| Factor | Rule 147 [VERIFY] | Rule 147A [VERIFY] | Decision Notes |
|---|---|---|---|
| Issuer formation | Must be organized in offering state | Can be organized out of state | If formed elsewhere, use 147A |
| Principal place of business | Required | Required | Document "nerve center" |
| General solicitation | Restricted | Permitted with residency legends | Choose 147A if broad internet use |
| Offers to out-of-state | Risky | Permitted if sales only in-state | Confirm offer definition |

Pull current text from eCFR for 17 CFR 230.147, 230.147A, and 230.152 [VERIFY]. Confirm Securities Act Sections 3(a)(11), 5, and 17(a) [VERIFY].

---

## Step 2: Analyze Issuer Eligibility (Doing Business Tests)

All four tests must be met. Document evidence for each:

| Test [VERIFY] | Threshold | Evidence Needed |
|---|---|---|
| Revenue test | ≥ 80% in-state | Revenue by customer/location schedule |
| Asset test | ≥ 80% in-state | Balance sheet, fixed asset register |
| Proceeds test | ≥ 80% used in-state | Use-of-proceeds budget and tracking |
| Employee test | Majority in-state | Payroll and headcount by state |

---

## Step 3: Build Residency Verification Protocol

Define residency standards for individuals and entities under Rule 147/147A and state law [VERIFY].

| Investor Type | Residency Standard [VERIFY] | Minimum Documents |
|---|---|---|
| Individual | Principal residence in state | Driver license + utility bill or tax record |
| Entity | Principal place of business in state | Operating agreement + business address proof |
| Entity formed for offering | Look-through to owners | Owner residency docs for all beneficial owners |

- Require documentary proof before acceptance and retain in investor file
- Use online gating and IP checks only as supplemental red flags
- Apply look-through review for entities formed to purchase the securities

---

## Step 4: Implement Advertising and Offer Controls

- Apply legends on all materials and landing pages
- Use state-only gating before access to offering materials
- Avoid paid ads that target beyond the state
- Train all personnel not to discuss the offering with non-residents
- Preserve copies of all ads and targeting settings

---

## Step 5: Establish Resale Restrictions and Transfer Controls

- Restricted resale period: six months from issuer sale [VERIFY]
- Place restrictive legends on certificates or book-entry statements
- Issue stop-transfer instructions to transfer agent or internal ledger
- Require approval of any transfer during restricted period

**Legend template:**
```text
THESE SECURITIES HAVE NOT BEEN REGISTERED UNDER THE SECURITIES ACT OF 1933.
FOR A PERIOD OF SIX MONTHS FROM THE DATE OF SALE BY THE ISSUER, ANY RESALE
MUST BE MADE ONLY TO PERSONS RESIDENT WITHIN THE STATE OF [STATE]. ANY
TRANSFER IN VIOLATION OF THIS RESTRICTION IS VOID.
```

**Subscription representation template:**
```text
Subscriber represents that Subscriber's principal residence (or principal
place of business) is in the State of [STATE], and agrees to provide
documentation reasonably requested to confirm residency. Subscriber
acknowledges the securities are restricted and may not be transferred to
non-residents during the applicable restricted period.
```

---

## Step 6: Analyze Integration Risk and State Registration

**Integration analysis:**

| Item | Risk | Mitigation |
|---|---|---|
| Recent offerings | Integration with intrastate | Apply Rule 152 framework and spacing [VERIFY] |
| Concurrent offerings | Confusing investor pools | Separate materials and investor lists |
| General solicitation elsewhere | Contaminates intrastate | Pause or segregate campaigns |

**State registration by qualification plan:**
- Confirm registration path under state law [VERIFY]
- Assemble required forms, consents to service, and filing fees
- Confirm financial statement requirements and audit thresholds [VERIFY]
- Address merit review items: escrow, commissions, pricing, dilution
- Align offering document, state forms, and marketing materials
- File or pre-clear advertising if required [VERIFY]

---

## Step 7: Produce Deliverables

1. **Compliance memo** — rule selection, eligibility analysis, residency controls, advertising controls, resale restrictions, integration analysis
2. **Execution checklist** for issuer and counsel
3. **Draft legend and subscription representations**
4. **State registration filing checklist**
5. **Assumptions, open items, and risk flags**

### Mandatory Front Matter

At the top of every output, include:
1. **Assumptions Used** — rule selected, doing business test results, residency standard applied
2. **Open Items / Needed Inputs** — missing financials, unresolved state law requirements, [VERIFY] items

### Contingencies
- Reject any non-resident subscription and document the rejection
- If a residency error is discovered, consult counsel immediately and assess remediation
- If controls cannot be implemented, recommend alternative exemptions

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the initial memo, ask:

1. Are the doing-business test calculations confirmed against current financials?
2. Is the advertising/distribution plan finalized, or are additional channels planned?
3. Should the residency verification process be tested with a sample investor workflow?
4. Are there concurrent or recent offerings that need integration analysis?

---

## Quality Audit

Before finalizing, verify:

- Safe harbor selection (147 vs. 147A) documented with rationale
- All four doing-business tests analyzed with evidence citations
- Residency verification protocol includes documentary proof requirements
- Legend language matches the correct rule and state
- Advertising controls are enforceable for the planned distribution channels
- Integration analysis covers all offerings in the 6-month look-back and look-forward
- State registration path confirmed with forms and fees identified
- Subscription representations match legend language
- All rule text citations verified or flagged [VERIFY]
- Assumptions and open items listed prominently

---

## Guidelines

- **Attorney review required**: Output is not legal advice; requires licensed attorney review before use
- Mark any unverified rule text, thresholds, or dates with `[VERIFY]`
- Resolve federal vs. state conflicts in favor of the more restrictive rule
- If residency or advertising controls cannot be enforced, recommend a different exemption
- Maintain a single source of truth across forms, disclosures, and marketing
- Preserve all investor residency evidence and advertising records
- Flag broker-dealer or finder compensation issues for separate review
- **Anti-hallucination**: Do not fabricate rule thresholds, state-specific requirements, or registration procedures. Every regulatory citation must be verified or flagged
- **Ethics**: Treat confidentiality and truthfulness obligations as mandatory (Model Rules 1.1, 1.3, 1.6, 3.3, 4.1) [VERIFY]
