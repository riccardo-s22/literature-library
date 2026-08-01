---
record_type: paper
record_status: partial
canonical_id: "10.1126/science.adz1652"
doi: "10.1126/science.adz1652"
pmid: "42490473"
title: "Single-cell multiomics connects 3D genome and transcriptome alterations in Alzheimer's disease"
year: 2026
source_type: primary
peer_reviewed: true
full_text_checked: false
supplement_checked: false
code_checked: false
data_checked: false
last_verified: 2026-08-01
priority: 1
projects: []
topics:
  - neurodegeneration
  - AD_ADRD
  - single_cell
  - multi_omics
  - transcriptomics
methods:
  - snRNAseq
  - analysis_method
  - spatial_transcriptomics
datasets: []
---

# Citation
- Full citation: Zhang Y, Lu X, Kunisky AK, Alam S, Tang J, Zhang R, Wang S, Zhang H, Baroudi J, Ichcho W, Jia D, Ghorbanikalateh S, Ghorbanikalateh S, Wang S, Bennett DA, Mathys H, Duan Z, Ma J. Single-cell multiomics connects 3D genome and transcriptome alterations in Alzheimer's disease. *Science*. 2026;393(6809):eadz1652.
- DOI / PMID / stable URL: https://doi.org/10.1126/science.adz1652 | PMID 42490473
- Related preprint or published version: None identified in this pass
- Correction, expression of concern, or retraction status: None identified as of 2026-08-01

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Introduces GAGE-seq, a new single-cell multi-omics method that jointly profiles gene expression and 3D chromatin architecture in individual cells; applied to human AD postmortem brain. Relevant to any single-cell or multi-omics analysis of neurodegeneration and to methods benchmarking for single-cell epigenomics.
- Why it is more or less useful than neighboring literature: Adds a previously missing dimension (3D genome organization) to single-cell AD profiling; Hicformer deep learning framework for predicting gene expression from 3D genome is a novel computational tool. Complements snRNA-seq and snATAC-seq papers in the library (Li 2023, Ruf 2026).

# Source inspection status
- Abstract inspected: Yes
- Full text inspected: No (Science paywalled; PMC accession not identified in this pass)
- Methods inspected: No
- Supplement inspected: No
- Figures/tables inspected: No
- Code repository inspected: No
- Data repository inspected: No
- Missing material: Full text, methods, supplement, code, and data availability not confirmed

# Study question and hypothesis
- Primary question: Does 3D genome organization contribute to cell-type-specific gene expression changes in Alzheimer's disease?
- Stated hypothesis: Higher-order chromatin alterations are a component of AD molecular pathology, not merely a consequence of transcriptomic changes
- Study type: Primary multi-omics study; single-cell method development and application

# Biological or clinical context
- Disease / exposure / process: Alzheimer's disease; transcriptomic and epigenomic alterations
- Organism: Human
- Tissue / cell type: Brain (postmortem); cell types not specified in abstract (neuronal and non-neuronal implied)
- Model system: human_cohort (postmortem research cohort)
- Cohort or population: Rush Alzheimer's Disease Center (David A. Bennett cohort); AD patients vs age-matched controls
- Relevant stage, age, sex, genotype, or disease severity: Postmortem AD pathology vs age-matched controls; specific staging, age, sex, and n not reported in abstract

# Study design
- Experimental or observational unit: Single cell (nucleus); postmortem brain tissue
- Unit of inference: Cell type; genomic loci
- Groups and sample size per group: AD patients vs age-matched controls; exact n not in abstract
- Biological replicates: Unknown (full text not inspected)
- Technical replicates: Unknown
- Randomization: Not applicable (postmortem observational)
- Blinding: Unknown
- Inclusion / exclusion criteria: Unknown
- Batch structure: Unknown
- Longitudinal, repeated-measures, paired, or donor structure: Cross-sectional postmortem
- Controls and comparators: Age-matched individuals without AD

