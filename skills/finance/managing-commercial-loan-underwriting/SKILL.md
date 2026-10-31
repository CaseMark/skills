---
name: managing-commercial-loan-underwriting
language: en
description: >
  Drafts commercial loan underwriting packages and credit memos for banks and nonbank
  lenders: financial spreads tied to source statements; cash available for debt service
  and DSCR after taxes, distributions and unfinanced capex; global cash flow across
  borrower, guarantors and affiliates; structure, amortization within collateral useful
  life and maximum loan amount; covenant levels with headroom; collateral and LTV on the
  lesser of cost or a lender-reviewed appraisal; appraisal and evaluation thresholds
  (12 CFR 34.43, $500,000 CRE threshold); CRE concentrations; Regulation O insider loans
  and board approval; Regulation B adverse action notices and spouse guaranty limits;
  Section 1071 compliance dates and firewall; leveraged lending
  status; policy tests, exceptions and a draft recommendation. Use for loan
  underwriting, credit memo, credit analysis, DSCR, global cash flow, risk rating or
  credit committee package. Declines to adjust spreads to meet policy thresholds.
  Drafts for credit officer review.
tags:
  - management
  - commercial-banking
  - risk
metadata:
  author: casemark
  practice_areas:
    - Commercial Banking
    - Trade Finance
    - Lending
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---

# Managing Commercial Loan Underwriting

Drafts the underwriting package for a commercial loan request: a spread tied to source statements, cash flow and global cash flow coverage, structure and covenants with headroom, collateral and LTV, the regulatory overlays that apply to the lender, policy tests and a draft recommendation, in the layout of `references/output-template.md`. Its aim is an accurate, sourced picture of repayment capacity and risk that a credit officer can rely on, whichever way the decision goes. Everything it produces is a draft for review by a qualified credit officer and, where a regulatory question turns on a legal reading, compliance staff or counsel; it never approves a loan or issues a commitment.

## Why This Skill Exists

Credit memos fail on definitions and on who is counted. A DSCR quoted on EBITDA looks strong until taxes, distributions and maintenance capex come out. Global cash flow that leaves out a guarantor's mortgage or the affiliate that owns the building overstates support. Appraisals ordered by the borrower, or reviewed by no one, set LTV. Amortization outruns the life of the equipment. Covenants are set at levels the borrower already fails. Insider loans go to a loan committee that has no authority under Regulation O, adverse action notices go out late with "internal standards" as the reason, and spouses are asked to sign guarantees Regulation B forbids. Section 1071's dates moved three times. And when the numbers miss policy, someone asks for the spread to be "cleaned up". This skill makes each of those choices visible, tests the request against the institution's own policy and the rules in force on the memo date, and keeps the numbers honest.

## Where Mistakes Hide

Read each input with this suspicion before drafting from it.

| Input / Document | What It Is Used For | Where the Error Hides |
|---|---|---|
| Borrower financial statements and tax returns | Spread, CADS and DSCR | DSCR computed on EBITDA instead of cash available for debt service after cash taxes, distributions (including pass-through tax distributions) and unfinanced maintenance capex; existing debt service left out of the denominator; interim periods annualized silently |
| Guarantor personal financial statements, personal returns and affiliate statements | Global cash flow and guarantor support; who is in the population | Guarantor's personal debt service, personal taxes and living expenses omitted; affiliate that leases to the borrower left out with its mortgage; distributions added to business cash flow already counted |
| Analyst or relationship manager adjustments to the spread | Normalized EBITDA and CADS | "One-time" expenses that recur every year added back; maintenance capex removed because it "will be financed"; projections or a friendlier DSCR method substituted to clear a policy minimum |
| Term sheet, structure proposal and covenant package | Amount, amortization, maturity, covenants | Amortization longer than the collateral's remaining economic life; covenant levels set from adjusted figures with no headroom test on actuals, producing a day-one default |
| Appraisal or evaluation | Collateral value and LTV | Appraisal ordered or provided by the borrower; stale effective date; no review before the decision; LTV on appraised value when a purchase price is lower; CRE over $500,000 treated as exempt |
| Institution capital and portfolio data | CRE concentration and pro forma ratios | CRE at or above 300 percent of total risk-based capital with 50 percent growth in 36 months ignored, or the 2006 guidance treated as a hard cap |
| Ownership charts and the bank's insider list | Regulation O screen of borrower, owners, guarantors and affiliates | A director's related interest not recognized; aggregation with existing credit skipped; loan committee approval used where the board must approve with the insider abstaining; a "director rate" below standard pricing; a proposed threshold applied before it is final |
| Decline decision, application file and draft notice | Regulation B notice of action taken | 30-day clock run from the decision date instead of the completed application; the over-$1 million business rule applied to a smaller business; "internal standards" given as the reason; wrong federal agency |
| Guaranty requirements in the approval conditions | Who must sign | A spouse with no ownership or role required to guarantee, contrary to 1002.7(d) |
| Section 1071 implementation plan | Demographic data collection and firewall | Superseded compliance dates; collection started before 1002.114(c)(1) permits it; underwriters given access to principal owners' race, ethnicity and sex without the 1002.108 determination and notice |
| Market benchmarks and leverage norms | Leverage limits | A 6.0x figure treated as a current OCC or FDIC rule after the December 5, 2025 withdrawal of the 2013 leveraged lending guidance |

