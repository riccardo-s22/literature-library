---
record_type: paper
record_status: verified
canonical_id: pmid:41339526
doi: 10.1038/s41587-025-02811-9
pmid: "41339526"
pmcid: PMC13368583
title: "Standardized metrics for assessment and reproducibility of imaging-based spatial transcriptomics datasets"
year: 2025
source_type: benchmark
peer_reviewed: true
full_text_checked: false
supplement_checked: false
code_checked: false
data_checked: false
last_verified: 2026-10-01
priority: 1
projects: []
topics:
  - transcriptomics
  - spatial_omics
  - single_cell
  - multi_omics
methods:
  - analysis_method
  - software
  - spatial_transcriptomics
  - benchmark
datasets: []
---

# Citation
- Full citation: Plummer JT, Dezem FS, Cook DP, et al. Standardized metrics for assessment and reproducibility of imaging-based spatial transcriptomics datasets. Nat Biotechnol. 2026;44(7):1213-1225. (Epub ahead of print Dec 3 2025.)
- DOI / PMID / stable URL: https://doi.org/10.1038/s41587-025-02811-9 / PMID 41339526 / PMC13368583
- Related preprint or published version: None identified
- Correction, expression of concern, or retraction status: None identified as of 2026-10-01

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Directly addresses the reproducibility gap in imaging-based spatial transcriptomics (Xenium, CosMx); provides standardized operating procedures (STSOPs), open-source QC software (SpatialQM), and a 254-profile reference dataset for benchmarking. Critical for evaluating and selecting spatial transcriptomics approaches for post-mortem human brain studies.
- Why it is more or less useful than neighboring literature: Currently the only multi-site, multi-platform benchmark for imaging-based spatial transcriptomics in the library; more reproducibility-focused than yang_2025_simo or yang_2026_fgot (which are integration methods). Directly enables quality evaluation of new spatial datasets before integration.

# Source inspection status
- Abstract inspected: Yes
- Full text inspected: No (PMC13368583 available — inspect for per-tissue QC thresholds, SpatialQM usage guidance, comparison metrics definitions)
- Methods inspected: No
- Supplement inspected: No
- Figures/tables inspected: No
- Code repository inspected: No
- Data repository inspected: No
- Missing material: Full text, GitHub URL for SpatialQM, exact repository accession for the 254 spatial profiles, tissue types benchmarked

# Study question and hypothesis
- Primary question: Can standardized metrics quantify and compare the performance of imaging-based spatial transcriptomics platforms across sites, tissue types, and RNA detection chemistries?
- Stated hypothesis: Standardized metrics will identify reproducible performance differences between platforms and enable integration of data from diverse sources.
- Study type: Benchmark resource / methods paper

# Biological or clinical context
- Disease / exposure / process: Methodology development; multi-tissue benchmarking (tissue types: six types, names Unknown from abstract — full text needed)
- Organism: Multiple (human and mouse implied; exact species Unknown — full text needed)
- Tissue / cell type: Six tissue types (Unknown — full text needed); includes brain (inferred)
- Model system: Tissue sections (centralized sectioning, distributed analysis)
- Cohort or population: Multiple global sites; exact site list Unknown — full text needed
- Relevant stage, age, sex, genotype, or disease severity: Unknown — full text needed

# Study design
- Experimental or observational unit: Tissue section / spatial profile
- Unit of inference: Platform-specific performance metric (sensitivity, SNR, FDR, cell-type annotation congruence)
- Groups and sample size per group: 254 spatial profiles total; Xenium and CosMx platforms; multiple global sites; centralized sectioning
- Biological replicates: Multiple sites and sections per tissue type (exact n Unknown)
- Technical replicates: Multiple platform runs per tissue (Xenium vs CosMx)
- Randomization: Not applicable (benchmark)
- Blinding: Not applicable
- Inclusion / exclusion criteria: Unknown — full text needed
- Batch structure: Multi-site; centralized sectioning controls pre-sequencing batch; platform batch unknown
- Longitudinal, repeated-measures, paired, or donor structure: Not applicable
- Controls and comparators: Platform-to-platform comparison (Xenium vs CosMx); imputed cell annotations vs scRNA-seq reference

