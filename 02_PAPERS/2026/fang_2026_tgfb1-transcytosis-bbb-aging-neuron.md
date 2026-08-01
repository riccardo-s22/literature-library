---
record_type: paper
record_status: partial
canonical_id: "10.1016/j.neuron.2026.06.003"
doi: "10.1016/j.neuron.2026.06.003"
pmid: "42385697"
title: "TGF-β1-induced endothelial transcytosis drives blood-brain barrier leakage during aging"
year: 2026
source_type: primary
peer_reviewed: true
full_text_checked: false
supplement_checked: false
code_checked: false
data_checked: false
last_verified: 2026-08-01
priority: 2
projects: []
topics:
  - neurodegeneration
  - AD_ADRD
  - aging
  - mechanobiology
methods:
  - controlled_exposure
  - imaging
  - animal_model
datasets: []
---

# Citation
- Full citation: Fang C, Ma Y, Wei P, Yang S, Yu M, Liu J, Suo S, Zhao R, Ji Y, Hussain B, Qiu L, Zhang Z, Chen X, Lin K, Wang F, Guo ZN, Yang Y, Chang J. TGF-β1-induced endothelial transcytosis drives blood-brain barrier leakage during aging. *Neuron*. 2026; doi:10.1016/j.neuron.2026.06.003.
- DOI / PMID / stable URL: https://doi.org/10.1016/j.neuron.2026.06.003 | PMID 42385697
- Related preprint or published version: None identified
- Correction, expression of concern, or retraction status: None identified as of 2026-08-01

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Identifies a specific molecular mechanism (TGF-β1 → Tgfbr2 → Smad2/4 → suppressed Mfsd2a → caveolar transcytosis) for age-related BBB breakdown; demonstrates that pharmacological TGF-β inhibition is sufficient to reduce BBB leakage and attenuate neurological dysfunction in aged mice. Relevant to BBB-focused mechanobiology and neurodegeneration models.
- Why it is more or less useful than neighboring literature: Provides a mechanistically defined molecular pathway for age-related BBB leakage distinct from tight junction disruption; adds a causal intervention (pharmacological or genetic TGFβ inhibition) not present in prior correlative BBB aging studies. Complements Chen 2025 (BBB-on-chip shear; [02_PAPERS/2025/chen_2025_bbb-on-chip-shear-astrogliosis.md]) and Trivedi 2026 (dried platelet BBB repair; [02_PAPERS/2026/trivedi_2026_dried-platelet-bbb-repair-tbi.md]).

# Source inspection status
- Abstract inspected: Yes
- Full text inspected: No (Neuron paywalled; PMC accession not identified)
- Methods inspected: No
- Supplement inspected: No
- Figures/tables inspected: No
- Code repository inspected: No
- Data repository inspected: No
- Missing material: Full text, methods, supplement not inspected

# Study question and hypothesis
- Primary question: What molecular mechanism drives age-related blood-brain barrier leakage, and can it be targeted therapeutically?
- Stated hypothesis: TGF-β1, increasing with aging, suppresses Mfsd2a expression in brain microvascular endothelial cells via Tgfbr2-Smad2/4 signaling, thereby promoting caveolar transcytosis and BBB leakage rather than tight junction disruption
- Study type: Mechanistic in vivo mouse study with genetic and pharmacological interventions

# Biological or clinical context
- Disease / exposure / process: Age-related BBB breakdown; cerebrovascular aging; neurodegeneration-associated BBB dysfunction
- Organism: Mouse (aged)
- Tissue / cell type: Brain microvascular endothelial cells; BBB
- Model system: animal_model (aged mice); AAV-mediated gene knockdown/restoration; pharmacological TGF-β inhibition; endothelial-specific Tgfbr2 knockout
- Cohort or population: Aged mice (specific strain/age not specified in abstract)
- Relevant stage, age, sex, genotype, or disease severity: Aged mice (onset of BBB leakage in midlife per abstract); endothelial-specific Tgfbr2 knockout

# Study design
- Experimental or observational unit: Mouse (individual)
- Unit of inference: BBB permeability (in vivo); protein expression in brain endothelial cells
- Groups and sample size per group: Aged vs young controls; AAV-caveolin-1 KD; AAV-Mfsd2a restoration; Tgfbr2 knockout; pharmacological TGF-β inhibition; exact n not reported in abstract
- Biological replicates: Unknown (full text not inspected)
- Technical replicates: Unknown
- Randomization: Unknown
- Blinding: Unknown
- Inclusion / exclusion criteria: Unknown
- Batch structure: Unknown
- Longitudinal, repeated-measures, paired, or donor structure: Unknown; longitudinal BBB onset (midlife) implied
- Controls and comparators: Young mice; vehicle/AAV-control for gene manipulation; wild-type for Tgfbr2 KO

