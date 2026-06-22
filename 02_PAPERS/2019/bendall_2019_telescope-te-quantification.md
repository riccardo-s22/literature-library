---
record_type: paper
record_status: verified
canonical_id: "10.1371/journal.pcbi.1006453"
doi: "10.1371/journal.pcbi.1006453"
pmid: "31568525"
pmcid: "PMC6786656"
title: "Telescope: Characterization of the retrotranscriptome by accurate estimation of transposable element expression"
year: 2019
source_type: method
peer_reviewed: true
full_text_checked: true
supplement_checked: false
code_checked: false
data_checked: true
last_verified: 2026-06-22
priority: 1
projects: []
topics: [transcriptomics, single_cell, multi_omics]
methods: [analysis_method, software, bulk_RNAseq]
datasets: []
---

# Citation
- Full citation: Bendall ML, de Mulder M, Iñiguez LP, Lecanda-Sánchez A, Pérez-Losada M, Ostrowski MA, Jones RB, Mulder LCF, Reyes-Terán G, Crandall KA, Ormsby CE, Nixon DF. "Telescope: Characterization of the retrotranscriptome by accurate estimation of transposable element expression." *PLoS Computational Biology* 2019;15(9):e1006453.
- DOI / PMID / stable URL: [DOI](https://doi.org/10.1371/journal.pcbi.1006453) · PMID 31568525 · PMC6786656
- Related preprint or published version: Peer-reviewed (PLoS Comput Biol), open access.
- Correction, expression of concern, or retraction status: **Unknown** — not checked (added 2026-06-22).

*Source: metadata + PMC full text retrieved from PubMed / PubMed Central. According to PubMed, DOI [10.1371/journal.pcbi.1006453](https://doi.org/10.1371/journal.pcbi.1006453).*

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Telescope is a **reusable, benchmarked software tool for locus-specific transposable-element / HERV quantification from RNA-seq**, resolving the multi-mapping ambiguity that defeats subfamily-level tools. Directly matches the signals-file priority "transposable-element and HERV quantification." Useful for the user's TE/HERV analyses (e.g., in neurodegeneration RNA-seq), and as a methods precedent with public ENCODE benchmarking and open code.
- Why it is more or less useful than neighboring literature: Provides **single-locus** resolution via a Bayesian reassignment EM model, benchmarked against six alternatives (RepEnrich, TEtranscripts, SalmonTE, unique counts, best counts, etc.) with precision/recall/F1 on simulations — more rigorous and finer-grained than family-level tools. Limitation: bulk RNA-seq, human HERV focus; not a single-cell-native method.

# Source inspection status
- Abstract inspected: yes
- Full text inspected: yes (PMC full text, ~51k chars)
- Methods inspected: yes (model, EM algorithm, annotation, simulation/benchmark design)
- Supplement inspected: no (S figures referenced)
- Figures/tables inspected: no (callouts read; panels not viewed)
- Code repository inspected: no (repo described — open-source, MIT, bioconda — but the exact GitHub URL was redacted in retrieved text; metadata abstract cites github.com/mlbendall/telescope)
- Data repository inspected: yes (ENCODE public RNA-seq; 13 cell types)
- Missing material: exact repo URL/version from full text (abstract gives github.com/mlbendall/telescope); supplementary benchmark tables.

# Study question and hypothesis
- Primary question: Can transposable-element (esp. HERV) expression be accurately quantified at single-locus resolution from RNA-seq despite pervasive multi-mapping ambiguity?
- Stated hypothesis: Reassigning ambiguously mapped fragments to their most probable source transcript via a Bayesian/EM model yields accurate locus-specific TE expression estimates.
- Study type: Computational methods development + benchmarking (simulation) + application (ENCODE).

# Biological or clinical context
- Disease / exposure / process: Retrotranscriptome / HERV expression (general; TE biology).
- Organism: Human (hg38).
- Tissue / cell type: 13 ENCODE human cell types (lines + primary; normal vs transformed).
- Model system: Public RNA-seq (ENCODE).
- Cohort or population: N/A (cell types).
- Relevant stage, age, sex, genotype, severity: N/A.

# Study design
- Experimental or observational unit: RNA-seq sample / simulated dataset.
- Unit of inference: Per-locus TE expression estimate.
- Groups and sample size per group: 13 ENCODE cell types; >2.7 billion fragments aligned to hg38 (23.6-46.1% ambiguous per sample); 14,968 annotated TE loci intersected; simulations across loci (250 estimates referenced).
- Biological replicates: ENCODE samples (as provided).
- Technical replicates: N/A.
- Randomization / blinding: N/A.
- Inclusion / exclusion criteria: Annotation modified to allow locus-specific quantification for comparator tools.
- Batch structure: N/A (benchmark).
- Controls and comparators: Six alternative TE-quantification approaches (RepEnrich, TEtranscripts, SalmonTE, unique counts, best counts, etc.).

# Experimental methods
- Assay / platform: In silico (RNA-seq quantification); benchmarking on simulated reads + ENCODE data.
- Primary endpoint: Locus-level quantification accuracy (precision, recall, F1) vs expected counts.
- Secondary endpoints: HERV expression landscape across ENCODE cell types; cell-type discriminability from retrotranscriptome.
- Exact reusable parameters and source location: Bayesian descriptive model of the RNA-seq process; iterative (EM) optimization reassigning multi-mapped fragments to most-probable source transcript; TE annotation (14,968 loci); GTF-based locus annotation.

# Computational and statistical methods
- Raw input: Aligned RNA-seq fragments (incl. ambiguously/multi-mapped); hg38 reference.
- Preprocessing: Alignment to hg38; intersection with TE annotation (14,968 loci).
- Statistical model: Bayesian generative model of RNA-seq fragment origin; assumes fragment count proportional to transcript abundance; iterative EM reassignment of ambiguous fragments to most likely source locus.
- Multiple-testing correction: N/A (quantification, not DE).
- Effect-size reporting: Precision/recall and F1 across loci/simulations; comparator error profiles (e.g., unique counts underestimate — 96/250 estimates miss ≥50% true expression; best counts ~12.1% fragments misassigned → false positives; RepEnrich discards reads).
- Batch handling: N/A.
- Validation strategy: Simulation with known truth (precision/recall/F1) vs six alternatives; ENCODE application.
- External validation: ENCODE multi-cell-type analysis.
- Software and versions: Telescope (Python, MIT license, Linux/MacOS, bioconda-installable); snakemake reproducibility pipeline for the ENCODE analysis. Version not extracted.
- Code availability: **Open-source, MIT license, bioconda** — github.com/mlbendall/telescope (from abstract); snakemake pipeline + simulation scripts + tutorial provided.

# Data and resource availability
- Repository and accession: Benchmark uses public **ENCODE** RNA-seq (13 cell types); TE annotation provided; software + test data + reproducibility pipeline public.
- Raw data available: Yes (ENCODE public).
- Processed data available: Yes (annotation, pipeline).
- Metadata completeness: High (ENCODE).
- Data-use restrictions: Open.
- Reusability for the user's work: **High** — directly installable, open, benchmarked locus-level TE/HERV quantifier for bulk RNA-seq.

# Main findings
| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| Telescope quantifies TE/HERV expression at single-locus resolution (vs subfamily) | Reported | Results | locus-level estimates over 14,968 loci | Yes | Bulk RNA-seq |
| Bayesian EM reassignment of ambiguous fragments outperforms unique/best-count and family-level tools | Reported | Results (benchmark) | precision/recall/F1 vs 6 methods | Yes | Simulation-based truth |
| Unique-counts approach systematically underestimates expression | Reported | Results | 96/250 estimates miss ≥50% true expression | Yes | — |
| Best-counts has high false-positive rate | Reported | Results | ~12.1% fragments misassigned | Yes | — |
| 23.6-46.1% of fragments per ENCODE sample map ambiguously (motivating the problem) | Reported | Results | range across samples | Yes | hg38 |
| Retrotranscriptome differs markedly across cell types; can aid cell-type identification | Reported | Results | qualitative across 13 cell types | Partial | Application, not formally classified |

# What is actually new?
- Methodological novelty: Bayesian/EM single-locus TE expression estimation directly modeling multi-mapping ambiguity.
- Biological novelty: Demonstrates cell-type-specific breadth/magnitude of the retrotranscriptome at locus resolution.
- Dataset or resource novelty: Open, benchmarked, reproducible pipeline + TE annotation.
- What was already known: Subfamily-level TE tools (RepEnrich, TEtranscripts, SalmonTE) that cannot resolve specific loci.

# Strengths
- Design strength: Head-to-head benchmark vs six methods with simulated ground truth.
- Validation strength: Precision/recall/F1 quantified; comparator error modes characterized.
- Reproducibility strength: MIT open-source, bioconda, snakemake pipeline, tutorial, test data.
- Translational realism: Real ENCODE data; large fragment volume.

# Limitations and bias risks
- Sample-size / power: Benchmark on simulations + 13 ENCODE cell types.
- Confounding: N/A (quantification benchmark).
- Batch / site effects: N/A.
- Pseudoreplication risk: N/A.
- Leakage / overfitting risk: Simulation truth controls this; real-data accuracy depends on annotation quality.
- Generalizability: Human (hg38) HERV/TE focus; bulk RNA-seq; not single-cell-native; accuracy bounded by TE annotation completeness.
- Missing controls / validation: Performance on non-human genomes / single-cell not assessed.
- Author-stated limitations: Accuracy depends on annotation and alignment; comparator tools required annotation modification for locus-level comparison.
- Additional limitations identified during review: Exact repo URL/version not in retrieved text (in abstract); older (2019) — check for updated versions.

# Transferability to the user's work
- Directly transferable elements: Telescope itself for locus-level TE/HERV quantification in human bulk RNA-seq (e.g., neurodegeneration cohorts where TE/HERV dysregulation is implicated).
- Elements requiring adaptation: Single-cell/snRNA-seq application (not native); non-human genomes; current annotation/version.
- Model, species, tissue, matrix, platform, or scale mismatch: Bulk vs single-cell; human-specific annotation.
- Assumptions required for transfer: Good alignment + up-to-date TE annotation; fragment-abundance proportionality.
- Confidence: high (well-benchmarked, open tool).

# Practical implications
- Experimental implication: N/A (computational).
- Analysis implication: Use Telescope for locus-resolved TE/HERV quantification; prefer over family-level tools when locus specificity matters; pair with donor-aware DE (cf. Prieto León 2025) for TE differential expression.
- Public dataset implication: ENCODE benchmark + annotation reusable.
- Biomarker / translational implication: Locus-specific HERV expression as candidate markers.
- Grant / manuscript implication: Citable, validated TE-quantification method.

# Contradictions and links
- Supports: Need for locus-level (not subfamily) TE quantification.
- Contradicts: Adequacy of unique/best-count and family-level approaches (shown to under/over-estimate).
- Replicates: N/A.
- Methodologically comparable papers: RepEnrich, TEtranscripts, SalmonTE (benchmarked against); Prieto León 2025 (downstream donor-aware DE on TE counts).
- Relevant synthesis notes: candidate for a "TE/HERV quantification methods" comparison.
- Relevant project decisions: (none yet)

# Follow-up actions
- [ ] Confirm current Telescope version/repo (github.com/mlbendall/telescope) and any single-cell extensions
- [ ] Evaluate annotation currency for hg38/T2T
- [ ] Consider a methods record in 04_METHODS/software/ for Telescope
- [ ] Check retraction/correction status

# Priority decision
- Priority: 1
- Read now (retain for methods/software)
- Rationale: A benchmarked, open, reusable locus-level TE/HERV quantifier directly matching a stated discovery priority; immediately actionable for any TE/HERV analysis. Bulk-only and 2019-era are the only caveats (verify current version).
