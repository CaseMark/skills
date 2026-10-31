---
name: building-equity-valuation-models
language: en
description: >
  Builds and reviews equity valuation models: DCF on unlevered free cash flow at WACC
  with relevered beta; Gordon growth and exit multiple terminal values with implied
  multiple and growth checks; mid-year convention, stub periods; trading comparables
  (LTM, NTM) and precedent transactions with control premium or discount for lack of
  control; the enterprise value to equity value bridge (debt, ASC 842 leases,
  preferred, noncontrolling interests, pensions, trapped cash); diluted shares
  (treasury stock method, convertibles); stock-based compensation; football field,
  sensitivities. States the standard of value (ASC 820 fair value, fair market value,
  investment value, statutory fair value). Use for DCF, comps, precedents, price
  targets, value per share, WACC, terminal value, net debt bridge, fair market value of
  closely held interests with DLOC and DLOM, DCF and comparables used to support the
  exit multiple in an LBO, or valuation model outputs behind an investment committee
  memo. Drafts for qualified review.
tags:
  - modeling
  - equity-research
  - valuation
metadata:
  author: casemark
  practice_areas:
    - Equity Research
    - Investment Management
  document_types:
    - Model
  skill_modes:
    - Modeling
---

# Building Equity Valuation Models

Builds, or reviews, a valuation of a company's equity: a DCF, trading comparables, precedent transactions, the bridge from enterprise value to equity value and value per share, sensitivities, and a reconciliation table that proves the model ties. The deliverable follows `references/output-template.md`, states the standard of value and the interest valued, and ends with ranked issues, hand-offs and open items. Everything it produces is a draft for review by a qualified valuation professional; it is not a conclusion of value under VS Section 100, an IVS-compliant report, a fairness opinion, or investment, tax, accounting or legal advice.

## Why This Skill Exists

A valuation model fails on consistency more often than on arithmetic. The discount rate must match the cash flow it discounts, the beta must match the capital structure in the weights, the terminal value must match the multiples and the economy it claims to grow with, the net debt must match what the cash flows leave out, and the share count must match the price it produces. Each mismatch moves value by double digits while every formula still calculates. Underneath sits a question models skip: value to whom, for what interest, under which standard. Fair value for financial reporting, fair market value for tax and investment value for a buyer give different answers for the same company, and a control premium that belongs in one is an error in another. This skill states those choices, ties every input to a document, and proves the model reconciles before anyone reads the per-share number.

## Where Mistakes Hide

Read each input with this suspicion before building from it.

