---
record_type: paper
record_status: needs_full_text
canonical_id: "PMID:42785333"
doi: "10.1016/S1474-4422(26)00284-X"
pmid: "42785333"
title: "Dynamic changes in plasma biomarkers of Alzheimer's disease in patients treated with lecanemab: a longitudinal cohort study"
year: 2026
source_type: primary
peer_reviewed: true
full_text_checked: false
supplement_checked: false
code_checked: false
data_checked: false
last_verified: 2026-11-01
priority: 2
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
- Full citation: Mu Y, Ibanez L, Babulal GM, Braunstein JB, Coble DW, Dixon R, et al. Dynamic changes in plasma biomarkers of Alzheimer's disease in patients treated with lecanemab: a longitudinal cohort study. Lancet Neurology. 2026 Nov;25(11):997–1009. Published online 2026 Sep 24. doi:10.1016/S1474-4422(26)00284-X.
- DOI / PMID: https://doi.org/10.1016/S1474-4422(26)00284-X / PMID 42785333
- Related preprint or published version: None identified
- Correction, expression of concern, or retraction status: None as of 2026-11-01

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Characterizes trajectory patterns of 130 plasma proteins across lecanemab-treated vs untreated AD patients; identifies which biomarkers normalise, overcorrect, or move in unexpected directions with amyloid clearance. Critical for interpreting plasma biomarker changes in intervention studies and for separating disease vs treatment effects.
- Why it is more or less useful than neighboring literature: Larger and more comprehensive than prior lecanemab biomarker sub-studies; Washington University/Knight ADRC cohort with Aβ-negative controls provides strong contrast; temporal trajectory classification is methodologically novel for biomarker interpretation.

# Source inspection status
- Abstract inspected: Yes (PubMed abstract)
- Full text inspected: No (Lancet Neurology paywalled; full text not accessible)
- Methods inspected: No (abstract-level only)
- Supplement inspected: No
- Figures/tables inspected: No
- Code repository inspected: No
- Data repository inspected: No
- Missing material: Full methods; protein assay platforms; trajectory classification model details; supplement tables; raw data accession

# Study question and hypothesis
- Primary question: How do plasma biomarkers of AD change over time in patients treated with lecanemab versus untreated controls, and do different biomarkers show distinct trajectory patterns?
- Stated hypothesis: Amyloid clearance by lecanemab will cause biomarker changes that reflect downstream downstream disease modification, not just amyloid removal; trajectory patterns will differ by biological mechanism.
- Study type: Longitudinal observational cohort with treatment comparison; plasma proteomics in real-world/trial cohort

# Biological or clinical context
- Disease / exposure / process: Alzheimer's disease; lecanemab (anti-amyloid antibody treatment)
- Organism: Homo sapiens
- Tissue / cell type: Plasma; reflecting CNS and systemic biology
- Model system: Clinical cohort (Washington University/Knight ADRC)
- Cohort or population: 197 lecanemab-treated patients; 1312 untreated AD-spectrum controls; 458 Aβ-negative controls
- Relevant stage, age, sex, genotype, or disease severity: AD-spectrum (MCI/early AD based on lecanemab indication); Aβ status confirmed; exact age/sex/APOE distribution unknown (full text not inspected)

# Study design
- Experimental or observational unit: Individual patient
- Unit of inference: Patient-level plasma biomarker trajectory
- Groups and sample size per group: Lecanemab n=197; untreated AD controls n=1312; Aβ- controls n=458; total N=1967
- Biological replicates: Large longitudinal cohort; multiple time points per patient (frequency unknown)
- Technical replicates: Unknown (full text not inspected)
- Randomization: Not applicable (observational cohort; lecanemab assignment not randomised in this study)
- Blinding: Not reported in abstract
- Inclusion / exclusion criteria: Not extracted (full text not inspected); lecanemab-treated patients presumably fulfil standard clinical eligibility
- Batch structure: Unknown; multi-year longitudinal cohort
- Longitudinal, repeated-measures, paired, or donor structure: Longitudinal repeated plasma samples; trajectory-level analysis
- Controls and comparators: Untreated AD-spectrum controls; Aβ-negative controls to establish non-disease baseline trajectories

