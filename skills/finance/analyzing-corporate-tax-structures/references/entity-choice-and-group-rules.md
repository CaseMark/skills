# Entity Choice, Rate Comparison and Group Rules

U.S. federal rules for comparing a C corporation with a pass-through, for the corporate penalty taxes, for consolidated groups and the corporate alternative minimum tax, and for state pass-through entity tax (PTE) elections. Each rule carries its citation and the tax year it applies to; each was checked on October 30, 2026 (see `primary-sources.md` for the URL and method). Figures marked [VERIFY] were not confirmed for the year shown. This file supports a draft for tax adviser review; it is not tax advice.

## Contents

1. Rates and thresholds by tax year
2. The two-layer comparison
3. Section 199A after Pub. L. 119-21
4. Accumulated earnings tax and personal holding company tax
5. Consolidated returns and dividends inside a group
6. Corporate alternative minimum tax
7. SALT cap and state PTE elections
8. Clocks and dates

## 1. Rates and thresholds by tax year

| Item | Figure | Tax year | Citation |
|---|---|---|---|
| Corporate income tax | 21 percent of taxable income, flat, no sunset | Taxable years beginning after Dec. 31, 2017 | IRC 11(b) |
| Top individual rate | 37 percent; MFJ and surviving spouse over $768,700, single and head of household over $640,600, married filing separately over $384,350 | 2026 | IRC 1(j)(2) (made permanent by Pub. L. 119-21); Rev. Proc. 2025-32 sec. 4.01 |
| Qualified dividends and long-term gain, top rate | 20 percent above the maximum 15 percent rate amount: MFJ and surviving spouse $613,700, head of household $579,600, married filing separately $306,850, all other individuals $545,500 | 2026 | IRC 1(h), 1(j)(5); Rev. Proc. 2025-32 sec. 4.03 |
| Section 1202 gain not excluded (28-percent rate gain) | Taxed at up to 28 percent | All years | IRC 1(h)(4), (7) |
| Net investment income tax | 3.8 percent above MAGI of $250,000 (joint) or $200,000 (other); not indexed | All years since 2013 | IRC 1411(a)(1), (b) |
| 199A threshold and phase-in end | $403,500 / $553,500 joint; $201,750 / $276,750 other; $201,775 / $276,775 married separate | 2026 | IRC 199A(e)(2), (b)(3)(B); Rev. Proc. 2025-32 sec. 4.26 |
| Built-in gains tax and passive investment income tax rate | Highest rate in IRC 11(b), so 21 percent | Same as IRC 11(b) | IRC 1374(b)(1); 1375(a) |
| Accumulated earnings tax; personal holding company tax | 20 percent | Since 2013 | IRC 531; 541 |
| Corporate AMT | 15 percent of adjusted financial statement income, less the CAMT foreign tax credit | Taxable years beginning after Dec. 31, 2022 | IRC 55(b)(2)(A) |
| 2027 inflation-adjusted brackets and thresholds | Not published when checked | 2027 | [VERIFY] |

## 2. The two-layer comparison

Every comparison computes both layers for each alternative and states the distribution policy that drives the second layer.

- **C corporation:** entity tax at 21 percent; the owner-level tax on distributed after-tax earnings at the qualified dividend rate plus NIIT where the owner's MAGI exceeds the 1411 threshold; on exit, gain on stock (possibly excluded under IRC 1202) or a second layer on an asset sale.
- **S corporation or partnership:** no entity-level federal income tax (except IRC 1374 and 1375 for S corporations with C history); owners pay at their marginal rate on their share, reduced by the IRC 199A deduction where it applies. NIIT reaches pass-through income only if the activity is passive to the owner or a trading business (IRC 1411(c)(2)). Self-employment tax on partnership income and reasonable compensation for S corporation shareholder-employees are payroll items: compute them or state that they are not modeled.
- **Break-even payout:** with entity rate t_c, owner dividend rate t_d (including NIIT) and pass-through effective rate t_p, the C corporation costs less in a year only if the share of after-tax earnings distributed, p, satisfies t_c + p(1 - t_c)t_d < t_p. Solve for p and report it; never compare 21 percent with 37 percent alone.
- **Exit:** model the expected exit (stock sale, asset sale, deemed asset sale) and its year. IRC 1202 applies only to C corporation stock issued while the issuer was a C corporation (IRC 1202(c)(1)); stock issued while an S election was in effect never becomes QSBS by revoking the election. Asset-sale mechanics and buyer elections go to analyzing-m-and-a-tax-implications.
- **State layer:** add state entity-level taxes, owner-level tax by residence and source, and any PTE election (Section 7). Never assume a state follows the federal classification or the federal 199A deduction [VERIFY by state].
- **Re-election clock:** after an S election terminates or is revoked, the corporation cannot re-elect for any taxable year before its fifth taxable year beginning after the first year the termination is effective, absent IRS consent (IRC 1362(g)).

