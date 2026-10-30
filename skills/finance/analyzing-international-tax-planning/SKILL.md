---
name: analyzing-international-tax-planning
language: en
description: >
  Evaluates U.S. international tax planning for cross-border structures, inbound and
  outbound, including foreign owners or foreign subsidiaries of a domestic structure,
  under Pub. L. 119-21: NCTI (formerly GILTI) without QBAI, subpart F, section 250 for
  NCTI and FDDEI (formerly FDII), FTC limits by basket, 245A and hybrid dividends,
  check-the-box, 367(d) inclusions and outbound transfers of intangibles, cost sharing
  arrangement structure, BEAT, the foreign-parented group corporate AMT test (59(k)(2)),
  CFCs, treaties and limitation on benefits, foreign interest limits on intercompany
  loans, FIRPTA and withholding, and Pillar Two (QDMTT, IIR, UTPR, side-by-side safe
  harbour) and GloBE effects of transfer pricing adjustments. Routes intercompany pricing,
  documentation and benchmarking to managing-transfer-pricing-compliance, and domestic
  entity choice, S corporation, QSBS, consolidated-group and PTE questions to
  analyzing-corporate-tax-structures. Drafts for tax adviser review.
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

# Analyzing International Tax Planning

Evaluates a cross-border structure for a U.S.-parented group (outbound), a foreign investor in the United States (inbound), or a domestic structure with foreign owners or foreign subsidiaries: CFC inclusions, the section 250 deduction, foreign tax credits by basket, repatriation, treaty withholding and limitation on benefits, BEAT, the corporate AMT test for foreign-parented groups, 367(d) and cost sharing structure, FIRPTA and Pillar Two exposure of foreign subsidiaries. The deliverable follows `references/output-template.md`: computations tied to the taxable year each rule governs, a reconciliation table, ranked issues, hand-offs and an open-items list. Everything it produces is a draft for review by a qualified tax adviser; it is not a tax opinion, a return position or legal advice.

## Why This Skill Exists

International tax figures fail on dates and definitions more than on arithmetic. Pub. L. 119-21 replaced GILTI with net CFC tested income, removed the QBAI return, set the section 250 deduction at 40 percent for NCTI and 33.34 percent for FDDEI, raised the deemed-paid credit to 90 percent, changed expense allocation to the NCTI basket, and set BEAT at 10.5 percent, each for taxable years beginning after December 31, 2025, while other changes key off the foreign corporation's year or a June 2025 date. Models built in 2024 still carry the old rates or the never-effective 2026 step-down. Treaty rates get claimed on a residence certificate without the limitation on benefits test, and the side-by-side arrangement gets read as ending Pillar Two exposure when foreign QDMTTs still apply. This skill fixes the rule set to each taxpayer's year, separates the U.S. and foreign layers, and proves the computation ties before anyone relies on an effective rate.

## Where Mistakes Hide

