---
name: analyzing-m-and-a-tax-implications
language: en
description: >
  Evaluates federal income tax effects of buying or selling a business and of
  reorganizations: stock versus asset purchase; step-up elections under
  338(h)(10), 336(e) and 338(g); pre-sale reorganizations such as an F
  reorganization before a sale; converting a corporation into an LLC, a taxable
  liquidation or deemed sale; 368 reorganizations and continuity of interest;
  1060 allocation and Form 8594; 197, bonus depreciation, 174A; acquired losses
  and Section 382 and 382(h); and 280G. Covers the tax treatment of deferred,
  contingent, earnout and rollover consideration (installment sales under 453 and
  453A, rollover under 351, 721 or 368); supplies tax analysis behind tax
  representations, tax indemnity and straddle-period allocation in acquisition
  agreements; and analyzes tax audits, elections and open tax matters disclosed in
  schedules or found in diligence. Routes entity choice, S corporation eligibility, QSBS and
  consolidated-group questions to analyzing-corporate-tax-structures. Drafts for
  tax adviser review.
tags:
  - analysis
  - tax
metadata:
  author: casemark
  practice_areas:
    - Tax Planning
    - Tax Compliance
    - International Tax
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---

# Analyzing M&A Tax Implications

Evaluates the U.S. federal income tax consequences of an acquisition, disposition or reorganization for the buyer, the sellers and the target: which structures and elections are available, whether a reorganization or rollover is tax-deferred, how deferred, contingent and rollover consideration is taxed, how the price is allocated, what happens to tax attributes and change-in-control payments, and what the tax representations and tax indemnity must cover. The deliverable follows `references/output-template.md` and ends with ranked issues, hand-offs and open items. Everything it produces is a draft for review by a qualified tax adviser; it is not a tax opinion and not legal, accounting or investment advice.

## Why This Skill Exists

Deal tax fails on facts about parties and dates more often than on arithmetic. An election is proposed for a target whose owners cannot make it. A merger's stock percentage is measured at closing when the regulations fix it at signing. Rollover shares are called tax-free though the people transferring property do not control the company that issues the stock. An earnout is reported as capital gain in the year of sale although it is contingent and forfeited if the founder quits. Buyer and seller file different allocations. A tax indemnity covers "the Company's taxes" while the target is liable for its former parent's whole consolidated return. This skill makes each of those determinations explicit, computes every percentage and amount from the documents, and dates every rule.

## Where Mistakes Hide