## 3. Section 199A after Pub. L. 119-21

- Pub. L. 119-21, sec. 70105 (July 4, 2025) struck the rule that 199A did not apply to taxable years beginning after Dec. 31, 2025, so the deduction continues; the 20 percent rate is unchanged (IRC 199A(b)(2)(A)).
- The phase-in range widened from $50,000 ($100,000 joint) to $75,000 ($150,000 joint) for the wage and UBIA limit (IRC 199A(b)(3)(B)) and for the specified service trade or business (SSTB) exclusion (IRC 199A(d)(3)), for taxable years beginning after Dec. 31, 2025.
- New minimum deduction: for taxable years beginning after Dec. 31, 2025, a taxpayer with at least $1,000 of qualified business income from active businesses in which the taxpayer materially participates gets at least $400; both amounts are indexed for taxable years beginning after 2026 (IRC 199A(i)).
- Per business: the lesser of 20 percent of QBI or the greater of 50 percent of W-2 wages or 25 percent of W-2 wages plus 2.5 percent of UBIA (IRC 199A(b)(2)); the limit does not apply below the threshold amount and phases in across the range (IRC 199A(b)(3)).
- Overall cap: the deduction cannot exceed 20 percent of taxable income less net capital gain (IRC 199A(a)).
- SSTB: fields listed in IRC 1202(e)(3)(A) other than engineering and architecture, plus investing, investment management and trading (IRC 199A(d)(2)); fully excluded above the end of the phase-in range.
- Aggregation (Treas. Reg. 1.199A-4): businesses may be combined for the wage and UBIA limit only if the same person or group owns 50 percent or more of each for a majority of the year including its last day, all report on the same taxable year, none is an SSTB, and at least two of three factors are met (same or customarily combined products or services; shared facilities or centralized functions; operated in coordination or reliance) (Treas. Reg. 1.199A-4(b)(1)). Once chosen, aggregation must be reported consistently in later years and cannot be added on an amended return except for 2018 (Treas. Reg. 1.199A-4(c)(1)).
- A C corporation gets no 199A deduction; a comparison that gives the pass-through 37 percent without 199A, or gives the C corporation 21 percent without the dividend layer, is wrong.

## 4. Accumulated earnings tax and personal holding company tax

- **AET:** 20 percent of accumulated taxable income of a corporation formed or availed of to avoid shareholder income tax by accumulating earnings (IRC 531, 532(a)). The accumulated earnings credit is at least $250,000 less accumulated E&P at the prior year-end, $150,000 for corporations whose principal function is services in health, law, engineering, architecture, accounting, actuarial science, performing arts or consulting, and for mere holding or investment companies only the $250,000 minimum (IRC 535(c)). It applies regardless of the number of shareholders (IRC 532(c)) and not to a personal holding company (IRC 532(b)(1)).
- **PHC:** 20 percent of undistributed personal holding company income (IRC 541) where at least 60 percent of adjusted ordinary gross income is PHC income and, at any time in the last half of the year, more than 50 percent in value of the stock is owned directly or indirectly by five or fewer individuals (IRC 542(a)). Consolidated groups apply the income test on a consolidated basis (IRC 542(b)).
- A retention strategy (the reason a C corporation looks cheaper) needs a documented reasonable-needs plan for the AET, and a holding company with passive income needs the PHC test run each year.

