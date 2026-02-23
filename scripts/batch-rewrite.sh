#!/usr/bin/env bash
#
# batch-rewrite.sh — Rewrites legal skills from DB exports to SKILL.md files
# Uses Claude Code CLI (claude -p) for each skill
#
# Usage:
#   ./scripts/batch-rewrite.sh                    # Process all remaining
#   ./scripts/batch-rewrite.sh --limit 10         # Process first 10 remaining
#   ./scripts/batch-rewrite.sh --slug my-skill    # Process a single skill
#   ./scripts/batch-rewrite.sh --dry-run          # Show what would be processed
#   ./scripts/batch-rewrite.sh --parallel 4       # Run 4 at a time (default: 3)

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
EXPORT_DIR="$REPO_ROOT/audit/export/by-slug"
SKILLS_DIR="$REPO_ROOT/skills/legal"
SYSTEM_PROMPT="$REPO_ROOT/scripts/rewrite-skill.md"
LOG_DIR="$REPO_ROOT/audit/rewrite-logs"
REMAINING_FILE="$REPO_ROOT/audit/remaining-slugs.txt"

# Defaults
LIMIT=0
SINGLE_SLUG=""
DRY_RUN=false
PARALLEL=3

# Parse args
while [[ $# -gt 0 ]]; do
  case $1 in
    --limit) LIMIT="$2"; shift 2 ;;
    --slug) SINGLE_SLUG="$2"; shift 2 ;;
    --dry-run) DRY_RUN=true; shift ;;
    --parallel) PARALLEL="$2"; shift 2 ;;
    *) echo "Unknown option: $1"; exit 1 ;;
  esac
done

mkdir -p "$LOG_DIR"

# Build the list of slugs to process
get_remaining_slugs() {
  python3 -c "
import json, os, sys

export_dir = '$EXPORT_DIR'
skills_dir = '$SKILLS_DIR'

# Get all existing skill directories
existing = set()
if os.path.exists(skills_dir):
    existing = set(os.listdir(skills_dir)) - {'.gitkeep', '.DS_Store'}

# Get all exported skill JSONs
slugs_to_process = []
for fname in sorted(os.listdir(export_dir)):
    if not fname.endswith('.json'):
        continue
    slug = fname[:-5]

    # Skip hub stubs (< 200 chars content)
    fpath = os.path.join(export_dir, fname)
    with open(fpath) as f:
        data = json.load(f)
    content = data.get('content', '') or ''
    if len(content) < 200:
        continue

    # Skip if already processed (check if any existing dir matches as suffix)
    already_done = False
    for existing_dir in existing:
        if slug == existing_dir or slug.endswith('-' + existing_dir) or slug.endswith(existing_dir):
            already_done = True
            break

    if not already_done:
        slugs_to_process.append(slug)

for s in slugs_to_process:
    print(s)
"
}

if [[ -n "$SINGLE_SLUG" ]]; then
  SLUGS=("$SINGLE_SLUG")
else
  mapfile -t SLUGS < <(get_remaining_slugs)
fi

