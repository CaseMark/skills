---
name: aml-compliance-program
language: en
description: >-
  Drafts and reviews Bank Secrecy Act (BSA) anti-money laundering (AML/CFT)
  compliance programs and policies for U.S. banks, credit unions, money services
  businesses, broker-dealers, mutual funds, insurers, loan or finance companies
  and, from January 1, 2028, investment advisers. Applies the program rule for the
  actual institution type in 31 C.F.R. Chapter X (1020.210, 1022.210, 1023.210,
  FINRA Rule 3310) and ties every control to the institution's own risk
  assessment; tests the BSA officer's authority and resources and the
  independence of independent testing; sets CIP, KYC, customer due diligence
  and beneficial ownership procedures under 1010.230 after the Corporate
  Transparency Act changes; writes SAR, CTR, structuring, SAR confidentiality
  and recordkeeping procedures with each clock from its own trigger; keeps OFAC
  sanctions compliance separate. Use for an AML policy, BSA program, gap
  analysis or board approval package. Routes transaction-level testing and SAR
  narratives to auditing-aml-transactions.
tags:
  - regulatory
  - policy
  - drafting
  - analysis
  - checklist
---

# AML Compliance Program

Drafts a new or updated BSA/AML compliance program, or a single policy or procedure within one, for a U.S. financial institution, or reviews an existing program element by element, so that the institution detects and reports suspicious activity and meets its recordkeeping and reporting duties. The deliverable is the program text or gap review, a rule map for the institution's type, a risk assessment linkage matrix, a clocks and retention table, ranked gaps, a reconciliation table and hand-offs, in the layout of `references/output-template.md`. Every output is a draft for review by counsel and the institution's BSA/AML officer before board or senior management approval.

## Why This Skill Exists

AML programs fail examinations in predictable places, and most of them are visible on paper before an examiner arrives. A downloaded template carries sections for products the institution does not offer and nothing for the ones its own risk assessment rates highest. A money transmitter copies its bank partner's policy and inherits a $5,000 SAR threshold and a 60-day filing extension that its rule does not give it. A procedure starts the SAR clock when the investigator closes the case. The BSA officer is a part-time branch manager reporting to the head of retail, and the person who tests the program reports to that officer. A beneficial ownership form asks for owners of "more than 25%" and stops when one is found. A policy drops beneficial ownership collection because U.S. companies no longer report to FinCEN. OFAC screening sits inside the BSA chapter with a five-year retention period. Each of these is a citable deficiency. The rules also moved in 2025 and 2026, so the program has to say which rules are in force and which are only proposed.

## Where Mistakes Hide

