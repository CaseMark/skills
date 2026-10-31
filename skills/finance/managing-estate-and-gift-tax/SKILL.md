---
name: managing-estate-and-gift-tax
language: en
description: >
  Evaluates federal estate, gift and generation-skipping transfer (GST) tax
  planning and compliance for U.S. citizens and residents: the $15,000,000 basic exclusion
  for 2026 under Pub. L. 119-21 (indexed, no sunset), the $19,000 annual
  exclusion, anti-clawback, portability and DSUE (last deceased spouse, Rev. Proc.
  2022-32 late election), GST exemption allocation and automatic allocation elections,
  Crummey withdrawal rights, split gifts, adequate disclosure of gifts, Form 706 and
  Form 709 deadlines with the IRC 7503 roll, alternate valuation, 6166 and 6161
  payment relief, retained-interest inclusion under 2036, and transfer-tax
  treatment of the fair market value of a transferred interest (2031, 2512, Chapter 14,
  valuation understatement penalties). Covers no step-up for grantor trust assets
  (Rev. Rul. 2023-2), Connelly redemption and life insurance, gifts of closely held
  stock and generational transfers. Routes valuation models, instrument drafting, state law
  and IRS disputes. Drafts for qualified review.
tags:
  - management
  - tax
  - valuation
metadata:
  author: casemark
  practice_areas:
    - Tax Planning
    - Tax Compliance
    - International Tax
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---

# Managing Estate and Gift Tax

Reviews and plans U.S. federal estate, gift and GST tax matters for a donor, a decedent's estate or a married couple: how much exclusion is left and from which year, whether each gift and election was made correctly and on time, what the gross estate includes and at what value, and what tax is due and when. The deliverable follows `references/output-template.md`: people and transfers, an exemption ledger, gift and GST reviews, gross estate and basis, a clock table computed by script, the tax computation, reconciliation checks, issues, hand-offs and open items. It documents transfers as of the dates they actually occur. Everything it produces is a draft for review by a qualified estate and gift tax adviser; it is not tax or legal advice, not a return and not an opinion.

## Why This Skill Exists

Transfer tax work fails on dates, people and paperwork more than on arithmetic. Pub. L. 119-21 (July 4, 2025) replaced the scheduled 2026 drop in the basic exclusion with a permanent $15,000,000 indexed amount, so plans and memos written for a sunset now give wrong advice. Portability is won or lost on one return filed by the right executor for the right spouse. An annual exclusion claimed for a trust with no withdrawal right, a gift reported without the disclosure the regulation lists, or a GST allocation not made on a timely return costs money years later, when it can no longer be fixed. Estate values move with facts a summary leaves out: life insurance paid to a company that must redeem the decedent's shares, control retained over a family partnership, assets in a grantor trust that never enter the estate and never get a new basis. This skill reads the instruments, dates every figure, computes every clock from its own trigger, and refuses to fix a missed date by changing the paper.

## Where Mistakes Hide

Read each input with this suspicion before relying on it.

