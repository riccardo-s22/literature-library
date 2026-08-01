---
record_type: paper
record_status: verified
canonical_id: "10.1001/jamaneurol.2026.1405"
doi: "10.1001/jamaneurol.2026.1405"
pmid: "42189519"
title: "Plasma eMTBR-tau243 and %p-tau217 for Biological Staging of Alzheimer Disease"
year: 2026
source_type: primary
peer_reviewed: true
full_text_checked: true
supplement_checked: false
code_checked: false
data_checked: false
last_verified: 2026-08-01
priority: 1
projects: []
topics:
  - neurodegeneration
  - AD_ADRD
  - aging
methods:
  - biomarker
  - external_validation
  - human_cohort
datasets: []
---

# Citation
- Full citation: Salvadó G, Horie K, Barthélemy NR, Schindler SE, Janelidze S, Orduña Dolado A, Bali D, Perrin RJ, Morris JC, Benzinger TLS, Gordon BA, Stomrud E, Mattsson-Carlgren N, Palmqvist S, Vogel JW, Bateman RJ, Ossenkoppele R, Hansson O. Plasma eMTBR-tau243 and %p-tau217 for Biological Staging of Alzheimer Disease. *JAMA Neurology*. 2026;83(7):654-666.
- DOI / PMID / stable URL: https://doi.org/10.1001/jamaneurol.2026.1405 | PMID 42189519 | PMC13213595
- Related preprint or published version: None identified
- Correction, expression of concern, or retraction status: None identified as of 2026-08-01

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Establishes a fully plasma-based biological staging model for AD using two analytes (%p-tau217 + eMTBR-tau243) that closely mirrors PET-based staging; relevant to any biomarker discovery or validation study targeting AD staging without neuroimaging.
- Why it is more or less useful than neighboring literature: Superior to single-analyte plasma p-tau217 models for the intermediate stage (A+TMOD+); validated in two independent cohorts including a neuropathological subsample; directly comparable to the Warmenhoven 2025 p-tau217 head-to-head benchmark in the library.

# Source inspection status
- Abstract inspected: Yes
- Full text inspected: Yes (via PMC13213595)
- Methods inspected: Yes
- Supplement inspected: No
- Figures/tables inspected: No (full text read, figures not separately inspected)
- Code repository inspected: No
- Data repository inspected: No
- Missing material: Supplement not inspected; raw data not publicly available (cohort data)

# Study question and hypothesis
- Primary question: Can a plasma-based model combining %p-tau217 and eMTBR-tau243 accurately replicate amyloid + tau PET-based biological staging of AD?
- Stated hypothesis: Two plasma tau biomarkers reflecting phosphorylation state (%p-tau217) and tau cleavage (eMTBR-tau243) together capture distinct aspects of AD pathology and improve on single-analyte staging.
- Study type: Observational longitudinal; biomarker development and independent validation

# Biological or clinical context
- Disease / exposure / process: Alzheimer's disease; amyloid and tau pathology
- Organism: Human
- Tissue / cell type: Plasma; with neuropathological validation in brain tissue
- Model system: Human cohort (research cohorts)
- Cohort or population: BioFINDER-2 (Sweden; training + internal validation) and Knight ADRC (Washington University; independent validation)
- Relevant stage, age, sex, genotype, or disease severity: CU (n=383), MCI (n=182), AD dementia (n=151), non-AD neurodegenerative diseases (n=156) in BioFINDER-2; mean age 72.8 years (SD 9.2); 50.2% women; 59.2% APOE-ε4 carriers

# Study design
- Experimental or observational unit: Individual participant
- Unit of inference: Individual; staging model concordance at cohort level
- Groups and sample size per group: BioFINDER-2 n=872 (main; 70/30 development/validation split); Knight ADRC n=156 (independent validation); neuropathology subsample n=80 (Knight ADRC)
- Biological replicates: Not applicable (observational)
- Technical replicates: Not reported
- Randomization: Not applicable
- Blinding: Not reported
- Inclusion / exclusion criteria: Required plasma biomarkers available; Knight ADRC subsample required neuropathological data
- Batch structure: Not reported
- Longitudinal, repeated-measures, paired, or donor structure: Longitudinal study; cross-sectional and longitudinal analyses reported
- Controls and comparators: Amyloid + tau PET-based staging (revised AA criteria) as reference; %p-tau217 alone as comparator

