---
name: managing-proxy-voting
language: en
description: Structures proxy voting processes with policy application, vote execution, and disclosure requirements. Use when managing proxy votes, applying voting policies, or documenting vote rationale.
tags:
  - management
  - fund-operations
metadata:
  author: casemark
  practice_areas:
    - Fund Administration
    - Investment Operations
    - Fund Accounting
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Proxy Voting

## When To Use

- Processing incoming proxy ballots for fund portfolio holdings
- Applying the fund's proxy voting policy (or client-specific guidelines) to determine vote direction
- Documenting vote rationale for contested or non-routine proposals
- Preparing Form N-PX or other proxy vote disclosure filings
- Resolving conflicts of interest in proxy voting decisions
- Coordinating with proxy advisory services (ISS, Glass Lewis) and reconciling their recommendations against internal policy

## Inputs To Gather

- **Portfolio holdings data** — Current positions across all accounts/funds eligible to vote, with share counts as of record date
- **Proxy voting policy** — Fund-level or adviser-level voting guidelines, including standing instructions for routine vs. non-routine matters
- **Proxy materials** — Meeting notices, proxy statements (DEF 14A), ballot forms, and any supplemental issuer communications
- **Advisory service recommendations** — ISS, Glass Lewis, or other vendor vote recommendations and research reports
- **Client-specific instructions** — Any separately managed account or sub-advisory mandates with custom voting guidelines that override the standard policy
- **Conflict of interest register** — Relationships with issuers (e.g., affiliated companies, business relationships) that could create a voting conflict
- **Prior voting records** — Historical votes on the same issuer or similar proposals for consistency review

## Workflow

1. **Capture ballot universe** — Ingest proxy ballots from the custodian or proxy platform (Broadridge, ProxyEdge, ISS Proxy Exchange). Match each ballot to the correct fund/account and confirm share entitlement against the record-date position. Flag any mismatches or missing ballots.

2. **Classify proposals** — Categorize each ballot item: routine (director elections-uncontested, auditor ratification), non-routine (say-on-pay, equity plan amendments, shareholder proposals), or contested/M&A. Non-routine and contested items require individual analysis; routine items can follow standing policy.

3. **Apply voting policy** — Map each proposal to the applicable policy guideline. For items where the policy provides a clear directive (e.g., "vote FOR uncontested director slates with majority voting"), record the vote direction. For items requiring case-by-case analysis, proceed to rationale development.

4. **Screen for conflicts** — Check the conflict register. If the fund adviser has a material business relationship with the issuer, route the vote through the conflict resolution process — typically deferring to advisory service recommendation or an independent voting committee. Document the conflict and resolution path.

5. **Develop vote rationale** — For non-routine and case-by-case items, draft a concise rationale covering: the proposal substance, policy guidance (if any), advisory service recommendation, and the basis for the final vote direction. Flag any deviation from advisory service recommendations.

6. **Execute votes** — Submit votes through the proxy voting platform before the cutoff deadline. Confirm submission receipts. For split votes across accounts (e.g., different client instructions for the same issuer), execute each account separately and verify correct allocation.

7. **Reconcile and close** — After the meeting date, reconcile voted ballots against the ballot universe. Confirm no ballots were missed. Archive ballot confirmations, rationale memos, and conflict disclosures.

8. **Prepare disclosure** — Compile voting records for regulatory filings:
   - **Form N-PX** (SEC) — Annual filing due August 31 covering the 12-month period ending June 30 [VERIFY current filing deadline and period]
   - **SRD II reporting** (EU-domiciled funds) — Annual disclosure of voting policy implementation [VERIFY applicability based on fund domicile]
   - **Client reporting** — Periodic vote summaries for separately managed account clients per IMA requirements

## Output

- **Proxy voting log** — Complete record of every ballot: issuer, meeting date, proposal number, proposal description, policy classification, advisory recommendation, vote cast, and rationale (for non-routine items)
- **Conflict of interest disclosures** — Documentation of any conflicts identified and the resolution method applied
- **Exception report** — Missed ballots, late submissions, deviations from policy, and split-vote situations with explanation
- **N-PX data file** — Formatted filing data ready for EDGAR submission [VERIFY XML/inline XBRL format requirements per current SEC rules]
- **Vote summary dashboard** — Aggregate statistics: total ballots voted, votes with/against management, votes with/against advisory service, votes requiring case-by-case analysis

## Quality Checks

- Confirm 100% ballot coverage — every eligible position has a corresponding voted ballot or documented reason for non-vote (e.g., share lending, market restrictions)
- Verify vote direction matches policy for all routine items; any override is documented with rationale
- Confirm all conflict-of-interest situations were routed through the prescribed resolution process before vote execution
- Validate that no votes were submitted after the proxy cutoff deadline
- Cross-check N-PX filing data against the internal voting log for completeness and accuracy
- Ensure vote rationale memos for contested/non-routine proposals include all required elements: proposal summary, policy reference, advisory recommendation, and decision basis
- [VERIFY] Confirm compliance with SEC Rule 206(4)-6 (proxy voting by investment advisers) and any applicable state or non-US regulatory requirements based on fund registration
