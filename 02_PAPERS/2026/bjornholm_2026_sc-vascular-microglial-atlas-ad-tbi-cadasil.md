---
record_type: paper
record_status: verified
canonical_id: "PMID:42463666"
doi: "10.1038/s41467-026-75367-0"
pmid: "42463666"
pmcid: "PMC13377223"
title: "Heterogenous microglial reactivity contrasts with stable vascular transcriptional programs in mouse models of Alzheimer's, CADASIL, and Traumatic Brain Injury"
year: 2026
source_type: primary
peer_reviewed: true
full_text_checked: true
supplement_checked: false
code_checked: false
data_checked: false
last_verified: 2026-11-01
priority: 1
projects: []
topics:
  - neurodegeneration
  - AD_ADRD
  - TBI
  - single_cell
  - transcriptomics
  - mechanobiology
methods:
  - snRNAseq
  - scRNAseq
  - spatial_transcriptomics
  - analysis_method
datasets: []
---

# Citation
- Full citation: Bjørnholm KD, Li H, Del Gaudio F, Mocci G, Shao W, Baldisseri E, et al. Heterogenous microglial reactivity contrasts with stable vascular transcriptional programs in mouse models of Alzheimer's, CADASIL, and Traumatic Brain Injury. Nature Communications. 2026;17(1). Published online 2026 Jul 16.
- DOI / PMID: https://doi.org/10.1038/s41467-026-75367-0 / PMID 42463666 / PMC13377223
- Related preprint or published version: None identified
- Correction, expression of concern, or retraction status: None as of 2026-11-01

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Establishes a comprehensive single-cell transcriptomic baseline for brain vascular cells (endothelial + mural) and microglia across AD, TBI, and CADASIL in mice. The convergence of microglial transcriptomes between late-stage TBI and AD is a key finding for understanding neurodegeneration risk after TBI and for interpreting glial state signatures across conditions.
- Why it is more or less useful than neighboring literature: More comprehensive than existing vascular atlases in scope (3 disease models, multiple timepoints, vascular + microglial combined). Directly addresses whether TBI leaves a molecular trace on the cerebrovasculature (answer: surprisingly little).

# Source inspection status
- Abstract inspected: Yes
- Full text inspected: Yes (PMC full text read)
- Methods inspected: Yes
- Supplement inspected: No (not accessed)
- Figures/tables inspected: No (figures not rendered via PMC API)
- Code repository inspected: No (Seurat v5.4.0 standard pipeline; no original code deposited per full text)
- Data repository inspected: No (source data linked to article; no GEO accession identified in full text)
- Missing material: Supplementary figures; data accession number; supplement tables with cell counts per model

# Study question and hypothesis
- Primary question: Do the cerebrovasculature and microglia undergo disease-specific transcriptional changes in models of AD, CADASIL, and TBI?
- Stated hypothesis: Disease-associated neuroinflammation affects vascular cells and microglia in a disease-specific manner.
- Study type: Unbiased sc/snRNA-seq cross-disease atlas study (mouse, multiple timepoints)

# Biological or clinical context
- Disease / exposure / process: Alzheimer's disease (AD), CADASIL (Notch3 mutation), traumatic brain injury (CCI)
- Organism: Mus musculus
- Tissue / cell type: Brain vascular cells (endothelial, VSMC, pericytes, perivascular macrophages), microglia
- Model system: 5xFAD (and CAA-high AD model for validation); CADASIL knock-in; C57BL/6J CCI TBI
- Cohort or population: Mouse, in vivo
- Relevant stage, age, sex, genotype, or disease severity: AD/CADASIL: 3, 6, 9, 12 months; TBI: 3 days and 28 days post-CCI; mixed sex inferred

# Study design
- Experimental or observational unit: Individual mouse → isolated vascular cell fractions
- Unit of inference: Cell type cluster per disease/timepoint
- Groups and sample size per group: Reported — >250,000 vascular and vessel-associated cells total across all conditions (exact per-group n not extracted from full text; supplement not inspected)
- Biological replicates: Multiple mice per timepoint (n ≥ 6 per condition confirmed in IHC validation)
- Technical replicates: Unknown (supplement not inspected)
- Randomization: Yes for TBI (random assignment to sham or CCI); none applicable for AD/CADASIL transgenics
- Blinding: Not reported in methods text read
- Inclusion / exclusion criteria: Tissue from perfused mice; standard viability sorting applied
- Batch structure: Multiple timepoints; model comparison performed within Seurat pipeline
- Longitudinal, repeated-measures, paired, or donor structure: Cross-sectional at each timepoint; no longitudinal tracking of individual mice
- Controls and comparators: WT C57BL/6J age-matched controls at each timepoint

