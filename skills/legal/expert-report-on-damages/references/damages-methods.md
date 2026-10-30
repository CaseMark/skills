# Damages Methods, Formulas and Consistency Rules

Working rules for building the damages analysis: choosing the measure, building the but-for and actual worlds, testing projections, removing overlap between categories, discounting, interest, and the special measures (reasonable royalty, unjust enrichment, personal economic loss). Authorities are listed with their check dates in the primary sources register. The measure of damages is a legal question for counsel; the expert quantifies the measure counsel identifies and says so in the report.

## Contents

1. Choose the measure and the plaintiff
2. The but-for and actual worlds
3. Lost profits: methods and the incremental margin
4. Testing management projections and other inputs
5. New and unestablished businesses
6. Causation, other causes and disaggregation
7. Mitigation
8. Overlap between damages categories
9. Valuation date, discounting and risk
10. Prejudgment interest and taxes
11. Reasonable royalty and patent lost profits
12. Unjust enrichment and disgorgement
13. Personal economic loss
14. Sensitivity and ranges

## 1. Choose the measure and the plaintiff

| Question | Why it matters | Who decides |
|---|---|---|
| Which claims survive (contract, tort, statute, IP), and which measure each allows (expectation, reliance, restitution, royalty, statutory) | A model that does not measure only the damages attributable to the liability theory fails (Comcast Corp. v. Behrend, 569 U.S. 27 (2013), decided at class certification; the principle that the model must match the theory is the useful part here) | Counsel instructs; expert records the instruction as an assumption |
| Which entity is the plaintiff, and whose losses are being measured | A subsidiary cannot ordinarily recover a parent's, affiliate's or shareholder's losses; consolidated statements overstate a single entity's loss `[VERIFY: governing law on affiliate and shareholder losses]` | Counsel; expert uses entity-level data |
| Contract limits: consequential-damages waiver, limitation of liability, liquidated damages, exclusive remedy | They may cap or exclude whole categories | Counsel applies the clause; expert computes each category separately so the clause can be applied |
| Period the law allows: limitations period, contract term, cure periods | Losses outside the period are not recoverable | Counsel; expert shows losses by period so any cut-off can be applied |

Compute each category and each period as a separate module so the court or jury can drop one without breaking the rest.

## 2. The but-for and actual worlds

- But-for world: the plaintiff's position had the defendant acted lawfully (which may mean an alternative lawful act, not no act at all; the choice is a legal question on which the expert takes counsel's instruction, per the FJC Reference Guide, 4th ed.).
- Actual world: what happened, from records kept in the ordinary course.
- Damages for a period = but-for result minus actual result, for the same entity, the same period, on the same accounting basis.

Consistency checks for every period table:

| Check | Fails when |
|---|---|
| Same dates | But-for uses a fiscal year (July-June) and actual uses calendar quarters; but-for runs 24 months and actual 20 |
| Same basis | Accrual revenue compared with cash receipts; gross revenue compared with net of returns and rebates |
| Same entity and scope | But-for from consolidated group projections; actual from the plaintiff entity alone |
| Same product scope | But-for includes product lines the claim does not reach |
| End date stated | Damages run past contract expiry or a date the law cuts off |

## 3. Lost profits: methods and the incremental margin

| Method | How it works | Main vulnerabilities |
|---|---|---|
| Before-and-after | Compares results in a clean period before (or after) the harmful act with results during it | Other changes between periods (market decline, pandemic, new competitor, price changes) attributed to the defendant |
| Yardstick (benchmark) | Uses comparable firms, stores, regions or product lines unaffected by the act | Comparables differ in size, maturity, geography, customer mix; selection not explained; only favorable comparables used |
| Sales projection or market model | Projects but-for sales from trend, regression, market size and share | Market share assumed, not derived; regression fit outside the data; trend window cherry-picked |
| Difference-in-differences | Change in the affected business minus change in a comparable unaffected one over the same periods | Unaffected group not truly unaffected; pre-period trends not parallel |

Lost profit = lost revenue x incremental margin, less any other costs avoided, plus any extra costs incurred because of the act.

- Incremental margin = revenue minus the costs that vary with the lost volume. It is not the gross margin from the income statement unless no selling, freight, commission or other costs vary with sales.
- Avoided costs include variable cost of goods, commissions, freight, royalties and any fixed or step costs actually shed (a warehouse lease ended, staff released). Costs fixed in the short run may become variable over a longer damages period (FJC Reference Guide, 4th ed., avoided costs).
- The measure is net, not gross, profit (Holt Atherton Indus., Inc. v. Heine, 835 S.W.2d 80 (Tex. 1992), Texas law; check the governing state).
- Show the cost classification table: account, amount, fixed or variable, basis for the classification.

## 4. Testing management projections and other inputs

Data sources in rough order of presumptive validity (FJC Reference Guide, 4th ed., Data Validity): government data; SEC filings and audited statements; records kept in the ordinary course; operating reports for management in the ordinary course; analyst reports; expert-designed surveys; marketing studies; industry reports; news articles; a company's damages study in the ordinary course; and last, a company's damages study prepared for litigation.

