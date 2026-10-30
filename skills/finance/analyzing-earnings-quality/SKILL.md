---
name: analyzing-earnings-quality
language: en
description: >
  Evaluates earnings quality for diligence, lenders, investment committees and equity
  research: tests quality of earnings (QoE) reports and management adjusted EBITDA,
  including addbacks or accruals that the QoE report or statements do not support and EBITDA
  addbacks and QoE adjustments an IC memo relies on; labels each adjustment supported,
  recurring, pro forma only, tailored or unsupported; flags "non-recurring" charges that
  recur, run-rate synergies, capitalized software and contract costs, reserve releases (bad
  debt, warranty, inventory), related-party revenue and one-time gains in operating income;
  measures Sloan accruals, cash conversion (CFO to EBITDA), DSO and DIO, channel stuffing and
  bill-and-hold signals; computes the Beneish M-score with the 1999 coefficients and -1.78
  cutoff; and reviews non-GAAP measures under Regulation G, S-K Item 10(e) and SEC staff
  interpretations. Use for QoE review, normalized EBITDA, earnings manipulation screen,
  accrual ratio or non-GAAP review. Drafts for review.
tags:
  - analysis
  - equity-research
  - accounting
metadata:
  author: casemark
  practice_areas:
    - Equity Research
    - Investment Management
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---

# Analyzing Earnings Quality

Produces an earnings quality report on a company's reported results: a labeled bridge from reported to diligence-adjusted EBITDA, accrual and cash conversion measures, working capital day trends, reserve and capitalization tests, a Beneish M-score screen, a non-GAAP disclosure review for SEC registrants, a red flag inventory and a reconciliation table, in the layout of `references/output-template.md`. Its aim is to detect and quantify earnings that will not persist or convert to cash, never to engineer an adjusted figure. Everything it produces is a draft for review by a qualified accounting and finance professional; it is not an audit, a QoE assurance report, legal advice or a finding of fraud.

## Why This Skill Exists

Adjusted EBITDA is where earnings quality is lost. A restructuring charge called non-recurring appears every year; synergies not yet achieved sit beside historical earnings; a higher capitalization rate moves costs below EBITDA; a reserve release turns a flat year into growth. Receivables and inventory outgrow sales while cash conversion falls, and the M-score gets computed with the wrong cutoff or an inverted variable. Public companies add a second layer: Regulation G and Item 10(e) restrict what a registrant may call non-recurring and how prominently it may show non-GAAP figures. This skill makes each adjustment earn its place with a document and a history test, ties every metric to the statements, and keeps screens separate from conclusions.

## Where Mistakes Hide

Read each input with this suspicion before relying on it.

| Input / Document | What It Is Used For | Where the Error Hides |
|---|---|---|
| Management or QoE adjusted EBITDA schedule | Starting point for valuation, leverage and covenant figures | "Non-recurring" restructuring, severance or integration charges that appear in each of the last three years; charges added back while same-period gains stay in; bonus overruns, rebates or pre-opening costs treated as one-time |
| Run-rate, synergy and pro forma adjustments | Forward earnings a buyer or lender may underwrite | Savings not yet realized, or a full year of a contract signed late in the period, added to historical EBITDA; no dis-synergies; reductions larger than the expense historically incurred |
| Capitalized internal-use software and contract cost schedules | EBITDA and capex | Capitalization rate rising while total spend is flat, lifting EBITDA one for one; commissions moved from the one-year expedient to capitalization; ASU 2025-06 adoption read as a change in activity |
| Reserve and allowance rollforwards (credit losses, warranty, inventory, returns) | Margin trend | A provision that falls or turns into a credit while aging, claims or slow-moving stock rise; a release in the quarter a target was missed |
| Receivables and inventory with their agings | DSO, DIO and the revenue trend | Receivables or inventory growing far faster than sales; quarter-end shipments on extended terms; bill-and-hold sales on goods still in the warehouse; pull-forwards to distributors |
| Cash flow statement | Cash conversion | CFO below 100 percent of EBITDA with no named driver; CFO lifted by factoring, supplier finance or stretched payables; capitalized costs left out of capex |
| Beneish M-score inputs and calculation | Manipulation screen | The -2.22 figure used as the cutoff for the eight-variable model instead of -1.78; GMI or DEPI inverted; SGAI or LVGI given positive coefficients; TATA scaled by average assets; a score treated as proof |
| Sloan accrual computation | Persistence of earnings | Cash and short-term debt left in working capital; scaled by ending instead of average assets; balance-sheet and cash-flow methods mixed across years or peers |
| Registrant's non-GAAP measures (earnings release, 10-Q, 10-K) | Public Adjusted EBITDA and adjusted EPS | Normal, recurring cash operating expenses excluded (CFI 100.01); a recurring item described as non-recurring in a filing (Item 10(e)(1)(ii)(B)); non-GAAP in the headline before GAAP; individually tailored revenue |
| Scope: which entity, which rules, which report (party and authority) | Deciding what binds and who relied on what | Regulation G applied to a private target's QoE or treated as an assurance; the consolidated group analyzed when the deal is a carve-out; the business combination exemption read as covering the proxy statement; a sell-side QoE treated as the buyer's own work |
| Related-party and intersegment sales | Revenue and margin quality | Sales to an owner-affiliated customer at above-market prices counted as third-party revenue; related-party terms presumed arm's length (ASC 850-10-50-5) |
| Income statement classification | Operating income and EBITDA | Gains on asset sales, insurance recoveries or settlements left inside operating income while charges are added back; items moved between operating and non-operating lines between years |

