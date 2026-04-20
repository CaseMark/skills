# Case-Summary Runbook — case.dev Commands

Copy-pasteable commands for the ingest → OCR → inventory → search loop described in `SKILL.md`. Not a script; run them as you need them.

Every command assumes `casedev auth status` shows you authenticated. Add `--json` where you want machine-readable output for the next step.

---

## 1. Ingest

**New vault for this case:**

```bash
casedev vault create --name "<Case Caption — YYYY-MM-DD>" \
  --description "Case-summary corpus" 
```

**Upload a folder (recursive):**

```bash
casedev vault upload /path/to/case-files --vault <vault-id>
```

Uploads concurrently, kicks off ingestion + graph-building automatically. Large corpora take minutes to hours to fully index — OCR runs in the background.

**Check ingestion status:**

```bash
casedev vault get <vault-id>
casedev jobs list --scope vault --vault <vault-id>
```

If you see pending ingest jobs, wait before searching — the vault will return partial hits.

---

## 2. OCR (only when needed)

Vault ingestion auto-OCRs most PDFs. Only fire this explicitly if you find non-searchable PDFs that slipped through (usually scans with no text layer).

**Find objects that might need OCR:**

```bash
casedev --json vault object list <vault-id> \
  | jq '.objects[] | select(.contentType == "application/pdf")'
```

**Kick off OCR on one:**

```bash
casedev ocr process --document-id <object-id> --engine default
casedev ocr watch <ocr-job-id>        # block until done
```

**Get word-level results (rarely needed, useful for exhibit alignment):**

```bash
casedev ocr words --vault <vault-id> --object <object-id> --page 1
```

---

## 3. Inventory

Before running queries, build a mental model of the corpus.

**Full list, filenames + sizes:**

```bash
casedev vault object list <vault-id> --wide
```

**Count by content type:**

```bash
casedev --json vault object list <vault-id> \
  | jq '[.objects[].contentType] | group_by(.) | map({type: .[0], count: length})'
```

**Filenames only, for pattern-matching against the search playbook:**

```bash
casedev --json vault object list <vault-id> \
  | jq -r '.objects[].name' | sort
```

---

## 4. Search (the MAP phase)

This is the loop you'll run many times. Every query returns ranked chunks with source object + location. See `SEARCH-PLAYBOOK.md` for query patterns per case dimension.

**Default (hybrid semantic + keyword):**

```bash
casedev search vault "<query>" --vault <vault-id> --limit 10
```

**Scope to a subset of objects** (e.g., medicals only, after inventory):

```bash
casedev search vault "<query>" --vault <vault-id> \
  --object <obj-id-1> --object <obj-id-2> --limit 10
```

**Method variants** (pick based on the question):

| Method | When to use |
|---|---|
| `hybrid` (default) | General factual queries |
| `vector` | Conceptual / paraphrased queries |
| `fast` | Cheap coverage sweeps |
| `global` | "What does this case say about X overall?" |
| `entity` | "Who is Dr. Smith?", "What is Exhibit 4?" |
| `graph` | Cross-document relationships (party → event → document) |
| `local` | Tight neighborhood of a single entity |

```bash
casedev search vault "policy limits demand response" \
  --vault <vault-id> --method entity --limit 5
```

**JSON mode for piping into notes:**

```bash
casedev --json search vault "<query>" --vault <vault-id> --limit 10 \
  | jq '.results[] | {object: .fileName, page: .pageNumber, text: .text}'
```

---

## 5. Retrieve a full object

When a chunk looks load-bearing, pull the source document to verify or read around it.

```bash
casedev vault download --vault <vault-id> --object <object-id> --out ./work
```

---

## 6. Staying honest

- Every citation in the memo = an object name + page (or chunk ID), produced by one of the commands above.
- If the vault didn't return a chunk for a claim, don't put that claim in the memo — or label it an assumption.
- Keep a scratch log of queries you ran and what came back. It lets you avoid re-asking and gives the attorney a record of how the memo was built.
