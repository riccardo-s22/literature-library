# Corpus Expansion Log

Chronological record of each corpus-expansion pass. The most recent run's date sets the `date_from`
window for the next monthly pass. Newest entries at the top. Maintained by the `expand-corpus` skill.

---

## 2026-08-01 — Monthly pass #2 (mode: monthly, window: 2026-07-01 → 2026-08-01)
**Window:** 2026-07-01 to 2026-08-01 (publication date filter, PubMed pdat). **Added: 6 records.** Library total: 34 → **40**.
Per-domain (before → after): D1 9→12 (+3), D2 7→8 (+1), D3 9→10 (+1), D4 9→9 (no new standalone D4; Sohn 2026 counted in D1+D4 cross-domain, Fang 2026 also D1+D4).

### Queries per domain
- **D1 Neurodeg/TBI/ALS/AD:** "neurodegeneration ALS TDP-43 tau biomarker CSF plasma 2026" + "Alzheimer staging biomarker plasma PET 2026" (PubMed, date-filtered). Top candidate: Salvadó 2026 (PMID 42189519, JAMA Neurol, 2026-07-01) — two-analyte plasma AD staging (%p-tau217 + eMTBR-tau243); PMC full text inspected. Second: Xia 2026 (PMID 42471754, Alzheimer's Dementia, 2026-07) — TDP-43 PET tracer [18F]JNJ-TDP43-1 (J&J); abstract inspected, PMC13380671 available.
- **D2 SWCNT/biosensors:** "carbon nanotube OR SWCNT OR nanoparticle fluorescence biosensor biomarker detection" (PubMed, date-filtered 2026-07-01 to 2026-08-01) + WebSearch for SWCNT NIR preprints. Selected: Chen 2026 (PMID 42525763, Sci Adv, 2026-07-29) — structurally defined DNA-scCNT sensor array (6 single-chirality species) + ensemble ML for multi-cancer liquid biopsy in serum (n=253); PMC full text inspected. D2 aptamer-CNT review (PMID 42509689) skipped — review. MWCNT polyester composites (PMID 42513879) — off-domain materials science.
- **D3 Transcriptomics/single-cell:** "neurodegeneration OR ALS OR Alzheimer single-cell OR snRNA-seq OR spatial transcriptomics software OR tool OR pipeline OR foundation model" + "differential expression OR splicing OR pseudobulk single-cell brain OR neuron" (PubMed, date-filtered). Large result sets (>10,000 hits); triage by abstract: Zhang 2026 (PMID 42490473, Science, 2026-07-23) — GAGE-seq joint single-cell 3D chromatin + transcriptome in AD postmortem brain + Hicformer deep learning framework; abstract inspected. ST review (PMID 42511496, Int J Mol Sci) — review, skip. Cerebellar connectome (PMID 42458125) — off-domain. TOPMed eQTL/sQTL (PMID 42462027, Science) — blood/lung focus, not brain-specific, skip. ANXA11/TDP-43 review (PMID 42414528, Acta Neuropathol) — review only; skip.
- **D4 Mechanobiology:** "blood-brain barrier OR astrocyte OR neural mechanobiology OR ECM stiffness OR force signaling OR confinement OR TBI blast neural injury" (PubMed, date-filtered). Triage of second metadata batch: Fang 2026 (PMID 42385697, Neuron, 2026-07-01) — TGF-β1/Mfsd2a/caveolin-1 mechanism for age-related BBB transcytosis with AAV + pharmacological interventions; abstract inspected. Sohn 2026 (PMID 42415348, Nucleus, 2026-07-07) — emerin nuclear mechanotransduction in tauopathy neurons (DIA proteomics + iPSC validation); PMC full text inspected (counted as D1+D4 cross-domain). Glia-ECM review (PMID 42505379, Cells) — review, skip. BBB permeability assessment review (PMID 42529882) — review, skip. Nat Immunol astrocyte innate immune (PMID 42373786, June 29) — outside window; skip. Amygdala astrocytes (PMID 41881020, March 2026) — outside window; skip.

### Records ADDED (path + priority + status)
- **D1** `02_PAPERS/2026/salvado_2026_plasma-staging-ad-ptau217-emtbr-tau243.md` — **P1, verified (PMC full text inspected)**. PMID 42189519, DOI 10.1001/jamaneurol.2026.1405, PMCID PMC13213595. JAMA Neurology 2026-07-01. Plasma %p-tau217 + eMTBR-tau243 two-analyte biological staging model for AD; C index 0.91 in BioFINDER-2 (n=872) and Knight ADRC (n=156); AUC 0.96 vs neuropathology (n=80).
- **D1** `02_PAPERS/2026/xia_2026_tdp43-pet-tracer-jnj-als-ftd-late.md` — **P1, partial (abstract inspected)**. PMID 42471754, DOI 10.1002/alz.71675, PMCID PMC13380671. Alzheimer's Dementia 2026-07. First characterized TDP-43 PET tracer [18F]JNJ-TDP43-1; Kd = 7.1 nM; brain uptake + rapid washout in rats + NHP; target engagement in AAV-hTDP43 model.
- **D1+D3** `02_PAPERS/2026/zhang_2026_gage-seq-3d-genome-transcriptome-alzheimer.md` — **P1, partial (abstract inspected)**. PMID 42490473, DOI 10.1126/science.adz1652. Science 2026-07-23. GAGE-seq joint single-cell 3D genome + transcriptome in AD postmortem brain (Rush ADRC); Hicformer deep learning for 3D genome–expression prediction; integration with spatial transcriptomics and chromatin accessibility.
- **D2** `02_PAPERS/2026/chen_2026_dna-scnt-ml-liquid-biopsy-cancer.md` — **P1, verified (PMC full text inspected)**. PMID 42525763, DOI 10.1126/sciadv.aef9530, PMCID PMC13418527. Science Advances 2026-07-29. Structurally defined DNA-scCNT array (6 single-chirality species) + ensemble ML for multi-cancer serum classification; 89% sensitivity / 96% specificity (n=253); early-stage LuC 92%/95%; ATP extraction protocol reusable.
- **D1+D4** `02_PAPERS/2026/sohn_2026_emerin-tau-nuclear-mechanotransduction-neurons.md` — **P2, verified (PMC full text inspected)**. PMID 42415348, DOI 10.1080/19491034.2026.2697135, PMCID PMC13349007. Nucleus 2026-07-07. Emerin elevated in iTau (BE(2)-C tau R406W) and tau mutant iPSC neurons; emerin overexpression → neurotoxicity + ↑F-actin + nuclear invagination; DIA proteomics ~5,300 proteins (Frost lab, Brown/UT Health).
- **D1+D4** `02_PAPERS/2026/fang_2026_tgfb1-transcytosis-bbb-aging-neuron.md` — **P2, partial (abstract inspected)**. PMID 42385697, DOI 10.1016/j.neuron.2026.06.003. Neuron 2026-07-01. TGF-β1/Tgfbr2/Smad2-4/Mfsd2a/caveolin-1 pathway drives age-related BBB leakage via caveolar transcytosis (not tight junction disruption); AAV + conditional KO + pharmacological inhibition validated in aged mice.

### Candidates SKIPPED (one-line reason)
- ANXA11/TDP-43 review (PMID 42414528, Acta Neuropathol) — review; no new primary data.
- TOPMed eQTL/sQTL cross-cohort Science (PMID 42462027) — blood + lung tissue focus, not brain; off-domain.
- Spatial transcriptomics aging brain review (PMID 42511496, Int J Mol Sci) — review.
- Cerebellar connectome (PMID 42458125, Cerebellum) — off-domain (rat tract-tracing, not relevant diseases).
- Glia-ECM CNS review (PMID 42505379, Cells) — review.
- BBB permeability review (PMID 42529882, J Zhejiang Univ Sci B) — review.
- Spliced. (PMID 42457577, Trends Genet) — editorial/commentary, not primary.
- Aptamer-CNT hybrid review (PMID 42509689, Mini Rev Med Chem) — review.
- MWCNT polyester composites (PMID 42513879, Materials Basel) — materials science, off-domain.
- Nat Immunol astrocyte innate immune (PMID 42373786, June 29) — outside window.
- Amygdala astrocyte encoding (PMID 41881020, March 2026) — outside window.

### Notes / needs_full_text (revisit when access available)
- needs_full_text: xia_2026 — PMC13380671 available; retrieve to confirm full pharmacokinetic parameters, selectivity panel, and autoradiography in human tissue.
- needs_full_text: zhang_2026 — Science paywalled; no PMC found; obtain via institutional access to confirm sample sizes, GAGE-seq protocol details, and Hicformer code availability.
- needs_full_text: fang_2026 — Neuron paywalled; no PMC found; obtain to confirm mouse strain/age, exact sample sizes, pharmacological inhibitor identity, and behavioral endpoint details.
- chen_2026: supplement not inspected; confirm per-group sample sizes, exact external validation split, and ML hyperparameters.
- sohn_2026: supplement not inspected; confirm emerin fold change, proteomic data accession (PRIDE/MassIVE), and iPSC neuron genotype.

### Gaps to target next pass (2026-08-01 → next monthly)
- **D1:** Mammalian calibrated blast/shock-tube TBI primary still absent; C. elegans model only. Monitor first-in-human [18F]JNJ-TDP43-1 PET study announcements. Plasma tau368 validation (Kac 2026 next steps). Human AD postmortem emerin data.
- **D2:** D2 gap narrowed with Chen 2026 (DNA-scCNT multi-cancer serum); however neurodegeneration biofluid SWCNT sensing still absent. Monitor ACS Nano, Biosensors Bioelectronics, Nanoscale for NIR SWCNT + biofluid + neuro-related analytes.
- **D3:** GAGE-seq and Hicformer code/data release (Zhang 2026); PRIME atlas-level sc+ST integration (bioRxiv, deferred from deepen pass #3); cross-cohort harmonization benchmarks for brain data.
- **D4:** Cauzzi 2026 (PNN/ECM/PV-IN/DA-loss, Neurobiol Dis) — identified as candidate in D4 searches but exact PMID/date not confirmed in window; verify in next pass. Confinement/migration assay linked to neural/glial injury readouts still absent.

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