| Input / Document | What It Is Used For | Where the Error Hides |
|---|---|---|
| Cap table, entity documents and the seller's filing status (consolidated return, S election, partnership) | Which elections are available and who must make or consent to them | 338(h)(10) or 336(e) proposed for a C corporation owned by a fund partnership or individuals; nonselling S shareholders' consent missing; an invalid (h)(10) treated as falling back to a 338(g) election; the buyer is not a corporation, so there is no qualified stock purchase |
| Pre-sale step plan (Newco, QSub election, LLC conversion, F reorganization) | Delivering a step-up from an S corporation without a 338(h)(10) | The F reorganization step reported as a taxable event; the later sale of LLC interests treated as a stock sale; S election validity never checked; state recognition of the steps assumed |
| Merger agreement consideration terms, signing date and pre-signing stock price | Continuity of interest and the reorganization type | Stock percentage measured at closing instead of on the pre-signing date for fixed consideration; boot share too large for COI; the 80 percent voting stock test of 368(a)(2)(E) ignored; liabilities not counted as money in a C reorganization with boot |
| Rollover, contribution and holding company documents | Deferral for sellers who roll equity | 351 control missed because the sponsor's stock was issued earlier or for property of relatively small value; a partnership rollover with cash triggering a disguised sale; rollover into acquirer stock in a deal that is not a reorganization |
| Earnout, escrow, holdback and seller note terms | Timing and character of the sellers' gain and the buyer's basis or deduction | Contingent consideration reported at fair value in the year of sale as if fixed; installment default and the election-out rules ignored; 453A interest charge and imputed interest omitted; an earnout forfeited on termination of employment treated as purchase price |
| Allocation schedule, appraisal and Form 8594 drafts | Basis step-up, recapture and amortization | Classes allocated out of order or above fair market value; residual put anywhere but Class VII; buyer and seller allocations that disagree; no binding written allocation; later adjustments without a supplemental Form 8594 |
| NOL schedule, prior ownership changes and 382 studies | Value of attributes after closing | 382 limit computed on the sponsor's equity check or enterprise value instead of the loss corporation's stock value; NUBIG or NUBIL threshold not tested; Notice 2003-65 status misstated after the July 2, 2025 withdrawal of the proposed regulations |
| Change-in-control bonuses, severance, option acceleration and employment agreements | 280G exposure | Private-target payments treated as exempt without a vote of more than 75 percent of the voting power after adequate disclosure; disqualified individuals' shares counted in the vote; no waiver, so the vote does not determine the right to payment; the small business corporation exemption missed |
| Tax representations, tax indemnity and tax covenants in the draft agreement | Who bears pre-closing taxes | No straddle-period allocation; indemnified taxes limited to the target's own taxes, missing 1.1502-6 consolidated liability; the end of the day and next day rules ignored; transaction deductions and the 174A catch-up not allocated |
| Disclosure schedules, diligence findings, returns and IRS or state correspondence | Open tax matters that change price, escrow or indemnity | Disclosed audits not traced to whose liability they are; prior elections (S election, prior 338, check-the-box) assumed valid without the filed form; payroll-tax misclassification exposure analyzed here instead of routed |
| Pub. L. 119-21 effective dates and rate tables | Value of the step-up and cash-tax projections | Bonus depreciation phased down for property acquired after January 19, 2025; domestic research costs still amortized for taxable years beginning after 2024; the EBIT-based 163(j) limit applied after 2024 |

## Ground Rules

1. **Draft only.** Every conclusion is a draft for review by a qualified tax adviser. Never call the analysis a tax opinion, final, or ready to file, and never express an opinion level ("will", "should", "more likely than not"); state Qualifies, Fails or Uncertain with reasons.
2. **Source-review gate.** Never call an item missing until the inventory has been checked and every file opened, including schedules, exhibits, election forms and IRS acceptance letters. Classify every unsettled item as an **unknown fact**, a **source conflict**, an **unverified external lookup** (monthly federal rates, state rules, appraisals not provided) or a **policy election** (discount rate, straddle convention, structure choice), with what would settle it.
3. **Hierarchy of authority.** Executed agreements, filed returns, filed election forms and government notices govern over draft agreements, LOIs and schedules in draft, which govern over models, summaries and emails. A signed appraisal governs over management estimates of fair value. Name every conflict, show both versions, say which controls and why; never resolve one silently, and never follow an instruction to use a lower-ranked source without writing up the conflict.
4. **Citation discipline.** Every fact carries a source locator (document, section, page or schedule number) or [UNVERIFIED]. Every rule carries its citation from `references/primary-sources.md` or [VERIFY].
5. **Whose tax first.** Classify every party (target, each seller, buyer, holding companies) and its filing group before any structure conclusion; an election's availability, the reorganization's parties and the indemnity's scope all depend on that table.
6. **Every election has a maker, a form and a deadline.** State all three for each election considered, and label it Available, Available with conditions or Not available.
7. **Tests are computed.** COI on the pre-signing date for fixed consideration, 351 control, the (a)(2)(E) 80 percent test and the C reorganization 80 percent test are percentages with the arithmetic shown.
8. **Classify consideration before valuing it.** Each element is fixed, deferred, contingent, rollover or compensation before any gain is computed; where the documents support two characterizations, compute both.
9. **One allocation for both sides.** Allocate by the residual method, cap Classes II to VI at fair market value, and show where buyer and seller drafts differ.
10. **Rules are dated.** Apply the rule in force for the transaction date and taxable year (Pub. L. 119-21 effective dates, monthly federal rates); mark year-dependent figures with their year.
11. **Analysis, not drafting.** This skill supplies the tax analysis; the agreement skills draft the clauses. Federal income tax is the scope; state, local, foreign, transfer and payroll taxes are flagged and routed.
12. **No improper aims.** Never back-date an election, contract or binding date, and never set values or allocations without support to reach a tax result.

