# Liens, Insureds, Limits and Multiple Claimants

How to build the insured-and-limits matrix, the lien matrix and the claimant matrix, and how each one shapes the offer. A demand fails most often here: it asks for money the policy cannot pay to this claimant, releases the wrong people, or makes acceptance depend on something the insurer cannot do. Sources and check dates are in `references/primary-sources.md`.

## Insured-and-limits matrix

Build one row per policy that may respond (primary auto or CGL, excess, umbrella, employer's policy, owner's policy where a permissive driver was at the wheel).

| Policy | Insurer | Named insured | Other insureds (driver, owner, employer, additional insured) | Per-person limit | Per-occurrence limit | Source (declarations page, sworn disclosure, adjuster letter) | Confirmed? |
|---|---|---|---|---|---|---|---|

Rules:
- The demand amount must fit the limit that applies to this claimant. A single injured person is usually capped at the per-person limit; derivative claims (loss of consortium, a parent's medical expense claim) commonly share that per-person limit `[VERIFY: policy language and state law]`. Demanding the per-occurrence limit for one claimant is not a demand "within limits" for that claimant.
- An adjuster's oral statement of limits is not confirmation. Use the declarations page or a statutory disclosure (Florida section 627.4137: sworn disclosure within 30 days of a written request). Where limits are unconfirmed, the first deliverable is the limits request, not the demand.
- Release every insured of the insurer to whom the demand is addressed for the claims released. Texas requires a demand that offers a full release of the insured (Garcia); California section 999.1(c) requires a complete release of the insurer's insureds; Missouri requires an unconditional release of the insureds. A narrower release (for example, the driver but not the owner insured under the same policy) counts as decided only after the memo explains the exposure left on each unreleased insured and the client gives documented release-scope authority. A user's drafting instruction is not that decision: draft the full release and record the narrower one as a judgment call. How state law treats a partial-insured demand is `[VERIFY]`.
- Excess or umbrella carriers get notice of the demand; whether a separate demand to each layer is needed is a strategy decision for counsel.

## Lien matrix

One row per payer or provider with a possible claim on the proceeds.

| Lienholder | Type | Basis (statute, plan document, notice) | Amount asserted | Source and date | Final or conditional? | Treatment in the offer |
|---|---|---|---|---|---|---|
| Medicare | Federal MSP recovery | 42 U.S.C. section 1395y(b)(2)(B); 42 C.F.R. section 411.24 | | conditional payment letter, date | conditional | claimant satisfies from proceeds |
| Medicaid | State recovery | federal Medicaid limits per Ahlborn; state statute `[VERIFY]` | | | | |
| ERISA plan | Plan reimbursement | plan document terms (McCutchen) | | | | |
| Hospital (Texas) | Tex. Prop. Code ch. 55 | section 55.007: release invalid unless the hospital is paid or is a party (McAllen) | | lien notice, date | | direct payment or escrow option |
| Hospital or provider (other states) | State lien statute | `[VERIFY: state statute and perfection]` | | | | |
| Workers' compensation carrier | Statutory subrogation | `[VERIFY: state statute]` | | | | |

Rules:
- The claimant is responsible for satisfying valid liens from the settlement proceeds. Do not make acceptance depend on the insurer obtaining a lien release, a Medicare final demand, or a provider's payoff letter within the demand window; the insurer controls none of them, and a condition it cannot perform undermines the claim that the demand was a reasonable opportunity to settle.
- Where a lienholder can pursue the insurer or defeat the release, give the insurer an option, not a condition: the letter states that the insurer may pay that lien amount directly to the lienholder, or into an escrow that pays it before the release is delivered, and that using the option is not a counteroffer. Medicare: if Medicare is not repaid within 60 days, the primary payer must reimburse Medicare even though it already paid the beneficiary, and paying the wrong party does not discharge it (42 C.F.R. section 411.24(i)). Texas hospital liens: a release of a claim covered by a hospital lien is invalid unless the charges are paid as the statute specifies or the hospital is a party to the release (Tex. Prop. Code section 55.007(a)); delivering a check naming the hospital as one of several co-payees was not payment (McAllen Hosps., L.P. v. State Farm Cnty. Mut. Ins. Co., No. 12-0983 (Tex. May 16, 2014)). Prefer direct payment or escrow over a joint check.
- Compare total asserted liens with the offer. If they approach or exceed it, flag a Critical item: the client may net little or nothing absent reductions, so client counseling and lien negotiation (hand-off to lien-resolution-summary) come before sending. Reductions available under federal or state law are `[VERIFY]` for each payer.
- California section 999.1(b) requires an offer to settle all claims within limits including satisfaction of all liens; that statutory term controls the clause's wording.
- Medicare: when a primary payment is received, the beneficiary or other party must reimburse Medicare within 60 days (42 C.F.R. section 411.24(h)); CMS may recover from any entity that received a primary payment, including an attorney. Insurers often ask for Medicare status or reporting data; supplying the beneficiary's identifiers for that purpose is a reasonable request `[VERIFY: whether it is a counteroffer under state law]`. How future medical expenses of a Medicare beneficiary are handled is a counsel decision recorded in the memo; never promise a set-aside the insurer must approve `[VERIFY: current CMS position on liability settlements]`.
- ERISA: the written plan terms control an equitable lien by agreement, and equitable doctrines cannot override clear terms; the common-fund doctrine still informs a plan that is silent on fees (US Airways, Inc. v. McCutchen, 569 U.S. 88 (2013)). Get the plan document, not the recovery vendor's letter.
- Medicaid: a state's recovery is limited by the federal anti-lien provision to the portion of the recovery for medical care (Arkansas Dep't of Health & Human Servs. v. Ahlborn, 547 U.S. 268 (2006)); Gallardo v. Marstiller, 596 U.S. 420 (2022), allows recovery from amounts for future medical care `[VERIFY: state allocation rules]`.
- Default payee: the client and the firm's trust account, subject to the lien option above and to any statute that sets payment mechanics. Where a payee line would include a lienholder, say so in the payment instructions and record the client's consent.

