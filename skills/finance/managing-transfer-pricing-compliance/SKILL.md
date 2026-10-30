---
name: managing-transfer-pricing-compliance
language: en
description: >
  Drafts and reviews transfer pricing compliance on intercompany pricing under IRC
  482, Treas. Reg. 1.482-1 to 1.482-9 and the OECD Transfer Pricing Guidelines:
  functional analysis (FAR, DEMPE), best method and tested party selection, profit
  level indicators, benchmarking and comparable accept/reject review, interquartile
  range and median by the regulation's percentile rule, year-end true-ups with customs
  and VAT effects, intercompany agreements against conduct, services cost method,
  intangible transfers and cost sharing, intercompany loans and the AFR safe haven,
  IRC 6662(e) penalty exposure, 1.6662-6(d) contemporaneous documentation, and Form
  8975 country-by-country reporting. Use for TP study, local file, benchmarking,
  arm's length range, IDR documentation or TP penalty protection. Cross-border
  structure, 367(d) and Pillar Two route to analyzing-international-tax-planning;
  domestic structure to analyzing-corporate-tax-structures. Drafts for tax review.
tags:
  - management
  - tax
metadata:
  author: casemark
  practice_areas:
    - Tax Planning
    - Tax Compliance
    - International Tax
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---

# Managing Transfer Pricing Compliance

Drafts or reviews transfer pricing compliance work for intercompany transactions: a transaction inventory, functional analysis, method and tested party selection, a benchmarking review with the arm's length range computed the way the regulations require, any year-end adjustment and its collateral effects, an agreement-against-conduct review, and a documentation and penalty-protection status table. The deliverable follows `references/output-template.md` and ends with ranked issues, hand-offs and open items. Everything it produces is a draft for review by a qualified tax professional; it is not tax or legal advice, a transfer pricing opinion, or an assurance of penalty protection.

## Why This Skill Exists

Transfer pricing work fails quietly. A study can be long, well formatted and useless: the tested party is the entity with the patents, the comparables do something else, the quartiles come from a spreadsheet function the regulation does not use, the true-up never reaches the customs entry, and the report was finished after the return was filed, so it protects nothing. The IRS ordinarily adjusts an out-of-range result to the median, not to the edge the taxpayer picked. An intangible contributed to a foreign subsidiary is a 367(d) event, not a paperwork change. A loan priced at the AFR is safe only inside the safe haven's conditions. This skill forces each choice into a table, ties each figure to a document, recomputes the range, and checks documentation dates against the filing date before anyone relies on the conclusion.

## Where Mistakes Hide

Read each input with this suspicion before relying on it.

| Input / Document | What It Is Used For | Where the Error Hides |
|---|---|---|
| Legal entity chart, CbC data and the request itself | Which entities, transactions, years and returns are in scope; who files Form 8975 | The wrong entity's return analyzed (the foreign counterparty's local rules assumed to be U.S. rules, or the reverse); an affiliate left out of the controlled population; the $850,000,000 CbC test run on the current year instead of the preceding period; a U.S. subsidiary of a foreign group treated as the CbC filer |
| Functional analysis (FAR) and interview notes | Characterizing each entity and choosing the tested party | The tested party is the more complex entity (the IP owner or principal) instead of the least complex one with reliable comparables; labels such as "limited-risk distributor" taken from the agreement while people and decisions sit elsewhere |
| Benchmarking study and accept/reject matrix | Comparable set and profit level indicators | Comparables with different functions, risks or assets; loss-making comparables kept or dropped with no reason; a prior year's search rolled forward; comparables' fiscal years not matched to the year under review; multi-year comparables tested against a single year of tested party results |
| Range computation and true-up schedule | Whether the result is arm's length and how much to adjust | The full min-to-max range used where the interquartile range applies; quartiles from QUARTILE.INC instead of the 1.482-1(e)(2)(iii)(C) rule; a point outside the interquartile range reported as arm's length; adjustment stopped at the quartile with no note that the IRS ordinarily adjusts to the median |
| Year-end adjustment entries, customs entries and VAT returns | Booking the true-up | True-up recorded on one side only, after the return was filed, or never reflected in customs value or VAT; an upward price on imported goods that IRC 1059A caps at customs value |
| Intercompany agreements | Contract terms, risk allocation and pricing clauses | Agreement contradicts conduct (markup, royalty base, risk borne, who decides); agreement signed after the period it covers; no agreement at all |
| Service charge allocations | Cost-only or marked-up service fees | Services cost method used for excluded activities or core services that fail the business judgment rule; shareholder or duplicative activities charged; BEAT services exception claimed for the markup component or for services that are excluded activities |
| Intangible transfers, licenses and cost sharing | Who earns the residual return | Legal title treated as the end of the analysis while DEMPE functions stay elsewhere; an outbound contribution of intangibles with no 367(d) analysis; a cost sharing arrangement without a contemporaneous written contract or a platform contribution payment |
| Intercompany loan agreements | Interest rate | AFR safe haven used for a non-dollar loan, by a lender in the lending business, or for back-to-back funds; the wrong AFR term or month; equity-like debt repriced instead of recharacterized |
| Documentation file and return filing dates | Penalty protection under IRC 6662(e) | Study finished after the return was filed, so not contemporaneous; principal documents missing; 30-day production deadline missed; reliance on documentation that does not show why other methods were rejected |

