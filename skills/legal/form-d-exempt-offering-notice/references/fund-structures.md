# Pooled Investment Fund Handling

Read this for any fund issuer. Form D asks the same questions of funds and operating companies, but funds put different people, amounts and investors behind the same fields.

## Contents

1. Related persons for a fund (Item 3)
2. Structures: parallel funds, feeders, offshore feeders and Regulation S
3. Issuer-specific reconciliation before any program presentation
4. Item 13 presentation for multi-vehicle programs
5. Item 15 placement fees
6. Qualification conflicts and the required write-up
7. Minimum investment waivers

## Related persons for a fund (Item 3)

Candidate list:

1. The general partner entity (or the manager, for a fund without a general partner).
2. The general partner's managing members, managers, executive officers and directors, that is, the natural persons performing the functions of an executive officer or director of the fund.
3. Where the firm's practice includes them, the investment adviser's executive officers `[VERIFY]`. The form's text does not mention investment advisers or managers; this is a firm-practice judgment call. State which practice you applied.

The form's text requires each executive officer, director and person performing similar functions, naming general and managing partners and managing members as examples. Listing an entity general partner as well as its principals is observed practice, not stated in the instructions `[VERIFY]`; use the clarification field to explain each entry's capacity.

**Source priority for the list.** Take the list from the governing documents in effect on the filing date: the schedule of managing members or general partners in the partnership agreement, the general partner's LLC agreement and any amendments, and incumbency certificates. Org charts, prior filings and client instructions are secondary sources and are often stale. If a client instruction or an org chart omits or adds a person, say so, cite both sources, and use the governing documents. If an amendment that may change the list is unreadable or still needed, the affected rows are Unknown fact rows with the consequence stated (`form-d-items.md`, Item 3).

**Check against the prior filing.** Compare the governing-documents list to the related persons on the previously filed notice. Flag every person who appears in the governing documents but not in the prior filing: it is an amendment trigger (new related person, never excepted), and each such person is a covered person to route to `bad-actor-disqualification-review`. Also flag persons on the prior filing who no longer appear in the governing documents, and confirm whether they have left.

## Structures

### Parallel funds

Two or more funds invest side by side under common terms. Present these options as a judgment call, with a recommendation:

- **Separate Form Ds**, one per fund. Each issuer has its own date of first sale, deadline, Item 13 amounts and Item 14 counts. Cleaner where the funds close at different times or rely on different exemptions or exclusions, and where states require separate filings.
- **Co-issuers on one Form D.** Multiple issuers in Item 1, one primary issuer, additional issuers on Items 1 and 2 continuation pages. Staff guidance permits one filing for issuers that sold in the same Regulation D offering, with a master fund and its feeders as the example. Consequences: one date of first sale and one deadline set by the earliest sale; each issuer needs its own CIK and CCC; one exemption selection and one set of Section 3(c) paragraphs for all issuers; some states require a filing per issuer. Do not predict the file numbers EDGAR assigns `[VERIFY]`.

State the date of first sale for each vehicle in either structure. If the vehicles have different first-sale dates, say how the filing structure changes the deadline. Under either structure, each issuer's own figures are computed first (next section).

### Feeder funds into a master or main fund

A feeder that invests in a main fund is one investor in the main fund. In the main fund's Form D, count the feeder once in Item 14 and its commitment once in the amount sold; do not add the feeder's own investors or their commitments on top. The feeder's investors and their commitments are reported on the feeder's own Form D if the feeder is a separate issuer offering its own interests, or on a co-issuer filing under the approach chosen above. Record the counting approach in the memo, and cross-reference it in the Item 13 clarification so a reader of the public filing is not misled.

### Offshore feeders and Regulation S

Sales to non-U.S. persons under Regulation S are outside Regulation D. Under Rule 500(g), Regulation S purchasers are not counted in Regulation D's purchaser count and the proceeds are excluded from the aggregate offering price, unless the issuer elects to rely solely on Regulation D for offers or sales outside the United States, in which case the non-U.S. investors are counted. Whether Form D reports Regulation S sales is not stated in the form's instructions `[VERIFY]`. Choose one of two approaches, present it as an Issuer election, and apply it consistently with prior filings:

- Report Regulation D sales only, and say so in the Item 13 clarification; or
- Report all sales, and say so in the Item 13 clarification.

Whenever any Regulation S sale exists, the issuer schedule and the worksheet present Items 13(b) and 14 in both variants on adjacent rows, "Regulation D only: $X / N investors" and "All sales: $Y / M investors", with the recommended variant marked. The draft never defaults to one figure, and the over-inclusive figure is never the only one shown. Item 12's states of solicitation includes a Foreign/Non-US option. If the offshore feeder is a separate issuer, decide whether it needs its own notice for any Regulation D sales it makes, and whether it has its own CIK; where the first accepted sale is a Regulation S sale, the date of first sale is a judgment call between that date and the first Regulation D acceptance, with the earlier used for the deadline.