# Experimental methods
- Assay / platform: In vivo BBB permeability assays (tracer leakage); AAV-mediated gene delivery (caveolin-1 KD; Mfsd2a restoration); endothelial-specific Tgfbr2 conditional KO; pharmacological TGF-β inhibition; electron microscopy (caveolar vesicle counting implied); neurological function tests
- Sample preparation: Unknown (full text not inspected)
- Dose, concentration, force, exposure, or perturbation: AAV injection (dose unknown); TGF-β1 (concentration unknown); pharmacological TGF-β inhibitor (compound unknown)
- Timing and sampling schedule: Unknown; BBB leakage stated to begin in midlife
- Matrix / medium / substrate / environmental conditions: Brain microvascular endothelial cells in vivo; mouse brain
- Primary endpoint: BBB permeability; caveolar transcytosis (vesicle density); Mfsd2a and caveolin-1 protein levels
- Secondary endpoints: Neurological dysfunction (behavioral measures); endothelial vesicle formation
- QC criteria: Unknown
- Failure or exclusion criteria: Unknown
- Exact reusable parameters and source location: Not available without full text

# Computational and statistical methods
- Raw input: BBB permeability tracer measurements; protein quantification; behavioral scores
- Preprocessing: Unknown
- Normalization: Unknown
- Feature filtering: Not applicable
- Covariates and design formula: Not specified
- Statistical test or model: Unknown
- Multiple-testing correction: Unknown
- Effect-size reporting: Not reported in abstract
- Batch handling: Not applicable
- Validation strategy: Multiple genetic and pharmacological interventions converging on same pathway
- External validation: Not reported in abstract
- Software and versions: Unknown
- Code availability: Not applicable

# Data and resource availability
- Repository and accession: Not reported
- Raw data available: Unknown
- Processed data available: Unknown
- Metadata completeness: Unknown
- Data-use restrictions: Not reported
- Reusability for the user's work: TGF-β1/Mfsd2a/caveolin-1 pathway as a molecular handle for BBB aging studies; pharmacological inhibitor compounds (if named in full text) could be used as positive controls in BBB assays

# Main findings
Use one row per consequential claim.

| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| BBB leakage begins in midlife in mice and is driven primarily by caveolar transcytosis, not tight junction disruption | Reported | Abstract | Qualitative; onset timing and mechanistic evidence not quantified in abstract | Partial | Exact age of onset not specified; tight junction integrity assay not described |
| TGF-β1 increases with aging and suppresses Mfsd2a via Tgfbr2-Smad2/4 signaling in brain endothelial cells | Reported | Abstract | Mechanistic signaling pathway; quantitative TGF-β1 levels not in abstract | Partial | Whether TGF-β1 increase is sufficient or necessary for BBB leakage onset not specified |
| AAV-caveolin-1 KD or Mfsd2a restoration reduces endothelial vesicle formation and BBB leakage in aged mice | Reported | Abstract | Qualitative reduction stated | Partial | Effect magnitude and statistical significance not in abstract |
| Endothelial-specific Tgfbr2 KO or pharmacological TGF-β inhibition reduces BBB leakage and attenuates neurological dysfunction in aged mice | Reported | Abstract | Qualitative; specific behavioral endpoints and effect sizes not in abstract | Partial | Pharmacological compound identity, dose, and treatment duration not specified |
| TGF-β1-induced endothelial transcytosis is a central mechanism for age-related BBB breakdown | Inference | Conclusions | Consistent with experimental data above; causal claim | Yes | Mouse model only; human relevance not established; TGF-β1 has pleiotropic effects |

# What is actually new?
- Biological novelty: First mechanistic demonstration that caveolar transcytosis (not tight junction disruption) is the primary mechanism of age-related BBB leakage in mice; TGF-β1/Tgfbr2/Smad2/4/Mfsd2a axis as the upstream driver
- Methodological novelty: AAV + conditional KO + pharmacological convergence on single pathway; cell-type specific (endothelial-specific Tgfbr2 KO) establishes cell autonomy
- Dataset or resource novelty: None specific
- What was already known: BBB permeability increases with aging; Mfsd2a suppresses transcytosis; caveolin-1 promotes caveolar formation; TGF-β1 has roles in cerebrovascular biology; tight junction disruption has been the conventional explanation for aging BBB leakage

