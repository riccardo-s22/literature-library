---
record_type: paper
record_status: verified
canonical_id: "10.1126/sciadv.aef9530"
doi: "10.1126/sciadv.aef9530"
pmid: "42525763"
title: "Integrating structurally defined DNA-carbon nanotube sensors with machine learning for cancer detection"
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
  - biosensors
  - nanomaterials
methods:
  - spectroscopy
  - biomarker
  - analysis_method
  - external_validation
datasets: []
---

# Citation
- Full citation: Chen P, Zheng X, Li Y, Li J, Zhou X, Wen Y, Liu J, Wang P, Li X, Chen R, Lin Z. Integrating structurally defined DNA-carbon nanotube sensors with machine learning for cancer detection. *Science Advances*. 2026;12(31):eaef9530.
- DOI / PMID / stable URL: https://doi.org/10.1126/sciadv.aef9530 | PMID 42525763 | PMC13418527
- Related preprint or published version: None identified
- Correction, expression of concern, or retraction status: None identified as of 2026-08-01

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Demonstrates that single-chirality, structurally defined DNA-coated SWCNTs (DNA-scCNTs) form a superior sensor array for liquid biopsy compared to chirality-mixed or stochastically functionalized CNTs; directly relevant to SWCNT biosensor design and spectral phenotyping of biofluids.
- Why it is more or less useful than neighboring literature: Advances on Kim 2022 (quantum-defect SWCNTs for ovarian cancer) and Cho 2021 (CoPhMoRe for SARS-CoV-2) by using enantiomerically pure, chirality-separated DNA-scCNTs with well-defined optical footprints, reducing batch variability. Multi-cancer (liver, lung, ovarian) detection in a single array is methodologically novel.

# Source inspection status
- Abstract inspected: Yes
- Full text inspected: Yes (via PMC13418527)
- Methods inspected: Yes (materials, DNA-scCNT preparation, spectroscopy, ML pipeline sections read)
- Supplement inspected: No
- Figures/tables inspected: No (text only)
- Code repository inspected: No
- Data repository inspected: No
- Missing material: Supplement, code, and raw spectral data not inspected

# Study question and hypothesis
- Primary question: Can a structurally defined DNA-scCNT sensor array, combined with ensemble ML, classify multiple cancer types from serum with clinical-grade accuracy?
- Stated hypothesis: Structural precision in DNA-CNT sensors (single chirality + well-defined DNA wrapping) reduces batch variability and improves cross-cohort ML transferability compared to heterogeneous CNT mixtures
- Study type: Primary proof-of-concept; external validation with independent cohort

# Biological or clinical context
- Disease / exposure / process: Liver cancer (LC), lung cancer (LuC), ovarian cancer (OC); vs noncancer controls (NC)
- Organism: Human
- Tissue / cell type: Serum (liquid biopsy)
- Model system: human_cohort (clinical samples)
- Cohort or population: Cancer patients and noncancer controls from Sun Yat-Sen University Cancer Center (Guangzhou, China); total 253 serum samples
- Relevant stage, age, sex, genotype, or disease severity: Early-stage lung cancer included; stage distribution for other cancers not specified in abstract; sex and age not reported in abstract

# Study design
- Experimental or observational unit: Individual serum sample
- Unit of inference: Individual cancer vs noncancer classification
- Groups and sample size per group: 253 total serum samples; LC, LuC, OC groups and NC controls (exact per-group n not in abstract; details in Methods)
- Biological replicates: Clinical specimens — each patient is one sample
- Technical replicates: Not reported in inspected text
- Randomization: Not reported (patient cohort)
- Blinding: Not reported
- Inclusion / exclusion criteria: Not specified in inspected text
- Batch structure: Not reported; multi-cancer study implies different collection sites/batches possible
- Longitudinal, repeated-measures, paired, or donor structure: Cross-sectional (single time point per patient)
- Controls and comparators: Noncancer controls; 17 established tumor biomarkers analyzed for correlation

