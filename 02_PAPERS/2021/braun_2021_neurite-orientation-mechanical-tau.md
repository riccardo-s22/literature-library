---
record_type: paper
record_status: needs_full_text
canonical_id: "10.1016/j.bpj.2021.07.011"
doi: "10.1016/j.bpj.2021.07.011"
pmid: "34293301"
pmcid: "PMC8392125"
title: "Orientation of neurites influences severity of mechanically induced tau pathology"
year: 2021
source_type: primary
peer_reviewed: true
full_text_checked: false
supplement_checked: false
code_checked: false
data_checked: false
last_verified: 2026-06-22
priority: 2
projects: []
topics: [mechanobiology, TBI, neurodegeneration]
methods: [controlled_exposure, imaging, cell_line]
datasets: []
---

# Citation
- Full citation: Braun NJ, Liao D, Alford PW. "Orientation of neurites influences severity of mechanically induced tau pathology." *Biophysical Journal* 2021;120(16):3272-3282.
- DOI / PMID / stable URL: [DOI](https://doi.org/10.1016/j.bpj.2021.07.011) · PMID 34293301 · PMC8392125
- Related preprint or published version: Peer-reviewed (Biophys J).
- Correction, expression of concern, or retraction status: **Unknown** — not checked (added 2026-06-22).

*Source: metadata + abstract retrieved from PubMed; PMC full text was EMPTY (abstract only), and the publisher full text returned HTTP 403. According to PubMed, DOI [10.1016/j.bpj.2021.07.011](https://doi.org/10.1016/j.bpj.2021.07.011).*

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Demonstrates with a **calibrated in vitro simulated-TBI stretch device** that the direction of high-strain-rate uniaxial stretch *relative to neurite alignment* — not bulk strain magnitude alone — governs mechanically-induced tau mislocalization and synaptic dysfunction. Directly relevant to mechanobiology of neural injury: argues that **neurite work/energy density** is a better injury metric than deformation magnitude. Supports calibrated-force experimental design and an architecture-aware injury readout.
- Why it is more or less useful than neighboring literature: Couples a controlled mechanical injury device with microfabricated neurite alignment and functional electrophysiology (mEPSC) + tau localization — a tighter mechanics-to-pathology link than overpressure-only models. Complements organoid blast models (Sirtori 2025; Silvosa 2022) by providing single-neuron-architecture resolution. Limitation: in vitro 2D culture; full Methods/parameters not yet inspected.

# Source inspection status
- Abstract inspected: yes
- Full text inspected: no (PMC full_text empty; publisher 403)
- Methods inspected: no
- Supplement inspected: no
- Figures/tables inspected: no
- Code repository inspected: no
- Data repository inspected: no
- Missing material: exact strain magnitude (%), strain rate (s^-1), calibration method, cell source/species, microfabrication parameters, sample sizes, viscoelastic-model constants, statistics, data/code availability — ALL Unknown pending full text.

# Study question and hypothesis
- Primary question: How does neuronal/neurite orientation relative to the direction of a uniaxial high-strain-rate stretch influence early-stage mechanically-induced tau pathology and synaptic function?
- Stated hypothesis: Deformation relative to local neuronal architecture (and neurite mechanical energy) predicts trauma-induced tauopathy better than bulk deformation magnitude.
- Study type: Controlled in vitro mechanical-injury experiment (case = parallel stretch vs comparator = perpendicular stretch), with biophysical modeling.

# Biological or clinical context
- Disease / exposure / process: Chronic traumatic encephalopathy (CTE) / repeated TBI; tauopathy (tau mislocalization to dendritic spines).
- Organism: **Unknown** (likely primary rodent cortical/hippocampal neurons — not confirmed from abstract).
- Tissue / cell type: Cultured neurons with controlled neurite alignment (cell type/species Unknown).
- Model system: 2D in vitro neuronal culture on microfabricated constructs + in vitro simulated-TBI stretch device.
- Cohort or population: N/A (cell culture).
- Relevant stage, age, sex, genotype, severity: **Unknown**.

# Study design
- Experimental or observational unit: Cultured neuron / culture construct (Unknown replicate definition).
- Unit of inference: Per-condition (parallel vs perpendicular stretch).
- Groups and sample size per group: **Unknown** (full text not inspected).
- Biological replicates: **Unknown**.
- Technical replicates: **Unknown**.
- Randomization / blinding: **Unknown**.
- Inclusion / exclusion criteria: **Unknown**.
- Batch structure: **Unknown**.
- Controls and comparators: Same strain applied parallel vs perpendicular to neurite alignment; injured vs uninjured implied.

# Experimental methods
- Assay / platform: Microfabricated cell-culture constructs to control neurite growth direction; in vitro simulated-TBI device applying controlled uniaxial high-strain-rate stretch; readouts = tau localization imaging + whole-cell electrophysiology (mEPSC amplitude).
- Sample preparation: **Unknown**.
- Dose / force / perturbation: Uniaxial high-strain-rate stretch; exact strain (%) and strain rate (s^-1) **Unknown** (described qualitatively as "high-strain-rate"; same strain across both orientations).
- Timing / sampling schedule: **Unknown**.
- Matrix / conditions: Microfabricated alignment substrate; details **Unknown**.
- Primary endpoint: Tau mislocalization to dendritic spines as a function of stretch direction.
- Secondary endpoints: mEPSC amplitude (synaptic function).
- QC / failure criteria: **Unknown**.
- Exact reusable parameters and source location: **Unknown** — to extract from full text (strain, strain rate, viscoelastic constants, alignment geometry).

# Computational and statistical methods
- Raw input: Imaging (tau localization), electrophysiology (mEPSC), mechanical injury parameters.
- Preprocessing / model: Experimental injury parameters (strain, strain rate, direction) combined with a **standard viscoelastic solid model**; **neurite work density** during stretch computed and correlated with tau mislocalization.
- Statistical test or model: **Unknown** (not inspected).
- Multiple-testing correction: **Unknown**.
- Effect-size reporting: Qualitative from abstract (parallel > perpendicular for tau mislocalization and mEPSC loss).
- Validation strategy: Internal correlation of neurite work density with pathology.
- External validation: **Unknown**.
- Software and versions: **Unknown**.
- Code availability: **Unknown**.

# Data and resource availability
- Repository and accession: **Unknown** (not inspected).
- Raw data available: **Unknown**.
- Processed data available: **Unknown**.
- Metadata completeness: **Unknown**.
- Data-use restrictions: **Unknown**.
- Reusability for the user's work: Conceptually high (architecture-aware injury metric); reusability of exact device parameters pending full-text inspection.

# Main findings
| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| Stretch parallel to neurite alignment causes greater tau mislocalization to dendritic spines than perpendicular stretch at equal strain | Reported | Abstract | qualitative (parallel > perpendicular) | Yes | Effect size not extracted (full text not seen) |
| Synaptic function (mEPSC amplitude) decreases with parallel stretch but little/no loss with perpendicular | Reported | Abstract | qualitative | Yes | Quantitative values Unknown |
| Neurite work density during stretch correlates with tau mislocalization (better predictor than bulk strain) | Reported/Derived | Abstract | correlation via viscoelastic model | Partial | Model constants/stats not inspected |

# What is actually new?
- Biological novelty: Neuronal architecture (neurite orientation) modulates mechanically-induced tauopathy at equal strain.
- Methodological novelty: Combining microfabricated neurite alignment + calibrated stretch device + viscoelastic energy modeling to define a mechanics-based injury metric (neurite work density).
- Dataset or resource novelty: **Unknown** (data availability not inspected).
- What was already known: Mechanical force alone can induce tau mislocalization and synaptic loss in randomly-organized cultures (authors' prior work).

# Strengths
- Design strength: Controlled comparison of stretch direction at matched strain; functional + molecular readouts.
- Validation strength: Mechanistic energy-based metric correlated with pathology.
- Reproducibility strength: **Unknown** (parameters not inspected).
- Translational realism: Models aligned neurite architecture (more brain-like than random cultures), though still 2D in vitro.

# Limitations and bias risks
- Sample-size / power: **Unknown** (full text not seen).
- Confounding: 2D culture vs 3D tissue mechanics.
- Batch / site effects: **Unknown**.
- Pseudoreplication risk: **Unknown** — confirm replicate definition.
- Leakage / overfitting risk: N/A (mechanistic model).
- Generalizability: In vitro 2D aligned neurons; species/cell type Unknown.
- Missing controls / validation: **Unknown** pending full text.
- Author-stated limitations: **Unknown** (not inspected).
- Additional limitations identified during review: Could not access Methods — all quantitative injury parameters remain Unknown.

# Transferability to the user's work
- Directly transferable elements: Concept that injury direction relative to neural architecture and neurite work density predict pathology — informs how to report/interpret calibrated injury in organoid/2D models (cf. Sirtori 2025 free-floating loading variability).
- Elements requiring adaptation: Exact device/strain parameters (pending extraction); 2D-to-3D translation.
- Model, species, tissue, matrix, platform, or scale mismatch: 2D aligned culture vs 3D organoid/tissue.
- Assumptions required for transfer: Comparable strain-rate regime; ability to control/measure local architecture.
- Confidence: low-moderate (abstract-only inspection).

# Practical implications
- Experimental implication: Report stretch/pressure *direction relative to tissue architecture* and estimate local mechanical energy, not just bulk strain — relevant for designing/interpreting calibrated injury experiments.
- Analysis implication: Consider neurite/strain-energy metrics as injury covariates.
- Public dataset implication: **Unknown**.
- Biomarker / translational implication: Architecture-dependent tau mislocalization as an injury severity correlate.
- Grant / manuscript implication: Supports the argument that bulk deformation under-predicts neurodegenerative risk.

# Contradictions and links
- Supports: Mechanical force → tau pathology (extends authors' prior random-culture work); architecture-aware injury metrics.
- Contradicts: Implicitly challenges bulk-strain-only injury thresholds.
- Replicates: Authors' earlier force-induced tau mislocalization finding, now with alignment control.
- Methodologically comparable papers: Sirtori 2025 (organoid blast, free-floating loading variability); Silvosa 2022 (organoid overpressure neurophysiology); Ruf 2026 / Leng 2021 (tau/TDP-43 cell-type readouts).
- Relevant synthesis notes: candidate for "calibrated mechanical injury → tau/TDP-43 proteinopathy" synthesis (architecture axis).
- Relevant project decisions: (none yet)

# Follow-up actions
- [ ] Obtain full text (institutional access / author copy) to extract strain %, strain rate, device, cell source, sample sizes, viscoelastic constants, statistics, data availability
- [ ] Re-classify record_status to verified once Methods inspected
- [ ] Cross-link with Sirtori 2025 and Silvosa 2022 in a mechanobiology synthesis
- [ ] Check retraction/correction status

# Priority decision
- Priority: 2
- Retain for methods (pending full-text verification)
- Rationale: Conceptually important calibrated-injury mechanobiology paper linking deformation geometry to tauopathy; downgraded operational confidence because only the abstract could be inspected (PMC empty, publisher 403). Resolve by obtaining the full text.
