---
record_type: paper
record_status: needs_full_text
canonical_id: "10.1101/2025.09.30.679471"
doi: "10.1101/2025.09.30.679471"
pmid: "41256511"
pmcid: "PMC12621674"
title: "Nephrobase Cell+: Multimodal Single-Cell Foundation Model for Decoding Kidney Biology"
year: 2025
source_type: preprint
peer_reviewed: false
full_text_checked: false
supplement_checked: false
code_checked: false
data_checked: false
last_verified: 2026-06-22
priority: 3
projects: []
topics: [transcriptomics, single_cell, spatial_omics, multi_omics]
methods: [analysis_method, scRNAseq, snRNAseq, snATACseq, spatial_transcriptomics]
datasets: []
---

# Citation
- Full citation: Li C, Ziyadeh E, Sharma Y, Dumoulin B, Levinsohn J, Ha E, Pan S, Rao V, Subramaniyam M, Szegedy M, Zhang N, Susztak K. "Nephrobase Cell+: Multimodal Single-Cell Foundation Model for Decoding Kidney Biology." *bioRxiv* 2025 (preprint).
- DOI / PMID / stable URL: [DOI](https://doi.org/10.1101/2025.09.30.679471) · PMID 41256511 · PMC12621674
- Related preprint or published version: **Preprint (bioRxiv) — not peer-reviewed.** Monitor for journal publication.
- Correction, expression of concern, or retraction status: **Unknown / preprint** — not checked (added 2026-06-22).

*Source: metadata + abstract (PubMed). Full text not inspected — set needs_full_text. According to PubMed, DOI [10.1101/2025.09.30.679471](https://doi.org/10.1101/2025.09.30.679471).*

# Why this source matters
- Decision, hypothesis, protocol, dataset, or interpretation it may affect: Fills the Domain-3 **foundation-model** sub-theme (and the cross-cutting "foundation models, benchmarking, batch handling, transferability" signal). An **organ-focused** multimodal single-cell foundation model (kidney) explicitly benchmarked against generalist models (Geneformer, scGPT, UCE) and classical methods (PCA, autoencoders) on batch mixing, cluster concordance, cross-species alignment, and **zero-shot annotation**. Useful as a methods reference even though the organ (kidney) is off the user's neuro domains — the architecture, benchmarking design, and organ-specific-vs-generalist question transfer.
- Why it is more or less useful than neighboring literature: Provides a concrete, multimodal (scRNA/snRNA/snATAC/spatial), cross-species pretraining + benchmark template; but it is a **preprint**, kidney-specific, and self-benchmarked (authors' own model wins) — interpret performance claims cautiously. Priority 3 (background/watchlist) given off-domain tissue + preprint status + self-comparison bias.

# Source inspection status
- Abstract inspected: yes
- Full text inspected: no
- Methods inspected: partial (architecture + benchmark scope from abstract)
- Supplement inspected: no
- Figures/tables inspected: no
- Code repository inspected: no
- Data repository inspected: no
- Missing material: full Methods, exact benchmark metrics/datasets, train/test split, independent (non-author) baselines, model/data availability.

# Study question and hypothesis
- Primary question: Can an organ-focused single-cell foundation model outperform generalist foundation models for kidney single-cell analysis (integration, annotation, cross-species)?
- Stated hypothesis: Organ-scale multimodal pretraining yields more robust, transferable representations than generalist models.
- Study type: Foundation-model development + benchmark (preprint).

# Biological or clinical context
- Disease / exposure / process: Kidney biology/disease (off the user's neuro domains).
- Organism: Human, mouse, rat, pig.
- Tissue / cell type: Kidney single-cell/nucleus + spatial.
- Model system: Large multimodal single-cell compendium.
- Cohort or population: ~4,319 samples; ~39.5M single-cell/nucleus profiles.
- Relevant stage/severity: N/A.

# Study design
- Experimental or observational unit: Cell/nucleus profile.
- Unit of inference: Cell-level embedding / annotation.
- Groups / sample size: ~39.5M profiles, 4,319 samples, 4 species, multiple modalities; pretraining ~100B tokens.
- Replicates / randomization / blinding: N/A.
- Inclusion / exclusion criteria: Not extracted.
- Batch structure: Donor/assay batches — explicitly targeted for correction.
- Controls and comparators: Geneformer, scGPT, UCE, PCA, autoencoders.

# Experimental methods
- Assay / platform: scRNA-seq, snRNA-seq, snATAC-seq, spatial transcriptomics (pretraining corpus).
- Model: Transformer encoder-decoder with gene-token cross-attention + mixture-of-experts; variants at 500M, 1B, and larger.
- Endpoint: Embedding quality, batch mixing, cluster concordance, cross-species homolog alignment, zero-shot annotation accuracy.
- Exact reusable parameters and source location: ~100B-token pretraining; MoE + gene-token cross-attention design (Methods — needs_full_text).

# Computational and statistical methods
- Raw input: Multimodal single-cell profiles.
- Preprocessing: Tokenization (~100B tokens); details not extracted.
- Statistical model: Self-supervised transformer pretraining; downstream embedding/annotation evaluation.
- Effect-size reporting: ">90% zero-shot annotation accuracy for major kidney lineages" (human + mouse); "highest cluster concordance and batch-mixing scores" (exact metrics not extracted).
- Batch handling: Removes donor/assay batch effects while preserving cell-type structure (claimed).
- Validation strategy: Cross-species evaluation; comparison to generalist models + classical baselines.
- External validation: Cross-species (human/mouse alignment); independent third-party benchmark not described.
- Software / versions: Not extracted.
- Code/model availability: Not extracted (verify; foundation-model weights/data availability is decision-relevant).

# Data and resource availability
- Repository and accession: Not extracted.
- Raw/processed data available: Unverified.
- Metadata completeness: Unverified.
- Data-use restrictions: Depends on source datasets.
- Reusability for the user's work: Model is kidney-specific; methodology/benchmark design reusable; weights availability unverified.

# Main findings
| Claim | Evidence type | Figure/table/section | Effect size or quantitative result | Directly supported? | Caveat |
|---|---|---|---|---|---|
| First kidney-focused single-cell foundation model | Reported | Abstract | ~39.5M profiles, ~100B tokens, 4 species | Partial | preprint; self-reported |
| Outperforms Geneformer/scGPT/UCE and PCA/autoencoders | Reported | Abstract | highest cluster concordance + batch mixing | Partial | self-benchmarked; metrics not extracted |
| >90% zero-shot annotation accuracy (human + mouse) | Reported | Abstract | >90% major lineages | Partial | exact protocol not extracted |
| 500M/1B variants also beat existing models | Reported | Abstract | qualitative | Partial | — |

# What is actually new?
- Methodological novelty: Organ-focused multimodal foundation model with MoE + gene-token cross-attention; organ-vs-generalist comparison.
- Dataset/resource novelty: Large kidney multimodal compendium + model (availability unverified).
- What was already known: Generalist single-cell foundation models (Geneformer, scGPT, UCE) and their batch/transferability limitations.

# Strengths
- Design strength: Large multimodal, cross-species pretraining; multiple model sizes.
- Validation strength: Multiple benchmark axes + cross-species.
- Reproducibility strength: Unverified (code/weights availability not confirmed).
- Translational realism: Kidney disease genomics.

# Limitations and bias risks
- Sample-size / power: Large corpus, but benchmark composition not extracted.
- Confounding / batch: Claims correction; independent verification absent.
- Pseudoreplication / leakage / overfitting: Pretraining/eval split and leakage controls not extracted — important for foundation-model claims.
- Generalizability: Kidney-specific; off the user's neuro domains.
- Missing controls / validation: Self-benchmarked (authors' model wins); no independent third-party evaluation.
- Author-stated limitations: Not extracted.
- Additional limitations identified during review: Preprint (not peer-reviewed); foundation-model performance claims warrant the signal-file caution (assumptions, leakage, independent comparison).

# Transferability to the user's work
- Directly transferable elements: Benchmark design (batch mixing, cluster concordance, zero-shot annotation, cross-species); organ-specific-vs-generalist framing.
- Elements requiring adaptation: Tissue (kidney → brain); the model itself is not brain-applicable.
- Mismatch: Kidney vs neuro; preprint.
- Assumptions required for transfer: Comparable evaluation metrics; leakage-controlled benchmarking.
- Confidence: low-moderate (methods template only).

# Practical implications
- Experimental implication: If considering a brain single-cell foundation model, reuse this benchmark battery.
- Analysis implication: Evaluate foundation models on batch mixing + zero-shot annotation with independent baselines; beware self-comparison bias.
- Public dataset implication: Watch for model/weights release.
- Biomarker / translational implication: Limited (off-domain).
- Grant / manuscript implication: Background on organ-specific foundation models.

# Contradictions and links
- Supports: Generalist foundation models have batch/transferability limits.
- Contradicts: Potentially the "generalist is sufficient" view (self-benchmarked — caution).
- Replicates: N/A.
- Methodologically comparable papers: zappia_2025 (feature selection for integration/querying), prieto-leon_2025 (count-model normalization).
- Relevant synthesis notes: watchlist for "single-cell foundation models + benchmarking."
- Relevant project decisions: (none yet)

# Follow-up actions
- [ ] Monitor for peer-reviewed publication and code/weights release
- [ ] On full text: extract exact benchmark metrics, datasets, leakage controls
- [ ] Re-evaluate priority if a brain foundation model becomes relevant
- [ ] Check preprint→publication status

# Priority decision
- Priority: 3
- Watchlist / retain for background (methods template)
- Rationale: Strong foundation-model + benchmarking exemplar for the Domain-3 signal, but kidney-specific, preprint, and self-benchmarked — background value with a monitoring action, not decision-changing for the user's neuro work.
