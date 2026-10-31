# Output Template

Produce the header and sections below in this order. Numbers go in tables; prose stays short. Every figure carries a source locator, a register ID or [UNVERIFIED]. State currency and units once (for example USD thousands, matching Schedule P) and do not mix units.

## Contents

1. Header and source-review register
2. Section 1. Scope and stated basis
3. Section 2. Data reconciliation
4. Section 3. Assumption register
5. Section 4. Triangles and factor selections
6. Section 5. Method indications by accident year
7. Section 6. Selected estimate and range
8. Section 7. Carried reserve position
9. Section 8. LAE, salvage and subrogation, reinsurance
10. Section 9. Prior-year development and AOS item E test
11. Section 10. Filing calendar check
12. Section 11. Reconciliation checks
13. Section 12. Issues, conflicts and judgment calls
14. Section 13. Declined parts
15. Section 14. Hand-offs
16. Section 15. Open items and [VERIFY] list

## Header

- Entity (legal name, NAIC number if any, pool participation percentage and lead company), lines and accident years covered, purpose (internal review, audit support, diligence, workpapers for the Appointed Actuary, ASC 944 disclosure), date prepared, "Draft for review by a credentialed actuary."
- Accounting date, valuation date, review date (ASOP No. 43 section 4.1(d)).
- Source-review register, one row per file:

| File | Type | Date | Rank | Status | Pages, tabs or exhibits read | Note |
|---|---|---|---|---|---|---|
| name as received | Annual Statement, Schedule P, reserve study, claims extract, treaty, Schedule F, claims memo, plan, email | | 1-4 | Reviewed / Not relevant / Unreadable after attempt / Still needed | | |

## 1. Scope and stated basis

Statutory, GAAP or other; gross, ceded, net; discounted or nominal (items, rates, authority); explicit risk margin; provision for uncollectible recoverables; LAE types (DCC, AO); salvage and subrogation anticipated or not; intended measure of the estimate. Lines or reserves excluded and why.

## 2. Data reconciliation

| Line | Item | Analysis data | Schedule P or ledger (part, column, line) | Difference | Explained by |
|---|---|---|---|---|---|

Show that the data used in the analysis, not only the data received, ties to Schedule P (2026 ASI, paragraph 7.C).

## 3. Assumption register

| ID | Assumption (factor, tail, ELR, trend, weight) | Value | Source locator or [UNVERIFIED] | Label (Supported / Judgmental / Unsupported) | Gap class if open | Sensitivity tested? |
|---|---|---|---|---|---|---|

Labels follow `references/reserving-methods.md` Section 14. Gap classes: unknown fact, source conflict, unverified external lookup, policy election.

## 4. Triangles and factor selections

Each triangle with its basis line; link ratios; averages; the selected factor with its label and the years excluded or adjusted; the tail with its support; diagnostics (paid to reported, average case per open claim, disposal rates) and any diagonal effect found.

## 5. Method indications by accident year

| Accident year | Paid | Reported | Case | CDF (paid / reported) | Development paid | Development reported | B-F (ELR, source) | Cape Cod | Other | Selected ultimate | Weight and reason |
|---|---|---|---|---|---|---|---|---|---|---|---|

Then the paid versus reported reconciliation: difference by year and its named cause.

## 6. Selected estimate and range

Intended measure; selected ultimate and unpaid by year and line, gross and net; IBNR; range of reasonable estimates (low and high) with its basis (ASOP No. 43 section 4.2(a)); sensitivities (tail, ELR, trend, case adjustment) in dollars.

## 7. Carried reserve position

| Basis | Carried | Low | Point | High | Carried minus point | Carried minus low | Label |
|---|---|---|---|---|---|---|---|

Label tests (apply to each basis separately, net and gross):
- **Within range**: low <= carried <= high. Report the distance from the point; a carried amount below the point is still Within range.
- **Below range**: carried < low. Report the shortfall to the low end.
- **Above range**: carried > high. Report the excess over the high end.
- **Point comparison only**: no range was built; report carried minus point and state that a range is needed before a position label can be assigned.
These are analysis labels for the Appointed Actuary or other credentialed reviewer. They are not ASOP No. 36 opinion types, and the draft never states that reserves "make a reasonable provision" or are "deficient" or "redundant".

## 8. LAE, salvage and subrogation, reinsurance

- LAE: DCC and AO separately; any reclassification under the SSAP No. 55 lists with amounts moved.
- Salvage and subrogation: data basis, anticipated amount, any double count removed.
- Reinsurance: gross, ceded and net by treaty; recoverables at risk (reinsurer, reason, amount); net shown with and without doubtful recoverables.

