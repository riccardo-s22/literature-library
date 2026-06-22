---
record_type: paper
record_status: verified
canonical_id: "10.1038/s41551-022-00860-y"
doi: "10.1038/s41551-022-00860-y"
pmid: "35301449"
pmcid: "PMC9108893"
title: "Detection of ovarian cancer via the spectral fingerprinting of quantum-defect-modified carbon nanotubes in serum by machine learning"
year: 2022
source_type: primary
peer_reviewed: true
full_text_checked: false
supplement_checked: false
code_checked: false
data_checked: false
last_verified: 2026-06-22
priority: 1
projects: []
topics: [biosensors, nanomaterials]
methods: [spectroscopy, biomarker, analysis_method, external_validation]
datasets: []
---

# Citation
- Full citation: Kim M, Chen C, Wang P, Mulvey JJ, Yang Y, Wun C, Antman-Passig M, Luo HB, Cho S, Long-Roche K, Ramanathan LV, Jagota A, Zheng M, Wang Y, Heller DA. "Detection of ovarian cancer via the spectral fingerprinting of quantum-defect-modified carbon nanotubes in serum by machine learning." *Nature Biomedical Engineering* 2022;6(3):267-275.
- DOI / PMID / stable URL: [DOI](https://doi.org/10.1038/s41551-022-00860-y) · PMID 35301449 · PMC9108893
- Related preprint or published version: Peer-reviewed (Nat Biomed Eng). NSF PAR copy at par.nsf.gov/servlets/purl/10352933.
- Correction, expression of concern, or retraction status: **Unknown** — not checked (added 2026-06-22).

*Source: metadata + abstract (PubMed) + corroborating WebSearch (Nature/PMC/NSF-PAR). Full text not inspected. According to PubMed, DOI [10.1038/s41551-022-00860-y](https://doi.org/10.1038/s41551-022-00860-y).*

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: The strongest decision-relevant SWCNT-spectral-phenotyping paper for the user's biosensor domain: a **realistic serum matrix**, an **array of quantum-defect-modified SWCNT sensors**, and a **machine-learning classifier validated on a clinically meaningful cohort (269 serum samples)** that matches/exceeds the best clinical screening test for high-grade serous ovarian carcinoma (87% sensitivity at 98% specificity vs CA-125+TVUS 84%/98%). Directly informs sensor-array + ML design and the "leakage-resistant ML validation in real biofluid" signal.
- Why it is more or less useful than neighboring literature: Unlike single-analyte CoPhMoRe demos (cho_2021, yoon_2025), this is a **disease-fingerprint / perception-based** approach (responds to unidentified serum biomarkers, not one protein) with a sizable patient cohort and head-to-head clinical benchmark — a template for the user's spectral-phenotyping ML work.

# Source inspection status
- Abstract inspected: yes
- Full text inspected: no (abstract + metadata; PMC9108893 not sliced this pass)
- Methods inspected: partial (sensor identities, sample count, metrics from abstract/WebSearch)
- Supplement inspected: no
- Figures/tables inspected: no
- Code repository inspected: no
- Data repository inspected: no
- Missing material: full Methods (spectral acquisition, feature engineering, classifier type/CV, train/test split, donor-aware splitting), supplement, code/data availability.

# Study question and hypothesis
- Primary question: Can an array of quantum-defect-modified SWCNTs + ML detect high-grade serous ovarian carcinoma directly from serum better than existing biomarkers?
- Stated hypothesis: A multiplexed SWCNT nIR "disease fingerprint" encodes ovarian-cancer-discriminating information beyond known protein biomarkers.
- Study type: Biosensor development + retrospective clinical-sample classification with ML.

# Biological or clinical context
- Disease / exposure / process: High-grade serous ovarian carcinoma (and other diseases / healthy controls).
- Organism: Human.
- Tissue / cell type: Serum.
- Model system: Patient serum samples (symptomatic individuals).
- Cohort or population: 269 serum samples (ovarian cancer vs other diseases vs healthy).
- Relevant stage, age, sex: Female; symptomatic cohort; stage distribution not extracted.

# Study design
- Experimental or observational unit: Serum sample (per individual).
- Unit of inference: Sample/patient-level classification.
- Groups and sample size per group: 269 total across ovarian cancer / other disease / healthy (per-group n not extracted).
- Biological replicates: Patient samples.
- Technical replicates: Not extracted.
- Randomization / blinding: Not extracted.
- Inclusion / exclusion criteria: Symptomatic individuals; details not extracted.
- Batch structure: Sensor-array measurements across samples (batch/drift handling not extracted — key QC to verify).
- Controls and comparators: Other diseases + healthy controls; clinical benchmark CA-125 + transvaginal ultrasonography.

# Experimental methods
- Assay / platform: Array of SWCNTs functionalized with quantum (sp3) defects + DNA wrappings; near-infrared fluorescence emission spectra. Best model used the combination: 4-N(C2H5)2*C T2C3T2C, 4-N(C2H5)2*(TAT)4, 3,4,5-F3*(TAT)4, 3,4,5-F3*(AT)15, 3,4,5-F3*(GT)15 (per WebSearch/abstract).
- Sample preparation: Serum incubated with sensor array (details in Methods, not inspected).
- Dose / perturbation: N/A (analyte = serum).
- Timing / sampling schedule: Single readout per sample (not verified).
- Matrix: Human serum (realistic clinical matrix — key strength).
- Primary endpoint: Classification of ovarian cancer vs non-cancer (sensitivity at fixed specificity).
- Secondary endpoints: Comparison to CA-125+TVUS; evidence that signal exceeds known protein biomarkers.
- QC criteria / failure criteria: Not extracted.
- Exact reusable parameters and source location: Best 5-sensor combination (above) — reusable sensor-selection result; full spectra-acquisition params in Methods (not inspected).

# Computational and statistical methods
- Raw input: nIR emission spectra (feature vectors per sensor).
- Preprocessing / feature engineering: Spectral features; details not extracted.
- Statistical model: Several ML classifiers trained and validated; best classifier reported. Type, cross-validation scheme, and **donor/sample-aware split** not extracted — must verify to assess leakage risk.
- Multiple-testing correction: N/A.
- Effect-size reporting: 87% sensitivity at 98% specificity (PPV/sensitivity equally weighted).
- Batch handling: Not extracted.
- Validation strategy: Train + validate on 269 samples; head-to-head vs clinical test.
- External validation: Not clearly an independent external cohort (single 269-sample set, internally split) — verify.
- Software / versions: Not extracted.
- Code availability: Not extracted.

# Data and resource availability
- Repository and accession: Not extracted (Nat Biomed Eng typically has data/code statements) — verify on article page.
- Raw data available: Unverified.
- Processed data available: Unverified.
- Metadata completeness: Unverified.
- Data-use restrictions: Human serum/clinical — likely restricted.
- Reusability for the user's work: Sensor-array design + ML pipeline highly instructive; raw spectra reuse to confirm.

# Main findings
| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| SWCNT array + ML detects HGSOC in serum at 87% sensitivity / 98% specificity | Reported | Abstract | 87% sens @ 98% spec | Yes | Internal split; verify donor-aware CV |
| Outperforms current best clinical screen (CA-125 + TVUS) | Reported | Abstract | 87/98 vs 84/98 | Yes | Same cohort comparison |
| Classifier performance not attainable by known protein biomarkers | Reported | Abstract | predictive value exceeds known proteins | Partial | Implies unidentified analytes (inference) |
| 269 serum samples used to train + validate | Reported | Abstract | n=269 | Yes | Per-group n not extracted |
| Best 5-sensor quantum-defect/DNA combination identified | Reported | Results (per WebSearch) | 5-sensor combo listed | Yes | From secondary source; confirm in full text |

# What is actually new?
- Biological novelty: Serum "disease fingerprint" for ovarian cancer beyond CA-125.
- Methodological novelty: Quantum-defect-modified SWCNT **sensor array** + ML perception-based classification in serum.
- Dataset/resource novelty: 269-sample serum spectral dataset (availability unverified).
- What was already known: Single-analyte SWCNT CoPhMoRe sensing; CA-125 limitations.

# Strengths
- Design strength: Sensor-array multiplexing; realistic serum matrix; clinically meaningful cohort and benchmark.
- Validation strength: Head-to-head vs standard-of-care; sizeable cohort.
- Reproducibility strength: Specific best-sensor combination reported.
- Translational realism: Human serum, symptomatic cohort — high.

# Limitations and bias risks
- Sample-size / power: 269 across multiple groups; per-class power not extracted.
- Confounding: Serum source/site, collection batch, comorbidity spectrum not extracted.
- Batch / site effects: Sensor drift/batch handling not described here — important to verify.
- Pseudoreplication risk: If multiple spectra per sample, must aggregate at sample level — verify.
- Leakage / overfitting risk: ML with internal split; **donor/sample-aware split and independent test set must be confirmed** (signal file priority).
- Generalizability: Symptomatic cohort (not asymptomatic screening); single study site likely.
- Missing controls / validation: True external cohort not confirmed.
- Author-stated limitations: Not extracted.
- Additional limitations identified during review: "Responds to unidentified biomarkers" is an inference; mechanistic/orthogonal chemical validation of corona interactions not confirmed.

# Transferability to the user's work
- Directly transferable elements: Quantum-defect SWCNT array design; perception-based ML on nIR spectra in serum; clinical-benchmark framing; reported best-sensor combination as a starting library.
- Elements requiring adaptation: Target disease/analyte; sensor library; classifier choice.
- Mismatch: Ovarian cancer serum vs the user's matrices (saliva/urine/sweat in seed records).
- Assumptions required for transfer: Comparable spectral acquisition; leakage-resistant CV.
- Confidence: high (as a design template), moderate (for exact metrics until Methods verified).

# Practical implications
- Experimental implication: Adopt a multi-chirality/quantum-defect sensor array rather than a single sensor; include realistic matrix from the start.
- Analysis implication: Use donor-aware splits and an independent test set; report sensitivity at fixed specificity vs a clinical benchmark.
- Public dataset implication: Possible reusable serum spectral dataset — verify availability.
- Biomarker / translational implication: Spectral fingerprinting can exceed single-protein biomarkers.
- Grant / manuscript implication: Flagship precedent for SWCNT+ML biofluid diagnostics.

# Contradictions and links
- Supports: Spectral-phenotyping over single-analyte sensing.
- Contradicts: none identified.
- Replicates: Concept extended by tian_2025 (ML decoding of SWCNT nIR spectra).
- Methodologically comparable papers: cho_2021, yoon_2025, lee_2025 (SWCNT CoPhMoRe/optical); tian_2025 (SWCNT spectral ML).
- Relevant synthesis notes: seed for "SWCNT spectral fingerprinting + ML in biofluids."
- Relevant project decisions: (none yet)

# Follow-up actions
- [ ] Inspect Methods/supplement for classifier type, CV scheme, donor-aware split, and external validation
- [ ] Confirm data/code availability
- [ ] Cross-link with tian_2025 and existing SWCNT records
- [ ] Check correction/retraction status

# Priority decision
- Priority: 1
- Read now (flagship SWCNT+ML biofluid reference)
- Rationale: Highest-relevance SWCNT spectral-phenotyping + ML study with a realistic serum matrix and clinical benchmark; central template for the user's biosensor program. Key open question: leakage-resistant validation, to confirm from Methods.