# Experimental methods
- Assay / platform: scRNA-seq (technology not specified in extracted text — likely 10X Chromium for cell isolation + standard library prep); also Visium HD spatial transcriptomics for CCI 3d and 28d sections
- Sample preparation: Reported — cell isolation from vascular segments of mouse brain; methodology previously published (Vanlandewijck lab protocol)
- Dose, concentration, force, exposure, or perturbation: CCI TBI — controlled cortical impact model; exact stereotaxic parameters not extracted from text
- Timing and sampling schedule: AD/CADASIL: 3, 6, 9, 12 months; TBI: 3 days, 28 days post-injury
- Matrix / medium / substrate / environmental conditions: Brain tissue, in vivo mouse model
- Primary endpoint: Transcriptional profiles of vascular cells and microglia by disease/timepoint
- Secondary endpoints: IHC validation of key transcriptomic hits; Visium HD spatial validation of DAM markers post-TBI
- QC criteria: Seurat v5.4.0 standard filtering; no original code generated
- Failure or exclusion criteria: Not extracted
- Exact reusable parameters and source location: Seurat v5.4.0; 10X Visium HD with standard mouse probe set v2.0 (Methods section); SpaceRanger for raw processing

# Computational and statistical methods
- Raw input: scRNA-seq count matrices; Visium HD SpaceRanger output
- Preprocessing: Aligned to mouse transcriptome (Clec7a excluded); Seurat v5.4.0 standard pipeline
- Normalization: Seurat defaults (inferred)
- Feature filtering: Standard Seurat variable-feature selection
- Covariates and design formula: Not extracted
- Statistical test or model: ANOVA or t-test with normality confirmed (Anderson-Darling test); Wilcoxon or Welch T if normality fails; mixed model for repeated groups
- Multiple-testing correction: FDR (p <0.05 threshold; *** p < 0.0005)
- Effect-size reporting: Volcano plots; average gene expression
- Batch handling: Unknown
- Validation strategy: IHC validation of key clusters (IBA1+CLEC7A co-occurrence quantified with JACoBi plugin); EM for ultrastructural validation
- External validation: CAA-high AD model used to validate 5xFAD results; branch-point EC and pial VSMC validated in separate C57BL/6J cohort at Uppsala
- Software and versions: Seurat v5.4.0; ggplot2 v3.5.0; EnhancedVolcano v1.20; GraphPad Prism 8.3.0
- Code availability: No original code generated (standard Seurat pipeline)

# Data and resource availability
- Repository and accession: Source data linked to the article (Nature Communications); no GEO/SRA accession identified in full text inspected. (Reported — data deposited but accession not visible in full text.)
- Raw data available: Unknown (not confirmed from full text)
- Processed data available: Source data files linked to publication
- Metadata completeness: Unknown
- Data-use restrictions: Unknown (Nature Communications open access article, CC BY 4.0)
- Reusability for the user's work: High — disease-specific microglial transcriptomes directly reusable for comparative analysis with organoid/blast TBI and AD models; vascular cell atlas provides baseline for BBB research

# Main findings
| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| Brain vasculature (ECs, mural cells) shows minimal transcriptomic changes in AD, CADASIL, and TBI | Reported | Results/Discussion | >200,000 cells analyzed; most vascular types show no significant DEGs | Yes | Mouse models only; human validation absent |
| Microglial transcriptomes are significantly altered in a disease-specific manner across AD, CADASIL, TBI | Reported | Results | Volcano plots show disease-specific DEGs in microglia | Yes | Single cell resolution but models differ in severity and type |
| Late-stage TBI and AD microglial transcriptomes converge | Reported | Results/Discussion | Convergence identified at late TBI timepoints | Yes | Timing dependency: convergence was not seen at early TBI |
| Two previously undescribed vascular cell subtypes identified: branch-point arterial ECs and a novel VSMC | Reported | Results | Cluster-level evidence; validated by IHC and separate mouse cohort | Yes | Functional significance unknown |
| Fenestrated ECs (choroid plexus-type) are enriched in 5xFAD AD model | Reported | Results | Enrichment in AD model; not in CADASIL or TBI | Yes | 5xFAD model lacks CAA at 12m; validated in separate CAA model |

