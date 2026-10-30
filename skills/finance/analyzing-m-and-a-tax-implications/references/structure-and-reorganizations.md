# Structure, Elections, Reorganizations and Rollover

U.S. federal income tax rules for choosing and testing an acquisition structure. Each rule carries its citation; the URL, method and check date are in `primary-sources.md`. This file supports a draft analysis for tax adviser review; it is not a tax opinion. State, local and foreign consequences are flagged and routed, never assumed to follow the federal answer.

## Contents

1. Classify every party first
2. Taxable stock purchase versus asset purchase
3. Deemed asset purchase elections: 338(g), 338(h)(10), 336(e)
4. F reorganization pre-sale steps
5. Tax-free reorganizations under section 368
6. Continuity of interest and continuity of business enterprise
7. Rollover equity: sections 351, 721 and 368
8. Pub. L. 119-21 items that change the value of a step-up
9. Outcome labels

## 1. Classify every party first

Record for the target, each seller and the buyer: entity type under state law, federal classification (C corporation, S corporation, partnership, disregarded entity), consolidated return membership and common parent, S election date and validity evidence, and any QSub or check-the-box elections. A disregarded entity's activities are treated as a branch or division of its owner (Treas. Reg. 301.7701-2(a)), so buying all of its interests is a purchase of its assets for federal income tax purposes. The answer to "which election is available" and "whose tax is it" turns on this table; build it before any structure conclusion.

## 2. Taxable stock purchase versus asset purchase

- **Stock purchase, no election:** buyer takes a cost basis in the stock; the target keeps its inside asset basis and its attributes (subject to section 382). Sellers recognize gain on the stock.
- **Asset purchase (or purchase of all interests in a disregarded entity):** buyer takes cost basis in each asset, allocated under section 1060. A C corporation seller recognizes corporate-level gain and, if it liquidates, its shareholders recognize gain again (IRC 336(a): gain recognized on liquidating distributions as if sold at fair market value; IRC 331(a): liquidating distributions are payment in exchange for the stock). Ordinary income recapture under sections 1245 and 1250 is part of the seller's cost.
- **Converting a corporation into an LLC (taxable liquidation):** a C corporation that converts into an LLC taxed as a partnership or a disregarded entity owned by individuals is treated as liquidating: corporate-level gain on its appreciated assets as if sold at fair market value (IRC 336(a)) and shareholder-level gain on the deemed liquidating distribution (IRC 331(a)). An S corporation conversion passes the gain through to the shareholders, plus any built-in gains tax (IRC 1374). The conversion is a deemed sale for tax purposes even though no buyer exists; the entity-choice decision behind it belongs to analyzing-corporate-tax-structures.
- **Partnership target:** buying all interests from the partners is treated for the buyer as a purchase of the partnership's assets (Form 8594 instructions, citing Rev. Rul. 99-6). Section 751 and 704(c) detail goes to analyzing-partnership-tax-structures.

## 3. Deemed asset purchase elections

| Element | 338(g) | 338(h)(10) | 336(e) |
|---|---|---|---|
| Trigger | Qualified stock purchase (QSP): a corporation buys stock meeting 1504(a)(2) (80 percent vote and value) by purchase within a 12-month acquisition period (IRC 338(d)(3)) | QSP from a selling consolidated group, a selling affiliate, or the S corporation shareholders (Treas. Reg. 1.338(h)(10)-1(c)(1)) | Qualified stock disposition by a domestic corporate seller (or S corporation shareholders) of 1504(a)(2) stock to unrelated purchasers within 12 months (Treas. Reg. 1.336-1(b)) |
| Buyer must be a corporation | Yes | Yes | No |
| Who elects | Purchasing corporation alone | Purchaser and the selling consolidated group, selling affiliate or S corporation shareholders jointly on Form 8023; nonselling S shareholders must consent (1.338(h)(10)-1(c)(3)) | Seller and target by written binding agreement, plus an election statement on the seller's return (1.336-2(h)) |
| Deadline | 15th day of the 9th month beginning after the month that includes the acquisition date (IRC 338(g)(1)) | Same (1.338(h)(10)-1(c)(3)) | Agreement by the due date (with extensions) of the return for the year including the disposition date (1.336-2(h)) |
| Who bears the deemed sale tax | Old target, so the buyer economically; sellers are also taxed on their stock: two levels | Seller group or S shareholders; the stock sale itself is disregarded | Seller side, as for 338(h)(10) |