| Input / Document | What It Is Used For | Where the Error Hides |
|---|---|---|
| Engagement letter, purpose and the subject interest (purchase agreement, buy-sell agreement, accounting Topic, statute) | Standard of value, premise, level of value, which entity and which class of shares | No standard of value stated, or ASC 820 fair value confused with statutory fair value; buyer-specific synergies inside a fair market value; a 100 percent value presented for a minority stake; the parent's shares valued when the interest is in a subsidiary |
| Management forecast and the unlevered free cash flow build | Explicit-period cash flows | Unlevered flows discounted at the cost of equity, or levered flows at WACC; taxes computed after interest; SBC added back as non-cash while future grants are ignored in the share count; a most-likely case treated as an expected case |
| Discount rate inputs (peer betas, capital structure, cost of debt, risk-free rate, equity risk premium) | WACC and cost of equity | Peer levered betas used without unlevering and relevering to the subject's capital structure; book weights; the historical coupon used as the cost of debt; risk-free rate or premium filled in from memory or undated; cash flows in one currency or in real terms discounted at a rate built in another currency or in nominal terms |
| Terminal value assumptions | Usually most of enterprise value | Perpetual growth above the long-run nominal growth of the economy the cash flows come from; terminal value over about 75 to 80 percent of EV with no explanation; Gordon growth and exit multiple values implying inconsistent multiples or growth; terminal year with capex below D&A at positive growth |
| Valuation date and discounting calendar | Discount factors | Mid-year factors of 0.5, 1.5, 2.5 used with a stub period; a full first fiscal year counted when part of it precedes the valuation date; net debt taken at a different date from the valuation date |
| Balance sheet and notes for the EV-to-equity bridge | Net debt and other claims | Finance lease liabilities, preferred stock, noncontrolling interests or pension deficits omitted; operating lease liabilities deducted while UFCF is already after lease cost (or not deducted on an IFRS 16 or EBITDAR basis); cash trapped by exchange controls or needed for operations counted as free; equity-method investments omitted or double counted |
| Share register, equity plans and convertible terms | Fully diluted shares and per-share value | Basic shares used; options added at gross count rather than by the treasury stock method; out-of-the-money options included; an in-the-money convertible left as debt or an out-of-the-money one converted; TSM priced at a figure inconsistent with the value concluded |
| Trading comparables (data-provider pulls, peer filings) | Market approach multiples | Peers with different growth or margin profiles used unadjusted; NTM multiples applied to LTM metrics; unaligned fiscal year ends; peer EV built on a different lease or bridge basis than the subject |
| Precedent transactions | Control-basis multiples | Control premium and synergies applied to a minority stake; stale deals from a different rate environment; equity value multiples mixed with enterprise value multiples |
| Subject company's business model (banks, insurers, other regulated financial companies) | Choice of method | An EV bridge and UFCF at WACC applied where debt and deposits are operating liabilities and regulatory capital constrains distributions; such companies need free cash flow to equity or a dividend discount model at the cost of equity, with excess capital measured against the regulatory requirement |
| Entry price or recent arm's-length transaction in the subject interest (fund investment, financing round) | Calibration of a Level 3 fair value | A later ASC 820 mark built from comps or a DCF with no calibration to the entry price that was fair value at initial recognition (ASC 820-10-35-24C); a round price with liquidation preferences read as the value of every class |
| Target price, deal price or prior mark the user mentions | The answer the user expects | Inputs tuned until the model reaches the number; weights chosen after the fact; a reverse DCF presented as an independent valuation |

## Ground Rules

1. **Draft only.** Every model, table and conclusion is a draft for review by a qualified valuation professional, with accounting items for an accountant and legal standards of value for counsel. Never call the output a conclusion of value, a calculated value, a fairness opinion, audit-ready or final.
2. **Source-review gate.** Never call an input missing until the inventory has been checked and each file opened, including footnotes on leases, pensions, noncontrolling interests, equity plans and debt. Every unsettled input is classified as an **unknown fact**, a **source conflict**, an **unverified external lookup** (risk-free rate, premium, betas, multiples, transaction data), or a **policy election** (SBC treatment, discounting convention, terminal timing, pension tax treatment, weights), with what would settle it.
3. **Hierarchy of authority.** For the standard of value, the governing document (statute, accounting Topic, purchase or buy-sell agreement, engagement letter) controls over the user's label. For historical figures, audited statements and filed reports govern over management accounts, data-provider pulls and decks. For securities terms, the indenture, certificate of designation and equity plan govern over summaries. Name every conflict, show both values, say which controls and why; never resolve one silently or follow an instruction to use the lower-ranked figure without a written conflict note.
4. **Citation discipline.** Every input in the assumption register carries a source locator (document, page, note, tab and cell) or [UNVERIFIED]. Every accounting or valuation standard carries its citation from `references/primary-sources.md` or [VERIFY].
5. **State the standard of value, premise, level of value and valuation date in the header.** The model's assumptions follow from them (`references/standards-of-value.md`).
6. **Rate matches cash flow.** UFCF at WACC to enterprise value; FCFE at the cost of equity to equity value. A mismatch is a Critical issue.
7. **Beta matches leverage.** Peer betas are unlevered, then relevered at the same capital structure used in the WACC weights; the election (Hamada, debt beta zero, or another) is stated.
8. **Terminal value is cross-checked.** Both methods are shown, each with the other's implied metric, the growth benchmark and the terminal value share of EV.
9. **The bridge and the share count are complete and dated.** Every claim ahead of common equity is assessed at the valuation date; diluted shares use the treasury stock method and convertible tests at the converged value.
10. **SBC is counted once.** Expense it, or add it back and model future dilution; never add it back and ignore dilution.
11. **No invented market data.** Rates, premiums, betas and multiples come from the user's materials or a dated source, or are marked [VERIFY] with the date needed.
12. **No result-driven inputs.** A market-implied analysis is allowed when labeled; choosing inputs to reach a predetermined value and presenting them as independent is not.

