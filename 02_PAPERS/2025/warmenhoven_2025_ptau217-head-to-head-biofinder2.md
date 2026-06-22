---
record_type: paper
record_status: verified
canonical_id: "10.1093/brain/awae346"
doi: "10.1093/brain/awae346"
pmid: "39468767"
pmcid: "PMC11788211"
title: "A comprehensive head-to-head comparison of key plasma phosphorylated tau 217 biomarker tests"
year: 2025
source_type: primary
peer_reviewed: true
full_text_checked: false
supplement_checked: false
code_checked: false
data_checked: false
last_verified: 2026-06-22
priority: 1
projects: []
topics: [neurodegeneration, AD_ADRD, aging]
methods: [biomarker, external_validation, human_cohort]
datasets: []
---

# Citation
- Full citation: Warmenhoven N, Salvadó G, Janelidze S, Mattsson-Carlgren N, Bali D, Orduña Dolado A, Kolb H, Triana-Baltzer G, Barthélemy NR, Schindler SE, Aschenbrenner AJ, Raji CA, Benzinger TLS, Morris JC, Ibanez L, Timsina J, Cruchaga C, Bateman RJ, Ashton N, Arslan B, Zetterberg H, Blennow K, Pichet Binette A, Hansson O. "A comprehensive head-to-head comparison of key plasma phosphorylated tau 217 biomarker tests." *Brain* 2025;148(2):416-431.
- DOI / PMID / stable URL: [DOI](https://doi.org/10.1093/brain/awae346) · PMID 39468767 · PMC11788211
- Related preprint or published version: Peer-reviewed (Brain).
- Correction, expression of concern, or retraction status: **Unknown** — not checked (added 2026-06-22). Note multiple industry-affiliated co-authors (J&J/Janssen, mass-spec and immunoassay developers) — competing-interest review advised.

*Source: metadata + abstract from PubMed. Full text not inspected. According to PubMed, DOI [10.1093/brain/awae346](https://doi.org/10.1093/brain/awae346).*

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: The single best decision-relevant benchmark for **which plasma p-tau217 assay to use** as an AD confirmatory vs triage test. Directly informs biomarker selection for any neurodegeneration project pairing fluid biomarkers with tau-PET/amyloid-PET. Establishes that the **mass-spectrometry %p-tau217 ratio (WashU)** outperforms all immunoassays (Lilly, Janssen, ALZpath, NULISA) against PET and cognition, and benchmarks plasma against CSF tests.
- Why it is more or less useful than neighboring literature: A large (n=998 BioFINDER-2), head-to-head, multi-assay comparison with an **independent external replication cohort (WashU, n=219)** and both cross-sectional and longitudinal PET outcomes — substantially stronger than single-assay sensitivity demonstrations. Fills the Domain-1 "tau-PET / fluid biomarker" sub-theme absent from the seed corpus.

# Source inspection status
- Abstract inspected: yes
- Full text inspected: no (abstract + metadata only)
- Methods inspected: partial (cohort sizes, assays, outcomes from abstract)
- Supplement inspected: no
- Figures/tables inspected: no
- Code repository inspected: no
- Data repository inspected: no
- Missing material: full Methods (assay protocols, ROC/Pdiff statistics, longitudinal model), supplement; BioFINDER-2 access terms.

# Study question and hypothesis
- Primary question: Which plasma p-tau217 test best detects AD pathology (Aβ-PET, tau-PET) and cognition, and how do they compare to each other and to CSF tests?
- Stated hypothesis: Plasma p-tau217 assays differ meaningfully in performance; the mass-spec %p-tau217 ratio may outperform immunoassays.
- Study type: Cross-sectional + longitudinal observational biomarker head-to-head comparison.

# Biological or clinical context
- Disease / exposure / process: Alzheimer's disease pathology (amyloid, tau).
- Organism: Human.
- Tissue / cell type: Plasma and CSF; PET imaging (Aβ, tau).
- Model system: Clinical cohorts.
- Cohort or population: BioFINDER-2 (Sweden), n=998, mean age 68.5 (range 20.0–92.5), 53% female, cognitively unimpaired + impaired. External: WashU St. Louis, n=219.
- Relevant stage, age, sex, genotype, severity: Full AD continuum (CU and CI).

# Study design
- Experimental or observational unit: Individual participant.
- Unit of inference: Participant-level assay performance.
- Groups and sample size per group: BioFINDER-2 n=998 (mixed CU/CI); replication WashU n=219; p-tau217NULISA in subsets of both.
- Biological replicates: N/A (observational).
- Technical replicates: Not extracted.
- Randomization / blinding: N/A (observational); assay measurements presumably masked to outcomes (not verified).
- Inclusion / exclusion criteria: Not extracted.
- Batch structure: Multiple assay platforms; details in Methods (not inspected).
- Longitudinal / paired structure: Cross-sectional + longitudinal PET outcomes; paired plasma/CSF.
- Controls and comparators: CSF p-tau217Lilly, FDA-approved p-tau181/Aβ42Elecsys, p-tau181Elecsys.

# Experimental methods
- Assay / platform: Plasma p-tau217 — mass spectrometry (%p-tau217WashU ratio; p-tau217WashU) and immunoassays (Lilly, Janssen, ALZpath, NULISA). CSF immunoassays (Lilly, Elecsys). Aβ-PET, tau-PET.
- Sample preparation: Not extracted.
- Dose / perturbation: N/A.
- Timing / sampling schedule: Cross-sectional + longitudinal (PET load over time).
- Matrix: Plasma, CSF.
- Primary endpoint: Discrimination of abnormal Aβ-PET and tau-PET status (AUC); association with PET load (R²) and cognition (MMSE).
- Secondary endpoints: Longitudinal PET-load associations; CSF comparison.
- QC criteria / failure criteria: Not extracted.
- Exact reusable parameters and source location: AUCs and Pdiff in abstract (below); full ROC/CI in Results/supplement (not inspected).

# Computational and statistical methods
- Raw input: Plasma/CSF biomarker values; PET SUVR; cognitive scores.
- Statistical test or model: ROC/AUC with pairwise AUC comparisons (Pdiff); R² regressions for PET load and cognition. Exact models not extracted.
- Multiple-testing correction: Not extracted.
- Effect-size reporting: AUCs, accuracy/sensitivity/specificity, R² (abstract).
- Validation strategy: Internal (BioFINDER-2) + external replication (WashU).
- External validation: Yes — WashU n=219.
- Software / versions: Not extracted.
- Code availability: Not extracted.

# Data and resource availability
- Repository and accession: BioFINDER-2 is a managed-access cohort (data on reasonable request, typically). **Not verified here.**
- Raw data available: Restricted (cohort governance) — unverified.
- Processed data available: Unverified.
- Metadata completeness: High (well-characterized cohort) — unverified specifics.
- Data-use restrictions: Likely controlled — verify with BioFINDER.
- Reusability for the user's work: Reference/benchmark value high; raw-data reuse gated.

# Main findings
| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| All plasma p-tau217 tests detect abnormal Aβ-PET and tau-PET well | Reported | Abstract/Results | Aβ-PET AUC 0.91–0.96; tau-PET AUC 0.94–0.97 | Yes | Full ROC not inspected |
| MS %p-tau217WashU outperforms all immunoassays | Reported | Abstract/Results | Pdiff < 0.007 vs each immunoassay | Yes | Industry co-authors; replicate independently |
| %p-tau217WashU accuracy for Aβ-PET status | Reported | Abstract | acc 0.93 (immunoassays 0.83–0.88), sens 0.91, spec 0.94 | Yes | — |
| %p-tau217WashU associates more strongly with PET load | Reported | Abstract | baseline Aβ-PET R²=0.72 vs 0.47–0.58; tau-PET R²=0.51 vs 0.38–0.45 | Yes | — |
| Among immunoassays, Lilly and ALZpath > Janssen for Aβ-PET | Reported | Abstract | Pdiff < 0.006 | Yes | — |
| Main results replicate in external WashU cohort | Reported | Abstract | n=219 replication | Yes | Smaller cohort |

# What is actually new?
- Biological novelty: None primary (biomarker benchmarking).
- Methodological novelty: Comprehensive multi-assay head-to-head incl. MS ratio vs immunoassays vs CSF, with external replication.
- Dataset/resource novelty: Cross-assay performance reference table.
- What was already known: p-tau217 is the strongest plasma AD biomarker; this ranks the specific tests.

# Strengths
- Design strength: Large, well-characterized cohort; multiple assays measured in the same samples; external replication.
- Validation strength: Independent WashU replication; both PET and cognition outcomes.
- Reproducibility strength: Standardized cohort.
- Translational realism: Real clinical plasma/CSF; spans the AD continuum.

# Limitations and bias risks
- Sample-size / power: Large overall; some assays (NULISA) only in subsets.
- Confounding: Comorbidities, renal function (known plasma p-tau confounder) not extracted.
- Batch / site effects: Multi-assay; handled in Methods (not inspected).
- Pseudoreplication risk: Low (participant-level).
- Leakage / overfitting risk: ROC comparisons; not an ML training pipeline.
- Generalizability: Predominantly European cohorts; ancestry diversity not extracted.
- Missing controls / validation: External replication present.
- Author-stated limitations: Need for multi-cohort reviews to settle triage-vs-confirmatory roles (abstract).
- Additional limitations identified during review: Strong industry affiliations on assay-comparison study; confirm competing-interest disclosures before citing the ranking as definitive.

# Transferability to the user's work
- Directly transferable elements: Assay-selection guidance (favor MS %p-tau217 where available; immunoassays as triage); benchmark AUCs for power calculations.
- Elements requiring adaptation: Cohort demographics; assay availability/cost.
- Mismatch: AD-focused; not validated for ALS/TBI tau biomarkers.
- Assumptions required for transfer: Comparable pre-analytics and matrix.
- Confidence: high (for AD plasma biomarker selection).

# Practical implications
- Experimental implication: When designing a fluid-biomarker arm, prefer p-tau217 (MS ratio if feasible) and pre-register the assay.
- Analysis implication: Use reported AUCs/effect sizes for sample-size planning.
- Public dataset implication: BioFINDER-2 as a (gated) reference cohort.
- Biomarker / translational implication: Plasma %p-tau217 as stand-alone confirmatory; some immunoassays as triage.
- Grant / manuscript implication: Citable assay-selection justification.

# Contradictions and links
- Supports: p-tau217 superiority over p-tau181/p-tau231 (see Fernández Arias 2025 record).
- Contradicts: none identified.
- Replicates: Internal + WashU.
- Methodologically comparable papers: Fernández Arias 2025 (fernandez-arias_2025_ptau217-memory-triad-biofinder2); leng_2021 / castanho_2025 (tissue-level AD).
- Relevant synthesis notes: seed for "AD fluid biomarker selection."
- Relevant project decisions: (none yet)

# Follow-up actions
- [ ] Inspect Methods/supplement for ROC CIs, confounder adjustment (renal), and longitudinal model
- [ ] Confirm competing-interest disclosures
- [ ] Cross-link with Fernández Arias 2025
- [ ] Check correction/retraction status

# Priority decision
- Priority: 1
- Read now (assay-selection reference)
- Rationale: Decision-changing head-to-head plasma p-tau217 benchmark with external validation; fills the tau-PET/fluid-biomarker gap. Main caveat: industry affiliations and uninspected Methods.