## Ground Rules

1. **Draft only.** Every spread, test, label and memo is a draft for credit officer review. Never approve, decline, commit, sign as a credit officer, or describe the output as an approval or commitment.
2. **Source-review gate.** Never call a document missing until the inventory has been checked and each file opened, including schedules, tax return statements, appraisal addenda and policy excerpts. Classify every unsettled item as an **unknown fact**, a **source conflict**, an **unverified external lookup** (insider list, UCC search, flood determination, credit report) or a **policy election** (DSCR definition where the policy is silent, living expense figure, stress case), with what would settle it.
3. **Hierarchy of authority.** For figures: audited over reviewed over compiled statements, then tax returns, then company-prepared statements, then the relationship manager's summary. For terms: the institution's written credit policy and the approved term sheet over emails and verbal instructions. For law: the regulation in force on the memo date over guidance, and guidance over practice. Name every conflict, show both values, say which controls and why; never resolve one silently.
4. **Citation discipline.** Every figure carries a source locator (document, page, schedule, line) or [UNVERIFIED]. Every regulatory statement carries its citation from `references/primary-sources.md` or [VERIFY].
5. **Institution policy sets the thresholds.** Minimum DSCR, maximum LTV, advance rates, amortization limits and leverage limits come from the institution's policy. Never invent one; a test with no policy level is "Not tested - policy not supplied".
6. **Coverage is cash, and the population is complete.** DSCR uses cash available for debt service, not EBITDA, unless the written policy says otherwise; global cash flow includes every guarantor and every affiliate the policy requires, with their debt service, and lists who was excluded and why.
7. **No adjusting the spread to meet a threshold.** Adjustments follow documents. A request to add back, reclassify, omit or substitute figures, or to change the DSCR method or the global population, so that a policy minimum, covenant or approval target is met, is declined in that part; the draft shows the actual figures, the gap and legitimate options.
8. **Value of record.** LTV is tested only on a value the lender may use: an appraisal or evaluation it engaged or properly accepted and reviewed before the decision, and for a purchase, the lesser of cost and that value. Anything else is "Indicative - not value of record".
9. **Structure fits the collateral and the covenants fit the actuals.** Amortization never exceeds remaining economic life or the policy maximum. Every covenant is tested on actual figures and given a headroom figure before it is proposed.
10. **Screen every party.** The borrower, each owner of 10 percent or more, each guarantor and each controlled affiliate is screened against the insider list; insider credit is aggregated, priced like comparable non-insider credit, and sent for board prior approval when Regulation O requires it.
11. **Regulation B applies to every commercial applicant.** Notices run on the clock that fits the applicant's revenue, from the clock's own trigger, with specific reasons; spouses are never required as guarantors when 1002.7(d) bars it; Section 1071 obligations are stated as of the memo date.
12. **Rules are dated.** State each regulatory status as of the memo date; a proposal is never applied as if final; re-check before relying on any status in `references/regulatory-overlays.md`.

## Checkpoint A: Pre-Draft Intake (Mandatory)

Collect these, then build the source-review register (`references/output-template.md`, Header).

1. **Lender:** type and primary regulator; total assets if the notice agency depends on it; insider list access.
2. **Request:** amount, purpose, product, rate, amortization, maturity, collateral, guarantors, use of proceeds.
3. **Borrower financials:** three fiscal years of statements with quality, interim statements, business tax returns, debt schedule.
4. **Guarantors and affiliates:** personal financial statements, personal returns, affiliate statements and debt schedules, contingent liabilities.
5. **Collateral:** appraisals or evaluations with engagement letters and review, purchase contract, equipment or vehicle valuations with remaining economic life, environmental, title, UCC and flood items.
6. **Policy:** the institution's credit policy excerpts for each test, its risk rating scale, its exception authority.
7. **Institution data where relevant:** total risk-based capital, CRE and construction totals now and 36 months ago, unimpaired capital and surplus, total insider credit.
8. **Ownership:** every owner of 10 percent or more, and the insider screen result for each party.
9. **Regulation B facts for a notice:** date the application became complete, applicant's gross revenue for its preceding fiscal year, applications received last year, decision and its reasons.

