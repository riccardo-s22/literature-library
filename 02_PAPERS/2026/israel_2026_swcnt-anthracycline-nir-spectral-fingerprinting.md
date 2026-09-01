---
record_type: paper
record_status: partial
canonical_id: "10.1021/acs.nanolett.6c01777"
doi: "10.1021/acs.nanolett.6c01777"
pmid: "42409644"
title: "Optical Spectral Fingerprinting Enables Sensitive Detection of Anthracycline Chemotherapeutics in Synthetic Clinical Biofluids"
year: 2026
source_type: primary
peer_reviewed: true
full_text_checked: true
supplement_checked: false
code_checked: false
data_checked: false
last_verified: 2026-09-01
priority: 2
projects: []
topics: [biosensors, nanomaterials]
methods: [spectroscopy, biomarker, analysis_method]
datasets: []
---

# Citation
- Full citation: Israel et al. (2026). Optical Spectral Fingerprinting Enables Sensitive Detection of Anthracycline Chemotherapeutics in Synthetic Clinical Biofluids. *Nano Letters*. https://doi.org/10.1021/acs.nanolett.6c01777
- DOI / PMID / stable URL: 10.1021/acs.nanolett.6c01777 / PMID 42409644 / PMCID PMC13397890
- Related preprint or published version: Unknown
- Correction, expression of concern, or retraction status: None as of 2026-09-01

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Demonstrates a complete ssDNA-SWCNT spectral fingerprinting workflow — from sensor array design through ML classification and biofluid validation — for small molecule discrimination. The SHAP-based feature attribution links specific ssDNA–chirality combinations to detection of each anthracycline, providing design guidance for new analyte targeting.
- Why it is more or less useful than neighboring literature: Unlike prior SWCNT anthracycline sensors that give a generic response, this uses an 84-element array + XGBoost with 100% multiclass classification accuracy. Validation in synthetic sweat and urine (not buffer only) and SHAP interpretation set this above many sensor papers in the library.

# Source inspection status
- Abstract inspected: Yes
- Full text inspected: Yes (full 33 kb PMC text accessed via PMC13397890)
- Methods inspected: Yes (see "Brief Methods" section and main text)
- Supplement inspected: No (detailed methods stated to be in supplement)
- Figures/tables inspected: No (PMC text only, no figures retrieved)
- Code repository inspected: No
- Data repository inspected: No
- Missing material: Supplementary detailed methods; raw spectral data repository; exact ssDNA sequences and dispersion protocols in supplement

# Study question and hypothesis
- Primary question: Can a ssDNA-SWCNT nanosensor array combined with machine learning discriminate between structurally similar anthracycline chemotherapeutics in synthetic clinical biofluids?
- Stated hypothesis: Distinct ssDNA–SWCNT combinations exhibit anthracycline-specific NIR spectral modulations enabling ML-based identification and concentration quantification
- Study type: Analytical/instrumental method development with ML classification; in vitro biofluid validation

# Biological or clinical context
- Disease / exposure / process: Anthracycline chemotherapy monitoring; cardiotoxicity risk from doxorubicin, daunorubicin, epirubicin, idarubicin
- Organism: Not applicable (in vitro)
- Tissue / cell type: Not applicable
- Model system: Synthetic urine, synthetic sweat (biofluid matrices); buffer controls
- Cohort or population: Not applicable
- Relevant stage, age, sex, genotype, or disease severity: Not applicable

# Study design
- Experimental or observational unit: Individual ssDNA–(n,m)SWCNT sensing element per anthracycline concentration
- Unit of inference: Anthracycline class and concentration classification accuracy
- Groups and sample size per group: 12 ssDNA sequences × 7 (n,m) SWCNT chiralities = 84 sensing elements; 4 anthracyclines × 7 concentrations (0.1, 0.5, 1, 5, 10, 50, 100 μM); training on 0.1, 1, 10, 100 μM; test on 0.5, 5, 50 μM
- Biological replicates: Not applicable
- Technical replicates: Not stated explicitly
- Randomization: Not reported
- Blinding: Not reported
- Inclusion / exclusion criteria: 48-feature subset selected by ANOVA significance; 36 excluded
- Batch structure: Not reported
- Longitudinal, repeated-measures, paired, or donor structure: Not applicable
- Controls and comparators: Buffer baseline; 100 μM drug concentration as upper range

