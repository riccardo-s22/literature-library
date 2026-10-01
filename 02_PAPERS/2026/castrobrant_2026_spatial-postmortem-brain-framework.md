---
record_type: paper
record_status: partial
canonical_id: pmid:42619824
doi: 10.64898/2026.07.28.740610
pmid: "42619824"
pmcid: PMC13484011
title: "An end-to-end framework for single-cell-resolution, whole-transcriptomic spatial profiling in post-mortem human brain"
year: 2026
source_type: preprint
peer_reviewed: false
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
  - neurodegeneration
  - AD_ADRD
methods:
  - analysis_method
  - software
  - spatial_transcriptomics
  - protocol_parameter
  - snRNAseq
datasets: []
---

# Citation
- Full citation: Castro Brant A, Aladyeva E, Nguyen-Hao HT, et al. An end-to-end framework for single-cell-resolution, whole-transcriptomic spatial profiling in post-mortem human brain. bioRxiv. 2026 Aug 1. DOI: 10.64898/2026.07.28.740610.
- DOI / PMID / stable URL: https://doi.org/10.64898/2026.07.28.740610 / PMID 42619824 / PMC13484011
- Related preprint or published version: Preprint (bioRxiv); peer-reviewed publication pending — monitor for journal version
- Correction, expression of concern, or retraction status: Preprint — not peer-reviewed as of 2026-10-01

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Directly addresses the challenge of applying single-cell-resolution whole-transcriptome spatial transcriptomics to post-mortem human brain — a key bottleneck for all AD and neurodegeneration spatial omics work. Provides an optimized 2-day experimental protocol + preservation-agnostic bioinformatics pipeline; the 530,000-cell FF+FFPE AD atlas is a reusable resource.
- Why it is more or less useful than neighboring literature: The only framework in the library specifically optimized for post-mortem brain tissue (FF and FFPE), including degraded RNA handling. Complements plummer_2025 (platform benchmarking metrics) and yang_2025_simo/yang_2026_fgot (integration methods); fills the experimental protocol gap that those computational papers assume is solved.

# Source inspection status
- Abstract inspected: Yes
- Full text inspected: No (PMC13484011 available — inspect for: exact spatial platform used, gene panel size, DAPI segmentation parameters, QC thresholds, GitHub pipeline URL, GEO accession)
- Methods inspected: No
- Supplement inspected: No
- Figures/tables inspected: No
- Code repository inspected: No
- Data repository inspected: No
- Missing material: Full text, pipeline GitHub URL, GEO accession for 530,000-cell atlas, exact spatial platform (Xenium? CosMx? other), gene panel, sequencing depth analysis

# Study question and hypothesis
- Primary question: Can single-cell-resolution, whole-transcriptome spatial transcriptomics be reliably applied to post-mortem human brain tissue (both fresh-frozen and FFPE) with standardized experimental and computational workflows?
- Stated hypothesis: A preservation-agnostic workflow combining an optimized 2-day protocol with reference-based bioinformatics can overcome the degradation and variability challenges of post-mortem brain spatial profiling.
- Study type: Methods/resource paper (framework development + application)

# Biological or clinical context
- Disease / exposure / process: Alzheimer's disease (application); general framework for post-mortem brain spatial transcriptomics
- Organism: Human (post-mortem)
- Tissue / cell type: Frontal cortex; neurons, glia, vascular cells
- Model system: Post-mortem human brain (7 specimens: 5 FF + 2 FFPE)
- Cohort or population: 7 AD frontal cortex specimens; diagnostic confirmation Unknown — full text needed; donor demographics (age, sex, PMI) Unknown
- Relevant stage, age, sex, genotype, or disease severity: AD (stage Unknown); PMI Unknown — critical for RNA quality interpretation

# Study design
- Experimental or observational unit: Tissue section
- Unit of inference: Cell (single-cell resolved spatial)
- Groups and sample size per group: 5 fresh-frozen (FF) + 2 FFPE specimens; single disease group (AD frontal cortex)
- Biological replicates: 7 specimens from (presumably) different donors
- Technical replicates: FF vs FFPE comparison provides a technical replicate dimension
- Randomization: Not applicable
- Blinding: Not applicable
- Inclusion / exclusion criteria: Unknown — full text needed
- Batch structure: Preservation method (FF vs FFPE); library preparation batch Unknown
- Longitudinal, repeated-measures, paired, or donor structure: Cross-sectional; some donors may have matched FF+FFPE (Unknown)
- Controls and comparators: FF vs FFPE comparison; reference scRNA-seq atlas for annotation

