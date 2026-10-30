# Output Template

Produce the header and the sections below, in this order. Put dates and amounts in tables; keep prose short. Every fact carries a source locator (document, page or line, transcript code) or [UNVERIFIED]; every rule carries its citation from `references/primary-sources.md` or [VERIFY]. Omit a section only when the request does not reach it, and say so in one line.

## Contents

1. Header and source-review register
2. Section 1. Controversy posture and blocking issues
3. Section 2. Clocks register
4. Section 3. Issue matrix
5. Section 4. Penalty analysis
6. Section 5. Privilege and record register
7. Section 6. Options and recommendation
8. Section 7. Draft documents
9. Section 8. Reconciliation checks
10. Section 9. Hand-offs
11. Section 10. Open items and [VERIFY] list

## Header and source-review register

- Taxpayer, taxpayer type (individual, C corporation, S corporation, partnership under BBA, estate), tax and periods, date prepared, "Draft for review by a qualified tax professional or counsel."
- Today's date; the circuit to which a Tax Court case would be appealable (7482(b)) and the fact that fixes it (legal residence or principal place of business, with source).
- Who is acting and under what authority: Form 2848 (taxes, forms and periods covered), officer title, partnership representative and designated individual.

| File | Type | Date | Rank | Status | Pages or sections read | Note |
|---|---|---|---|---|---|---|
| name as received | notice, letter, Form 4549/RAR, NOPA, IDR, transcript, return, consent, penalty approval form, engagement letter, correspondence | | 1-4 | Reviewed / Not relevant / Unreadable after attempt / Still needed | | |

Rank: 1 the IRS notice or form itself and the IRS transcript; 2 the filed return and executed consents or agreements; 3 the examiner's workpapers, NOPAs and correspondence; 4 client summaries, emails and recollection.

## 1. Controversy posture and blocking issues

One paragraph: current stage (exam, 30-day letter, Appeals, notice of deficiency, docketed, collection, BBA NOPPA or FPA), what the IRS has proposed, and the amount in dispute. Then a ranked list of blocking issues: any deadline within 10 business days or already passed, any authority gap, any hard stop, any source conflict that changes a date.

## 2. Clocks register

One block per clock in the fixed format in `references/clocks-and-deadlines.md` Section 2, then a summary table. Each clock has its own trigger.

| # | Clock | Authority | Trigger event and date (source) | Counting rule | Raw last day | Rolled? | Due date | Competing reading | Owner |
|---|---|---|---|---|---|---|---|---|---|

For the petition clock add: the date stated on the notice, the circuit, and that circuit's jurisdictional and tolling status with the case name. Tolling is never listed as a due date.

## 3. Issue matrix

| # | Adjustment (IRS amount) | Taxpayer position | Key facts (locators) | Authority for | Authority against | Documentation status | Hazards view and settlement range | Recommendation |
|---|---|---|---|---|---|---|---|---|

Documentation status is one of: documented, partly documented (name the gap), undocumented (client assertion only), conceded (date, by whom, with written authorization or not).

## 4. Penalty analysis

| Penalty (section) | Amount and computation | Threshold test | 6751(b): proposer, supervisor, approval date, first communication, notice date, assessment date | Governing timing rule (circuit or regulation) | Reasonable cause record | Other defenses (6662(d)(2)(B), FTA eligibility) | Assessment |
|---|---|---|---|---|---|---|---|

State whether FTA is available for each penalty; it is never available for 6662.

## 5. Privilege and record register

| Document or communication | Author and recipient | Date | Purpose | Protection claimed (attorney-client, 7525, Kovel, work product, none) | Limits that defeat it (criminal, state, return preparation, shelter promotion, waiver) | Produced, withheld or logged |
|---|---|---|---|---|---|---|

## 6. Options and recommendation

| Option | What it does | Deadline it depends on | Cost and payment required | Effect on other clocks | Risks | Recommended? |
|---|---|---|---|---|---|---|

Typical options: respond at exam; request competent authority assistance or an APA (with any protective claim); sign a consent (fixed, open-ended, restricted) or refuse; protest to Appeals; petition the Tax Court; pay, claim and sue; request a CDP or equivalent hearing; BBA modification, push-out or petition. Judgment calls list the options, the choice and what changes under each.

## 7. Draft documents

Drafts only, each headed "DRAFT - not for filing or signature until reviewed": IDR cover letter, protest (Pub. 5 elements), consent counterproposal or cover letter, penalty abatement or reasonable cause statement, refund claim explanation, CDP hearing request statement, BBA modification request outline, petition outline. A signature block is left blank with the authorized signer named.

## 8. Reconciliation checks

Every row is computed, not asserted. A Fail goes to Section 1.

| # | Check | Test | Result (Pass / Fail / Not applicable) | Note |
|---|---|---|---|---|
| C1 | Each clock has its own trigger | No two clocks share a trigger unless the statute says so | | |
| C2 | Dates recomputed by script | Script output matches every due date in Section 2 | | |
| C3 | 7503 roll | Every raw last day on a weekend or D.C. holiday is rolled; no others | | |
| C4 | Notice date versus statute | Petition due date is the earlier of the statutory date and the notice's stated date | | |
| C5 | Refund look-back | Refund requested is at or below tax paid within the applicable look-back | | |
| C6 | Deficiency arithmetic | Tax required to be shown minus tax shown equals the deficiency used for penalties | | |
| C7 | Penalty arithmetic | Rate times the penalized portion; threshold test shown | | |
| C8 | Imputed underpayment | Netting by category and rate by partner type tie to the NOPPA and the modification schedule | | |
| C9 | Authority | Every signature-ready document has a documented signer for that tax and period | | |
| C10 | Concessions | Every conceded item has written client authorization and a source | | |

## 9. Hand-offs

A hand-off names the facts the receiving workflow needs; a bare skill name is not a hand-off.

| To | Why | Facts passed (amounts, dates, notices, locators) | Open questions | What this draft did not do |
|---|---|---|---|---|
| managing-tax-provision-preparation | ASC 740 reserve and disclosure effect of the proposed adjustments | | | |
| analyzing-state-income-tax | State reporting of the federal change and state exposure | | | |
| analyzing-partnership-tax-structures | Partner-level allocation and outside basis effects of a BBA adjustment or push-out | | | |
| managing-transfer-pricing-compliance | Pricing substance behind a proposed 482 adjustment, a MAP position or an APA proposal: method, comparables, range, 6662(e) documentation | | | |
| legal-research | Criminal exposure, state controversy procedure, or circuit law not covered here; no dedicated skill exists for these | | | |

Add or remove rows to match the matter.

## 10. Open items and [VERIFY] list

| # | Open item | Gap class (unknown fact / source conflict / unverified external lookup / policy election) | Depends on | Owner | Next action | Changes which date or amount |
|---|---|---|---|---|---|---|

Then each [VERIFY] statement and what would settle it.

Close with: "Draft for review by a qualified tax professional or counsel. Not legal or tax advice, and not a filing."
