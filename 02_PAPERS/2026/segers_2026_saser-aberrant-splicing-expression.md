---
record_type: paper
record_status: needs_full_text
canonical_id: "10.1186/s13059-026-03973-8"
doi: "10.1186/s13059-026-03973-8"
pmid: ""
pmcid: ""
title: "saseR: juggling offsets unlocks RNA-seq tools for fast and scalable differential usage, aberrant splicing and expression retrieval"
year: 2026
source_type: method
peer_reviewed: true
full_text_checked: false
supplement_checked: false
code_checked: false
data_checked: false
last_verified: 2026-06-22
priority: 2
projects: []
topics: [transcriptomics, multi_omics]
methods: [analysis_method, software, bulk_RNAseq]
datasets: []
---

# Citation
- Full citation: Segers A, Gilis J, Van Heetvelde M, Risso D, De Baere E, Clement L. "saseR: juggling offsets unlocks RNA-seq tools for fast and scalable differential usage, aberrant splicing and expression retrieval." *Genome Biology* 2026; DOI 10.1186/s13059-026-03973-8.
- DOI / PMID / stable URL: [DOI](https://doi.org/10.1186/s13059-026-03973-8). Bioconductor package: saseR.
- Related preprint or published version: **Peer-reviewed (Genome Biology) is canonical.** Preprint: bioRxiv [10.1101/2023.06.29.547014](https://doi.org/10.1101/2023.06.29.547014) (PMID 39464066, PMC11507730) — the abstract/text I inspected this pass is the preprint version; treat published-version specifics as needing re-verification.
- Correction, expression of concern, or retraction status: **Unknown** — not checked (added 2026-06-22).

*Source: bioRxiv preprint metadata + abstract (PubMed, PMID 39464066); published-version DOI confirmed via WebSearch (Genome Biology, Springer). Springer full text gated (auth required) this pass → needs_full_text. According to PubMed, preprint DOI [10.1101/2023.06.29.547014](https://doi.org/10.1101/2023.06.29.547014).*

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Fills the Domain-3 splicing/outlier and **reusable-methods** signal. A single, **scalable** Bioconductor framework that — by replacing normalization **offsets** — unifies differential transcript usage, **aberrant splicing**, and aberrant **expression** outlier detection for both short- and long-read RNA-seq. Claims to be much faster than state-of-the-art and to dramatically outperform existing tools at aberrant-splicing detection. Directly reusable for rare-disease outlier analysis and DTU.
- Why it is more or less useful than neighboring literature: Broader than MAJIQ-CLIN (covers expression + splicing + DTU in one workflow) and emphasizes scalability for large compendia; pairs naturally with aicher_2026 (MAJIQ-CLIN) and prieto-leon_2025 (count-model normalization) for a methods synthesis. Less clinically packaged than MAJIQ-CLIN.

# Source inspection status
- Abstract inspected: yes (preprint)
- Full text inspected: no (published Genome Biology version gated; preprint full text not sliced this pass)
- Methods inspected: no
- Supplement inspected: no
- Figures/tables inspected: no
- Code repository inspected: no (Bioconductor saseR exists; not opened/verified this pass)
- Data repository inspected: no
- Missing material: full Methods, benchmark datasets (GTEx / Kremer-type rare-disease / Mendelian), exact performance numbers vs FRASER/OUTRIDER/DEXSeq, package version, runtime benchmarks.

# Study question and hypothesis
- Primary question: Can a single offset-based negative-binomial framework provide fast, scalable differential usage + aberrant splicing + aberrant expression analysis across RNA-seq applications?
- Stated hypothesis: Replacing normalization offsets "unlocks" existing bulk RNA-seq tools for these tasks at scale and with better aberrant-splicing detection.
- Study type: Computational method development + benchmarking.

# Biological or clinical context
- Disease / exposure / process: Generic (incl. rare-disease diagnostics via expression/splicing outliers).
- Organism: Human (and general).
- Tissue / cell type: Bulk RNA-seq (various).
- Model system: Public RNA-seq benchmarks (not extracted in detail).
- Cohort or population: N/A (method).
- Relevant stage/severity: N/A.

# Study design
- Experimental or observational unit: RNA-seq sample / feature (gene, bin, junction).
- Unit of inference: Per-feature differential usage / outlier call.
- Groups / sample size: Not extracted (benchmark datasets).
- Replicates / randomization / blinding: N/A.
- Inclusion / exclusion criteria: Not extracted.
- Batch structure: Handled via design/offsets (verify).
- Controls and comparators: State-of-the-art DTU/outlier tools (e.g., DEXSeq, FRASER, OUTRIDER — implied; confirm in full text).

# Experimental methods
- Assay / platform: Short- and long-read bulk RNA-seq (analysis only).
- Endpoint: Differential transcript usage; aberrant splicing outliers; aberrant expression outliers.
- Exact reusable parameters and source location: Core idea = adapted normalization offsets within a negative-binomial framework to model aberrant splicing; scalable parameter estimation (Methods — needs_full_text).

# Computational and statistical methods
- Raw input: RNA-seq count matrices (gene/bin/junction).
- Preprocessing: Offset construction (the central methodological move).
- Statistical model: Negative-binomial regression with adapted offsets; outlier detection layered on top.
- Multiple-testing correction: Not extracted.
- Effect-size reporting: Performance/runtime benchmarks (numbers not extracted).
- Batch handling: Via design matrix/offsets (verify).
- Validation strategy: Benchmark vs existing tools across applications.
- External validation: Public benchmark datasets (not extracted).
- Software / versions: Bioconductor `saseR` (version not extracted).
- Code availability: Bioconductor (confirm version/release).

# Data and resource availability
- Repository and accession: Benchmark datasets not extracted.
- Raw/processed data available: Unverified.
- Metadata completeness: Unverified.
- Data-use restrictions: Depends on benchmark datasets.
- Reusability for the user's work: High — installable Bioconductor package for DTU/aberrant splicing/expression.

# Main findings
| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| Offset replacement unlocks scalable DTU + aberrant splicing + expression in one workflow | Reported | Abstract | qualitative | Partial | full text needed |
| Much faster than state-of-the-art methods | Reported | Abstract | runtime not extracted | Partial | benchmark details needed |
| Dramatically outperforms existing tools at aberrant-splicing detection | Reported | Abstract | metrics not extracted | Partial | tools/metrics not extracted |
| Single workflow for short- and long-read RNA-seq | Reported | Abstract | qualitative | Partial | — |

# What is actually new?
- Methodological novelty: Offset-based unification of DTU + aberrant splicing + aberrant expression in a scalable NB framework.
- Dataset/resource novelty: `saseR` Bioconductor package.
- What was already known: DEXSeq (DTU), FRASER (aberrant splicing), OUTRIDER (aberrant expression) as separate tools.

# Strengths
- Design strength: Unified, scalable framework spanning multiple tasks and read types.
- Validation strength: Benchmarked vs state-of-the-art (details pending).
- Reproducibility strength: Open Bioconductor package.
- Translational realism: Rare-disease outlier application.

# Limitations and bias risks
- Sample-size / power: Benchmark composition not extracted.
- Confounding / batch: Offset/design-based handling — verify adequacy.
- Pseudoreplication / leakage / overfitting: Not assessable without full text.
- Generalizability: Bulk RNA-seq; single-cell applicability not claimed here.
- Missing controls / validation: Cannot fully assess (needs_full_text).
- Author-stated limitations: Not extracted.
- Additional limitations identified during review: Published-version specifics (numbers, datasets) not yet inspected — preprint-based notes only.

# Transferability to the user's work
- Directly transferable elements: `saseR` for DTU and aberrant splicing/expression outlier detection.
- Elements requiring adaptation: Design/offset specification per dataset.
- Mismatch: Bulk-RNA-seq focus.
- Assumptions required for transfer: NB-appropriate count data; suitable control set for outliers.
- Confidence: moderate (pending full text).

# Practical implications
- Experimental implication: Single pipeline for usage + outlier analyses.
- Analysis implication: Consider `saseR` vs MAJIQ-CLIN/FRASER/OUTRIDER; benchmark on own data.
- Public dataset implication: Reusable benchmarks (to identify in full text).
- Biomarker / translational implication: Scalable outlier detection for diagnostics.
- Grant / manuscript implication: Methods citation for scalable RNA-seq outlier analysis.

# Contradictions and links
- Supports: Need for scalable splicing/expression outlier tools (cf. aicher_2026).
- Contradicts: none identified.
- Replicates: Overlaps DEXSeq/FRASER/OUTRIDER functionality in one framework.
- Methodologically comparable papers: aicher_2026 (MAJIQ-CLIN), prieto-leon_2025 (RUV/pseudobulk), bendall_2019 (TE quantification).
- Relevant synthesis notes: seed for "aberrant splicing/expression methods comparison."
- Relevant project decisions: (none yet)

# Follow-up actions
- [ ] Obtain Genome Biology full text; extract benchmark datasets, metrics vs FRASER/OUTRIDER/DEXSeq, runtimes, package version
- [ ] Verify Bioconductor `saseR` release + vignette
- [ ] Record PMID/PMCID of the published version once indexed
- [ ] Build a methods synthesis with MAJIQ-CLIN
- [ ] Check correction/retraction status

# Priority decision
- Priority: 2
- Retain for methods (needs full text)
- Rationale: Reusable, scalable Bioconductor framework directly serving the splicing/outlier signal; canonical published version confirmed but full text gated — finalize numbers after access.
