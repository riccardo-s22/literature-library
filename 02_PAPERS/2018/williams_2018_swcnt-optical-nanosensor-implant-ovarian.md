---
record_type: paper
record_status: verified
canonical_id: "10.1126/sciadv.aaq1090"
doi: "10.1126/sciadv.aaq1090"
pmid: "29675469"
pmcid: "PMC5906074"
title: "Noninvasive ovarian cancer biomarker detection via an optical nanosensor implant"
year: 2018
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
methods: [spectroscopy, biomarker, imaging]
datasets: []
---

# Citation
- Full citation: Williams RM, Lee C, Galassi TV, Harvey JD, Leicher R, Sirenko M, Dorso MA, Shah J, Olvera N, Dao F, Levine DA, Heller DA. "Noninvasive ovarian cancer biomarker detection via an optical nanosensor implant." *Science Advances* 2018;4(4):eaaq1090.
- DOI / PMID / stable URL: [DOI](https://doi.org/10.1126/sciadv.aaq1090) · PMID 29675469 · PMC5906074
- Related preprint or published version: Peer-reviewed (Sci Adv).
- Correction, expression of concern, or retraction status: **Unknown** — not checked beyond metadata (2026-06-22).

*Source: PubMed metadata + abstract (full text not inspected). According to PubMed, DOI [10.1126/sciadv.aaq1090](https://doi.org/10.1126/sciadv.aaq1090).*

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Foundational **in vivo implantable SWCNT optical nanosensor** — fills the corpus's missing "in-vivo nanosensor" axis (existing SWCNT records are ex vivo serum/biofluid: [[kim_2022_swcnt-ovarian-cancer-serum-ml]], [[lee_2025_swcnt-patch-sensor-biofluid-tracing]], [[cho_2021_cophmore-swcnt-sars-cov-2-saliva]]). Demonstrates antibody-functionalized nanotube bandgap modulation as a quantitative, implant-based readout in live animals.
- Why it is more or less useful than neighboring literature: First in vivo optical nanosensor for noninvasive cancer-biomarker detection in orthotopic models — a design precedent for implantable continuous monitoring, complementary to (not redundant with) the serum-ML ovarian work (kim_2022).

# Source inspection status
- Abstract inspected: yes
- Full text inspected: no
- Methods inspected: no
- Supplement / figures / code / data inspected: no
- Missing material: exact LoD, sensor formulation (chirality/wrapping), membrane spec, animal-model counts, calibration/interference data, in vivo signal stability.

# Study question and hypothesis
- Primary question: Can an implantable antibody-functionalized SWCNT optical sensor detect the ovarian-cancer biomarker HE4 in vivo?
- Stated hypothesis: A sensor placed proximal to disease sites can detect HE4 earlier/more sensitively than serum assays.
- Study type: Sensor engineering + in vivo validation in orthotopic ovarian-cancer models.

# Biological or clinical context
- Disease / exposure / process: High-grade serous ovarian carcinoma (HGSC); biomarkers HE4 and CA-125 (typically undetectable in serum until advanced stages).
- Organism: Mouse (orthotopic models) + human patient biofluids (benign vs disease).
- Tissue / cell type: Peritoneal/reproductive-tract proximal placement; biofluids.
- Model system: Four ovarian-cancer models; sensor encased in semipermeable membrane.
- Cohort or population: Patient biofluids (benign vs malignant) for discrimination; counts not extracted.

# Study design
- Experimental unit / unit of inference: Animal/implant; patient biofluid samples.
- Groups and sample size per group: **Unknown** (four models; n per group not extracted).
- Randomization / blinding / replicates: Not extracted.
- Controls and comparators: Benign vs disease biofluids; (in vivo sham/membrane controls implied, not extracted).

# Experimental methods
- Assay / platform: Antibody-functionalized SWCNT complex; **HE4 detection via modulation of nanotube optical bandgap** (NIR fluorescence shift); implant within semipermeable membrane.
- Sample preparation: Sensor complex synthesis (formulation not extracted).
- Dose / analyte: HE4 (nanomolar sensitivity reported).
- Matrix: Patient biofluids; in vivo tissue environment.
- Primary endpoint: Quantitative HE4 detection distinguishing disease from benign; in vivo optical readout in live animals.
- QC / interference: Not extracted (selectivity/interference controls to verify in full text).
- Exact reusable parameters and source location: **needs full text** — sensor formulation, LoD, membrane spec, in vivo optical setup.

# Computational and statistical methods
- Not extracted (full text not inspected).

# Data and resource availability
- Repository and accession: **Unknown** (not inspected).
- Reusability for the user's work: High as a design precedent for implantable SWCNT sensing; quantitative reuse requires full-text parameters.

# Main findings
| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| SWCNT complex quantifies HE4 via optical bandgap modulation | Reported | Abstract | nanomolar sensitivity | Yes | formulation/LoD not extracted |
| Discriminates disease from benign patient biofluids | Reported | Abstract | qualitative discrimination | Yes | cohort size unknown |
| Implant detects HE4 in vivo in 4 ovarian-cancer models | Reported | Abstract | first in vivo optical nanosensor | Yes | model counts not extracted |

# What is actually new?
- Biological/translational novelty: Noninvasive, implant-based in vivo biomarker detection proximal to disease.
- Methodological novelty: Antibody-SWCNT bandgap-modulation sensor in a semipermeable-membrane implant.
- What was already known: HE4/CA-125 as HGSC serum markers (late-stage); SWCNT NIR fluorescence biocompatibility.

# Strengths / Limitations
- Strengths: True in vivo demonstration; orthotopic models; clinically motivated analyte; tissue-transparent NIR window.
- Limitations: 2018 prototype; long-term stability/biofouling, selectivity in complex matrices, and cohort sizes need full-text verification; single analyte (HE4).

# Transferability to the user's work
- Directly transferable elements: Implantable SWCNT optical-sensor architecture; antibody-functionalization + membrane encapsulation; NIR bandgap-modulation readout.
- Elements requiring adaptation: Different analytes/matrices (e.g., neuro biofluids); corona-phase vs antibody recognition.
- Mismatch: Oncology implant vs neuro-biomarker context.
- Confidence: moderate (concept high; parameters pending).

# Practical implications
- Experimental implication: Template for implantable continuous biomarker monitoring with SWCNTs.
- Biomarker/translational implication: Proximal-implant strategy for early detection where serum markers lag.

# Contradictions and links
- Supports: SWCNT optical sensing in realistic/in vivo contexts (cf. [[kim_2022_swcnt-ovarian-cancer-serum-ml]] serum ML; [[lee_2025_swcnt-patch-sensor-biofluid-tracing]] wearable patch).
- Methodologically comparable papers: cho_2021 (CoPhMoRe recognition), tian_2025 (NIR ML decoding).
- Relevant synthesis notes: seed for "in vivo / implantable SWCNT optical sensing."

# Follow-up actions
- [ ] Retrieve full text; extract LoD, formulation, membrane spec, model counts, selectivity/interference data
- [ ] Confirm correction/retraction status
- [ ] Cross-link into a SWCNT-sensing synthesis (serum vs wearable vs implant)

# Priority decision
- Priority: 2
- Retain for methods (implantable-sensor design precedent)
- Rationale: Fills the in-vivo SWCNT nanosensor gap and anchors the implant-design axis; quantitative parameters require full text.