# Experimental methods
- Assay / platform: GAGE-seq (genome architecture and gene expression by sequencing) — novel joint profiling of single-cell gene expression and 3D chromatin structure; spatial transcriptomics (integration); chromatin accessibility (integration)
- Sample preparation: Postmortem brain tissue; nuclei isolation implied; details in full text (not inspected)
- Dose, concentration, force, exposure, or perturbation: Not applicable
- Timing and sampling schedule: Not applicable (postmortem cross-sectional)
- Matrix / medium / substrate / environmental conditions: Postmortem brain tissue
- Primary endpoint: Cell-type-specific chromatin and transcriptomic differences in AD vs control
- Secondary endpoints: Integration with spatial transcriptomics; prediction of gene expression from 3D genome features
- QC criteria: Unknown
- Failure or exclusion criteria: Unknown
- Exact reusable parameters and source location: Unknown; full text not inspected

# Computational and statistical methods
- Raw input: GAGE-seq reads (joint 3D chromatin contacts + gene expression); spatial transcriptomics data; chromatin accessibility data
- Preprocessing: Unknown
- Normalization: Unknown
- Feature filtering: Unknown
- Covariates and design formula: Unknown
- Statistical test or model: Unspecified in abstract; Hicformer deep learning framework for predicting cell-type-specific gene expression from 3D genome features
- Multiple-testing correction: Unknown
- Effect-size reporting: Unknown
- Batch handling: Unknown
- Validation strategy: Integration with independent spatial transcriptomics and chromatin accessibility datasets implied
- External validation: Unknown
- Software and versions: Hicformer (novel); other tools unknown
- Code availability: Unknown (not confirmed; likely available given Science publication standards)

# Data and resource availability
- Repository and accession: Unknown; Rush ADRC data typically requires data-use agreement
- Raw data available: Unknown
- Processed data available: Unknown
- Metadata completeness: Unknown
- Data-use restrictions: Rush ADRC data requires agreement; GAGE-seq data availability unknown
- Reusability for the user's work: GAGE-seq method and Hicformer code (if released) would be directly relevant to single-cell multi-omics analysis

# Main findings
Use one row per consequential claim.

| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| 3D genome organization is altered in AD in a cell-type-specific manner | Reported | Abstract | Qualitative: chromatin reorganization linked to cell-type-specific dysregulation | Yes | Scale, effect size, specific cell types and loci unknown without full text |
| AD-associated chromatin alterations affect genome compartments and regulatory elements | Reported | Abstract | Qualitative: altered niches reflecting genome compartment remodeling and regulatory element reorganization | Yes | Mechanistic specificity unknown without full text |
| 3D genome features are essential for predicting disease-relevant, cell-type-specific gene expression | Reported | Abstract | Hicformer deep learning; specific accuracy metrics not in abstract | Partial | "Essential" is a strong claim; comparative performance vs transcriptome-only models unknown without full text |
| Higher-order chromatin alterations are a component of AD molecular pathology | Inference | Abstract / conclusions | Inferred from combined 3D genome + transcriptome evidence | Yes | Causality not established; postmortem study cannot determine whether chromatin changes precede or follow gene expression changes |

# What is actually new?
- Biological novelty: First single-cell characterization of 3D genome organization changes in human AD brain; establishes chromatin architecture as a disease-relevant omics layer beyond accessibility and expression
- Methodological novelty: GAGE-seq: joint single-cell profiling of 3D chromatin contacts and gene expression (previously not combinable at single-cell resolution); Hicformer: deep learning framework for 3D genome–to–expression prediction
- Dataset or resource novelty: Rush ADRC postmortem brain dataset with joint 3D genome + transcriptome profiling; integration with existing spatial transcriptomics and chromatin accessibility data
- What was already known: snRNA-seq and snATAC-seq changes in AD brain are well-characterized; 3D genome organization is cell-type-specific and disrupted in cancer; single-cell Hi-C existed but was not jointly profiled with gene expression

# Strengths
- Design strength: Novel method enabling multi-dimensional measurement in individual cells; integration with multiple independent data types (spatial, accessibility)
- Validation strength: Integration with existing ADRC datasets provides contextualization
- Reproducibility strength: Unknown until code and data released
- Translational or ecological realism: Human postmortem AD brain tissue is clinically relevant; Rush ADRC is a well-characterized research cohort

