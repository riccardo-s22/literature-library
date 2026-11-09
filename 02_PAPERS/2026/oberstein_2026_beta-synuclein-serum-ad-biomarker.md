---
record_type: paper
record_status: needs_full_text
canonical_id: "PMID:42904923"
doi: "10.1093/brain/awag361"
pmid: "42904923"
title: "Serum β-synuclein predicts dementia conversion and mortality beyond amyloid-β and phospho-tau"
year: 2026
source_type: primary
peer_reviewed: true
full_text_checked: false
supplement_checked: false
code_checked: false
data_checked: false
last_verified: 2026-11-01
priority: 1
projects: []
topics:
  - neurodegeneration
  - AD_ADRD
  - transcriptomics
methods:
  - proteomics
  - biomarker
datasets: []
---

# Citation
- Full citation: Oberstein TJ, Lindner E, Kittel J, Hahn J, Koeglsperger T, Danek A, et al. Serum β-synuclein predicts dementia conversion and mortality beyond amyloid-β and phospho-tau. Brain. 2026 Oct 21. doi:10.1093/brain/awag361.
- DOI / PMID: https://doi.org/10.1093/brain/awag361 / PMID 42904923
- Related preprint or published version: None identified
- Correction, expression of concern, or retraction status: None as of 2026-11-01

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Establishes β-synuclein (SNCB) as an independent serum biomarker for dementia conversion and mortality in AT-classified MCI/SCI patients; directly relevant to cross-disease neurodegeneration biomarker panel design and to distinguishing AD-specific from transdiagnostic signatures.
- Why it is more or less useful than neighboring literature: Novel: β-synuclein is not yet part of standard AD biomarker panels. Provides incremental prognostic value over pTau181 and Aβ42/40 in a well-characterised memory clinic cohort. More clinically translatable than mouse-only datasets; serum matrix is biofluid-accessible.

# Source inspection status
- Abstract inspected: Yes (PubMed abstract)
- Full text inspected: No (Brain journal paywalled; full text not accessible)
- Methods inspected: No (abstract-level only)
- Supplement inspected: No
- Figures/tables inspected: No
- Code repository inspected: No
- Data repository inspected: No
- Missing material: Full methods; figure data; supplement; cohort details beyond abstract; statistical model specification; raw data accession

# Study question and hypothesis
- Primary question: Does serum β-synuclein independently predict dementia conversion and mortality in AT-classified non-demented patients, beyond existing AD biomarkers?
- Stated hypothesis: β-synuclein elevation reflects synaptic/neuronal damage in AD and provides prognostic information additive to amyloid and tau biomarkers.
- Study type: Longitudinal observational cohort (memory clinic); biomarker validation study

# Biological or clinical context
- Disease / exposure / process: Alzheimer's disease (AD), mild cognitive impairment (MCI), subjective cognitive impairment (SCI)
- Organism: Homo sapiens
- Tissue / cell type: Serum; inferred to reflect CNS neuronal/synaptic damage
- Model system: Human memory clinic cohort; CSF AT-classified
- Cohort or population: 259 non-demented participants from single-centre memory clinic; stratified by CSF AT status: A-T- (n=97), A-T+ (n=65), A+T+ AD (n=97)
- Relevant stage, age, sex, genotype, or disease severity: Non-demented at baseline (MCI/SCI); median follow-up 4.1 years; AT classification by CSF

# Study design
- Experimental or observational unit: Individual patient
- Unit of inference: Patient-level outcome (dementia conversion, mortality)
- Groups and sample size per group: A-T- n=97; A-T+ n=65; A+T+ n=97; total n=259
- Biological replicates: Single-centre cohort (no independent external validation reported in abstract)
- Technical replicates: Unknown (full text not inspected)
- Randomization: Not applicable (observational)
- Blinding: Not reported in abstract
- Inclusion / exclusion criteria: Non-demented at baseline; memory clinic referral; CSF AT classification available; exact criteria unknown (full text not inspected)
- Batch structure: Unknown (single-centre, serum assay)
- Longitudinal, repeated-measures, paired, or donor structure: Longitudinal; baseline biomarker, follow-up for dementia conversion and mortality (median 4.1 years)
- Controls and comparators: A-T- group as biomarker-negative control; internal comparison across AT strata