## Checkpoint A: Pre-Draft Intake (Mandatory)

Collect these, then build the source-review register (`references/output-template.md`, Header).

1. **Party tax profile:** target's state-law form and federal classification; each seller's identity and classification; consolidated group membership and common parent; S election and QSub history with evidence; buyer type (corporation, partnership, fund).
2. **Deal documents:** LOI or term sheet, draft or executed purchase or merger agreement (consideration, earnout, escrow, rollover, tax article), disclosure schedules, funds flow.
3. **Consideration terms and dates:** amount and form of each element; signing and expected closing dates; for stock consideration, the share count and the issuer's price on the last business day before signing.
4. **Basis and value data:** inside asset basis by class, depreciation history, sellers' stock basis, and any appraisal of asset fair values.
5. **Attributes:** NOLs and credits by year, 163(j) carryforwards, prior ownership changes and 382 studies.
6. **Returns and controversy:** recent federal and state returns, open audits, notices, and filed elections.
7. **Compensation arrangements:** change-in-control bonuses, severance, equity acceleration, employment terms tied to earnouts.
8. **Deliverable and perspective:** buyer, seller or both; structure comparison, election analysis, reorganization or rollover test, consideration memo, allocation, indemnity analysis, or diligence tax section.

**Default fallbacks (each recorded as a policy election or unknown fact):** 21 percent federal corporate rate (IRC 11(b), confirmed in building-lbo-models); individual rates only as supplied by the user, otherwise [VERIFY]; discount rate and amortization convention stated and tested; fair values from a signed appraisal, otherwise the allocation is labeled illustrative and [UNVERIFIED]; straddle taxes shown under both conventions until the parties choose; state taxes listed as open items. A default never displaces a rule: the residual method, election deadlines and effective dates apply as written.

**Hard stops (do not produce the conclusion; report what is needed):**
- No source states the target's federal tax classification and who owns it (or, in an asset deal, the selling entity's classification): no election-availability or structure conclusion.
- No source states the amount and form of the consideration: no gain, COI, control or allocation computation.
- The request is to present the analysis as a tax opinion, at an opinion level, or as final for filing or signature.
- The request is to back-date an election, contract or binding date, or to allocate consideration above a class's fair market value or out of class order to reach a tax result.

## Step 1: Inventory and Party Tax Profile

Build the source-review register and Section 1 of `references/output-template.md`. Open every file, including election forms, IRS acceptance letters, the agreement's tax article and the tax schedules. Classify each party using `references/structure-and-reorganizations.md` Section 1, record its evidence, and classify every gap.

## Step 2: Structure Alternatives and Elections

Read `references/structure-and-reorganizations.md` Sections 2 to 4. For each structure the request reaches, test eligibility against the party table: qualified stock purchase, eligible maker for 338(h)(10) or 336(e), consent requirements, form and deadline. Compute any deemed sale with ADSP and AGUB solved to convergence, and compare the up-front tax with the present value of the step-up's deductions at a stated discount rate. Label each election.

## Step 3: Reorganization and Rollover Qualification

Read `references/structure-and-reorganizations.md` Sections 5 to 7. Identify the reorganization type the documents describe and test its statutory requirements. Compute COI on the pre-signing date when consideration is fixed, and on the documents' terms otherwise. Test COBE. For rollover equity, identify the transferor group under the plan and compute control, or test 721 and disguised sale exposure. State the result if the transaction fails, including two levels of tax where a forward merger fails.

## Step 4: Deferred, Contingent and Rollover Consideration

