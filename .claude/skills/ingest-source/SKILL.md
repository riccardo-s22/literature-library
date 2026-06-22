---
name: ingest-source
description: >
  Read a paper, preprint, protocol, or resource (from a PDF path, DOI, PMID, URL, or pasted text) and
  integrate it into the LIBRARY as a canonical paper record. Use whenever the user wants to "ingest",
  "add", "file", "log", or "extract" a source into the literature knowledge base.
---

# Ingest a source into the library

Goal: turn one source into a verified, linked record under `02_PAPERS/<year>/` using the canonical
template, following `00_AGENT/CLAUDE.md` (mode A) and `00_AGENT/MAINTENANCE_WORKFLOW.md`.

## 1. Read the source — actually inspect it
- **PDF on disk** → use the `Read` tool (it renders PDFs); read methods, figures, and supplement, not
  just the abstract.
- **DOI / PMID / PMCID** → resolve metadata with the PubMed tools
  (`mcp__claude_ai_PubMed__get_article_metadata`, `convert_article_ids`, `get_full_text_article`) or
  Scholar Gateway; fall back to `WebFetch` on the publisher/preprint page. Load schemas first with
  ToolSearch (e.g. `select:mcp__claude_ai_PubMed__get_article_metadata`).
- **URL** → `WebFetch` the page; if it is a PDF link, download to `08_INBOX/` and `Read` it.
- Record exactly what you inspected (full text? supplement? methods? code? data?) — never fill a record
  from title/abstract alone when it will influence a real decision; mark unseen items **needs_full_text**.

## 2. Verify identity (MAINTENANCE_WORKFLOW §2)
Confirm title, authors, venue, year, and canonical ID (DOI > PMID > accession > URL). Check for a
published version of a preprint, and for correction / expression of concern / retraction. Check
`02_PAPERS/` for an existing record (dedup keys: DOI, PMID, normalized title+author+year) — update it
rather than duplicating.

## 3. Extract into the template
Copy `00_AGENT/templates/PAPER_RECORD_TEMPLATE.md` to
`02_PAPERS/<year>/<firstauthor>_<year>_<short-topic>.md`. Fill the YAML and body. For each consequential
claim use one row of the findings table with figure/table/section location and effect size. Apply the
controlled tags in `00_AGENT/LIBRARY_STRUCTURE.md`. Label content **Reported / Derived / Inference /
Unknown**; never invent numbers, accessions, or conclusions. Capture limitations, leakage/batch/
pseudoreplication risks, negative findings, and transferability to the user's domains.

## 4. Link
Add links to relevant `01_PROJECTS/<slug>/` context, methods in `04_METHODS/`, datasets in
`03_DATASETS/`, related/contradictory papers, and any syntheses in `05_SYNTHESIS/`. If it changes a
project decision, note it for that project's `DECISIONS.md`.

## 5. Refresh the catalog & report
After writing the record, rebuild the retrieval index so it stays current:
`python3 00_AGENT/tools/build_index.py`. Then state the record path, `record_status`, priority (1/2/3)
with rationale, and the single most useful follow-up (e.g. inspect a missing supplement, add to a
synthesis, validate in an independent dataset). Set `last_verified` to today.