## 5. Consolidated returns and dividends inside a group

- **Affiliated group:** chains of includible corporations with a common parent, where stock with at least 80 percent of total voting power and at least 80 percent of total value of each member is owned directly by other members, and the parent directly owns such stock of at least one member (IRC 1504(a)(1), (2)). Both tests, vote and value, every day the member is in the group.
- **Stock excluded from the test:** stock that is nonvoting, limited and preferred as to dividends without significant participation in growth, with redemption and liquidation rights not exceeding issue price (except a reasonable premium), and not convertible (IRC 1504(a)(4)). Convertible or participating preferred counts in the value test.
- **Not includible:** tax-exempt corporations, most insurance companies, foreign corporations, RICs and REITs, DISCs and S corporations (IRC 1504(b)).
- **Five-year rule:** a member that leaves cannot rejoin the group's consolidated return before the 61st month after its first year outside, absent a waiver (IRC 1504(a)(3)).
- **Election and continuation:** the group files a consolidated return by the due date (with extensions) of the parent's return; each member consents by joining (IRC 1501; Treas. Reg. 1.1502-75(a)(1), (b)); a group that filed must keep filing unless permitted to discontinue (Treas. Reg. 1.1502-75(a)(2)).
- **Liability:** the parent and every member during any part of the year are severally liable for the group's tax; intercompany tax-sharing agreements do not reduce that liability (Treas. Reg. 1.1502-6(a), (c)). State this to any minority investor or buyer of a member.
- **Membership dates:** a corporation becomes or ceases to be a member at the end of the day its status changes, and its tax year ends then (Treas. Reg. 1.1502-76(b)(1)(ii)(A)).
- **Intercompany transactions:** matching and acceleration rules treat members as divisions of one corporation (Treas. Reg. 1.1502-13(a)(6)). Intercompany pricing among members is handled under that regulation, not by transfer pricing analysis; cross-border or non-member intercompany pricing goes to managing-transfer-pricing-compliance.
- **Acquired losses:** losses from separate return limitation years are limited to the member's cumulative contribution to consolidated taxable income (Treas. Reg. 1.1502-21(c)); IRC 382 overlap rules apply. Loss limitations arising from an acquisition go to analyzing-m-and-a-tax-implications.
- **Dividends outside consolidation:** 100 percent DRD for qualifying dividends between members of an affiliated group (IRC 243(a)(3), (b)); 65 percent from a 20-percent owned corporation (by vote and value, ignoring 1504(a)(4) stock) (IRC 243(c)); 50 percent otherwise (IRC 243(a)(1)).

## 6. Corporate alternative minimum tax

- Applies to an "applicable corporation" (not an S corporation, RIC or REIT) whose average annual adjusted financial statement income (AFSI) for the three taxable years ending with any prior taxable year ending after Dec. 31, 2021 exceeds $1,000,000,000 (IRC 59(k)(1)(A), (B)(i)). Tentative minimum tax is 15 percent of AFSI less the CAMT foreign tax credit (IRC 55(b)(2)(A)); tax is owed only to the extent it exceeds regular tax plus BEAT (IRC 55(a)).
- **Aggregation:** solely for the status test, all AFSI of persons treated as a single employer with the corporation under IRC 52(a) or (b) is included (IRC 59(k)(1)(D)). IRC 52(a) uses the IRC 1563(a) controlled group with "more than 50 percent" in place of "at least 80 percent" (vote or value), and IRC 52(b) reaches commonly controlled partnerships and proprietorships. A corporation outside the consolidated return can still be inside the aggregation group.
- **Other status rules:** fewer than three years of existence uses the period in existence; short years are annualized; predecessors count (IRC 59(k)(1)(E)). Foreign-parented multinational groups have an additional $100,000,000 test that routes to analyzing-international-tax-planning (IRC 59(k)(1)(B)(ii), (2)).
- **Guidance status:** proposed regulations were published Sept. 13, 2024 (89 Fed. Reg. 75062); Notice 2025-27 offers an interim simplified method using $500,000,000 and $50,000,000 thresholds. Neither is final law; confirm current status before relying on either [VERIFY].
- Once a corporation is an applicable corporation it stays one unless an ownership change or a run of years below the test leads the IRS to determine otherwise (IRC 59(k)(1)(C)).

