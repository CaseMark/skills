---
name: analyzing-loss-reserves
language: en
description: >
  Evaluates property and casualty loss and LAE reserves in drafts for review by a
  credentialed actuary: paid and reported loss development
  triangles by accident year, age-to-age and tail factor selection, chain ladder,
  Bornhuetter-Ferguson and Cape Cod with an independent expected loss ratio, IBNR,
  case reserve strengthening and settlement changes (Berquist-Sherman), paid versus
  incurred reconciliation, loss trend and social inflation, DCC and AO, salvage and
  subrogation, reinsurance recoverable collectibility, statutory discounting under
  SSAP No. 55 and SSAP No. 65, Schedule P reconciliation, carried reserve against a
  range of reasonable estimates, prior-year development and the adequacy side of
  reserve releases, ASC 944 claims development disclosures, and workpapers for an
  Appointed Actuary's Statement of Actuarial Opinion and AOS under ASOP Nos. 36 and
  43. Use for loss reserve review, reserve adequacy or reserve study review. Never
  issues an opinion or selects reserves to hit a target.
tags:
  - analysis
  - insurance
metadata:
  author: casemark
  practice_areas:
    - Insurance
    - Actuarial Science
    - Reinsurance
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---

# Analyzing Loss Reserves

Evaluates property and casualty loss and loss adjustment expense (LAE) reserves: it builds or reviews development triangles, projects ultimate losses by several methods, selects an estimate and a range of reasonable estimates, compares the carried reserve with both, and reconciles every figure to Schedule P or the ledger, in the layout of `references/output-template.md`. Its aim is an unbiased estimate of unpaid claims; it never chooses assumptions to produce a target reserve, earnings result or ratio. Everything it produces is a draft for review by a credentialed actuary; it is not a Statement of Actuarial Opinion (SAO), an Actuarial Opinion Summary (AOS), or accounting or legal advice.

## Why This Skill Exists

A loss reserve is a forecast dressed as a balance. A chain ladder looks objective until the factors come from two immature years, the triangle stops at 120 months with development still running, or a claims department's case strengthening runs down the latest diagonal and is counted twice. A Bornhuetter-Ferguson estimate is only as independent as its expected loss ratio, and the plan loss ratio is the easiest one to grab. Reinsurance, salvage and subrogation, discounting and the DCC and AO split each move the net figure in ways that Schedule P and SSAP No. 55 and No. 65 constrain. And because reserves move earnings, people ask for reserves that hit a number. This skill puts every assumption on a register with a label, keeps paid and incurred evidence side by side, applies the statutory and GAAP basis as written, and keeps the opinion where the law puts it: with the Appointed Actuary.

## Where Mistakes Hide

Read each input with this suspicion before projecting from it.

