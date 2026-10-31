# Arrangement Review Rules

Operational rules for a compliance department's review of physician financial arrangements under the physician self-referral law (42 U.S.C. 1395nn; 42 C.F.R. 411.350-411.389). Regulation text was read in the current eCFR on 2026-10-30. Citations are to 42 C.F.R. unless a U.S.C. section is named. This file says what to look for in the files and records; the legal element tables, stand-in-the-shoes analysis and exception opinions belong to stark-law-aks-compliance, which confirmed the same regulations on the same date.

## Contents

1. Scope and party map
2. Inventory build and reconciliation
3. Document tests by arrangement type
4. Performance tests: as written, as paid, as performed
5. FMV and commercial reasonableness file
6. Group practice compensation plans
7. Referral-tracking controls
8. Escalation triggers

## 1. Scope and party map

- **Physician party.** The physician, any immediate family member (411.351: spouse; birth or adoptive parent, child or sibling; step-relatives; in-laws; grandparents and grandchildren and their spouses), and any entity either of them owns or is paid through (a practice, an LLC that owns real estate, a management company). A lease paid to an LLC owned by a physician's spouse is a physician arrangement and belongs in the inventory. The spouse's LLC is not a "physician organization" (411.351 limits that term to a physician, a physician practice or a group practice), so whether the arrangement is direct or indirect is counsel's call; record the ownership facts and send the question to stark-law-aks-compliance.
- **Entity party.** Every legal entity in the system that furnishes designated health services (DHS) or bills for them: each hospital, each provider-based or freestanding imaging, lab or therapy entity, home health and DME entities. A contract signed by a foundation, a medical group subsidiary or a real estate subsidiary still needs review for whether it is an indirect arrangement; send that question to counsel.
- **Direction of payment.** Review payments in both directions: entity to physician (directorships, call coverage, employment, rent the hospital pays as tenant) and physician to entity (rent, equipment, purchased services, staff the physician should be paying for).
- **Non-physician referral sources** (nurse practitioners, marketers, other hospitals) are outside this review's Stark scope; list them and route to conducting-anti-kickback-analysis.

## 2. Inventory build and reconciliation

The master contract list is a starting point, not the population. Reconcile it against independent records and add every arrangement found.

| Independent source | What it reveals | Typical arrangement missing from the master list |
|---|---|---|
| Accounts payable vendor master and payment register (filter: physician names, NPIs, tax IDs, practices, LLCs disclosed on conflict forms) | Payments to physicians or their entities | Directorships signed by a department head; rent the hospital pays to a physician-owned LLC; one-off honoraria |
| Payroll and W-2 register | Employed physicians and stipends paid through payroll | Administrative stipends added to employment pay without a writing |
| Rent roll, accounts receivable, real estate lease roster, facilities space map, badge and room-scheduling data | Space and equipment the entity leases to physicians | Expired leases still invoiced; extra suites or rooms occupied without a lease; free storage or parking |
| Staffing rosters and shared-services cost allocations | Staff, scribes, IT, billing or supplies provided to a practice | Free services, which are remuneration in kind (411.351 definition of remuneration) |
| Nonmonetary compensation and gift logs, event invoices, CME sponsorship records | Items and services given to physicians | Meals, tickets and gifts never logged |
| Conflict-of-interest questionnaires, medical staff roster | Family relationships and ownership | Arrangements with immediate family members |

Personal services arrangements: where a physician has more than one services arrangement with the entity, 411.357(d)(1)(ii) is met if the agreements incorporate each other by reference or cross-reference "a master list of contracts that is maintained and updated centrally and is available for review by the Secretary upon request", maintained "in a manner that preserves the historical record of contracts." An arrangement missing from the master list therefore is a documentation gap with legal weight, not only a housekeeping item.

## 3. Document tests by arrangement type

Test the executed copy, not the database fields. Record signer, signature date for each party, effective date, expiration date, renewal or holdover language, and what is specified.