## 7. SALT cap and state PTE elections

- **SALT cap (individuals):** $40,000 for taxable years beginning in 2025, $40,400 in 2026, 101 percent of the prior year's amount for 2027 through 2029, and $10,000 from 2030; half for married filing separately; reduced by 30 percent of MAGI over $500,000 (2025) or $505,000 (2026), indexed at 101 percent through 2029 (the threshold is halved for married filing separately), but not below $10,000 (IRC 164(b)(6), (7), as amended by Pub. L. 119-21, sec. 70120). Exact 2027 to 2029 figures after rounding are [VERIFY].
- **Entity-level deduction:** income taxes a state imposes directly on a partnership or S corporation ("Specified Income Tax Payments") are deductible by the entity and are not taken into account in the owner's SALT cap (Notice 2020-75, sec. 3). The enacted IRC 164(b)(6) contains no PTE restriction. Proposed regulations promised by the notice are [VERIFY].
- **Where PTE elections misfire:**
  - Residents and nonresidents: many states tax resident owners on all income and nonresidents on state-source income only, and some limit the election or the owner credit by residence; a nonresident owner's home state may not credit the PTE tax paid to another state. Compute the federal saving owner by owner and net it against any lost home-state credit [VERIFY each state and year].
  - Owner composition: corporate, trust or tax-exempt owners may be excluded from the PTE base or the credit, which changes the payment per owner [VERIFY by state].
  - S corporation one-class rule: state laws requiring the corporation to pay or withhold tax for some shareholders are disregarded only if, counting the constructive distributions, the shares still confer identical distribution and liquidation rights; timing differences alone are allowed (Treas. Reg. 1.1361-1(l)(2)(ii)). PTE payments for some owners need equalizing distributions; check the governing provisions.
  - Sunsets and deadlines: several state regimes had sunsets tied to the federal SALT cap and have been extended or changed by 2026 legislation (secondary source: Forvis Mazars, June 10, 2026); confirm each state's election deadline, estimated payment rule and sunset for the year [VERIFY].
  - Value of the election shrinks for owners whose SALT is under the federal cap in that year; compute it year by year through 2030.

## 8. Clocks and dates

Each clock has its own trigger. Never anchor one clock to another's event.

| Clock | Trigger event | Length or test | Citation |
|---|---|---|---|
| S election timing | Start of the taxable year for which the election is made | Filed in the prior year or by the 15th day of the 3rd month of the year | IRC 1362(b) |
| S termination for an ineligible shareholder or second class | Date the corporation ceases to be a small business corporation | Effective on and after that date | IRC 1362(d)(2)(B) |
| Re-election after termination | First taxable year the termination is effective | No election before the 5th taxable year beginning after it, absent consent | IRC 1362(g) |
| Built-in gains recognition period | First day of the first taxable year for which the corporation is an S corporation (not the filing date) | 5 years | IRC 1374(d)(7)(A) |
| QSBS holding period | Acquisition of the stock (for stock received for property, the exchange date) | More than 5 years (acquired on or before July 4, 2025); 3, 4, 5 years for 50, 75, 100 percent (acquired after) | IRC 1202(a), (i)(1)(A) |
| QSBS rollover | Sale of QSBS held more than 6 months | Replacement QSBS purchased within 60 days | IRC 1045(a) |
| Consolidated membership | End of the day ownership crosses the 80 percent vote or value line | Same day | Treas. Reg. 1.1502-76(b) |
| Reconsolidation bar | First taxable year in which the corporation ceased to be a member | Not before the 61st month | IRC 1504(a)(3) |
| CAMT status | Close of each prior taxable year ending after Dec. 31, 2021 | Three-year average AFSI | IRC 59(k)(1) |
| PHC ownership test | Any time in the last half of the taxable year | More than 50 percent by value, five or fewer individuals | IRC 542(a)(2) |
| State PTE election | Each state's own deadline | [VERIFY by state and year] | State statute |
