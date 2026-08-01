---
record_type: paper
record_status: verified
canonical_id: "10.1080/19491034.2026.2697135"
doi: "10.1080/19491034.2026.2697135"
pmid: "42415348"
title: "Elevation of the mechanically-sensitive protein emerin links nuclear mechanotransduction to tau-induced cytoskeletal remodeling in neurons"
year: 2026
source_type: primary
peer_reviewed: true
full_text_checked: true
supplement_checked: false
code_checked: false
data_checked: false
last_verified: 2026-08-01
priority: 2
projects: []
topics:
  - neurodegeneration
  - AD_ADRD
  - mechanobiology
methods:
  - cell_line
  - iPSC
  - imaging
datasets: []
---

# Citation
- Full citation: Sohn C, Pardo S, Molleur D, Paduri SR, Lambert M, Uttke Z, Sohn EJ, Thomas MG, Weintraub ST, Frost B. Elevation of the mechanically-sensitive protein emerin links nuclear mechanotransduction to tau-induced cytoskeletal remodeling in neurons. *Nucleus*. 2026;17(1):2697135.
- DOI / PMID / stable URL: https://doi.org/10.1080/19491034.2026.2697135 | PMID 42415348 | PMC13349007
- Related preprint or published version: None identified
- Correction, expression of concern, or retraction status: None identified as of 2026-08-01

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Identifies emerin (LEM-domain nuclear envelope protein) as an elevated mediator of nuclear mechanotransduction in tauopathy neurons; provides a molecular link between tau-induced cytoskeletal changes and nuclear mechanical dysfunction. Relevant to mechanobiology of neurodegeneration and to understanding how mechanical force signaling connects to tau pathology.
- Why it is more or less useful than neighboring literature: Bridges mechanobiology (nuclear mechanics, LINC complex, emerin) and neurodegeneration (tau, AD, FTD) domains; complements Elpers 2023 (nuclear confinement assay) and Leclech 2025 (nuclear deformation by topography) in the library by demonstrating a disease-relevant nuclear mechanotransduction pathway in neurons.

# Source inspection status
- Abstract inspected: Yes
- Full text inspected: Yes (via PMC13349007; full text read through Results and Discussion)
- Methods inspected: Partially (proteomic methods, iTau model described in Results)
- Supplement inspected: No
- Figures/tables inspected: No (text only)
- Code repository inspected: No
- Data repository inspected: No
- Missing material: Supplement not inspected; exact proteomic data availability not confirmed

# Study question and hypothesis
- Primary question: Does pathogenic tau alter nuclear mechanotransduction by affecting emerin levels and localization in neurons?
- Stated hypothesis: Pathogenic tau elevates emerin and redistributes it from nucleus to cytoplasm, disrupting the mechanical and signaling interface between cytoskeleton and nucleoskeleton, contributing to neurotoxicity
- Study type: Mechanistic cellular study (in vitro + iPSC-derived neurons)

# Biological or clinical context
- Disease / exposure / process: Tauopathy; Alzheimer's disease; FTD-associated tau mutation R406W
- Organism: Human (iPSC-derived neurons); cell line (BE(2)-C neuroblastoma)
- Tissue / cell type: Neurons (iPSC-derived; BE(2)-C neuroblastoma inducible tau model)
- Model system: cell_line (BE(2)-C iTau inducible tau R406W); iPSC (tau mutant iPSC-derived neurons)
- Cohort or population: Not applicable (cell culture)
- Relevant stage, age, sex, genotype, or disease severity: Tau R406W (FTD-associated mutation); iGFP control (transgene overexpression control without disease tau); iPSC-derived neurons (genotype not specified in inspected text)

# Study design
- Experimental or observational unit: Cell (BE(2)-C or iPSC-derived neuron)
- Unit of inference: Protein abundance (emerin); cellular phenotype (neurotoxicity, nuclear morphology, F-actin)
- Groups and sample size per group: iTau (doxycycline-induced tau R406W) vs iGFP (doxycycline-induced GFP control); replicate n not specified in abstract; emerin overexpression (gain-of-function) as third condition
- Biological replicates: Not specified in inspected text
- Technical replicates: DIA mass spectrometry: high group correlation among replicates stated
- Randomization: Not reported
- Blinding: Not reported
- Inclusion / exclusion criteria: Not applicable
- Batch structure: Not reported
- Longitudinal, repeated-measures, paired, or donor structure: Not applicable (cell culture)
- Controls and comparators: iGFP (transgenic expression control); uninduced iTau cells (basal)

