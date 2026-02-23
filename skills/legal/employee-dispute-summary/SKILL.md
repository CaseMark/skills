---
name: employee-dispute-summary
description: Produces a structured, source-cited summary of U.S. employment disputes for HR and litigation review, covering allegations, responses, procedural history, resolutions, risks, and next steps. Use for HR investigations, EEOC/agency matters, discrimination, harassment, retaliation, wrongful termination, wage-hour disputes, grievance/arbitration files, or when asked to “summarize an employee dispute” or “employment litigation summary.”
tags:
  - litigation
  - summarization
  - summary
---

# Employee Dispute Summary

Create an objective, source-cited summary of an employee dispute for HR and legal decision-making.

## Prerequisites

1. **Source corpus**: complaints, witness statements, investigation reports, correspondence, disciplinary records, employment agreements, policies/handbooks, performance reviews, agency filings, pleadings, settlement docs.
2. **Parties list**: all individuals/entities with roles and relationships.
3. **Timeline anchors**: key dates, deadlines, hearings, and process milestones.
4. **Forum details**: internal process, arbitration, EEOC/state agency, court, union grievance.
5. **Resolution terms**: any settlement, award, or decision documents, if applicable.

## Output Structure / Process

1. **Executive Overview** (2–3 sentences)
   - Nature of dispute, core claims, current status, and immediate next step.
2. **Parties and Roles**
   | Party | Role | Relationship | Counsel/Rep | Source |
   |---|---|---|---|---|
3. **Allegations Matrix**
   | Allegation | Claim Type | Alleged Conduct | Dates/Locations | Witnesses | Policy/Statute Cited | Status | Source |
   |---|---|---|---|---|---|---|---|
4. **Responses and Defenses**
   | Party | Position | Admissions | Denials | Affirmative Defenses | Disputed Facts | Source |
   |---|---|---|---|---|---|---|
5. **Procedural History Timeline**
   | Date | Event | Forum/Process | Outcome/Status | Next Deadline | Source |
   |---|---|---|---|---|---|
6. **Resolution / Outcome (if any)**
   | Resolution Type | Date | Monetary Terms | Non-Monetary Terms | Confidentiality/Non-Admission | Appeal/Review Status | Source |
   |---|---|---|---|---|---|---|
7. **Findings / Determinations**
   | Decision-Maker | Finding | Standard Applied | Scope | Effective Date | Source |
   |---|---|---|---|---|---|
8. **Outstanding Issues and Next Steps**
   - [ ] Open factual disputes
   - [ ] Pending procedural steps
   - [ ] Required notices/approvals
   - [ ] Evidence gaps to close
   - [ ] Decision points for HR/Legal
9. **Risk and Policy Impact**
   | Risk Area | Exposure Level | Rationale | Potential Remedies | Policy/Operational Impact | Source |
   |---|---|---|---|---|---|
10. **Source Map**
    | Fact/Assertion | Source Doc ID | Page/Section | Confidence |
    |---|---|---|---|
11. **Gaps / Additional Information Needed**
    - List missing documents, unclear facts, or unverified assertions.

**Source Handling Rules**
- Tag each factual assertion with a source marker like `[Doc-12]`.
- If quoting, use quotation marks and cite the document and page/section.
- If a fact is disputed, state both positions and label as **Disputed**.

## Guidelines

- Maintain neutrality; do not assess credibility or intent.
- State legal conclusions only if formally determined by a court, arbitrator, or agency.
- Identify the governing policy version and effective date when cited.
- Note any privilege or confidentiality restrictions; avoid reproducing sensitive material beyond what is necessary.
- If jurisdiction is unclear or non-U.S., flag it explicitly and adjust labels; use `[VERIFY]` for uncertain citations.
- Highlight anti-retaliation and preservation obligations when implicated by the facts.
- Keep the document concise and scannable; target 2–5 pages for complex matters.