# Experimental methods
- Assay / platform: NIR fluorescence spectroscopy of ssDNA-SWCNT arrays; spectral features: intensity and wavelength changes per chirality peak
- Sample preparation: HiPco SWCNT dispersed with 12 ssDNA sequences separately; bulk chirality SWCNT allowing analysis of 7 (n,m) species simultaneously; anthracyclines added to sensor array
- Dose, concentration, force, exposure, or perturbation: 4 anthracyclines (doxorubicin, daunorubicin, epirubicin, idarubicin) at 7 concentrations: 0.1, 0.5, 1, 5, 10, 50, 100 μM
- Timing and sampling schedule: Not reported (single endpoint per concentration)
- Matrix / medium / substrate / environmental conditions: Buffer; synthetic sweat; synthetic urine; plasma and whole blood noted as future work
- Primary endpoint: Multiclass classification accuracy (anthracycline identity); concentration quantification accuracy
- Secondary endpoints: Anthracycline-specific limits of detection (LOD) from binding kinetic fits; SHAP feature importance
- QC criteria: ANOVA significance for feature selection (48 of 84 elements); PCA as unsupervised benchmark
- Failure or exclusion criteria: Features not meeting ANOVA significance excluded
- Exact reusable parameters and source location: 12 ssDNA sequences (selected from prior SWCNT sorting/sensing literature); 7 SWCNT chiralities: (7,5), (7,6), (9,4), (8,7), (8,6), (9,5)+(10,3), (10,2); XGBoost with 3-fold cross-validation; training set at 0.1/1/10/100 μM; test at 0.5/5/50 μM

# Computational and statistical methods
- Raw input: NIR fluorescence spectra (intensity and wavelength) per ssDNA-(n,m) combination per anthracycline concentration
- Preprocessing: Intensity and wavelength change from baseline extracted
- Normalization: Not stated
- Feature filtering: ANOVA-based selection → 48 significant features from 84 elements
- Covariates and design formula: Anthracycline class (4-class) and concentration (7-level); binary classification in biofluid validation
- Statistical test or model: Decision tree (DT), SVM, XGBoost; 3-fold cross-validation; XGBoost SHAP for feature attribution; traditional binding kinetics (non-linear fits) for LOD
- Multiple-testing correction: Not reported for ANOVA feature selection
- Effect-size reporting: Classification accuracy: DT 94±12%, SVM 98±4%, XGBoost 100% (cross-validation); test set: DT 100%, SVM 50%, XGBoost 100%; biofluid binary classification: daunorubicin 100%, idarubicin 100%, doxorubicin/epirubicin poor
- Batch handling: Not reported
- Validation strategy: Hold-out test set at intermediate concentrations (0.5/5/50 μM not used in training); biofluid validation in synthetic sweat + urine
- External validation: Synthetic biofluids only; plasma/whole blood not yet tested
- Software and versions: XGBoost (version Unknown); SHAP (version Unknown); PCA (library Unknown)
- Code availability: Unknown; stated to be for future framework development

# Data and resource availability
- Repository and accession: Unknown; no accession stated
- Raw data available: Unknown
- Processed data available: Unknown
- Metadata completeness: Spectral response data could be inferred from figures (not retrieved)
- Data-use restrictions: Unknown
- Reusability for the user's work: The 12 ssDNA + 7 SWCNT array design is reusable for small-molecule detection; XGBoost + SHAP workflow is directly transferable; synthetic biofluid matrices reported

# Main findings
| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| XGBoost achieves 100% multiclass classification of 4 anthracyclines in buffer | Reported | Results (classification section) | 100% cross-validation + test set accuracy | Yes | Training/test split uses only concentration-based hold-out; no sample-level donor variation |
| SHAP identifies anthracycline-specific ssDNA-(n,m) combinations | Reported | Results (SHAP analysis) | Top features differ by anthracycline (e.g., (TCG)TC-(9,5)+(10,3) for daunorubicin) | Yes | Mechanistic SHAP interpretation (π-π stacking, DNA intercalation) is Inference |
| Daunorubicin and idarubicin maintain 100% concentration classification in synthetic biofluids | Reported | Results (biofluid validation) | 100% binary concentration accuracy in sweat + urine | Yes | Doxorubicin and epirubicin show poor concentration discrimination in biofluids |
| Small-diameter SWCNT species (<0.9 nm) show higher anthracycline responsivity | Reported | ANOVA results | (7,5), (7,6), (9,4) have 32–39 significant features vs. fewer for >0.95 nm | Partial | (10,2) is exception; confounding from spectral congestion possible |
| PCA insufficient for anthracycline discrimination (PC1+PC2 = 77% variance, overlap remains) | Reported | PCA section | Substantial overlap in first two PCs | Yes | Confirms need for supervised ML |

