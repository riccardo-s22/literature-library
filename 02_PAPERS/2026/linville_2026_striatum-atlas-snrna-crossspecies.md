---
record_type: paper
record_status: verified
canonical_id: pmid:42679819
doi: 10.1016/j.cell.2026.08.006
pmid: "42679819"
title: "Cross-species single-cell atlas of the striatum defines cell-type and subregion disease vulnerabilities."
year: 2026
source_type: primary
peer_reviewed: true
full_text_checked: false
supplement_checked: false
code_checked: false
data_checked: false
last_verified: 2026-10-01
priority: 2
projects: []
topics:
  - neurodegeneration
  - single_cell
  - transcriptomics
  - spatial_omics
methods:
  - snRNAseq
  - analysis_method
  - software
datasets: []
---

# Citation
- Full citation: Linville RM, James BT, Galani K, et al. Cross-species single-cell atlas of the striatum defines cell-type and subregion disease vulnerabilities. Cell. 2026 Sep 1. DOI: 10.1016/j.cell.2026.08.006.
- DOI / PMID / stable URL: https://doi.org/10.1016/j.cell.2026.08.006 / PMID 42679819
- Related preprint or published version: None identified
- Correction, expression of concern, or retraction status: None identified as of 2026-10-01

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Provides a large-scale reference atlas of striatal cell types and subregions relevant to Huntington's disease, opioid use disorder, and antipsychotic pharmacology. The cross-species comparison with 109 human + 22 mouse samples enables evaluation of whether mouse models faithfully recapitulate human striatal cell-type diversity — critical for selecting models in neurodegeneration research. The Huntington's disease neuronal subtype vulnerability mapping provides a disease-relevant cell-type reference directly usable for genetic and spatial studies.
- Why it is more or less useful than neighboring literature: Largest cross-species striatum atlas in the library; paired somatic repeat expansion measurements provide a unique disease vulnerability layer not available in purely transcriptomic atlases. Complements existing neurodegeneration single-cell papers (li_2023_c9orf72 for ALS/FTD; ruf_2026 for TDP-43 motor cortex); adds pharmacological and GWAS integration not present in those papers. Less directly applicable to ALS/AD frontal cortex work than other D1 records in this library.

# Source inspection status
- Abstract inspected: Yes
- Full text inspected: No (Cell journal; inspect for atlas accession ID, total cell count, clustering parameters, software versions, CAG repeat measurement platform, spatial transcriptomics details)
- Methods inspected: No
- Supplement inspected: No
- Figures/tables inspected: No
- Code repository inspected: No
- Data repository inspected: No
- Missing material: Full text, data repository accession (GEO or Broad Single Cell Portal or CellxGene), exact cell count per subtype, clustering parameters, CAG repeat measurement platform, spatial transcriptomics extent

# Study question and hypothesis
- Primary question: What is the landscape of cell-type and subregional specialization in the human and mouse striatum, and how does it relate to neurodegenerative and neuropsychiatric disease vulnerability?
- Stated hypothesis: Striatal cell types and subregions are differentially vulnerable to neurodegenerative and neuropsychiatric conditions, with cross-species differences in key pharmacological targets and disease mechanisms.
- Study type: Resource / atlas paper with disease-application analyses

# Biological or clinical context
- Disease / exposure / process: Huntington's disease (primary disease application); neuropsychiatric disorders (antipsychotic pharmacology, opioid use disorder)
- Organism: Human and mouse (cross-species)
- Tissue / cell type: Striatum (dorsal and ventral); medium spiny neurons, interneurons, glia (complete cell type list Unknown — full text needed)
- Model system: Post-mortem human brain; mouse brain
- Cohort or population: 109 human samples + 22 mouse samples; sources include Broad/MIT, Mayo Clinic, McGill, MGH, NIH/NIAAA, Nova Southeastern, Dana-Farber; donor demographics Unknown — full text needed
- Relevant stage, age, sex, genotype, or disease severity: Includes Huntington's disease patients (somatic CAG repeat expansion measured); non-diseased controls presumed; exact genotypes and HD staging Unknown — full text needed

# Study design
- Experimental or observational unit: Nucleus (single cell) within a tissue sample
- Unit of inference: Cell type / subtype; subregion (dorsal vs ventral striatum)
- Groups and sample size per group: 109 human samples + 22 mouse samples; HD vs non-HD subsets (exact n Unknown — full text needed)
- Biological replicates: Multiple donors per species (n=109 human, n=22 mouse)
- Technical replicates: Unknown
- Randomization: Not applicable (observational atlas)
- Blinding: Unknown
- Inclusion / exclusion criteria: Unknown — full text needed
- Batch structure: Multi-site (MIT, Broad, NIMH, Mayo, MGH, McGill, Dana-Farber); exact batch correction strategy Unknown — full text needed
- Longitudinal, repeated-measures, paired, or donor structure: Cross-sectional; paired snRNA-seq + somatic CAG repeat expansion in HD subset
- Controls and comparators: Cross-species comparison (human vs mouse); HD vs control in disease subanalysis (controls Unknown — full text needed)

