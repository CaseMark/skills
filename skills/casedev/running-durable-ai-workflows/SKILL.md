---
name: running-durable-ai-workflows
language: en
description: Builds and runs durable, crash-recoverable AI workflows using Smithers (smithers-orchestrator). Use when a task requires multi-step orchestration that must survive failures — map-reduce over large document sets, sequential processing with structured intermediate outputs, iterative refinement loops, or any long-running agent pipeline where losing progress is unacceptable. Not for single-shot tasks a prompt can handle directly.
---

# Durable AI Workflows with Smithers

Smithers (`smithers-orchestrator`) turns a JSX tree into a durable, resumable workflow backed by SQLite. Each completed step persists automatically — crashes, rate limits, or context exhaustion lose zero finished work.

**Docs:** <https://smithers.sh>

## When to Use This

Reach for a Smithers workflow when the task has **all** of these traits:

1. **Multi-step** — more than one distinct processing phase
2. **Long-running** — minutes to hours (large documents, many chunks, iterative refinement)
3. **Progress matters** — restarting from scratch on failure is expensive or unacceptable

If a task is single-shot or completes in one LLM call, just do it directly. Don't add workflow machinery for simple work.

### Good Candidates

- Processing a 50k-page medical record: chunk → summarize each → cross-reference → compose narrative
- Iterative document drafting: write → review → revise (loop until approved)
- Parallel multi-model review: fan out to multiple agents, merge results
- Sequential pipeline with validation gates between stages

### Bad Candidates

- Summarize a 10-page contract (one prompt)
- Draft a single motion (one prompt)
- Any task where failure just means re-running a single call

## Setup

```bash
bunx smithers-orchestrator init    # scaffolds .smithers/ directory
bun add smithers-orchestrator ai @ai-sdk/anthropic zod
```

Minimal `tsconfig.json`:

```json
{
  "compilerOptions": {
    "jsx": "react-jsx",
    "jsxImportSource": "smithers-orchestrator",
    "target": "ESNext",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "strict": true,
    "noEmit": true,
    "skipLibCheck": true
  }
}
```

## Core Concepts

### Workflow Structure

Every workflow is a JSX tree. `createSmithers` registers Zod schemas (each becomes a SQLite table). Tasks produce typed, validated outputs.

```tsx
/** @jsxImportSource smithers-orchestrator */
import { createSmithers, Sequence, Task } from "smithers-orchestrator";
import { ToolLoopAgent as Agent } from "ai";
import { anthropic } from "@ai-sdk/anthropic";
import { z } from "zod";

const { Workflow, smithers, outputs } = createSmithers({
  summary: z.object({
    text: z.string(),
    pageRange: z.string(),
    keyFindings: z.array(z.string()),
  }),
});

const summarizer = new Agent({
  model: anthropic("claude-sonnet-4-20250514"),
  instructions: "Summarize document chunks. Return structured JSON.",
});

export default smithers((ctx) => (
  <Workflow name="summarize-chunk">
    <Task id="summarize" output={outputs.summary} agent={summarizer}>
      {`Summarize pages ${ctx.input.startPage}-${ctx.input.endPage}`}
    </Task>
  </Workflow>
));
```

### Running & Resuming

```bash
# Start a workflow
bunx smithers-orchestrator up workflow.tsx --input '{"startPage":1,"endPage":500}'

# Resume after crash (skips completed tasks)
bunx smithers-orchestrator up workflow.tsx --run-id <id> --resume true

# Monitor
bunx smithers-orchestrator ps
bunx smithers-orchestrator inspect <run-id>
bunx smithers-orchestrator logs <run-id> --follow
```

### Data Flow Between Tasks

Tasks read upstream outputs via `ctx.outputMaybe()`. The runtime re-renders after each task completes — downstream tasks mount only when their dependencies are ready.

