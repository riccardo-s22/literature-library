---
record_type: paper
record_status: partial
canonical_id: "10.1016/j.cell.2026.06.013"
doi: "10.1016/j.cell.2026.06.013"
pmid: "42385702"
title: "Recurrent patterns of TOP1-mediated neuronal genomic damage shared by major neurodegenerative disorders"
year: 2026
source_type: primary
peer_reviewed: true
full_text_checked: true
supplement_checked: false
code_checked: false
data_checked: false
last_verified: 2026-09-01
priority: 1
projects: []
topics: [neurodegeneration, ALS, AD_ADRD, single_cell, transcriptomics]
methods: [snRNAseq, FANS]
datasets: []
---

# Citation
- Full citation: Zhou et al. (2026). Recurrent patterns of TOP1-mediated neuronal genomic damage shared by major neurodegenerative disorders. *Cell*. https://doi.org/10.1016/j.cell.2026.06.013
- DOI / PMID / stable URL: 10.1016/j.cell.2026.06.013 / PMID 42385702 / PMCID PMC13340254
- Related preprint or published version: Unknown
- Correction, expression of concern, or retraction status: None as of 2026-09-01

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Establishes TOP1-mediated somatic mutagenesis as a shared genomic mechanism across ALS, FTD, and AD neurons, independent of specific proteinopathy (TDP-43 vs. tau). Directly relevant to interpretations of somatic mutation burden in neurodegenerative disease and to TDP-43 pathology studies in ALS/FTD.
- Why it is more or less useful than neighboring literature: First study performing single-cell WGS across multiple neurodegenerative diseases in matched neurons with/without TDP-43 pathology using FANS sorting. Provides a cell-type-resolved mechanistic link between TOP1 mutagenesis and cortical-selective neuronal vulnerability that is not available from bulk genomics.

# Source inspection status
- Abstract inspected: Yes
- Full text inspected: Yes (Methods, Results sections read; full 68 kb PMC text accessed)
- Methods inspected: Yes
- Supplement inspected: No
- Figures/tables inspected: No
- Code repository inspected: No (SCAN2 software is publicly available per prior publications)
- Data repository inspected: No
- Missing material: Supplementary tables (sample metadata, QC data, sSNV/sIndel catalogs); data repository accessions not confirmed from text

# Study question and hypothesis
- Primary question: Do neurons from ALS, FTD, and AD share recurrent patterns of somatic mutation, and what mutagenic mechanism underlies these patterns?
- Stated hypothesis: TDP-43 pathology or tau pathology drives somatic mutagenesis in neurons; different disease categories might show distinct mutational signatures.
- Study type: Cross-disease comparative cohort study using single-cell whole-genome sequencing (scWGS) of postmortem human neurons

# Biological or clinical context
- Disease / exposure / process: ALS (TDP-43 proteinopathy), FTD (TDP-43 proteinopathy), Alzheimer's disease (tau + amyloid proteinopathy)
- Organism: Human (postmortem)
- Tissue / cell type: Motor/premotor cortex neurons (ALS), prefrontal cortex neurons (FTD, AD, controls); cerebellar neurons (ALS, FTD — internal controls)
- Model system: Human postmortem brain tissue; FANS-sorted neuronal nuclei; iPSC-derived NGN2 neurons (TDP-43 knockdown validation)
- Cohort or population: 6 C9orf72-ALS brains, 6 C9orf72-FTD brains, 29 AD brains, neurotypical controls (24 newly sequenced + 56 previously published prefrontal cortex neurons); exact ages unknown from text
- Relevant stage, age, sex, genotype, or disease severity: All ALS/FTD cases have C9orf72 repeat expansion; AD cases unspecified; controls span various ages

# Study design
- Experimental or observational unit: Single neuronal nucleus (sorted by FANS, amplified by PTA)
- Unit of inference: Somatic mutation burden per neuron; group comparisons across disease and cell type
- Groups and sample size per group: ALS: 6 brains × 3 TDP-43+ + 3 TDP-43− neurons = ~36 neurons (minimum); FTD: same; AD: 29 neurons; controls: 80+ neurons; exact per-group passing-QC counts in Supplementary Table S2
- Biological replicates: 6 ALS brains, 6 FTD brains; 29 AD brains; 80+ control neurons across ages
- Technical replicates: PTA amplification from single nuclei; multiplex PCR QC and Picogreen quantification
- Randomization: Not reported
- Blinding: Not reported
- Inclusion / exclusion criteria: QC criteria include amplification uniformity; cells failing QC excluded (see Supplementary Tables S2, S3)
- Batch structure: Not reported explicitly; Boston Children's Hospital IRB approved
- Longitudinal, repeated-measures, paired, or donor structure: Cross-sectional postmortem; TDP-43+ and TDP-43− neurons are paired within the same brain
- Controls and comparators: Age-matched neurotypical controls; cerebellar neurons from same diseased brains; TDP-43+ neurons from same ALS/FTD brains as matched controls