| Arrangement | Writing and signature | Term and expiry | What the writing must specify | Watch for |
|---|---|---|---|---|
| Office space, entity as lessor or lessee (411.357(a)) | Signed by the parties | At least 1 year; holdover only on the same terms ((a)(7)) | The premises | Space occupied beyond the specified premises; lessor use of the space (exclusive use, (a)(3)); percentage or per-click rent on lessor-referred patients ((a)(5)) |
| Equipment (411.357(b)) | Signed | At least 1 year; holdover ((b)(6)) | The equipment | Equipment used off-schedule or by the lessor; per-use charges on lessor-referred patients |
| Personal services, including medical directorships and call coverage (411.357(d)(1)) | Signed | At least 1 year; holdover ((d)(1)(vii)) | The services; all services or master list ((d)(1)(ii)) | Compensation over FMV; services beyond what is reasonable and necessary ((d)(1)(iii)); duplicate directorships |
| Fair market value compensation (411.357(l)) | Signed; items, compensation and timeframe specified | Any length; renewable any number of times if terms and compensation do not change; no more than one arrangement for the same items in a year ((l)(2)) | Items, services, space or equipment; compensation; timeframe | Requires that the arrangement not violate the AKS ((l)(5)): that question goes to counsel |
| Bona fide employment (411.357(c)) | No writing required by the exception | None | Identifiable services | Productivity pay on DHS the physician orders rather than personally performs ((c)(4) permits only personally performed) |
| Limited remuneration (411.357(z)) | No writing, signature or set-in-advance requirement | Calendar-year aggregate cap | Items or services the physician provides to the entity | Cap applies per calendar year; FMV, commercial reasonableness and no volume or value still required |
| Physician recruitment by a hospital (411.357(e)) | Signed by the hospital and the physician; also by the practice when money flows through a practice that does not pass all of it to the physician ((e)(4)(i)) | Per the agreement | The recruitment payments and conditions | Not conditioned on referrals; physician free to hold privileges elsewhere; relocation test; income-guarantee costs allocated by the practice not above actual incremental costs ((e)(4)(iii)); records of actual costs and pass-through amounts kept at least 6 years ((e)(4)(iv)) |
| Retention payments in underserved areas (411.357(t)) | Bona fide firm written outside offer, or the physician's written certification under (t)(2) | Not more than once every 5 years with the same physician ((t)(3)(ii)) | Payment amount, capped by (t)(1)(iv) | Area or patient-population qualification; amount and terms not altered during the term in a way that reflects referrals |
| Timeshare (411.357(y)) | Signed; specifies premises, equipment, personnel, items, supplies and services | Any | What is covered and the schedule | Used predominantly for evaluation and management services; equipment in the same building and not advanced imaging, radiation therapy or non-waived lab equipment; no possessory leasehold interest ((y)(9)); a timeshare used as exclusive space goes to counsel for review as a lease under 411.357(a) or (l) |

Writing by collection of documents (411.354(e)(2)) and electronic signatures (411.354(e)(3)) count, but only documents that existed at the time. The 90-day writing and signature rule (411.354(e)(4)) and its limits are in `references/limits-and-clocks.md`.

## 4. Performance tests: as written, as paid, as performed

For every arrangement and every period in which terms changed, build three columns.

- **As written:** the rate, cap, schedule, premises or equipment in the executed document and signed amendments.
- **As paid:** the AP, payroll or AR records for the period, by month.
- **As performed:** duty logs, timesheets, call schedules and call logs, meeting minutes and deliverables; room and equipment scheduling, badge or access data, facilities records.

Rules:

- A payment that differs from the written rate is a discrepancy even when it is below a contractual cap. A contract that pays per documented hour is not met by a fixed monthly amount paid without logs.
- CMS states that parties that detect and correct administrative or operational errors or payment discrepancies while the arrangement is ongoing are not "turning back the clock", and gives the example of a medical director paid $150 an hour against a written $140 (85 FR 77581-77582). Whether a discrepancy was unintended is a fact counsel decides; record what the records show.
- After expiration or termination, discrepancies must be reconciled within 90 consecutive calendar days and only where the arrangement otherwise fully complies (411.353(h)). Once a relationship has ended, parties cannot retroactively cure noncompliance by recovering or repaying compensation (85 FR 77581).
- An intended change in rate is a modification, not a discrepancy: it must meet 411.354(d)(1)(ii) (confirmed in stark-law-aks-compliance).
- Logs: a medical directorship without duty logs is not by itself a regulatory element failure, but without them the file cannot show services actually furnished, FMV for services actually provided, or that aggregate services were reasonable and necessary. OIG's General Compliance Program Guidance (Nov. 2023, section V.D) says arrangement tracking should "account for service and activity logs and use of lease space and equipment to ensure consistency with contract terms." Logs prepared after the fact are labeled with their actual preparation date and are never presented as contemporaneous.
- Call coverage: compare call stipends paid with the published call schedule and call logs, day by day. A stipend paid for a day the physician was not scheduled, swapped off, or did not respond is a discrepancy, and a per-day rate paid for unrestricted "availability" with no call obligation is a review item for FMV and commercial reasonableness.
- Space and equipment: compare the premises or equipment specified with what is occupied or used. Extra rooms, extra sessions, storage, parking or staff at no charge are remuneration and need their own exception.