Rules that decide the answer:
- A C corporation owned by individuals, a fund partnership or other non-corporate holders is not eligible for 338(h)(10) or 336(e). The buyer's only deemed asset route is a 338(g) election, which taxes the target on the deemed sale while the sellers still pay tax on the stock sale.
- If a 338(h)(10) election is not valid, the section 338 election is also not valid (1.338(h)(10)-1(c)(5)). Never treat an invalid (h)(10) as falling back to 338(g).
- The election is irrevocable (IRC 338(g)(3); 1.338(h)(10)-1(c)(4)).
- ADSP (seller side) is the grossed-up amount realized for the recently purchased stock plus old target's liabilities, which may include the tax on the deemed sale (Treas. Reg. 1.338-4(b), (d)); AGUB (buyer side) includes new target's liabilities, including that tax where target bears it (1.338-5(e)). The tax is circular: solve by iteration or closed form, T = rate x (amount realized + other liabilities - basis) / (1 - rate) when all gain is taxed at one rate, and show convergence.
- An S corporation target that converted from C status within the 5-year recognition period owes the built-in gains tax on the deemed sale (IRC 1374(d)(7)).
- Deemed sale allocations follow the same classes as section 1060 (1.338-6); the Form 8023 instructions point to Form 8883 for the old and new target statements rather than Form 8594.

## 4. F reorganization pre-sale steps

Typical S corporation sequence: shareholders form Newco and contribute the target's stock; Newco elects QSub treatment for the target; the target converts to an LLC; the buyer purchases the LLC interests.
- The contribution and QSub election are a reorganization under section 368(a)(1)(F) when the requirements of Treas. Reg. 1.368-2(m)(1) are met. The S election continues for Newco, Newco takes a new EIN and the old target keeps its EIN (Rev. Rul. 2008-18, Situation 1).
- Related events before or after a potential F reorganization generally do not cause it to fail (1.368-2(m)(3)(ii)). The sale that follows is taxable, but the F step is not a taxable event; never report gain on it.
- Because the converted LLC is disregarded, the buyer's purchase of its interests is a purchase of assets: cost basis, 1060 allocation and Form 8594, with no 338 election needed and no risk of a broken S election defeating a 338(h)(10).
- Check before relying on the steps: the S election's validity (single class of stock, eligible shareholders), state recognition of the F reorganization and conversion, and any state entity-level tax [VERIFY by state].

## 5. Tax-free reorganizations under section 368

| Type | Statutory test (IRC 368) | Consideration limit |
|---|---|---|
| A: statutory merger | (a)(1)(A) | No statutory limit; COI and COBE apply |
| B: stock for stock | (a)(1)(B): solely voting stock; control (80 percent under 368(c)) immediately after | Any boot disqualifies |
| C: stock for assets | (a)(1)(C): substantially all properties for voting stock; liabilities assumed disregarded | (a)(2)(B): boot allowed only if at least 80 percent of all property's FMV is acquired for voting stock, counting assumed liabilities as money for that test |
| D: transfer to controlled corporation | (a)(1)(D): transferor or its shareholders control the transferee; stock distributed under 354, 355 or 356 | Statutory distribution requirement |
| F: mere change | (a)(1)(F); Treas. Reg. 1.368-2(m) | Section 4 |
| Forward triangular | (a)(2)(D): substantially all properties; no acquiring-subsidiary stock used; would qualify as an A merger into the parent | COI as for an A |
| Reverse triangular | (a)(2)(E): surviving target holds substantially all properties; former target shareholders exchange stock constituting control (80 percent) for parent voting stock | At most about 20 percent boot, because control must be acquired for voting stock |

Boot received by target shareholders is taxed under section 356 up to realized gain. A forward merger that fails section 368 is a taxable transfer of target's assets followed by liquidation: corporate-level gain (IRC 336(a)) and shareholder gain (IRC 331(a)). A reverse triangular merger that fails (a)(2)(E) is usually a taxable stock purchase, which may be a QSP.

## 6. Continuity of interest and continuity of business enterprise

