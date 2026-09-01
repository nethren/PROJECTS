# Portfolio Workflow

This repository tracks project status. Actual projects are sibling folders under
the shared local parent and are opened independently.

Machine-specific paths are private local state. Copy
`templates/local-paths.example.json` to `.local/project-paths.json`, keep tracked
record metadata set to `local_path: local-only`, and add the corresponding slug
and absolute path to the ignored mapping.

## Capture an idea

1. Choose a stable kebab-case slug.
2. Run `scripts/new-idea <slug>`, or copy `templates/idea.md` to
   `inbox/<slug>.md` manually. The helper refuses to overwrite an existing file.
3. Fill in the title, capture date, problem or opportunity, intended user, rough
   outcome, source when useful, and open questions.
4. Do not select a stack or create a repository merely to capture an idea.

## Promote an idea to backlog

1. Clarify the problem, beneficiary, rough outcome, and reason to pursue it.
2. Reject or archive ideas that are not worth pursuing; delete only on explicit
   owner request.
3. Create `backlog/<slug>.md` from `templates/project-record.md`.
4. Set `status: backlog`, retain the capture date as `created`, and use `null`,
   `not created`, or `not used` for locations that do not exist.
5. Remove the inbox record only after confirming the backlog record preserved
   its useful context.
6. Add the project to `PROJECTS.md` with a relative link to its record.

## Present a project in the portfolio

1. Write for a viewer who may know nothing about the project: lead with the
   outcome, intended user, and evidence of progress.
2. Keep `PROJECTS.md` concise. Link the project name to its pipeline record and
   link the remote/cloud column to the canonical public or access-controlled
   destination.
3. Describe factual status and a concrete next action; do not inflate unfinished
   work or duplicate the project's README.
4. Before publication, remove or withhold sensitive project names,
   descriptions, absolute paths, and private cloud links as required by the
   chosen repository visibility.

## Hand off ideation to VS Code

1. Finish project qualification here: confirm the outcome, first milestone,
   next action, sensitivity, visibility, and sibling slug.
2. Bootstrap the independent sibling repository with its own customized
   `README.md` and root `AGENTS.md`.
3. Open that sibling folder—not the common parent and not this control repo—as
   the VS Code workspace. This keeps Git status, searches, terminal commands,
   and agent context inside one project boundary.
4. Use the Codex IDE extension or another coding agent beside the source. Open
   files and selections may provide immediate editor context, while the
   repository's own instructions provide durable project context.
5. Commit, test, and push according to that project's approved workflow.
6. Return to this repository only when the project status, outcome, location,
   public link, or next action changes.

## Bootstrap a software project

Before changing the filesystem, the owner must decide the final name and slug,
local parent, sensitivity, remote timing and visibility, treatment of existing
files, and—if public—the license. The owner must also authorize local Git
initialization and commits when applicable.

1. Confirm `active/` will remain within the three-project limit.
2. Verify the exact sibling path does not exist; if it does, stop and inspect it.
3. Create the project as `<shared-parent>/<slug>`, never beneath this repository.
4. Copy and customize the software README and `AGENTS.md` templates; do not use
   symbolic links between repositories.
5. Add a stack-appropriate `.gitignore` and safe `.env.example` if needed.
6. Initialize local Git only if approved and the folder is not already a repo.
7. Create the smallest runnable skeleton and run its documented validation.
8. Create an initial commit only if approved. Remote creation is a separate,
   opt-in operation.
9. Move the portfolio record from `backlog/` to `active/`, set `status: active`,
   set `local_path: local-only`, update the ignored local path mapping and next
   action, then update `PROJECTS.md`.
10. Open the sibling project independently for implementation work.

## Register an existing project

1. Inventory the exact folder, Git boundary, status, remotes, ignored and
   untracked files, and potentially large or sensitive content.
2. Decide whether it stays in place or moves. Never move it without approval of
   exact source and destination paths.
3. If moving valuable or unpushed work, verify a backup and close applications
   holding the folder open.
4. Resolve target collisions explicitly; never overwrite or implicitly merge.
5. After an approved move, reopen the project, verify Git status and remotes,
   and run its documented checks.
6. Create exactly one portfolio record and add it to `PROJECTS.md` only after its
   final path is verified.
7. If repositories are nested, stop so the owner can decide whether that
   relationship is intentional.

## Pause or archive a project

1. Update current state and final links.
2. Record disposition as `completed`, `abandoned`, `superseded`, or `paused`,
   along with the date and a short retrospective.
3. Move the record from `active/` to `archive/` and set `status: archive`.
4. Update `PROJECTS.md` in the same change.
5. Do not delete or move the actual project folder unless separately approved.

## Restore an archived project

1. Confirm why the project is being resumed and define a new next action.
2. Verify its local and remote/cloud locations still exist.
3. Confirm the work-in-progress limit.
4. Move its record to `active/`, set `status: active`, update dates, and update
   `PROJECTS.md`.

## Update paths on a new computer

1. Verify the project independently on the new machine.
2. Update the slug's absolute path in ignored `.local/project-paths.json`.
3. Keep the tracked record set to `local_path: local-only`; do not publish the
   machine-specific path in `PROJECTS.md`.
4. Use a separate local mapping per machine. Do not claim paths are portable or
   that a cloud link proves sync.

## Reconcile local and cloud state

1. Inspect local Git status, the configured remote URL, and branch tracking.
2. Confirm the remote belongs to the intended provider account/organization and
   has the approved visibility.
3. Compare committed work with the remote; uncommitted work is neither remotely
   available nor backed up.
4. For non-code projects, verify the canonical cloud location and documented
   export/backup policy without duplicating the content here.
5. Update records only with verified locations and dates.

## End-of-session update

When portfolio-level state changes, update the record's current state, next
action, and `updated` date, then update `PROJECTS.md`. Commit or push only under
the approved workflow for the repository being changed.

Run `scripts/check-workspace` after portfolio changes. Use
`scripts/check-workspace --help` for options.