```tsx
const analysis = ctx.outputMaybe(outputs.analysis, { nodeId: "analyze" });

<Sequence>
  <Task id="analyze" output={outputs.analysis} agent={analyst}>
    {`Analyze ${ctx.input.document}`}
  </Task>
  {analysis ? (
    <Task id="report" output={outputs.report} agent={reporter}>
      {`Write report based on: ${analysis.summary}`}
    </Task>
  ) : null}
</Sequence>
```

## Control Flow Components

### Sequence (default)

Children run top-to-bottom. `<Workflow>` implicitly sequences its children.

### Parallel

Fan out work with an optional concurrency cap:

```tsx
<Parallel maxConcurrency={5}>
  {chunks.map((chunk) => (
    <Task key={chunk.id} id={`summarize-${chunk.id}`} output={outputs.chunkSummary} agent={summarizer}>
      {`Summarize: ${chunk.text}`}
    </Task>
  ))}
</Parallel>
```

### Loop

Iterate until a condition is met:

```tsx
<Loop until={latestReview?.approved === true} maxIterations={5} onMaxReached="return-last">
  <Sequence>
    <Task id="draft" output={outputs.draft} agent={writer}>
      {feedback ? `Revise. Feedback: ${feedback}` : `Draft: ${ctx.input.topic}`}
    </Task>
    <Task id="review" output={outputs.review} agent={reviewer}>
      Review the latest draft. Return { approved: boolean, feedback: string }.
    </Task>
  </Sequence>
</Loop>
```

### Approval (Human Gate)

Pause for human review before proceeding:

```tsx
<Approval
  id="confirm"
  output={outputs.decision}
  request={{ title: "Proceed with filing?", summary: draftSummary }}
  onDeny="skip"
/>
```

Operator approves via CLI:

```bash
bunx smithers-orchestrator ps --status waiting-approval
bunx smithers-orchestrator approve <run-id> --node confirm --by operator
bunx smithers-orchestrator up workflow.tsx --run-id <run-id> --resume true
```

## Common Patterns

### Map-Reduce Over Large Documents

The core pattern for processing documents too large for a single context window:

```tsx
export default smithers((ctx) => {
  const chunkSummaries = ctx.input.chunks.map((c) =>
    ctx.outputMaybe(outputs.chunkSummary, { nodeId: `chunk-${c.id}` })
  );
  const allDone = chunkSummaries.every(Boolean);

  return (
    <Workflow name="medical-record-review">
      {/* Map: summarize each chunk in parallel */}
      <Parallel maxConcurrency={5}>
        {ctx.input.chunks.map((chunk) => (
          <Task key={chunk.id} id={`chunk-${chunk.id}`} output={outputs.chunkSummary} agent={chunkSummarizer}>
            {`Summarize pages ${chunk.startPage}-${chunk.endPage}. Extract key findings, dates, providers.`}
          </Task>
        ))}
      </Parallel>

      {/* Reduce: compose final narrative from all summaries */}
      {allDone ? (
        <Task id="compose" output={outputs.narrative} agent={narrativeComposer}>
          {`Compose a coherent narrative from these summaries:\n${chunkSummaries.map((s) => s.text).join("\n---\n")}`}
        </Task>
      ) : null}
    </Workflow>
  );
});
```

### Iterative Refinement

Write → review → revise until quality threshold is met. See the Loop example above.

### Parallel Multi-Agent Review

Fan out to multiple models, merge their findings:

```tsx
<Parallel>
  <Task id="review-claude" output={outputs.review} agent={claude} continueOnFail>
    Review this document for issues.
  </Task>
  <Task id="review-codex" output={outputs.review} agent={codex} continueOnFail>
    Review this document for issues.
  </Task>
</Parallel>
```

### Conditional Branching on Output

Route downstream work based on what a task produced:

```tsx
const analysis = ctx.outputMaybe(outputs.analysis, { nodeId: "analyze" });

{analysis?.risk === "high" ? (
  <Task id="escalate" output={outputs.escalation} agent={escalator}>
    {`Critical finding: ${analysis.summary}`}
  </Task>
) : null}
```

