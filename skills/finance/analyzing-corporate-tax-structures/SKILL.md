---
name: analyzing-corporate-tax-structures
language: en
description: >
  Evaluates U.S. domestic entity choice and corporate tax structure: C corporation
  versus S corporation versus LLC or partnership on both layers (21 percent corporate
  rate plus dividend and NIIT tax, against owner rates net of the Section 199A
  deduction), break-even payout, and exit under Section 1202 QSBS (pre- and
  post-July 4, 2025 regimes, gross assets test, holding period tiers, per-issuer cap).
  Tests S corporation eligibility and one class of stock under Treas. Reg. 1.1361-1(l);
  Section 1374 built-in gains; LLC to corporation conversions; consolidated return
  eligibility under Section 1504 and the 1.1502 regulations; accumulated earnings and
  personal holding company tax; corporate AMT status with controlled-group
  aggregation; and state PTE elections under the SALT cap. Use for entity selection,
  S election, QSBS, holding company or consolidated group questions. Hands
  cross-border structures, transfer pricing and acquisition structuring to sibling
  skills. Drafts for qualified tax adviser review.
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

# Analyzing Corporate Tax Structures

Evaluates the U.S. federal tax structure of a domestic business and its owners: which entity type fits, whether the elections and statuses the plan relies on actually hold (S corporation, QSBS, consolidated group, corporate AMT), and the total tax on both layers under stated distribution and exit assumptions. The deliverable follows `references/output-template.md`: a structure snapshot, status tests, a clock table, a two-layer comparison, reconciliation checks, ranked issues, hand-offs and open items. Everything it produces is a draft for review by a qualified tax adviser; it is not tax, legal or accounting advice and not a tax opinion.

## Why This Skill Exists

Entity choice is usually argued with one number, 21 percent against 37 percent, and that number leaves out the dividend layer, NIIT, the Section 199A deduction and the exit. Pub. L. 119-21 (July 4, 2025) changed several inputs at once: it kept Section 199A past 2025, created a second QSBS regime for stock acquired after July 4, 2025, raised the SALT cap through 2029, and left the corporate rate alone. The structures that look best on a spreadsheet also fail on status: an S election ended by one side letter, QSBS lost to a gross assets test measured at fair market value, a subsidiary outside the consolidated group by a few points of value, a corporate AMT test run one entity at a time. This skill settles status before savings, dates every rate, and computes both layers.

## Where Mistakes Hide

Read each input with this suspicion before relying on it.

| Input / Document | What It Is Used For | Where the Error Hides |
|---|---|---|
| Rate comparison or entity-choice model | Choosing C corporation or pass-through | 21 percent compared with 37 percent alone: no dividend tax or NIIT on distributed C earnings, no 199A deduction for the pass-through, no distribution policy, no exit; the C corporation's retention advantage claimed without the accumulated earnings tax test |
| Section 199A workpaper | Owner-level tax on pass-through income | Sunset after 2025 still assumed; old $50,000 / $100,000 phase-in; wage and UBIA limit or SSTB exclusion skipped above the threshold; threshold taken from the wrong year; a C corporation given the deduction |
| Stock ledger, charter, bylaws, shareholders' agreement and side letters of an S corporation | S eligibility and one class of stock | A partnership, LLC, corporation or nonresident alien admitted as shareholder; a liquidation preference or priority return in a binding agreement (a governing provision); disproportionate distributions treated as fatal when governing provisions are identical, or ignored when uncorrected |
| QSBS stock ledger, issuance records and balance sheets at issuance | Section 1202 exclusion at exit | The 3/4/5-year tiers applied to stock acquired on or before July 4, 2025; the $50,000,000 test applied to stock issued after July 4, 2025, or $75,000,000 to earlier stock; a disqualified field (consulting, financial services, health) or a pivot into one; stock issued while an S election was in effect |
| Conversion plan (LLC to corporation, C to S, S to C) | Timing of elections and exit | QSBS holding period tacked back to LLC formation; gross assets measured at tax basis instead of the fair market value of contributed property; the Section 1374 recognition period counted from the Form 2553 filing date rather than the first S year; the five-year re-election bar missed |
| Ownership chart for a holding company and its subsidiaries | Consolidated return, dividends received deduction | A member below 80 percent of value though at 100 percent of vote; convertible or participating preferred treated as excluded stock; a 100 percent DRD claimed for a non-member; an S corporation or foreign corporation listed as a member |
| Financial statements used for the corporate AMT test | Applicable corporation status | Each corporation tested alone against $1,000,000,000 instead of with every IRC 52(a) or (b) group member; the consolidated return group used as the aggregation group; status treated as tax owed |
| PTE election workpapers and owner residence list | State tax and the federal SALT cap | Saving computed as if every owner were a resident; a nonresident owner's home state assumed to credit the other state's PTE tax; PTE payments for some S corporation shareholders without equalizing distributions; the SALT cap taken as $10,000 for 2025-2029 |
| Retained earnings plan and income mix of a C or holding corporation | Penalty tax exposure | Accumulation with no documented reasonable business needs; passive income over 60 percent with five or fewer individual owners, triggering the personal holding company tax |
| Prior memos, advisor summaries and articles | Background and starting assumptions | Stale law (199A sunset, $10,000 SALT cap, one QSBS regime) or misquoted thresholds treated as authority over the statute |