# Experimental methods
- Assay / platform: DIA-HPLC mass spectrometry (unbiased proteomics); immunofluorescence (emerin localization, F-actin, nuclear morphology); iPSC-derived neuron differentiation; lentiviral emerin overexpression; co-immunoprecipitation (emerin binding partners); neurotoxicity assays
- Sample preparation: BE(2)-C cells; doxycycline induction of iTau (tau R406W) or iGFP; cell lysis for DIA-MS
- Dose, concentration, force, exposure, or perturbation: Doxycycline induction (dose not specified in inspected text); emerin overexpression via lentiviral construct
- Timing and sampling schedule: Not specified in inspected text
- Matrix / medium / substrate / environmental conditions: Standard cell culture conditions (details not reported)
- Primary endpoint: Emerin protein abundance change in iTau vs iGFP; emerin nuclear vs cytoplasmic distribution; neurotoxicity
- Secondary endpoints: F-actin levels; nuclear invagination; emerin binding partner changes (co-IP)
- QC criteria: DIA-MS group correlation verified; fold-change threshold ≥1.5 for significance
- Failure or exclusion criteria: Not reported
- Exact reusable parameters and source location: ~5,300 proteins detected per DIA-MS sample; 175 upregulated + 115 downregulated at FC ≥ 1.5 in iTau vs iGFP; Metascape gene enrichment analysis for GO terms; details in Results section and supplement (not inspected)

# Computational and statistical methods
- Raw input: DIA-HPLC MS raw files; proteomic quantification per protein per sample
- Preprocessing: Not specified in inspected text
- Normalization: Not specified
- Feature filtering: FC ≥ 1.5 threshold; statistical significance criteria not specified in inspected text
- Covariates and design formula: iTau vs iGFP (binary comparison); emerin overexpression as separate condition
- Statistical test or model: Not specified in inspected text; Metascape GO enrichment for pathway analysis
- Multiple-testing correction: Not specified
- Effect-size reporting: Fold change ≥ 1.5; 175 up / 115 down proteins
- Batch handling: Not applicable
- Validation strategy: iPSC-derived neurons as independent validation of emerin elevation; gain-of-function (emerin overexpression) phenocopy experiment
- External validation: iPSC-derived tau mutant neurons (independent cell model)
- Software and versions: Metascape (GO enrichment); MS analysis software not specified in inspected text
- Code availability: Not reported

# Data and resource availability
- Repository and accession: Proteomic data deposition not confirmed (supplement not inspected; likely PRIDE or MassIVE)
- Raw data available: Unknown
- Processed data available: Unknown (Supplemental Data 1 referenced in text for proteomic results)
- Metadata completeness: Unknown
- Data-use restrictions: Not reported
- Reusability for the user's work: iTau BE(2)-C model is available (published model from Frost lab); proteomic dataset may be deposited

# Main findings
Use one row per consequential claim.

| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| Pathogenic tau (iTau model) increases emerin protein levels in neurons | Reported | Results (proteomics) | Emerin among 175 upregulated proteins (FC ≥ 1.5) in iTau vs iGFP; exact FC not in abstract | Yes | BE(2)-C is a neuroblastoma line, not primary neurons; FTD tau R406W mutation |
| Emerin is elevated in tau mutant iPSC-derived neurons | Reported | Results (iPSC validation) | Qualitative elevation confirmed | Yes | iPSC genotype and exact magnitude not specified in inspected text |
| Emerin overexpression in neurons is sufficient to cause neurotoxicity, increase F-actin, and drive nuclear invagination | Reported | Results (gain-of-function) | Phenocopy of iTau cellular phenotypes | Yes | Overexpression levels may not match physiological disease range |
| Pathogenic tau causes emerin to redistribute from nucleus to cytoplasm | Reported | Results (imaging) | Cytosolic emerin enrichment and nuclear depletion in iTau | Yes | Mechanism of redistribution not established (trafficking vs retention) |
| Altered emerin binding partners in iTau neurons reflect cytosolic relocalization and increased cytoskeletal interactions | Reported | Results (co-IP) | Qualitative binding partner shift; specifics in supplement | Partial | Exact binding partners and interaction changes not listed in abstract or inspected text body |
| Emerin-mediated disruption of LINC complex signaling contributes to tau neurotoxicity | Inference | Discussion | Consistent with existing LINC/emerin literature; not directly tested causally | Partial | LINC complex manipulation not performed; causal chain from tau → emerin → toxicity not fully established |

# What is actually new?
- Biological novelty: Identifies emerin as a novel mediator linking tau pathology (AD/FTD) to nuclear mechanical dysfunction in neurons; connects tau's effects on F-actin to LINC complex mechanotransduction via emerin
- Methodological novelty: Unbiased DIA proteomics in iTau cellular tauopathy model to discover mechanotransduction proteins; iPSC-derived neuron validation as independent test system
- Dataset or resource novelty: DIA proteome of iTau vs iGFP BE(2)-C cells (~5,300 proteins; likely deposited)
- What was already known: Tau disrupts nuclear morphology, F-actin, and cytoskeleton; emerin is a key nuclear mechanotransducer in non-neuronal cells; LINC complex regulates nuclear mechanotransduction; nuclear stiffness is reduced in AD brain