| Input / Document | What It Is Used For | Where the Error Hides |
|---|---|---|
| Charter, license, FinCEN registration, SEC or CFTC registration, regulator and SRO | Choosing the program, SAR and CDD rules for the institution type | Bank rule 1020.210 applied to an MSB; the 60-day "no suspect" extension given to an MSB (1022.320 has none); 1010.230 imposed on an MSB as law; FINRA 3310 annual testing missed for a broker-dealer; MSB FinCEN registration renewal, the January 1 agent-list revision, and 180-day re-registration after a more than 10% ownership transfer or a more than 50% increase in agents left out of an MSB program (1022.380); Part 1032 treated as in force before January 1, 2028; the April 2026 proposed program rule treated as final |
| Risk assessment (products, services, customers, geographies, channels; inherent and residual) | Sizing every control | Generic template not tied to it; sections for foreign correspondent or private banking the institution does not offer; no controls for its highest-rated rows; one review cycle for every customer; risk assessment stale after a new product; National Priorities never reviewed |
| The request itself: who asks, for what, and to what end | Scope and authority of the drafting | A request to design procedures that avoid SAR filing, exempt favored customers from SAR decisions, coach customers to stay under $10,000, or tell a customer a SAR was filed, accepted as an ordinary drafting task |
| Org chart, BSA officer job description, board minutes, budget | Approval body; officer designation, authority, independence, resources | Officer reports to a revenue line, is part-time with no staff or budget, or is outside the U.S.; program approved by a body the rule does not name; appointment treated as enough |
| Independent testing engagement letter, audit reports | Independent testing | Tester is the BSA officer, a direct report, or the consultant who wrote the policies; MSB "independent review" done by the designated compliance person; a fixed frequency asserted as a bank regulation |
| Alert logs, case files, SAR decision records | SAR thresholds and clocks | Clock from case closure or from the alert date instead of initial detection; extension used when the subject is known; continuing-activity review called a legal requirement; continuing SAR anchored to detection instead of the prior filing |
| Teller scripts, exit letters, subpoena procedures | Customer-facing and third-party communications | Script explains how to keep deposits under the CTR threshold; closure letter or call reveals a SAR; subpoena response produces the SAR instead of declining and notifying FinCEN |
| Legal entity onboarding form, beneficial ownership certification, operating agreements | CDD and beneficial ownership | "More than 25%" instead of "25 percent or more"; holding-company ownership not looked through; control person dropped; CTA reporting exemption read as ending CDD collection; certification relied on despite facts that call it into question |
| Sanctions policy, screening procedures, OFAC reports | OFAC compliance | Treated as a BSA element; five-year retention instead of ten; rejected-transaction reports omitted; foreign branches excluded; strict liability treated as risk tolerance |
| Record retention schedule | Retention periods and start events | Beneficial ownership verification records kept from account closure instead of record creation; SAR retention from detection instead of filing |

## Ground Rules

1. **Draft only.** Nothing is filed, adopted or sent. Every output is a draft for counsel and BSA/AML officer review and is never called final or approved.
2. **Source-review gate.** Never call a document missing until the inventory has been checked and the file opened, with OCR or extraction tried. Classify every open item as one of four gap classes: *unknown fact* (who the officer reports to), *source conflict* (policy says board approval, minutes show a committee), *unverified external lookup* (a state MSB rule not in `references/primary-sources.md`), or *policy election* (re-certifying beneficial owners at every new account).
3. **Hierarchy of authority.** For law: 31 U.S.C. and 31 C.F.R. Chapter X as currently in force, then the functional regulator's program rule and SEC-approved SRO rules, then FinCEN orders and exceptive relief, then interagency FAQs and FinCEN guidance, then the FFIEC manual, then proposed rules (never binding), then vendor templates. For facts: board minutes and executed documents, then system configurations and logs, then policy descriptions, then interviews. Name every conflict in the reconciliation table (the FFIEC manual's five-year OFAC retention against 31 C.F.R. 501.601's ten years) and state which controls; never resolve one silently.
4. **Citation discipline.** Every rule statement carries its section and comes from `references/primary-sources.md`, or is marked `[VERIFY]`. Every fact about the institution carries a source locator (document, page or section) or `[UNVERIFIED]`. Re-read the current eCFR text of each rule relied on before the program goes for approval. Never invent a citation, threshold or deadline.
5. **Institution type first.** Determine each entity's type, regulator and SRO before drafting, and use that type's program, SAR and CDD rules. Never transplant a bank provision into a non-bank program without labeling it a policy election.
6. **The risk assessment drives the program.** Every section answers a row of the institution's own risk assessment or a stated legal minimum. A high-rated risk without a control is a Critical gap; template text for products not offered is removed or marked not applicable with its basis.
7. **Current law, labeled.** State what is in force on the date checked. The April 10, 2026 proposed program rule, the 2026 banking agency proposals, and the investment adviser rule before January 1, 2028 are labeled proposed or not yet effective; their elements may be adopted only as labeled design choices.
8. **Clocks from their own triggers.** Each SAR, CTR, exemption and OFAC deadline is computed from the trigger its rule uses, with dates and weekdays. An alert is not initial detection; case closure is not either.
9. **No evasion, no tipping off.** Decline to draft any procedure, threshold, script or exception whose purpose is to avoid filing a required SAR or CTR, to help or advise a customer to structure, or to reveal a SAR; produce the compliant alternative instead. Legitimate aims stated in the same request (fewer false-positive alerts, shorter customer conversations, faster closures) are met by compliant means.
10. **SAR confidentiality everywhere.** Every procedure that touches a SAR (exit letters, subpoenas, affiliate sharing, employment references, board reporting when a director is the subject) carries the confidentiality rule and the permitted channels.
11. **Officer and tester are tested on facts.** Assess the BSA/AML officer's authority, independence, resources, competence and U.S. location, and the tester's independence under the governing rule, from documents; a title alone proves nothing.
12. **Sanctions stand apart.** OFAC compliance is a separate regime under 31 C.F.R. Chapter V with strict civil liability, its own reports and ten-year records; it may share people and systems but never sits as a BSA element.
13. **Program design here; transaction testing elsewhere.** This skill writes and reviews the program and policies. Testing actual transactions, lookbacks and SAR narratives go to auditing-aml-transactions.

