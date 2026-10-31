# Output Template: Draft Credit Memo and Underwriting Package

Produce the header and the sections below, in this order. Numbers go in tables; prose stays short. Every figure carries a source locator (document, page, schedule, line) or [UNVERIFIED]. State currency and units once in the header.

## Contents

1. Header and source-review register
2. Section 1. Request and draft recommendation
3. Section 2. Parties, ownership and insider screen
4. Section 3. Financial spread and tie-out
5. Section 4. Policy tests
6. Section 5. Cash flow and coverage
7. Section 6. Structure, covenants and headroom
8. Section 7. Collateral and LTV
9. Section 8. Regulatory overlays
10. Section 9. Proposed risk rating
11. Section 10. Reconciliation checks
12. Section 11. Issues, conflicts and exceptions
13. Section 12. Declined requests
14. Section 13. Hand-offs
15. Section 14. Open items and [VERIFY] list

## Header

- Borrower, request, lender name and type (national bank or federal savings association, state member bank, state nonmember bank, nonbank lender), total assets band if Regulation B Appendix A depends on it, date prepared, and "Draft for credit officer review. Not a credit approval or commitment."
- Source-review register:

| File | Type | Period or date | Quality or rank | Status | Pages or schedules read | Note |
|---|---|---|---|---|---|---|
| | audited, reviewed, compiled FS; tax return; PFS; appraisal; evaluation; credit policy excerpt; term sheet; email | | | Reviewed / Unreadable after attempt / Still needed | | |

## 1. Request and draft recommendation

Amount, purpose, product, rate, amortization, maturity, collateral, guarantors. Then one draft recommendation label for the credit officer, chosen by these tests, applied in order:

