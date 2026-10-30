# Top-44 Skills Upgrade: Execution Plan

Companion to `UPGRADE-PLAYBOOK.md` and `scripts/run_top15_upgrade.py`. The playbook says *what* each skill must look like. This plan says *how* the work gets done, by whom, in what order, and how it is checked.

Status: **in progress.** Phase 0 (harness hardening) done 2026-10-30. Phase 1 pilot authored and reviewed; fix pass running. Eval and content rules from the pilot review are in Appendix A.

---

## 1. Baseline (measured 2026-10-30)

`python3 scripts/run_top15_upgrade.py status` reports **0 / 44 complete**. All 44 target directories exist. No slug is in `spec/reserved-slugs.json`.

| Vertical | Skills | Current state | Work type |
|---|---|---|---|
| legal (batches 1-3) | 14 | 36-227 lines. No trap maps, no evals. Only `demand-letter` has references (5). `disclosure-schedules` (36 lines) and `due-diligence-report` (98) are near-stubs. `disclosure-schedules` has no tags. | Rewrite controller + build bundle. `demand-letter` is light-touch (see 4.3). |
| med (batches 4-6) | 15 | 164-283 lines. All 15 already pass `validate_enrichment.py` and carry the required headings. No trap maps, no evals. `reconciling-medications` has 1 reference. | Restructure + add trap map, references, evals. Preserve what passes. |
| finance (batches 7-9) | 15 | 14 of 15 have 44-69 non-blank body lines, so the enrichment validator treats them as stubs and skips them. `auditing-aml-transactions` (128 non-blank) is the exception. The harness fails all 15 on missing required headings. | Near-full rewrite from stub. |

Repo checks at baseline: bundle tests pass (`node --test ...`, 13/13). `validate_enrichment.py` passes all 400 med skills and fails 5 finance skills (395 finance skills are stubs).

---

## 2. Gaps found in the playbook and harness (fix in Phase 0)

The harness is the gate every subagent will be judged by, so its gaps become quality gaps. These were found by reading it against the real CI in `.github/workflows/skill-qa.yml`, `scripts/validate_enrichment.py`, and `scripts/embed-skills.js`.

| # | Gap | Consequence | Fix |
|---|---|---|---|
| H1 | Harness has 11 injection patterns; `skill-qa.yml` has 28. Missing include `new instructions:`, `<system>`, `IMPORTANT: ignore`, `wget http`, `forget previous`, `developer mode`, `jailbreak`, `base64 decode`, `do anything now`, prompt-leak phrasings, hidden HTML comments. | A skill passes locally and is flagged for security review in CI. | Copy the CI list verbatim. |
| H2 | `system\s*:\s` matches ordinary prose such as "Coding system: ICD-10-CM" or "Payment system: IPPS". | Likely false positives in med revenue-cycle and finance skills. | Keep the pattern (CI uses it) but put the phrasing ban in every brief. |
| H3 | Line bands disagree. Playbook says 140-320 (Part 1), 140-300 (Part 2). Harness enforces legal 80-500 non-blank; status uses whole-file 130-350. CI counts legal body as all lines incl. blanks. | Subagents get three different targets. | One rule: **body 140-320 lines counted CI-style** for every vertical, plus med/finance **100-400 non-blank**. Error outside band. |
| H4 | No `## Troubleshooting` check, though the playbook requires it. | Silent omission. | Add to required headings for all verticals. |
| H5 | No `FILLER_PHRASES` check. One banned phrase is the natural one to write: *"When in doubt about a data point, mark with [VERIFY] rather than guessing."* | Finance rewrites fail `validate_enrichment.py` after the fact. | Import the list from `validate_enrichment.py`; quote it in briefs. |
| H6 | Frontmatter parsed with regex. Inline `tags: [a, b]` skips the legal tag check; `language` is never checked. | Bad tags slip through. | Parse with `yaml.safe_load` as CI does. Check `language: en`. |
| H7 | No `evals.json` schema check beyond counting `evals`. | Evals that cannot be run. | Require `skill_name == slug`, 3-5 entries, each with `id`, `name`, `prompt`, `expected_output`, `files`, `expected_behavior`; every `files` path exists. Schema follows the Form D suite. |
| H8 | No reference-integrity check. | Orphan reference files or `SKILL.md` pointing at files that do not exist. | Every `references/*.md` named in `SKILL.md` exists, every file in `references/` is named in `SKILL.md`, no subdirectories under `references/`. |
| H9 | Binary check is an extension list. `embed-skills.js` decides by UTF-8 decoding. | A non-UTF-8 `.md` would ship base64. | Strict UTF-8 decode of every file in the bundle. |
| H10 | Injection scan covers `SKILL.md` only. References and evals are served by the MCP adapter too. | Adversarial eval prompts are the most likely place to trip a pattern. | Scan every text file in the bundle. |
| H11 | `prompt` prints a 4-line brief and ignores the playbook it loads. | Subagents start with no context. | Emit the full brief in Appendix A, filled per slug. |
| H12 | `status` "READY" uses looser rules than `verify`. | Scorecard says READY while verify fails. | `READY` = verify has zero errors and zero warnings. |

