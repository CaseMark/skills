# Output Template

Produce the header and the sections below, in this order. Put figures in tables. Every fact carries a source locator (document, page, schedule, line or paragraph) or [UNVERIFIED]; every rule carries its citation and year from `primary-sources.md` or [VERIFY]. State the as-of date, the currency and the tax years once in the header.

## Contents

1. Header and source-review register
2. Section 1. Question, scope and result range
3. Section 2. People and transfers
4. Section 3. Exemption ledger
5. Section 4. Gift review
6. Section 5. GST review
7. Section 6. Gross estate, valuation and basis
8. Section 7. Clock table
9. Section 8. Tax computation and payment
10. Section 9. State layer
11. Section 10. Reconciliation checks
12. Section 11. Issues and judgment calls
13. Section 12. Declined and not prepared items
14. Section 13. Hand-offs
15. Section 14. Open items and [VERIFY] list
16. Label tests

## Header

- Client or matter, as-of date, tax years, "Draft for review by a qualified estate and gift tax adviser."
- Deliverable type: gift plan review, Form 709 reporting position, Form 706 issue list, portability review, estate tax projection, or review of a supplied memo or model.
- Source-review register, one row per file:

| File | Type | Date | Rank | Status | Pages or schedules read | Note |
|---|---|---|---|---|---|---|

Rank 1: executed instruments (wills, trusts, assignments, partnership and shareholder agreements), filed returns and IRS letters, death certificates. Rank 2: appraisals and valuation reports, account statements at the valuation date, insurance statements. Rank 3: inventories, ledgers, models and spreadsheets. Rank 4: emails, memos, summaries and commentary. Status: Reviewed / Not relevant / Unreadable after attempt / Still needed.

## 1. Question, scope and result range

The decision asked, the transfers or estate covered, what is routed elsewhere, and the result as a range or as conditional on named elections.

## 2. People and transfers

| Person | Role (donor, consenting spouse, decedent, predeceased spouse, executor, trustee, donee, skip person) | Citizenship and residence | Domicile state | Key date (gift, death, marriage) | Source |
|---|---|---|---|---|---|

Then one row per transfer: date completed (the date the transfer was actually made, from the executed document), transferor, transferee or trust, property, value and its source.

## 3. Exemption ledger

| Year | Gift or event | Gross amount | Annual exclusion | Marital or charitable deduction | Taxable gift | Cumulative taxable gifts | BEA for the year | DSUE (from whom) | Remaining exclusion | Citation |
|---|---|---|---|---|---|---|---|---|---|---|

Add the DSUE line: deceased spouse, date of death, last deceased spouse (Yes/No), BEA in the year of death, taxable estate plus adjusted taxable gifts, DSUE amount, portability status label.

## 4. Gift review

| Gift | Interest label | Withdrawal right and notice (locator) | Split-gift consent | Form 709 required (who) | Disclosure label | Missing disclosure items | Citation |
|---|---|---|---|---|---|---|---|

## 5. GST review

| Transfer | Skip type (direct skip, indirect skip, none) | GST trust under IRC 2632(c)(3)(B)? (exception relied on) | Automatic allocation? | Allocation or election needed, by whom, by when | Inclusion ratio status | Citation |
|---|---|---|---|---|---|---|

## 6. Gross estate, valuation and basis

| Asset | Owner or trust | Inclusion label and section | Date-of-death value (source) | Alternate value and date (source) | Valuation support | Basis label | Citation |
|---|---|---|---|---|---|---|---|

For an entity interest, show the entity's value with and without any item in dispute (for example life insurance proceeds after Connelly), the percentage held and the arithmetic. Valuation modeling is routed; this section records the value relied on, its support and its disclosure.

## 7. Clock table

As-of date stated. One row per triggered element from `deadlines-and-elections.md`.

| # | Element | Trigger event and date (locator) | Prescribed date and weekday | Rolled date under IRC 7503 (or "no roll") | Status label | Who acts | Citation |
|---|---|---|---|---|---|---|---|

## 8. Tax computation and payment

