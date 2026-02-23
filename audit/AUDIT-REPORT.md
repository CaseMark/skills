# Legal Skills DB Audit Report

**Date:** 2026-02-23
**Source:** Neon pgvector DB (agentskills-legal)
**Total skills:** 830 (829 public, 1 draft)

## Database Structure

### Hierarchy

| Level | Count | What's here |
|-------|-------|-------------|
| 0 (root) | 62 | Practice area hubs + standalone skills + reference/tone skills |
| 1 | 82 | Sub-practice hubs (Appeals, Commercial Litigation, Corporate Finance, etc.) |
| 2 | 682 | **The actual product** — forms, templates, document generators |
| 3 | 4 | Reference materials attached to specific forms |

### Skill Types

| Type | Count |
|------|-------|
| form | 741 |
| root | 77 |
| reference | 10 |
| user | 2 |

### Content Size Distribution

| Size | Count | Assessment |
|------|-------|------------|
| <5K chars | 128 | Healthy — mostly hub stubs and reference skills |
| 5-10K | 235 | Healthy |
| 10-20K | 231 | Borderline — many could be trimmed |
| 20-30K | 105 | Too long — these are 400-600 line skills |
| 30-40K | 77 | Way too long |
| 40K+ | 53 | Massive — 10K+ tokens each. These hurt agent context. |

**235 skills (28%) are over 20K chars and need trimming or splitting.**

### Embedding Coverage

- 774 skills have embeddings
- **56 skills have NO embeddings** — invisible to semantic search
- All 56 missing-embedding skills are either new root skills or forms that were ingested without the embedding step

### Practice Area Coverage

| Practice Area | Skills |
|---------------|--------|
| Litigation | 318 |
| Transactional | 220 |
| Regulatory | 207 |
| Corporate | 140 |
| Real Estate | 4 |
| Bankruptcy | 3 |
| IP / Employment / Criminal | 1 each |

---

## Problem 1: Duplicate Clusters (49 pairs above 0.85 similarity)

### Critical Duplicates (>0.90 similarity — essentially the same skill twice)

| Skill A | Skill B | Similarity | Action |
|---------|---------|-----------|--------|
| Deposition Summary Page-line | Deposition Summaries Deep Analysis | 0.946 | Merge → single depo summary skill |
| Corporate: Securities & Capital Markets | Regulatory: Securities & Capital Markets | 0.938 | Merge → one hub |
| Environmental Indemnity Agreement | Environmental Indemnity Agreement (Transactional) | 0.937 | Merge |
| Term Loan Agreement (Corporate Finance) | Loan Agreement (Term) | 0.931 | Merge |
| Discovery Summarization | Discovery Document Summarization | 0.927 | Merge → single discovery summary skill |
| Arbitration Agreement (Employment) | Employee Arbitration Agreement | 0.924 | Merge |
| Corporate: Mergers & Acquisitions | Transactional: Mergers & Acquisitions | 0.921 | Merge → one hub |
| Police Report Summaries | Police/Incident Report Summary | 0.920 | Merge |
| Class Action Motion Final Settlement | Class Action Motion Preliminary Settlement | 0.917 | **Keep both** — these are distinct legal motions |
| Settlement Demand Letter (PI) | Demand Letter (PI) | 0.916 | Merge |

### Cluster: Discovery Summarization (4 skills → should be 1)

| Slug | Name | Chars |
|------|------|-------|
| discovery-summarization | Discovery Summarization | 4,416 |
| litigation-discovery-document-summarization | Discovery Document Summarization | 3,639 |
| discovery-document-summaries | Discovery Document Summaries | 5,700 |
| discovery-response-summary | Discovery response | 6,337 |

**Action:** Merge into one skill: `discovery-summarization`. Combine the best instructions from each.

### Cluster: Settlement Summaries (4 skills → should be 1-2)

| Slug | Name | Chars |
|------|------|-------|
| settlement-summaries | Settlement Summaries | 5,397 |
| settlement-agreement-summaries | Settlement Agreement Summaries | 3,818 |
| draft-settlement-summaries | Draft Settlement Summaries | 4,263 |
| complex-settlement-agreement-summary | Complex Settlement Agreement Summary | 15,016 |

**Action:** Merge basic three into `settlement-summarization`. Keep `complex-settlement-agreement-summary` as a separate advanced skill if content is substantially different, otherwise fold in.

### Cluster: Deposition Summaries (3 skills → should be 1)

| Slug | Name | Chars |
|------|------|-------|
| deposition-summary-page-line | Deposition Summary - Page-line | 6,846 |
| deposition-summaries-deep-analysis | Deposition Summaries - Deep Analysis | 6,935 |
| deposition-summary-with-key-document-index | Deposition Summary with Key Document Index | 7,777 |

**Action:** Merge into one skill: `deposition-summarization`. These are three output format variations — should be one skill with format options.

---

## Problem 2: Cross-Practice Hub Duplicates (6 pairs of identical hubs)

The practice area hubs were duplicated across Corporate, Regulatory, and Transactional. These are ~100 char stub skills that exist purely for hierarchy. One hub has the children, the other is nearly empty.

| Hub Name | Corporate/Regulatory | Children | Transactional | Children |
|----------|---------------------|----------|---------------|----------|
| Securities & Capital Markets | corporate-securities... | 15 | regulatory-securities... | 1 |
| Mergers & Acquisitions | corporate-mergers... | 15 | transactional-mergers... | 3 |
| Corporate Governance | corporate-corporate-governance | 26 | transactional-corporate-governance | 2 |
| Non-Profit Organizations | corporate-non-profit... | 15 | regulatory-non-profit... | 1 |
| Employment & Consulting | transactional-employment... | 16 | regulatory-employment... | 2 |
| IP Licensing | transactional-ip-licensing | 20 | regulatory-ip-licensing | 1 |