# Experimental methods
- Assay / platform: Photoluminescence (PL) spectroscopy in NIR; six-channel DNA-scCNT sensor array; UV-vis-NIR absorption spectroscopy; atomic force microscopy (AFM) for structural characterization; circular dichroism (CD) spectroscopy
- Sample preparation: SG65i CoMoCAT SWCNT powder (Sigma-Aldrich); DNA oligomers from Sangon Biotech; chirality separation by aqueous two-phase (ATP) extraction (PEG + salt systems); redispersed in 10 mM PBS. Serum samples incubated with DNA-scCNT sensors; PL measured with NS Super NanoSpectralyzer (Applied NanoFluorescence) using 730 nm laser excitation
- Dose, concentration, force, exposure, or perturbation: Six sensor channels: (GGC)(GC)-(−)(6,4), TTA(TAT)ATT-(−)(6,5), C(GCCCC)-(+)(7,3), CGCGC-(−)(7,5), TCTC-(−)(8,3), C(CCG)-(+)(9,1); each chirality identified by DNA resolving sequence
- Timing and sampling schedule: Cross-sectional; incubation time for serum + sensor not specified in inspected text
- Matrix / medium / substrate / environmental conditions: Undiluted or diluted human serum (details in supplement not inspected)
- Primary endpoint: Multi-cancer classification accuracy (sensitivity, specificity) in external validation cohort
- Secondary endpoints: Early-stage lung cancer detection; cost per test; correlation of sensor response with established tumor biomarkers (Spearman)
- QC criteria: ATP extraction purity verified by UV-vis-NIR and PL; AFM for structural confirmation
- Failure or exclusion criteria: Not reported in inspected text
- Exact reusable parameters and source location: ATP extraction protocol (PEG/salt compositions) in Methods section; chirality-specific DNA sequences listed in Methods; PL instrument model in Methods

# Computational and statistical methods
- Raw input: Multichannel PL fingerprints from six DNA-scCNT sensors across serum samples; features include peak wavelength (λ) and integrated intensity (dint) for each chirality channel
- Preprocessing: Feature extraction from PL spectra (peak position and integral); details in supplement not inspected
- Normalization: Not specified in inspected text
- Feature filtering: Six-channel × multiple spectral features; SHAP (SHapley Additive exPlanations) for feature importance
- Covariates and design formula: Not specified; disease group as outcome
- Statistical test or model: Ensemble machine learning (specific algorithm not named in abstract; random forest or gradient boosting implied); Mantel test for correlation of fingerprints with biomarker levels
- Multiple-testing correction: Not specified
- Effect-size reporting: Sensitivity and specificity per cancer type; mean values: 89% sensitivity, 96% specificity; early-stage LuC: 92% sensitivity, 95% specificity
- Batch handling: Not reported; cross-site batch effects not discussed in inspected text
- Validation strategy: External validation cohort (exact split/holdout details in supplement not inspected); "external validation cohort" stated in text
- External validation: Yes — stated as external validation; cohort source not separately specified from Sun Yat-Sen Cancer Center
- Software and versions: Not specified in inspected text
- Code availability: Not reported; not confirmed available

# Data and resource availability
- Repository and accession: Not reported in inspected text
- Raw data available: Unknown
- Processed data available: Unknown
- Metadata completeness: Unknown
- Data-use restrictions: Clinical samples from single institution (Sun Yat-Sen Cancer Center); patient data confidentiality
- Reusability for the user's work: DNA-scCNT preparation protocol is reusable; ML pipeline architecture (ensemble + SHAP) is transferable; serum dataset likely not publicly deposited

# Main findings
Use one row per consequential claim.

| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| DNA-scCNT sensor array + ensemble ML classifies liver, lung, and ovarian cancer from noncancer serum | Reported | Results | Mean sensitivity 89%, specificity 96% in external validation (n=253 total) | Yes | External validation cohort composition and exact per-group n not confirmed without supplement |
| Early-stage lung cancer detected with 92% sensitivity and 95% specificity at ~$4/test | Reported | Results / cost analysis | 92% sensitivity, 95% specificity; estimated ~$4 USD per test | Yes | Early-stage definition and staging criteria not confirmed in inspected text |
| Context-dependent serum microenvironment shapes sensor-marker interactions beyond individual biomarkers | Reported | Discussion | Spearman correlations between 17 tumor markers and sensor features; AFP shows no LC correlation but distinct OC correlation | Yes | Correlation ≠ causation; biological mechanism of sensor interaction unresolved |
| Structural definition of DNA-scCNTs (single chirality + ordered wrapping) is critical for cross-batch reproducibility | Inference | Introduction / rationale | Not directly tested vs stochastic CNTs in same study; inferred from structural characterization | Partial | Direct head-to-head comparison with chirality-mixed CNTs not shown |

# What is actually new?
- Biological novelty: Multi-cancer serum fingerprinting from a single sensor array; context-dependent tumor marker–sensor interactions as a detection mechanism
- Methodological novelty: First use of enantiomerically pure, single-chirality (scCNT) arrays — six distinct DNA-chirality combinations — for liquid biopsy; structural determinism reduces batch-to-batch variability vs prior CoPhMoRe or heterogeneous CNT approaches
- Dataset or resource novelty: 253-sample multi-cancer serum cohort with 17 tumor biomarker correlation dataset
- What was already known: DNA-wrapped CNTs for cancer detection (Kim 2022, Cho 2021); chirality separation of SWCNTs by ATP extraction; ensemble ML for optical fingerprint classification