## Checkpoint A: Pre-Draft Intake (Mandatory)

Collect, from documents where possible:

1. Today's date; the requester and their role (BSA officer, counsel, consultant, management); the deliverable (new program, update, gap review, single policy or procedure); the approval date targeted.
2. Each entity's legal name and type: charter or license, functional regulator, SRO, FinCEN MSB registration and agent list, SEC registration (advisers), states of operation.
3. The current risk assessment with its date, methodology and ratings; any new products, channels, acquisitions or customer segments since.
4. The existing program, policies and procedures, with approval records (board or senior management minutes).
5. Organization chart, BSA/AML officer job description, reporting line, staffing and budget; location of the officer.
6. Independent testing: engagement letters, last two reports, who performed them and to whom they reported; remediation status.
7. Examination reports, MRAs, consent orders and lookback findings still open.
8. Customer onboarding forms, beneficial ownership certification, CIP procedures, risk-rating model, periodic review cycles.
9. Monitoring system scenarios and thresholds, alert and case workflow, SAR committee charter, SAR and CTR volumes.
10. Sanctions policy, screening lists and timing, blocking and reporting procedures.
11. Training plan, audiences and completion records; record retention schedule.

**Defaults if not supplied** (a governing rule overrides any default it addresses): rules as checked on today's date in `references/primary-sources.md`; risk assessment "not supplied," treated as a Critical item and routed to bsa-risk-assessment while the draft proceeds on the institution's described products; approval body as the institution-type table names it; independent testing every 12 to 18 months for banks as a risk-based design choice, but annual on a calendar-year basis for broker-dealers under FINRA 3310(c); beneficial ownership identified at first account opening and on reliability or risk triggers under FIN-2026-R001; no continuing-activity review schedule unless the institution elects one; OFAC records ten years.

**Hard stops (label "Declined: hard stop"; produce the request, routing or compliant alternative, not the requested text):**
1. The request is for a procedure, threshold, script or exception whose purpose is to avoid filing a required SAR or CTR, to exempt particular customers from SAR decisions, to advise or help customers structure transactions, or to evade sanctions screening.
2. The request is to disclose a SAR, or information that would reveal one, to the subject or any person outside the channels in 1020.320(e) and its analogs (customer letters or calls, civil discovery production).
3. No entity's institution type can be determined from the documents and the requester cannot state it: produce the intake request and the institution-type determination table only.

**Not hard stops:** a missing or stale risk assessment, an officer without authority or resources, a non-independent tester, or a proposed rule in the request (each is a Critical item; status "Not ready: blocking issues"); multiple institution types in one group (map each).

## Step 1: Institution Type and Rule Map

Read `references/program-rules-by-institution.md`, sections 1 and 7. Fill Part 2 of `references/output-template.md` for every entity: program rule, SAR rule with threshold and deadline, CDD and 1010.230 coverage, approval body, independent testing standard, other regimes. Record the rule-status line with the date checked. If any entity's type is undeterminable, stop at the intake request (hard stop 3).