# Experimental methods
- Assay / platform: FANS (NeuN + TDP-43 co-staining) → PTA single-cell whole-genome amplification (BioSkryb ResolveDNA Kit v1) → Illumina NovaSeq (150 bp × 2); snRNA-seq validation of nuclear purity; iPSC NGN2 neurons with CRISPRi TDP-43 knockdown
- Sample preparation: Dounce homogenization in chilled lysis buffer; sucrose cushion ultracentrifugation (30,000 × g, 1 h); filtration (40 μm); Alexa Fluor 488-anti-NeuN + Alexa Fluor 647-anti-TDP-43 co-staining; DAPI; FANS into 96-well plates
- Dose, concentration, force, exposure, or perturbation: Not applicable (observational)
- Timing and sampling schedule: Postmortem; timing relative to death not stated
- Matrix / medium / substrate / environmental conditions: Fresh frozen postmortem brain tissue (Massachusetts ADRC + NIH NeuroBioBank)
- Primary endpoint: Somatic SNV and indel burden per neuron; mutational signature attribution
- Secondary endpoints: Cryptic exon detection in snRNA-seq (TDP-43 loss-of-function confirmation); RNaseH2 and RRM gene expression by qPCR
- QC criteria: Picogreen yield, 4-locus multiplex PCR, SCAN2 genotyping QC; cells failing excluded
- Failure or exclusion criteria: Amplification unevenness, insufficient DNA yield
- Exact reusable parameters and source location: 150 bp × 2 sequencing; 30× depth for cortical neurons, 22× for cerebellar; FANS antibodies: Millipore MAB377X (NeuN) + Abnova H00023435-M01 (TDP-43); PTA kit: BioSkryb 100136; qPCR: Power SYBR Green Cells-to-CT Kit (Thermo Fisher 4402954); CRISPRi: Tetracycline-inducible NGN2 + dCAS9-ZIM3-KRAB-BFP in KOLF2.1J and FA11 iPSC lines

# Computational and statistical methods
- Raw input: Illumina FASTQ reads
- Preprocessing: bwa mem v0.7.15-r1140 (-M flag) aligned to GRCh37d5
- Normalization: Not applicable (somatic mutation counting)
- Feature filtering: SCAN2 single-cell genotyper; ~35% sSNV recovery, ~24% sIndel recovery; estimated aggregate error rate <10%
- Covariates and design formula: Age as covariate for mutation burden modeling; disease vs. control comparison
- Statistical test or model: Linear age-mutation model; observed/expected burden ratios per cell; FDR-corrected differential gene expression for snRNA-seq (FDR < 0.05)
- Multiple-testing correction: FDR for snRNA-seq
- Effect-size reporting: Reported (>67,000 sSNVs + >12,000 sIndels catalogued; some neurons >1000 sIndels equivalent to hundreds of years of age-related accumulation)
- Batch handling: Not explicitly reported
- Validation strategy: Internal: paired TDP-43+ vs. TDP-43− neurons; cerebellar internal control; snRNA-seq cryptic exon validation. External: iPSC-derived NGN2 neurons with CRISPRi TDP-43 knockdown
- External validation: iPSC CRISPRi TDP-43 knockdown + immunofluorescence
- Software and versions: bwa mem v0.7.15-r1140; SCAN2 (version unspecified in text); Seurat (clustering/UMAP, Leiden algorithm resolution=0.8); SCAN2 v2 inferred from "SCAN2" citation
- Code availability: SCAN2 previously published; specific code for this study Unknown

# Data and resource availability
- Repository and accession: Not confirmed from text; Supplementary Tables S1–S5 contain case metadata, QC, single-cell metadata, sSNV/sIndel catalogs
- Raw data available: Unknown (likely dbGaP for human genomic data, not confirmed)
- Processed data available: Unknown
- Metadata completeness: Supplementary tables available; exact accessions not confirmed
- Data-use restrictions: Human postmortem genomics — likely controlled access
- Reusability for the user's work: The FANS+PTA scWGS protocol and SCAN2 analysis pipeline are directly reusable for single-neuron genomics in postmortem tissue

# Main findings
| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| ALS, FTD, and AD neurons show elevated somatic mutation burdens vs. controls | Reported | Results | Neurons with >1000 sIndels (hundreds of years of age-equivalent accumulation) observed | Yes | All ALS/FTD cases are C9orf72; AD cases uncharacterized genetically |
| Shared 2-bp deletion mutational pattern across ALS, FTD, and AD | Reported | Results | Two-bp deletions characterize sIndel burden in all three disease categories | Yes | Pattern specific to motor/premotor/prefrontal cortex; absent in cerebellum |
| TOP1-mediated mutagenesis underlies the 2-bp deletion signature | Reported | Results / computational and experimental | Computational signature matching + CRISPRi TDP-43 knockdown in iPSC neurons | Partial | Mechanistic link is inferential/partially experimental; in vitro validation in NGN2 neurons not in postmortem tissue |
| Cerebellar neurons spared from elevated somatic mutations in the same diseased brains | Reported | Results | Cerebellar neurons from same ALS/FTD brains show no excess mutation | Yes | Only ALS/FTD tested in cerebellum, not AD |
| TDP-43+ and TDP-43− neurons (within same ALS/FTD brains) both show elevated sSNV/sIndel burden | Reported | Results | Both sorted populations show excess mutations | Yes | Suggests TOP1 mutagenesis is not strictly dependent on nuclear TDP-43 depletion |

