# Covenant Mechanics

Calculation and timing rules for the quarterly compliance package. Read the section named in the SKILL.md step before doing that step. Every term below is a pattern seen in filed credit agreements; the executed agreement, as amended, governs every number. Two filed agreements are used as worked references throughout, both read in full on EDGAR (see `references/primary-sources.md`):

- **Agreement W**: Westrock Coffee credit agreement dated October 21, 2026 (term loan and revolver with maintenance covenants), Exhibit 10.1, accession 0001104659-26-117845.
- **Agreement V**: Verra Mobility amended and restated ABL revolving credit agreement dated October 17, 2025 (springing fixed charge covenant), Exhibit 10.1, accession 0001193125-25-242530.

## Contents

1. Reading the agreement
2. Test period, covenant level and step-downs
3. Springing covenants
4. Consolidated EBITDA bridge
5. Debt, cash netting, fixed charges, ratios and headroom
6. Clocks: each element with its own trigger
7. Equity cures
8. Default, Event of Default and the status vocabulary
9. Basket and builder basket register

## 1. Reading the agreement

- Work from a conformed copy that folds in every amendment, waiver, consent and joinder, then confirm it against the executed amendments themselves. A conformed copy prepared by counsel ranks below the executed instruments.
- Read in full: the definitions article (Consolidated EBITDA, Consolidated Net Income, Pro Forma Basis, Test Period, the debt and cash definitions, Restricted and Unrestricted Subsidiary, Specified Equity Contribution or Cure Amount, Available Amount, Required Lenders and every class-vote definition); the financial covenant section; the reporting covenant section; the Events of Default article and the right-to-cure section; the amendments section; the accounting-terms section (frozen GAAP, lease treatment); and the business-day timing section.
- Use the compliance certificate exhibit as the form. Agreement W's compliance certificate covenant requires a schedule showing each run-rate and pro forma adjustment with a brief description (Section 5.11).
- Reporting entity: covenants usually run on the Borrower and its Restricted Subsidiaries. Remove Unrestricted Subsidiaries, and a parent's own results, using the consolidating information the agreement requires when parent financial statements are delivered instead (Agreement W Section 5.04(f); Agreement V Section 9.01(c)).

## 2. Test period, covenant level and step-downs

- The Test Period is defined, not assumed. In Agreement W it is the four consecutive fiscal quarters most recently ended "for which financial statements have been (or were required to be) delivered". A single-quarter or annualized test must be stated in the agreement.
- The first test date is in the covenant itself (Agreement W: commencing with the Test Period ending December 31, 2026).
- A step-down applies by reference to the end date of the Test Period, read from the grid's own words (Agreement W: 4.50x for any Test Period ending on or before June 30, 2027; 4.25x for Test Periods ending after June 30, 2027 and on or before June 30, 2028; 4.00x after). The date the certificate is delivered does not move the level.
- Step-up elections (Agreement W allows a 0.50x step-up after a specified acquisition, capped at 4.50x, for four full fiscal quarters, at most twice) require a timely written notice; confirm the notice exists before using the higher level.

## 3. Springing covenants

- Read the trigger exactly: what is measured (revolver loans, letter of credit exposure, availability), what is excluded (undrawn letters of credit up to a dollar amount, cash-collateralized letters of credit), the threshold, and the date measured (last day of the fiscal quarter, or any day).
- Agreement V: the fixed charge coverage ratio of at least 1.0x applies on any date when Availability is below the greater of 10.0 percent of Aggregate Commitments and $15.0 million, tested for the four quarters ending with the most recent quarter for which financial statements were delivered, and at the end of each later quarter until Availability has exceeded the threshold for 30 consecutive days.
- A quarter-end utilization test is measured at quarter end. A repayment after quarter end does not change whether that quarter is tested; a draw after quarter end does not make it tested.
- When the covenant is not tested, record "Not tested" with the trigger computation; still compute the ratio for the lender package if the agreement or user requires it, labeled informational.
- Springing covenants often benefit only revolving lenders; waivers and amendments of them commonly need the revolving class vote (Section 1 of `references/amendments-classification-and-lmt.md`).

## 4. Consolidated EBITDA bridge

Start where the definition starts (usually Consolidated Net Income, itself defined with exclusions), then one clause per row.

