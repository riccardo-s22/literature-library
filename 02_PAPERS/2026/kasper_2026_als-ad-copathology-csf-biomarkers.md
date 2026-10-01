---
record_type: paper
record_status: verified
canonical_id: pmid:42112660
doi: 10.1002/ana.78227
pmid: "42112660"
pmcid: PMC13327596
title: "Alzheimer's Disease Co-Pathology and Cognitive Impairment in Amyotrophic Lateral Sclerosis"
year: 2026
source_type: primary
peer_reviewed: true
full_text_checked: false
supplement_checked: false
code_checked: false
data_checked: false
last_verified: 2026-10-01
priority: 1
projects: []
topics:
  - neurodegeneration
  - ALS
  - AD_ADRD
  - aging
methods:
  - biomarker
  - human_cohort
  - external_validation
datasets: []
---

# Citation
- Full citation: Kasper E, Lehto A, Jürs A, et al. Alzheimer's Disease Co-Pathology and Cognitive Impairment in Amyotrophic Lateral Sclerosis. Ann Neurol. 2026;100(1):123-138.
- DOI / PMID / stable URL: https://doi.org/10.1002/ana.78227 / PMID 42112660 / PMC13327596
- Related preprint or published version: None identified
- Correction, expression of concern, or retraction status: None identified as of 2026-10-01

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Directly relevant to interpreting multi-biomarker profiles in ALS/ALS-FTD cohorts; establishes that tau-related CSF biomarkers (p-tau, total tau) associate with cognitive deficits in ALS independent of plasma TDP-43 levels — affects interpretation of CSF vs plasma biomarker panels in studies combining AD and TDP-43 pathology readouts.
- Why it is more or less useful than neighboring literature: Largest multi-biomarker ALS study (n=192) in the library cross-examining both AD-related (CSF Aβ, p-tau, t-tau) and ALS-specific (plasma TDP-43, NfL) markers with cognitive outcomes; includes autopsy validation subset; from the German DZNE multicenter network. Complements irwin_2024 (cryptic-HDGFL2 TDP-43 biomarker) and kac_2026 (tau368/p-tau ratio for FTLD-TDP vs FTLD-tau).

# Source inspection status
- Abstract inspected: Yes
- Full text inspected: No (PMC13327596 available — inspect for method details and autopsy sub-cohort sizes)
- Methods inspected: No
- Supplement inspected: No
- Figures/tables inspected: No
- Code repository inspected: No
- Data repository inspected: No
- Missing material: Full text, supplemental tables with individual biomarker AUC values, exact autopsy cohort n

# Study question and hypothesis
- Primary question: Are AD-related neuropathological changes (tau, Aβ, TDP-43) associated with cognitive impairment in ALS patients, as measured by in vivo biomarkers and postmortem brain pathology?
- Stated hypothesis: AD-related pathological changes contribute to cognitive decline in ALS, particularly in ALSci and ALS-FTD.
- Study type: Observational cohort + autopsy sub-cohort

# Biological or clinical context
- Disease / exposure / process: ALS, ALS-FTD, cognitively impaired ALS (ALSci); comparison to healthy controls
- Organism: Human
- Tissue / cell type: CSF, plasma; postmortem brain
- Model system: Human cohort; multicenter DZNE network
- Cohort or population: 192 individuals with ALS or ALS-FTD; 100 healthy controls; autopsy data available for a subset (n Unknown — full text needed)
- Relevant stage, age, sex, genotype, or disease severity: Unknown from abstract; median age Unknown; sex breakdown Unknown

# Study design
- Experimental or observational unit: Individual patient
- Unit of inference: Individual biomarker value and cognitive test score
- Groups and sample size per group: ALS n=Unknown, ALSci n=Unknown, ALS-FTD n=Unknown (summing to 192 total); HC n=100
- Biological replicates: N/A (observational)
- Technical replicates: Unknown
- Randomization: Not applicable
- Blinding: Unknown
- Inclusion / exclusion criteria: Unknown — full text needed
- Batch structure: Multicenter (DZNE sites); site-specific batch handling Unknown
- Longitudinal, repeated-measures, paired, or donor structure: Unknown (single time-point most likely)
- Controls and comparators: Healthy controls (n=100)