# Experimental methods
- Assay / platform: Single-cell-resolution whole-transcriptome spatial transcriptomics (exact platform Unknown — full text needed; likely Xenium or CosMx based on plummer_2025 context); DAPI-based nuclear segmentation
- Sample preparation: Optimized 2-day condensed protocol (improves library quality, lower qPCR cycle thresholds, more consistent fragment size distributions)
- Dose, concentration, force, exposure, or perturbation: N/A
- Timing and sampling schedule: 2-day experimental workflow (condensed from prior multi-day protocols)
- Matrix / medium / substrate / environmental conditions: Fresh-frozen and formalin-fixed paraffin-embedded post-mortem brain sections
- Primary endpoint: Library quality (qPCR Ct, fragment size distribution); cell detection; annotation congruence with scRNA-seq reference
- Secondary endpoints: Sequencing saturation analysis; cost-effective sequencing depth recommendation; FF vs FFPE comparison
- QC criteria: DAPI-based nuclear segmentation; reference-guided integration; clustering; cell-type annotation (exact thresholds Unknown — full text needed)
- Failure or exclusion criteria: Unknown — full text needed
- Exact reusable parameters and source location: 2-day protocol in Methods/Supplement; sequencing saturation analysis in manuscript

# Computational and statistical methods
- Raw input: Spatial transcriptomics raw data (pixel coordinates + transcript assignments)
- Preprocessing: DAPI-based nuclear segmentation; transcript assignment
- Normalization: Unknown — full text needed
- Feature filtering: Reference-based highly variable gene selection (preservation-agnostic — key claim)
- Covariates and design formula: Preservation method (FF vs FFPE) as a covariate in integration
- Statistical test or model: Clustering; reference-guided annotation; cross-sample harmonization
- Multiple-testing correction: N/A (resource paper)
- Effect-size reporting: N/A
- Batch handling: Reference-based HVG selection designed to be preservation-agnostic; enables FF+FFPE cross-sample harmonization
- Validation strategy: 530,000-cell atlas with resolved major neuronal, glial, and vascular populations; recapitulated cortical architecture
- External validation: Comparison of FF- and FFPE-derived spatial profiles
- Software and versions: Pipeline (GitHub Unknown — full text needed); SpatialQM-compatible (inferred)
- Code availability: Open-source pipeline (stated in abstract); URL Unknown — full text needed

# Data and resource availability
- Repository and accession: 530,000-cell AD frontal cortex atlas — "publicly available resource" (exact accession Unknown — full text needed; likely GEO or Zenodo)
- Raw data available: Unknown — likely Yes based on "publicly available" statement
- Processed data available: Yes (530,000-cell atlas with cell-type annotations)
- Metadata completeness: Unknown — donor demographics (age, sex, PMI) critical for interpreting RNA quality
- Data-use restrictions: Unknown
- Reusability for the user's work: High — 530,000-cell AD cortex atlas directly reusable as a reference for new AD brain spatial datasets; pipeline reusable for any post-mortem brain experiment

# Main findings
Use one row per consequential claim.

| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| Condensed 2-day protocol improves library quality (lower Ct, more consistent fragment sizes) vs. prior multi-day workflows | Reported | Abstract | Qualitative improvement; exact Ct values Unknown | Yes | Comparative data may be internal only; full text needed |
| Sequencing saturation analysis identifies cost-effective depths that maximize transcript recovery | Reported | Abstract | Saturation curves (exact values Unknown) | Yes | Tissue-specific; brain results may differ from other tissues |
| Reference-based HVG selection enables robust cross-sample harmonization independent of preservation method | Reported | Abstract | Harmonization achieves unified atlas (530,000 cells) | Yes | 5 FF + 2 FFPE is a small n; preservation effects may be underestimated |
| Applied to 7 AD frontal cortex specimens, the framework resolves major neuronal, glial, and vascular populations | Reported | Abstract | 530,000 cells; major cell populations resolved | Yes | AD-only cohort; no control samples |
| FF- and FFPE-derived spatial profiles can be directly compared | Reported | Abstract | Comparison successful (qualitative) | Yes | Preprint — not peer-reviewed; FF vs FFPE comparison n=5+2 is small |