## Step 2: Screen the Request

Read `references/sar-ctr-and-sanctions-rules.md`, section 6. Compare each requested item against the hard stops. For any item that fires, label it "Declined: hard stop," state why, and draft the compliant alternative; continue with the rest of the request.

## Step 3: Tie the Program to the Risk Assessment

Read `references/program-rules-by-institution.md`, section 3. Build the Part 3 matrix: each risk row, its rating and source page, the section that answers it, the control strength and the residual rating. Flag template residue and uncovered high-rated rows as Critical. Record the National Priorities review. Route a missing or stale assessment to bsa-risk-assessment.

## Step 4: Governance, Officer and Approval

Read `references/program-rules-by-institution.md`, section 4. Name the approval body the rule requires and compare it with the approval record. Test the officer against the authority, independence, resources, competence and location table, citing the documents; recommend the board resolution, reporting line and resources needed.

## Step 5: CIP, CDD and Beneficial Ownership

Read `references/program-rules-by-institution.md`, section 6. Draft or test customer risk profiles, risk tiers and review cycles by tier, EDD triggers, and, for covered institutions, the beneficial ownership procedure: 25 percent or more with look-through to individuals, one control person always, trust and exclusion rules, timing under FIN-2026-R001 with the reliability trigger, verification, and both retention start events. Explain that the Corporate Transparency Act reporting changes do not alter 1010.230.

## Step 6: Monitoring, SAR, CTR and Confidentiality

Read `references/sar-ctr-and-sanctions-rules.md`, sections 1 to 5. Write the alert-to-decision workflow with a review time standard and dual control; quote the SAR definitions and the threshold for the type; fill the Part 5 clock table with one trigger per row; state continuing-activity reviews as elective; draft CTR aggregation, exemption and structuring-detection procedures; put the confidentiality rule and permitted channels into each procedure that touches a SAR.

## Step 7: Training and Independent Testing

Read `references/program-rules-by-institution.md`, section 5. Set role-based training audiences, content and frequency. Name who may test under the governing rule and who may not, the reporting line to the board or committee, scope tied to the risk assessment, frequency, and remediation tracking. A tester who fails the independence test is a Critical gap.

## Step 8: Sanctions Program, Retention and Assembly

Read `references/sar-ctr-and-sanctions-rules.md`, sections 7 and 8. Draft or test the sanctions compliance program as a separate document or chapter with OFAC's five components, its reports and ten-year records. Fill the retention table with start events. Assign the status label and finding labels exactly as in `references/output-template.md`, rank gaps by severity, complete the reconciliation table, hand-offs, open items and every `[VERIFY]` item with what would settle it.

## Checkpoint B: Post-Draft Alignment

Confirm with the user or state as open items:

1. Is each entity's type, regulator and SRO correct, and has the rule status been re-checked on the approval date?
2. Does every high-rated risk have a control, and has template residue been removed?
3. Will the board or senior management give the officer the authority, reporting line and resources the draft recommends?
4. Is the independent tester independent under the governing rule, and does the tester report to the board or a committee?
5. Does the institution elect any optional practices (per-account beneficial ownership re-certification, continuing-activity reviews, written no-SAR rationales)?

If the user does not answer, recommend confirming the risk assessment and the officer's mandate first; those are the most common reasons a program is cited.

## Quality Audit

Before responding, confirm each statement. If one fails, fix the draft.

