---
record_type: paper
record_status: needs_full_text
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
last_verified: 2026-09-01
priority: 1
projects: []
topics: [neurodegeneration, AD_ADRD, aging, mechanobiology]
methods: [imaging, bulk_RNAseq]
datasets: []
---

# Citation
- Full citation: Fang et al. (2026). TGF-β1-induced endothelial transcytosis drives blood-brain barrier leakage during aging. *Neuron*. https://doi.org/10.1016/j.neuron.2026.06.003
- DOI / PMID / stable URL: 10.1016/j.neuron.2026.06.003 / PMID 42385697
- Related preprint or published version: Unknown
- Correction, expression of concern, or retraction status: None as of 2026-09-01

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Establishes that age-related BBB leakage is driven primarily by increased endothelial caveolar transcytosis (not tight junction disruption), mediated by TGF-β1, and reversible by AAV-mediated knockdown of caveolin-1 or restoration of Mfsd2a. Directly relevant to BBB mechanobiology, neurodegeneration risk, and TBI contexts where BBB integrity is a primary endpoint.
- Why it is more or less useful than neighboring literature: Mechanistically separates transcytosis from tight junction disruption as the primary BBB aging mechanism — a conceptual clarification with direct therapeutic implications. The genetic rescue approach (AAV caveolin-1 KD, Mfsd2a restoration) provides causal evidence not available from descriptive BBB aging studies.

# Source inspection status
- Abstract inspected: Yes
- Full text inspected: No
- Methods inspected: No
- Supplement inspected: No
- Figures/tables inspected: No
- Code repository inspected: No
- Data repository inspected: No
- Missing material: Full methods, animal model details, sample sizes, imaging parameters, RNA-seq data accession, TGF-β1 pathway details, quantitative leakage measurements

# Study question and hypothesis
- Primary question: What is the primary mechanism of age-related blood-brain barrier leakage, and can it be reversed?
- Stated hypothesis: Endothelial caveolar transcytosis (not tight junction disruption) drives age-related BBB leakage via TGF-β1 signaling
- Study type: Primary mechanistic study; in vivo animal model with genetic intervention

# Biological or clinical context
- Disease / exposure / process: Brain aging; cerebrovascular disease; neurodegenerative disease risk; BBB breakdown
- Organism: Unknown — likely mouse (inferred from AAV approach and context)
- Tissue / cell type: Brain endothelial cells; blood-brain barrier
- Model system: In vivo mouse model (inferred); AAV-mediated gene manipulation
- Cohort or population: Unknown — aged vs. young mice; N Unknown
- Relevant stage, age, sex, genotype, or disease severity: Midlife age point (BBB leakage reported to begin in midlife — from abstract)

# Study design
- Experimental or observational unit: Animal or brain region
- Unit of inference: BBB permeability; caveolin-1 and Mfsd2a expression; TGF-β1 signaling
- Groups and sample size per group: Unknown — young, midlife, aged; AAV knockdown groups
- Biological replicates: Unknown
- Technical replicates: Unknown
- Randomization: Unknown
- Blinding: Unknown
- Inclusion / exclusion criteria: Unknown
- Batch structure: Unknown
- Longitudinal, repeated-measures, paired, or donor structure: Cross-sectional at multiple age points (young, midlife, aged) based on abstract
- Controls and comparators: Young mice; aged + control AAV; multiple age time points

# Experimental methods
- Assay / platform: BBB permeability assay (tracers Unknown); AAV-mediated gene knockdown (caveolin-1) and overexpression (Mfsd2a); immunofluorescence; Unknown imaging
- Sample preparation: Unknown
- Dose, concentration, force, exposure, or perturbation: TGF-β1 signaling perturbation; AAV knockdown/rescue; ages: at least young and midlife/aged
- Timing and sampling schedule: Multiple age time points; AAV delivery timing Unknown
- Matrix / medium / substrate / environmental conditions: In vivo CNS vasculature
- Primary endpoint: BBB permeability (tracer leakage); transcytosis rate; tight junction integrity
- Secondary endpoints: TGF-β1 pathway components; caveolin-1 expression; Mfsd2a expression
- QC criteria: Unknown
- Failure or exclusion criteria: Unknown
- Exact reusable parameters and source location: Unknown — full text required

# Computational and statistical methods
- Raw input: Unknown — likely imaging data, possibly RNA-seq
- Preprocessing: Unknown
- Normalization: Unknown
- Feature filtering: Unknown
- Covariates and design formula: Age as factor; AAV treatment as factor
- Statistical test or model: Unknown
- Multiple-testing correction: Unknown
- Effect-size reporting: Unknown — qualitative from abstract ("begins in midlife", "driven primarily by transcytosis")
- Batch handling: Unknown
- Validation strategy: Genetic rescue (AAV) provides causal validation; multiple age points
- External validation: Unknown
- Software and versions: Unknown
- Code availability: Unknown

# Data and resource availability
- Repository and accession: Unknown
- Raw data available: Unknown
- Processed data available: Unknown
- Metadata completeness: Unknown
- Data-use restrictions: Unknown
- Reusability for the user's work: TGF-β1 pathway and caveolin-1/Mfsd2a axis as experimental targets for BBB integrity assays; relevant to TBI and BBB-on-chip models in the library