# What is actually new?
- Biological novelty: 530,000-cell AD frontal cortex spatial atlas (FF + FFPE); resolution of cortical architecture in diseased post-mortem tissue.
- Methodological novelty: First preservation-agnostic (FF+FFPE) end-to-end workflow for single-cell-resolution whole-transcriptome spatial profiling of post-mortem human brain; condensed 2-day protocol; reference-based HVG selection for cross-sample harmonization.
- Dataset or resource novelty: 530,000-cell AD frontal cortex atlas publicly available; directly reusable for AD neurodegeneration studies.
- What was already known: Post-mortem brain spatial transcriptomics is challenging due to RNA degradation; computational methods for integration exist but lacked experimental standardization.

# Strengths
- Design strength: Both FF and FFPE in the same study enables direct comparison; end-to-end framework covers experiment through analysis.
- Validation strength: Recapitulated expected cortical architecture (internal validation); 530,000-cell scale.
- Reproducibility strength: Open-source pipeline + published atlas; reference-based HVG is a reproducible method.
- Translational or ecological realism: Post-mortem human brain is the most relevant material for neurodegeneration studies; FF+FFPE inclusion enables use of archival samples.

# Limitations and bias risks
- Sample-size or power limitation: n=7 specimens, AD only; no control brains in this dataset.
- Confounding: PMI, brain bank, fixation conditions vary; not controlled in this study.
- Batch or site effects: Single-site study; cross-site generalizability Unknown.
- Pseudoreplication risk: Single-cell resolved data from 7 donors — donor-level pseudoreplication risk if not explicitly modeled in clustering.
- Leakage or overfitting risk: Reference-based annotation may over-assign rare cell types; validation with independent markers needed.
- Generalizability limitation: AD frontal cortex only; performance on TBI, ALS, or other neurodegenerative tissues Unknown.
- Missing controls: No non-diseased control brain specimens; single brain region.
- Missing validation: Independent site validation of the protocol; peer review not yet completed.
- Author-stated limitations: Not available (abstract only)
- Additional limitations identified during review: Preprint status is a key risk; peer review may alter conclusions. The atlas covers AD only, limiting reference utility for TBI or ALS studies.

# Transferability to the user's work
- Directly transferable elements: 2-day protocol and reference-based HVG selection for new post-mortem brain spatial experiments; 530,000-cell AD atlas as a reference for annotation; sequencing depth guidance.
- Elements requiring adaptation: Protocol would need testing on TBI or ALS tissue (RNA quality may differ); gene panel may need adjustment for non-AD neurodegeneration.
- Model, species, tissue, matrix, platform, or scale mismatch: AD frontal cortex; other brain regions and diseases not benchmarked.
- Assumptions required for transfer: RNA quality of new samples is comparable to those in the study (PMI, fixation conditions similar).
- Confidence: moderate (preprint risk)

# Practical implications
- Experimental implication: Adopt the 2-day protocol and reference-based HVG selection when running any whole-transcriptome spatial experiment on post-mortem brain tissue; check preprint for peer-reviewed publication before finalizing protocols.
- Analysis implication: Use the 530,000-cell AD atlas as a cell-type annotation reference; apply reference-based HVG selection when integrating FF and FFPE data.
- Public dataset implication: Verify GEO or equivalent accession for 530,000-cell atlas before using as reference.
- Biomarker or translational implication: Framework enables comparison of spatial biomarker distributions across preservation methods (FF vs FFPE archival samples).
- Grant or manuscript implication: Citing this framework justifies choice of spatial platform and protocol for brain studies; demonstrates feasibility of FFPE archival tissue.

# Contradictions and links
- Supports: plummer_2025 (spatial transcriptomics benchmarking); yang_2025_simo, yang_2026_fgot (integration methods that require QC-passed spatial inputs)
- Contradicts: No direct contradictions
- Replicates: N/A (methods paper)
- Methodologically comparable papers: plummer_2025 (spatial touchstone benchmark); ren_2026 (multi-organ spatial atlas)
- Relevant synthesis notes: None yet
- Relevant project decisions: None yet

# Follow-up actions
- [ ] Monitor for peer-reviewed publication (currently bioRxiv preprint)
- [ ] Inspect PMC13484011 full text: extract spatial platform name, gene panel size, GitHub pipeline URL, GEO accession, donor demographics, sequencing depth recommendations
- [ ] Compare 2-day protocol to castrobrant_2026 vs plummer_2025 STSOPs for consistency
- [ ] Retrieve GEO accession and evaluate AD cortex atlas for use as spatial reference in neurodegeneration studies

# Priority decision
- Priority: 1
- Read now
- Rationale: End-to-end protocol + AD cortex atlas directly applicable to any post-mortem brain spatial transcriptomics project; fills the key experimental gap (how to handle degraded/archival brain tissue) not addressed by existing computational integration papers.