## Issuer-specific reconciliation before any program presentation

Every issuer on a Form D, whether on its own notice or as a co-issuer line, reports its own Items 13, 14 and 15. Compute each issuer's figures separately, from that issuer's executed documents, before any program-wide number is written anywhere. Produce one issuer calculation schedule per issuer, then one program schedule. Both go in Section 3 of the output (`output-template.md`).

**Investor reconciliation table.** One row per investor of the issuer, every investor, before any total:

| Investor | Introduced by (agent or direct) | State or non-U.S. | Executed amount (subscription, each executed amendment, acceptance date) | Ledger amount | Delta | Regulation D or S | Resolution |
|---|---|---|---|---|---|---|---|

A non-zero delta is a conflict: the executed document controls, and the row's Resolution names the Section 2 entry. The table is the only source of the issuer's Item 13(b) and Item 15 figures; an empty or partial table means the draft is incomplete.

**Per-issuer schedule.**

| Line | Content | Source |
|---|---|---|
| Amount sold (Item 13(b)) | Sum of the table's executed amounts; for a fund, commitments, not capital called; never a figure copied from a ledger total, closing memo or email | Investor reconciliation table |
| Total offering amount (Item 13(a)) | The issuer's own cap, its allocation of a shared cap, or the program cap under the approach selected in the next section | Offering document and supplements; prior filing for the approach |
| Remaining (Item 13(c)) | (a) minus (b), or Indefinite | Arithmetic |
| Investors (Item 14) | Count by investor name; non-accredited count by name | Executed questionnaires |
| Feeder or master counting | A feeder is one investor in the master, for the feeder's commitment; the feeder's own investors appear only on the feeder's schedule | The feeder's subscription into the master |
| Regulation D versus Regulation S | When any Regulation S sale exists: 13(b) and 14 in both variants (Regulation D only; all sales), with the recommended one marked | Table's Regulation D or S column; offering document |
| Sales compensation (Item 15) | Rate times the table's executed amounts for agent-introduced investors; payer; estimate flag; any ledger fee figure is a cross-check only | Placement agreement; investor reconciliation table |

**Program schedule.** Sum the issuer schedules and show: the program cap; program amount sold; program remaining (cap less all vehicles' sales); the duplicate check (a feeder commitment appears once at the master and once on the feeder's own schedule, never twice at the master, and never at the program level twice); and the Regulation S total.