## Ground Rules

1. **Draft only.** Every comparison, status conclusion and recommendation is a draft for review by a qualified tax adviser. Never call a conclusion final, an opinion, or confirmed for a third party.
2. **Source-review gate.** Never call a document missing until the inventory has been checked and each file opened, including exhibits, side letters and spreadsheet tabs. Classify every unsettled item as an **unknown fact**, a **source conflict**, an **unverified external lookup** (published rates, state rules, valuations) or a **policy election** (distribution policy, exit year, election choices), with what would settle it.
3. **Hierarchy of authority.** For facts: executed governing documents, filed elections and IRS acceptance letters, and filed returns govern over the stock ledger and valuation reports, which govern over cap table spreadsheets and models, which govern over emails, memos and summaries. For law: the Code and final regulations govern over revenue procedures and notices, which govern over proposed regulations, which govern over commentary. Name every conflict, show both versions, say which controls and why; never resolve one silently.
4. **Citation discipline.** Every fact carries a source locator or [UNVERIFIED]; every rule carries its citation from `references/primary-sources.md` or [VERIFY].
5. **Every rate and threshold carries its tax year.** A figure without a year is incomplete. Inflation-adjusted figures for a year not yet published are [VERIFY].
6. **Two layers, every time.** A comparison computes entity-level and owner-level tax for each alternative under a stated distribution policy and states the break-even payout; a single-layer rate comparison is never the answer.
7. **Status before savings.** S eligibility, QSBS qualification, consolidated group membership and corporate AMT status are tested before any saving that depends on them is computed. A failed status test removes that saving.
8. **Regime by date.** Apply the Section 1202 regime by acquisition and issue date, block by block; date each election by its effective date; give each clock its own trigger event.
9. **Right taxpayer, right group.** Say whose tax each line is (entity, owner, consolidated group, aggregation group) and which persons a test counts. Never substitute the consolidated group for the IRC 52 group or a single entity for either.
10. **No altered records.** Never backdate, re-date or restate issuance records, elections, valuations or governing documents to reach a status or holding period, and never draft a statement that a status holds when the file shows a fact that breaks it.
11. **State law is read, not assumed.** State PTE rules, credits and conformity come from the state statute for the year or are [VERIFY]; residents and nonresidents are computed separately.
12. **Domestic scope.** Cross-border structure goes to analyzing-international-tax-planning, intercompany pricing outside the consolidated return rules goes to managing-transfer-pricing-compliance, and acquisition or disposition structure goes to analyzing-m-and-a-tax-implications, each with a complete hand-off.

## Checkpoint A: Pre-Draft Intake (Mandatory)

Collect these, then build the source-review register (`references/output-template.md`, Header).

1. **The question:** new entity, conversion, election, holding company or group structure, or review of an existing plan; the alternatives to compare; the tax years.
2. **Entities:** legal name, jurisdiction, current federal classification with its source (Form 2553 and IRS acceptance letter, Form 8832, default rule), fiscal year.
3. **Owners:** each owner's type, residence (state and country), ownership by vote and by value, material participation, and marginal rate band for the year.
4. **Governing documents:** charter, bylaws or operating agreement, shareholders' or investor rights agreements, side letters, and any amendment proposed.
5. **Financials:** projected taxable income by year, W-2 wages and UBIA for 199A, balance sheets at each stock issuance, financial statement income for three years for the corporate AMT test, accumulated E&P.
6. **Stock history:** stock ledger with each block's issue date, acquisition date, consideration and holder; prior Section 1202 exclusions by issuer.
7. **Policies and plans:** distribution policy (payout share), expected exit (type and year), planned conversions and their effective dates.
8. **States:** where the business operates and where owners reside; any PTE election made or proposed.

**Default fallbacks (each recorded as a policy election or unknown fact):** federal-only analysis with the state layer marked "not modeled" if state facts are missing; payout share shown at 0 percent, break-even and 100 percent if no policy is given; owner rate at the top bracket for the year with the band stated; exit modeled as a stock sale in the year the user names, or at the next Section 1202 tier date if none is named. Payroll and self-employment taxes are stated as not modeled unless wages and compensation are supplied.

