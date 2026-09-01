# Corpus Expansion Log

Chronological record of each corpus-expansion pass. The most recent run's date sets the `date_from`
window for the next monthly pass. Newest entries at the top. Maintained by the `expand-corpus` skill.

---

## 2026-09-01 — Monthly pass #2 (mode: monthly, window: 2026-07-01 → 2026-09-01)
**Window:** 2026-07-01 to 2026-09-01 (PubMed `datetype=pdat`). **Added: 10 records.** Library total: 34 → **44**.
Per-domain (before → after): D1 9→14, D2 7→9, D3 9→11, D4 9→10.

### Queries per domain
- **D1 Neurodeg/TBI/ALS/AD:** (1) "ALS FTD TDP-43 single cell transcriptomics postmortem cortex 2026" → PMID 42385702 (Zhou Cell, TOP1 somatic mutations); PMID 42551425 (Petrescu Cell, ALS cognitive language/executive snRNA+spatial). (2) "neurodegeneration spatial transcriptomics synucleinopathy dopamine vulnerability 2026" → PMID 42481480 (Rumpf Nat Commun, spatial multi-omics PD substantia nigra). (3) "iPSC organoid APOE4 astrocyte alpha-synuclein tau 2026" → PMID 42636814 (Mesentier-Louro Cell Stem Cell, APOE4 astrocyte cholesterol α-syn miBrains). (4) "FTD frontoinsular cortex single-cell transcriptomics selective vulnerability 2026" → PMID 42523377 (Breevoort bioRxiv, FTD frontoinsular scRNA-seq preprint). Excluded: PMID 42560134 (neuroinflammation AD review) — review; PMID 42276043 (nuclear proteome NSC, May 2026 pub) — outside window; PMID 42049021 (astrocyte collagen ischemic stroke, April 2026) — outside window; PMID 42129551 (OINS neural crest Nature) — outside domain; PMID 42398271 (15-PGDH PD neuroprotection) — pharmacological, not cell-type transcriptomic primary; PMID 42660464 (TBI multi-omics review) — review; PMID 42421066 (NETs NMOSD BBB) — off-domain autoimmune.
- **D2 SWCNT/biosensors:** (1) PubMed "single-walled carbon nanotube NIR fluorescence sensor biofluid 2026 [datetype=pdat]" → PMID 42409644 (Israel Nano Lett, ssDNA-SWCNT spectral fingerprinting 4 anthracyclines in synthetic urine/sweat, PMC open). (2) "SWCNT fiber probe neural dopamine imaging near-infrared 2026" → PMID 42503866 (Shin ACS Nano, NeuRIFI dual-readout NIR fiber probe, DNA-SWCNT, 90 nM DA, ex vivo brain). No additional on-domain SWCNT papers identified in window.
- **D3 Transcriptomics/single-cell/spatial/multi-omics:** (1) "spatial transcriptomics cross-omics integration translation transformer 2026" → PMID 42426404 (Wang Nat Methods, NicheTrans spatial cross-omics translation). (2) "NHP macaque brain atlas single-cell aging lifespan multimodal 2026" → PMID 42612631 (Zhang Cell, multimodal macaque brain atlas 2.9M nuclei 8 regions 23 female macaques). Also found and deferred: PMID 42462710 (Cell, isoform-resolved spatial MERFISH — strong D3 candidate but July 2026 pub date confirmed, will capture in deepen pass); PMID 42190664 (Cell, spatial CRISPR screen) — off-domain cancer. Excluded PMID 42137938 (HFpEF snRNA-seq cardiac) — off-domain. Excluded PMID 42276047 (pancreatic cancer scRNA-seq) — off-domain.
- **D4 Mechanobiology/BBB:** (1) "blood-brain barrier aging transcytosis caveolin TGF 2026" → PMID 42385697 (Fang Neuron, TGF-β1-induced endothelial transcytosis drives age-related BBB leakage). (2) "BBB mechanobiology neural ECM confinement 2026" → confirmed D4 record already in library (trivedi, strat, chen). No additional D4 primary studies confirmed in window beyond Fang 2026. Excluded PMID 42261674 (baroreceptor mechanotransduction review) — review; excluded PMID 42049021 (astrocyte collagen ischemic stroke) — outside window.