## 5. FMV and commercial reasonableness file

- Check that the file holds a valuation or other FMV support whose scope matches the arrangement as written (duties, hours, specialty, space type, square footage) and whose date precedes the compensation it supports.
- Check for a separate statement of business need or commercial reasonableness (411.351 definition; 85 FR 77530 treats FMV, commercial reasonableness and volume or value as separate requirements, as confirmed in stark-law-aks-compliance).
- A refresh interval for FMV support (for example every two or three years, or at each renewal or rate change) is a **policy election** of the organization, not a regulatory rule. State the policy the organization uses; if none, report "No FMV refresh policy" as a control gap. Holdovers must continue to satisfy the exception, including FMV ((a)(7)(iii), (b)(6)(iii), (d)(1)(vii)(C)), so a long holdover on an old valuation is a review item.
- Compensation above a survey percentile is not a violation by itself; it is a reason to confirm the valuation addressed it.

## 6. Group practice compensation plans

Applies only where the practice qualifies as a group practice under 411.352 (a counsel conclusion; record its source). Members may not be paid directly or indirectly based on the volume or value of their referrals (411.352(g)), except:

- **Overall profits** (411.352(i)(1)): profits from all DHS of the group or of a component of at least five physicians, divided in a reasonable and verifiable manner. Deemed acceptable if divided per capita, by the distribution of non-DHS revenue, or where DHS revenue is under 5 percent of group revenue and each physician's share is 5 percent or less of his or her total compensation.
- **Productivity bonus** (411.352(i)(2)): based on services the physician personally performed or services "incident to" them. Deemed acceptable if based on total patient encounters or RVUs personally performed, on non-DHS services, or under the same 5 percent test.
- **Supporting documentation** of the method and resulting amounts must be available to the Secretary on request (411.352(i)(4)).

Review items: a bonus line computed from technical-component or facility revenue for tests the physician orders; DHS profits split by service line or by site in a component smaller than five physicians; a plan whose written method differs from what payroll calculated. In-office ancillary services (411.355(b)) for the group's own DHS depend on group practice status, so a plan defect can affect every in-office DHS referral; escalate.

## 7. Referral-tracking controls

Referral data has legitimate uses (network adequacy, patient access, quality, a directed referral requirement that meets 411.354(d)(4)). The review checks where the data goes.

- Volume or value: compensation to a physician takes referrals into account only if the formula includes the physician's referrals as a variable that correlates positively with pay (411.354(d)(5)(i)). A dashboard whose output feeds a bonus, a rate, a tier or a stipend puts referrals into the formula.
- Directed referrals: neither the existence nor the amount of compensation may be contingent on the number or value of referrals to a particular provider; a requirement may use an established percentage (411.354(d)(4)(vi); 85 FR 77539-77540). Renewal or termination tied to referral counts fails this.
- Intent: dashboards and pro formas that track a physician's referrals are AKS intent evidence (stark-law-aks-compliance); the AKS analysis is counsel's.
- Controls to test: who can see physician-level referral data; whether it appears in compensation committee, contracting or renewal materials; whether access is logged; whether policy separates referral reporting from compensation decisions.

## 8. Escalation triggers

Escalate to counsel (label "Potential noncompliance: escalate to counsel") when any of these appears; do not decide the legal question:

- A payment period with no signed writing after the 90-day window closed, or with free space, staff or services.
- A rate or formula change not in writing before the services, or applied retroactively.
- A holdover on changed terms, or with FMV support that no longer covers the arrangement.
- Payments above the written terms after expiration or termination, or not reconciled within 90 days.
- Nonmonetary compensation over the calendar-year limit outside the 411.357(k)(3) conditions, or any cash or cash equivalent given as a gift.
- A compensation formula, bonus, renewal or termination that uses referral data.
- A group practice bonus or profit share outside 411.352(i).
- Recruitment money without the required signatures or cost and pass-through records; a retention payment repeated within 5 years; a timeshare used as exclusive space or for excluded equipment.
- Call stipends paid for days not scheduled or not worked, unless counsel confirms an unintended error corrected during the term.
