---
record_type: paper
record_status: needs_full_text
canonical_id: "10.1016/j.cell.2026.07.045"
doi: "10.1016/j.cell.2026.07.045"
pmid: "42612631"
title: "Multimodal brain cell atlas across the adult macaque lifespan"
year: 2026
source_type: resource
peer_reviewed: true
full_text_checked: false
supplement_checked: false
code_checked: false
data_checked: false
last_verified: 2026-09-01
priority: 2
projects: []
topics: [transcriptomics, single_cell, multi_omics, neurodegeneration, aging]
methods: [snRNAseq, snATACseq, analysis_method]
datasets: []
---

# Citation
- Full citation: Zhang et al. (2026). Multimodal brain cell atlas across the adult macaque lifespan. *Cell*. https://doi.org/10.1016/j.cell.2026.07.045
- DOI / PMID / stable URL: 10.1016/j.cell.2026.07.045 / PMID 42612631
- Related preprint or published version: Unknown
- Correction, expression of concern, or retraction status: None as of 2026-09-01

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Provides a comprehensive transcriptomic and chromatin accessibility atlas of 2,955,873 nuclei from 8 brain regions across 23 female cynomolgus macaques spanning the adult lifespan. Critical reference resource for aging-associated gene expression and chromatin changes in non-human primate brain — directly relevant to extrapolation from primate aging to human neurodegeneration.
- Why it is more or less useful than neighboring literature: NHP atlases are rare and highly valuable for species-translation of human aging/neurodegeneration findings; 8-region coverage + dual modality (snRNA-seq + snATAC-seq) + lifespan design makes this a unique reference layer. Larger and multi-modal compared to previous NHP single-cell atlases.

# Source inspection status
- Abstract inspected: Yes
- Full text inspected: No
- Methods inspected: No
- Supplement inspected: No
- Figures/tables inspected: No
- Code repository inspected: No
- Data repository inspected: No
- Missing material: Data accession, library preparation platform, cell type annotations, age range of animals, brain regions profiled, chromatin accessibility analysis approach

# Study question and hypothesis
- Primary question: How do transcriptomic and chromatin accessibility profiles of brain cells change across the adult macaque lifespan?
- Stated hypothesis: Brain cell types show age-associated molecular changes that parallel human neurodegeneration
- Study type: Atlas / resource; cross-sectional lifespan design in NHP

# Biological or clinical context
- Disease / exposure / process: Brain aging; neurodegeneration relevance (aging as risk factor)
- Organism: Cynomolgus macaque (Macaca fascicularis)
- Tissue / cell type: 8 brain regions (specific regions Unknown); all major cell types expected
- Model system: Non-human primate (adult female cynomolgus macaque, n=23)
- Cohort or population: 23 female cynomolgus macaques; age range Unknown (adults spanning lifespan)
- Relevant stage, age, sex, genotype, or disease severity: Adult lifespan (specific range Unknown); all female (sex limitation)

# Study design
- Experimental or observational unit: Single nucleus
- Unit of inference: Cell type × brain region × age; 2,955,873 total nuclei
- Groups and sample size per group: 23 animals across lifespan; 8 brain regions; per-animal and per-region counts Unknown
- Biological replicates: 23 individual macaques (biological replicates at animal level)
- Technical replicates: Unknown
- Randomization: Not applicable (observational)
- Blinding: Not applicable
- Inclusion / exclusion criteria: Unknown
- Batch structure: 23 animals likely processed in batches; batch correction Unknown
- Longitudinal, repeated-measures, paired, or donor structure: Cross-sectional lifespan design (not longitudinal within animals)
- Controls and comparators: Age as continuous covariate; no disease condition

# Experimental methods
- Assay / platform: snRNA-seq + snATAC-seq (specific platforms Unknown); 8 brain regions
- Sample preparation: Unknown — tissue dissection of 8 regions, nuclei isolation
- Dose, concentration, force, exposure, or perturbation: Not applicable
- Timing and sampling schedule: Single postmortem time point per animal
- Matrix / medium / substrate / environmental conditions: Flash-frozen or FFPE brain tissue Unknown
- Primary endpoint: Age-associated cell-type-resolved transcriptomic and chromatin accessibility changes
- Secondary endpoints: Unknown
- QC criteria: Unknown
- Failure or exclusion criteria: Unknown
- Exact reusable parameters and source location: Unknown — full text required

# Computational and statistical methods
- Raw input: snRNA-seq and snATAC-seq reads
- Preprocessing: Unknown
- Normalization: Unknown
- Feature filtering: Unknown
- Covariates and design formula: Age as continuous variable; brain region as factor; sex not variable (all female)
- Statistical test or model: Unknown — trajectory analysis likely; differential gene expression by age
- Multiple-testing correction: Unknown
- Effect-size reporting: Unknown
- Batch handling: Unknown
- Validation strategy: Unknown — internal replication across brain regions likely
- External validation: Unknown
- Software and versions: Unknown
- Code availability: Unknown

