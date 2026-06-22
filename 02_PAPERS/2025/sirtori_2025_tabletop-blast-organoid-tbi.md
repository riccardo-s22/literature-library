---
record_type: paper
record_status: verified
canonical_id: "10.1016/j.crmeth.2025.101213"
doi: "10.1016/j.crmeth.2025.101213"
pmid: "41187748"
pmcid: "PMC12664893"
title: "A tabletop blast device for the study of the long-term consequences of traumatic brain injury on brain organoids"
year: 2025
source_type: method
peer_reviewed: true
full_text_checked: true
supplement_checked: false
code_checked: false
data_checked: false
last_verified: 2026-06-22
priority: 1
projects: []
topics: [neurodegeneration, TBI, ALS, AD_ADRD, mechanobiology, organoid]
methods: [organoid, controlled_exposure, imaging]
datasets: []
---

# Citation
- Full citation: Sirtori R, Pandey A, Shukla A, Fallini C. "A tabletop blast device for the study of the long-term consequences of traumatic brain injury on brain organoids." *Cell Reports Methods* 2025;5(11):101213.
- DOI / PMID / stable URL: [DOI](https://doi.org/10.1016/j.crmeth.2025.101213) · PMID 41187748 · PMC12664893
- Related preprint or published version: Peer-reviewed (Cell Rep Methods). The authors cite a related pre-print of their own on LINC-complex mechanical strain and DNA damage (not yet identified here).
- Correction, expression of concern, or retraction status: **Unknown** — not checked (added 2026-06-22).

*Source: metadata + full text retrieved from PubMed / PubMed Central. According to PubMed, DOI [10.1016/j.crmeth.2025.101213](https://doi.org/10.1016/j.crmeth.2025.101213).*

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Provides a **low-cost, calibrated, tunable blast/pressure-wave device** to deliver reproducible mechanical injury to free-floating human iPSC cortical brain organoids (cBOs), with documented downstream neurodegenerative readouts (caspase-3, MAP2 loss, pTau aggregation, TDP-43 nuclear depletion + cryptic exon de-repression in STMN2/UNC13A/HDGFL2, γH2A.X DNA damage, reduced pCREB/PKA). Directly relevant as a **methods/protocol precedent** for an organoid TBI/blast injury model and as a bridge between mechanobiology (force calibration) and TDP-43/tau proteinopathy.
- Why it is more or less useful than neighboring literature: Unlike high-intensity focused ultrasound, piezoelectric/pneumatic actuators, or microfluidic shear systems, this device is gravity-based, cheap, portable, and tunable (drop height → peak pressure; drop-weight length → impulse). It explicitly cross-validates against a published computer-controlled pressure chamber (cf. Silvosa 2022) and against rodent/human FE intracranial-pressure simulations. From the same group as the user (URI / Fallini lab) — high practical relevance.

# Source inspection status
- Abstract inspected: yes
- Full text inspected: yes (PMC full text, including STAR Methods)
- Methods inspected: yes (device assembly, calibration, injury delivery, IF, WB, statistics)
- Supplement inspected: no (figures/supplementary referenced but not viewed)
- Figures/tables inspected: no (Key Resources Table read; figure panels not viewed)
- Code repository inspected: no (paper reports no original code)
- Data repository inspected: no (data shared "upon request" — no accession)
- Missing material: figure panels; supplementary measurements/drawings of the device; exact n per experiment (stated to be in figure legends, not extracted).

# Study question and hypothesis
- Primary question: Can a simple, low-cost tabletop blast device deliver reproducible, tunable pressure waves to human brain organoids and recapitulate the acute and chronic neurodegenerative consequences of blast TBI (bTBI)?
- Stated hypothesis: A gravity-driven impact device producing a calibrated compressive pressure pulse can model bTBI-linked neurodegeneration in cBOs comparably to more complex/expensive systems.
- Study type: Methods/feasibility study (device development + biological validation), case (injured) vs sham control, in vitro human organoid model.

# Biological or clinical context
- Disease / exposure / process: Blast traumatic brain injury (bTBI); downstream TDP-43 proteinopathy, tau phosphorylation/aggregation, DNA damage, CREB pathway suppression.
- Organism: Human (iPSC-derived).
- Tissue / cell type: Cortical brain organoids (cBOs) — deep-layer CTIP2+ and upper-layer SATB1+ cortical neurons (MAP2+), astrocytes by ~3 months.
- Model system: Free-floating human iPSC cortical brain organoids, ~90 days in culture at injury.
- Cohort or population: Two independent control iPSC lines — "2a" (Ababneh et al.) and c52iso (Cedars-Sinai CS52iALS-C9n6.ISOC3, an isogenic control).
- Relevant stage, age, sex, genotype, severity: cBOs matured 90 days; peak pressure used 0.9–1.2 MPa, impulse 0.6 MPa (70 mm drop weight, 6 mm drop height) — modeling non-lethal blast.

# Study design
- Experimental or observational unit: Individual organoid / experimental batch (n = biological replicates, stated in figure legends — not extracted).
- Unit of inference: Organoid-level (injured vs sham).
- Groups and sample size per group: Injured vs sham; exact n **Unknown** (per-figure legends, not inspected). Data from both iPSC lines aggregated for final WB analysis.
- Biological replicates: Independent organoids / batches (count Unknown).
- Technical replicates: Calibration: 3 replicate drops per height per weight.
- Randomization: Not described.
- Blinding: Not described.
- Inclusion / exclusion criteria: Not described.
- Batch structure: Two iPSC lines; results aggregated.
- Longitudinal / paired / donor structure: Acute (24 h) and long-term (7 days post-injury) timepoints.
- Controls and comparators: Sham organoids — identical handling/loading into device but spacer not removed (no impact). Cross-comparison to published pressure-chamber method (Silvosa 2022) and FE intracranial-pressure models.

# Experimental methods
- Assay / platform: Custom gravity-driven tabletop blast device (drop weight → aluminum plug/piston → liquid-filled cavity → free-floating organoids); pressure measured with PCB Piezotronics ICP 113B22 sensor → 482C signal conditioner → Tektronix MSO2024 oscilloscope (sample rate 50 MS/s). Readouts: immunofluorescence (Leica DMi8 Thunder, 20x/63x, deconvolution Autoquant X3, Fiji MFI), western blot (LI-COR Odyssey; detergent-soluble vs urea-soluble fractionation).
- Sample preparation: cBOs from 2 iPSC lines, dual-SMAD-style patterning (Dorsomorphin/SB-431542), matured 90 days; injury delivered free-floating in medium inside sealed chamber.
- Dose, concentration, force, exposure, or perturbation: Peak pressure 0.9–1.2 MPa, specific impulse 0.6 MPa, via 70 mm drop weight at 6 mm drop height. Calibration range: drop heights 2–10 mm (2 mm steps), short (70 mm) vs long (215 mm) drop weights; P and I scale with drop height by power-law fit; impulse increases with drop-weight length while first-peak P depends only on drop height.
- Timing and sampling schedule: Collection at 24 h (acute) and 7 days (long-term) post-injury.
- Matrix / medium / substrate / environmental conditions: Organoids free-floating in maturation medium in liquid-filled aluminum cavity; air bubbles excluded for repeatability; device sterilized (autoclave or 70% EtOH).
- Primary endpoint: Acute neuronal death (cleaved caspase-3 in MAP2+ cells; MAP2 loss).
- Secondary endpoints: pTau (Ser202/Thr205) insoluble accumulation; TDP-43 nuclear depletion + ~50% solubility shift; STMN2/UNC13A reduction; HDGFL2 cryptic-exon isoform detection; γH2A.X DNA-damage increase; pCREB/PKA reduction.
- QC criteria: No air bubbles in chamber; secondary rebound pressure pulse (~10% of first peak) ignored.
- Failure or exclusion criteria: Not described.
- Exact reusable parameters and source location: Device assembly + calibration protocol in STAR Methods; injury delivery 6-step protocol; IF (10 µm cryosections, 0.21 µm Z-step) and WB (30 µg protein, 4–20% Tris-Glycine, RIPA + 8M urea fractionation) protocols fully specified in STAR Methods.

# Computational and statistical methods
- Raw input: Pressure-time traces; IF MFI; WB band intensities.
- Preprocessing: IF adaptive blind deconvolution (10 iterations, Autoquant X3); WB band quantification in ImageJ.
- Normalization: Not detailed (WB likely loading-control normalized — GAPDH/H3 antibodies listed).
- Statistical test or model: Normality by D'Agostino & Pearson omnibus; parametric (Student's t-test) if normal, non-parametric otherwise; significance p < 0.05; data as mean ± SD.
- Multiple-testing correction: Not described.
- Effect-size reporting: Qualitative/relative (e.g., "~50% shift of TDP-43"); exact effect sizes per figure legends (not extracted).
- Batch handling: Data from both iPSC lines aggregated.
- Validation strategy: Replication of previously published organoid-bTBI phenotypes; cross-comparison of pressure profile to published chamber method and FE intracranial-pressure simulations.
- External validation: Conceptual comparison to literature; no independent external dataset.
- Software and versions: Autoquant X3 (Media Cybernetics), Fiji/ImageJ (NIH), Prism 9 (GraphPad). Exact sub-versions Unknown.
- Code availability: Paper reports **no original code**.

# Data and resource availability
- Repository and accession: None. Data (IF raw images, WB images, pressure measurements) shared **upon request** to the lead contact (C. Fallini); no public accession.
- Raw data available: Upon request only.
- Processed data available: Upon request only.
- Metadata completeness: N/A (no deposited dataset).
- Data-use restrictions: Request-gated.
- Reusability for the user's work: **High as a protocol/device** (fully specified, low-cost, tunable); low as a reusable public dataset (no deposit).

# Main findings
| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| Device generates reproducible, tunable pressure waves; peak P depends on drop height, impulse on drop-weight length | Reported | Results (calibration) / Fig.2 | P and I scale with drop height by power-law; 3 reps/height | Yes | Figures not viewed; absolute P/I curve coefficients not extracted |
| Blast (0.9–1.2 MPa, 0.6 MPa impulse) induces acute neuronal death | Reported | Results / Fig.3 | ↑ caspase-3 in MAP2+ cells at 24 h; MAP2 ↓ at 1 wk | Yes | Exact n / effect size in figure legend (not extracted) |
| Deep-layer (CTIP2+) neurons more susceptible than upper-layer (SATB1+) | Reported | Results / Fig.3 | CTIP2 ↓, SATB1 unchanged | Yes | Consistent with prior reports |
| Blast causes pTau insoluble accumulation and ~50% TDP-43 solubility shift + nuclear depletion | Reported | Results / Fig.4 | pTau in insoluble fraction only; ~50% TDP-43 shift to urea-soluble | Yes | Quantification per figure |
| TDP-43 dysfunction de-represses cryptic exons (STMN2/UNC13A ↓, HDGFL2 cryptic isoform detected) | Reported | Results / Fig.4 | UNC13A loss correlates with TDP-43 nuclear depletion | Partial | Protein-level; splicing inferred from protein readouts |
| Blast increases DNA damage (γH2A.X) and reduces pCREB/PKA at 7 days | Reported | Results / Fig.5 | ↑ γH2A.X, ↓ pCREB & PKA | Yes | Novel readouts in human organoid bTBI |

# What is actually new?
- Biological novelty: First demonstration (per authors) of persistent γH2A.X DNA damage and reduced CREB/PKA pathway activity in a human organoid bTBI model 1 week post-injury.
- Methodological novelty: A low-cost, gravity-driven, tunable tabletop blast device for organoids, replacing expensive HIFU/piezoelectric/microfluidic systems.
- Dataset or resource novelty: A reusable, fully-specified device/protocol (not a deposited dataset).
- What was already known: TBI as risk factor for tau/TDP-43/amyloid pathology; deep-layer neuron vulnerability; TDP-43 cryptic-exon de-repression (STMN2/UNC13A/HDGFL2) — replicated here.

# Strengths
- Design strength: Two independent iPSC lines (incl. isogenic control); calibrated, characterized pressure waveform; sham handled identically.
- Validation strength: Replicates multiple published bTBI phenotypes; pressure profile cross-checked against chamber method and FE models.
- Reproducibility strength: Full STAR Methods incl. device build, calibration curves, and antibody RRIDs; air-bubble QC.
- Translational realism: Human iPSC organoids; peak P consistent with non-lethal human-skull intracranial pressure estimates.

# Limitations and bias risks
- Sample-size / power: Exact n not extracted (in figure legends); feasibility-scale study.
- Confounding: Free-floating organoids → variable pressure loading per organoid; in vitro–in vivo correspondence uncertain (author-stated).
- Batch / site effects: Two iPSC lines aggregated; line-specific effects not separately reported.
- Pseudoreplication risk: If multiple organoids per batch counted as independent, verify n-definition (stated as independent organoids or batches).
- Leakage / overfitting risk: N/A (no ML).
- Generalizability: Models closed/blast TBI only — cannot model blunt-impact/penetrating TBI (author-stated); free-floating loading not equivalent to in-vivo skull mechanics.
- Missing controls / validation: No in-vivo cross-validation (author recommends animal/postmortem validation).
- Author-stated limitations: In-vitro vs in-vivo pressure correspondence unresolved; device build needs specialized fabrication; cannot model blunt impact.
- Additional limitations identified during review: No deposited data/accession; effect sizes not extractable from text alone; blinding/randomization not described.

# Transferability to the user's work
- Directly transferable elements: The whole device + calibration + injury-delivery protocol; the readout panel (caspase-3/MAP2, pTau, TDP-43 solubility/localization, STMN2/UNC13A/HDGFL2, γH2A.X, pCREB/PKA); IF and WB fractionation protocols with RRIDs.
- Elements requiring adaptation: Pressure/impulse tuning to a desired injury severity; organoid immobilization if reduced variability is needed.
- Model, species, tissue, matrix, platform, or scale mismatch: Free-floating cBO loading vs in-vivo skull mechanics; closed/blast only.
- Assumptions required for transfer: Access to machine-shop fabrication; comparable organoid maturation.
- Confidence: high (this is the user's own group's published protocol).

# Practical implications
- Experimental implication: Adoptable bench protocol for reproducible organoid bTBI with tunable dose; directly supports a blast-TBI organoid project.
- Analysis implication: Pair with snRNA-seq/splicing readouts (cf. Ruf 2026) to map cell-type-specific cryptic-exon responses to calibrated injury.
- Public dataset implication: No deposited dataset — consider depositing future data; cannot serve as external validation cohort.
- Biomarker / translational implication: HDGFL2/STMN2/UNC13A cryptic events as injury biomarkers in a human model.
- Grant / manuscript implication: Citable, calibrated human organoid bTBI platform with cost/accessibility advantage.

# Contradictions and links
- Supports: TDP-43/tau proteinopathy as downstream of mechanical brain injury; deep-layer cortical neuron vulnerability.
- Contradicts: (none identified)
- Replicates: Prior organoid bTBI pTau/TDP-43/cryptic-exon phenotypes; rodent CREB-suppression and DNA-damage findings (now in human organoids).
- Methodologically comparable papers: Silvosa 2022 (computer-controlled pressure chamber on cerebral organoids — cross-compared here); Braun 2021 (calibrated stretch device, tau pathology); Ruf 2026 (cell-type TDP-43/cryptic exons — complementary readout layer).
- Relevant synthesis notes: candidate seed for "calibrated mechanical injury → TDP-43/tau proteinopathy" synthesis.
- Relevant project decisions: (none yet — no project created)

# Follow-up actions
- [ ] Inspect figures + supplementary device drawings to extract exact P/I calibration coefficients and per-experiment n
- [ ] Identify the cited companion LINC-complex pre-print
- [ ] Consider depositing or linking future organoid datasets generated with this device
- [ ] Cross-link with Silvosa 2022 and Braun 2021 in a mechanobiology→proteinopathy synthesis
- [ ] Check retraction/correction status

# Priority decision
- Priority: 1
- Read now (and retain for methods)
- Rationale: Directly transferable, peer-reviewed, low-cost calibrated bTBI organoid protocol from the user's own group, bridging mechanobiology and TDP-43/tau proteinopathy; the only gaps (figure-level n/effect sizes) are minor follow-ups.