# Strengths
- Design strength: Multi-cancer classification from a single array; external validation cohort; correlation with established biomarkers provides mechanistic grounding
- Validation strength: External validation reported; 17 tumor biomarker correlation validates biological plausibility
- Reproducibility strength: Chirality-separated DNA-scCNTs provide batch-to-batch structural uniformity (by design); ATP extraction protocol is reproducible
- Translational or ecological realism: Serum matrix (clinically accessible); cost estimate (~$4/test); multi-cancer detection from one platform

# Limitations and bias risks
- Sample-size or power limitation: 253 total samples across 4 groups; per-group n and cancer stage distribution not fully reported in abstract
- Confounding: Single institution (Sun Yat-Sen Cancer Center, China); ethnic and demographic homogeneity likely; no independent external geographic cohort confirmed
- Batch or site effects: Not discussed; all samples from one center
- Pseudoreplication risk: Not applicable (independent patient samples)
- Leakage or overfitting risk: External validation stated but split details not confirmed; "external" may mean held-out from same institution rather than geographically independent
- Generalizability limitation: Single-institution cohort; validation outside China not shown; breast cancer, prostate cancer, and colorectal cancer not included
- Missing controls: Benign nodule controls not mentioned; healthy age-matched vs patient-matched controls not specified
- Missing validation: Cross-institution batch validation; long-term sensor stability in biobank serum; interference from drugs, diet, comorbidities
- Author-stated limitations: Not specified in inspected text (supplement not inspected)
- Additional limitations identified during review: Code and raw spectral data not confirmed as available; head-to-head comparison with heterogeneous CNT arrays not included in same study

# Transferability to the user's work
- Directly transferable elements: ATP extraction protocol for chirality-separated DNA-scCNTs; PL spectroscopy setup (NS NanoSpectralyzer); SHAP analysis for sensor feature importance; ensemble ML classification framework
- Elements requiring adaptation: Multi-cancer panel vs single disease target; human serum vs other biofluids; cancer-specific vs neurological biomarkers
- Model, species, tissue, matrix, platform, or scale mismatch: Serum-based cancer detection; not directly applicable to neurodegeneration biomarker detection without redesigning corona chemistry and ML target
- Assumptions required for transfer: DNA-scCNT sensors respond to protein/metabolite changes in other biofluids; ML model generalizes to geographically and demographically distinct cohorts
- Confidence: high (for reported SWCNT preparation and PL measurement parameters); moderate (for generalizability of ML performance)

# Practical implications
- Experimental implication: Adopt ATP-separated single-chirality SWCNT approach for next-generation sensor arrays; use SHAP analysis for sensor channel importance attribution in biomarker studies
- Analysis implication: Ensemble ML with SHAP provides interpretable feature importance for high-dimensional spectral fingerprint data; Mantel test as a tool to validate biological relevance of sensor responses
- Public dataset implication: 253-sample serum dataset not publicly deposited (as of this record); monitor for future data release
- Biomarker or translational implication: Demonstrates path to affordable multi-cancer liquid biopsy; ~$4/test cost if chirality separation scaled up; cancer-specific validation needed before neurodegeneration application
- Grant or manuscript implication: Strong precedent for structurally defined sensor arrays + ML for liquid biopsy; cite for technical framework, not disease-specific claims

# Contradictions and links
- Supports: Kim 2022 (SWCNT ovarian cancer serum ML; [02_PAPERS/2022/kim_2022_swcnt-ovarian-cancer-serum-ml.md]); Cho 2021 (CoPhMoRe SARS-CoV-2 saliva; [02_PAPERS/2021/cho_2021_cophmore-swcnt-sars-cov-2-saliva.md])
- Contradicts: None directly; suggests structural heterogeneity of prior CNT sensors is a limitation (implied critique of Kim 2022 and Tian 2025 approaches)
- Replicates: Extends Kim 2022 ovarian cancer detection with a structurally superior sensor design
- Methodologically comparable papers: Kim 2022; Tian 2025 (SWCNT NIR ML virus ID; [02_PAPERS/2025/tian_2025_swcnt-nir-ml-virus-spectral-decoding.md]); Lee 2025 (SWCNT skin patch; [02_PAPERS/2025/lee_2025_swcnt-patch-sensor-biofluid-tracing.md])
- Relevant synthesis notes: None yet
- Relevant project decisions: None yet

# Follow-up actions
- [ ] Inspect supplement for exact per-group sample sizes, validation cohort composition, and ML hyperparameters
- [ ] Search for companion data/code repository (likely SCAU GitHub or Zenodo)
- [ ] Compare ATP extraction protocol parameters to existing Benbasat 2021 QC methods in library
- [ ] Add to synthesis on SWCNT biosensors when created

# Priority decision
- Priority: 1
- Read now
- Rationale: Highest-rigor SWCNT biosensor paper in the July 2026 window; introduces structurally defined DNA-scCNT arrays as a methodological advance over prior work; multi-cancer serum detection with external validation directly relevant to SWCNT biosensor domain