| Input / Document | What It Is Used For | Where the Error Hides |
|---|---|---|
| Development triangles (paid and reported, by accident year) | Age-to-age factors and ultimates | Factors selected from one or two immature or volatile years, or driven by one large claim; triangles on mixed bases (gross and net, with and without DCC, net of salvage in one and not the other); latest diagonal not tied to Schedule P |
| Tail factor | Development beyond the last age | Tail omitted (1.000) while the last observed factors still exceed 1.000 and claims remain open; a benchmark tail with no source; the tail's leverage across every accident year not shown |
| Claims department changes (case reserve reviews, new systems, settlement initiatives) | Validity of reported and paid patterns | Case strengthening on the latest diagonal inflates reported factors and is applied to strengthened values, counting it twice; a settlement speed-up inflates paid factors; management says nothing changed while average case per open claim jumped |
| Paid and incurred indications | Method selection and weights | Paid and reported results averaged without explaining a gap; one method silently dropped; ASOP No. 43 multiple-method disclosure missing |
| Expected loss ratio for B-F and expected claims | IBNR for immature years | The business plan, budget or board target used as the a priori ratio; older loss ratios used without on-level or trend adjustment; Cape Cod cross-check not run |
| Loss trend and social inflation | ELR and late development | Trend ignored or set at general inflation while liability severities (verdicts, attorney representation) rise faster; older-year factors applied to a changed severity environment without sensitivity |
| Reinsurance treaties, Schedule F and ceded reserves | Net estimate | Full credit taken for ceded reserves on a reinsurer in liquidation or with paid recoverables over 90 days past due; net derived with a net-to-gross ratio that ignores treaty terms; retroactive reinsurance left in Schedule P |
| Salvage, subrogation and deductibles | Net of recoveries estimate | Anticipated salvage and subrogation deducted from an estimate already projected on data net of recoveries received; impaired recoverables or uncollectible deductibles credited |
| Stated basis (statutory or GAAP) and discount | Measurement | Statutory reserves discounted outside tabular workers compensation indemnity or long-term disability, or without a state prescribed or permitted practice; LAE discounted at all; Schedule P Part 2 reported net of discount |
| LAE records | DCC and AO estimates | Coverage-dispute attorney fees, bad-faith suit costs or adjusters coded as DCC (they are AO under SSAP No. 55), inflating the DCC triangle; AO reserve omitted |
| Carried reserve, point estimate and range | Carried reserve position | A carried amount below the point but inside the range called deficient; a range quoted with no stated basis; carried compared on a gross basis to a net range |
| Entity, pool share and line scope; who opines | Whose reserves, which figures, whose conclusion | Pool totals used for one participant's AOS; life, annuity or long-duration A&H reserves swept in; the analyst writing the Appointed Actuary's opinion or signing for her |
| Prior-year development and reserve releases | Adequacy of releases; AOS item E | A release presented as adequacy evidence without a re-estimate; one-year adverse development ratios rounded below 5% before the three-of-five-years test |

## Ground Rules

1. **Draft only.** Every estimate, range, label and exhibit is a draft for review by a credentialed actuary. Never call it final, signed, approved or an opinion; never state that reserves "make a reasonable provision", are "deficient" or are "redundant".
2. **Source-review gate.** Never call data missing until the inventory is checked and each file opened, including Schedule P parts, treaty schedules and claims memos. Classify every gap as an **unknown fact**, a **source conflict**, an **unverified external lookup** (industry factors, benchmark tails, reinsurer ratings), or a **policy election** (method weights, tail choice, intended measure), with what would settle it.
3. **Hierarchy of authority.** State insurance law, then the NAIC Annual Statement Instructions and SSAPs (statutory) or ASC 944 (GAAP), then ASOPs, then practice notes. For data, the filed Annual Statement and Schedule P govern over a reserve study's exhibits, which govern over management summaries and email. Name every conflict, show both values, say which controls and why; never resolve one silently.
4. **Citation discipline.** Every figure carries a source locator (document, exhibit, part, column, line or cell) or [UNVERIFIED]; every rule carries its citation from `references/primary-sources.md` or [VERIFY].
5. **No target-driven reserves.** Factors, tails, ELRs, trends, method weights and the selected point come from the evidence. Decline any request, from anyone, to choose them so the reserve, IBNR, a loss or combined ratio, earnings, surplus, RBC, an IRIS ratio or a covenant reaches a stated figure.
6. **Independent ELR.** A business plan, budget or target loss ratio is never the a priori ELR; it may appear only as a labeled sensitivity beside an independent ELR and the Cape Cod ELR.
7. **Every assumption labeled.** Each factor, tail, ELR, trend and weight is Supported, Judgmental or Unsupported under `references/reserving-methods.md` Section 14; an Unsupported assumption is an issue, not a footnote.
8. **Paid and incurred side by side.** Show both indications by year and explain every material gap before weighting.
9. **Basis as written.** Apply the stated basis: undiscounted statutory reserves unless SSAP No. 65 or a state prescribed or permitted practice allows a discount; LAE never discounted under SSAP No. 65; gross, ceded and net consistent; salvage and subrogation counted once.
10. **Range is not a point.** Report the carried position against both the range and the point with the labels and tests in `references/output-template.md` Section 7.
11. **The opinion belongs to the Appointed Actuary.** Prepare exhibits, reconciliations and the list of decisions; never write the opinion conclusion in a credentialed actuary's name or sign for one.
12. **P&C only.** Life, annuity and long-duration accident and health reserves and health benefit plan claim liabilities are out of scope; name them and route them.