**Hard stops (do not produce the blocked item; deliver the analysis up to the stop and report what is needed):**
- The entities or owners cannot be identified with a federal classification and an owner type for each: no comparison or status conclusion is produced.
- A Section 1202 conclusion is requested for a block whose acquisition date, issue date or gross assets at issuance is unknown and cannot be bracketed from the file: no exclusion figure for that block.
- The request is to draft a representation, term sheet clause, investor letter or filing position stating that an S election, QSBS status, consolidated group membership or other status holds, when the file shows a fact that breaks it: the statement is not drafted; the conflict is written up.
- The request is to backdate, re-date or alter issuance records, election dates, valuations or governing documents to reach a status, holding period or threshold.
- The request is to present the analysis as a final tax opinion or as advice to a third party.

## Step 1: Inventory, Structure Snapshot and Registers

Open every file and build the source-review register. Draw the structure snapshot and the owner table from executed documents and the stock ledger, not from a summary. Classify every gap. Record the question, alternatives, tax years and out-of-scope items for Section 1 of the template.

## Step 2: Route Out-of-Scope Questions

Before any analysis, check the triggers in Ground Rule 12. A foreign owner, foreign subsidiary or treaty question, cross-border or non-member intercompany pricing, or a purchase, sale or pre-sale reorganization of a business is routed with the facts listed in Section 9 of `references/output-template.md`. Continue with the domestic questions only.

## Step 3: Status and Eligibility Tests

Read `references/s-corp-qsbs-conversion-rules.md` Sections 1 to 6 and `references/entity-choice-and-group-rules.md` Sections 4 to 6. Complete the status table:

- S eligibility: every shareholder's type and residence; every governing provision for distribution and liquidation rights; distribution history against ownership by year.
- QSBS by block: regime by date, gross assets before and immediately after issuance (contributed property at fair market value), active business and excluded fields, holding period tier, per-issuer limit.
- Consolidated group: 80 percent vote and 80 percent value for each member every day, with each class of preferred stock tested under IRC 1504(a)(4).
- Corporate AMT: the IRC 52(a) or (b) group listed and its AFSI summed against the threshold.
- AET and PHC: retention plan and income mix.

A failed or undeterminable test is an issue, not a footnote.

## Step 4: Clock Table

Read `references/entity-choice-and-group-rules.md` Section 8. Build one row per timed element with its own trigger event and the document that proves the trigger date: S election effective date, recognition period, re-election bar, each QSBS block's tier dates, consolidated membership dates, PTE election deadlines.

## Step 5: Two-Layer Comparison

Read `references/entity-choice-and-group-rules.md` Sections 1 to 3. For each alternative and tax year, compute entity-level tax, owner-level tax on wages, pass-through income or dividends under the stated payout share, the 199A deduction with its binding limit named, NIIT, and the exit under the Section 1202 result from Step 3. Solve the break-even payout share. Remove any saving whose status test failed.

## Step 6: State Layer and PTE Elections

Read `references/entity-choice-and-group-rules.md` Section 7. Compute the SALT cap for each owner and year through 2030, the PTE tax base and credit owner by owner (residents and nonresidents separately), any loss of a home-state credit, and, for an S corporation, the equalizing distributions the one-class rule requires. State rules not read for the year stay [VERIFY].

## Step 7: Sensitivities

Run the sensitivities in Section 6 of `references/output-template.md`: payout share, exit year against the Section 1202 tiers and the Section 1374 recognition period, rate band, residence, and year-dependent figures.

## Step 8: Reconcile, Rank Issues and Hand Off

Complete the reconciliation checks R1 to R10 in `references/output-template.md` Section 7; each Fail becomes an issue. Rank issues by the template's severity rule, each with the sources in conflict, the controlling source, the effect on status or tax, and a recommendation with its alternative. Write complete hand-offs and the open items and [VERIFY] list from `references/primary-sources.md`.

## Checkpoint B: Post-Draft Alignment

Before the Quality Audit, re-read the request and confirm:
- The deliverable answers the decision asked, for the alternatives and years asked, and states what was routed elsewhere.
- Each conclusion that depends on a policy election (payout share, exit year, election choice) says so and shows the other outcome.
- Every user instruction that conflicts with a governing document or the statute is written up, not followed silently, and no status is stated as holding when a fact in the file breaks it.
- The closing line from the template is present.

## Quality Audit

Confirm each statement is true of the draft; fix the draft if one is not.