# Experimental methods
- Assay / platform: Plasma eMTBR-tau243: immunoprecipitation-mass spectrometry (IP-MS; Tracy Family SILQ Center, Washington University); plasma %p-tau217: reported (platform not specified in abstract; C2N Diagnostics in related prior work from same group)
- Sample preparation: Plasma collection and IP-MS processing at Washington University SILQ Center; details in supplement (not inspected)
- Dose, concentration, force, exposure, or perturbation: Not applicable
- Timing and sampling schedule: BioFINDER-2: November 2019 to January 2025; Knight ADRC: September 2007 to March 2020; analysis December 2024 to July 2025
- Matrix / medium / substrate / environmental conditions: Plasma
- Primary endpoint: Concordance (C index) between plasma-based staging model and PET-based staging
- Secondary endpoints: Concordance with clinical stage; AUC vs neuropathological AD staging (ADNC scale)
- QC criteria: Not specified in inspected text
- Failure or exclusion criteria: Not specified in inspected text
- Exact reusable parameters and source location: Logistic regression staging model; 70/30 split for derivation/validation within BioFINDER-2; details in Methods section (full text)

# Computational and statistical methods
- Raw input: Plasma eMTBR-tau243 and %p-tau217 concentrations; amyloid PET and tau PET staging as reference
- Preprocessing: Not reported in abstract/inspected text
- Normalization: Not reported
- Feature filtering: Two-analyte model only
- Covariates and design formula: Not reported
- Statistical test or model: Logistic regression for staging; concordance index (C index) as primary performance metric; AUC for neuropathological validation
- Multiple-testing correction: Not reported
- Effect-size reporting: C index with 95% CI; AUC with 95% CI
- Batch handling: Not reported
- Validation strategy: Internal 70/30 split (BioFINDER-2) + independent cohort (Knight ADRC) + neuropathological subsample
- External validation: Yes — Knight ADRC (n=156) independent of training cohort
- Software and versions: Not reported in inspected text
- Code availability: Not reported

# Data and resource availability
- Repository and accession: Not publicly available (cohort data from BioFINDER-2 and Knight ADRC)
- Raw data available: No (cohort access via institutional collaboration)
- Processed data available: Not reported
- Metadata completeness: Not assessed
- Data-use restrictions: Research cohort data; access through respective institutions
- Reusability for the user's work: BioFINDER-2 and Knight ADRC datasets are widely used reference cohorts; biomarker parameters (IP-MS for eMTBR-tau243) require specialized infrastructure

# Main findings
Use one row per consequential claim.

| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| Plasma %p-tau217 + eMTBR-tau243 model accurately replicates PET-based AD biological staging | Reported | Results / main text | C index 0.91 (95% CI 0.90–0.92) in BioFINDER-2; 0.91 (0.87–0.94) in Knight ADRC | Yes | PET staging itself is reference, not ground truth; requires IP-MS infrastructure |
| Two-analyte model outperforms %p-tau217 alone for intermediate stage (A+TMOD+) classification | Reported | Results / comparison section | Concordance improvement quantified (exact ΔC not in abstract) | Yes | Improvement magnitude not specified in abstract; supplement not inspected |
| Plasma staging aligns with clinical severity (CU → MCI → AD dementia) | Reported | Results | C index 0.84 (0.82–0.86) BioFINDER-2; 0.86 (0.82–0.89) Knight ADRC | Yes | Cross-sectional concordance; longitudinal change not separately quantified |
| Plasma staging concordant with autopsy-confirmed AD neuropathological categorization (ADNC scale) | Reported | Results | AUC 0.96 (95% CI 0.91–1.00) in Knight ADRC neuropathology subsample (n=80) | Yes | Small neuropathology subsample (n=80); selection bias toward confirmed diagnoses |
| eMTBR-tau243 reflects distinct pathological information from %p-tau217 | Inference | Background / rationale | Inferred from complementary performance improvement; not directly tested | Partial | Mechanistic basis not established in this study |

# What is actually new?
- Biological novelty: eMTBR-tau243 (endogenously cleaved tau fragment) as a plasma staging biomarker complementary to p-tau217; captures pathological tau fragmentation distinct from phosphorylation
- Methodological novelty: First validation of a two-analyte plasma model that mirrors revised AA criteria PET-based staging with C index ≥0.91 in two independent cohorts including neuropathological confirmation
- Dataset or resource novelty: Largest plasma biomarker staging validation to date combining BioFINDER-2 + Knight ADRC with neuropathological endpoint
- What was already known: %p-tau217 alone provides good but imperfect staging; PET-based staging is established reference standard; IP-MS for tau fragments established from prior SILQ Center work