## Claimant matrix and multiple claimants

List every person with a potential claim against the same insureds from the same occurrence, from the crash report, the insurer's correspondence and the client's account.

| Claimant | Represented by | Injuries and specials known | Demand made? (date, amount) | Per-person exposure | Source |
|---|---|---|---|---|---|

Rules:
- If the sum of plausible claims exceeds the per-occurrence limit, the demand must deal with it. A demand that ignores known competing claimants invites the response that no prudent insurer could pay one claimant the whole occurrence limit.
- Florida section 624.155(6): an insurer facing competing third-party claims exceeding the limits is not liable beyond the limits if, within 90 days after notice of the competing claims, it files interpleader or makes the limits available to all claimants through binding arbitration. A demand to a Florida insurer in a multi-claimant case should expect that response and should not set a window that forecloses it without counsel's decision.
- Texas: an insurer may make a reasonable settlement with one of several claimants even if it reduces the limits available to the others (Soriano). Speed matters, but the demand still has to be within the per-person limit.
- Georgia: an insurer has no duty to settle one of several claims for the full limits absent a valid time-limited demand (Hughes, as described in commentary) `[VERIFY: holding on multiple claimants]`.
- Explain why the occurrence limit is actually contested: add each claimant's plausible per-person recovery and compare the sum with the per-occurrence limit. If every claimant's claim is capped at the per-person limit and the sum of those caps does not exceed the occurrence limit, there is no competition for the occurrence limit; say so.
- Options counsel may choose among, recorded as a judgment call: demand the per-person limit for the client only; propose a global settlement or mediation among all claimants; demand a specific share with a pro rata mechanism; or wait for competing claims to be quantified. Each option has a different response window and a different bad faith record.

## Client authority

Record the source of each authority (signed authority letter, engagement email, date). Documented authority for the offer amount is required before any letter is drafted; without it, stop. Documented authority for the release scope, the claims reserved, the lien approach and the payee line is required before the letter is sent; if any is missing, list it as a Critical open item that blocks sending and draft the letter on the defaults.
