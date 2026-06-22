# Corpus Expansion Log

Chronological record of each corpus-expansion pass. The most recent run's date sets the `date_from`
window for the next monthly pass. Newest entries at the top. Maintained by the `expand-corpus` skill.

---

## 2026-06-22 — Deepen pass #2 (mode: deepen)
**Window:** none (date-agnostic). **Added: 9 records.** Library total: 13 → **22**.
Per-domain (before → after): D1 4→6, D2 3→5, D3 3→6, D4 3→5.

### Queries per domain
- **D1 Neurodeg/TBI/ALS/AD:** "plasma tau-PET fluid biomarker ptau217 cohort"; "C9orf72 ALS FTD single-nucleus glial states cortex".
- **D2 SWCNT/biosensors:** "SWCNT NIR sensor ML EEM biofluid" (PubMed 0 hits → WebSearch); "carbon nanotube optical nanosensor serum ML corona phase"; WebSearch "SWCNT sensor array ML serum biomarker"; "ovarian cancer quantum-defect CNT serum ML".
- **D3 Transcriptomics:** "aberrant splicing outlier detection RNA-seq rare disease method"; "single-cell foundation model transcriptomics benchmark zero-shot"; "scRNA-seq integration benchmark batch effect".
- **D4 Mechanobiology:** "ECM stiffness remodeling reactive astrocyte hydrogel mechanotransduction" (PubMed over-specified → WebSearch); WebSearch "ECM stiffness neural injury astrocyte hydrogel 3D mechanobiology"; "compression injury astrocyte 3D hydrogel".

### Records ADDED (path + priority + status)
- **D1** `02_PAPERS/2025/warmenhoven_2025_ptau217-head-to-head-biofinder2.md` — P1, verified (abstract/metadata; full text not inspected). PMID 39468767.
- **D1** `02_PAPERS/2023/li_2023_c9orf72-snrna-snatac-als-ftd.md` — P1, verified (PMC full text inspected). PMID 37714849.
- **D2** `02_PAPERS/2022/kim_2022_swcnt-ovarian-cancer-serum-ml.md` — P1, verified (abstract/metadata). PMID 35301449.
- **D2** `02_PAPERS/2025/tian_2025_swcnt-nir-ml-virus-spectral-decoding.md` — P2, verified (abstract/metadata). PMID 40574605.
- **D3** `02_PAPERS/2026/aicher_2026_majiq-clin-splicing-outlier.md` — P2, needs_full_text. PMID 42267532.
- **D3** `02_PAPERS/2026/segers_2026_saser-aberrant-splicing-expression.md` — P2, needs_full_text. Published Genome Biology DOI 10.1186/s13059-026-03973-8 (canonical); preprint PMID 39464066 inspected.
- **D3** `02_PAPERS/2025/li_2025_nephrobase-cell-plus-foundation-model.md` — P3, needs_full_text (preprint). PMID 41256511.
- **D4** `02_PAPERS/2023/saleh_2023_ecm-stiffness-composition-astrocyte.md` — P2, verified (PMC full-text page inspected). PMID 37233366.
- **D4** `02_PAPERS/2025/wip_2025_compression-injury-astrocyte-3d-hydrogel.md` — P2, needs_full_text (bioRxiv 403; author list Unknown). DOI 10.1101/2025.06.20.660800.

### Candidates SKIPPED (one-line reason)
- Fernández Arias 2025 (Brain, p-tau217 memory, PMID 39879633) — strong D1 candidate but redundant with Warmenhoven for this pass; hold for next pass (would push D1 to 7).
- "Spectral Fingerprinting of Engineered Nanomaterials for Precision Biosensing" (ACS Nano 5c18348) — review/perspective, not primary; orient-only.
- Acharya 2024 (Adv Mater Technol) SWCNT optical biosensor review — review, not primary.
- Shtepliuk 2026 (Adv Intell Syst) electronic-nose ovarian cancer — not SWCNT/optical; off the spectral-phenotyping axis.
- General scRNA-seq integration benchmark hits (PMIDs 31948481, 34949812, 39703500, etc.) — zappia_2025 already covers feature-selection-for-integration; defer cross-cohort harmonization to a dedicated next-pass query.

### Notes / needs_full_text (revisit when access available)
- needs_full_text: aicher_2026, segers_2026, li_2025 (preprint), wip_2025 (bioRxiv 403 + author list Unknown).
- Verified-but-abstract-only (promote after full text): warmenhoven_2025, kim_2022, tian_2025.
- Carried over from seed: braun_2021, carvalho_2023, yoon_2025.
- Data accessions unconfirmed for li_2023 and warmenhoven_2025 (verify GEO / BioFINDER terms before reuse).
- **Gaps to target next pass:** D3 cross-cohort harmonization + spatial integration still thin (foundation-model slot is off-domain kidney). D2 dispersion/corona QC + in-vivo nanosensor still unrepresented. D4 blast/impulse calibration (have organoid blast sirtori_2025 + compression wip_2025; want a calibrated shock-tube/impulse primary) and confinement migration unrepresented.

---

## 2026-06-22 — Seed build (mode: deepen)
**Window:** none (initial build). **Added: 12 records** + 1 pre-existing (Ruf 2026) = 13 total.

By domain (3 each):
- **Neurodegeneration/TBI/ALS/AD:** leng_2021 (P1), castanho_2025 (P2), sirtori_2025 (P1).
- **SWCNT/biosensors:** cho_2021 (P1), lee_2025 (P2), yoon_2025 (P2, needs_full_text).
- **Transcriptomics/single-cell/computational:** bendall_2019 (P1), prieto-leon_2025 (P1), zappia_2025 (P2).
- **Mechanobiology/ECM/barriers:** braun_2021 (P2, needs_full_text), chen_2025 (P2), carvalho_2023 (P3, needs_full_text).

**needs_full_text (revisit when access available):** braun_2021, carvalho_2023, yoon_2025.
**Notes:** 6/13 independently re-verified against PubMed — all real. Next pass: deepen to ~6/domain,
then switch to monthly date-filtered runs.