**Default fallbacks (each disclosed as a policy election or unknown fact):** CADS as defined in `references/underwriting-rules.md` Section 2 where the policy is silent; a stress of revenue down 10 percent and rate up 200 basis points where the policy names none; the guarantor's stated living expenses, else an unknown fact. Where a regulation states the general rule differently, it overrides the default; `references/regulatory-overlays.md` Section 11 lists each override.

**Hard stops:**
- **Whole deliverable (label "Not produced - hard stop"):** when the deliverable includes a DSCR, global cash flow or recommendation, and there are no figures for the borrower's most recent completed fiscal year from statements, tax returns or a sourced spread (for a newly formed single-purpose borrower, the collateral property's operating statement for its most recent year); or a guaranty is proposed, the stated policy requires global cash flow, and there are no personal income, tax and debt service figures for that guarantor. Parties tested: the borrower and each proposed guarantor. Produce only the document request list.
- **Decline that part (label "Declined in part"; the rest is drafted):**
  - a request to issue, sign or describe the output as a credit approval, commitment or final decision;
  - a request to change, add back, reclassify, omit or substitute spread or cash flow figures, the DSCR definition or the global population in order to meet a policy threshold, covenant level or approval target;
  - a request to use as value of record an appraisal engaged or provided by the borrower or its broker, or one not reviewed by the lender, for a loan subject to the agencies' appraisal regulations;
  - a request to recommend or document credit to an insider of the bank or its affiliates (tested against the borrower, each owner of 10 percent or more, each guarantor and each company they control) on terms more favorable than comparable non-insider credit, or without the board prior approval 215.4(b) requires;
  - a request to send a Regulation B notice whose only reason is internal standards, policy or a score, or to require a spouse's or other non-applicant's signature or guaranty that 1002.7(d) bars.

## Step 1: Inventory, Parties and Register

Open every file and build the source-review register. List every party in `references/output-template.md` Section 2 and record each insider screen result; an unrun screen is an unverified external lookup. Read `references/regulatory-overlays.md` Section 4 now if any party may be an insider.

## Step 2: Spread and Tie-Out

Read `references/underwriting-rules.md` Section 1. Spread each period from the highest-ranked source, tie each total (check C1), and make each normalization adjustment one sourced row. Flag recurring "one-time" items by showing them across years.

## Step 3: Cash Flow, DSCR and Global Cash Flow

Read `references/underwriting-rules.md` Sections 2 and 3. Build CADS, recompute debt service from terms (C2, C3), compute business DSCR and global DSCR against their separate policy minimums, list the global population (C4), and run the sensitivities. Show any EBITDA-based figure only as a labelled secondary number.

## Step 4: Requested Adjustments

Read `references/underwriting-rules.md` Section 4. For each adjustment someone has asked for, decide whether a document supports it. Record unsupported ones in Section 12 of the template as "Declined in part" when they were requested to meet a threshold, show the gap in CADS dollars and turns, and list the legitimate options.

## Step 5: Structure, Covenants and Headroom

Read `references/underwriting-rules.md` Sections 5 and 6. Test amortization against remaining economic life (C6), compute the maximum loan amount at the policy DSCR, and test each proposed covenant on actual figures first (C7), labelling any failure "Day-one default".

## Step 6: Collateral, Appraisal and LTV

Read `references/underwriting-rules.md` Section 7 and `references/regulatory-overlays.md` Sections 1 and 2. Decide whether an appraisal or evaluation is required, who engaged it, whether it was reviewed and is still valid, and label each value. Compute LTV on cost and on value and test on the lesser (C5).

## Step 7: Regulatory Overlays

Read `references/regulatory-overlays.md` Sections 3 to 9 and the clock table in Section 10. Complete template Section 8 with a finding label for each overlay: CRE concentration pro forma, Regulation O aggregation, terms and approval (C8), Regulation B clocks from their own triggers (C9), reasons and signatures, Section 1071 status on the memo date, leveraged lending status, and SBA routing.

## Step 8: Policy Tests, Rating and Recommendation

Fill template Section 4 with a result label per test, using the written tests there. Propose a risk rating on the institution's scale or mark it not rated. Choose the draft recommendation label by the tests in template Section 1, in order.

## Step 9: Issues, Hand-offs and Open Items

Rank issues by the template's severity rule. Write each hand-off with the facts the receiving workflow needs, and list open items with gap class, owner and next action. Mark every [VERIFY] item.

## Checkpoint B: Post-Draft Alignment

- The deliverable matches the request (full memo, spread review, notice draft or regulatory check) and states its limits.
- Every declined part is in template Section 12 with its label, and the rest of the request was still drafted.
- No statement approves, commits or signs for the lender; the closing line is present.
- Every conflict between the user's instructions and the policy, the documents or a regulation is written up.

## Quality Audit