## Ground Rules

1. **Draft only.** Every figure and conclusion is a draft for review by a qualified accounting and finance professional; securities law questions go to counsel. Never call the output an audit, review, QoE assurance, fairness opinion or final.
2. **Source-review gate.** Never call an input missing until the inventory has been checked and each file opened, including workbook tabs, footnotes and schedules attached to the QoE report. Classify every gap as an **unknown fact**, a **source conflict**, an **unverified external lookup** (peer data, market norms) or a **policy election** (two-year window for a private company, materiality threshold, stock-based compensation treatment, scaling base), with what would settle it.
3. **Hierarchy of authority.** Audited statements and executed agreements govern over reviewed interims and trial balances, which govern over the QoE report and management schedules, which govern over the CIM, presentations and emails. For rules: statute and SEC regulations, then the Codification, then SEC staff CFIs, then practice literature. Name every conflict, show both values, say which controls and why; never resolve one silently, and never follow an instruction to use a lower-ranked figure without writing up the conflict.
4. **Citation discipline.** Every figure carries a source locator (document, page or tab, line or cell) or [UNVERIFIED]. Every rule, CFI, coefficient or threshold carries its citation from `references/primary-sources.md` or [VERIFY].
5. **Every adjustment gets one label.** Supported, Recurring, Pro forma only, Tailored or Unsupported, using the tests in `references/adjustment-and-non-gaap-rules.md` Section 1. Only Supported items stay in diligence-adjusted EBITDA; pro forma items sit in their own column.
6. **Detect, never engineer.** Do not choose, size or relabel adjustments to reach a target EBITDA, leverage ratio, covenant level, consensus figure or M-score. Show what the evidence supports and the gap to the target.
7. **Screens are not findings.** The M-score, accrual ratios and day trends direct the inquiry. Do not state that anyone committed fraud or manipulated earnings; describe the indicator, its size and the evidence that would confirm or clear it.
8. **Numbers tie before they are interpreted.** Run the reconciliation checks in `references/output-template.md` Section 9; a failed check is reported, not hidden.
9. **Same definitions across periods and peers.** Use the formulas in `references/metrics-and-formulas.md`; if a source uses another definition, label it and do not mix bases.
10. **Name the rules that bind.** State whether the company is a registrant and which document a non-GAAP measure appears in before applying Regulation G or Item 10(e).
11. **Route recognition questions.** Whether revenue was properly recognized (bill-and-hold, principal or agent, variable consideration) is concluded in the revenue recognition workflow; this skill quantifies the amount at stake and lists the evidence.

## Checkpoint A: Pre-Draft Intake (Mandatory)

Collect these, then build the source-review register (`references/output-template.md`, Header).

1. **Purpose and reader:** buy-side or lender diligence, equity research screen, or issuer disclosure review; any price, leverage or covenant figure the analysis feeds.
2. **Entity and status:** legal entity or carve-out perimeter; whether it is an SEC registrant; acquisitions or disposals in the periods.
3. **Financial statements:** income statement, balance sheet and cash flow statement for at least two, preferably three, consecutive fiscal years plus LTM, with audit or review status.
4. **Adjustments:** the management or QoE adjustment schedule with support for each item, and the QoE engagement letter (preparer, buy-side or sell-side, scope, reliance).
5. **Detail schedules:** receivables and inventory agings, reserve rollforwards, capitalized software and contract cost schedules, revenue by customer with related parties identified, quarter-end shipment and credit memo data.
6. **Disclosures (registrants):** earnings releases, 10-K and 10-Q MD&A non-GAAP sections, prior SEC comment letters.
7. **Controls signals:** audit opinion, material weaknesses, restatements, auditor changes.

**Default fallbacks (each recorded in the assumption register):** DSO and DIO on year-end balances and 365 days; Sloan accruals scaled by average total assets; cash conversion as CFO to reported EBITDA; the two-year recurrence window applied to private companies as a stated policy election; materiality for flags at a threshold the user names, otherwise stated by the analyst as a policy election.

