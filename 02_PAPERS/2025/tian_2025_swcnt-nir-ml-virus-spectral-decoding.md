---
record_type: paper
record_status: verified
canonical_id: "10.1021/acsnano.5c05727"
doi: "10.1021/acsnano.5c05727"
pmid: "40574605"
title: "Decoding Hidden Features in Near-Infrared Fluorescence Spectra of Single-Walled Carbon Nanotubes via Machine Learning for Multiplexed Virus Identification"
year: 2025
source_type: primary
peer_reviewed: true
full_text_checked: false
supplement_checked: false
code_checked: false
data_checked: false
last_verified: 2026-06-22
priority: 2
projects: []
topics: [biosensors, nanomaterials]
methods: [spectroscopy, analysis_method, biomarker]
datasets: []
---

# Citation
- Full citation: Tian C, Lee S, Park S, Cho Y, Baek C, Cho SY. "Decoding Hidden Features in Near-Infrared Fluorescence Spectra of Single-Walled Carbon Nanotubes via Machine Learning for Multiplexed Virus Identification." *ACS Nano* 2025;19(26):23992-24004.
- DOI / PMID / stable URL: [DOI](https://doi.org/10.1021/acsnano.5c05727) · PMID 40574605
- Related preprint or published version: Peer-reviewed (ACS Nano).
- Correction, expression of concern, or retraction status: **Unknown** — not checked (added 2026-06-22).

*Source: metadata + abstract (PubMed). Full text not inspected (ACS PMC/publisher returned 403 this pass). According to PubMed, DOI [10.1021/acsnano.5c05727](https://doi.org/10.1021/acsnano.5c05727).*

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Methods precedent for the user's **spectral-ML / EEM-style SWCNT phenotyping** signal: a framework that extracts *hidden multispectral features* across the 900–1400 nm window (beyond peak shift/intensity) to boost sensitivity/specificity and enable multiplexed detection **at ultralow concentrations** and **in human serum after minimal fine-tuning**. Demonstrates transfer-learning/fine-tuning to complex biological matrices — directly relevant to dispersion/matrix-robustness and donor-aware ML signals.
- Why it is more or less useful than neighboring literature: Complements kim_2022 (array + ML on serum) with a **single-sensor, full-spectrum ML** approach and explicit wavelength-attribution analysis; uses CoPhMoRe of three coronaviruses as a model. Less clinically validated than kim_2022 (model-system viruses, not a patient cohort), hence Priority 2.

# Source inspection status
- Abstract inspected: yes
- Full text inspected: no
- Methods inspected: partial (model system, spectral window, matrix from abstract)
- Supplement inspected: no
- Figures/tables inspected: no
- Code repository inspected: no
- Data repository inspected: no
- Missing material: full Methods (ML architecture, CV scheme, sample numbers, accuracy metrics, fine-tuning protocol), supplement, code/data availability.

# Study question and hypothesis
- Primary question: Can ML extract analyte-specific "hidden" multispectral features from SWCNT nIR fluorescence to enable sensitive, multiplexed detection below conventional detection limits?
- Stated hypothesis: Subtle, distributed spectral features (beyond peak intensity/shift) carry analyte-specific information exploitable by ML.
- Study type: Sensor + ML methods development (model analytes: three coronaviruses).

# Biological or clinical context
- Disease / exposure / process: Coronavirus detection (model system).
- Organism: Human (serum matrix test) + viral analytes.
- Tissue / cell type: Buffer + human serum.
- Model system: CoPhMoRe SWCNT sensors vs three pathogenic coronaviruses.
- Cohort or population: N/A (analytical samples; counts not extracted).
- Relevant stage/severity: N/A.

# Study design
- Experimental or observational unit: Spectral measurement per condition.
- Unit of inference: Spectrum-level classification / quantification.
- Groups and sample size per group: Not extracted (three viruses; concentration series below detection limit).
- Replicates: Not extracted.
- Randomization / blinding: Not extracted.
- Inclusion / exclusion criteria: Not extracted.
- Batch structure: Not extracted.
- Controls and comparators: Traditional peak-based analysis vs ML; buffer vs serum.

# Experimental methods
- Assay / platform: Corona-phase molecular recognition (CoPhMoRe) SWCNT nIR fluorescence; emission analyzed across 900–1400 nm.
- Sample preparation: Sensor incubated with virus; spectra collected below conventional detection limits.
- Dose / perturbation: Virus concentration series (ultralow); exact values not extracted.
- Timing / sampling schedule: Early-stage spectral variation used to optimize detection timing (abstract).
- Matrix: Buffer + human serum (with minimal fine-tuning).
- Primary endpoint: Multiplexed virus classification + adsorption-rate quantification.
- Secondary endpoints: Identification of unknown viruses; per-wavelength contribution to discrimination; detection-timing optimization.
- QC criteria / failure criteria: Not extracted.
- Exact reusable parameters and source location: 900–1400 nm analysis window; per-wavelength feature attribution; serum fine-tuning strategy (Methods/supplement — not inspected).

# Computational and statistical methods
- Raw input: SWCNT nIR emission spectra (intensity across 900–1400 nm).
- Preprocessing / feature engineering: Multispectral feature extraction (beyond peak intensity/shift).
- Statistical model: ML classifier (architecture/type not extracted); quantitative wavelength-contribution assessment; transfer/fine-tuning for serum.
- Multiple-testing correction: N/A.
- Effect-size reporting: "Accurate" classification + adsorption-rate quantification (numeric accuracy not extracted).
- Batch handling: Not extracted.
- Validation strategy: Generalization to unknown viruses + complex matrix (serum) with fine-tuning.
- External validation: Not described (model-system study).
- Software / versions: Not extracted.
- Code availability: Not extracted.

# Data and resource availability
- Repository and accession: Not extracted.
- Raw data / processed data available: Unverified.
- Metadata completeness: Unverified.
- Data-use restrictions: Likely none for model-system spectra (unverified).
- Reusability for the user's work: ML/feature-extraction framework reusable; raw spectra availability to confirm.

# Main findings
| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| ML decodes hidden multispectral features indistinguishable to traditional analysis | Reported | Abstract | qualitative; boosts sens/spec | Yes | numbers not extracted |
| Enables multiplexed detection of 3 coronaviruses below conventional detection limits | Reported | Abstract | sub-LOD multiplexing | Yes | model system |
| Per-wavelength attribution within 900–1400 nm quantified | Reported | Abstract | wavelength contributions assessed | Yes | — |
| Model identifies unknown viruses + optimizes detection timing | Reported | Abstract | qualitative | Partial | mechanism not detailed here |
| Retains performance in human serum after minimal fine-tuning | Reported | Abstract | transfer to serum | Yes | extent/metrics not extracted |

# What is actually new?
- Biological novelty: Limited (model-system virus detection).
- Methodological novelty: Full-spectrum "hidden feature" ML decoding + per-wavelength attribution + serum fine-tuning for SWCNT sensing.
- Dataset/resource novelty: Spectral ML framework (code/data availability unverified).
- What was already known: SWCNT spectral diversity; CoPhMoRe; ML for sensor readout (kim_2022).

# Strengths
- Design strength: Single-sensor multiplexing via spectral richness; explicit interpretability (wavelength attribution).
- Validation strength: Generalization to unknown analytes + serum transfer.
- Reproducibility strength: Defined spectral window; interpretable features.
- Translational realism: Serum demonstration (with fine-tuning) — moderate (model viruses, not patient cohort).

# Limitations and bias risks
- Sample-size / power: Sample numbers not extracted.
- Confounding: Serum-batch/matrix variability handling not detailed.
- Batch / site effects: Not described here.
- Pseudoreplication risk: Spectra-per-condition aggregation not described.
- Leakage / overfitting risk: ML with sub-LOD signals — CV scheme and train/test independence must be verified.
- Generalizability: Model viruses; clinical samples not tested.
- Missing controls / validation: No patient cohort / external validation.
- Author-stated limitations: Not extracted.
- Additional limitations identified during review: Metrics not in abstract; full text needed to judge rigor.

# Transferability to the user's work
- Directly transferable elements: 900–1400 nm full-spectrum ML decoding; per-wavelength interpretability; serum fine-tuning strategy.
- Elements requiring adaptation: Target analyte; sensor chemistry; classifier.
- Mismatch: Virus model vs the user's biomarker targets.
- Assumptions required for transfer: Comparable spectral acquisition; leakage-resistant CV.
- Confidence: moderate (methods template).

# Practical implications
- Experimental implication: Exploit the full nIR spectrum (not just peak features); plan a serum fine-tuning step.
- Analysis implication: Add wavelength-attribution for interpretability; pre-register CV to avoid sub-LOD overfitting.
- Public dataset implication: Possible reusable spectral set — verify.
- Biomarker / translational implication: Sub-LOD multiplexing feasible with spectral ML.
- Grant / manuscript implication: Methods citation for SWCNT spectral ML interpretability.

# Contradictions and links
- Supports: Spectral-fingerprinting + ML approach of kim_2022.
- Contradicts: none identified.
- Replicates: Concept (ML on SWCNT nIR spectra).
- Methodologically comparable papers: kim_2022 (array + ML serum), cho_2021/yoon_2025/lee_2025 (SWCNT optical).
- Relevant synthesis notes: seed for "SWCNT spectral ML + matrix robustness."
- Relevant project decisions: (none yet)

# Follow-up actions
- [ ] Inspect Methods/supplement for ML architecture, CV, sample numbers, metrics, fine-tuning protocol
- [ ] Confirm code/data availability
- [ ] Cross-link with kim_2022 and seed SWCNT records
- [ ] Check correction/retraction status

# Priority decision
- Priority: 2
- Retain for methods
- Rationale: Reusable spectral-ML/interpretability framework with serum-transfer demonstration; strong methods precedent but model-system (no clinical cohort) and metrics uninspected, so P2.