| Row | Rule |
|---|---|
| Starting point | Consolidated Net Income as defined; list its exclusions (extraordinary or non-recurring items, Unrestricted Subsidiary income except cash distributions, effects of purchase accounting) |
| Standard add-backs | Interest, taxes, D&A, non-cash charges, each "to the extent deducted" and "without duplication"; a non-cash accrual added back now is deducted when paid later (Agreement V clause (iv); Agreement W clause (a)(iv)) |
| Category add-backs | Restructuring, integration, severance, transaction costs: check each against the clause that names it and its own cap |
| Clause sublimits | Dollar caps per Test Period (Agreement W: public company costs up to $2.5 million; litigation and investigation costs up to $1.0 million) |
| Run-rate savings and synergies | Only for actions taken, initiated or expected within the stated window (12 months in Agreement W; 24 months in Agreement V), reasonably quantifiable or identifiable and factually supportable, net of benefits already realized, and dropped if not achieved in time (Agreement V) |
| Aggregate cap | Apply the cap with its base and its effective dates (below) |
| Pro forma | Acquired EBITDA in, Disposed EBITDA out, for the full Test Period; pro forma adjustments often share the cap |
| Deductions | Non-cash gains, FX gains, minority interest per the definition |
| Deemed figures | Some agreements fix EBITDA for pre-closing quarters (Agreement W deems quarterly amounts for September 30, 2025 through September 30, 2026); use them for those quarters only |

Caps differ in base and date. Agreement W: for Test Periods ending on or before December 31, 2026, run-rate savings and pro forma adjustments may not exceed 15 percent of EBITDA "calculated after giving effect to such capped adjustments"; from the Test Period ending March 31, 2027, an Aggregate Adjustment Cap of 25 percent applies to clauses (a)(xi)-(xiii), (a)(xvi), run-rate savings and pro forma adjustments, "calculated prior to giving effect to such capped add-backs". Agreement V has no percentage cap on Pro Forma Cost Savings. Never assume a cap that is not in the text, and never drop one that is.

Cap arithmetic: with base B (EBITDA before the capped items) and capped items C, a cap of p percent of B allows min(C, pB). A cap of p percent of EBITDA after the capped items allows min(C, pB / (1 - p)). Show the base, the cap, the amount disallowed and the clause.

Earnings-release "Adjusted EBITDA", management EBITDA and GAAP operating income plus D&A are different measures. Reconcile each to Consolidated EBITDA in its own row; never paste one in as the other.

## 5. Debt, cash netting, fixed charges, ratios and headroom

- Debt: the agreement's debt definition at the test date (Agreement W measures Consolidated Total Net Debt "as of the last day of the Test Period"). Check what is in (capital leases, drawn letters of credit, purchase money debt) and out (undrawn letters of credit, earn-outs until due, defeased notes). Agreement V excludes acquisition debt between signing and closing except when testing that acquisition.
- Cash netting: only unrestricted cash, often capped in dollars; equity cure proceeds are excluded from netting in the cure quarter (Agreement W definition of Specified Equity Contribution, clause (d)).
- Fixed charges: Agreement V uses cash interest plus scheduled principal; the numerator deducts unfinanced cash capex, cash taxes and certain dividends.
- Ratios to two decimals as the agreement rounds (check for a rounding clause); test ≤ or ≥ exactly as written ("greater than", "less than").
- Headroom: EBITDA cushion = EBITDA minus (Debt ÷ maximum ratio), in dollars and as a percentage of EBITDA; debt capacity = maximum ratio × EBITDA minus Debt. Report the next Test Period's level beside the current one when a step-down is coming.

## 6. Clocks: each element with its own trigger