## Ground Rules

1. **Draft only.** Every analysis, range and conclusion is a draft for review by a qualified tax professional. Never call it final, an opinion, or penalty protection.
2. **Source-review gate.** Never call an input missing until the inventory has been checked and each file opened, including spreadsheet tabs, agreement schedules and database exports. Classify every unsettled item as an **unknown fact**, a **source conflict**, an **unverified external lookup** (foreign rules, AFRs, comparable financials, database data) or a **policy election** (point in range, multi-year versus single year, disputed comparable), and say what would settle it.
3. **Hierarchy of authority.** Executed agreements, filed returns, statutory or audited accounts, APAs and IRS correspondence govern over the general ledger, which governs over studies, database exports and management schedules, which govern over emails and user statements. For legal rules, the statute and regulations govern over IRS guidance, which governs over the OECD Guidelines for U.S. purposes; for a foreign return, that country's law governs [VERIFY]. Name every conflict, show both values, say which controls and why; never resolve one silently.
4. **Citation discipline.** Every figure carries a source locator or [UNVERIFIED]; every rule carries a citation from `references/primary-sources.md` or [VERIFY].
5. **Conduct over labels.** Characterization follows the functional analysis and actual conduct (Treas. Reg. 1.482-1(d)(3)(ii)(B); OECD Chapter I). Never write a characterization or residual-profit conclusion that the facts in the file contradict.
6. **The range is computed, not copied.** Recompute every PLI and the quartiles and median by the regulation's percentile rule; report spreadsheet figures only as a reconciling difference.
7. **Out of range means two numbers.** Quantify the adjustment to the nearest quartile and to the median, and state which a self-initiated true-up uses and why.
8. **Dates are facts.** Documentation status depends on when each document was finalized and when the return was filed. Never backdate, redate or describe a document as contemporaneous unless it existed when the return was filed.
9. **Outcome-neutral selection.** The tested party, PLI, comparable set and agreement terms are chosen on the facts, never to reach a margin, rate or adjustment named in advance. Report a requested target as a constraint the analysis does not adopt.
10. **Both sides, all taxes.** Every adjustment is traced to the counterparty's books and return and to customs, VAT and withholding; foreign effects are [VERIFY] by jurisdiction.
11. **Stay in lane.** Price the transaction here; route structure, 367(d) computations, Pillar Two and other cross-border regimes, and domestic structure to the skills in Related Skills, with the facts they need.

## Checkpoint A: Pre-Draft Intake (Mandatory)

Collect these, then build the source-review register in `references/output-template.md` (Header).

1. **Scope:** the entities, controlled transactions, taxable years and jurisdictions, and which return the work supports.
2. **Deliverable type:** documentation report, benchmarking or range test, year-end true-up, agreement review, penalty exposure review, or loan or services pricing review.
3. **Organization chart and CbC facts:** ownership, ultimate parent, consolidated revenue for the preceding reporting period.
4. **Transaction data:** amounts, currencies and invoices by transaction; ledgers for both sides.
5. **Tested party financials:** segmented profit and loss reconciled to the trial balance or statutory accounts, for each year tested.
6. **Functional analysis inputs:** interviews, job descriptions, decision records, R&D and marketing budgets, risk control evidence.
7. **Comparables:** the study, search strategy, database export with each comparable's financials and fiscal year end, and the accept/reject matrix.
8. **Agreements:** executed intercompany agreements with schedules, and any APA or ruling.
9. **Dates:** return filing date for each year, the date each document was finalized, and any IDR date.

**Default fallbacks (each recorded as a policy election or unknown fact):** U.S. rules where a U.S. return is affected and foreign rules marked [VERIFY]; the interquartile range where comparables are not shown to meet 1.482-1(e)(2)(iii)(A); the comparables' data for the year under review unless the study supports multi-year data; for a loan, the AFR the user supplies for the month the loan was made, otherwise [VERIFY]; a missing agreement treated as terms imputed from conduct.

