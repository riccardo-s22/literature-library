---
name: library-maintenance
description: >
  Run the library upkeep pass — deduplication, version/preprint linking, staleness review, retraction
  and correction checks, dataset-availability re-verification, and synthesis refresh. Use for "audit",
  "clean up", "check for retractions", or "update" the literature library.
---

# Maintain the library

Goal: keep records canonical, current, and trustworthy. Follows `00_AGENT/MAINTENANCE_WORKFLOW.md`
(steps 7–13). Scope the pass with the user (whole library, one project, or high-priority records only).

## Checks
1. **Deduplicate** — match on DOI, then PMID/PMCID, then accession, then normalized title+author+year.
   Merge notes into the canonical record; preserve unique provenance. (`Grep`/`Glob` to find dupes.)
2. **Version handling** — link preprints to published versions; mark the canonical one; preserve
   meaningful changes in cohort/analysis/conclusions; never silently replace a cited version.
3. **Staleness** — surface records informing active decisions whose `last_verified` is old, datasets/
   software that may have changed, preprints that may now be published, and fields with a new
   benchmark/atlas/guideline.
4. **Retraction & correction control** — for priority-1 sources, check for retraction, correction,
   expression of concern, or major critique (PubMed tools / `WebFetch` the publisher & Retraction Watch).
   On any status change, update `record_status` and every linked synthesis and `DECISIONS.md`.
5. **Dataset re-verification** — confirm accession & file availability, annotation/build, and
   controlled-access changes for datasets in use.
6. **Synthesis refresh** — re-open syntheses with unresolved watchlist items or new decision-relevant
   evidence; mark them `needs_update` if you cannot fully refresh now.
7. **Exclusion log** — record sources excluded (irrelevant, duplicate, unverifiable, fatally flawed,
   retracted, misleading) so they are not reassessed repeatedly.

8. **Rebuild the catalog** — after any record changes, regenerate the retrieval index:
   `python3 00_AGENT/tools/build_index.py` (writes `INDEX.md` and `00_AGENT/index.csv`). Use the index's
   "Oldest verification dates" section to drive the next staleness pass.

## Report
List changes made, records needing user input, status changes that affect decisions, and stamp updated
`last_verified` / `last_updated` dates. Confirm the catalog was rebuilt. Make no claim of having checked
an external source you did not actually open.
