# 01_PROJECTS — One folder per active research project

To start a project, create `01_PROJECTS/<slug>/` (stable human-readable slug, e.g.
`als_spectral_biomarkers`, `blast_tbi_organoid_mechanics`) containing:

- `PROJECT_CONTEXT.md` — copy from `00_AGENT/templates/PROJECT_CONTEXT_TEMPLATE.md` and fill in
  decision context, model system, available samples/data, constraints, and priority literature needs.
- `DECISIONS.md` — dated decision log (decision, evidence, alternatives, risks, revision trigger).
- `OPEN_QUESTIONS.md` — unresolved biological / experimental / analytical / dataset questions.
- `project_syntheses/` — project-scoped synthesis notes.

The agent consults the relevant `PROJECT_CONTEXT.md` before recommending any experiment, dataset, or
analysis, and will not ask you to repeat information already recorded there.
