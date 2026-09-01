---
record_type: paper
record_status: needs_full_text
canonical_id: "10.1021/acsnano.6c07740"
doi: "10.1021/acsnano.6c07740"
pmid: "42503866"
title: "A Dual-Readout Near-Infrared Fluorescent Fiber Probe for High Spatiotemporal Resolution Neurotransmitter Mapping"
year: 2026
source_type: primary
peer_reviewed: true
full_text_checked: false
supplement_checked: false
code_checked: false
data_checked: false
last_verified: 2026-09-01
priority: 2
projects: []
topics: [biosensors, nanomaterials, neurodegeneration]
methods: [spectroscopy, imaging]
datasets: []
---

# Citation
- Full citation: Shin S et al. (2026). A Dual-Readout Near-Infrared Fluorescent Fiber Probe for High Spatiotemporal Resolution Neurotransmitter Mapping. *ACS Nano*. https://doi.org/10.1021/acsnano.6c07740
- DOI / PMID / stable URL: 10.1021/acsnano.6c07740 / PMID 42503866
- Related preprint or published version: Unknown
- Correction, expression of concern, or retraction status: None as of 2026-09-01

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Introduces the NeuRIFI platform: DNA-functionalized SWCNT nanosensors on implantable optical fibers for simultaneous fiber photometry (point measurement) and wide-field NIR imaging (spatial mapping) of dopamine in deep brain tissue. Directly extends SWCNT NIR sensing to in situ neurochemical imaging with high spatiotemporal resolution.
- Why it is more or less useful than neighboring literature: Unlike prior SWCNT sensors validated only in buffer or synthetic biofluids, NeuRIFI is validated in tissue phantoms and ex vivo mouse brain at 3 mm depth. The dual-readout architecture (photometry + remote NIR imaging) simultaneously provides quantitative point validation and spatially resolved dopamine flux — a significant technical advance over single-readout SWCNT systems.

# Source inspection status
- Abstract inspected: Yes
- Full text inspected: No (no PMC access; abstract from PubMed)
- Methods inspected: No
- Supplement inspected: No
- Figures/tables inspected: No
- Code repository inspected: No
- Data repository inspected: No
- Missing material: Full methods, fiber functionalization protocol, SWCNT dispersion parameters, ex vivo brain preparation details, imaging setup, statistical analysis

# Study question and hypothesis
- Primary question: Can DNA-SWCNT-functionalized implantable optical fibers provide simultaneous photometric and spatially resolved NIR imaging of dopamine in deep brain tissue?
- Stated hypothesis: Dual-readout architecture combining fiber photometry (validation) and NIR camera imaging (spatial mapping) enables high-resolution neurotransmitter mapping at tissue depth
- Study type: Instrumentation/sensor development with ex vivo biological validation