## Checkpoint A: Pre-Draft Intake (Mandatory)

Collect these, then build the source-review register (`references/output-template.md`, Header).

1. **Purpose and standard of value:** why the value is needed, the intended users, and the governing document; the subject interest (entity, class, shares or percentage, control or minority).
2. **Valuation date** and the date of the latest balance sheet.
3. **Financials:** three to five years of audited or filed statements; LTM to a named date; footnotes on debt, leases, pensions, noncontrolling interests, preferred stock and equity plans.
4. **Forecast:** management or analyst case with its author and date; whether SBC is included in operating expenses.
5. **Capital structure and securities:** debt schedule, cash by jurisdiction, basic shares, options and warrants (count and strike), RSUs and PSUs, convertible terms.
6. **Market inputs:** risk-free rate, equity risk premium, peer betas and capital structures, peer multiples and transaction data, each with source and date.
7. **Deliverable:** new model, review of a supplied model, or a quick range.

**Default fallbacks (each stated in the assumption register as a policy election or unknown fact):** standard of value defaults to investment value to the user on a going-concern basis only when the purpose is internal analysis (never for reporting, tax, appraisal, litigation or fairness purposes); end-of-period discounting unless the user elects mid-year; SBC expensed; pension deficit after tax at the marginal rate; NCI at estimated value, book as a labeled fallback; TSM at the implied value per share, iterated; Hamada relevering with debt beta zero; US federal tax at 21 percent under IRC 11(b) with state and foreign taxes [VERIFY].

**Hard stops (report what is needed instead):**
- The purpose is financial reporting, tax, appraisal or other litigation, or a fairness opinion, and the standard of value or the valuation date cannot be identified from the request or the documents: do not produce a value.
- Neither historical financial statements nor a forecast exist for the subject: do not produce a value.
- The request is to present the output as a signed valuation report, a conclusion of value or calculated value under VS Section 100, an IVS-compliant report, a fairness opinion, or audited fair value: decline that presentation, label it "Not produced (hard stop)" under the template, and deliver the labeled draft.
- The request is to choose or adjust inputs to reach a predetermined value or price while presenting them as independent estimates: decline that part, label it "Not produced (hard stop)", and offer a labeled market-implied analysis.
- Per-share value is requested but no share count or list of dilutive securities is available: decline the per-share part, produce enterprise and equity value as far as the inputs allow, and label the per-share line "Not produced (hard stop)" with the template's wording.

## Step 1: Scope, Standard of Value and Inventory

Read `references/standards-of-value.md` in full. Fix the standard of value, premise, level of value, subject interest and valuation date, and record any conflict between the user's label and the governing document. If the subject is a bank, insurer or other regulated financial company, plan an equity-basis method (FCFE or dividend discount) per `references/valuation-mechanics.md` Section 1 instead of an EV bridge. Build the source-review register and assumption register. For a supplied model, trace each input cell to a source and list hard-coded values in calculated rows.

## Step 2: Forecast and Unlevered Free Cash Flow

Read `references/valuation-mechanics.md` Sections 1 and 2. Rebuild UFCF from EBIT with operating taxes, D&A, capex and working capital; tie the base year to the statements (V1). Decide the cash flow type and the matching rate (V2). Find SBC in the forecast, state the treatment, and if it is added back, either model future dilution or compute the value with it expensed and report the difference (V10).

## Step 3: Discount Rate

Read `references/valuation-mechanics.md` Section 3. Unlever each peer beta, take the median, relever at the subject's capital structure, and use the same structure for the weights (V3). Use the current pre-tax cost of debt and the marginal tax rate. Every market input carries its source and date or [VERIFY].

## Step 4: DCF and Terminal Value