1. DSCR is computed on CADS after cash taxes, distributions and unfinanced capex, with debt service on all debt recomputed from terms.
2. Global cash flow names every included and excluded party, includes affiliate and personal debt service, and does not double count distributions.
3. Every spread total ties to its source, and every adjustment has a document and a reason.
4. No figure, method or population was changed to meet a threshold; any such request appears as "Declined in part".
5. Amortization is within remaining economic life and the policy maximum, and the maximum loan amount is computed.
6. Each covenant is tested on actual figures with a headroom figure; failures are labelled "Day-one default".
7. LTV uses the lesser of cost and a value of record; every other value is labelled "Indicative - not value of record".
8. The appraisal or evaluation requirement, engagement and review are tested under the lender's regulation, and CRE concentration ratios are shown pro forma where relevant.
9. Every party was screened for insider status; insider credit is aggregated, priced at standard terms and routed for board approval with abstention when required.
10. Each Regulation B clock runs from its own trigger with weekday stated; reasons are specific; the agency matches Appendix A; no barred spouse signature is required.
11. Section 1071 and leveraged lending statements match the status in `references/regulatory-overlays.md` as of the memo date, and no proposal is applied as final.
12. Every policy test, finding and recommendation label matches its written test, and the draft-for-review closing line is present.

## Guidelines

- Work in the source's units and state them once; never mix thousands and whole dollars.
- Present the downside case with the same care as the base case.
- Prefer the institution's own spreading template and definitions; flag defects rather than rebuilding unasked.
- Treat fair lending and insider rules as hard requirements, not underwriting judgment.
- Do not speculate about an applicant's protected characteristics, and never use them in analysis.
- Say plainly when a request does not work at the asked-for amount, and compute what would.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Spread does not tie to the statements | Reclassified lines or a different period | Re-spread from the source; record the difference as a source conflict |
| Tax return and statements disagree | Book-tax differences or a restated year | Reconcile through Schedule M-1 or M-3; name the controlling figure |
| Statements are scans or unreadable | Image-only PDF | Attempt extraction; if still unreadable, record it, list dependent outputs and request a readable copy |
| Guarantor PFS is over a year old or unsigned | Stale or unverified support | Use with [UNVERIFIED], request a current signed PFS, and show global cash flow without it |
| Appraisal effective date is old or the engagement letter is missing | Validity or independence unknown | Treat as "Indicative - not value of record" until engagement and review are confirmed |
| Policy excerpt missing for a test | Policy not supplied | Mark "Not tested - policy not supplied" and list as a policy election |
| Insider list not available | Screen not run | Record an unverified external lookup; recommendation becomes "Not ready for decision" if the screen could change a requirement |
| A regulatory status looks stale | Year-dependent rule | Check `references/primary-sources.md` and mark [VERIFY] with the date needed |

## Related Skills

- managing-debt-covenant-compliance: post-close covenant calculations, compliance certificates, waivers and headroom monitoring after the loan closes.
- analyzing-earnings-quality: addbacks or adjustments a QoE report or the statements do not support.
- managing-commercial-real-estate-lending: property-level CRE underwriting with property valuation, cash flow analysis and environmental review.
- analyzing-property-valuations: appraisal analysis across income, sales comparison and cost approaches.
- managing-construction-lending: draw schedules, budget tracking and completion risk for construction loans.
- managing-sba-lending: SBA eligibility, packaging and guaranty documentation under the SOP in effect.
- drafting-credit-memos: formatting a finished credit memo when the analysis here is complete.
- managing-credit-portfolio-risk: portfolio concentration metrics and stress testing beyond one loan's pro forma.
- building-lbo-models: reviewing a sponsor or lender LBO model behind an acquisition loan.
- term-loan-agreement: drafting the term loan agreement and covenant package once terms are approved.
- guaranty-agreement: drafting the guaranty, including payment versus collection and caps.
- loan-modification-agreement: documenting a CRE accommodation or workout.
- legal-research: Regulation O, Regulation B or Section 1071 questions that need a legal reading; no dedicated skill exists.

## Reference Files

- `references/underwriting-rules.md`: spreading, CADS and DSCR, global cash flow, disallowed adjustments, structure and useful life, covenant headroom, collateral and LTV, risk rating and policy tests.
- `references/regulatory-overlays.md`: appraisal and evaluation rules, supervisory LTV limits, CRE concentration and workout statements, Regulation O, Regulation B notices and signatures, Section 1071, leveraged lending status, SBA SOP, clock table and default overrides.
- `references/output-template.md`: deliverable sections, recommendation, policy test, value and finding labels with their tests, reconciliation checks, declined requests, hand-offs and open items.
- `references/primary-sources.md`: each authority checked with URL, method and date, the disposition of the prior version's content, and the [VERIFY] list.
