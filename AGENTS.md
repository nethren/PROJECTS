# Control-repository instructions

## Scope

These instructions govern only this personal-project control repository. They
do not govern sibling project repositories. Each software project must be
independently understandable and have its own tailored root `AGENTS.md`.

Codex discovers project instructions from the project root toward the current
working directory; closer instructions override broader ones. See the official
[AGENTS.md documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

## Repository purpose

This repository contains portfolio records, workflow documentation, and
reusable templates. Its directory is named `PROJECTS` rather than `_personal`
by owner decision. Actual projects are siblings under the shared local parent,
not children of this repository.

## Required boundaries

- Preserve the one-project/one-repository boundary.
- Never initialize Git in the common parent directory.
- Do not create nested project repositories under this repository.
- Do not copy project source, generated builds, datasets, or media libraries
  into this repository.
- Do not publish, create a remote, push, or change repository visibility without
  the owner's explicit decision.
- Do not move, rename, overwrite, or delete an existing folder without
  confirming the exact source and destination paths.
- Do not store secrets, access tokens, private keys, `.env` files, database
  dumps, or sensitive personal content in records or templates.
- Treat cloud URLs as references, not proof that synchronization is current.
- Keep detailed implementation plans in the actual project repository.

## Record and pipeline rules

- Pipeline stages are `inbox`, `backlog`, `active`, and `archive`.
- Move the Markdown record between stages; do not move the actual project.
- Use one stable kebab-case slug and exactly one canonical record per project.
- Use `local_path: local-only` in tracked records and store the matching
  machine-specific path in ignored `.local/project-paths.json`.
- Use `null`, `not created`, or `not used` for unknown or absent remote/cloud
  locations; never invent links.
- Update the relevant pipeline record and `PROJECTS.md` together.
- Keep at most three projects active unless the owner records an override.
- Delete an idea only when the owner explicitly requests deletion; otherwise
  archive it with a reason.

## Before editing

1. Inspect existing files and Git status.
2. Preserve existing content and unrelated changes.
3. Check that the intended slug, record location, and local path are unique.
4. Pause for owner input whenever a decision changes external state, privacy,
   credentials, an existing folder, or repository boundaries.

## Validation

After changing portfolio state:

- verify each registered project has exactly one pipeline record;
- verify the record directory, front-matter status, and `PROJECTS.md` agree;
- verify slugs and local paths are unique;
- verify relative Markdown links resolve;
- inspect for accidental nested `.git` directories and secrets;
- report Git status and any validation exception.
