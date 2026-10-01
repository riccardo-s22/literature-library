---
record_type: paper
record_status: verified
canonical_id: pmid:42561511
doi: 10.1016/j.neurot.2026.e01032
pmid: "42561511"
pmcid: PMC13464227
title: "Intrabody B1 targeting TDP-43 modulates neuroinflammatory and metabolic pathways in a preclinical ALS model"
year: 2026
source_type: primary
peer_reviewed: true
full_text_checked: false
supplement_checked: false
code_checked: false
data_checked: false
last_verified: 2026-10-01
priority: 2
projects: []
topics:
  - neurodegeneration
  - ALS
  - transcriptomics
  - multi_omics
methods:
  - analysis_method
  - animal_model
  - controlled_exposure
  - bulk_RNAseq
datasets: []
---

# Citation
- Full citation: Al Ojaimi Y, Dupuis A, Palla M, et al. Intrabody B1 targeting TDP-43 modulates neuroinflammatory and metabolic pathways in a preclinical ALS model. Neurotherapeutics. 2026;23(5):e01032.
- DOI / PMID / stable URL: https://doi.org/10.1016/j.neurot.2026.e01032 / PMID 42561511 / PMC13464227
- Related preprint or published version: None identified
- Correction, expression of concern, or retraction status: None identified as of 2026-10-01

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Informs mechanistic understanding of TDP-43-driven neuroinflammatory and metabolic pathways; negative result (molecular modulation without functional benefit post-symptom onset) is directly relevant to design of TDP-43-targeting interventions and the timing question for ALS therapies. Multi-omics (transcriptomics + metabolomics + plasma biomarkers) in the same cohort provides a reusable multi-readout ALS mouse model dataset.
- Why it is more or less useful than neighboring literature: Combines AAV-delivered scFv therapeutic with comprehensive multi-omics readout (RNA-seq, metabolomics, PET, plasma NfL/TDP-43) in a single study; captures both molecular effects and lack of functional benefit — critical negative evidence. Complementary to irwin_2024 (TDP-43 fluid biomarker) and li_2023_c9orf72 (glial states in ALS).

# Source inspection status
- Abstract inspected: Yes
- Full text inspected: No (PMC13464227 available — inspect for AAV dose, titer, injection site, RNA-seq details, metabolomic platform)
- Methods inspected: No
- Supplement inspected: No
- Figures/tables inspected: No
- Code repository inspected: No
- Data repository inspected: No
- Missing material: Full text, supplemental data tables, RNAseq accession, metabolomics accession

# Study question and hypothesis
- Primary question: Does AAV-delivered anti-TDP-43 intrabody scFv B1 modulate neuroinflammatory and metabolic pathways and provide functional benefit in a preclinical ALS mouse model when administered after symptom onset?
- Stated hypothesis: scFv B1 will reduce TDP-43-driven inflammatory signaling and yield functional benefit.
- Study type: Preclinical interventional (AAV gene delivery in transgenic mice)

# Biological or clinical context
- Disease / exposure / process: ALS (TDP-43 proteinopathy); AAV-mediated intrabody delivery after symptom onset
- Organism: Mouse (transgenic)
- Tissue / cell type: CNS (motor neurons, glia); plasma
- Model system: hTDP-43(WTxA315T) transgenic mouse model; NSC-34 motor neuron-like cells (in vitro)
- Cohort or population: Two cohorts: longitudinal (nine months) and terminal (six months post-treatment); exact group sizes Unknown — full text needed
- Relevant stage, age, sex, genotype, or disease severity: Symptomatic onset; hTDP-43 (WTxA315T); sex breakdown Unknown

# Study design
- Experimental or observational unit: Individual mouse
- Unit of inference: Group mean (treated vs untreated)
- Groups and sample size per group: B1-treated and control; exact n Unknown — full text needed
- Biological replicates: Multiple mice per group (n Unknown)
- Technical replicates: Unknown
- Randomization: Assumed (preclinical); details Unknown
- Blinding: Unknown
- Inclusion / exclusion criteria: Symptom onset trigger for intervention; criteria Unknown
- Batch structure: Unknown; two separate cohort designs (longitudinal vs terminal)
- Longitudinal, repeated-measures, paired, or donor structure: Longitudinal cohort (9 months); terminal cohort (6 months post-treatment)
- Controls and comparators: Wild-type (implied); hTDP-43(WTxA315T) without B1

