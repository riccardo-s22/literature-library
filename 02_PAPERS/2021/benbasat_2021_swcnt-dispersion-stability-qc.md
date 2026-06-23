---
record_type: paper
record_status: verified
canonical_id: "10.3390/nano11102618"
doi: "10.3390/nano11102618"
pmid: "34685058"
pmcid: "PMC8540064"
title: "Development of Quality Control Methods for Dispersibility and Stability of Single-Wall Carbon Nanotubes in an Aqueous Medium"
year: 2021
source_type: primary
peer_reviewed: true
full_text_checked: false
supplement_checked: false
code_checked: false
data_checked: false
last_verified: 2026-06-22
priority: 3
projects: []
topics: [biosensors, nanomaterials]
methods: [spectroscopy, analysis_method]
datasets: []
---

# Citation
- Full citation: Ben Basat M, Lachman N. "Development of Quality Control Methods for Dispersibility and Stability of Single-Wall Carbon Nanotubes in an Aqueous Medium." *Nanomaterials (Basel)* 2021;11(10):2618.
- DOI / PMID / stable URL: [DOI](https://doi.org/10.3390/nano11102618) · PMID 34685058 · PMC8540064
- Related preprint or published version: Peer-reviewed (Nanomaterials, MDPI).
- Correction, expression of concern, or retraction status: **Unknown** — not checked beyond metadata (2026-06-22).

*Source: PubMed metadata + abstract (full text not inspected). According to PubMed, DOI [10.3390/nano11102618](https://doi.org/10.3390/nano11102618).*

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Fills the corpus's missing **SWCNT dispersion / batch-QC** axis flagged in the signals file (dispersion QC, batch robustness). Provides fast, scalable characterization methods (UV-Vis, rheology, precipitant sheet resistance, validated against microscopy + Raman) to quantify dispersion quality/stability and compare surfactants — directly relevant to reproducibility of any SWCNT optical-sensor preparation.
- Why it is more or less useful than neighboring literature: It is **materials/industrial** in scope (composite additives), not biosensing — so the biological-matrix relevance is indirect. But the QC methodology transfers to sensor-grade dispersion control, which no current corpus record covers.

# Source inspection status
- Abstract inspected: yes
- Full text inspected: no
- Methods inspected: no
- Supplement / figures / code / data inspected: no
- Missing material: exact UV-Vis metrics/thresholds, rheology protocol, surfactant panel, energy-input settings, acceptance criteria.

# Study question and hypothesis
- Primary question: Can simple, scalable characterizations serve as a quality-control system for aqueous SWCNT dispersion quality and stability?
- Stated hypothesis: Complementary fast measurements (UV-Vis, rheology, sheet resistance) track dispersion quality consistently with microscopy/Raman.
- Study type: Methods/QC development (materials science).

# Biological or clinical context
- Disease / exposure / process: N/A (materials QC).
- Organism / tissue: N/A (aqueous SWCNT dispersions).
- Model system: Water-based SWCNT dispersions (physical + chemical dispersion).
- Cohort or population: N/A.

# Study design
- Experimental unit / unit of inference: Dispersion batch / condition.
- Groups: Various dispersing energies and surfactants (panel not extracted).
- Controls and comparators: Microscopy + Raman as reference validation of dispersion/SWCNT quality.

# Experimental methods
- Assay / platform: UV-Vis spectroscopy; rheological measurements; precipitant sheet resistance; cross-validated with microscopy and Raman spectroscopy.
- Sample preparation: Aqueous dispersion via combined physical + chemical methods; varied surfactants and dispersing energies.
- Primary endpoint: Dispersion quality + stability indices; surfactant effectiveness ranking.
- QC criteria: Fast/repeatable indication of dispersion quality and stability (acceptance thresholds not extracted).
- Exact reusable parameters and source location: **needs full text** — extract UV-Vis dispersion metrics and rheology/sheet-resistance protocols for a sensor-prep QC SOP.

# Computational and statistical methods
- Not extracted (full text not inspected).

# Data and resource availability
- Repository and accession: **Unknown** (not inspected).
- Reusability for the user's work: Moderate — QC method templates transfer to SWCNT sensor dispersion control; thresholds are application-specific.

# Main findings
| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| UV-Vis + rheology + sheet resistance track dispersion quality/stability | Reported | Abstract | qualitative, fast/scalable | Yes | thresholds not extracted |
| Methods correlate with microscopy + Raman | Reported | Abstract | cross-validated | Yes | — |
| Protocol ranks surfactant dispersion effectiveness | Reported | Abstract | comparative | Yes | panel not extracted |

# What is actually new?
- Methodological novelty: A combined, scalable QC workflow for aqueous SWCNT dispersion quality/stability.
- What was already known: Individual characterizations (UV-Vis, Raman) of SWCNT dispersion exist; integration into a fast QC system is the contribution.

# Strengths / Limitations
- Strengths: Scalable, fast, orthogonally validated QC; surfactant comparison.
- Limitations: Industrial-composite context (not biofluid/sensor); no biological matrix; exact acceptance criteria require full text; single materials lab.

# Transferability to the user's work
- Directly transferable elements: UV-Vis/rheology/Raman QC logic for dispersion batch control; surfactant-screening approach.
- Elements requiring adaptation: Biosensor-grade dispersions (chirality purity, corona phase, biofluid stability) need sensor-specific endpoints.
- Mismatch: Composite-materials vs optical-biosensor application.
- Confidence: moderate (method), low (direct biosensor numbers).

# Practical implications
- Experimental implication: Basis for a dispersion-QC SOP to improve SWCNT sensor batch reproducibility.
- Analysis implication: Track UV-Vis/rheology indices as batch covariates to flag dispersion-driven sensor variability.

# Contradictions and links
- Supports: Reproducibility/QC emphasis for SWCNT platforms (cf. [[kim_2022_swcnt-ovarian-cancer-serum-ml]], [[tian_2025_swcnt-nir-ml-virus-spectral-decoding]], [[cho_2021_cophmore-swcnt-sars-cov-2-saliva]]).
- Relevant synthesis notes: seed for "SWCNT dispersion/corona QC & batch robustness."

# Follow-up actions
- [ ] Retrieve full text; extract UV-Vis/rheology metrics + surfactant panel + acceptance thresholds
- [ ] Adapt into a sensor-prep dispersion-QC checklist
- [ ] Confirm correction/retraction status

# Priority decision
- Priority: 3
- Retain for methods / background (dispersion-QC reference)
- Rationale: Closes the dispersion/QC coverage gap with reusable characterization methods, but is materials-engineering in scope with only indirect biosensor transfer.