# Experimental methods
- Assay / platform: Xenium and CosMx imaging-based spatial transcriptomics; single-cell RNA profiling for reference
- Sample preparation: Centralized sectioning (standardized pre-analysis); Unknown staining/prep details — full text needed
- Dose, concentration, force, exposure, or perturbation: N/A
- Timing and sampling schedule: N/A
- Matrix / medium / substrate / environmental conditions: Tissue sections from six tissue types
- Primary endpoint: Reproducibility, sensitivity, dynamic range, SNR, FDR, cell-type annotation congruence
- Secondary endpoints: Integration metrics; multi-omics extension (spatial proteomics)
- QC criteria: Standardized metrics captured in SpatialQM (exact thresholds Unknown — full text needed)
- Failure or exclusion criteria: Unknown — full text needed
- Exact reusable parameters and source location: SpatialQM software (GitHub — URL Unknown); STSOPs document (supplemental materials likely)

# Computational and statistical methods
- Raw input: Imaging-based spatial transcriptomics raw reads / spot/cell assignments
- Preprocessing: DAPI-based cell segmentation (implied); transcript assignment per cell
- Normalization: Unknown — full text needed
- Feature filtering: Unknown
- Covariates and design formula: N/A (benchmark)
- Statistical test or model: Performance metrics comparison across platforms and sites; FDR computation; congruence scoring
- Multiple-testing correction: Unknown
- Effect-size reporting: Unknown — full text needed
- Batch handling: Centralized sectioning minimizes pre-library batch; site batch quantified by metrics
- Validation strategy: 254-profile repository compared against user data; direct platform comparison
- External validation: Reference scRNA-seq profiles for cell annotation imputation
- Software and versions: SpatialQM (open-source, version Unknown); Xenium and CosMx proprietary analysis pipelines
- Code availability: SpatialQM released as open-source (repository URL Unknown — full text needed)

# Data and resource availability
- Repository and accession: 254 spatial profiles in a web-based application; also public and newly generated ST datasets. Exact repository (GEO or dedicated server) Unknown — full text needed
- Raw data available: Yes (254 spatial profiles published)
- Processed data available: Yes (annotated datasets)
- Metadata completeness: High (centralized design)
- Data-use restrictions: Unknown — likely permissive (academic multi-site collaboration)
- Reusability for the user's work: High — SpatialQM directly applicable to any new Xenium/CosMx dataset from post-mortem brain tissue; STSOPs guide experimental design.

# Main findings
Use one row per consequential claim.

| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| Six tissue types across global sites on Xenium and CosMx have systematically different sensitivity and SNR profiles | Reported | Abstract | Quantitative differences Unknown — full text needed | Yes | Platform selection (Xenium, CosMx) was based on widespread use; excludes other platforms (Vizium, MERFISH) |
| SpatialQM enables evaluation of any user dataset against the 254-profile reference | Reported | Abstract | Benchmark coverage Unknown | Yes | Software open-source but version/maintenance stability Unknown |
| Reference-based cell annotation imputation enables direct comparison of imaging-based with scRNA-seq profiling | Reported | Abstract | Congruence score Unknown | Yes | Quality of imputation depends on reference atlas completeness |
| Multi-omics extension to spatial proteomics is demonstrated | Reported | Abstract | Unknown scope | Partial | Proteomics component details Unknown — full text needed |

# What is actually new?
- Biological novelty: None (methods/benchmark paper)
- Methodological novelty: First multi-site, multi-platform, standardized-sectioning benchmark for imaging-based spatial transcriptomics with open software (SpatialQM) and a curated 254-profile reference.
- Dataset or resource novelty: 254 spatial profiles (Xenium + CosMx) from 6 tissues, multiple global sites, web-accessible.
- What was already known: Imaging-based spatial transcriptomics performance varies by tissue and platform; reproducibility was unquantified.