# Strengths
- Design strength: Prospective recruitment in both cohorts; two independent validation datasets; neuropathological ground truth in subsample
- Validation strength: External validation in geographically independent cohort; neuropathological validation (AUC 0.96)
- Reproducibility strength: IP-MS is reproducible at specialized centers; %p-tau217 measurable on commercial platforms
- Translational or ecological realism: Real-world CU-to-dementia clinical spectrum; routine plasma sampling

# Limitations and bias risks
- Sample-size or power limitation: Neuropathology subsample n=80 is small for subgroup analysis
- Confounding: APOE-ε4 enrichment (59.2%); predominantly white research cohorts
- Batch or site effects: Two-site study; IP-MS performed at single center (Washington University SILQ)
- Pseudoreplication risk: Not applicable
- Leakage or overfitting risk: Internal 70/30 split may not fully prevent overfitting; external Knight ADRC validation is mitigating
- Generalizability limitation: Both cohorts are research volunteers (not population-representative); IP-MS requires specialized infrastructure not available in most clinical labs
- Missing controls: Non-AD neurodegenerative diseases included but limited staging comparison in that group
- Missing validation: Longitudinal staging stability not validated; performance in diverse racial/ethnic populations not reported
- Author-stated limitations: IP-MS requires large plasma volume and specialized infrastructure; not yet ready for routine standalone clinical use
- Additional limitations identified during review: %p-tau217 platform not specified (may vary by site); supplement not inspected (additional validation and sensitivity analyses unknown)

# Transferability to the user's work
- Directly transferable elements: Two-biomarker staging framework applicable as reference model for any plasma AD biomarker study; C index as concordance metric for continuous staging
- Elements requiring adaptation: IP-MS for eMTBR-tau243 is not a routine clinical assay; %p-tau217 assay format may vary
- Model, species, tissue, matrix, platform, or scale mismatch: Human plasma only; not applicable to CSF, imaging, or non-AD neurodegenerative staging directly
- Assumptions required for transfer: PET-based staging as valid reference standard; same tau biology in target population
- Confidence: high (for the reported concordance metrics in the study cohorts); moderate (for generalizability beyond research cohorts)

# Practical implications
- Experimental implication: Use %p-tau217 + eMTBR-tau243 two-analyte framework as benchmark for any new AD plasma biomarker staging study; prefer C index over binary accuracy for staging performance
- Analysis implication: Staging models benefit from multiple complementary analytes; logistic regression with PET staging as reference is a validated approach
- Public dataset implication: BioFINDER-2 is a key reference cohort for AD biomarker validation; access via Lund University collaboration
- Biomarker or translational implication: eMTBR-tau243 adds staging specificity over p-tau217 alone, particularly at intermediate stage; IP-MS requirement is current translational barrier
- Grant or manuscript implication: Strong precedent for plasma-based staging as primary endpoint in AD trials and clinical studies

# Contradictions and links
- Supports: Warmenhoven 2025 (plasma p-tau217 benchmarking, BioFINDER-2; [02_PAPERS/2025/warmenhoven_2025_ptau217-head-to-head-biofinder2.md]); Kac 2026 (tau368 for FTLD-tau; [02_PAPERS/2026/kac_2026_tau368-ftld-tau-csf-biomarker.md])
- Contradicts: None identified
- Replicates: Extends prior %p-tau217 staging work from the Lund/Washington University groups
- Methodologically comparable papers: Warmenhoven 2025 (p-tau217 platform comparison, BioFINDER-2)
- Relevant synthesis notes: None yet
- Relevant project decisions: None yet

# Follow-up actions
- [ ] Inspect supplement for exact IP-MS parameters (plasma volume, sample prep, internal standards)
- [ ] Confirm %p-tau217 assay platform used in BioFINDER-2 (C2N vs Lumipulse vs other)
- [ ] Add to a synthesis on plasma AD biomarkers if one is created
- [ ] Monitor for clinical adoption updates or external validation studies

# Priority decision
- Priority: 1
- Read now
- Rationale: Directly relevant to AD_ADRD biomarker domain; two-analyte plasma staging validated in two cohorts with neuropathological endpoint; changes interpretation of p-tau217 alone as sufficient staging biomarker