### Continue-As-New for Very Long Runs

For workflows with hundreds of iterations (e.g., processing a massive document set), accumulated SQLite state grows. Hand off to a fresh run with carried state:

```tsx
<ContinueAsNew when={iterationCount > 100} carry={{ summary: rolledUpState }} />
```

### Side-Effect Tools with Idempotency

When tasks make external mutations (create tickets, send emails, call APIs), mark tools as side effects and use the runtime's idempotency key to prevent duplicates on retry:

```tsx
import { defineTool } from "smithers-orchestrator/tools";

const createTicket = defineTool({
  name: "linear.create",
  schema: z.object({ title: z.string(), description: z.string() }),
  sideEffect: true,
  idempotent: false,
  async execute(args, ctx) {
    return linear.createIssue({ ...args, idempotencyKey: ctx.idempotencyKey });
  },
});
```

### Optional Non-Blocking Steps

Use `continueOnFail` for nice-to-have steps that shouldn't block the pipeline:

```tsx
<Task id="citation-check" output={outputs.citations} agent={citationChecker} continueOnFail>
  Verify all citations. Pipeline continues even if this fails.
</Task>
```

### Project Structure

For larger workflows, extract schemas to their own file:

```ts
// schemas.ts
export const schemas = {
  chunkSummary: z.object({ text: z.string(), pageRange: z.string(), findings: z.array(z.string()) }),
  narrative:    z.object({ title: z.string(), body: z.string(), citations: z.array(z.string()) }),
};

// workflow.tsx
import { schemas } from "./schemas";
const { Workflow, smithers, outputs } = createSmithers(schemas);
```

## Task Configuration

### Retries & Timeouts

```tsx
<Task
  id="api-call"
  agent={agent}
  retries={3}
  retryPolicy={{ backoff: "exponential", initialDelayMs: 1000 }}
  timeoutMs={60_000}
  continueOnFail  // pipeline continues even if this task fails
>
```

### Caching (Skip Expensive Re-runs)

```tsx
<Task
  id="analyze"
  output={outputs.analysis}
  agent={analyst}
  cache={{ by: (ctx) => ({ doc: ctx.input.documentId }), version: "v1" }}
>
```

Tweak downstream tasks without re-running expensive upstream ones.

### Agent Tool Permissions

Match tools to the task's role — least privilege:

```tsx
const analyst     = new Agent({ model, instructions: "..." });                         // no tools
const reviewer    = new Agent({ model, instructions: "...", tools: { read, grep } });  // read-only
const implementer = new Agent({ model, instructions: "...", tools: { read, write, edit, bash } });
```

## CLI Quick Reference

| Command | Purpose |
|---------|---------|
| `up workflow.tsx` | Start or resume a workflow |
| `up workflow.tsx --resume true` | Resume from last checkpoint |
| `up workflow.tsx --detach` | Run in background |
| `ps` | List runs |
| `inspect <run-id>` | Detailed run state |
| `logs <run-id> --follow` | Tail events |
| `chat <run-id>` | View agent transcripts |
| `approve <run-id> --node <id>` | Approve a pending gate |
| `deny <run-id> --node <id>` | Deny a pending gate |
| `why <run-id>` | Explain why a run is blocked |
| `node <node-id> --run-id <id>` | Debug a specific task |

All commands: `bunx smithers-orchestrator <command>`

## Key Principles

1. **One Task per logical operation.** Don't split cross-dependent reasoning into separate tasks — you lose coherence. A single Task can use multiple tools internally.
2. **Stable IDs.** Use meaningful IDs (`chunk-${id}`, not array indices) so resume matches correctly.
3. **Zod schemas for everything.** Every Task output should have a schema. Validation failures trigger automatic retries — the agent self-corrects.
4. **Start simple.** Begin with a `<Sequence>` of 2-3 tasks. Add `<Parallel>`, `<Loop>`, and `<Approval>` only when the task genuinely needs them.
