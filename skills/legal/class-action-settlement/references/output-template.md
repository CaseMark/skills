# Output Template

Produce the header and the seven parts in this order. Keep sentences plain; put detail in tables. Every date shows its weekday; every figure carries a source locator or `[UNVERIFIED]`.

## Contents

1. Header and source-review register
2. Part 1. Approval-readiness determination
3. Part 2. Blocking issues and judgment calls
4. Part 3. Reconciliation tables (scope, value, clocks)
5. Part 4. Draft agreement articles or redline
6. Part 5. Approval-paper inserts and Rule 23(e)(3) statement
7. Part 6. CAFA notice package
8. Part 7. Hand-offs, open items and `[VERIFY]` list

## Header

- Case caption, court and judge, case number, today's date, the side the user represents, and the preparer note: "Draft for attorney review."
- Posture: class certified (date, Rule 23(b) category) or proposed for settlement only; settlement stage (term sheet, draft agreement, preliminary approval motion, final approval motion).
- Governing law: Rule 23 and CAFA chapter 114 (federal), or the state class rule `[VERIFY]`; the controlling circuit; local rules, standing orders and the judge's procedures checked or not.
- **Source-review register**, one row per file:

| File | Type | Date | Status | Pages read | Note |
|---|---|---|---|---|---|
| name as received | complaint, certification order, term sheet, agreement draft, notice, claim form, administrator proposal, fee declaration, side letter, scheduling order | | Reviewed / Not relevant / Unreadable after attempt / Still needed | | method tried, or who supplies it |

## Part 1. Approval-readiness determination

One of these labels, used exactly:

- **Ready for attorney review**: no open item above Low.
- **Ready subject to listed confirmations**: open items are High or lower.
- **Not ready: blocking issues**: at least one Critical item is open. The draft is still included unless a hard stop in SKILL.md applies; it may not be signed or filed until each Critical item is closed.
- **Declined: hard stop**: a hard stop applies. No document of the kind requested; give the reason, what the hard stop calls for, and the compliant alternative.

Then a one-paragraph summary of the Rule 23(e)(1)(B) showing (likely approval under 23(e)(2); likely certification of the settlement class) and the weakest factor.

## Part 2. Blocking issues and judgment calls

| # | Severity | Issue | Why the court or an objector will care | Source | Recommendation and alternatives | Owner |
|---|---|---|---|---|---|---|

Severity: **Critical** (settlement class or release broader than the litigated class or the identical factual predicate without justification; value statement that presents gross or face value as class benefit; reversion, clear-sailing or kicker clause not disclosed and analyzed; coupon fee measured on face value; service award barred in the controlling circuit; objection deadline before the fee motion; CAFA notice keyed to the wrong trigger or a hearing inside the 1715(d) period; an agreement or objector payment not identified to the court; a partial-settlement bar order without a judgment-reduction credit; groups with conflicting claims under one representative without analysis); **High** (claims rate unsourced; residual-fund terms missing; cy pres recipient relationships undisclosed; another pending action not addressed); **Medium** (notice readability, claim-form burden, website contents); **Low** (clean-up). Every row ends in a recommendation and what changes under the alternative.

Judgment calls (subclasses or separate counsel, claims-made versus automatic payment, fee deferral, cy pres recipient, the length of the opt-out window beyond any floor) state the options, the recommended choice and the reason.

## Part 3. Reconciliation tables

**3A. Scope comparison**

| Element | Operative complaint (locator) | Certification order (locator) | Settlement agreement (locator) | Difference | Justification or fix |
|---|---|---|---|---|---|
| Class geography | | | | | |
| Products, accounts or conduct | | | | | |
| Class period | | | | | |
| Exclusions | | | | | |
| Released claims (by category, with factual predicate) | | | | | |
| Released parties | | | | | |
| Other pending actions whose claims are released | | | | | |

**3B. Value reconciliation** (state every input; show low, expected and high claims rates)

| Line | Amount | Source (locator) | Note |
|---|---|---|---|
| Gross settlement fund or face value of relief | | | |
| Less notice and administration | | administrator bid | |
| Less requested fees | | | |
| Less expenses | | | |
| Less service awards | | | |
| Net fund | | computed | |
| Class members / notice reach | | | |
| Claims rate (low / expected / high) | | comparable settlements named | |
| Expected valid claims | | computed | |
| Expected class payout | | computed | |
| Residue and destination (redistribution / cy pres / reversion) | | | |
| Fee / gross fund | | computed | |
| Fee / (fee + expected class payout) | | computed | |
| Coupons: face value, expected redemption rate, expected redeemed value | | | 1712(a) |

**3C. Clocks table** in the format of `references/clocks-and-cafa-notice.md`, sections 2 and 5: one row per deadline with its own trigger, rule, evidence and computed date.