## Checkpoint A: Pre-Draft Intake (Mandatory)

Collect these, then fill the source-review register (`references/output-template.md`, Header).

1. **Entity and scope:** legal entity, NAIC number, pool participation and lead company, lines, accident years, purpose, and which reserves are in scope (loss, DCC, AO, premium items).
2. **Loss data:** paid and reported triangles by accident year (or Schedule P Parts 2 and 3), claim counts, case reserves on the latest diagonal, with the basis of each.
3. **Exposure:** earned premium by year, rate changes for on-leveling, or another exposure base.
4. **Carried reserves:** case, IBNR, DCC and AO, gross and net, by line and year; Annual Statement Exhibit A amounts if statutory.
5. **Prior work:** the last reserve study or Actuarial Report, selected factors, tails and ELRs, and the prior point and range.
6. **Change information:** claims department memos on case reserving, systems, settlement practice; reinsurance program changes; large losses and catastrophes; trend studies.
7. **Recoveries:** treaties and ceded reserves by reinsurer; Schedule F aging; salvage and subrogation basis; deductible receivables.
8. **Basis:** statutory, GAAP or other; discounting and any state prescribed or permitted practice; materiality standard if one is set.
9. **Analysis date** and the statutory year-end in question, for the filing calendar check.

**Default fallbacks (each stated in the assumption register):** all-year volume-weighted factors as a starting point only, never as a selection without review; an exponentially decaying tail fitted to the last observed factors when no tail study exists, labeled Judgmental; an ELR from on-level, trended mature-year ultimate loss ratios when no pricing study exists; undiscounted reserves (SSAP No. 65 paragraph 10 overrides any user default to discount, except tabular workers compensation indemnity, long-term disability or a state prescribed or permitted practice); intended measure an actuarial central estimate unless the user names another.

**Hard stops.** Each tests the parties named; check them against parties the request implies but does not name (a parent holding company, a pool lead, a buyer or seller, the CFO acting for the board).
- **No loss data.** A projection of ultimate or unpaid losses is requested for an entity or line, and no paid or reported loss history by accident, report or policy year for that entity or line is in the file (triangle, Schedule P Parts 2 and 3, or a claims extract, supplied as a document or a labeled excerpt). Stop the projection for that line; list what is needed. Netting, reclassifying or comparing an estimate the file already contains is not a projection.
- **Target-driven selection.** Anyone (the user, management, the board, a parent or pool lead, a buyer, seller, lender or rating agency) asks that a factor, tail, ELR, trend, weight, point or range be chosen or moved so a reserve, IBNR, release, ratio, earnings, surplus, RBC, IRIS result or covenant reaches a stated figure. Decline that part.
- **Opinion or sign-off.** The request is to issue, sign, date or finalize an SAO or AOS, to write the OPINION paragraph's conclusion or the risk of material adverse deviation answer in the name of the Appointed Actuary or any other actuary, or to state that a credentialed actuary reached a conclusion she has not reached. Decline that part; prepare the exhibits and decision list instead.
- **Out-of-scope reserves.** An adequacy conclusion is requested, for the company, an affiliate or a pool member, on life, annuity or long-duration A&H reserves (contract reserves, long-term care, Actuarial Guideline LI) or health benefit plan claim liabilities. Decline that part.
- **Filed figures set aside.** The user, the company or its parent directs that filed Annual Statement or Schedule P figures be replaced with management figures without a written conflict note. Stop until the conflict is documented.

A declined part carries the fixed label in `references/output-template.md` Section 13, using the hard stop's bold name, and the rest of the deliverable is completed.

## Step 1: Inventory, Scope and Stated Basis

Open every file and fill the source-review register. Record the entity, pool share, lines, years and the three dates. Read `references/statutory-and-gaap-rules.md` Sections 1 to 6 and write Section 1 of the template: basis, discount, risk margin, gross or net, recoverables, LAE types, salvage and subrogation, intended measure. Apply the hard stops now.

