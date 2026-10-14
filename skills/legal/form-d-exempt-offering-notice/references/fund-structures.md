# Pooled Investment Fund Handling

Read this for any fund issuer. Form D asks the same questions of funds and operating companies, but funds put different people, amounts and investors behind the same fields.

## Related persons for a fund (Item 3)

Candidate list:

1. The general partner entity (or the manager, for a fund without a general partner).
2. The general partner's managing members, managers, executive officers and directors, that is, the natural persons performing the functions of an executive officer or director of the fund.
3. Where the firm's practice includes them, the investment adviser's executive officers `[VERIFY]`. The form's text does not mention investment advisers or managers; this is a firm-practice judgment call. State which practice you applied.

The form's text requires each executive officer, director and person performing similar functions, naming general and managing partners and managing members as examples. Listing an entity general partner as well as its principals is observed practice, not stated in the instructions `[VERIFY]`; use the clarification field to explain each entry's capacity.

**Source priority for the list.** Take the list from the governing documents in effect on the filing date: the schedule of managing members or general partners in the partnership agreement, the general partner's LLC agreement and any amendments, and incumbency certificates. Org charts, prior filings and client instructions are secondary sources and are often stale. If a client instruction or an org chart omits or adds a person, say so, cite both sources, and use the governing documents.

**Check against the prior filing.** Compare the governing-documents list to the related persons on the previously filed notice. Flag every person who appears in the governing documents but not in the prior filing: it is an amendment trigger (new related person, never excepted), and each such person is a covered person to route to `bad-actor-disqualification-review`. Also flag persons on the prior filing who no longer appear in the governing documents, and confirm whether they have left.

## Structures

### Parallel funds

Two or more funds invest side by side under common terms. Present these options as a judgment call, with a recommendation:

- **Separate Form Ds**, one per fund. Each issuer has its own date of first sale, deadline, Item 13 amounts and Item 14 counts. Cleaner where the funds close at different times or rely on different exemptions or exclusions, and where states require separate filings.
- **Co-issuers on one Form D.** Multiple issuers in Item 1, one primary issuer, additional issuers on Items 1 and 2 continuation pages. Staff guidance permits one filing for issuers that sold in the same Regulation D offering, with a master fund and its feeders as the example. Consequences: one filing, so one date of first sale for the offering and one deadline set by the earliest sale; each issuer needs its own CIK and CCC; one exemption selection (506(b) and 506(c) cannot both appear) and one set of Section 3(c) paragraphs for all issuers; some states require a filing per issuer. Do not predict the file numbers that EDGAR assigns; in observed filings the primary issuer carries the base number and each additional issuer a sequential suffix, which is empirical rather than SEC text `[VERIFY]`.

State the date of first sale for each vehicle in either structure. If the vehicles have different first-sale dates, say how the filing structure changes the deadline.

### Feeder funds into a master or main fund

A feeder that invests in a main fund is one investor in the main fund. In the main fund's Form D, count the feeder once in Item 14 and in the amount sold; do not add the feeder's own investors on top. The feeder's investors are reported on the feeder's own Form D if the feeder is a separate issuer offering its own interests, or on a co-issuer filing under the approach chosen above. Record the counting approach in the memo, and cross-reference it in the Item 13 clarification so a reader of the public filing is not misled.

### Offshore feeders and Regulation S

Sales to non-U.S. persons under Regulation S are outside Regulation D. Under Rule 500(g), Regulation S purchasers are not counted in Regulation D's purchaser count and the proceeds are excluded from the aggregate offering price, unless the issuer elects to rely solely on Regulation D for offers or sales outside the United States, in which case the non-U.S. investors are counted. Whether Form D reports Regulation S sales is not stated in the form's instructions `[VERIFY]`. Choose one of two approaches and apply it consistently with prior filings:

- Report Regulation D sales only, and say so in the Item 13 clarification; or
- Report all sales, and say so in the Item 13 clarification.

Item 12's states of solicitation includes a Foreign/Non-US option. If the offshore feeder is a separate issuer, decide whether it needs its own notice for any Regulation D sales it makes, and whether it has its own CIK.

