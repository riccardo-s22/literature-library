---
record_type: paper
record_status: verified
canonical_id: "10.1038/s41593-020-00764-7"
doi: "10.1038/s41593-020-00764-7"
pmid: "33432193"
pmcid: "PMC7854528"
title: "Molecular characterization of selectively vulnerable neurons in Alzheimer's disease"
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
topics: [neurodegeneration, AD_ADRD, aging, single_cell, transcriptomics]
methods: [snRNAseq, imaging]
datasets: []
---

# Citation
- Full citation: Leng K, Li E, Eser R, Piergies A, Sit R, Tan M, Neff N, Li SH, Rodriguez RD, Suemoto CK, Leite REP, Ehrenberg AJ, Pasqualucci CA, Seeley WW, Spina S, Heinsen H, Grinberg LT, Kampmann M. "Molecular characterization of selectively vulnerable neurons in Alzheimer's disease." *Nature Neuroscience* 2021;24(2):276-287.
- DOI / PMID / stable URL: [DOI](https://doi.org/10.1038/s41593-020-00764-7) · PMID 33432193 · PMC7854528
- Related preprint or published version: Peer-reviewed (Nat Neurosci). A bioRxiv preprint preceded it (not separately verified here).
- Correction, expression of concern, or retraction status: **Unknown** — not checked (added 2026-06-22).

*Source: metadata + PMC full text retrieved from PubMed / PubMed Central. According to PubMed, DOI [10.1038/s41593-020-00764-7](https://doi.org/10.1038/s41593-020-00764-7).*

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Establishes **RORB+ excitatory neurons in entorhinal cortex (EC) layer II as selectively vulnerable in AD**, validated histologically, and identifies a homeostatically-impaired reactive astrocyte subpopulation. Foundational reference for cell-type-specific vulnerability and for the RORB marker (note: RORB also appears among vulnerable subtypes in Ruf 2026's ALS motor cortex). Methods precedent for cross-sample alignment (scAlign) to define disease-independent subpopulations before testing abundance shifts.
- Why it is more or less useful than neighboring literature: A landmark, highly-cited snRNA-seq vulnerability study with orthogonal quantitative neuropathology validation in an independent, larger cohort — stronger validation than DE-only snRNA-seq AD studies. Limitation: small sequencing cohort (10 individuals), APOE-matched (ε3/ε3) by design.

# Source inspection status
- Abstract inspected: yes
- Full text inspected: yes (PMC full text, ~60k chars)
- Methods inspected: partial (cohort, alignment, QC, statistics extracted; full wet-lab/seq parameters in supplement not viewed)
- Supplement inspected: no
- Figures/tables inspected: no (figure callouts read; panels not viewed)
- Code repository inspected: no
- Data repository inspected: no (Data Availability section not present in retrieved PMC text — **accession not verified**)
- Missing material: GEO/accession for snRNA-seq; exact sequencing chemistry/version; supplementary cohort table.

# Study question and hypothesis
- Primary question: Which neuronal populations are selectively vulnerable across the progression of AD-type tau neurofibrillary pathology, and what are their molecular signatures?
- Stated hypothesis: Specific neuronal subpopulations are selectively depleted with tau pathology progression; their molecular identity can be resolved by snRNA-seq with disease-independent subpopulation definition.
- Study type: Cross-sectional human post-mortem snRNA-seq + orthogonal quantitative neuropathology validation.

# Biological or clinical context
- Disease / exposure / process: Alzheimer's disease; tau neurofibrillary pathology (Braak staging).
- Organism: Human.
- Tissue / cell type: Entorhinal cortex (EC, mid-uncus) and superior frontal gyrus (SFG, BA8); nuclei across excitatory/inhibitory neurons, astrocytes, oligodendrocytes, OPCs, microglia, endothelial cells.
- Model system: Human post-mortem brain tissue.
- Cohort or population: snRNA-seq: 10 male APOE ε3/ε3 individuals spanning Braak 0, 2, 6. Validation: independent cohort of 26 individuals spanning Braak 0–6, devoid of non-AD neuropathology.
- Relevant stage, age, sex, genotype, severity: All-male, ε3/ε3 (to control genetic/sex confounders); Braak-staged.

# Study design
- Experimental or observational unit: Individual donor.
- Unit of inference: Donor-level, cell-type-subpopulation-resolved.
- Groups and sample size per group: snRNA-seq Braak 0 n=3, Braak 2 n=4, Braak 6 n=3 (per-region; total 10). Validation cohort n=26.
- Biological replicates: Donors per Braak stage (above).
- Technical replicates: Not extracted.
- Randomization: N/A (observational).
- Blinding: Not described in retrieved text (histology delineation by cytoarchitectonic criteria).
- Inclusion / exclusion criteria: ε3/ε3 male donors for snRNA-seq; validation cohort devoid of non-AD neuropathology; rigorous cytoarchitectonic EC delineation.
- Batch structure: Multiple individuals; technical/experimental factors mitigated by cross-sample alignment (scAlign).
- Longitudinal / paired / donor structure: Cross-sectional; matched EC + SFG per individual.
- Controls and comparators: Braak 0 (cortical-free) as control; progression contrast Braak 0 vs 2 vs 6.

# Experimental methods
- Assay / platform: snRNA-seq (droplet-based; exact chemistry not extracted). Validation: multiplex immunofluorescence (DAPI, TBR1, RORB, CP-13 phospho-tau Ser202) + Nissl overlay.
- Sample preparation: Nuclei extracted from frozen post-mortem EC and SFG (detailed protocol in supplement, not viewed).
- Dose / force / perturbation: N/A.
- Timing / sampling schedule: Single post-mortem timepoint.
- Matrix / conditions: Frozen post-mortem tissue.
- Primary endpoint: Relative abundance changes of cell-type subpopulations across Braak stages; identification of selectively vulnerable subpopulation.
- Secondary endpoints: DE genes per subpopulation across Braak; reactive astrocyte signature; histological validation of RORB+ depletion and tau co-localization.
- QC criteria: Standard snRNA-seq QC (recovered 42,528 EC + 63,608 SFG cells); details in supplement.
- Exact reusable parameters and source location: scAlign cross-sample alignment performed before clustering; analyses of gene expression use original (unaligned) data — key design pattern to avoid disease-driven clustering artifacts.

# Computational and statistical methods
- Raw input: snRNA-seq UMI counts (EC, SFG separately).
- Preprocessing / alignment: scAlign cross-sample alignment per region prior to clustering; clusters defined in alignment space, expression analyses on original data.
- Normalization / feature filtering: Standard (details in supplement, not extracted).
- Statistical test or model: Cell-type relative-abundance shifts tested by **beta regression**, multiple-testing corrected with **Holm's method**. DE between clusters and across Braak (method details in supplement).
- Multiple-testing correction: Holm (abundance); FDR for DE (not fully extracted).
- Effect-size reporting: Relative-abundance trends with p-values (e.g., EC excitatory neurons Braak 2 p=0.18, Braak 6 p=0.02; SFG excitatory Braak 6 p=0.05).
- Batch handling: scAlign removes individual-of-origin clustering effects (demonstrated vs un-aligned clustering).
- Validation strategy: Independent 26-donor histological validation of RORB+ depletion + tau co-localization.
- External validation: Compared to prior AD snRNA-seq (Mathys, Marinaro, Grubman).
- Software and versions: scAlign; others not extracted.
- Code availability: Not extracted from retrieved text.

# Data and resource availability
- Repository and accession: **Unknown — not present in retrieved PMC text.** snRNA-seq data was deposited (typical for Nat Neurosci) but the accession could not be confirmed here; verify on the Nature article page or GEO before citing.
- Raw data available: Likely (controlled or open) — unverified.
- Processed data available: Unverified.
- Metadata completeness: Supplementary cohort table not inspected.
- Data-use restrictions: Human post-mortem genomic data may be controlled — verify.
- Reusability for the user's work: Potentially high (EC/SFG AD snRNA-seq reference + RORB-vulnerability signature) **conditional on confirming accession**.

# Main findings
| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| RORB+ excitatory neurons in EC are selectively vulnerable in AD | Reported | Results / Fig. + Ext Data | snRNA-seq subpopulation depletion + histology | Yes | snRNA-seq cohort n=10 |
| Histological validation: RORB+ fraction of excitatory neurons drops with Braak progression | Reported | Results (26-donor validation) | Reduction in Braak 2-4 and 5-6 vs 0-1 | Yes | Independent cohort strengthens claim |
| Phospho-tau (CP-13) preferentially in RORB+ vs RORB- excitatory neurons | Reported | Results / IF | qualitative preferential co-localization | Yes | Subset of cases |
| EC excitatory neuron relative abundance declines with Braak stage | Reported | Results | Braak 6 p=0.02 (EC), SFG p=0.05 | Partial | Few significant after correction; trends |
| A reactive-like astrocyte subpopulation downregulates homeostatic genes | Reported | Results | qualitative signature | Yes | Subpopulation definition dependent |
| Inhibitory neuron subpopulations show no significant vulnerability | Reported | Results | no significant abundance change | Yes | Consistent with excitatory-selective tau vulnerability |

# What is actually new?
- Biological novelty: Molecular identity (RORB) of the long-known morphologically vulnerable EC layer II neurons; reactive astrocyte homeostatic-gene loss.
- Methodological novelty: scAlign cross-sample alignment to define disease-independent subpopulations before abundance testing; pairing snRNA-seq with rigorous cytoarchitectonic multiplex-IF validation.
- Dataset or resource novelty: EC + SFG AD-progression snRNA-seq (accession to confirm).
- What was already known: EC layer II stellate-neuron vulnerability (morphological); AD snRNA-seq DE studies without explicit vulnerability framing.

# Strengths
- Design strength: APOE ε3/ε3, all-male sequencing cohort controls major confounders; matched EC+SFG; alignment removes donor-driven clustering.
- Validation strength: Independent 26-donor quantitative neuropathology validation with tau co-localization — strong orthogonal confirmation.
- Reproducibility strength: Clear alignment-then-original-data analysis design.
- Translational realism: Human post-mortem, Braak-staged.

# Limitations and bias risks
- Sample-size / power: snRNA-seq n=10 (3/4/3 per stage) — modest; few abundance changes survive correction.
- Confounding: All-male ε3/ε3 limits generalization across sex/genotype (deliberate design tradeoff); PMI/agonal not extracted.
- Batch / site effects: Mitigated by scAlign; residual not fully characterized.
- Pseudoreplication risk: Many nuclei per donor — donor-level aggregation used for abundance (good).
- Leakage / overfitting risk: Subpopulation defined then tested for abundance — alignment design reduces circularity; DE still on same data.
- Generalizability: EC/SFG only; male ε3/ε3 only.
- Missing controls / validation: Histology validates RORB depletion (present).
- Author-stated limitations: EC heterogeneity; cross-sectional design cannot establish temporal causality.
- Additional limitations identified during review: Data accession not verifiable from retrieved text.

# Transferability to the user's work
- Directly transferable elements: RORB as a vulnerability marker; scAlign disease-independent subpopulation workflow; beta-regression for compositional abundance; multiplex-IF validation design.
- Elements requiring adaptation: Region (EC/SFG) and disease (AD) — if applied to ALS/TBI, vulnerable-subtype identity may differ (though RORB recurs in Ruf 2026 motor cortex).
- Model, species, tissue, matrix, platform, or scale mismatch: AD cortex vs other neurodegeneration/regions.
- Assumptions required for transfer: Comparable nuclei QC; donor-level compositional modeling.
- Confidence: moderate-high.

# Practical implications
- Experimental implication: Use RORB+ marker and EC cytoarchitectonic delineation for vulnerability studies; pair snRNA-seq with multiplex-IF validation.
- Analysis implication: Adopt scAlign-then-original-data and beta-regression compositional testing with Holm/FDR.
- Public dataset implication: Candidate AD snRNA-seq reference — verify accession first.
- Biomarker / translational implication: RORB+ EC neuron loss as an early vulnerability axis.
- Grant / manuscript implication: Citable foundation for cell-type-specific tau vulnerability.

# Contradictions and links
- Supports: Excitatory-selective tau vulnerability; reactive astrocyte homeostatic loss.
- Contradicts: Marinaro's broad inhibitory-neuron depletion in familial AD (not reproduced here for sporadic/staged cohort).
- Replicates: Morphological EC layer II vulnerability (now molecularly defined).
- Methodologically comparable papers: Mathys et al., Marinaro et al., Grubman et al. (AD snRNA-seq); Ruf 2026 (RORB among vulnerable ALS motor-cortex subtypes — cross-disease link); Castanho 2025 (AD resilience, ROSMAP).
- Relevant synthesis notes: candidate seed for "cell-type-specific tau/TDP-43 vulnerability across neurodegeneration."
- Relevant project decisions: (none yet)

# Follow-up actions
- [ ] Verify and record the snRNA-seq accession + access terms (GEO/controlled)
- [ ] Confirm DE method/FDR and sequencing chemistry from supplement
- [ ] Cross-link RORB vulnerability with Ruf 2026 (ALS) and Castanho 2025 (AD resilience)
- [ ] Check retraction/correction status

# Priority decision
- Priority: 1
- Read now (and retain as a reference)
- Rationale: Landmark, well-validated cell-type vulnerability study directly relevant to the neurodegeneration domain and cross-linked (RORB) to the existing Ruf 2026 record; main gap is the unverified data accession.