| Input / Document | What It Is Used For | Where the Error Hides |
|---|---|---|
| Prior-year provision workpapers, GILTI and FDII models, "10.5 percent" planning memos | Effective U.S. rate on NCTI and FDDEI | The 50 percent / 37.5 percent section 250 rates, or the 37.5 percent / 21.875 percent step-down Pub. L. 119-21 struck before it took effect, applied to taxable years beginning after December 31, 2025 (40 percent and 33.34 percent apply); the 13.125 percent FDII rate carried into 2026 |
| Form 8992 schedules and CFC tested income workpapers | NCTI inclusion and inclusion percentage | 10 percent of QBAI still subtracted as a net deemed tangible income return for a U.S. shareholder year beginning after 2025, understating the inclusion and the inclusion percentage; high-taxed income left in or taken out without a valid group-wide election |
| Form 1118 and FTC limitation worksheets by category | Foreign tax credit and residual U.S. tax | NCTI-basket credits pooled with general or branch baskets; excess NCTI-basket credits carried forward (904(c) bars it); 80 percent used instead of 90 percent; interest and R&E apportioned to the NCTI basket for post-2025 years (904(b)(5) bars it); withholding on 245A dividends credited; the 10 percent disallowance on post-June 28, 2025 NCTI PTEP ignored |
| Taxable-year calendar of each U.S. shareholder and each CFC | Selecting the rule set | Year classified by when it ends or when the return is filed; a fiscal-year shareholder whose year began before January 1, 2026 moved onto NCTI rules (proposed Treas. Reg. 1.951A-7(c) keeps former 951A for that year); the one-month deferral repeal short year missed |
| Entity chart, stock ledgers and Forms 5471 (party and scope) | Who is the U.S. shareholder, CFC, withholding agent or constituent entity, and whose tax is computed | CFC status tested with downward attribution after 958(b)(4) was restored for foreign corporation years beginning after 2025; pro rata share taken at year end instead of by period of ownership; the payer's own withholding liability left out of an inbound memo |
| Treaty, residence certificate and Form W-8BEN-E | Reduced withholding on dividends, interest and royalties | Residence treated as entitlement; LOB not tested (ownership and base erosion, active trade or business, which excludes holding and group financing, derivative benefits, headquarters company); portfolio interest claimed by a 10-percent shareholder |
| Form 8832 elections, local entity law and hybrid instruments | Whether an entity or payment exists for U.S. tax, and 245A or 267A treatment | Per se entity treated as eligible; effective date more than 75 days before filing; second election inside 60 months; deemed liquidation on a change ignored; payment deductible abroad on stock treated as eligible for 245A |
| Dividend history, ex-dividend dates and sale plans | 245A deduction and repatriation cost | Holding period of more than 365 days in the 731-day window not met because of a planned sale; PTEP not sourced first; hybrid deduction account not computed; foreign withholding on a 245A dividend credited or deducted |
| Subpart F and NCTI high-tax elections, 954(c)(6) analysis | Excluding high-taxed or related-party income | Election assumed rather than evidenced; 18.9 percent threshold tested on the wrong unit; 954(c)(6) treated as expiring after 2025 when it is permanent; the election's effect on the 960(d) tax pool not modeled |
| GloBE workpapers, OECD Central Record and local QDMTT law | Top-up tax of foreign subsidiaries | Side-by-side safe harbour read as removing QDMTT exposure, treated as automatic, or applied to fiscal years commencing before January 1, 2026; local adoption assumed; covered taxes taken from U.S. calculations |
| BEAT workpapers | Base erosion minimum tax | 12.5 percent or 10 percent used for a year beginning after 2025 (10.5 percent applies); gross receipts and base erosion percentage tests skipped; payments with full 30 percent withholding not removed |
| FIRPTA and partnership exit documents | Inbound real estate and partnership dispositions | 15 percent 1445 withholding or 10 percent 1446(f) withholding missed; USRPHC 50 percent test run on book values without the five-year lookback |

## Ground Rules

1. **Draft only.** Every computation, position and recommendation is a draft for review by a qualified tax adviser. Never call the output a tax opinion, a return position, final, or sufficient for penalty protection.
2. **Source-review gate.** Never call an input missing until the inventory has been checked and every file opened, including return attachments, Forms 5471 schedules, workbook tabs and treaty protocols. Classify every unsettled item as an **unknown fact**, a **source conflict**, an **unverified external lookup** (treaty text, local Pillar Two law, state law, exchange rates) or a **policy election** (high-tax election, credit versus deduction, SbS election, entity classification), with what would settle it.
3. **Hierarchy of authority.** For law: the Code, then final and temporary regulations, then proposed regulations the taxpayer chooses to rely on in their entirety, then notices and revenue procedures, then forms, instructions and IRS FAQs; a treaty with its protocols and technical explanation, read with the later-in-time rule; local implementing law over OECD model rules, commentary and guidance. For facts: executed documents and filed elections, then filed returns and audited statements, then workpapers and models, then emails and summaries. Name every conflict, show both readings, say which controls and why; never resolve one silently or follow a user instruction to use a lower-ranked source without writing up the conflict.
4. **Citation discipline.** Every input carries a source locator or [UNVERIFIED]. Every rule carries a citation from `references/primary-sources.md` or [VERIFY].
5. **Every rate carries its year.** State each rate and threshold with the taxable year it applies to and whose year that is. Classify a year by its beginning date.
6. **No QBAI after 2025.** For a U.S. shareholder year beginning after December 31, 2025, NCTI is net tested income with no deemed tangible return.
7. **Credits stay in their basket.** Compute the limitation separately for NCTI, foreign branch, passive and general categories; NCTI-basket excess credits are lost, not carried.
8. **Treaty benefits need the LOB.** Apply a treaty rate only after the treaty's LOB article is tested and passed on stated facts; otherwise apply the statutory rate and name the withholding agent.
9. **Pillar Two is a separate layer.** The side-by-side safe harbour can switch off IIR and UTPR top-up for U.S.-parented groups from fiscal years commencing on or after January 1, 2026 if elected; QDMTTs apply regardless.
10. **Elections are facts, not assumptions.** Treat an election as made only with evidence of the filing; model the effect both ways when it is still open.
11. **Legitimate planning only.** Plan around the rules as written. Do not backdate elections, document substance or ownership that did not exist, or help keep a position from a tax authority or auditor.
12. **Stay in scope.** Do not set intercompany prices or benchmark them, choose a domestic entity form, or decide state treatment; route them with the facts.

