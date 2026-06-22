---
record_type: paper
record_status: partial
canonical_id: "10.1038/s41467-026-69944-6"
doi: "10.1038/s41467-026-69944-6"
pmid: "41803120"
pmcid: "PMC12982666"
title: "Multi-modal dissection of cell-type specific TDP-43 pathology in the motor cortex"
year: 2026
source_type: primary
peer_reviewed: true
full_text_checked: true
supplement_checked: false
code_checked: false
data_checked: false
last_verified: 2026-06-22
priority: 1
projects: []
topics: [neurodegeneration, ALS, AD_ADRD, single_cell, transcriptomics, spatial_omics, multi_omics]
methods: [snRNAseq, snATACseq, FANS, spatial_transcriptomics]
datasets: []
---

# Citation
- Full citation: Ruf WP, Kühlwein JK, Meier L, Brockmann SJ, LeeBae J, Sadri-Vakili G, Yilmazer-Hanke D, Petri S, Thal DR, Grozdanov V, Danzer KM. "Multi-modal dissection of cell-type specific TDP-43 pathology in the motor cortex." *Nature Communications* 2026;17(1). 
- DOI / PMID / stable URL: [DOI](https://doi.org/10.1038/s41467-026-69944-6) · PMID 41803120 · PMC12982666
- Related preprint or published version: published, peer-reviewed (Nat Commun). Transparent Peer Review file available.
- Correction, expression of concern, or retraction status: **Unknown** — not checked (added 2026-06-22).

*Source: metadata and full text retrieved from PubMed / PubMed Central.*

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Provides a cell-type-resolved map of which cortical neuron subtypes carry TDP-43 pathology in human motor cortex, with paired chromatin accessibility. Candidate **public dataset for independent validation** of cell-type-specific cryptic-exon / DEG signatures, and a **methods precedent** for FANS-based sorting on TDP-43 nuclear signal coupled to snRNA-seq.
- Why it is more or less useful than neighboring literature: Combines (a) FANS nuclear sorting on TDP-43 status, (b) 10X Multiome (ATAC+RNA in the same nucleus), and (c) spatial layer context across a multi-center cohort — higher resolution of the *affected* cell identity than imputation-only studies (cf. Gittings et al., Wang et al.) which were limited to L2-3 ITC neurons.

# Source inspection status
- Abstract inspected: yes
- Full text inspected: yes (PMC full text, ~67k chars)
- Methods inspected: yes (partial — extracted key passages)
- Supplement inspected: no (Supplementary Data 1–25 referenced but not opened)
- Figures/tables inspected: no (figure callouts present but figures not viewed)
- Code repository inspected: no
- Data repository inspected: no
- Missing material: data/code **accession numbers** — still unresolved on 2026-06-22 (Nature auth-walled; PMC truncates before the Data Availability section). Supplementary cohort table (to confirm exact totals). Figures and Supplementary Data 1–25 not yet opened.

# Study question and hypothesis
- Primary question: Which transcriptional cell types in human motor cortex are affected by cytoplasmic TDP-43 pathology in ALS / ALS-FTD, and what cell-type-specific transcriptional/chromatin aberrations accompany it?
- Stated hypothesis: TDP-43 pathology and its downstream effects (e.g., cryptic exon inclusion) are **cell-type specific**, affecting distinct gene sets per cell type.
- Study type: Cross-sectional, multi-center, human post-mortem single-nucleus multi-omic + spatial study (case–control).

# Biological or clinical context
- Disease / exposure / process: ALS, ALS-FTD (sporadic and C9orf72-HRE familial); TDP-43 proteinopathy.
- Organism: Human.
- Tissue / cell type: Primary/ motor cortex; nuclei (excitatory & inhibitory neurons, glia; vascular/immune excluded).
- Model system: Human post-mortem flash-frozen tissue.
- Cohort or population: Multi-center (incl. Ulm, Hannover; Clinical Neuroanatomy of Ulm). Diagnosis by standardized criteria, pathologically confirmed by pTDP-43 pathology.
- Relevant stage, age, sex, genotype, severity: Genotyped for variants in 43 ALS-associated genes; sex used as a covariate in DGE. Other details in supplement (not inspected).

# Study design
- Experimental or observational unit: Individual donor (post-mortem).
- Unit of inference: Donor-level, cell-type-resolved.
- Groups and sample size per group: **Multi-omic (ATAC+RNA) cohort:** 30 sporadic ALS + 10 sporadic ALS-FTD + 7 familial ALS-FTD (C9orf72 HRE) + 32 controls. **FANS-seq subset:** 10 ALS-FTD samples (7 familial C9orf72 + 3 sporadic). The abstract's "20 ALS-FTD" aggregates these groups differently. [Reported] *Resolved 2026-06-22 from the PMC HTML; confidence **moderate** — a secondary extraction cited "72 unique samples" yet the listed groups sum to 79, so confirm exact totals against the supplementary cohort table.*
- Biological replicates: Multiple donors per group (see above).
- Technical replicates: Multiple samples pooled per 10X well; demultiplexed by genetic polymorphism.
- Randomization: Samples pooled per reaction well with random anonymized IDs assigned after demultiplexing; balanced label-permutation negative controls used.
- Blinding: Investigators **not** blinded to allocation during experiments/outcome assessment. [Reported]
- Inclusion / exclusion criteria: No data excluded from analyses; vascular & immune cells excluded due to low numbers. Sample size not predetermined by a statistical method (estimated from prior genomics studies). [Reported]
- Batch structure: Multi-center; multiplexed pooling per 10X well. [Reported]
- Longitudinal / paired / donor structure: Cross-sectional; donor-structured.
- Controls and comparators: 32 neurologically unaffected controls; balanced random-permutation negative control for spurious results.

# Experimental methods
- Assay / platform: 10X Genomics **Multiome (ATAC + RNA-seq) Kit** on Chromium Next GEM Chip J → >245,000 nuclei with simultaneous chromatin + transcriptome. Plus **FANS** (fluorescence-activated nuclei sorting) on neuronal TDP-43 signal coupled to snRNA-seq. [Reported]
- Sample preparation: ~80 mg tissue mechanically homogenized (7 ml glass grinder), filtered through 70 µm then 40 µm strainers; nuclei isolated via OptiPrep gradient (working solution 50% OptiPrep, 5 mM CaCl, 3 mM Mg(Ac)…). [Reported]
- Dose/force/perturbation: N/A (observational).
- Timing/sampling schedule: Single post-mortem timepoint.
- Matrix/conditions: Fresh/flash-frozen post-mortem motor cortex.
- Primary endpoint: Cell-type-resolved DEGs and cryptic transcriptional events associated with TDP-43 pathology.
- Secondary endpoints: Chromatin accessibility changes; spatial layer localization.
- Sequencing: snATAC libraries on NovaSeq 6000 SP PE150; snRNA (gene expression) libraries on NovaSeq 6000 S4 PE150 (Illumina). [Reported]
- QC criteria: **Unknown** (not extracted; likely in supplement).
- Exact reusable parameters and source location: TDP-43-signal FANS gating strategy (Fig. + Supplementary Fig., not inspected); genotyping across 43 ALS genes; Multiome well-pooling + genetic demultiplexing.

# Computational and statistical methods
- Raw input: 10X Multiome FASTQs (ATAC + GEX).
- Preprocessing: 10X CellRanger references (versions 2020-A and 2024-A; gene-type/name conversion via release-note spec files). For an external bulk comparison (Liu et al.), reads re-aligned with STAR (ENCODE RNA-seq params) and counted with Rsubread featureCounts. [Reported]
- Covariates and design formula: Sex used as a covariate in DGE (DESeq2 for the external comparison). Within-study DGE tooling: 'BulkR' R package for differential expression results. [Reported, partial]
- Statistical test or model: Fisher's exact test for overrepresentation; ANOVA (R 'stats'); effect sizes via 'effsize'/'effectsize'; accuracy/confusion via 'caret'. [Reported]
- Multiple-testing correction: Benjamini-Hochberg FDR; significance at FDR < 0.05 unless stated. [Reported]
- Chromatin: gene–peak correlation via Signac (default, 500 kbp window each side); peak annotation via ChIPseeker (6 genomic categories, last = peaks ≤3 kbp around TSS). [Reported]
- Enrichment: ShinyGO, StringDB, fgsea, clusterProfiler. [Reported]
- Batch handling: Multi-center inclusion + genetic demultiplexing; label-permutation negative control. [Reported]
- Validation strategy: Balanced sample-label permutation as negative control; cross-center cohort. [Reported]
- External validation / reuse: External **spatialLIBD / Maynard et al.** 10X Visium DLPFC dataset (12 slides, 3 controls) used for spatial/layer context. NOTE: this is **DLPFC**, not motor cortex — see caveat. [Reported]
- Software and versions: GEOquery, STAR, Rsubread, DESeq2, BulkR, Signac, ChIPseeker, spatialLIBD, ggplot2, ShinyGO, StringDB, fgsea, clusterProfiler, caret, effsize, effectsize; CellRanger refs 2020-A/2024-A. Exact versions **Unknown** (not extracted). [Reported, partial]
- Code availability: Stated as provided with the study; **specific repository/accession not extracted — verify.**

# Data and resource availability
- Repository and accession: **Unknown — still unverified after two attempts on 2026-06-22.** The Methods state raw data, processed data, and analysis code are provided with the study, but the actual accession could not be retrieved: (1) the Nature Communications page (`https://www.nature.com/articles/s41467-026-69944-6`) redirects to an authentication wall; (2) both the PMC full-text API and PMC HTML (`PMC12982666`) truncate before the Data/Code Availability section. Human post-mortem genomic data is commonly controlled-access (e.g., EGA), but this is not confirmed. *Do not cite an accession until confirmed — next try the article PDF or supplementary "Reporting Summary".*
- Raw data available: Stated yes (accession unverified).
- Processed data available: Stated yes (accession unverified).
- Metadata completeness: **Unknown** (supplementary cohort table not inspected).
- Data-use restrictions: **Unknown** — human post-mortem genomic data is commonly controlled-access; verify.
- Reusability for the user's work: Potentially high as a validation cohort for cell-type-specific TDP-43 / cryptic-exon signatures, **conditional on** confirming accession and access terms.

# Main findings
| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| Mainly excitatory cortical neurons are affected by TDP-43 pathology | Reported | Results/Abstract | qualitative | Yes | Figures not inspected |
| Most-affected types: IT L2-3 LINC00507-FREM3, L3-5 RORB-LNX2, L3-5 RORB-ADGRL4, L6 THEMIS-LINC00343; ET L5 FEZF2-NTNG1 | Reported | Results/Abstract | named subtypes | Yes | Subtype assignment depends on clustering |
| Most DEGs in the most abundant type (LINC00507 FREM3) in both ALS and ALS-FTD; ~5,471 genes identified | Reported | Results (Fig.) | 5,471 genes | Partial | Exact thresholds/figure not inspected |
| Transcriptional aberrations (e.g., cryptic exon inclusion) are cell-type specific, hitting distinct gene sets per type | Reported/Inference | Abstract/Results | qualitative | Yes | Central claim; supplement not inspected |
| >245,000 nuclei profiled with simultaneous ATAC + RNA (10X Multiome) | Reported | Results | >245,000 nuclei | Yes | — |

# What is actually new?
- Biological novelty: Cell-type-resolved identification of the *specific* vulnerable excitatory neuron subtypes carrying TDP-43 pathology in motor cortex, with cell-type-specific cryptic/DEG sets.
- Methodological novelty: FANS sorting on TDP-43 nuclear signal coupled to snRNA-seq + same-nucleus Multiome at cohort scale.
- Dataset/resource novelty: Large multi-center human motor-cortex single-nucleus multi-omic dataset (accession to be confirmed).
- What was already known: TDP-43 pathology in >95% ALS / >50% FTD; prior imputation studies limited to L2-3 ITC neurons.

# Strengths
- Design strength: Multi-center cohort; same-nucleus multi-omics; balanced permutation negative control; genetic demultiplexing reduces sample-swap risk.
- Validation strength: Permutation negative control; cross-center inclusion.
- Reproducibility strength: Authors state raw + processed data + code released; random seeds specified in code/methods.
- Translational realism: Human post-mortem, pathology-confirmed.

# Limitations and bias risks
- Sample-size / power: No statistical pre-specification of sample size; rare subtypes and vascular/immune cells under-sampled (excluded).
- Confounding: Post-mortem interval, agonal state, medication, comorbidity — **Unknown** (not extracted); sex modeled as covariate.
- Batch/site effects: Multi-center → site/batch confounding risk; mitigated by pooling + permutation but not fully characterized here.
- Pseudoreplication risk: Many nuclei per donor — donor-level inference required; confirm mixed/pseudobulk modeling in supplement.
- Leakage/overfitting risk: Cell-type assignment + downstream DEG on same data; verify independent validation in supplement.
- Generalizability: Motor cortex only; spatial context borrowed from **DLPFC** (Maynard et al.), a different region — layer mapping is approximate.
- Missing controls / validation: Internal orthogonal validation of cryptic events (e.g., RT-PCR/protein) **Unknown**.
- Blinding: Investigators not blinded.
- Author-stated limitations: A relevant aspect possibly associated with lack of some cell-type differences (text truncated; revisit).
- Additional limitations identified during review: Abstract vs methods cohort-count discrepancy (resolved 2026-06-22: multi-omic 30/10/7/32 + FANS subset of 10; abstract aggregates differently); data accession not verifiable from open sources (Nature auth-walled, PMC truncated).

# Transferability to the user's work
- Directly transferable elements: FANS-on-TDP-43 + snRNA-seq workflow; cell-type taxonomy (Allen-style IT/ET nomenclature); donor-aware DGE + permutation negative control design; Signac/ChIPseeker peak-to-gene approach.
- Elements requiring adaptation: Region (motor cortex) and disease focus; spatial mapping if a true motor-cortex spatial reference is needed.
- Mismatch: If user works in a different region/model, the specific vulnerable-subtype list may not transfer.
- Assumptions required for transfer: Comparable nuclei QC, donor-level modeling, and access to the released data.
- Confidence: moderate (pending supplement + accession verification).

# Practical implications
- Experimental implication: Strong precedent for sorting strategy and same-nucleus multi-omic design for TDP-43 work.
- Analysis implication: Adopt donor-aware DGE with balanced label-permutation negative controls; FDR < 0.05 (BH); gene–peak linkage via Signac.
- Public dataset implication: Candidate independent-validation cohort for cell-type-specific cryptic-exon/DEG signatures — **verify accession & access first**.
- Biomarker/translational implication: Cell-type-specific cryptic events as candidate targets/markers.
- Grant/manuscript implication: Citable evidence that TDP-43 transcriptional effects are cell-type specific.

# Contradictions and links
- Supports: Cell-type-specific TDP-43 vulnerability (extends imputation-based work).
- Contradicts: Prior view limited to L2-3 ITC neurons — broadens the affected set.
- Replicates: Conceptually replicates upper-layer ITC vulnerability while adding RORB/THEMIS/FEZF2 types.
- Methodologically comparable papers: Gittings et al.; Wang et al.; Liu et al. (bulk, re-analyzed); Maynard et al. (spatialLIBD, reused).
- Relevant synthesis notes: (none yet — candidate seed for a "cell-type-specific TDP-43 vulnerability" synthesis)
- Relevant project decisions: (none yet — no project created)

# Follow-up actions
- [ ] Record the exact data/code accession + access terms — BLOCKED 2026-06-22 (Nature auth-walled; PMC truncated). Retry via the article PDF or the supplementary Reporting Summary.
- [x] Resolve cohort group counts — done 2026-06-22 (multi-omic 30 sALS / 10 sALS-FTD / 7 fALS-FTD C9orf72 / 32 control; FANS subset 10); still confirm exact totals (72 vs 79) against the supplementary cohort table
- [ ] Confirm donor-level (pseudobulk/mixed-model) statistics and any orthogonal validation of cryptic events
- [ ] If accession confirmed and reusable, create a dataset record in 03_DATASETS/ and link it here
- [ ] Consider seeding a synthesis on cell-type-specific TDP-43 vulnerability (≥3 sources available)
- [ ] Check retraction/correction status

# Priority decision
- Priority: 1
- Read now (and verify supplement/data)
- Rationale: Directly relevant, peer-reviewed, multi-omic human cohort that could serve as an independent validation dataset and a strong methods precedent; the main gating items (accession, exact cohort counts) are verifiable follow-ups, not fatal gaps.