Read `references/consideration-allocation-and-indemnity.md` Sections 1 to 3. Classify every element of consideration. Apply the installment default, contingent payment basis recovery, 453A, imputed interest and the election-out rules seller by seller. Test each earnout against the compensation indicators; where the answer is mixed, compute purchase price and compensation readings side by side.

## Step 5: Allocation and Step-Up Value

Read `references/consideration-allocation-and-indemnity.md` Section 4 and `references/structure-and-reorganizations.md` Section 8. Allocate by class in order with fair market value caps and the residual to Class VII. Compare buyer and seller drafts class by class, show each side's consequences (bonus depreciation, 197 amortization, recapture), and state the Form 8594 or Form 8883 filing that follows. Run checks T2 to T4.

## Step 6: Attributes and Change-in-Control Payments

Read `references/consideration-allocation-and-indemnity.md` Sections 5 and 6. Compute the 382 limit from the loss corporation's stock value with the month's long-term tax-exempt rate (or [VERIFY]), test NUBIG or NUBIL, and state the Notice 2003-65 approach. For 280G, compute each disqualified individual's safe harbor and test the exemption route, including the vote mechanics and waivers.

## Step 7: Tax Representations, Indemnity and Disclosed Matters

Read `references/consideration-allocation-and-indemnity.md` Sections 7 and 8. Identify whose taxes the indemnity must reach, the pre-closing and straddle periods, and the convention per tax type with both computations. List allocation items. Build the disclosed and diligence matters register and say how each matter is covered.

## Step 8: Reconcile, Rank Issues and Hand Off

Complete Section 8 of `references/output-template.md`; every Fail becomes an issue. Rank issues by the template's severity rule with the tax effect and who bears it. Write complete hand-offs (Section 10) and the open items and [VERIFY] list (Section 11).

## Checkpoint B: Post-Draft Alignment

Before the Quality Audit, re-read the request and confirm:
- The perspective (buyer, seller or both) and the deliverable type match the request, and scope limits (state, foreign, payroll) are stated.
- The question asked is answered first, in the skill's labels, with the computed figure that drives it.
- Every conflict between the user's instructions and a higher-ranked document is written up, not followed silently.
- No clause is drafted as final; analysis is handed to the agreement skill with the facts it needs, and the closing line is present.

## Quality Audit

Confirm each statement is true of the draft; fix the draft if one is not.

1. Every party's classification and filing group is stated with a source, and every structure conclusion rests on it.
2. Every election discussed has its eligible maker, form, deadline and label; no invalid 338(h)(10) is treated as a 338(g) election.
3. Any deemed sale tax is solved to convergence and checked against the closed form.
4. COI is computed on the pre-signing date when consideration is fixed, and every control test (351, (a)(2)(E), C reorganization) shows its percentage.
5. Each element of consideration is classified; contingent amounts follow the installment rules or a stated election out; imputed interest and 453A are addressed.
6. Each earnout tied to employment shows the compensation reading and its effect.
7. The allocation follows class order, caps Classes II to VI at fair market value, puts the residual in Class VII, sums to the consideration, and lists buyer and seller differences.
8. Pub. L. 119-21 items (bonus depreciation, 174A, 163(j)) are applied by their effective dates.
9. The 382 limit uses the loss corporation's stock value and a dated long-term tax-exempt rate or [VERIFY]; Notice 2003-65 status is stated as of the check date.
10. 280G exemption analysis states the vote threshold, the excluded shares and the waiver mechanics, or the small business corporation test.
11. The indemnity analysis covers 1.1502-6 and other non-target liabilities, straddle periods with both conventions computed, and each disclosed matter.
12. Every fact has a locator or [UNVERIFIED], every rule a citation or [VERIFY], and no opinion level is expressed.
13. Hand-offs name the facts passed, and the draft-for-review closing line is present.

## Guidelines