# Experimental methods
- Assay / platform: CSF total-tau, phosphorylated-tau (likely p-tau181), beta-amyloid; plasma TDP-43 (extracellular vesicle TDP-43), plasma NfL
- Sample preparation: Unknown — full text needed
- Dose, concentration, force, exposure, or perturbation: N/A
- Timing and sampling schedule: Unknown
- Matrix / medium / substrate / environmental conditions: CSF and plasma
- Primary endpoint: Association between AD-related biomarkers and cognitive performance (ECAS)
- Secondary endpoints: Group differences in biomarker levels; postmortem ABC score and TDP-43 burden
- QC criteria: Unknown
- Failure or exclusion criteria: Unknown
- Exact reusable parameters and source location: Unknown — full text needed

# Computational and statistical methods
- Raw input: Biomarker concentrations (CSF, plasma); ECAS cognitive domain scores
- Preprocessing: Unknown
- Normalization: Unknown
- Feature filtering: Unknown
- Covariates and design formula: Unknown — regression analyses examining biomarker-cognition associations
- Statistical test or model: Group comparisons; regression analyses; ROC/AUC implied
- Multiple-testing correction: Unknown
- Effect-size reporting: AUC reported for distinguishing cognitive impairment groups (exact values Unknown — full text needed)
- Batch handling: Unknown (multicenter)
- Validation strategy: Autopsy sub-cohort with ABC scores and TDP-43 burden
- External validation: Postmortem neuropathology (subset)
- Software and versions: Unknown
- Code availability: Unknown

# Data and resource availability
- Repository and accession: Unknown — full text needed
- Raw data available: Unknown
- Processed data available: Unknown
- Metadata completeness: Unknown
- Data-use restrictions: Unknown
- Reusability for the user's work: High if data deposited; CSF/plasma biomarker reference ranges would be reusable

# Main findings
Use one row per consequential claim.

| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| Patients with ALSci and ALS-FTD show elevated AD-related biomarkers (Aβ, p-tau, t-tau) vs healthy controls | Reported | Abstract | Quantitative differences; exact values Unknown | Yes | Single-time-point; multicenter site batch effects Unknown |
| Significant differences in CSF Aβ between HC and ALSci, but not between HC and cognitively unimpaired ALS | Reported | Abstract | Not quantified in abstract | Yes | Aβ differences may reflect co-occurring AD; causality unclear |
| CSF p-tau and t-tau strongly associated with domain-specific cognitive performance in ALS | Reported | Abstract | Strong association (Inference: likely r or β coefficient; exact value Unknown) | Yes | Cross-sectional association; direction of causality not established |
| Plasma EV-TDP-43 and NfL show weak or no association with cognition | Reported | Abstract | Weak/no association | Yes | EV-TDP-43 specificity to neuronal TDP-43 vs systemic sources Unknown |
| Postmortem temporal and hippocampal TDP-43 burden (not total) associated with cognitive dysfunction | Reported | Abstract | Regional specificity (temporal, hippocampal) noted | Partial | Small autopsy sub-cohort; sampling details Unknown |

# What is actually new?
- Biological novelty: Demonstrates that tau-related CSF biomarkers, not plasma TDP-43, distinguish cognitively impaired from cognitively unimpaired ALS patients; suggests AD co-pathology is a mechanistically distinct contributor to cognitive decline in ALS.
- Methodological novelty: Largest multi-biomarker cohort (n=192) in ALS/ALS-FTD crossing both AD and TDP-43 biomarkers simultaneously.
- Dataset or resource novelty: DZNE multicenter cohort with concurrent in vivo biomarker and postmortem data.
- What was already known: TDP-43 pathology is defining in ALS; tau pathology can co-occur in ALS; NfL is an ALS disease-activity marker. Not previously shown in this n at this scale across cognitive subgroups.