## Checkpoint A: Pre-Draft Intake (Mandatory)

Collect these, then build the source-review register (`references/output-template.md`, Header).

1. **Entity chart:** each entity's jurisdiction, U.S. classification and any Form 8832, owners and percentages by vote and value, and changes during the year with dates.
2. **Taxable years:** beginning and ending dates for each U.S. shareholder and each foreign corporation.
3. **CFC financials:** gross income by type, deductions, foreign income taxes, E&P and PTEP accounts; QBAI only for shareholder years beginning before 2026.
4. **U.S. parent data:** taxable income, interest expense, R&E, other deductions, foreign-source income by basket, FTC carryovers, export sales and services for FDDEI.
5. **Elections and filings:** prior Forms 5471, 8992, 8993, 1118; high-tax, 962 and classification elections.
6. **Payments and distributions:** intercompany flows by type and date; dividend and ex-dividend dates; planned sales.
7. **Inbound facts:** payee residence and ownership chain, treaty and its articles, W-8 forms, U.S. real property holdings, partnership interests.
8. **Pillar Two data:** consolidated revenue in euros, jurisdictional GloBE income, covered taxes, SBIE, local QDMTT status, safe harbour and SbS elections.
9. **Deliverable:** planning memo, review of a model or provision, repatriation comparison, inbound withholding analysis, or Pillar Two exposure summary.

**Default fallbacks (each recorded as a policy election or unknown fact):** foreign taxes credited, not deducted; no high-tax election, 962 election or safe harbour election without evidence; statutory withholding until the LOB is documented; state treatment an open item; amounts in the source currency with the translation rate [UNVERIFIED] if not given.

**Hard stops (do not produce the blocked output; report what is needed):**
- The owners and ownership percentages of the entity whose tax is being computed are not stated in the file or the request: no CFC, NCTI, 245A or withholding computation for that entity.
- The beginning and ending dates of the taxable year of a U.S. shareholder or foreign corporation whose year-dependent liability is being computed are not stated: no computation for that year.
- A conclusion that a treaty rate applies is requested and neither the treaty text nor a statement of its benefit and LOB articles is available: give the statutory treatment only.
- The request is to backdate an election beyond the period the regulation allows, to document substance or ownership that did not exist, or to keep a position or transaction from a tax authority or auditor.
- The request is to present the draft as a final tax opinion, a signed return position or a penalty-protection opinion.

## Step 1: Inventory, Structure and Taxable Years

Build the source-review register and Sections 1 and 2 of `references/output-template.md`. Open every file. Map each entity, its classification and its owners by period. List every taxable year with its beginning date, then read `references/us-international-rules.md` Section 1 and assign the rule set to each item for each year, naming whose year controls.

## Step 2: Ownership Tests and Elections

Read `references/us-international-rules.md` Sections 4 and 8. Re-test CFC and U.S. shareholder status with 958(b)(4) as restored for foreign corporation years beginning after 2025 and section 951B for foreign-controlled groups. Build the elections register (Section 8 of the template) with evidence for each election, its deadline and its consistency rule.

## Step 3: Subpart F and NCTI