Steps in order: gross estate; deductions; taxable estate; adjusted taxable gifts; tentative tax base; tentative tax; gift tax payable; applicable exclusion (BEA + DSUE) and credit; net estate tax. Show each alternative (for example date-of-death and alternate valuation, or the appraisal's value and the corrected value). Then payment: due date, 6166 eligibility (35 percent test with the arithmetic) and acceleration risk, 6161 need.

## 9. State layer

Domicile state and any state where real or tangible property sits; each state's estate or inheritance tax as read for the year with its citation, or "not modeled" with [VERIFY].

## 10. Reconciliation checks

Each row computed, not asserted. A Fail goes to Section 11.

| # | Check | Test | Result (Pass / Fail / Not applicable) | Difference | Note |
|---|---|---|---|---|---|
| R1 | Year figures | Each gift uses the BEA and annual exclusion for its own year; each estate uses the BEA for the year of death | | | |
| R2 | Ledger ties | Cumulative taxable gifts equal the sum of prior Forms 709 plus current gifts | | | |
| R3 | Exclusion limit | Taxable gifts used do not exceed BEA plus available DSUE; any excess shows gift tax | | | |
| R4 | DSUE | DSUE comes only from the last deceased spouse with an election made or available, and does not exceed the BEA of that spouse's year of death | | | |
| R5 | Present interest | Every annual exclusion claimed for a trust gift has a withdrawal right in the instrument at the time of the transfer | | | |
| R6 | Split gifts | Splitting, if elected, covers every gift by either spouse to third parties for the year, and both returns are filed where required | | | |
| R7 | GST | Each trust transfer with skip potential has an inclusion ratio status and an allocation or election plan by the C16 date | | | |
| R8 | Inclusion | Every transferred asset with retained enjoyment, control, insurance incidents or a three-year release is tested under 2035, 2036, 2038, 2042 | | | |
| R9 | Basis | Step-up claimed only for property in the gross estate | | | |
| R10 | Clocks | Every triggered clock row has a computed date, weekday, roll result and status label | | | |
| R11 | Tax arithmetic | Tentative tax minus gift tax payable minus credit equals net tax in each alternative | | | |

## 11. Issues and judgment calls

| # | Severity | Issue | Sources in conflict (locators) | Controlling source and why | Effect on tax or deadline | Recommendation and alternative | Owner |
|---|---|---|---|---|---|---|---|

Severity: Critical (an election or deadline is lost or at risk, or tax changes materially); High (a figure changes materially under an alternative reading); Medium (a conflict with a clear controlling source); Low (clean-up).

## 12. Declined and not prepared items

When a hard stop blocks part of a request, deliver the rest and list the blocked part here using these labels verbatim:
- **Declined: altered-record request**: a request to backdate, re-date or alter a document, signature, notice, appraisal or valuation date (hard stop H3). State what was asked, why it is declined, and the accurate alternative (for example a transfer dated when it is actually made).
- **Not prepared: H1 (transferor facts missing)**, **Not prepared: H2 (prior transfers unknown)**, **Not prepared: H4 (no valuation support)**, **Not prepared: H5 (final advice or opinion requested)**: name the missing item and what would allow the work.

## 13. Hand-offs

A hand-off names the facts the receiving workflow needs.

| To | Trigger | Facts passed (figures, dates, locators) | Open questions | What this analysis did not do |
|---|---|---|---|---|
| building-equity-valuation-models | Fair market value of a closely held interest: the appraisal of the entity interest, the DCF or comparables, and discounts for lack of control or marketability as modeled | | | This skill kept the transfer-tax treatment: 2031 and 2512 standard, Chapter 14, adequate disclosure, inclusion, penalties |
| ilit | Drafting an irrevocable life insurance trust or other Crummey trust instrument | | | |
| flp-agreement | Drafting a family limited partnership agreement | | | |
| legal-research | No dedicated skill exists: GRAT, SLAT, IDGT or dynasty trust instruments, QDOT terms, state estate or inheritance tax law, nonresident alien estate tax and treaties, 2032A eligibility, Crummey notice law | | | |
| managing-tax-controversy | An estate or gift tax return under IRS examination, a statute extension, a protest or a Tax Court petition | | | |

Add or remove rows to match the matter, using the Related Skills list in SKILL.md.

## 14. Open items and [VERIFY] list

| # | Open item | Gap class (unknown fact, source conflict, unverified external lookup, policy election) | Depends on | Owner | Next action | Changes which result |
|---|---|---|---|---|---|---|

Close with: "Draft for review by a qualified estate and gift tax adviser. Not tax or legal advice, not a return, and not an opinion."

## Label tests

Use each label only when its test is met; when two seem to fit, the test decides.

| Label set | Label | Test |
|---|---|---|
| Interest | Present interest | The donee (or a trust beneficiary under a withdrawal right in the instrument when the gift was made) can use, possess or withdraw the property now |
| Interest | Future interest | Use, possession or enjoyment begins later, or the only access is a trustee's discretion; no annual exclusion |
| Interest | Not determinable | The instrument or the transfer date is missing |
| Disclosure | Adequately disclosed | Every item in Treas. Reg. 301.6501(c)-1(f)(2)(i)-(v) is on the return or attached, or a (f)(3) appraisal replaces item (iv) |
| Disclosure | Not adequately disclosed | Any (f)(2) item is missing and no (f)(3) appraisal supplies item (iv); the gift tax period stays open |
| Disclosure | Not determinable | The return or its attachments were not supplied |
| Portability | Elected | A timely Form 706 was filed and the executor did not opt out |
| Portability | Available by Rev. Proc. 2022-32 | No timely return, the estate was not required to file by value, and the fifth anniversary of death has not passed |
| Portability | Ruling route only | Not required to file by value, no timely return, and the fifth anniversary has passed |
| Portability | Lost | The estate was required to file by value and missed the C5 deadline |
| Portability | Not usable | The decedent is no longer the survivor's last deceased spouse and no DSUE was applied to gifts before the later spouse died; this label replaces any election label for that survivor, and the clock table still lists an open election window with the reason it does not help |
| GST | Exempt (inclusion ratio zero) | Exemption allocated (timely, late or automatically) equals the value of the transfer at the valuation date that applies |
| GST | Partially exempt | Some but less than full exemption allocated |
| GST | Non-exempt | No allocation and none automatic |
| GST | Not determinable | Prior allocations or the trust terms are unknown |
| Inclusion | Included | The facts meet each element of the section (for example a retained right to income under 2036(a)(1)) |
| Inclusion | Inclusion risk | Retained control, enjoyment or a release within three years is present but a fact or exception remains to be tested (bona fide sale, who holds the power, when it was released) |
| Inclusion | Not included | No inclusion section applies on the stated facts |
| Basis | Step-up (IRC 1014) | The asset is in the gross estate under a 1014(b) category |
| Basis | Carryover (IRC 1015) | The asset left by completed gift and is not in the gross estate, including assets of a grantor trust outside the estate |
| Clock | Open; Open (rolled by IRC 7503); Passed; Not triggered; Not determinable | As defined in `deadlines-and-elections.md` Section 4 |
