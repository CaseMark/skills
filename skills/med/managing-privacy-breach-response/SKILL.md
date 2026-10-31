---
name: managing-privacy-breach-response
language: en
description: >
  Evaluates healthcare privacy incidents and drafts the breach determination and notice plan for
  HIPAA covered entities, business associates, 42 CFR Part 2 programs and non-HIPAA health apps.
  Places discovery from the record (first workforce or agent knowledge, imputed vendor knowledge),
  tests the encryption safe harbor and the three breach exceptions, runs the four-factor
  low-probability risk assessment, treats ransomware as a presumed breach, counts affected individuals
  by state for HHS and media thresholds, and builds a clocks table giving each notice its own trigger
  and a script-computed deadline: individual, HHS, media, vendor, BAA, law enforcement delay,
  Part 2, FTC Health Breach Notification Rule and state attorney general notices.
  Use for HIPAA breach risk assessment, 60-day clock, misdirected PHI, stolen laptop, ransomware,
  vendor breach, Part 2 breach or state breach notice. Declines to backdate discovery or write a
  fixed no-breach conclusion. Drafts for privacy officer and counsel review.
tags:
  - management
  - healthcare-compliance
  - risk
metadata:
  author: casemark
  practice_areas:
    - Healthcare Compliance
    - HIPAA
    - Healthcare Regulation
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---

# Managing Privacy Breach Response

Builds the breach determination and notification plan for one privacy incident: a source register and incident timeline, a discovery date placed from the record, the threshold, safe harbor and exception analysis, a four-factor risk assessment, affected-population counts by state, and a clocks table in which every notice has its own trigger and a script-computed deadline. It covers the HIPAA Breach Notification Rule, Part 2 records, the FTC Health Breach Notification Rule and the state statutes it has checked. The aim is an accurate, documented determination, whatever it turns out to be. Everything it produces is a draft for review by the privacy officer and counsel; it is not legal advice and it sends no notice.

## Why This Skill Exists

An impermissible use or disclosure of PHI is presumed to be a breach unless the entity demonstrates, through a documented four-factor assessment, a low probability that the PHI was compromised, and the entity carries the burden of proof (45 C.F.R. 164.402, 164.414). Most failed responses are clock and scope errors rather than judgment calls: the 60-day limit counted from the end of the investigation, a business associate's knowledge not imputed, a safe harbor claimed for a device whose password traveled with it, media notice sent or skipped on a total rather than a per-state count, or a Part 2 program or a state attorney general forgotten. Since February 16, 2026 Part 2 programs give breach notice under the same rule, and several states now run shorter clocks with different triggers. This skill keeps the regimes, triggers and deadlines apart and shows its work.

## Where Mistakes Hide

| Input / Document | What It Is Used For | Where the Error Hides |
|---|---|---|
| Incident ticket, help-desk log, supervisor email, investigation memo | Placing discovery and starting every clock | Discovery set at the date the investigation closed, the privacy officer was told or a committee met, instead of the first day any workforce member or agent (other than the wrongdoer) knew or should have known; a user request to "use the investigation end date" followed |
| Four-factor risk assessment worksheet | Deciding whether notice is required | A low-probability conclusion with one or more factors unaddressed; "no evidence of misuse" used for factor 3; a recipient attestation (factor 4) carrying the whole result; a conclusion chosen first and justified afterward |
| Encryption attestation, device management log, theft report | Unsecured-PHI determination | Safe harbor claimed when the password, PIN or recovery key was with the device, the device was on and unlocked, a copy sat in email or backup unencrypted, or the encryption was not shown to meet NIST SP 800-111 or FIPS 140-2 |
| Ransomware forensic report | Breach determination after malware | Encryption by ransomware treated as "no breach unless exfiltration is proven", contrary to the HHS presumption; log gaps ignored |
| Affected-individual list with addresses | HHS, media and state thresholds | Media notice triggered by a total of 500 or more instead of more than 500 residents of one state or jurisdiction; facility state used instead of residence; duplicates counted; FTC's "500 or more" media test confused with HIPAA's |
| Business associate agreement and vendor notice letter | Business associate timing and the covered entity's own clock | A BAA term shorter than 60 days ignored; the vendor's notice date used as the covered entity's discovery when the vendor is its agent; "independent contractor" wording treated as settling agency |
| Misdirected email, fax or chart access log (party and scope) | Exception analysis | Misdirected PHI inside the workforce treated as automatically excepted, when exception (ii) needs a recipient authorized to access PHI at the same entity and exception (i) needs good faith, scope of authority and no further use |
| Program designation, funding and record type (authority and scope) | Choosing the regimes and who must notify | Part 2 records handled only under HIPAA, or a Part 2 program that is not a covered entity told it has no duty; a non-HIPAA app put under HIPAA or under nothing instead of the FTC rule |
| Website, portal or app tracking inventory (pixels, session replay, analytics SDKs) | Deciding whether data sent to a tracking vendor was an impermissible disclosure | Portal or telehealth tracking dismissed as "just analytics" without a business associate agreement or authorization; or a breach finding built on the vacated part of HHS's bulletin (IP address plus an unauthenticated public page, Am. Hosp. Ass'n v. Becerra, N.D. Tex. June 20, 2024); discovery dated from counsel's review instead of when staff knew the data was flowing |
| State-law matrix and residence counts | State resident and attorney general notices | A state deadline shorter than 60 days, a different trigger ("determines", "detected") or an attorney general notice missed; a HIPAA deemed-compliance clause read as a full exemption |