Read `references/us-international-rules.md` Sections 2 to 4. For each CFC, compute subpart F income after 954(c)(6) and any valid high-tax election, then tested income or loss and tested foreign income taxes. Aggregate to NCTI (or GILTI for a pre-2026 shareholder year, with QBAI), the inclusion percentage, the deemed-paid credit at the year's percentage and the section 78 gross-up. Apply the section 250 deduction at the year's rate after the taxable income limit.

## Step 4: Foreign Tax Credit by Basket

Read `references/us-international-rules.md` Section 5. Assign income and taxes to the four baskets; allocate deductions with 904(b)(5) for NCTI-basket years beginning after 2025; compute each limitation, credit and excess; record lost NCTI-basket excess and any 960(d)(4) disallowance. Produce the effective-rate bridge.

## Step 5: FDDEI and Outbound Transfers

Read `references/us-international-rules.md` Sections 6 and 9. Build DEI with the disposition exclusion for sales after June 16, 2025, allocate deductions without interest or R&E for post-2025 years, test foreign use and foreign person evidence, and compute FDDEI. For transfers to foreign corporations and outbound restructurings, identify 367(a) gain and 367(d) inclusions; for a cost sharing arrangement, set out its structure (participants, platform contribution transactions, 367(d) interplay and where intangible income lands). Route the pricing of royalties, buy-ins and platform contributions, and their documentation and benchmarking, to managing-transfer-pricing-compliance.

## Step 6: Repatriation

Read `references/us-international-rules.md` Sections 7 and 8. Source each distribution from PTEP first, then test 245A: foreign-source portion, holding period (count the days and give the date it is or will be met), hybrid deduction accounts, and 245A(d). Compare repatriation pathways by total tax cost for the year of each.

## Step 7: Inbound Payments, Treaties and BEAT

Read `references/us-international-rules.md` Section 10 and `references/pillar-two-and-treaties.md` Sections 4 to 6. For each payment, name the withholding agent, the beneficial owner and the statutory rate; test the treaty's LOB article item by item before applying a treaty rate; test portfolio interest eligibility. Run the BEAT applicable taxpayer tests and rate for the year, the corporate AMT applicable-corporation test for a foreign-parented group (59(k)(1)(B)(ii) and (2)), treaty and foreign interest-limitation rules on intercompany loans, and FIRPTA and 1446 withholding where real property or partnership interests are involved.

## Step 8: Pillar Two

Read `references/pillar-two-and-treaties.md` Sections 1 to 3 and 8. Confirm scope, compute jurisdictional ETR and top-up by fiscal year, test safe harbours under local adoption, compute QDMTT exposure, reflect transfer pricing adjustments and year-end true-ups in GloBE income of both parties, and state for each fiscal year commencing on or after January 1, 2026 whether the SbS election is made and what IIR and UTPR exposure remains.

## Step 9: Reconcile, Rank Issues and Hand Off

Complete the reconciliation checks in `references/output-template.md` Section 9; every Fail becomes an issue. Rank issues by the template's severity rule. Add state conformity as an open item per filing state (`references/pillar-two-and-treaties.md` Section 7). Write complete hand-offs and the open items and [VERIFY] list.

## Checkpoint B: Post-Draft Alignment

Before the Quality Audit, re-read the request and confirm:
- The deliverable answers the question asked (liability, rate, comparison or exposure) for the years asked, and says which years it does not cover.
- Every figure the user supplied that conflicts with a higher-ranked source or with the rule set for the year is written up, not adopted silently.
- No transfer pricing amount, domestic entity choice or state conclusion is presented as this skill's own finding.
- The closing line from the template is present.

## Quality Audit

Confirm each statement is true of the draft; fix the draft if one is not.

