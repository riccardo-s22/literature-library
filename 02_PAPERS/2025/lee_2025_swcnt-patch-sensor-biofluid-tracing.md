---
record_type: paper
record_status: verified
canonical_id: "10.1038/s41467-025-58425-x"
doi: "10.1038/s41467-025-58425-x"
pmid: "40188097"
pmcid: "PMC11972314"
title: "Spatiotemporal molecular tracing of ultralow-volume biofluids via a soft skin-adaptive optical monolithic patch sensor"
year: 2025
source_type: resource
peer_reviewed: true
full_text_checked: true
supplement_checked: false
code_checked: false
data_checked: false
last_verified: 2026-06-22
priority: 2
projects: []
topics: [biosensors, nanomaterials]
methods: [spectroscopy, imaging, biomarker]
datasets: []
---

# Citation
- Full citation: Lee YS, Shin S, Kang GR, Lee S, Kim DW, Park S, Cho Y, Lim D, Jeon SH, Cho SY, Pang C. "Spatiotemporal molecular tracing of ultralow-volume biofluids via a soft skin-adaptive optical monolithic patch sensor." *Nature Communications* 2025;16(1):3272.
- DOI / PMID / stable URL: [DOI](https://doi.org/10.1038/s41467-025-58425-x) · PMID 40188097 · PMC11972314
- Related preprint or published version: Peer-reviewed (Nat Commun), open access; Transparent Peer Review + Source Data available.
- Correction, expression of concern, or retraction status: **Unknown** — not checked (added 2026-06-22).

*Source: metadata + PMC full text retrieved from PubMed / PubMed Central. According to PubMed, DOI [10.1038/s41467-025-58425-x](https://doi.org/10.1038/s41467-025-58425-x).*

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: A **wearable, multiplexed DNA/SWCNT (CoPhMoRe) optical patch (3D MIN)** that captures and senses ultralow-volume biofluid (sweat) on dynamic skin, with a 20×15 corona-library screen, four selected sensors (vitamins B2/B6/B9, cortisol), nIR LODs, spatiotemporal stand-off imaging, and **HPLC orthogonal validation** in real human sweat. Matches biosensor-domain priorities: biofluid-compatible optical nanosensors, corona-library screening, calibration/LOD, specificity controls, dispersion QC (DLS, UV-vis-nIR), translational form factor, and orthogonal chemical validation. Strong **device/resource precedent** for low-volume biofluid spectral phenotyping.
- Why it is more or less useful than neighboring literature: Combines corona-phase sensing with a frog-toe-pad-inspired adhesive microfluidic capture layer and a stand-off nIR imaging readout — a deployable, multiplexed platform with real on-body validation and orthogonal HPLC confirmation. More integrated/translational than buffer-only sensor demos. Limitations: sensors embedded in hydrogel raise LOD ~1 order; sweat target (not neuro biomarker); small human subject n.

# Source inspection status
- Abstract inspected: yes
- Full text inspected: yes (PMC full text incl. Methods)
- Methods inspected: yes (fabrication, nIR imaging, on-body protocol, HPLC)
- Supplement inspected: no (extensive Supplementary referenced)
- Figures/tables inspected: no (callouts read; panels not viewed)
- Code repository inspected: N/A
- Data repository inspected: partial — Nat Commun "Source Data" provided (not opened); no sequence/omics accession.
- Missing material: Supplementary figures/notes (drainage/adhesion models), full library heatmap, Source Data values.

# Study question and hypothesis
- Primary question: Can optical SWCNT nanosensors be monolithically integrated into a soft, skin-adaptive microstructured patch to capture and sense ultralow-volume biofluids in real time, multiplexed, on dynamic surfaces?
- Stated hypothesis: A bioinspired (tree-frog-toe-pad) 3D microchannel + soft-PDMS adhesion layer with embedded DNA/SWCNT/hydrogel enables simultaneous low-volume fluid capture and selective nIR molecular sensing on wet, rough, moving skin.
- Study type: Device development + analytical characterization + in vitro sweating-skin model + on-body human validation.

# Biological or clinical context
- Disease / exposure / process: Non-invasive health monitoring (vitamins B2/B6/B9, cortisol, vitamin C) via sweat.
- Organism: Human (sweat); porcine skin (in vitro adhesion/flow).
- Tissue / cell type: N/A (biofluid/skin interface).
- Model system: Artificial sweating-skin (syringe pump + porcine skin); human forearm/forehead.
- Cohort or population: 3 human subjects (vitamin C dosing 0/1.5/3 g); HPLC on 2 subjects (n=5 sweat samples). IRB SKKU 2023-12-057.

# Study design
- Experimental or observational unit: Patch (sensor array) × analyte/flow condition; per human subject for on-body.
- Unit of inference: Per-sensor nIR response; per-subject sweat tracing.
- Groups and sample size per group: 20×15 nanosensor library screened; 4 sensors selected (+1 vitamin C sensor for visualization); 3 on-body subjects across 3 doses; HPLC n=5.
- Biological replicates: Small human n (3 subjects); analytical replicates for calibration.
- Technical replicates: Multiarray (4 spatially encoded sensors); flow-rate series.
- Randomization / blinding: Not described.
- Inclusion / exclusion criteria: Sensors selected for strongest non-overlapping target response; specificity tested against fixed non-target analytes (1 µM).
- Batch structure: Not detailed (single fabrication line).
- Controls and comparators: DI water control; 0 g vitamin C control subject; 3D MIN w/ vs w/o hydrogel; flat vs soft/medium/hard hexagonal pads; artificial sweat with 15 interferent analytes; HPLC orthogonal validation.

# Experimental methods
- Assay / platform: DNA/SWCNT CoPhMoRe nIR fluorescence embedded in polyacrylamide (PAAm) hydrogel within a hexagonal-microchannel s-PDMS patch (3D MIN). Readout: nIR microscope (in vitro) and stand-off nIR camera (NINOX OWL 640, 900 nm longpass, 721 nm laser excitation, 20 cm standoff); XCAP v3.8 + ImageJ v1.54f.
- Sample preparation: SWCNT suspended with 20 DNA sequences; UV-vis-nIR (E11/E22) individualization; DLS for dispersion uniformity; PAAm pregel (5 g AAm, 0.05 g KPS, 10 mL DI) mixed 1:1 with DNA/SWCNT; O2 plasma 3 min; cured 80 °C/20 min. Patch master via photolithography/RIE; channel width 200 µm, height 300 µm, spacing 600 µm.
- Dose / concentration / force: Analyte series nM-µM (sweat-relevant); flow rates 0.5/0.25/0.1 µL/min·cm² (daily sweat ~0.37); adhesion preload up to 2.0 N.
- Timing: Detects 75 nL in 45 s at 0.1 µL/min·cm²; response times 28.3-45.6 s (flow-dependent); cortisol saturation 68 s.
- Matrix / conditions: Sweat / artificial sweat (15 analytes); wet/dry rough surfaces (Ra 80/160 µm); on-body forehead/forearm.
- Primary endpoint: Selective nIR ΔF response + LOD per analyte; low-volume capture performance.
- Secondary endpoints: Adhesion strength/adaptability; multiarray spatiotemporal fingerprints; on-body vitamin C tracing.
- QC criteria: UV-vis-nIR individualization; DLS size uniformity; specificity in mixed-analyte solutions; HPLC confirmation of sweat vitamin C.
- Failure / exclusion criteria: Bare nanosensor/hydrogel (no microstructure) detaches under motion (reported); hydrogel embedding raises LOD ~1 order (reported limitation).
- Exact reusable parameters and source location: Full fabrication + imaging + on-body protocol in Methods; corona library (20 DNA × 15 analytes); LODs and flow/volume metrics in Results.

# Computational and statistical methods
- Raw input: nIR emission images/spectra; ΔF = (I-I0)/I0.
- Preprocessing: Integrated nIR intensity ratios; image processing in ImageJ.
- Statistical model: Calibration curves; LOD = 3× buffer-noise; drainage (fluid-dynamics squeeze/channel model), swelling (Fickian diffusion), adhesion (capillary-bridge) physical models (Supplementary Notes 1-7); first-order binding model to estimate sweat concentration.
- Effect-size reporting: Library responses -74% to +3500% ΔF; LODs 1.74 nM (B2), 323 nM (B6), 991 nM (B9), 2270 nM (cortisol); vitamin C 3D MIN responses -22% to +932% (0-200 µM); adhesion 15.4 kPa dry / 11.3 kPa wet; estimated sweat vitamin C 5-60 µM.
- Multiple-testing correction: N/A.
- Validation strategy: Specificity vs fixed interferents; in vitro flow model; on-body dosing (0/1.5/3 g) with dose-response; **HPLC orthogonal validation** of sweat vitamin C.
- External validation: HPLC; sweat concentration ranges matched to literature.
- Software and versions: XCAP 3.8; ImageJ 1.54f.
- Code availability: N/A.

# Data and resource availability
- Repository and accession: Nature Communications "Source Data" provided (no omics accession). No public dataset accession.
- Raw data available: Source Data file (not opened).
- Processed data available: In-paper + Source Data.
- Metadata completeness: Fabrication/instrument details complete in Methods.
- Data-use restrictions: N/A.
- Reusability for the user's work: **High as a device/protocol** (corona-library screen + adhesive microfluidic capture + stand-off nIR imaging); not a reusable dataset.

# Main findings
| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| 3D MIN captures + senses ultralow-volume biofluid (75 nL in 45 s at 0.1 µL/min·cm²) | Reported | Results / Fig | beats prior wearables (≥1 µL, 100 s-20 min) | Yes | In vitro + on-body |
| 20×15 DNA/SWCNT CoPhMoRe library yields selective sensors (ΔF -74% to +3500%) | Reported | Results / heatmap | 4 selected (B2/B6/B9/cortisol) | Yes | Library in supplement |
| Per-analyte LODs: 1.74/323/991/2270 nM (B2/B6/B9/cortisol) | Reported | Results | 3× noise | Yes | Hydrogel embedding raises LOD ~1 order |
| Soft hexagonal pad gives strong adhesion on wet rough skin (11.3 kPa wet) and stays on under motion | Reported | Results | 73% adaptability (Ra 160 µm) | Yes | Porcine + human-hand tests |
| On-body sweat vitamin C tracing is dose-responsive (0/1.5/3 g) with high spatial resolution | Reported | Results | est. 5-60 µM in sweat | Yes | n=3 subjects |
| HPLC confirms vitamin C in captured sweat (orthogonal validation) | Reported | Results / HPLC | peak matches pure standard, rises over time | Yes | Strong orthogonal check |

# What is actually new?
- Methodological novelty: Monolithic integration of optical SWCNT nanosensors with a bioinspired adhesive microfluidic capture layer enabling ultralow-volume, multiplexed, stand-off sensing without exercise/iontophoresis.
- Biological novelty: Real-time spatiotemporal sweat tracing of challenging low-abundance analytes (B-vitamins, cortisol) at rest.
- Dataset or resource novelty: Reusable corona-library + patch fabrication + stand-off imaging protocol.
- What was already known: DNA/SWCNT CoPhMoRe sensing; wearable sweat sensors requiring higher volumes/rates.

# Strengths
- Design strength: Corona-library screen + specificity controls + multiarray; physical models for drainage/adhesion/swelling.
- Validation strength: In vitro flow model + on-body dose-response + **HPLC orthogonal validation**; interferent-rich artificial sweat.
- Reproducibility strength: Detailed fabrication (channel dimensions, plasma, cure), dispersion QC (UV-vis-nIR, DLS), instrument/software versions.
- Translational realism: On-body, no exercise/iontophoresis, low-volume, stand-off readout, biocompatibility (6 h, minimal irritation).

# Limitations and bias risks
- Sample-size / power: Only 3 on-body subjects; HPLC n=5.
- Confounding: Hydrogel embedding raises LOD ~1 order vs solution; DI-water gives slight response (swelling artifact).
- Batch / site effects: Single fabrication line; batch reproducibility of SWCNT not characterized.
- Pseudoreplication risk: N/A.
- Leakage / overfitting risk: N/A.
- Generalizability: Sweat analytes (not neuro biomarkers); skin interface; small human cohort.
- Missing controls / validation: No multi-batch/multi-donor donor-aware validation; sweat-blood correlation assumed (not measured here).
- Author-stated limitations: Hydrogel-embedding LOD penalty; single-use patch to avoid over-absorption.
- Additional limitations identified during review: No deposited dataset (Source Data only); donor-aware/leakage-resistant ML validation not applicable/absent.

# Transferability to the user's work
- Directly transferable elements: Corona-library screening + DNA/SWCNT dispersion QC (UV-vis-nIR, DLS); PAAm hydrogel embedding; stand-off nIR imaging setup; specificity testing in interferent-rich matrix; HPLC orthogonal-validation design; adhesive microfluidic capture concept.
- Elements requiring adaptation: Retarget library to neuro/serum/CSF biomarkers; recover LOD lost to hydrogel embedding; add donor-aware validation.
- Model, species, tissue, matrix, platform, or scale mismatch: Sweat vs serum/CSF; wearable vs benchtop.
- Assumptions required for transfer: Access to corona library + nIR imaging + microfabrication.
- Confidence: high for the platform/workflow; moderate for new analyte target.

# Practical implications
- Experimental implication: Adopt corona-library + dispersion QC + orthogonal HPLC validation; consider hydrogel-embedding LOD tradeoff.
- Analysis implication: Use 3× noise LOD; first-order binding for concentration estimation; report flow-rate-dependent response times.
- Public dataset implication: Source Data only.
- Biomarker / translational implication: Multiplexed low-volume optical biofluid phenotyping is feasible on-body.
- Grant / manuscript implication: Citable deployable SWCNT optical sensing platform with orthogonal validation.

# Contradictions and links
- Supports: DNA/SWCNT CoPhMoRe biofluid sensing; corona-library screening (cf. Cho 2021).
- Contradicts: Assumption that wearable sweat sensing requires high volumes/rates.
- Replicates: CoPhMoRe selective recognition behavior.
- Methodologically comparable papers: Cho 2021 (CoPhMoRe SARS-CoV-2 saliva, optode); Yoon 2025 (CoPhMoRe uric acid urine paper strip, same Cho SY group); Dewey 2024 (SWCNT nanosensor review).
- Relevant synthesis notes: candidate seed for "SWCNT corona-phase biofluid sensing platforms & QC" synthesis.
- Relevant project decisions: (none yet)

# Follow-up actions
- [ ] Inspect Supplementary (library heatmap, drainage/adhesion models) and Source Data
- [ ] Note the hydrogel-embedding LOD penalty when designing embedded sensors
- [ ] Cross-link with Cho 2021 and Yoon 2025 in a corona-phase biofluid synthesis
- [ ] Check retraction/correction status

# Priority decision
- Priority: 2
- Retain for methods + translational reference
- Rationale: Strong, well-validated (incl. HPLC) deployable SWCNT optical biofluid-sensing platform with a reusable corona-library + capture-layer workflow; Priority 2 because the target is sweat (non-neuro), human n is small, and it is a device (no deposited dataset).