# Experimental methods
- Assay / platform: Serum β-synuclein quantification (assay platform not specified in abstract; likely Simoa or ELISA)
- Sample preparation: Serum (baseline); unknown details (full text not inspected)
- Dose, concentration, force, exposure, or perturbation: Not applicable (observational)
- Timing and sampling schedule: Baseline serum collection; longitudinal follow-up median 4.1 years
- Matrix / medium / substrate / environmental conditions: Human serum
- Primary endpoint: Dementia conversion; all-cause mortality
- Secondary endpoints: Comparison of β-synuclein with CSF pTau181 and Aβ42/40 for prediction
- QC criteria: Unknown (full text not inspected)
- Failure or exclusion criteria: Unknown
- Exact reusable parameters and source location: Assay details unavailable (full text required)

# Computational and statistical methods
- Raw input: Serum β-synuclein concentrations; CSF Aβ42/40 and pTau181; clinical outcome data
- Preprocessing: Unknown (full text not inspected)
- Normalization: Unknown
- Feature filtering: Not applicable (targeted biomarker assay)
- Covariates and design formula: Unknown; age and AT status presumably included
- Statistical test or model: Hazard ratio model (reported: HR=1.40 per SD for dementia conversion); survival analysis
- Multiple-testing correction: Unknown
- Effect-size reporting: Cohen's d=0.69 (β-synuclein in AD vs A-T- group); HR=1.40 per SD increase for dementia conversion
- Batch handling: Unknown (single-centre)
- Validation strategy: AT stratification used to contextualize effect; pTau181/Aβ42/40 included as covariates
- External validation: Not reported in abstract; single-centre study
- Software and versions: Unknown
- Code availability: Not reported in abstract

# Data and resource availability
- Repository and accession: Not identified in abstract; likely subject to institutional data-sharing restrictions
- Raw data available: Unknown (full text not inspected)
- Processed data available: Unknown
- Metadata completeness: Unknown
- Data-use restrictions: Unknown
- Reusability for the user's work: Moderate — serum β-synuclein values and AT-stratified outcomes not directly reusable without raw data; conceptual value for biomarker panel design is high; cross-disease comparison possible if serum data become available

# Main findings
| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| Serum β-synuclein is selectively elevated in A+T+ AD compared to A-T- controls | Reported | Abstract | Cohen's d=0.69 | Yes (abstract) | Full methods and figures not inspected |
| β-synuclein independently predicts dementia conversion (HR=1.40 per SD) | Reported | Abstract | HR=1.40 per SD; p-value and CI not extracted | Yes (abstract) | Independence from pTau181/Aβ42/40 stated but covariate model not confirmed from full text |
| β-synuclein provides prognostic information beyond pTau181 and Aβ42/40 for mortality | Reported | Abstract | Effect size not extracted | Yes (abstract) | Single-centre; no external validation cohort reported |

# What is actually new?
- Biological novelty: β-synuclein (SNCB; minor synaptic protein) as a serum biomarker with independent prognostic value in AT-classified AD — not previously validated at this scale in serum
- Methodological novelty: AT stratification framework applied to β-synuclein; incremental value tested against standard pTau181/Aβ42/40
- Dataset or resource novelty: Memory clinic cohort with long longitudinal follow-up (4.1 years) and AT classification (n=259)
- What was already known: α-synuclein is elevated in Parkinson's; serum neurofilament light (NEFL) and pTau217 predict AD; β-synuclein had been observed in CSF but serum data limited