| Label | Test that must be true |
|---|---|
| Not produced - hard stop | A Checkpoint A hard stop that blocks the whole deliverable fired (no figures for the borrower's most recent fiscal year). Only the document request list is produced. |
| Not ready for decision | An open item (unknown fact, source conflict or unverified external lookup) changes a policy test result or a regulatory requirement, for example no value of record for real estate collateral or an insider screen not run. |
| Recommend decline | At least one policy test is "Fails", or a regulatory requirement cannot be met, and no alternative structure within the stated purpose meets every policy test. |
| Recommend restructure | At least one policy test is "Fails" at the requested structure, and a specified alternative (amount, amortization within useful life, collateral, guarantor, equity) meets every policy test. Name the alternative and its figures. |
| Recommend approval with conditions | Every policy test is "Meets" or "Exception - documented", and conditions precedent or regulatory steps (for example board prior approval) remain. |
| Recommend approval as proposed | Every policy test is "Meets", there are no exceptions, no conditions beyond standard documentation, and no open items. |

The label is a draft recommendation; the credit officer or committee decides.

## 2. Parties, ownership and insider screen

| Party | Role (borrower, co-borrower, guarantor, owner of 10 percent or more, affiliate in global cash flow) | Ownership | Insider screen result and date | Included in global cash flow? Why |
|---|---|---|---|---|

Insider screen results: "Not an insider", "Insider - [executive officer, director, principal shareholder or related interest of ...]", or "Not screened" (an unverified external lookup).

## 3. Financial spread and tie-out

Columns by fiscal year and interim period with statement quality. Rows: revenue, gross profit, operating expenses (with recurring items visible by year), EBITDA (reported, lender-adjusted, borrower-adjusted), interest, taxes, net income, capex (maintenance and growth, financed and unfinanced), distributions, total debt, tangible net worth, working capital. One row per normalization adjustment with source and reason.

## 4. Policy tests

| Test | Policy citation | Required | Actual | Result | Note |
|---|---|---|---|---|---|

Result labels:
- **Meets**: the actual figure, computed on the policy's own definition from sourced figures, satisfies the required level.
- **Exception - documented**: the actual figure does not satisfy the level, the policy permits an exception, and the draft states its size, mitigants and the approval authority the policy names. The skill documents; it does not grant.
- **Fails**: the actual figure does not satisfy the level and no permitted exception is documented.
- **Not tested - policy not supplied**: the institution's level for this test was not provided (a policy election to settle).

## 5. Cash flow and coverage

- CADS build per `references/underwriting-rules.md` Section 2, each line sourced; EBITDA-only DSCR shown only as a labelled secondary figure.
- Debt service table: each debt, amount, rate, amortization, monthly and annual payment.
- Global cash flow: entities and persons included and excluded, global cash available, global debt service, global DSCR.
- Sensitivities and break-even.

## 6. Structure, covenants and headroom

Amortization against remaining economic life of the collateral; maturity and refinance test; maximum loan amount at the policy DSCR. Covenant table:

| Covenant | Definition | Level | Actual | Projected (by year) | Headroom (formula from underwriting-rules Section 6) | First test date |
|---|---|---|---|---|---|---|

A covenant failed on actual figures is labelled "Day-one default", not headroom.

## 7. Collateral and LTV

| Collateral | Valuation source and date | Engaged by | Reviewed by and date | Value label | Value | Advance rate (policy) | Lendable value | LTV |
|---|---|---|---|---|---|---|---|---|

Value labels: **Value of record** (an appraisal or evaluation the regulation permits the lender to use, engaged by the lender or accepted under 34.45(b)(2) or its equivalents, reviewed before the decision, within the institution's validity criteria) and **Indicative - not value of record** (anything else, including borrower-ordered or borrower-provided appraisals, unreviewed reports and broker opinions). LTV is shown on both cost and value for purchases and tested on the lesser. Perfection items are listed as conditions precedent.

## 8. Regulatory overlays

| Overlay | Applies? Why | Finding label | Required action and owner | Rule |
|---|---|---|---|---|
| Appraisal or evaluation | | | | |
| CRE concentration (institution level, pro forma) | | | | |
| Regulation O | | | | |
| Regulation B notice and signatures | | | | |
| Section 1071 | | | | |
| SBA SOP (if SBA) | | | | |

Finding labels:
- **Compliant**: the facts show each requirement of the rule is met.
- **Noncompliant - remediate**: a requirement that applied on the facts was not met (for example a notice sent after its deadline, a missing board approval). State the remediation and that compliance staff must review it.
- **Not yet applicable**: the rule's compliance date or trigger has not occurred on the memo date.
- **Open - needs counsel**: the result turns on a legal reading, a [VERIFY] item or a fact the skill cannot settle.

## 9. Proposed risk rating

Proposed borrower and facility ratings on the institution's scale with the definition each driver meets, or "Not rated - scale not supplied".

## 10. Reconciliation checks

| # | Check | Test | Result (Pass / Fail / Not run) |
|---|---|---|---|
| C1 | Spread ties to source | Each spread total equals the source statement total | |
| C2 | Debt service recomputed | Payment recomputed from amount, rate, amortization and frequency | |
| C3 | DSCR arithmetic | CADS / debt service recomputed; CADS lines sum | |
| C4 | Global population | Every guarantor and included affiliate has both cash flow and debt service rows; distributions not double counted | |
| C5 | LTV basis | LTV uses the lesser of cost and value of record | |
| C6 | Amortization within useful life | Amortization not longer than remaining economic life or policy maximum | |
| C7 | Covenant on actual | Each covenant tested on actual figures before projections | |
| C8 | Insider aggregation | Insider credit aggregated with all credit to the person and related interests | |
| C9 | Notice clock | Each Regulation B clock computed from its own trigger | |

## 11. Issues, conflicts and exceptions

| # | Severity | Issue | Sources in conflict | Controlling source and why | Effect on a policy test or regulatory finding | Recommendation | Owner |
|---|---|---|---|---|---|---|---|

Severity: Critical (a policy test or regulatory finding changes); High (a figure moves materially but the result does not change); Medium (a conflict with a clear controlling source); Low (clean-up).

## 12. Declined requests

When a hard stop or ground rule blocks part of a request, the rest of the deliverable is still drafted and the blocked part is recorded with the label **Declined in part**:

| Label | Request (as received) | What was declined | Ground rule or hard stop | What the draft does instead |
|---|---|---|---|---|
| Declined in part | | | | |

## 13. Hand-offs

A hand-off names the facts the receiving workflow needs; a bare skill name is not a hand-off.

| To | Why | Facts passed | Open questions | What this draft did not do |
|---|---|---|---|---|
| managing-debt-covenant-compliance | Post-close covenant calculations and compliance certificates | Covenant definitions, levels, first test dates | | |
| analyzing-earnings-quality | Addbacks or normalization not supported by the statements | | | |
| legal-research | Regulation O, Regulation B or Section 1071 questions needing a legal reading (no dedicated skill exists) | | | |

Add or remove rows to match the matter.

## 14. Open items and [VERIFY] list

| # | Open item | Gap class | Owner | Next action | Changes which test or finding |
|---|---|---|---|---|---|

Gap classes: unknown fact, source conflict, unverified external lookup, policy election.

Close with: "Draft for credit officer review. Not a credit approval, commitment or legal advice."