## Ground Rules

1. **Draft only.** Every output is a draft for the privacy officer and counsel. Never state that notice was sent, that a regulator accepted a filing, or that the analysis is legal advice.
2. **Source-review gate.** Do not call any log, ticket, contract or list missing until every supplied file has been opened and searched, including scans and attachments. Classify each unresolved gap as an unknown fact, a source conflict, an unverified external lookup (for example a state statute not checked here) or a policy election (for example choosing to notify without a risk assessment).
3. **Hierarchy of authority.** Law: statute and regulation (HITECH 13402, 45 C.F.R. 164.400-414, 42 C.F.R. 2.16, 16 C.F.R. Part 318, state statutes), then agency guidance and preambles, then the BAA or QSO agreement (which can shorten a deadline but never lengthen one), then internal policy. Facts: system logs, tickets, original emails and forensic artifacts govern over incident summaries, vendor letters and memos. Name every conflict in the reconciliation table; never resolve one silently.
4. **Citation discipline.** Every date, count and factual finding carries a source locator or `[UNVERIFIED]`. Every rule carries its citation or `[VERIFY]` as listed in `references/primary-sources.md`.
5. **Discovery is a finding of fact.** Place discovery from the record under 164.404(a)(2) and show rejected candidate dates. Never backdate or postpone discovery, and never adopt a date because it gives more time.
6. **The conclusion follows the analysis.** The four factors are each addressed with evidence before any conclusion. Never draft a risk assessment to a conclusion fixed in advance ("write it up as no breach"), never omit an adverse fact, and say plainly when the evidence does not demonstrate a low probability.
7. **Presumption and burden.** An impermissible use or disclosure is a breach unless an exception or a demonstrated low probability is documented. Missing evidence counts against the low-probability finding, not for it.
8. **One clock per notice, each with its own trigger.** Individual, media, HHS, business associate, BAA, Part 2, FTC and each state's resident and attorney general notices are separate rows. Compute every date by script from its trigger date, paste the inputs and outputs, and state each date's weekday and whether it rolls (federal clocks never roll; state roll rules are `[VERIFY]` and are not applied until confirmed). The 60-day figures are outer limits; "without unreasonable delay" can require earlier notice.
9. **Regime first, never merged.** Decide the entity's role for each data flow (covered entity, business associate, Part 2 program, PHR vendor or related entity, service provider) and give each regime and state its own outcome row.
10. **Outcome vocabulary.** Use the labels in `references/breach-determination-rules.md`, Section 10, verbatim: Not an impermissible use or disclosure; Not a breach: PHI secured (encryption or destruction safe harbor); Not a breach: exception (i), (ii) or (iii) applies; Not a breach: low probability of compromise demonstrated; Presumed breach: notification required; Cannot determine. Add "provisional pending <facts>" when an unchecked fact could change the result.
11. **Minimum necessary in the draft.** Use counts, data-element names and role labels; keep names, record numbers and diagnoses out of the work product.

## Checkpoint A: Pre-Draft Intake (Mandatory)

Collect before Step 1:

1. Today's date, and the entity's role for the affected data: covered entity type, business associate, Part 2 program, PHR vendor, PHR related entity or third party service provider.
2. What happened: systems, devices or records involved, and the incident date or range.
3. Who first knew and when: each person (role and employer) who saw, reported or should have noticed the event, with dates, through to the privacy officer.
4. Data elements and record types, including Part 2 records, psychotherapy notes, SSN, financial data.
5. Security status: encryption product and standard, key or password custody, device state, every copy; or the destruction method.
6. The recipient or actor, and evidence of acquisition or viewing (forensics, access and mail logs).
7. Mitigation: return, deletion, attestations and who gave them.
8. Affected individuals: unique count, state of residence, deceased, bad contact data.
9. Contracts: BAA or QSO agreement notice terms; the vendor's notice and its date.
10. Any law enforcement request for delay: written or oral, date, official.