Read `references/valuation-mechanics.md` Sections 4 and 5. Set the calendar from the valuation date, with a stub period where needed, and state the convention (V4). Compute terminal value by Gordon growth and by exit multiple; show the implied exit multiple, the implied growth, the long-run nominal growth benchmark with its source, and the terminal value share of EV (V5, V6). Explain any share above about 75 to 80 percent.

## Step 5: Trading Comparables and Precedent Transactions

Read `references/valuation-mechanics.md` Sections 8 and 9 and `references/standards-of-value.md` Section 5. Document peer selection with growth and margins; match LTM to LTM and NTM to NTM and calendarize (V11). For precedents, record the stake acquired and premium; adjust or exclude control-basis indications for a minority interest so the level of value matches the subject interest (V12). For an ASC 820 Level 3 mark of an interest bought at a price that was fair value, calibrate to that entry price (`references/standards-of-value.md` Section 4) or list the entry price and model as an unknown fact.

## Step 6: Enterprise Value to Equity Value Bridge

Read `references/valuation-mechanics.md` Section 6. Assess every listed item at the valuation date, including items set to zero with a reason; match the lease treatment to the EBITDA and UFCF basis (V7, V8). Exclude trapped or operating cash with the source that shows the restriction.

## Step 7: Fully Diluted Shares and Per-Share Value

Read `references/valuation-mechanics.md` Section 7. Start from basic shares, apply the treasury stock method to in-the-money options and warrants, count RSUs, test each convertible, and iterate the per-share value to convergence (V9). If share data are missing, use the label "Not produced (hard stop)" from the template.

## Step 8: Weighting, Football Field and Sensitivities

Read `references/valuation-mechanics.md` Section 10. Present each method's range, the weights and their reasons, and the two-way tables with a centre cell equal to the base case (V13). Label any market-implied analysis as such.

## Step 9: Reconcile, Rank Issues and Hand Off

Complete the reconciliation table in `references/output-template.md` Section 11; every Fail or Not built row becomes an issue. Rank issues by the template's severity rule with the effect on value, write complete hand-offs (Section 13), and list open items and every [VERIFY] statement (Section 14).

## Checkpoint B: Post-Draft Alignment

Before the Quality Audit, re-read the request and confirm:
- The value answers the question asked, for the interest and the standard of value in the header, at the valuation date.
- The deliverable type matches the request (new model, review, quick range) and scope limits are stated.
- Every conflict between the user's instructions and a higher-ranked document is written up, not followed silently.
- No statement presents the draft as a conclusion of value, fairness opinion or recommendation to buy or sell; the closing line from the template is present.

## Quality Audit

Confirm each statement is true of the draft; fix the draft if one is not.

1. The header states the standard of value, premise, level of value, subject interest and valuation date, and the assumptions follow them.
2. UFCF is discounted at WACC (or FCFE at the cost of equity), and operating taxes are on EBIT.
3. Peer betas are unlevered and relevered at the capital structure used in the WACC weights; weights sum to 100 percent.
4. Every market input has a source and date or [VERIFY]; none came from memory.
5. Discount factors match the valuation date, any stub period and the stated convention.
6. Terminal value appears by both methods with the implied multiple, the implied growth, the growth benchmark and the TV share of EV, and a share above about 75 to 80 percent is explained.
7. The bridge assesses debt, finance and operating leases (on the matching basis), preferred, NCI, pensions, cash restrictions and non-operating assets at the valuation date.
8. Diluted shares apply the treasury stock method and the convertible test at the converged value.
9. SBC is either expensed or added back with future dilution modeled, and the treatment is stated.
10. Comparable multiples match period (LTM or NTM) and basis (EV or equity) to the subject metric, and peer differences in growth and margin are addressed.
11. Premiums and discounts match the subject interest; no control-basis indication is applied unadjusted to a minority interest; a Level 3 fair value is calibrated to any entry price that was fair value, or the gap is an open item.
12. Every reconciliation check is computed; every conflict names both sources, the controlling one and the effect; every open item has an owner.
13. The draft-for-review closing line is present and nothing calls the output a conclusion of value or final.

## Guidelines