### Records ADDED (path + priority + status)
- **D1** `02_PAPERS/2026/zhou_2026_top1-somatic-mutations-als-ftd-ad.md` — **P1, partial (PMC full text inspected: methods, results)**. PMID 42385702, DOI 10.1016/j.cell.2026.06.013, PMCID PMC13340254. Cell 2026-07-01. Single-cell WGS (PTA+FANS) of 469 neurons from ALS (6 C9orf72), FTD (6 C9orf72), AD (29), and controls; TOP1-mediated 2-bp deletion signature shared across diseases; cerebellar neurons spared; validated in iPSC CRISPRi TDP-43 KD.
- **D1** `02_PAPERS/2026/rumpf_2026_spatial-multiomics-synucleinopathy-dopamine.md` — **P1, needs_full_text**. PMID 42481480, DOI 10.1038/s41467-026-74961-6. Nat Commun 2026-07-21. Spatial transcriptomics + spatial proteomics + αSyn SAA in PD substantia nigra; early synaptic pruning + context-specific dopaminergic vulnerability.
- **D1** `02_PAPERS/2026/petrescu_2026_als-cognitive-language-snrna-spatial.md` — **P1, needs_full_text**. PMID 42551425, DOI 10.1016/j.cell.2026.07.008. Cell 2026-08-04. Spatial + snRNA-seq of ALS prefrontal cortex; distinct cellular phenotypes of language vs. executive decline in ALS.
- **D1** `02_PAPERS/2026/mesentier-louro_2026_apoe4-astrocyte-alpha-syn-mibrains.md` — **P2, needs_full_text**. PMID 42636814, DOI 10.1016/j.stem.2026.08.001. Cell Stem Cell 2026-08-24. APOE4 astrocyte cholesterol dysregulation promotes α-synuclein pathology in iPSC-derived miBrain organoids.
- **D1** `02_PAPERS/2026/breevoort_2026_ftd-frontoinsular-cortex-snrnaseq-vulnerability.md` — **P2, needs_full_text (preprint)**. PMID 42523377, DOI 10.64898/2026.07.13.738307. bioRxiv 2026-07-14. snRNA-seq atlas of FTD frontoinsular cortex; molecular correlates of selective neuronal vulnerability in behavioral variant FTD.
- **D2** `02_PAPERS/2026/israel_2026_swcnt-anthracycline-nir-spectral-fingerprinting.md` — **P2, partial (PMC full text inspected)**. PMID 42409644, DOI 10.1021/acs.nanolett.6c01777, PMCID PMC13397890. Nano Lett 2026. 84-element ssDNA-SWCNT array (12 ssDNA × 7 SWCNT chiralities); XGBoost 100% 4-class anthracycline classification; SHAP feature attribution; validated in synthetic urine + sweat.
- **D2** `02_PAPERS/2026/shin_2026_swcnt-fiber-probe-dopamine-neuroimaging.md` — **P2, needs_full_text**. PMID 42503866, DOI 10.1021/acsnano.6c07740. ACS Nano 2026-08-11. NeuRIFI: DNA-SWCNT on implantable optical fiber; dual-readout (photometry + remote NIR imaging) DA mapping; 90 nM sensitivity, 20 ms temporal, ~1.5 μm/pixel spatial; validated in tissue phantoms + ex vivo mouse brain (3 mm depth).
- **D3** `02_PAPERS/2026/wang_2026_nichetrans-spatial-crossomics-translation.md` — **P2, needs_full_text**. PMID 42426404, DOI 10.1038/s41592-026-03153-3. Nat Methods 2026-07-09. NicheTrans: Transformer-based spatial cross-omics translation incorporating cell-cell niche context; applied to AD brain glial spatial data.
- **D3** `02_PAPERS/2026/zhang_2026_macaque-brain-atlas-lifespan-multimodal.md` — **P2, needs_full_text**. PMID 42612631, DOI 10.1016/j.cell.2026.07.045. Cell 2026-08-18. Multimodal (snRNA-seq + snATAC-seq) atlas; 2,955,873 nuclei; 8 brain regions; 23 female cynomolgus macaques; adult lifespan coverage.
- **D4** `02_PAPERS/2026/fang_2026_tgfb1-bbb-transcytosis-aging.md` — **P1, needs_full_text**. PMID 42385697, DOI 10.1016/j.neuron.2026.06.003. Neuron 2026-07-01. TGF-β1 drives age-related BBB leakage via endothelial caveolar transcytosis (not tight junctions); onset at midlife; AAV knockdown of caveolin-1 or Mfsd2a restoration reverses leakage.