# Strengths
- Design strength: Large n (192), multicenter DZNE network, concurrent in vivo + postmortem validation.
- Validation strength: Autopsy sub-cohort to confirm in vivo biomarker findings.
- Reproducibility strength: Multicenter reduces single-site bias.
- Translational or ecological realism: CSF and plasma biomarkers directly applicable to clinical monitoring; ECAS is a validated cognitive screening tool for ALS.

# Limitations and bias risks
- Sample-size or power limitation: Subgroup analyses (ALSci, ALS-FTD) may be underpowered; autopsy sub-cohort n Unknown.
- Confounding: Age, sex, disease duration, site not fully controlled (details Unknown); comorbid AD diagnoses may not be clinically excluded.
- Batch or site effects: Multicenter; batch correction strategy Unknown.
- Pseudoreplication risk: Low for CSF/plasma biomarkers; low for ECAS
- Leakage or overfitting risk: N/A (observational)
- Generalizability limitation: DZNE cohort may not generalize to non-European or community ALS populations.
- Missing controls: No cognitively impaired non-ALS control group to isolate ALS-specific cognitive biomarker pattern.
- Missing validation: Independent cohort validation of CSF tau cutoffs for ALS cognitive impairment.
- Author-stated limitations: Unknown — full text needed.
- Additional limitations identified during review: Plasma EV-TDP-43 assay platform (exact assay, antibody, LOQ) unspecified in abstract; potential CSF contamination with blood Unknown.

# Transferability to the user's work
- Directly transferable elements: Multi-biomarker panel design (CSF tau + Aβ + plasma TDP-43 + NfL) as reference for ALS/ALS-FTD cohort studies; CSF tau association with cognitive domains.
- Elements requiring adaptation: Cognitive endpoints (ECAS) may need supplementation with neuroimaging for mechanistic interpretation.
- Model, species, tissue, matrix, platform, or scale mismatch: Human cohort; direct relevance to ALS/FTD biomarker design; transferability to organoid or animal model readouts is indirect (biomarker levels are matrix-dependent).
- Assumptions required for transfer: AD co-pathology is assumed clinically relevant; pathological confirmation is in a sub-cohort only.
- Confidence: moderate

# Practical implications
- Experimental implication: In ALS biomarker studies, measure CSF tau/p-tau alongside TDP-43 markers; cognitive stratification (ECAS or equivalent) should be incorporated.
- Analysis implication: Regression models for ALS cognitive outcomes should include CSF tau as a covariate, not just NfL or TDP-43.
- Public dataset implication: Verify whether DZNE multicenter data are available for reuse (check BioFINDER or DZNE data-sharing policy).
- Biomarker or translational implication: CSF p-tau and t-tau, not plasma TDP-43, are the biomarkers of cognitive impairment in ALS — contrary to the assumption that TDP-43 burden drives all cognitive decline.
- Grant or manuscript implication: Strong justification for including AD co-pathology assessments in TBI-to-neurodegeneration longitudinal designs.

# Contradictions and links
- Supports: irwin_2024 (TDP-43 functional loss as biomarker); kac_2026 (tau isoforms for FTLD-tau discrimination); warmenhoven_2025 (plasma tau in AD/ADRD)
- Contradicts: Simple model where plasma TDP-43 alone predicts cognitive impairment in ALS
- Replicates: DZNE network biomarker studies (previous smaller cohorts; author group overlap)
- Methodologically comparable papers: warmenhoven_2025 (head-to-head plasma ptau217), kac_2026 (CSF tau368 ratio)
- Relevant synthesis notes: None yet
- Relevant project decisions: None yet

# Follow-up actions
- [ ] Inspect PMC13327596 full text: extract autopsy sub-cohort n, exact regression coefficients, exact biomarker assay platforms and LOQ values
- [ ] Confirm DZNE data sharing policy for potential independent validation
- [ ] Add to synthesis on TDP-43 and tau biomarker landscape in ALS/FTD if one is built

# Priority decision
- Priority: 1
- Read now
- Rationale: Largest multi-biomarker ALS cohort in the library; establishes CSF tau (not plasma TDP-43) as the cognitive biomarker in ALS; directly informs future cohort and biomarker panel design in this domain.