# Biological or clinical context
- Disease / exposure / process: Dopamine neuromodulation; volume transmission; neurochemical mapping (relevant to Parkinson's disease and dopaminergic circuit research)
- Organism: Mouse (ex vivo brain); tissue phantoms
- Tissue / cell type: Deep brain tissue; ex vivo mouse brain (3 mm depth)
- Model system: Tissue phantoms; ex vivo mouse brain
- Cohort or population: Not applicable (ex vivo validation)
- Relevant stage, age, sex, genotype, or disease severity: Unknown (ex vivo model — mouse strain, age, sex not stated in abstract)

# Study design
- Experimental or observational unit: Fiber probe + brain tissue preparation
- Unit of inference: Dopamine flux mapping at defined spatiotemporal resolution
- Groups and sample size per group: Unknown — ex vivo preparations N Unknown
- Biological replicates: Unknown
- Technical replicates: Unknown
- Randomization: Unknown
- Blinding: Not applicable
- Inclusion / exclusion criteria: Unknown
- Batch structure: Unknown
- Longitudinal, repeated-measures, paired, or donor structure: Unknown (likely acute ex vivo sessions)
- Controls and comparators: Unknown — dopamine concentration standards in tissue phantoms (inferred)

# Experimental methods
- Assay / platform: DNA-SWCNT-functionalized implantable optical fiber; dual-readout NIR system (fiber photometry channel + remote NIR camera channel); frame-by-frame intensity derivative analysis for transient flux
- Sample preparation: Unknown — optical fiber functionalization with DNA-SWCNT; ex vivo mouse brain preparation Unknown
- Dose, concentration, force, exposure, or perturbation: Dopamine (concentration range Unknown); sensor validated at 90 nM minimum detection
- Timing and sampling schedule: Transient DA flux at 20 ms temporal resolution
- Matrix / medium / substrate / environmental conditions: Tissue phantoms; ex vivo mouse brain (3 mm depth)
- Primary endpoint: Spatiotemporal resolution of dopamine detection: 90 nM sensitivity, 20 ms temporal resolution, ~1.5 μm/pixel spatial resolution
- Secondary endpoints: Deep-brain signal acquisition reliability; photometric vs. imaging channel agreement
- QC criteria: Unknown
- Failure or exclusion criteria: Unknown
- Exact reusable parameters and source location: 90 nM DA sensitivity; 20 ms temporal resolution; ~1.5 μm/pixel spatial; 3 mm tissue depth; DNA-SWCNT (specific DNA sequence and chirality Unknown — full text required); NIR fluorescence emission within tissue-transparent window (900–1600 nm range inferred)

# Computational and statistical methods
- Raw input: NIR fluorescence image sequences (frame-by-frame)
- Preprocessing: Frame-to-frame intensity derivative for transient DA flux
- Normalization: Unknown
- Feature filtering: Unknown
- Covariates and design formula: Unknown
- Statistical test or model: Unknown
- Multiple-testing correction: Unknown
- Effect-size reporting: Detection sensitivity (90 nM), temporal resolution (20 ms), spatial resolution (~1.5 μm/pixel) — Reported
- Batch handling: Unknown
- Validation strategy: Tissue phantoms first; ex vivo mouse brain second
- External validation: None reported
- Software and versions: Unknown
- Code availability: Unknown

# Data and resource availability
- Repository and accession: Unknown
- Raw data available: Unknown
- Processed data available: Unknown
- Metadata completeness: Unknown
- Data-use restrictions: Unknown
- Reusability for the user's work: NeuRIFI platform is directly relevant to in situ SWCNT sensor deployment in neural tissue; the DNA-SWCNT functionalization protocol is directly transferable to nanosensor implant work

# Main findings
| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| NeuRIFI resolves transient DA flux at 90 nM sensitivity, 20 ms temporal, ~1.5 μm/pixel spatial resolution | Reported | Abstract | 90 nM / 20 ms / 1.5 μm | Unknown (abstract only) | Ex vivo mouse brain only; in vivo not yet demonstrated |
| Deep-brain signal acquisition at 3 mm depth is reliable | Reported | Abstract | 3 mm depth validated | Unknown (abstract only) | Tissue phantom + ex vivo; no in vivo validation |
| Dual-readout provides photometric (point) + spatial (field-level) information simultaneously | Reported | Abstract | Synchronous readout demonstrated | Unknown (abstract only) | Full performance characterization pending full text |

# What is actually new?
- Biological novelty: Volume transmission (spatial dopamine fields) is spatially resolved for the first time with SWCNT-based imaging, without genetic labels
- Methodological novelty: Dual-readout NIR fiber probe (photometry + remote imaging) with DNA-SWCNT functionalization; label-free neurochemical spatial imaging at depth
- Dataset or resource novelty: Unknown
- What was already known: SWCNT sensors detect dopamine in solution; fiber photometry provides point-in-space neurochemical signals; prior SWCNT implants detected ovarian cancer and steroid hormones in vivo

# Strengths
- Design strength: Dual-readout architecture provides internal photometric validation of the remote imaging signal
- Validation strength: Tissue phantoms + ex vivo mouse brain with defined depth (3 mm); LOD and resolution quantified
- Reproducibility strength: Quantitative performance metrics (LOD, temporal res, spatial res) reported
- Translational or ecological realism: Ex vivo mouse brain at clinically relevant depth; NIR optical window minimizes tissue absorption

# Limitations and bias risks
- Sample-size or power limitation: Unknown — ex vivo N Unknown
- Confounding: Ex vivo brain lacks vascular perfusion and in vivo dynamics; dopamine release dynamics may differ from in vivo
- Batch or site effects: Unknown
- Pseudoreplication risk: Unknown
- Leakage or overfitting risk: Not applicable
- Generalizability limitation: Ex vivo only; in vivo dopamine dynamics, immune response to implant, long-term stability not demonstrated
- Missing controls: Selectivity against norepinephrine, serotonin, and other catecholamines not reported from abstract
- Missing validation: In vivo validation; long-term implant stability; interferant selectivity
- Author-stated limitations: Unknown — full text required
- Additional limitations identified during review: DNA sequence and SWCNT chirality not stated in abstract — critical for reproducibility

# Transferability to the user's work
- Directly transferable elements: DNA-SWCNT on implantable optical fiber design; dual-readout photometry + NIR imaging architecture; tissue phantom validation approach
- Elements requiring adaptation: Ex vivo mouse brain → in vivo; DNA-SWCNT functionalization protocol needs full details from supplementary methods
- Model, species, tissue, matrix, platform, or scale mismatch: Mouse ex vivo → human tissue would require recalibration; in vivo extension would require biocompatibility validation
- Assumptions required for transfer: DNA-SWCNT NIR response is stable in biological matrices over the sensing timeframe
- Confidence: moderate (abstract + clear performance metrics)

# Practical implications
- Experimental implication: DNA-SWCNT fiber probe enables label-free dopamine spatial mapping in deep brain tissue — applicable to organoid or acute slice imaging with adaptation; relevant to in situ sensing in TBI or organoid injury models
- Analysis implication: Frame-to-frame intensity derivative for transient flux is a reusable computational approach for NIR image series
- Public dataset implication: Unknown
- Biomarker or translational implication: Label-free NIR spatial mapping of dopamine is a step toward intraoperative or diagnostic neurochemical monitoring
- Grant or manuscript implication: Supports SWCNT NIR sensor work for in situ neurochemical sensing; strong methods precedent for implantable SWCNT platforms

# Contradictions and links
- Supports: williams_2018_swcnt-optical-nanosensor-implant-ovarian.md (implantable SWCNT in vivo); lee_2025_swcnt-patch-sensor-biofluid-tracing.md (SWCNT in tissue sensing contexts)
- Contradicts: Nothing in current library
- Replicates: Unknown
- Methodologically comparable papers: williams_2018_swcnt-optical-nanosensor-implant-ovarian.md; cho_2021_cophmore-swcnt-sars-cov-2-saliva.md (SWCNT sensor application)
- Relevant synthesis notes: None yet
- Relevant project decisions: None yet

# Follow-up actions
- [ ] Retrieve full text from ACS Nano for DNA sequence, SWCNT chirality, and functionalization protocol
- [ ] Check selectivity data (catecholamine interference) in supplement
- [ ] Monitor for in vivo follow-up validation study
- [ ] Add to synthesis on SWCNT implantable sensor platforms

# Priority decision
- Priority: 2
- Retain for methods
- Rationale: First dual-readout DNA-SWCNT fiber probe for spatially resolved dopamine mapping in neural tissue with validated depth performance; directly relevant to SWCNT neurochemical sensing and implantable sensor design