### Candidates SKIPPED (one-line reason)
- PMID 42560134 (neuroinflammation AD, Int J Dev Neurosci) — review.
- PMID 42276043 (nuclear proteome NSC, Cell May 2026) — pub date 2026-05, outside window.
- PMID 42049021 (astrocyte collagen ischemia, Cell Metab April 2026) — pub date 2026-04, outside window.
- PMID 42129551 (OINS neural crest, Nature) — off-domain (developmental visceral nervous system).
- PMID 42398271 (15-PGDH PD neuroprotection, Redox Biol) — pharmacological, not cell-type transcriptomic primary.
- PMID 42660464 (TBI multi-omics aging review, Ageing Res Rev) — review.
- PMID 42421066 (NETs NMOSD BBB, J Neuroinflammation) — off-domain autoimmune.
- PMID 42261674 (baroreceptor mechanotransduction review, Hypertension) — review.
- PMID 42462710 (Cell, isoform-resolved spatial MERFISH, June 2026) — pub date confirmed 2026-06, outside window; record for next pass.
- PMID 42190664 (spatial CRISPR screen, Cell) — off-domain (cancer).
- PMID 42276047 (pancreatic cancer snRNA-seq, Cancer Cell) — off-domain.
- PMID 42137938 (HFpEF cardiac snRNA-seq, Circ Res) — off-domain (cardiac).
- All Journal of Ethnopharmacology hits (42532227, 42497599, 42492703, 42492702, 42486454, 42476206, 42472598, 42462419) — off-domain (TCM, hepatotoxicity, microbiology).
- Carbon catabolite repression papers (42662560, 42602370) — off-domain (microbiology/bioprocessing).

### Notes / needs_full_text (revisit when access available)
- needs_full_text: rumpf_2026 — Nat Commun open access; retrieve for cohort size, spatial platform, data accession.
- needs_full_text: petrescu_2026 — Cell paywall; retrieve for cohort, spatial platform, data accession.
- needs_full_text: mesentier-louro_2026 — Cell Stem Cell paywall; retrieve for miBrain protocol details.
- needs_full_text: breevoort_2026 — bioRxiv preprint; retrieve for cohort composition, FTD subtypes, data accession; monitor for peer review.
- needs_full_text: shin_2026 — ACS Nano paywall; retrieve for DNA sequence, SWCNT chirality, fiber functionalization protocol.
- needs_full_text: wang_2026 — Nat Methods paywall; retrieve for benchmark details, code availability, AD dataset accession.
- needs_full_text: zhang_2026 — Cell paywall; retrieve for brain regions profiled, age range, data accession.
- needs_full_text: fang_2026 — Neuron paywall, no PMC; retrieve for animal model, sample sizes, TGF-β1 mechanism details.
- Zhou 2026 supplement not inspected — Tables S1–S5 contain case metadata, QC, mutation catalogs.
- Israel 2026 supplement not inspected — detailed dispersion protocol and exact ssDNA sequences.

### Gaps to target next pass (2026-09-01 → next monthly)
- **D1:** Blast TBI primary studies with calibrated pressure/impulse waveforms still absent (only organoid + C. elegans in library). isoform-resolved spatial MERFISH (PMID 42462710, Cell June 2026) deferred — check in next pass.
- **D2:** No in vivo implantable SWCNT neural sensor primary (Shin 2026 ex vivo only). Corona-phase QC in real patient biofluids still thin.
- **D3:** Cross-cohort harmonization benchmark (PRIME/GAMMI) still absent. NicheTrans benchmark performance vs. comparators needs full-text confirmation.
- **D4:** Confinement/migration assay linked to neural or glial phenotype (gap from previous passes). Verify Fang 2026 animal model details and check for RNA-seq data deposit.

---

## 2026-07-01 — Monthly pass #1 (mode: monthly, window: 2026-06-22 → 2026-07-01)
**Window:** 2026-06-22 to 2026-07-01 (publication date filter). **Added: 4 records.** Library total: 30 → **34**.
Per-domain (before → after): D1 8→9, D2 7→7 (no new records), D3 8→9, D4 7→9.