| Input / Document | What It Is Used For | Where the Error Hides |
|---|---|---|
| Planning memo, software projection or prior adviser letter | Remaining exclusion and the case for gifting now | A BEA from the wrong year; the pre-2026 "sunset to about half" assumed though Pub. L. 119-21 removed it; anti-clawback described as covering gifts the 2022 proposed exceptions target, or the proposed exceptions treated as final; 2027 indexed figures stated as known |
| Deceased spouse's estate file, Form 706 or decision not to file | Portability and the survivor's DSUE | No Form 706 filed so no election; DSUE taken from a spouse who is no longer the last deceased spouse; DSUE capped at the survivor's BEA instead of the deceased spouse's year; Rev. Proc. 2022-32 used for an estate that was required to file; the election treated as the survivor's to make |
| People, marriage and citizenship records (who gave, who consented, who is executor) | Whose exclusion, consent, election and marital deduction apply | Split gifts assumed without both spouses' consent or for only some gifts of the year; a noncitizen spouse given an unlimited marital deduction; a skip person misidentified; the surviving spouse acting for the deceased spouse's estate when someone else is executor |
| Trust instrument, Crummey provisions and contribution records | Annual exclusion and GST treatment of trust gifts | Exclusion claimed with no withdrawal right in the instrument; a withdrawal right added after the transfer; contribution dates not matched to the instrument; the trust assumed to receive automatic GST allocation when it is not a GST trust, or an automatic allocation left in place where it wastes exemption |
| Form 709 as filed, attachments and the appraisal behind it | Starting the gift tax statute and fixing the value | A closely held interest reported with "per appraisal" and no attachment; no 100 percent entity value or discount description; an appraiser who is a family member or employee; the statute assumed closed when it never started |
| Partnership, LLC or company agreements and the donor's retained roles | Discounts and estate inclusion | Discounts claimed while the donor keeps control of distributions or the income (2036), a release within three years of death (2035), or a lapse or liquidation restriction Chapter 14 disregards; the discount used without valuation support |
| Grantor trust instrument and basis records | Income tax basis after death | Step-up assumed for assets of an irrevocable grantor trust outside the estate, contrary to Rev. Rul. 2023-2; adjusted taxable gifts to that trust left out of the estate tax base |
| Buy-sell or redemption agreement and company-owned life insurance | Value of a decedent's closely held shares | The redemption obligation netted against the insurance proceeds, which Connelly v. United States rejects; the agreement price taken as the estate tax value without IRC 2703 |
| Deadline calendar and election checklist | Form 706, 709, portability, 2032, 6166, GST and split-gift timing | One anchor used for every deadline; nine months counted as 270 days; a weekend or DC holiday not rolled under IRC 7503; a filing extension treated as an extension to pay; 6166 or 2032 lost by a late return |
| Domicile and property location records | State estate and inheritance tax | The state layer left out, or a state threshold or portability rule assumed without reading the statute for the year |

## Ground Rules

1. **Draft only.** Every figure, status and recommendation is a draft for review by a qualified estate and gift tax adviser. Never call a conclusion final, an opinion, or a return ready to sign.
2. **Source-review gate.** Never call a document missing until the inventory has been checked and each file opened, including schedules, attachments and exhibits. Classify every unsettled item as an **unknown fact**, a **source conflict**, an **unverified external lookup** (published figures, state law, values) or a **policy election** (gift splitting, portability, 2032, 6166, GST allocation), with what would settle it.
3. **Hierarchy of authority.** For facts: executed instruments, filed returns and IRS letters govern over appraisals and account statements, which govern over inventories, ledgers and models, which govern over emails, memos and summaries. For law: the Code and final regulations govern over revenue procedures and rulings, which govern over proposed regulations, which govern over commentary. Name every conflict, show both versions, say which controls and why; never resolve one silently.
4. **Citation discipline.** Every fact carries a source locator or [UNVERIFIED]; every rule carries its citation from `references/primary-sources.md` or [VERIFY].
5. **Every figure carries its year.** Use the BEA and annual exclusion for the year of each gift and the BEA for the year of death. The BEA is $15,000,000 for 2026 and indexed after 2026 with no scheduled reduction; a figure for a year not yet published is [VERIFY].
6. **Right person, right return.** For each figure, name whose exclusion, consent, election or return it is: donor, consenting spouse, decedent, last deceased spouse, executor or trustee. Only the executor of the deceased spouse's estate elects portability; only both spouses together split gifts, and for every gift to third parties that year.
7. **Clocks by script.** Each deadline has its own trigger from `references/deadlines-and-elections.md`, is computed by script, and shows its weekday and whether IRC 7503 moves it. Check every window open on the as-of date. A filing extension never extends payment.
8. **No altered records.** Never backdate, re-date or alter a gift document, assignment, trust instrument or amendment, Crummey notice, appraisal, valuation date or signature, and never report a transfer in a year or at a date the executed documents contradict. A transfer is documented when it actually happens; a missed date is reported with its cure, not papered over.
9. **Value is supported, then disclosed.** A value for a closely held or hard-to-value interest comes from an appraisal or the financial data the disclosure regulation lists; the valuation itself is routed to building-equity-valuation-models. This skill tests the value against the transfer-tax rules (2031, 2512, Chapter 14, inclusion, penalties) and the disclosure requirements.
10. **Inclusion and basis together.** Test every transferred asset for inclusion under 2035, 2036, 2038 and 2042 before relying on a discount or an exclusion from the estate, and give a basis step-up only to property in the gross estate.
11. **State law is read, not assumed.** A state estate or inheritance tax figure comes from the state statute for the year, or the state layer is marked "not modeled" with [VERIFY].
12. **Scope.** U.S. citizens and residents under federal transfer tax. Nonresident aliens, treaties, instrument drafting, valuation models and IRS disputes are routed with a complete hand-off (Related Skills).

