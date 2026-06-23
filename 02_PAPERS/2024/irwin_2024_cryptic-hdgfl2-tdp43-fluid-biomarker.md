---
record_type: paper
record_status: verified
canonical_id: "10.1038/s41591-023-02788-5"
doi: "10.1038/s41591-023-02788-5"
pmid: "38278991"
pmcid: "PMC10878965"
title: "A fluid biomarker reveals loss of TDP-43 splicing repression in presymptomatic ALS-FTD"
year: 2024
source_type: primary
peer_reviewed: true
full_text_checked: true
supplement_checked: false
code_checked: false
data_checked: false
last_verified: 2026-06-22
priority: 1
projects: []
topics: [neurodegeneration, ALS, AD_ADRD]
methods: [biomarker, external_validation]
datasets: []
---

# Citation
- Full citation: Irwin KE, Jasin P, Braunstein KE, Sinha IR, Garret MA, Bowden KD, Chang K, Troncoso JC, Moghekar A, Oh ES, Raitcheva D, Bartlett D, Miller T, Berry JD, Traynor BJ, Ling JP, Wong PC. "A fluid biomarker reveals loss of TDP-43 splicing repression in presymptomatic ALS-FTD." *Nature Medicine* 2024;30(2):382-393.
- DOI / PMID / stable URL: [DOI](https://doi.org/10.1038/s41591-023-02788-5) · PMID 38278991 · PMC10878965
- Related preprint or published version: Peer-reviewed (Nat Med).
- Correction, expression of concern, or retraction status: **Unknown** — no notice seen in retrieved PMC text (checked 2026-06-22).

*Source: PMC full text (~64k chars) retrieved from PubMed Central + metadata. According to PubMed, DOI [10.1038/s41591-023-02788-5](https://doi.org/10.1038/s41591-023-02788-5).*

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Establishes a **cryptic-exon neoepitope (HDGFL2) fluid biomarker** that reports loss of TDP-43 splicing repression directly, and does so **presymptomatically** in C9orf72 carriers. This is the missing mechanism-proximal TDP-43 biomarker complement to the corpus's TDP-43 pathology and ALS/FTD records ([[ruf_2026_celltype-tdp43-motor-cortex]], [[li_2023_c9orf72-snrna-snatac-als-ftd]], [[sirtori_2025_tabletop-blast-organoid-tbi]]) and the p-tau217 AD-biomarker axis ([[warmenhoven_2025_ptau217-head-to-head-biofinder2]]).
- Why it is more or less useful than neighboring literature: Unlike NfL/pNfH (nonspecific neurodegeneration markers), cryptic HDGFL2 is a **direct readout of TDP-43 loss-of-function**, and the paper shows it peaks *earlier* than Nfs — a mechanism-specific, early-stage biomarker concept directly reusable for assay design and trial enrichment.

# Source inspection status
- Abstract inspected: yes
- Full text inspected: yes (PMC full text)
- Methods inspected: partial (cohort composition, MSD/sandwich ELISA design, comparator assays extracted; full antibody-screening and exact statistics in Methods/supplement not fully viewed)
- Supplement inspected: no (Extended Data / Supplementary Figs referenced, not opened)
- Figures/tables inspected: no (callouts read; panels not viewed)
- Code repository inspected: no
- Data repository inspected: no (ASCOT splicing catalog referenced as a public resource used for target selection)
- Missing material: exact AUC/sensitivity/specificity values; full cohort demographics; antibody clone identifiers; deposited-data accession (if any).

# Study question and hypothesis
- Primary question: Can detection of a TDP-43-dependent cryptic exon-encoded neoepitope in CSF/blood reveal early (presymptomatic) loss of TDP-43 splicing repression in ALS-FTD?
- Stated hypothesis: Because cryptic exon inclusion reflects TDP-43 loss of function, a neoepitope-specific immunoassay should detect TDP-43 dysregulation before symptom onset.
- Study type: Biomarker-development study (antibody generation + immunoassay) applied to human CSF/blood cohorts, including longitudinal C9orf72 carriers.

# Biological or clinical context
- Disease / exposure / process: ALS-FTD spectrum; loss of TDP-43 nuclear splicing repression → cryptic exon inclusion (HDGFL2).
- Organism: Human.
- Tissue / cell type: CSF and blood (biofluids); HeLa cells (TDP-43-depleted) for antibody validation.
- Model system: Human cohorts + in vitro antibody validation.
- Cohort or population: Familial (C9orf72) ALS-FTD, sporadic ALS, and controls; longitudinal C9orf72 mutation carriers from NINDS.
- Relevant stage, age, sex, genotype: Includes **presymptomatic** C9orf72 carriers and symptomatic converters; positive age correlation of cryptic HDGFL2 in carriers (= 0.025).

# Study design
- Experimental or observational unit: Individual participant (CSF/blood sample); some longitudinal repeated samples.
- Unit of inference: Participant-level biomarker level by disease/genotype/stage.
- Groups and sample size per group (from full text): 12 healthy controls (16 CSF samples); 29 presymptomatic C9orf72 carriers (47 CSF samples); 3 symptomatic converters (4 CSF samples); 17 additional symptomatic carriers; plus sporadic ALS CSF and blood samples. Longitudinal NINDS C9orf72 cohort = 47 carriers / 89 CSF samples (overlapping framing).
- Biological replicates: Multiple participants per group; repeated longitudinal sampling in carriers.
- Technical replicates: Immunoassay replicates (not extracted).
- Randomization / blinding: N/A (biomarker cohort study).
- Inclusion / exclusion criteria: Recruited by C9orf72 mutation status (carriers); LoD-based censoring (ratios below LoD set to 0).
- Batch structure: Multi-site sample sources (NINDS; Natural History/Biomarker Study of ALS, protocol 13-N-0188); comparator assays run by Biogen.
- Longitudinal / paired structure: Longitudinal CSF in carriers; paired CSF↔blood for correlation.
- Controls and comparators: Healthy controls; NfL (Quanterix Simoa) and pNfH (ProteinSimple Ella) as established neurodegeneration comparators; antibody controls (cryptic vs WT HDGFL2 overexpression lysates).

# Experimental methods
- Assay / platform: Novel **monoclonal antibody** specific to the HDGFL2 cryptic exon-encoded neoepitope; **sandwich / MSD ELISA** for cryptic HDGFL2 in CSF and blood. Comparators: NfL (Simoa), pNfH (Ella).
- Sample preparation: CSF and plasma per source protocols.
- Dose / perturbation: N/A (human biofluids); antibody validation in TDP-43-depleted HeLa.
- Timing / sampling schedule: Longitudinal CSF sampling across presymptomatic→symptomatic transition in carriers.
- Matrix: Human CSF and blood/plasma.
- Primary endpoint: Cryptic HDGFL2 signal (ratio) by disease/genotype/stage.
- Secondary endpoints: Temporal ordering vs NfL/pNfH; CSF↔blood correlation; proposed NfL:cryptic-HDGFL2 staging ratio.
- QC criteria: LoD censoring; antibody specificity confirmed by loss of signal with cryptic-specific antibody controls.
- Failure or exclusion criteria: Below-LoD signals set to 0 ng/ml.
- Exact reusable parameters and source location: Three-part monoclonal screening strategy (recognize cryptic peptide; validate in TDP-43-depleted HeLa; confirm specificity vs WT) — reusable template for neoepitope assay development (Results, "Novel antibody specific to cryptic neoepitope in HDGFL2").

# Computational and statistical methods
- Raw input: Immunoassay signal ratios; comparator NfL/pNfH levels.
- Preprocessing: LoD censoring.
- Statistical test or model: Correlation analyses (cryptic HDGFL2 vs age, vs Nfs, CSF vs blood); group comparisons (values not fully extracted).
- Target selection: TDP-43-dependent in-frame cryptic exons chosen via **ASCOT** (alternative splicing catalog from public bulk RNA-seq) — in-frame, high-expression, broadly relevant genes; ~3% of cryptic exons produce in-frame neoepitopes.
- Effect-size reporting: Reported qualitatively here (cryptic HDGFL2 peaks earlier than Nfs; positive age correlation in carriers, = 0.025); exact AUC/sensitivity not extracted.
- Validation strategy: Antibody specificity controls; cross-fluid (CSF↔blood) concordance; temporal ordering vs Nfs.
- External validation: Multiple independent cohorts/sources (NINDS, Natural History study).
- Software / versions: UCSC Genome Browser, ggplot2 (R) for visualization; ASCOT for splicing.
- Code availability: Not confirmed from retrieved text.

# Data and resource availability
- Repository and accession: **Unknown** — not confirmed in retrieved text (ASCOT is the public resource used; assay data deposition not verified).
- Raw data available: Unverified.
- Processed data available: Unverified.
- Metadata completeness: Cohort composition stated in text; full demographics in supplement (not inspected).
- Data-use restrictions: Human clinical samples — controlled.
- Reusability for the user's work: High conceptual reuse (neoepitope assay design, staging-ratio concept); raw data reuse unverified.

# Main findings
| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| Cryptic HDGFL2 accumulates in CSF in familial/sporadic ALS-FTD vs controls | Reported | Abstract/Results | significantly higher | Yes | exact effect size not extracted |
| Detectable presymptomatically in C9orf72 carriers | Reported | Results | positive in presymptomatic carriers | Yes | small symptomatic-converter n (3) |
| Cryptic HDGFL2 rises earlier than NfL/pNfH | Reported | Results/Fig | peak precedes NF peak | Yes | proposed staging scale (NfL:cryptic HDGFL2) |
| Cryptic HDGFL2 detectable in blood, correlated with CSF | Reported | Abstract/Results | highly correlated CSF↔blood | Yes | — |
| Positive correlation with age in carriers | Reported | Results | = 0.025 (carriers); n.s. overall (= 0.20) | Partial | confound of age vs proximity-to-onset |

# What is actually new?
- Biological novelty: First fluid biomarker reporting **TDP-43 loss-of-function directly** (cryptic neoepitope) and detectable **before symptom onset**.
- Methodological novelty: Neoepitope-specific monoclonal + sandwich/MSD ELISA; ASCOT-guided in-frame cryptic-exon target selection.
- Dataset/resource novelty: Reusable assay concept and staging ratio (NfL:cryptic HDGFL2).
- What was already known: Loss of TDP-43 splicing repression in post-mortem ALS/FTD tissue; NfL/pNfH as nonspecific neurodegeneration markers.

# Strengths
- Design strength: Longitudinal presymptomatic carriers; mechanism-proximal target.
- Validation strength: Antibody specificity controls; CSF↔blood concordance; temporal ordering vs established markers.
- Reproducibility strength: Multiple independent cohorts/sources.
- Translational realism: Human CSF and blood; trial-relevant (enrichment, target engagement).

# Limitations and bias risks
- Sample-size / power: Few symptomatic converters (n=3) for the key presymptomatic→symptomatic transition.
- Confounding: Age vs disease-proximity; site/assay batch (comparators run externally).
- Batch / site effects: Multi-source samples.
- Pseudoreplication risk: Longitudinal repeated samples per participant — must be modeled at participant level.
- Leakage / overfitting risk: Low (not a trained classifier), but reported thresholds need prospective validation.
- Generalizability: Strongest evidence in C9orf72 familial disease; sporadic-ALS performance and specificity vs other TDP-43 proteinopathies (e.g., LATE, FTLD-TDP) need broader cohorts.
- Missing controls / validation: Pathological correlation in same individuals noted by authors as needed; alternative platforms (e.g., NULISA) proposed as future work.
- Author-stated limitations: Need postmortem-pathology correlation; explore additional ELISA platforms.
- Additional limitations identified during review: Exact diagnostic-accuracy metrics not extracted here; deposition/accession unverified.

# Transferability to the user's work
- Directly transferable elements: Neoepitope-assay design strategy; ASCOT-based in-frame cryptic-exon target selection; staging-ratio concept; CSF↔blood bridging logic.
- Elements requiring adaptation: Genotype scope (C9orf72) → sporadic/TDP-43 contexts; matrix-specific assay validation.
- Model, species, tissue, matrix, platform, scale mismatch: Human biofluid clinical assay vs organoid/in vitro TBI models in the corpus — mechanism (TDP-43 LOF) is the bridge, not platform.
- Assumptions required for transfer: Cryptic-exon neoepitope is stable/detectable in the chosen matrix.
- Confidence: high (concept), moderate (quantitative thresholds).

# Practical implications
- Experimental implication: Use cryptic-neoepitope readouts as a TDP-43 LOF endpoint in models (e.g., blast/organoid TDP-43 work, [[sirtori_2025_tabletop-blast-organoid-tbi]]).
- Analysis implication: Model longitudinal samples at participant level; treat below-LoD as censored, not zero, where possible.
- Public dataset implication: ASCOT is a reusable splicing catalog for cryptic-exon target discovery.
- Biomarker / translational implication: Mechanism-specific, presymptomatic ALS-FTD biomarker; trial enrichment + target engagement.
- Grant / manuscript implication: Strong citable anchor for "TDP-43 loss-of-function fluid biomarker."

# Contradictions and links
- Supports: TDP-43 LOF as an early, measurable event (cf. [[ruf_2026_celltype-tdp43-motor-cortex]], [[li_2023_c9orf72-snrna-snatac-als-ftd]]).
- Contradicts: none directly identified.
- Replicates: Cross-cohort + cross-fluid concordance internally.
- Methodologically comparable papers: [[warmenhoven_2025_ptau217-head-to-head-biofinder2]] (fluid biomarker head-to-head / staging logic).
- Relevant synthesis notes: seed for "TDP-43 loss-of-function fluid biomarkers."
- Relevant project decisions: (none yet)

# Follow-up actions
- [ ] Extract exact diagnostic-accuracy metrics (AUC/sens/spec) from full text + Extended Data
- [ ] Confirm any deposited data/assay accession + antibody clone IDs
- [ ] Cross-link to a TDP-43 synthesis with ruf_2026 / li_2023 / sirtori_2025
- [ ] Monitor for replication in sporadic ALS / LATE / FTLD-TDP

# Priority decision
- Priority: 1
- Read now (and retain as TDP-43 biomarker anchor)
- Rationale: Mechanism-proximal, presymptomatic TDP-43 loss-of-function fluid biomarker — fills a flagged gap and cross-links the ALS/FTD/TDP-43 cluster to the biomarker axis; main missing items are exact accuracy metrics and data accession.
