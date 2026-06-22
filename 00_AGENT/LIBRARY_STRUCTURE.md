# Literature Library Structure

## Recommended folders

```text
00_AGENT/
  CLAUDE.md
  CURRENT_LITERATURE_SIGNALS.md
  LIBRARY_STRUCTURE.md
  MAINTENANCE_WORKFLOW.md
  templates/

01_PROJECTS/
  <project_slug>/
    PROJECT_CONTEXT.md
    DECISIONS.md
    OPEN_QUESTIONS.md
    project_syntheses/

02_PAPERS/
  <year>/
    <first_author>_<year>_<short_title>.md

03_DATASETS/
  <repository>_<accession>.md

04_METHODS/
  experimental/
  computational/
  protocols/
  software/

05_SYNTHESIS/
  biological_questions/
  methods_comparisons/
  dataset_landscapes/
  evidence_gaps/

06_CONCEPTS/
  genes_pathways/
  biomarkers/
  cell_types/
  exposures_stressors/
  endpoints/

07_WATCHLIST/
  preprints/
  new_datasets/
  emerging_methods/

08_INBOX/

09_ARCHIVE/
```

## Design principle
Store each source once, then link it into projects and syntheses. Avoid copying the same paper summary into multiple project folders.

## Canonical identifiers
Use the first available stable identifier in this order:
1. DOI
2. PMID or PMCID
3. repository accession
4. trial or protocol identifier
5. stable publisher or institutional URL

A preprint and its peer-reviewed version should be linked as related versions, not treated as unrelated evidence.

## File naming
- Paper: `firstauthor_year_short-topic.md`
- Dataset: `repository_accession.md`
- Method: `method_short-name.md`
- Synthesis: `question_short-name_YYYY-MM-DD.md`
- Project: stable human-readable slug, such as `als_spectral_biomarkers` or `blast_tbi_organoid_mechanics`

Do not encode the entire title in the filename.

## Required YAML metadata for paper records

```yaml
record_type: paper
record_status: verified | partial | needs_full_text | superseded | retracted
canonical_id: ""
doi: ""
pmid: ""
title: ""
year: 0
source_type: primary | review | method | benchmark | protocol | resource | preprint
peer_reviewed: true | false
full_text_checked: true | false
supplement_checked: true | false
code_checked: true | false
data_checked: true | false
last_verified: YYYY-MM-DD
priority: 1 | 2 | 3
projects: []
topics: []
methods: []
datasets: []
```

## Required YAML metadata for dataset records

```yaml
record_type: dataset
record_status: verified | partial | restricted | unavailable | superseded
repository: ""
accession: ""
title: ""
organism: ""
tissue_or_model: ""
modality: []
raw_data_available: true | false | unknown
processed_data_available: true | false | unknown
metadata_quality: high | moderate | low | unknown
access: open | controlled | mixed | unavailable
last_verified: YYYY-MM-DD
priority: 1 | 2 | 3
projects: []
topics: []
```

## Controlled tag families
Use a small controlled vocabulary, supplemented by free-text keywords only when needed.

### Domain
- neurodegeneration
- aging
- TBI
- ALS
- AD_ADRD
- biosensors
- nanomaterials
- mechanobiology
- transcriptomics
- single_cell
- spatial_omics
- multi_omics

### Evidence type
- primary_study
- review
- method
- benchmark
- protocol
- atlas
- dataset
- software
- preprint

### Model
- human_cohort
- patient_derived_cells
- iPSC
- organoid
- animal_model
- cell_line
- ex_vivo
- controlled_exposure

### Data modality
- bulk_RNAseq
- snRNAseq
- scRNAseq
- spatial_transcriptomics
- proteomics
- lipidomics
- metabolomics
- spectroscopy
- imaging
- physiological_endpoints

### Utility
- experiment_design
- protocol_parameter
- analysis_method
- public_dataset
- external_validation
- biomarker
- mechanism
- translational_constraint
- negative_evidence

## Links between records
Use relative links when possible. Link papers to:
- datasets they generated or reused;
- methods or software they introduced;
- project contexts they inform;
- syntheses in which they are compared;
- related versions, corrections, or replications.

## Decision log
Each project should have a `DECISIONS.md` file. Record:
- date;
- decision;
- evidence used;
- alternatives considered;
- unresolved risks;
- conditions that would trigger revision.

This prevents the library from repeatedly reopening settled questions without new evidence.
