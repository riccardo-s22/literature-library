---
record_type: paper
record_status: verified
canonical_id: "10.1038/s41467-025-56523-4"
doi: "10.1038/s41467-025-56523-4"
pmid: "39893194"
pmcid: "PMC11787318"
title: "Spatial integration of multi-omics single-cell data with SIMO"
year: 2025
source_type: primary
peer_reviewed: true
full_text_checked: false
supplement_checked: false
code_checked: false
data_checked: false
last_verified: 2026-06-22
priority: 2
projects: []
topics: [transcriptomics, single_cell, spatial_omics, multi_omics]
methods: [analysis_method, software, scRNAseq, spatial_transcriptomics]
datasets: []
---

# Citation
- Full citation: Yang P, Jin K, Yao Y, Jin L, Shao X, Li C, Lu X, Fan X. "Spatial integration of multi-omics single-cell data with SIMO." *Nature Communications* 2025;16(1):1265.
- DOI / PMID / stable URL: [DOI](https://doi.org/10.1038/s41467-025-56523-4) · PMID 39893194 · PMC11787318
- Related preprint or published version: Peer-reviewed (Nat Commun).
- Correction, expression of concern, or retraction status: **Unknown** — not checked beyond metadata (2026-06-22).

*Source: PubMed metadata + abstract (full text in PMC, not yet inspected). According to PubMed, DOI [10.1038/s41467-025-56523-4](https://doi.org/10.1038/s41467-025-56523-4).*

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Adds an **on-domain spatial multi-omics integration method** to the corpus's computational axis, replacing the off-domain kidney foundation-model slot ([[li_2025_nephrobase-cell-plus-foundation-model]]) and complementing the single-cell integration/feature-selection records ([[zappia_2025_feature-selection-scrnaseq-integration]], [[prieto-leon_2025_ruv-pseudobulk-scrnaseq]]). SIMO probabilistically aligns spatial transcriptomics with scRNA-seq and extends to chromatin accessibility and DNA methylation — modalities not previously co-profiled spatially.
- Why it is more or less useful than neighboring literature: Goes beyond transcriptome-only spatial mapping to multi-omic spatial integration with benchmarking on simulated data — directly relevant for spatial brain/injury multi-omics analyses.

# Source inspection status
- Abstract inspected: yes
- Full text inspected: no (available in PMC — promote after inspection)
- Methods inspected: no
- Supplement / figures / code / data inspected: no
- Missing material: probabilistic-alignment model details, benchmark competitors/metrics, runtime/scaling, exact datasets, code/repo link.

# Study question and hypothesis
- Primary question: Can multi-omics single-cell data be integrated into spatial coordinates via probabilistic alignment, beyond scRNA-seq↔ST?
- Stated hypothesis: A probabilistic alignment can place multiple single-cell modalities (RNA, ATAC, methylation) into spatial context accurately and robustly.
- Study type: Computational method development + benchmarking (simulated + real datasets).

# Biological or clinical context
- Disease / exposure / process: Method (tissue-agnostic).
- Organism / tissue: Multiple (real-world datasets; not enumerated here).
- Model system: Spatial transcriptomics + single-cell multi-omics.
- Cohort or population: N/A.

# Study design
- Experimental/observational unit: Cells/spots across modalities.
- Groups / comparators: Benchmarked vs prior integration tools (names not extracted) on simulated datasets (ground-truth accuracy/robustness).
- Validation: Simulation benchmarks + biological application (topological cell patterns, multi-omic regulatory modes).

# Experimental / computational methods
- Assay / platform: Computational — SIMO (Spatial Integration of Multi-Omics) via probabilistic alignment.
- Inputs: ST + scRNA-seq (+ scATAC, sc methylation).
- Primary endpoint: Alignment accuracy/robustness (simulated); recovery of spatial multimodal heterogeneity (real data).
- Validation strategy: Simulated ground truth; biological plausibility on real data.
- External validation: Multiple real datasets (not enumerated).
- Software / code availability: SIMO released as a tool (repo link **not extracted** — confirm in full text).
- Exact reusable parameters and source location: **needs full text** — model/priors, benchmark metrics, datasets.

# Data and resource availability
- Repository and accession: **Unknown** (not inspected; check Code/Data Availability in PMC).
- Reusability for the user's work: Potentially high for spatial multi-omics projects — conditional on confirming code/inputs.

# Main findings
| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| SIMO integrates ST with scRNA-seq and extends to ATAC + methylation | Reported | Abstract | qualitative capability | Yes | full-text metrics not extracted |
| High accuracy/robustness on simulated benchmarks | Reported | Abstract | qualitative (vs prior tools) | Partial | competitors/metrics not extracted |
| Reveals multimodal spatial heterogeneity + regulatory modes in real data | Reported | Abstract | qualitative | Yes | datasets not enumerated |

# What is actually new?
- Methodological novelty: Spatial placement of multiple single-cell modalities (incl. methylation/ATAC) via probabilistic alignment.
- Dataset/resource novelty: SIMO software.
- What was already known: scRNA-seq↔ST mapping tools exist; multi-omic spatial co-placement was limited.

# Strengths / Limitations
- Strengths: Multi-modal scope; simulation benchmarking; published in Nat Commun.
- Limitations: Benchmark breadth and real-data generalizability need full-text check; method assumptions (alignment priors) unverified here.

# Transferability to the user's work
- Directly transferable elements: Spatial multi-omics integration for brain/injury ST + scRNA/scATAC datasets.
- Elements requiring adaptation: Tissue-specific tuning; verify performance on neural tissue.
- Mismatch: Demo tissues vs neural-injury context.
- Confidence: moderate (pending full-text/benchmark inspection).

# Practical implications
- Analysis implication: Candidate for placing snRNA/snATAC neural data into spatial context (cf. [[ruf_2026_celltype-tdp43-motor-cortex]], [[li_2023_c9orf72-snrna-snatac-als-ftd]]).
- Public dataset implication: Pairs with spatial brain datasets for validation.

# Contradictions and links
- Supports: Reusable spatial-integration methods (cf. [[zappia_2025_feature-selection-scrnaseq-integration]]).
- Methodologically comparable papers: [[yang_2026_fgot-spatial-interpretable-integration]] (interpretable integration), zappia_2025.
- Relevant synthesis notes: seed for "spatial multi-omics integration methods."

# Follow-up actions
- [ ] Inspect PMC full text + Code/Data Availability; extract benchmarks, competitors, repo
- [ ] Test on a neural ST + scRNA dataset
- [ ] Confirm correction/retraction status
- [ ] Promote to full_text_checked

# Priority decision
- Priority: 2
- Retain for methods (spatial multi-omics integration)
- Rationale: On-domain, published spatial multi-omics method that replaces the off-domain kidney foundation-model slot; needs full-text benchmark verification.