### Queries per domain
- **D1 Neurodeg/TBI/ALS/AD:** "neurodegeneration ALS TDP-43 tau biomarker single cell 2026" + "tauopathy FTLD biomarker CSF 2026" (PubMed, date-filtered). Top hits triage: TREM2 review (Mol Psychiatry, PMID 41792456) → review, skip; β2M aging brain (PMID 42082100) → review, skip; tauopathy drug status review → review, skip. Selected: Kac 2026 (PMID 42340485, Acta Neuropathol, published 2026-06-24) — p-tau/tau368 ratio for FTLD-tau vs FTLD-TDP discrimination; PMC full text retrieved and inspected.
- **D2 SWCNT/biosensors:** "single-walled carbon nanotube SWCNT NIR fluorescence biosensor biofluid serum plasma 2026" (PubMed, date-filtered) + WebSearch ("SWCNT single-walled carbon nanotube NIR fluorescence biosensor biofluid serum plasma 2026"). PubMed: off-domain CNT drug-delivery and materials-science papers only. WebSearch: SWCNT NIR-II high-throughput screening (bioRxiv) — 403 Forbidden on fetch; abstract suggests in vitro characterization, not biofluid sensing. No on-domain SWCNT biosensor primary papers confirmed in window. WebSearch second pass ("ACS Nano OR Small 2026 single-walled carbon nanotube optical sensor serum biomarker near-infrared June July 2026"): confirmed DNA-SWCNT ML paper (PMID 41498822, Nano Lett) published January 7 2026 — outside window → skip. **No D2 candidates found in window.**
- **D3 Transcriptomics:** "single-cell RNA-seq spatial transcriptomics multi-omics integration 2026" + "scRNA-seq splicing differential expression computational method 2026" (PubMed, date-filtered). Most hits off-domain (glioblastoma modeling, intervertebral disc, lymphoma). Selected: Ren 2026 (PMID 42374103, Sci Data, published 2026-06-27) — Stereo-seq unified multi-organ spatial atlas including brain, as D3 benchmark resource (P3).
- **D4 Mechanobiology:** "mechanobiology OR ECM stiffness OR neural injury OR blood-brain barrier OR force signaling OR confinement migration" (PubMed, date-filtered 2026-06-22 to 2026-07-01). Triage: macrophage ICH white matter repair (PMID 42381008, scRNA-seq, off-domain injury type) → skip; medicinal plants AD review → skip; BBB vascular gate neuroendocrine (PMID 42102817, Cell, May 2026) — outside window → confirm: published 2026-05-07 → skip; fenofibrate brain edema TBI → primarily pharmacological, not mechanobiology primary; astrocyte mechanobiology review (PMID 42206674, Glia, 2026-Jul) → viable D4 review (P3); dried platelet BBB repair TBI (PMID 41843452, Blood, 2026-06-25) → P2 primary study with Ang-1/Tie2 mechanism and cortical transcriptomics.

### Records ADDED (path + priority + status)
- **D1** `02_PAPERS/2026/kac_2026_tau368-ftld-tau-csf-biomarker.md` — **P1, verified (PMC full text inspected)**. PMID 42340485, DOI 10.1007/s00401-026-03042-1, PMCID PMC13294230. Acta Neuropathol 2026-06-24. p-tau181/tau368 and p-tau212/tau368 CSF ratios discriminate autopsy-confirmed FTLD-tau from FTLD-TDP; Penn INDD cohort n=176 + UCSD IHC sub-cohort n=16.
- **D3** `02_PAPERS/2026/ren_2026_stereo-seq-multiorgan-spatial-atlas.md` — P3, verified (abstract/metadata). PMID 42374103, DOI 10.1038/s41597-026-07752-9. Sci Data 2026-06-27. Unified Stereo-seq multi-organ dataset (10 mouse organs including brain, 23 sections, cell-bin + bin-50, cell type annotations + matched histology images).
- **D4** `02_PAPERS/2026/trivedi_2026_dried-platelet-bbb-repair-tbi.md` — P2, verified (abstract/metadata). PMID 41843452, DOI 10.1182/blood.2025031826. Blood 2026-06-25. Freeze-dried platelet biologic reduces ICH, restores BBB integrity, attenuates neuroinflammation in murine TBI via Ang-1/Tie2 pathway; includes cortical/hippocampal transcriptomics.
- **D4** `02_PAPERS/2026/strat_2026_astrocyte-mechanobiology-review.md` — P3, verified (abstract/metadata). PMID 42206674, DOI 10.1002/glia.70167. Glia 2026-07. Review synthesizing astrocyte mechanosensing elements (integrins, focal adhesions, junctional proteins, mechanosensitive channels) across development and disease (TBI, glaucoma, glioma).