## Checkpoint A: Pre-Draft Intake (Mandatory)

Collect these, then build the source-review register (`references/output-template.md`, Header).

1. **Question and as-of date:** planning, a gift return, an estate return, portability, GST, or review of a memo; the date the analysis speaks from.
2. **People:** donor or decedent and every spouse (current, predeceased, later deceased), with citizenship, residence, domicile state, marriage dates and dates of death; executor and trustees.
3. **Prior transfers:** every Form 709 filed, or a statement that none was filed, for the donor and any consenting spouse; prior GST allocations and elections.
4. **Instruments:** wills, trusts (with withdrawal and distribution terms), assignments, partnership, LLC and shareholder agreements, buy-sell and redemption agreements, life insurance ownership and beneficiaries.
5. **Values:** appraisals and valuation reports with their dates; account statements at death and at the six-month date; the entity's full value where an interest is transferred.
6. **Estate facts:** gross estate inventory, deductions claimed, prior Form 706 of a deceased spouse, any filing or payment extension already requested.
7. **States:** domicile and the location of real and tangible property.

**Default fallbacks (each recorded as a policy election or unknown fact):** state layer "not modeled" if the state statute was not read; deadlines shown without extensions, with the extended date as a separate row (but an income tax extension for the year extends Form 709 under IRC 6075(b)(2), so ask before using the April 15 default); projections after 2026 use the 2026 BEA labelled a [VERIFY] proxy, which understates an indexed amount; no gift splitting unless both spouses consent, because consent is all-or-nothing for the year; deductions shown as zero only when the user says so.

**Hard stops (deliver everything else and label the blocked part as Section 12 of the template requires):**
- **H1.** The donor or decedent, or any spouse whose exclusion, DSUE, consent or marital deduction the result uses (including a predeceased or later deceased spouse and a consenting spouse), cannot be identified with citizenship or residence and the date of each gift or death: no exclusion, DSUE or tax figure for that person.
- **H2.** A remaining-exclusion, GST-exemption or tax figure is requested and the prior taxable gifts and GST allocations of the donor or decedent, and of a consenting spouse for any split year, are unknown and cannot be bracketed from filed Forms 709 or a statement that none were filed: that figure is not prepared.
- **H3.** The request is to backdate, re-date or alter a gift document, assignment, trust instrument or amendment, Crummey notice, appraisal, valuation date or signature of the donor, a spouse, a trustee, an executor or an appraiser, or to report a transfer at a date the executed documents contradict: that part is declined.
- **H4.** The donor, a consenting spouse or the executor asks for a Form 706 or 709 reporting value for an interest not traded on an established exchange, and neither an appraisal or valuation report (supplied as a file or a labelled excerpt) nor the financial data listed in Treas. Reg. 301.6501(c)-1(f)(2)(iv) is in the file: no reporting value is drafted.
- **H5.** The request is to present the work as a final return, a tax opinion, or advice addressed to a third party (lender, buyer, beneficiary, court).

## Step 1: Inventory, People and Routing

Open every file and build the source-review register. Fill the people table and the transfer list in Section 2 of `references/output-template.md` from executed documents. Check each hard stop against every person the facts imply, including a predeceased spouse, a consenting spouse and an executor named only in a will. Route out-of-scope questions now with the Related Skills list.

## Step 2: Exemption Ledger and Portability

Read `references/transfer-tax-rules.md` Sections 1 to 4. Build the ledger year by year with that year's BEA and annual exclusion. For each deceased spouse, compute DSUE, decide who the last deceased spouse is, and give the portability status label from the template's label tests. Test anti-clawback only where a lower BEA is in issue, and state that the 2022 exceptions are proposed.