**3D. Figure and identifier conflicts**

| Item | Value used | Source 1 (locator) | Source 2 (locator) | Conflict? | Value used and why |
|---|---|---|---|---|---|

## Part 4. Draft agreement articles or redline

When drafting from a term sheet, use this article order; when reviewing, redline only the affected sections and give the reason for each change.

```text
I    Recitals: litigation history, certification status, arm's-length negotiation, mediator, no admission
II   Definitions: Settlement Class, Class Period, Released Claims (tied to the factual predicate),
     Released Parties (named), Notice Date, Opt-Out Deadline, Objection Deadline, Claims Deadline,
     Effective Date, Net Settlement Fund
III  Settlement Fund: amount; funding date; escrow or qualified settlement fund (Treas. Reg. 1.468B-1);
     non-reversionary unless a stated justification is approved by the court
IV   Settlement Class certification for settlement only; reversion to prior posture if not approved
V    Relief and allocation: formula, tiers or subclasses, claim requirements, automatic payments where
     data allow, deficiency cure, second distribution, residue
VI   Notice and administration: administrator, methods, website, reach estimate, reporting of
     claims, opt-outs and objections
VII  Exclusion and objection: content required by Rule 23(e)(5)(A); deadlines keyed to the Notice Date;
     no extraneous burdens
VIII Fees, expenses and service awards: subject to court approval; motion due before the objection
     deadline; no kicker (reductions stay with the class); any clear-sailing term disclosed; timing of
     payment; service awards only where the circuit permits
IX   Release: identical factual predicate; named Released Parties; unknown-claims waiver if any,
     limited to the same predicate
X    Approval and termination: preliminary and final approval; CAFA notice by defendants within 10 days
     of filing; termination rights; any opt-out threshold identified under Rule 23(e)(3)
XI   General: no admission, Rule 408, integration, amendments with court approval, governing law,
     continuing jurisdiction, counterparts
Exhibits: notice forms, claim form, proposed preliminary approval order, proposed final judgment
```

## Part 5. Approval-paper inserts and Rule 23(e)(3) statement

This skill drafts inserts, not the motions. The preliminary approval motion itself is drafted by class-settlement-preliminary-approval, and the final approval motion and Rule 23(h) fee request by final-settlement-approval; pass these inserts to them.

- Preliminary approval motion inserts: likely-certification analysis; the four 23(e)(2) factors with the record for each; the value reconciliation from 3B; scope differences from 3A with reasons; claims-rate basis; residual-fund plan; fee terms and their timing; other pending actions; the clocks table.
- Rule 23(e)(3) statement: identify every agreement made in connection with the proposal, by date, parties and subject, including any opt-out termination agreement and any objector agreement. If the parties ask to file terms under seal, say so; the identification itself is not omitted.

## Part 6. CAFA notice package

| Official | Basis (1715(a)) | State | Address source | Date served | Method | Items enclosed (1715(b)(1)-(8)) |
|---|---|---|---|---|---|---|

Show the 10-day computation from the filing date and the earliest final approval order date under 1715(d) in the fixed format.

## Part 7. Hand-offs, open items and `[VERIFY]` list

A hand-off carries the facts the receiving workflow needs; a skill name alone is not a hand-off.

| To | When | What to pass |
|---|---|---|
| class-settlement-preliminary-approval | Agreement terms settled; the preliminary approval motion itself is to be drafted (this skill supplies only the Part 5 inserts) | Part 5 inserts, scope table, value reconciliation, clocks table, 23(e)(3) list |
| class-notice-plan | Notice methods, reach and budget need a plan | Class data sources, contact rates, administrator bids, deadlines |
| class-action-notice | Long-form and summary notices to be drafted | Class definition, release text, deadlines with triggers, fee and award requests |
| class-claim-form | A claim form is needed | Eligibility, documentation, payment tiers, claims deadline |
| final-settlement-approval | The Rule 23(h) fee, expense and service-award request is to be drafted, and the final approval motion after the notice period closes | Fee basis, value reconciliation, fee-motion filing date before the objection deadline, claims, opt-out and objection counts, CAFA declaration, responses to objections |
| attorneys-fees-motion | A lodestar cross-check is needed for the Rule 23(h) request | Hours and rates by biller, lodestar total, multiplier implied by the requested fee |
| settlement-agreement | The dispute is not a class action | Parties, claims, payment terms |

**Open items**, each with owner and next action:

| # | Open item | Gap class | Owner | Next action | Blocks signing or filing? |
|---|---|---|---|---|---|

**`[VERIFY]` list:** each statement, why it is unconfirmed, and what would settle it.

Close with: "Draft for attorney review. Not to be signed or filed until counsel confirms the controlling circuit law, the local rules and the judge's procedures, and every Critical item is closed."