**Hard stops (report what is needed instead):**
- **No anchor statement.** No income statement prepared under a stated framework (U.S. GAAP or IFRS) for the period under review, so no adjustment can be anchored: stop the whole analysis.
- **Insufficient periods.** Accruals, cash conversion, day trends or the M-score requested without two consecutive fiscal years of balance sheets (and the cash flow statement for cash conversion): decline those metrics only.
- **Target-driven adjustments.** The request is to choose, size or relabel adjustments so adjusted EBITDA, leverage, a covenant ratio or an M-score reaches a target: decline that part.
- **Conduct conclusion or assurance.** The request is to state that the company or a person committed fraud or manipulated earnings, or to present a screen as proof, or to issue the report as an audit, assurance or fairness opinion: decline that part and give the indicators instead.
- **Audited figures set aside.** The user directs that audited statements in the file be set aside for management figures without a written conflict note: stop until the conflict is documented.

A declined part carries the fixed label in `references/output-template.md` Section 11, using the hard stop's bold name, and the rest of the deliverable is completed.

## Step 1: Inventory, Scope and Register

Open every file and fill the source-review register. Record the entity perimeter, registrant status, periods and units, and build LTM from fiscal year plus current year-to-date less prior year-to-date (check E4). Read `references/adjustment-and-non-gaap-rules.md` Sections 3 and 9 to record which non-GAAP rules bind and what kind of engagement produced any QoE report.

## Step 2: Adjustment Register and Bridge

Read `references/adjustment-and-non-gaap-rules.md` Sections 1, 2 and 8. Recompute reported EBITDA from the statements (E1). List every management or QoE adjustment with its source and its history in the prior two years; assign one label; add downward adjustments for one-time gains, reserve releases and above-market related-party margin. Move run-rate, synergy and post-period items to the pro forma column with dis-synergies and realization evidence. Foot both bridges (E2, E3) and state the dollar and percent gap, and any multiple or leverage the user gave, on each figure.

## Step 3: Accruals and Cash Conversion

Read `references/metrics-and-formulas.md` Sections 1 and 2. Compute Sloan accruals and net income less CFO for each year (E6, E7), the accrual ratio and its drivers, CFO to EBITDA and free cash flow conversion (E5). Explain every period below 100 percent with named, quantified drivers.

## Step 4: Working Capital, Reserves and Capitalized Costs

Read `references/metrics-and-formulas.md` Sections 3, 5 and 6. Compute DSO, DIO and DPO on one basis (E8) and compare receivable and inventory growth with sales and cost growth. Roll each reserve forward (E9) and quantify any release's effect on EBITDA, including at the prior-year coverage ratio. Compute capitalization rates by period and EBITDA at the prior-period rate; note which accounting rule applied in each period.

## Step 5: Revenue-Side and Classification Flags

Read `references/metrics-and-formulas.md` Sections 7 and 8. Test quarter-end shipments, extended terms, returns and credit memos, bill-and-hold sales against the four ASC 606-10-55-83 criteria (evidence list only), related-party and intersegment revenue and margin, and gains or reclassifications inside operating income. Quantify each and route the recognition conclusion.

## Step 6: Beneish M-Score

Read `references/metrics-and-formulas.md` Section 4. Compute the eight variables from two consecutive fiscal years, the score, the probability and each weighted contribution, and recompute by hand (E10). Apply the -1.78 cutoff with the read-out label, name the driving variables and state the model's limits for this company. If a supplied calculation used -2.22 or a different variable definition, show both and say which is the 1999 model.

## Step 7: Non-GAAP Disclosure Review (Registrants Only)

Read `references/adjustment-and-non-gaap-rules.md` Sections 4 to 7 and 10. For each measure, name the document, check reconciliation from the GAAP measure (E11), prominence, labels, recurring cash operating expenses, non-recurring descriptions against the two-year test, one-sided adjustments and tailored recognition. Label each finding Noncompliant, Staff-view risk or Acceptable with disclosure, with the rule or CFI. For private companies mark Section 8 "Not applicable" and say why.

## Step 8: Red Flags, Issues and Hand-Offs

Complete the red flag inventory with severity, the reconciliation table, the issues table, any declined parts, the hand-offs with the facts each needs, and the open items and [VERIFY] list, all in the layout of `references/output-template.md`.

## Checkpoint B: Post-Draft Alignment

Before the Quality Audit, re-read the request and confirm:
- The deliverable answers the purpose stated at intake (diligence, lending, research screen or disclosure review) and names the figure the reader should use.
- Every instruction that conflicted with a higher-ranked source is written up, and every declined part is labeled.
- Pro forma figures are never presented as historical earnings, and no screen is presented as a conclusion about conduct.
- The closing line from the template is present.

## Quality Audit