# Main findings
| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| Age-related BBB leakage begins in midlife | Reported (abstract) | Unknown | Unknown | Unknown | Abstract only |
| BBB leakage is driven by endothelial caveolar transcytosis, not tight junction disruption | Reported (abstract) | Unknown | Unknown | Unknown | Abstract only; mechanistic claim requires full text verification |
| AAV knockdown of caveolin-1 or Mfsd2a restoration ameliorates BBB leakage | Reported (abstract) | Unknown | Unknown | Unknown | Genetic rescue — magnitude of rescue Unknown |
| TGF-β1 drives the transcytosis increase | Reported (abstract) | Unknown | Unknown | Unknown | Abstract only; upstream driver mechanistic evidence pending |

# What is actually new?
- Biological novelty: Causal demonstration that transcytosis (not tight junction disruption) is the primary age-related BBB mechanism; TGF-β1 as upstream driver; genetic rescue at midlife
- Methodological novelty: AAV-mediated caveolin-1 knockdown + Mfsd2a restoration in aging BBB context; specific timing (midlife) of intervention
- Dataset or resource novelty: Unknown
- What was already known: Age-related BBB leakage is associated with neurodegeneration; caveolin-1 and Mfsd2a regulate transcytosis; TGF-β signaling modulates vascular biology

# Strengths
- Design strength: AAV genetic rescue provides causal evidence; multiple age time points establish midlife onset
- Validation strength: Genetic intervention in vivo (causal) vs. descriptive studies
- Reproducibility strength: Unknown
- Translational or ecological realism: In vivo aging model; AAV gene therapy as translatable approach

# Limitations and bias risks
- Sample-size or power limitation: Unknown
- Confounding: Unknown — other age-related vascular changes not fully controlled
- Batch or site effects: Unknown
- Pseudoreplication risk: Unknown — vessel vs. animal as unit of analysis
- Leakage or overfitting risk: Not applicable
- Generalizability limitation: Unknown — sex of animals not stated from abstract; aging timeline may differ across strains
- Missing controls: Unknown — whether TJ proteins are measured to confirm no TJ disruption; whether TGF-β1 blockade recapitulates the rescue
- Missing validation: Unknown — human tissue validation of midlife onset not confirmed from abstract
- Author-stated limitations: Unknown
- Additional limitations identified during review: No PMCID — full text not yet in PMC; abstract-only inspection

# Transferability to the user's work
- Directly transferable elements: Caveolin-1/Mfsd2a/TGF-β1 axis as molecular targets for BBB integrity assays; transcytosis measurement approach
- Elements requiring adaptation: In vivo genetic rescue approach → BBB-on-chip or ex vivo systems would require chemical or siRNA-based replication
- Model, species, tissue, matrix, platform, or scale mismatch: Mouse in vivo BBB; direct translation to human or to TBI context requires validation; TBI may activate distinct transcytosis pathways
- Assumptions required for transfer: Age-related TGF-β1-driven transcytosis is conserved across species and overlaps with injury-driven BBB dysfunction
- Confidence: moderate (abstract clearly states mechanism and rescue; Neuron publication implies rigorous validation; full text needed for quantitative details)

# Practical implications
- Experimental implication: Caveolin-1 and Mfsd2a are mechanistic targets to modulate in BBB integrity assays; midlife age point is the relevant intervention window; TGF-β1 inhibitors could be tested in BBB-on-chip models
- Analysis implication: Unknown
- Public dataset implication: Unknown — RNA-seq or imaging data may be deposited
- Biomarker or translational implication: Caveolin-1 and Mfsd2a expression in endothelial cells as markers of age-related BBB dysfunction; TGF-β1 as upstream serum/CSF biomarker candidate
- Grant or manuscript implication: Supports mechanistic framing of BBB failure in aging-related neurodegeneration grants; TGF-β1 pathway as a molecular link between aging and neurodegeneration risk

# Contradictions and links
- Supports: chen_2025_bbb-on-chip-shear-astrogliosis.md (BBB integrity under mechanical/inflammatory stress); trivedi_2026_dried-platelet-bbb-repair-tbi.md (BBB repair after TBI)
- Contradicts: Nothing in current library; prior models emphasizing tight junction disruption as primary mechanism
- Replicates: Unknown
- Methodologically comparable papers: chen_2025_bbb-on-chip-shear-astrogliosis.md (BBB models)
- Relevant synthesis notes: None yet
- Relevant project decisions: None yet

# Follow-up actions
- [ ] Retrieve full text when available in PMC or via institutional access
- [ ] Confirm mouse model (strain, sex, age range for "midlife")
- [ ] Check for RNA-seq data accession and imaging datasets
- [ ] Determine whether TGF-β1 inhibitor experiment is included
- [ ] Add to synthesis on BBB integrity mechanisms in aging and TBI

# Priority decision
- Priority: 1
- Read now
- Rationale: Establishes causal transcytosis mechanism for age-related BBB leakage with genetic rescue — directly relevant to BBB mechanobiology and TBI research in the library; changes interpretation of age-related BBB dysfunction from structural (tight junctions) to functional (transcytosis)