# Experimental methods
- Assay / platform: AAV-CAP.B10 delivery; PET imaging (neurometabolic); plasma biomarkers (NfL, TDP-43); behavioral testing; RNA-seq; metabolomics; immunohistochemistry (implied)
- Sample preparation: Unknown — full text needed
- Dose, concentration, force, exposure, or perturbation: AAV-CAP.B10 delivering scFv B1; dose Unknown — full text needed
- Timing and sampling schedule: Symptom-onset administration; 6 or 9 months follow-up
- Matrix / medium / substrate / environmental conditions: Mouse CNS; plasma
- Primary endpoint: Motor behavior (behavioral testing); plasma NfL
- Secondary endpoints: RNA-seq (transcriptomics); metabolomics; PET; plasma TDP-43
- QC criteria: Unknown
- Failure or exclusion criteria: Unknown
- Exact reusable parameters and source location: AAV titer and injection site Unknown — full text needed

# Computational and statistical methods
- Raw input: RNA-seq reads; metabolite peak areas; behavioral scores; PET data; ELISA values
- Preprocessing: Unknown — full text needed
- Normalization: Unknown
- Feature filtering: Unknown
- Covariates and design formula: Unknown
- Statistical test or model: Group comparisons; pathway enrichment analysis (implied from NF-κB attenuation claim)
- Multiple-testing correction: Unknown
- Effect-size reporting: Partial normalization of metabolic/trophic genes toward wild-type levels; NF-κB-related inflammatory signatures attenuated — quantitative values Unknown
- Batch handling: Unknown
- Validation strategy: In vitro NSC-34 NF-κB data as mechanistic corroboration
- External validation: None identified
- Software and versions: Unknown
- Code availability: Unknown

# Data and resource availability
- Repository and accession: Unknown — full text needed (RNA-seq and metabolomics data likely deposited; check GEO / Metabolomics Workbench)
- Raw data available: Unknown
- Processed data available: Unknown
- Metadata completeness: Unknown
- Data-use restrictions: Unknown
- Reusability for the user's work: Moderate — multi-omics ALS mouse dataset reusable for comparison if deposited publicly; plasma TDP-43 stabilization as target engagement endpoint reusable

# Main findings
Use one row per consequential claim.

| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| In NSC-34 cells, scFv B1 reduced NF-κB activation in response to TDP-43 overexpression | Reported | Abstract | Direction only; exact fold-change Unknown | Yes | Cell line model; not primary motor neurons |
| scFv B1 achieves robust CNS expression via AAV-CAP.B10 after symptom onset | Reported | Abstract | Unknown quantification | Yes | AAV tropism and titer Unknown |
| RNA-seq reveals attenuation of NF-κB-related inflammatory signatures and partial normalization of metabolic/trophic genes | Reported | Abstract | Partial normalization; fold-changes Unknown | Yes | Partial; pathway-level effect only |
| Metabolomics shows shifts toward WT-like oxidative stress, mitochondrial, and phospholipid metabolites | Reported | Abstract | Direction only; Unknown magnitude | Yes | Clinical relevance Unknown; assay platform Unknown |
| Plasma TDP-43 levels were stabilized (systemic target engagement) | Reported | Abstract | Stabilization — Unknown quantification vs control | Yes | EV vs total TDP-43 distinction Unknown |
| B1 did NOT improve motor behavior or reduce plasma NfL post-symptom onset | Reported | Abstract | No significant difference | Yes | Negative result; timing of intervention (post-onset) is the key confound |

# What is actually new?
- Biological novelty: Demonstrates that upstream TDP-43-driven inflammatory and metabolic pathways can be modulated molecularly without translating to functional or neurodegenerative benefit post-symptom onset — distinguishes molecular target engagement from therapeutic efficacy.
- Methodological novelty: Multi-omics (RNA-seq, metabolomics, PET, plasma biomarkers) in a single TDP-43 therapeutic study; use of AAV-CAP.B10 neuro-specific capsid.
- Dataset or resource novelty: Multi-omics hTDP-43(WTxA315T) mouse longitudinal dataset (if deposited).
- What was already known: TDP-43 drives inflammatory and metabolic dysregulation in ALS; scFv intrabodies can engage intracellular targets via AAV delivery.

