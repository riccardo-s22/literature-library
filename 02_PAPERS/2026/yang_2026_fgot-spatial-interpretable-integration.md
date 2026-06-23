---
record_type: paper
record_status: verified
canonical_id: "10.1016/j.cels.2025.101479"
doi: "10.1016/j.cels.2025.101479"
pmid: "41643671"
title: "Interpretable data integration for single-cell and spatial multi-omics"
year: 2026
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
- Full citation: Yang C, He Z, Nie Q, Zhang L. "Interpretable data integration for single-cell and spatial multi-omics." *Cell Systems* 2026;17(2):101479.
- DOI / PMID / stable URL: [DOI](https://doi.org/10.1016/j.cels.2025.101479) · PMID 41643671
- Related preprint or published version: Peer-reviewed (Cell Systems); transparent peer-review record included in supplement.
- Correction, expression of concern, or retraction status: **Unknown** — not checked beyond metadata (2026-06-22).

*Source: PubMed metadata + abstract (full text not inspected). According to PubMed, DOI [10.1016/j.cels.2025.101479](https://doi.org/10.1016/j.cels.2025.101479).*

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Adds an **interpretable** single-cell/spatial multi-omics integration method (FGOT) that, unlike latent-space-only tools, also recovers gene↔regulatory-element links per cell state — complementing [[yang_2025_simo-spatial-multiomics-integration]] (probabilistic placement) and [[zappia_2025_feature-selection-scrnaseq-integration]]. Distinct first-author "Yang" from SIMO record (Chenghui Yang, Wuhan; vs Penghui Yang, Zhejiang).
- Why it is more or less useful than neighboring literature: Targets the interpretability gap (regulatory-link inference + post hoc interpretability for existing integration methods), works on paired/unpaired sc and paired spatial multi-omics — useful for mechanistic regulatory analysis, not just embedding.

# Source inspection status
- Abstract inspected: yes
- Full text inspected: no
- Methods inspected: no
- Supplement / figures / code / data inspected: no (transparent peer-review record noted as available)
- Missing material: FGOT (feature-guided optimal transport) formulation, benchmark datasets/competitors, accuracy metrics, code/repo link.

# Study question and hypothesis
- Primary question: Can integration of single-cell/spatial multi-omics simultaneously align modalities and reveal interpretable transcriptional regulatory links?
- Stated hypothesis: A feature-guided optimal-transport method can recover cell heterogeneity and state-specific gene–regulatory-element links that latent-alignment methods miss.
- Study type: Computational method development + benchmarking/validation.

# Biological or clinical context
- Disease / exposure / process: Method (tissue-agnostic; disease screening of regulatory elements demonstrated).
- Organism / tissue: Multiple (human/animal; not enumerated).
- Model system: Paired/unpaired single-cell multi-omics; paired spatial multi-omics.
- Cohort or population: N/A.

# Study design
- Experimental/observational unit: Cells/features across modalities.
- Comparators / validation: Benchmarked and validated via histone-modification data and 3D-genomics data (regulatory-link ground truth); robustness/accuracy in integration + inference.

# Experimental / computational methods
- Assay / platform: Computational — **FGOT (feature-guided optimal transport)**; provides post hoc interpretability for existing integration methods.
- Inputs: Paired/unpaired single-cell multi-omics; paired spatial multi-omics.
- Primary endpoint: Integration accuracy + transcriptional regulatory-link inference.
- Validation strategy: Histone-modification and 3D-genomics data as orthogonal validation.
- Software / code availability: FGOT (repo link **not extracted** — confirm in full text).
- Exact reusable parameters and source location: **needs full text** — OT formulation, benchmarks, datasets.

# Data and resource availability
- Repository and accession: **Unknown** (not inspected).
- Reusability for the user's work: Potentially high for regulatory-link inference in spatial/sc multi-omics — conditional on confirming code/inputs.

# Main findings
| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| FGOT jointly integrates and infers gene–regulatory-element links | Reported | Abstract | qualitative capability | Yes | formulation/metrics not extracted |
| Provides post hoc interpretability for existing integration methods | Reported | Abstract | qualitative | Yes | — |
| Robust/accurate vs histone-mark and 3D-genomics validation | Reported | Abstract | qualitative | Partial | metrics/competitors not extracted |
| Enables state/location-specific regulatory-element screening in disease | Reported | Abstract | qualitative | Yes | datasets not enumerated |

# What is actually new?
- Methodological novelty: Feature-guided OT recovering interpretable regulatory links alongside alignment; post hoc interpretability layer.
- Dataset/resource novelty: FGOT software.
- What was already known: Latent-space integration methods exist but obscure gene–regulatory connections.

# Strengths / Limitations
- Strengths: Interpretability focus; orthogonal validation (histone marks, 3D genomics); handles unpaired data; published in Cell Systems with transparent review.
- Limitations: Benchmark breadth/competitors and neural-tissue performance need full-text check; OT assumptions unverified here.

# Transferability to the user's work
- Directly transferable elements: Interpretable regulatory-link inference for brain sc/spatial multi-omics; post hoc interpretability for prior integrations.
- Elements requiring adaptation: Neural-tissue tuning; verify on snATAC+snRNA neural data.
- Mismatch: Demo tissues vs neural-injury context.
- Confidence: moderate (pending full-text/benchmark inspection).

# Practical implications
- Analysis implication: Infer cell-state-specific regulatory links in ALS/AD cortex multi-omics (cf. [[li_2023_c9orf72-snrna-snatac-als-ftd]], [[ruf_2026_celltype-tdp43-motor-cortex]]).
- Public dataset implication: Pairs with histone-mark/3D-genomics resources for validation.

# Contradictions and links
- Supports: Reusable, interpretable integration methods (cf. [[yang_2025_simo-spatial-multiomics-integration]], [[zappia_2025_feature-selection-scrnaseq-integration]]).
- Methodologically comparable papers: yang_2025 (SIMO), zappia_2025.
- Relevant synthesis notes: seed for "spatial multi-omics integration methods."

# Follow-up actions
- [ ] Inspect full text + Code/Data Availability; extract OT method, benchmarks, repo
- [ ] Test interpretable regulatory-link inference on neural snRNA+snATAC data
- [ ] Confirm correction/retraction status
- [ ] Promote to full_text_checked

# Priority decision
- Priority: 2
- Retain for methods (interpretable sc/spatial integration)
- Rationale: On-domain, published method adding interpretability/regulatory-link inference to the integration toolkit; needs full-text verification.
