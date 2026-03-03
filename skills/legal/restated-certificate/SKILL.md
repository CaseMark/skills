---
name: restated-certificate
description: Drafts an Amended and Restated Certificate of Incorporation for Delaware corporations in preferred stock financing rounds. Covers authorized capital, preferred stock rights (dividends, liquidation, conversion, anti-dilution), protective provisions, and DGCL compliance. Use when drafting charter documents, restated certificates, venture financing corporate documents, or Delaware certificate amendments from term sheets and cap tables.
---

# Amended and Restated Certificate of Incorporation

Drafts a filing-ready Amended and Restated Certificate of Incorporation for a Delaware corporation in connection with a preferred stock financing round. Delaware-specific — do not apply to other states without modification.

## Prerequisites

Collect before drafting:

1. **Term sheet** — pricing, liquidation preference multiple, anti-dilution method, protective provisions, board composition
2. **Prior Certificate** — current authorized capital, existing preferred series, unusual provisions
3. **Cap table** — shares outstanding, option pool, warrants, convertible notes
4. **Transaction documents** — SPA, IRA, voting agreement, ROFR/co-sale (for cross-reference)
5. **Registered agent** — name, physical Delaware street address (no P.O. boxes), county

## Quick Start

1. Gather all prerequisites above
2. Run pre-draft verification (cross-check term sheet against cap table and SPA)
3. Draft articles I–VII using the document skeleton
4. Verify anti-dilution formula and liquidation waterfall with sample numbers
5. Cross-check all defined terms against transaction documents
6. Confirm filing readiness with Delaware Secretary of State requirements

## Pre-Draft Verification

Extract and cross-check — flag discrepancies before drafting:

| Data Point | Source | Verify Against |
|---|---|---|
| Pre/post-money valuation | Term sheet | Cap table |
| Price per share | Term sheet | SPA, cap table math |
| Shares issued this round | Term sheet | SPA |
| Total authorized Common | Cap table | Outstanding + pool + all conversions + cushion |
| Total authorized Preferred (per series) | Term sheet | Shares issued + warrant/note conversions + anti-dilution cushion |
| Option pool size | Term sheet | Board resolutions, cap table |
| Liquidation preference multiple | Term sheet | SPA |
| Dividend rate and type | Term sheet | — |
| Anti-dilution method | Term sheet | — |
| Board composition | Term sheet | Voting agreement |

## Document Skeleton

```
AMENDED AND RESTATED CERTIFICATE OF INCORPORATION
OF [EXACT LEGAL NAME]

[Corporation] hereby certifies:

1. Original Certificate filed with the Delaware Secretary of State on [DATE].
2. This Amended and Restated Certificate has been duly adopted pursuant to
   Sections 242 and 245 of the DGCL [by board consent under §245 / by board
   and stockholder approval under §242].
3. The text of the Certificate is hereby amended and restated in its entirety
   as follows:

ARTICLE I — NAME
ARTICLE II — REGISTERED OFFICE AND AGENT
ARTICLE III — PURPOSE
ARTICLE IV — AUTHORIZED CAPITAL
ARTICLE V — PREFERRED STOCK RIGHTS
ARTICLE VI — DIRECTOR EXCULPATION
ARTICLE VII — [Additional governance as needed]

IN WITNESS WHEREOF...
[Signature block: name, title, date]
```

## Core Articles

**Article I — Name.** Must include corporate designator (Corp., Inc., etc.) per DGCL §102(a)(1). Must match across all transaction documents exactly.

**Article II — Registered Office.** Physical street address in Delaware with county. Named registered agent who has consented to serve.

**Article III — Purpose.** Standard broad clause: "any lawful act or activity for which corporations may be organized under the DGCL." Narrow only if regulatory/tax reasons require.

**Article IV — Authorized Capital.**

```
Total authorized: [X] shares
  Common Stock: [X] shares, $[0.0001] par value
  Preferred Stock: [X] shares, $[0.0001] par value
    Series Seed: [X] shares
    Series A: [X] shares
    Undesignated: [X] shares (blank check authority)
```

Common must cover: outstanding + option pool + all preferred as-converted + warrants/notes + cushion.

**Article V — Preferred Stock Rights.** Draft in this order:

