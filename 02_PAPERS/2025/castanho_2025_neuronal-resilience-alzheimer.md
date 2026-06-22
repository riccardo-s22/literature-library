---
record_type: paper
record_status: verified
canonical_id: "10.1186/s13024-025-00892-3"
doi: "10.1186/s13024-025-00892-3"
pmid: "41035073"
pmcid: "PMC12487324"
title: "Molecular hallmarks of excitatory and inhibitory neuronal resilience to Alzheimer's disease"
year: 2025
source_type: primary
peer_reviewed: true
full_text_checked: true
supplement_checked: false
code_checked: false
data_checked: true
last_verified: 2026-06-22
priority: 2
projects: []
topics: [neurodegeneration, AD_ADRD, aging, single_cell, transcriptomics, multi_omics]
methods: [snRNAseq, bulk_RNAseq]
datasets: []
---

# Citation
- Full citation: Castanho I, Naderi Yeganeh P, Boix CA, Morgan SL, Mathys H, Prokopenko D, White B, Soto LM, Pegoraro G, Shah S, Ploumakis A, Kalavros N, Bennett DA, Lange C, Kim DY, Bertram L, Tsai LH, Kellis M, Tanzi RE, Hide W. "Molecular hallmarks of excitatory and inhibitory neuronal resilience to Alzheimer's disease." *Molecular Neurodegeneration* 2025;20(1):103.
- DOI / PMID / stable URL: [DOI](https://doi.org/10.1186/s13024-025-00892-3) · PMID 41035073 · PMC12487324
- Related preprint or published version: Peer-reviewed (Mol Neurodegener), open access.
- Correction, expression of concern, or retraction status: **Unknown** — not checked (added 2026-06-22).

*Source: metadata + PMC full text retrieved from PubMed / PubMed Central. According to PubMed, DOI [10.1186/s13024-025-00892-3](https://doi.org/10.1186/s13024-025-00892-3).*

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Defines transcriptomic/cellular hallmarks of **cognitive resilience** (cognition preserved despite AD pathology) by integrating ROSMAP bulk RNA-seq + multiregion snRNA-seq + WGS rare variants. Positions resilience as an intermediate AD state; flags excitatory/inhibitory balance, MEF2C/RELN/ATP8B1 markers, LINGO1 downregulation, chaperone reorganization, and SST interneuron involvement. A strong **public-data-reuse template** (AMP-AD/ROSMAP) and a complementary contrast to vulnerability-focused studies (Leng 2021, Ruf 2026).
- Why it is more or less useful than neighboring literature: Multi-modal integration (bulk + snRNA + genetics) on a large, deeply-phenotyped cohort with an explicit resilient group and an independent validation snRNA-seq dataset — more decision-relevant for "what protects neurons" than DE-only case/control studies. Effect sizes are modest (DLPFC) and the design is observational/cross-sectional.

# Source inspection status
- Abstract inspected: yes
- Full text inspected: yes (PMC full text, ~79k chars)
- Methods inspected: yes (cohort, bulk + snRNA pipelines, DE models, EWCE, CellChat, rare-variant analysis)
- Supplement inspected: no (supplementary tables referenced, not viewed)
- Figures/tables inspected: no (callouts read; panels not viewed)
- Code repository inspected: no
- Data repository inspected: partial — primary data are **public ROSMAP/AMP-AD** (bulk via syn2580853; multiregion snRNA from prior ROSMAP publications). Exact snRNA accession not re-extracted.
- Missing material: specific snRNA accession/synID; supplementary subject-count tables; code repository.

# Study question and hypothesis
- Primary question: What molecular and cellular signatures distinguish cognitively resilient individuals (preserved cognition despite AD pathology) from AD and controls?
- Stated hypothesis: Resilience is a definable intermediate state characterized by preserved neuronal function and balanced network activity, driven by specific excitatory/inhibitory populations and survival signaling.
- Study type: Observational, cross-sectional multi-omic integration (bulk RNA-seq + snRNA-seq + WGS genetics) of a human post-mortem cohort; reuse of public ROSMAP data.

# Biological or clinical context
- Disease / exposure / process: Alzheimer's disease; cognitive resilience/reserve; E/I balance.
- Organism: Human.
- Tissue / cell type: DLPFC (bulk + snRNA), entorhinal cortex, hippocampus (snRNA); excitatory/inhibitory neurons, astrocytes, microglia, OPCs.
- Model system: Human post-mortem (ROSMAP).
- Cohort or population: ROSMAP (Religious Orders Study / Rush Memory and Aging Project). Bulk RNA-seq n=631 DLPFC; multiregion snRNA-seq n=48 subjects. Independent DLPFC snRNA-seq used for validation.
- Relevant stage, age, sex, genotype, severity: Resilient group defined as no cognitive impairment + moderate/frequent plaques + Braak III-VI + age > 80. APOE status modeled.

# Study design
- Experimental or observational unit: Individual ROSMAP participant.
- Unit of inference: Donor-level; cell-type-resolved (snRNA).
- Groups and sample size per group (bulk RNA-seq): AD n=187; Resilient (RES) n=68; Control (CTRL) n=44; Presymptomatic (PRE) n=83; "Other" n=249.
- snRNA-seq: n=48 subjects across DLPFC/EC/HC, classified into AD/RES/CTRL/age-matched groups (per-group cell/subject counts in supplementary table — not extracted).
- Biological replicates: Donors per group (above).
- Technical replicates: N/A (reused data).
- Randomization / blinding: N/A (observational reuse).
- Inclusion / exclusion criteria: Group definitions by pathology (plaques/Braak) + cognition (NCI/MCI/AD); a BIDMC validation set excluded comorbidities (diabetes) and screened for TDP-43.
- Batch structure: Modeled as covariate (bulk); QC per region (snRNA).
- Longitudinal / paired / donor structure: Cross-sectional; deep ante-mortem cognitive phenotyping.
- Controls and comparators: CTRL (low pathology, no impairment); contrasts AD vs RES, AD vs CTRL, RES vs CTRL, AD vs PRE, PRE vs CTRL, RES vs PRE.

# Experimental methods
- Assay / platform: Reused ROSMAP bulk RNA-seq (DLPFC) and droplet snRNA-seq (multiregion); WGS-derived rare/common variants.
- Sample preparation: As in original ROSMAP publications (not re-performed).
- Primary endpoint: DEGs and cell-type enrichment distinguishing resilience.
- Secondary endpoints: Cell-proportion shifts (Dirichlet); ligand-receptor signaling (CellChat, e.g., BDNF-NTRK2, ANGPT2-TEK, SST/SSTR1); rare-variant cell-type enrichment (EWCE).
- Exact reusable parameters and source location: Bulk normalization = CQN (library size + GC + gene length); iterative PCA confounder selection (AMP-AD harmonization protocol); covariates: batch, sex, RIN, %coding, %intergenic, PMI, age at death, %pass-filter aligned.

# Computational and statistical methods
- Raw input: ROSMAP bulk read counts (syn2580853, AMP-AD); ROSMAP multiregion snRNA-seq processed counts (protein-coding, doublet/mito/ribo-filtered).
- Preprocessing: Bulk CQN normalization; Limma-Voom residualization for confounders. snRNA re-annotated per region; QC per region.
- Statistical test or model: Bulk DEGs by Limma-Voom + moderated t-tests adjusting for covariates incl. APOE; FDR correction; thresholds FDR < 0.1 and |log2FC| > log2(1.1). snRNA DEGs by **MAST** per cell subtype per region; **Bonferroni** correction; adj-P < 0.1 and |log2FC| > 0.2. Cell composition by **Dirichlet** test. Rare-variant enrichment by **EWCE**. Cell-cell communication by **CellChat**.
- Multiple-testing correction: FDR (bulk), Bonferroni (snRNA/MAST).
- Effect-size reporting: log2FC with explicit thresholds; modest DLPFC effects (rationale given).
- Batch handling: Covariate adjustment (bulk); per-region QC (snRNA).
- Validation strategy: Independent DLPFC snRNA-seq dataset confirms rare-variant cell-type enrichment; BIDMC tissue set (comorbidity-excluded).
- External validation: Yes (independent snRNA-seq).
- Software and versions: CQN, Limma-Voom, MAST, EWCE, CellChat (versions not extracted).
- Code availability: Not extracted.

# Data and resource availability
- Repository and accession: Bulk RNA-seq via **AMP-AD Knowledge Portal, synID syn2580853** (ROSMAP DLPFC). Multiregion snRNA-seq from prior ROSMAP publications (specific synID not re-extracted). All primary data are public/consortium-accessible.
- Raw data available: Yes (ROSMAP/AMP-AD, controlled-ish access via Synapse data-use agreement).
- Processed data available: Yes (consortium-processed counts).
- Metadata completeness: High (deep ROSMAP clinical/pathologic phenotyping).
- Data-use restrictions: AMP-AD/Synapse data-use terms apply.
- Reusability for the user's work: **High** — well-annotated, public, multi-modal AD reference suitable for independent validation and resilience/vulnerability contrasts; ready DE/normalization pipeline to mirror.

# Main findings
| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| Resilience is a transcriptomic intermediate state on the AD continuum | Reported/Inference | Results | qualitative (polygenic + DE positioning) | Yes | Cross-sectional |
| Only GFAP and KLF4 distinguish RES from CTRL at bulk tissue level | Reported | Results / Fig | 2 genes at tissue level | Yes | Modest DLPFC signal |
| Broad LINGO1 downregulation + chaperone reorganization (Hsp90 down; Hsp40/70/110 up) in resilient excitatory neurons | Reported | Results / snRNA | cell-type-specific DE | Yes | MAST/Bonferroni thresholds |
| MEF2C, ATP8B1, RELN mark resilient neurons; MEF2C+ inhibitory neurons over-represented in resilient brains | Reported | Results / snRNA + Dirichlet | composition + markers | Yes | Subtype annotation dependent |
| EC excitatory subtypes signal via BDNF-NTRK2 (LINGO1-modulated) and ANGPT2-TEK | Reported | Results / CellChat | ligand-receptor inference | Partial | CellChat is inferential |
| Rare protective variants enriched in excitatory neurons/OPCs; common risk variants biased to microglia/immune | Reported | Results / EWCE | cell-type enrichment | Yes | Validated in independent DLPFC snRNA |
| Vulnerable SST cortical interneurons survive in resilience (compensation against hyperexcitability) | Reported/Inference | Results | composition + SST signaling | Partial | Interpretive |

# What is actually new?
- Biological novelty: Cell-type-resolved molecular hallmarks of resilience (E/I balance, chaperone reorganization, neurotrophic/angiopoietin signaling, SST interneuron compensation).
- Methodological novelty: Discrete resilience classification integrated across bulk + snRNA + rare/common genetics with EWCE + CellChat.
- Dataset or resource novelty: Reuse/integration template over public ROSMAP/AMP-AD data.
- What was already known: Cognitive resilience/reserve concept; RORB+ EC vulnerability (Leng 2021, cited); microglial bias of common AD risk variants.

# Strengths
- Design strength: Large, deeply-phenotyped ROSMAP cohort; explicit resilient group; multi-omic + genetic integration; independent validation snRNA-seq.
- Validation strength: Rare-variant enrichment confirmed in an independent DLPFC dataset.
- Reproducibility strength: Public data + standard, documented pipelines (CQN, Limma-Voom, MAST, EWCE, CellChat) with explicit thresholds/covariates.
- Translational realism: Human, ante-mortem cognition linked to molecular state.

# Limitations and bias risks
- Sample-size / power: snRNA n=48; some subgroups small; DLPFC effects modest by design (relaxed thresholds).
- Confounding: Observational; resilience defined by thresholds; residual confounding despite covariate adjustment.
- Batch / site effects: Addressed via covariates/QC; not fully eliminable in reused data.
- Pseudoreplication risk: snRNA donor-level grouping used (MAST per subtype) — confirm mixed-model handling in supplement.
- Leakage / overfitting risk: Marker discovery + interpretation on overlapping data; partial independent validation present.
- Generalizability: ROSMAP (largely older, specific recruitment); cortical/hippocampal regions.
- Missing controls / validation: Functional validation of survival signaling not performed (transcriptomic/inferential).
- Author-stated limitations: Inherent to cross-sectional, threshold-based resilience definition.
- Additional limitations identified during review: Exact snRNA synID not re-extracted; CellChat ligand-receptor results are inferential.

# Transferability to the user's work
- Directly transferable elements: ROSMAP/AMP-AD reuse pipeline (CQN + Limma-Voom + confounder PCA); MAST per-subtype DE with explicit thresholds; EWCE for variant-to-cell-type enrichment; resilience vs vulnerability framing.
- Elements requiring adaptation: Disease focus (AD) and brain regions; resilience definition for other disorders.
- Model, species, tissue, matrix, platform, or scale mismatch: AD cortex/hippocampus vs other neurodegeneration.
- Assumptions required for transfer: Access to ROSMAP/AMP-AD; comparable phenotyping.
- Confidence: moderate-high for methods/data reuse.

# Practical implications
- Experimental implication: Provides candidate resilience markers (MEF2C, RELN, ATP8B1, LINGO1, chaperones) for targeted study.
- Analysis implication: Adoptable public-data DE pipeline + EWCE + CellChat workflow.
- Public dataset implication: Strong independent-validation/reference resource (ROSMAP/AMP-AD).
- Biomarker / translational implication: E/I balance and chaperone reorganization as resilience axes.
- Grant / manuscript implication: Citable resilience framework complementing vulnerability literature.

# Contradictions and links
- Supports: RORB+ EC vulnerability (Leng 2021) as the complementary "vulnerable" pole; microglial bias of AD risk variants.
- Contradicts: (none directly; offers resilience counterpoint to vulnerability emphasis)
- Replicates: Cited Leng 2021 EC vulnerability finding.
- Methodologically comparable papers: Mathys et al. (ROSMAP snRNA, co-author); Leng 2021; Ruf 2026 (cell-type TDP-43, different disease).
- Relevant synthesis notes: candidate seed for "vulnerability vs resilience cell-type signatures."
- Relevant project decisions: (none yet)

# Follow-up actions
- [ ] Extract exact multiregion snRNA-seq synID + per-group cell/subject counts from supplement
- [ ] Locate code repository
- [ ] Consider a dataset record for ROSMAP/AMP-AD (syn2580853) if used for validation
- [ ] Cross-link with Leng 2021 and Ruf 2026 in a vulnerability/resilience synthesis
- [ ] Check retraction/correction status

# Priority decision
- Priority: 2
- Retain for methods + external validation
- Rationale: Strong, well-validated multi-omic resilience study on a public, reusable cohort; decision-relevant as both a biological contrast to vulnerability work and a reproducible public-data reuse template. Priority 2 (supporting/validation) rather than 1 because effect sizes are modest and the design is observational.