Defaults when an input is missing:

- Residence unknown for some individuals: count them in an "unknown residence" row; media and state rows for them are Cannot determine.
- Count uncertain: use the best estimate, flag every threshold within 10 percent of the estimate, and note that HHS accepts an estimate with a later addendum.
- Business associate agency unclear: compute the covered entity clock both ways and use the earlier date as the working deadline.
- Encryption standard or key custody not shown: treat the PHI as unsecured; the entity bears the burden of proof.
- BAA not supplied: use the 60-day regulatory limit and list the BAA as still needed; a common BAA term is shorter, so the contract may override this default.
- State not checked in `references/notification-clocks.md`: list it as `[VERIFY]` and route to legal-research; do not assume the HIPAA 60 days.

Hard stops (the named output is not produced):

- No facts from which discovery can be placed (no date on which anyone at the entity or its agent learned of the incident): produce the discovery-fact request and the timeline of what is known, and do not compute any deadline.
- The entity's role for the affected data cannot be determined: list the candidate regimes with what would settle the role, and do not state any regime outcome or deadline.
- Shifted discovery requested: a discovery date later than the record supports (for example the investigation end date), or any backdating of discovery. Decline to record it, log it as "Declined: shifted discovery date", explain 164.404(a)(2), and continue with the date the record supports and its deadlines.
- Fixed conclusion requested: a "no breach" or low-probability result set in advance, or a risk assessment that leaves out adverse facts. Decline to write it, log it as "Declined: fixed conclusion", and continue with the four-factor assessment and the conclusion the evidence supports.

## Step 1: Frame the Incident and the Regimes

Read `references/breach-determination-rules.md`, Section 1. State the incident in one line, the entity's role for each data flow, and every regime and state that will be tested. Name any mismatch between the user's framing and the role (for example a Part 2 program told it is "not HIPAA, so nothing applies").

## Step 2: Build the Source Register and Incident Timeline

Open every supplied file and fill the source register and timeline in `references/output-template.md`, Section 2. Record each person who knew, with role, employer and date. Where two sources give different dates, record both and add a reconciliation row.

## Step 3: Place Discovery

Read `references/breach-determination-rules.md`, Section 2. Fill the discovery block (`references/output-template.md`, Section 3): first knowledge by any workforce member or agent, the reasonable-diligence date, the business associate's discovery and agency analysis, and each rejected candidate date with the reason. If a discovery-date hard stop or decline applies, apply it here.

## Step 4: Run the Threshold, Safe Harbor and Exception Questions

Read `references/breach-determination-rules.md`, Sections 3 to 5 and 7 to 9. Answer in order: protected information, impermissible use or disclosure (including disclosures to tracking-technology vendors), secured or not, each exception's conditions. Test encryption against the HHS guidance, including key custody, device state and every copy. For Part 2 records apply 42 C.F.R. 2.16(b); for a non-HIPAA app apply 16 C.F.R. Part 318, which has no low-probability test.

## Step 5: Run the Four-Factor Risk Assessment

Read `references/breach-determination-rules.md`, Sections 6 and 7. Fill every row of the factor table in `references/output-template.md`, Section 5, with evidence and gaps, then weigh the factors together. For ransomware, start from the HHS presumption. Write the outcome with the verbatim label for each regime.

## Step 6: Count the Affected Population

Read `references/notification-clocks.md`, Section 4. Deduplicate, then count by state or jurisdiction of residence, unknown residence, deceased, Part 2 subset and bad contact data. Apply each threshold separately: HHS (500 or more), HIPAA media (more than 500 residents of one state or jurisdiction), FTC media (500 or more), and each state attorney general threshold.

## Step 7: Build the Clocks Table

Read `references/notification-clocks.md`, Sections 1 to 3, 5 and 7. Add one row per notice per regime per state, each with its trigger event, trigger date and source, the rule, the script-computed deadline and the days left from today. Put the BAA's contractual clock and the business associate's regulatory clock on separate rows. Flag any deadline already passed or within 5 days at the top of the output.

## Step 8: Plan Notice Content and Recipients

Read `references/notification-clocks.md`, Section 6. Check the planned content against 164.404(c) and each state's elements, list recipients and methods, including substitute notice and next of kin. Route drafting of letters to data-breach-consumer-notice.

## Step 9: Reconcile, List Gaps and Hand Off

Complete the reconciliation table, the gaps and declined requests, the hand-offs and the open items in `references/output-template.md`, Sections 9 to 12. Check every rule relied on against `references/primary-sources.md` and carry each `[VERIFY]` into the open items.

## Checkpoint B: Post-Draft Alignment