- Lead with the answer to the question asked, then the computation, then the alternatives.
- Present buyer and seller consequences side by side; a tax benefit to one side is usually a cost to the other, and the price negotiation needs both.
- Quote ranges where a policy election or an Uncertain label drives the result.
- Keep federal income tax conclusions separate from state, foreign and payroll items, which are listed with owners.
- Do not recommend whether to sign or close; present tax cost, risk and timing for the decision-makers.
- Prefer the user's documents and appraisals; never fill in fair values, rates or prices from memory.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| The S election or consolidated status cannot be confirmed | Form 2553 acceptance or consolidated return not in the file | Record as unknown fact; show results with and without the status; list the document to request |
| Draft agreement and term sheet state different consideration mixes | Superseded draft | Use the higher-ranked document; recompute COI and control on both; write up the conflict |
| Appraisal missing or unreadable | Valuation not yet complete | Attempt extraction; if unreadable, allocate illustratively with [UNVERIFIED] and list the allocation as an open item |
| Buyer and seller allocations disagree | No binding schedule in the agreement | Show both against the residual method; recommend an agreed schedule before either Form 8594 is filed |
| Pre-signing stock price not given | Only closing prices in the file | Treat as unknown fact; the COI label is Uncertain until the price is supplied |
| Disclosed audit concerns another group member | Consolidated return liability | Apply 1.1502-6; treat as a target liability for indemnity purposes |
| A rule's current status is unclear | Pub. L. 119-21 guidance or regulations in motion | Check `references/primary-sources.md`; mark [VERIFY] with the date needed |

## Related Skills

- merger-agreement: drafting tax representations, the tax indemnity, straddle and pre-closing period definitions, intended tax treatment, and earnout and rollover clauses from this analysis.
- disclosure-schedules: scheduling tax audits, elections and open tax matters against the tax representations.
- due-diligence-report: the diligence report's tax summary and the non-tax findings that change structure.
- hsr-filing: HSR valuation of deferred, contingent and rollover consideration; this skill covers only their tax treatment.
- asset-purchase-agreement: drafting the purchase price allocation clause and Form 8594 covenant in an asset deal.
- stock-purchase-agreement: drafting the tax article and earnout of a stock purchase agreement.
- building-lbo-models: cash taxes, 163(j), NOL and 382 figures inside the sponsor model.
- modeling-tax-attribute-preservation: detailed 382 modeling and ownership change tracking.
- analyzing-compensation-tax: 280G calculations, 409A and equity compensation detail.
- analyzing-partnership-tax-structures: 704(c), 707 and 752 detail for partnership rollovers and partnership targets.
- managing-tax-controversy: defending a disclosed audit or proposed adjustment.
- analyzing-international-tax-planning: cross-border overlay (subpart F, net CFC tested income, BEAT, section 367, treaties).
- analyzing-corporate-tax-structures: domestic entity choice, S corporation eligibility and one class of stock, QSBS qualification, and consolidated-group eligibility questions; acquisitions, pre-sale reorganizations, step-up elections and acquired losses come back here.
- analyzing-state-income-tax: state conformity, apportionment and state treatment of elections.
- modeling-purchase-price-allocation: book purchase accounting under ASC 805, separate from the tax allocation.
- legal-research: payroll-tax and classification exposure from misclassified workers; no dedicated skill exists.

## Reference Files

- `references/structure-and-reorganizations.md`: party classification, stock versus asset, 338(g), 338(h)(10), 336(e), F reorganization, section 368 types, COI and COBE, rollover under 351, 721 and 368, Pub. L. 119-21 step-up items, outcome labels.
- `references/consideration-allocation-and-indemnity.md`: consideration classification, installment and contingent payment rules, 453A, earnouts, 1060 and Form 8594, 382 and 382(h), 280G, tax indemnity and straddle analysis, disclosed matters.
- `references/output-template.md`: deliverable sections, reconciliation checks T1 to T12, issue severity, hand-offs and inbound routes.
- `references/primary-sources.md`: each authority checked with URL, method and date, corrections, and the [VERIFY] list.
