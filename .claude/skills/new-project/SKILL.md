---
name: new-project
description: >
  Scaffold a new research project inside the LIBRARY so recommendations become project-aware. Use when
  the user starts a new study, analysis, grant, or manuscript and wants the library to track its
  context, decisions, and open questions.
---

# Scaffold a new project

Goal: a `01_PROJECTS/<slug>/` folder the librarian consults before recommending any experiment, dataset,
or analysis. Follows `00_AGENT/LIBRARY_STRUCTURE.md` and the project template.

## Steps
1. Agree a stable, human-readable **slug** (e.g. `als_spectral_biomarkers`,
   `blast_tbi_organoid_mechanics`). Create `01_PROJECTS/<slug>/` and `01_PROJECTS/<slug>/project_syntheses/`.
2. Copy `00_AGENT/templates/PROJECT_CONTEXT_TEMPLATE.md` to `01_PROJECTS/<slug>/PROJECT_CONTEXT.md` and
   fill in: decision context & deliverable, scientific objective/aims, model & study system, available
   samples/data & known quality problems, methods & compute environment, fixed constraints, decisions
   already made, knowledge gaps, priority literature needs, and planned outputs.
3. Create `DECISIONS.md` (dated log: decision, evidence, alternatives, risks, revision trigger) and
   `OPEN_QUESTIONS.md` (biological / experimental / analytical / dataset gaps).
4. Interview the user only for fields that are genuinely unknown — do not ask for anything already
   recorded. Mark unresolved fields **Unknown** rather than guessing.
5. Set `project_status` and `last_updated`, and report the paths created and the top 2–3 literature
   needs to address next.
