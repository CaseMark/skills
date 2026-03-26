---
name: redline
description: Compares two document versions and produces AI-powered redline analysis with structured change summaries, risk flags, and clause-by-clause breakdowns. Use when the user mentions "redline", "compare documents", "what changed", "version comparison", "contract diff", "track changes", or needs to understand differences between document versions.
---

# case.dev Redline Comparison

AI-powered document comparison that goes beyond visual diffs. Upload two versions of a contract or legal document, get a structured analysis of what changed, what it means, and what to watch out for.

Requires the `casedev` CLI. See `setup` skill for installation and auth.

## Quick Start

```bash
# Compare two local files
casedev redline compare ./contract-v1.pdf ./contract-v2.docx --json

# Compare two vault objects
casedev redline compare \
  --vault VAULT_ID \
  --base OBJECT_ID_V1 \
  --target OBJECT_ID_V2 \
  --json
```

## Compare Documents

### Local files

```bash
casedev redline compare ./old-version.pdf ./new-version.docx --json
```

Accepts PDF, DOCX, DOC, and TXT. Mixed formats supported (e.g., PDF vs DOCX).

### Vault objects

```bash
casedev redline compare \
  --vault VAULT_ID \
  --base OBJECT_ID \
  --target OBJECT_ID \
  --json
```

### URL sources

```bash
casedev redline compare \
  --base-url "https://example.com/v1.pdf" \
  --target-url "https://example.com/v2.pdf" \
  --json
```

## Output Structure

The default JSON output contains:

```json
{
  "summary": "Plain-English narrative of key changes",
  "riskFlags": [
    {
      "severity": "high",
      "clause": "Indemnification (Section 8.2)",
      "change": "Cap reduced from $5M to $1M",
      "impact": "Significantly increases exposure for indemnifying party"
    }
  ],
  "changes": [
    {
      "section": "Section 3.1 — Payment Terms",
      "type": "modified",
      "before": "Net 30 from invoice date",
      "after": "Net 60 from invoice date",
      "significance": "medium"
    }
  ],
  "stats": {
    "sectionsModified": 12,
    "sectionsAdded": 2,
    "sectionsRemoved": 1,
    "riskFlagsHigh": 1,
    "riskFlagsMedium": 3
  }
}
```

## Options

| Flag | Description |
|------|-------------|
| `--format` | Output format: `json` (default), `markdown`, `text` |
| `--detail` | Detail level: `summary`, `standard` (default), `detailed` |
| `--focus` | Comma-separated clause types to prioritize (e.g., `indemnification,termination,liability`) |
| `--perspective` | Analysis perspective: `neutral` (default), `drafter`, `reviewer` |
| `--json` | Shorthand for `--format json` |

### Detail levels

- **`summary`** — Executive overview only. Key changes and high-severity risk flags. Fast.
- **`standard`** — Full clause-by-clause breakdown with all risk flags. Default.
- **`detailed`** — Everything in standard plus original/modified text excerpts, suggested responses, and negotiation context.

### Perspective

- **`neutral`** — Objective analysis of changes.
- **`drafter`** — Flags changes that weaken your position (you drafted the original).
- **`reviewer`** — Flags changes you should push back on (you're reviewing incoming edits).

## Common Workflows

### Quick contract review

A partner sends back a marked-up contract. See what changed and whether to worry:

```bash
casedev redline compare ./our-draft.docx ./their-markup.docx \
  --perspective reviewer \
  --detail summary \
  --json
```

### Deep-dive on specific clauses

Focus analysis on the clauses that matter most:

```bash
casedev redline compare ./v3.pdf ./v4.pdf \
  --focus "indemnification,limitation-of-liability,termination,governing-law" \
  --detail detailed \
  --json
```

### Vault-based comparison

Compare two versions already stored in a vault:

```bash
casedev redline compare \
  --vault VAULT_ID \
  --base OBJECT_ID_V1 \
  --target OBJECT_ID_V2 \
  --format markdown
```

### Multi-version negotiation tracking

Compare across multiple rounds to see the negotiation arc:

```bash
# Compare each consecutive pair
casedev redline compare --vault VAULT_ID --base V1_ID --target V2_ID --json > round1.json
casedev redline compare --vault VAULT_ID --base V2_ID --target V3_ID --json > round2.json
casedev redline compare --vault VAULT_ID --base V3_ID --target V4_ID --json > round3.json
```

## Supported Formats

| Format | Input | Notes |
|--------|-------|-------|
| PDF | ✅ | OCR applied automatically for scanned documents |
| DOCX | ✅ | Preserves section/heading structure |
| DOC | ✅ | Converted to DOCX internally |
| TXT | ✅ | Plain text comparison |

Cross-format comparison is supported (e.g., compare a PDF against a DOCX).

## Troubleshooting

**"Unable to extract text"**: Document may be a scanned image without OCR text layer. Re-upload to a vault (automatic OCR) or use `casedev ocr process` first.

**Large documents timeout**: Documents over 200 pages may need `--detail summary` for faster processing.

**"No significant changes found"**: Documents may be identical or near-identical. Check you're comparing the right versions.

**Risk flags seem off**: Use `--perspective` to align analysis with your role in the negotiation. Default `neutral` perspective doesn't assume a side.
