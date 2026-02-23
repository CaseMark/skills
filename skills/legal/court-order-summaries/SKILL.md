---
name: court-order-summaries
description: Generates structured summaries of court orders and decisions, distilling obligations, deadlines, monetary awards, injunctive relief, and procedural requirements into a clear reference document. Flags ambiguities for attorney review rather than interpreting gaps. Converts relative timeframes to specific calendar dates. Designed for post-trial and compliance contexts across U.S. litigation. Use when summarizing court orders, judgments, injunctions, consent decrees, or compliance orders.
tags:
  - litigation
  - summarization
  - summary
---

# Court Order Summary

Transforms a court order into a structured, action-oriented reference document covering who must do what, by when, and with what consequences.

## Prerequisites

1. Full text of the court order (with entry date visible)
2. Identification of all named parties and their roles
3. Applicable court rules for computing time (to calculate deadline dates)

## Output Structure

### 1. Executive Overview *(2–3 sentences)*
Core holding, most urgent deadline, and primary obligated party.

> ⚠ Flag any provisions requiring **immediate action** (TROs, preliminary injunctions, <10-day deadlines) here.

---

### 2. Parties & Roles

| Party | Role | Obligations Under This Order |
|-------|------|------------------------------|
| [Name] | Plaintiff/Defendant/Third Party | Brief description |

---

### 3. Deadlines & Required Actions

| Party | Action Required | Deadline (Specific Date) | Order Ref. | Consequence if Missed |
|-------|----------------|--------------------------|------------|----------------------|
| | | | ¶/p./§ | |

- Convert all relative timeframes (e.g., "within 30 days") to specific calendar dates from the order's entry date
- Account for weekends, court holidays, and applicable time-computation rules
- Note any automatic stays or deadline suspensions pending appeal

---

### 4. Monetary Obligations

| Obligor | Obligee | Amount | Type (judgment/sanction/fee/bond) | Due Date | Order Ref. |
|---------|---------|--------|-----------------------------------|----------|------------|

---

### 5. Injunctive / Equitable Relief

| Type | Party Bound | Specific Conduct Required or Prohibited | Duration / Conditions | Order Ref. |
|------|------------|----------------------------------------|----------------------|------------|
| Mandatory injunction | | | | |
| Prohibitory injunction | | | | |

---

### 6. Procedural & Ongoing Requirements

- Reporting obligations (frequency, recipient, format)
- Notice provisions
- Compliance certifications
- Court supervision or monitoring requirements

---

### 7. Findings & Future Proceedings

- Key findings of fact or conclusions of law with precedential or preclusive effect
- Rights preserved or limited (appeal, modification, enforcement)
- Conditions precedent or contingent obligations

---

### 8. Ambiguities & Attorney Review Items

List any provisions that are unclear, internally inconsistent, or require legal interpretation. Do **not** resolve ambiguities — flag them.

---

## Guidelines

- **Fidelity**: Reproduce deadlines and obligations verbatim or in direct paraphrase; never paraphrase in a way that changes scope
- **No gap-filling**: If the order is silent on a consequence or procedure, say so — do not infer
- **Cite everything**: Every obligation, deadline, and finding must reference its paragraph, page, or section number
- **Plain language**: Use accessible terms where possible; retain legally significant terms of art with brief parenthetical context
- **Immediate flags first**: Anything actionable within 7 days must appear in the Executive Overview
- **Jurisdiction**: U.S. federal and state courts; note the specific court and jurisdiction on the summary header