# Experimental methods
- Assay / platform: 130 plasma proteins measured (platform not specified in abstract — likely Olink Proximity Extension Assay or SomaScan; details require full text)
- Sample preparation: Plasma; longitudinal samples per patient (exact collection protocol unknown)
- Dose, concentration, force, exposure, or perturbation: Lecanemab standard clinical dosing (10mg/kg biweekly); exact regimen unknown (full text not inspected)
- Timing and sampling schedule: Longitudinal; exact sampling frequency and total follow-up duration not extracted from abstract
- Matrix / medium / substrate / environmental conditions: Human plasma
- Primary endpoint: Trajectory classification of 130 plasma proteins in treated vs untreated groups
- Secondary endpoints: Identification of normalising vs overcorrecting vs opposite-direction biomarkers; comparison to Aβ- controls
- QC criteria: Unknown (full text not inspected)
- Failure or exclusion criteria: Unknown
- Exact reusable parameters and source location: Assay panel and trajectory model details unavailable without full text

# Computational and statistical methods
- Raw input: Longitudinal plasma protein concentrations (130 proteins per patient per visit)
- Preprocessing: Unknown (full text not inspected)
- Normalization: Unknown
- Feature filtering: 34 of 130 proteins showed significant changes; selection criteria unknown
- Covariates and design formula: Unknown; likely age, sex, APOE, disease severity
- Statistical test or model: Trajectory classification model (4 trajectory types defined); mixed-effects longitudinal models inferred
- Multiple-testing correction: Unknown (full text not inspected)
- Effect-size reporting: Not extracted from abstract; 34 significant proteins reported
- Batch handling: Unknown; multi-year longitudinal cohort
- Validation strategy: Aβ-negative controls used to anchor pre-disease baseline; untreated AD controls used for trajectory comparison
- External validation: Not reported in abstract (single-cohort study)
- Software and versions: Unknown
- Code availability: Not reported in abstract

# Data and resource availability
- Repository and accession: Knight ADRC data — partially available via NIAGADS or RADC; specific accession for this dataset unknown (full text not inspected)
- Raw data available: Unknown
- Processed data available: Unknown; Lancet Neurology open-data policies vary
- Metadata completeness: Unknown
- Data-use restrictions: Likely NIAGADS controlled-access agreement if deposited
- Reusability for the user's work: Moderate — the 4 trajectory classes and the 34-protein panel are directly conceptually reusable; raw data requires data-sharing agreement; useful as benchmark for biomarker dynamics in intervention contexts

# Main findings
| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| 34 of 130 plasma proteins significantly changed with lecanemab treatment | Reported | Abstract | 34/130 proteins; effect sizes not extracted | Yes (abstract) | Full statistical model not inspected |
| Four trajectory types: normalising (pTau217, MAPT, GFAP), overcorrecting (Aβ peptides), opposite-direction (NPTXR, NRGN, TREM2), unchanged (NEFL, APOE) | Reported | Abstract | Trajectory classification; exact effect sizes not extracted | Yes (abstract) | Classification model details not confirmed from full text |
| pTau217, MAPT, and GFAP normalise toward Aβ- control levels with lecanemab | Reported | Abstract | Direction and trend reported; effect size not extracted | Yes (abstract) | Speed and degree of normalisation unknown |
| NEFL and APOE do not change significantly with lecanemab | Reported | Abstract | Unchanged trajectory class | Yes (abstract) | May indicate downstream damage not modified by amyloid removal |
| NPTXR, NRGN, and TREM2 move in the opposite direction to expected normalisation | Reported | Abstract | Opposite-direction trajectory class | Yes (abstract) | Biological interpretation unclear; could reflect treatment effect or confounding |

# What is actually new?
- Biological novelty: Systematic trajectory classification of 130 plasma proteins across lecanemab treatment — identifies which markers reflect treatment vs disease vs secondary effects; TREM2/NRGN/NPTXR moving opposite to expected is novel and mechanistically puzzling
- Methodological novelty: 4-class trajectory framework for longitudinal multi-protein biomarker analysis under treatment; large untreated cohort comparison (n=1312)
- Dataset or resource novelty: Largest lecanemab plasma proteomics longitudinal dataset identified as of 2026-11-01; Knight ADRC cohort
- What was already known: Lecanemab clears amyloid; pTau217 decreases with amyloid removal; NEFL tracks neurodegeneration; TREM2 elevated in AD

