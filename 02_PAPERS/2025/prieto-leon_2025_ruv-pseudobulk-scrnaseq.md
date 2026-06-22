---
record_type: paper
record_status: verified
canonical_id: "10.1093/nargab/lqaf179"
doi: "10.1093/nargab/lqaf179"
pmid: "41368194"
pmcid: "PMC12684399"
title: "Removal of unwanted variation in pseudobulk analysis of single-cell RNA sequencing data and the leveraging of pseudoreplicates"
year: 2025
source_type: method
peer_reviewed: true
full_text_checked: true
supplement_checked: false
code_checked: false
data_checked: true
last_verified: 2026-06-22
priority: 1
projects: []
topics: [transcriptomics, single_cell, multi_omics]
methods: [analysis_method, snRNAseq, scRNAseq]
datasets: []
---

# Citation
- Full citation: Prieto León S, De Troyer E, Geys H, Van den Berge K, Thas O. "Removal of unwanted variation in pseudobulk analysis of single-cell RNA sequencing data and the leveraging of pseudoreplicates." *NAR Genomics and Bioinformatics* 2025;7(4):lqaf179.
- DOI / PMID / stable URL: [DOI](https://doi.org/10.1093/nargab/lqaf179) · PMID 41368194 · PMC12684399
- Related preprint or published version: Peer-reviewed (NAR Genom Bioinform), open access.
- Correction, expression of concern, or retraction status: **Unknown** — not checked (added 2026-06-22).

*Source: metadata + PMC full text retrieved from PubMed / PubMed Central. According to PubMed, DOI [10.1093/nargab/lqaf179](https://doi.org/10.1093/nargab/lqaf179).*

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: A **donor-aware, batch-confounding-resistant methodology** for pseudobulk differential expression in scRNA-seq. It (1) benchmarks how to apply RUV (RUV2/RUVIII/RUV4) in pseudobulk — concluding **per-cell-type estimation (Trail 2)** is best — and (2) introduces **RUVIII PBPS**, which controls FDR when there are no technical replicates or trustworthy negative-control genes. Directly addresses the signals-file priority "donor-aware differential expression" and "benchmark datasets that expose batch/confounding limits." High-value reusable method for the user's snRNA-seq DE work (e.g., validating cell-type DEGs from Ruf 2026 / Castanho 2025).
- Why it is more or less useful than neighboring literature: Concretely operationalizes pseudobulk RUV with FDR/TPR evidence under confounding and model misspecification — more actionable than generic batch-correction reviews. It exposes a real failure mode (negative-control-gene misspecification → inflated FDR) and offers a workaround (PBPS). Limitation: single benchmark dataset (lupus PBMC, immune cell types), not brain tissue.

# Source inspection status
- Abstract inspected: yes
- Full text inspected: yes (PMC full text, including Methods, simulations, case study, discussion)
- Methods inspected: yes (three "trails", PBPS algorithm, simulation design)
- Supplement inspected: no (Appendices A-F referenced; supplemental file not opened)
- Figures/tables inspected: no (figure callouts read; panels not viewed)
- Code repository inspected: no (a GitHub repo is referenced — URL not extracted)
- Data repository inspected: yes (benchmark dataset is public — lupus, CZ CELLxGENE)
- Missing material: GitHub URL/version; appendix simulation parameters; exact effect-size tables.

# Study question and hypothesis
- Primary question: How should RUV methods be implemented for pseudobulked scRNA-seq differential expression to control FDR and preserve biological signal, and what can be done when technical replicates / negative-control genes are unavailable?
- Stated hypothesis: Applying RUV per cell type (Trail 2) and/or generating pseudobulk pseudosamples (PBPS) controls FDR under confounding/misspecification better than naive or batch-as-covariate approaches.
- Study type: Methods development + benchmarking (simulation on real data + case study).

# Biological or clinical context
- Disease / exposure / process: Methodological (batch/unwanted variation in scRNA-seq); case study = systemic lupus erythematosus (SLE) vs control PBMC.
- Organism: Human (PBMC).
- Tissue / cell type: PBMC; 8 of 11 cell types analyzed (CD4/CD8 T, classical/nonclassical monocytes, conventional/plasmacytoid DC, NK, B).
- Model system: Public scRNA-seq benchmark data.
- Cohort or population: Lupus dataset from CZ CELLxGENE Discover; control subset 37 healthy (European/Asian, 24-28 y); case subset 85 SLE+control samples (29-34 y); 4 sequencing "processing cohorts" as the batch variable.
- Relevant stage, age, sex, genotype, severity: Subsets curated to limit age/sex confounding.

# Study design
- Experimental or observational unit: Subject (single-cell sample); pseudobulk sample = sample × cell type.
- Unit of inference: Subject-level, per cell type (pseudobulk).
- Groups and sample size per group: Control subset 37 subjects; case subset 85 samples; 880 PBPS generated in the case study (10 per group).
- Biological replicates: Subjects per group (above).
- Technical replicates: Unbalanced across processing cohorts (cohort 4 has none — motivates PBPS).
- Randomization: Mock-treatment assignment in simulations (balanced or confounded designs).
- Blinding: N/A.
- Inclusion / exclusion criteria: Subsets selected to control age/sex; 8/11 cell types used.
- Batch structure: 4 processing cohorts = primary known unwanted-variation source; cohorts partly confounded with disease/ethnicity in case subset.
- Longitudinal / paired / donor structure: Donor-structured pseudobulk; within-individual correlation across cell-type pseudobulk samples explicitly modeled.
- Controls and comparators: Naive UQ; UQ Batch (batch as fixed effect); RUV2/RUVIII/RUV4 × Trails 1/2/3; RUVIII Batch; RUVIII PBPS.

# Experimental methods
- Assay / platform: Reanalysis of public scRNA-seq (no wet lab).
- Primary endpoint: FDR control and TPR in simulated DE; batch-removal metrics (ASW, RLE, PCA).
- Secondary endpoints: ISG-signature recovery and GSEA overlap in the lupus case study.
- Exact reusable parameters and source location: Trail 2 (per-cell-type RUV estimation) recommended; 5 unwanted factors used; pseudo-count of 1 added before log; PBPS algorithm fully specified (group by biological covariates + known unwanted source, resample cells with replacement at average cell count, pseudobulk).

# Computational and statistical methods
- Raw input: scRNA-seq counts → pseudobulk (sum cells by sample × cell type).
- Preprocessing: Upper-quartile (UQ) normalization; pseudobulk aggregation (edgeR-style downstream).
- Normalization / batch handling: RUV2, RUVIII, RUV4 (R `ruv` package) applied via three "trails": T1 all-cells (assumes independence — flawed), T2 per-cell-type (recommended), T3 per-sample (loses biological signal). New: **RUVIII PBPS** uses pseudobulk pseudosamples as negative-control samples, allowing all genes as negative controls.
- Statistical test or model: DE per cell type (bulk-style, e.g., edgeR) with RUV factors as covariates; simulations across 100 datasets with DE in a fraction of genes; balanced vs confounded vs misspecified-model scenarios.
- Multiple-testing correction: FDR (evaluated at multiple nominal levels; TPR/FDR curves).
- Effect-size reporting: TPR vs FDR tradeoff curves; ASW (e.g., processing-cohort ASW 0.41→<0.16 after RUV); case-study DEG counts (e.g., naive UQ 1727 CD4T DEGs, 1012 also DE across batches → inflation).
- Validation strategy: Simulated DE on real data with known truth; ISG signature as sensitivity proxy; Kruskal-Wallis association of RUV factors with batch.
- External validation: Single benchmark dataset (lupus); cross-cell-type consistency reported.
- Software and versions: R `ruv` package; edgeR-style DE; CZ CELLxGENE for data. Versions not extracted.
- Code availability: GitHub repository referenced (URL/version not extracted).

# Data and resource availability
- Repository and accession: Lupus benchmark dataset from **CZ CELLxGENE Discover** (public). Specific dataset DOI/accession not re-extracted.
- Raw data available: Yes (public CELLxGENE).
- Processed data available: Yes (subsets defined in paper; details in Appendix C).
- Metadata completeness: High for the curated subsets (cohort, ethnicity, age, disease).
- Data-use restrictions: Public.
- Reusability for the user's work: **High** — method + benchmark directly reusable for donor-aware pseudobulk DE; code on GitHub.

# Main findings
| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| RUV should be estimated per cell type (Trail 2) for pseudobulk scRNA-seq | Reported | Results/Discussion | T2 best across RUV2/RUVIII/RUV4 | Yes | Demonstrated on lupus PBMC |
| Trail 1 (all-cells) introduces RLE shifts; Trail 3 (per-sample) erodes biological signal | Reported | Results / Fig.4-5 | T3 lowers mock-treatment ASW <0.6 | Yes | — |
| Under confounding/misspecification, RUV2 or RUVIII (T1/T2) control FDR; RUV4 inflates FDR | Reported | Results / Fig.5 | RUV4 inflated FDR + lower TPR | Yes | RUV4 not recommended in these settings |
| RUVIII PBPS controls FDR when no technical replicates / negative-control genes exist | Reported | Results / Fig.6,8 | better FDR than UQ Batch in misspecified models | Yes | Needs biological + technical metadata |
| Negative-control-gene misspecification inflates FDR / lowers TPR | Reported | Results 3.2.1 / Appendix F | two NC sets → discordant DEGs | Yes | Practical warning |
| Naive (no-RUV) DE inflates DEGs under batch-disease confounding | Reported | Case study | 1727 CD4T DEGs, 1012 batch-driven | Yes | Demonstrates real risk |

# What is actually new?
- Methodological novelty: Systematic guidance on *how* to apply RUV in pseudobulk (three trails; per-cell-type recommended) and the **RUVIII PBPS** pseudosample strategy enabling RUVIII without technical replicates/negative-control genes (fewer samples needed than PRPS).
- Biological novelty: N/A (methods paper; lupus used as testbed).
- Dataset or resource novelty: A reproducible pseudobulk-RUV benchmark + GitHub code.
- What was already known: RUV family for bulk; pseudobulk DE practice; PRPS for replicate-free RUVIII in bulk.

# Strengths
- Design strength: Simulation-on-real-data with known truth; balanced/confounded/misspecified scenarios; multiple RUV methods × trails.
- Validation strength: FDR/TPR curves at multiple nominal levels; ISG-signature sensitivity proxy; explicit confounding stress tests.
- Reproducibility strength: Public benchmark data + GitHub code; standard metrics (ASW/RLE/PCA).
- Translational realism: Models real failure mode (batch-disease confounding) that affects donor-structured studies.

# Limitations and bias risks
- Sample-size / power: Single benchmark (lupus PBMC); modest subject counts.
- Confounding: Deliberately studied; conclusions may depend on lupus-specific structure.
- Batch / site effects: The object of study (processing cohort).
- Pseudoreplication risk: Explicitly handled (within-individual correlation; pseudobulk by donor×cell type).
- Leakage / overfitting risk: Simulations control truth; NC-gene misspecification highlighted as a real risk.
- Generalizability: Immune PBMC cell types only — **not validated on brain/nuclei data** (transferability caveat for the user's snRNA-seq).
- Missing controls / validation: Only one real dataset; no multi-tissue benchmark.
- Author-stated limitations: PBPS count chosen arbitrarily (could be optimized); PBPS needs biological+technical metadata; RUVIII Batch discouraged under high factor-batch correlation (multicollinearity).
- Additional limitations identified during review: GitHub URL/versions not extracted; appendices not inspected.

# Transferability to the user's work
- Directly transferable elements: Trail-2 per-cell-type RUV recommendation; RUVIII PBPS for replicate-free designs; ASW/RLE/PCA batch diagnostics; the confounding-aware FDR/TPR evaluation framework.
- Elements requiring adaptation: Apply to snRNA-seq nuclei / brain cell types (validate, since benchmark is PBMC); choose PBPS count by within-group variance.
- Model, species, tissue, matrix, platform, or scale mismatch: PBMC immune cells vs brain nuclei; droplet scRNA vs snRNA.
- Assumptions required for transfer: At least one known unwanted-variation source; exchangeability of cells within biological×technical subgroups.
- Confidence: high for the methodology; moderate for direct brain-data transfer.

# Practical implications
- Experimental implication: Record batch/processing metadata at the donor level to enable RUV/PBPS.
- Analysis implication: Use per-cell-type RUV (Trail 2); avoid RUV4 in confounded settings; use RUVIII PBPS when lacking technical replicates/negative-control genes; always run ASW/RLE/PCA batch diagnostics before DE.
- Public dataset implication: Reusable lupus benchmark + code for testing one's own pseudobulk pipeline.
- Biomarker / translational implication: Reduces false-positive DEG inflation that would mislead biomarker discovery.
- Grant / manuscript implication: Citable, principled donor-aware pseudobulk DE workflow.

# Contradictions and links
- Supports: Donor-level/pseudobulk inference over cell-level pseudoreplication; need for batch-aware DE.
- Contradicts: Naive batch-as-covariate (UQ Batch) sufficiency claims under confounding/misspecification; routine RUV4 use.
- Replicates: Extends PRPS concept (bulk) to pseudobulk via PBPS.
- Methodologically comparable papers: Ruf 2026 / Leng 2021 / Castanho 2025 (donor-structured snRNA DE that would benefit from this RUV/PBPS approach); Zappia 2025 (complementary atlas-integration benchmark).
- Relevant synthesis notes: candidate for a "donor-aware single-cell DE best-practices" methods synthesis.
- Relevant project decisions: (none yet)

# Follow-up actions
- [ ] Extract GitHub URL + package versions; inspect Appendices C-F for simulation parameters
- [ ] Validate Trail-2 / RUVIII PBPS on a brain snRNA-seq dataset before adopting for ALS/AD work
- [ ] Consider a methods record in 04_METHODS/computational/ for the pseudobulk-RUV workflow
- [ ] Check retraction/correction status

# Priority decision
- Priority: 1
- Read now (retain for methods)
- Rationale: Directly improves donor-aware pseudobulk DE (a recurring need across the library's snRNA-seq records), with a concrete recommendation (Trail 2) and a replicate-free workaround (RUVIII PBPS), plus public benchmark + code. Brain-data transfer needs a quick validation, hence the one follow-up.