Before relying on any projection, budget or business plan, record:

| Test | Evidence |
|---|---|
| Who prepared it, when, and for what purpose (operations, lender, board, sale process, litigation) | Metadata, author testimony, board minutes |
| Assumptions behind each line (volume, price, cost, timing) | Workpapers, interview notes |
| Track record: earlier budgets and forecasts against actual results | Budget-to-actual table for at least three prior periods where available |
| Consistency with history, industry data and capacity | Growth rate against historical growth and market growth |
| Whether it pre-dates the dispute | Dates relative to the harmful act and the dispute |

The Third Circuit affirmed exclusion of a damages opinion built on a business plan when the expert did not know who prepared the figures or the assumptions behind them; there is no per se rule for or against business plans, and reliance is judged case by case (ZF Meritor, LLC v. Eaton Corp., 696 F.3d 254 (3d Cir. 2012)). An economist's model resting on assumptions without foundation in the record should have been excluded (Elcock v. Kmart Corp., 233 F.3d 734 (3d Cir. 2000)).

If a projection fails the tests, do not adopt it. Present a supported alternative (historical trend, yardstick or market model), show the projection-based figure only as a sensitivity labeled with its weaknesses, and report the reliance question to counsel. Communications between the expert and the client's managers are not protected by Rule 26(b)(4)(C), which covers only the party's attorney; interview notes and management emails containing facts or data are listed as considered.

## 5. New and unestablished businesses

- Reasonable certainty: lost profits need not be proven with mathematical precision but may not be speculative. Texas: a new business is not barred merely because it is new; the question is whether profits can be shown by objective facts, figures or data (Texas Instruments, Inc. v. Teletron Energy Mgmt., Inc., 877 S.W.2d 276 (Tex. 1994); Holt Atherton). New York: lost profits of a new venture receive greater scrutiny and must have been within the parties' contemplation for a contract claim (Kenford Co. v. County of Erie, 67 N.Y.2d 257 (1986), as applied in Schonfeld v. Hilliard, 218 F.3d 164 (2d Cir. 2000)). California: the trial court acts as gatekeeper and may exclude a speculative market-share projection for a new venture (Sargon Enters., Inc. v. University of S. Cal., 55 Cal. 4th 747 (2012)). Other states: `[VERIFY]`.
- Where lost profits of a new venture are too speculative, the market value of a lost income-producing asset (a contract, license or business) may be a recoverable alternative measure (Schonfeld).
- Useful evidence: the founders' track record in the same business, signed customer commitments, the plaintiff's own early results, a yardstick of comparable start-ups with their survival rate.

## 6. Causation, other causes and disaggregation

- Isolate the effect of the harmful act from other causes: industry downturn, pandemic, input costs, competitor entry, the plaintiff's own decisions. Use control groups, industry indices or regression, and show the adjustment.
- An opinion connected to the data only by the expert's say-so may be excluded: "too great an analytical gap" (General Elec. Co. v. Joiner, 522 U.S. 136 (1997)).
- When several acts are challenged and some may be held lawful, provide damages for the combinations the factfinder may reach; when acts interact, separate figures do not simply add (FJC Reference Guide, 4th ed., Disaggregation).

## 7. Mitigation

- The plaintiff cannot recover losses it reasonably could have avoided; actual mitigation earnings reduce damages (FJC Reference Guide, 4th ed., Mitigation of Losses). Whether mitigation efforts were reasonable is a factfinder question; the expert quantifies.
- Replacement business offsets the loss only if the plaintiff could not have had both. If it had capacity to serve the replacement customer and the lost one (a "lost volume" position), the replacement profit may not be an offset. That is a fact and law question: compute damages with and without the offset, state the capacity evidence, and flag it for counsel `[VERIFY: governing law on lost-volume claims]`.
- Measure the offset on the same incremental-margin basis and over the same months as the loss.

## 8. Overlap between damages categories

Build an overlap matrix before totaling. Rows and columns are the claimed categories; each cell answers "do these two measure the same dollars for the same period?"