Playbook clarifications to apply in the same commit:
- Evals schema: adopt the Form D shape (H7). Evals are authored, not executed; there is no generic runner (Form D's `check-package.py` is skill-specific). Each `expected_behavior` should be graded by a human or LLM judge later.
- Cross-domain links: name related skills by slug in plain text (`See the med skill conducting-stark-law-analysis`), never as markdown links.

---

## 3. Execution model

### 3.1 Roles

| Role | Who | Does | Does not |
|---|---|---|---|
| Orchestrator | Main session | Phase 0 fixes, dispatch, gate runs, commits, pushes, final report. Resolves cross-skill routing. | Author skill content. |
| Author agent | 1 subagent per skill | Research, write `SKILL.md`, `references/`, `evals/evals.json`, run `verify --slug`, iterate until clean. | Touch any path outside its own skill directory. Commit or push. |
| Reviewer agent | 1 subagent per batch, fresh context | Adversarial review of the batch's 5 bundles: fact-check citations and thresholds against primary sources, test trap maps against evals, check routing between sibling skills. Returns findings per skill. | See the author's reasoning. Edit files. |
| Fix agent | Author agent resumed via SendMessage | Applies reviewer findings. | Expand scope. |

Each vertical has its own checkout: legal in `/home/user/skills` (branch `claude/keen-edison-d1mcoa`), med in `/home/user/wt-med`, finance in `/home/user/wt-finance` (git worktrees of the vertical branches). Authors write only inside `skills/<domain>/<slug>/` of their vertical's checkout, so five can run in one checkout without conflicts and nothing is copied between trees. Only the orchestrator runs git.

Network limits (found in the pilot; case.dev now works around them, see Appendix A): direct fetches of most primary-source hosts are blocked in this environment, including law.cornell.edu, uscode.house.gov, ecfr.gov, leginfo, justia, qualitynet.cms.gov, cms.gov, ecqi.healthit.gov and pmc.ncbi.nlm.nih.gov. Authors verify through search excerpts restricted to the issuing body's site and label each source "excerpt-confirmed" or `[VERIFY]`. Allowing those hosts in the environment's network settings would let authors read full texts.

### 3.2 Per-batch pipeline

```
dispatch 5 author agents (parallel, background)
   └─ each: inspect → research → references → SKILL.md → evals → verify --slug (loop until 0 errors)
orchestrator: verify --batch N, validate_enrichment (med/finance), node bundle tests
dispatch 1 reviewer agent on the batch (fresh context, given only the bundles + playbook)
resume authors with their findings → re-verify
orchestrator: commit "Upgrade batch N: <name>" → push
```

Each batch is 6 agents plus fix-pass resumes, which fits the session's under-10-agents-per-workflow guideline. Batches can run as a Workflow script per batch or as Agent calls in waves.

### 3.3 Phases

| Phase | Scope | Exit criteria |
|---|---|---|
| **0. Harness hardening** | Fix H1-H12 in `scripts/run_top15_upgrade.py`; apply playbook clarifications; re-run `status` and `verify --all` to confirm it now fails for the right reasons. | Harness matches CI; baseline report regenerated. |
| **1. Pilot (3 skills)** | One per vertical: `bad-faith-demand` (legal), `managing-sepsis-bundles` (med), `building-lbo-models` (finance). Full pipeline incl. reviewer. | All 3 pass every gate; **user reviews the three bundles** and approves the pattern or adjusts the brief. |
| **2. Legal** | Batches 1 (remaining 4), 2, 3 | 14/14 legal verify clean; bundle tests green. |
| **3. Med** | Batches 4 (remaining 4), 5, 6 | 15/15 verify clean; `validate_enrichment.py --vertical med` still 400/400. |
| **4. Finance** | Batches 7, 8 (remaining 4), 9 | 15/15 verify clean; `validate_enrichment.py --vertical finance` shows the 15 targets passing. |
| **5. Cross-skill pass** | One reviewer agent over all 44 descriptions and "Related skills" sections. | No two skills claim the same trigger without routing between them. |
| **6. Close-out** | `verify --all`, full CI-equivalent runs, PR. | 44/44 READY. |

Phases 2-4 can overlap two batches at a time after the pilot if throughput matters (10 authors concurrently).

---

## 4. Vertical-specific direction

### 4.1 Legal (14)
- Tags from the 19 controlled tags only. `disclosure-schedules` needs tags added.
- Model on `form-d-exempt-offering-notice`: plain prose purpose, `## Why This Skill Exists`, `## Where Mistakes Hide` table, numbered `## Ground Rules`, Checkpoint A, Steps, Checkpoint B, Quality Audit, Guidelines, Troubleshooting, Reference Files.
- Jurisdiction-contingent law (bad-faith time-limited demand statutes, summary judgment standards, HSR thresholds which adjust every year) is `[VERIFY]` unless confirmed against a primary source with a date.
- HSR size-of-transaction thresholds and filing fees change annually. State them with the effective date checked, and instruct the agent to re-confirm.

### 4.2 Med (15)
- These already pass enrichment. Restructure, do not discard: keep the required headings, move deep criteria tables out to `references/`, add the trap map, add evals.
- Preserve `tags` and `metadata` exactly.
- Clinical thresholds, doses, and time windows each carry the guideline and year (for example Surviving Sepsis Campaign, AHA/ASA, ACC/AHA, NICHD three-tier FHR categories). Anything not confirmed against the guideline text is `[VERIFY]`.
- No patient-specific dosing presented as an order. Every output is draft for clinician review.
- Revenue-cycle skills (DRG, risk adjustment, coding denials) must not phrase as "upcoding" advice; the trap maps should focus on documentation-supported code assignment.

### 4.3 `demand-letter` (decided: light touch)
It is both a target and a gold-standard reference, and it was reworked in PR CaseMark/skills#66. Decided 2026-10-30: add a trap map, Ground Rules, Troubleshooting, Related Skills, `references/primary-sources.md`, `## Contents` headers on the four references over 100 lines, and evals. Keep the five existing references, their uppercase names, and `assets/examples/`. The harness records two exceptions for it: up to six references, and `TEMPLATE.md` serves as the output template.

### 4.4 Finance (15)
- Near-full rewrites. Preserve `tags` and `metadata`. Body must clear 100 non-blank lines and hit the 140-320 band.
- Standards cited by section: ASC 606, ASC 450, IRC sections, Treas. Reg. 1.482, OECD Transfer Pricing Guidelines, BSA/AML (31 CFR Chapter X), SSAP / ASOP for loss reserves. Rates, exemption amounts, and thresholds that change by year (estate and gift exclusion, GILTI/BEAT rates, NCTI changes) are dated or `[VERIFY]`.
- Model skills (`building-lbo-models`, `building-equity-valuation-models`) need a reconciliation table in `output-template.md`: sources and uses ties, debt schedule rolls forward, balance sheet balances.

### 4.5 Overlaps that need explicit routing
Each pair names the other in a Related Skills section and in its description's scope.

| Skill | Overlaps with | Split |
|---|---|---|
| legal `stark-law-aks-compliance` | med `conducting-stark-law-analysis`, med `conducting-false-claims-analysis` | Legal: counsel's compliance analysis and opinion. Med: provider-side operational review. |
| legal `aml-compliance-program` | finance `auditing-aml-transactions` | Program design and policy vs. transaction-level testing. |
| legal `merger-agreement`, `disclosure-schedules`, `due-diligence-report`, `hsr-filing` | each other; finance `analyzing-m-and-a-tax-implications` | Deal-document chain; tax hand-off. |
| legal `bad-faith-demand`, `demand-letter`, `coverage-opinion` | each other | Insurer-directed policy-limits demand vs. general pre-suit demand vs. coverage position. |
| finance `analyzing-corporate-tax-structures`, `analyzing-international-tax-planning`, `managing-transfer-pricing-compliance` | each other | Domestic structure vs. cross-border vs. intercompany pricing. |

---

## 5. Definition of done (per skill)

1. `python3 scripts/run_top15_upgrade.py verify --slug <slug>` returns PASS with zero warnings (hardened harness).
2. med/finance: `python3 scripts/validate_enrichment.py --vertical <v> --only-failures` does not list the slug.
3. `node --test scripts/embed-skills.test.js scripts/repair-bundles.test.js scripts/skills-catalog.test.js` passes.
4. 2-4 references, each under 100 lines or opening with `## Contents`; `output-template.md` and `primary-sources.md` always present.
5. 3-5 evals, each aimed at a named row of the trap map.
6. Reviewer findings resolved or explicitly deferred with a reason in the commit message.
7. Every `[VERIFY]` item listed in `references/primary-sources.md`.

---

## 6. Git and PR plan

Decided 2026-10-30: **one PR per vertical.**

| PR | Branch | Contents |
|---|---|---|
| Legal | `claude/keen-edison-d1mcoa` (designated branch) | Playbook, harness, this plan, Phase 0 harness fixes, batches 1-3 |
| Med | `claude/keen-edison-d1mcoa-med` | Branched from the Phase 0 commit; batches 4-6 |
| Finance | `claude/keen-edison-d1mcoa-finance` | Branched from the Phase 0 commit; batches 7-9 |

- One commit per batch on its vertical branch.
- All three branches share the Phase 0 commit, so the med and finance PRs show the harness change until the legal PR merges. Merge legal first; the other two then show only their own skills.
- The `skill-qa.yml` structural check and Claude deep review run only on `skills/legal/**`. The med and finance PRs rely on the harness, `validate_enrichment.py`, and the reviewer agents, and the PR body should say so.

---

## 7. Cost and risk

**Agent volume:** about 44 author runs, 9 batch reviewers, 1 cross-skill reviewer, plus fix-pass resumes. Roughly 55-65 agent runs. Each author run does web research and writes 4-6 files.

| Risk | Mitigation |
|---|---|
| Plausible but wrong citations, thresholds, or doses | Reviewer agent with fresh context verifies against primary sources; unconfirmed items are `[VERIFY]`; human domain review before merge (the gold standards are labeled pilot pending expert review for the same reason). |
| Agents drift outside their directory | Brief forbids it; orchestrator checks `git status` against the expected paths before each commit. |
| Injection-pattern false positives (`system:`) | H1/H2/H10; phrasing ban in brief. |
| Med skills lose content that currently passes | Brief says restructure; orchestrator diffs heading sets before and after. |
| Uniform boilerplate across 44 skills | Trap maps must be skill-specific; reviewer rejects generic rows. Filler-phrase gate. |
| Annual figures go stale | Every dated figure carries its effective date and a re-check instruction. |

---

## Appendix A: Author agent brief (template)

`python3 scripts/run_top15_upgrade.py prompt --slug <slug>` prints this block with the placeholders filled.

```
You are upgrading one skill in the CaseMark/skills repo. Work in the checkout at {repo} (the {domain} branch). Planning documents are read from /home/user/skills.

Target: skills/{domain}/{slug}   (batch {n}: {batch_name})
Current state: body {lines} lines, {refs} references, {evals} evals, trap map: {trap}
{exception}

Read first, in this order:
1. /home/user/skills/UPGRADE-PLAYBOOK.md: the binding spec.
2. /home/user/skills/UPGRADE-EXECUTION-PLAN.md sections 4 and 5: vertical rules and definition of done.
3. /home/user/skills/skills/legal/form-d-exempt-offering-notice/SKILL.md, its references/, and its evals/evals.json: the model to imitate for structure, trap map, ground rules, and evals.
4. The current {repo}/skills/{domain}/{slug}/SKILL.md. Keep whatever in it is accurate and useful.

Scope: write only inside {repo}/skills/{domain}/{slug}/. Do not run git. Do not edit any other skill or any script.

Deliverables:
- SKILL.md. Body (after frontmatter) 140-320 lines, blank lines included.
  Frontmatter: name: {slug}; language: en; description in third person ("Drafts...", "Evaluates..."), at most 1024 characters, dense with the words a user would search; {tag_rule}.
  Headings, in this order:
    # <Title>, then a 2-4 sentence purpose paragraph stating the deliverable and that it is a draft for qualified human review
    ## Why This Skill Exists
    ## Where Mistakes Hide  (one 3-column table: | Input / Document | What It Is Used For | Where the Error Hides |, at least 5 rows, every row specific to this skill)
    ## Ground Rules  (numbered: draft only; source-review gate with gap classes unknown fact / source conflict / unverified external lookup / policy election; hierarchy of authority with conflicts named, never resolved silently; citation discipline with source locator or [UNVERIFIED]; then skill-specific rules)
    ## Checkpoint A: Pre-Draft Intake (Mandatory)  (numbered inputs, default fallbacks, and explicit hard stops)
    ## Step 1: ... through ## Step N: ...  (each step says which references/ file to read and when)
    ## Checkpoint B: Post-Draft Alignment
    ## Quality Audit  (10-13 numbered checks)
    ## Guidelines
    ## Troubleshooting  (degraded, unreadable, or conflicting inputs)
    ## Related Skills  (plain-text slugs with one line each on when to hand off; never markdown links)
    ## Reference Files  (one line per file in references/)
- references/: 2-4 .md files, flat. Always output-template.md (deliverable schema, reconciliation table, hand-off table) and primary-sources.md (each authority checked, with citation, what it supports, and the date checked; then a [VERIFY] list). Add 1-2 domain-rules files. Name every file in SKILL.md as references/<file>.md. No links from one reference file to another .md file. A file over 100 lines opens with ## Contents.
- evals/evals.json:
  {"skill_name": "{slug}", "notes": "<what the suite covers>", "evals": [ 3-5 x
    {"id": 1, "name": "<kebab-case>", "prompt": "<realistic user request with the matter facts inline>",
     "expected_output": "<one-sentence summary of a passing answer>", "files": [],
     "expected_behavior": ["Must: ...", "Must: ...", "Must not: ..."],
     "trap_note": "<which trap-map row; why a weak skill fails; why the trap is live on these facts>"} ]}
  Each eval targets a named row of the trap map and plants the trap in its facts, so a weak skill fails it. If a fixture is long, put it in evals/fixtures/<name>.md and list "fixtures/<name>.md" in files.

Eval rules (from the pilot review; each one was violated at least once there):
- No eval may expect output that one of the skill's own hard stops would block. In each eval's expected_output, name the hard stops you checked.
- Prove the trap is live on the stated facts. Say why a weak skill fails in the eval's trap_note field, not in expected_output. Recompute every number with a script and put the key figures in the notes.
- No Must line may depend on a [VERIFY] fact. Confirm the fact, or make the Must require analyzing both readings.
- Must lines are single, gradable requirements: no "alternatively", no exhaustive claims ("the one criterion left"), and outcome labels taken verbatim from the skill's own vocabulary.
- Define in the prompt every quantity the arithmetic depends on ("tax EBITDA", "price paid for the target's stock").
- Check each hard stop's trigger literally against every eval prompt. If a hard stop fires when X is missing, every eval that omits X either supplies it or expects the hard-stop output.
- A Must line may not require a rule your primary-sources lists as circuit-, state- or forum-variable unless you read that rule for the eval's forum.
- The hard-stop check covers parties and documents the prompt implies but never names, such as a merger subsidiary, or a term sheet's class definition when only its relief is described.
- The eval's facts must establish every legal predicate a Must line presumes. For example, before asserting a post-signing breach, state that the representations are remade at closing.
- A "Must not" that forbids producing what the user asked for needs a hard stop or ground rule behind it. Otherwise phrase it as "not without first ...".
- Do not require [VERIFY] for a figure a sibling skill has confirmed; cite the sibling instead.

Content rules (from the pilot review):
- In every clocks or windows table, give each timed element its own trigger event. Do not assume one anchor for all of them.
- A default that a common statute or rule overrides must say so where the default is stated.
- If the description carries a search phrase naming an improper aim ("bad faith setup", "upcoding", "back-solve"), the purpose sentence states the legitimate aim, and a Ground Rule, a hard stop and an eval cover the improper one.
- The trap map includes at least one row on party, authority or scope: who can release, who is in the population, which entity's tax. In your report, list two or three high-frequency traps you considered and left out.
- Templates and exemplar branches must not contain text the skill's routing sends elsewhere. When routing changes, rewrite or remove the template branch too.
- Every skill you route to must claim that trigger in its own description or scope. If no skill does, route to legal-research (or the vertical's general research skill) and say no dedicated skill exists.
- If the routing target has not been upgraded yet, list the trigger in your report as unclaimed, so that batch's author adds it.
- Before writing [VERIFY], try the issuing body's own page, summary, FAQ or training material. Cite only documents you actually saw.

Research: verify every statute, regulation, guideline, threshold, dose, rate, and standard you cite against the primary source itself. Today is 2026-10-30. Use case.dev first; the helper `{casedev}` takes an API path and a JSON body and reads the API key itself (never print, echo, or write the key).
- Read a known page or PDF in full: `{casedev} /search/v1/contents '{"urls":["<url>"],"text":true}'`. Works for law.cornell.edu, ecfr.gov, govinfo.gov, irs.gov, state legislature PDFs, and most PDFs. It does not render JavaScript pages (qualitynet.cms.gov returns nothing); find a PDF of the same document instead.
- Find sources: `{casedev} /search/v1/search '{"query":"...","numResults":10}'`. For case law also `{casedev} /legal/v1/find '{"query":"...","numResults":10}'` (it returns mostly court documents; fetch statutes by their official URL instead).
- Verify case citations: `{casedev} /legal/v1/verify '{"text":"<citations>"}'`. Full text of an opinion: `{casedev} /legal/v1/full-text '{"url":"<url>","maxCharacters":50000,"highlightQuery":"<question>"}'`.
- Responses can exceed 100,000 characters. Pipe them through python and print only the section you need.
- In primary-sources.md, record for each authority the URL read, the method ("full text via case.dev" or "search excerpt"), and the date. Prefer the official publisher; a mirror (for example a hospital association's copy of a CMS manual) is acceptable when labeled as one. Paywalled sources such as the FASB Codification stay excerpt-based.
- WebSearch and WebFetch remain fallbacks. Mark anything still unconfirmed, jurisdiction-dependent, or year-dependent [VERIFY]. Never invent a citation.

Banned text anywhere in the bundle (the harness scans every file):
- Injection triggers from .github/workflows/skill-qa.yml. Watch for "<word> system: <value>" (write "the coding system is ICD-10-CM"), "new instructions:", "developer mode", "jailbreak", "base64 decode", "eval(", "exec(".
- The FILLER_PHRASES list in scripts/validate_enrichment.py, including "When in doubt about a data point, mark with [VERIFY] rather than guessing".

Related skills to route to: {related}

Before you finish, loop until both are clean (the harness finds your checkout itself):
  python3 /home/user/skills/scripts/run_top15_upgrade.py verify --slug {slug} --strict
  {enrichment_cmd}

Return: files written with line counts, the trap-map row names, each eval's name and the row it targets, every [VERIFY] item, and anything unresolved.
```

## Appendix B: Reviewer agent brief (template)

```
Review the five upgraded skill bundles in batch {n}: {paths}. You did not write them.
Read UPGRADE-PLAYBOOK.md and UPGRADE-EXECUTION-PLAN.md section 5 first.
For each bundle:
1. Spot-check at least 5 cited authorities, thresholds, or clinical values against primary sources by web search. Report each as confirmed, wrong (with the correct value and source), or unverifiable.
2. Is each trap-map row specific to this skill and real-world plausible? Flag generic rows.
3. Does each eval actually exercise a trap-map row, and would a weak skill fail it?
4. Do Checkpoint A hard-stops, Ground Rules, and Quality Audit agree with each other?
5. Routing: do sibling skills in this batch and the overlap table route to each other cleanly?
6. For each eval: would a skill that follows its own hard stops and ground rules pass it? Is the trap live on the stated facts? Does any Must depend on a [VERIFY] fact?
7. Does any default, clock anchor, or rule conflict with a common statute, measure specification, or standard?
8. Recompute every number in every eval with python.
Do not edit files. Return findings per skill, ranked by severity, each with file, line, problem, and fix.
```
