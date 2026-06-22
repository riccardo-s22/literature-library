---
name: expand-corpus
description: >
  Iteratively grow the LIBRARY paper corpus by searching the literature across the four topic domains,
  deduplicating against existing records, and ingesting the best new candidates. Has two modes: a
  one-off "deepen" pass (fill domains to a target depth regardless of date) and a recurring "monthly"
  pass (find literature published since the last run). Use when asked to expand/grow the corpus, do the
  monthly literature pass, or catch up on new papers.
---

# Expand the paper corpus

Goal: add genuinely relevant, *verified* records across the four domains — never bulk-import abstracts.
Every paper goes through the `ingest-source` discipline (real inspection, no fabrication, controlled
tags, `needs_full_text` + Unknown where the full text is inaccessible). Read `00_AGENT/CLAUDE.md`
(mode A + evidence rules) and `00_AGENT/CURRENT_LITERATURE_SIGNALS.md` before searching.

## Modes
- **monthly** (default for the scheduled run): only consider literature **published since the last run**.
- **deepen**: ignore dates; fill thinner domains up to the target depth using the strongest papers.

## 1. Establish the baseline (what's already here)
- Read `00_AGENT/EXPANSION_LOG.md` — the last run's date, queries, and per-domain counts. The new
  search window is `date_from = <last run date>` (monthly mode).
- Read `00_AGENT/index.csv` / `INDEX.md` for current per-domain coverage and every existing DOI/PMID.
  Build the dedup set from these IDs (and `Grep 02_PAPERS/ -i` for the DOI/PMID/title before writing).

## 2. Search each domain (per CURRENT_LITERATURE_SIGNALS)
For each of the four domains, run targeted queries with the PubMed tools (load schemas first via
ToolSearch: `select:mcp__claude_ai_PubMed__search_articles,mcp__claude_ai_PubMed__get_article_metadata,mcp__claude_ai_PubMed__get_full_text_article,mcp__claude_ai_PubMed__convert_article_ids`),
using `date_from`/`date_to` in monthly mode. For SWCNT/biosensor and pure-methods work that PubMed
indexes poorly, also use `WebSearch`/`WebFetch` (and arXiv/bioRxiv). Domains:
1. Neurodegeneration / brain aging / TBI–blast / ALS / AD–ADRD (TDP-43, tau, glia, organoid injury).
2. SWCNT & nanomaterial biosensors / spectral phenotyping / biofluid biomarkers.
3. Transcriptomics & single-cell / spatial / multi-omics & reproducible computational workflows.
4. Mechanobiology / ECM / neural injury / barriers / force signaling.

## 3. Triage before ingesting
Rank candidates by the prioritization reminder in the signals file (most likely to change a decision,
reveal a reusable dataset, strengthen validation, expose a failure mode, improve reproducibility).
Drop anything off-domain, duplicate, or low-relevance. **Default target: up to 3–5 new records per
domain per run**, Priority 1–2 first. Quality over volume — adding two strong records beats five weak ones.

## 4. Ingest the survivors
For each kept paper, follow `ingest-source`: verify identity + retraction/preprint status, inspect the
real source (PMC full text via the saved-file + `python3` slicing pattern; `jq` is NOT installed), fill
`PAPER_RECORD_TEMPLATE.md` into `02_PAPERS/<year>/`, controlled tags only, set `priority` and
`last_verified` to today. Mark `needs_full_text` + Unknown where access fails; never invent values.

## 5. Log, index, report
- Append a dated entry to `00_AGENT/EXPANSION_LOG.md`: run date, mode, search window, queries per domain,
  records ADDED (path + priority), and candidates SKIPPED with the one-line reason (so future runs don't
  re-assess them — this is the lightweight exclusion log).
- Rebuild the catalog: `python3 00_AGENT/tools/build_index.py`.
- Report: new total, per-domain counts, the added records, anything `needs_full_text`, and notable gaps
  to target next month.

## Guardrails
Stay within the four domains and the controlled vocabulary. Do not create projects, datasets, or
syntheses in this pass (separate skills). Do not re-ingest an existing record. If a run finds nothing
new worth adding, that is a valid outcome — log it and stop.