## Step 3: Gift Review and Disclosure

Read `references/transfer-tax-rules.md` Sections 5 and 6. For each gift: present or future interest from the instrument as it stood on the transfer date; split-gift consent and who files; Form 709 required or not; disclosure label with the missing items listed. For a closely held interest, check the (f)(2)(iv) items and whether any appraisal meets (f)(3), including the appraiser's relationship to donor and donee.

## Step 4: GST Review

Read `references/transfer-tax-rules.md` Section 7. Classify each transfer (direct skip, indirect skip, none), test whether a trust is a GST trust under IRC 2632(c)(3)(B), and state whether exemption was or will be allocated automatically, must be allocated affirmatively, or should be elected out, by whom and by which Form 709.

## Step 5: Gross Estate, Valuation and Basis

Read `references/transfer-tax-rules.md` Sections 8 to 10. List every asset with its inclusion label and section, the value relied on and its support. Recompute any entity value that a Connelly redemption, a 2703 agreement or Chapter 14 changes, and show both versions. Route the valuation model to building-equity-valuation-models. Give each asset a basis label; grantor trust assets outside the estate keep carryover basis.

## Step 6: Clock Table

Read `references/deadlines-and-elections.md`. For every element the matter triggers, compute the prescribed date by script from its own trigger, its weekday, the IRC 7503 rolled date, and the status label on the as-of date. List every Open window, who must act, and whether acting would help.

## Step 7: Tax Computation, Payment and State Layer

Read `references/transfer-tax-rules.md` Sections 2, 11 and 12. Compute the gift or estate tax in each alternative (date-of-death and alternate valuation; the supplied value and the supported value), with the ratio of any reported value to the supported value under IRC 6662(g). Test 6166 eligibility and acceleration and the need for a 6161 request. Add the state layer or mark it "not modeled".

## Step 8: Reconcile, Issues, Hand-Offs and Open Items

Complete reconciliation checks R1 to R11 in `references/output-template.md` Section 10; each Fail becomes an issue. Rank issues by the template's severity rule. List declined and not prepared items with the template's labels verbatim. Write complete hand-offs and the open items and [VERIFY] list from `references/primary-sources.md`.

## Checkpoint B: Post-Draft Alignment

Before the Quality Audit, re-read the request and confirm:
- The deliverable answers the question for the people, transfers and years asked, and says what was routed.
- Each result that depends on an election (portability, split gifts, GST allocation, 2032, 6166) shows the outcome with and without it and who must make it.
- No user instruction that conflicts with an executed document, a filed return or the statute was followed silently; any backdating request appears in Section 12 as "Declined: altered-record request".
- The closing line from the template is present.

## Quality Audit

Confirm each statement is true of the draft; fix the draft if one is not.

1. Every BEA, annual exclusion and GST figure shows its year and source, and nothing assumes a 2026 sunset.
2. The exemption ledger ties to prior Forms 709 and current gifts, and remaining exclusion equals BEA plus usable DSUE minus cumulative taxable gifts.
3. DSUE comes only from the last deceased spouse, with the election status label and the person who must elect.
4. Each trust gift's annual exclusion rests on a withdrawal right in the instrument on the transfer date.
5. Split gifts, if used, cover all of both spouses' gifts for the year and show both returns where required.
6. Each reported gift of a closely held interest has its disclosure label and the missing (f)(2) or (f)(3) items.
7. Each trust transfer has a GST classification, the GST trust test result, and an allocation or election plan by the timely Form 709 date.
8. Every transferred asset with retained enjoyment, control, insurance incidents or a recent release is tested under 2035, 2036, 2038 or 2042.
9. Entity values reflect Connelly and IRC 2703 where a redemption or buy-sell agreement exists, with both versions shown.
10. No basis step-up is given to property outside the gross estate.
11. Every triggered clock row shows trigger, prescribed date, weekday, IRC 7503 result and status on the as-of date, and every Open window is listed.
12. Every fact has a locator or [UNVERIFIED]; every hard stop's blocked part carries its label; the state layer is read or marked "not modeled".
13. The draft-for-review closing line is present and nothing is presented as a return or opinion.

## Guidelines