# Strengths
- Design strength: Multi-site, multi-platform, centralized sectioning — the most controlled design possible for this benchmark question.
- Validation strength: Open software + reference dataset allows independent benchmarking by any user.
- Reproducibility strength: STSOPs enable procedural standardization; 254-profile dataset is a persistent resource.
- Translational or ecological realism: Six real tissue types include human samples (tissue types Unknown — full text needed).

# Limitations and bias risks
- Sample-size or power limitation: Only Xenium and CosMx benchmarked; Vizium, MERFISH, CODEX not included.
- Confounding: Centralized sectioning controls one variable but tissue origin (donor age, sex, fixation history) may vary across sites.
- Batch or site effects: Characterized and quantified (the goal of the study), not eliminated.
- Pseudoreplication risk: Low (different tissues, sites, sections are genuine replicates)
- Leakage or overfitting risk: Low for a benchmark study
- Generalizability limitation: Brain-specific performance Unknown — may differ from the 6 tissue benchmarks if brain tissue quality is lower (RNA degradation).
- Missing controls: Post-mortem human brain is not among the 6 benchmark tissues (if brain is included this becomes highly relevant).
- Missing validation: Long-term maintenance and update of SpatialQM Unknown.
- Author-stated limitations: Unknown — full text needed.
- Additional limitations identified during review: 254 profiles is small relative to the field; updates needed as new platforms (Visium HD, MERSCOPE) emerge.

# Transferability to the user's work
- Directly transferable elements: SpatialQM QC pipeline; STSOPs for Xenium/CosMx experiments on brain tissue; 254-profile reference for benchmarking new datasets.
- Elements requiring adaptation: If using Xenium/CosMx on post-mortem brain, apply STSOPs then compare metrics to the 254-profile reference; expect lower performance metrics if brain RNA quality is poor.
- Model, species, tissue, matrix, platform, or scale mismatch: Benchmark tissues may not include post-mortem brain (confirm from full text); performance on post-mortem brain may differ from benchmarked tissues.
- Assumptions required for transfer: RNA quality of test samples is sufficient for spatial transcriptomics; panel design (gene selection) is comparable.
- Confidence: high (if brain tissue is among the six types) / moderate (if not)

# Practical implications
- Experimental implication: Before running Xenium or CosMx on new tissue, download SpatialQM and STSOPs; use 254-profile benchmark to set QC thresholds for cell segmentation, sensitivity, and annotation congruence.
- Analysis implication: Apply SpatialQM after data generation to detect site- or batch-driven performance drops before integration.
- Public dataset implication: 254-profile repository is a reusable reference; check if any tissues are neurological.
- Biomarker or translational implication: Standardized metrics allow comparison of spatial data across different cohorts (e.g., comparing AD vs TBI spatial profiles).
- Grant or manuscript implication: Citing SpatialQM and STSOPs in methods sections strengthens reproducibility claims for imaging-based spatial transcriptomics experiments.

# Contradictions and links
- Supports: yang_2025_simo (multi-omics integration benefits from standardized inputs); ren_2026_stereo-seq-multiorgan (atlas quality depends on QC); castrobrant_2026 (post-mortem brain spatial framework)
- Contradicts: No direct contradictions
- Replicates: N/A (benchmark)
- Methodologically comparable papers: zappia_2025 (feature selection for scRNA-seq integration); yang_2026_fgot (spatial integration)
- Relevant synthesis notes: None yet
- Relevant project decisions: None yet

# Follow-up actions
- [ ] Inspect PMC13368583 full text: confirm which six tissue types are benchmarked; extract SpatialQM GitHub URL and exact metrics definitions; verify whether post-mortem brain is among the benchmarked tissues
- [ ] Download SpatialQM and evaluate against existing spatial datasets in library
- [ ] Check 254-profile repository accession for brain tissues

# Priority decision
- Priority: 1
- Read now
- Rationale: SpatialQM and STSOPs are directly adoptable for any new imaging-based spatial transcriptomics experiment on brain tissue; this is the field's first standardized benchmark — fills the reproducibility gap identified in previous passes.