**Hard stops (do not produce the blocked output; report what is needed):**
- The request is to backdate or redate a study or agreement, or to describe documentation as in existence when the return was filed when it was not. Decline that part; an exposure analysis and a correctly dated report may proceed.
- The request is to choose the tested party, PLI or comparables, or rewrite agreements, to reach a margin, rate or adjustment named in advance.
- The request is to present the draft as final, as an opinion, or as assurance of penalty protection.
- A benchmarking, range or true-up deliverable has no financial data for the tested party from any source, so no PLI can be computed.
- An executed agreement in the file contradicts the user's stated terms and the user directs that it be ignored without a written conflict note.

## Step 1: Scope, Inventory and Source Register

Build the source-review register and the controlled transaction inventory (`references/output-template.md` Header and Section 1). Open every file. Confirm which entity's return each transaction affects and whether a U.S. return is affected. Run the CbC test on the preceding period's revenue (`references/documentation-and-penalties.md` Section 6). Classify every gap.

## Step 2: Functional Analysis and Characterization

Read `references/pricing-rules.md` Section 2, and Section 8 when intangibles are involved. Build the FAR table for each transaction's parties, apply the Chapter I risk framework, and record evidence for each row. For intangibles, build the DEMPE table. Characterize each entity from the table, not from the agreement's label, and note every place the agreement and the evidence disagree.

## Step 3: Method, Tested Party and Profit Level Indicator

Read `references/pricing-rules.md` Sections 1 and 3. Evaluate each specified method against the available data; record why each rejected method was rejected (this becomes principal documents 4 and 5). Select the tested party as the least complex party with reliable data and comparables, and a single PLI suited to its functions. If an existing study tested the more complex party, say so and re-test.

## Step 4: Benchmarking and Comparable Review

Read `references/pricing-rules.md` Section 5. Check the search strategy against the tested party's functions and risks. For each comparable confirm functions, fiscal year end and years used, recompute its PLI (R3), and record an accept or reject reason. Investigate every loss-making or abnormally profitable comparable; never accept or reject one on its result alone. Where a disputed comparable changes the conclusion, carry both sets forward.

## Step 5: Range, Result and Year-End Adjustment

Read `references/pricing-rules.md` Sections 4 and 6. State whether the full range or the interquartile range applies and why. Compute the quartiles and median by position (R4), compute the tested party's PLI from reconciled financials (R2), and test it. If outside, quantify the adjustment to the nearest quartile and to the median (R5) and state the choice. A self-initiated adjustment must appear on a timely filed return. Trace the true-up to both entities' books, customs value and VAT (R6), and route those effects.

## Step 6: Services, Intangibles and Loans

