---
record_type: paper
record_status: verified
canonical_id: "10.1038/s41467-023-41033-y"
doi: "10.1038/s41467-023-41033-y"
pmid: "37714849"
pmcid: "PMC10504300"
title: "Divergent single cell transcriptome and epigenome alterations in ALS and FTD patients with C9orf72 mutation"
year: 2023
source_type: primary
peer_reviewed: true
full_text_checked: true
supplement_checked: false
code_checked: false
data_checked: false
last_verified: 2026-06-22
priority: 1
projects: []
topics: [neurodegeneration, ALS, AD_ADRD, single_cell, transcriptomics, multi_omics]
methods: [snRNAseq, snATACseq, analysis_method]
datasets: []
---

# Citation
- Full citation: Li J, Jaiswal MK, Chien JF, Kozlenkov A, Jung J, Zhou P, Gardashli M, Pregent LJ, Engelberg-Cook E, Dickson DW, Belzil VV, Mukamel EA, Dracheva S. "Divergent single cell transcriptome and epigenome alterations in ALS and FTD patients with C9orf72 mutation." *Nature Communications* 2023;14(1):5714.
- DOI / PMID / stable URL: [DOI](https://doi.org/10.1038/s41467-023-41033-y) · PMID 37714849 · PMC10504300
- Related preprint or published version: Peer-reviewed (Nat Commun).
- Correction, expression of concern, or retraction status: **Unknown** — not checked beyond retrieved PMC text (no notice seen) (added 2026-06-22).

*Source: PMC full text (~82k chars) retrieved from PubMed Central + metadata. According to PubMed, DOI [10.1038/s41467-023-41033-y](https://doi.org/10.1038/s41467-023-41033-y).*

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Fills the **C9orf72 / ALS-FTD glial-state** sub-theme. Provides paired snRNA-seq + snATAC-seq from human **motor (BA4) and frontal (BA9) cortex** across C9-ALS, C9-FTD, and controls — a direct cross-disease, cross-region, multi-omic complement to the existing ALS motor-cortex TDP-43 record (ruf_2026) and AD vulnerability records (leng_2021, castanho_2025). Identifies upper-layer (L2/3) excitatory neurons and reactive astrocytes as most affected in C9-ALS.
- Why it is more or less useful than neighboring literature: Concordant transcriptome + chromatin-accessibility + histone-mark evidence (not DE alone), and contrasts C9-ALS vs C9-FTD directly — strong for cell-type-resolved, genotype-defined neurodegeneration. Useful reusable reference layer for ALS/FTD cortex.

# Source inspection status
- Abstract inspected: yes
- Full text inspected: yes (PMC full text)
- Methods inspected: partial (cohort, regions, nuclei counts, DE/motif analyses; full wet-lab/seq params and exact stats in supplement not viewed)
- Supplement inspected: no (Supplementary Datasets 1–N referenced, not opened)
- Figures/tables inspected: no (callouts read; panels not viewed)
- Code repository inspected: no
- Data repository inspected: no (GEO/accession not confirmed from retrieved text)
- Missing material: exact GEO accession; full DE statistics; ArchR/peak-calling parameters; donor metadata table.

# Study question and hypothesis
- Primary question: What are the cell-type-, region-, and disease-specific transcriptomic and epigenomic alterations in C9orf72-mutation ALS vs FTD cortex?
- Stated hypothesis: C9-ALS and C9-FTD produce divergent, cell-type- and region-dependent molecular disruptions extending beyond motor neurons to other neurons and glia.
- Study type: Cross-sectional human post-mortem multi-omic single-nucleus study (snRNA-seq + snATAC-seq).

# Biological or clinical context
- Disease / exposure / process: C9orf72 repeat-expansion ALS and FTD.
- Organism: Human.
- Tissue / cell type: Motor cortex (Brodmann area 4) and dorsolateral prefrontal/frontal cortex (Brodmann area 9); 14 major cell types (8 neuronal, 6 glial).
- Model system: Autopsied human brain.
- Cohort or population: C9-ALS n=6, C9-FTD n=5, pathologically normal controls n=6 (Supplementary Dataset).
- Relevant stage, age, sex, genotype: All C9orf72 repeat-expansion carriers (ALS/FTD); controls pathologically normal. Demographics in supplement (not extracted).

# Study design
- Experimental or observational unit: Individual donor.
- Unit of inference: Donor-level, cell-type-resolved (donor pseudobulk for DE; subsampling to equalize power).
- Groups and sample size per group: C9-ALS n=6, C9-FTD n=5, control n=6 (per region; motor + frontal).
- Biological replicates: Donors per group (above).
- Technical replicates: Not extracted.
- Randomization / blinding: N/A (observational).
- Inclusion / exclusion criteria: C9orf72 expansion confirmed (ALS/FTD); controls pathologically normal. Nuclei QC (median 6351 UMIs / 2665 genes per nucleus).
- Batch structure: Multiple donors; technical biases modeled as covariates (Methods).
- Longitudinal / paired structure: Cross-sectional; matched motor + frontal cortex per donor.
- Controls and comparators: Pathologically normal controls; C9-ALS vs C9-FTD contrast.

# Experimental methods
- Assay / platform: Droplet snRNA-seq + snATAC-seq (10x-type; exact chemistry in supplement). chromVAR TF-motif deviation analysis (archetype motifs v2.0-beta) via ArchR.
- Sample preparation: Nuclei isolated from frozen post-mortem BA4 and BA9.
- Dose / perturbation: N/A.
- Timing / sampling schedule: Single post-mortem timepoint.
- Matrix: Frozen post-mortem cortex.
- Primary endpoint: Cell-type-specific DE genes and differential chromatin accessibility across disease and region.
- Secondary endpoints: TF-motif accessibility (chromVAR), reactive-astrocyte signatures, GO enrichment, C9-FTD glial changes.
- QC criteria: 105,120 high-quality nuclei retained (45,376 C9-ALS; 9,445 C9-FTD; 50,299 control); median 6351 UMIs / 2665 genes per nucleus.
- Exact reusable parameters and source location: Subsampling cell types to equal numbers to ensure equal statistical power before comparing DE-gene counts across layers (Results) — good practice to avoid depth-driven DE inflation.

# Computational and statistical methods
- Raw input: snRNA-seq UMI counts; snATAC fragment matrices.
- Preprocessing: 14 major cell types defined by grouping marker-sharing subpopulations.
- Normalization / feature filtering: Standard (supplement).
- Covariates / design: DE controlling for technical covariates (Methods); donor-level analysis.
- Statistical test or model: DE genes at FDR < 0.05; ATAC peaks via edgeR mode (FDR < 0.05); chromVAR deviation z-scores with GC/fragment-matched background peaks (ArchR addBgdPeaks).
- Multiple-testing correction: FDR (BH-type), threshold 0.05.
- Effect-size reporting: Fold-enrichment of DE-gene counts (e.g., L2/3 vs L5/6: 2.48× motor, 2.69× frontal); reactive-astrocyte gene fold-changes (e.g., 9.4× and 10× in motor cortex).
- Batch handling: Technical covariates; equalized subsampling for fair cross-type comparison.
- Validation strategy: Concordance across transcriptome + chromatin accessibility + histone modifications.
- External validation: Comparison to prior ALS/FTD literature (text).
- Software / versions: ArchR, chromVAR, edgeR (versions not extracted).
- Code availability: Not confirmed from retrieved text.

# Data and resource availability
- Repository and accession: **Unknown — not confirmed in retrieved PMC text.** snRNA/snATAC data presumably deposited (typical for Nat Commun); verify GEO/accession on the article page before reuse.
- Raw data available: Likely (controlled, human genomic) — unverified.
- Processed data available: Unverified.
- Metadata completeness: Supplementary Dataset (donor table) not inspected.
- Data-use restrictions: Human genomic data may be controlled — verify.
- Reusability for the user's work: Potentially high (ALS/FTD motor+frontal cortex multi-omic reference) conditional on confirming accession.

# Main findings
| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| C9-ALS shows pervasive transcriptomic change concordant with chromatin accessibility + histone marks | Reported | Abstract/Results | concordant multi-omic alterations | Yes | n=6 ALS |
| Upper-layer (L2/3) excitatory neurons and astrocytes most affected in C9-ALS | Reported | Results | most pronounced disruption | Yes | — |
| More DE genes in upper- vs deep-layer excitatory neurons | Reported | Results | 2.48× (motor), 2.69× (frontal), after power-matched subsampling | Yes | Subsampled for fair comparison |
| Reactive-astrocyte genes elevated in C9-ALS | Reported | Results | CD44 9.4× motor / 3.7× frontal; another gene 10× both | Yes | Activation + structural remodeling inferred |
| Neuronal GO: increased proteostasis/metabolism/protein synthesis, decreased neuronal function | Reported | Results | GO FDR<0.05 (mito, protein synthesis, proteostasis, nucleocytoplasmic transport, DNA damage) | Yes | — |
| C9-FTD frontal cortex has fewer high-quality neuronal nuclei + many glial DE changes | Reported | Abstract/Results | qualitative; glial-dominant changes | Partial | Lower neuronal yield may bias |

# What is actually new?
- Biological novelty: Cell-type- and region-specific divergence of C9-ALS vs C9-FTD; upper-layer excitatory + reactive-astrocyte vulnerability in C9-ALS with epigenomic concordance.
- Methodological novelty: Paired snRNA + snATAC + histone-mark integration in genotype-defined ALS/FTD cortex; power-matched DE comparison.
- Dataset/resource novelty: C9-ALS/C9-FTD motor + frontal cortex multi-omic atlas (accession to confirm).
- What was already known: ALS extends beyond motor neurons; glia implicated — here resolved by cell type, region, and chromatin.

# Strengths
- Design strength: Genotype-defined (single mutation) cohort; matched regions; multi-omic concordance.
- Validation strength: Cross-modality concordance (RNA + ATAC + histone marks); power-matched comparisons.
- Reproducibility strength: Explicit subsampling and covariate control described.
- Translational realism: Human post-mortem ALS/FTD cortex.

# Limitations and bias risks
- Sample-size / power: Small (6/5/6 donors); FTD especially limited and with lower neuronal yield.
- Confounding: PMI, age, sex not extracted; C9-FTD neuronal dropout may confound glial-vs-neuronal contrasts.
- Batch / site effects: Modeled as covariates; residual unquantified here.
- Pseudoreplication risk: Mitigated by donor-level analysis + subsampling (good).
- Leakage / overfitting risk: Low (not a predictive model).
- Generalizability: C9orf72 carriers only — may not extend to sporadic ALS/FTD or TDP-43 without C9 expansion.
- Missing controls / validation: External replication not in retrieved text.
- Author-stated limitations: Context-dependence across cell types/regions/diseases (abstract).
- Additional limitations identified during review: Data accession not verifiable from retrieved text; FTD neuronal yield asymmetry.

# Transferability to the user's work
- Directly transferable elements: ALS/FTD cortex cell-type taxonomy; reactive-astrocyte and L2/3-excitatory vulnerability axes; power-matched DE comparison practice; snRNA+snATAC integration design.
- Elements requiring adaptation: C9-specific genotype — compare to sporadic/TDP-43 ALS (ruf_2026) with caution.
- Mismatch: C9orf72 vs other ALS/FTD genotypes; cortex vs spinal cord.
- Assumptions required for transfer: Comparable nuclei QC and donor-level modeling.
- Confidence: moderate-high.

# Practical implications
- Experimental implication: Target upper-layer excitatory neurons and reactive astrocytes in ALS cortex studies; pair RNA with chromatin.
- Analysis implication: Subsample to equalize power before cross-cell-type DE-count comparisons; model technical covariates at donor level.
- Public dataset implication: Candidate ALS/FTD multi-omic reference — verify accession.
- Biomarker / translational implication: Reactive-astrocyte (CD44/CHI3L1) axis in C9-ALS cortex.
- Grant / manuscript implication: Citable cross-disease (ALS vs FTD), genotype-defined cell-type evidence.

# Contradictions and links
- Supports: Non-cell-autonomous (glial) and broad-neuronal involvement in ALS; reactive-astrocyte signatures (cf. leng_2021 AD astrocytes; chen_2025 astrogliosis).
- Contradicts: none directly identified.
- Replicates: Multi-omic concordance internally.
- Methodologically comparable papers: ruf_2026 (ALS motor-cortex TDP-43 snRNA/snATAC), leng_2021, castanho_2025; prieto-leon_2025 (pseudobulk/pseudoreplicate handling).
- Relevant synthesis notes: seed for "cell-type-resolved ALS/FTD cortical vulnerability."
- Relevant project decisions: (none yet)

# Follow-up actions
- [ ] Confirm and record GEO/accession + access terms
- [ ] Inspect supplement for donor metadata, exact stats, ArchR params
- [ ] Cross-link with ruf_2026 (TDP-43 ALS motor cortex)
- [ ] Check correction/retraction status

# Priority decision
- Priority: 1
- Read now (and retain as ALS/FTD cortex reference)
- Rationale: Strong cross-disease, cross-region, multi-omic single-nucleus study filling the C9orf72/glial-state gap and directly cross-linking to existing ALS/AD records; main gap is unverified data accession.