### Candidates SKIPPED (one-line reason)
- TREM2 in neurodegeneration (PMID 41792456, Mol Psychiatry) — review, orient-only.
- β2M aging brain knowledge mapping (PMID 42082100) — review, orient-only.
- Tauopathy drug-status reviews and miRNA reviews — reviews, orient-only.
- Medicinal plants / phytochemicals for AD (PMID 42382677) — integrative review, off-domain evidence quality.
- BBB vascular gate neuroendocrine cancers (PMID 42102817, Cell, May 2026) — outside window (published 2026-05-07).
- Macrophage CTSS lipid metabolic reprogramming ICH (PMID 42381008) — scRNA-seq primary study but injury type is intracerebral hemorrhage (off-domain from TBI blast/mechanobiology focus); biological question is macrophage lipid handling, not neural mechanobiology or TBI blast.
- Fenofibrate brain edema TBI (identified in search) — pharmacological intervention, not mechanobiology primary; TBI model details not matching D4 calibration gap.
- Glioblastoma evolution modeling (PMID 42374477) — off-domain (cancer biology, not neurodegeneration/TBI).
- SWCNT-related papers identified: DNA-SWCNT ML (PMID 41498822, Nano Lett) — published January 2026, outside monthly window; no biofluid-compatible SWCNT biosensor papers in window.

### Notes / needs_full_text (revisit when access available)
- needs_full_text: trivedi_2026 (Blood paywalled; full text needed for: TBI model type, exact group sizes, transcriptomic platform, data deposition accession; check COI disclosure for Cellphire Therapeutics author).
- needs_full_text: strat_2026 (Glia paywalled; full text needed to extract mechanosensing pathways, signaling molecules, primary studies cited per mechanism).
- needs_full_text: ren_2026 (Scientific Data; verify data accession/repository, data-use terms, brain annotation quality vs. Allen Brain Atlas/BICCN).
- Kac 2026: supplementary tables not inspected (subgroup AUCs, PSP-inclusive analyses, full cohort demographics). Access via PMC supplementary files when needed.
- D2 gap persists: no new on-domain SWCNT biosensor papers in this window. Continue monitoring ACS Nano, Small, Nanoscale, Biosensors and Bioelectronics in next monthly pass.

