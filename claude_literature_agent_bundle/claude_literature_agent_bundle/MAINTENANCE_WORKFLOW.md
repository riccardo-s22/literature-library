# Literature Library Maintenance Workflow

## 1. Intake
Place new citations, PDFs, links, datasets, protocols, and notes in `08_INBOX/`.
For each item, record at minimum:
- stable identifier or URL;
- date added;
- reason it was added;
- likely project or topic;
- source type.

Do not create a full record from title or abstract alone when the source will influence an experimental or analytical decision.

## 2. Verify identity
Before extraction:
- confirm title, authors, venue, year, DOI or accession;
- check whether a preprint has a published version;
- check for correction, expression of concern, or retraction;
- identify duplicate records.

## 3. Triage
Assign:
- project links;
- topic tags;
- source type;
- Priority 1, 2, or 3;
- record status: verified, partial, needs full text, superseded, restricted, or excluded.

Priority 1 items receive full extraction first.

## 4. Extract
Use the appropriate template.
For consequential claims, record the figure, table, supplement, page, or methods section.
Capture negative findings and failed validation, not only positive conclusions.

## 5. Link
Connect the record to:
- project context;
- relevant method;
- generated or reused dataset;
- synthesis notes;
- related or contradictory papers;
- decision log entries.

## 6. Synthesize
Create or refresh a synthesis when:
- at least three sources address the same decision-relevant question;
- evidence conflicts;
- a new benchmark or major dataset changes the landscape;
- a grant, experiment, or analysis requires a defensible evidence summary.

## 7. Deduplicate
Primary match keys:
1. DOI;
2. PMID / PMCID;
3. accession;
4. normalized title + first author + year.

Merge annotations into the canonical record. Preserve unique notes and provenance.

## 8. Version handling
- Link preprint and published article.
- Mark the publication as canonical when appropriate.
- Preserve meaningful changes in cohort, analysis, conclusions, or supplementary data.
- Do not silently replace a cited version if conclusions changed.

## 9. Staleness review
Review records when:
- they inform an active decision and have not been verified recently;
- a dataset or software resource may have changed;
- a preprint may now be published;
- a field has a new benchmark, guideline, atlas, or consensus statement;
- a synthesis contains unresolved watchlist items.

The date of last verification must be visible in each canonical record.

## 10. Retraction and correction control
For high-priority sources, periodically check for:
- retraction;
- correction;
- expression of concern;
- major post-publication critique;
- replacement dataset or code release.

If status changes, update all linked syntheses and decisions.

## 11. Dataset maintenance
For datasets used or recommended:
- verify accession and file availability;
- preserve the downloaded manifest and metadata version;
- record the genome build, annotation, and processing provenance;
- note controlled-access changes;
- keep project-specific sample sheets separate from the canonical dataset record.

## 12. Quality audit
A complete high-priority record should answer:
- What was tested?
- In what model and with how many independent units?
- What exact method and parameters were used?
- What was the quantitative result?
- How was it validated?
- What are the key limitations?
- What data or code are available?
- What decision does this source change?

If any answer is unknown, mark it unknown rather than inferring it silently.

## 13. Exclusion log
Keep a short record of sources excluded because of:
- irrelevance;
- duplicate publication;
- inaccessible or unverifiable data;
- fatal design limitation;
- retraction;
- misleading title or abstract;
- no meaningful applicability.

This avoids repeatedly reassessing the same unsuitable source.