TOTAL=${#SLUGS[@]}
echo "=== CaseMark Skill Batch Rewrite ==="
echo "Total skills to process: $TOTAL"
echo "Parallel workers: $PARALLEL"
echo ""

if [[ "$LIMIT" -gt 0 ]] && [[ "$LIMIT" -lt "$TOTAL" ]]; then
  SLUGS=("${SLUGS[@]:0:$LIMIT}")
  echo "Limited to first $LIMIT skills"
fi

if $DRY_RUN; then
  echo "DRY RUN — would process:"
  for slug in "${SLUGS[@]}"; do
    echo "  $slug"
  done
  exit 0
fi

# Read system prompt
SYSTEM_PROMPT_CONTENT=$(cat "$SYSTEM_PROMPT")

# Process a single skill
process_skill() {
  local slug="$1"
  local idx="$2"
  local total="$3"
  local json_file="$EXPORT_DIR/${slug}.json"
  local log_file="$LOG_DIR/${slug}.log"

  if [[ ! -f "$json_file" ]]; then
    echo "[$idx/$total] SKIP $slug — no JSON export found" | tee -a "$log_file"
    return 1
  fi

  echo "[$idx/$total] Processing: $slug"

  # Read the JSON content
  local skill_json
  skill_json=$(cat "$json_file")

  # Call claude -p with the skill JSON as the prompt
  local result
  result=$(claude -p "Rewrite this skill into a SKILL.md file. Here is the skill JSON:

$skill_json" \
    --system-prompt "$SYSTEM_PROMPT_CONTENT" \
    --allowedTools "" \
    --output-format json \
    --max-turns 1 \
    2>"$log_file")

  local exit_code=$?

  if [[ $exit_code -ne 0 ]]; then
    echo "[$idx/$total] FAILED $slug (exit $exit_code)" | tee -a "$log_file"
    return 1
  fi

  # Extract the result text from JSON output
  local skill_content
  skill_content=$(echo "$result" | python3 -c "
import json, sys
data = json.load(sys.stdin)
text = data.get('result', '')
# Strip any markdown code fences that might wrap the output
if text.startswith('\`\`\`markdown'):
    text = text[len('\`\`\`markdown'):].strip()
if text.startswith('\`\`\`'):
    text = text[3:].strip()
if text.endswith('\`\`\`'):
    text = text[:-3].strip()
print(text)
")

  # Extract the new slug from the frontmatter
  local new_slug
  new_slug=$(echo "$skill_content" | python3 -c "
import sys, re
content = sys.stdin.read()
m = re.search(r'^name:\s*(.+)$', content, re.MULTILINE)
if m:
    print(m.group(1).strip())
else:
    print('')
")

  if [[ -z "$new_slug" ]]; then
    echo "[$idx/$total] FAILED $slug — could not extract slug from output" | tee -a "$log_file"
    echo "$skill_content" >> "$log_file"
    return 1
  fi

  # Validate the output starts with frontmatter
  if [[ ! "$skill_content" == ---* ]]; then
    echo "[$idx/$total] FAILED $slug — output doesn't start with ---" | tee -a "$log_file"
    echo "$skill_content" >> "$log_file"
    return 1
  fi

  # Create the skill directory and write the file
  local skill_dir="$SKILLS_DIR/$new_slug"
  mkdir -p "$skill_dir"
  echo "$skill_content" > "$skill_dir/SKILL.md"

  local line_count
  line_count=$(wc -l < "$skill_dir/SKILL.md")
  echo "[$idx/$total] OK $slug → $new_slug ($line_count lines)" | tee -a "$log_file"

  # Log the mapping
  echo "$slug → $new_slug" >> "$LOG_DIR/_slug-mapping.txt"
}

export -f process_skill
export EXPORT_DIR SKILLS_DIR LOG_DIR SYSTEM_PROMPT_CONTENT

# Run with GNU parallel if available, otherwise sequential with background jobs
if command -v parallel &>/dev/null; then
  echo "Using GNU parallel with $PARALLEL workers"
  echo ""

  IDX=0
  for slug in "${SLUGS[@]}"; do
    ((IDX++))
    echo "$slug $IDX ${#SLUGS[@]}"
  done | parallel --colsep ' ' -j "$PARALLEL" --bar process_skill {1} {2} {3}
else
  echo "GNU parallel not found — using background jobs"
  echo ""

  IDX=0
  RUNNING=0
  PIDS=()

  for slug in "${SLUGS[@]}"; do
    ((IDX++))

    process_skill "$slug" "$IDX" "${#SLUGS[@]}" &
    PIDS+=($!)
    ((RUNNING++))

    # Wait if we hit the parallel limit
    if [[ $RUNNING -ge $PARALLEL ]]; then
      wait "${PIDS[0]}"
      PIDS=("${PIDS[@]:1}")
      ((RUNNING--))
    fi
  done

  # Wait for remaining
  for pid in "${PIDS[@]}"; do
    wait "$pid" || true
  done
fi

echo ""
echo "=== Complete ==="
echo "Processed: ${#SLUGS[@]} skills"
echo "Output: $SKILLS_DIR"
echo "Logs: $LOG_DIR"

# Count results
if [[ -f "$LOG_DIR/_slug-mapping.txt" ]]; then
  SUCCESS=$(wc -l < "$LOG_DIR/_slug-mapping.txt")
  echo "Successful: $SUCCESS"
fi