# Strengths
- Design strength: Multiple independent interventions (AAV KD, AAV restoration, conditional KO, pharmacological) converging on same pathway; endothelial-specific manipulation establishes cell autonomy
- Validation strength: Pharmacological + genetic orthogonal validation; neurological function endpoint connects to clinical relevance
- Reproducibility strength: AAV and conditional KO approaches are well-established; pharmacological intervention provides translational proof of concept
- Translational or ecological realism: Aged mice with spontaneous BBB leakage (not acute injury model); pharmacological inhibition (not genetic only) suggests therapeutic avenue

# Limitations and bias risks
- Sample-size or power limitation: Mouse numbers unknown (full text not inspected)
- Confounding: TGF-β1 has broad effects beyond brain endothelium; systemic TGF-β1 changes with aging have multiple targets; Mfsd2a suppression could have additional consequences
- Batch or site effects: Unknown; single institution (Shenzhen Institute of Advanced Technology + Jilin University)
- Pseudoreplication risk: Unknown
- Leakage or overfitting risk: Not applicable
- Generalizability limitation: Mouse model only; whether this mechanism operates in human aging brain not established; mouse vs human endothelial biology may differ
- Missing controls: Human tissue validation not reported; TGF-β1 source (brain vs systemic) not fully dissected
- Missing validation: No human brain vascular endothelial validation; no cross-species confirmation
- Author-stated limitations: Not visible without full text
- Additional limitations identified during review: Publication date is border of window (July 1, 2026); Neuron journal paywalled; full methods and statistical details not accessible

# Transferability to the user's work
- Directly transferable elements: TGF-β1/Mfsd2a/caveolin-1 pathway as molecular readout for BBB integrity in aging; AAV-Mfsd2a as a gene therapeutic approach for BBB restoration; pharmacological TGF-β inhibition as positive control in BBB models
- Elements requiring adaptation: Translate from aged mice to human iPSC-derived BBB or organoid models; need human endothelial validation
- Model, species, tissue, matrix, platform, or scale mismatch: Mouse in vivo only; not directly transferable to in vitro BBB-on-chip or organoid models without adaptation
- Assumptions required for transfer: TGF-β1/Mfsd2a axis is conserved between mouse and human brain endothelium; caveolar transcytosis is the primary BBB leakage mechanism in aging human brain
- Confidence: moderate (for mouse findings); low (for human translation)

# Practical implications
- Experimental implication: Include Mfsd2a and caveolin-1 expression as BBB integrity markers in aging or injury studies; test TGF-β inhibition as a positive control in BBB repair experiments
- Analysis implication: None currently
- Public dataset implication: None identified
- Biomarker or translational implication: TGF-β1 and Mfsd2a could serve as vascular biomarkers of age-related BBB integrity decline; pharmacological TGF-β inhibitors (if specified) may be repurposable for BBB preservation
- Grant or manuscript implication: Supports TGF-β pathway as therapeutic target for age-related neurovascular disease; cite as mechanism paper for aging BBB field

# Contradictions and links
- Supports: Chen 2025 (BBB-on-chip shear conditioning; [02_PAPERS/2025/chen_2025_bbb-on-chip-shear-astrogliosis.md]); Trivedi 2026 (platelet-based BBB repair; [02_PAPERS/2026/trivedi_2026_dried-platelet-bbb-repair-tbi.md])
- Contradicts: Prior models emphasizing tight junction disruption as primary aging BBB mechanism (general field; no specific record in library)
- Replicates: None
- Methodologically comparable papers: Strat 2026 (astrocyte mechanobiology review; [02_PAPERS/2026/strat_2026_astrocyte-mechanobiology-review.md]); Saleh 2023 (ECM stiffness astrocyte response; [02_PAPERS/2023/saleh_2023_ecm-stiffness-composition-astrocyte.md])
- Relevant synthesis notes: None yet
- Relevant project decisions: None yet

# Follow-up actions
- [ ] Access full text for methods details, exact mouse ages/strains, sample sizes, and pharmacological compound identity
- [ ] Search for PMC accession or postprint
- [ ] Check for companion human data (brain vasculature Mfsd2a in aging cohort)
- [ ] Add to synthesis on BBB models and mechanobiology when created

# Priority decision
- Priority: 2
- Retain for mechanism and background
- Rationale: Identifies a specific molecular mechanism for age-related BBB leakage in mice with pharmacological intervention evidence; useful background for BBB studies in neurodegeneration and mechanobiology domains, though mouse-only and lacks human validation