# Strengths
- Design strength: Large untreated and Aβ-negative control groups provide strong trajectory context; multi-time-point longitudinal design
- Validation strength: Aβ- controls as biological baseline anchor; 1312 untreated comparators reduce selection bias
- Reproducibility strength: Single-centre but large n; standard clinical cohort (Knight ADRC); methodological details require full text
- Translational or ecological realism: Real-world lecanemab recipients; plasma biomarker panel clinically actionable

# Limitations and bias risks
- Sample-size or power limitation: n=197 treated; may be underpowered for subgroup analyses by APOE or severity
- Confounding: Lecanemab eligibility criteria may select patients with specific biomarker profiles; selection into treatment not randomised
- Batch or site effects: Multi-year longitudinal collection; potential drift in assay performance
- Pseudoreplication risk: Repeated measures per patient — mixed-effects model required (likely used but not confirmed)
- Leakage or overfitting risk: Trajectory classification on training data without external validation (inferred; full text not inspected)
- Generalizability limitation: Single centre (Washington University/Knight ADRC); mainly US academic memory clinic population
- Missing controls: No randomised placebo control; treatment assignment observational
- Missing validation: No independent cohort validation of trajectory classes; no CSF confirmation of biomarker trajectories
- Author-stated limitations: Not extracted (full text not inspected)
- Additional limitations identified during review: Trajectory classification model details unknown; unclear whether 130-protein panel or targeted assays used

# Transferability to the user's work
- Directly transferable elements: 4-class trajectory framework for categorising biomarker responses to intervention; specific protein panel (pTau217, GFAP, NEFL, TREM2, NRGN, NPTXR, MAPT) as candidate panel for TBI/AD biomarker studies
- Elements requiring adaptation: Treatment context is anti-amyloid therapy; adaptation to TBI context requires different comparator groups; platform-specific assay details needed
- Model, species, tissue, matrix, platform, or scale mismatch: Clinical intervention trial (lecanemab) vs pre-clinical TBI/organoid models; plasma vs serum
- Assumptions required for transfer: Protein trajectories reflect shared downstream biology between lecanemab-treated AD and TBI-to-AD progression
- Confidence: low (no direct TBI relevance; treatment-vs-disease distinction may not transfer; full text not inspected)

# Practical implications
- Experimental implication: Use the 4-trajectory classification (normalising/overcorrecting/opposite/unchanged) as a conceptual framework when interpreting longitudinal biomarker data in TBI studies
- Analysis implication: Trajectory-based mixed-effects modelling rather than single-timepoint comparison for longitudinal plasma proteomics
- Public dataset implication: Knight ADRC data likely available via NIAGADS controlled access; 1312-patient untreated cohort is a large reference dataset
- Biomarker or translational implication: NEFL/APOE stability under amyloid clearance suggests these track neurodegeneration independent of amyloid; TREM2 response to lecanemab may inform microglial state monitoring
- Grant or manuscript implication: Cite as evidence that biomarker trajectories under treatment can diverge from baseline disease trajectories; contrasts with Oberstein 2026 (prognostic biomarkers) and Bjørnholm 2026 (cellular state atlas)

# Contradictions and links
- Supports: AD biomarker dynamics literature; microglial marker (TREM2) response to amyloid
- Contradicts: Simplistic view that amyloid clearance normalises all downstream AD biomarkers
- Replicates: Prior smaller lecanemab biomarker sub-studies (CLARITY AD phase 3 sub-study)
- Methodologically comparable papers: oberstein_2026 (serum β-synuclein AD biomarker); bjornholm_2026 (cellular atlas context for TREM2 biology)
- Relevant synthesis notes: None yet
- Relevant project decisions: None recorded

# Follow-up actions
- [ ] Obtain full text (Lancet Neurology — check institutional access)
- [ ] Extract full 34-protein list and trajectory assignments
- [ ] Identify proteomics platform (Olink vs SomaScan vs other)
- [ ] Check Knight ADRC NIAGADS for data-sharing agreement and accession
- [ ] Cross-reference TREM2 trajectory with Bjørnholm 2026 TREM2 microglial findings

# Priority decision
- Priority: 2
- Retain for methods and biomarker panel design
- Rationale: Largest published lecanemab plasma proteomics longitudinal study; trajectory classification framework is methodologically transferable; TREM2/pTau217/GFAP panel directly relevant to AD/TBI biomarker work; Lancet Neurology, peer-reviewed, Sep 2026.
