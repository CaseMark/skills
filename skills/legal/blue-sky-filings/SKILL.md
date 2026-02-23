---
name: blue-sky-filings
description: Produces a practitioner-grade Blue Sky compliance memorandum and execution plan for U.S. securities offerings. Analyzes NSMIA covered securities preemption, classifies offerings under Regulation D/Rule 506 or alternative federal exemptions, maps state jurisdictional nexus distinguishing offers from sales, and generates a state-by-state filing plan with Form D/EFD workflow, fee schedules, amendment triggers, and renewal calendars. Embeds anti-hallucination guardrails requiring primary-source citations or [VERIFY] flags for all state-specific requirements. Use when advising on private placement Blue Sky compliance, Reg D notice filings, multi-state offering coordination, or state securities registration exemptions.
tags:
  - analysis
  - checklist
  - corporate
  - drafting
  - memo
  - regulatory
  - research
---

# Blue Sky Filings Compliance Workflow

Produces an integrated Blue Sky compliance memo and execution plan: jurisdictional nexus analysis, NSMIA/Reg D exemption memo, and state-by-state filing plan with timelines and recordkeeping requirements.

## Prerequisites

1. **Offering summary** — security type, aggregate amount, price/valuation, planned closing dates, single-close vs. rolling/evergreen
2. **Federal legal basis** — Rule 506(b), 506(c), 504, Section 4(a)(2), Reg S, registered offering, Rule 147/147A, or other
3. **Offering documents** — PPM, investor deck, term sheet, subscription agreement, investor questionnaire, AV verification procedures (if 506(c))
4. **Investor geography** — state of residence/domicile (individuals) or principal place of business (entities); states where offers were directed
5. **Intermediaries** — identity, geographic footprint, and state registration status of any broker-dealers, finders, or placement agents
6. **First sale date** — confirmed or projected; confirm internal definition used
7. **Prior filings** — any existing Blue Sky matrices, prior Form D filings, or ongoing offerings

Optional: priority investor states, issuer type (reporting company, fund, private operating company), non-U.S. investors (Reg S interplay), expected secondary transfers or SPV structures.

## Output Structure / Process

### Step 1 — Federal Posture & Covered Security Classification

Identify whether securities are "covered securities" under 15 U.S.C. § 77r [VERIFY: https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title15-section77r].

| Category | NSMIA Section | Preempts State Registration? | State Authority Preserved |
|---|---|---|---|
| Exchange-listed securities | 18(b)(1) | Yes | Fraud enforcement |
| Registered investment company securities | 18(b)(2) | Yes (Form NF, not Form D) | Fraud enforcement |
| Rule 506(b) / 506(c) offerings | 18(b)(4)(F) | Yes | Notice filings, fees, consent to service, fraud |
| Rule 504 offerings | — | No | Full state registration authority |
| Rule 147/147A intrastate | — | No | Full state registration authority |
| Section 4(a)(2) (without Rule 506) | — | Generally no | Full state registration authority |

For non-covered securities, analyze state pathways: registration by coordination, registration by qualification (merit review states), registration by notification/filing, or available state transactional/issuer exemptions.

**Document:** factual basis for exemption selection — whether general solicitation occurred (506(b) vs. 506(c) determination), how investor qualification was verified, and why all exemption conditions are satisfied.

### Step 2 — Jurisdictional Nexus Map (Offers vs. Sales)

For each state, document the factual hook triggering Blue Sky obligations:

- Location of investors who **received offers** (especially critical in 506(c) general solicitation offerings)
- Location of investors who **completed purchases**
- Location of issuer personnel conducting solicitation
- Accessibility of marketing materials in additional states

**Entity investors:** principal place of business, state of formation, and location of the investment decision-maker may each matter — confirm which address concept the subscription agreement uses for Blue Sky representations.

**Negative space:** document states considered and excluded, with reasoning (e.g., "employees located here but no solicitation activity and no investors expected").

**Evidence to preserve:** where subscription materials were sent, investor residency representations, where acceptance occurred, wire origin records.

### Step 3 — State-by-State Compliance Pathway

For each state, specify:

| Field | Content |
|---|---|
| Federal basis | Exemption relied upon |
| Preempted? | Yes / No per Step 1 |
| State filing method | EFD / direct filing / state portal |
| Forms required | Form D copy, Form U-2 (consent to service), state-specific forms |
| Fee | Amount + calculation basis [VERIFY] |
| Deadline | Days after first sale [VERIFY] |
| Renewal required? | Yes/No; if yes, annual anniversary date |
| Source URL | Link to state regulator's current filing page, or [VERIFY] flag |

**Intermediary check:** NSMIA does not preempt state broker-dealer registration. Confirm placement agents/finders are registered in each solicitation state — an unregistered intermediary can jeopardize the issuer's exemption.

**State-specific flags** (all require verification against current regulator guidance before reliance):
- **New York** — Rule 506 offerings accepted via EFD; legacy GBL § 359-e may add complexity for certain structures [VERIFY]
- **California** — Section 25102(f) exemption for non-Rule-506 private placements requires pre-existing relationships; stricter than federal standards [VERIFY]
- **Texas / Washington** — Known to issue comments on notice filings if risk disclosures deemed insufficient [VERIFY]
- **Merit review states** — Confirm state does not impose additional conditions on covered security notice filings beyond Form D + fee

