---
name: recall
description: >
  Retrieve knowledge from the LIBRARY archive — find the records relevant to a question, topic, gene,
  method, dataset, organism, or project and return them ranked, with paths. Use whenever the user asks
  "what do we have on…", "find records about…", "which papers/datasets cover…", or needs to pull
  existing evidence before answering. This is the read/retrieval entry point to the knowledge base.
---

# Recall knowledge from the archive

Goal: return the smallest set of genuinely relevant records, ranked, each with its path — so the user
(or a downstream answer) can go straight to the evidence. Retrieve before reasoning; never answer a
library question from memory when a record may exist.

## 1. Start from the catalog
Read `INDEX.md` at the library root — it lists every record (grouped by type, sorted by priority) and
has a **Topic index** (tag → records) and a staleness watch. This is the fastest entry point.
If `INDEX.md` is missing or looks out of date, rebuild it first:
`python3 00_AGENT/tools/build_index.py`. For structured filtering, `00_AGENT/index.csv` has one row
per record (type, year, priority, status, topics, ids, path).

## 2. Translate the request into the controlled vocabulary
Map the user's words to the tag families in `00_AGENT/LIBRARY_STRUCTURE.md` (domain, evidence type,
model, data modality, utility). Search both the controlled tags and free-text synonyms.

## 3. Search the records
- **By tag / metadata** → the Topic index in `INDEX.md`, or filter `index.csv`.
- **By full text** → `Grep` across `02_PAPERS/ 03_DATASETS/ 04_METHODS/ 05_SYNTHESIS/ 06_CONCEPTS/ 01_PROJECTS/`
  for genes, methods, accessions, or phrases. Grep the YAML keys too (e.g. `topics:`, `doi:`, `organism:`).
- **By relationship** → follow the `Contradictions and links` / `Linked records` sections to pull
  related, contradictory, or superseding records.

## 4. Rank and return
Order by: direct relevance → Priority (1>2>3) → record_status (verified > partial) → recency
(`last_verified`). For each hit return: title, type, priority, status, one-line why-it-matches, and the
clickable `path`. Prefer 3–8 strong hits over an exhaustive dump. Surface conflicting evidence rather
than just the agreeing records.

## 5. Report gaps honestly
If nothing in the archive covers the request, say so plainly and suggest the next action (e.g.
`/find-datasets`, `/ingest-source`, or a web search) — an empty result is a valid answer, not a prompt
to invent records. Note any matched records whose `last_verified` is stale.