# Experimental methods
- Assay / platform: Single-nucleus RNA sequencing (snRNA-seq); somatic trinucleotide (CAG) repeat expansion measurement (platform Unknown — full text needed; likely PacBio or similar); spatial transcriptomics (in keywords — extent and platform Unknown — full text needed)
- Sample preparation: Post-mortem human brain and mouse brain tissue; exact nuclei isolation protocol Unknown — full text needed
- Dose, concentration, force, exposure, or perturbation: N/A
- Timing and sampling schedule: N/A (cross-sectional)
- Matrix / medium / substrate / environmental conditions: Frozen post-mortem brain tissue
- Primary endpoint: Cell-type atlas: neuronal subtypes and transcriptional gradients along dorsolateral-ventromedial axis
- Secondary endpoints: Cross-species pharmacological target differences; GWAS integration; HD neuronal subtype vulnerability
- QC criteria: Unknown — full text needed
- Failure or exclusion criteria: Unknown — full text needed
- Exact reusable parameters and source location: Clustering and annotation parameters Unknown — full text needed; CAG repeat expansion methodology Unknown

# Computational and statistical methods
- Raw input: snRNA-seq reads; CAG repeat sequencing reads; (possibly spatial transcriptomics raw data)
- Preprocessing: Standard snRNA-seq pipeline (exact software Unknown — full text needed)
- Normalization: Unknown
- Feature filtering: Unknown
- Covariates and design formula: Species (human vs mouse) as covariate in cross-species integration; disease status in HD subanalysis
- Statistical test or model: Clustering, UMAP, differential expression, GWAS integration (exact methods Unknown); CAG expansion analysis
- Multiple-testing correction: Unknown
- Effect-size reporting: Transcriptional gradients and subtype differences reported; quantitative values Unknown
- Batch handling: Multi-site integration with harmonization (exact method Unknown — full text needed)
- Validation strategy: Cross-species comparison (internal); GWAS integration (external disease-relevance); somatic repeat expansion (orthogonal biological readout)
- External validation: Integration with GWAS datasets; pharmacological study data
- Software and versions: Unknown — full text needed (Broad Institute group typically releases code)
- Code availability: Unknown — full text needed

# Data and resource availability
- Repository and accession: Atlas data — exact accession Unknown — full text needed; likely Broad Single Cell Portal, GEO, or CellxGene
- Raw data available: Likely Yes (Cell journal + multi-site NIH-affiliated consortium)
- Processed data available: Likely Yes (atlas with annotated cell types)
- Metadata completeness: Unknown — donor demographics (age, sex, PMI, disease stage) critical for neurodegeneration subanalyses
- Data-use restrictions: Unknown
- Reusability for the user's work: Moderate — striatum atlas provides a reference for cell-type annotation in any striatal snRNA-seq or spatial study; HD neuronal vulnerability map applicable to neurodegeneration comparisons; cross-species evaluation framework generalizable

# Main findings
Use one row per consequential claim.

| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| snRNA-seq of 109 human + 22 mouse striatal samples defines rare neuronal subpopulations and transcriptional gradients along the dorsolateral-ventromedial axis | Reported | Abstract | Cell counts Unknown; gradient extent Unknown | Yes | Multi-site; batch correction approach Unknown |
| Notable species differences exist in pharmacological targets, connectivity, and disease mechanisms between human and mouse striatum | Reported | Abstract | Specific differences Unknown — full text needed | Yes | Cross-species comparison may be confounded by tissue preparation differences |
| Human striatum is enriched for opioid receptor expression sites relative to mouse; ventral striatum shows biased chronic antipsychotic action | Reported | Abstract | Enrichment magnitude Unknown | Yes | Functional validation of pharmacological targets not described in abstract |
| Paired snRNA-seq and somatic CAG repeat expansion measurements identify subregion- and neuronal-subtype-specific Huntington's disease vulnerability | Reported | Abstract | Specific vulnerability profiles Unknown — full text needed | Yes | Correlation is associative; mechanistic basis Unknown |
| GWAS integration with the atlas identifies cell-type-specific disease-associated loci | Reported | Abstract | Specific GWAS signals Unknown — full text needed | Yes | GWAS-to-cell-type inference is statistical; functional validation not described in abstract |

# What is actually new?
- Biological novelty: First cross-species atlas resolving rare striatal neuronal subpopulations with paired transcriptomic + somatic CAG repeat expansion data in Huntington's disease; human-enriched opioid receptor sites mapped at single-cell resolution.
- Methodological novelty: Pairing snRNA-seq with somatic trinucleotide repeat expansion measurement at single-cell resolution in post-mortem human brain; cross-species atlas enabling direct pharmacological target comparison.
- Dataset or resource novelty: 109-sample human striatum atlas (dorsal + ventral) with disease-vulnerability mapping; largest post-mortem human striatum snRNA-seq resource by sample count.
- What was already known: Striatum subregions have distinct roles in reward vs motor control; Huntington's disease preferentially affects medium spiny neurons; antipsychotics act on dopamine receptors.