**Arithmetic check.** For each issuer, show that (a) minus (b) equals (c). If the identity does not hold, name the expressly adopted treatment that explains it: Indefinite; a shared cap reported in full on each issuer (then each issuer's (c) overstates program capacity, and the program schedule gives the true remaining); or Regulation S sales excluded from (b) and (c) but shown on the program schedule. Any other difference is an error to fix before drafting.

**Program totals in issuer fields.** Do not put a program-wide amount in an issuer's Item 13 unless all three hold: (1) the selected reporting approach supports it (a co-issuer filing that reports the offering as a whole, or an established approach of reporting the shared cap on each issuer with a clarification); (2) the rationale is stated in Section 4; and (3) the Item 13 clarification says what scope the number covers, for example "Total offering amount is the $250,000,000 cap shared by [Issuer] and [Parallel Issuer]; this issuer has sold $106,000,000." Item 14 has no clarification field, so a program-wide investor count never goes on an issuer's own notice.

**Worked example (synthetic).** Program cap $250,000,000 shared by Main and Parallel; Feeder invests all of its commitments in Main.

| Issuer | Sold (13(b)) | Investors (14) | Commissions (15) |
|---|---|---|---|
| Main | $91,000,000 from five investors plus the Feeder's $15,000,000 = $106,000,000 | 6 (five investors plus the Feeder) | 2 percent of the $25,000,000 introduced by the agent = $500,000 |
| Parallel | $50,000,000 | 2 | 2 percent of $20,000,000 = $400,000 |
| Feeder | $15,000,000 | 3 | none |
| Program | $156,000,000 (Main plus Parallel; the Feeder's $15,000,000 is already inside Main) | not reported as a count | $900,000 |

Program remaining: $250,000,000 less $156,000,000 = $94,000,000. If Main and Parallel each report the $250,000,000 cap as (a), their (c) figures ($144,000,000 and $200,000,000) each overstate program capacity; the clarification says the cap is shared and Section 4 states the $94,000,000. The Feeder reports its own cap or allocation.

## Item 13 presentation for multi-vehicle programs

Choose one of: report the program cap with a clarification; report a per-vehicle allocation; or report Indefinite where the amount cannot be determined. Follow the issuer's prior-filing approach unless there is a reason to change, and explain any change in the memo. The per-issuer figures come from the schedules above, and the conditions for using a program total apply. Compare the current cap in the offering documents (and any supplement) with the cap on the prior filing. A cap increase is an amendment trigger when the cumulative increase since the previously filed notice exceeds 10 percent; compute the percentage.

## Item 15 placement fees

Placement fees are often paid by the adviser rather than the fund. Report the commissions and finder's fees connected with the offering, per issuer from the schedule above, estimating unknown amounts, and explain the adviser as payer in Item 15's clarification. SEC Securities Act Forms C&DI 130.08 confirms the amounts are not limited to payments from offering proceeds. The adviser's payment does not justify $0. If a prior filing reported $0 but the documents show placement fees, escalate the discrepancy rather than copying it, and assess a corrective amendment.

## Qualification conflicts and the required write-up

For every investor, extract the accredited-investor and (for 3(c)(7) funds) qualified-purchaser or knowledgeable-employee status from the executed subscription and questionnaire, and compare it to the administrator's ledger flags.

If any questionnaire shows an investor who is neither a qualified purchaser nor a knowledgeable employee in a Section 3(c)(7) fund, or who is not an accredited investor, or whose answers conflict with the ledger flag, escalate before filing. Do not just report the count. A ledger flag establishes only what the administrator recorded; it never controls over an executed questionnaire.

**Rule 506(b) consequences of a non-accredited investor.** Non-accredited purchasers are permitted only under Rule 506(b) (Rule 506(c) requires all purchasers to be accredited), limited to 35 in any 90-day period, each of whom must have, alone or with a purchaser representative, the knowledge and experience to evaluate the investment, or the issuer must reasonably so believe immediately before the sale. The issuer must furnish the Rule 502(b) information (for a non-reporting issuer, specified non-financial and financial statement information) a reasonable time before sale. Rule 508 is unlikely to cure a failure to deliver that information to the very investor it protects `[VERIFY]` (inference from the rule text).

**Investment Company Act consequences.** A Section 3(c)(7) issuer's outstanding securities must be owned exclusively by qualified purchasers at the time of acquisition, subject to the carve-outs (knowledgeable employees; securities received by gift, bequest or involuntary transfer from a qualified purchaser). A non-qualifying owner outside them means the fund cannot rely on 3(c)(7) and would have to qualify under Section 3(c)(1) (not more than 100 beneficial owners, 250 for a qualifying venture capital fund) `[VERIFY]` as applied to a mixed fund. That changes the Item 6 selection and the Item 14 counts. Adjacent questions outside Form D (adviser fee arrangements under the Advisers Act; rescission or redemption mechanics) are named as open questions for the attorney, not analyzed `[VERIFY]`.

**Required write-up for each conflict.** The output states, in this order:

1. **The questionnaire response as given.** The question, the box checked or the figure entered, the date and the signatory. Quote it.
2. **The governing requirement.** The exemption (Rule 506(b) or (c)) and the exclusion (Section 3(c)(1) or 3(c)(7)) in the offering and governing documents, with the definition the response is tested against (accredited investor under Rule 501(a); qualified purchaser under Section 2(a)(51); knowledgeable employee under Rule 3c-5).
3. **The legal or fund-structure issue** the response raises, with the consequences set out above.
4. **What the record establishes and what it does not.** An executed questionnaire establishes what the investor represented. It does not establish that the representation is wrong, that the ledger is wrong, or that the investor qualifies by another route (for example, a family company owned by qualified purchasers, or a knowledgeable employee). A questionnaire that is unsigned, undated or internally inconsistent is itself a conflict to raise with the investor.
5. **The recommended next step, with owner.** Confirm with the investor whether the response was an error and obtain a corrected executed questionnaire; or, if the response stands, counsel decides among the options the documents allow (reject before acceptance; rescind or redeem; transfer; admit as a knowledgeable employee if the facts support it; rely on a different exemption or exclusion).
6. **The Form D consequence if the investor remains as the questionnaire describes.** The Item 6 selection (for a 3(c)(7) fund, whether 3(c)(1) is available and its 100-owner limit; for Rule 506(c), that it is unavailable with a non-accredited purchaser); the Item 14 non-accredited count and total; the Item 13 amount sold (unchanged unless the subscription is rescinded, since the sale occurred); and the blocking-issue entry in Section 2. Show the counts and selections under each outcome.

Present the decision points to the attorney: whether the subscription was accepted and when; whether the investor can be rejected, redeemed or transferred; whether the exemption and the exclusion survive; and what the filing should say. Do not recommend filing until the attorney has resolved it.

## Minimum investment waivers

If the general partner accepted a commitment below the stated minimum, run the Item 11 decision framework in `form-d-items.md` and present the recommended value and alternatives in Section 4. There is no clarification field on Item 11.