- Show the tax arithmetic step by step so a reviewer can redo it; label every amount with its year.
- Keep the donor's view, the estate's view and each beneficiary's basis view separate; the lowest transfer tax can leave the highest income tax.
- Treat a client's preferred answer, and a prior adviser's memo, as a hypothesis to test against the statute and the instruments.
- When an election or deadline is already lost, say so plainly and give the remaining cure (late election procedure, letter ruling, late allocation at current value), not a workaround that changes the record.
- Do not opine on value; record the value relied on, its support and its disclosure, and route the valuation.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Prior Forms 709 missing or only a summary of gifts exists | Returns not kept or never filed | Request transcripts or copies; bracket from records if possible; otherwise H2 applies to the remaining-exclusion figure |
| Trust instrument is unsigned, partial or a later restatement | Executed original not supplied | Analyze the text supplied with [UNVERIFIED]; list each conclusion that depends on the executed terms on the transfer date |
| Appraisal is a draft, undated or prepared by a relative | Valuation support incomplete | Record the gap; test it against 301.6501(c)-1(f)(3); route the valuation; H4 applies if no support at all |
| Inventory value and statement value differ | Different valuation dates or a stale inventory | The statement at the valuation date controls; show both and the date of each |
| Executor and surviving spouse give different facts about a prior return | Return not located | Treat filing as an unverified external lookup; show the portability result under each version |
| A memo states a figure or rule the statute contradicts | Stale law or misquoted commentary | The statute controls; record the conflict in Section 11 |
| State rules unclear for the year | Recent amendment or repeal | Mark [VERIFY] with the state and year; show the federal result alone |

## Related Skills

- building-equity-valuation-models: fair market value of a closely held interest, including the appraisal of the entity interest, DCF, comparables and discounts for lack of control or marketability as modeled; this skill keeps the transfer-tax treatment of that value.
- ilit: drafting an irrevocable life insurance trust or another Crummey trust instrument.
- flp-agreement: drafting a family limited partnership agreement.
- qprt: drafting a qualified personal residence trust under IRC 2702.
- charitable-remainder-trust: drafting a CRAT or CRUT.
- revocable-living-trust: drafting a revocable living trust.
- last-will-and-testament: drafting or reviewing a will.
- shareholder-agreement: drafting buy-sell terms in a shareholder agreement.
- deed-of-gift: drafting the deed for a gift of real or personal property.
- legal-research: no dedicated skill exists for GRAT, SLAT, IDGT or dynasty trust instruments, QDOT terms, state estate and inheritance tax law, nonresident alien estate tax and treaties, 2032A eligibility, or Crummey notice law.
- managing-tax-controversy: an estate or gift tax return under IRS examination, a statute extension, a protest, a Tax Court petition or a penalty defense.
- analyzing-corporate-tax-structures: S election and QSBS consequences when closely held stock is given or passes at death.
- conducting-wealth-transfer-analysis: designing transfer structures and comparing trust designs across family goals.
- managing-estate-planning: reviewing an overall estate plan and legacy documentation beyond the transfer tax.
- managing-trust-administration: administering an existing trust, distribution decisions and trust tax reporting.
- managing-charitable-giving-strategies: choosing among charitable vehicles, donor-advised funds and foundations.
- analyzing-life-insurance-products: comparing life insurance products and costs for an ILIT or a redemption plan.
- managing-business-succession-planning: business exit planning and buyer identification.
- estate-administration-summary: a probate or estate administration status summary.
- final-tax-return-filing: the decedent's final individual income tax return.

## Reference Files

- `references/transfer-tax-rules.md`: figures by year, tax computation, BEA and anti-clawback, portability, gifts and Crummey rights, adequate disclosure, GST, inclusion, valuation and Chapter 14, basis, 6166 and 6161, noncitizen spouses and states.
- `references/deadlines-and-elections.md`: clock table with a trigger per element, the date script, IRC 7503 and DC holidays, window status labels, election traps.
- `references/output-template.md`: deliverable sections, ledger and review tables, clock table, reconciliation checks R1 to R11, decline labels, hand-off table, label tests.
- `references/primary-sources.md`: each authority checked with URL, method and date, conflicts found, disposition of the prior stub, and the [VERIFY] list.