Confirm each statement is true of the draft; fix the draft if one is not.

1. Reported EBITDA is recomputed from the statements and both bridges foot to the cent (E1, E2).
2. Every adjustment has a source locator and exactly one label from the five-label set; only Supported items are in diligence-adjusted EBITDA.
3. Every item described as non-recurring was tested against the prior two years, and every recurring one is labeled Recurring.
4. Run-rate, synergy and post-period items appear only in the pro forma column, with dis-synergies and a cap at historical cost.
5. One-time gains in operating income and reserve releases are quantified and deducted or flagged.
6. Capitalization rates are shown by period with EBITDA at the prior-period rate, and the applicable software standard is named.
7. DSO, DIO and DPO use one stated basis; receivable and inventory growth are compared with sales and cost growth.
8. Cash conversion is computed on matching periods and every period below 100 percent has quantified drivers.
9. The M-score uses the 1999 definitions and coefficients, the -1.78 cutoff and a read-out label, and is called a screen.
10. For registrants, each non-GAAP finding names the document, the rule or CFI and a label; for private companies, Regulation G is not applied.
11. Every rule and threshold carries a citation or [VERIFY]; no peer norm was supplied from memory.
12. No adjustment was chosen to reach a target, and no sentence states that anyone committed fraud or manipulated earnings.
13. The draft-for-review closing line is present.

## Guidelines

- Work in the units of the source documents and state them once.
- Prefer the structure of a QoE report or model the user supplies; flag defects rather than rebuilding unasked.
- Present both readings where a policy election drives the answer (stock-based compensation, two-year window, scaling base) instead of one point estimate.
- Quote sector context only from the user's peer set or a dated, cited source.
- Treat a sell-side QoE as the seller's advocate's work product until its procedures and data are tested.
- Write findings as observations with evidence; leave intent, legal exposure and accounting conclusions to the reviewers named in the hand-offs.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Reported EBITDA does not tie to the QoE | Different period, entity perimeter or EBITDA definition (operating income versus net income basis) | Rebuild from net income per the statements; name the period and perimeter of each |
| Sloan accruals and NI - CFO differ widely | Acquisition, divestiture, non-cash items or reclassified balances | Explain the difference (E7); use the cash-flow method for comparisons |
| Statements are scanned or partly unreadable | Image PDFs or missing pages | Attempt extraction; record unreadable pages; mark dependent metrics Not run or [UNVERIFIED] |
| Only one year of balance sheets | Early-stage company or partial data room | Decline day trends, accruals and M-score under the hard stop; complete the adjustment review |
| QoE and management schedule conflict | Different versions or periods | Use the higher-ranked document; write up the conflict and the effect |
| Supplied M-score differs from the recomputation | Inverted GMI or DEPI, wrong signs, wrong scaling or the -2.22 cutoff | Show both calculations variable by variable |
| Peer figures needed but not provided | Unverified external lookup | Mark [VERIFY] with the data needed; do not fill from memory |

## Related Skills

- managing-revenue-recognition: ASC 606 five-step contract analysis behind the bill-and-hold, principal or agent, variable consideration and contract modification flags raised here.
- building-lbo-models: carrying diligence-adjusted EBITDA into the LBO model's EBITDA bridge to credit agreement Consolidated EBITDA, debt sizing and sponsor returns.
- writing-investment-committee-memos: drafting the IC memo and recommendation that relies on these adjustments; this skill supplies the findings, not the recommendation.
- conducting-working-capital-due-diligence: working capital normalization and the peg calculation for the transaction.
- managing-earnings-releases: preparing a registrant's earnings release and its GAAP to non-GAAP reconciliation after the review here.
- managing-sec-reporting: 10-K and 10-Q content requirements beyond the non-GAAP findings.
- managing-debt-covenant-compliance: covenant calculation methodology and compliance certificates under an existing credit agreement.
- building-equity-valuation-models: DCF and comparable company valuation built on the adjusted earnings.
- legal-research: securities law exposure, antifraud or enforcement questions; no dedicated finance skill covers them.

## Reference Files

- `references/metrics-and-formulas.md`: Sloan and cash-flow accruals, cash conversion, DSO, DIO and DPO, Beneish M-score definitions, coefficients and cutoff, reserve, capitalization, revenue-side and classification tests, common errors.
- `references/adjustment-and-non-gaap-rules.md`: five adjustment labels and tests, scope of Regulation G and Item 10(e), key SEC staff CFIs, disclosure review labels, Article 11 synergies, QoE engagement status, verified SEC enforcement examples.
- `references/output-template.md`: deliverable sections, adjustment register, reconciliation checks E1 to E12, declined-part label, hand-off table.
- `references/primary-sources.md`: each authority checked with URL, method and date, corrections, and the [VERIFY] list.