# Strengths
- Design strength: AT-classified cohort with longitudinal follow-up; direct comparison with established biomarkers
- Validation strength: Multiple AT strata; direct comparison vs Aβ42/40 and pTau181 as covariates
- Reproducibility strength: Single-centre limits reproducibility; biomarker assay details unavailable
- Translational or ecological realism: Serum matrix; memory clinic patients; real-world prognostic design

# Limitations and bias risks
- Sample-size or power limitation: n=259 total; A-T+ stratum n=65 is modest
- Confounding: Age, sex, APOE not confirmed controlled (full text not inspected)
- Batch or site effects: Single-centre; no external validation
- Pseudoreplication risk: Not applicable (patient-level observational)
- Leakage or overfitting risk: Unknown — incremental model over pTau181/Aβ42/40 requires careful cross-validation
- Generalizability limitation: Memory clinic referral bias; one centre; serum assay platform unspecified
- Missing controls: No Parkinson's or other synucleinopathy comparison; no longitudinal serum sampling
- Missing validation: No independent external cohort; no head-to-head vs NEFL or pTau217
- Author-stated limitations: Not extracted (full text not inspected)
- Additional limitations identified during review: Serum β-synuclein assay platform unknown — cross-platform comparability unclear; single-centre design limits generalizability

# Transferability to the user's work
- Directly transferable elements: β-synuclein as a candidate serum biomarker to add to AD/neurodegeneration panel; AT stratification framework; HR=1.40 per SD as effect-size benchmark for power calculations
- Elements requiring adaptation: Serum assay platform must be identified and matched; cohort characteristics may differ from TBI or organoid contexts
- Model, species, tissue, matrix, platform, or scale mismatch: Human serum (clinical cohort) vs organoid/mouse models; different disease contexts
- Assumptions required for transfer: β-synuclein release into serum reflects synaptic loss that may also occur in TBI
- Confidence: low-moderate (full text not inspected; single-centre; translational path unclear)

# Practical implications
- Experimental implication: Consider including serum β-synuclein in biomarker panels for AD/TBI longitudinal studies; obtain assay details from full text
- Analysis implication: HR=1.40 per SD provides a power-calculation anchor for biomarker studies targeting dementia conversion
- Public dataset implication: Dataset not publicly available; contact authors for data-sharing
- Biomarker or translational implication: β-synuclein may complement pTau217/NEFL/GFAP panel for dementia prediction; independently additive to Aβ and pTau181
- Grant or manuscript implication: Cite as first serum validation of β-synuclein in AT-classified cohort; contrast with Mu 2026 (lecanemab-driven biomarker dynamics)

# Contradictions and links
- Supports: AD/ADRD biomarker panel literature (pTau217, NEFL, GFAP); synuclein biology in neurodegeneration
- Contradicts: Papers arguing that serum synuclein species are not sufficiently sensitive for AD-specific use
- Replicates: Prior smaller CSF β-synuclein studies (not extracted)
- Methodologically comparable papers: mu_2026 (Lancet Neurology, plasma biomarker dynamics); bjornholm_2026 (vascular/microglial atlas as complementary atlas-level reference)
- Relevant synthesis notes: None yet
- Relevant project decisions: None recorded

# Follow-up actions
- [ ] Obtain full text (Brain journal — check institutional access or request reprint)
- [ ] Extract exact β-synuclein assay platform, LOD/LOQ, and batch QC details
- [ ] Confirm covariate model (age, sex, APOE) and CI for HR=1.40
- [ ] Check for external validation cohort or planned replication study
- [ ] Compare β-synuclein effect size against NEFL, pTau217, GFAP in same cohort

# Priority decision
- Priority: 1
- Read now
- Rationale: First serum validation of β-synuclein as independent prognostic biomarker in AT-classified AD; direct clinical relevance for biomarker panel design in neurodegeneration studies; Brain journal, peer-reviewed, Oct 2026.