| Element | Trigger event | Pattern in filed agreements (confirm in yours) |
|---|---|---|
| Quarterly financial statements | End of each of the first three fiscal quarters | 45 days (Agreement W 5.04(b); Agreement V 9.01(a)) |
| Annual audited financial statements | Fiscal year end | 90 days, opinion without going concern or scope qualification, with carve-outs for an upcoming maturity or a potential covenant breach (Agreement W 5.04(a); Agreement V 9.01(b)) |
| Compliance certificate with covenant calculations | Delivery of the financial statements | Concurrent (Agreement W 5.11) |
| No-default certificate and Available Amount usage | Delivery of the financial statements | Within 10 Business Days of delivery (Agreement W 5.04(c)) |
| Equity cure deadline | The day financial statements are required to be delivered (Agreement W); or becoming subject to the springing test or delivering the statements (Agreement V) | 15 Business Days (Agreement W); 10 Business Days (Agreement V) |
| Notice of Default | A Responsible Officer obtaining actual knowledge | Promptly (Agreement W 5.05(a)) |
| Financial covenant breach | The test date result | No grace; Event of Default subject only to the cure right (Agreement W 7.01(d) with 7.02; Agreement V 11.03(i) with 10.11(b)) |
| Other covenant breach, including late reporting | Written notice from the agent (or Required Lenders) | 30 days after notice (Agreement W 7.01(e); Agreement V 11.03(iii)) |
| Interest or fee non-payment | Due date | 5 Business Days (Agreement W 7.01(c); Agreement V 11.01) |
| Misrepresentation in a certificate | Notice from the agent, if curable | 30 days (Agreement W 7.01(a)) |
| Springing test release | Availability back above threshold | 30 consecutive days (Agreement V 10.11(a)) |
| Due date on a non-Business Day | The stated date | Extends to the next Business Day unless the agreement says otherwise (Agreement V 1.11) |
| Waiver for debt classification (US GAAP) | Financial statements issued or available to be issued | Waiver must be in hand before that date (ASC 470-10-45-11(a)) |

Compute each date from its own trigger, count Business Days with the agreement's definition and the holidays that apply, and show the count.

## 7. Equity cures

- Read: eligible equity (cash common equity), the window and its trigger, the number limits (per rolling four quarters, consecutive quarters, life of facility), the maximum amount (no more than needed), where it counts (EBITDA for the cure quarter and later Test Periods that include it, or debt paydown), and what it is disregarded for (baskets, pricing, other ratios).
- Agreement W: no more than five cures over the life of the facilities; in each four consecutive quarters, two quarters without a cure; amount capped at what is needed; disregarded for baskets and netting; no cash netting or debt reduction credit in the cure quarter; lenders need not fund during the 15 Business Day window until the cure is received.
- Agreement V: no more than two in any twelve fiscal months and five over the term; no pro forma debt reduction; no borrowing during the interim period; no acceleration during it.
- Minimum cure where the cure counts as EBITDA: (Debt ÷ maximum ratio) minus EBITDA. Never also reduce Debt by the cure when the agreement denies it.
- A cure deems the breach cured for the agreement; it does not change the GAAP financial statements.

## 8. Default, Event of Default and the status vocabulary

A Default is an event that with notice or lapse of time would become an Event of Default (Agreement V definition). Use only these status labels, exactly as written:

| Status | Use when |
|---|---|
| Compliant | Tested and passes with cushion at or above the watch threshold (10 percent of EBITDA unless the user sets another) |
| Compliant - watch | Tested and passes, cushion below the watch threshold, or a step-down within the next two Test Periods would fail at current figures |
| Not tested | A springing condition is not met at the measurement date; show the trigger computation |
| Default - grace period running | A covenant with a grace period is breached and the grace period has not run |
| Breach - cure available | A financial covenant fails, a cure right exists, its limits are met and its window is open |
| Breach - waived | A breach covered by an effective waiver; cite the waiver and its effective date |
| Event of Default | Breach with no grace period, no available or exercised cure, and no effective waiver |
| Undetermined | A required input is missing; name the gap |

Forecast results carry the same labels with "(forecast)" in the Basis column.

## 9. Basket and builder basket register

- One row per basket: covenant (debt, liens, investments, restricted payments, junior debt payments, asset sales), basket name and clause, type (fixed dollar, grower tied to EBITDA or total assets, ratio-based, builder), capacity formula, usage to date with dates and transaction, remaining capacity, and whether reclassification between baskets is permitted.
- Grower baskets use EBITDA without cure amounts (Agreement W 7.02(b); Agreement V 10.11(b)).
- Builder basket roll (Agreement W "Available Amount"): starting point and start date (50 percent of cumulative Consolidated Net Income from the first day of the closing fiscal quarter), plus declined mandatory prepayments, returns from Unrestricted Subsidiaries, qualified equity proceeds, minus investments and restricted payments made from it, floored at zero. Check usage conditions (no Event of Default, sometimes a ratio test) at each use.
- Reconcile usage reported in prior certificates to the register; a use not reported is an open item, not an assumption.