# Limitations and bias risks
- Sample-size or power limitation: Unknown n; single-cell 3D genome profiling is low-throughput relative to snRNA-seq
- Confounding: Postmortem tissue quality, PMI, and batch effects; known to affect single-cell studies in brain
- Batch or site effects: Single cohort (Rush ADRC); no cross-cohort validation
- Pseudoreplication risk: Unclear; donor-level vs cell-level analysis not specified in abstract
- Leakage or overfitting risk: Hicformer performance on held-out data not described in abstract; overfitting risk for deep learning on small postmortem datasets
- Generalizability limitation: Single research cohort; no cross-disease or cross-brain-region validation
- Missing controls: Non-AD neurodegenerative controls not mentioned; disease stage not specified
- Missing validation: Cross-cohort replication not described in abstract
- Author-stated limitations: Not visible in abstract
- Additional limitations identified during review: GAGE-seq throughput relative to snRNA-seq and snATAC-seq is unknown; 3D chromatin data is sparse at single-cell resolution; code availability not yet confirmed

# Transferability to the user's work
- Directly transferable elements: GAGE-seq as method for any postmortem human brain multi-omics study; Hicformer as tool for 3D genome–expression integration; Rush ADRC data as reference
- Elements requiring adaptation: GAGE-seq requires specialized library preparation; computational pipeline needs code release
- Model, species, tissue, matrix, platform, or scale mismatch: Human only; postmortem tissue with PMI considerations; not applicable to cell lines or animal models without adaptation
- Assumptions required for transfer: 3D genome alterations are consistent across brain regions and stages; GAGE-seq data quality is comparable to snRNA-seq
- Confidence: moderate (for findings); low (for methods transferability until code and protocols released)

# Practical implications
- Experimental implication: Monitor GAGE-seq protocol and code release; consider 3D chromatin profiling as add-on to snRNA-seq/snATAC-seq in future postmortem brain studies
- Analysis implication: Hicformer may provide a new axis for predicting gene expression in disease; watch for benchmarking against standard snRNA-seq-only models
- Public dataset implication: GAGE-seq Rush ADRC dataset will be a reference resource when released
- Biomarker or translational implication: Chromatin architecture changes could identify regulatory circuits not visible from expression alone; not immediately clinically actionable
- Grant or manuscript implication: Strong precedent for 3D genome layer in neurodegeneration multi-omics; cite as method development + AD application

# Contradictions and links
- Supports: Li 2023 (snRNA-seq + snATAC-seq in ALS/FTD; [02_PAPERS/2023/li_2023_c9orf72-snrna-snatac-als-ftd.md]); Ruf 2026 (TDP-43 cell-type pathology, snRNA-seq + snATAC-seq; [02_PAPERS/2026/ruf_2026_celltype-tdp43-motor-cortex.md])
- Contradicts: None identified
- Replicates: None (first of its kind for 3D genome in AD single cells)
- Methodologically comparable papers: Yang 2026 (fGOT spatial integration; [02_PAPERS/2026/yang_2026_fgot-spatial-interpretable-integration.md]); Yang 2025 (SIMO spatial multi-omics; [02_PAPERS/2025/yang_2025_simo-spatial-multiomics-integration.md])
- Relevant synthesis notes: None yet
- Relevant project decisions: None yet

# Follow-up actions
- [ ] Access full text and supplement (Science subscription or institutional access)
- [ ] Identify GAGE-seq protocol and Hicformer code repository (likely GitHub from Ma lab, CMU)
- [ ] Identify Rush ADRC data accession when released
- [ ] Add to synthesis on AD single-cell multi-omics when created

# Priority decision
- Priority: 1
- Read now
- Rationale: First single-cell 3D genome + transcriptome profiling in AD brain; Science journal; introduces new multi-omics method (GAGE-seq) and framework (Hicformer) relevant to computational neuroscience and single-cell analysis domains