# Strengths
- Design strength: Largest sample count (109 human) for a striatum snRNA-seq atlas; cross-species comparison with 22 mouse samples enables direct model evaluation; multi-site consortium reduces single-center bias.
- Validation strength: GWAS integration and pharmacological data provide external cross-validation of cell-type annotations; somatic repeat expansion is an orthogonal disease-relevant readout.
- Reproducibility strength: Cell atlas resource publicly available (expected); multi-site consortium design.
- Translational or ecological realism: Post-mortem human brain is the gold standard for human striatal cell biology; GWAS integration links atlas to disease risk genetics.

# Limitations and bias risks
- Sample-size or power limitation: HD-specific subanalysis n Unknown; rare cell types may be underpowered despite large total N.
- Confounding: Multi-site with diverse tissue sources — PMI, fixation conditions, brain bank protocols vary; batch correction is critical and details Unknown.
- Batch or site effects: Multi-site (at least 7 institutions); batch handling Unknown — full text needed.
- Pseudoreplication risk: Number of individual donors vs 109 "samples" Unknown; multiple nuclei per donor — donor-level pseudoreplication risk if not modeled.
- Leakage or overfitting risk: GWAS integration may over-assign loci to cell types if cell-type reference is derived from overlapping data.
- Generalizability limitation: Striatum only; findings may not generalize to cortex, hippocampus, or other brain regions; species differences noted but mechanistic basis Unknown.
- Missing controls: Control vs HD breakdown Unknown; disease severity staging Unknown.
- Missing validation: Spatial transcriptomics referenced in keywords but extent and validation Unknown — full text needed; functional validation of pharmacological targets not in abstract.
- Author-stated limitations: Unknown — full text needed.
- Additional limitations identified during review: Post-mortem atlas misses activity-dependent gene expression; CAG repeat expansion methodology in post-mortem tissue may have technical caveats (cell-type contamination, allele dropout).

# Transferability to the user's work
- Directly transferable elements: Striatum cell-type reference atlas for annotation of new snRNA-seq or spatial data from striatum; HD neuronal vulnerability map as a disease-comparison reference; cross-species evaluation framework for validating mouse model cell-type fidelity.
- Elements requiring adaptation: Primarily a striatum resource — limited direct utility for cortex, hippocampus, or motor neuron (ALS, TBI) studies; GWAS integration approach is generalizable.
- Model, species, tissue, matrix, platform, or scale mismatch: Striatum only; does not address frontal cortex (AD/ADRD), motor cortex (ALS), or hippocampus (TBI).
- Assumptions required for transfer: Atlas cell-type annotations are accurate; cross-species transcriptional homology is valid for ortholog gene comparisons.
- Confidence: moderate (P2 utility — strong striatum reference resource; limited direct ALS/TBI/AD frontal cortex transferability)

# Practical implications
- Experimental implication: Use this atlas as a cell-type reference for new striatum snRNA-seq or spatial transcriptomics experiments; check atlas for cell-type markers before designing spatial panels targeting striatal cell types.
- Analysis implication: When integrating new striatum data, use this 109-sample atlas for cell-type annotation and label transfer; use the cross-species comparison framework to evaluate mouse model fidelity before committing to a striatal mouse model.
- Public dataset implication: Retrieve data accession (GEO or Broad Single Cell Portal or CellxGene) for use as snRNA-seq reference in deconvolution or annotation transfer tasks.
- Biomarker or translational implication: Human-enriched opioid receptor expression sites and antipsychotic action mapping provide a cell-type-level basis for understanding drug responses in neuropsychiatric disorders.
- Grant or manuscript implication: Cross-species atlas justifies choice of mouse model for striatal studies; HD vulnerability map provides a disease-relevance argument for cell-type-resolved spatial analysis.

# Contradictions and links
- Supports: yang_2025_simo, yang_2026_fgot (integration methods that benefit from a large reference atlas); castrobrant_2026 (post-mortem brain atlas framework)
- Contradicts: No direct contradictions in this library
- Replicates: N/A (resource paper)
- Methodologically comparable papers: castrobrant_2026 (post-mortem brain spatial atlas); plummer_2025 (benchmarking atlas quality)
- Relevant synthesis notes: None yet
- Relevant project decisions: None yet

# Follow-up actions
- [ ] Retrieve data accession (GEO or Broad Single Cell Portal or CellxGene) for 109-sample human striatum atlas
- [ ] Inspect full text: extract exact cell counts per subtype, clustering parameters, software versions, spatial transcriptomics platform and panel, CAG repeat expansion methodology, batch correction approach, donor-level vs sample-level n
- [ ] Evaluate atlas utility as a reference for striatum-relevant analyses in neurodegeneration projects
- [ ] Confirm whether spatial transcriptomics data was generated (keyword is suggestive but extent Unknown)

# Priority decision
- Priority: 2
- Retain for reference resource
- Rationale: Largest human striatum snRNA-seq atlas available; disease vulnerability mapping for Huntington's disease directly usable in neurodegeneration projects; cross-species comparison enables mouse model evaluation. Priority 2 (not P1) because primary focus is striatum — less immediately applicable to ALS/TBI/AD frontal cortex work that dominates this library's current projects.