| Section | Key Decisions |
|---|---|
| Dividends | Cumulative vs. non-cumulative; rate; when-as-if-declared vs. auto-accruing; series priority |
| Liquidation Preference | Preference amount (OIP × multiple + accrued dividends); pari passu vs. senior; participating vs. non-participating; cap |
| Optional Conversion | Ratio = OIP ÷ Conversion Price; initial CP = OIP; no fractional shares |
| Mandatory Conversion | Qualified IPO trigger (min proceeds + min price); majority/supermajority Preferred vote |
| Anti-Dilution | Broad-based weighted average; enumerate carve-outs |
| Voting Rights | As-converted with Common; separate class vote for protective provisions |
| Protective Provisions | Majority/supermajority Preferred consent for enumerated actions |
| Board Designation | Seats for Common, each Preferred series, independent/mutual |

See `references/DETAILS.md` for anti-dilution formula, carve-out checklist, protective provisions checklist, and liquidation waterfalls.

**Article VI — Director Exculpation.** DGCL §102(b)(7) maximum exculpation with statutory carve-outs (loyalty breach, bad faith, §174, improper personal benefit). Include future-amendment auto-update clause.

**Article VII+ — Optional Provisions.** Indemnification + mandatory advancement; D&O insurance authority; corporate opportunity waiver; forum selection (Court of Chancery); written consent/special meeting provisions.

## Pitfalls and Checks

1. **Defined terms** — define once, use consistently; cross-check against SPA/IRA/voting agreement definitions
2. **Mathematical verification** — test liquidation waterfall at multiple exit values; verify anti-dilution formula with sample down-round
3. **Cross-references** — verify all internal section references and subsection numbering
4. **DGCL compliance** — cite §§242, 245 in recitals; §102(a)(1) for name; §102(b)(7) for exculpation; §151 for stock rights
5. **Blank check preferred** — if authorized, ensure protective provisions cover future series designation
6. **Par value consistency** — match across Common and Preferred unless justified
7. **Filing readiness** — document must be executable and fileable as-is
8. **Never guess** share numbers, valuations, or pricing — flag gaps and request clarification

---

And the companion **references/DETAILS.md** (the detailed checklists, formulas, and waterfalls extracted from the original):

# Restated Certificate — Detailed References

## Anti-Dilution Formula (Broad-Based Weighted Average)

```
Adjusted CP = CP × (A + B) / (A + C)

Where:
  CP  = Conversion Price in effect immediately prior to new issuance
  A   = Shares of Common outstanding on fully-diluted, as-converted basis
  B   = Aggregate consideration received ÷ CP (shares purchasable at old price)
  C   = Number of shares actually issued in new issuance
```

## Anti-Dilution Carve-Outs Checklist

- [ ] Employee/consultant equity under board-approved plans
- [ ] Bank/equipment lender securities
- [ ] Strategic partner/vendor/customer securities (board-approved)
- [ ] Sponsored research/collaboration securities (board-approved)
- [ ] Acquisition consideration (board-approved)
- [ ] Conversion/exercise of existing convertible securities
- [ ] Stock splits, stock dividends, recapitalizations
- [ ] Securities approved by requisite Preferred holders

## Protective Provisions Checklist

- [ ] Amend certificate or bylaws adversely affecting Preferred
- [ ] Authorize/create senior or pari passu stock
- [ ] Increase/decrease authorized Preferred or Common
- [ ] Declare dividends or distributions on Common
- [ ] Redeem/repurchase Common or Preferred (except terminated-employee repurchases at cost)
- [ ] Liquidate, dissolve, or wind up
- [ ] Consummate deemed liquidation event (M&A, asset sale)
- [ ] Amend transaction documents adversely to Preferred
- [ ] Change board size
- [ ] Incur debt above board-approved thresholds
- [ ] Exclusively license or dispose of material IP

Determine whether series vote together or have separate series votes for specific matters.

## Liquidation Waterfalls

**Non-Participating:**
1. Pay Preferred liquidation preference (OIP × multiple + accrued dividends)
2. Remaining proceeds to Common only
3. Each Preferred holder may elect to convert and take Common pro rata instead

**Participating (with cap):**
1. Pay Preferred liquidation preference
2. Remaining proceeds shared pro rata among Preferred (as-converted) and Common
3. Preferred participation ceases at cap (e.g., 3× OIP); further proceeds to Common only
