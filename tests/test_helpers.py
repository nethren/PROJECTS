from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
import textwrap
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
NEW_IDEA = REPOSITORY_ROOT / "scripts" / "new-idea"
CHECK_WORKSPACE = REPOSITORY_ROOT / "scripts" / "check-workspace"
IDEA_TEMPLATE = REPOSITORY_ROOT / "templates" / "idea.md"


class WorkspaceFixture(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        for directory in (".git", "inbox", "backlog", "active", "archive", "templates"):
            (self.root / directory).mkdir()
        (self.root / ".local").mkdir()
        (self.root / ".local" / "project-paths.json").write_text(
            json.dumps({"workspace_root": str(self.root), "projects": {}}),
            encoding="utf-8",
        )
        shutil.copy2(IDEA_TEMPLATE, self.root / "templates" / "idea.md")
        (self.root / "PROJECTS.md").write_text(
            "# Personal Projects Portfolio\n", encoding="utf-8"
        )

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def run_new_idea(self, *arguments: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [str(NEW_IDEA), "--root", str(self.root), *arguments],
            check=False,
            capture_output=True,
            text=True,
        )

    def run_check(self) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [str(CHECK_WORKSPACE), "--root", str(self.root)],
            check=False,
            capture_output=True,
            text=True,
        )

    def write_record(
        self,
        stage: str,
        slug: str,
        *,
        local_path: str | None = None,
        status: str | None = None,
    ) -> Path:
        record = self.root / stage / f"{slug}.md"
        record.write_text(
            textwrap.dedent(
                f"""\
                ---
                name: "{slug.replace('-', ' ').title()}"
                slug: "{slug}"
                type: "software"
                status: "{status or stage}"
                visibility: "private"
                local_path: "local-only"
                remote_url: null
                cloud_workspace: null
                created: 2026-09-01
                updated: 2026-09-01
                ---

                # {slug.replace('-', ' ').title()}

                ## Outcome

                A useful outcome.

                ## Why now

                It is timely.

                ## Current state

                Planning.

                ## Next action

                Write the first executable acceptance test.
                """
            ),
            encoding="utf-8",
        )
        with (self.root / "PROJECTS.md").open("a", encoding="utf-8") as index:
            index.write(f"\n[{slug}]({stage}/{slug}.md)\n")
        mapping_file = self.root / ".local" / "project-paths.json"
        mapping = json.loads(mapping_file.read_text(encoding="utf-8"))
        mapping["projects"][slug] = local_path or f"/tmp/{slug}"
        mapping_file.write_text(json.dumps(mapping), encoding="utf-8")
        return record


class NewIdeaTests(WorkspaceFixture):
    def test_creates_dated_idea_and_refuses_overwrite(self) -> None:
        first = self.run_new_idea("quiet-reader")
        self.assertEqual(first.returncode, 0, first.stderr)
        content = (self.root / "inbox" / "quiet-reader.md").read_text(encoding="utf-8")
        self.assertIn("# quiet reader", content)
        self.assertRegex(content, r"\*\*Captured:\*\* \d{4}-\d{2}-\d{2}")

        second = self.run_new_idea("quiet-reader")
        self.assertNotEqual(second.returncode, 0)
        self.assertIn("already exists", second.stderr)

    def test_rejects_invalid_slug(self) -> None:
        result = self.run_new_idea("Not Valid")
        self.assertEqual(result.returncode, 2)
        self.assertIn("invalid slug", result.stderr)


class CheckWorkspaceTests(WorkspaceFixture):
    def test_accepts_valid_workspace(self) -> None:
        self.write_record("active", "quiet-reader")
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("1 record(s), no errors", result.stdout)

    def test_reports_duplicate_paths(self) -> None:
        shared = "/tmp/shared-project"
        self.write_record("backlog", "first-project", local_path=shared)
        self.write_record("active", "second-project", local_path=shared)
        result = self.run_check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("duplicate local path", result.stderr)

    def test_rejects_tracked_absolute_path(self) -> None:
        record = self.write_record("backlog", "quiet-reader")
        content = record.read_text(encoding="utf-8").replace(
            'local_path: "local-only"', 'local_path: "/tmp/quiet-reader"'
        )
        record.write_text(content, encoding="utf-8")

        result = self.run_check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("put absolute paths in .local/project-paths.json", result.stderr)

    def test_reports_missing_local_mapping(self) -> None:
        self.write_record("active", "quiet-reader")
        mapping_file = self.root / ".local" / "project-paths.json"
        mapping_file.write_text(
            json.dumps({"workspace_root": str(self.root), "projects": {}}),
            encoding="utf-8",
        )

        result = self.run_check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("local-only path missing", result.stderr)

    def test_reports_status_mismatch_broken_link_and_nested_git(self) -> None:
        record = self.write_record("active", "quiet-reader", status="backlog")
        with record.open("a", encoding="utf-8") as handle:
            handle.write("\n[Missing](missing.md)\n")
        (self.root / "active" / "nested" / ".git").mkdir(parents=True)

        result = self.run_check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("does not match directory", result.stderr)
        self.assertIn("broken relative link", result.stderr)
        self.assertIn("nested Git boundary", result.stderr)


if __name__ == "__main__":
    unittest.main()