# Strengths
- Design strength: Unbiased proteomics for discovery; gain-of-function validation (emerin overexpression phenocopies); iPSC-derived neurons for translatability
- Validation strength: iPSC-derived neurons provide independent confirmation of emerin elevation in human context
- Reproducibility strength: DIA-MS with high group correlation; iTau model is published and accessible
- Translational or ecological realism: Human iPSC-derived neurons; tau R406W is a human disease mutation; connects to Alzheimer's disease brain stiffness literature

# Limitations and bias risks
- Sample-size or power limitation: Replicate n not specified; typical small n for MS proteomics (3–5 replicates)
- Confounding: BE(2)-C is a neuroblastoma line (not primary neurons); R406W is a rare FTD mutation (not most common AD tau state)
- Batch or site effects: Single laboratory; single cell model
- Pseudoreplication risk: Unknown without supplement
- Leakage or overfitting risk: Not applicable
- Generalizability limitation: Results specific to tau R406W in BE(2)-C and iPSC neurons; relevance to sporadic AD (3R/4R tau) not established
- Missing controls: Post-translational modification state of emerin not characterized; whether emerin elevation precedes or follows tau pathology not determined
- Missing validation: In vivo validation (animal model of tauopathy) not reported; human postmortem AD brain emerin levels not examined
- Author-stated limitations: Mechanistic connection between tau → emerin → LINC disruption → toxicity not fully established; emerin function in post-mitotic neurons underexplored
- Additional limitations identified during review: Supplement not inspected; causality of emerin in tau toxicity (vs upstream marker) cannot be confirmed from abstract + text alone

# Transferability to the user's work
- Directly transferable elements: DIA-MS workflow for unbiased proteomic discovery in inducible neuronal tauopathy models; emerin as a mechanotransduction readout in neuronal cultures; iTau model as validated system for tau-nuclear mechanical interactions
- Elements requiring adaptation: Tau R406W → sporadic AD hyperphosphorylated tau or other tauopathies; BE(2)-C → primary neurons or iPSC-derived neurons for full relevance
- Model, species, tissue, matrix, platform, or scale mismatch: Cell line model (not in vivo or ex vivo); FTD mutation (not AD sporadic tau); iPSC validation partially addresses this
- Assumptions required for transfer: Emerin elevation is a conserved response to pathological tau across different tauopathies and neuronal subtypes
- Confidence: moderate (for emerin elevation and localization findings); low (for causal role in toxicity and generalizability to sporadic AD)

# Practical implications
- Experimental implication: Measure emerin levels and localization as a mechanotransduction readout in tauopathy models; use iTau + iGFP BE(2)-C as a discovery system for nuclear mechanobiology proteins
- Analysis implication: DIA-MS for unbiased protein-level discovery in inducible cell models is a validated approach; Metascape for GO enrichment is reproducible
- Public dataset implication: DIA proteome of iTau model (likely deposited in PRIDE/MassIVE; check supplement for accession)
- Biomarker or translational implication: Emerin localization change as a potential cellular biomarker of tau-driven nuclear mechanical stress; not yet actionable for fluid biomarkers
- Grant or manuscript implication: Mechanobiology of neurodegeneration is an emerging niche; emerin and LINC complex are understudied in AD neurons; cite as foundational for nuclear mechanotransduction in tauopathy

# Contradictions and links
- Supports: Elpers 2023 (nuclear mechanobiology agarose confinement; [02_PAPERS/2023/elpers_2023_agarose-confinement-nuclear-mechanobiology.md]); Leclech 2025 (topography-induced nuclear deformation; [02_PAPERS/2025/leclech_2025_microtopography-nuclear-deformation.md]); Braun 2021 (neurite orientation and mechanical tau pathology; [02_PAPERS/2021/braun_2021_neurite-orientation-mechanical-tau.md])
- Contradicts: None identified
- Replicates: First characterization of emerin in neuronal tauopathy; extends prior fibroblast emerin work to neurons
- Methodologically comparable papers: Prior proteomics studies of iTau model from Frost lab (prior publications); Braun 2021 (tau + mechanobiology)
- Relevant synthesis notes: None yet
- Relevant project decisions: None yet

# Follow-up actions
- [ ] Inspect supplement for exact emerin FC, sample sizes, and proteomic data accession
- [ ] Retrieve proteomic data from PRIDE/MassIVE when confirmed deposited
- [ ] Confirm whether emerin elevation is observed in human AD postmortem brain (may be in later papers)
- [ ] Add to synthesis on mechanobiology of neurodegeneration when created

# Priority decision
- Priority: 2
- Retain for methods and mechanism
- Rationale: Provides molecular mechanism connecting tau pathology to nuclear mechanotransduction in neurons; useful for mechanobiology-neurodegeneration intersection; supporting rather than decision-changing evidence at this stage
