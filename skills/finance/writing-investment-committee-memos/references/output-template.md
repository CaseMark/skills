# Output Template

Produce the header and the sections below, in this order. Use the firm's own IC template when the user supplies one, and map every section here into it; a section the firm template lacks goes in an annex rather than being dropped. Put numbers in tables and keep prose short. Every figure carries a source locator (document, page or tab and cell, version and date), a register ID, or [UNVERIFIED]. State the currency and units once in the header.

## Contents

1. Header and source-review register
2. Section 1. Executive summary and proposed recommendation
3. Section 2. Company, market and deal overview
4. Section 3. Investment thesis and KPIs
5. Section 4. Cases, returns and value-creation bridge
6. Section 5. Valuation and comparables
7. Section 6. Financing
8. Section 7. Risk matrix
9. Section 8. Diligence status and findings
10. Section 9. Conflicts, fees and fund constraints
11. Section 10. Information handling and distribution
12. Section 11. Approval requested and conditions
13. Section 12. Reconciliation checks
14. Section 13. Issues log and declined requests
15. Section 14. Hand-offs
16. Section 15. Open items and [VERIFY] list

## Header and source-review register

- Deal name, investing fund or funds and amounts, strategy (buyout, growth, credit, real estate), memo stage (screening, final IC, follow-on, add-on), IC meeting date, date prepared.
- First line, verbatim: "DRAFT for deal team and investment committee review. The committee makes the investment decision."
- Model file name, version and date that every figure ties to; currency and units.
- Distribution status: "Internal: deal team and IC only" or "External distribution requested: compliance review required before release" (Section 10).

| File | Type | Version or date | Rank | Status | Sections, pages or tabs read | Note |
|---|---|---|---|---|---|---|
| name as received | model, commitment letter, fee letter, term sheet, QoE, legal DD, commercial DD, environmental, insurance, tax, LPA, side letter, allocation policy, IC charter, CIM, prior memo, email | | 1-4 | Reviewed / Not relevant / Unreadable after attempt / Still needed | | |

## 1. Executive summary and proposed recommendation

Proposed recommendation, using one label verbatim: **Proposed: approve**, **Proposed: approve subject to conditions**, **Proposed: decline**, or **Proposed: defer pending diligence**. Follow with the deal team's three-sentence thesis, the headline terms (price, multiple and the EBITDA it applies to, equity check, ownership, leverage at close on credit agreement EBITDA), sponsor-case and downside returns (dated IRR and MOIC, gross or net stated), the top three risks, any diligence item not at **Complete**, and any conflict requiring consent. Every figure equals the body figure (check M13).

## 2. Company, market and deal overview

Business description, end markets, history, process (auction, bilateral, intermediary), exclusivity, timetable. Facts only, each sourced.

## 3. Investment thesis and KPIs

| # | Thesis pillar | KPI | Baseline (date, source) | Target in sponsor case (date) | Disconfirming result and trigger | Value in bridge ($) | Owner |
|---|---|---|---|---|---|---|---|

A pillar without a measurable KPI, a baseline and a disconfirming result is listed in Section 13 as an issue, not presented as thesis.

## 4. Cases, returns and value-creation bridge

| Case | Source (model tab, version) | Revenue CAGR | Exit EBITDA | Exit multiple (rationale) | Net debt at exit | Equity value | MOIC | IRR (dated) | Gross or net | Minimum liquidity and covenant headroom |
|---|---|---|---|---|---|---|---|---|---|---|
| Management case | | | | | | | | | | |
| Sponsor case (base) | | | | | | | | | | |
| Downside case | | | | | | | | | | |
| Exit at entry multiple | | | | | | | | | | |

Then the dated sponsor cash flow schedule (date, event, contribution, distribution, source), the holding period in years, and the value-creation bridge: EBITDA growth at the entry multiple, multiple change on exit EBITDA, net debt reduction and interim distributions, and a total that equals exit equity plus distributions less contributions (check M6). A case the model does not contain is shown as "Not modeled" with an open item, never filled in by hand.

## 5. Valuation and comparables

Selection criteria stated before the results; the full candidate set; each exclusion with its reason; median, mean, range and quartiles for the full set and for the selected set; the entry multiple's position in both; LTM or NTM basis and the dates of each comparable.

## 6. Financing

| Term | Memo assumption | Commitment papers (document, section) | Match? | Effect if different |
|---|---|---|---|---|

Rows: each tranche amount, price (OID), margin and floor, fees, amortization, maturity, covenants, flex, conditions and expiry. Commitment status: committed, highly confident, indicative or none.

## 7. Risk matrix

| # | Risk | Category | Probability (High / Medium / Low, with basis) | Impact (amount or effect on IRR and MOIC) | Mitigant (contractual, structural, operational) | Residual risk | Linked case or sensitivity | Owner | Source |
|---|---|---|---|---|---|---|---|---|---|

A mitigant names a mechanism (indemnity and cap, insurance and exclusions, price adjustment, covenant, plan with owner and date). "Monitor" alone is not a mitigant.