Read `references/pricing-rules.md` Sections 7 to 9 for the transaction types in scope. For services, test services cost method eligibility condition by condition and apply the benefit test. For intangibles, identify every transfer, license or contribution, test legal ownership against DEMPE, and flag any outbound transfer for 367(d) or cost sharing analysis. For loans, confirm bona fide debt, then test each safe haven condition (currency, lender's business, situs of funds, AFR term and month) before using it; otherwise list the credit and market data needed under 1.482-2(a)(2)(i). Recompute interest (R10).

## Step 7: Intercompany Agreements Against Conduct

Compare each agreement clause with invoicing and conduct (Section 6 of the template; R7). Record the agreement's execution date against the period it covers. Where terms and conduct differ, state that the IRS may disregard the terms and impute terms from conduct, and recommend an amendment effective prospectively, never a backdated one.

## Step 8: Documentation, Penalty Protection and Reporting

Read `references/documentation-and-penalties.md` in full. Map the file to the ten principal documents with their finalization dates and the return filing date (R8). Compute the 30-day production date from any IDR. For any proposed or estimated adjustment, show the penalty threshold arithmetic. Confirm Form 8975, Form 5472 and foreign local file obligations, with foreign items [VERIFY]. Check consistency across the CbC report, master file and local files (R9).

## Step 9: Reconcile, Rank Issues and Hand Off

Complete the reconciliation table (`references/output-template.md` Section 9); every Fail becomes an issue. Rank issues by the template's severity rule, each with the sources in conflict, the controlling source, the effect by entity and year, and a recommendation. Write complete hand-offs (Section 11) and the open items and [VERIFY] list (Section 12).

## Checkpoint B: Post-Draft Alignment

Before the Quality Audit, re-read the request and confirm:
- The deliverable type matches the request and the scope (entities, years, jurisdictions) is stated.
- The answer to the user's actual question (in range or not, how much to adjust, protected or not) appears in the first section, with the figures.
- Every instruction that conflicted with a higher-ranked source or a ground rule is written up, not followed silently.
- Nothing routed to another skill was analyzed here beyond the facts that skill needs.

## Quality Audit

Confirm each statement is true of the draft; fix the draft if one is not.

1. Every controlled transaction in scope is in the inventory and ties to both entities' ledgers (R1).
2. Each entity's characterization matches its FAR or DEMPE table, and every agreement-versus-conduct difference is listed.
3. The tested party is the least complex party with reliable data, or the draft explains why not.
4. Every rejected method has a written reason; the selected method is a specified method or the unspecified-method test is addressed.
5. Every comparable has a fiscal year, years used, recomputed PLI and an accept or reject reason; no loss-maker is accepted or rejected on its result alone.
6. The range type is justified, and the quartiles and median are computed by the regulation's rule with positions shown (R4).
7. An out-of-range result shows the adjustment to the nearest quartile and to the median, and states that a self-initiated adjustment must be on a timely filed return.
8. Every true-up is traced to both sides, customs value, VAT and withholding, or routed (R6).
9. Safe haven, services cost method and 367(d) conclusions each list the conditions tested.
10. Every principal document has a finalization date compared with the return filing date; no document is called contemporaneous without that comparison (R8).
11. Penalty arithmetic shows each threshold as "lesser of" with gross receipts, and the rate applied.
12. Every figure has a source locator or [UNVERIFIED], every rule a citation or [VERIFY], and every foreign rule is [VERIFY].
13. The closing line from the template is present and nothing is called final, an opinion, or penalty protection.

## Guidelines

- Lead with the answer and the numbers; put method discussion after the tables.
- Keep the U.S. and foreign readings side by side where they differ (point in range, ownership of intangibles, compensating adjustments).
- Prefer the user's existing study structure; flag defects rather than rebuilding it unasked.
- Treat a prior-year study as a starting point to update, not as evidence for the current year.
- Recommend prospective fixes (amended agreements, policy changes, APA or MAP consideration) with their owners; never suggest repairing a past year by redating documents.
- Do not opine on whether a position will be sustained; present the exposure, the evidence and the alternatives.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Quartiles differ from the study's | Spreadsheet quartile function or a different comparable count | Recompute by position under 1.482-1(e)(2)(iii)(C); report both and the difference |
| Tested party PLI will not reconcile | Segmentation includes uncontrolled sales or allocated costs | Rebuild from the trial balance; record the segmentation as a policy election |
| Database export unreadable or missing fiscal years | Export truncated or a summary only | Attempt extraction; request the full export; mark affected comparables [UNVERIFIED] |
| Agreement and invoices disagree | Agreement outdated or never implemented | Treat the executed agreement as rank 1 for its terms and conduct as evidence of substance; write up the conflict |
| Return filing date unknown | Not in the file | Ask; until then mark contemporaneous status as unknown fact, never as met |
| Foreign counterpart rejects the U.S. range or point | Different rules or practice | Show both readings, flag double tax exposure, route MAP or APA questions |
| User supplies an AFR with no month or term | Lookup incomplete | Ask for the loan date and term; mark the safe haven test [VERIFY] until supplied |

## Related Skills

- analyzing-international-tax-planning: cross-border structure, 367(d) inclusions and outbound restructurings, cost sharing structure, Pillar Two GloBE effects of TP adjustments, NCTI, FDDEI, BEAT, treaties and foreign interest limits.
- analyzing-corporate-tax-structures: domestic structure, entity selection, consolidation and state nexus questions raised by the pricing.
- managing-indirect-tax-analysis: customs value and VAT or GST effects of prices and year-end true-ups.
- managing-tax-controversy: IRS examination strategy, IDR negotiation, protests and appeals of a proposed 482 adjustment, competent authority and APA requests.
- managing-income-tax-provisions: provision and uncertain tax position effects of TP exposure and true-ups.
- managing-intercompany-transactions: booking, settlement, netting and elimination of intercompany charges once priced.
- managing-subsidiary-financing: designing intercompany debt, guarantees and structural subordination before the interest rate is priced.

## Reference Files

- `references/pricing-rules.md`: best method rule, comparability, tested party and PLIs, interquartile range computation and adjustment point, data years and loss-makers, year-end adjustments, services, intangibles and 367(d), loans and the safe haven, OECD differences, Amount B and Pillar Two notes.
- `references/documentation-and-penalties.md`: IRC 6662(e) thresholds, 1.6662-6(d) requirements, contemporaneous filing-date test, ten principal documents, 30-day production, Form 8975, master and local files, 6038A, 1059A and customs.
- `references/output-template.md`: deliverable sections, source register, tables, reconciliation checks R1 to R10, severity, hand-offs and open items.
- `references/primary-sources.md`: each authority checked with URL, method and date, corrections, and the [VERIFY] list.
