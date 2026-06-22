---
name: ingest-dataset
description: >
  Evaluate a public dataset (from an accession, repository URL, or associated paper) and integrate it
  into the LIBRARY as a canonical dataset record. Use when the user wants to assess, add, or vet a
  specific dataset (GEO/SRA/ArrayExpress/ENA/PRIDE/Zenodo/etc.) for reuse or validation.
---

# Ingest a dataset into the library

Goal: a verified record under `03_DATASETS/<repository>_<accession>.md` that says not just what the
dataset is, but whether it can actually support a specific analysis — per `00_AGENT/CLAUDE.md` (mode E)
and `00_AGENT/MAINTENANCE_WORKFLOW.md` §11.

## 1. Inspect the real source — not the abstract
- Open the **accession page** (`WebFetch` GEO/SRA/ENA/ArrayExpress/PRIDE/Zenodo, etc.).
- Read the **associated paper(s)** for cohort and design detail (use `ingest-source` if worth a full record).
- Check the actual **file manifest, sample metadata, and processed-data availability** — confirm a clear
  sample-to-file mapping, group labels, donor IDs, and batch variables. Note genome build / annotation
  version. Test-open or download to `08_INBOX/` if feasible.

## 2. Fill the template
Copy `00_AGENT/templates/DATASET_RECORD_TEMPLATE.md` to `03_DATASETS/<repository>_<accession>.md`.
Complete YAML (organism, tissue_or_model, modality, raw/processed availability, metadata_quality,
access) and body: sample structure with counts per group, covariates, batch/donor structure, access &
license terms.

## 3. Judge suitability honestly
State the proposed analysis and: exact inclusion criteria it satisfies, critical mismatches, minimum
preprocessing, whether it supports independent validation or pooling, harmonization needs, main
confounders, leakage risks, and expected statistical limitations. Give an overall suitability
(strong / conditional / weak). Do **not** recommend a dataset just because its title looks relevant.

## 4. Link, refresh catalog & report
Link to the projects, analyses, and syntheses it serves. Rebuild the retrieval index
(`python3 00_AGENT/tools/build_index.py`). Report the record path, priority, suitability verdict, and
next action (e.g. construct a sample sheet, request controlled access). Set `last_verified`.