- Work in the units of the source documents and state them once; never mix thousands and millions.
- Prefer the structure of a model the user supplies; flag defects rather than rebuilding unasked, and show the value effect of each fix separately.
- Quote ranges for anything driven by a policy election; give the base case and the alternative.
- Keep inputs on one assumption sheet and formulas elsewhere; a pasted value in a calculated row is a defect to report.
- Present the downside with the same care as the base case.
- Do not recommend buying, selling, bidding or a rating; present value, ranges, risks and sensitivities for the decision-maker.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Per-share value moves when recalculated | TSM price not iterated, or circular reference switched off | Iterate the price and share count to convergence and report the last change |
| EV far above comps | Terminal growth too high, rate mismatch, or SBC added back | Run V2, V5 and V10 first |
| DCF and comps disagree on the subject's own EBITDA basis | Lease basis differs (US GAAP versus IFRS 16 peers) | Restate all to one basis per `references/valuation-mechanics.md` Section 6 |
| Filings are scans or footnotes unreadable | Image PDFs | Attempt extraction; if still unreadable, record it, use the best lower-ranked source with [UNVERIFIED], and list the dependent outputs |
| Supplied model and filing disagree on debt or shares | Model built on an older quarter | Use the filing at the valuation date; write up the conflict and the effect |
| User's label conflicts with the governing document's standard of value | Informal language ("fair value" meaning fair market value) | Follow the governing document; record a source conflict |
| Peer data undated or from an unknown provider | Pasted pull | Mark [VERIFY] with the date needed; do not rely on it for the concluded range |

## Related Skills

- building-lbo-models: LBO models, sponsor returns (IRR, MOIC), debt capacity and cash sweep; this skill supplies the DCF and comparables used to support the exit multiple.
- conducting-cost-of-capital-analysis: a stand-alone WACC study (equity risk premium, beta estimation, debt cost measurement).
- analyzing-comparable-transactions: building the precedent transaction set and computing deal premiums in depth.
- modeling-sum-of-parts-valuations: conglomerates or multi-segment companies valued segment by segment.
- building-merger-models: accretion and dilution for a strategic acquirer.
- analyzing-fairness-opinions: reviewing a banker's fairness opinion and its valuation analyses.
- managing-fair-value-measurement: ASC 820 hierarchy classification and valuation technique documentation for a reported fair value.
- managing-impairment-testing: goodwill and long-lived asset impairment tests using these values.
- managing-business-combinations: purchase price allocation after an acquisition.
- managing-lease-accounting-asc842: measuring the lease liabilities used in the bridge.
- analyzing-convertible-bonds: convertible structure, equity sensitivity, credit floor and conversion premium beyond the conversion test.
- managing-equity-compensation-accounting: SBC accounting, award fair values (Black-Scholes) and expense recognition.
- managing-pension-fund-obligations: funded status and actuarial assumptions behind the pension deficit used in the bridge.
- analyzing-earnings-quality: accruals, cash conversion and accounting red flags in the earnings the model capitalizes.
- managing-estate-and-gift-tax: estate and gift tax planning and the transfer-tax treatment of a value; this skill models the fair market value of the closely held interest (entity DCF or comparables, DLOC and DLOM as modeled) that it relies on.
- writing-equity-research-notes: a research note with thesis, valuation, risks and rating justification built on this model.
- writing-investment-committee-memos: drafting or reviewing the IC memo that turns LBO or valuation model outputs into an IC recommendation; this skill builds the DCF, trading comparables and precedent transaction models behind the memo's valuation section.

## Reference Files

- `references/standards-of-value.md`: standards and premises of value, VS Section 100, IVS (effective January 31, 2025), ASC 820 fair value and hierarchy, premiums and discounts by subject interest.
- `references/valuation-mechanics.md`: cash flow and rate matching, UFCF and SBC, WACC relevering, discounting calendar, terminal value cross-checks, EV-to-equity bridge with ASC 842 leases, treasury stock method and convertibles, comparables, precedents, weighting.
- `references/output-template.md`: deliverable sections, partial-decline label, assumption register, reconciliation checks V1 to V13, issue severity, hand-off table.
- `references/primary-sources.md`: each authority checked with citation, method and date, and the [VERIFY] list.