| Pair | Usual overlap | Resolution |
|---|---|---|
| Lost profits and lost business value | A value as of date D capitalizes all cash flows after D, including those also claimed as lost profits after D | Use one framework: value at the breach date alone, or lost profits to date T plus value at T of flows after T |
| Lost profits and unjust enrichment (defendant's profits) on the same sales | Same sales counted twice | Present as alternatives, or deduct the overlap where the law allows both |
| Patent lost profits and reasonable royalty | Same units | Lost profits on units the patentee would have sold; royalty on the rest |
| Reliance (out-of-pocket) and expectation (lost profits) | Costs of building the business plus the profits it would have earned net of those costs | Choose one, or net the costs (FJC Reference Guide, 4th ed.) |
| Price erosion and lost volume | Erosion applied to units already in lost volume | Apply erosion only to units actually sold |

Comparing a value at one date with a sum at another date needs a stated interest or discount convention; never add amounts measured as of different dates without one.

## 9. Valuation date, discounting and risk

- Valuation date: sometimes set by law (breach of contract is typically valued as of the breach date); otherwise the experts may differ, and the choice changes the rates and the information available (FJC Reference Guide, 4th ed.). Get counsel's instruction and state it.
- Losses after the valuation date are discounted to present value at a rate reflecting the time value of money and a risk premium matched to the risk of that flow. Count risk once: either haircut the projected flows for risk or use a risk-adjusted rate, not both.
- Losses before the valuation date are brought forward (capitalized), often by the prejudgment interest the law sets (section 10); do not discount past losses with a forward-looking risk rate and then add statutory interest on top.
- For personal lost earnings, the discount rate reflects the safest available investment, and inflation should be treated consistently in the earnings growth and the rate (Jones & Laughlin Steel Corp. v. Pfeifer, 462 U.S. 523 (1983)).
- Show the formula: PV = sum over periods t of loss(t) / (1 + r)^t, with t measured from the valuation date and the timing convention (end of period or mid-period) stated.

## 10. Prejudgment interest and taxes

- Whether prejudgment interest is awarded, from what date, at what rate and whether it compounds are legal questions governed by statute, contract or the court's discretion. Example: New York requires interest on a sum awarded for breach of contract, computed from the earliest ascertainable date or from each item's date, fixed in the verdict and computed by the clerk (N.Y. C.P.L.R. 5001), at 9 percent per year unless a statute provides otherwise (C.P.L.R. 5004). Patent: prejudgment interest should ordinarily be awarded under 35 U.S.C. 284 (General Motors Corp. v. Devex Corp., 461 U.S. 648 (1983)). Post-judgment interest in federal court runs under 28 U.S.C. 1961.
- The expert does not opine that the plaintiff is entitled to interest or choose the statutory rate. Report damages before interest. If counsel instructs, add a separately labeled illustrative interest schedule stating the instructed rate, accrual dates and compounding.
- Interest never runs on losses dated after the valuation date.
- Taxes: when the loss and the award are taxed at the same rate, the adjustments cancel and pretax figures may be used; when treatment differs (capital gain against ordinary income; a non-taxable personal injury award against taxable wages), the difference is a disputed issue to address explicitly (FJC Reference Guide, 4th ed.) `[VERIFY: governing law on tax adjustment]`.

## 11. Reasonable royalty and patent lost profits

- 35 U.S.C. 284: damages adequate to compensate for infringement, in no event less than a reasonable royalty, with interest and costs as fixed by the court; the court may receive expert testimony on damages or a reasonable royalty.
- Patent lost profits (Panduit Corp. v. Stahlin Bros. Fibre Works, Inc., 575 F.2d 1152 (6th Cir. 1978)): demand for the patented product, absence of acceptable noninfringing substitutes, manufacturing and marketing capability, and the amount of profit.
- Reasonable royalty: hypothetical negotiation at the time infringement began, commonly framed with the Georgia-Pacific factors (Georgia-Pacific Corp. v. U.S. Plywood Corp., 318 F. Supp. 1116 (S.D.N.Y. 1970)).
- The 25 percent rule of thumb is inadmissible as a baseline (Uniloc USA, Inc. v. Microsoft Corp., 632 F.3d 1292 (Fed. Cir. 2011)). The entire market value of a multi-feature product may be the base only where the patented feature drives customer demand (Uniloc). Comparable licenses must actually support the rate the expert draws from them; reading a per-unit rate into licenses that do not show it is not based on sufficient facts or data (EcoFactor, Inc. v. Google LLC, 137 F.4th 1333 (Fed. Cir. 2025) (en banc)).
- Apportion: separate the value of the patented feature from unpatented features, the infringer's own contributions and the comparables' different terms.

## 12. Unjust enrichment and disgorgement

- Measure the defendant's gain attributable to the wrong: revenue from the tainted sales less the costs the law allows to be deducted, apportioned to the wrongful element. Burden allocations differ by statute (trademark, copyright, trade secret, fiduciary duty) `[VERIFY: governing statute]`.
- Do not add the defendant's gain to the plaintiff's lost profits on the same sales (section 8).

## 13. Personal economic loss

- Lost earnings and earning capacity: pre-incident earnings base, growth, worklife and survival probabilities, fringe benefits, post-incident residual earnings, taxes where the law requires, personal consumption in a death claim, and discounting (FJC Reference Guide, 4th ed., Loss of Personal Income; Jones & Laughlin).
- Every assumption about return to work, residual capacity or retirement age must have a basis in the record (Elcock).
- Personal injury wage-loss reports for a plaintiff's demand package go to economic-loss-report; this skill handles personal economic loss in commercial, employment and other matters where a retained expert report is required.

## 14. Sensitivity and ranges

- Vary only inputs that are genuinely uncertain, within ranges that have their own support (historical range, analyst range, comparable range). A sensitivity table is not a way to reach a preferred number.
- Show which single assumption moves the result most, so counsel and the court can see what the opinion depends on.
- Where a gap in the data makes a point estimate unsupported, give a range and the reason, or decline to quantify that category.
