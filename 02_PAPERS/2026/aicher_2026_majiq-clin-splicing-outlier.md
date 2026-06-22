---
record_type: paper
record_status: needs_full_text
canonical_id: "10.1016/j.gim.2026.102628"
doi: "10.1016/j.gim.2026.102628"
pmid: "42267532"
title: "MAJIQ-CLIN: A novel tool to help identify Mendelian disease-causing variants from RNA-Seq data"
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
- Full citation: Aicher JK, Issakova D, Slaff B, Jewell S, Lahens NF, Grant GR, Baralle D, Rosenfeld JA, Scott DA, [et al.], Bhoj EJ, Barash Y. "MAJIQ-CLIN: A novel tool to help identify Mendelian disease-causing variants from RNA-Seq data." *Genetics in Medicine* 2026; in press, 102628.
- DOI / PMID / stable URL: [DOI](https://doi.org/10.1016/j.gim.2026.102628) · PMID 42267532
- Related preprint or published version: Peer-reviewed (Genet Med). PMCID not yet assigned at verification.
- Correction, expression of concern, or retraction status: **Unknown** — not checked (added 2026-06-22).

*Source: metadata + abstract (PubMed). Full text not inspected — set needs_full_text. According to PubMed, DOI [10.1016/j.gim.2026.102628](https://doi.org/10.1016/j.gim.2026.102628).*

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Fills the Domain-3 **splicing / outlier-detection** sub-theme. A method to detect, quantify, prioritize, and visualize **RNA splicing aberrations in a single patient vs a control cohort** (outlier LSVs and private LSVs), benchmarked on synthetic data and real Undiagnosed Diseases Network cases. Directly relevant to the user's "splicing and outlier detection" signal and to any rare-disease/aberrant-event analysis from bulk RNA-seq.
- Why it is more or less useful than neighboring literature: A clinically oriented, single-patient outlier framework (complementary to cohort DE/DTU tools and to saseR's scalable aberrant-event detection); claims favorable accuracy + efficiency vs existing tools and avoids reprocessing when data are added. Less general than saseR (splicing-focused), so paired as a method comparison.

# Source inspection status
- Abstract inspected: yes
- Full text inspected: no
- Methods inspected: partial (concepts: oLSV/pLSV, synthetic + real evaluation)
- Supplement inspected: no
- Figures/tables inspected: no
- Code repository inspected: no (MAJIQ-CLIN tool not located/verified this pass)
- Data repository inspected: no
- Missing material: full Methods, benchmark details (tools compared, metrics), UDN case results, software availability/version, synthetic-data generator.

# Study question and hypothesis
- Primary question: Can RNA splicing aberrations be reliably detected, quantified, prioritized, and visualized in individual patients vs controls to raise the Mendelian diagnostic rate?
- Stated hypothesis: A scalable LSV-based outlier method (oLSV/pLSV) improves detection of splice-altering variants over existing tools.
- Study type: Computational method development + benchmark (synthetic + real clinical RNA-seq).

# Biological or clinical context
- Disease / exposure / process: Suspected Mendelian genetic disorders (diagnostic RNA-seq).
- Organism: Human.
- Tissue / cell type: Patient RNA-seq (tissue not specified in abstract).
- Model system: Synthetic data + real patient cohorts (incl. Undiagnosed Diseases Network).
- Cohort or population: Control cohort + patient samples; counts not extracted.
- Relevant stage/severity: N/A.

# Study design
- Experimental or observational unit: Patient RNA-seq sample vs control cohort.
- Unit of inference: Per-patient local splicing variation (LSV) outlier calls.
- Groups and sample size per group: Not extracted.
- Replicates / randomization / blinding: N/A / not extracted.
- Inclusion / exclusion criteria: Not extracted.
- Batch structure: Tool claims to control confounders such as batches (verify).
- Controls and comparators: Control cohort for outlier calling; comparison to existing splicing-outlier tools (e.g., FRASER-class — not confirmed).

# Experimental methods
- Assay / platform: Bulk RNA-seq (patient vs control).
- Sample preparation: N/A (computational).
- Endpoint: Detection of outlier LSVs (oLSV) and private LSVs (pLSV); prioritization + visualization.
- QC criteria: Not extracted.
- Exact reusable parameters and source location: oLSV/pLSV definitions; incremental processing (no reprocessing on new data) — details in Methods (needs_full_text).

# Computational and statistical methods
- Raw input: Patient + control RNA-seq.
- Preprocessing: MAJIQ-style LSV quantification (build on MAJIQ framework — inferred from name; verify).
- Statistical model: Outlier detection of LSV deviations vs control distribution (exact model not extracted).
- Multiple-testing correction: Not extracted.
- Effect-size reporting: Accuracy vs synthetic ground truth (numbers not extracted).
- Batch handling: Claims confounder/batch control.
- Validation strategy: Systematic synthetic benchmark across aberration types + transcript inclusion levels; solved-case recovery on real datasets; application to unsolved UDN cases.
- External validation: Real clinical datasets (UDN).
- Software / versions: MAJIQ-CLIN (version not extracted); availability not confirmed.
- Code availability: Not confirmed.

# Data and resource availability
- Repository and accession: Not extracted.
- Raw/processed data available: Unverified.
- Metadata completeness: Unverified.
- Data-use restrictions: Clinical patient data — likely controlled.
- Reusability for the user's work: Tool potentially directly usable for splicing-outlier analysis once availability confirmed.

# Main findings
| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| MAJIQ-CLIN detects oLSVs/pLSVs from patient vs control RNA-seq | Reported | Abstract | qualitative | Partial | full text needed |
| Compares favorably in accuracy + efficiency to existing tools | Reported | Abstract | numbers not in abstract | Partial | tools/metrics not extracted |
| Validated on synthetic data across aberration types/inclusion levels | Reported | Abstract | synthetic benchmark | Partial | details not extracted |
| Recovers solved test cases; applied to unsolved UDN cases | Reported | Abstract | qualitative | Partial | case counts not extracted |
| Efficient on large datasets; no reprocessing when data added | Reported | Abstract | qualitative | Partial | — |

# What is actually new?
- Methodological novelty: Single-patient splicing-outlier (oLSV/pLSV) framework with incremental scaling and visualization for diagnostics.
- Dataset/resource novelty: Synthetic splicing-aberration benchmark (availability unverified).
- What was already known: FRASER/LeafCutterMD-class outlier splicing tools; MAJIQ LSV quantification.

# Strengths
- Design strength: Synthetic ground-truth benchmark + real clinical application.
- Validation strength: Solved-case recovery + UDN deployment.
- Reproducibility strength: Incremental processing avoids reruns (claimed).
- Translational realism: Clinical diagnostics focus.

# Limitations and bias risks
- Sample-size / power: Cohort/case counts not extracted.
- Confounding: Tissue expression of the relevant gene limits detectability (general caveat for RNA-seq diagnostics).
- Batch / site effects: Claims control; verify.
- Pseudoreplication / leakage / overfitting: N/A or not assessable without full text.
- Generalizability: Tissue-dependent; performance vs each competitor tool not extracted.
- Missing controls / validation: Cannot assess fully (needs_full_text).
- Author-stated limitations: Not extracted.
- Additional limitations identified during review: Tool availability/version unconfirmed.

# Transferability to the user's work
- Directly transferable elements: oLSV/pLSV outlier concept; patient-vs-control splicing diagnostic workflow.
- Elements requiring adaptation: Tissue choice; control-cohort construction.
- Mismatch: Mendelian-diagnostics framing vs broader transcriptomics.
- Assumptions required for transfer: Adequate control cohort; gene expressed in sampled tissue.
- Confidence: moderate (pending full text).

# Practical implications
- Experimental implication: Collect a matched control RNA-seq cohort for outlier splicing analysis.
- Analysis implication: Consider MAJIQ-CLIN alongside saseR/FRASER for aberrant-splicing detection; compare tools.
- Public dataset implication: Synthetic benchmark may be reusable.
- Biomarker / translational implication: Splice-outlier prioritization for diagnostics.
- Grant / manuscript implication: Methods option for splicing-outlier pipelines.

# Contradictions and links
- Supports: Need for splicing-aware diagnostic tools (cf. saseR).
- Contradicts: none identified.
- Replicates: Concept overlaps FRASER-class tools.
- Methodologically comparable papers: segers_2025 (saseR aberrant splicing/expression), bendall_2019 (TE quantification), prieto-leon_2025 (RUV/pseudobulk).
- Relevant synthesis notes: seed for "aberrant splicing / outlier detection methods comparison."
- Relevant project decisions: (none yet)

# Follow-up actions
- [ ] Obtain full text; extract benchmark tools, metrics, case counts, software availability/version
- [ ] Confirm MAJIQ-CLIN code/release and license
- [ ] Cross-link with saseR for a methods synthesis
- [ ] Check correction/retraction status

# Priority decision
- Priority: 2
- Retain for methods (needs full text)
- Rationale: Directly addresses the splicing/outlier-detection signal with a clinically validated tool, but Methods/benchmark/availability uninspected — promote/finalize after full-text review.