1. Each entity's institution type is stated, and every program, SAR and CDD provision cites that type's rule.
2. No bank-only provision (60-day extension, 1010.230, 1020.315 exemptions) appears as law in a non-bank program.
3. Every program section maps to a risk assessment row or a cited legal minimum, and every high-rated row has a control.
4. The approval body matches the rule, and the officer's authority, independence, resources and U.S. location are tested from documents.
5. The independent tester is independent under the governing rule (FINRA 3310.01(c), 1022.210(d)(4), FFIEC manual), with a reporting line to the board or a committee.
6. Each clock in Part 5 has its own trigger, date and weekday; no SAR clock starts at alert generation or case closure.
7. Continuing-activity review is described as elective, and any continuing SAR is anchored to the prior filing date.
8. The beneficial ownership procedure uses 25 percent or more, looks through entities, always names one control person, and treats CTA reporting changes as leaving 1010.230 unchanged.
9. No text in the output coaches structuring, exempts customers from SAR decisions, or reveals a SAR; each declined item has a compliant alternative.
10. OFAC compliance is a separate program or chapter with ten-year records and 10-business-day reports.
11. Proposed and not-yet-effective rules are labeled as such with the date checked.
12. Status and finding labels are used exactly as in `references/output-template.md`, and every rule cited is in `references/primary-sources.md` or marked `[VERIFY]`.
13. The output closes with the draft-for-review line.

## Guidelines

- Write for the board and the examiner at once: plain statements of who does what, by when, with what authority, and why the control fits this institution's risks.
- Prefer the institution's own terms for products and systems; define each acronym once.
- Be definite about what the rule requires and separate it from what the institution elects. Mark elections as such so a later change does not look like a violation.
- Smaller, lower-risk institutions may keep programs short; risk-based does not mean optional, and each pillar still appears.
- When a user instruction conflicts with a rule (keep the 60-day extension for an MSB, let the officer test the program), draft the compliant version and explain the change.
- Keep SAR facts out of the program document itself; examples use fictional customers.

## Troubleshooting

| Problem | Likely cause | What to do |
|---|---|---|
| Existing policy is a scanned PDF and partly unreadable | Image-only scan | Try OCR; list unreadable sections; review what is readable and mark dependent findings `[UNVERIFIED]` |
| Policy, minutes and org chart disagree on the BSA officer or approval body | Stale policy cover page | Use the minutes and org chart; record the conflict in Part 7; list a policy update |
| Risk assessment ratings conflict with the volumes reported | Methodology not updated | Flag as source conflict; draft to the higher rating; route the refresh to bsa-risk-assessment |
| Entity looks like both an MSB and a bank program manager | Fintech partnership | Map each role; the bank partner's program covers its customers; the fintech's MSB status is `[VERIFY]` under 1010.100(ff) |
| User cites a "new FinCEN rule" by name only | Proposal or press coverage | Check its status; if proposed, label it and offer its elements as design choices |
| Requester wants the program "exam-ready by Friday" with no risk assessment | Time pressure | Draft on described products, status "Not ready: blocking issues," and put the risk assessment first in next steps |

## Related Skills

- auditing-aml-transactions: hand off transaction-level testing, red-flag screening of actual transactions, lookbacks and SAR narrative drafting; this skill covers program design and policy.
- bsa-risk-assessment: hand off when the risk assessment is missing, stale, or omits a product, channel or acquisition.
- cip-policy: hand off a standalone customer identification program policy.
- reviewing-kyc-documentation: hand off review of individual customer files against the CIP, CDD and EDD procedures written here.
- managing-sanctions-screening: hand off screening design, match investigation and escalation detail for the sanctions program.
- legal-research: hand off state MSB licensing law, foreign AML law, payment stablecoin issuer rules and other rules outside this skill's register; no dedicated skill covers them.

## Reference Files

- `references/program-rules-by-institution.md`: institution-type rule table, program components, risk assessment linkage, governance and officer tests, independent testing, CDD and beneficial ownership after the CTA changes, rule status as of 2026-10-30.
- `references/sar-ctr-and-sanctions-rules.md`: clocks table, SAR decision design, continuing activity, CTRs and structuring, SAR confidentiality, declined requests with alternatives, retention schedule, OFAC as a separate regime.
- `references/output-template.md`: deliverable layout, status and finding labels, rule map, linkage matrix, clock format, severity scale, reconciliation table, hand-off table.
- `references/primary-sources.md`: every authority checked with URL, method, what it supports and date checked, plus the `[VERIFY]` list.
