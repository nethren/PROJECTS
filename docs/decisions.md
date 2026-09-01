# Portfolio Decisions

Record dated decisions that apply across projects. Project-specific choices
belong in the project repository.

## 2026-09-01 — Control repository location and name

- **Decision:** Use the current Git root as the control repository and retain its
  existing `PROJECTS` directory name instead of `_personal`.
- **Consequence:** Actual project folders must be siblings under the control
  repository's parent; they must never be created inside this repository.

## 2026-09-01 — Existing neighboring folders

- **Decision:** Do not register or modify the neighboring `Fitness` and
  `Fragrance` folders during this setup.

## 2026-09-01 — Initial control-repository remote preference (superseded)

- **Decision:** Prefer a private Git remote later. Keep the repository local-only
  until the owner chooses the Git provider and account and explicitly approves
  remote creation or connection.
- **Reason:** Portfolio records can expose private project names, local paths,
  interests, and cloud links.
- **Superseded by:** The public-repository/private-local-paths decision below.

## 2026-09-01 — Work-in-progress limit

- **Decision:** Allow at most three active personal projects unless an explicit
  override and reason are recorded.

## 2026-09-01 — Portfolio-first presentation

- **Decision:** Make the repository landing page and `PROJECTS.md` a curated
  portfolio for Git viewers, while retaining the internal pipeline and control
  workflow.
- **Consequence:** Project summaries lead with outcomes and verified links. A
  privacy review is mandatory before any remote is made public because canonical
  records may contain absolute local paths or private links.

## 2026-09-01 — Public repository and private local paths

- **Decision:** Publish the control repository as a public GitHub portfolio
  under the `nethren` account with the repository name `PROJECTS` and the MIT
  license.
- **Result:** Created [nethren/PROJECTS](https://github.com/nethren/PROJECTS)
  with public visibility and `main` as its default branch.
- **Decision:** Tracked records use `local_path: local-only`. Absolute paths live
  in ignored `.local/project-paths.json`, keyed by project slug.
- **Reason:** Git viewers should see project outcomes and source links without
  learning machine-specific filesystem details.

## 2026-09-01 — Ideation and implementation tools

- **Decision:** Use this control repository and Codex desktop primarily for
  ideation and portfolio management. Use VS Code with Codex or another coding
  agent for project implementation.
- **Consequence:** Open each sibling project as its own VS Code workspace. Its
  root `README.md` and `AGENTS.md` must be complete because this control
  repository's instructions do not apply to sibling repositories.

## Decisions still required

- Backup expectations beyond the public GitHub remote.
- Preferred package managers and runtimes, chosen per project unless a genuine
  cross-project default emerges.