## Item 13 for multi-vehicle programs

Choose one of: report the program cap with a clarification; report a per-vehicle allocation; or report Indefinite where the amount cannot be determined. Follow the issuer's prior-filing approach unless there is a reason to change, and explain any change in the memo. When the cap is shared across vehicles, per-issuer arithmetic overstates program capacity: each issuer's "remaining" (cap less only its own sales) is larger than what the program can still sell. Report the figure the issuer's prior approach and clarification support, state the program-wide remaining (cap less the sales of all vehicles) in the memo, and make the clarification say which one the number is. Compare the current cap in the offering documents (and any supplement) with the cap on the prior filing. A cap increase is an amendment trigger when the cumulative increase since the previously filed notice exceeds 10 percent; compute the percentage.

## Item 15 placement fees

Placement fees are often paid by the adviser rather than the fund. Report the amount with a clarification, or report 0, and follow the issuer's prior approach. A staff interpretation states Item 15 is not limited to payments made out of offering proceeds `[VERIFY]`, which cuts against reporting 0 solely because the adviser bears the fee. If the prior filing reported 0 and the documents show a placement fee, escalate rather than copy the prior approach.

## Qualification conflicts

For every investor, extract the accredited-investor and (for 3(c)(7) funds) qualified-purchaser or knowledgeable-employee status from the executed subscription and questionnaire, and compare it to the administrator's ledger flags.

If any questionnaire shows an investor who is neither a qualified purchaser nor a knowledgeable employee in a Section 3(c)(7) fund, or who is not an accredited investor, or whose answers conflict with the ledger flag, escalate before filing. Do not just report the count. Explain the consequences and the decision the attorney needs to make.

**Rule 506(b) consequences of a non-accredited investor.** Non-accredited purchasers are permitted only under Rule 506(b); Rule 506(c) requires that all purchasers be accredited. Under Rule 506(b) there may be no more than 35 non-accredited purchasers in any 90-day period. Each non-accredited purchaser, alone or with a purchaser representative, must have the knowledge and experience to evaluate the merits and risks, or the issuer must reasonably believe so immediately before the sale. The issuer must furnish the Rule 502(b) information to each non-accredited purchaser a reasonable time before sale; for a non-reporting issuer that includes specified non-financial and financial statement information. The Rule 502(c) bar on general solicitation continues to apply. The Rule 508 insignificant-deviation defense is unlikely to cure a failure to deliver Rule 502(b) information to the very investor it protects `[VERIFY]` (this is an inference from the rule text).

**Investment Company Act consequences.** A Section 3(c)(7) issuer must have outstanding securities owned exclusively by qualified purchasers at the time of acquisition, and must not be making a public offering. Statutory and rule carve-outs apply: knowledgeable employees are excluded in determining ownership, and securities received by gift, bequest or involuntary transfer from a qualified purchaser are deemed owned by a qualified purchaser. A non-qualifying owner outside those carve-outs means the fund cannot rely on 3(c)(7) for that issue. The fund would have to qualify under Section 3(c)(1) instead (not more than 100 beneficial owners, 250 for a qualifying venture capital fund, and no public offering) `[VERIFY]` the application to a mixed fund, as no staff guidance was located. That changes the Item 6 selection and the Item 14 non-accredited count.

Adjacent questions that sit outside Form D (for example, whether the adviser's fee arrangements depend on investor status under the Investment Advisers Act, or what rescission or redemption mechanics the documents allow) should be named as open questions for the attorney, not analyzed here `[VERIFY]`.

Present to the attorney the decision points: whether the subscription was accepted and when; whether the investor can be rejected, redeemed or transferred; whether the exemption and the exclusion survive; and what the filing should say. Do not recommend filing until the attorney has resolved it.

## Minimum investment waivers

If the GP accepted a commitment below the stated minimum, flag the Item 11 judgment call: whether the investor is an outside investor, and whether the answer is the lowest amount below which no waiver will be granted or 0. See `form-d-items.md` Item 11.