# Strengths
- Design strength: Dual-cohort design (longitudinal + terminal) with comprehensive multi-omics readout; in vitro mechanistic validation in NSC-34.
- Validation strength: Plasma TDP-43 as systemic target-engagement marker confirmed.
- Reproducibility strength: Two separate cohorts in same paper.
- Translational or ecological realism: Symptomatic intervention timing is clinically relevant (most ALS patients present post-symptom onset).

# Limitations and bias risks
- Sample-size or power limitation: Exact group sizes Unknown; hTDP-43 overexpression models are aggressive and may not reflect gradual TDP-43 proteinopathy in human ALS.
- Confounding: Transgenic overexpression model may not reflect human sporadic ALS biology.
- Batch or site effects: Unknown
- Pseudoreplication risk: Unknown; litter effects not mentioned.
- Leakage or overfitting risk: Metabolomic "shifts toward WT" without quantitative thresholds could be overfitted.
- Generalizability limitation: hTDP-43 overexpression model; results may not generalize to TDP-43-loss-of-function or C9orf72 ALS.
- Missing controls: GFP or empty vector AAV control not mentioned in abstract.
- Missing validation: Pre-symptomatic intervention arm absent; independent replication.
- Author-stated limitations: Need for earlier and likely combinatorial interventions in ALS.
- Additional limitations identified during review: AAV-CAP.B10 is an engineered capsid not yet in human use; translatability pathway unclear.

# Transferability to the user's work
- Directly transferable elements: Multi-omics endpoint design (RNA-seq + metabolomics + plasma NfL + plasma TDP-43) reusable as a readout panel for ALS model studies; negative result constrains expectations for post-onset TDP-43 targeting.
- Elements requiring adaptation: AAV titer and route would need optimization; NSC-34 results should be validated in primary motor neurons.
- Model, species, tissue, matrix, platform, or scale mismatch: Mouse; hTDP-43 transgenic; does not recapitulate all aspects of human sporadic ALS.
- Assumptions required for transfer: TDP-43 target engagement via scFv is assumed equivalent to reduction of TDP-43 proteinopathy.
- Confidence: moderate

# Practical implications
- Experimental implication: When designing ALS therapeutic studies, target engagement (plasma TDP-43 stabilization) ≠ functional rescue; include multi-omics to detect molecular vs functional dissociation.
- Analysis implication: RNA-seq pathway analysis for NF-κB/inflammatory pathways and metabolomics of oxidative stress endpoints together form a multi-layer validation strategy.
- Public dataset implication: Check GEO and Metabolomics Workbench for deposited data from this study.
- Biomarker or translational implication: Plasma TDP-43 as a target-engagement biomarker is supported; plasma NfL as a functional outcome marker remains the higher bar.
- Grant or manuscript implication: Negative result justifies pre-symptomatic intervention arm in ALS mechanistic studies.

# Contradictions and links
- Supports: irwin_2024 (TDP-43 functional loss drives ALS biology); kasper_2026 (TDP-43 plasma biomarker as engagement marker)
- Contradicts: Simple model where TDP-43 molecular modulation post-onset leads to functional benefit
- Replicates: No direct replication
- Methodologically comparable papers: li_2023_c9orf72 (multi-omics in ALS/FTD mouse)
- Relevant synthesis notes: None yet
- Relevant project decisions: None yet

# Follow-up actions
- [ ] Inspect PMC13464227 full text: extract AAV dose/titer, RNA-seq accession, metabolomics accession, exact group sizes, behavioral test details
- [ ] Check for RNA-seq data deposit in GEO
- [ ] Compare inflammatory gene signatures with ruf_2026 (cell-type-resolved TDP-43 pathology in motor cortex)

# Priority decision
- Priority: 2
- Retain for methods / mechanism
- Rationale: Provides important negative evidence that molecular TDP-43 target engagement does not confer post-onset functional benefit; multi-omics readout panel is reusable; PMC full text available.
