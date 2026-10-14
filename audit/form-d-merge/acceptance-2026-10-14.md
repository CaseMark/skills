# CD-1817 merge-readiness evidence — October 14, 2026

The corrected Form D skill passed a fresh blind check of all 12 Cascade issue-detection requirements. This evaluates attorney-review drafting, not the fictional offering's eligibility or a filing submission. The evaluator received the eight-file bundle fetched from a deployed preview and only the 27 closing-source files. No answer key, generator, ticket, prior conclusions or parent history was supplied. All 26 PDFs (111 pages) and all three workbook sheets were read. The served source files and ZIP were compared byte for byte with the tracked skill files.

## Cascade checks

Evidence locations below refer to `cascade-draft.md` in the attached validation package.

| # | Required issue | Result | Actual output evidence |
|---|---|---|---|
| 1 | Non-accredited/non-QP Delacroix conflicts with the ledger and intended exclusions | PASS | Section 2 issue 2 and investor M5 reconciliation identify the signed questionnaire, Rule 502(b)/sophistication gaps and 3(c)(7) conflict; counsel must select a lawful remedy before filing. |
| 2 | Raman omitted from related persons | PASS | Sections 1/2 identify her March 2 admission from LPA/Supplement; all three Item 3 drafts include her, with vehicle-authority confirmation. |
| 3 | Cap increased more than 10% | PASS | Section 1 computes $400m to $500m = 25% and identifies an immediate change-driven amendment independently of the annual date. |
| 4 | Saturday acceptance controls Parallel deadline | PASS | Section 1 uses October 3, Sunday October 18 raw day 15, and Monday October 19 due date; rejects the ledger's October 5 date. |
| 5 | Saguaro accepted commitment differs from ledger | PASS | Section 2 issue 6 uses $12m instead of $15m; corrected main sales $324.75m and program $382.75m; commission difference $45,000. |
| 6 | Arizona placement-agent registration gap | PASS | Section 2 issue 7 and blue-sky handoff identify AZ solicitation against the agent exhibit and request registration/exemption evidence. |
| 7 | Raman bad-actor questionnaire missing | PASS | Section 5 explicitly identifies missing diligence for the newly admitted person. |
| 8 | Ofori Yes answer needs actual-order review | PASS | Section 5 identifies Washington order S-21-3318-22-CO01 and directs counsel review; neither automatic clearance nor disqualification is asserted. |
| 9 | Agent certification stale | PASS | Section 5 identifies September 22, 2025 certification and missing required 2026 closing bring-downs. |
| 10 | Two new issuers lack EDGAR access | PASS | Section 1 prioritizes separate Form ID/account/delegation work against October 15/19 deadlines. Main CIK no-match and unconfirmed accession are flagged rather than treated as valid. |
| 11 | Feeder capital/Reg S double counting | PASS | Sections 2/3 count the feeder once in Main, report $15m/one purchaser for feeder Reg D with $30m Reg S separated, and reconcile program capacity. |
| 12 | Annual amendment cannot delay earlier triggers | PASS | Section 1 identifies conditional November 18 anniversary, immediate triggers and reset following an actual amendment. |

All three drafts use Items 1–16 and signature fields, citations/confidence, six output sections and permitted clarification fields. Adviser-paid commissions are included: Main $2,692,500, Parallel $570,000, Feeder $225,000, with estimates and payer clarification. Missing authority, diligence, real identifiers and source documents remain explicit blockers for a real filing.

## Rubric corrections