## Step 2: Data Reconciliation and Diagnostics

Read `references/reserving-methods.md` Sections 1 and 7 and `references/statutory-and-gaap-rules.md` Section 8. Tie the data used to Schedule P Parts 1 to 3 or the ledger (check R1). Run the diagnostics: paid to reported ratios, average case per open claim, disposal rates, large losses, and any calendar-year diagonal effect. Record each operational change with its date and evidence.

## Step 3: Factor and Tail Selection

Read `references/reserving-methods.md` Sections 2 and 3. Compute link ratios and averages for paid and reported triangles; select each factor with its label and the years excluded or adjusted; support the tail or fit one, and show its dollar effect and a sensitivity. Restate data for a detected case adequacy or settlement change before selecting (Section 7).

## Step 4: Projection Methods

Read `references/reserving-methods.md` Sections 4 to 6 and 9. Run development on paid and reported data; build the ELR from an independent source with on-level and trend adjustments and run B-F; run Cape Cod as the data-derived cross-check. Fill template Section 5 and checks R2 to R5.

## Step 5: Reconcile Paid and Incurred and Select

Read `references/reserving-methods.md` Sections 8 and 13. Explain every material paid-versus-reported gap by a named cause; weight methods by year with reasons; select the estimate and build the range with its basis; run sensitivities (tail, ELR, trend, case adjustment).

## Step 6: LAE, Salvage and Subrogation, Reinsurance and Discount

Read `references/reserving-methods.md` Sections 10 to 12 and `references/statutory-and-gaap-rules.md` Sections 5 to 7. Test the DCC and AO classification and estimate AO; confirm salvage and subrogation is counted once; derive ceded and net by treaty and show net with and without doubtful recoverables; test any discount against SSAP No. 65 and the state. Run R6 to R8.

## Step 7: Carried Reserve Position and Development History

Read `references/output-template.md` Sections 7 and 9. Assign the carried position label on each basis with its test, and compute one-year development and the AOS item E test from Schedule P Part 2 and surplus. Treat any release as a question of whether the re-estimate supports it; hand earnings-management questions to analyzing-earnings-quality.

## Step 8: Regulatory and Disclosure Workpapers

Read `references/statutory-and-gaap-rules.md` Sections 9 to 11. For statutory work, prepare the Exhibit A and B data checks, the Schedule P reconciliation exhibit, the AOS figures on the company's own share, and the filing calendar check (template Section 10), leaving every opinion decision to the Appointed Actuary. For GAAP work, prepare the ASC 944 claims development tables and reconciliation.

## Step 9: Issues, Declines and Hand-offs

Complete the reconciliation table (R1 to R10); every Fail becomes an issue ranked by the template's severity rule. Write declined parts with the fixed label, complete hand-offs, and the open items and [VERIFY] list.

## Checkpoint B: Post-Draft Alignment

Before the Quality Audit, re-read the request and confirm:
- The deliverable answers the question asked (estimate, review of a study, carried position, disclosure tables or opinion workpapers) and states its scope limits.
- Every declined part carries the fixed label and the rest of the work is complete.
- No sentence states an opinion type, a reasonable-provision conclusion or a risk of material adverse deviation answer as the skill's own or as the Appointed Actuary's.
- Every instruction from the user that conflicts with a filed figure or a rule is written up, not followed silently.

## Quality Audit

Confirm each statement is true of the draft; fix the draft if one is not.

1. The data used ties to Schedule P or the ledger (R1), and the basis of every triangle is stated.
2. Every selected factor and the tail carry a label; no factor rests on immature, volatile or distorted years without a stated adjustment.
3. The tail is supported or fitted, its dollar effect is shown, and a tail of 1.000 is justified by the data.
4. Any case adequacy or settlement change is diagnosed, quantified and adjusted for, and its effect on each method is shown.
5. Paid and reported indications appear side by side by year with every material gap explained.
6. The B-F ELR is independent and documented, Cape Cod is shown, and any plan ratio appears only as a labeled sensitivity.
7. Trend, including social inflation where liability lines are involved, is stated with its source and tested.
8. DCC and AO follow the SSAP No. 55 lists; salvage and subrogation is counted once; gross minus ceded equals net and doubtful recoverables are shown.
9. No statutory discount is applied outside SSAP No. 65 or a confirmed state practice, and no LAE is discounted.
10. The carried position label matches its written test on each basis, and the range basis is disclosed.
11. Prior-year development and the item E test use unrounded ratios from Schedule P Part 2 and the company's own share.
12. No declined part is replaced by a figure produced another way, and no opinion language appears.
13. Every figure has a source locator or [UNVERIFIED], every rule a citation or [VERIFY], and the closing line from the template is present.