### Gaps to target next pass (2026-07-01 → next monthly)
- **D1:** Plasma tau368 / plasma biomarker validation of the p-tau/tau368 ratio (author-stated future work in Kac 2026). FTD plasma biomarker and presymptomatic FTLD-tau cohort studies. Any mammalian calibrated shock-tube or blast TBI primary (still absent; only organoid + C. elegans models in library).
- **D2:** Persistent gap: no new biofluid-compatible SWCNT optical nanosensor papers in June window. Continue monitoring for in-vivo neural SWCNT nanosensor and corona-phase QC in biofluid matrices.
- **D3:** Cross-cohort harmonization benchmark still thin (PRIME/GAMMI deferred from deepen pass #3). Verify Ren 2026 data accessibility and evaluate brain tissue annotation quality for benchmarking use.
- **D4:** Confinement/migration assay linked to neural or glial injury readouts (gap from deepen pass #3 still open). Verify Trivedi 2026 transcriptomic data deposition for cross-comparison with organoid/blast TBI datasets.

---

## 2026-06-22 — Deepen pass #3 (mode: deepen, comprehensive)
**Window:** none (date-agnostic). **Added: 8 records.** Library total: 22 → **30**.
Per-domain (before → after): D1 6→8, D2 5→7, D3 6→8, D4 5→7.

### Queries per domain
- **D1 Neurodeg/TBI/ALS/AD:** "TDP-43 cryptic exon biomarker ALS FTD fluid CSF" / "cryptic exon TDP-43 detection assay" (→ Irwin HDGFL2); "blast traumatic brain injury chronic 2025" / "blast overpressure brain injury tau" (most hits clinical/military epi or reviews; selected the C. elegans calibrated shock-wave model).
- **D2 SWCNT/biosensors (PubMed indexes poorly → WebSearch + DOI/PMCID convert):** "SWCNT NIR sensor in vivo implantable biofluid" (→ Heller/Williams implant, Sci Adv 2018); "SWCNT dispersion surfactant corona reproducibility batch QC" (→ Ben Basat dispersion QC).
- **D3 Transcriptomics:** "spatial transcriptomics integration benchmark method single-cell alignment"; "single-cell data integration batch correction benchmark atlas" (→ SIMO, FGOT). Off-domain/biological-application hits (lung ARDS 41455968, etc.) skipped.
- **D4 Mechanobiology:** "confined migration nucleus mechanics DNA damage deformation" (→ Leclech microtopography nuclear deformation; Lammerding agarose confinement protocol).

### Records ADDED (path + priority + status)
- **D1** `02_PAPERS/2024/irwin_2024_cryptic-hdgfl2-tdp43-fluid-biomarker.md` — **P1, verified (PMC full text inspected)**. PMID 38278991, Nat Med 2024. Cryptic-HDGFL2 fluid biomarker of TDP-43 loss-of-function, presymptomatic ALS-FTD.
- **D1** `02_PAPERS/2025/tittelmeier_2025_celegans-shockwave-blast-mtbi.md` — P2, needs_full_text (bioRxiv preprint). PMID 41509442. Calibrated explosive shock-wave br-mTBI model in C. elegans (Tau/PTL-1).
- **D2** `02_PAPERS/2018/williams_2018_swcnt-optical-nanosensor-implant-ovarian.md` — P2, verified (abstract/metadata). PMID 29675469, Sci Adv 2018. First in vivo implantable SWCNT optical nanosensor (HE4).
- **D2** `02_PAPERS/2021/benbasat_2021_swcnt-dispersion-stability-qc.md` — P3, verified (abstract/metadata). PMID 34685058, Nanomaterials 2021. SWCNT dispersion/stability QC methods (materials scope; indirect biosensor transfer).
- **D3** `02_PAPERS/2025/yang_2025_simo-spatial-multiomics-integration.md` — P2, verified (abstract/metadata; PMC full text not yet inspected). PMID 39893194, Nat Commun 2025. SIMO spatial multi-omics integration.
- **D3** `02_PAPERS/2026/yang_2026_fgot-spatial-interpretable-integration.md` — P2, verified (abstract/metadata). PMID 41643671, Cell Systems 2026. FGOT interpretable sc/spatial integration + regulatory-link inference. (Distinct first-author Yang from SIMO.)
- **D4** `02_PAPERS/2025/leclech_2025_microtopography-nuclear-deformation.md` — P2, verified (abstract/metadata; PMC full text not yet inspected). PMID 39873289, Adv Sci 2025. Topography-driven 3D nuclear deformation + AFM.
- **D4** `02_PAPERS/2023/elpers_2023_agarose-confinement-nuclear-mechanobiology.md` — P2, verified (abstract/metadata). PMID 37459474, Curr Protoc 2023. Lammerding-lab agarose confinement protocol (directly adoptable).

### Candidates SKIPPED (one-line reason)
- PRIME (bioRxiv 42239079, atlas-level sc+ST integration) — strong but preprint; SIMO+FGOT (both published) preferred this pass; hold for next.
- GAMMI (41643?/42108634, Brief Bioinform mosaic integration), SpateCV (41162996 gene imputation) — viable D3 methods but redundant with SIMO/FGOT for this pass; defer.
- Lung ARDS multi-omics (41455968) — biological application, off the methods axis + off-domain tissue.
- Most "blast TBI 2025" hits (LIMBIC-CENC psychological/vestibular/community-reintegration epi: 41263138, 41206627, 41334709; reviews 41379430, 40996480) — clinical/epidemiology or reviews, not mechanistic primaries.
- Ferret UVB+CCI+hypobaria model (40510002, J Neurotrauma) — solid calibrated model but hypobaria/air-travel focus; Tittelmeier chosen as the calibrated-impulse primary. Reconsider next pass if a mammalian shock-tube primary is wanted.
- Kim 2023 (38505424) confined-migration review; "SWCNT for biosensing" Basu 2025 Small review; ACS Nano 4c13076 in-vivo-transducer review — reviews/orient-only.

### Notes / needs_full_text (revisit when access available)
- needs_full_text: tittelmeier_2025 (preprint — extract overpressure/impulse, group sizes).
- Verified-but-abstract-only (promote after full text): williams_2018, benbasat_2021, yang_2025 (SIMO, PMC available), yang_2026 (FGOT), leclech_2025 (PMC available).
- Irwin 2024: extract exact diagnostic-accuracy metrics (AUC/sens/spec) + any data accession from full text/Extended Data.
- **Gaps to target next pass:** D3 cross-cohort harmonization benchmark still thin (PRIME/GAMMI deferred); D2 in-vivo *neuro* nanosensor + corona-phase QC in biofluid (current QC paper is materials-scope); D1 a mammalian calibrated shock-tube primary (have invertebrate + organoid); D4 link confinement protocols to neural/glial injury readouts. The kidney foundation-model slot (li_2025) remains off-domain — consider archiving once a brain/neural foundation-model record is added.

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
