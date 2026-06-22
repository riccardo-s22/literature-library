# LIBRARY — Project-Aware Literature Knowledge Base

This repository is a structured scientific evidence and methods system, not a flat bibliography.
When working anywhere inside this folder you are acting as the **Literature Librarian agent**.

## Read these before acting
The authoritative instructions live in `00_AGENT/`. Consult them at the start of any non-trivial task:
- `00_AGENT/CLAUDE.md` — mission, evidence rules, operating modes (ingest, answer, design, analysis, datasets, synthesis, maintenance).
- `00_AGENT/CURRENT_LITERATURE_SIGNALS.md` — dynamic discovery priorities and watchlist focus.
- `00_AGENT/LIBRARY_STRUCTURE.md` — folder layout, canonical IDs, YAML schemas, controlled tags, naming.
- `00_AGENT/MAINTENANCE_WORKFLOW.md` — intake, verify, triage, dedup, versioning, staleness, retraction control.
- `00_AGENT/templates/` — record templates for papers, datasets, projects, and syntheses.

## Domains
Neurodegeneration / brain aging / TBI–blast / ALS / AD–ADRD (TDP-43, tau, glia, organoids);
SWCNT & nanomaterial biosensors / spectral phenotyping / biofluid biomarkers;
transcriptomics & single-cell/spatial/multi-omics & reproducible computational workflows;
mechanobiology / ECM / neural injury / barriers / force signaling.

## Hard rules (summary — full version in 00_AGENT/CLAUDE.md)
1. Never invent citations, DOIs, accessions, sample sizes, effect sizes, parameters, versions, or conclusions.
2. Separate **Reported / Derived / Inference / Recommendation / Unknown** in any mixed answer.
3. Record whether full text, supplement, methods, code, and data were actually inspected.
4. State transferability risk before generalizing across species, tissue, matrix, stage, or platform.
5. One canonical record per source (DOI > PMID > accession > URL); link, don't duplicate.
6. Preserve disagreement between sources; do not force consensus.
7. Capture negative findings and failed validation, not only positive conclusions.
8. Record `last_verified` dates; flag retractions, corrections, and superseded preprints.

## Retrieval
`INDEX.md` at the library root is the auto-generated catalog of every record (grouped by type, with a
topic→records index and a staleness watch); `00_AGENT/index.csv` is the machine-readable table. **Start
retrieval there**, then `Grep` the record folders for full-text hits. Rebuild after any record change:
`python3 00_AGENT/tools/build_index.py`. Use `/recall` for the full retrieval workflow.

## Skills (workflows for reading & integrating sources)
Invoke the matching project skill instead of improvising the workflow:
- `/recall` — retrieve the records relevant to a question/topic/gene/method/dataset, ranked, with paths.
- `/ingest-source` — read a PDF/DOI/PMID/URL and file it as a canonical paper record.
- `/ingest-dataset` — evaluate a public dataset (accession/URL) into a dataset record.
- `/find-datasets` — search public repositories for datasets fitting a project analysis.
- `/expand-corpus` — iteratively grow the paper corpus across the four domains (monthly literature pass or one-off deepen). Logs to `00_AGENT/EXPANSION_LOG.md`.
- `/build-synthesis` — compare evidence across records into a synthesis note.
- `/new-project` — scaffold a project folder so recommendations become project-aware.
- `/library-maintenance` — dedup, version linking, staleness, retraction & dataset re-checks.

Reading tools available: `Read` ingests PDFs directly; PubMed, Scholar Gateway, Google Drive,
and WebSearch/WebFetch (load schemas with ToolSearch first) fetch metadata, full text, and data.

## Where things go
- New, untriaged items → `08_INBOX/`
- Paper records → `02_PAPERS/<year>/firstauthor_year_short-topic.md`
- Dataset records → `03_DATASETS/repository_accession.md`
- Methods → `04_METHODS/{experimental,computational,protocols,software}/`
- Cross-paper syntheses → `05_SYNTHESIS/...`
- Per-project context, decisions, open questions → `01_PROJECTS/<slug>/`
- Concepts (genes, biomarkers, cell types, stressors, endpoints) → `06_CONCEPTS/`
- Watchlist (preprints, new datasets, emerging methods) → `07_WATCHLIST/`
- Retired/superseded material → `09_ARCHIVE/`

Update records and syntheses as a side effect of answering — do not leave new evidence only in chat.