## Guidelines

- Work in Schedule P units (thousands) for statutory work unless the user's materials use another unit; state it once.
- Prefer the structure of a reserve study the user supplies; flag defects rather than rebuilding unasked.
- Present sensitivities with the same care as the selected estimate; the range and its basis are part of the answer.
- Quote ranges for anything that depends on a policy election.
- Describe releases and strengthening in terms of evidence, never in terms of the earnings they produce.
- Keep claim-level personal information out of the deliverable; aggregate to the level the analysis needs.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Latest diagonal does not tie to Schedule P | Different basis (gross versus net, DCC, salvage), pooling share or a remapped line | Reconcile item by item; if unexplained, record a source conflict and use Schedule P |
| Reported and paid ultimates diverge sharply | Case adequacy or settlement change | Run the diagnostics in `references/reserving-methods.md` Section 7 and restate |
| One accident year's factors are far off the rest | Large loss, catastrophe, or thin data | Separate or cap the loss and develop it alone, or exclude with a label |
| Triangle is a scan or partly unreadable | Degraded input | Attempt extraction; record unreadable cells; use Schedule P for those years; list dependent outputs |
| Only a reserve study summary is supplied | No underlying data | Review the study's assumptions and labels; any new projection is blocked under No loss data |
| Treaty terms unclear for ceded IBNR | Missing treaty or schedule | Show net under the stated assumption with [UNVERIFIED] and the gross-to-net sensitivity |
| Study and Annual Statement carried amounts differ | Timing, late adjustments or pool share | Use the filed amount; write up the conflict |
| Benchmark factors requested but not provided | Unverified external lookup | Mark [VERIFY] with the source needed; do not fill from memory |

## Related Skills

- analyzing-earnings-quality: whether reserve releases or prior-year development were used to manage reported earnings and how they affect normalized earnings; this skill supplies the adequacy re-estimate.
- managing-reinsurance-programs: reinsurer credit and counterparty evaluation behind a collectibility concern raised here.
- managing-insurance-regulatory-filings: preparing Schedule P, Schedule F, risk-based capital and other annual statement schedules.
- managing-claims-analysis: claims department severity and frequency trending and case reserve monitoring behind a case adequacy change.
- analyzing-insurance-financials: combined ratio, capital and company-level financial analysis that uses this skill's reserve result.
- analyzing-premium-pricing: rate indications and loss cost estimates; a pricing ELR used here must carry its own derivation.
- managing-insurance-capital-modeling: reserve risk in economic, regulatory or rating agency capital models.
- analyzing-catastrophe-risk: catastrophe model output for event losses reserved separately.
- No finance skill covers life, annuity or long-duration A&H reserve adequacy; refer those to a credentialed life or health actuary.

## Reference Files

- `references/reserving-methods.md`: data checks, factor and tail selection, chain ladder, B-F, Cape Cod, Berquist-Sherman adjustments, paid-incurred reconciliation, trend, LAE, salvage and subrogation, reinsurance, ranges and assumption labels.
- `references/statutory-and-gaap-rules.md`: hierarchy, ASOP Nos. 43, 36 and 20, SSAP Nos. 55, 65 and 62R, Schedule P, the 2026 NAIC actuarial opinion instructions, the filing calendar and ASC 944 disclosures.
- `references/output-template.md`: deliverable sections, assumption register, carried position and item E label tests, reconciliation checks R1 to R10, declined-part label, hand-off table.
- `references/primary-sources.md`: each authority checked with URL, method and date, and the [VERIFY] list.