# What is actually new?
- Biological novelty: First demonstration of a recurrent, TOP1-dependent 2-bp deletion signature shared by TDP-43 proteinopathies and tau/amyloid proteinopathies at single-neuron resolution; cortical selectivity of the mutational excess
- Methodological novelty: FANS co-staining for NeuN + TDP-43 followed by PTA-based scWGS — enables mutation profiling specifically in TDP-43-pathological neurons
- Dataset or resource novelty: Single-neuron WGS catalog spanning ALS, FTD, AD, and controls with paired TDP-43+ and TDP-43− neurons per brain
- What was already known: Elevated DNA damage in neurodegenerative disease; age-related somatic mutation accumulation in neurons; C9orf72 repeat expansion causes chromosomal fragility

# Strengths
- Design strength: Paired TDP-43+ and TDP-43− neurons within same brains; cerebellar internal control; multiple disease categories in single study
- Validation strength: snRNA-seq cryptic exon detection confirms TDP-43 loss of function; CRISPRi iPSC validation of TOP1 mechanism
- Reproducibility strength: SCAN2 previously published and validated; detailed FANS protocol reported; reagent catalog numbers given
- Translational or ecological realism: Human postmortem tissue; disease-relevant genotypes; cortical regions most affected in ALS/FTD

# Limitations and bias risks
- Sample-size or power limitation: 6 ALS + 6 FTD brains; all C9orf72 — cannot disentangle C9orf72-specific vs. sporadic ALS/FTD effects
- Confounding: C9orf72 repeat expansion itself may independently drive genomic instability
- Batch or site effects: Tissues from two sources (Massachusetts ADRC, NIH NeuroBioBank); batch handling not reported
- Pseudoreplication risk: Low — single-neuron unit of measurement
- Leakage or overfitting risk: Not applicable (mutation counting, not ML classification)
- Generalizability limitation: All ALS/FTD cases are C9orf72; does not address TARDBP, FUS, or sporadic ALS; AD genotypes not specified
- Missing controls: Non-TDP-43 ALS (TARDBP or FUS mutation) not included; tau-only controls absent
- Missing validation: Independent cohort for mutation burden replication; in vivo TOP1 manipulation not done
- Author-stated limitations: C9orf72 exclusivity; absence of non-TDP-43 ALS forms; SCAN2 recovery rates (~35% sSNV, ~24% sIndel) are partial
- Additional limitations identified during review: Postmortem interval not reported; sex breakdown of cases not confirmed from text

# Transferability to the user's work
- Directly transferable elements: FANS protocol for TDP-43 pathological neuron sorting; PTA-based scWGS workflow; SCAN2 pipeline; snRNA-seq cryptic exon approach for TDP-43 loss-of-function confirmation
- Elements requiring adaptation: C9orf72-specific findings may not generalize to sporadic ALS or other genotypes
- Model, species, tissue, matrix, platform, or scale mismatch: Human postmortem — translatable to postmortem tissue studies; not applicable to cell-line or organoid systems without adaptation
- Assumptions required for transfer: TOP1 mutagenesis mechanism generalizes beyond C9orf72
- Confidence: moderate

# Practical implications
- Experimental implication: FANS + TDP-43 co-staining enables enrichment of pathological neurons for downstream genomics; applicable to TBI or other injury contexts with TDP-43 pathology
- Analysis implication: SCAN2 pipeline for single-cell somatic mutation calling in postmortem tissue is a validated reusable resource
- Public dataset implication: Single-neuron WGS catalog likely to be deposited; monitor for controlled-access release
- Biomarker or translational implication: Somatic mutation burden (especially sIndel pattern) may be a cell-autonomous contributor to neuronal vulnerability, independent of proteinopathy type
- Grant or manuscript implication: Supports inclusion of TOP1 pathway in mechanistic frameworks for ALS/FTD grant applications

# Contradictions and links
- Supports: ruf_2026_celltype-tdp43-motor-cortex.md (cell-type-resolved TDP-43 pathology in motor cortex)
- Contradicts: Nothing directly in the current library
- Replicates: Prior SCAN2 somatic mutation studies in AD neurons (cited in paper)
- Methodologically comparable papers: ruf_2026_celltype-tdp43-motor-cortex.md (FANS + snRNA-seq)
- Relevant synthesis notes: None yet
- Relevant project decisions: None yet

# Follow-up actions
- [ ] Confirm data deposit accession (likely dbGaP or similar controlled-access repository)
- [ ] Inspect supplement for full case metadata and QC tables
- [ ] Check SCAN2 version and code repository link
- [ ] Assess whether non-C9orf72 ALS replication data are available elsewhere
- [ ] Monitor for correction or follow-up validation in sporadic ALS

# Priority decision
- Priority: 1
- Read now
- Rationale: First single-neuron cross-disease somatic mutation study with direct TDP-43 pathology stratification; highly relevant to mechanistic interpretation of ALS/FTD molecular biology and to TDP-43 loss-of-function experimental frameworks
