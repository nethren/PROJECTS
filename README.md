# Personal Projects Portfolio

This repository is the public-facing index and private working control center
for my personal projects. It highlights what I am building, why each project
matters, its current state, and where the work can be found.

## Portfolio

Browse the curated [`PROJECTS.md`](PROJECTS.md) index for project outcomes,
status, next steps, and links to code or live work. There are no registered
projects yet; new entries will appear there as they are approved for the
portfolio.

Each software project remains independently usable and versioned. Its source,
technical documentation, history, and project-specific instructions live in its
own repository rather than being copied here.

## How this repository works

This repository's directory is named `PROJECTS` rather than `_personal` by
owner decision.

Actual projects do not live inside this repository. Each software project is a
separate sibling folder under the shared local parent, with its own Git
repository, README, instructions, and—when approved—remote repository.

## Five-minute quick start

1. Run `scripts/new-idea <slug>` to create `inbox/<slug>.md` safely, or copy
   [`templates/idea.md`](templates/idea.md) manually.
2. Describe the problem or opportunity and the rough outcome.
3. When the idea is worth considering, create a full record from
   [`templates/project-record.md`](templates/project-record.md) in `backlog/`.
4. Before activating it, decide its outcome, next action, local path, project
   type, visibility, and whether it needs a repository.
5. Move only the Markdown record through `inbox → backlog → active → archive`.
   Never move the actual project merely to change its portfolio status.

## Ideate here, build in VS Code

Use this repository for ideation, prioritization, and portfolio updates. When an
idea becomes active, open only that project's sibling repository as the VS Code
workspace and implement it there with Codex or another coding agent.

The project's own root `README.md` and `AGENTS.md` carry the outcome, setup,
commands, conventions, and safety boundaries into the IDE. When a coding session
changes portfolio-level status, return here to update the canonical record and
`PROJECTS.md`.

See [`docs/workflow.md`](docs/workflow.md) for the complete workflow and
[`PROJECTS.md`](PROJECTS.md) for the portfolio index.

Validate the portfolio at any time with:

```sh
scripts/check-workspace
```

## Working rules

- Keep no more than three active personal projects unless an override is
  deliberately recorded.
- Treat the pipeline record as the canonical portfolio status and update it
  together with `PROJECTS.md`.
- Store implementation details in the actual project repository.
- Never store project source, secrets, credentials, `.env` files, personal
  documents, database dumps, or large binary assets here.
- Do not create remotes, publish repositories, change visibility, move existing
  folders, or initialize an existing project without owner approval.
- Machine-specific project paths live only in ignored
  `.local/project-paths.json`; tracked records use `local-only` instead of an
  absolute path.
- Before publishing changes, review records for private names, sensitive
  descriptions, and access-controlled cloud links.

## Helper scripts

- `scripts/new-idea <slug>` creates a dated inbox record and refuses invalid or
  existing slugs.
- `scripts/check-workspace` checks records, links, paths, project-index coverage,
  and Git boundaries without changing files.

Both commands provide `--help`. Their test suite uses only Python's standard
library:

```sh
python3 -m unittest discover -s tests -v
```

## Templates

- [`idea.md`](templates/idea.md) — capture a raw idea
- [`project-record.md`](templates/project-record.md) — track portfolio status
- [`software-README.md`](templates/software-README.md) — start project docs
- [`software-AGENTS.md`](templates/software-AGENTS.md) — start project guidance
- [`non-code-project.md`](templates/non-code-project.md) — plan non-code work
- [`local-paths.example.json`](templates/local-paths.example.json) — local-only
  machine path mapping

Portfolio-wide decisions are recorded in
[`docs/decisions.md`](docs/decisions.md).

Released under the [MIT License](LICENSE).