## 8. Diligence status and findings

| Workstream | Provider and report date | Status label | Material findings | Effect on price, structure or returns | Open items, owner and date |
|---|---|---|---|---|---|

Status labels, verbatim: **Complete: no material findings**; **Complete: findings reported**; **In progress**; **Not started**; **Not in scope** (with the reason). A workstream with a reported finding is never **Complete: no material findings**.

## 9. Conflicts, fees and fund constraints

Complete every row; write "Checked: none found" with the documents checked, never a bare "None".

| Conflict or constraint | Facts | Governing document and provision | Consent or approval needed (LPAC, investors, none) and status | Disclosure made or required |
|---|---|---|---|---|
| Allocation among funds, vehicles and accounts | | | | |
| Co-investment allocation and terms | | | | |
| Cross-fund or affiliated-fund holding in the company | | | | |
| Affiliated service providers and fees from the company | | | | |
| Transaction, monitoring and other fees; offsets | | | | |
| Personal interests of firm personnel | | | | |
| Fund limits (concentration, geography, leverage, investment period) | | | | |

## 10. Information handling and distribution

MNPI screen (public issuers touched by the deal, what was received, under which NDA, wall-crossing and restricted-list status, compliance contact). Distribution plan: internal only, or the external audience and the compliance review it needs (Marketing Rule and Rule 206(4)-8 points from `references/regulatory-and-disclosure.md`). An external version is a separate document marked "Draft for compliance review" and is not released by this skill.

## 11. Approval requested and conditions

The exact authority sought (for example, authority to submit a binding offer at up to a stated enterprise value with stated financing), conditions precedent (consents, open diligence, financing), and the decisions reserved to the committee.

## 12. Reconciliation checks

Every row is computed, not asserted. A Fail or Not tested row goes to Section 13.

| # | Check | Test | Result (Pass / Fail / Not tested) | Difference | Note |
|---|---|---|---|---|---|
| M1 | IRR ties to the model | Memo IRR = XIRR of the model's dated sponsor cash flows, within 0.1 percentage point | | | |
| M2 | MOIC ties | Memo MOIC = total distributions / total contributions, including add-on equity and recaps | | | |
| M3 | Sources and uses | Memo sources and uses equal the model and the funds flow; sources minus uses = 0 | | | |
| M4 | Leverage at close | Debt / credit agreement EBITDA equals the commitment papers' sizing | | | |
| M5 | Financing terms | Every financing row in Section 6 matches the commitment papers | | | |
| M6 | Value bridge | EBITDA growth + multiple change + net debt reduction + interim distributions = equity gain | | | |
| M7 | Cases exist | Every case in Section 4 is in the stated model version | | | |
| M8 | Exit multiple | Exit multiple at or below entry, or a documented rationale plus an exit-at-entry row | | | |
| M9 | Comparables statistics | Recomputed from the full set; exclusions listed | | | |
| M10 | Risk matrix complete | Every risk has probability, impact, mitigant, residual risk and owner | | | |
| M11 | Diligence labels | Every workstream has a status label consistent with its report | | | |
| M12 | Conflicts table | Every row completed with documents checked | | | |
| M13 | Summary equals body | Every executive-summary figure equals the body figure | | | |

## 13. Issues log and declined requests

| # | Severity | Issue | Sources in conflict (locators) | Controlling source and why | Effect on returns, price or approval | Recommendation | Owner |
|---|---|---|---|---|---|---|---|

Severity: Critical (a returns figure, leverage figure, known material risk, diligence finding or conflict is wrong or missing); High (a case, comparable set or financing term changes the price or approval conditions); Medium (presentation, or a conflict with a clear controlling source); Low (clean-up).

**Declined requests.** When a hard stop or ground rule blocks part of a request, the rest of the memo is still drafted, and the blocked part is recorded here with the label **Declined in part**:

| Label | Request (as received) | What was declined | Ground rule or hard stop | What the memo does instead |
|---|---|---|---|---|
| Declined in part | | | | |

## 14. Hand-offs

A hand-off names the facts the receiving workflow needs; a bare skill name is not a hand-off.

| To | Why | Facts passed (figures, dates, locators) | Open questions | What this memo did not do |
|---|---|---|---|---|
| building-lbo-models | Missing case, rerun at a different exit multiple or financing, dated cash flow schedule | | | |
| building-equity-valuation-models | DCF or comparables rebuild behind the valuation section | | | |
| analyzing-earnings-quality | Addbacks, accruals or QoE adjustments the memo relies on | | | |
| managing-advertising-compliance | Any memo content leaving the deal team and IC for investors | | | |
| managing-co-investment-processes | Co-investment allocation and terms | | | |

Add or remove rows to match the matter.

## 15. Open items and [VERIFY] list

| # | Open item | Gap class | Depends on | Owner | Next action | Changes which section |
|---|---|---|---|---|---|---|

Gap classes: unknown fact, source conflict, unverified external lookup, policy election.

Close with: "Draft for deal team and investment committee review. The committee makes the investment decision. Not investment, legal, tax or accounting advice."