1. Every taxable year is classified by its beginning date and labeled with its rule set and whose year controls.
2. Every rate and threshold shows its taxable year and citation; no pre-2026 or never-effective rate is applied to a year beginning after 2025.
3. No QBAI return is subtracted for a U.S. shareholder year beginning after December 31, 2025.
4. The deemed-paid percentage, the section 78 gross-up and the section 250 rate match the year, and the 250(a)(2) limit was tested.
5. FTC limitations are computed by basket; NCTI-basket excess is not carried; interest and R&E are not allocated to the NCTI basket for post-2025 years.
6. CFC and U.S. shareholder status reflect 958(b)(4) and pro rata shares by period of ownership for the years they govern.
7. Every 245A claim shows PTEP sourcing, the holding period count and date, the hybrid dividend test and 245A(d).
8. Every treaty rate rests on a tested LOB article and the treaty's own text; otherwise the statutory rate and the withholding agent are stated.
9. Pillar Two exposure shows QDMTT top-up separately from IIR and UTPR and states the SbS election status by fiscal year.
10. Every election relied on has evidence or is modeled both ways.
11. Every reconciliation check was computed; every Fail is an issue with severity and owner.
12. Transfer pricing, domestic entity choice, withholding operations, state treatment and provision accounting are handed off with facts.
13. The draft-for-review closing line is present and nothing is called final or an opinion.

## Guidelines

- Work in the source currency and units; translate only with a stated rate and date.
- Show the computation chain, not just results; a reviewer should recompute any line.
- Present options with the tax cost of each and the year it applies to; do not recommend a structure as the only answer.
- Quote ranges when a figure depends on an open election, proposed regulation or local law.
- Prefer the user's model structure; flag defects rather than rebuilding unasked.
- Do not opine on penalties, reportable transaction status or economic substance beyond flagging the question for the tax adviser.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| NCTI residual looks too low against a prior-year model | QBAI or 50 percent deduction carried forward | Rebuild with `references/us-international-rules.md` Sections 2 and 3 for the year |
| Credits exceed the limitation in one basket and are short in another | Baskets pooled | Separate the four categories; show NCTI excess as lost |
| Forms 5471 and the entity chart disagree on ownership | Chart not updated for a transfer | Use the executed transfer documents; write up the conflict; recompute pro rata shares by period |
| Treaty text unavailable or only a summary table | No primary text in the file | Apply statutory rates; list the treaty, article and protocol needed; mark [VERIFY] |
| GloBE workpapers in a different currency or year-end | Consolidated statements' currency and fiscal year | Compute in the GloBE currency for the fiscal year; translate for U.S. figures separately |
| Scanned or unreadable Form 8832 or election statement | Image file | Attempt extraction; if unreadable, treat the election as unproven and model both ways |
| Proposed regulation and the user's position differ | Reliance choice open | Show both readings and the reliance condition (rules followed in their entirety) |

## Related Skills

- managing-transfer-pricing-compliance: intercompany pricing, documentation and benchmarking, including arm's-length method, FAR and DEMPE analysis, the pricing of cost sharing buy-ins, platform contributions and 367(d) royalties, and APAs.
- analyzing-corporate-tax-structures: domestic entity choice, S corporation, QSBS, consolidated-group and PTE questions, and the domestic corporate AMT test outside the foreign-parented group rule.
- managing-international-withholding-tax: W-8 forms, QI and QDD compliance, Forms 1042 and 1042-S, operational treaty claims.
- analyzing-state-income-tax: state treatment and apportionment of NCTI, subpart F, section 78, section 250 and section 245A amounts.
- managing-income-tax-provisions: ASC 740 accounting for NCTI, Pillar Two top-up taxes and uncertain positions.
- analyzing-m-and-a-tax-implications: cross-border acquisition structure, stock versus asset purchases and 338 elections.
- managing-tax-controversy: IRS examinations, competent authority and treaty disputes.
- analyzing-partnership-tax-structures: partnership allocations and outside basis behind 1446 and 864(c)(8) exposures.

## Reference Files

- `references/us-international-rules.md`: rule set by taxable year, rate table, NCTI, subpart F, FTC, FDDEI, 245A, entity classification, 367 and cost sharing structure, inbound withholding, BEAT, foreign-parented corporate AMT test, intercompany loan interest limits and FIRPTA.
- `references/pillar-two-and-treaties.md`: GloBE mechanics, the side-by-side arrangement, treaty and LOB tests, 2016 Model rates and state conformity.
- `references/output-template.md`: deliverable sections, reconciliation checks X1 to X11, issue severity, hand-off table and accepted hand-ins.
- `references/primary-sources.md`: each authority checked with URL, method and date, and the [VERIFY] list.
