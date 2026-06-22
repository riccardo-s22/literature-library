---
record_type: paper
record_status: verified
canonical_id: "10.1002/advs.202508271"
doi: "10.1002/advs.202508271"
pmid: "40867058"
pmcid: "PMC12631881"
title: "Shear Conditioning Promotes Microvascular Endothelial Barrier Resilience in a Human BBB-on-a-Chip Model of Systemic Inflammation Leading to Astrogliosis"
year: 2025
source_type: primary
peer_reviewed: true
full_text_checked: true
supplement_checked: false
code_checked: false
data_checked: false
last_verified: 2026-06-22
priority: 2
projects: []
topics: [mechanobiology, neurodegeneration, TBI, iPSC]
methods: [iPSC, ex_vivo, imaging, controlled_exposure]
datasets: []
---

# Citation
- Full citation: Chen K, Linares IM, Trempel MA, Feidler AM, De Silva D, Farajollahi S, Jones J, Kuebel J, Kasap P, Engelhardt B, Flax J, Abhyankar VV, Waugh RE, Gelbard HA, Terrando N, McGrath JL. "Shear Conditioning Promotes Microvascular Endothelial Barrier Resilience in a Human BBB-on-a-Chip Model of Systemic Inflammation Leading to Astrogliosis." *Advanced Science* 2025;12(43):e08271.
- DOI / PMID / stable URL: [DOI](https://doi.org/10.1002/advs.202508271) · PMID 40867058 · PMC12631881
- Related preprint or published version: Peer-reviewed (Adv Sci), open access.
- Correction, expression of concern, or retraction status: **Unknown** — not checked (added 2026-06-22).

*Source: metadata + PMC full text retrieved from PubMed / PubMed Central. According to PubMed, DOI [10.1002/advs.202508271](https://doi.org/10.1002/advs.202508271).*

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: A **human BBB-on-a-chip (µSiM) under calibrated fluid shear** showing that shear preconditioning (0.5 Pa, 48 h) makes the endothelial barrier more resilient to circulating inflammation, and that astrocyte activation (astrogliosis) requires **fibrinogen** in addition to high-dose cytokines. Directly relevant to mechanobiology of barriers under load and to TBI-relevant fibrinogen-driven astrogliosis. Strong **device/protocol precedent** for barrier-under-flow modeling with glial readouts.
- Why it is more or less useful than neighboring literature: Quantifies a specific, physiologically-grounded shear regime (post-capillary venule range 0.1–0.6 Pa) and isolates fibrinogen as the trigger for astrogliosis — a mechanistically clean, reproducible model. More controlled than static BBB models; less complex than full neurovascular-unit chips. Limitation: monoculture/coculture (not full NVU), and the key permeability reduction is significant only at p < 0.1.

# Source inspection status
- Abstract inspected: yes
- Full text inspected: yes (PMC full text, ~73k chars)
- Methods inspected: yes (device, cell differentiation, shear setup, inflammatory challenges, COMSOL validation)
- Supplement inspected: no (Supporting Information referenced)
- Figures/tables inspected: no (callouts read; panels not viewed)
- Code repository inspected: no (COMSOL model used; no code repo noted)
- Data repository inspected: no (no explicit data-availability/accession found in retrieved text)
- Missing material: exact n per condition (some in figure legends), supplementary methods, formal data-availability statement.

# Study question and hypothesis
- Primary question: Does endothelial shear preconditioning alter human BBB barrier resilience to systemic inflammation, and what circulating factors drive downstream astrocyte activation?
- Stated hypothesis: Physiological shear stress conditions brain microvascular endothelium toward a resilient, anti-inflammatory phenotype; astrogliosis downstream requires factors beyond cytokines alone (fibrinogen).
- Study type: Controlled in vitro microphysiological (organ-chip) experiment; shear-conditioned vs static; dose-response inflammatory challenge ± fibrinogen.

# Biological or clinical context
- Disease / exposure / process: Systemic inflammation → BBB dysfunction → neuroinflammation/astrogliosis (relevant to sepsis-associated encephalopathy and TBI).
- Organism: Human.
- Tissue / cell type: Brain microvascular endothelial-like cells (EECM-BMECs from IMR90-4 hiPSC) in apical channel; primary human astrocytes (PHAs) in basolateral "brain" compartment.
- Model system: µSiM-BBB (microphysiological system with ultrathin 100 nm silicon nanomembrane) + fluidic insert (closed microfluidic).
- Cohort or population: N/A (cell-based; single hiPSC line IMR90-4).
- Relevant stage, age, sex, genotype, severity: EECM-BMECs used passages 4–6.

# Study design
- Experimental or observational unit: Individual µSiM chip / device replicate.
- Unit of inference: Per-condition (static vs shear; ± cytomix dose; ± fibrinogen).
- Groups and sample size per group: Static vs shear-conditioned; low-dose cytomix (10 pg/mL) vs high-dose (50 pg/mL); ± fibrinogen. Exact n per condition in figure legends (not fully extracted).
- Biological replicates: Multiple device replicates (count Unknown; lower SD reported for shear).
- Technical replicates: Not separately extracted.
- Randomization / blinding: Not described.
- Inclusion / exclusion criteria: Not described.
- Batch structure: Single hiPSC line; differentiation batches not detailed.
- Longitudinal / paired / donor structure: 48 h shear conditioning; challenge timepoints; 6 h de-alignment assay.
- Controls and comparators: Static culture; vehicle; phase-contrast monolayer-continuity checks; monoculture astrocyte cytokine-resistance control.

# Experimental methods
- Assay / platform: µSiM-BBB on ultrathin (100 nm) optically-clear silicon nanomembrane; modular fluidic insert converts static → closed microfluidic. Readouts: small-tracer permeability, EC alignment, glycocalyx (HA) expression, ICAM-1, neutrophil transmigration, astrocyte GFAP morphology (hypertrophy/process elongation). COMSOL used to validate tracer retention/shear.
- Sample preparation: IMR90-4 hiPSC (WiCell) → EPCs over 3 days → CD31+ MACS isolation → EECM-BMEC expansion in hECSR (hESFM + B-27 + 20 ng/mL bFGF-2 + pen/strep); seeded at 2×10⁶ cells/mL (40,000 cells/cm²) on collagen IV (400 µg/mL) / fibronectin (100 µg/mL)-coated channels.
- Dose, concentration, force, exposure, or perturbation: **Wall shear stress 0.5 Pa (5 dyne/cm²), 48 h** (high end of post-capillary venule range 0.1–0.6 Pa). Cytomix = TNF-α/IL-1β/IFN-γ at 10 pg/mL (low/early sepsis) and 50 pg/mL (severe). Fibrinogen added as additional circulating factor.
- Timing / sampling schedule: 48 h shear preconditioning; inflammatory challenge post-conditioning; 6 h de-alignment assay timepoint.
- Matrix / conditions: 37 °C, 5% CO₂; collagen IV/fibronectin coating; PDMS inserts.
- Primary endpoint: Barrier permeability under static vs shear, ± inflammatory challenge.
- Secondary endpoints: EC alignment, glycocalyx, ICAM-1, neutrophil transmigration; astrocyte GFAP activation ± fibrinogen.
- QC criteria: Phase-contrast monolayer continuity; barrier reproducibility (SD as % of mean).
- Failure or exclusion criteria: Not described.
- Exact reusable parameters and source location: Shear regime (0.5 Pa/48 h), cytomix doses (10 vs 50 pg/mL), differentiation protocol, coating concentrations — all in Methods/Results.

# Computational and statistical methods
- Raw input: Permeability measurements, imaging (alignment, GFAP, glycocalyx), transmigration counts.
- Preprocessing: Standard; COMSOL simulation for tracer retention/shear validation.
- Statistical test or model: Group comparisons (test not fully extracted); significance reported at p < 0.05, p < 0.1, p < 0.001 thresholds.
- Multiple-testing correction: Not described in retrieved text.
- Effect-size reporting: Permeability reduction with shear significant only at p < 0.1 (not p < 0.05); low-dose challenge: shear stays tight, static leaks (p < 0.001); high-dose disrupts both.
- Batch handling: Not detailed.
- Validation strategy: COMSOL physical validation of shear/tracer; internal dose-response and ± fibrinogen contrasts; monoculture astrocyte control.
- External validation: Conceptual alignment with clinical fibrinogen-leak astrogliosis.
- Software and versions: COMSOL (version Unknown); imaging/analysis software not extracted.
- Code availability: Not stated (COMSOL model).

# Data and resource availability
- Repository and accession: No explicit data-availability statement or accession found in retrieved text (model/device study; data likely in figures/supplement).
- Raw data available: Unknown (no accession).
- Processed data available: Unknown.
- Metadata completeness: N/A (no deposited dataset).
- Data-use restrictions: N/A.
- Reusability for the user's work: **High as a protocol/platform**; not a reusable public dataset.

# Main findings
| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| Shear (0.5 Pa, 48 h) aligns ECs, lowers baseline permeability, increases glycocalyx | Reported | Results / Fig | permeability ↓ (sig at p<0.1, not p<0.05); lower SD | Partial | Permeability effect only p<0.1 |
| Shear-conditioned barriers resist low-dose (10 pg/mL) cytomix; static barriers leak | Reported | Results / Fig | static leaks vs shear tight (p<0.001) | Yes | — |
| High-dose (50 pg/mL) cytomix disrupts even shear-conditioned barriers | Reported | Results | barrier breakdown | Yes | — |
| Shear reduces inflammatory ICAM-1 upregulation and neutrophil transmigration | Reported | Results | reduced responses | Yes | counts in figures |
| High-dose cytomix alone fails to activate primary human astrocytes | Reported | Results | no GFAP activation | Yes | astrocytes cytokine-resistant |
| Fibrinogen + high-dose cytomix triggers astrocyte activation (astrogliosis) | Reported | Results / Fig | GFAP morphological activation | Yes | mirrors clinical fibrinogen leak |

# What is actually new?
- Biological novelty: Fibrinogen is the necessary co-factor (with cytokines) for astrogliosis in this human BBB model; astrocytes are otherwise cytokine-resistant.
- Methodological novelty: First flow/shear-based experiments in the µSiM-BBB; integration of calibrated shear conditioning with downstream glial sensing.
- Dataset or resource novelty: Reusable shear-BBB-on-chip protocol (not a deposited dataset).
- What was already known: Shear conditioning improves EC barrier/anti-inflammatory phenotype (eNOS, KLF2/4, glycocalyx); static models overestimate adhesion.

# Strengths
- Design strength: Calibrated, physiologically-grounded shear regime; dose-response; clean isolation of fibrinogen as astrogliosis trigger; static vs shear controls.
- Validation strength: COMSOL physical validation; monoculture astrocyte cytokine-resistance control; phase-contrast monolayer QC.
- Reproducibility strength: Detailed differentiation + device protocols; shear improved reproducibility (lower SD).
- Translational realism: Human hiPSC endothelium + primary human astrocytes; venule-range shear; fibrinogen relevance to TBI.

# Limitations and bias risks
- Sample-size / power: Key permeability reduction only p < 0.1; exact n per condition not fully extracted.
- Confounding: Single hiPSC line (IMR90-4); monoculture/coculture, not full NVU (no pericytes/neurons).
- Batch / site effects: Differentiation-batch effects not characterized.
- Pseudoreplication risk: Device-replicate definition not fully extracted.
- Leakage / overfitting risk: N/A.
- Generalizability: One endothelial source; specific shear value; in vitro.
- Missing controls / validation: No multi-donor endothelium; no in-vivo cross-validation.
- Author-stated limitations: Model is a foundation for more complete NVU models (acknowledged).
- Additional limitations identified during review: No explicit data-availability statement/accession; stats test not fully specified in retrieved text.

# Transferability to the user's work
- Directly transferable elements: Shear-conditioning protocol (0.5 Pa/48 h); cytomix dose tiers; fibrinogen-driven astrogliosis assay; EECM-BMEC differentiation + µSiM device setup; COMSOL shear validation approach.
- Elements requiring adaptation: Adding pericytes/neurons for full NVU; mechanical-injury (vs inflammatory) loading if modeling TBI directly.
- Model, species, tissue, matrix, platform, or scale mismatch: Inflammatory/shear model vs direct mechanical TBI; coculture vs full NVU.
- Assumptions required for transfer: Access to µSiM platform and hiPSC differentiation capacity.
- Confidence: moderate-high for protocol reuse.

# Practical implications
- Experimental implication: Use shear preconditioning and report exact wall shear stress; include fibrinogen when modeling astrogliosis from barrier breakdown (relevant to blast/TBI).
- Analysis implication: Pre-register barrier-permeability significance thresholds (note p<0.1 result here).
- Public dataset implication: No deposited dataset.
- Biomarker / translational implication: Fibrinogen leak as a mechanistic driver of astrogliosis.
- Grant / manuscript implication: Citable human BBB-under-flow platform linking systemic inflammation to glial activation.

# Contradictions and links
- Supports: Shear improves EC barrier/anti-inflammatory phenotype; fibrinogen as astrogliosis trigger (clinical literature).
- Contradicts: Static-model assumption that cytokines alone drive astrogliosis (astrocytes here are cytokine-resistant without fibrinogen).
- Replicates: Prior shear-conditioning EC benefits.
- Methodologically comparable papers: Sirtori 2025 / Silvosa 2022 (organoid mechanical injury — different loading modality); Braun 2021 (calibrated neural stretch).
- Relevant synthesis notes: candidate for "barriers under mechanical/inflammatory load → glial state" synthesis.
- Relevant project decisions: (none yet)

# Follow-up actions
- [ ] Extract exact n per condition and stat tests from figure legends/supplement
- [ ] Confirm whether any data/code are deposited
- [ ] Cross-link to TBI/blast injury records (fibrinogen-astrogliosis axis)
- [ ] Check retraction/correction status

# Priority decision
- Priority: 2
- Retain for methods + mechanism
- Rationale: Well-controlled human BBB-under-shear platform with a clean fibrinogen-astrogliosis mechanism, directly useful as a barrier-mechanobiology protocol; Priority 2 because it is a model/device study (no deposited dataset) and the headline permeability effect is only p<0.1.