# What is actually new?
- Biological novelty: Not applicable (method development)
- Methodological novelty: First 4-way anthracycline discrimination by SWCNT spectral fingerprinting with ML; SHAP attribution of per-analyte sensor contributions; biofluid (sweat + urine) validation
- Dataset or resource novelty: 84-element ssDNA-SWCNT spectral library for anthracyclines; SHAP-ranked sensor-analyte association table (Table 1)
- What was already known: SWCNT as generic anthracycline sensors (non-specific doxorubicin detection); ssDNA sequences used for SWCNT chirality sorting

# Strengths
- Design strength: 84-element sensor array with multiple ssDNA sequences + chiralities; hold-out test at intermediate concentrations not seen during training
- Validation strength: Two synthetic biofluid matrices (sweat + urine) with matrix effects evaluated
- Reproducibility strength: ssDNA sequences, SWCNT chiralities, and concentration range all specified; ANOVA + SHAP pipeline described
- Translational or ecological realism: Synthetic clinical biofluids used (sweat, urine); authors note plasma/whole blood as next step

# Limitations and bias risks
- Sample-size or power limitation: No patient samples; no biological variability modeled; single-batch sensor preparation assumed
- Confounding: Matrix composition of synthetic biofluids not fully characterized; co-administered drugs or metabolites not tested
- Batch or site effects: Single laboratory; no cross-batch sensor variability reported
- Pseudoreplication risk: Not applicable
- Leakage or overfitting risk: Low for classification (hold-out test at untrained concentrations); concentration regression models not fully described
- Generalizability limitation: Synthetic sweat/urine ≠ patient samples; poor doxorubicin/epirubicin concentration discrimination in biofluids
- Missing controls: Selectivity against anthracycline metabolites (e.g., doxorubicinol) not tested; protein-binding interference not characterized
- Missing validation: Real patient biofluid validation; plasma or whole blood matrix; orthogonal chemical validation of sensor-drug binding
- Author-stated limitations: Plasma/whole blood validation pending; coadministered metabolites not tested
- Additional limitations identified during review: No biological replicates; SVM test accuracy (50%) suggests instability; concentration discrimination poor for structurally most similar pair (dox/epirubicin)

# Transferability to the user's work
- Directly transferable elements: ssDNA-SWCNT array design framework; XGBoost + SHAP spectral fingerprinting workflow; biofluid matrix validation approach
- Elements requiring adaptation: ssDNA sequences and training data would need to be regenerated for new analyte classes; SWCNT dispersion QC protocol not detailed in main text (in supplement)
- Model, species, tissue, matrix, platform, or scale mismatch: In vitro only; synthetic biofluids; no real patient samples
- Assumptions required for transfer: SWCNT response is stable across batches; biofluid matrix effects are consistent across individuals
- Confidence: moderate

# Practical implications
- Experimental implication: 12-ssDNA × 7-chirality array provides a validated starting library for small-molecule spectral fingerprinting; ANOVA-based feature pre-selection reduces dimensionality before ML
- Analysis implication: XGBoost + SHAP pipeline directly applicable to other SWCNT spectral datasets; 3-fold CV with concentration hold-out is appropriate train/test paradigm for sensor arrays
- Public dataset implication: Spectral library may be released; monitor corresponding author for data deposit
- Biomarker or translational implication: Therapeutic drug monitoring in urine/sweat (non-invasive) is a validated use case for SWCNT spectral fingerprinting
- Grant or manuscript implication: Supports methodological framework for extending SWCNT sensors to other small-molecule targets; XGBoost + SHAP is a publishable analysis approach

# Contradictions and links
- Supports: kim_2022_swcnt-ovarian-cancer-serum-ml.md (SWCNT + ML for biomarker classification in biofluids); cho_2021_cophmore-swcnt-sars-cov-2-saliva.md (CoPhMoRe in clinical matrices)
- Contradicts: Nothing in current library
- Replicates: Prior SWCNT anthracycline detection (non-specific, not cited in library)
- Methodologically comparable papers: tian_2025_swcnt-nir-ml-virus-spectral-decoding.md (NIR + ML for SWCNT spectral decoding); lee_2025_swcnt-patch-sensor-biofluid-tracing.md
- Relevant synthesis notes: None yet
- Relevant project decisions: None yet

# Follow-up actions
- [ ] Retrieve supplementary detailed methods for SWCNT dispersion protocol and exact ssDNA sequences
- [ ] Confirm data deposit accession (raw spectra)
- [ ] Test in real patient urine/plasma per author future directions
- [ ] Check for follow-up publication with patient sample validation

# Priority decision
- Priority: 2
- Retain for methods
- Rationale: Provides a validated 84-element ssDNA-SWCNT array + XGBoost + SHAP workflow for small-molecule spectral fingerprinting in biofluids; directly relevant to the biosensor/spectral phenotyping domain