1. Does the output answer the question asked, for each regime and state, with one outcome row each?
2. Is discovery placed from the record, with rejected dates listed, and was any request to shift it declined?
3. Is each of the four factors addressed with evidence before the conclusion, and does the conclusion follow from them?
4. Does every deadline have its own trigger and a script-computed date, and are passed or imminent deadlines at the top?
5. Does any result depend on a `[VERIFY]` item, and would it change under the other reading?
6. Is anything phrased as legal advice, as a sent notice, or with unnecessary PHI? Remove it.

## Quality Audit

1. The header names the entity's role and every regime and state tested.
2. The source register covers every supplied file; nothing is called missing without a search.
3. The discovery block shows first knowledge by role and date, the business associate and agency analysis, and rejected candidate dates with reasons.
4. No discovery date was moved to an investigation end, notice or meeting date.
5. The safe harbor analysis addresses the encryption standard, key custody, device state and every copy, or the destruction method.
6. Each exception is tested condition by condition, including the recipient's authority to access PHI.
7. Each of the four factors has evidence or a stated gap, and the conclusion uses the verbatim outcome label.
8. Ransomware starts from the HHS presumption and "no evidence of exfiltration" is not treated as proof.
9. Counts are deduplicated and split by state of residence; HHS, HIPAA media, FTC media and state thresholds are applied separately.
10. Every clock row has its own trigger event and date, a script-computed deadline and days left; BAA and regulatory business associate clocks are separate rows.
11. Part 2, FTC and state regimes each have their own row when they apply, and unchecked states are `[VERIFY]`.
12. Every conflict is in the reconciliation table and every declined request is recorded with its reason.
13. Every `[VERIFY]` relied on appears in the open items with what would settle it.

## Guidelines

- Notify early when the facts are clear. Sixty days is a ceiling; holding finished notices to day 60 can itself be unreasonable delay.
- An entity may choose to notify without a risk assessment. Record that as a policy election, not as a finding that a breach occurred.
- A lost or stolen device is not "pending recovery"; the clock runs.
- A business associate's notice to the covered entity should identify each affected individual where possible and supply the content elements as they become available (164.410(c)).
- A HIPAA-compliant notice does not settle state law. Some states deem HIPAA compliance sufficient only for content, or still require attorney general notice.
- The proposed Security Rule amendments (90 FR 898) are not law as of October 30, 2026; describe them only as proposals.
- Keep the response file assembled as it happens: the burden of proof is the entity's, and the file is retained for six years.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Two plausible discovery dates | An early report was not escalated, or a vendor knew first | Show both, apply 164.404(a)(2) and the agency analysis, use the earlier as the working date, and add a reconciliation row |
| Forensic report says "no evidence of access" but logs cover only part of the window | Log retention gap or tool limits | Record the gap under factor 3; it cannot support low probability; ask forensics what the gap covers |
| Address file and forensic count disagree | Duplicates, household records, stale addresses | Count unique individuals from the source of record; list both counts and the threshold effect |
| Scanned BAA or unreadable vendor letter | Image-only file | Attempt OCR; if still unreadable, list it as unreadable and compute the regulatory clock with the contractual one marked Cannot determine |
| User insists on a later discovery date or a "no breach" result | Pressure to gain time or avoid notice | Decline that part under Ground Rules 5 and 6, record it in Section 10, and deliver the honest analysis |
| States outside the checked list | Statute not verified here | Mark `[VERIFY]`, keep the HIPAA rows, and route the state survey to legal-research |
| Law enforcement asked for delay by phone | Oral statement | Document the official and the date; delay at most 30 days unless a written statement follows; show the tolling computation as `[VERIFY]` |

## Related Skills

- data-breach-consumer-notice: drafting individual, substitute and multi-state consumer notice letters from this determination.
- hipaa-baa: drafting or amending business associate agreement breach-notice terms.
- managing-cybersecurity-healthcare: containment, forensics and incident response program work behind the facts used here.
- auditing-hipaa-compliance: program-level audit of breach notification policies, training and the breach log.
- managing-substance-abuse-confidentiality: Part 2 consent, redisclosure and QSO agreement questions outside breach notice.
- legal-research: state breach statutes not verified in this skill; no dedicated state-statute survey skill exists.

## Reference Files

- `references/breach-determination-rules.md`: regime map, discovery and imputed knowledge, safe harbor, exceptions, four factors, ransomware, Part 2, FTC rule, outcome vocabulary.
- `references/notification-clocks.md`: federal clocks table with triggers, business associate and BAA clocks, law enforcement delay, counting rules, checked state overlays, notice content, date script.
- `references/output-template.md`: deliverable sections, discovery block, factor table, population table, clocks table, reconciliation table, hand-off table.
- `references/primary-sources.md`: each authority checked with URL, method and date, and the `[VERIFY]` list.
