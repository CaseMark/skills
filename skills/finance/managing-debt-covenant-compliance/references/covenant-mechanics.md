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
- Read the accounting-terms section. Agreement W Section 1.02(g) construes accounting terms "in accordance with GAAP, as in effect from time to time" but, if a GAAP change would affect a ratio and an amendment is requested, the ratio is "interpreted on the basis of GAAP as in effect and applied immediately before such change" until amended; Section 1.02(h) ignores fair value elections under ASC 825-10-25 and ASC 470-20 bifurcation, valuing convertible debt "at the full stated principal amount thereof"; and its definition of "Capitalized Lease Obligations" keeps leases that would be operating leases under "GAAP as in effect on December 31, 2021" out of debt. Agreement V Section 13.07(a) has its own GAAP-change mechanism, computes ratios without giving effect to ASC 805, and bases lease accounting on "U.S. GAAP as in effect on the Closing Date".
- Read the cross-default clause. Agreement W Section 7.01(f)(i) is triggered when Material Indebtedness becomes due early or a holder may accelerate it "(with all applicable grace periods having expired)"; a waiver under this facility does not bind holders of other debt, so check each instrument's own cross-default.
- Use the compliance certificate exhibit as the form. Agreement W's compliance certificate covenant requires a schedule showing each run-rate and pro forma adjustment with a brief description (Section 5.11).
- Reporting entity: covenants usually run on the Borrower and its Restricted Subsidiaries. Remove Unrestricted Subsidiaries, and a parent's own results, using the consolidating information the agreement requires when parent financial statements are delivered instead (Agreement W Section 5.04(f); Agreement V Section 9.01(c)).

## 2. Test period, covenant level and step-downs

- The Test Period is defined, not assumed. Agreement W (Section 1.01): "the period of four consecutive fiscal quarters of the Borrower then most recently ended (taken as one accounting period) for which financial statements have been (or were required to be) delivered pursuant to Section 5.04(a) or 5.04(b)". A single-quarter or annualized test must be stated in the agreement.
- Agreement W has two maintenance covenants in Section 6.09: (a) a maximum Secured Net Leverage Ratio and (b) a minimum Fixed Charge Coverage Ratio of 1.20 to 1.00. Its Total Net Leverage Ratio is defined but is not the maintenance test.
- The first test date is in the covenant itself. Section 6.09(a): "Permit the Secured Net Leverage Ratio as of the last day of any Test Period (commencing with the Test Period ending on the last day of the Test Period ending on December 31, 2026) to be greater than (i) in the case of any Test Period ending on or prior to June 30, 2027, 4.50 to 1.00, (ii) in the case of any Test Period ending after June 30, 2027 and on or prior to June 30, 2028, 4.25 to 1.00, and (iii) in the case of any Test Period ending after June 30, 2028, 4.00 to 1.00".
- A step-down applies by reference to the end date of the Test Period, read from the grid's own words. The date the certificate is delivered does not move the level.
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

Caps differ in base and date. Agreement W (definition of "Adjusted Consolidated EBITDA", clause (b) proviso): for the Closing Date and Test Periods ending on or prior to December 31, 2026, run-rate savings and pro forma adjustments "shall not exceed 15% of Adjusted Consolidated EBITDA for any relevant Test Period (calculated after giving effect to such capped adjustments)"; from the Test Period ending March 31, 2027, the Aggregate Adjustment Cap covers clauses (a)(xi), (a)(xii), (a)(xiii) and (a)(xvi), run-rate savings and pro forma adjustments, which "shall not exceed 25% of Adjusted Consolidated EBITDA for the applicable Test Period (calculated prior to giving effect to such capped add-backs and adjustments)". Agreement V has no percentage cap on Pro Forma Cost Savings. Never assume a cap that is not in the text, and never drop one that is.

Cap arithmetic: with base B (EBITDA before the capped items) and capped items C, a cap of p percent of B allows min(C, pB). A cap of p percent of EBITDA after the capped items allows min(C, pB / (1 - p)). Show the base, the cap, the amount disallowed and the clause.

Earnings-release "Adjusted EBITDA", management EBITDA and GAAP operating income plus D&A are different measures. Reconcile each to Consolidated EBITDA in its own row; never paste one in as the other.

## 5. Debt, cash netting, fixed charges, ratios and headroom

