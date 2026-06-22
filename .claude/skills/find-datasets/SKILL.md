---
name: find-datasets
description: >
  Search public repositories for datasets that fit a specific analysis or experiment in one of the
  user's projects, then create a dataset record for each viable candidate. Use when the user asks to
  "find", "search for", or "identify" public datasets suitable for an analysis.
---

# Find reusable public datasets

Goal: a short, ranked set of genuinely usable candidates — not a search dump — each captured with the
`ingest-dataset` workflow. Follows `00_AGENT/CLAUDE.md` (mode E).

## 1. Pin the requirement
Read the relevant `01_PROJECTS/<slug>/PROJECT_CONTEXT.md` (model system, assay, sample structure,
intended analysis, constraints). Restate the exact inclusion criteria a dataset must meet (organism,
tissue/model, disease/exposure, modality, group structure, covariates needed, raw vs processed).

## 2. Search the right repositories
Use `WebSearch` plus the relevant tools/repositories for the modality, e.g. GEO, SRA/ENA,
ArrayExpress/BioStudies, Single Cell Portal, CELLxGENE, HCA, GTEx, AD Knowledge Portal / Synapse,
PRIDE/ProteomeXchange, MetaboLights, Zenodo/Figshare. Use the PubMed tools to find data-availability
statements in candidate papers (load schemas via ToolSearch first). Prefer atlases, benchmarks, and
validation cohorts when they serve the decision.

## 3. Triage before recording
Discard candidates that fail a hard criterion (wrong organism/tissue, no per-group counts, no usable
metadata, inaccessible). For survivors, run `ingest-dataset` to create a record under `03_DATASETS/`.

## 4. Report
Return a ranked table: candidate, accession, why it fits, the critical caveat, suitability
(strong/conditional/weak), and link to its dataset record. Note explicitly when no dataset clears the
bar — that is a valid, useful answer.
