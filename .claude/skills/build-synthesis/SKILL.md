---
name: build-synthesis
description: >
  Build or refresh a cross-paper synthesis note that answers one decision-relevant question by
  comparing evidence across multiple existing library records. Use when a question depends on several
  papers, when evidence conflicts, or when a defensible evidence summary is needed for a grant/experiment.
---

# Build a cross-paper synthesis

Goal: a synthesis under `05_SYNTHESIS/<subfolder>/<question_short-name>_<YYYY-MM-DD>.md` that preserves
agreement *and* disagreement and ends in an actionable recommendation. Follows `00_AGENT/CLAUDE.md`
(mode F) and `MAINTENANCE_WORKFLOW.md` §6 (synthesize when ≥3 sources address the same question, when
evidence conflicts, or when a decision needs a defensible summary).

## 1. Frame one answerable question
State a single biological / experimental / analytical / dataset question and the project decision it
informs. Define scope: included source types, organisms/models, date range, inclusion & exclusion
criteria, search limits.

## 2. Gather the evidence from the library first
Search existing records in `02_PAPERS/`, `03_DATASETS/`, `04_METHODS/`, and prior `05_SYNTHESIS/` notes
(use `Grep`/`Glob`). Ingest any missing key source via `ingest-source` before relying on it — do not
synthesize from memory. Pick the appropriate `05_SYNTHESIS/` subfolder (biological_questions,
methods_comparisons, dataset_landscapes, evidence_gaps).

## 3. Synthesize using the template
Copy `00_AGENT/templates/SYNTHESIS_NOTE_TEMPLATE.md`. Fill the evidence matrix (one row per source with
model, design, key parameter, result, strength, limitation, relevance). Capture convergence, and for
each disagreement give the likely cause (model, population, assay, dose, timing, endpoint, analysis,
power, bias). List evidence gaps and candidate datasets/resources. Keep **Reported / Inference /
Speculative** distinct, especially for new hypotheses.

## 4. Land the recommendation, link back & refresh catalog
Give the bottom line (3–6 sentences), a confidence level, and the conditions that would change it. Link
the synthesis to its sources and to the relevant `01_PROJECTS/<slug>/` and `DECISIONS.md`. Rebuild the
retrieval index (`python3 00_AGENT/tools/build_index.py`). Report the path and any sources still needing
follow-up. Set `last_updated` to today.
