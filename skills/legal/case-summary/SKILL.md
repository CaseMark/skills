---
name: case-summary
language: en
description: Summarize a large case from a pile of files. Use when a user arrives with a folder, zip, or vault of case documents and asks for a case summary, case evaluation, litigation package, or "can you summarize this case for me." Teaches the agent to ingest the corpus into a case.dev vault, OCR anything non-searchable, iteratively search the vault across the dimensions that matter (parties, timeline, injuries, liability, damages, liens), and synthesize an attorney-ready memo.
tags:
  - litigation
  - summary
  - analysis
---

# Case Summary

A user shows up with a pile of legal documents — often hundreds or thousands — and says "summarize this case." This skill is the playbook for doing that well.

The work is map-reduce, but the "map" and "reduce" happen inside your reasoning loop, not in a script. You ingest the files once, then iteratively search the vault for each dimension of the case, reading only the chunks that matter, and synthesize a memo at the end. Case.dev gives you the primitives; this skill tells you how to use them for this specific job.

## The loop

**1. Ingest.** Put the corpus into a case.dev vault so you can search and chunk it. See `references/RUNBOOK.md` for the exact commands.

**2. OCR.** Any PDF that isn't already searchable will not be indexed usefully. Kick off OCR on those first — it's asynchronous, keep moving.

**3. Inventory.** Pull the object list. Skim filenames to build a mental model: what practice area, what kinds of documents, how many of each. This is the only time you'll care about every file.

**4. Map — iterative vault search.** For each dimension of the case, query the vault with targeted questions and read the returned chunks:

- **Parties & posture** — who sued whom, in what venue, represented by whom
- **Timeline / incident facts** — what happened, when, where, witnesses
- **Injuries / harm** — what's claimed, per-body-part and per-provider
- **Treatment** — providers, dates, diagnoses, procedures, prognosis
- **Damages** — specials (billed/paid), future care, wage loss, non-economic exposure
- **Liability** — duty, breach, causation, comparative-fault evidence; admissions in depositions; admissions in discovery responses
- **Defenses raised** — pleaded affirmative defenses, liability denials
- **Liens and offsets** — Medicare/Medicaid, ERISA plan, hospital/provider liens, workers' comp, subrogation
- **Key testimony** — who said what, where it hurts, where it helps

Don't brute-force read every file. Drive the vault with focused search queries, pull the 3-10 most relevant chunks per query, cite by object name + page. See `references/SEARCH-PLAYBOOK.md` for the query patterns that work.

**5. Reduce — synthesize.** Assemble the memo using `references/OUTPUT-TEMPLATE.md`. Every claim in the memo must cite either a specific object (by filename + page/Bates) or a specific chunk returned from the vault. No citation = cut the claim or label it an assumption.

**6. Review.** Run the checklist at the bottom of this file before delivering.

## What this skill does not do

- It does not value the case. Ranges belong in the memo, but the skill doesn't encode valuation methodology — that's attorney judgment informed by jurisdiction, venue, and insurance posture.
- It does not resolve liens. It identifies them; an attorney resolves them.
- It does not replace an attorney review of the final memo. Always flag the memo as AI-generated and require sign-off.

## References

- `references/RUNBOOK.md` — the exact case.dev commands for ingest, OCR, search, inventory, chunk retrieval
- `references/SEARCH-PLAYBOOK.md` — vault-search queries tuned for each dimension above
- `references/OUTPUT-TEMPLATE.md` — memo shape and citation format

## Scale notes

- **< 20 files**: skip the vault loop; just read everything. This skill is overkill.
- **20–200 files**: one vault, one pass through the search playbook, one memo. ~1 hour of agent time.
- **200–2,000 files**: one vault, expect 40-80 targeted searches across the dimensions, checkpoint your notes as you go. Multi-hour run.
- **2,000+ files**: recommend splitting by practice-area phase (e.g., pleadings vault, medicals vault, discovery vault) and summarizing each before rolling up. Be explicit with the user about scope.

## Quality checklist

- [ ] Every file in the corpus is either searched-over or explicitly noted as out-of-scope
- [ ] Every OCR job finished (or its absence is noted in the memo)
- [ ] Parties, venue, posture correct
- [ ] Timeline continuous; gaps > 30 days flagged
- [ ] Every damages number traces to a billing document
- [ ] Every liability claim traces to admissible evidence, not just counsel argument
- [ ] Liens identified, not just mentioned
- [ ] Red flags section is honest, not decorative
- [ ] Memo is labeled AI-generated and requires attorney review
