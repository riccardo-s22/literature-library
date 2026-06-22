# Claude Literature Agent Bundle

This bundle turns a literature collection into a project-aware scientific knowledge base.

## Recommended use
1. Use `CLAUDE.md` as the main instruction file.
2. Add the other files as project knowledge or source files.
3. Create one `PROJECT_CONTEXT.md` per active research project.
4. Store each paper and dataset as one canonical record.
5. Ask Claude to update records and syntheses, not just answer questions in chat.

## Minimum viable setup
Start with:
- `CLAUDE.md`
- `CURRENT_LITERATURE_SIGNALS.md`
- `PAPER_RECORD_TEMPLATE.md`
- `DATASET_RECORD_TEMPLATE.md`
- one completed project context

Add the full folder structure once the collection grows.

## Suggested first commands
- “Ingest this paper using the canonical paper record template and link it to the relevant project.”
- “Compare the evidence across all records relevant to this experimental parameter and create a synthesis note.”
- “Find public datasets suitable for this exact analysis and create one dataset record per candidate.”
- “Audit this project for missing controls, under-supported design choices, and unvalidated analysis steps.”
- “Update the decision log only when new evidence changes an existing choice.”

## Important distinction
`CURRENT_LITERATURE_SIGNALS.md` tells the agent what to watch. `PROJECT_CONTEXT.md` tells it what matters now. `CLAUDE.md` tells it how to reason and maintain evidence.