1. Every comparison shows entity-level and owner-level tax for each alternative under a stated payout share, with the break-even payout share.
2. The 199A deduction, where used, applies the post-Pub. L. 119-21 rules for the year, names the binding limit and is not given to a C corporation.
3. Every rate and threshold shows its tax year and citation, or [VERIFY].
4. Each S corporation shareholder is a permitted shareholder, and every governing provision was read for identical distribution and liquidation rights; disproportionate distributions are classified under Treas. Reg. 1.1361-1(l)(2).
5. Each QSBS block shows its acquisition and issue dates, the regime that follows, gross assets before and after issuance, the active business test, the tier and the per-issuer limit.
6. Any conversion shows its effective date, the QSBS acquisition date it creates, gross assets at fair market value and any built-in gain consequence.
7. The Section 1374 recognition period runs from the first day of the first S year.
8. Each consolidated member meets 80 percent of vote and 80 percent of value, and DRD percentages match membership.
9. The corporate AMT status test aggregates every IRC 52(a) or (b) group member and does not equate status with tax owed.
10. PTE analysis computes residents and nonresidents separately and addresses equalizing distributions for an S corporation.
11. Every fact has a source locator or [UNVERIFIED]; every conflict names both sources and the controlling one.
12. Every routed question has a complete hand-off, and nothing cross-border, transfer pricing or acquisition structuring is analyzed here beyond the hand-off.
13. The draft-for-review closing line is present and nothing is presented as a tax opinion.

## Guidelines

- Work in the units of the source documents and state them once; label every amount with its tax year.
- Prefer ranges and conditional conclusions to a single answer where a policy election drives the result.
- Treat a client's preferred answer as a hypothesis to test, not an input.
- Keep the owner's view and the entity's view separate; the best entity result can be the worse owner result.
- Show the arithmetic for each status threshold (percentages of vote and value, gross assets, AFSI totals) so a reviewer can check it.
- Do not opine on valuation; take values from a valuation report or mark them [UNVERIFIED].

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Governing documents are scans or only a term sheet exists | Executed versions not provided or unreadable | Attempt extraction; if unreadable, record it, analyze the term sheet with [UNVERIFIED], and list the conclusions that depend on the executed text |
| Stock ledger and cap table spreadsheet disagree | Transfers or issuances not posted | The ledger with transfer records controls; write up the conflict and test both versions for S eligibility and QSBS |
| Form 2553 filed but no IRS acceptance letter | Election status unconfirmed | Treat the election as an unverified external lookup; analyze both outcomes |
| Balance sheet at a stock issuance missing | Gross assets test not determinable | Bracket from the nearest balance sheets and capital raised; if it cannot be bracketed, the QSBS hard stop applies to that block |
| Financial statements cover only some group members | Corporate AMT aggregation incomplete | List the missing IRC 52 members and mark status Not determinable rather than computing it from part of the group |
| A memo or article states a different threshold than the statute | Stale or misquoted commentary | The statute controls; record the conflict in Section 8 |
| State PTE rules unclear for the year | Recent amendment or sunset | Mark [VERIFY] with the state and year; show the federal result with and without the election |

## Related Skills

- analyzing-international-tax-planning: foreign owners or subsidiaries, CFC, treaty, inbound and outbound structures, and the foreign-parented group corporate AMT test.
- managing-transfer-pricing-compliance: pricing of related-party transactions that are cross-border or outside the consolidated return intercompany rules.
- analyzing-m-and-a-tax-implications: buying or selling a business, pre-sale reorganizations, step-up elections, acquired losses and Section 382.
- analyzing-partnership-tax-structures: allocations, basis, waterfalls and carried interest inside an LLC or partnership alternative.
- analyzing-state-income-tax: nexus, apportionment and combined reporting beyond the PTE election decision.
- managing-income-tax-provisions: ASC 740 effects of an entity change or election.
- analyzing-compensation-tax: equity compensation, Section 409A and Section 280G issues raised by the structure.
- managing-estate-and-gift-tax: gifts of stock, generational transfers and the estate and gift tax side of succession planning.
- managing-tax-controversy: an election, status or exclusion already under IRS examination.
- analyzing-tax-reform-impacts: proposed legislation that would change the comparison.

## Reference Files

- `references/entity-choice-and-group-rules.md`: rates by year, the two-layer comparison, Section 199A, AET and PHC, consolidated returns and DRD, corporate AMT, SALT cap and PTE elections, clocks table.
- `references/s-corp-qsbs-conversion-rules.md`: S eligibility, one class of stock, termination and relief, Section 1374, QSBS regimes and tests, conversions.
- `references/output-template.md`: deliverable sections, status table, clock table, comparison table, reconciliation checks R1 to R10, issue severity, hand-off table.
- `references/primary-sources.md`: each authority checked with URL, method and date, conflicts found, and the [VERIFY] list.