The original answer key is not controlling authority. The version-2 corrected synthetic package preserves all 27 source files and corrects these expectations against [SEC Securities Act Forms interpretations 130.03 and 130.06–130.08](https://www.sec.gov/rules-regulations/staff-guidance/corporation-finance-interpretations/securities-act-forms), reviewed October 14:

- Unlimited minimum-investment waiver discretion calls for zero; a past small subscription does not establish a binding floor. Confirm each vehicle's governing policy. Item 11 has no clarification field.
- Historical purchasers and sales are not automatically removed after withdrawal or redemption. A claim that an accepted transaction never took legal effect needs counsel's analysis.
- Include offering commissions even when the adviser pays them. Private-equity Item 5 uses revenue, and an unconfirmed previous NAV election does not establish the current issuer's election.

These corrections were made after the blind output and checked against primary sources. The skill already states the waiver-floor and historical-count rules; no answer-key information was sent to the evaluator. The twelve issue checks above are separately evidenced.

## Operating-company and XML checks

A second independent evaluator used the same served bundle and a separate synthetic operating-company file. It correctly used September 30 acceptance and October 15 deadline, $1.2m sold/$2.8m remaining, one non-accredited purchaser, the Rule 502(b) information gap, waivable-minimum issue, commissions and $100,000 related-person proceeds. Missing broker/authority/diligence/access information remains explicit.

The actual SEC archive linked from its technical-specifications page was downloaded through the Codex in-app browser. The index labels Version 12 (September 2021); included specification is Version 13 (March 2025), and the root XSD comment is X0808. The unmodified root XSD and both state-code includes controlled local validation.

- Incomplete case: actual partial TEST XML fails XSD validation for missing required broker/signature data. Failure and original artifact are retained; facts were not invented to force success.
- Supplemented case: a separate, explicitly synthetic source record supplies local-schema test broker/contact/signature values. The resulting TEST XML passes that same unmodified XSD with zero errors. Synthetic signature/credentials have no real authority and are never to be submitted.
- No EDGAR TEST or LIVE connection/submission occurred. Local XSD success does not establish EDGAR business-rule acceptance or legal compliance. Real EDGAR validation remains part of an authorized filing engagement.

## Infrastructure evidence

- Skills publisher/catalog: 9 tests pass; CI publication, structural validation and code review are green at `10022aa47fa8c73bf88e5a67162e6900414cd59d` before this evidence-only commit.
- Site: 20 targeted tests and typecheck pass; both Vercel previews are READY at `abbedf4b9fe7996ed5d9d20db49a0fe51a3dadfc`. Real Neon thenable behavior, restricted publisher permissions, failed-snapshot rollback and complete-bundle retirement are covered.
- Router: 111 prior targeted tests and all PR checks remain green at `5cd66019e981d4b9afe7b5db2d826ff80112d532`. Read-only checks against the isolated Neon branch confirm both aliases, seven companions, fourteen companion aliases and canonical rank 1 for all three required resolver queries.
- Live site: 40/40 page/markdown/source/download/image/query/slash redirect checks reach a 200 destination in one hop; ordinary slash controls remain 308. Original v5 URLs returned 200 before publication. Archive/supersession rendering and the real metadata image URL were also checked.
- The actual generated metadata image has a query cache token rather than the hypothetical path suffix supported by the helper. Vercel normalizes bare empty query tokens; ordinary query parameters were preserved in the 40-check matrix. No invented metadata suffix was counted as availability evidence.
- Clone configuration blocker CD-1820 is resolved with branch-scoped preview connections to isolated Neon branch `br-autumn-dew-akrvhg6f` in project `damp-surf-64851057`; no production credentials copied. CLI fallback used the user's existing authenticated credentials after the connector denied environment access.
- Migrations 018 and 019 ran transactionally on that isolated copy and preserved both original v5 snapshots. Migration 020's rollback/preconditions/reference backup, deduplication and idempotence were tested on disposable PostgreSQL. No production migration or content publication occurred.
- Final read-only security review found no introduced blockers.

## Reviewed release order

This is ready for human review and an ordered merge, not an instruction to merge content first. Apply 018 to the intended database; release site/router infrastructure (monorepo through `preview`, then the reviewed production promotion); run transactional 019 before content merge; verify both original snapshots/readiness checks; merge content; verify complete public source/MCP bundle; run transactional 020; repeat live production smoke checks. The publisher refuses reserved-root retirement without its snapshots.

The repository requires a human reviewer to approve/merge. The Linear team has no In Review status; use its available review/staging workflow without inventing a status. The isolated acceptance branch remains attached to the clone preview for review; retain it while those credentials are configured.