- Debt: read where the ratio, not just the debt definition, fixes the measurement date. In Agreement W, "Consolidated Total Net Debt" is measured "as of any date of determination" (Section 1.01), but the covenant ratio fixes the date: the Secured Net Leverage Ratio counts secured Consolidated Debt "outstanding as of the last day of the most recently ended Test Period" less "the Unrestricted Cash Amount as of the last day of such Test Period", and the Total Net Leverage Ratio uses "Consolidated Total Net Debt outstanding as of the last day of the Test Period most recently ended as of such date" (both Section 1.01). Check what is in (capital leases, drawn letters of credit, purchase money debt) and out (undrawn letters of credit, earn-outs until due, defeased notes). Agreement V excludes acquisition debt between signing and closing except when testing that acquisition.
- Cash netting: only unrestricted cash, often capped (Agreement W's Unrestricted Cash Amount "shall not be deemed to be greater than 100% of Adjusted Consolidated EBITDA for the most recently ended Test Period"); equity cure proceeds are excluded from netting in the cure quarter (Agreement W definition of Specified Equity Contribution, clause (d)).
- Fixed charges: Agreement V uses cash interest plus scheduled principal; the numerator deducts unfinanced cash capex, cash taxes and certain dividends.
- Test the unrounded ratio against the level unless the agreement has a rounding clause; round only for display. Without a clause, 4.504x fails a 4.50x maximum even though it displays as 4.50x. Agreement W has no rounding clause. Agreement V Section 13.07(b) has one: ratios are calculated "carrying the result to one place more than the number of places by which such ratio is expressed herein and rounding the result up or down to the nearest number (with a rounding-down if there is no nearest number)"; apply such a clause exactly, show the unrounded and the clause-rounded figure, and flag any pass that depends on it. Apply the comparison exactly as written ("greater than", "less than").
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
| Due date on a non-Business Day | The stated date | Extends to the immediately succeeding Business Day "except as otherwise expressly provided" (Agreement W 1.04; Agreement V 1.11); a cure count keyed to the required delivery date runs from the extended date only if the agreement says so or the user's counsel confirms that reading |
| Waiver for debt classification (US GAAP) | Financial statements issued or available to be issued | Waiver must be in hand before that date (ASC 470-10-45-11(a)) |

Compute each date from its own trigger, give its weekday, say whether a Business Day roll moved it, count Business Days with the agreement's definition (Agreement W: any day that is not a Saturday, Sunday or day "on which commercial banks in New York City are authorized or required by law to remain closed"), check every holiday inside the counting window, and show the count.

## 7. Equity cures

- Read: eligible equity (cash common equity), any notice requirement, the window (which may open during the fiscal quarter itself) and its trigger, the number limits (per rolling four quarters, consecutive quarters, life of facility), the maximum amount (no more than needed), where it counts (EBITDA for the cure quarter and later Test Periods that include it, or debt paydown), and what it is disregarded for (baskets, pricing, other ratios).
- Agreement W: a cash common equity contribution "during the relevant fiscal quarter or on or prior to the day that is fifteen (15) Business Days after the day on which financial statements are required to be delivered", counted "at the request of the Borrower by written notice to the Administrative Agent of the intention to make such Specified Equity Contribution" (definition of "Specified Equity Contribution"); no more than five cures over the life of the facilities; in each four consecutive quarters, two quarters without a cure; amount capped at what is needed; disregarded for baskets and netting; no cash netting or debt reduction credit in the cure quarter; lenders need not fund during the 15 Business Day window until the cure is received.
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
| Undetermined | A required input is missing (including when the first hard stop applies); name the gap |

Forecast results carry the same labels with "(forecast)" in the Basis column.

## 9. Basket and builder basket register

- One row per basket: covenant (debt, liens, investments, restricted payments, junior debt payments, asset sales), basket name and clause, type (fixed dollar, grower tied to EBITDA or total assets, ratio-based, builder), capacity formula, usage to date with dates and transaction, remaining capacity, and whether reclassification between baskets is permitted.
- Grower baskets use EBITDA without cure amounts (Agreement W 7.02(b); Agreement V 10.11(b)).
- Builder basket roll (Agreement W "Available Amount"): starting point and start date (50 percent of cumulative Consolidated Net Income from the first day of the closing fiscal quarter), plus declined mandatory prepayments, returns from Unrestricted Subsidiaries, qualified equity proceeds, minus investments and restricted payments made from it, floored at zero. Check usage conditions (no Event of Default, sometimes a ratio test) at each use.
- Reconcile usage reported in prior certificates to the register; a use not reported is an open item, not an assumption.