- COI requires that a substantial part of the value of the target's proprietary interests be preserved in issuing corporation stock (Treas. Reg. 1.368-1(e)(1)(i)). Stock later redeemed by the issuer in connection with the deal does not count.
- **Signing date rule:** if a binding contract provides fixed consideration (the number of shares, the amount of money and the other property), value the consideration on the last business day before the first date the contract is binding (1.368-1(e)(2)(i), (iii)). Closing-date prices are irrelevant under that rule. A modification of the consideration terms resets the date, with exceptions that only protect deals that already preserved COI (1.368-1(e)(2)(ii)(B)).
- Regulatory examples: 40 percent stock and 60 percent cash preserves a substantial part (1.368-1(e)(2)(v), Example 1); stock worth 20 percent of total consideration does not (Example 7). Between those points the regulations give no bright line; treat 21 to 39 percent as Uncertain and route to tax counsel.
- COBE: the issuing corporation must continue the target's historic business or use a significant portion of its historic business assets in a business (1.368-1(d)(1)); a significant line of business is enough (1.368-1(d)(2)(ii)).

## 7. Rollover equity: sections 351, 721 and 368

- **Section 351:** no gain if property is transferred to a corporation solely for its stock and the transferors are in control (80 percent of vote and of each other class under 368(c)) immediately after (IRC 351(a)). Cash or other property received is gain up to its amount (351(b)).
- Count only persons who transfer property in the same plan. Stock already owned by a sponsor that contributes nothing new does not count. Stock issued for property of relatively small value compared with stock already owned, where the main purpose is to qualify the other transferors, is not treated as issued for property (Treas. Reg. 1.351-1(a)(1)(ii)); Example 2 there shows a transferor receiving 78 percent failing control.
- Usual fix: a newly formed holding company funded at closing by the sponsor's cash and the rolling sellers' target shares, all under one plan, so the transferor group holds 80 percent or more. Record the plan documents and timing.
- **Section 721:** contributions to a partnership are tax-free without a control test (IRC 721(a)), but a related distribution of money to the contributing partner can be a disguised sale (IRC 707(a)(2)(B)); transfers within two years are presumed a sale unless the facts and circumstances clearly establish otherwise (Treas. Reg. 1.707-3(c)). Route the 704(c), 707 and 752 detail to analyzing-partnership-tax-structures.
- **Section 368:** a rollover into the acquirer's stock in a merger is tax-deferred only if the whole transaction is a reorganization (Sections 5 and 6).

## 8. Pub. L. 119-21 items that change the value of a step-up

- **Bonus depreciation:** 100 percent additional first-year depreciation for qualified property acquired after January 19, 2025 (IRC 168(k) as amended by Pub. L. 119-21, section 70301; effective-date note in the U.S. Code). Used property qualifies only if the taxpayer or a predecessor did not use it before and it was acquired by purchase within 179(d)(2) and (3), so not from a related party or with carryover basis (Treas. Reg. 1.168(k)-2(b)(3)(iii)). building-lbo-models confirmed the same rule on 2026-10-30.
- **Section 197:** goodwill, going concern value and other section 197 intangibles acquired in a step-up transaction are amortized ratably over 15 years beginning with the month of acquisition (IRC 197(a)); anti-churning rules apply to pre-August 1993 intangibles in related-party deals (197(f)(9)).
- **Section 174A:** domestic research or experimental expenditures paid or incurred in taxable years beginning after December 31, 2024 are deductible when paid or incurred, with an election to amortize over at least 60 months (IRC 174A(a), (c)). Taxpayers may elect to deduct unamortized 2022-2024 domestic amounts in the first taxable year beginning after 2024 or ratably over two years (Pub. L. 119-21, section 70302(f)(2)); eligible small businesses could elect retroactive application (70302(f)(1)), with procedures in Rev. Proc. 2025-28. Which party gets the catch-up deduction is a purchase agreement point (consideration file, Section 6).
- **Section 163(j):** adjusted taxable income again adds back depreciation, amortization and depletion for taxable years beginning after December 31, 2024 (IRC 163(j)(8) as amended); building-lbo-models holds the modeling rules.

## 9. Outcome labels

Use these labels verbatim. Elections: **Available**, **Available with conditions**, **Not available**. Qualification tests (368 type, COI, COBE, 351 control): **Qualifies**, **Fails**, **Uncertain**. Every label carries the computed figure and the citation it rests on.