**Action:** For each pair, keep the hub with more children. Reparent the orphaned children from the duplicate. Delete the empty hub.

---

## Problem 3: One-Off Duplicates (25 remaining pairs)

These are individual skills that exist in two versions, usually because one was created manually and another through the evolution pipeline.

| Skill A | Skill B | Similarity | Action |
|---------|---------|-----------|--------|
| Environmental Indemnity Agreement | Environmental Indemnity (Transactional) | 0.937 | Merge |
| Term Loan Agreement | Loan Agreement (Term) | 0.931 | Merge |
| Arbitration Agreement (Employment) | Employee Arbitration Agreement | 0.924 | Merge |
| Police Report Summaries | Police/Incident Report Summary | 0.920 | Merge |
| Settlement Demand Letter (PI) | Demand Letter (PI) | 0.916 | Merge |
| Pre-Trial Statement | Pre-Trial Statement/Report | 0.914 | Merge |
| E-Discovery Protocol (ESI) | E-Discovery Protocol Agreement | 0.903 | Merge |
| Stock Purchase Agreement (M&A) | Stock Purchase Agreement | 0.889 | Merge |
| Amicus Curiae Brief | Amicus Briefs | 0.888 | Merge |
| Class Action Notice to Members | Communication Plan for Class Notice | 0.886 | Merge |
| Subordination Agreement | Subordination Agreement (Debt) | 0.884 | Merge |
| Insider Trading Policy (Financial) | Insider Trading Policy | 0.884 | Merge |
| Cross-Examination Key Points | Cross-Examination Summaries | 0.883 | Merge |
| Investigator Agreement (Clinical) | Clinical Trial Agreement | 0.879 | **Review** — may be distinct |
| Board Meeting Summaries | Shareholder Meeting Summaries | 0.879 | **Keep both** — different meeting types |
| Residential Real Estate (hub) | Commercial Real Estate (hub) | 0.879 | **Keep both** — different practice areas |
| Verdict/Judgment Summary | Verdict Analysis | 0.876 | Merge |
| Board Resolution to Dissolve | Shareholder Resolution to Dissolve | 0.874 | **Keep both** — different corporate actions |
| Mediation Statement | Mediation Statement/Brief | 0.871 | Merge |
| Pre-Litigation Demand Letter | Demand Letter (PI) | 0.869 | Merge into demand letter family |
| Commercial Leasing (hub) | Commercial Real Estate (hub) | 0.867 | **Keep both** — parent/sibling hubs |
| Energy Regulation Summaries | Renewable Energy Regulation Summaries | 0.866 | Merge |
| Asset Purchase Agreement (APA) | Asset Purchase Agreement (M&A hub child) | 0.866 | Merge |
| Notice of Appeal - Criminal | Notice of Appeal | 0.865 | Merge — add criminal-specific section |
| Bill of Sale | Bill of Sale (CRE) | 0.864 | Merge |
| Settlement Demand Letter (PI) | Settlement Demand Package | 0.861 | Merge into demand letter family |
| Assignment of IP | Assignment of License | 0.857 | **Keep both** — different legal instruments |
| Insurance Policy Summaries | Insurance Correspondence Summarization | 0.855 | **Review** — may warrant keeping separate |
| Tender of Defense | Tender Letter Denial | 0.852 | **Keep both** — opposite actions |
| Insurance Policy Summaries | Insurance Claim Summaries | 0.851 | **Keep both** — different document types |

---

## Problem 4: Skills Missing Embeddings (56 skills)

These 56 skills exist in the DB but are invisible to semantic search via `legal_skill_find`. They need to be re-embedded.

All standalone root skills and most deposition forms are missing embeddings. This suggests the latest ingestion batch skipped the embedding step.

---

## Problem 5: Oversized Skills (235 skills over 20K chars)

53 skills are over 40K characters (~10K tokens). The Anthropic spec recommends <500 lines (~2-3K tokens for the main SKILL.md).

These need to be either:
- **Trimmed**: Remove verbose explanations, boilerplate, redundant examples
- **Split**: Move reference material into `references/` subdirectory

The hub stubs (100-600 chars) at levels 0-1 are the opposite problem — too thin to be useful as skills. These should become metadata/categories, not skill entries.

---

## Summary: Net Impact

| Action | Skills Affected | Net Change |
|--------|----------------|------------|
| Merge duplicate clusters (discovery, settlement, depo) | ~11 skills → 3 | -8 |
| Merge cross-practice hub dupes | 12 hubs → 6 | -6 |
| Merge one-off duplicates (~20 clear merges) | ~40 skills → 20 | -20 |
| Re-embed missing skills | 56 skills | 0 (no deletion) |
| Trim/split oversized skills | 235 skills | 0 (same count, better quality) |

**Estimated total after dedup: ~796 skills** (from 830). The skill count stays high for SEO/traffic. The quality improves significantly — fewer confusing near-duplicates, all skills have embeddings, oversized skills get trimmed.

---

## Recommended Execution Order

1. **Re-embed the 56 missing-embedding skills** — quickest win, zero risk
2. **Merge the 3 obvious clusters** (discovery, settlement, depo summaries) — highest confusion reduction
3. **Collapse the 6 cross-practice hub dupes** — reparent children, delete empty hubs
4. **Merge the ~20 one-off duplicates** — go pair by pair
5. **Trim oversized skills** — biggest effort, do progressively

Steps 1-4 can be scripted. Step 5 needs AI assistance (Claude to read and trim each skill).
