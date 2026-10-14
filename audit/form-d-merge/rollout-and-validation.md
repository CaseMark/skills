# CD-1817 review fixes and rollout

Reviewed October 14, 2026. Companion-file publication and alias activation are release requirements.

## Publication and rollout order

1. Apply site migration 018 to the intended skills database. It creates the alias snapshot table and reuse guard.
2. Deploy the site and router infrastructure. The monorepo PR targets `preview`; validate staging before the normal reviewed production promotion. No aliases activate from the static map or from a missing target.
3. Apply migration 019 **before** merging the skills content PR. It captures actual current content and versions. The snapshots are readable, but old skill URLs and discovery remain available while the target is missing/private.
4. Merge the content PR after review. The embed workflow publishes each root, its complete tracked source manifest, and its MCP companion rows in one transaction. Failed publication aborts before retiring the deleted roots. Reference-only changes also trigger publication.
5. Apply migration 020 after confirming the new public root and all seven references are present. It finalizes archival and repoints references using its backup table.
6. Run site redirect checks and API/MCP checks below. Active aliases redirect immediately after the target becomes public; pending results are not cached across that transition.

A public root, its source files and companions commit together. Alias activation is scoped to the same domain as the target. Pending aliases do not exclude old roots from discovery. Do not bypass the reviewed merge or perform production migrations merely to test these fixes.

## Required release evidence

- `scripts/verify-skill-redirects.sh https://agentskills.legal`: old page, markdown, source, download and OG variants have one 301 and a **200 destination**. Supply `OG_IMAGE_HASH` only for a real generated metadata-image hash. Unit tests cover path mapping for arbitrary hashes; a made-up hash is not availability evidence.
- Download the target ZIP and inspect `SKILL.md` plus all seven `references/*.md` files. Verify binary files, if any, decode correctly.
- `read_skill` on `form-d`, `form-d-notice` and `form-d-exempt-offering-notice`: equal target content, aliases carry `redirected_from`, and bundle metadata includes all seven references. Read each companion and compare its bytes to GitHub.
- `resolve_skill` for `Form D`, `Reg D notice filing` and `fund Form D`: target discoverable; neither retired root appears.
- Re-run the twelve Cascade checks using the **served bundle**, with only the 27 closing-source files as inputs. Keep the answer key and generator separate. Attach output and grading evidence; prior local-folder runs do not prove publication.
- Add operating-company and XML coverage before claiming those paths validated. Fresh checks are recorded in `acceptance-2026-10-14.md`; they cover the served Cascade bundle, an operating company and both incomplete/supplemented local XML. Actual EDGAR environment submission is not claimed.

## Item 15 rubric correction

SEC Securities Act Forms C&DI 130.08 requires commissions and finder fees without limiting them to payments from offering proceeds:
https://www.sec.gov/rules-regulations/staff-guidance/compliance-disclosure-interpretations/securities-act-forms

Do not accept $0 solely because an adviser pays the fee. Report the offering fees, estimate when needed, and explain the payer. Assess a corrective amendment if a prior notice contradicts the documents. Both skill references and the source register now reflect this rule.

A corrected synthetic ZIP is attached to CD-1817. Only the answer key, its generator and a correction note changed; all 27 source files were verified byte-identical. The corrected key was rendered and inspected. The original acceptance rubric's $0 option is superseded.

## Local evidence

- PostgreSQL publication tests: full source/MCP tree, binary fidelity, stale companion retirement, rollback on failed companion insert, reference-only change detection, and all seven Form D references.
- Site middleware integration: missing/private target leaves old URLs and listings available; publication activates single-hop 301s immediately; query strings, trailing slashes, tenant boundaries and POST tracking behavior covered.
- Router alias integration and PostgreSQL catalog tests: pending targets remain discoverable, public aliases disappear from discovery, custom precedence remains, companion encoding survives export.
- Site production build and typecheck pass with dummy database URLs. These are compile checks, not a claim that production data or post-deploy routes have been validated.
- Read-only security review found no introduced blockers. No production migration, merge or deployment was performed by this fix pass. Preview configuration/publication and the complete isolated release rehearsal are recorded in `acceptance-2026-10-14.md`.

## Merge-readiness update

See `acceptance-2026-10-14.md` for the fresh 12/12 issue checks, corrected rubric, operating-company/XML results, 40/40 live redirect matrix, resolver evidence and resolved CD-1820 configuration. Migrations 018–020 now run as complete transactions. The publisher checks original snapshots through a restricted boolean readiness function before any write; 020 rejects a private or incomplete replacement. Site alias filters now preserve Neon thenables during query composition, avoiding post-activation page errors. Production execution still follows the ordered, human-reviewed release above.
