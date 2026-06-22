---
record_type: paper
record_status: verified
canonical_id: "10.1038/s41592-025-02624-3"
doi: "10.1038/s41592-025-02624-3"
pmid: "40082610"
pmcid: "PMC11978513"
title: "Feature selection methods affect the performance of scRNA-seq data integration and querying"
year: 2025
source_type: benchmark
peer_reviewed: true
full_text_checked: true
supplement_checked: false
code_checked: false
data_checked: true
last_verified: 2026-06-22
priority: 2
projects: []
topics: [transcriptomics, single_cell, multi_omics, spatial_omics]
methods: [analysis_method, scRNAseq, snRNAseq]
datasets: []
---

# Citation
- Full citation: Zappia L, Richter S, Ramírez-Suástegui C, Kfuri-Rubens R, Vornholz L, Wang W, Dietrich O, Frishberg A, Luecken MD, Theis FJ. "Feature selection methods affect the performance of scRNA-seq data integration and querying." *Nature Methods* 2025;22(4):834-844.
- DOI / PMID / stable URL: [DOI](https://doi.org/10.1038/s41592-025-02624-3) · PMID 40082610 · PMC11978513
- Related preprint or published version: Peer-reviewed (Nat Methods), open access.
- Correction, expression of concern, or retraction status: **Unknown** — not checked (added 2026-06-22).

*Source: metadata + PMC full text retrieved from PubMed / PubMed Central. According to PubMed, DOI [10.1038/s41592-025-02624-3](https://doi.org/10.1038/s41592-025-02624-3).*

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: A **benchmark of >20 feature-selection methods** for scRNA-seq integration and atlas querying, evaluated not just on batch correction + bio-conservation but also on **query-to-reference mapping, label transfer, and detection of unseen populations**. Directly informs the signals-file priorities "single-cell reference mapping and spatial integration" and "benchmarks that expose batch/transferability limits." Decision-relevant for anyone building or mapping onto reference atlases (e.g., mapping ALS/AD nuclei onto cortical references).
- Why it is more or less useful than neighboring literature: Goes beyond prior integration benchmarks (which fixed feature selection) to isolate feature selection as the variable, and adds query/atlas-mapping metrics — exposing that good reference integration does not guarantee good handling of novel query biology. Practical guidance: highly-variable-gene (HVG) selection (Seurat-VST) is robust; supervised (Wilcoxon) can top scores but is dataset-variable. Limitation: scRNA-seq human/mouse tissue atlases, not spatial or brain-specific per se.

# Source inspection status
- Abstract inspected: yes
- Full text inspected: yes (PMC full text, ~64k chars)
- Methods inspected: yes (metric categories, method list, datasets, integration models)
- Supplement inspected: no (Supplementary Methods / Reporting Summary referenced)
- Figures/tables inspected: no (callouts read; panels not viewed)
- Code repository inspected: no (data/code availability behind the Nature article link; repo URL not in retrieved text)
- Data repository inspected: partial — uses public atlases (HLCA, Reed breast, Human endoderm/lung, etc.); specific accessions not re-extracted.
- Missing material: exact code/data-availability URLs (in Nature online content), full metric definitions (Supplementary Methods), per-dataset effect tables.

# Study question and hypothesis
- Primary question: How do different feature-selection methods affect scRNA-seq sample integration AND the downstream use of the integrated reference for querying (mapping, label transfer, detecting unseen populations)?
- Stated hypothesis: Feature selection is a consequential, under-evaluated preprocessing step; the choice affects both reference integration quality and the model's ability to handle novel query biology.
- Study type: Computational benchmark across multiple datasets, integration models, and metric categories.

# Biological or clinical context
- Disease / exposure / process: Methodological (atlas building / reference mapping); tissues include lung (HLCA), breast (Reed), endoderm, immune/epithelial compartments.
- Organism: Human and mouse (per MeSH).
- Tissue / cell type: Multiple tissue atlases and compartments (HLCA full/immune/epithelial; Reed breast; Human endoderm; others).
- Model system: Public reference atlases + query datasets.
- Cohort or population: N/A (benchmark datasets).

# Study design
- Experimental or observational unit: Dataset × feature-selection method × integration model combination.
- Unit of inference: Method performance ranking per metric category and overall.
- Groups and sample size per group: >20 feature-selection methods (with variants); multiple datasets (HLCA and subsets, Reed breast, Human endoderm, lung, etc.); default 200 features for most methods (some dynamically select fewer).
- Biological replicates: Multiple datasets serve as replication across tissues.
- Randomization / blinding: N/A.
- Inclusion / exclusion criteria: Some methods failed to run on some datasets (NBumi on Reed breast >24h; scPNMF >400 GB or >24h on HLCA/HLCA immune/epithelial/Human endoderm/Reed breast; Anticor errored on Human endoderm) — reported transparently.
- Batch structure: Integration evaluated for batch removal vs bio-conservation explicitly.
- Controls and comparators: Multiple integration backends (scVI; scANVI; others) and feature-selection variants compared.

# Experimental methods
- Assay / platform: In silico benchmark of scRNA-seq preprocessing/integration.
- Primary endpoint: Overall and per-category method performance across 5 metric categories: (1) batch-effect removal, (2) conservation of biological variation, (3) query-to-reference mapping quality, (4) label-transfer quality, (5) detection of unseen populations.
- Secondary endpoints: Effect of number of features; batch-aware feature selection; lineage-specific selection; method-set overlap (Jaccard); consistency across integration models.
- Exact reusable parameters and source location: 200 features as default for most methods; dynamic-selection methods (Anticor, DUBStepR, NBumi, Seurat-MVP, triku) and scPNMF use fewer; integration via scVI (primary ranking) and scANVI.

# Computational and statistical methods
- Raw input: scRNA-seq count matrices (reference + query) from public atlases.
- Preprocessing: Feature selection by each method (>20, with variants); integration with scVI/scANVI etc.
- Statistical model: scIB-style integration metrics; overall scores aggregated and ranked across datasets; method similarity by Jaccard overlap of selected feature sets.
- Multiple-testing correction: N/A (benchmark ranking).
- Effect-size reporting: Mean overall scores and rankings; Seurat-VST highest overall ranking; Wilcoxon (supervised, uses labels) highest mean but more variable; triku competitive but batch-biased.
- Validation strategy: Cross-dataset consistency; multiple integration backends; query/label-transfer/unseen-population tasks.
- External validation: Multiple independent atlases.
- Software and versions: scVI, scANVI, >20 feature-selection tools; figures in ggplot2 v3.5.0, patchwork v1.2.0, tidyverse v2.0.0. Other versions in Supplementary Methods.
- Code availability: Stated as available via the Nature online-content data/code-availability section (URL not in retrieved text).

# Data and resource availability
- Repository and accession: Public atlases (HLCA, Reed breast, Human endoderm/lung, etc.); specific accessions in the Nature data-availability statement (not re-extracted).
- Raw data available: Yes (public atlases).
- Processed data available: Yes (benchmark pipeline; via online content).
- Metadata completeness: High (established atlases).
- Data-use restrictions: Generally open (atlas-specific terms).
- Reusability for the user's work: **High** — actionable feature-selection guidance + benchmark code for reference-mapping pipelines.

# Main findings
| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| Feature selection materially affects integration AND downstream query/atlas-mapping performance | Reported | Results | across 5 metric categories | Yes | scRNA-seq atlases |
| HVG selection (Seurat-VST) is robust and top-ranked overall | Reported | Results / Fig | highest overall ranking, consistent | Yes | scVI ranking |
| Supervised Wilcoxon (label-based) has highest mean score but is dataset-variable | Reported | Results | highest mean, higher variance | Partial | May need per-dataset tuning |
| triku competitive but biased toward batch correction over bio-conservation | Reported | Results | category tradeoff | Yes | — |
| Good reference integration does not guarantee good handling of novel query biology | Reported/Inference | Main/Results | motivates query-aware metrics | Yes | conceptual but evidenced |
| Several methods fail on large atlases (memory/time) | Reported | Results | scPNMF >400GB; NBumi >24h | Yes | practical scalability limits |

# What is actually new?
- Methodological novelty: First systematic benchmark of feature selection specifically for integration *and* query/atlas-mapping, with unseen-population detection and label-transfer metrics.
- Biological novelty: N/A (methods/benchmark).
- Dataset or resource novelty: Reusable feature-selection benchmark + guidance for atlas analysts.
- What was already known: HVGs generally help integration (prior single-method benchmarks); ~250 integration tools exist.

# Strengths
- Design strength: Multiple datasets, integration backends, and metric categories; isolates feature selection as the variable.
- Validation strength: Query-aware metrics (mapping, label transfer, unseen populations) beyond batch/bio-conservation.
- Reproducibility strength: Public atlases; documented tool versions; code via Nature online content.
- Translational realism: Large real atlases (HLCA) with scalability reporting.

# Limitations and bias risks
- Sample-size / power: Finite set of datasets/tissues; brain not a focus.
- Confounding: Integration-model choice interacts with feature selection (addressed by testing multiple backends).
- Batch / site effects: The object of study.
- Pseudoreplication risk: N/A.
- Leakage / overfitting risk: Supervised (Wilcoxon) uses labels also used in evaluation — flagged by authors as variable/possibly optimistic.
- Generalizability: scRNA-seq human/mouse tissue atlases; spatial and brain-specific transfer not directly tested.
- Missing controls / validation: Spatial-omics integration not benchmarked.
- Author-stated limitations: Supervised selection may not generalize; some methods unscalable.
- Additional limitations identified during review: Exact code/data URLs and full metric definitions in supplement (not inspected).

# Transferability to the user's work
- Directly transferable elements: Default to Seurat-VST HVGs for robust integration/mapping; evaluate query-mapping and unseen-population detection, not just batch removal; be cautious with supervised feature selection; mind scalability on large atlases.
- Elements requiring adaptation: Apply/validate on brain snRNA-seq and spatial data (not directly benchmarked).
- Model, species, tissue, matrix, platform, or scale mismatch: General tissue atlases vs brain/spatial; scRNA vs snRNA.
- Assumptions required for transfer: Comparable atlas-mapping workflow (scVI/scANVI-style).
- Confidence: moderate-high for general guidance; moderate for brain/spatial transfer.

# Practical implications
- Experimental implication: N/A (computational).
- Analysis implication: Choose feature selection deliberately (Seurat-VST as a robust default); report query-mapping/label-transfer/unseen-population metrics when building or mapping onto references.
- Public dataset implication: Reusable benchmark + atlases for pipeline validation.
- Biomarker / translational implication: Better atlas mapping → more reliable cell-type assignment for downstream biomarker work.
- Grant / manuscript implication: Citable justification for feature-selection choices in atlas/reference-mapping pipelines.

# Contradictions and links
- Supports: HVG superiority for integration (now across many methods); query-aware evaluation.
- Contradicts: Assumption that feature selection is a negligible preprocessing choice; that integration quality alone predicts query performance.
- Replicates: Extends prior single-method HVG benchmarks.
- Methodologically comparable papers: ProjectSVR (reference mapping) and Acera-Mateos 2025 (multimodal integration benchmark) — both candidate companions; Prieto León 2025 (donor-aware DE downstream); Ruf 2026 / Leng 2021 (snRNA atlases that would be mapped).
- Relevant synthesis notes: candidate for a "single-cell integration / reference-mapping best practices" methods synthesis.
- Relevant project decisions: (none yet)

# Follow-up actions
- [ ] Extract code/data-availability URLs and full metric definitions from Nature online content + Supplementary Methods
- [ ] Validate Seurat-VST guidance on a brain snRNA-seq atlas-mapping task
- [ ] Consider a methods record for the integration/feature-selection workflow
- [ ] Check retraction/correction status

# Priority decision
- Priority: 2
- Retain for methods + external validation
- Rationale: Decision-relevant benchmark that changes a concrete preprocessing choice (feature selection) for atlas integration/reference mapping and adds query-aware metrics; Priority 2 because it is general-tissue (not brain/spatial specific) and the headline guidance still needs a quick brain-data check.
