---
name: search
description: Searches the web, legal databases, case law, patents, and case.dev knowledge base via the casedev CLI. Use when the user mentions "search", "legal research", "find cases", "case law", "patent search", "web search", "fetch URL", "webfetch", "legal skills", or needs to research legal topics, find similar cases, or retrieve web content.
---

# case.dev Search

Unified search across web, legal databases, case law, patents, vault contents, and the case.dev skills knowledge base.

Requires the `casedev` CLI. See `setup` skill for installation and auth.

## Web Search

```bash
casedev search web "employment discrimination California" --json
casedev search web "SEC enforcement actions 2024" --limit 20 --json
```

Flags: `--limit` (default: 10), `--news`, `--type` (search|news), `--include-domain`, `--exclude-domain`.

## Web Fetch

```bash
casedev search webfetch "https://example.com/ruling.html" --json
```

Flags: `--livecrawl`, `--subpages`, `--subpage-target N`, `--max-chars N`, `--timeout N`, `--context`, `--no-summary`, `--fallback`.

Multiple URLs: `casedev search webfetch URL1 URL2 --json`

## Legal Search

```bash
casedev search legal "breach of fiduciary duty" --json
casedev search legal "ERISA preemption" --jurisdiction "federal" --json
```

Flags: `--jurisdiction`, `--limit` (default: 10), `--deep`, `--alt-query` (repeatable, for deep mode).

Deep mode example:
```bash
casedev search legal "force majeure pandemic" --deep \
  --alt-query "impossibility of performance COVID" \
  --alt-query "frustration of purpose" --json
```

## Case Search

### By query
```bash
casedev search cases "wrongful termination retaliation" --json
```

### By similarity
```bash
casedev search cases --url "https://casetext.com/case/example-v-example" --json
casedev search cases --url "https://example.com/case" --after "2020-01-01" --json
```

Flags: `--jurisdiction`, `--limit` (default: 10), `--url` (similarity mode), `--after` (date filter).

## Patent Search

```bash
casedev search patent "machine learning NLP" --json
```

Flags: `--assignee`, `--inventor`, `--status`, `--type`, `--filing-from`, `--filing-to`, `--offset`, `--limit` (default: 25).

## Vault Semantic Search

```bash
casedev search vault "indemnification clause" --vault VAULT_ID --json
```

See `vaults` skill for full vault search documentation.

## Skills Knowledge Base

```bash
casedev skills search "contract review" --json
casedev skills read SKILL_SLUG --json
casedev skills read SKILL_SLUG --content-only
```

## Troubleshooting

**No legal results**: Try broader terms, remove jurisdiction filter, or use `--deep` mode with `--alt-query` variations.

**Web fetch unavailable**: Use `--fallback` to fall back to web search.