# What is actually new?
- Biological novelty: Striking cerebrovascular transcriptional stability despite neuroinflammation across three distinct diseases; convergence of late TBI and AD microglial programs
- Methodological novelty: Simultaneous cross-disease vascular+microglial sc atlas at multiple timepoints; Visium HD spatial validation of DAM markers at TBI timepoints
- Dataset or resource novelty: Transcriptomic repository of major vascular cell types and microglia across AD, CADASIL, TBI — potentially reusable atlas
- What was already known: Microglia respond to brain injury; vascular changes in AD have been reported; TBI predisposes to neurodegeneration

# Strengths
- Design strength: Unbiased, systematic comparison across 3 disease models with matched timepoints; large cell numbers
- Validation strength: IHC validation with JACoBi co-occurrence analysis; independent mouse cohort validation; Visium HD spatial confirmation
- Reproducibility strength: Standard Seurat pipeline; multiple timepoints; genotype-specific controls
- Translational or ecological realism: Mouse models; controlled cortical impact is an established TBI model; 5xFAD and CADASIL are validated human-disease models

# Limitations and bias risks
- Sample-size or power limitation: Per-group cell counts not extracted; exact mouse n per condition not confirmed from full text
- Confounding: Different disease models affect different cell populations; CADASIL affects VSMC specifically
- Batch or site effects: Unknown; multiple mouse groups/timepoints processed
- Pseudoreplication risk: Cell-level statistics not extracted; potential pseudoreplication if not corrected for mouse-level pseudobulk
- Leakage or overfitting risk: Not applicable (descriptive atlas)
- Generalizability limitation: Mouse models; human BBB/vascular cells may respond differently
- Missing controls: No age-controlled analysis noted; TBI sham controls used but TBI severity not quantified
- Missing validation: Human brain scRNA-seq validation of microglial convergence finding
- Author-stated limitations: 5xFAD model lacks CAA at 12m (addressed with supplementary model)
- Additional limitations identified during review: No direct human data; CCI is focal not blast/diffuse TBI (less relevant to blast injury models)

# Transferability to the user's work
- Directly transferable elements: Microglial transcriptome comparison pipeline (Seurat v5.4.0); DAM marker set (CLEC7A, TREM2, TYROBP, APOE); vascular marker panel for ECs and mural cells; Visium HD for spatial TBI validation
- Elements requiring adaptation: Must adjust for human tissue; blast TBI paradigm differs from CCI
- Model, species, tissue, matrix, platform, or scale mismatch: Mouse CCI vs. blast overpressure; 5xFAD vs. sporadic AD
- Assumptions required for transfer: Microglial state signatures are conserved across mouse models and partially to human
- Confidence: moderate (mouse-only; mechanistic principles likely transferable but magnitudes unknown)

# Practical implications
- Experimental implication: Use this vascular+microglial atlas as a reference when analyzing TBI organoid or blast model sc data; compare DAM signatures against late-TBI convergence with AD
- Analysis implication: Pseudobulk correction essential when comparing microglial clusters across disease models
- Public dataset implication: Source data available (linked to article); pursue GEO/SRA accession from authors for raw count matrices
- Biomarker or translational implication: Microglial convergence between late TBI and AD may inform longitudinal biomarker design (e.g., DAM-associated proteins in CSF/plasma at late TBI timepoints)
- Grant or manuscript implication: Cites vascular resilience hypothesis; contrast with Trivedi 2026 BBB repair findings

# Contradictions and links
- Supports: Trivedi 2026 (platelet-mediated BBB repair after TBI — vascular resilience angle); strat_2026 (astrocyte mechanobiology review); sirtori_2025 (blast TBI organoid model)
- Contradicts: Reports suggesting vascular disruption is a primary driver of TBI neurodegeneration (vascular stability finding conflicts with injury-driven BBB damage narratives)
- Replicates: Vanlandewijck lab vascular atlases (prior scRNA-seq of brain vasculature)
- Methodologically comparable papers: ruf_2026 (TDP-43 cell-type sc atlas); li_2023 (C9orf72 sn-RNA/ATAC)
- Relevant synthesis notes: None yet
- Relevant project decisions: None recorded

# Follow-up actions
- [ ] Obtain GEO/SRA accession from article supplementary or contact authors
- [ ] Inspect supplementary figures for per-group cell counts and DEG tables
- [ ] Cross-compare DAM marker enrichment at late TBI against ruf_2026 TDP-43 motor cortex sc data
- [ ] Evaluate whether Visium HD data from TBI sections are accessible for independent analysis

# Priority decision
- Priority: 1
- Read now
- Rationale: First comprehensive simultaneous vascular+microglial cross-disease sc atlas including TBI; late-TBI/AD microglial convergence finding is directly decision-relevant for TBI neurodegeneration interpretation; Nature Communications, peer-reviewed, PMC full text inspected.