# Data and resource availability
- Repository and accession: Unknown — atlas resource likely deposited at CNCB, NCBI, or Allen Brain Cell Atlas
- Raw data available: Unknown
- Processed data available: Unknown — likely interactive browser for atlas-class papers in Cell
- Metadata completeness: Unknown
- Data-use restrictions: Unknown
- Reusability for the user's work: High value as a NHP aging reference atlas for cross-species comparison with human neurodegenerative datasets; snRNA-seq and snATAC-seq layers separately usable

# Main findings
| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| Comprehensive NHP brain atlas: 2,955,873 nuclei from 8 regions, 23 female macaques | Reported (abstract) | Unknown | 2,955,873 nuclei | Yes (abstract) | All female — male aging biology not captured |
| Molecular basis of brain aging investigated via transcriptomics + chromatin accessibility | Reported (abstract) | Unknown | Unknown | Unknown | Abstract only; specific aging changes Unknown |

# What is actually new?
- Biological novelty: Multi-region, lifespan-spanning NHP brain atlas with dual omics modality; aging-associated molecular characterization at cell-type resolution
- Methodological novelty: Multimodal (snRNA-seq + snATAC-seq) 8-region NHP atlas at this scale
- Dataset or resource novelty: Largest multimodal NHP brain cell atlas to date (2.9M+ nuclei, 8 regions)
- What was already known: Single-region NHP atlases; human aging snRNA-seq atlases; marmoset and macaque single-cell references for specific regions

# Strengths
- Design strength: 23 animals × 8 regions × 2 modalities; large N for NHP; adult lifespan coverage
- Validation strength: Unknown
- Reproducibility strength: Atlas-class dataset; likely full data deposit
- Translational or ecological realism: Cynomolgus macaque is the most translationally relevant NHP model for human aging; 8-region coverage spans motor, cognitive, and limbic areas

# Limitations and bias risks
- Sample-size or power limitation: 23 animals limits statistical power for trajectory modeling of rare cell types
- Confounding: All female — sex × age interactions not assessable
- Batch or site effects: 23 animals likely processed in batches; batch correction critical
- Pseudoreplication risk: Per-cell analyses must account for donor structure
- Leakage or overfitting risk: Unknown
- Generalizability limitation: Female-only design; one macaque species; cross-species translation to humans requires validation
- Missing controls: No disease model; limited to aging
- Missing validation: Unknown
- Author-stated limitations: Unknown
- Additional limitations identified during review: All female; cross-sectional (not longitudinal)

# Transferability to the user's work
- Directly transferable elements: Reference atlas for cross-species mapping; snRNA-seq cell-type annotations for 8 brain regions; aging trajectory as reference for disease-associated changes
- Elements requiring adaptation: Species translation (macaque → human) requires orthology mapping and validation
- Model, species, tissue, matrix, platform, or scale mismatch: NHP ≠ human; disease-relevant findings require human validation; all-female design may not capture sex-dimorphic aging patterns
- Assumptions required for transfer: Age-associated macaque molecular changes parallel human neurodegeneration preclinical states
- Confidence: moderate (atlas resource with clear scale; details pending full text)

# Practical implications
- Experimental implication: Use as reference atlas for cross-species snRNA-seq comparison; cell-type annotation of NHP datasets
- Analysis implication: Reference for label transfer from macaque to human brain cell types; aging trajectory baseline
- Public dataset implication: 2.9M nuclei dataset likely to be deposited — high value for reanalysis
- Biomarker or translational implication: Age-associated chromatin changes in macaque provide NHP validation layer for human aging biomarkers
- Grant or manuscript implication: Atlas as reference for NHP aging/neurodegeneration grant aims; supports translatability claims

# Contradictions and links
- Supports: castanho_2025_neuronal-resilience-alzheimer.md (aging × neurodegeneration); leng_2021_rorb-vulnerable-neurons-ad.md (neuronal vulnerability)
- Contradicts: Nothing in current library
- Replicates: Unknown — builds on prior single-region NHP atlases
- Methodologically comparable papers: ren_2026_stereo-seq-multiorgan-spatial-atlas.md (multi-organ atlas); li_2025_nephrobase-cell-plus-foundation-model.md (multi-modal atlas)
- Relevant synthesis notes: None yet
- Relevant project decisions: None yet

# Follow-up actions
- [ ] Retrieve full text for data accession, brain regions profiled, and age range of animals
- [ ] Confirm data deposit repository (CNCB, NCBI, Allen Brain)
- [ ] Evaluate for use as reference atlas in cross-species snRNA-seq comparisons
- [ ] Note sex limitation (female-only) when using for translational inferences

# Priority decision
- Priority: 2
- Retain for background
- Rationale: Largest multimodal NHP brain atlas spanning the adult lifespan; high reusability as reference for aging and neurodegeneration; full-text inspection needed to confirm data access
