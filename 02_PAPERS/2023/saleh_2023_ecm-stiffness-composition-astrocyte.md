---
record_type: paper
record_status: verified
canonical_id: "10.3390/jfb14050256"
doi: "10.3390/jfb14050256"
pmid: "37233366"
title: "Xeno-Free Biomimetic ECM Model for Investigation of Matrix Composition and Stiffness on Astrocyte Cell Response"
year: 2023
source_type: primary
peer_reviewed: true
full_text_checked: true
supplement_checked: false
code_checked: false
data_checked: false
last_verified: 2026-06-22
priority: 2
projects: []
topics: [mechanobiology, nanomaterials, neurodegeneration]
methods: [ex_vivo, imaging, controlled_exposure]
datasets: []
---

# Citation
- Full citation: Saleh BM, Pourmostafa A, Patrawalla NY, Kishore V. "Xeno-Free Biomimetic ECM Model for Investigation of Matrix Composition and Stiffness on Astrocyte Cell Response." *Journal of Functional Biomaterials* 2023;14(5):256.
- DOI / PMID / stable URL: [DOI](https://doi.org/10.3390/jfb14050256) · PMID 37233366
- Related preprint or published version: Peer-reviewed (J Funct Biomater, MDPI; open access, CC-BY).
- Correction, expression of concern, or retraction status: **Unknown** — not checked (added 2026-06-22).

*Source: WebFetch of PMC full-text page (PMC10218816) + metadata. According to PubMed, DOI [10.3390/jfb14050256](https://doi.org/10.3390/jfb14050256).*

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Fills the Domain-4 **ECM stiffness/composition → glial state** sub-theme with a tunable, **xeno-free** brain-mimetic hydrogel and human astrocytes. Provides exact, reusable matrix formulations and a brain-relevant stiffness range (0.2–1.2 kPa vs native 0.5–1 kPa), with astrocyte-activation readouts (spreading, GFAP↑, ALDH1L1↓). A practical recipe for the user's neural-ECM / astrogliosis models, complementing the alginate-ECM seed record (carvalho_2023) and BBB-on-chip astrogliosis record (chen_2025).
- Why it is more or less useful than neighboring literature: More directly usable than carvalho_2023 (full text inspected here; explicit compositions + stiffness + astrocyte markers) and disentangles **composition vs stiffness** effects. Limited to 2D-on/within-hydrogel astrocyte response without mechanical loading (static), so a foundation rather than an injury model.

# Source inspection status
- Abstract inspected: yes
- Full text inspected: yes (via PMC full-text page summary)
- Methods inspected: partial (compositions, stiffness, cell source, key readouts; full rheology/IF protocols not line-by-line)
- Supplement inspected: no
- Figures/tables inspected: no
- Code repository inspected: n/a
- Data repository inspected: n/a
- Missing material: exact rheology protocol, full IF quantification tables, replicate-level stats.

# Study question and hypothesis
- Primary question: How do ECM composition (collagen I vs hyaluronic acid content) and stiffness independently affect human astrocyte response in a xeno-free brain-mimetic hydrogel?
- Stated hypothesis: Composition and stiffness jointly regulate astrocyte spreading, metabolic activity, and activation markers.
- Study type: In vitro biomaterials / mechanobiology study.

# Biological or clinical context
- Disease / exposure / process: Astrocyte activation / reactive astrogliosis (neural ECM mechanobiology).
- Organism: Human.
- Tissue / cell type: Normal human astrocytes (NHA, passage 4, Lonza).
- Model system: Photocrosslinkable hydrogel (human skin-derived collagen type I + thiolated hyaluronic acid crosslinked with PEGDA).
- Cohort or population: N/A (cell line).
- Relevant stage/severity: N/A.

# Study design
- Experimental or observational unit: Hydrogel construct.
- Unit of inference: Construct/condition-level astrocyte response.
- Groups and sample size per group: Four collagen–HA–PEGDA compositions (mg/mL): 6-6-5, 6-12-5, 12-6-5, 12-12-5. N=6–12 hydrogels per group across timepoints.
- Biological replicates: N=6–12 constructs/group (cell-line-based; donor diversity N/A).
- Technical replicates: Not extracted.
- Randomization / blinding: Not extracted.
- Inclusion / exclusion criteria: Not extracted.
- Batch structure: Not extracted.
- Controls and comparators: Across compositions; stiffness gradient 0.2–1.2 kPa.

# Experimental methods
- Assay / platform: Hydrogel fabrication + rheology (stiffness); immunofluorescence (GFAP, ALDH1L1); cell spreading morphometry; metabolic activity assay.
- Sample preparation: NHA encapsulated/seeded in photocrosslinked collagen-HA-PEGDA hydrogels.
- Dose / force / perturbation: No external mechanical loading (static stiffness/composition variation).
- Timing / sampling schedule: Multiple timepoints (specific days not extracted).
- Matrix: Xeno-free collagen I + thiolated HA + PEGDA; stiffness 0.2–1.2 kPa (brain-mimetic 0.5–1 kPa).
- Primary endpoint: Astrocyte spreading, metabolic activity, GFAP/ALDH1L1 expression vs composition/stiffness.
- Secondary endpoints: Composition (HA content) effect on growth suppression.
- QC criteria: Not extracted.
- Exact reusable parameters and source location: Four exact compositions (above); stiffness range; cell source/passage — Methods/Results.

# Computational and statistical methods
- Raw input: Imaging/metabolic readouts.
- Statistical test or model: Group comparisons across compositions/timepoints (test not extracted).
- Multiple-testing correction: Not extracted.
- Effect-size reporting: Qualitative directional (softer/collagen-rich → more spreading, GFAP↑, ALDH1L1↓; higher HA → suppressed growth).
- Validation strategy: Multiple compositions + replicates.
- External validation: None.
- Software / versions: Not extracted.
- Code availability: N/A.

# Data and resource availability
- Repository and accession: N/A (no sequencing/imaging deposit noted).
- Raw/processed data available: Within paper/figures (CC-BY).
- Metadata completeness: Moderate.
- Data-use restrictions: Open access (CC-BY).
- Reusability for the user's work: High — directly reusable hydrogel formulations + stiffness range + astrocyte-activation readouts.

# Main findings
| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| Stiffness tunable 0.2–1.2 kPa across compositions (brain-mimetic) | Reported | Results/rheology | 0.2–1.2 kPa | Yes | static stiffness |
| Softer, collagen-rich (low HA) hydrogels promote astrocyte spreading + metabolic activity | Reported | Results | qualitative directional | Yes | N=6–12/group |
| Higher HA content suppresses astrocyte growth | Reported | Results | qualitative | Yes | — |
| Soft hydrogels trigger astrocyte activation (spreading↑, GFAP↑, ALDH1L1↓) | Reported | Results/IF | marker-level | Yes | activation inferred from markers |

# What is actually new?
- Biological novelty: Disentangles composition vs stiffness effects on human astrocyte activation in a xeno-free system.
- Methodological novelty: Xeno-free, tunable collagen-I/thiolated-HA/PEGDA brain-mimetic hydrogel.
- Dataset/resource novelty: Reusable formulation matrix.
- What was already known: Stiffness modulates astrocyte reactivity (general); HA influences glial behavior.

# Strengths
- Design strength: Factorial composition × stiffness; replicates (N=6–12).
- Validation strength: Multiple readouts (morphology, metabolism, markers).
- Reproducibility strength: Exact compositions + open access.
- Translational realism: Human astrocytes; brain-relevant stiffness; xeno-free.

# Limitations and bias risks
- Sample-size / power: Moderate (N=6–12 constructs); single cell source (NHA).
- Confounding: Composition and stiffness partially covary (addressed by factorial design but not fully orthogonal).
- Batch / site effects: Not described.
- Pseudoreplication risk: Constructs from one cell lot — donor generalization limited.
- Leakage / overfitting risk: N/A.
- Generalizability: Single human astrocyte source; static (no injury loading).
- Missing controls / validation: No in vivo / multi-donor validation.
- Author-stated limitations: Not extracted.
- Additional limitations identified during review: GFAP↑/ALDH1L1↓ interpreted as activation — orthogonal functional confirmation limited.

# Transferability to the user's work
- Directly transferable elements: Hydrogel recipes; brain-mimetic stiffness range; astrocyte-activation marker panel (GFAP/ALDH1L1).
- Elements requiring adaptation: Add mechanical loading for injury models; multi-donor astrocytes; 3D vs 2D.
- Mismatch: Static model vs the user's injury/blast emphasis.
- Assumptions required for transfer: Comparable crosslinking/rheology.
- Confidence: high (as a substrate/readout template).

# Practical implications
- Experimental implication: Use these formulations to set brain-relevant stiffness and tune astrocyte reactivity baseline before applying injury.
- Analysis implication: Report composition AND stiffness; use GFAP/ALDH1L1 + morphometry + metabolism.
- Public dataset implication: N/A.
- Biomarker / translational implication: GFAP/ALDH1L1 as activation readouts in engineered ECM.
- Grant / manuscript implication: Methods citation for xeno-free neural-ECM substrate.

# Contradictions and links
- Supports: Stiffness/composition control of astrocyte reactivity (cf. chen_2025 astrogliosis; carvalho_2023 alginate-ECM).
- Contradicts: none identified.
- Replicates: General stiffness–reactivity relationship.
- Methodologically comparable papers: carvalho_2023 (alginate ECM), chen_2025 (BBB-on-chip astrogliosis), braun_2021 (mechanical tau).
- Relevant synthesis notes: seed for "ECM stiffness/composition → glial state."
- Relevant project decisions: (none yet)

# Follow-up actions
- [ ] Extract exact rheology + IF quantification and statistics from full text/figures
- [ ] Pair with a mechanically-loaded model (e.g., compression/blast) for injury context
- [ ] Cross-link with carvalho_2023 and chen_2025
- [ ] Check correction/retraction status

# Priority decision
- Priority: 2
- Retain for methods (substrate + readouts)
- Rationale: Directly reusable xeno-free neural-ECM formulations with brain-relevant stiffness and astrocyte-activation readouts; static (no injury loading) keeps it P2 rather than P1.
