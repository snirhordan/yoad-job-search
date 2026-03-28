"""Tests for Issue #2: Data infrastructure — preferences, history, and posting storage."""
import os
import pathlib

DATA_DIR = pathlib.Path.home() / ".yoad-jobs"
PROJECT_DIR = pathlib.Path.home() / "yoad"


class TestDataDirectoryStructure:
    """Verify ~/.yoad-jobs/ directory structure exists with required subdirs."""

    def test_data_dir_exists(self):
        assert DATA_DIR.is_dir(), f"{DATA_DIR} should exist"

    def test_resume_subdir_exists(self):
        assert (DATA_DIR / "resume").is_dir()

    def test_jobs_subdir_exists(self):
        assert (DATA_DIR / "jobs").is_dir()


class TestPreferencesFile:
    """Verify preferences.md contains all required sections for Yoad's profile."""

    def setup_method(self):
        self.prefs_path = DATA_DIR / "preferences.md"
        assert self.prefs_path.exists(), "preferences.md must exist"
        self.content = self.prefs_path.read_text()

    def test_target_roles_section(self):
        assert "## Target Roles" in self.content

    def test_contains_junior_developer(self):
        lower = self.content.lower()
        assert "junior" in lower and "developer" in lower

    def test_experience_level_section(self):
        assert "## Experience Level" in self.content

    def test_experience_0_to_2_years(self):
        assert "0-2" in self.content or "entry" in self.content.lower()

    def test_tech_stack_section(self):
        assert "## Tech Stack" in self.content

    def test_any_language(self):
        lower = self.content.lower()
        assert "any" in lower or "all" in lower, "Should indicate openness to any tech stack"

    def test_location_preferences_section(self):
        assert "## Location" in self.content

    def test_israel_in_locations(self):
        assert "Israel" in self.content

    def test_remote_in_locations(self):
        lower = self.content.lower()
        assert "remote" in lower

    def test_must_haves_section(self):
        assert "## Must-Have" in self.content

    def test_nice_to_haves_section(self):
        assert "## Nice-to-Have" in self.content

    def test_dealbreakers_section(self):
        assert "## Dealbreaker" in self.content

    def test_dealbreaker_5plus_years(self):
        assert "5+" in self.content, "Should exclude 5+ years experience roles"

    def test_dealbreaker_unpaid(self):
        lower = self.content.lower()
        assert "unpaid" in lower

    def test_dealbreaker_commission_only(self):
        lower = self.content.lower()
        assert "commission" in lower


class TestJobHistoryFile:
    """Verify job-history.md exists with correct template."""

    def test_history_file_exists(self):
        assert (DATA_DIR / "job-history.md").exists()

    def test_history_has_header(self):
        content = (DATA_DIR / "job-history.md").read_text()
        assert "Job Search History" in content or "job-history" in content.lower()


class TestCVInProject:
    """Verify Yoad's CV is accessible in the project."""

    def test_cv_exists(self):
        cv = PROJECT_DIR / "Yoad Hordan - CV.pdf"
        assert cv.exists(), "Yoad's CV should be in project root"