## 9. Prior-year development and AOS item E test

| Calendar year | Prior year-end surplus | One-year development (Schedule P Part 2 Summary; positive = adverse) | Ratio | Adverse over 5%? |
|---|---|---|---|---|

Label tests: one-year development is **Adverse** when the current year-end estimate for prior accident years exceeds the prior year-end estimate, **Favorable** when it is lower. **Item E required** when the ratio exceeds 5% (strictly) in three or more of the past five calendar years; otherwise **Item E not required**. Ratios are not rounded before the test. Explain the main drivers of adverse or favorable development; a release is described for its support, not its earnings effect.

## 10. Filing calendar check

For the statutory year-end in question, list each window in `references/statutory-and-gaap-rules.md` Section 10 that is open on the analysis date, with its trigger, its date and weekday, and whether a state rule may move it; say "not triggered" for windows whose trigger has not occurred.

## 11. Reconciliation checks

| # | Check | Test | Result (Pass / Fail / Not run) | Difference |
|---|---|---|---|---|
| R1 | Latest diagonal ties | By year and line, under the form's own line definitions: analysis paid = Schedule P Part 3; analysis reported (paid plus case) = Part 2 minus Part 4, a derived line because Part 2 includes bulk and IBNR; latest-year unpaid = Part 1 (or ledger for GAAP-only) | | |
| R2 | Unpaid identity | Ultimate - paid = case + IBNR, by year | | |
| R3 | Triangle arithmetic | Incremental sums to cumulative; link ratios recompute | | |
| R4 | CDF build | Product of selected factors x tail = CDF at each age | | |
| R5 | B-F and Cape Cod | Expected claims x (1 - 1/CDF) recomputed for one year; Cape Cod ELR = reported / used-up premium | | |
| R6 | Gross - ceded = net | By line and treaty | | |
| R7 | Salvage and subrogation | Counted once, on the stated data basis | | |
| R8 | LAE split | DCC + AO = total LAE; Schedule P DCC columns tie | | |
| R9 | Carried ties | Carried amounts = Annual Statement (Exhibit A items 1 to 4) or ledger | | |
| R10 | Range contains point | Low <= point <= high | | |

## 12. Issues, conflicts and judgment calls

| # | Severity | Issue | Sources in conflict (locators) | Controlling source and why | Effect on unpaid (gross and net) | Recommendation | Owner |
|---|---|---|---|---|---|---|---|

Severity: Critical (a check fails, or the carried position label changes under the alternative); High (unpaid moves by more than the materiality standard the user gave, or 5% of net unpaid if none was given); Medium (a conflict with a clear controlling source); Low (presentation).

## 13. Declined parts

When a hard stop declines part of a request, open that part with this fixed label, using the hard stop's name exactly as Checkpoint A gives it:

"Declined - [hard stop name]: [the part requested]. Needed to proceed: [what would allow it, or 'nothing; this part will not be produced']."

Hard stop names: No loss data; Target-driven selection; Opinion or sign-off; Out-of-scope reserves; Filed figures set aside. For example, "Declined - Target-driven selection: setting AY2024-2025 IBNR at $30.0m to reach a 97% combined ratio. Needed to proceed: nothing; this part will not be produced." Complete the rest of the deliverable. A declined part is never replaced by a figure produced another way.

## 14. Hand-offs

A hand-off names the facts the receiving workflow needs; a bare skill name is not a hand-off.

| To | Why | Facts passed (figures, dates, locators) | Open questions | What this analysis did not do |
|---|---|---|---|---|
| Appointed Actuary or other credentialed actuary | Opinion type, materiality, risk of material adverse deviation, signature | | | |
| analyzing-earnings-quality | The earnings-management question only, under its "earnings manipulation screen", "reserve releases" and "one-time gains in operating income" wording; loss reserve adequacy stays in this analysis | | | |
| managing-reinsurance-programs | Reinsurer credit and counterparty evaluation | | | |
| managing-insurance-regulatory-filings | Schedule P, Schedule F and annual statement schedule preparation | | | |

Add or remove rows to match the matter.

## 15. Open items and [VERIFY] list

| # | Open item | Gap class | Depends on | Owner | Next action | Changes which output |
|---|---|---|---|---|---|---|

Then each [VERIFY] statement and what would settle it.

Close with: "Draft for review by a credentialed actuary. Not a Statement of Actuarial Opinion, not an Actuarial Opinion Summary and not legal, accounting or investment advice."