### Step 4 — Form D & EFD Filing Workflow

**SEC Form D timing:** File via EDGAR no later than **15 calendar days** after first sale. [VERIFY current instructions at https://www.sec.gov/info/edgar/sitefaq.htm]

"First sale" = issuer first receives irrevocable consideration (subscription accepted + payment received — not distribution of offering materials or investor expressions of interest).

**Filing checklist:**
- [ ] Confirm first sale date and implicated states for first closing
- [ ] Verify Form D fields match offering documents: issuer legal name, jurisdiction, executive officer names, total offering amount, minimum investment, exemption boxes, non-accredited investor inclusion
- [ ] File Form D via EDGAR
- [ ] Submit state notices via EFD (participating states) or direct filing (non-EFD states); pay applicable fees
- [ ] Save conformed copies, fee receipts, and state acceptance confirmations to deal closing binder
- [ ] Complete **Rule 506(d) bad actor screening** for all covered persons (issuer, directors, officers, GPs, managing members, compensated solicitors) — a disqualifying event eliminates Rule 506 and NSMIA preemption entirely

**Multi-closing offerings:** File additional state notices for each new investor state at or before first sale in that state.

**Fee budgeting:** Fees range from ~$100 flat to percentage-based calculations with caps, varying significantly by state. Aggregate fees across many states can be material — budget in advance. [All specific fee amounts require current verification.]

### Step 5 — Amendments, Renewals & Closing Filings

**Form D amendment triggers:**
- Adding general solicitation to a 506(b) offering (requires restructuring to 506(c))
- Change to minimum investment amount
- Addition or change of placement agent
- Expansion into new investor states
- Material change to use of proceeds
- Increase in total offering amount

**Amendment process:** File SEC Form D amendment via EDGAR + file new/amended state notices in all affected states.

**Renewal obligations:** Many state notice filings expire **12 months** after initial filing date. Rolling/evergreen offerings must renew before expiration — a compliance gap during a lapsed period may create rescission exposure for investors who purchased during that window. Deliver a compliance calendar to the client before closing listing every expiration date.

**Closing/final filing:** Upon offering completion, file a Form D amendment reporting total amount sold and offering close with the SEC and affected states.

**Internal escalation protocol (embed in client memo):** "If any investor is added in a state not on the current Blue Sky tracker, counsel must be notified before circulating final subscription documents, and no funds shall be accepted until state notice filing method and timing requirements are confirmed."

### Step 6 — Deliverable Structure

Produce a memo with three integrated layers:

1. **Executive Summary** (for CFOs/board) — plain language: what must be done, by when, who is responsible
2. **Legal Analysis** — covered securities/preemption framework, chosen exemption and conditions, limits of state authority
3. **Implementation Section** — state-by-state filing plan (narrative with embedded specifics), recordkeeping requirements, escalation rules, compliance calendar

Include a mandatory **"Assumptions and Open Items"** section listing every [VERIFY] item with:
- What needs to be confirmed
- Where/how to confirm it (e.g., "Confirm on [State] Securities Division website page titled 'Rule 506 Filings' and archive page to deal binder")
- Who is responsible and by when

## Guidelines

- **Anti-hallucination:** Every state-specific requirement (deadline, fee, form, portal) must cite a verifiable primary source URL or carry a `[VERIFY]` flag with verification instructions — never state state law requirements as facts without sourcing
- **Rescission framing:** Primary litigation risk for filing failures is investor rescission under Section 12 of the Securities Act and analogous state provisions (e.g., Section 410 of the Uniform Securities Act [VERIFY]) — frame all compliance gaps in terms of this concrete exposure
- **Offer ≠ Sale:** Do not conflate offer states and sale states; Rule 506(c) general solicitation may expand the offer footprint significantly beyond the sale footprint; confirm whether each state requires notice for offer-only activity
- **No merit review for covered securities:** NSMIA preempts state substantive review of offering terms (compensation, warrant coverage, dilution) for Rule 506 — but confirm state is not attempting to impose it
- **Form D consistency:** Total offering amount on state EFD filings must exactly match Part C, Question 1 of the SEC Form D — discrepancies are a common trigger for regulatory inquiries
- **Local counsel:** For merit review states, high-profile offerings, or states with aggressive enforcement postures, recommend engaging local Blue Sky counsel for confirmation
- **Confidentiality:** Treat all drafts as privileged attorney work product; limit distribution; issuer and investor information (identities, residency, financials) is confidential under Model Rule 1.6
- **Scope:** Covers Blue Sky analysis and filing planning for U.S. private placements under Regulation D. Does not cover: rescission litigation, EDGAR credential setup, SEC registration statement preparation, non-securities state regulatory requirements, or substantive state merit review analysis

---
*All output is LLM-assisted draft guidance requiring attorney review before use or filing. Does not constitute legal advice. State administrative rules and fee schedules change frequently; verify all state-specific requirements via primary sources before reliance.*
