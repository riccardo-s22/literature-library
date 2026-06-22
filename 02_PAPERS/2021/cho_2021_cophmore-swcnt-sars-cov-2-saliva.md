---
record_type: paper
record_status: verified
canonical_id: "10.1021/acs.analchem.1c02889"
doi: "10.1021/acs.analchem.1c02889"
pmid: "34698489"
pmcid: "PMC8565189"
title: "Antibody-Free Rapid Detection of SARS-CoV-2 Proteins Using Corona Phase Molecular Recognition to Accelerate Development Time"
year: 2021
source_type: primary
peer_reviewed: true
full_text_checked: true
supplement_checked: false
code_checked: false
data_checked: false
last_verified: 2026-06-22
priority: 1
projects: []
topics: [biosensors, nanomaterials]
methods: [spectroscopy, biomarker]
datasets: []
---

# Citation
- Full citation: Cho SY, Jin X, Gong X, Yang S, Cui J, Strano MS. "Antibody-Free Rapid Detection of SARS-CoV-2 Proteins Using Corona Phase Molecular Recognition to Accelerate Development Time." *Analytical Chemistry* 2021;93(44):14685-14693.
- DOI / PMID / stable URL: [DOI](https://doi.org/10.1021/acs.analchem.1c02889) · PMID 34698489 · PMC8565189
- Related preprint or published version: Peer-reviewed (Anal Chem).
- Correction, expression of concern, or retraction status: **Unknown** — not checked (added 2026-06-22).

*Source: metadata + PMC full text retrieved from PubMed / PubMed Central. According to PubMed, DOI [10.1021/acs.analchem.1c02889](https://doi.org/10.1021/acs.analchem.1c02889).*

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: A canonical **corona-phase molecular recognition (CoPhMoRe)** SWCNT optical nanosensor study (Strano lab) that detects SARS-CoV-2 N and S proteins antibody-free via nIR fluorescence, **validated in 100% human saliva** with reported LODs, Hill-equation kinetics, BSA interferent controls, dispersion/QC details, and a deployable fiber-optic (optode) readout. Directly matches the biosensor-domain priorities: realistic biofluid matrix, selectivity/interference controls, surface chemistry, dispersion QC, optical settings, and translational constraints. A strong **methods precedent** for empirical corona-phase library screening.
- Why it is more or less useful than neighboring literature: Antibody-free, rapid (<5 min), with explicit saliva-matrix performance, interferent control (BSA), and a full corona-library screen (44 corona phases / 11 PEG-phospholipid backbones) — more transferable as a sensor-development workflow than single-target demonstrations. Limitation: viral-protein target (not a neuro biomarker); S-protein sensing degrades in saliva (negative finding captured).

# Source inspection status
- Abstract inspected: yes
- Full text inspected: yes (PMC full text incl. Experimental Section)
- Methods inspected: yes (SWCNT dispersion, screening, optode, 3D-print tip, buffers)
- Supplement inspected: no (SI referenced)
- Figures/tables inspected: no (callouts read; panels not viewed)
- Code repository inspected: N/A
- Data repository inspected: no (no dataset accession; ACS paper)
- Missing material: SI tables (saliva sourcing, full library responses); figure panels.

# Study question and hypothesis
- Primary question: Can CoPhMoRe (PEG-phospholipid corona on SWCNT) recognize SARS-CoV-2 N and S proteins antibody-free with biofluid compatibility and rapid, field-deployable readout?
- Stated hypothesis: A screened PEG-phospholipid corona on nIR-fluorescent SWCNT forms 3D recognition interfaces selective for viral proteins, enabling label-free detection without antibodies.
- Study type: Sensor development + analytical characterization (corona-library screen, kinetics, biofluid validation, instrumentation demo).

# Biological or clinical context
- Disease / exposure / process: COVID-19 / SARS-CoV-2 antigen detection (N nucleocapsid, S spike).
- Organism: Human (saliva matrix); recombinant viral proteins.
- Tissue / cell type: N/A (biofluid sensing).
- Model system: Buffer + 1%/100% human saliva; recombinant N/S proteins.
- Cohort or population: N/A (no patient cohort; saliva as matrix).

# Study design
- Experimental or observational unit: Nanosensor (corona phase) × analyte condition.
- Unit of inference: Per-sensor analytical response (turn-on/turn-off, LOD, kinetics).
- Groups and sample size per group: 44 unique corona phases from 11 PEG-phospholipid backbones screened; 2 lead sensors selected (18:0 PEG1000 PE/SWCNT for N; 14:0 PEG2000 PE/SWCNT for S).
- Biological replicates: Analytical replicates (exact n not extracted); concentration series fM-nM.
- Technical replicates: Screening in 96-well format; controls vs buffer and BSA.
- Randomization / blinding: N/A.
- Inclusion / exclusion criteria: Top 80% of dispersion reserved (QC); leads chosen for distinguishable specific responses.
- Batch structure: SWCNT batch HR27-104 (NanoIntegris) — single batch noted.
- Controls and comparators: Buffer-only; BSA interferent (10 µg/mL) for non-specific binding/stability; saliva control (-analyte) vs +analyte.

# Experimental methods
- Assay / platform: nIR fluorescence of PEG-phospholipid/SWCNT (CoPhMoRe). Screening on customized nIR microscope (Zeiss Axio + Acton SP2500 + LN2-cooled InGaAs, 20X, 785 nm 150 mW excitation, 950-1250 nm emission). Deployment: Lab-on-Fiber optode (561/785 nm lasers, RP29 reflection probe 6-around-1, PDF10C/PDF10C InGaAs detector, 900 nm SP/LP filters, 3D-printed VeroClear sensing tip, <10 µL sample).
- Sample preparation: 1 mg HiPCO SWCNT + 1 mg PEG-phospholipid in 1 mL DI; probe ultrasonication 10 W 30 min; centrifuge 30,300 RCF ×1 hr twice; top 80% retained; UV-vis-nIR to confirm individualized SWCNT ((6,5),(7,6),(9,4) chiralities); accessible surface area via molecular-probe adsorption (riboflavin).
- Dose / concentration: Viral proteins 10 µg/mL for screening; concentration series fM-nM for kinetics; saliva 1% and 100%.
- Timing: Rapid response <5 min; 60-min incubation for screening; optode response time τ = 5.1 min (90% of plateau).
- Matrix / conditions: N-protein buffer (15 mM Na2HPO4/5 mM NaH2PO4/0.25 M NaCl, pH 7.5); S-protein buffer (2 mM Tris/200 mM NaCl, pH 8.0); 1%/100% human saliva.
- Primary endpoint: Selective nIR fluorescence modulation (ΔF/F) to N vs S vs BSA; LOD.
- Secondary endpoints: Hill-equation kinetics; saliva-matrix performance; optode field readout.
- QC criteria: BSA interferent control; UV-vis-nIR individualization check; top-80% dispersion selection.
- Failure / exclusion criteria: S-protein sensor response diminished in saliva (reported negative result).
- Exact reusable parameters and source location: Full dispersion + screening + optode protocol in Experimental Section (reusable as a CoPhMoRe workflow).

# Computational and statistical methods
- Raw input: nIR emission spectra (950-1250 nm); ΔF/F responses.
- Preprocessing: Integrated nIR intensity ratios (post/pre injection).
- Statistical model: Hill-equation cooperative-binding fits (R² = 0.998 N, 0.980 S); positive cooperativity (n: 1.12 S; values reported); proportionality/Kd parameters reported.
- LOD: 48-49 fM (N) and 350 pM (S); computed as buffer-noise + 3× signal.
- Effect-size reporting: ΔF up to 50-71% (N), 40-45% (S); saliva +N response 45.4% (100% saliva), optode 85.7% (+) vs 30% (background).
- Validation strategy: BSA interferent; saliva matrix; optode integration; clinical-range comparison (saliva N protein 10^? pg/mL; sensor LOD 2.4 pg/mL covers clinical range).
- Software and versions: N/A (analytical).
- Code availability: N/A.

# Data and resource availability
- Repository and accession: None (ACS paper; data in figures/SI).
- Raw data available: Not deposited (SI tables only).
- Processed data available: In-paper.
- Metadata completeness: Reagent/instrument details complete in Experimental Section.
- Data-use restrictions: N/A.
- Reusability for the user's work: **High as a protocol/workflow** (corona-library screen → lead selection → biofluid validation → optode); not a reusable dataset.

# Main findings
| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| CoPhMoRe SWCNT detect SARS-CoV-2 N and S proteins antibody-free via nIR fluorescence | Reported | Results | ΔF up to 50% (N), 40% (S) in <5 min | Yes | Recombinant proteins |
| LOD 48-49 fM (N) and 350 pM (S) | Reported | Results | from Hill-fit + 3× noise | Yes | Buffer-based LOD |
| Lead sensors selective vs BSA interferent | Reported | Results | BSA near-zero response | Yes | Single interferent tested |
| N-protein sensing preserved in 100% human saliva (45.4% ΔF); S-protein sensing diminished in saliva | Reported | Results | N robust; S attenuated (glycoprotein fouling hypothesis) | Yes | Important negative result for S |
| Fiber-optic optode gives field readout: +SARS-CoV-2 85.7% vs 30% saliva background; τ=5.1 min | Reported | Results | statistically significant | Yes | Background saliva quench unexplained |
| CoPhMoRe enables rapid sensor development (full screen in ~6 days) | Reported | Results | 44 corona phases / 11 backbones | Yes | Workflow advantage |

# What is actually new?
- Methodological novelty: Antibody-free CoPhMoRe sensor for a viral target with a deployable optode and a documented rapid-development workflow.
- Biological novelty: N-protein detection robust in 100% saliva (phosphorylated N unaffected by glycoproteins), unlike glycosylated S.
- Dataset or resource novelty: Reusable corona-library screening + dispersion/QC + optode protocol.
- What was already known: PEG-phospholipid SWCNT detect proteins in biofluids; CoPhMoRe concept.

# Strengths
- Design strength: Full corona-library screen with interferent control; lead selection by specificity.
- Validation strength: Biofluid (100% saliva) validation; Hill-equation kinetics; clinical-range comparison; optode demo.
- Reproducibility strength: Detailed dispersion/QC, instrument settings, buffers, 3D-print parameters.
- Translational realism: Saliva matrix; portable optode; low sample volume (<10 µL).

# Limitations and bias risks
- Sample-size / power: Analytical replicates; no patient cohort (recombinant proteins + pooled saliva).
- Confounding: Saliva background quenching (origin unclear); single SWCNT batch.
- Batch / site effects: One SWCNT batch — batch-to-batch reproducibility not tested.
- Pseudoreplication risk: N/A.
- Leakage / overfitting risk: N/A.
- Generalizability: Viral proteins, not neuro biomarkers; S sensor fails in saliva.
- Missing controls / validation: Limited interferent panel (BSA only); no clinical patient samples; no inter-donor saliva variability (donor-aware validation absent).
- Author-stated limitations: Development timeline may extend if no commercial polymer suffices; saliva background mechanism unexplored.
- Additional limitations identified during review: No deposited data; single-batch SWCNT; donor-aware/leakage-resistant validation not performed (relevant to signals-file emphasis).

# Transferability to the user's work
- Directly transferable elements: CoPhMoRe corona-library screening workflow; PEG-phospholipid/SWCNT dispersion + QC (probe sonication, 30,300 RCF, top-80%, UV-vis-nIR individualization, MPA surface-area); BSA interferent control; nIR microscope + optode settings; 3D-print tip parameters.
- Elements requiring adaptation: Retarget corona library to a neuro/biofluid biomarker; add donor-aware validation and broader interferent panels.
- Model, species, tissue, matrix, platform, or scale mismatch: Saliva/viral vs serum/CSF/neuro biomarkers.
- Assumptions required for transfer: Access to corona-phase library + nIR instrumentation.
- Confidence: high for the workflow; moderate for a new analyte target.

# Practical implications
- Experimental implication: Adopt the corona-library screen + dispersion QC + interferent control as a sensor-development template.
- Analysis implication: Use Hill-equation fits for kinetics/LOD; report buffer-noise-based LOD; test in the actual biofluid early.
- Public dataset implication: None (no deposit).
- Biomarker / translational implication: Antibody-free optical biofluid sensing feasible; matrix effects (glycoprotein fouling) must be screened per analyte.
- Grant / manuscript implication: Citable CoPhMoRe precedent with biofluid validation and deployable readout.

# Contradictions and links
- Supports: PEG-phospholipid SWCNT biofluid sensing; CoPhMoRe selectivity.
- Contradicts: Assumption that all corona sensors transfer to biofluid equally (S-protein sensor fails in saliva).
- Replicates: Prior CoPhMoRe cooperative-binding behavior.
- Methodologically comparable papers: Yoon 2025 (CoPhMoRe uric acid in urine, paper strip); Lee 2025 (SWCNT optical patch sensor, ultralow-volume biofluid); Dewey 2024 (SWCNT nanosensor review).
- Relevant synthesis notes: candidate seed for "SWCNT corona-phase biofluid sensing: matrix effects & QC" synthesis.
- Relevant project decisions: (none yet)

# Follow-up actions
- [ ] Inspect SI for saliva sourcing, full library responses, and donor variability
- [ ] Note absence of donor-aware/leakage-resistant validation when comparing across biosensor papers
- [ ] Cross-link with Yoon 2025 and Lee 2025 in a corona-phase biofluid synthesis
- [ ] Check retraction/correction status

# Priority decision
- Priority: 1
- Read now (retain for methods)
- Rationale: Canonical, detailed CoPhMoRe biofluid-validated SWCNT sensor with a fully reusable development/QC workflow and an honest negative result (S in saliva); directly seeds the biosensor domain and the corona-phase methods line. Priority 1 for methods value despite the non-neuro target.
